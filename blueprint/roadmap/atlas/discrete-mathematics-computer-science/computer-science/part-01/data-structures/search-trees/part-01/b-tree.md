---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BTree, Cslib.Algorithms.Lean.BTree.flattenAux, Cslib.Algorithms.Lean.BTree.flatten, Cslib.Algorithms.Lean.BTree.flattenAux_eq, Cslib.Algorithms.Lean.BTree.flatten_node_nil_cons, Cslib.Algorithms.Lean.BTree.flatten_node_cons_nil, Cslib.Algorithms.Lean.BTree.flatten_node_nil_nil, Cslib.Algorithms.Lean.BTree.flatten_node_append_cons
statement: formalized
proof: formalized
---

# B-tree

72 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html).

## Raw B-trees

A raw B-tree with keys in a type $\alpha$ is either a leaf, holding a list
of keys, or an internal node, holding a list of separator keys and a list of child raw B-trees.
The type imposes no invariant: that an internal node with $k$ keys has $k + 1$ children, the
bounds on key counts, the balance of the tree and the ordering of the keys are imposed
separately by the structural and ordering invariants of B-trees.

Formalized by `Cslib.Algorithms.Lean.BTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#btree).

## Accumulating flattening of a B-tree

Given a raw B-tree $T$ and a list $s$, this returns
the inorder traversal of $T$ followed by $s$. For a leaf it is the leaf's key list followed by
$s$. For an internal node with separator keys $k_1, \dots, k_m$ and children $c_0, \dots, c_n$
it is the sequence $c_0, k_1, c_1, k_2, \dots$, in which children and keys alternate starting
with a child until one of the two lists runs out, then the remaining keys or children in
order, and finally $s$; each key contributes itself, and each child contributes its own
accumulating flattening with everything after it as the suffix. In particular every key of
the tree occurs in the result.

The result is built from right to left, so each key is copied only once.

Formalized by `Cslib.Algorithms.Lean.BTree.flattenAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-aux).

## Inorder flattening of a B-tree

The flattening of a raw B-tree is the list of its keys
defined recursively: for a leaf it is the leaf's key list, and for an internal node with keys
$k_1, k_2, \dots$ and children $c_1, c_2, \dots$ it is the flattening of $c_1$, then $k_1$, then
the flattening of $c_2$, then $k_2$, and so on, alternating while both lists last; whatever
remains of the longer list is then appended in order, each surplus child contributing its
flattening and each surplus key contributing itself. In particular every key of the tree occurs
in the flattening.

The flattening is computed in linear time by an accumulator-passing auxiliary function.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten).

## The accumulating B-tree flattening is correct

For every raw B-tree $T$ and every list
$s$, the accumulating flattening of $T$ with suffix $s$ equals the inorder flattening of $T$
followed by $s$.

Formalized by `Cslib.Algorithms.Lean.BTree.flattenAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-aux-eq).

## Flattening a keyless node, one child at a time

For a raw B-tree $c$ and a list $C$ of
raw B-trees, the flattening of the node with no keys and child list $c$ followed by $C$ is the
flattening of $c$ followed by the flattening of the node with no keys and child list $C$.

This covers nodes with more children than a well-formed node would have.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_node_nil_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-node-nil-cons).

## Flattening a childless node, one key at a time

For a key $k$ and a list of keys $K$, the
flattening of the node with key list $k$ followed by $K$ and no children is $k$ followed by the
flattening of the node with key list $K$ and no children.

This covers nodes with more keys than a well-formed node would have.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_node_cons_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-node-cons-nil).

## Flattening of the empty node

The flattening of the internal node with no keys and no
children is the empty list.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_node_nil_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-node-nil-nil).

## Splitting a node's flattening at a separator

Let $K_1$ and $K_2$ be lists of keys, $m$ a
key, and $C_1$ and $C_2$ lists of raw B-trees such that $C_1$ has exactly one more element than
$K_1$. Then the flattening of the node whose key list is $K_1$ followed by $m$ followed by $K_2$
and whose child list is $C_1$ followed by $C_2$ equals the flattening of the node with keys $K_1$
and children $C_1$, followed by $m$, followed by the flattening of the node with keys $K_2$ and
children $C_2$.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_node_append_cons`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-node-append-cons).

## Membership in a B-tree

A key $x$ belongs to a tree $T$ when $x$ occurs in the inorder
flattening of $T$.

Structurally, a key belongs to an internal node exactly when it is one of the node's separator
keys or belongs to one of its children.

Formalized by `Cslib.Algorithms.Lean.BTree.Mem`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#mem).

## Ordered B-tree

