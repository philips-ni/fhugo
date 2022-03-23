+++
title = "LeetCode tips"
author = ["Fei Ni"]
date = 2022-02-10
lastmod = 2022-03-23T12:01:32-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

<style>
  .ox-hugo-toc ul {
    list-style: none;
  }
</style>
<div class="ox-hugo-toc toc">
<div></div>

<div class="heading">Table of Contents</div>

- <span class="section-num">1</span> [Bit o/p](#bit-o-p)
    - <span class="section-num">1.1</span> [set a bit in pos for number](#set-a-bit-in-pos-for-number)
    - <span class="section-num">1.2</span> [unset/clear a bit in pos for number](#unset-clear-a-bit-in-pos-for-number)
    - <span class="section-num">1.3</span> [Toggling a bit at nth position](#toggling-a-bit-at-nth-position)
    - <span class="section-num">1.4</span> [Checking if bit at nth position is set or unset:](#checking-if-bit-at-nth-position-is-set-or-unset)
    - <span class="section-num">1.5</span> [Stripping off the lowest set bit :](#stripping-off-the-lowest-set-bit)
    - <span class="section-num">1.6</span> [Getting lowest set bit of a number](#getting-lowest-set-bit-of-a-number)
    - <span class="section-num">1.7</span> [XOR](#xor)
- <span class="section-num">2</span> [String tips](#string-tips)
- <span class="section-num">3</span> [Linked List](#linked-list)
- <span class="section-num">4</span> [tortoise & hare](#tortoise-and-hare)
- <span class="section-num">5</span> [Sliding window](#sliding-window)
- <span class="section-num">6</span> [Heap](#heap)
- <span class="section-num">7</span> [Binary Search](#binary-search)
- <span class="section-num">8</span> [Rolling Hash](#rolling-hash)
- <span class="section-num">9</span> [Stack](#stack)
- <span class="section-num">10</span> [Monotonic stack](#monotonic-stack)
- <span class="section-num">11</span> [Queue](#queue)
- <span class="section-num">12</span> [Robot Bounded In Circle](#robot-bounded-in-circle)
- <span class="section-num">13</span> [Monotonic queue](#monotonic-queue)
- <span class="section-num">14</span> [Tree traverse](#tree-traverse)
- <span class="section-num">15</span> [Trie Tree](#trie-tree)
- <span class="section-num">16</span> [Segment Tree](#segment-tree)
- <span class="section-num">17</span> [Binary index tree （树状数组)](#binary-index-tree-树状数组)
- <span class="section-num">18</span> [Union Find](#union-find)
- <span class="section-num">19</span> [DFS](#dfs)
- <span class="section-num">20</span> [BFS](#bfs)
- <span class="section-num">21</span> [Sort](#sort)
- <span class="section-num">22</span> [Topology sort](#topology-sort)
- <span class="section-num">23</span> [DP](#dp)
- <span class="section-num">24</span> [Backtracking](#backtracking)
- <span class="section-num">25</span> [Standard parser implementation](#standard-parser-implementation)
- <span class="section-num">26</span> [multiple threading](#multiple-threading)
    - <span class="section-num">26.1</span> [dead lock](#dead-lock)
    - <span class="section-num">26.2</span> [live lock](#live-lock)
    - <span class="section-num">26.3</span> [Starvation](#starvation)
    - <span class="section-num">26.4</span> [Race condition](#race-condition)
    - <span class="section-num">26.5</span> [Vmware questions](#vmware-questions)
- <span class="section-num">27</span> [System design template](#system-design-template)
- <span class="section-num">28</span> [Leetcode template](#leetcode-template)
- <span class="section-num">29</span> [Links](#links)

</div>
<!--endtoc-->



## <span class="section-num">1</span> Bit o/p {#bit-o-p}


### <span class="section-num">1.1</span> set a bit in pos for number {#set-a-bit-in-pos-for-number}

```c++
num |= (1 << pos);
```


### <span class="section-num">1.2</span> unset/clear a bit in pos for number {#unset-clear-a-bit-in-pos-for-number}

```c++
num &= (~(1 << pos));
```


### <span class="section-num">1.3</span> Toggling a bit at nth position {#toggling-a-bit-at-nth-position}

```c++
num ^= (1 << pos);
```


### <span class="section-num">1.4</span> Checking if bit at nth position is set or unset: {#checking-if-bit-at-nth-position-is-set-or-unset}

```c++
bool bit = num & (1<<pos);
```


### <span class="section-num">1.5</span> Stripping off the lowest set bit : {#stripping-off-the-lowest-set-bit}

```c++
num = num & (num-1);
```


### <span class="section-num">1.6</span> Getting lowest set bit of a number {#getting-lowest-set-bit-of-a-number}

```c++
int ret = num & (-num);
```


### <span class="section-num">1.7</span> XOR {#xor}

```c++
0^N == N
N^N == 0
M^N == N^M
a^b^a = b
```

```python
 '''
 Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

 You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



 Example 1:

 Input: nums = [1,2,1,3,2,5]
 Output: [3,5]
 Explanation:  [5, 3] is also a valid answer.
 '''
from functools import reduce
class Solution(object):
    def singleNumber(self, nums):
      a_xor_b = reduce(lambda x, y: x ^ y, nums)
      xor_sum = dict()
      for a in nums:
	  b = a_xor_b ^ a
	  if b in xor_sum and xor_sum[b] == a:
	      return [b,a]
	  xor_sum[a] = b
```

-   <https://leetcode.com/problems/binary-gap/>
-   <https://leetcode.com/problems/single-number-iii/>
-   <https://leetcode.com/problems/decode-xored-permutation/>
-   <https://emre.me/computer-science/bit-manipulation-tricks/>


## <span class="section-num">2</span> String tips {#string-tips}

```python
# check if a string is something like "abcabcabc"
def repeatedSubstringPattern(self, str):
    return str in (2 * str)[1:-1]
```

```python
def isRotatedFrom(self, s1, s2):
    return s1 in (s2 + s2)
```


## <span class="section-num">3</span> Linked List {#linked-list}

```python
class ListNode(object):
    def __init__(self, x):
	self.val = x
	self.next = None
```

```c++
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
```

-   Dummy node
-   three points (pre, curr, next)
-   <https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/>
-   <https://leetcode.com/problems/reverse-linked-list/>
-   <https://leetcode.com/problems/lru-cache/> (hash + linkedList)
-   <https://leetcode.com/problems/lfu-cache/>

    ```c++
    list<int> usage;
    //  insert key into the begin of list
    usage.insert(usage.begin(), key);
    // move the node of it to the begin of list
    usage.splice(usage.begin(), usage, it);
    ```


## <span class="section-num">4</span> tortoise & hare {#tortoise-and-hare}

```python
class Solution:
    def findDuplicate(self, nums):
	# Find the intersection point of the two runners.
	tortoise = nums[0]
	hare = nums[0]
	while True:
	    # print "tortoise: %d, hare: %d" % (tortoise, hare)
	    tortoise = nums[tortoise]
	    hare = nums[nums[hare]]
	    # print "tortoise: %d, hare: %d" % (tortoise, hare)
	    if tortoise == hare:
		break
	# Find the "entrance" to the cycle.
	ptr1 = nums[0]
	ptr2 = tortoise
	while ptr1 != ptr2:
	    ptr1 = nums[ptr1]
	    ptr2 = nums[ptr2]
	return ptr1
```


## <span class="section-num">5</span> Sliding window {#sliding-window}

Sliding Window Technique is a method for finding subarrays in an array that satisfy given conditions.
We do this via maintaining a subset of items as our window, and resize and move that window within the larger list until we find a solution.
Sliding Window Technique is a subset of Dynamic Programming, and it frequently appears in algorithm interviews.

Examples:

-   Easy: Statically Sized Sliding Window: Given an array of integers, find maximum/minimum sum subarray of the required size.
-   Medium: Dynamically Sized Sliding Window: Given an array of positive integers, find the subarrays that add up to a given number.
-   Variation (Medium): Same question but for an array with all integers (positive, 0, negative). The optimal solution is Kadane’s Algorithm, but Sliding Window can still be applied with modifications (not recommended though).
-   Medium: Flipping/Swapping: Given an array of 0’s and 1’s, find the maximum sequence of continuous 1’s that can be formed by flipping at-most k 0’s to 1’s.
-   Hard: Strings: Given a string and n characters, find the shortest substring that contains all the desired characters.

    ```python
    # Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
    # Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    # Output: 6
    # Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    # Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    class Solution:
        def longestOnes(self, nums: List[int], k: int) -> int:
    	left = 0
    	for right in range(len(nums)):
    	    # If we included a zero in the window we reduce the value of k.
    	    # Since k is the maximum zeros allowed in a window.
    	    k -= 1 - nums[right]
    	    # A negative k denotes we have consumed all allowed flips and window has
    	    # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
    	    if k < 0:
    		# If the left element to be thrown out is zero we increase k.
    		k += 1 - nums[left]
    		left += 1
    	return right - left + 1

    ```

Links:

-   <https://quanticdev.com/algorithms/dynamic-programming/sliding-window/>
-   <https://leetcode.com/problems/max-consecutive-ones-iii>


## <span class="section-num">6</span> Heap {#heap}

scenarios:

-   top K ordered items
-   two-heaps pattern,  where we are given a set of elements such that we can divide them into two parts, To be able to solve these kinds of problems, we want to know the smallest element in one part and the biggest element in the other part.
    -   <https://emre.me/coding-patterns/two-heaps/>

Notes:

-   python default heap is minHeap
-   C++ default heap is maxHeap

<!--listend-->

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
	// using minHeap here
	priority_queue<int, vector<int>, greater<int>> pq;
	for (int num : nums) {
	    pq.push(num);
	    if (pq.size() > k) {
		pq.pop();
	    }
	}
	return pq.top();
    }
};
```

```python
def findKthLargest(self, nums, k):
    heap = nums[:k]
    heapify(heap)
    for n in nums[k:]:  heappushpop(heap, n)
    return heap[0]
```

```python
from heapq import *

class MedianFinder:
    def __init__(self):
	"""
	initialize your data structure here.
	"""
	self.small = []
	self.large = []
	# heapq.heapify(self.small)
	# heapq.heapify(self.large)


    def addNum(self, num: int) -> None:
	heapq.heappush(self.small,num)
	tmp = heapq.heappop(self.small)
	heapq.heappush(self.large, -1 * tmp)
	if len(self.large) > len(self.small):
	    tmp = heapq.heappop(self.large)
	    heapq.heappush(self.small, -1 * tmp)


    def findMedian(self) -> float:
	if len(self.large) == len(self.small):
	    return (-1 * self.large[0] + self.small[0]) / 2
	else:
	    return self.small[0]
```

-   <https://leetcode.com/problems/find-median-from-data-stream/>


## <span class="section-num">7</span> Binary Search {#binary-search}

```c++
vector<int> searchRange(vector<int>& nums, int target) {
     return {findBound(nums, target, true), findBound(nums, target, false)};
}

 int findBound(vector<int>& nums, int target, bool lower) {
     int l = 0, r = nums.size() - 1, answer = -1;

     while(l <= r) {
	 int mid = (l+r)/2;
	 if (nums[mid] == target) {
	     answer = mid; // keep the current answer as you mignt not be able to comback if this was the answer.
	     if (lower) {
		 r = mid - 1;
	     } else {
		 l = mid + 1;
	     }
	 } else if (nums[mid] > target) {
	     r = mid - 1;
	 } else {
	     l = mid + 1;
	 }
     }

     return answer;
 }
```

```python
import bisect

# bisect_left(a, x, lo=0, hi=None)
# This method returns the index i where must be inserted the value x such that list a is kept ordered
a = [1, 3, 5, 6, 7, 9, 10, 12, 14]
x = 8
# i = bisect.bisect_left(a, x, lo=2, hi=7) # [5, 6, 7, 9, 10]
i = bisect.bisect_left(a, x)
print(i) # 5
a.insert(i, x)
print(a) # [1, 3, 5, 6, 7, 8, 9, 10, 12, 14]

# bisect_right(a, x, lo=0, hi=None)
# This function works the same as bisect_left but in the event that x value already appears in the a list , the index i would be just after the rightmost x value already there.
a = [1, 2, 3, 4, 4, 7]
x = 4
i = bisect.bisect_right(a, x)
print(i) # 5

a.insert(i, x)
print(a) # [1, 2, 3, 4, 4, 4, 7]
```

-   <https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/>


## <span class="section-num">8</span> Rolling Hash {#rolling-hash}

```c++
class Solution {
public:
    string longestPrefix(string &s) {
	long h1 = 0, h2 = 0, mul = 1, len = 0, mod = 1000000007;
	for (int i = 0, j = s.length() - 1; j > 0; ++i, --j) {
	    int first = s[i] - 'a', last = s[j] - 'a';
	    h1 = (h1 * 26 + first) % mod;
	    h2 = (h2 + mul * last) % mod;
	    mul = mul * 26 % mod;
	    if (h1 == h2)
		len = i + 1;
	}
	return s.substr(0, len);
    }
};

```

```python
class Solution(object):
    def longestPrefix(self, s):
	hashF = hashB = 0
	code = 32
	mod = int(1e9 + 7)

	l = 0
	mul = 1
	for i in range(len(s) - 1):
	    hashF = (hashF * code + ord(s[i])) % mod
	    hashB = (hashB + ord(s[~i]) * mul) % mod
	    mul = (mul * code) % mod
	    if hashF == hashB:
		l = i + 1
	return s[:l]

```

-   <https://leetcode.com/problems/longest-happy-prefix/>


## <span class="section-num">9</span> Stack {#stack}

-   <https://leetcode.com/problems/valid-parentheses/>


## <span class="section-num">10</span> Monotonic stack {#monotonic-stack}

```python
# trapping-rain-water
class Solution:
    def trap(self, height: List[int]) -> int:
	res, stk = 0, []
	for i in range(len(height)):
	    while stk and height[i] > height[stk[-1]]:
		h = height[stk.pop()]
		if stk:
		    minH = min(height[stk[-1]], height[i])
		    res += (minH - h) * (i - stk[-1] - 1)
	    stk.append(i)
	returnb2 res
```

-   <https://leetcode.com/problems/largest-rectangle-in-histogram/>
-   <https://leetcode.com/problems/trapping-rain-water/>


## <span class="section-num">11</span> Queue {#queue}


## <span class="section-num">12</span> Robot Bounded In Circle {#robot-bounded-in-circle}

It's said to be used by Amazon very often

```python
class Solution(object):
    def isRobotBounded(self, instructions):
	"""
	:type instructions: str
	:rtype: bool
	"""

	di = (0,1)
	# G -> (0,1), L -> (-1,0), R -> (1,0)
	x,y = 0,0
	for instruction in instructions:
	    if instruction == 'G':
		x,y = x+di[0],y+di[1]
	    elif instruction == 'L':
		di = (-di[1],di[0]) # very smart way to change direction
	    else:
		di = (di[1],-di[0])
	return (x==0 and y==0) or di!=(0,1)
```

-   <https://leetcode.com/problems/robot-bounded-in-circle/>


## <span class="section-num">13</span> Monotonic queue {#monotonic-queue}


## <span class="section-num">14</span> Tree traverse {#tree-traverse}

-   <https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/?ref=lbp>
-


## <span class="section-num">15</span> Trie Tree {#trie-tree}

```bash
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
```

```python
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
	self.children = collections.defaultdict(TrieNode)
	self.is_word = False

class Trie:
    def __init__(self):
	self.root = TrieNode()
    def insert(self, s):
	curr = self.root
	for i in s:
	    curr = curr.children[i]
	curr.is_word = True
    def search(self, s):
	curr = self.root
	for i in s:
	    if i in curr.children:
		curr = curr.children[i]
	    else:
		return False
	return curr.is_word

    def startsWith(self,s):
	curr = self.root
	for i in s:
	    if i in curr.children:
		curr = curr.children[i]
	    else:
		return False
	return True
```

```c++
class Trie {
public:
    Trie() {}

    void insert(string word) {
	Trie* node = this;
	for (char ch : word) {
	    if (!node->next.count(ch)) { node->next[ch] = new Trie(); }
	    node = node->next[ch];
	}
	node->isword = true;
    }

    bool search(string word) {
	Trie* node = this;
	for (char ch : word) {
	    if (!node->next.count(ch)) { return false; }
	    node = node->next[ch];
	}
	return node->isword;
    }

    bool startsWith(string prefix) {
	Trie* node = this;
	for (char ch : prefix) {
	    if (!node->next.count(ch)) { return false; }
	    node = node->next[ch];
	}
	return true;
    }

private:
    map<char, Trie*> next = {};
    bool isword = false;
};
```

-   <https://leetcode.com/problems/implement-trie-prefix-tree/submissions/>


## <span class="section-num">16</span> Segment Tree {#segment-tree}

```python
#Segment tree node
class Node(object):
    def __init__(self, start, end):
	self.start = start
	self.end = end
	self.total = 0
	self.left = None
	self.right = None

class NumArray(object):
    def __init__(self, nums):
	"""
	initialize your data structure here.
	:type nums: List[int]
	"""
	#helper function to create the tree from input array
	def createTree(nums, l, r):
	    #base case
	    if l > r:
		return None
	    #leaf node
	    if l == r:
		n = Node(l, r)
		n.total = nums[l]
		return n
	    mid = (l + r) // 2
	    root = Node(l, r)
	    #recursively build the Segment tree
	    root.left = createTree(nums, l, mid)
	    root.right = createTree(nums, mid+1, r)

	    #Total stores the sum of all leaves under root
	    #i.e. those elements lying between (start, end)
	    root.total = root.left.total + root.right.total
	    return root
	self.root = createTree(nums, 0, len(nums)-1)

    def update(self, i, val):
	"""
	:type i: int
	:type val: int
	:rtype: int
	"""
	#Helper function to update a value
	def updateVal(root, i, val):
	    #Base case. The actual value will be updated in a leaf.
	    #The total is then propogated upwards
	    if root.start == root.end:
		root.total = val
		return val
	    mid = (root.start + root.end) // 2
	    #If the index is less than the mid, that leaf must be in the left subtree
	    if i <= mid:
		updateVal(root.left, i, val)
	    #Otherwise, the right subtree
	    else:
		updateVal(root.right, i, val)
	    #Propogate the changes after recursive call returns
	    root.total = root.left.total + root.right.total

	    return root.total

	return updateVal(self.root, i, val)

    def sumRange(self, i, j):
	"""
	sum of elements nums[i..j], inclusive.
	:type i: int
	:type j: int
	:rtype: int
	"""
	#Helper function to calculate range sum
	def rangeSum(root, i, j):
	    #If the range exactly matches the root, we already have the sum
	    if root.start == i and root.end == j:
		return root.total
	    mid = (root.start + root.end) // 2
	    #If end of the range is less than the mid, the entire interval lies
	    #in the left subtree
	    if j <= mid:
		return rangeSum(root.left, i, j)
	    #If start of the interval is greater than mid, the entire inteval lies
	    #in the right subtree
	    elif i >= mid + 1:
		return rangeSum(root.right, i, j)
	    #Otherwise, the interval is split. So we calculate the sum recursively,
	    #by splitting the interval
	    else:
		return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
	return rangeSum(self.root, i, j)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
```

-   <https://leetcode.com/problems/range-sum-query-mutable/>


## <span class="section-num">17</span> Binary index tree （树状数组) {#binary-index-tree-树状数组}

It's also named as Fenwick tree
Doing similar work as segment tree, less code, both are good at rangeSum and rangeQuery
The idea to create a array bit, bit[x] store the sum of bit[x-lowBit(x)+1,x] inclusive.
please notice, bit is using 1-based indexing

-   [About binary index tree](https://blog.csdn.net/bestsort/article/details/80796531?spm=1001.2101.3001.6650.3&utm%5Fmedium=distribute.pc%5Frelevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7EHighlightScore-3.queryctrv2&depth%5F1-utm%5Fsource=distribute.pc%5Frelevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7EHighlightScore-3.queryctrv2&utm%5Frelevant%5Findex=6)
-   <https://www.youtube.com/watch?v=RgITNht%5Ff4Q>

<!--listend-->

```python
def lowBit(n):
    return n & (-n)
class BIT:
    def __init__(self, size):
	self.bit = [0] * (size + 1)

    def getSum(self, idx):  # Get sum in range [1..idx], 1-based indexing
	s = 0
	while idx > 0:
	    s += self.bit[idx]
	    idx -= lowBit(idx)
	return s

    def getSumRange(self, left, right):  # left, right inclusive, 1-based indexing
	return self.getSum(right) - self.getSum(left - 1)

    def addValue(self, idx, val):  # 1-based indexing
	while idx < len(self.bit):
	    self.bit[idx] += val
	    idx += lowBit(idx)

class NumArray:

    def __init__(self, nums: List[int]):
	self.nums = nums
	self.bit = BIT(len(nums))
	for i, v in enumerate(nums):
	    self.bit.addValue(i+1, v)

    def update(self, index: int, val: int) -> None:
	diff = val - self.nums[index]  # get diff amount of `val` compared to current value
	self.bit.addValue(index+1, diff)  # add this `diff` amount at index `index+1` of BIT, plus 1 because in BIT it's 1-based indexing
	self.nums[index] = val # update latest value of `nums[index]`

    def sumRange(self, left: int, right: int) -> int:
	return self.bit.getSumRange(left+1, right+1)
```

-   <https://leetcode.com/problems/range-sum-query-mutable/discuss/1406686/C%2B%2BJavaPython-Binary-Indexed-Tree>
-   <https://zhuanlan.zhihu.com/p/92920381>


## <span class="section-num">18</span> Union Find {#union-find}

```python
# Idea: find minimal edges to make graph fully traversable
# - we can use union-find here, we will have 2 union here, one for Alice, one for Bob
# - because type 3 may add travese for both Alice and Boby, so we will pick such edges firstly
# - every time while we pick one edge, we update the union, also update the requiredEdgeNum, if both node of this edge alread in union, we don't need add this edge
# - At the end we check if both union are fully connected, if yes, the answer is len(edges) - requiredEdgeNum
class UnionFind:
    def __init__(self,n):
	self.distinct_component_num = n
	self.components = list(range(n+1))
    def union(self,i,j):
	if self.find(i) == self.find(j):
	    return False
	else:
	    self.components[self.find(i)] = j
	    self.distinct_component_num -= 1
	    return True

    def find(self,i):
	if i == self.components[i]:
	    return i
	else:
	    self.components[i] = self.find(self.components[i])
	    return self.components[i]

    def connected(self):
	return self.distinct_component_num == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
	required_edge_num = 0
	edges.sort(key=lambda x:x[0], reverse = True)
	alice = UnionFind(n)
	bob = UnionFind(n)
	for e in edges:
	    if e[0] == 3:
		tmp1 = alice.union(e[1],e[2])
		tmp2 = bob.union(e[1],e[2])
		if tmp1 or tmp2:
		    required_edge_num += 1
	    elif e[0] == 2:
		if bob.union(e[1],e[2]):
		    required_edge_num += 1
	    elif e[0] == 1:
		if alice.union(e[1],e[2]):
		    required_edge_num += 1
	if alice.connected() and bob.connected():
	    return len(edges) - required_edge_num
	else:
	    return -1
```

```python
# a graph is a valid tree only if len(edges) == n-1 and no cycle
def validTree(self, n, edges):
    parent = list(range(n))
    def find(x):
	return x if parent[x] == x else find(parent[x])
    def union(xy): # xy is a list of x and y
	x, y = map(find, xy)
	parent[x] = y
	return x != y
    return len(edges) == n-1 and all(map(union, edges))
```

-   <https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/>
-   <https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/>
-   <https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/>


## <span class="section-num">19</span> DFS {#dfs}

```python
class Solution:
    def numIslands(self, grid):
	if not grid:
	    return 0

	count = 0
	for i in range(len(grid)):
	    for j in range(len(grid[0])):
		if grid[i][j] == '1':
		    self.dfs(grid, i, j)
		    count += 1
	return count

    def dfs(self, grid, i, j):
	if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
	    return
	grid[i][j] = '#'
	self.dfs(grid, i+1, j)
	self.dfs(grid, i-1, j)
	self.dfs(grid, i, j+1)
	self.dfs(grid, i, j-1)
```

-   <https://leetcode.com/problems/number-of-islands/>


## <span class="section-num">20</span> BFS {#bfs}

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
	if not root:
	    return []
	q = deque([root])
	ret = []
	level = 0
	while len(q) > 0:
	    sz = len(q)
	    current = [-1] * sz
	    for i in range(0,sz):
		node = q.popleft()
		if level % 2 == 0:
		    current[i] = node.val
		else:
		    current[sz-i-1] = node.val
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)
	    level += 1
	    ret.append(current)
	return ret
```

-   <https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/>


## <span class="section-num">21</span> Sort {#sort}

Sort 2D array

```cpp
vector<vector<int>>& edges;
sort(begin(edges), end(edges),
     [](vector<int>& a, vector<int>& b) { return a[0] > b[0]; });
```

```python
edges: List[List[int]]
edges.sort(key:lambda x: x[0], reverse=False)
```

More python example:

```python
  l = [[1,2,3],[3,4,6,],[2,4,5],[2,101,5],[2,34,1]]
  l.sort(key=lambda x: (x[0],x[1]), reverse=True)
  print(l)


  students= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

  def compare(e):
    return (e[1],e[0])

  students = sorted(students,key=compare)
  print(students)


  # task: sort the list of strings, such that items listed as '_fw' come before '_bw'
  foolist = ['Goo_fw', 'Goo_bw', 'Foo_fw', 'Foo_bw', 'Boo_fw', 'Boo_bw']

  def sortfoo(s):
      s1, s2 = s.split('_')
      r = 1 if s2 == 'fw' else 2     # forces 'fw' to come before 'bw'
      return (r, s1)                 # order first by 'fw'/'bw', then by name

  foolist.sort(key=sortfoo)          # sorts foolist inplace

  print(foolist)
  # prints:
  # ['Boo_fw', 'Foo_fw', 'Goo_fw', 'Boo_bw', 'Foo_bw', 'Goo_bw']

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
	r = Counter(nums)
	return sorted(nums, key=lambda x: (r[x], -x))
```


## <span class="section-num">22</span> Topology sort {#topology-sort}

```python
class Solution:
    def findOrder(self, N,P):
	graph = defaultdict(list)
	indegree = [0] * N
	q = deque()
	ans = []
	for nxt, pre in P:
	    graph[pre].append(nxt)
	    indegree[nxt] += 1
	for i in range(N):
	    if indegree[i] == 0:
		q.append(i)
	while q:
	    cur = q.popleft()
	    ans.append(cur)
	    for nxt in graph[cur]:
		indegree[nxt] -= 1
		if indegree[nxt] == 0:
		    q.append(nxt)
	return ans if len(ans) == N else []
```

-   <https://leetcode.com/problems/course-schedule/>
-   <https://leetcode.com/problems/course-schedule-ii/>


## <span class="section-num">23</span> DP {#dp}

```python
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
	events.sort()
	starts = [x for x,y,z in events]

	@lru_cache(None)
	def dp(idx, k):
	    if k == 0 or idx >= len(events):
		return 0
	    next_event = bisect_right(starts, events[idx][1])
	    return max(dp(idx+1, k), events[idx][2] + dp(next_event, k-1))

	return dp(0,k)
```

-   <https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/>
-   <https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/>


## <span class="section-num">24</span> Backtracking {#backtracking}

```python
#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
class Solution(object):
    def permute(self, l):
	if len(l) == 0:
	    return [[]]
	permuations = []
	curr = []
	isVisited = [False] * len(l)
	self.backTracking(permuations, curr, isVisited, l)
	return permuations

    def backTracking(self, permuations,  curr, isVisited, l):
	if len(curr) == len(l):
	    permuations.append(curr[:])
	    return

	for i in range(len(l)):
	    if not isVisited[i]:
		isVisited[i] = True
		curr.append(l[i])
		self.backTracking(permuations, curr, isVisited, l)
		isVisited[i] = False
		curr.pop()
```

-   <https://leetcode.com/problems/permutations/submissions/>
-   <https://leetcode.com/problems/word-search-ii/>


## <span class="section-num">25</span> Standard parser implementation {#standard-parser-implementation}

```python
class Solution:
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]

    def expTree(self, s: str) -> 'Node':
	tokens = collections.deque(list(s))
	return self.parse_expression(tokens)

    def parse_expression(self, tokens):
	lhs = self.parse_term(tokens)
	while len(tokens) > 0 and tokens[0] in ['+', '-']:
	    op = tokens.popleft()
	    rhs = self.parse_term(tokens)
	    lhs = Node(val=op, left=lhs, right=rhs)
	return lhs

    def parse_term(self, tokens):
	lhs = self.parse_factor(tokens)
	while len(tokens) > 0 and tokens[0] in ['*', '/']:
	    op = tokens.popleft()
	    rhs = self.parse_factor(tokens)
	    lhs = Node(val=op, left=lhs, right=rhs)
	return lhs

    def parse_factor(self, tokens):
	if tokens[0] == '(':
	    tokens.popleft() # consume '('
	    node = self.parse_expression(tokens)
	    tokens.popleft() # consume ')'
	    return node
	else:
	    # Single operand
	    token = tokens.popleft()
	    return Node(val=token)
```

-   <https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/>


## <span class="section-num">26</span> multiple threading {#multiple-threading}

```python
from threading import Lock

class Foo:
    def __init__(self):
	self.locks = (Lock(),Lock())
	self.locks[0].acquire()
	self.locks[1].acquire()

    def first(self, printFirst):
	printFirst()
	self.locks[0].release()

    def second(self, printSecond):
	with self.locks[0]:
	    printSecond()
	    self.locks[1].release()


    def third(self, printThird):
	with self.locks[1]:
	    printThird()
```

```python
'''
There are two kinds of threads: oxygen and hydrogen. Your goal is to group these threads to form water molecules.

This solution uses Semaphore and Barrier. It is simple to understand, and performs well.

Semantics
a Semaphore -- trying to acquire it, is possible if there are tokens left. Otherwise the thread that tried is asked to wait until a different thread returns the tokens it was using.
a Barrier -- if a thread reaches it, it can cross it, only if a predefined number of other threads have also arrived.
Logic
The solution creates 1 Semaphore for Hydrogen, and allows 2 threads to aquire it concurrently. Likewise, we create one for Oxygen, but this one only allows 1 thread.

To ensure the molecule is generated at once, we use a barrier, which can only be crossed when 3 atoms have gathered.

After each function completes, we release the token on the Semaphore.
'''

from threading import Semaphore
from threading import Barrier

class H2O:
    def __init__(self):
	self.sem_h = Semaphore(2)
	self.sem_o = Semaphore(1)
	self.bar_assembling = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
	with self.sem_h:
	    self.bar_assembling.wait()
	    releaseHydrogen()
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
	with self.sem_o:
	    self.bar_assembling.wait()
	    releaseOxygen()
```

```python
from concurrent import futures

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
	hostname = lambda url: url.split('/')[2]
	seen = {startUrl}

	with futures.ThreadPoolExecutor(max_workers=16) as executor:
	    tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
	    while tasks:
		for url in tasks.popleft().result():
		    if url not in seen and hostname(startUrl) == hostname(url):
			seen.add(url)
			tasks.append(executor.submit(htmlParser.getUrls, url))

	return list(seen)
```


### <span class="section-num">26.1</span> dead lock {#dead-lock}

A deadlock is a situation in which processes block each other due to resource acquisition and none of the processes makes any progress as they wait for the resource held by the other process.
To successfully characterize a scenario as deadlock, the following four conditions must hold simultaneously:

-   Mutual Exclusion: At least one resource needs to be held by a process in a non-sharable mode. Any other process requesting that resource needs to wait.
-   Hold and Wait: A process must hold one resource and requests additional resources that are currently held by other processes.
-   No Preemption: A resource can’t be forcefully released from a process. A process can only release a resource voluntarily once it deems to release.
-   Circular Wait: A set of a process {p0, p1, p2,.., pn} exists in a manner that p0 is waiting for a resource held by p1, pn-1 waiting for a resource held by p0.


### <span class="section-num">26.2</span> live lock {#live-lock}

In the case of a livelock, the states of the processes involved in a live lock scenario constantly change. On the other hand, the processes still depend on each other and can never finish their tasks.


### <span class="section-num">26.3</span> Starvation {#starvation}

Starvation is an outcome of a process that is unable to gain regular access to the shared resources it requires to complete a task and thus, unable to make any progress.

One of the possible solutions to prevent starvation is to use a resource scheduling algorithm with a priority queue that also uses the aging technique. Aging is a technique that periodically increases the priority of a waiting process. With this approach, any process waiting for a resource for a longer duration eventually gains a higher priority. And as the resource sharing is driven through the priority of the process, no process starves for a resource indefinitely.

Another solution to prevent starvation is to follow the round-robin pattern while allocating the resources to a process. In this pattern, the resource is fairly allocated to each process providing a chance to use the resource before it is allocated to another process again.


### <span class="section-num">26.4</span> Race condition {#race-condition}

When two processes are competing with each other causing data corruption


### <span class="section-num">26.5</span> Vmware questions {#vmware-questions}

-   What's the diffrence between mutex and spinlock?
    -   mutex will sleep for waiting
    -   spinlock will keep trying (busy waiting)
    -   mutex need do context switch
    -   spinlock doesn't do context switch
    -   using spinlock , we should keep the protected area code very simple and running fast, otherwise ,it may occupy a lot of cpu
-   Can you talk about condition variable
    -   contdition variable always comes with a lock and a condtion checking monitor
    -   condition variable support notify, so once some state chane, we can we can notify condition vaiable, and it will recheck the condition

<!--listend-->

-   <https://leetcode.com/problems/design-bounded-blocking-queue/>
-   <https://leetcode.com/problemset/concurrency/>
-   <https://leetcode.com/problems/print-in-order/discuss/335939/5-Python-threading-solutions>-(Barrier-Lock-Event-Semaphore-Condition)-with-explanation
-   <https://www.baeldung.com/cs/deadlock-livelock-starvation>
-   <https://leetcode.com/problems/fizz-buzz-multithreaded/discuss/542960/python-greater99.28-a-standard-Lock>()-based-solution-with-detailed-explanation
-   <https://stackoverflow.com/questions/5869825/when-should-one-use-a-spinlock-instead-of-mutex>


## <span class="section-num">27</span> System design template {#system-design-template}

```nil
(1) FEATURE EXPECTATIONS [5 min]
	(1) Use cases
	(2) Scenarios that will not be covered
	(3) Who will use
	(4) How many will use
	(5) Usage patterns
(2) ESTIMATIONS [5 min]
	(1) Throughput (QPS for read and write queries)
	(2) Latency expected from the system (for read and write queries)
	(3) Read/Write ratio
	(4) Traffic estimates
		- Write (QPS, Volume of data)
		- Read  (QPS, Volume of data)
	(5) Storage estimates
	(6) Memory estimates
		- If we are using a cache, what is the kind of data we want to store in cache
		- How much RAM and how many machines do we need for us to achieve this ?
		- Amount of data you want to store in disk/ssd
(3) DESIGN GOALS [5 min]
	(1) Latency and Throughput requirements
	(2) Consistency vs Availability  [Weak/strong/eventual => consistency | Failover/replication => availability]
(4) HIGH LEVEL DESIGN [5-10 min]
	(1) APIs for Read/Write scenarios for crucial components
	(2) Database schema
	(3) Basic algorithm
	(4) High level design for Read/Write scenario
(5) DEEP DIVE [15-20 min]
	(1) Scaling the algorithm
	(2) Scaling individual components:
		-> Availability, Consistency and Scale story for each component
		-> Consistency and availability patterns
	(3) Think about the following components, how they would fit in and how it would help
		a) DNS
		b) CDN [Push vs Pull]
		c) Load Balancers [Active-Passive, Active-Active, Layer 4, Layer 7]
		d) Reverse Proxy
		e) Application layer scaling [Microservices, Service Discovery]
		f) DB [RDBMS, NoSQL]
			> RDBMS
			    >> Master-slave, Master-master, Federation, Sharding, Denormalization, SQL Tuning
			> NoSQL
			    >> Key-Value, Wide-Column, Graph, Document
				Fast-lookups:
				-------------
				    >>> RAM  [Bounded size] => Redis, Memcached
				    >>> AP [Unbounded size] => Cassandra, RIAK, Voldemort
				    >>> CP [Unbounded size] => HBase, MongoDB, Couchbase, DynamoDB
		g) Caches
			> Client caching, CDN caching, Webserver caching, Database caching, Application caching, Cache @Query level, Cache @Object level
			> Eviction policies:
				>> Cache aside
				>> Write through
				>> Write behind
				>> Refresh ahead
		h) Asynchronism
			> Message queues
			> Task queues
			> Back pressure
		i) Communication
			> TCP
			> UDP
			> REST
			> RPC
(6) JUSTIFY [5 min]
	(1) Throughput of each layer
	(2) Latency caused between each layer
	(3) Overall latency justification
```


## <span class="section-num">28</span> Leetcode template {#leetcode-template}

```bash
If input array is sorted then
    - Binary search
    - Two pointers

If asked for all permutations/subsets then
    - Backtracking

If given a tree then
    - DFS
    - BFS

If given a graph then
    - DFS
    - BFS

If given a linked list then
    - Two pointers

If recursion is banned then
    - Stack

If must solve in-place then
    - Swap corresponding values
    - Store one or more different values in the same pointer

If asked for maximum/minimum subarray/subset/options then
    - Dynamic programming

If asked for top/least K items then
    - Heap

If asked for common strings then
    - Map
    - Trie

Else
    - Map/Set for O(1) time & O(n) space
    - Sort input for O(nlogn) time and O(1) space
```


## <span class="section-num">29</span> Links {#links}

-   <https://emre.me/categories/#coding-patterns>
-   <https://github.com/seanprashad/leetcode-patterns>
