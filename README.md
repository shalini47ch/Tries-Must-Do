#  Tries-Must-Do

A curated collection of **Trie problems** organized by the patterns they follow.

The goal is to first understand the **Normal Trie Template** and then recognize how each problem modifies or extends that template.

---

##  Trie Pattern Roadmap

| Pattern                                    | Problems              | What Changes from the Base Template |
| ------------------------------------------ | --------------------- | ----------------------------------- |
| **Pattern 1 — Normal Trie**                | Implement Trie        | Base Trie pattern                   |
| **Pattern 2 — Trie + DFS**                 | Add & Search Words    | `search()` → DFS for `.`            |
| **Pattern 3 — Prefix + DFS**               | Search Suggestions    | Prefix traversal + DFS collection   |
| **Pattern 4 — Trie + DFS**                 | Longest Word          | DFS + `isEnd()` checking            |
| **Pattern 5 — Prefix Matching**            | Replace Words         | Stop immediately when `isEnd()`     |
| **Pattern 6 — Component Trie**             | Remove Sub-Folders    | Trie using folder components        |
| **Pattern 7 — Trie of Characters**         | Longest Common Prefix | Trie-based prefix matching          |
| **Pattern 8 — Trie + DFS**                 | Words Within 2 Edits  | DFS + mismatch count                |
| **Pattern 9 — Binary Trie**                | Maximum XOR           | `links=[None, None]`                |
| **Pattern 10 — Trie + Matrix DFS**         | Word Search II        | Trie + board DFS + store word       |
| **Pattern 11 — Reverse Trie**              | Stream of Characters  | Insert words in reverse             |
| **Pattern 12 — Trie + DP**                 | Concatenated Words    | Trie + DP                           |
| **Pattern 13 — Trie + Backtracking**       | Word Squares          | Trie + backtracking                 |
| **Pattern 14 — Reverse Trie + Palindrome** | Palindrome Pairs      | Reverse Trie + palindrome checking  |

---

# 1️⃣ Normal Trie Template

The **Normal Trie** is the base pattern.

Most Trie problems start with these four basic operations:

* `containsKey()` → check whether a character exists
* `put()` → create a new Trie node
* `get()` → move to the next node
* `isEnd()` / `setEnd()` → identify complete words

### Base Template

```python
# first create a node and then perform the functions accordingly

class Node:
    def __init__(self):
        self.links=[None for i in range(26)]
        self.flag=False
    
    def containsKey(self,ch):
        return self.links[ord(ch)-ord("a")]!=None 
    
    def put(self,ch):
        self.links[ord(ch)-ord("a")]=Node()
    
    def get(self,ch):
        return self.links[ord(ch)-ord("a")]
    
    def setEnd(self):
        self.flag=True 
    
    def isEnd(self):
        return self.flag


class Trie:

    def __init__(self):
        self.root=Node()
        
    def insert(self, word: str) -> None:
        node=self.root
        
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                node.put(word[i])
            
            node=node.get(word[i])
        
        node.setEnd()

    def search(self, word: str) -> bool:
        node=self.root
        
        for i in range(0,len(word)):
            if not node.containsKey(word[i]):
                return False
            
            node=node.get(word[i])
        
        return node.isEnd()
        
    def startsWith(self, prefix: str) -> bool:
        node=self.root
        
        for i in range(0,len(prefix)):
            if not node.containsKey(prefix[i]):
                return False
            
            node=node.get(prefix[i])
        
        return True
```

### Core Idea

```text
                 root
                  |
        ┌─────────┴─────────┐
        a                   b
        |                   |
        p                   a
        |                   |
        p                   t
        |                   |
       ...                 ...
```

Each node represents a character, and `flag=True` tells us that a **complete word ends at that node**.

---

# Problems Based on This Pattern

## 1. Implement Trie

**Pattern:** Normal Trie Template

The basic problem used to learn:

* `insert()`
* `search()`
* `startsWith()`

This is the foundation for all the Trie patterns below.

---

# 2️⃣ Trie + DFS

## Add & Search Words

**Pattern:**

```text
Normal Trie
     +
DFS
```

### What changes?

Normal search checks one character at a time.

But when the word contains:

```text
.
```

`.` can represent **any character**.

Therefore, at `.`:

```text
Try every available child
        ↓
      DFS
```

### Recognition

Use:

> **Trie + DFS when one character can represent multiple possibilities.**

---

# 3️⃣ Prefix Traversal + DFS

## Search Suggestions

