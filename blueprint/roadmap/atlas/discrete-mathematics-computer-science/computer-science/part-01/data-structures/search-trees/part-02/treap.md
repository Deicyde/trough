---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Treap.Tree, Cslib.Algorithms.Lean.Treap.Tree.AllNodes, Cslib.Algorithms.Lean.Treap.Tree.MemNode, Cslib.Algorithms.Lean.Treap.Tree.MemKey, Cslib.Algorithms.Lean.Treap.Tree.contentsAux, Cslib.Algorithms.Lean.Treap.Tree.contents, Cslib.Algorithms.Lean.Treap.Tree.contents_node, Cslib.Algorithms.Lean.Treap.Tree.size
statement: formalized
proof: formalized
---

# Treap

51 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html).

## Treap

## Treap trees

For a type $\kappa$ of keys and a type $\nu$ of values, a treap tree is
either empty or a node made of a left subtree, a key in $\kappa$, a value in $\nu$, a
natural-number priority and a right subtree. Trees are finite, and no ordering of keys or
priorities is imposed; the treap invariants are stated separately.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#tree).

## Treap predicate holding at every node

Let $p$ be a predicate on a key, a value and a
natural-number priority. A tree satisfies $p$ at every node when $p(k, v, n)$ holds for the key
$k$, value $v$ and priority $n$ of each of its nodes. By recursion, this holds for the empty
tree, and holds for a node exactly when it holds for the left subtree, $p$ holds at the node's
key, value and priority, and it holds for the right subtree.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.AllNodes`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#all-nodes).

## Entry membership in a treap tree

A key $k$, value $v$ and priority $p$ form an entry
of a treap tree when some node stores exactly $k$, $v$ and $p$: the empty tree has no
entries, and $(k, v, p)$ is an entry of a node with left subtree $L$, root key $r$, root value
$w$, root priority $q$ and right subtree $R$ exactly when it is an entry of $L$, or $k = r$,
$v = w$ and $p = q$, or it is an entry of $R$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.MemNode`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#mem-node).

## Key membership in a treap tree

A key $k$ is a key of a treap tree when it is stored
at some node: no key belongs to the empty tree, and $k$ belongs to a node with left subtree
$L$, root key $r$ and right subtree $R$ exactly when $k$ belongs to $L$, or $k = r$, or $k$
belongs to $R$.

Membership is structural and does not assume the search-tree or heap invariants.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.MemKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#mem-key).

## Treap inorder traversal onto a suffix

For a tree $t$ and a list $s$ of key-value pairs,
the traversal of $t$ onto $s$ is defined by recursion: for the empty tree it is $s$, and for a
node with left subtree $l$, key $k$, value $v$ and right subtree $r$ it is the traversal of $l$
onto the list obtained by putting $(k, v)$ in front of the traversal of $r$ onto $s$. The result
is the key-value pairs of $t$ in inorder, priorities dropped, followed by $s$.

No ancestor recopies a completed traversal, so the traversal takes linear time.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.contentsAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#contents-aux).

## Treap inorder contents

The contents of a tree $t$ is the list of its key-value pairs in
inorder (left subtree, then node, then right subtree), with priorities dropped. It is defined as
the inorder traversal of $t$ onto the empty list, which takes linear time.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.contents`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#contents).

## Treap inorder contents of a node

For trees $l$ and $r$, a key $k$, a value $v$ and a
natural-number priority $n$, the inorder list of key-value pairs of the node with left subtree
$l$, key $k$, value $v$, priority $n$ and right subtree $r$ is the inorder list of $l$, followed
by $(k, v)$, followed by the inorder list of $r$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.contents_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#contents-node).

## Size of a treap tree

The size of a tree is its number of nodes, computed recursively:
the empty tree has size $0$, and a node with left subtree $L$ and right subtree $R$ has size
equal to the size of $L$ plus one plus the size of $R$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.size`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#size).

## Ordered treap tree

For a key type equipped with a relation $<$, a treap tree is
ordered when it is empty, or when it is a node with key $k$ whose left and right subtrees are
both ordered, every key $x$ in the left subtree satisfies $x < k$, and every key $y$ in the
right subtree satisfies $k < y$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#ordered).

## Heap order of treap priorities

A tree is heap-ordered when the priority of every
node is at most the priority of every node below it. Recursively, the empty tree is
heap-ordered, and a node with priority $p$ is heap-ordered when its left and right subtrees
are heap-ordered and every node in them has priority at least $p$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.HeapOrdered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#heap-ordered).

## Valid treap

