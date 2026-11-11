---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.WeightBalancedTree.numNodes_empty, Cslib.Algorithms.Lean.WeightBalancedTree.numNodes_node, Cslib.Algorithms.Lean.WeightBalancedTree.weight, Cslib.Algorithms.Lean.WeightBalancedTree.Balanced, Cslib.Algorithms.Lean.WeightBalancedTree.balance, Cslib.Algorithms.Lean.WeightBalancedTree.insert, Cslib.Algorithms.Lean.WeightBalancedTree.fromList, Cslib.Algorithms.Lean.WeightBalancedTree.balanced_node
statement: formalized
proof: formalized
---

# Weight-balanced tree

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html).

## Number of keys of the empty tree

The empty binary tree has $0$ nodes.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.numNodes_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#num-nodes-empty).

## Number of keys of a node

Write $|t|$ for the number of nodes of a binary tree $t$. For
binary trees $l$ and $r$ and a key $k$, the node with key $k$, left subtree $l$ and right subtree
$r$ has $|l| + |r| + 1$ nodes.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.numNodes_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#num-nodes-node).

## Weight of a binary tree

The Nievergelt–Reingold weight $w(t)$ of a binary tree $t$
is its number of keys plus one. Equivalently, it counts the external leaves: the empty tree
has weight $1$, and the weight of a node is the sum of the weights of its two children.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.weight`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#weight).

## Weight-balanced trees

Write $|t|$ for the number of keys of a binary tree $t$ and
$w(t) = |t| + 1$ for its weight. A binary tree is weight-balanced, or satisfies the
invariant $\mathrm{BB}[1/4]$, when it is empty, or when it is a node with left subtree $L$
and right subtree $R$ such that $L$ and $R$ are weight-balanced,
$4\,w(L) \le 3(w(L) + w(R))$ and $4\,w(R) \le 3(w(L) + w(R))$. Since the weight of a node
is $w(L) + w(R)$, this says that each child has weight at most three quarters of the
weight of the node.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.Balanced`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#balanced).

## Weight-balanced rebalancing

For binary trees $L$, $R$ and a key $k$, write $|t|$ for
the number of keys of a tree $t$, $w(t) = |t| + 1$ for its weight, $w = w(L) + w(R)$, and
$\langle X, x, Y \rangle$ for the node with key $x$, left subtree $X$ and right subtree
$Y$. The rebalanced node $\mathrm{balance}(L, k, R)$ is defined as follows.
If $3w < 4\,w(L)$, then $L = \langle A, a, B \rangle$ is a node; if $|B| \le 2|A|$, the
result is the single rotation $\langle A, a, \langle B, k, R \rangle \rangle$, and
otherwise $B = \langle B_1, b, B_2 \rangle$ is a node and the result is the double
rotation $\langle \langle A, a, B_1 \rangle, b, \langle B_2, k, R \rangle \rangle$.
Otherwise, if $3w < 4\,w(R)$, then $R = \langle C, c, D \rangle$ is a node; if
$|C| \le 2|D|$, the result is $\langle \langle L, k, C \rangle, c, D \rangle$, and
otherwise $C = \langle C_1, d, C_2 \rangle$ is a node and the result is
$\langle \langle L, k, C_1 \rangle, d, \langle C_2, c, D \rangle \rangle$.
In all remaining cases the result is $\langle L, k, R \rangle$.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.balance`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#balance).

## Weight-balanced insertion

For a key $x$ of a linearly ordered type, the insertion
$\mathrm{insert}(x, t)$ of $x$ into a binary tree $t$ is defined by recursion on $t$. Into the
empty tree it gives the single node with key $x$. Into the node $N$ with key $k$, left subtree
$L$ and right subtree $R$ it gives $\mathrm{balance}(\mathrm{insert}(x, L), k, R)$ if $x < k$,
$\mathrm{balance}(L, k, \mathrm{insert}(x, R))$ if $k < x$, and $N$ itself if $x = k$, where
$\mathrm{balance}$ is weight-balanced rebalancing.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#insert).

## Weight-balanced tree from a list

The tree built from a list $x_1, \dots, x_n$ of
elements of a linearly ordered type is obtained from the empty tree by inserting
$x_n, x_{n-1}, \dots, x_1$ in this order with weight-balanced insertion; the empty list
gives the empty tree.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.fromList`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#from-list).

## Building a weight-balanced node

Let $L$ and $R$ be weight-balanced trees and $k$ a
key, and write $|t|$ for the number of keys of a tree $t$. If
$4(|L| + 1) \le 3(|L| + |R| + 2)$ and $4(|R| + 1) \le 3(|L| + |R| + 2)$, then the node with
key $k$, left subtree $L$ and right subtree $R$ is weight-balanced.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.balanced_node`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#balanced-node).

## Weight form of the balance condition at a node

Write $|t|$ for the number of keys of
a tree $t$ and $w(t) = |t| + 1$ for its weight. Let $N$ be the node with key $k$, left subtree
$L$ and right subtree $R$. Then $N$ is weight-balanced if and only if $L$ and $R$ are
weight-balanced, $4\,w(L) \le 3\,w(N)$ and $4\,w(R) \le 3\,w(N)$. This is the classical
$\mathrm{BB}[1/4]$ invariant: each child has weight at most three quarters of the weight of
the node.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.balanced_node_iff_weight`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#balanced-node-iff-weight).

## Weight-balanced rebalancing preserves the number of keys