**Pattern:**

```text
Trie
 +
Prefix Traversal
 +
DFS Collection
```

First traverse the Trie using the search prefix.

For example:

```text
searchWord = "mou"
```

After reaching:

```text
m → o → u
```

perform DFS from that node to collect possible words.

### Recognition

Use this pattern when:

> **You need all/some words beginning with a given prefix.**

---

# 4️⃣ Trie + DFS

## Longest Word

**Pattern:**

```text
Trie + DFS + isEnd()
```

During DFS, only continue to a child if:

```python
child.isEnd()
```

This ensures that every prefix of the selected word is itself a valid word.

### Recognition

Use this when:

> **A word is valid only if all of its prefixes are also present.**

---

# 5️⃣ Prefix Matching

## Replace Words

**Pattern:**

```text
Trie + Prefix Search
```

Insert all dictionary roots into the Trie.

While searching a word:

```text
Traverse character by character
        ↓
If isEnd() becomes True
        ↓
Stop immediately
```

The first complete word encountered is the shortest valid root.

### Recognition

Use this when:

> **You need the shortest/first valid prefix of a word.**

---

# 6️⃣ Component Trie

## Remove Sub-Folders

**Pattern:**

```text
Trie of folder components
```

Instead of storing individual characters, split paths using:

```text
/
```

For example:

```text
/a/b/c
```

becomes:

```text
a → b → c
```

### Recognition

Use this when:

> **The Trie keys are components separated by a delimiter instead of characters.**

---

# 7️⃣ Trie-Based Prefix Matching

## Longest Common Prefix

**Pattern:**

```text
Trie + Prefix Matching
```

Insert all strings into the Trie and determine how far all strings share the same path.

### Recognition

Use this when:

> **The problem asks for a common prefix among multiple strings.**

---

# 8️⃣ Trie + DFS + Mismatch Count

## Words Within Two Edits of Dictionary

**Pattern:**

```text
Trie
 +
DFS
 +
Mismatch Count
```

While traversing the Trie:

```text
same character
    ↓
continue normally

different character
    ↓
mismatch += 1
```

Stop exploring when:

```python
mismatch > 2
```

### Recognition

Use this when:

> **You need to search Trie paths while allowing a limited number of character differences.**

---

# 9️⃣ Binary Trie

## Maximum XOR of Two Numbers

**Pattern:**

```text
Binary Trie
```

Instead of:

```python
links=[None for i in range(26)]
```

use:

```python
links=[None,None]
```

because each number is represented using:

```text
0 / 1
```

To maximize XOR, always try to take the **opposite bit**.

```text
current bit = 0 → prefer 1
current bit = 1 → prefer 0
```

### Recognition

Use this when:

> **The problem involves maximizing/minimizing XOR between numbers.**

---

# 🔟 Trie + Matrix DFS

## Word Search II

**Pattern:**

```text
Trie
 +
Board DFS
```

Instead of searching every word independently:

```text
Build Trie of all words
        ↓
DFS from every board cell
        ↓
Follow only valid Trie paths
```

The Trie allows us to stop searching when the current character sequence does not match any word.

A useful optimization is to store the complete word in the Trie node:

```python
node.word
```

### Recognition

Use this when:

> **Multiple words need to be searched simultaneously inside a grid.**

---

# 1️⃣1️⃣ Reverse Trie

## Stream of Characters

**Pattern:**

```text
Reverse Trie
 +
Streaming Search
```

Insert every word **in reverse**.

For example:

```text
apple
```

is stored as:

```text
e → l → p → p → a
```

When a new character arrives, traverse the stream backwards.

### Recognition

Use this when:

> **The search depends on suffixes or the most recently received characters.**

---

# 1️⃣2️⃣ Trie + DP

## Concatenated Words

**Pattern:**

```text
Trie + DP
```

A word is concatenated if it can be formed using **two or more smaller words** from the dictionary.

Example:

```text
cat
cats
dog
catsdog
```

Here:

```text
catsdog = cats + dog
```

The Trie efficiently checks whether a substring is a valid dictionary word, while DP determines whether the complete word can be formed.

### Recognition

Use this when:

> **A string needs to be split into multiple valid dictionary words.**

---

# 1️⃣3️⃣ Trie + Backtracking

## Word Squares

**Pattern:**

```text
Trie
 +
Backtracking
 +
Prefix Search
```

At every step, construct the prefix required for the next row.

Use the Trie to quickly obtain words matching that prefix.

### Recognition

Use this when:

