---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MatrixChain.Parenthesization, Cslib.Algorithms.Lean.MatrixChain.Parenthesization.matrixIndices, Cslib.Algorithms.Lean.MatrixChain.Parenthesization.rows, Cslib.Algorithms.Lean.MatrixChain.Parenthesization.cols, Cslib.Algorithms.Lean.MatrixChain.Parenthesization.DimensionCompatible, Cslib.Algorithms.Lean.MatrixChain.Parenthesization.IsValid, Cslib.Algorithms.Lean.MatrixChain.scalarMultiplicationCost, Cslib.Algorithms.Lean.MatrixChain.Cost
statement: formalized
proof: formalized
---

# Matrix chain multiplication

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html).

## Parenthesization

A parenthesization of $n$ matrices is a full binary tree whose leaves are
labeled by indices in $\{0, \dots, n - 1\}$: either a single leaf naming matrix $i$, or a product
node with a left and a right parenthesization as factors. Labels may be repeated, omitted, or out
of order.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Parenthesization`, an inductive type declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#parenthesization).

## Leaf indices of a parenthesization

The leaf indices of a parenthesization of $n$ matrices
form the list of indices in $\{0, \dots, n - 1\}$ obtained by reading its leaves from left to
right: $[i]$ for a single leaf naming matrix $i$, and the concatenation of the lists of the left
and right factors for a product node.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Parenthesization.matrixIndices`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-indices).

## Row count of a parenthesization

Let $p = (p_0, \dots, p_n)$ be a vector of natural
numbers, regarding matrix $i$ (for $0 \le i < n$) as having $p_i$ rows and $p_{i+1}$ columns. The
row count of a parenthesization of $n$ matrices with respect to $p$ is $p_i$ for a single leaf
naming matrix $i$, and the row count of the left factor for a product node.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Parenthesization.rows`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#rows).

## Column count of a parenthesization

Let $p = (p_0, \dots, p_n)$ be a vector of natural
numbers, regarding matrix $i$ (for $0 \le i < n$) as having $p_i$ rows and $p_{i+1}$ columns. The
column count of a parenthesization of $n$ matrices with respect to $p$ is $p_{i+1}$ for a single
leaf naming matrix $i$, and the column count of the right factor for a product node.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Parenthesization.cols`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#cols).

## Dimension-compatible parenthesization

Let $p = (p_0, \dots, p_n)$ be a vector of natural
numbers, regarding matrix $i$ (for $0 \le i < n$) as having $p_i$ rows and $p_{i+1}$ columns. A
parenthesization of $n$ matrices is dimension-compatible with $p$ when, at every product node, the
column count of the left factor equals the row count of the right factor, where row and column
counts are taken with respect to $p$. A single leaf is always dimension-compatible.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Parenthesization.DimensionCompatible`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#dimension-compatible).

## Valid parenthesization

Let $p = (p_0, \dots, p_n)$ be a vector of natural numbers,
regarding matrix $i$ (for $0 \le i < n$) as having $p_i$ rows and $p_{i+1}$ columns. A
parenthesization of $n$ matrices is valid for $p$ when its leaf indices, read left to right, are
exactly $0, 1, \dots, n - 1$, and it is dimension-compatible with $p$.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Parenthesization.IsValid`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#is-valid).

## Scalar multiplication count of a parenthesization

Let $p = (p_0, \dots, p_n)$ be a vector
of natural numbers, regarding matrix $i$ (for $0 \le i < n$) as having $p_i$ rows and $p_{i+1}$
columns, and let $r(T)$ and $c(T)$ be the row and column counts of a parenthesization $T$ with
respect to $p$. The scalar multiplication count of a single leaf is $0$, and that of a product
node with factors $L$ and $R$ is the sum of the counts of $L$ and $R$ plus $r(L)\,c(L)\,c(R)$.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.scalarMultiplicationCost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#scalar-multiplication-cost).

## Matrix-chain cost

A matrix-chain cost is a pair of natural numbers counting the abstract
events charged by matrix-chain ordering and reconstruction: the number of split candidates
evaluated by the dynamic program, and the number of tree nodes emitted during reconstruction.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Cost`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#cost).

## Total matrix-chain cost

The total of a matrix-chain cost is its number of candidate
evaluations plus its number of reconstruction nodes.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Cost.total`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#total).

