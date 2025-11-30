#!/usr/bin/env python3
"""
Monitor indexing progress and report status.
"""
import os
import sys
import time
import subprocess
import chromadb
from chromadb.config import Settings as ChromaSettings

def get_process_info(pid):
    """Get process information."""
    try:
        result = subprocess.run(
            ['ps', '-p', str(pid), '-o', 'pid,pcpu,pmem,etime,command'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0 and len(result.stdout.strip().split('\n')) > 1:
            return result.stdout.strip()
        return None
    except:
        return None

def get_chunk_count():
    """Get current chunk count from ChromaDB."""
    db_path = "./chroma_db"
    collection_name = "mindos_rag"
    
    if not os.path.exists(db_path):
        return 0
    
    try:
        client = chromadb.PersistentClient(
            path=db_path,
            settings=ChromaSettings(anonymized_telemetry=False)
        )
        collection = client.get_collection(name=collection_name)
        return collection.count()
    except:
        return 0

def monitor_indexing():
    """Monitor indexing progress."""
    # Find the indexing process
    result = subprocess.run(
        ['ps', 'aux'],
        capture_output=True,
        text=True
    )
    
    pid = None
    for line in result.stdout.split('\n'):
        if 'python' in line and 'cli.py index' in line and 'grep' not in line:
            parts = line.split()
            if len(parts) > 1:
                try:
                    pid = int(parts[1])
                    break
                except:
                    pass
    
    if not pid:
        print("❌ Indexing process not found")
        return
    
    print(f"📊 Monitoring indexing process (PID: {pid})")
    print("=" * 60)
    
    start_time = time.time()
    last_count = 0
    check_interval = 30  # Check every 30 seconds
    total_chunks = 3486  # Expected total
    
    while True:
        # Check if process is still running
        proc_info = get_process_info(pid)
        if not proc_info:
            print("\n⚠️  Process no longer running")
            final_count = get_chunk_count()
            print(f"📊 Final count: {final_count}/{total_chunks} chunks indexed")
            if final_count == total_chunks:
                print("✅ Indexing completed successfully!")
            else:
                print("❌ Indexing may have failed or was interrupted")
            break
        
        # Get current progress
        current_count = get_chunk_count()
        elapsed = time.time() - start_time
        elapsed_min = elapsed / 60
        
        # Calculate progress
        if current_count > 0:
            progress = (current_count / total_chunks) * 100
            rate = current_count / elapsed if elapsed > 0 else 0
            remaining = total_chunks - current_count
            eta_min = (remaining / rate) if rate > 0 else 0
        else:
            progress = 0
            rate = 0
            eta_min = 0
        
        # Calculate chunks added since last check
        chunks_added = current_count - last_count
        rate_since_last = chunks_added / (check_interval / 60) if check_interval > 0 else 0
        
        # Display status
        print(f"\n⏱️  Time elapsed: {elapsed_min:.1f} minutes")
        print(f"📈 Progress: {current_count}/{total_chunks} chunks ({progress:.1f}%)")
        
        if chunks_added > 0:
            print(f"⚡ Rate: {rate_since_last:.1f} chunks/minute (since last check)")
            if rate > 0:
                print(f"📊 Average rate: {rate:.1f} chunks/minute")
                print(f"⏳ Estimated time remaining: {eta_min:.1f} minutes")
        else:
            print("⏸️  No new chunks added since last check (may be in conversion/parsing phase)")
        
        # Show process info
        if proc_info:
            lines = proc_info.split('\n')
            if len(lines) > 1:
                parts = lines[1].split()
                if len(parts) >= 3:
                    cpu = parts[1]
                    mem = parts[2]
                    print(f"💻 Process: {cpu}% CPU, {mem}% MEM")
        
        print("-" * 60)
        
        # Check if complete
        if current_count >= total_chunks:
            print("\n🎉 Indexing completed!")
            break
        
        last_count = current_count
        time.sleep(check_interval)

if __name__ == "__main__":
    try:
        monitor_indexing()
    except KeyboardInterrupt:
        print("\n\n⏹️  Monitoring stopped by user")