A binary tree whose nodes each carry a key, a value and a natural-number
priority, with keys compared by a relation $<$ (any `LT` instance; no order axioms are
assumed), is a valid treap when it satisfies both of the following at every node: every key in
the left subtree is less than the node's key and the node's key is less than every key in the
right subtree (search-tree order with respect to $<$), and the node's priority is at most the
priority of every node in its left and right subtrees (min-heap order on priorities).

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#valid).

## Treap lookup

Looking up a key $k$ in a tree with keys in a linearly ordered type follows
the binary search tree comparisons. The empty tree gives no value. At a node with key $r$ and
value $v$, the lookup continues in the left subtree if $k < r$, continues in the right subtree
if $r < k$, and otherwise returns $v$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookup`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup).

## Lookup with cost

The costed lookup of a key $k$ in a tree with keys in a linearly
ordered type returns a possibly absent value together with a natural number counting the
visited nodes. On the empty tree it returns no value and cost $0$. At a node with key $r$ and
value $v$, if $k < r$ it returns the result of the costed lookup of $k$ in the left subtree
with cost increased by $1$; if $r < k$ it does the same with the right subtree; otherwise it
returns $v$ with cost $1$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookupWithCost`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup-with-cost).

## Root priority of a treap tree

The root priority of a treap tree is an optional
natural number: it is absent for the empty tree, and for a node it is the priority stored at
that node.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.rootPriority`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#root-priority).

## Treap merge

The merge of two treap trees is defined recursively. Merging the empty
tree with a tree $T$, or $T$ with the empty tree, gives $T$. If both trees are nodes, with
root priorities $p$ for the first and $q$ for the second, then when $p \le q$ the result keeps
the root of the first tree and its left subtree, and its right subtree is the merge of the
first tree's right subtree with the second tree; otherwise the result keeps the root of the
second tree and its right subtree, and its left subtree is the merge of the first tree with
the second tree's left subtree.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.merge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#merge).

## Result of a treap split

For key type $\kappa$ and value type $\nu$, a split result
consists of a lower tree, an optional entry given by a value in $\nu$ together with a
natural-number priority, and an upper tree, where both trees are treap trees with keys in
$\kappa$ and values in $\nu$.

The structure imposes no constraint; on an ordered tree, splitting at a pivot fills the lower
tree with the keys below the pivot, the upper tree with the keys above it, and the entry with
the pivot's value and priority when the pivot occurs.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.SplitResult`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#split-result).

## Treap split

Let the keys come from a linear order, and write $(L, k, v, q, R)$ for the
node with left subtree $L$, key $k$, value $v$, priority $q$ and right subtree $R$. Splitting
a tree at a pivot $p$ returns a split result, defined by recursion on the tree. The empty tree
splits into two empty trees and no entry. For a node $(L, k, v, q, R)$: if $k < p$, split $R$
at $p$ into a lower tree $R_1$, an optional entry $e$ and an upper tree $R_2$, and return the
lower tree $(L, k, v, q, R_1)$, the entry $e$ and the upper tree $R_2$; if $p < k$, split $L$
at $p$ into $L_1$, $e$ and $L_2$, and return the lower tree $L_1$, the entry $e$ and the upper
tree $(L_2, k, v, q, R)$; otherwise $k = p$, and return the lower tree $L$, the entry
$(v, q)$ and the upper tree $R$.

On an ordered tree, the lower tree holds the keys below $p$, the upper tree holds the keys
above $p$, and the entry is the value and priority stored at $p$ when $p$ occurs.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.split`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#split).

## Treap insertion

For a key $k$ of a linearly ordered key type, a value $v$, a priority
$p$ and a tree $t$, inserting $k$ with value $v$ and priority $p$ into $t$ splits $t$ at $k$,
drops the entry the split finds at $k$ if any, merges the part below $k$ with the single node
$(k, v, p)$, and then merges the result with the part above $k$; all merges are
priority-guided.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#insert).

## Treap deletion

For a key $k$ of a linearly ordered key type and a tree $t$, deleting
$k$ from $t$ splits $t$ at $k$ and returns the priority-guided merge of the part of the split
below $k$ with the part above $k$; the entry the split finds at $k$, if any, is dropped.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.erase`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#erase).

## Treap all-nodes predicate via node membership

Let $p$ be a predicate on a key, a value
and a natural-number priority, and let $t$ be a tree. Then $p$ holds at every node of $t$ if and
only if $p(k, v, n)$ holds for every key $k$, value $v$ and priority $n$ such that the entry
$(k, v, n)$ occurs as a node of $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.allNodes_iff_forall_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#all-nodes-iff-forall-mem).

## Entry membership implies key membership in a treap