A B-tree over a type with a relation $<$ is ordered when its inorder
flattening is strictly increasing, that is, each key of the flattening is less than every
key that comes after it. This single condition packages sortedness of the keys at each node
and the separator bounds between a node's keys and the keys stored in its subtrees.

Formalized by `Cslib.Algorithms.Lean.BTree.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#ordered).

## The separator keys of an ordered node are sorted

If an internal node with separator list
$K$ is ordered, then $K$ is strictly increasing: every key of $K$ is smaller than every key that
comes after it in $K$.

Formalized by `Cslib.Algorithms.Lean.BTree.Ordered.node_keys_pairwise`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#node-keys-pairwise).

## Separator bounds in an ordered B-tree node

Let $K_1$ and $K_2$ be lists of keys,
$k$ a key, and $C_1$ and $C_2$ lists of B-trees such that $C_1$ has exactly one more tree
than $K_1$ has keys. If the internal node whose key list is $K_1$ followed by $k$ followed
by $K_2$, and whose child list is $C_1$ followed by $C_2$, is ordered, then every key in the
flattening of the node with keys $K_1$ and children $C_1$ is less than $k$, and $k$ is less
than every key in the flattening of the node with keys $K_2$ and children $C_2$.

Here the last tree of $C_1$ is the subtree immediately left of $k$ and the first tree of
$C_2$ the one immediately right of it; in particular, every key in a child of an ordered
node lies strictly between the separators adjacent to it.

Formalized by `Cslib.Algorithms.Lean.BTree.Ordered.separator_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#separator-bounds).

## An ordered B-tree has no duplicate keys

For a linearly ordered key type, the flattening
of an ordered raw B-tree has no duplicate entries.

Formalized by `Cslib.Algorithms.Lean.BTree.Ordered.flatten_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-nodup).

## Structural invariant of a B-tree

For a minimum degree $t$ and a minimum key count $m$
for the top node, the invariant is defined inductively over the height: a leaf with $k$ keys
satisfies it at height $0$ when $m \le k \le 2t - 1$, and for every natural number $h$, an
internal node with $k$ keys satisfies it at height $h + 1$ when $m \le k \le 2t - 1$, the
node has exactly $k + 1$ children, and every child satisfies the invariant with minimum key
count $t - 1$ at height $h$. Here $2t - 1$ and $t - 1$ are truncated at $0$.

Consequently all leaves of a valid tree sit at the same depth, every node has at most
$2t - 1$ keys, and every node other than the top one has at least $t - 1$ keys. Non-root
trees are used with $m = t - 1$; the root of a B-tree satisfies the root invariant instead.

Formalized by `Cslib.Algorithms.Lean.BTree.Valid`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#valid).

## Root invariant of a B-tree

For a minimum degree $t$ and a height $h$, a tree
satisfies the root invariant when either $h = 0$ and the tree is a leaf with at most
$2t - 1$ keys (possibly none, for the empty tree), or $h = h' + 1$ and the tree is an
internal node with between $1$ and $2t - 1$ keys and exactly one more child than keys,
every child satisfying the structural invariant for minimum degree $t$, minimum top-node
key count $t - 1$ and height $h'$. Here $2t - 1$ and $t - 1$ are truncated at $0$.

Formalized by `Cslib.Algorithms.Lean.BTree.ValidRoot`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#valid-root).

## Root-valid B-trees are valid

If a tree satisfies the root invariant for minimum
degree $t$ at height $h$, then for some natural number $m$ it satisfies the structural
invariant for minimum degree $t$, minimum top-node key count $m$ and height $h$.

Formalized by `Cslib.Algorithms.Lean.BTree.ValidRoot.valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#valid-2).

## B-tree search

For a linearly ordered key type, the search for a key $x$ in a raw B-tree
proceeds as follows. At a leaf, report whether $x$ is in the leaf's key list. At an internal
node with separators $k_1, \dots, k_m$ and children $c_0, c_1, \dots$, scan the separators in
order. On reaching $k_i$, report failure if the node has no child $c_{i-1}$; otherwise search
$c_{i-1}$ if $x < k_i$, report success if $x = k_i$, and move on to the next separator if
$k_i < x$. If every separator is less than $x$, search the child $c_m$, or report failure if
the node has no such child.