## Matrix-chain result

A matrix-chain result for $n$ matrices pairs a natural number, the
reported optimal scalar multiplication count, with a parenthesization of $n$ matrices, the
reported optimal parenthesization. The structure itself does not require the count to be minimal
or to be attained by the parenthesization.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.Result`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Basic.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#result).

## Matrix-chain ordering

Given $n \ge 1$ and natural numbers $p_0, \dots, p_n$, where matrix
$i$ of the chain ($0 \le i < n$) has $p_i$ rows and $p_{i+1}$ columns, the algorithm computes,
bottom-up by interval length, values $m_{i,j}$ for $0 \le i \le j < n$: $m_{i,i} = 0$ and, for
$i < j$, $m_{i,j}$ is the least value of $m_{i,k} + m_{k+1,j} + p_i p_{k+1} p_{j+1}$ over
$i \le k < j$, and the first split point $k$ attaining it is recorded. It then rebuilds a
parenthesization of the whole chain from the recorded split points and returns $m_{0,n-1}$
together with this parenthesization. One event is charged per evaluated split candidate and one
per reconstructed tree node.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order).

## Matrix-chain ordering returns a valid parenthesization

For every $n \ge 1$ and all
natural numbers $p_0, \dots, p_n$, the parenthesization returned by the matrix-chain ordering
algorithm on the dimensions $p_0, \dots, p_n$ is valid: its leaves are the matrices
$0, 1, \dots, n - 1$ in order, each exactly once, and at every multiplication node the column
count of the left factor equals the row count of the right factor, where matrix $i$ has $p_i$
rows and $p_{i+1}$ columns.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder_parenthesization_valid`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order-parenthesization-vali).

## Matrix-chain ordering reports the cost of its parenthesization

For every $n \ge 1$ and
all natural numbers $p_0, \dots, p_n$, the scalar-multiplication cost of the parenthesization
returned by the matrix-chain ordering algorithm on the dimensions $p_0, \dots, p_n$ equals the
optimal cost it reports.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder_cost_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order-cost-eq).

## Reported matrix-chain cost is a lower bound

For every $n \ge 1$, all natural numbers
$p_0, \dots, p_n$ and every parenthesization $T$ of $n$ matrices that is valid for these
dimensions, the optimal cost reported by the matrix-chain ordering algorithm on the dimensions
$p_0, \dots, p_n$ is at most the scalar-multiplication cost of $T$.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder_minimal`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order-minimal).

## Split candidates evaluated by matrix-chain ordering

For every $n \ge 1$ and all natural
numbers $p_0, \dots, p_n$, the matrix-chain ordering algorithm run on the dimensions
$p_0, \dots, p_n$ evaluates exactly $\binom{n+1}{3}$ split candidates.

This is the number of triples $i \le k < j < n$, so the dynamic program evaluates one candidate
for every interval split.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder_candidateEvaluations`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order-candidate-evaluations).

## Reconstruction size in matrix-chain ordering

For every $n \ge 1$ and all natural numbers
$p_0, \dots, p_n$, the matrix-chain ordering algorithm run on the dimensions $p_0, \dots, p_n$
charges exactly $2n - 1$ reconstruction events.

This is the number of nodes of a full binary tree with $n$ leaves.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder_reconstructionNodes`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order-reconstruction-nodes).

## Exact event count of matrix-chain ordering

For every $n \ge 1$ and all natural numbers
$p_0, \dots, p_n$, the total number of events charged by the matrix-chain ordering algorithm run
on the dimensions $p_0, \dots, p_n$ is $\binom{n+1}{3} + (2n - 1)$.

The first term counts evaluated split candidates and the second the nodes of the reconstructed
tree.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order-time).

## Cubic bound for matrix-chain ordering

For every $n \ge 1$ and all natural numbers
$p_0, \dots, p_n$, the total number of events charged by the matrix-chain ordering algorithm run
on the dimensions $p_0, \dots, p_n$ is at most $3n^3$.

Formalized by `Cslib.Algorithms.Lean.MatrixChain.matrixChainOrder_time_le_three_mul_cube`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MatrixChain/Correctness.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html#matrix-chain-order-time-le-three-mul-cub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matrix chain multiplication](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/dynamic-programming/matrix-chain-multiplication)
