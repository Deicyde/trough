---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TwoThreeTree.Tree, Cslib.Algorithms.Lean.TwoThreeTree.Overflow, Cslib.Algorithms.Lean.TwoThreeTree.height, Cslib.Algorithms.Lean.TwoThreeTree.height_eq, Cslib.Algorithms.Lean.TwoThreeTree.Balanced, Cslib.Algorithms.Lean.TwoThreeTree.balanced, Cslib.Algorithms.Lean.TwoThreeTree.Mem, Cslib.Algorithms.Lean.TwoThreeTree.All
statement: formalized
proof: formalized
---

# 2–3 tree

40 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html).

## Height-indexed 2-3 trees

For a type $\alpha$ of keys, the 2-3 trees over $\alpha$ indexed
by height are generated as follows. The leaf is a tree of height $0$ and stores no key. For a
natural number $h$, a key $a$ and trees $l$, $r$ of height $h$, the 2-node with separator $a$
and children $l$, $r$ is a tree of height $h + 1$. For a natural number $h$, keys $a$, $b$ and
trees $l$, $m$, $r$ of height $h$, the 3-node with separators $a$, $b$ and children $l$, $m$,
$r$ is a tree of height $h + 1$. Hence all leaves of a tree of height $h$ lie at depth $h$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Tree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#tree).

## Insertion results for 2-3 trees

For a type $\alpha$ and a natural number $h$, an
insertion result at height $h$ is either a 2-3 tree over $\alpha$ of height $h$, or a split:
two 2-3 trees $l$ and $r$ over $\alpha$ of height $h$ together with a promoted key $k \in \alpha$.

It records the outcome of inserting a key into a tree of height $h$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Overflow`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#overflow).

## Height of a 2-3 tree

The height of a 2-3 tree is computed along its leftmost spine:
a leaf has height $0$, and a 2-node or a 3-node has height one more than the height of its
leftmost child.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.height`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#height).

## Computed height equals the height index

For every 2-3 tree $t$ with height index $h$,
the height of $t$ computed along its leftmost spine equals $h$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.height_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#height-eq).

## Balance invariant for 2-3 trees

A leaf is balanced, and a node is balanced when all of
its subtrees are balanced and have the same computed height, where the computed height of a
tree is the length of its leftmost path from the root down to a leaf. Hence all leaves of a
balanced tree lie at the same depth.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Balanced`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#balanced).

## Every height-indexed 2-3 tree is balanced

For every height $h$, every 2-3 tree of
height $h$ satisfies the balance invariant: at every node, the subtrees are balanced and have
equal computed heights.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.balanced`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#balanced-2).

## Membership in a 2-3 tree

A key $x$ is a member of a 2-3 tree when it is one of the
separator keys stored at its nodes: nothing is a member of a leaf; $x$ is a member of a 2-node
with key $a$ and children $l, r$ when it is a member of $l$, equals $a$, or is a member of $r$;
and $x$ is a member of a 3-node with keys $a, b$ and children $l, m, r$ when it is a member of
$l$, equals $a$, is a member of $m$, equals $b$, or is a member of $r$.

Membership is structural and does not use the ordering invariant.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Mem`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#mem).

## Predicate on all keys of a 2-3 tree

For a predicate $p$ on keys and a 2-3 tree $t$,
$\mathrm{All}_p(t)$ states that every separator key stored at a node of $t$ satisfies $p$: it
is true at a leaf, and at a node it requires $p$ of each key of the node and
$\mathrm{All}_p$ of each of its subtrees.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.All`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#all).

## All-keys predicate agrees with membership on 2-3 trees

For every predicate $p$ on
keys and every 2-3 tree $t$ of height $h$, the recursive predicate requiring $p$ at every key
stored at a node of $t$ holds if and only if $p(x)$ holds for every member $x$ of $t$, where
$x$ is a member of $t$ when it equals one of the keys stored at some node of $t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.all_iff_forall_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#all-iff-forall-mem).

## Ordering invariant for 2-3 trees

