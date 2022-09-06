#Recursion

#CSM WS4
'''
P6 Mario needs to jump over a series of Piranha plants, represented as a string of 0’s and
1's. Mario only moves forward and can either step (move forward one space) or jump
(move forward two spaces) from each position. How many different ways can Mario
traverse a level without stepping or jumping into a Piranha plant? Assume that every
level begins with a 1 (where Mario starts) and ends with a 1 (where Mario must end
up).
Hint: Does it matter whether Mario goes from left to right or right to left? Which one is easier
to check?
'''

def mario_number(level):


    """
    Return the number of ways that Mario can traverse the
    level, where Mario can either hop by one digit or two
    digits each turn. A level is defined as being an integer
    with digits where a 1 is something Mario can step on and
    0 is something Mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """

    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level // 10) + mario_number((level// 10) // 10)

#CSM WS8 
'''
Write has_cycle which takes in a Link and returns True if and only
if there is a cycle in the Link. Note that the cycle may start at any node and be of
any length. Try writing a solution that keeps track of all the links we've seen. Then
try to write a solution that doesn't store those witnessed links (consider using two
pointers!).
'''
def has_cycle(s):
    """
    >>> has_cycle(Link.empty)
    False
    >>> a = Link(1, Link(2, Link(3)))
    >>> has_cycle(a)
    False
    >>> a.rest.rest.rest = a
    >>> has_cycle(a)
    True
    """
    seen_before = []
    while s is not Link.empty:
        if s in seen_before:
            return True
        seen_before.append(s)
    return False
    # Alternative solution - less intuitive but more efficient
    if s is Link.empty:
        return False
    slow, fast = s, s.rest
    while fast is not Link.empty:
        if fast.rest is Link.empty:
            return False
        elif fast is slow or fast.rest is slow:
            return True
        slow, fast = slow.rest, fast.rest.rest
    return False

#!!!!!!IMPORTANT & HARD 
# summer20 Q4
def lemon(xv):
    """
    A lemon-copy is a perfect replica of a nested list's box-and-pointer structure.
        If an environment diagram were drawn out, the two should be entirely
        separate but identical.

    A `xv` is a list that only contains ints and other lists.

    The function `lemon` generates a lemon-copy of the given list `xv`.

    Note: The `isinstance` function takes in a value and a type and determines
        whether the value is of the given type. So

        >>> isinstance("abc", str)
        True
        >>> isinstance("abc", list)
        False

    Here's an example, where lemon_y = lemon(y)


                             +-----+-----+            +-----+-----+-----+
                             |     |     |            |     |     |     |
                             |  +  |  +-------------> | 200 | 300 |  +  |
        y +----------------> |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
        lemon_y +-+             |                |       ^           |
                  |             +----------------+       |           |
                  |                                      +-----------+
                  |
                  |          +-----+-----+            +-----+-----+-----+
                  |          |     |     |            |     |     |     |
                  +------->  |  +  |  +-------------> | 200 | 300 |  +  |
                             |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
                                |                |       ^           |
                                +----------------+       |           |
                                                         +-----------+

    >>> x = [200, 300]
    >>> x.append(x)
    >>> y = [x, x]              # this is the `y` from the doctests
    >>> lemon_y = lemon(y)      # this is the `lemon_y` from the doctests
    >>> # check that lemon_y has the same structure as y
    >>> len(lemon_y)
    2
    >>> lemon_y[0] is lemon_y[1]
    True
    >>> len(lemon_y[0])
    3
    >>> lemon_y[0][0]
    200
    >>> lemon_y[0][1]
    300
    >>> lemon_y[0][2] is lemon_y[0]
    True
    >>> # check that lemon_y and y have no list objects in common
    >>> lemon_y is y
    False
    >>> lemon_y[0] is y[0]
    False
    """
def lemon(xv):
    '''deep copy the link'''
    lemon_lookup = []
    def helper(xv):
        if isinstance(xv, int):
            return xv
        for old_new in lemon_lookup:
            if old_new[0] is xv:
                return old_new[1]
        new_xv = []
        lemon_lookup.append((xv, new_xv))
        for element in xv:
            new_xv.append(helper(element))
        return new_xv
    return helper(xv)



