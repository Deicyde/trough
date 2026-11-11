---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BinarySearchTree.Mem, Cslib.Algorithms.Lean.BinarySearchTree.inorderAux, Cslib.Algorithms.Lean.BinarySearchTree.inorder, Cslib.Algorithms.Lean.BinarySearchTree.All, Cslib.Algorithms.Lean.BinarySearchTree.Ordered, Cslib.Algorithms.Lean.BinarySearchTree.contains, Cslib.Algorithms.Lean.BinarySearchTree.insert, Cslib.Algorithms.Lean.BinarySearchTree.rank
statement: formalized
proof: formalized
---

# Binary search tree

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html).

## Membership in a binary tree

A key $x$ belongs to a binary tree $T$ when it is the key
of some node of $T$: no key belongs to the empty tree, and $x$ belongs to a node with key $k$,
left subtree $L$ and right subtree $R$ exactly when $x$ belongs to $L$, $x = k$, or $x$
belongs to $R$.

This membership does not use the search-tree ordering.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.Mem`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#mem).

## Inorder traversal of a binary tree with an accumulator

For a binary tree $t$ and a list
$s$, the accumulated traversal of the empty tree onto $s$ is $s$, and the accumulated traversal of
a node with key $k$, left subtree $L$ and right subtree $R$ onto $s$ is the accumulated traversal
of $L$ onto the list consisting of $k$ followed by the accumulated traversal of $R$ onto $s$.

Unfolding the recursion, the result is the inorder traversal of $t$ followed by $s$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.inorderAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#inorder-aux).

## Inorder traversal of a binary tree

The inorder traversal of a binary tree $t$ is the
accumulated inorder traversal of $t$ onto the empty list. Equivalently, the empty tree gives the
empty list, and a node with key $k$, left subtree $L$ and right subtree $R$ gives the inorder
traversal of $L$, then $k$, then the inorder traversal of $R$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.inorder`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#inorder).

## A predicate holding at every key of a binary tree

For a predicate $p$ on a type $\alpha$,
the empty binary tree satisfies "every key satisfies $p$", and a node with key $k$, left subtree
$L$ and right subtree $R$ satisfies it exactly when $L$ satisfies it, $p(k)$ holds and $R$
satisfies it.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.All`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#all).

## Ordered binary trees

Let $\alpha$ be a type with a relation $<$. The empty tree is
ordered, and a binary tree with root key $k$, left subtree $L$ and right subtree $R$ is ordered
when $L$ and $R$ are ordered, every key of $L$ is less than $k$, and $k$ is less than every key
of $R$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#ordered).

## Search in a binary search tree

For a linearly ordered type $\alpha$, a key $x \in \alpha$ and
a binary tree $t$ with keys in $\alpha$, the search for $x$ in $t$ returns a Boolean: false if $t$
is empty, and if $t$ is a node with key $k$, left subtree $L$ and right subtree $R$, the search
for $x$ in $L$ when $x < k$, the search for $x$ in $R$ when $k < x$, and true otherwise.

Unlike the index of a key in a binary tree, which encodes the root-to-node path as a positive
binary number, this search returns only whether the key was found.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#contains).

## Insertion into a binary search tree

For a linearly ordered type $\alpha$, a key
$x \in \alpha$ and a binary tree $t$ with keys in $\alpha$, inserting $x$ into the empty tree gives
the single node with key $x$ and empty subtrees; inserting $x$ into a node with key $k$, left
subtree $L$ and right subtree $R$ inserts $x$ into $L$ when $x < k$, inserts $x$ into $R$ when
$k < x$, and returns the node unchanged when $x = k$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#insert).

## Rank of a key in a binary tree

For a linearly ordered type $\alpha$, a key
$x \in \alpha$ and a binary tree $t$ with keys in $\alpha$, the rank of $x$ in $t$ is the number
of positions of the inorder traversal of $t$ whose entry is strictly less than $x$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.rank`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#rank).

## Inorder selection in a binary tree