Let $\alpha$ be a type with a relation $<$. The leaf is
ordered. A 2-node with separator $a$ and children $l$, $r$ is ordered when $l$ and $r$ are
ordered, $y < a$ for every key $y$ stored in $l$, and $a < y$ for every key $y$ stored in $r$. A
3-node with separators $a$, $b$ and children $l$, $m$, $r$ is ordered when $l$, $m$ and $r$ are
ordered, $a < b$, $y < a$ for every key $y$ stored in $l$, $a < y$ and $y < b$ for every key $y$
stored in $m$, and $b < y$ for every key $y$ stored in $r$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ordered).

## Accumulated inorder traversal of a 2-3 tree

For a 2-3 tree $t$ and a list $s$, the
accumulated traversal $F(t, s)$ is defined by recursion on $t$: for a leaf, $F(t, s) = s$; for
a 2-node with key $a$ and children $l, r$, $F(t, s)$ is $F(l, s')$ where $s'$ is $a$ prepended
to $F(r, s)$; for a 3-node with keys $a, b$ and children $l, m, r$, $F(t, s)$ is $F(l, s')$
where $s'$ is $a$ prepended to $F(m, s'')$ and $s''$ is $b$ prepended to $F(r, s)$.

The result is the inorder traversal of $t$ followed by $s$. It is built without recopying the
traversals of left subtrees.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.flattenAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#flatten-aux).

## Inorder traversal of a 2-3 tree

The flattening of a 2-3 tree $t$ is the accumulated
inorder traversal of $t$ onto the empty list. Equivalently, the flattening of a leaf is empty;
that of a 2-node with key $a$ and children $l, r$ is the flattening of $l$, then $a$, then the
flattening of $r$; and that of a 3-node with keys $a, b$ and children $l, m, r$ is the flattening
of $l$, then $a$, then the flattening of $m$, then $b$, then the flattening of $r$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.flatten`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#flatten).

## The accumulated traversal appends the suffix

For every 2-3 tree $t$ (of any height)
and every list $s$, the accumulated inorder traversal of $t$ onto $s$ equals the flattening of
$t$ followed by $s$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.flattenAux_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#flatten-aux-eq).

## The inorder traversal lists exactly the keys of a 2-3 tree

For every 2-3 tree $t$ of
height $h$ and every key $x$, $x$ occurs in the inorder traversal of $t$ if and only if $x$ is a
member of $t$, that is, one of the separator keys stored at its nodes.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.mem_flatten`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#mem-flatten).

## All-keys predicate agrees with the flattening on 2-3 trees

For every predicate $p$
on keys and every 2-3 tree $t$ of height $h$, every key stored at a node of $t$ satisfies $p$
if and only if every element of the inorder flattening of $t$ satisfies $p$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.all_iff_forall_flatten`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#all-iff-forall-flatten).

## Inorder traversal of an ordered 2-3 tree is strictly increasing

Let $\alpha$ be a
linearly ordered type. For every natural number $h$ and every ordered 2-3 tree $t$ over $\alpha$
of height $h$, the flattening (inorder traversal) of $t$ is strictly increasing: whenever a key
$x$ occurs before a key $y$ in it, $x < y$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.ordered_flatten_pairwise`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ordered-flatten-pairwise).

## The traversal of an ordered 2-3 tree has no duplicates

If the keys are linearly ordered
and a 2-3 tree $t$ (of any height) is ordered, then no key occurs twice in the flattening of
$t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.flatten_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#flatten-nodup).

## Search in a 2-3 tree

For a linearly ordered key type, searching a 2-3 tree for a key
$x$ returns false at a leaf. At a 2-node with key $a$, it searches the left subtree if $x < a$,
otherwise the right subtree if $a < x$, and otherwise returns true. At a 3-node with keys $a$
and $b$, it searches the left subtree if $x < a$; otherwise, if $a < x$, it searches the
middle subtree if $x < b$, otherwise the right subtree if $b < x$, and otherwise returns true;
if neither $x < a$ nor $a < x$, it returns true.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#contains).

## Search in an ordered 2-3 tree is correct

Let the keys be linearly ordered and let $t$ be
a 2-3 tree of height $h$ that satisfies the ordering invariant. Then searching $t$ for a key
$x$ returns true if and only if $x$ occurs in the inorder flattening of $t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#contains-eq-true-iff).

## Insertion into a height-indexed 2-3 tree

Inserting a key $x$ into a 2-3 tree of
height $h$ yields either a single tree of height $h$ or a split into two trees of height $h$
around a promoted key. Inserting into a leaf gives the split of two leaves around $x$. At a
2-node with key $a$, insertion recurses into the left child if $x < a$ and into the right child
if $a < x$; a returned tree replaces that child, and a returned split around $k$ is absorbed by
turning the node into a 3-node with keys $k, a$ (left) or $a, k$ (right). At a 3-node with keys
$a, b$, insertion recurses into the left child if $x < a$, the middle child if $a < x < b$, and
the right child if $a < x$ and $b < x$; a returned tree replaces that child, and a returned split
makes the node split into two 2-nodes, promoting $a$, the child's promoted key, or $b$
respectively. In the remaining cases $x$ equals a key of the node and the tree is returned
unchanged.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.ins`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ins).

## Insertion specification for 2-3 trees

Let $\alpha$ be linearly ordered, let
$x \in \alpha$, and let $t$ be a 2-3 tree of height $h$. An insertion result of height $h$ meets
the specification for inserting $x$ into $t$ when the following holds. If it is a single tree
$t'$ of height $h$, then $t'$ is ordered and its inorder traversal equals the ordered insertion
of $x$ into the inorder traversal of $t$. If it is a split into trees $l$ and $r$ of height $h$
around a promoted key $k$, then $l$ and $r$ are ordered, every key of $l$ is less than $k$,
every key of $r$ is greater than $k$, and the traversal of $l$ followed by $k$ and then the
traversal of $r$ equals the ordered insertion of $x$ into the inorder traversal of $t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.InsSpec`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ins-spec).