Formalized by `Cslib.Algorithms.Lean.BTree.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#contains).

## Result of inserting into a B-tree subtree

An insertion result over a key type $\alpha$
is either a single tree over $\alpha$, or a triple $(\ell, m, r)$ of two trees $\ell$ and $r$
over $\alpha$ and a key $m$ of $\alpha$. In insertion, the first form is a subtree that did not
split, and the second form is an overflowing node split into two trees of the same height, with
the median key $m$ promoted between them; the type itself does not record heights.

Formalized by `Cslib.Algorithms.Lean.BTree.InsResult`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#ins-result).

## Flattening of a B-tree insertion result

The flattening of an insertion result that is a
single tree is the flattening of that tree; for a result that splits into a left tree $\ell$, a
promoted median key $m$ and a right tree $r$, it is the flattening of $\ell$, followed by $m$,
followed by the flattening of $r$.

Formalized by `Cslib.Algorithms.Lean.BTree.grownFlatten`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#grown-flatten).

## Insertion into a B-tree leaf

Over a linearly ordered key type, let $t$ be a natural
number, $x$ a key, $K$ the key list of a leaf, and $K'$ the result of ordered insertion of $x$
into $K$. If $K'$ has at most $2t - 1$ keys, the insertion result is the single leaf with keys
$K'$. Otherwise the leaf is split: the result consists of the leaf holding the first $t - 1$ keys
of $K'$, the next key of $K'$ promoted as the median, and the leaf holding the remaining keys.
Here subtraction of natural numbers is truncated at $0$.

Formalized by `Cslib.Algorithms.Lean.BTree.insLeaf`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 670](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L670). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#ins-leaf).

## Splitting a B-tree node

Let $t$ be a minimum degree, $s = t - 1$ (so $s = 0$ when
$t = 0$), $k_1, \dots, k_m$ a list of keys and $c_1, \dots, c_n$ a list of B-trees. If
$m > s$, splitting returns the pair of internal nodes formed by the keys $k_1, \dots, k_s$
with the first $t$ children (all of them if $n < t$) and by the keys $k_{s+2}, \dots, k_m$
with the children after the first $t$, together with the key $k_{s+1}$ promoted between
them. If $m \le s$, it returns the single internal node with keys $k_1, \dots, k_m$ and
children $c_1, \dots, c_n$ unchanged.

On an overfull node with $2t$ keys and $t \ge 1$, the promoted key $k_t$ is the median key.

Formalized by `Cslib.Algorithms.Lean.BTree.splitNode`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#split-node).

## Rebuilding an internal node after insertion

For minimum degree $t$, a separator list $K$
and a child list $C$, the result is the internal node with separators $K$ and children $C$, kept
as a single tree when $K$ has at most $2t - 1$ keys, and otherwise split by node splitting into
two nodes and a promoted median key.

Formalized by `Cslib.Algorithms.Lean.BTree.mkNode`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#mk-node).

## Split-returning insertion into a B-tree subtree

For minimum degree $t$ and a key $x$,
insertion of $x$ into a tree returns an insertion result and is defined by recursion. At a leaf
with key list $K$, it is leaf insertion of $x$ into $K$. At an internal node, the separator list
and the child list are scanned together from the left. If $x$ is smaller than the current
separator, or no separator is left but a child is, $x$ is inserted into the current child. If $x$
is larger than the current separator, the scan moves on to the next separator and child. If $x$
equals the current separator, or no child is left, the remaining lists are kept unchanged. When
the child that received $x$ returns a single tree, that tree replaces the child; when it returns
two trees $\ell$, $r$ with a median $m$, the child is replaced by $\ell$ and $r$ with $m$ inserted
as a separator between them. The rebuilt separator and child lists are then turned into a node by
the internal-node rebuilding step: kept as one node if there are at most $2t - 1$ separators, and
split otherwise.

Formalized by `Cslib.Algorithms.Lean.BTree.ins`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#ins).

## B-tree insertion

For minimum degree $t$, the tree obtained by inserting a key $x$ into a
tree $T$ is computed from the split-returning insertion of $x$ into $T$: if that returns a single
tree, this tree is the result; if it returns two trees $\ell$ and $r$ with a promoted median key
$m$, the result is a new root node with the single separator $m$ and the two children $\ell$ and
$r$.

When $T$ is a B-tree of minimum degree $t$, inserting a key already present in $T$ returns a tree
with the same flattening.

Formalized by `Cslib.Algorithms.Lean.BTree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#insert).

## The empty B-tree

The empty B-tree is the leaf with no keys.

