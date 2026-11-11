---
declaration: section
origin: cited
lean: MetaMathlibExt.Matrix.det_toeplitzHessenberg_eq_sum_compositions_general, MetaMathlibExt.Matrix.det_toeplitzHessenberg_eq_sum_compositions, MetaMathlibExt.toeplitzHessenbergDet, MetaMathlibExt.toeplitzHessenbergDet_one, MetaMathlibExt.toeplitzHessenbergDet_two, MetaMathlibExt.toeplitzHessenbergDet_eq_sum_compositions, MetaMathlibExt.trudiPartitionSum, MetaMathlibExt.trudiPartitionSum_eq_sum_compositions
statement: formalized
proof: formalized
---

# Toeplitz–Hessenberg determinants

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html).

## Trudi's formula for Toeplitz–Hessenberg determinants, general case

Let $R$ be a
commutative ring, let $n \ge 0$, and let $a_0, a_1, a_2, \dots$ be any elements of $R$. Let $A_n$
be the $n \times n$ matrix whose entry in row $i$ and column $j$ ($0 \le i, j < n$) is $a_{i+1-j}$
if $j \le i + 1$ and $0$ otherwise; for $n = 0$ it is the empty matrix, whose determinant is $1$.
Then

$$\det A_n = \sum_{c} (-a_0)^{n - \ell(c)} \, a_{c_1} a_{c_2} \cdots a_{c_{\ell(c)}},$$

where $c = (c_1, \dots, c_{\ell(c)})$ runs over the compositions of $n$, that is, the finite
sequences of positive integers with sum $n$, and $\ell(c)$ is the number of parts of $c$.

No hypothesis $n \ge 1$ or $a_0 \ne 0$ is needed.

Formalized by `MetaMathlibExt.Matrix.det_toeplitzHessenberg_eq_sum_compositions_general`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#det-toeplitz-hessenberg-eq-sum-compositi).

## Trudi's formula for Toeplitz–Hessenberg determinants

Let $R$ be a commutative ring, let
$n \ge 1$, and let $a_0, a_1, a_2, \dots$ be elements of $R$ with $a_0 \ne 0$. Let $A_n$ be the
$n \times n$ matrix whose entry in row $i$ and column $j$ ($0 \le i, j < n$) is $a_{i+1-j}$ if
$j \le i + 1$ and $0$ otherwise. Then

$$\det A_n = \sum_{c} (-a_0)^{n - \ell(c)} \, a_{c_1} a_{c_2} \cdots a_{c_{\ell(c)}},$$

where $c = (c_1, \dots, c_{\ell(c)})$ runs over the compositions of $n$, that is, the finite
sequences of positive integers with sum $n$, and $\ell(c)$ is the number of parts of $c$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Some Hessenberg-Toeplitz Matrices with Motzkin Number Entries*, Journal of Integer Sequences 26 (2023), Article 23.3.4, matrix display `DetHess` lines 146–155, Lemma `lem1` lines 157–166 with equation `Trudi` at lines 159–161 and the equivalent composition sum at lines 163–165, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Shattuck/sh36.tex>.

Formalized by `MetaMathlibExt.Matrix.det_toeplitzHessenberg_eq_sum_compositions`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#det-toeplitz-hessenberg-eq-sum-compositi-2).

## Toeplitz–Hessenberg determinant

Let $R$ be a commutative ring, let $a_0, a_1, a_2, \dots$
be elements of $R$ and let $n \ge 0$. The Toeplitz–Hessenberg determinant $\det A_n$ is the
determinant of the $n \times n$ matrix $A_n = A_n(a_0; a_1, \dots, a_n)$ whose entry in row $i$
and column $j$ ($0 \le i, j < n$) is $a_{i+1-j}$ if $j \le i + 1$ and $0$ otherwise. Thus $a_0$
fills the superdiagonal, $a_1$ the diagonal, and every entry above the superdiagonal is $0$. For
$n = 0$ the determinant is $1$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Section 2, display (1) and the notation `D_±`.

Formalized by `MetaMathlibExt.toeplitzHessenbergDet`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#toeplitz-hessenberg-det).