Write $|t|$ for the number of
nodes of a binary tree $t$. For binary trees $l$ and $r$ and a key $k$, the weight-balanced
rebalancing of $l$, $k$, $r$ has exactly $|l| + |r| + 1$ nodes.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.numNodes_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#num-nodes-balance).

## Weight-balanced rebalancing restores balance

Let $L$ and $R$ be weight-balanced trees
and $k$ a key, and write $|t|$ for the number of keys of a tree $t$. If
$4(|L| + 1) \le 3(|L| + |R| + 2) + 1$ and $4(|R| + 1) \le 3(|L| + |R| + 2) + 1$, then the
rebalanced node $\mathrm{balance}(L, k, R)$ is weight-balanced.

These hypotheses are the two inequalities of the weight-balance invariant for the node with
children $L$ and $R$, each with its right-hand side increased by $1$; this is the precondition that
one insertion step maintains.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.balanced_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#balanced-balance).

## Membership after weight-balanced rebalancing

For binary trees $l$ and $r$ and a key $k$,
an element $x$ occurs in the weight-balanced rebalancing of $l$, $k$, $r$ exactly when $x$ occurs
in $l$, $x = k$, or $x$ occurs in $r$. Membership is structural: $x$ is the key of some node.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.mem_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#mem-balance).

## Weight-balanced rebalancing preserves ordering

Let the keys carry a linear order, let $l$
and $r$ be ordered binary trees (strict binary search trees), and let $k$ be a key such that every
key of $l$ is less than $k$ and every key of $r$ is greater than $k$. Then the weight-balanced
rebalancing of $l$, $k$, $r$ is ordered.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.ordered_balance`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#ordered-balance).

## Weight-balanced insertion adds at most one key

Let the keys carry a linear order. For
every key $x$ and every binary tree $t$, the tree obtained from $t$ by weight-balanced insertion
of $x$ has at most one more node than $t$.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.numNodes_insert_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#num-nodes-insert-le).

## Weight-balanced insertion does not decrease the number of keys

Let the keys
carry a linear order. For every key $x$ and every binary tree $t$, the number of nodes of $t$ is
at most the number of nodes of the tree obtained from $t$ by weight-balanced insertion of $x$.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.le_numNodes_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#le-num-nodes-insert).

## Weight-balanced insertion preserves balance

For every key $x$ of a linearly ordered
type and every weight-balanced tree $t$, the tree obtained by inserting $x$ into $t$ with
weight-balanced insertion is weight-balanced.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.balanced_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 541](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L541). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#balanced-insert).

## Membership after weight-balanced insertion

Let the keys carry a linear order. For all
keys $x$, $y$ and every binary tree $t$, $y$ occurs in the tree obtained from $t$ by
weight-balanced insertion of $x$ exactly when $y = x$ or $y$ occurs in $t$.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.mem_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#mem-insert).

## Weight-balanced insertion preserves the search-tree order

Let the keys be linearly
ordered. If a binary tree $t$ is ordered as a search tree (at every node, every key of the left
subtree is strictly smaller and every key of the right subtree strictly larger than the key at
the node), then the tree obtained from $t$ by weight-balanced insertion of any key $x$ is again
ordered.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.ordered_insert`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#ordered-insert).

## Weight-balanced trees built by insertion are balanced

For every list
$x_1, \dots, x_n$ of elements of a linearly ordered type, the tree obtained from the empty
tree by inserting $x_n, x_{n-1}, \dots, x_1$ in this order with weight-balanced insertion
is weight-balanced.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.balanced_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#balanced-from-list).

## Weight-balanced trees built from a list are ordered

Let the keys carry a linear order.
For every list $xs$, the weight-balanced tree built from $xs$ by repeated insertion is ordered,
that is, a strict binary search tree.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.ordered_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#ordered-from-list).

## Membership in a weight-balanced tree built from a list

Let the keys carry a linear
order. For every key $x$ and every list $xs$, $x$ occurs in the weight-balanced tree built from
$xs$ by repeated insertion exactly when $x$ is an element of $xs$.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.mem_fromList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 656](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L656). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#mem-from-list).

## Exponential weight lower bound for weight-balanced trees

Write $w(t)$ for the
weight of a binary tree $t$ (its number of keys plus one), and measure height so that the empty
tree has height $0$ and a node has height one more than the taller of its children. If $t$ is
weight balanced with parameter $1/4$ (at every node, each child has weight at most three
quarters of the weight of the node) and has height $k + 1$ for a natural number $k$, then
$w(t) \ge (4/3)^k$; in integer form, $4^k \le 3^k \, w(t)$.

The proof uses the weight form of the invariant: the taller child has weight at most three
quarters of the weight of the node.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.pow_height_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#pow-height-le).

## Height of a weight-balanced tree is logarithmic

Write $|t|$ for the number of keys of a
binary tree $t$ and $h(t)$ for its height, where the empty tree has height $0$ and a node has
height one more than the larger height of its two subtrees. If $t$ is weight-balanced, then
$h(t) \le \lfloor \log_2 ((|t| + 1)^3) \rfloor + 1$.

The proof passes from the exponential weight lower bound in base $4/3$ to base $2$, using
$(4/3)^3 > 2$.

Formalized by `Cslib.Algorithms.Lean.WeightBalancedTree.height_le_log2`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/WeightBalancedTree.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html#height-le-log2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weight-balanced tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/search-trees/weight-balanced-tree)