Formalized by `Cslib.Algorithms.Lean.BTree.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#empty).

## B-trees of a given minimum degree

A tree $T$ is a B-tree of minimum degree $t$ when
$t \ge 2$ (the CLRS Chapter 18 minimum-degree requirement), $T$ is ordered, and $T$ is
root-valid at some height. This is the invariant preserved by insertion and by building a tree
from a list.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#is-btree).

## The minimum degree of a B-tree is at least two

If a tree is a B-tree of minimum
degree $t$, then $t \ge 2$.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.two_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#two-le).

## B-trees are ordered

If a tree is a B-tree of minimum degree $t$, then it is ordered:
each key of its inorder flattening is less than every key that comes after it.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.ordered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#ordered-2).

## B-trees satisfy the root invariant

If $T$ is a B-tree of minimum degree $t$, then there
is a height $h$ such that $T$ satisfies the root structural invariant of minimum degree $t$ at
height $h$.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.exists_validRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#exists-valid-root).

## The empty tree is a B-tree

For every key type equipped with a binary relation $<$ and
every natural number $t \ge 2$, the empty B-tree is a B-tree of minimum degree $t$.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#empty-2).

## B-tree insertion as sorted list insertion

Let $\alpha$ be linearly ordered, let
$t \ge 2$, and let $T$ be a B-tree of minimum degree $t$ with keys in $\alpha$. For every key
$x \in \alpha$, the inorder flattening of the tree obtained by inserting $x$ into $T$ with
minimum degree $t$ equals the sorted insertion of $x$ into the inorder flattening of $T$.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-insert).

## Membership after B-tree insertion

Let $t \ge 2$ and let $T$ be a B-tree of minimum
degree $t$ over a linearly ordered key type. For all keys $x$ and $y$, $y$ belongs to the tree
obtained by inserting $x$ into $T$ if and only if $y = x$ or $y$ belongs to $T$.

Formalized by `Cslib.Algorithms.Lean.BTree.mem_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#mem-insert).

## Insertion preserves the B-tree invariant

Let $t \ge 2$ and let the keys come from a
linearly ordered type. If $T$ is a B-tree of minimum degree $t$, then for every key $x$ the tree
obtained by inserting $x$ into $T$ is again a B-tree of minimum degree $t$: it is ordered and
root-valid at some height.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#insert-2).

## Correctness of B-tree search

Let $\alpha$ be linearly ordered and let $T$ be a B-tree
of minimum degree $t$ with keys in $\alpha$. For every key $x \in \alpha$, the search procedure
returns true on $x$ and $T$ if and only if $x$ is a member of $T$, that is, $x$ occurs in the
inorder flattening of $T$.

Formalized by `Cslib.Algorithms.Lean.BTree.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#contains-eq-true-iff).

## Size of a B-tree after insertion

Let $\alpha$ be linearly ordered, let $t \ge 2$, let
$T$ be a B-tree of minimum degree $t$ with keys in $\alpha$, and let $x \in \alpha$. Let $T'$ be
the tree obtained by inserting $x$ into $T$ with minimum degree $t$. If $x$ occurs in the
inorder flattening of $T$, then the flattening of $T'$ has the same length as that of $T$;
otherwise it is one longer.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_length_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-length-insert).

## B-tree built from a list

For a linearly ordered key type and a natural number $t$, the
tree built from the empty list is the empty tree, and the tree built from a list with head $x$
and tail $L$ is the result of inserting $x$, with minimum degree $t$, into the tree built from
$L$. Thus the elements are inserted from right to left.

Formalized by `Cslib.Algorithms.Lean.BTree.fromList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#from-list).

## Building from a list yields a B-tree

For a linearly ordered key type, every natural
number $t \ge 2$ and every list $L$ of keys, the tree obtained by inserting the elements of $L$
from right to left into the empty tree, each insertion with minimum degree $t$, is a B-tree of
minimum degree $t$.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#from-list-2).

## Membership in a B-tree built from a list

Let $t \ge 2$ and let $xs$ be a list over a
linearly ordered key type. A key $x$ belongs to the tree of minimum degree $t$ built from $xs$
(by inserting the elements of $xs$ into the empty tree, from right to left) if and only if $x$
is an element of $xs$.

Formalized by `Cslib.Algorithms.Lean.BTree.mem_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree.lean, line 1284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree.lean#L1284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#mem-from-list).

## Building a B-tree from a strictly increasing list

Let $t \ge 2$. For every strictly
increasing list $L$ of keys, the tree built from $L$ by inserting its keys from right to left
into the empty tree with minimum degree $t$ has flattening exactly $L$.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_fromList_of_pairwise`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-from-list-of-pairwise).

## B-tree deletion by rebuilding

For a minimum degree $t$, a key $x$ and a tree $T$, the
rebuilding deletion of $x$ from $T$ is the tree obtained by inserting the keys of the list $L$,
from right to left, into the empty tree with B-tree insertion of minimum degree $t$, where $L$ is
the inorder flattening of $T$ with the first occurrence of $x$ removed ($L$ is the flattening
itself when $x$ does not occur in it).

This is a reference implementation, not the single-pass borrow-and-merge deletion of CLRS
Section 18.3, which is formalized separately.

Formalized by `Cslib.Algorithms.Lean.BTree.deleteRebuild`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete-rebuild).

