---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.RedBlackTree.Color, Cslib.Algorithms.Lean.RedBlackTree.Tree, Cslib.Algorithms.Lean.RedBlackTree.erase, Cslib.Algorithms.Lean.RedBlackTree.Mem, Cslib.Algorithms.Lean.RedBlackTree.inorderAux, Cslib.Algorithms.Lean.RedBlackTree.inorder, Cslib.Algorithms.Lean.RedBlackTree.All, Cslib.Algorithms.Lean.RedBlackTree.Ordered
statement: formalized
proof: formalized
---

# Red–black tree

82 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html).

## Red-black node colors

The colors of red-black tree nodes are the two values red and
black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.Color`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#color).

## Red-black tree data type

A red-black tree with keys in a type $\alpha$ is either empty or
a node consisting of a color (red or black), a left subtree, a key in $\alpha$, and a right
subtree.

No ordering, color or balance invariant is imposed by the type itself.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.Tree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#tree).

## Color erasure

The color erasure of a red-black tree is the binary tree obtained by
forgetting the node colors: the empty tree goes to the empty binary tree, and a node with key $k$
and subtrees $l$ and $r$ goes to the binary-tree node with key $k$ whose subtrees are the color
erasures of $l$ and $r$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.erase`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#erase).

## Membership in a red-black tree

An element $x$ is a member of a red-black tree $t$ when $x$
is a member of the binary tree obtained from $t$ by erasing its colors, that is, when $x$ equals
the key of some node of $t$.

Membership is structural: it does not use the search-tree ordering.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.Mem`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem).

## Inorder traversal onto a suffix

For a red-black tree $t$ and a list $s$, this is the
accumulator form of the binary-search-tree inorder traversal applied to the color erasure of $t$:
for the empty tree it returns $s$, and for a node with key $k$ and subtrees $l$ and $r$ it returns
the result for $l$ with suffix the list $k$ followed by $u$, where $u$ is the result for $r$ with
suffix $s$.

Thus the result lists the keys of $t$ in inorder followed by $s$, in time linear in the size
of $t$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.inorderAux`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder-aux).

## Inorder traversal of a red-black tree

The inorder traversal of a red-black tree $t$ is
the binary-search-tree inorder traversal of the color erasure of $t$, computed in linear time
with an accumulator starting from the empty list. It lists the keys of $t$ from left to right:
the empty tree gives the empty list, and a node with key $k$ and subtrees $l$ and $r$ gives the
traversal of $l$, then $k$, then the traversal of $r$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.inorder`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder).

## Predicate holding at every key of a red-black tree

For a predicate $p$ on $\alpha$ and a
red-black tree $t$ with keys in $\alpha$, $p$ holds at every key of $t$ when $p$ holds at every key
of the binary search tree obtained from $t$ by erasing colors.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.All`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#all).

## Ordered red-black tree

Let $\alpha$ be a type with a relation $<$. A red-black tree with
keys in $\alpha$ is ordered when, at every node with key $k$, every key $y$ in the left subtree
satisfies $y < k$ and every key $z$ in the right subtree satisfies $k < z$.

Equivalently, the binary tree obtained by erasing the colors is an ordered binary search tree.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.Ordered`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ordered).

## Red-black membership is membership in the underlying binary tree

For every red-black tree
$t$ and every $x$, $x$ is a member of $t$ if and only if $x$ is a member of the binary tree obtained
from $t$ by erasing its colors.

This holds by definition.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.mem_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem-erase).

## All keys of a red-black tree via its color erasure

For every predicate $p$ on $\alpha$
and every red-black tree $t$ with keys in $\alpha$, $p$ holds at every key of $t$ if and only if
$p$ holds at every key of the binary search tree obtained from $t$ by erasing colors. This holds
by definition.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.all_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#all-erase).

## A red-black tree is ordered exactly when its underlying binary tree is

For keys with a
relation $<$, a red-black tree $t$ is ordered if and only if the binary tree obtained from $t$ by
erasing its colors is an ordered binary search tree.

This holds by definition.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.ordered_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ordered-erase).

## Inorder traversal ignores colors

For every red-black tree $t$, the inorder traversal of
$t$ equals the binary-search-tree inorder traversal of the color erasure of $t$; this holds by
definition.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.inorder_erase`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder-erase).

## Root color