> **Backtracking choices are restricted by prefixes.**

---

# 1️⃣4️⃣ Reverse Trie + Palindrome Checking

## Palindrome Pairs

**Pattern:**

```text
Reverse Trie
 +
Palindrome Checking
```

Insert words in reverse and search for matching prefixes/suffixes while checking whether the remaining part is a palindrome.

### Recognition

Use this when:

> **The problem combines string reversal, prefixes/suffixes, and palindrome conditions.**

---

# 🗺️ Quick Pattern Recognition

When you see a Trie problem, ask:

```text
1. Is it normal character insertion/search?
        ↓
   Normal Trie

2. Is there a wildcard like "."?
        ↓
   Trie + DFS

3. Do I need words starting with a prefix?
        ↓
   Prefix Traversal + DFS

4. Do I need all prefixes to be valid words?
        ↓
   Trie + DFS + isEnd()

5. Do I need the shortest valid prefix?
        ↓
   Prefix Matching + isEnd()

6. Are the keys components like /a/b/c?
        ↓
   Component Trie

7. Is it XOR?
        ↓
   Binary Trie

8. Is it a board/grid with many words?
        ↓
   Trie + DFS

9. Does the search depend on the suffix/recent stream?
        ↓
   Reverse Trie

10. Does a word need to be split into smaller words?
        ↓
    Trie + DP

11. Is it prefix-based backtracking?
        ↓
    Trie + Backtracking

12. Does it involve reversed words + palindrome?
        ↓
    Reverse Trie + Palindrome Checking
```

---

# 📚 LeetCode Problems

## Array

| Problem                                                                                                                | Pattern               |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [0212 — Word Search II](https://leetcode.com/problems/word-search-ii/)                                                 | Trie + Matrix DFS     |
| [0421 — Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Binary Trie           |
| [0472 — Concatenated Words](https://leetcode.com/problems/concatenated-words/)                                         | Trie + DP             |
| [2452 — Words Within Two Edits of Dictionary](https://leetcode.com/problems/words-within-two-edits-of-dictionary/)     | Trie + DFS + Mismatch |

## String

| Problem                                                                                                            | Pattern               |
| ------------------------------------------------------------------------------------------------------------------ | --------------------- |
| [0212 — Word Search II](https://leetcode.com/problems/word-search-ii/)                                             | Trie + Matrix DFS     |
| [0472 — Concatenated Words](https://leetcode.com/problems/concatenated-words/)                                     | Trie + DP             |
| [2452 — Words Within Two Edits of Dictionary](https://leetcode.com/problems/words-within-two-edits-of-dictionary/) | Trie + DFS + Mismatch |

## Trie

| Problem                                                                                                                | Pattern               |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [0212 — Word Search II](https://leetcode.com/problems/word-search-ii/)                                                 | Trie + Matrix DFS     |
| [0421 — Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Binary Trie           |
| [0472 — Concatenated Words](https://leetcode.com/problems/concatenated-words/)                                         | Trie + DP             |
| [2452 — Words Within Two Edits of Dictionary](https://leetcode.com/problems/words-within-two-edits-of-dictionary/)     | Trie + DFS + Mismatch |

## Hash Table

| Problem                                                                                                                | Pattern     |
| ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| [0421 — Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Binary Trie |

## Bit Manipulation

| Problem                                                                                                                | Pattern     |
| ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| [0421 — Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Binary Trie |

## Backtracking

| Problem                                                                | Pattern           |
| ---------------------------------------------------------------------- | ----------------- |
| [0212 — Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie + Matrix DFS |

## Matrix

| Problem                                                                | Pattern           |
| ---------------------------------------------------------------------- | ----------------- |
| [0212 — Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie + Matrix DFS |

## Dynamic Programming

| Problem                                                                        | Pattern   |
| ------------------------------------------------------------------------------ | --------- |
| [0472 — Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Trie + DP |

## Depth-First Search

| Problem                                                                        | Pattern   |
| ------------------------------------------------------------------------------ | --------- |
| [0472 — Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Trie + DP |

## Sorting

| Problem                                                                        | Pattern   |
| ------------------------------------------------------------------------------ | --------- |
| [0472 — Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Trie + DP |

---

# Goal

The objective of this repository is **not to memorize individual Trie solutions**.

Instead:

```text
Learn the Normal Trie
        ↓
Understand what the problem adds
        ↓
Identify the pattern
        ↓
Modify the Trie template
        ↓
Solve the problem
```

> **Master the pattern, not the problem.** 
