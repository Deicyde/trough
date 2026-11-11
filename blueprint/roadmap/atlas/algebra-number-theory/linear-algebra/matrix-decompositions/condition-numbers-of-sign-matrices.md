---
declaration: section
origin: cited
lean: Matrix.SignConditionNumber.SignMatrix, Matrix.SignConditionNumber.SignMatrix.realize, Matrix.SignConditionNumber.SignMatrix.realize_entries, Matrix.SignConditionNumber.exists_realize_iff, Matrix.SignConditionNumber.conditionNumber, Matrix.SignConditionNumber.minimumConditionNumber, Matrix.SignConditionNumber.conditionNumber_eq_top_of_smallest_eq_zero, Matrix.SignConditionNumber.conditionNumber_eq_ratio_of_smallest_ne_zero
statement: formalized
proof: formalized
---

# Condition numbers of sign matrices

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html).

## Boolean encoding of sign matrices

For a natural number $n$, a sign matrix of order $n$ is
encoded as an $n \times n$ matrix with entries in the Booleans $\{\mathrm{true}, \mathrm{false}\}$,
whose rows and columns are indexed by $\{0, \dots, n - 1\}$.

Formalized by `Matrix.SignConditionNumber.SignMatrix`, an abbreviation declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#sign-matrix).

## Real sign matrix of a Boolean matrix

The realization of a Boolean $n \times n$ matrix $A$
is the real $n \times n$ matrix whose $(i, j)$ entry is $-1$ if $A_{ij}$ is true and $1$ if
$A_{ij}$ is false.

Formalized by `Matrix.SignConditionNumber.SignMatrix.realize`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#realize).

## Realized sign matrices have entries $\pm 1$

For every Boolean $n \times n$ matrix $A$ and
all indices $i, j$, the $(i, j)$ entry of the real realization of $A$ is $1$ or $-1$.

Formalized by `Matrix.SignConditionNumber.SignMatrix.realize_entries`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#realize-entries).

## Boolean matrices realize exactly the sign matrices

Send each $n \times n$ Boolean
matrix to the real matrix whose entry is $-1$ where the Boolean entry is true and $1$ where it
is false. A real $n \times n$ matrix $M$ arises in this way if and only if every entry of $M$
is $1$ or $-1$.

Formalized by `Matrix.SignConditionNumber.exists_realize_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#exists-realize-iff).

## Condition number of a square real matrix

For a real $n \times n$ matrix $A$, let
$\sigma_0 \ge \sigma_1 \ge \dots$ be the singular values of $A$ acting on Euclidean space
$\mathbb{R}^n$, indexed from $0$ and extended by $\sigma_i = 0$ for $i \ge n$. The condition
number of $A$, an element of $[0, \infty]$, is $\infty$ if $\sigma_{n-1} = 0$ and
$\sigma_0 / \sigma_{n-1}$ otherwise, where $n - 1$ is read as $0$ when $n = 0$.

The minimum over sign matrices is only taken at positive order.

Formalized by `Matrix.SignConditionNumber.conditionNumber`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#condition-number).

## Minimum condition number of sign matrices

For a positive integer $n$, the minimum
condition number of order $n$ is the least condition number of a real $n \times n$ sign matrix,
that is, a matrix all of whose entries are $1$ or $-1$; the minimum is taken over the finitely
many such matrices.

Formalized by `Matrix.SignConditionNumber.minimumConditionNumber`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#minimum-condition-number).

## Infinite condition number from a vanishing singular value

Let $A$ be a real
$n \times n$ matrix with singular values $\sigma_0 \ge \sigma_1 \ge \dots$ on Euclidean space
$\mathbb{R}^n$, indexed from $0$ and extended by zeros, where $n - 1$ is read as $0$ when
$n = 0$. If $\sigma_{n-1} = 0$, then the condition number of $A$ is $\infty$.

Formalized by `Matrix.SignConditionNumber.conditionNumber_eq_top_of_smallest_eq_zero`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#condition-number-eq-top-of-smallest-eq-z).

## Condition number as a singular-value ratio

Let $A$ be a real $n \times n$ matrix with
singular values $\sigma_0 \ge \sigma_1 \ge \dots$ on Euclidean space $\mathbb{R}^n$, indexed from
$0$ and extended by zeros, where $n - 1$ is read as $0$ when $n = 0$. If $\sigma_{n-1} \ne 0$,
then the condition number of $A$ equals $\sigma_0 / \sigma_{n-1}$.

Formalized by `Matrix.SignConditionNumber.conditionNumber_eq_ratio_of_smallest_ne_zero`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#condition-number-eq-ratio-of-smallest-ne).

## The zero matrix has infinite condition number

For every natural number $n$, the
condition number of the real $n \times n$ zero matrix is $\infty$; this includes the
$0 \times 0$ matrix.

Formalized by `Matrix.SignConditionNumber.conditionNumber_zero`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#condition-number-zero).

## The minimum condition number is attained

For every positive integer $n$, there is an
$n \times n$ Boolean matrix whose realization as a real sign matrix ($-1$ for true, $1$ for
false) has condition number equal to the minimum condition number of order $n$.

Formalized by `Matrix.SignConditionNumber.minimumConditionNumber_attained`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#minimum-condition-number-attained).

## Condition numbers are at least one

For every natural number $n$ and every real
$n \times n$ matrix $A$, the condition number of $A$ is at least $1$.

Formalized by `Matrix.SignConditionNumber.one_le_conditionNumber`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#one-le-condition-number).

## The minimum condition number is at least one

For every positive integer $n$, the minimum
condition number of the real $n \times n$ sign matrices is at least $1$.

Formalized by `Matrix.SignConditionNumber.one_le_minimumConditionNumber`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#one-le-minimum-condition-number).

## Condition number of the order-one identity

The condition number of the $1 \times 1$
real identity matrix is $1$.

Formalized by `Matrix.SignConditionNumber.conditionNumber_one_order_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#condition-number-one-order-one).