The root color of a red-black tree is the color of its root node; the empty
tree has root color black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.colorOf`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#color-of).

## Red property of red-black trees

A red-black tree satisfies the red property when no red
node has a red child, where empty subtrees count as black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.RedOk`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#red-ok).

## Red invariant away from the root

A red-black tree satisfies the relaxed red invariant
when it is empty, or when its left and right subtrees both satisfy the red invariant (no red node
has a red child). The root itself is unconstrained, so a red root may have a red child.

This is the intermediate invariant of Okasaki's unchecked insertion.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.AlmostRedOk`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#almost-red-ok).

## Black height

The black height of a red-black tree is the number of black nodes on its
leftmost root-to-leaf path, counting the empty leaf as one black node: the empty tree has black
height $1$, a red node has the black height of its left subtree, and a black node has the black
height of its left subtree plus $1$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.blackHeight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#black-height).

## Black-height balanced red-black tree

A red-black tree is balanced when every root-to-leaf
path contains the same number of black nodes. Recursively: the empty tree is balanced, and a node
is balanced when both of its subtrees are balanced and have the same black height (the number of
black nodes on the leftmost root-to-leaf path, counting the leaf).

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.Balanced`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#balanced).

## Valid red-black tree

Let $\alpha$ be a type with a relation $<$. A red-black tree with
keys in $\alpha$ is valid when it is ordered, satisfies the red property (no red node has a red
child), is balanced (every root-to-leaf path contains the same number of black nodes), and its
root is black, where the empty tree counts as black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.Valid`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid).

## Search in a red-black tree

Searching a red-black tree over a linearly ordered type for a
key $x$ returns a Boolean, ignoring colors: the empty tree gives false, and at a node with key $k$
the search continues in the left subtree if $x < k$, continues in the right subtree if $k < x$,
and returns true otherwise.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.contains`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#contains).

## Okasaki's rebalancing

Given a color $c$, red-black trees $l$ and $r$, and a key $k$,
rebalancing produces a tree as follows. Suppose $c$ is black and one of these configurations
occurs, taking the first that applies: $l$ is a red node with a red left child; $l$ is a red node
with a red right child; $r$ is a red node with a red left child; $r$ is a red node with a red
right child. The black root and the two red nodes then hold three keys and leave four subtrees,
which read in inorder as $t_1, x, t_2, y, t_3, z, t_4$. The result is a red node with key $y$, left
child the black node with subtrees $t_1, t_2$ and key $x$, and right child the black node with
subtrees $t_3, t_4$ and key $z$. In every other case the result is the node with color $c$, left
subtree $l$, key $k$ and right subtree $r$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.balance`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#balance).

## Unchecked red-black insertion

For keys from a linearly ordered type, the unchecked
insertion of $x$ into a red-black tree is defined by recursion on the tree. Inserting $x$ into the
empty tree gives a red node with key $x$ and two empty subtrees. Inserting $x$ into a node with
color $c$, left subtree $l$, key $k$ and right subtree $r$ gives: if $x < k$, Okasaki's
rebalancing of color $c$, left subtree the insertion of $x$ into $l$, key $k$ and right subtree
$r$; if $k < x$, Okasaki's rebalancing of color $c$, left subtree $l$, key $k$ and right subtree
the insertion of $x$ into $r$; otherwise the node itself, unchanged.

The result may have a red root with a red child, so it need not satisfy the red invariant.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.ins`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ins).

## Blackening the root

Recoloring the root of a red-black tree black leaves the empty tree
unchanged and turns a node with any color, left subtree $l$, key $k$ and right subtree $r$ into the
black node with left subtree $l$, key $k$ and right subtree $r$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.makeBlack`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#make-black).

## Recoloring the root black does not change the color erasure

