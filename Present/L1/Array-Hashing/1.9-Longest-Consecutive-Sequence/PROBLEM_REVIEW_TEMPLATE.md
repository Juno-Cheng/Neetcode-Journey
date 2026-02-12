# Problem Review Template

Use this template for each problem you solve to internalize the thinking process.

---

## Problem: [Problem Name]

### 📋 Problem Statement
[Copy problem description]

### 🎯 Constraints & Requirements
- Time: O(?)
- Space: O(?)
- Special requirements

---

## 💭 My Thinking Process

### Step 1: Naive Solution
**What I tried first:**
```
[Describe your initial approach]
```

**Why it's slow:**
- [ ] Nested loops → O(n²)
- [ ] Repeated calculations
- [ ] Not using optimal data structure
- [ ] Other: _______________

**Time/Space:** O(?) / O(?)

---

### Step 2: Identifying the Bottleneck
**What's the slow part?**
```
[What specific operation is slow?]
```

**What redundant work am I doing?**
```
[What am I calculating/checking multiple times?]
```

**Example:**
- Checking every element when I only need to check sequence starts
- Recalculating values that could be stored
- etc.

---

### Step 3: The Key Insight
**What's the "aha!" moment?**
```
[The realization that leads to optimization]
```

**Why does this work?**
```
[Explain the logic]
```

**Example for Longest Consecutive:**
- Insight: Only need to expand sequences from their start
- Why: If we expand from every element, we do redundant work
- Solution: Check if `num - 1` exists - if not, it's a start!

---

### Step 4: Optimal Solution
**Pattern Used:** [Pattern name, e.g., "Sequence Start Optimization"]

**Key Code:**
```python
# The critical part that makes it optimal
if condition:  # This filter is key!
    # Process
```

**Why this is optimal:**
- [Explain time/space complexity]
- [Why it's better than naive]

---

## 📊 Complexity Analysis

**Time:** O(?) 
**Why:** [Explanation]

**Space:** O(?)
**Why:** [Explanation]

**Is this optimal?** Yes/No
**Why:** [Explanation]

---

## 🔗 Pattern Recognition

**Pattern Category:** [e.g., Hash Set, Two Pointers, etc.]

**When to use this pattern:**
- [Characteristics of problems that use this]
- [Constraints that suggest it]

**Similar problems:**
1. [Problem name] - [Why it's similar]
2. [Problem name] - [Why it's similar]

---

## 🎓 What I Learned

**Key Takeaway:**
```
[One sentence summary of the main lesson]
```

**Common Mistake to Avoid:**
```
[What not to do]
```

**How to Remember:**
```
[Mnemonic or mental model]
```

---

## 🔄 Review Schedule

- [ ] Day 1: Learned solution
- [ ] Day 2: Re-solved from memory
- [ ] Day 4: Re-solved again
- [ ] Day 7: Found similar problem
- [ ] Day 14: Quick review
- [ ] Day 30: Full re-solve

---

## 📝 Notes

[Any additional thoughts, variations, edge cases, etc.]

---

## ✅ Self-Assessment

**Can I explain it to someone else?** Yes/No
**Can I solve it from memory?** Yes/No
**Can I apply the pattern to similar problems?** Yes/No

**If No, what do I need to review?**
```
[What to focus on]
```