## Rebuilding deletion unfolds to erase and rebuild

For every minimum degree $t$, key $x$
and tree $T$, the rebuilding deletion of $x$ from $T$ with minimum degree $t$ equals the tree
built from the list obtained by removing the first occurrence of $x$ from the flattening of $T$,
by inserting its keys from right to left into the empty tree with minimum degree $t$.

Formalized by `Cslib.Algorithms.Lean.BTree.deleteRebuild_eq_fromList_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete-rebuild-eq-from-list-erase).

## Flattening after rebuilding deletion

Let $t \ge 2$, let $T$ be an ordered tree and let
$x$ be a key. The flattening of the rebuilding deletion of $x$ from $T$ with minimum degree $t$
is the flattening of $T$ with the first occurrence of $x$ removed (unchanged if $x$ does not
occur).

No occupancy hypothesis on $T$ is needed.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_deleteRebuild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-delete-rebuild).

## Rebuilding deletion yields a B-tree

Let $t \ge 2$. For every key $x$ and every tree $T$,
whether or not $T$ is itself a B-tree, the rebuilding deletion of $x$ from $T$ with minimum
degree $t$ is a B-tree of minimum degree $t$.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.deleteRebuild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete-rebuild-2).

## Rebuild deletion yields an ordered tree

Let $t \ge 2$ and let keys come from a linearly
ordered type. For every key $x$ and every tree $T$, not necessarily ordered, the tree obtained
from $T$ by rebuild deletion of $x$ (removing the first occurrence of $x$, if any, from the
inorder flattening of $T$ and rebuilding a B-tree of minimum degree $t$ from the remaining keys)
is ordered: its inorder flattening is strictly increasing.

Formalized by `Cslib.Algorithms.Lean.BTree.ordered_deleteRebuild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#ordered-delete-rebuild).

## Rebuilding deletion yields a root-valid tree

Let $t \ge 2$. For every key $x$ and every
tree $T$, there is a height $h$ such that the rebuilding deletion of $x$ from $T$ with minimum
degree $t$ is root-valid of minimum degree $t$ and height $h$: all leaves sit at depth $h$, every
node holds at most $2t - 1$ keys, every non-root node holds at least $t - 1$ keys, an internal
root holds at least one key, and an internal node with $k$ keys has $k + 1$ children.

No relation between $h$ and the height of $T$ is claimed.

Formalized by `Cslib.Algorithms.Lean.BTree.deleteRebuild_validRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete-rebuild-valid-root).

## Membership after rebuild deletion from a B-tree

Let $t \ge 2$ and let $T$ be a B-tree of
minimum degree $t$ with keys in a linearly ordered type. For all keys $x$ and $y$, the key $y$
lies in the tree obtained from $T$ by rebuild deletion of $x$ (erasing $x$ from the inorder
flattening of $T$ and rebuilding a B-tree of minimum degree $t$ from the remaining keys) if and
only if $y \ne x$ and $y$ lies in $T$.

Formalized by `Cslib.Algorithms.Lean.BTree.mem_deleteRebuild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#mem-delete-rebuild).

## The deleted key is absent after rebuild deletion

Let $t \ge 2$ and let $T$ be a B-tree of
minimum degree $t$ with keys in a linearly ordered type. For every key $x$, the tree obtained
from $T$ by rebuild deletion of $x$ (erasing $x$ from the inorder flattening of $T$ and
rebuilding a B-tree of minimum degree $t$ from the remaining keys) does not contain $x$.

Formalized by `Cslib.Algorithms.Lean.BTree.not_mem_deleteRebuild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#not-mem-delete-rebuild).

## Search after rebuilding deletion

Let $t \ge 2$, let $T$ be a B-tree of minimum degree
$t$, and let $x$ and $y$ be keys. The B-tree search for $y$ in the rebuilding deletion of $x$
from $T$ with minimum degree $t$ returns true if and only if $y \ne x$ and $y$ is stored in $T$.

Formalized by `Cslib.Algorithms.Lean.BTree.contains_deleteRebuild_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#contains-delete-rebuild-iff).

## Rebuilding deletion of an absent key

Let $t \ge 2$, let $T$ be an ordered tree and let
$x$ be a key that does not occur in the flattening of $T$. Then the rebuilding deletion of $x$
from $T$ with minimum degree $t$ has the same flattening as $T$.

The tree itself may be rebuilt to a different shape with the same flattening.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_deleteRebuild_of_not_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-delete-rebuild-of-not-mem).

## Key count after rebuilding deletion