For every red-black
tree $t$, the color erasure of the tree obtained from $t$ by recoloring its root black (the empty
tree is left unchanged) equals the color erasure of $t$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.erase_makeBlack`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#erase-make-black).

## Red-black tree insertion

For keys from a linearly ordered type, inserting $x$ into a
red-black tree $t$ gives the unchecked insertion of $x$ into $t$ with its root recolored black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#insert).

## Red-black tree from a list

The red-black tree built from a list over a linearly ordered
type inserts the elements of the list into the empty tree from right to left: the empty list
gives the empty tree, and a list with head $x$ and tail $xs$ gives the insertion of $x$ into the
tree built from $xs$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.fromList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#from-list).

## All keys versus members of a red-black tree

For every predicate $p$ on $\alpha$ and every
red-black tree $t$ with keys in $\alpha$, $p$ holds at every key of $t$ if and only if $p(x)$ holds
for every $x \in \alpha$ that is a (structural) member of $t$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.all_iff_forall_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#all-iff-forall-mem).

## Membership in the inorder traversal of a red-black tree

For every red-black tree $t$ and
every $x$, $x$ occurs in the inorder traversal of $t$ if and only if $x$ is a member of $t$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.mem_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem-inorder).

## The inorder traversal of an ordered red-black tree is strictly increasing

For keys from a
linearly ordered type, if a red-black tree $t$ is ordered, then every entry of the inorder
traversal of $t$ is strictly smaller than every later entry.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.ordered_inorder`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ordered-inorder).

## Membership after insertion into a red-black tree

For keys from a linearly ordered type, a
key $y$ is a member of the red-black tree obtained by inserting $x$ into $t$ if and only if $y = x$
or $y$ is a member of $t$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.mem_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 594](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem-insert).

## Red-black insertion preserves the search-tree order

Let $\alpha$ be a linearly ordered
type, $x \in \alpha$ a key, and $t$ a red-black tree with keys in $\alpha$. If $t$ is ordered (at
every node with key $k$, every key in the left subtree is less than $k$ and every key in the right
subtree is greater than $k$), then the tree obtained by inserting $x$ into $t$ is ordered.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.ordered_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ordered-insert).

## Red-black insertion preserves the red property

Let $\alpha$ be a linearly ordered type,
$x \in \alpha$ a key, and $t$ a red-black tree with keys in $\alpha$. If no red node of $t$ has a
red child, then no red node of the tree obtained by inserting $x$ into $t$ has a red child.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.redOk_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#red-ok-insert).

## Red-black insertion preserves black-height balance

Let $\alpha$ be a linearly ordered type.
If a red-black tree $t$ with keys in $\alpha$ is balanced (every root-to-leaf path contains the same
number of black nodes), then for every $x \in \alpha$ the tree obtained by inserting $x$ into $t$ is
balanced.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.balanced_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#balanced-insert).

## Insertion raises the black height by at most one

Let $\alpha$ be a linearly ordered type.
For every red-black tree $t$ with keys in $\alpha$ and every $x \in \alpha$, the black height of the
tree obtained by inserting $x$ into $t$ equals either the black height of $t$ or the black height of
$t$ plus one.

Any increase comes from recoloring the root black at the end of insertion.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.blackHeight_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 614](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L614). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#black-height-insert).

## Red-black insertion yields a valid tree from the invariants

Let $\alpha$ be a linearly
ordered type, $x \in \alpha$ a key, and $t$ a red-black tree with keys in $\alpha$ that is
ordered, satisfies the red property (no red node has a red child), and is balanced (every
root-to-leaf path contains the same number of black nodes). Then the tree obtained by inserting
$x$ into $t$ is valid.

The root of $t$ need not be black, since insertion recolors the root black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.valid_insert_of_invariants`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid-insert-of-invariants).

## Red-black insertion preserves validity

Let $\alpha$ be a linearly ordered type and
$x \in \alpha$. If $t$ is a valid red-black tree with keys in $\alpha$, then the tree obtained by
inserting $x$ into $t$ is also valid.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.valid_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid-insert).

## Search in an ordered red-black tree is correct

Let $t$ be a red-black tree over a
linearly ordered type that is ordered (every left key is smaller and every right key larger,
recursively). Then for every key $x$, the search for $x$ in $t$ returns true if and only if $x$
is a key of some node of $t$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.contains_eq_true_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#contains-eq-true-iff).

## Ordered red-black trees have duplicate-free inorder traversals

For a red-black tree $t$
over a linearly ordered type that is ordered (every left key is smaller and every right key
larger, recursively), the inorder traversal of $t$ contains no key twice.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.inorder_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder-nodup).

## The empty red-black tree is valid

For every type $\alpha$ with a relation $<$, the empty
red-black tree with keys in $\alpha$ is a valid red-black tree.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.valid_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid-empty).

## Red-black trees built from a list are valid

Let $\alpha$ be a linearly ordered type. For
every list $l$ of elements of $\alpha$, the red-black tree obtained from the empty tree by
inserting the elements of $l$ one at a time, from the last to the first, is valid.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.valid_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 669](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L669). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid-from-list).

## Membership in a red-black tree built from a list

For keys from a linearly ordered type and
every list $xs$, a key $x$ is a member of the red-black tree built from $xs$ by successive
insertion if and only if $x$ occurs in $xs$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.mem_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem-from-list).

## Splicing two red-black trees

The splice of a red-black tree $t$ with a red-black tree $s$ is
defined by recursion on $t$. The splice of the empty tree with $s$ is $s$. The splice of the node
with color $c$, left subtree $l$, key $k$ and right subtree $r$ with $s$ is the node with color
$c$, left subtree $l$, key $k$ and right subtree the splice of $r$ with $s$.

So $s$ becomes the right subtree of the rightmost node of $t$, and all existing colors are kept.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.join`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#join).

