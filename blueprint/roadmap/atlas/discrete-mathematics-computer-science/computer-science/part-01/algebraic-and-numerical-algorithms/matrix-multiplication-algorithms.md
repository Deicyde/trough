---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate, Cslib.Algorithms.Lean.Matrix.matrixAccumulate, Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_apply, Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_ret, Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_time, Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_zero_inner, Cslib.Algorithms.Lean.Matrix.matrixAccumulate_ret, Cslib.Algorithms.Lean.Matrix.matrixAccumulate_time
statement: formalized
proof: formalized
---

# Matrix multiplication algorithms

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html).

## Rectangular matrix accumulation

Let $\alpha$ be a type with an addition and a
multiplication, and let $A$, $B$, $C$ be $p \times q$, $q \times r$ and $p \times r$ matrices over
$\alpha$, stored as vectors of rows. Rectangular matrix accumulation adds the product $AB$ to the
accumulator $C$: for $i < p$, then $j < r$, then $k < q$, each in increasing order, it replaces
$C_{ij}$ by $C_{ij} + A_{ik} B_{kj}$. It returns the final matrix together with a cost pair
(scalar multiplications, scalar additions), charging one of each for every such update.

Formalized by `Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#rectangular-matrix-accumulate).

## Square matrix accumulation

Let $\alpha$ be a type with an addition and a multiplication,
and let $A$, $B$, $C$ be $n \times n$ matrices over $\alpha$, stored as vectors of rows. Square
matrix accumulation on $A$, $B$, $C$ is rectangular matrix accumulation on $A$, $B$, $C$ with all
three dimensions equal to $n$: it adds $AB$ to the accumulator $C$ and returns the result with
its cost pair (scalar multiplications, scalar additions).

Formalized by `Cslib.Algorithms.Lean.Matrix.matrixAccumulate`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#matrix-accumulate).

## Entries of rectangular matrix accumulation

Let $\alpha$ be a commutative additive monoid
with a multiplication, and let $A$, $B$, $C$ be $p \times q$, $q \times r$ and $p \times r$
matrices over $\alpha$, stored as vectors of rows. For all $i < p$ and $j < r$, the $(i, j)$ entry
of the matrix returned by rectangular matrix accumulation on $A$, $B$, $C$ is
$C_{ij} + \sum_{k < q} A_{ik} B_{kj}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_apply`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#rectangular-matrix-accumulate-apply).

## Rectangular matrix accumulation computes $C + AB$

Let $\alpha$ be a commutative additive
monoid with a multiplication, and let $A$, $B$, $C$ be $p \times q$, $q \times r$ and $p \times r$
matrices over $\alpha$, stored as vectors of rows. The matrix returned by rectangular matrix
accumulation on $A$, $B$, $C$ equals $C + AB$, where $AB$ is the matrix product,
$(AB)_{ij} = \sum_{k < q} A_{ik} B_{kj}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#rectangular-matrix-accumulate-ret).

## Operation count of rectangular matrix accumulation

Let $\alpha$ be a type with an
addition and a multiplication, and let $A$, $B$, $C$ be $p \times q$, $q \times r$ and
$p \times r$ matrices over $\alpha$. Rectangular matrix accumulation on $A$, $B$, $C$ has cost
$(pqr, pqr)$: it charges exactly $pqr$ scalar multiplications and exactly $pqr$ scalar
additions.

Formalized by `Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#rectangular-matrix-accumulate-time).

## Rectangular matrix accumulation with zero inner dimension

Let $\alpha$ be a type with an
addition and a multiplication. If $A$ is a $p \times 0$ matrix, $B$ a $0 \times r$ matrix and $C$
a $p \times r$ matrix over $\alpha$, then rectangular matrix accumulation on $A$, $B$, $C$ returns
$C$ unchanged at cost $(0, 0)$.

Formalized by `Cslib.Algorithms.Lean.Matrix.rectangularMatrixAccumulate_zero_inner`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#rectangular-matrix-accumulate-zero-inner).

## Square matrix accumulation computes $C + AB$

Let $\alpha$ be a commutative additive
monoid with a multiplication, and let $A$, $B$, $C$ be $n \times n$ matrices over $\alpha$, stored
as vectors of rows. The matrix returned by square matrix accumulation on $A$, $B$, $C$ equals
$C + AB$, where $AB$ is the matrix product, $(AB)_{ij} = \sum_{k < n} A_{ik} B_{kj}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.matrixAccumulate_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#matrix-accumulate-ret).

## Operation count of square matrix accumulation

Let $\alpha$ be a type with an addition
and a multiplication, and let $A$, $B$, $C$ be $n \times n$ matrices over $\alpha$. Square matrix
accumulation on $A$, $B$, $C$ has cost $(n^3, n^3)$: it charges exactly $n^3$ scalar
multiplications and exactly $n^3$ scalar additions.

Formalized by `Cslib.Algorithms.Lean.Matrix.matrixAccumulate_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Multiply.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Multiply.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#matrix-accumulate-time).

