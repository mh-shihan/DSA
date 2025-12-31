# Script to automatically update README.md statistics
# Run this script whenever you add new files to update the statistics

# Get counts
$totalFiles = (Get-ChildItem -Path "c:\DSA" -Recurse -Include "*.cpp", "*.js" -File).Count
$cppFiles = (Get-ChildItem -Path "c:\DSA" -Recurse -Include "*.cpp" -File).Count
$jsFiles = (Get-ChildItem -Path "c:\DSA" -Recurse -Include "*.js" -File).Count

$phase1Files = (Get-ChildItem -Path "c:\DSA\Phase-1" -Recurse -Include "*.cpp", "*.js" -File -ErrorAction SilentlyContinue).Count
$phase2Files = (Get-ChildItem -Path "c:\DSA\Phase-2" -Recurse -Include "*.cpp", "*.js" -File -ErrorAction SilentlyContinue).Count
$leetcodeFiles = (Get-ChildItem -Path "c:\DSA\leetCode" -Recurse -Include "*.cpp", "*.js" -File -ErrorAction SilentlyContinue).Count
$code360Files = (Get-ChildItem -Path "c:\DSA\Code360" -Recurse -Include "*.cpp", "*.js" -File -ErrorAction SilentlyContinue).Count
$experimentsFiles = (Get-ChildItem -Path "c:\DSA\Experiments" -Recurse -Include "*.cpp", "*.js" -File -ErrorAction SilentlyContinue).Count

# Handle null counts
if ($null -eq $phase1Files) { $phase1Files = 0 }
if ($null -eq $phase2Files) { $phase2Files = 0 }
if ($null -eq $leetcodeFiles) { $leetcodeFiles = 0 }
if ($null -eq $code360Files) { $code360Files = 0 }
if ($null -eq $experimentsFiles) { $experimentsFiles = 0 }

# Read the current README
$readmePath = "c:\DSA\README.md"
$readmeContent = Get-Content -Path $readmePath -Raw

# Find and replace the statistics section
$newStatisticsSection = @"
## 📊 Repository Statistics

| Metric | Count |
|--------|-------|
| **Total Problems Solved** | $totalFiles |
| **C++ Problem Files** | $cppFiles |
| **JavaScript Problem Files** | $jsFiles |
| **Phase-1 Files** | $phase1Files |
| **Phase-2 Files** | $phase2Files |
| **LeetCode Files** | $leetcodeFiles |
| **Code360 Files** | $code360Files |
| **Experiments Files** | $experimentsFiles |

### Problem Categories

- 📊 **Array Problems** - Search, sort, and manipulation
- 🔍 **Binary Search** - Multiple search implementations
- 🔄 **Sorting Algorithms** - Bubble, Selection, Insertion, Heap Sort
- 🔗 **Linked List** - Insertion, deletion, traversal operations
- 🎯 **Bit Manipulation** - Power of 2, set bits, complement operations
- 📐 **Math Problems** - Number operations and conversions
- 🎨 **Pattern Programs** - Character and number patterns
- 🏗️ **Data Structures** - 2D Arrays, Stacks, Queues, OOP
- 💻 **Platform Problems** - LeetCode and Code360 solutions

---
"@

# Replace using regex pattern to find the statistics section
$readmeContent = $readmeContent -replace '(?s)(## Overview.*?---\s*)(## 📊 Repository Statistics.*?---\s*)', "`$1$newStatisticsSection"

# Write updated content back
Set-Content -Path $readmePath -Value $readmeContent -Encoding UTF8

Write-Host "✅ README.md statistics updated successfully!"
Write-Host ""
Write-Host "Current Statistics:"
Write-Host "- Total Files: $totalFiles"
Write-Host "- C++ Files: $cppFiles"
Write-Host "- JavaScript Files: $jsFiles"
Write-Host "- Phase-1: $phase1Files"
Write-Host "- Phase-2: $phase2Files"
Write-Host "- LeetCode: $leetcodeFiles"
Write-Host "- Code360: $code360Files"
Write-Host "- Experiments: $experimentsFiles"