## Unbalanced red-black tree deletion

For a key $x$ of a linearly ordered type, unbalanced
deletion of $x$ from a red-black tree is defined by recursion on the tree. The empty tree stays
empty. At a node with color $c$, left subtree $l$, key $k$ and right subtree $r$: if $x < k$, the
result is the node with color $c$, left subtree the unbalanced deletion of $x$ from $l$, key $k$
and right subtree $r$; if $k < x$, it is the node with color $c$, left subtree $l$, key $k$ and
right subtree the unbalanced deletion of $x$ from $r$; otherwise (so $x = k$) it is the splice of
$l$ with $r$.

Colors are kept, so the result need not satisfy the red invariant or be black-height balanced.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.del`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#del).

## Rebuilding a red-black tree from its keys

For a linearly ordered key type, the rebuild of
a red-black tree $t$ is the tree obtained from the empty tree by inserting the keys of the inorder
traversal of $t$ one at a time with Okasaki insertion, starting from the last key.

The result is a valid red-black tree whose keys are exactly the keys of $t$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.rebalance`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#rebalance).

## Red-black tree deletion by rebuilding

For a key $x$ of a linearly ordered type and a
red-black tree $t$, deleting $x$ from $t$ by rebuilding first forms the unbalanced deletion of
$x$ from $t$, then rebalances it: starting from the empty tree, it inserts the keys of the inorder
traversal of that tree one at a time, from the last key to the first.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.delete`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#delete).

## Membership in a splice

For red-black trees $t$ and $s$ with keys of any type, a key $x$
belongs to the splice of $t$ with $s$ if and only if $x$ belongs to $t$ or $x$ belongs to $s$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.mem_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem-join).

## Inorder traversal of a splice

For red-black trees $t$ and $s$ with keys of any type,
the inorder traversal of the splice of $t$ with $s$ is the inorder traversal of $t$ followed by the
inorder traversal of $s$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.inorder_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder-join).

## Joining separated ordered trees preserves order

Let $<$ be a relation on the keys, and let
$L$ and $R$ be red-black trees that are ordered for $<$ such that $a < b$ for every key $a$ of $L$
and every key $b$ of $R$. Then the join of $L$ and $R$, obtained by putting $R$ in place of the
empty right subtree of the rightmost node of $L$ (or $R$ itself if $L$ is empty) and keeping all
colors, is ordered.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.ordered_join`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ordered-join).

## Membership after deletion by rebuilding

Let $x$ and $y$ be keys of a linearly ordered
type and let $t$ be an ordered red-black tree. Then $y$ belongs to the tree obtained from $t$ by
deleting $x$ by rebuilding if and only if $y$ belongs to $t$ and $y \ne x$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.mem_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem-delete).

## The deleted key is absent after deletion by rebuilding

Let $x$ be a key of a linearly
ordered type and let $t$ be an ordered red-black tree. Then $x$ does not belong to the tree
obtained from $t$ by deleting $x$ by rebuilding.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.not_mem_delete_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#not-mem-delete-self).

## Inorder traversal after deletion by rebuilding

Let $x$ be a key of a linearly ordered
type and let $t$ be an ordered red-black tree. Then the inorder traversal of the tree obtained from
$t$ by deleting $x$ by rebuilding is the inorder traversal of $t$ with the first occurrence of $x$
removed (it is unchanged if $x$ does not occur).

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.inorder_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder-delete).

## Red-black deletion yields a valid red-black tree