## Recursive matrix multiply-accumulate

Let $\alpha$ be a type with an addition and a
multiplication, let $k$ be a natural number and $n = 2^k$, and let $A$, $B$, $C$ be $n \times n$
matrices over $\alpha$, stored as vectors of rows. The procedure adds the product of $A$ and $B$
to the accumulator $C$ by the eight-call recursion of CLRS. When $n = 1$, writing $a$, $b$, $c$
for the single entries of $A$, $B$, $C$, it replaces $c$ by $c + ab$. Otherwise it splits each
matrix $M$ into four $(n/2) \times (n/2)$ quadrants $M_{11}$ (top left), $M_{12}$ (top right),
$M_{21}$ (bottom left) and $M_{22}$ (bottom right), and updates, in this order,
$C_{11} \gets C_{11} + A_{11} B_{11}$, $C_{12} \gets C_{12} + A_{11} B_{12}$,
$C_{21} \gets C_{21} + A_{21} B_{11}$, $C_{22} \gets C_{22} + A_{21} B_{12}$, then
$C_{11} \gets C_{11} + A_{12} B_{21}$, $C_{12} \gets C_{12} + A_{12} B_{22}$,
$C_{21} \gets C_{21} + A_{22} B_{21}$, $C_{22} \gets C_{22} + A_{22} B_{22}$, each by a
recursive call on the accumulator left by the previous one. It returns the final accumulator
together with two counters: the number of scalar multiplications and the number of accumulator
additions.

Only these two operations are charged; calls, indexing and allocation are free.

Formalized by `Cslib.Algorithms.Lean.Matrix.recursiveMatrixAccumulate`, a definition declared in [CSLibExt/Algorithms/Lean/Matrix/Recursive.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Recursive.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#recursive-matrix-accumulate).

## Entries of the recursive matrix multiply-accumulate

Let $\alpha$ be an additive
commutative monoid with a multiplication, let $k$ be a natural number and $n = 2^k$, and let
$A = (a_{ij})$, $B = (b_{ij})$, $C = (c_{ij})$ be $n \times n$ matrices over $\alpha$, with
indices running from $0$ to $n - 1$. For all indices $i, j < n$, entry $(i, j)$ of the matrix
returned by the recursive multiply-accumulate procedure on $A$, $B$, $C$ equals
$c_{ij} + \sum_{t < n} a_{it} b_{tj}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.recursiveMatrixAccumulate_apply`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Recursive.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Recursive.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#recursive-matrix-accumulate-apply).

## Correctness of the recursive matrix multiply-accumulate

Let $\alpha$ be an additive
commutative monoid with a multiplication, let $k$ be a natural number and $n = 2^k$, and let
$A = (a_{ij})$, $B = (b_{ij})$, $C$ be $n \times n$ matrices over $\alpha$, with indices running
from $0$ to $n - 1$. Viewed as a matrix, the result returned by the recursive multiply-accumulate
procedure on $A$, $B$, $C$ equals $C + AB$, where $AB$ is the matrix product with entries
$(AB)_{ij} = \sum_{t < n} a_{it} b_{tj}$.

Formalized by `Cslib.Algorithms.Lean.Matrix.recursiveMatrixAccumulate_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Recursive.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Recursive.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#recursive-matrix-accumulate-ret).

## Operation count of the recursive matrix multiply-accumulate

Let $\alpha$ be a type with
an addition and a multiplication, let $k$ be a natural number and $n = 2^k$, and let $A$, $B$,
$C$ be $n \times n$ matrices over $\alpha$. The recursive multiply-accumulate procedure on $A$,
$B$, $C$ performs exactly $8^k$ scalar multiplications and exactly $8^k$ accumulator additions.
Since $8^k = n^3$, each count is the cube of the dimension.

Calls, indexing and allocation are uncharged.

Formalized by `Cslib.Algorithms.Lean.Matrix.recursiveMatrixAccumulate_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Matrix/Recursive.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Matrix/Recursive.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html#recursive-matrix-accumulate-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matrix multiplication algorithms](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/matrix-multiplication-algorithms)