If a key $k$, value $v$ and
priority $p$ form an entry of a treap tree $t$, that is, some node of $t$ stores exactly $k$,
$v$ and $p$, then $k$ is a key of $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.memKey_of_memNode`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#mem-key-of-mem-node).

## Inorder contents list the treap's entries

For every tree $t$, key $k$ and value $v$,
the pair $(k, v)$ occurs in the inorder key-value list of $t$ if and only if $t$ has a node
with key $k$ and value $v$, for some priority.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.mem_contents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#mem-contents).

## Keys occurring in the inorder contents

For a key $k$ and a tree $t$, some pair
$(k, v)$ occurs in the inorder list of key-value pairs of $t$ if and only if $k$ is the key
of some node of $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.key_mem_contents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#key-mem-contents).

## Treap all-nodes predicate on keys via key membership

Let $p$ be a predicate on keys and
let $t$ be a tree. Then the key of every node of $t$ satisfies $p$ if and only if $p(k)$ holds
for every key $k$ that occurs in $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.allNodes_key_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#all-nodes-key-iff).

## Inorder key list of a treap

The inorder key list of a tree $t$ is the list of first
components of the inorder list of key-value pairs of $t$, that is, the keys of $t$ in
inorder.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.keys`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#keys).

## Inorder keys of a node

For trees $l$ and $r$, a key $k$, a value $v$ and a priority
$p$, the inorder key list of the node with left subtree $l$, entry $(k, v, p)$ and right
subtree $r$ is the inorder key list of $l$, followed by $k$, followed by the inorder key list
of $r$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.keys_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#keys-node).

## The inorder key list lists exactly the keys of a treap

For every treap tree $t$ and
key $k$, $k$ occurs in the inorder key list of $t$ if and only if $k$ is a key of $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.mem_keys`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#mem-keys).

## Inorder keys of an ordered treap are strictly increasing

Let the keys come from a
linearly ordered type. If a treap tree $t$ is ordered, then its inorder key list is strictly
increasing: each key in the list is smaller than every key after it.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.ordered_keys`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#ordered-keys).

## Treap keys are distinct

For a linearly ordered key type, if a tree is ordered as a
binary search tree (at every node, every key in the left subtree is smaller and every key in
the right subtree is larger than the node's key), then its inorder key list has no
duplicates.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.keys_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#keys-nodup).

## Treap lookup finds exactly the stored entries

Let $t$ be a tree with keys in a linearly
ordered type that is ordered as a binary search tree (every key in a left subtree is smaller and
every key in a right subtree is larger than the node's key). For every key $k$ and value $v$,
looking up $k$ in $t$ returns $v$ if and only if $t$ has a node with key $k$ and value $v$, for
some priority.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookup_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup-eq-some-iff).

## Treap lookup agrees with the inorder contents

Let $t$ be a tree with keys in a linearly
ordered type that is ordered as a binary search tree (every key in a left subtree is smaller and
every key in a right subtree is larger than the node's key). For every key $k$ and value $v$,
looking up $k$ in $t$ returns $v$ if and only if the pair $(k, v)$ occurs in the inorder
key-value list of $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookup_contents`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup-contents).

## Costed lookup returns the ordinary lookup result

For every tree $t$ with keys in a
linearly ordered type and every key $k$, the value component of the costed lookup of $k$ in $t$
(ignoring the visit count) equals the result of looking up $k$ in $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookupWithCost_result`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup-with-cost-result).

## Lookup cost is at most the tree size

For every tree $t$ with keys in a linearly ordered
type and every key $k$, the number of nodes visited by the costed lookup of $k$ in $t$ is at most
the number of nodes of $t$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookupWithCost_le_size`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup-with-cost-le-size).

## The root of a heap-ordered tree has minimal priority

If a nonempty tree whose root
has priority $p$ is heap-ordered, then every node of the tree, the root included, has
priority at least $p$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.heap_root_min`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#heap-root-min).

## Keys of a merged treap

For all trees $l$ and $r$ and every key $k$, $k$ is the key of
some node of the merge of $l$ and $r$ if and only if $k$ is the key of some node of $l$ or of
some node of $r$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.memKey_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#mem-key-merge).

## Treap merge concatenates inorder contents

For trees $l$ and $r$, the inorder list of
key-value pairs of the priority-guided merge of $l$ and $r$ is the inorder list of $l$ followed
by the inorder list of $r$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.contents_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#contents-merge).

## Separated treap trees

For keys equipped with a binary relation $<$, two trees $L$
and $R$ are separated when $a < b$ for every key $a$ occurring at a node of $L$ and every
key $b$ occurring at a node of $R$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.Separated`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#separated).

## Treap merge preserves search-tree order

Let the keys come from a linearly ordered
type. If treap trees $L$ and $R$ are both ordered and every key of $L$ is smaller than every
key of $R$, then the merge of $L$ and $R$ is ordered.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.ordered_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#ordered-merge).

## Merging preserves heap order

If two trees $l$ and $r$ are both heap-ordered in their
priorities, then the priority-guided merge of $l$ and $r$ is heap-ordered.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.heapOrdered_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#heap-ordered-merge).

## Treap split preserves search-tree order

Let the keys come from a linearly ordered
type and let $t$ be an ordered treap tree. For every pivot key $k$, the lower tree and the
upper tree produced by splitting $t$ at $k$ are both ordered.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.ordered_split`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#ordered-split).

## Treap split preserves heap order

Let the keys come from a linearly ordered type and let
$t$ be a heap-ordered treap tree. For every pivot key $k$, the lower tree and the upper tree
produced by splitting $t$ at $k$ are both heap-ordered.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.heapOrdered_split`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#heap-ordered-split).

## Split bounds for an ordered treap

Let the keys come from a linear order and let $T$ be
an ordered tree. For every pivot $p$, every key of the lower tree obtained by splitting $T$ at
$p$ is strictly less than $p$, and every key of the upper tree is strictly greater than $p$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.split_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#split-bounds).

## Splitting a treap preserves validity

Let the keys come from a linear order. If a tree
is a valid treap, then for every pivot $p$, both the lower tree and the upper tree obtained by
splitting it at $p$ are valid treaps.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.valid_split`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#valid-split).

## Merging separated treaps preserves validity

Let the keys come from a linear order. If
$L$ and $R$ are valid treaps and every key of $L$ is strictly less than every key of $R$, then
the merge of $L$ and $R$ is a valid treap.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.valid_merge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 656](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L656). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#valid-merge).