For every linearly ordered key type,
every key $x$ and every red-black tree $t$, the tree obtained by deleting $x$ from $t$ is a valid
red-black tree: it is ordered, no red node has a red child, every root-to-leaf path contains the
same number of black nodes, and its root is black (the empty tree counts as black). No hypothesis
on $t$ is needed.

The result is valid because deletion rebuilds the tree by repeated insertion, which always
produces a valid red-black tree.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.valid_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid-delete).

## Red-black deletion yields an ordered tree

For every linearly ordered key type, every key
$x$ and every red-black tree $t$, the tree obtained by deleting $x$ from $t$ is ordered: at every
node, all keys in the left subtree are strictly smaller than the node's key and all keys in the
right subtree are strictly larger. No hypothesis on $t$ is needed.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.ordered_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ordered-delete).

## Red-black deletion yields a tree with no red-red edge

For every linearly ordered key
type, every key $x$ and every red-black tree $t$, the tree obtained by deleting $x$ from $t$
satisfies the red invariant: no red node has a red child. No hypothesis on $t$ is needed.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.redOk_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#red-ok-delete).

## Deletion by rebuilding is black-height balanced

For every linearly ordered type of
keys, every key $x$ and every red-black tree $t$, with no hypothesis on $t$, the tree obtained
from $t$ by deleting $x$ by rebuilding is black-height balanced.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.balanced_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#balanced-delete).

## Deletion by rebuilding gives a black root

For every linearly ordered type of keys,
every key $x$ and every red-black tree $t$, with no hypothesis on $t$, the root of the tree
obtained from $t$ by deleting $x$ by rebuilding is black, where the empty tree counts as having
a black root.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.colorOf_delete`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/Delete.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#color-of-delete).

## Extended root colors

An extended color is one of three values: red, black or double
black.

Double black marks the root of a tree after a deletion and counts as two black nodes in its black
height.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.BColor`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#bcolor).

## Trees with a possibly double-black root

A tree with a possibly double-black root over a
type $\alpha$ is one of the following: a genuine red-black tree over $\alpha$; the double-black
empty tree; or a double-black node consisting of a left subtree, a key in $\alpha$ and a right
subtree, where both subtrees are genuine red-black trees. Hence a double black can occur only at
the root.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.BBTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#bbtree).

## Inorder traversal of a possibly double-black tree

The inorder traversal of a red-black
tree whose root may be double black ignores the double-black mark: a genuine tree gives its
inorder traversal, the double-black empty tree gives the empty list, and a double-black node with
left child $l$, key $k$ and right child $r$ gives the inorder traversal of $l$, followed by $k$,
followed by the inorder traversal of $r$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.inorderBB`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder-bb).

## Black height of a possibly double-black tree

The black height of a genuine red-black tree
is its usual black height. The double-black empty tree has black height $2$, and a double-black
node with left subtree $L$ has black height $h(L) + 2$, where $h(L)$ is the usual black height of
$L$. Thus a double-black root counts as two black nodes, where the usual black height counts the
empty tree as one.

For an ordered, balanced red-black tree satisfying the red invariant, deleting any key by the
double-black descent, before the root is blackened, yields a tree whose black height in this sense
equals the black height of the original tree.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.bhBB`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#bh-bb).

## Black-height balance of a possibly double-black tree

A tree whose root may be double
black is balanced when it is a genuine red-black tree that is balanced, when it is the
double-black empty tree, or when it is a double-black node whose left and right subtrees are both
balanced and have the same black height.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.BalancedBB`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#balanced-bb).

## Red invariant for trees with a possibly double-black root

A tree whose root may be
double black satisfies the red invariant in the following cases: a genuine red-black tree
satisfies it when it satisfies the usual red invariant (no red node has a red child); the
double-black empty tree always satisfies it; and a double-black node with left subtree $l$ and
right subtree $r$ satisfies it when both $l$ and $r$ satisfy the usual red invariant.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.RedOkBB`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#red-ok-bb).

## Extended root color

The extended color of a tree whose root may be double black is the
color of its root, red or black, when it is a genuine red-black tree, where the empty tree counts
as black; it is double black for the double-black empty tree and for every double-black node.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.colorBB`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#color-bb).

## Adding a black to the root

Add one black to the root of a red-black tree, producing a
tree whose root may be double black: the empty tree becomes the double-black empty tree, a red
root becomes black, and a black root becomes double black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.incrBlack`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#incr-black).

