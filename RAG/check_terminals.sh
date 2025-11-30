#!/bin/bash
# Script to check what's running in your RAG system

echo "=== RAG System Process Check ==="
echo ""

echo "📊 Python processes related to RAG:"
ps aux | grep -E "python.*cli.py|python.*index|python.*chat|python.*query|python.*check_progress" | grep -v grep || echo "  No RAG processes running"
echo ""

echo "💾 Current indexing progress:"
cd /Users/guyrobo/MindOS/MindOS-Labs/RAG
source venv/bin/activate 2>/dev/null
python check_progress.py 2>/dev/null || echo "  Could not check progress"
echo ""

echo "🔍 Stuck processes (running > 30 minutes):"
ps aux | awk '$10 > 30 && /python.*cli.py/ && !/grep/ {print "  PID: "$2" | Runtime: "$10" | Command: "$11" "$12" "$13" "$14}'
echo ""

echo "📝 Active log files:"
ls -lh /Users/guyrobo/MindOS/MindOS-Labs/RAG/indexing_output.log 2>/dev/null && echo "  indexing_output.log exists" || echo "  No indexing log file"
echo ""

echo "✅ What you need:"
echo "  - One terminal for running queries: python src/cli.py query 'your question'"
echo "  - One terminal for chat: python src/cli.py chat"
echo "  - Indexing can run in background (or you can test with current 1707 chunks)"
echo ""

echo "🧹 To clean up stuck processes, run:"
echo "  pkill -9 -f 'python.*cli.py index'"