Let $t \ge 2$, let $T$ be an ordered tree with
flattening of length $n$, and let $x$ be a key. The flattening of the rebuilding deletion of $x$
from $T$ with minimum degree $t$ has length $n - 1$ if $x$ occurs in the flattening of $T$, and
length $n$ otherwise.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_length_deleteRebuild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-length-delete-rebuild).

## Rebuilding deletion of the same key twice

Let $t \ge 2$, let $T$ be an ordered tree (its
flattening is strictly increasing) and let $x$ be a key. Deleting $x$ twice by rebuilding with
minimum degree $t$ gives a tree with the same flattening as deleting $x$ once.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_deleteRebuild_deleteRebuild`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/Delete.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-delete-rebuild-delete-rebuild).

## Number of keys at the root of a B-tree

For a raw B-tree $T$, this is the length of the
key list stored at the root of $T$: the number of keys of $T$ if $T$ is a leaf, and the number of
separator keys of $T$ if $T$ is an internal node. Keys in the children are not counted.

Formalized by `Cslib.Algorithms.Lean.BTree.keyCount`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#key-count).

## Splitting off the last element of a list

For a nonempty list $l$, the result is the pair
consisting of $l$ with its last element removed and the last element of $l$; for the empty list
there is no result.

Formalized by `Cslib.Algorithms.Lean.BTree.splitLast`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#split-last).

## Rightmost key of a B-tree

For a tree $T$, the rightmost key of $T$ is an optional key
defined by descending the rightmost spine: for a leaf it is the last of its keys (none if the
leaf has no keys); for an internal node with at least one child it is the rightmost key of its
last child; for an internal node with no children it is the last of its separator keys (none
if there are none).

If $T$ satisfies the structural B-tree invariant for a minimum degree $t \ge 2$ and has at least
one key at its root, the rightmost key exists and is the last key of the inorder flattening of
$T$, so on an ordered tree it is the greatest key. Each step splits a child list of length at
most $2t$, so on a valid tree of height $h$ the descent costs $O(t h)$, without computing the
flattening.

Formalized by `Cslib.Algorithms.Lean.BTree.maxKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#max-key).

## Leftmost key of a B-tree

For a tree $T$, the leftmost key of $T$ is an optional key
defined by descending the leftmost spine: for a leaf it is the first of its keys (none if the
leaf has no keys); for an internal node with at least one child it is the leftmost key of its
first child; for an internal node with no children it is the first of its separator keys (none
if there are none).

If $T$ satisfies the structural B-tree invariant for a minimum degree $t \ge 2$ and has at least
one key at its root, the leftmost key exists and is the first key of the inorder flattening of
$T$, so on an ordered tree it is the least key.

Formalized by `Cslib.Algorithms.Lean.BTree.minKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#min-key).

## Merging two B-tree nodes around a separator

Given a key $s$ and trees $L$ and $R$, the
merge of $L$ and $R$ around $s$ is defined as follows. If $L$ and $R$ are leaves with key lists
$k_1$ and $k_2$, it is the leaf with keys $k_1$, then $s$, then $k_2$. If $L$ and $R$ are internal
nodes with key lists $k_1, k_2$ and child lists $c_1, c_2$, it is the internal node with keys
$k_1$, then $s$, then $k_2$, and children $c_1$ followed by $c_2$. In every other case it is $L$.

In deletion from a B-tree of minimum degree $t$, it is applied to two trees of the same height
that each hold $t - 1$ keys at the root, so the merged node holds $2t - 1$ keys.

Formalized by `Cslib.Algorithms.Lean.BTree.merge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#merge).

## Borrowing a key from the right sibling

Given a tree $c$ (the child), a separator key $k$
and a tree $s$ (the right sibling) such that $c$ and $s$ are both leaves or both internal nodes,
$s$ has at least one key, and, when they are internal nodes, $s$ has at least one child: $k$
becomes the last key of $c$, the first key of $s$ is removed from $s$ and becomes the new
separator, and, for internal nodes, the first child of $s$ is removed from $s$ and becomes the
last child of $c$. The result is the triple of the new child, the new separator and the new
sibling. In every other case the result is the unchanged triple $(c, k, s)$.

