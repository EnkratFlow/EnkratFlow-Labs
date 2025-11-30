#!/bin/bash

# Script to check git status for all repositories
# Usage: ./check-git-status.sh

WORKSPACE="/Users/guyrobo/MindOS/MindOS-Labs"

echo "=========================================="
echo "Git Repository Status Check"
echo "=========================================="
echo ""

# Function to check a repository
check_repo() {
    local repo_path=$1
    local repo_name=$2
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📁 Checking: $repo_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if [ ! -d "$repo_path/.git" ]; then
        echo "❌ Not a git repository (no .git directory found)"
        echo ""
        return
    fi
    
    cd "$repo_path" || return
    
    # Get current branch
    current_branch=$(git branch --show-current 2>/dev/null || echo "unknown")
    echo "📍 Current branch: $current_branch"
    
    # Check for uncommitted changes
    echo ""
    echo "📝 Uncommitted changes:"
    if git diff --quiet && git diff --cached --quiet; then
        echo "   ✅ Working directory is clean"
    else
        echo "   ⚠️  You have uncommitted changes:"
        git status --short
    fi
    
    # Fetch latest from remote
    echo ""
    echo "🔄 Fetching latest from remote..."
    git fetch origin 2>&1 | grep -v "^From" | grep -v "^$" || echo "   ✅ Fetch completed"
    
    # Check if remote exists
    if git remote get-url origin &>/dev/null; then
        remote_url=$(git remote get-url origin)
        echo "   🔗 Remote: $remote_url"
    else
        echo "   ⚠️  No remote 'origin' configured"
        echo ""
        return
    fi
    
    # Check if branch exists on remote
    if git ls-remote --heads origin "$current_branch" &>/dev/null; then
        # Compare local vs remote
        echo ""
        echo "📊 Comparison with origin/$current_branch:"
        
        local_commits=$(git log origin/$current_branch..HEAD --oneline 2>/dev/null | wc -l | tr -d ' ')
        remote_commits=$(git log HEAD..origin/$current_branch --oneline 2>/dev/null | wc -l | tr -d ' ')
        
        if [ "$local_commits" -gt 0 ]; then
            echo "   ⬆️  Local is ahead by $local_commits commit(s):"
            git log origin/$current_branch..HEAD --oneline | head -5 | sed 's/^/      /'
            if [ "$local_commits" -gt 5 ]; then
                echo "      ... and $((local_commits - 5)) more"
            fi
        fi
        
        if [ "$remote_commits" -gt 0 ]; then
            echo "   ⬇️  Remote is ahead by $remote_commits commit(s):"
            git log HEAD..origin/$current_branch --oneline | head -5 | sed 's/^/      /'
            if [ "$remote_commits" -gt 5 ]; then
                echo "      ... and $((remote_commits - 5)) more"
            fi
        fi
        
        if [ "$local_commits" -eq 0 ] && [ "$remote_commits" -eq 0 ]; then
            echo "   ✅ Local and remote are in sync"
        fi
    else
        echo "   ⚠️  Branch '$current_branch' does not exist on remote"
    fi
    
    # Check for untracked files
    echo ""
    echo "📄 Untracked files:"
    untracked=$(git ls-files --others --exclude-standard | wc -l | tr -d ' ')
    if [ "$untracked" -gt 0 ]; then
        echo "   ⚠️  $untracked untracked file(s) found"
        git ls-files --others --exclude-standard | head -10 | sed 's/^/      /'
        if [ "$untracked" -gt 10 ]; then
            echo "      ... and $((untracked - 10)) more"
        fi
    else
        echo "   ✅ No untracked files"
    fi
    
    echo ""
    cd - > /dev/null
}

# Check snarktank repository
check_repo "$WORKSPACE/snarktank" "snarktank"

# Check tv_strategies repository
check_repo "$WORKSPACE/tv_strategies" "tv_strategies"

echo "=========================================="
echo "✅ Status check complete!"
echo "=========================================="