## Inserting into a treap preserves validity

Let the keys come from a linear order. If a
tree is a valid treap, that is, its keys are in strict binary-search-tree order and its
priorities are in min-heap order, then for every key $k$, value $v$ and natural-number
priority $q$, the tree obtained by inserting $k$ with value $v$ and priority $q$ is again a
valid treap.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#valid-insert).

## Erasing from a treap preserves validity

Let the keys come from a linear order. If a
tree is a valid treap, that is, its keys are in strict binary-search-tree order and its
priorities are in min-heap order, then for every key $k$ the tree obtained by erasing $k$ from
it is again a valid treap.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.valid_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#valid-erase).

## Treap inorder contents split at a pivot

Let the keys come from a linearly ordered type,
let $t$ be a tree and $k$ a pivot key, and let splitting $t$ at $k$ produce a lower tree $L$, an
optional value-priority pair found at $k$, and an upper tree $G$. Then the inorder list of
key-value pairs of $t$ is the inorder list of $L$, followed by $(k, v)$ if the split found a pair
with value $v$ (and by nothing if it found none), followed by the inorder list of $G$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.contents_split`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#contents-split).

## Treap inorder contents after insertion

Let the keys come from a linearly ordered type,
let $t$ be a tree, $k$ a key, $v$ a value and $n$ a natural-number priority, and let $L$ and $G$
be the lower and upper trees produced by splitting $t$ at $k$. Then the inorder list of key-value
pairs of the tree obtained by inserting $k$ with value $v$ and priority $n$ into $t$ is the
inorder list of $L$, followed by $(k, v)$, followed by the inorder list of $G$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.contents_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 731](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L731). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#contents-insert).

## Treap inorder contents after erasure

Let the keys come from a linearly ordered type, let
$t$ be a tree and $k$ a key, and let $L$ and $G$ be the lower and upper trees produced by
splitting $t$ at $k$. Then the inorder list of key-value pairs of the tree obtained by erasing
$k$ from $t$ is the inorder list of $L$ followed by the inorder list of $G$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.contents_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#contents-erase).

## Treap lookup after insertion

Let $t$ be a valid treap with keys in a linearly ordered
type, that is, $t$ is ordered as a binary search tree by key and as a min-heap by priority. For
every key $k$, value $v$ and priority $p \in \mathbb{N}$, looking up $k$ in the tree obtained by
inserting $k$ with value $v$ and priority $p$ into $t$ returns $v$.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookup_insert_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 747](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L747). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup-insert-eq).

## Erased keys are not found

Let $t$ be a valid treap with keys in a linearly ordered type,
that is, $t$ is ordered as a binary search tree by key and as a min-heap by priority. For every
key $k$, looking up $k$ in the tree obtained by erasing $k$ from $t$ returns no value.

Formalized by `Cslib.Algorithms.Lean.Treap.Tree.lookup_erase_eq_none`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/Treap.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/Treap.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html#lookup-erase-eq-none).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Treap](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/treap/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/search-trees/treap)