Formalized by `Cslib.Algorithms.Lean.BTree.borrowRight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#borrow-right).

## Borrowing a key from the left sibling

Given a tree $s$ (the left sibling), a separator key
$k$ and a tree $c$ (the child) such that $s$ and $c$ are both leaves or both internal nodes, $s$
has at least one key, and, when they are internal nodes, $s$ has at least one child: the last key
of $s$ is removed from $s$ and becomes the new separator, $k$ becomes the first key of $c$, and,
for internal nodes, the last child of $s$ is removed from $s$ and becomes the first child of $c$.
The result is the triple of the new sibling, the new separator and the new child. In every other
case the result is the unchanged triple $(s, k, c)$.

Formalized by `Cslib.Algorithms.Lean.BTree.borrowLeft`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#borrow-left).

## Deletion within a B-tree node

Let $D$ be an operation that deletes a key from a tree, let
$t$ be a natural number, let $x$ be a key of a linearly ordered key type, and write $|c|$ for the
number of keys stored at the root of a tree $c$. Deleting $x$ within a node with separator list
$K$ and child list $C$, using $D$ on children, produces a new separator list and a new child list.
Write $k$ for the first separator, $c$ for the first child, and $K'$ and $C'$ for the remaining
separators and children.

If $K$ is empty and $C$ is nonempty, $D$ deletes $x$ from the first child and nothing else
changes; if both are empty, so is the result.

If $x < k$ and either $|c| \ge t$ or $C'$ is empty, $D$ deletes $x$ from $c$. Otherwise let $s$
be the first tree of $C'$. If $|s| \ge t$, borrowing for $c$ from its right sibling $s$ with
separator $k$ gives $(c', k', s')$, which replace $c$, $k$ and $s$, and $D$ deletes $x$ from $c'$.
If $|s| < t$, the trees $c$ and $s$ are merged with $k$ into one tree, which replaces $c$ and $s$,
$k$ is dropped from the separators, and $D$ deletes $x$ from the merged tree.

If $k < x$, $K'$ is empty and $C'$ consists of a single tree $l$: if $|l| \ge t$, $D$ deletes $x$
from $l$; otherwise, if $|c| \ge t$, borrowing for $l$ from its left sibling $c$ with separator
$k$ gives $(c', k', l')$, which replace $c$, $k$ and $l$, and $D$ deletes $x$ from $l'$;
otherwise the result has no separators and a single child, obtained by applying $D$ to delete $x$
from the merge of $c$ and $l$ with $k$. If $k < x$ and $K'$ is nonempty, $k$ and $c$ are kept
and the deletion continues recursively within $K'$ and $C'$.

If $x = k$ and $C'$ is nonempty with first tree $r$: if $|c| \ge t$, the key $p$ found by
descending the rightmost spine of $c$ (following last children down to a leaf or to an internal
node without children, and taking the last key there) replaces $k$ and $D$ deletes $p$ from $c$;
otherwise, if $|r| \ge t$, the key $q$ found by descending the leftmost spine of $r$ (following
first children in the same way and taking the first key there) replaces $k$ and $D$ deletes $q$
from $r$; otherwise $c$ and $r$ are merged with $k$ into one tree, which replaces $c$ and $r$,
$k$ is dropped from the separators, and $D$ deletes $x$ from the merged tree.

In every remaining case (a shape of the separator and child lists not covered above, or a spine
descent that ends at a node with no keys) the lists are returned unchanged.

Formalized by `Cslib.Algorithms.Lean.BTree.delList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#del-list).

## Height-indexed B-tree deletion

Given a height $h$, a minimum degree $t$, a key $x$ of a
linearly ordered key type and a tree $T$, the result is defined as follows. If $T$ is a leaf, the
result is the leaf whose key list is that of $T$ with the first occurrence of $x$ erased,
whatever $h$ is. If $T$ is an internal node and $h = 0$, the result is $T$. If $T$ is an internal
node and $h = n + 1$, the result is the internal node whose separator and child lists are
obtained by deletion of $x$ within the node of $T$ (with minimum degree $t$), where deletion from
a child is height-indexed deletion with minimum degree $t$ at height $n$.

The correctness specification only covers heights that match the shape of the tree.

Formalized by `Cslib.Algorithms.Lean.BTree.delH`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#del-h).

## Height of a B-tree along first children

The height of a B-tree is computed by
following first children: a leaf has height $0$, an internal node with no children has height
$0$, and an internal node whose first child is $c$ has height one more than the height of $c$.

If a tree satisfies the B-tree structural invariant (or the root invariant) at height $h$,
then this height equals $h$.

Formalized by `Cslib.Algorithms.Lean.BTree.treeHeight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#tree-height).

## Top-down B-tree deletion

Deleting a key $x$ of a linearly ordered key type from a tree $T$
with minimum degree $t$ applies height-indexed deletion of $x$ with minimum degree $t$ to $T$ at
the height of $T$, where the height of a leaf, or of an internal node without children, is $0$,
and the height of any other internal node is one more than the height of its first child. If the
outcome is an internal node with no keys and exactly one child, the result is that child;
otherwise the result is the outcome itself.

This follows the top-down deletion of CLRS Section 18.3.

Formalized by `Cslib.Algorithms.Lean.BTree.delete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete).

## Deletion from a B-tree erases the key from its flattening