## Correctness of 2-3 tree insertion

Let $\alpha$ be linearly ordered, let $x \in \alpha$,
and let $t$ be an ordered 2-3 tree of height $h$. Then inserting $x$ into $t$ meets the insertion
specification. If the insertion returns a single tree $t'$ of height $h$, then $t'$ is ordered
and its inorder traversal is the ordered insertion of $x$ into the inorder traversal of $t$. If
it returns a split into trees $l$ and $r$ of height $h$ around a promoted key $k$, then $l$ and
$r$ are ordered, every key of $l$ is less than $k$, every key of $r$ is greater than $k$, and
the traversal of $l$ followed by $k$ and then the traversal of $r$ is the ordered insertion of
$x$ into the inorder traversal of $t$.

Balance is automatic from the height index.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.ins_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ins-spec-2).

## 2-3 trees of unspecified height

For a type $\alpha$, a 2-3 tree of unspecified height
over $\alpha$ is a pair $(h, t)$ of a natural number $h$ and a height-indexed 2-3 tree $t$ over
$\alpha$ of height $h$.

It serves as a standalone search tree.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#root).

## Turning an insertion result into a 2-3 tree

An insertion result at height $h$ becomes a
2-3 tree of unspecified height as follows: a tree $t$ of height $h$ gives $t$ itself, of height
$h$, and a split into trees $l$, $r$ of height $h$ around a key $k$ gives the 2-node with
separator $k$, left child $l$ and right child $r$, of height $h + 1$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Overflow.toRoot`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#to-root).

## Empty 2-3 tree

The empty 2-3 tree is the root of height $0$ whose underlying tree is
the leaf.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 829](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L829). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#empty).

## Inorder traversal of a 2-3 tree root

The flattening of a 2-3 tree root is the
flattening of its underlying tree, that is, the list of its keys in inorder.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.flatten`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 833](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L833). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#flatten-2).

## Search in a rooted 2-3 tree

For a linearly ordered key type, searching a root (a 2-3
tree packaged with its height) for a key $x$ returns the Boolean result of the 2-3 tree search
for $x$ in the underlying height-indexed tree.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 837](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L837). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#contains-2).

## Ordering invariant for 2-3 trees of unspecified height

Let $\alpha$ be a type with a
relation $<$. A 2-3 tree of unspecified height over $\alpha$ is ordered when its underlying
height-indexed 2-3 tree satisfies the ordering invariant.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ordered-2).

## Insertion into a 2-3 tree root