## Recoloring the root black

For a red-black tree $t$, this is the tree obtained from $t$
by coloring its root black: the empty tree stays empty, and a node with left subtree $l$, key
$k$ and right subtree $r$, of either color, becomes the black node with left subtree $l$, key
$k$ and right subtree $r$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.rootBlack`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#root-black).

## Absorbing a double-black root

Blackening sends a tree whose root may be double black to
a genuine red-black tree by changing only its root: a genuine tree has its root recolored black
(the empty tree stays empty), the double-black empty tree becomes the empty tree, and a
double-black node becomes the black node with the same subtrees and key.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.blacken`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#blacken).

## Leftmost key of a red-black tree

For a red-black tree $t$ over a type $\alpha$, the
leftmost key of $t$ is either a key in $\alpha$ or undefined. It is undefined when $t$ is empty.
When $t$ is a node, of either color, with left subtree $l$ and key $k$, it is the leftmost key of
$l$ if that is defined, and $k$ otherwise. Hence the leftmost key is defined exactly when $t$ is
nonempty.

Under the search-tree invariant the leftmost key is the minimum key of the tree.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.minKey`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#min-key).

## Left repair after double-black deletion

Write $\mathrm{R}$ and $\mathrm{B}$ for red and
black, and $N(c, T, y, T')$ for the node of color $c$ with left subtree $T$, key $y$ and right
subtree $T'$. Given a color $c$, a tree $D$, a key $k$ and a tree $S$, the left repair returns a
tree whose root may be double black, by the first case that applies. If
$S = N(\mathrm{B}, T_1, y, N(\mathrm{R}, T_2, z, T_3))$ or, failing that,
$S = N(\mathrm{B}, N(\mathrm{R}, T_1, y, T_2), z, T_3)$, it returns
$N(c, N(\mathrm{B}, D, k, T_1), y, N(\mathrm{B}, T_2, z, T_3))$. Otherwise, if
$S = N(\mathrm{B}, T_1, y, T_2)$, it returns $N(\mathrm{B}, D, k, N(\mathrm{R}, T_1, y, T_2))$ when
$c$ is red, and the double-black node with left child $D$, key $k$ and right child
$N(\mathrm{R}, T_1, y, T_2)$ when $c$ is black. In the next three cases $c$ is not used. If
$S = N(\mathrm{R}, N(\mathrm{B}, T_1, y, N(\mathrm{R}, T_2, z, T_3)), w, T_4)$ or, failing that,
$S = N(\mathrm{R}, N(\mathrm{B}, N(\mathrm{R}, T_1, y, T_2), z, T_3), w, T_4)$, it returns
$N(\mathrm{B}, N(\mathrm{R}, N(\mathrm{B}, D, k, T_1), y, N(\mathrm{B}, T_2, z, T_3)), w, T_4)$.
Otherwise, if $S = N(\mathrm{R}, N(\mathrm{B}, T_1, y, T_2), w, T_3)$, it returns
$N(\mathrm{B}, N(\mathrm{B}, D, k, N(\mathrm{R}, T_1, y, T_2)), w, T_3)$. In every remaining case
it returns $N(c, D, k, S)$.

The repair is meant for a deficient left subtree $D$ whose double black has been absorbed, so
that $D$ has one black node fewer than its sibling $S$ on every root-to-leaf path.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.fixLeft`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#fix-left).

## Right repair after double-black deletion

