---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.CartesianTree.HeapOrdered, Cslib.Algorithms.Lean.CartesianTree.root, Cslib.Algorithms.Lean.CartesianTree.all_iff_forall_inorder, Cslib.Algorithms.Lean.CartesianTree.mem_of_root_eq_some, Cslib.Algorithms.Lean.CartesianTree.root_le_of_heapOrdered, Cslib.Algorithms.Lean.CartesianTree.splitAtFirst, Cslib.Algorithms.Lean.CartesianTree.splitAtFirst_not_mem_fst, Cslib.Algorithms.Lean.CartesianTree.listMin
statement: formalized
proof: formalized
---

# Cartesian tree

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html).

## Min-heap ordered binary tree

Let $\alpha$ be a type with a relation $\le$. A binary tree
with keys in $\alpha$ is min-heap ordered when, at every node, the key $k$ of that node satisfies
$k \le y$ for every key $y$ in its left subtree and every key $y$ in its right subtree. The empty
tree is min-heap ordered.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.HeapOrdered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#heap-ordered).

## Optional root key of a binary tree

For a binary tree $T$ with keys in $\alpha$, the
root key of $T$ is an optional element of $\alpha$: it is absent (none) when $T$ is empty, and it
is $k$ when the top node of $T$ holds the key $k$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.root`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#root).

## A predicate holds on every key iff it holds along the inorder traversal

For every
predicate $p$ on $\alpha$ and every binary tree $T$ with keys in $\alpha$, every key of $T$
satisfies $p$ if and only if every element of the inorder traversal of $T$ satisfies $p$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.all_iff_forall_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#all-iff-forall-inorder).

## The root of a binary tree is one of its keys

For every binary tree $T$ and every key $k$,
if $T$ is nonempty with root key $k$, then $k$ is a key of $T$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.mem_of_root_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#mem-of-root-eq-some).

## The root of a heap-ordered tree is below every key

Let $T$ be a binary tree over a
preordered type that is heap-ordered (in min-heap order). If $T$ has root key $k$, then
$k \le x$ for every key $x$ occurring in $T$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.root_le_of_heapOrdered`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#root-le-of-heap-ordered).

## Splitting a list at the first occurrence of a value

For a value $m$ of a type with
decidable equality and a list $xs$, the split of $xs$ at $m$ is the pair of the part of $xs$
before the first occurrence of $m$ and the part after it; that occurrence itself is dropped. If
$m$ does not occur in $xs$, the split is the pair of $xs$ and the empty list.

Only equality on the element type is needed, not the linear order required to build Cartesian
trees.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.splitAtFirst`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#split-at-first).

## Splitting at the first occurrence leaves the value out of the left part

Let $m$ be an
element of a type with decidable equality and let $xs$ be a list in which $m$ occurs. When $xs$ is
split at the first occurrence of $m$, the left part does not contain $m$.

Together with the reconstruction property (the left part, then $m$, then the right part give back
$xs$), this characterizes the split point, including how duplicates of $m$ are handled when
building Cartesian trees; reconstruction alone would hold for a split at any occurrence.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.splitAtFirst_not_mem_fst`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#split-at-first-not-mem-fst).

## Minimum of a nonempty list

For an element $a$ and a list $as$ over a linear order, the
left-fold minimum of $a$ and $as$ is the minimum of the list with head $a$ and tail $as$. It is
computed from the head: it equals $a$ when $as$ is empty, and when $as$ has head $b$ and tail $bs$
it equals the left-fold minimum of $\min(a, b)$ and $bs$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.listMin`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#list-min).

## Fuel-bounded Cartesian tree construction

Let $\alpha$ be a linear order. For a natural
number $n$ (the fuel) and a list $xs$ over $\alpha$, the tree built from $xs$ with fuel $n$ is
the empty tree if $n = 0$ or $xs$ is empty. Otherwise $n = k + 1$ and $xs$ is nonempty; let $m$
be the minimum of $xs$, and let $L$ and $R$ be the parts of $xs$ before and after the first
occurrence of $m$. Then the tree has root $m$, its left subtree is built from $L$ with fuel $k$,
and its right subtree is built from $R$ with fuel $k$.

Each split produces strictly shorter lists, so a fuel of at least the length of $xs$ never runs
out.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.buildFuel`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#build-fuel).

## Cartesian tree of a list

For a list $xs$ over a linear order, the Cartesian tree of $xs$
is the result of the fuel-bounded Cartesian tree construction on $xs$ with fuel equal to the
length of $xs$. So the empty list gives the empty tree, and otherwise the root is the minimum $m$
of $xs$, the left subtree is built in the same way from the elements before the first occurrence
of $m$, and the right subtree from the elements after that occurrence.

Its inorder traversal is $xs$ and it is min-heap ordered.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.build`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#build).

## Inorder traversal of a Cartesian tree

For every list $xs$ over a linear order, the
inorder traversal of the Cartesian tree of $xs$ is $xs$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.inorder_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#inorder-build).

## The keys of a Cartesian tree permute its input

For every list $xs$ over a linear order,
the inorder traversal of the Cartesian tree of $xs$ is a permutation of $xs$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.perm_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#perm-build).

## Keys of a Cartesian tree

For every list $xs$ over a linear order and every element $x$,
$x$ is a key of the Cartesian tree of $xs$ if and only if $x$ occurs in $xs$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.mem_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#mem-build).

## Cartesian trees are heap-ordered

For every list $xs$ over a linear order, the Cartesian
tree of $xs$ is min-heap ordered.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.heapOrdered_build`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#heap-ordered-build).

## The Cartesian tree of a nonempty list has a root

For every nonempty list $xs$ over a
linearly ordered type, the Cartesian tree of $xs$ has a root key $m$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.root_build_cons_isSome`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#root-build-cons-is-some).

## The root of a Cartesian tree is a minimum of the list

Let $xs$ be a list over a
linearly ordered type. If the Cartesian tree of $xs$ has root key $m$, then $m$ occurs in $xs$
and $m \le y$ for every element $y$ of $xs$.

Formalized by `Cslib.Algorithms.Lean.CartesianTree.root_build_min`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/CartesianTree.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html#root-build-min).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cartesian tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/data-structures/search-trees/cartesian-tree)
