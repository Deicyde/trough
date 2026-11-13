---
declaration: section
origin: cited
lean: MetaMathlibExt.BellMatrix, MetaMathlibExt.BellMatrix.h, MetaMathlibExt.BellMatrix.entry, MetaMathlibExt.bell_riordan_central_coefficient
statement: formalized
proof: formalized
---

# Bell matrices

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/bell-matrices/index.html).

## Bell matrix

Let $R$ be a commutative ring. A Bell matrix over $R$ is given by a formal
power series $g \in R[[X]]$ whose constant coefficient is a unit of $R$. The corresponding
Riordan-array pair is $(g, Xg)$.

Formalized by `MetaMathlibExt.BellMatrix`, a structure declared in [MathlibExt/NumberTheory/BellMatrix.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BellMatrix.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/bell-matrices/index.html#bell-matrix).

## Second component of a Bell matrix

For a Bell matrix over a commutative ring $R$ given by
the power series $g$, the second component of its Riordan-array pair is the power series
$h = Xg \in R[[X]]$.

Formalized by `MetaMathlibExt.BellMatrix.h`, a definition declared in [MathlibExt/NumberTheory/BellMatrix.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BellMatrix.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/bell-matrices/index.html#h).

## Entries of a Bell matrix

For a Bell matrix over a commutative ring $R$ given by the
power series $g$, and natural numbers $n$ and $k$, the entry in row $n$ and column $k$ is the
coefficient of $X^n$ in $g \cdot (Xg)^k$.

Formalized by `MetaMathlibExt.BellMatrix.entry`, a definition declared in [MathlibExt/NumberTheory/BellMatrix.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BellMatrix.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/bell-matrices/index.html#entry).

## Central coefficients of Bell matrices

Let $g \in \mathbb{Z}[[X]]$ be the power series of a
Bell matrix over $\mathbb{Z}$, with constant coefficient $g(0) = 1$, and let
$u \in \mathbb{Z}[[X]]$ be a power series with constant coefficient $0$ such that substituting
$u$ for $X$ in $X \, g(X)^{-1}$ gives $X$. Then for every natural number $n$, the entry of the
Bell matrix in row $2n$ and column $n$ equals $(n+1)$ times the coefficient of $X^{n+1}$ in $u$.

The source writes the right-hand side as $(n+1)\,[x^n]\,\tfrac{1}{x} u(x)$.

## Sources

- Paul Barry, "On the Central Coefficients of Bell Matrices," Journal of Integer Sequences 14 (2011), Article 11.4.3, Theorem `laterthm`, lines 167-169, <https://cs.uwaterloo.ca/journals/JIS/VOL14/Barry3/barry132.tex>.

Formalized by `MetaMathlibExt.bell_riordan_central_coefficient`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/BellRiordanCentralCoefficient.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/PowerSeries/BellRiordanCentralCoefficient.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/bell-matrices/index.html#bell-riordan-central-coefficient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bell matrices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/bell-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/bell-matrices)