Write $\mathrm{R}$ and $\mathrm{B}$ for red and
black, and $N(c, T, y, T')$ for the node of color $c$ with left subtree $T$, key $y$ and right
subtree $T'$. Given a color $c$, a tree $S$, a key $k$ and a tree $D$, the right repair returns a
tree whose root may be double black, by the first case that applies. If
$S = N(\mathrm{B}, N(\mathrm{R}, T_1, y, T_2), z, T_3)$ or, failing that,
$S = N(\mathrm{B}, T_1, y, N(\mathrm{R}, T_2, z, T_3))$, it returns
$N(c, N(\mathrm{B}, T_1, y, T_2), z, N(\mathrm{B}, T_3, k, D))$. Otherwise, if
$S = N(\mathrm{B}, T_1, y, T_2)$, it returns $N(\mathrm{B}, N(\mathrm{R}, T_1, y, T_2), k, D)$ when
$c$ is red, and the double-black node with left child $N(\mathrm{R}, T_1, y, T_2)$, key $k$ and
right child $D$ when $c$ is black. In the next three cases $c$ is not used. If
$S = N(\mathrm{R}, T_1, y, N(\mathrm{B}, N(\mathrm{R}, T_2, z, T_3), w, T_4))$ or, failing that,
$S = N(\mathrm{R}, T_1, y, N(\mathrm{B}, T_2, z, N(\mathrm{R}, T_3, w, T_4)))$, it returns
$N(\mathrm{B}, T_1, y, N(\mathrm{R}, N(\mathrm{B}, T_2, z, T_3), w, N(\mathrm{B}, T_4, k, D)))$.
Otherwise, if $S = N(\mathrm{R}, T_1, y, N(\mathrm{B}, T_2, z, T_3))$, it returns
$N(\mathrm{B}, T_1, y, N(\mathrm{B}, N(\mathrm{R}, T_2, z, T_3), k, D))$. In every remaining case
it returns $N(c, S, k, D)$.

The repair is the mirror image of the left repair, meant for a deficient right subtree $D$ whose
double black has been absorbed, so that $D$ has one black node fewer than its sibling $S$ on
every root-to-leaf path.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.fixRight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#fix-right).

## Rebalancing after deletion from the left subtree

Let $c$ be a color, $L$ a tree whose
root may be double black, $k$ a key and $R$ a red-black tree. If $L$ is a genuine red-black tree,
the result is the genuine node with color $c$, left subtree $L$, key $k$ and right subtree $R$.
Otherwise the double black of $L$ is absorbed first: a double-black empty tree becomes the empty
tree, and a double-black node becomes the black node with the same children and key. The result is
then the left-deficit repair (Fix Left) applied to the color $c$, the absorbed tree, the key $k$
and the sibling $R$; it may again have a double-black root.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.balLeft`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#bal-left).

## Rebalancing after deletion from the right subtree

Let $c$ be a color, $L$ a red-black
tree, $k$ a key and $R$ a tree whose root may be double black. If $R$ is a genuine red-black
tree, the result is the genuine node with color $c$, left subtree $L$, key $k$ and right subtree
$R$. Otherwise the double black of $R$ is absorbed first: a double-black empty tree becomes the
empty tree, and a double-black node becomes the black node with the same children and key. The
result is then the right-deficit repair (Fix Right) applied to the color $c$, the sibling $L$, the
key $k$ and the absorbed tree; it may again have a double-black root.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.balRight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#bal-right).

## Double-black deletion

For a key $x$ of a linearly ordered type, deleting $x$ from a
red-black tree returns a tree whose root may be double black, by recursion on the tree. The
empty tree gives the empty tree. At a node of color $c$ with left subtree $l$, key $k$ and right
subtree $r$: if $x < k$, the result is the left reassembly of color $c$, the deletion of $x$
from $l$, key $k$ and $r$; if $k < x$, it is the right reassembly of color $c$, $l$, key $k$ and
the deletion of $x$ from $r$. A reassembly rebuilds the node when the recursive result is a
genuine tree, and otherwise repairs the double-black child against its sibling. If $x = k$ and
$l$ is empty, the result is $r$ when $c$ is red and $r$ with one black added at its root when
$c$ is black; otherwise, if $r$ is empty, the same with $l$ in place of $r$. If $x = k$ and both
subtrees are nonempty, let $s$ be the leftmost key of $r$; the result is the right reassembly of
color $c$, $l$, key $s$ and the deletion of $s$ from $r$. Thus a node with two children is
deleted by promoting its successor, the minimum key of its right subtree.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.del`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#del-2).

## Red-black tree deletion by the double-black method

For a key $x$ of a linearly ordered
type and a red-black tree $t$, deleting $x$ from $t$ runs the double-black deletion of $x$ from
$t$, which returns a tree whose root may be double black, and then absorbs a remaining double
black at the root and recolors the root black.

When $t$ is ordered, has no red node with a red child and has the same number of black nodes on
every root-to-leaf path, the result is a valid red-black tree; when $t$ is only ordered, the
inorder traversal of the result is that of $t$ with $x$ erased.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.deleteBal`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#delete-bal).

## Double-black deletion erases the key from the inorder traversal

For a key $x$ of a
linearly ordered type and an ordered red-black tree $t$, the inorder traversal of the tree
obtained by deleting $x$ from $t$ by the double-black method is the inorder traversal of $t$
with the first occurrence of $x$ removed (unchanged if $x$ does not occur).

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.inorder_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#inorder-delete-bal).

## Keys after double-black deletion

For keys $x$ and $y$ of a linearly ordered type and an
ordered red-black tree $t$, $y$ is a key of the tree obtained by deleting $x$ from $t$ by the
double-black method if and only if $y$ is a key of $t$ and $y \ne x$.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.mem_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#mem-delete-bal).

## The deleted key is absent after double-black deletion

Let $\alpha$ be a linearly
ordered type and $t$ a red-black tree with keys in $\alpha$ that is ordered, that is, at every
node all keys of the left subtree are strictly smaller and all keys of the right subtree are
strictly larger than the node's key. Then for every $x \in \alpha$, the key $x$ does not occur in
the tree obtained by deleting $x$ from $t$ by the double-black method.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.not_mem_deleteBal_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#not-mem-delete-bal-self).

## Double-black deletion preserves the search-tree order

Let $\alpha$ be a linearly
ordered type and $t$ a red-black tree with keys in $\alpha$ that is ordered, that is, at every
node all keys of the left subtree are strictly smaller and all keys of the right subtree are
strictly larger than the node's key. Then for every $x \in \alpha$, the tree obtained by deleting
$x$ from $t$ by the double-black method is again ordered.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.ordered_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#ordered-delete-bal).

## Double-black deletion yields a valid tree from the structural invariants

Let $\alpha$
be a linearly ordered type and $t$ a red-black tree with keys in $\alpha$ that is ordered,
satisfies the red invariant (no red node has a red child), and is black-height balanced (all
root-to-leaf paths contain the same number of black nodes). Then for every $x \in \alpha$, the
tree obtained by deleting $x$ from $t$ by the double-black method is a valid red-black tree.

The root of $t$ need not be black, since the deletion recolors the root of its result black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.valid_deleteBal_of_invariants`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid-delete-bal-of-invariants).

