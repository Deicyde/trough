---
declaration: section
origin: cited
lean: MetaMathlibExt.zagierMatrix, MetaMathlibExt.zagierInverseP, MetaMathlibExt.zagierInverseQ, MetaMathlibExt.zagierInverseP_eq_zagierInverseQ, MetaMathlibExt.zagierInverseP_mul_zagierMatrix, MetaMathlibExt.zagierMatrix_mul_zagierInverseP, MetaMathlibExt.zagier_matrix_inverse
statement: formalized
proof: formalized
---

# Zagier's matrix and Bernoulli numbers

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html).

## Zagier's matrix

For a natural number $K$, Zagier's matrix $A_K$ is the rational matrix
with rows and columns indexed by $1 \le i, j \le K - 1$ (empty when $K \le 1$) whose
$(i, j)$ entry is

$$(A_K)_{ij} = \binom{2K - 2j}{2i - 1} + \binom{2K - 2j}{2K - 2i},$$

where $\binom{m}{k} = 0$ for $k > m$.

Formalized by `MetaMathlibExt.zagierMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html#zagier-matrix).

## First Bernoulli formula for the inverse of Zagier's matrix

For a natural number $K$,
$P_K$ is the rational matrix with rows and columns indexed by $1 \le i, j \le K - 1$ (empty
when $K \le 1$) whose $(i, j)$ entry is

$$(P_K)_{ij} = \frac{2}{2i-1} \sum_{n=0}^{2K-2i} \binom{2j-1}{2K-2i-n+1} \binom{n+2i-2}{n} B_n,$$

where $B_n$ is the $n$-th Bernoulli number with $B_1 = -\frac{1}{2}$ and $\binom{m}{k} = 0$
for $k > m$.

Formalized by `MetaMathlibExt.zagierInverseP`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html#zagier-inverse-p).

## Second Bernoulli formula for the inverse of Zagier's matrix

For a natural number $K$,
$Q_K$ is the rational matrix with rows and columns indexed by $1 \le i, j \le K - 1$ (empty
when $K \le 1$) whose $(i, j)$ entry is

$$(Q_K)_{ij} = -\frac{2}{2i-1} \sum_{n=0}^{2K-2i} \binom{2K-2j}{2K-2i-n+1} \binom{n+2i-2}{n} B_n,$$

where $B_n$ is the $n$-th Bernoulli number with $B_1 = -\frac{1}{2}$ and $\binom{m}{k} = 0$
for $k > m$.

Formalized by `MetaMathlibExt.zagierInverseQ`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean, line 656](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean#L656). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html#zagier-inverse-q).

## The two Bernoulli formulas for the inverse of Zagier's matrix agree

For every natural
number $K$, the matrices $P_K$ and $Q_K$ given by the first and second Bernoulli formulas
for the inverse of Zagier's matrix are equal: $P_K = Q_K$.

Formalized by `MetaMathlibExt.zagierInverseP_eq_zagierInverseQ`, a lemma declared in [MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html#zagier-inverse-p-eq-zagier-inverse-q).

## Left inverse of Zagier's matrix

For every natural number $K$, the matrix $P_K$
given by the first Bernoulli formula is a left inverse of Zagier's matrix $A_K$:
$P_K A_K = I$, where $I$ is the $(K - 1) \times (K - 1)$ identity matrix.

Formalized by `MetaMathlibExt.zagierInverseP_mul_zagierMatrix`, a lemma declared in [MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean, line 815](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean#L815). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html#zagier-inverse-p-mul-zagier-matrix).

## Right inverse of Zagier's matrix

For every natural number $K$, the matrix $P_K$
given by the first Bernoulli formula is a right inverse of Zagier's matrix $A_K$:
$A_K P_K = I$, where $I$ is the $(K - 1) \times (K - 1)$ identity matrix.

Formalized by `MetaMathlibExt.zagierMatrix_mul_zagierInverseP`, a lemma declared in [MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean, line 854](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean#L854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html#zagier-matrix-mul-zagier-inverse-p).

## Zagier's matrix conjecture

Let $K$ be a natural number, let $B_n$ be the $n$-th
Bernoulli number with $B_1 = -\frac{1}{2}$, and let $\binom{m}{k} = 0$ for $k > m$. Let $A$,
$P$ and $Q$ be the $(K - 1) \times (K - 1)$ rational matrices, with rows and columns indexed
by $1 \le i, j \le K - 1$, whose entries are

$$A_{ij} = \binom{2K - 2j}{2i - 1} + \binom{2K - 2j}{2K - 2i},$$



$$P_{ij} = \frac{2}{2i-1} \sum_{n=0}^{2K-2i} \binom{2j-1}{2K-2i-n+1} \binom{n+2i-2}{n} B_n,$$



$$Q_{ij} = -\frac{2}{2i-1} \sum_{n=0}^{2K-2i} \binom{2K-2j}{2K-2i-n+1} \binom{n+2i-2}{n} B_n.$$

Then $P = Q$, $AP = I$ and $PA = I$, where $I$ is the identity matrix; that is, the two
Bernoulli formulas agree and give the two-sided inverse of $A$.

The source assumes $K \ge 2$. The assumption is not needed: for $K \le 1$ the matrices are
empty.

## Sources

- Yawen Ma and Lee-Peng Teo, "Another Proof of Zagier's Matrix Conjecture," Journal of Integer Sequences 25 (2022), Article 22.6.4, Theorem [Zagier's conjecture], equations (eq12) and (eq13), lines 279–285, https://cs.uwaterloo.ca/journals/JIS/VOL25/Teo/teo4.tex

Formalized by `MetaMathlibExt.zagier_matrix_inverse`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean, line 872](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ZagierMatrixInverse.lean#L872). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html#zagier-matrix-inverse).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zagier's matrix and Bernoulli numbers](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/zagier-s-matrix-and-bernoulli-numbers)
