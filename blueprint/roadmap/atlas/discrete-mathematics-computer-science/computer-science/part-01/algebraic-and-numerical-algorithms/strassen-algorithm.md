---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate, Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate_ret, Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate_apply, Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate_time
statement: formalized
proof: formalized
---

# Strassen algorithm

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/strassen-algorithm/index.html).

## Strassen's matrix accumulator

Let $R$ be a type with a zero, an addition, a subtraction
and a multiplication (no ring axioms are assumed). For $k \ge 0$ and $2^k \times 2^k$ matrices
$A$, $B$, $C$ over $R$, this procedure runs Strassen's seven-product recursion for adding $AB$ to
$C$. It returns a $2^k \times 2^k$ matrix together with a pair of counts: the number of scalar
multiplications and the number of scalar additions and subtractions it performs.
For $k = 0$, with $a$, $b$, $c$ the single entries of $A$, $B$, $C$, it performs one
multiplication and one addition and returns the $1 \times 1$ matrix with entry $c + ab$.
For $k + 1$, write $X_{11}, X_{12}, X_{21}, X_{22}$ for the top-left, top-right, bottom-left and
bottom-right $2^k \times 2^k$ blocks of a matrix $X$. The procedure forms, entrywise,
$S_1 = B_{12} - B_{22}$, $S_2 = A_{11} + A_{12}$, $S_3 = A_{21} + A_{22}$,
$S_4 = B_{21} - B_{11}$, $S_5 = A_{11} + A_{22}$, $S_6 = B_{11} + B_{22}$,
$S_7 = A_{12} - A_{22}$, $S_8 = B_{21} + B_{22}$, $S_9 = A_{11} - A_{21}$ and
$S_{10} = B_{11} + B_{12}$; obtains $P_1, \dots, P_7$ by seven recursive calls with the zero
matrix as accumulator on the pairs $(A_{11}, S_1)$, $(S_2, B_{22})$, $(S_3, B_{11})$,
$(A_{22}, S_4)$, $(S_5, S_6)$, $(S_7, S_8)$ and $(S_9, S_{10})$; and returns the matrix with
blocks $C_{11} + P_5 + P_4 - P_2 + P_6$, $C_{12} + P_1 + P_2$, $C_{21} + P_3 + P_4$ and
$C_{22} + P_5 + P_1 - P_3 - P_7$, each sum formed entrywise from left to right.
Each entrywise scalar addition or subtraction adds one to the second count and each base-case
multiplication adds one to the first; indexing, allocation, copying and zero-fill are uncharged.

Formalized by `Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Strassen/Basic.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Strassen/Basic.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/strassen-algorithm/index.html#strassen-matrix-accumulate).

## Correctness of Strassen's matrix accumulator

Let $R$ be a non-unital, non-associative
ring. For every $k \ge 0$ and all $2^k \times 2^k$ matrices $A$, $B$, $C$ over $R$, the matrix
returned by Strassen's accumulator on $A$, $B$, $C$ equals $C + AB$, where $AB$ is the usual
matrix product, $(AB)_{ij} = \sum_t A_{it} B_{tj}$.

Multiplication in $R$ need not be commutative or associative.

Formalized by `Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Strassen/Correctness.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Strassen/Correctness.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/strassen-algorithm/index.html#strassen-matrix-accumulate-ret).

## Entries of Strassen's matrix accumulator

Let $R$ be a non-unital, non-associative ring.
For every $k \ge 0$, all $2^k \times 2^k$ matrices $A$, $B$, $C$ over $R$ and all indices
$i, j$, the $(i, j)$ entry of the matrix returned by Strassen's accumulator on $A$, $B$, $C$ is
$C_{ij} + \sum_{t} A_{it} B_{tj}$, the sum running over all $2^k$ indices $t$.

Formalized by `Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate_apply`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Strassen/Correctness.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Strassen/Correctness.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/strassen-algorithm/index.html#strassen-matrix-accumulate-apply).

## Operation counts of Strassen's matrix accumulator

Let $R$ be a type with a zero, an
addition, a subtraction and a multiplication. For every $k \ge 0$ and all $2^k \times 2^k$
matrices $A$, $B$, $C$ over $R$, Strassen's accumulator on $A$, $B$, $C$ performs exactly $7^k$
scalar multiplications and exactly $(25 \cdot 7^k - 22 \cdot 4^k)/3$ scalar additions and
subtractions.

This count does not charge allocation or bit operations.

Formalized by `Cslib.Algorithms.Lean.Matrix.strassenMatrixAccumulate_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Strassen/Costs.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Strassen/Costs.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/strassen-algorithm/index.html#strassen-matrix-accumulate-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strassen algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/strassen-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/strassen-algorithm)