#!!!HARD
# Summer20 Q7
def village(apple, t):
    """
    The `village` operation takes
        a function `apple` that maps an integer to a tree where
            every label is an integer.
        a tree `t` whose labels are all integers

    And applies `apple` to every label in `t`.

    To recombine this tree of trees into a a single tree,
        simply copy all its branches to each of the leaves
        of the new tree.

    For example, if we have
        apple(x) = tree(x, [tree(x + 1), tree(x + 2)])
    and
        t =         10
                  /    \
                20      30

    We should get the output

        village(apple, t)
          =                    10
                           /       \
                        /             \
                      11               12
                    /    \           /    \
                  20      30       20      30
                 / \     /  \     /  \    /  \
                21 22  31   32   21  22  31  32
    >>> t = tree(10, [tree(20), tree(30)])
    >>> apple = lambda x: tree(x, [tree(x + 1), tree(x + 2)])
    >>> print_tree(village(apple, t))
    10
      11
        20
          21
          22
        30
          31
          32
      12
        20
          21
          22
        30
          31
          32
    """
    def graft(t, bs):
        """
        Grafts the given branches `bs` onto each leaf
        of the given tree `t`, returning a new tree.
        """
        if is_leaf(t):
            return tree(label(t), bs)
        new_branches = [graft(b, bs) for b in branches(t)]
        return tree(label(t), new_branches)
    base_t = apple(label(t))
    bs = [village(apple, b) for b in branches(t)]
    return graft(base_t, bs)