To insert a key $x$ into a root, that is, a 2-3 tree
together with its height $h$, insert $x$ into the underlying tree. If this returns a single tree
of height $h$, that tree is the new root, of height $h$. If it returns a split into trees $l$
and $r$ around a key $k$, the new root is the 2-node with key $k$ and children $l$ and $r$, of
height $h + 1$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 846](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L846). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#insert).

## The empty 2-3 tree is ordered

For every type $\alpha$ with a relation $<$, the empty
2-3 tree of unspecified height over $\alpha$ (the leaf, of height $0$) satisfies the ordering
invariant.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.ordered_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 850](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L850). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ordered-empty).

## The stored height of a 2-3 tree root is its computed height

For every root $t$, that
is, a 2-3 tree together with its height index, the height of the underlying tree computed along
its leftmost spine equals the stored height of $t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.height_tree`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 858](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L858). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#height-tree).

## Every rooted 2-3 tree is balanced

For every root, that is, a 2-3 tree packaged with its
height, the underlying height-indexed tree satisfies the balance invariant.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.balanced`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 863](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L863). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#balanced-3).

## Insertion preserves the ordering of 2-3 trees

Let $\alpha$ be a linearly ordered type.
If $t$ is an ordered 2-3 tree of unspecified height over $\alpha$ and $x \in \alpha$, then the
tree obtained by inserting $x$ into $t$ is ordered.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.ordered_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 867](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L867). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ordered-insert).

## Insertion into a 2-3 tree is ordered insertion into its traversal

Let the keys be
linearly ordered, let $t$ be an ordered 2-3 tree root and let $x$ be a key. Then the flattening
of the root obtained by inserting $x$ into $t$ equals the ordered insertion of $x$ into the
flattening of $t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.flatten_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 887](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L887). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#flatten-insert).

## Keys after insertion into a 2-3 tree

Let $\alpha$ be linearly ordered and let $t$ be an
ordered 2-3 tree root over $\alpha$. For all $x, y \in \alpha$, $y$ occurs in the inorder
traversal of the root obtained by inserting $x$ into $t$ if and only if $y = x$ or $y$ occurs in
the inorder traversal of $t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.mem_flatten_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 910](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#mem-flatten-insert).

## Search in a rooted 2-3 tree is correct

Let the keys be linearly ordered and let $t$ be
a root (a 2-3 tree packaged with its height) whose underlying tree satisfies the ordering
invariant. Then searching $t$ for a key $x$ returns true if and only if $x$ occurs in the
inorder flattening of $t$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 915](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L915). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#contains-eq-true-iff-2).

## Insertion raises the height of a 2-3 tree by at most one

For linearly ordered keys,
every key $x$ and every 2-3 tree root $t$, the stored height of the root obtained by inserting
$x$ into $t$ is at most the stored height of $t$ plus one.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.height_insert_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 920](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L920). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#height-insert-le).

## Building a 2-3 tree from a list

For linearly ordered keys, the 2-3 tree root built from
a list is defined by recursion: the empty list gives the empty 2-3 tree, and a list with head $x$
and tail $xs$ gives the result of inserting $x$ into the root built from $xs$. Thus the elements
are inserted into the empty tree from the last to the first.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.fromList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 925](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L925). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#from-list).

## Building a 2-3 tree from a list gives an ordered tree

Let $\alpha$ be a linearly ordered
type. For every list $L$ of elements of $\alpha$, the 2-3 tree of unspecified height built from
$L$, by inserting the elements of $L$ from right to left into the empty tree, is ordered.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.ordered_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 930](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L930). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#ordered-from-list).

## Keys of a 2-3 tree built from a list

Let $\alpha$ be linearly ordered. For every list
$L$ over $\alpha$ and every $x \in \alpha$, $x$ occurs in the inorder traversal of the 2-3 tree
built from $L$ (by inserting its elements from right to left into the empty tree) if and only
if $x$ occurs in $L$.

Formalized by `Cslib.Algorithms.Lean.TwoThreeTree.Root.mem_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean, line 938](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/TwoThreeTree.lean#L938). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html#mem-from-list).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 2–3 tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/2-3-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/search-trees/2-3-tree)