For a binary tree $t$ and a natural number $i$,
selecting index $i$ in $t$ returns the entry at zero-based position $i$ of the inorder traversal
of $t$ when $i$ is less than the length of that traversal, and returns nothing otherwise.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.select`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#select).

## Binary search tree built from a list

For a linearly ordered type $\alpha$, the binary tree
built from a list $[x_1, \ldots, x_n]$ of elements of $\alpha$ is obtained from the empty tree by
inserting $x_n$, then $x_{n-1}$, and so on down to $x_1$, using binary search tree insertion; the
empty list gives the empty tree.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.fromList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#from-list).

## A predicate holds at all keys of a binary tree iff it holds at all its members

For a
type $\alpha$, a predicate $p$ on $\alpha$ and a binary tree $t$ with keys in $\alpha$, every key
of $t$ satisfies $p$ in the recursive sense (the empty tree qualifies, and a node qualifies when
its left subtree qualifies, its key satisfies $p$ and its right subtree qualifies) if and only if
$p(x)$ holds for every $x$ that is a member of $t$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.all_iff_forall_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#all-iff-forall-mem).

## Membership in the inorder traversal of a binary tree

For every binary tree $T$ and every
key $x$, $x$ occurs in the inorder traversal of $T$ if and only if $x$ lies in $T$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.mem_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#mem-inorder).

## Membership after insertion into a binary search tree

Let the keys be linearly ordered.
For all keys $x, y$ and every binary tree $T$, $y$ lies in the tree obtained by inserting $x$
into $T$ if and only if $y = x$ or $y$ lies in $T$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.mem_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#mem-insert).

## Binary search tree insertion preserves order

Let $\alpha$ be a linearly ordered type.
For every key $x \in \alpha$ and every ordered binary tree $T$ over $\alpha$, the tree obtained
by inserting $x$ into $T$ is ordered.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.ordered_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#ordered-insert).

## Search in a binary search tree is correct

For a linearly ordered type $\alpha$, a key
$x \in \alpha$ and a binary tree $t$ with keys in $\alpha$ that is ordered (recursively, every
key in the left subtree of a node is strictly smaller than the node's key and every key in its
right subtree is strictly larger), the comparison search for $x$ in $t$ returns true if and only
if $x$ is a member of $t$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#contains-eq-true-iff).

## The inorder traversal of an ordered binary tree is strictly increasing

Let $\alpha$ be
a linearly ordered type. If a binary tree $T$ over $\alpha$ is ordered, then in the inorder
traversal of $T$ every key is less than every key that comes after it.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.ordered_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#ordered-inorder).

## The inorder traversal of a binary search tree has no duplicates

For a linearly ordered
type $\alpha$ and a binary tree $t$ with keys in $\alpha$ that is ordered (recursively, every key
in the left subtree of a node is strictly smaller than the node's key and every key in its right
subtree is strictly larger), the inorder traversal of $t$ is a list with no repeated entries.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.inorder_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#inorder-nodup).

## Binary search trees built from a list are ordered

Let $\alpha$ be a linearly ordered
type. For every list $xs$ of elements of $\alpha$, the tree obtained from the empty tree by
inserting the elements of $xs$ one at a time, from the last element to the first, is ordered.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.ordered_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#ordered-from-list).

## Members of the binary search tree built from a list

For a linearly ordered type $\alpha$,
a key $x \in \alpha$ and a list $xs$ of elements of $\alpha$, $x$ is a member of the binary tree
built from $xs$ by successive binary search tree insertion if and only if $x$ occurs in $xs$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.mem_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#mem-from-list).

## The length of the inorder traversal of a binary tree is its number of nodes

For every
binary tree $T$, the number of nodes of $T$ (each node carries one key, and the empty tree has
none) equals the length of the inorder traversal of $T$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.numNodes_eq_length_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#num-nodes-eq-length-inorder).

## Inserting a present key into a binary search tree leaves its size unchanged

Let the
keys be linearly ordered, and let $T$ be an ordered binary tree. If a key $x$ lies in $T$, then
the tree obtained by inserting $x$ into $T$ has the same number of nodes as $T$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.numNodes_insert_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#num-nodes-insert-of-mem).

## Inserting an absent key into a binary search tree adds one node

Let the keys be
linearly ordered. For every binary tree $T$ and every key $x$ that does not lie in $T$, the tree
obtained by inserting $x$ into $T$ has one more node than $T$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.numNodes_insert_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#num-nodes-insert-of-not-mem).

## Rank counts the smaller inorder entries

For a linearly ordered type $\alpha$, a key
$x \in \alpha$ and a binary tree $t$ with keys in $\alpha$, the rank of $x$ in $t$ equals the
length of the list obtained from the inorder traversal of $t$ by keeping exactly the entries
strictly less than $x$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.rank_eq_count_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#rank-eq-count-inorder).

## Selection is indexing into the inorder traversal

For a binary tree $t$ and a natural
number $i$, selecting index $i$ in $t$ gives the same result as looking up zero-based position
$i$ of the inorder traversal of $t$: the entry at that position when $i$ is less than the length
of the traversal, and nothing otherwise.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.select_eq_getElem?_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#select-eq-get-elem-inorder).

## Selecting the rank of a key returns the key

Let $\alpha$ be a linearly ordered type
and let $t$ be a binary search tree with keys in $\alpha$, that is, at every node each key of the
left subtree is strictly smaller and each key of the right subtree is strictly larger than the
node's key. If $x$ is a key of $t$, then selecting, in $t$, the index equal to the rank of $x$
in $t$ returns $x$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.select_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#select-rank).

## The rank of a selected key is its index

Let $\alpha$ be a linearly ordered type and
let $t$ be a binary search tree with keys in $\alpha$, that is, at every node each key of the
left subtree is strictly smaller and each key of the right subtree is strictly larger than the
node's key. If selecting index $i$ in $t$ returns a key $x$, then the rank of $x$ in $t$
equals $i$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.rank_select`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#rank-select).