## The $1 \times 1$ Toeplitz–Hessenberg determinant

For every commutative ring $R$ and every
sequence $a_0, a_1, a_2, \dots$ in $R$, the Toeplitz–Hessenberg determinant of size $1$ built
from $a$ is $\det A_1 = a_1$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Section 2, display (1).

Formalized by `MetaMathlibExt.toeplitzHessenbergDet_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#toeplitz-hessenberg-det-one).

## The $2 \times 2$ Toeplitz–Hessenberg determinant

For every commutative ring $R$ and every
sequence $a_0, a_1, a_2, \dots$ in $R$, the Toeplitz–Hessenberg determinant of size $2$ built
from $a$ is $\det A_2 = a_1^2 - a_0 a_2$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Section 2, display (1).

Formalized by `MetaMathlibExt.toeplitzHessenbergDet_two`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#toeplitz-hessenberg-det-two).

## Trudi's formula in composition form

Let $R$ be a commutative ring, let
$a_0, a_1, a_2, \dots$ be elements of $R$ and let $n \ge 0$. The Toeplitz–Hessenberg determinant
$\det A_n$ of size $n$ built from $a$ satisfies

$$\det A_n = \sum_{c} (-a_0)^{n - \ell(c)} \, a_{c_1} a_{c_2} \cdots a_{c_{\ell(c)}},$$

where $c = (c_1, \dots, c_{\ell(c)})$ runs over the compositions of $n$, that is, the finite
sequences of positive integers with sum $n$, and $\ell(c)$ is the number of parts of $c$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 1 and Section 3 (the composition form of the determinant).

Formalized by `MetaMathlibExt.toeplitzHessenbergDet_eq_sum_compositions`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#toeplitz-hessenberg-det-eq-sum-compositi).

## Trudi's partition sum

Let $R$ be a commutative semiring, let $s \in R$, let $n$ be a
natural number, and let $a : \mathbb{N} \to R$ (only $a_1, \dots, a_n$ enter). Trudi's
partition sum is

$$
\sum_{\alpha} s^{|\alpha|} \, m_n(\alpha) \, a_1^{\alpha_1} a_2^{\alpha_2} \cdots a_n^{\alpha_n},
$$

where $\alpha = (\alpha_1, \dots, \alpha_n)$ runs over the tuples of natural numbers with
$\alpha_1 + 2\alpha_2 + \cdots + n\alpha_n = n$, $|\alpha| = \alpha_1 + \cdots + \alpha_n$, and
$m_n(\alpha) = |\alpha|! / (\alpha_1! \cdots \alpha_n!)$ is the multinomial coefficient, taken in
$R$. Such a tuple records a partition of $n$ with $\alpha_i$ parts equal to $i$. For $n = 0$ the
sum has the single empty term and equals $1$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 1 (notation `α̃`, `|α|`, `m_n(α)`).

Formalized by `MetaMathlibExt.trudiPartitionSum`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#trudi-partition-sum).

## Trudi's partition sum as a sum over compositions

Let $R$ be a commutative semiring, let
$s \in R$, let $a_0, a_1, a_2, \dots$ be elements of $R$ and let $n \ge 0$. Trudi's partition sum

$$\sum_\alpha s^{|\alpha|} m_n(\alpha) \, a_1^{\alpha_1} a_2^{\alpha_2} \cdots a_n^{\alpha_n},$$

taken over the tuples $\alpha = (\alpha_1, \dots, \alpha_n)$ of nonnegative integers with
$\alpha_1 + 2\alpha_2 + \dots + n\alpha_n = n$, where $|\alpha| = \alpha_1 + \dots + \alpha_n$ and
$m_n(\alpha) = |\alpha|! / (\alpha_1! \cdots \alpha_n!)$, equals

$$\sum_c s^{\ell(c)} \, a_{c_1} a_{c_2} \cdots a_{c_{\ell(c)}},$$

where $c = (c_1, \dots, c_{\ell(c)})$ runs over the compositions of $n$, that is, the finite
sequences of positive integers with sum $n$, and $\ell(c)$ is the number of parts of $c$.

The multinomial coefficient $m_n(\alpha)$ counts the compositions of $n$ in which each part $i$
occurs $\alpha_i$ times.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 1 and the composition reading of `det(A_n)` in Section 3.

Formalized by `MetaMathlibExt.trudiPartitionSum_eq_sum_compositions`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 603](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L603). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#trudi-partition-sum-eq-sum-compositions).

## Brioschi's formula: the case $a_0 = 1$ of Trudi's formula

Let $R$ be a commutative ring
and let $a_0, a_1, a_2, \dots$ be elements of $R$ with $a_0 = 1$. For every $n \ge 0$, the
Toeplitz–Hessenberg determinant $\det A_n$ of size $n$ built from $a$ satisfies

$$\det A_n = (-1)^n \sum_\alpha (-1)^{|\alpha|} m_n(\alpha) a_1^{\alpha_1} \cdots a_n^{\alpha_n},$$

where the sum, Trudi's partition sum with weight $-1$ per part, runs over the tuples
$\alpha = (\alpha_1, \dots, \alpha_n)$ of nonnegative integers with
$\alpha_1 + 2\alpha_2 + \dots + n\alpha_n = n$, with $|\alpha| = \alpha_1 + \dots + \alpha_n$ and
$m_n(\alpha) = |\alpha|! / (\alpha_1! \cdots \alpha_n!)$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 1 with `a_0 = 1` (the sign `D_+`).

Formalized by `MetaMathlibExt.toeplitzHessenbergDet_eq_neg_one_pow_mul_trudiPartitionSum`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#toeplitz-hessenberg-det-eq-neg-one-pow-m).

## Trudi's formula when $a_0 = -1$

Let $R$ be a commutative ring and let
$a_0, a_1, a_2, \dots$ be elements of $R$ with $a_0 = -1$. For every $n \ge 0$, the
Toeplitz–Hessenberg determinant $\det A_n$ of size $n$ built from $a$ satisfies

$$\det A_n = \sum_\alpha m_n(\alpha) \, a_1^{\alpha_1} a_2^{\alpha_2} \cdots a_n^{\alpha_n},$$

where the sum, Trudi's partition sum with weight $1$ per part, runs over the tuples
$\alpha = (\alpha_1, \dots, \alpha_n)$ of nonnegative integers with
$\alpha_1 + 2\alpha_2 + \dots + n\alpha_n = n$, with $|\alpha| = \alpha_1 + \dots + \alpha_n$ and
$m_n(\alpha) = |\alpha|! / (\alpha_1! \cdots \alpha_n!)$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 1 with `a_0 = -1` (the sign `D_-`).

Formalized by `MetaMathlibExt.toeplitzHessenbergDet_eq_trudiPartitionSum_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#toeplitz-hessenberg-det-eq-trudi-partiti).

## Two values of Trudi's partition sum

For an integer $s$, integers $a_1, a_2, \dots$ and
$n \ge 0$, write
$T_n(s; a) = \sum_\alpha s^{|\alpha|} m_n(\alpha) \, a_1^{\alpha_1} \cdots a_n^{\alpha_n}$ for
Trudi's partition sum, where $\alpha = (\alpha_1, \dots, \alpha_n)$ runs over the tuples of
nonnegative integers with $\alpha_1 + 2\alpha_2 + \dots + n\alpha_n = n$, with
$|\alpha| = \alpha_1 + \dots + \alpha_n$ and
$m_n(\alpha) = |\alpha|! / (\alpha_1! \cdots \alpha_n!)$. Then $T_4(1; a) = 8$, the number of
compositions of $4$, when $a_i = 1$ for all $i$; and $T_3(-1; a) = -1 + 4 - 3 = 0$ when $a_i = i$
for all $i$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 1.

Formalized by `MetaMathlibExt.trudiPartitionSum_examples`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/TrudiBrioschiDeterminant.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html#trudi-partition-sum-examples).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Toeplitz–Hessenberg determinants](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/toeplitz-hessenberg-determinants)
