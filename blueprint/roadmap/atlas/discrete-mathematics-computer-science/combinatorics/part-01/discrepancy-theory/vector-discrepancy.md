---
declaration: section
origin: cited
lean: MatrixDiscrepancy.vectorDiscrepancy, MatrixDiscrepancy.vectorDiscrepancy_attained
statement: formalized
proof: formalized
---

# Vector discrepancy

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/vector-discrepancy/index.html).

## Vector discrepancy

For a real $m \times n$ matrix $A$, the vector discrepancy of $A$ is
the infimum, over all families $u_1, \dots, u_n$ of unit vectors in the Euclidean space
$\mathbb{R}^n$, of $\max_{1 \le i \le m} \lVert \sum_{j=1}^{n} A_{ij} u_j \rVert$ (taken to be $0$
when $m = 0$), where $\lVert \cdot \rVert$ is the Euclidean norm; it is an element of
$[0, \infty]$.

Formalized by `MatrixDiscrepancy.vectorDiscrepancy`, a definition declared in [MathlibExt/Combinatorics/VectorDiscrepancy.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VectorDiscrepancy.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/vector-discrepancy/index.html#vector-discrepancy).

## The vector discrepancy is attained

Let $A$ be a real $m \times n$ matrix with $n \ge 1$.
Then there are unit vectors $u_1, \dots, u_n$ in the Euclidean space $\mathbb{R}^n$ such that
the vector discrepancy of $A$ equals $\max_{1 \le i \le m} \lVert \sum_{j=1}^{n} A_{ij} u_j \rVert$
(taken to be $0$ when $m = 0$), where $\lVert \cdot \rVert$ is the Euclidean norm.

Formalized by `MatrixDiscrepancy.vectorDiscrepancy_attained`, a theorem declared in [MathlibExt/Combinatorics/VectorDiscrepancy.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VectorDiscrepancy.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/vector-discrepancy/index.html#vector-discrepancy-attained).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vector discrepancy](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/vector-discrepancy/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/discrepancy-theory/vector-discrepancy)