Let $t \ge 2$ and let $T$ be a
B-tree of minimum degree $t$ over a linearly ordered key type. For every key $x$, the inorder
flattening of the tree obtained from $T$ by top-down deletion of $x$ with minimum degree $t$ is
the flattening of $T$ with the first occurrence of $x$ removed (unchanged if $x$ does not occur).

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1773](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-delete).

## Top-down deletion lowers the height by at most one

Let $t \ge 2$ and let $T$ be an
ordered tree over a linearly ordered key type (its inorder flattening is strictly increasing)
that satisfies the root invariant of B-trees of minimum degree $t$ at height $h$. For every key
$x$, the tree obtained by deleting $x$ from $T$ with minimum degree $t$ satisfies the root
invariant of minimum degree $t$ at height $h$ or at height $h - 1$, where $h - 1$ is truncated
subtraction, so equal to $0$ when $h = 0$.

Formalized by `Cslib.Algorithms.Lean.BTree.delete_validRoot`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1792](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete-valid-root).

## Top-down deletion preserves the B-tree invariant

Let $t \ge 2$ and let $T$ be a B-tree of
minimum degree $t$ over a linearly ordered key type. For every key $x$, the tree obtained by
deleting $x$ from $T$ with minimum degree $t$ is again a B-tree of minimum degree $t$.

Formalized by `Cslib.Algorithms.Lean.BTree.IsBTree.delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1865](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1865). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete-2).

## Deletion from a B-tree yields an ordered tree

Let $t \ge 2$ and let $T$ be a B-tree of
minimum degree $t$ over a linearly ordered key type. For every key $x$, the tree obtained from $T$
by deleting $x$ (with minimum degree $t$) is ordered: its inorder flattening is strictly
increasing.

Formalized by `Cslib.Algorithms.Lean.BTree.ordered_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1878](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1878). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#ordered-delete).

## Top-down deletion yields a root-valid tree

Let $t \ge 2$ and let $T$ be a B-tree of
minimum degree $t$ over a linearly ordered key type. For every key $x$, the tree obtained by
deleting $x$ from $T$ with minimum degree $t$ satisfies the root invariant of B-trees of minimum
degree $t$ at some height.

Formalized by `Cslib.Algorithms.Lean.BTree.delete_validRoot_exists`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1884](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1884). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#delete-valid-root-exists).

## Membership after deletion from a B-tree

Let $t \ge 2$ and let $T$ be a B-tree of minimum
degree $t$ over a linearly ordered key type. For all keys $x$ and $y$, $y$ belongs to the tree
obtained from $T$ by deleting $x$ (with minimum degree $t$) if and only if $y \ne x$ and $y$
belongs to $T$.

Formalized by `Cslib.Algorithms.Lean.BTree.mem_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1891](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1891). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#mem-delete).

## The deleted key is absent after deletion from a B-tree

Let $t \ge 2$ and let $T$ be a
B-tree of minimum degree $t$ over a linearly ordered key type. For every key $x$, $x$ does not
belong to the tree obtained from $T$ by deleting $x$ (with minimum degree $t$).

Formalized by `Cslib.Algorithms.Lean.BTree.not_mem_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1905](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1905). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#not-mem-delete).

## Search after top-down deletion

Let $t \ge 2$ and let $T$ be a B-tree of minimum degree $t$
over a linearly ordered key type. For all keys $x$ and $y$, searching for $y$ in the tree obtained
by deleting $x$ from $T$ with minimum degree $t$ succeeds if and only if $y \ne x$ and $y$ is a
key of $T$.

Formalized by `Cslib.Algorithms.Lean.BTree.contains_delete_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1912](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1912). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#contains-delete-iff).

## Deletion shortens the flattening by one exactly when the key is present

Let $t \ge 2$,
let $T$ be a B-tree of minimum degree $t$ over a linearly ordered key type, and let $x$ be a key.
If $x$ occurs in the inorder flattening of $T$, the flattening of the tree obtained from $T$ by
deleting $x$ (with minimum degree $t$) has length one less than the flattening of $T$; otherwise
the two flattenings have the same length.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_length_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1919](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1919). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-length-delete).

## Repeated top-down deletion

Let $t \ge 2$ and let $T$ be a B-tree of minimum degree $t$
over a linearly ordered key type. For every key $x$, deleting $x$ from $T$ twice with minimum
degree $t$ gives a tree with the same inorder flattening as deleting $x$ from $T$ once.

Formalized by `Cslib.Algorithms.Lean.BTree.flatten_delete_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean, line 1931](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BTree/DeleteBalanced.lean#L1931). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html#flatten-delete-delete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: B-tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/b-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/search-trees/b-tree)