## Double-black deletion preserves validity

Let $\alpha$ be a linearly ordered type and
$t$ a valid red-black tree with keys in $\alpha$: it is ordered, satisfies the red invariant, is
black-height balanced, and has a black root. Then for every $x \in \alpha$, the tree obtained by
deleting $x$ from $t$ by the double-black method is again a valid red-black tree.

The proof uses only that $t$ is ordered, satisfies the red invariant and is balanced.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.valid_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#valid-delete-bal).

## Double-black deletion from a valid tree keeps the red invariant

Let $\alpha$ be a
linearly ordered type and $t$ a valid red-black tree with keys in $\alpha$: it is ordered,
satisfies the red invariant, is black-height balanced, and has a black root. Then for every
$x \in \alpha$, the tree obtained by deleting $x$ from $t$ by the double-black method satisfies
the red invariant: no red node has a red child.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.redOk_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#red-ok-delete-bal).

## Double-black deletion keeps a valid tree balanced

Let $\alpha$ be a linearly ordered
type, $x \in \alpha$, and $T$ a valid red-black tree over $\alpha$. Then the tree obtained from
$T$ by double-black deletion of $x$ is balanced.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.balanced_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#balanced-delete-bal).

## Double-black deletion leaves a black root

For every key $x$ of a linearly ordered type
and every red-black tree $t$, valid or not, the root of the tree obtained by deleting $x$ from $t$
by the double-black method is black, where the empty tree counts as black.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.colorOf_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#color-of-delete-bal).

## Black height after double-black deletion

Let $\alpha$ be a linearly ordered type,
$x \in \alpha$, $T$ a valid red-black tree over $\alpha$, and $T'$ the tree obtained from $T$ by
double-black deletion of $x$. Then the black height of $T'$ either equals the black height of $T$
or is one less than it.

The black height drops by one when a double black left by the deletion is absorbed at the root.

Formalized by `Cslib.Algorithms.Lean.RedBlackTree.DeleteBalanced.blackHeight_deleteBal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean, line 1279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/RedBlackTree/DeleteBalanced.lean#L1279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html#black-height-delete-bal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Red–black tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/red-black-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/search-trees/red-black-tree)