## Minimum condition number of order one

The minimum condition number of order $1$ is $1$:
the least condition number of a $1 \times 1$ real sign matrix is $1$.

Formalized by `Matrix.SignConditionNumber.minimumConditionNumber_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumber.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#minimum-condition-number-one).

## Subpolynomial sequences

A sequence $f \colon \mathbb{N} \to [0, \infty)$ is subpolynomial
when for every real $\varepsilon > 0$ we have $f(n) = o(n^{\varepsilon})$ as $n \to \infty$.

Formalized by `Matrix.SignConditionNumber.IsSubpolynomial`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#is-subpolynomial).

## Admissible decay exponents

A real number $\alpha$ is an admissible exponent when there is a
subpolynomial sequence $f \colon \mathbb{N} \to [0, \infty)$ such that for every positive integer
$n$ the minimum condition number $\kappa_n$ of the real $n \times n$ sign matrices satisfies
$\kappa_n = 1 + f(n) / n^{\alpha}$, as an equality in $[0, \infty]$.

Formalized by `Matrix.SignConditionNumber.IsAdmissibleExponent`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#is-admissible-exponent).

## Decay exponent of minimum sign-matrix condition numbers

The decay exponent is the
supremum, taken in the extended reals $[-\infty, \infty]$, of the set of admissible exponents
$\alpha \in \mathbb{R}$.

The supremum need not be attained; it is $-\infty$ when no exponent is admissible.

Formalized by `Matrix.SignConditionNumber.decayExponent`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#decay-exponent).

## Hadamard hypothesis

The Hadamard hypothesis is the proposition that for every natural
number $n$ divisible by $4$ there is an $n \times n$ Hadamard matrix with integer entries, that is,
an integer matrix $H$ with all entries $\pm 1$ such that
$H H^{\mathsf{T}} = H^{\mathsf{T}} H = n I$.

This is the Hadamard conjecture, stated as a proposition to be used as a hypothesis.

Formalized by `Matrix.SignConditionNumber.HadamardHypothesis`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#hadamard-hypothesis).

## Symmetric conference matrices

A real $n \times n$ matrix $C$ is a symmetric conference
matrix when $n \ge 2$, $C^{\mathsf{T}} = C$, every diagonal entry of $C$ is $0$, every off-diagonal
entry of $C$ is $1$ or $-1$, and $C C^{\mathsf{T}} = (n - 1) I$, where $I$ is the identity
matrix.

Formalized by `Matrix.SignConditionNumber.IsSymmetricConference`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#is-symmetric-conference).

## Adding the identity to a symmetric conference matrix gives a sign matrix

If $C$ is a real
$n \times n$ symmetric conference matrix and $I$ is the $n \times n$ identity matrix, then there is
a Boolean $n \times n$ matrix whose realization as a real sign matrix equals $C + I$.

Formalized by `Matrix.SignConditionNumber.IsSymmetricConference.exists_realize_add_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SignConditionNumberDecay.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html#exists-realize-add-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Condition numbers of sign matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/matrix-decompositions/condition-numbers-of-sign-matrices)
