---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.OptimalBST.expectedSearchCost, Cslib.Algorithms.Lean.OptimalBST.optimalBST, Cslib.Algorithms.Lean.OptimalBST.optimalBST_empty, Cslib.Algorithms.Lean.OptimalBST.optimalBST_table_spec, Cslib.Algorithms.Lean.OptimalBST.optimalBST_minimal, Cslib.Algorithms.Lean.OptimalBST.optimalBST_time, Cslib.Algorithms.Lean.OptimalBST.optimalBST_time_bounds
statement: formalized
proof: formalized
---

# Optimal binary search tree

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html).

## Expected search cost of a binary search tree

Let $R$ be an additive commutative monoid,
let $n$ be a natural number, and let $p_0, \dots, p_{n-1} \in R$ (key weights) and
$q_0, \dots, q_n \in R$ (dummy-key weights) be given. Let $T$ be a binary tree whose nodes are
labelled by elements of $\{0, \dots, n-1\}$ and whose inorder traversal is $0, 1, \dots, n-1$, so
each key labels exactly one node and $T$ has exactly $n + 1$ empty subtrees. The depth of a node
or empty subtree is its distance from the root, the root having depth $0$; write $d(k)$ for the
depth of the node labelled $k$ and $\ell_0, \dots, \ell_n$ for the depths of the empty subtrees
listed from left to right. The expected search cost of $T$ is

$$\sum_{k=0}^{n-1} (d(k) + 1) \cdot p_k + \sum_{i=0}^{n} (\ell_i + 1) \cdot q_i,$$

where $m \cdot x$ denotes the $m$-fold sum of $x$ in $R$.

Formalized by `Cslib.Algorithms.Lean.OptimalBST.expectedSearchCost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Basic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Basic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html#expected-search-cost).

## Optimal binary search tree procedure

Let $R$ be a linearly ordered additive commutative
monoid in which addition is monotone, let $n$ be a natural number, and let
$p_0, \dots, p_{n-1}, q_0, \dots, q_n \in R$. The procedure (CLRS OPTIMAL-BST, with keys indexed
from $0$) fills a cost table $e$ of size $(n+1) \times (n+1)$, an auxiliary weight table $w$ of
the same size, and a root table of size $n \times n$ with entries in $\{0, \dots, n-1\}$ or
empty; all entries start as $0$ or empty. First it sets $e[a][a] = w[a][a] = q_a$ for
$a = 0, \dots, n$. Then for $\ell = 1, \dots, n$ in increasing order and, for each $\ell$, for
$a = 0, \dots, n - \ell$ in increasing order, with $b = a + \ell$, it sets
$w[a][b] = w[a][b-1] + p_{b-1} + q_b$ and examines the candidate roots $r = a, \dots, b-1$ in
increasing order, replacing the current best only when the candidate value
$e[a][r] + e[r+1][b] + w[a][b]$ is strictly smaller. It stores the resulting minimum in $e[a][b]$
and the earliest minimizing $r$ at position $(a, b-1)$ of the root table. The procedure returns
the cost table $e$ and the root table, with running time equal to the total number of candidate
roots examined.

Formalized by `Cslib.Algorithms.Lean.OptimalBST.optimalBST`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Basic.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Basic.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html#optimal-bst).

## Optimal BST with no keys

Let $R$ be a linearly ordered additive commutative monoid in
which addition is monotone. For $n = 0$ keys and a single dummy weight $q_0 \in R$, the optimal
binary search tree procedure returns the $1 \times 1$ cost table whose only entry is $q_0$, the
empty $0 \times 0$ root table, and running time $0$.

Formalized by `Cslib.Algorithms.Lean.OptimalBST.optimalBST_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Correctness.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Correctness.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html#optimal-bst-empty).

## Optimal BST table recurrence

Let $R$ be a linearly ordered additive commutative monoid
in which addition is monotone, let $n$ be a natural number, let
$p_0, \dots, p_{n-1}, q_0, \dots, q_n \in R$, and let $e$ and $\rho$ be the cost table and the
root table returned by the optimal binary search tree procedure on these weights. For
$a \le b \le n$ write $w(a, b) = \sum_{i=a}^{b-1} p_i + \sum_{i=a}^{b} q_i$. Then
$e[a][a] = q_a$ for every $a \le n$, and for all $a < b \le n$ there is an $r$ with
$a \le r < b$ such that $\rho[a][b-1] = r$, $e[a][b] = e[a][r] + e[r+1][b] + w(a, b)$, and for
every $t$ with $a \le t < b$

$$e[a][b] \le e[a][t] + e[t+1][b] + w(a, b),$$

with strict inequality when $t < r$. So $e[a][b]$ is the minimum of
$e[a][t] + e[t+1][b] + w(a, b)$ over $a \le t < b$, and $r$ is the earliest $t$ attaining it.

Formalized by `Cslib.Algorithms.Lean.OptimalBST.optimalBST_table_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Correctness.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Correctness.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html#optimal-bst-table-spec).

## The optimal BST procedure finds the minimum expected search cost

Let $R$ be a linearly
ordered additive commutative monoid in which addition is monotone, let $n$ be a natural number,
and let $p_0, \dots, p_{n-1}, q_0, \dots, q_n \in R$. Let $e$ be the cost table returned by the
optimal binary search tree procedure on these weights. Then $e[0][n]$ is the least expected
search cost, with key weights $p$ and dummy-key weights $q$, of a binary tree whose nodes are
labelled by elements of $\{0, \dots, n-1\}$ and whose inorder traversal is $0, 1, \dots, n-1$:
some such tree has expected search cost $e[0][n]$, and every such tree has expected search cost
at least $e[0][n]$.

Formalized by `Cslib.Algorithms.Lean.OptimalBST.optimalBST_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Correctness.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Correctness.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html#optimal-bst-minimal).

## Exact running time of the optimal BST procedure

Let $R$ be a linearly ordered additive
commutative monoid in which addition is monotone. For every natural number $n$ and all
$p_0, \dots, p_{n-1}, q_0, \dots, q_n \in R$, the running time of the optimal binary search tree
procedure on these weights, which is the number of candidate roots it examines, equals
$\binom{n+2}{3}$.

Formalized by `Cslib.Algorithms.Lean.OptimalBST.optimalBST_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Cost.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Cost.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html#optimal-bst-time).

## Cubic running time of the optimal BST procedure

Let $R$ be a linearly ordered additive
commutative monoid in which addition is monotone. For every natural number $n$ and all
$p_0, \dots, p_{n-1}, q_0, \dots, q_n \in R$, the running time $T$ of the optimal binary search
tree procedure on these weights, which is the number of candidate roots it examines, satisfies
$n^3 \le 6T$ and $T \le n^3$.

Formalized by `Cslib.Algorithms.Lean.OptimalBST.optimalBST_time_bounds`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Cost.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/OptimalBST/Cost.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html#optimal-bst-time-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Optimal binary search tree](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/dynamic-programming/optimal-binary-search-tree)