#SP20 Q2
"""A: (3 pts) Implement is_power, which takes a positive integer base and a
non-negative integer s. It returns whether s is a power of base, meaning that there
is some non-negative integer n such that pow(base, n) equals s.

IMPORTANT: You may not call pow, use the ** operator, or import any function
(such as math.log). Your solution must be recursive.

Check the doctests with: python3 ok -q a
"""
def is_power(base, s):
    """Return whether s is a power of base.

    >>> is_power(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
    True
    >>> is_power(5, 1)    # pow(5, 0) = 1
    True
    >>> is_power(5, 5)    # pow(5, 1) = 5
    True
    >>> is_power(5, 15)   # 15 is not a power of 5 (it's a multiple)
    False
    >>> is_power(3, 9)
    True
    >>> is_power(3, 8)
    False
    >>> is_power(3, 10)
    False
    >>> is_power(1, 8)
    False
    >>> is_power(2, 0)    # 0 is not a power of any positive base.
    False

    >>> is_power(4, 16)
    True
    >>> is_power(4, 64)
    True
    >>> is_power(4, 63)
    False
    >>> is_power(4, 65)
    False
    >>> is_power(4, 32)
    False
    """
    assert base > 0 and s >= 0
    assert type(base) is int and type(s) is int
    if s == 1:
        return True
    elif base == 1 or s == 0 or s % base != 0:
        return False
    else:
        return is_power(base, s // base)


curry2 = lambda f: lambda x: lambda y: f(x, y)

"""B: (5 pts) Implement powers, a generator function which takes positive
integers n and k. It yields all integers m that are both powers of k and whose
digits appear in order in n.

Assume that is_power is implemented correctly.

Note: powers may yield its results in any order. The doctests below check what
is yielded, but not the order. The built-in sorted function used in the doctests
takes in an iterable object and returns a list containing the elements of the
iterable in non-decreasing order.

Check the doctests with: python3 ok -q b
"""
def powers(n, k):
    """Yield all powers of k whose digits appear in order in n.

    >>> sorted(powers(12345, 5))
    [1, 5, 25, 125]
    >>> sorted(powers(54321, 5))  # 25 and 125 are not in order
    [1, 5]
    >>> sorted(powers(2493, 3))
    [3, 9, 243]

    >>> sorted(powers(2493, 2))
    [2, 4]
    >>> sorted(powers(164352, 2))
    [1, 2, 4, 16, 32, 64]
    """
    curry2 = lambda f: lambda x: lambda y: f(x, y)
    def build(seed):
        """Yield all non-negative integers whose digits appear in order in seed.
        0 is yielded because 0 has no digits, so all its digits are in seed.
        """
        if seed == 0:
            yield 0
        else:
            for x in build(seed // 10):
                yield x
                yield x * 10 + seed % 10
    yield from filter(curry2(is_power)(k), build(n))



#SP21 !!!!!!!YIELD QUESTION Q3(b)(c)
'''
Definition. An infinite iterator t is one for which next(t) can be called any number of times and always
returns a value.
Implement ring, a generator function that takes a non-empty list s. It returns an infinite generator that
repeatedly yields the values of s in the order they appear in s.
'''
def ring(s):
    """Yield all values of 
    non-empty s in order, repeatedly.
    >>> t = ring([2, 5, 3])
    >>> [next(t), next(t), next(t), next(t), next(t), next(t), next(t)]
    [2, 5, 3, 2, 5, 3, 2]
    """
    while True:
        yield from s

'''
ii. (1.0 pt) Fill in blank (b).
(c) (5.0 points)
Implement fork, a function that takes an infinite iterator t. It returns two infinite iterators that each
iterate over the contents of t.
'''
def fork(t):
    """Return two iterators with the same contents as infinite iterator t.
    >>> a, b = fork(ring([1, 2, 3]))
    >>> [next(a), [next(b), next(b), next(b)], next(a), [next(b), next(b), next(b)], next(a)]
    [1, [1, 2, 3], 2, [1, 2, 3], 3]
    """
    s = []
    def copy():
        i = 0
        while True:
            if len(s) == i :
                s.append(next(t))
            yield s[i]
            i += 1
    return copy(),copy()



#SU21 final Q8
'''
(a) (9.0 points)
Consider the function merger, which returns the result of merging all the terms in a sequence using f, a
two-argument function. The function f is applied to the first and second elements until there is only one
element in the subsequence.
For example, merging the sequence 1, 2, 3 with the function lambda x, y: x + y would return the
result 6.
Now consider the sequence of ascending integers: 1, 2, 3, ... k and all of its unique ascending subsequences of at least length two. For example, the sequence [1,2,3,4] has the following unique ascending subsequences of length at least two: [1,2], [1,3], [1,4], [1,2,3], [1,2,4], [1,3,4], [2,3],
[2,4], [2,3,4], [3,4], [1,2,3,4]. Our goal is to count the number of subsequences of merger that
result in exactly N when merging with f.
For the first doctest, f is lambda x, y: x + y, N is 6, and K is 4, so only [1,2,3] and [2,4] add up to
6, meaning count_merger(6, 4, lambda x, y: x + y) returns 2.
Write a function count_merger that returns the number of ways to make exactly N using at least two
unique, ascending integers from range 1 to K (inclusive) and a function f which is a two-argument function.

'''
def count_merger(n,k,f):
    """
    Returns the number of ways to make exactly N using at least two unique,
    ascending integers from range 1 to K (inclusive) and a function f that
    accepts two integers as arguments and returns an integer.
    Assume K >= 1.
    >>> from operator import add, mul, sub
    >>> add1_mult = lambda x, y: (x + 1) * y
    >>> count_merger(6, 4, lambda x, y: x + y) # 1 + 2 + 3 = 6, 2 + 4 = 6
    2
    >>> count_merger(36, 6, mul) # 1 * 2 * 3 * 6; 2 * 3 * 6
    2
    >>> count_merger(36, 6, add)
    0
    >>> count_merger(36, 6, add1_mult) # (5 + 1) * 6
    1
    >>> count_merger(24, 3, lambda x, y: 24) # f(1, 2); f(f(1, 2), 3); f(1, 3); f(2, 3)
    4
    >>> count_merger(1, 1, lambda x, y: x)
    0
    >>> count_merger(-2, 5, sub) # 1 - 3; 2 - 4; 3 - 5
    3
    """
    def helper(start, i):
        if i > k:
            return 0

        a = helper(start, i + 1)
        b = helper( f(start, i) , i + 1 )

        if f(start, i) == n:
            return 1 + a + b
        else:
            return a+b
        
    total = 0
    i = 1
    while i<=k:#i<k
        total += helper(i, i + 1) 
        i += 1

    return total

#SP21 mt2 Q8
'''
https://cs61a.org/exam/sp21/mt2/61a-sp21-mt2_sol.pdf
Generates each word that can be formed by following a path
in TREE_OF_LETTERS from the root to a leaf,
where WORDS_LIST is a list of allowed words (with no duplicates).
'''
def word_finder(letter_tree, words_list):
    def string_builder(t, str):
        str += t.label
        if t.is_leaf() and str in words_list:
            yield str
        for b in t.branches:
            yield from string_builder(b, str)
    yield from string_builder(letter_tree, "")



#SP19 mt2 Q6
'''
6. (15 points) Trie this
A Trie is a Tree where every node in the tree contains a single letter except for the root which is always the
empty string. Every path from the root to a leaf forms a word. You may assume no words are substrings of
other words in the trie (e.g., hi and him). The gure below is a trie generated by storing the words [this,
is, the, trie]. The Tree class is dened on Page 2 of the Midterm 2 Study Guide.
(a) (7 pt) Implement add_word which takes a Trie and a word and adds the word to the trie.
'''
def make_trie(words):
    """ Makes a tree where every node is a letter of a word.
    All words end as a leaf of the tree.
    words is given as a list of strings.
    """
    trie = Tree('')
    for word in words:
        add_word(trie, word)
        return trie

def add_word(trie, word):
    if word == '':
        return
    branch = None
    for b in trie.branches:
        if b.label == word[0]:
            branch = b
    if not branch:
        branch = Tree(word[0])
        trie.branches.append(branch)
    add_word(branch, word[1:])


'''
(b) (8 pt) Implement get_words, which takes a Trie and returns a list of all the words the Trie is storing.
'''
def get_words(trie):
    '''
    >>> get_words(make_trie(['this', 'is', 'the', 'trie']))
    ['this', 'the', 'trie', 'is']
    '''
    if trie.is_leaf():
        return [trie.label]
    return sum([[trie.label + word for word in get_words(branch)] for branch in trie.branches], [])
    #sum([[...],[...]] , [])
    #the last [] tells sum the data type what we are summing



#FA20 !!!!!!!Fork Tree(https://cs61a.org/exam/fa20/mt2/61a-fa20-mt2_sol.pdf)

#CSM WS05Last Question
'''
Fill in num_nums, which finds the number of d-digit numbers with 
digits 1 through 9 such that digit x is repeated exactly t times.'''
def num_nums(d, x, t):
    '''
    >>> num_nums(2, 1, 2)
    1 # only 11 satisfies criteria
    >>> num_nums(2, 1, 1)
    16 # 12, 13, 14, 15, 16, 17, 18, 19, 21, 31, 41, 51, 61,
    71, 81, 91
    '''
    if d == 0 and t > 0:
        return 0
    elif d == 0 and t == 0:
        return 1
    elif t < 0:
        return 0
    else:
        with_d_here = num_nums(d - 1, x, t - 1)
        without_d_here = 8 * num_nums(d - 1, x, t)
        return with_d_here + without_d_here




#Lecture:
def partition(val,largest_ele):
    if largest_ele == 0 or val < 0:
        return
    else:
        if val == largest_ele:
            yield str(largest_ele)
        else:
            for i in partition(val-largest_ele,largest_ele):
                yield str(largest_ele) + " + " + i
            yield from partition(val,largest_ele)



#Fa21 Final Q8
'''
Implement segment, which takes a positive integer n (such as 3456) and a two-argument function grouped.
It returns a linked list s containing linked lists of digits (such as <<3 4> <5 6>>). Together, the elements
of s contain all digits of n in order. Two adjacent digits a and b (with a to the left of b) appear in the
same element of s if grouped(a, b) returns a true value.
The Link class appears on page 2 (left column) of the midterm 2 study guide.
'''
def segment(n, grouped):
    """Return a linked list of linked lists of the digits of positive n.
    Adjacent digits a and b appear in the same linked list if grouped(a, b).
    >>> print(segment(3233344, lambda a, b: a == b))
    <<3> <2> <3 3 3> <4 4>>
    >>> print(segment(314159, lambda a, b: a == 1))
    <<3> <1 4> <1 5> <9>>
    """
    part = Link.empty
    parts = Link.empty
    while n:
        if part is Link.empty or grouped(n%10,part.first):
            part = Link(n%10,part)
        else:
            parts = Link(part, parts)
            part = Link(n%10)
        n //= 10
    return parts






#FA19 mt2 Q5  Combination
'''
Implement partitions, which is a generator function that takes positive integers n and m. It yields
strings describing all partitions of n using parts up to size m. Each partition is a sum of non-increasing
positive integers less than or equal to m that totals n. The partitions function yields a string for each
partition exactly once.
You may not use lambda, if, and, or, lists, tuples, or dictionaries in your solution (other than what
already appears in the template).
'''
def partitions(n, m):
    """Yield all partitions of N using parts up to size M.
    >>> list(partitions(1, 1))
    ['1']
    >>> list(partitions(2, 2))
    ['2', '1 + 1']
    >>> list(partitions(4, 2))
    ['2 + 2', '2 + 1 + 1', '1 + 1 + 1 + 1']
    >>> for p in partitions(6, 4):
    ... print(p)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n == m:
        yield str(m)
    if n > 0 and m > 0:
        for p in partitions(n - m, m):
            yield str(m) + ' + ' + p
        yield from partitions(n, m - 1)



#FA18 mt2 Q6  Link Mutation
'''
Implement replace, which takes two non-empty linked lists s and t, as well as positive integers i and j with
i < j. It mutates s by removing elements with indices from i to j (removing element i but not removing
element j) and replacing them with t. Afterward, s contains all of the objects in t, so a change to t would be
reflected in s as well. t may change as a result of calling replace. Assume s has at least j elements.'''
def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.
    >>> s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    >>> replace(s, t, 2, 4)
    >>> print(s)
    <3, 4, 0, 1, 2, 7>
    >>> t.rest.first = 8
    >>> print(s)
    <3, 4, 0, 8, 2, 7>
    """
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        replace(s.rest, t, i - 1, j - 1)
    else:
        for k in range(j - i):
            s.rest = s.rest.rest
        end = t
        while end.rest is not Link.empty:
            end = end.rest
        s.rest, end.rest = t, s.rest



#FA18 mt2 Q7 Tree https://cs61a.org/exam/fa18/mt2/61a-fa18-mt2_sol.pdf
def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> [f(v) for f in lookups(k, 2)]
    ['C', 'A']
    >>> [f(v) for f in lookups(k, 3)]
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    if k.label == key:
        yield lambda v: v.label
    for i in range(len(k.branches)):
        for lookup in lookups(k.branches[i], key):
            yield new_lookup(i, lookup)


def new_lookup(i, f):
    def g(v):
        return f(v.branches[i])
    return g

#FA17 mt3 Q5 Autumn Leaves Tree Mutation
'''
Definition. A pile (of leaves) for a tree t with no repeated leaf labels is a dictionary in which the label for
each leaf of t is a key, and its value is the path from that leaf to the root. Each path from a node to the root is
either an empty tuple, if the node is the root, or a two-element tuple containing the label of the node’s parent
and the rest of the path (i.e., the path to the root from the node’s parent).
(a) (5 pt) Implement pile, which takes a tree constructed using the tree data abstraction. It returns a pile for
that tree. You may use the tree, label, branches, and is_leaf functions from the midterm 2 study guide.'''
def pile(t):
    """Return a dict that contains every path from a leaf to the root of tree t.
    >>> pile(tree(5, [tree(3, [tree(1), tree(2)]), tree(6, [tree(7)])]))
    {1: (3, (5, ())), 2: (3, (5, ())), 7: (6, (5, ()))}
    """
    p = {}
    def gather(u, parent):
        if is_leaf(u):
            p[label(u)] = parent
        for b in branches(u):
            gather(b, (label(u), parent))
    gather(t, ())
    return p

'''(b)Implement Path, a class whose constructor takes a tree t constructed by tree and a leaf_label.
Assume all leaf labels of t are unique. When a Path is printed, labels in the path from the root to the leaf of
t with label leaf_label are displayed, separated by dashes. Assume pile is implemented correctly.'''
class Path:
    """A path through a tree from the root to a leaf, identified by its leaf label.
    >>> a = tree(5, [tree(3, [tree(1), tree(2)]), tree(6, [tree(7)])])
    >>> print(Path(a, 7), Path(a, 2))
    5-6-7 5-3-2
    """
    def __init__(self, t, leaf_label):
        self.pile, self.end = pile(t), leaf_label
    def __str__(self):
        path, s = self.pile[self.end], str(self.end)
        while path:
            path, s = path[1], str(path[0]) + '-' + s
        return s






#####!!!!One Line Recursion


# Method 1: Recursive Fibonacci
def fib(n): return 1 if n in {0, 1} else fib(n-1) + fib(n-2)
print(fib(10))
#89
# Method 2: Recursive Factorial
def fac(x): return 1 if x<=1 else x * fac(x-1)
print(fac(10))
# 3628800
# Method 3: Recursive Factorial with Lambda
fac = lambda n: 1 if n<=1 else n * fac(n-1)
print(fac(10))
# 3628800
# Method 4: Recursive Quicksort
unsorted = [33, 2, 3, 45, 6, 54, 33]
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
print(q(unsorted))
# [2, 3, 6, 33, 33, 45, 54]


#FA16 mt2 Q3: https://cs61a.org/exam/fa16/mt2/61a-fa16-mt2_sol.pdf#page=6

'''Implement quota, which takes a one-argument function f and a non-negative integer limit. The function it
returns has the same behavior as f, except that each value is only returned up to limit times. After that, the
function returns an “Over quota” message instead, and the limit is decreased by 1 for future calls.'''
def quota(f, limit):
    """A decorator that limits the number of times a value can be returned.
    >>> square = lambda x: x * x
    >>> square = quota(square, 3)
    >>> square(6) # 1st call with return value 36
    36
    >>> [square(5) for x in range(3)] # 3 calls when the limit is 3
    [25, 25, 25]
    >>> square(5) # 4th call with return value 25
    'Over quota! Limit is now 2'
    >>> square(-6) # 2nd call with return value 36
    36
    >>> square(-6) # 3rd call when the limit is 2
    'Over quota! Limit is now 1'
    >>> square(7) # 1st call when the limit is 1
    49
    >>> square(5) # 5th call with return value 25
    'Over quota! Limit is now 0'
    """
def quota(f, limit):
    values = []
    def limited(n):
        nonlocal limit
        y = f(n)
        count = len([x for x in values if x == y])
        values.append(y)
        if count < limit:
            return y
        limit = limit - 1
        return 'Over quota! Limit is now ' + str(limit)
    return limited

#FA16 mt2 Q7: https://cs61a.org/exam/fa16/mt2/61a-fa16-mt2_sol.pdf#page=6
'''
Implement sums, which takes two positive integers n and k. It returns a list of lists containing all
the ways that a list of k positive integers can sum to n. Results can appear in any order.'''
def sums(n, k):
    """Return the ways in which K positive integers can sum to N.
    >>> sums(2, 2)
    [[1, 1]]
    >>> sums(2, 3)
    []
    >>> sums(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums(5, 3)
    [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    if k == 1:
        return [[n]]
    y = []
    for x in range(1, n): # range(1, n-k+2) is OK
        y.extend([s + [x] for s in sums(n-x, k-1)])
    return y
    #OR
    if n == 0 and k == 0:
        return [[]]
    y = []
    for x in range(1, n+1):
        y.extend([s + [x] for s in sums(n-x, k-1)])
    return y

#shorter version
f = lambda x, y: (x and [[x] + z for z in y] + f(x-1, y)) or []
def sums(n, k):
    g = lambda w: (w and f(n, g(w-1))) or [[]]
    return [v for v in g(k) if sum(v) == n]



# Recursive practice:https://medium.com/co-learning-lounge/recursive-function-python-practice-examples-c37df75555e8

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')

def GCD(a, b):
	low = min(a, b)
	high = max(a, b)

	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return GCD(low, high%low)




#FA16 Q6 Binary Tree
'''Implement binary, which takes a list s of unique integers. It returns a binary search tree containing
all of those integers, represented as a BTree instance or BTree.empty. The values in any path of this tree
must appear in the same order as they did in s. The BTree class is on page 2 of the midterm 2 study guide.'''
from tree import *
def binary(s):
    """Construct a binary search tree from S for which all paths are in order.
    >>> binary([3, 5, 1])
    BTree(3, BTree(1), BTree(5))
    >>> binary([4, 3, 7, 6, 2, 9, 8])
    BTree(4, BTree(3, BTree(2)), BTree(7, BTree(6), BTree(9, BTree(8))))
    """
    assert len(s) == len(set(s)), 'All elements of s should be unique'
    if not s:
        return BTree.empty
    root = s[0]
    left = [x for x in s if x < root]
    right = [x for x in s if x > root]
    return BTree(root, binary(left), binary(right))


#SP20 Q1 !!!!!!!!!Hard !Tree Curry
'''
1) A "number tree" is a Tree whose labels are _unique_ positive integers.
   No repeated labels appear in a number tree.

2) A "plucking order" for a number tree t is a sequence of unique positive
   integers that are all labels of t.

3) A plucking order is "valid" if both of these conditions are true:
   (a) the plucking order contains all labels of t, and
   (b) in the plucking order, the label for each node of t appears after
       the labels of all its descendant nodes. Thus, leaves appear first.

Note: redwood, pine, and cyprus are all kinds of trees.
"""

"""A: (3 pts) Implement order, which takes a number tree called redwood. It returns
a valid plucking order as a list of numbers. If there is more than one valid
plucking order for redwood, your order function can return any one of them.

IMPORTANT: You do not need to return EVERY valid plucking order; just one.

Check the doctests with: python3 ok -q a
'''
def order(redwood):
    """Return a list containing a valid plucking order for the labels of t.

    >>> order(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))               # The only valid plucking order.
    [4, 3, 2, 1]
    >>> order(Tree(1, [Tree(2), Tree(3)])) in [[2, 3, 1], [3, 2, 1]]  # There are 2 valid orders.
    True
    >>> o = order(Tree(1, [Tree(2, [Tree(3)]), Tree(4, [Tree(5)])]))  # There are many valid orders,
    >>> o.index(5) < o.index(4)                                       # but all have 5 before 4,
    True
    >>> o.index(3) < o.index(2)                                       # and 3 before 2,
    True
    >>> o[4:]                                                         # and 1 at the end.
    [1]

    >>> order(Tree(7, [Tree(4, [Tree(6)]), Tree(5)])) in [[6, 5, 4, 7], [5, 6, 4, 7], [6, 4, 5, 7]]
    True
    """
    plucking_order = []
    for b in redwood.branches:
        plucking_order.extend(order(b))
    return plucking_order + [redwood.label]


"""B: (5 pts) Implement pluck, which takes a number tree called pine and returns
a function that is called repeatedly on the elements of a plucking order. If that
plucking order is valid, the final call returns 'success!'. Otherwise, if one of
the repeated calls is on a number that is not part of a valid plucking order, the
error string 'Hey, not valid!' is returned.

Since pine is a number tree and the values passed to plucker form a plucking
order, you can assume that:
- The labels of pine are unique,
- All values k passed to the plucker function are unique for a given pine, and
- All values k are labels of pine.

Check the doctests with: python3 ok -q b
"""
def pluck(pine):
    """Return a function that returns whether a plucking order is valid
    for a number tree t when called repeatedly on elements of a plucking order.

    Calling the function returned by pluck should not mutate pine.

           +---+
           | 1 |
           +---+
           /   \----          /                 +---+         +---+
       | 2 |         | 6 |
       +---+         +---+
         |            /          |           /          +---+      +---+ +---+
       | 3 |      | 7 | | 8 |
       +---+      +---+ +---+
        / \               |
       /   \              |
    +---+ +---+         +---+
    | 4 | | 5 |         | 9 |
    +---+ +---+         +---+

    >>> b0 = Tree(2, [Tree(3, [Tree(4), Tree(5)])])
    >>> b1 = Tree(6, [Tree(7), Tree(8, [Tree(9)])])
    >>> t = Tree(1, [b0, b1])
    >>> pluck(t)(9)(8)(7)(6)(5)(4)(3)(2)(1)
    'success!'
    >>> pluck(t)(5)(9)(4)(7)(3)(8)(6)(2)(1)
    'success!'
    >>> pluck(t)(2)
    'Hey, not valid!'
    >>> pluck(t)(5)(9)(7)(6)
    'Hey, not valid!'

    >>> pluck(b0)(5)(2)
    'Hey, not valid!'
    >>> pluck(b0)(4)(5)(3)(2)
    'success!'
    """
    def plucker(k):


        def pluck_one_leaf(cyprus):
            """Return a copy of cyprus without leaf k and check that k is a
            leaf label, not an interior node label.
            """
            if not cyprus.is_leaf() and cyprus.label == k:
                return 'Hey, not valid!'
            plucked_branches = []
            for b in cyprus.branches:
                skip_this_leaf = b.is_leaf() and b.label == k
                if not skip_this_leaf:
                    plucked_branch_or_error = pluck_one_leaf(b)
                    if isinstance(plucked_branch_or_error, str):
                        return plucked_branch_or_error
                    else:
                        plucked_branches.append(plucked_branch_or_error)
            return Tree(cyprus.label, plucked_branches)

            
        nonlocal pine
        if pine.is_leaf():
            assert k == pine.label, 'all k must appear in pine'
            return 'success!'
        pine = pluck_one_leaf(pine)
        if isinstance(pine, str):
            return pine
        return plucker
    return plucker





'''__________________________________________Build-in resources_____________________________________'''

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)




class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        print("open")
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
        
        
        


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'