## Join of two binary trees

The join of the empty tree and a tree $R$ is $R$. The join of a tree
with root key $k$, left subtree $L_1$ and right subtree $L_2$ and a tree $R$ is the tree with root
key $k$, left subtree $L_1$ and right subtree the join of $L_2$ and $R$. Thus, when the first tree
is nonempty, $R$ becomes the right subtree of its rightmost node.

In the inorder traversal of the join, every key of the first tree comes before every key of the
second tree.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.join`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#join).

## Deletion from a binary search tree

Let $x$ be a key of a linearly ordered type. Deleting $x$
from the empty tree gives the empty tree. Deleting $x$ from a tree with root key $k$, left subtree
$L$ and right subtree $R$ gives the tree with root key $k$, left subtree $L$ with $x$ deleted and
right subtree $R$ if $x < k$; the tree with root key $k$, left subtree $L$ and right subtree $R$
with $x$ deleted if $k < x$; and the join of $L$ and $R$ otherwise, that is, if $x = k$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.delete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#delete).

## Membership in a join

For binary trees $L$ and $R$, a key $x$ occurs in the join of $L$ and
$R$ if and only if $x$ occurs in $L$ or $x$ occurs in $R$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.mem_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#mem-join).

## Inorder traversal of a join

For binary trees $L$ and $R$, the inorder traversal of the join
of $L$ and $R$ is the inorder traversal of $L$ followed by the inorder traversal of $R$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.inorder_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#inorder-join).

## Joining separated ordered trees

Let $L$ and $R$ be ordered binary search trees over a type
with a relation $<$. If $a < b$ for every key $a$ of $L$ and every key $b$ of $R$, then the join
of $L$ and $R$ is ordered.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.ordered_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#ordered-join).

## Deletion keeps the other keys

Let $t$ be a binary tree over a linearly ordered type, not
necessarily ordered, and let $x$ and $y$ be keys with $y \ne x$. If $y$ occurs in $t$, then $y$
occurs in the tree obtained by deleting $x$ from $t$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.mem_delete_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#mem-delete-of-mem).

## The deleted key is gone

If $t$ is an ordered binary search tree over a linearly ordered type
and $x$ is a key, then $x$ does not occur in the tree obtained by deleting $x$ from $t$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.not_mem_delete_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#not-mem-delete-self).

## Membership after deletion

If $t$ is an ordered binary search tree over a linearly ordered
type, then for all keys $x$ and $y$, the key $y$ occurs in the tree obtained by deleting $x$ from
$t$ if and only if $y$ occurs in $t$ and $y \ne x$.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.mem_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#mem-delete).

## Deletion preserves the search-tree order

If $t$ is an ordered binary search tree over a
linearly ordered type, then for every key $x$ the tree obtained by deleting $x$ from $t$ is
ordered.

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.ordered_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#ordered-delete).

## Inorder traversal after deletion

If $t$ is an ordered binary search tree over a linearly
ordered type and $x$ is a key, then the inorder traversal of the tree obtained by deleting $x$
from $t$ is the inorder traversal of $t$ with the first occurrence of $x$ removed (and is the
inorder traversal of $t$ itself if $x$ does not occur in it).

Formalized by `Cslib.Algorithms.Lean.BinarySearchTree.inorder_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinarySearchTree/Delete.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html#inorder-delete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary search tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/search-trees/binary-search-tree)
