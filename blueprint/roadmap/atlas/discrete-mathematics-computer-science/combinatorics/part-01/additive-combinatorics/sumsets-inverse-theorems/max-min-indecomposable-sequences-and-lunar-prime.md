---
declaration: section
origin: cited
lean: MetaMathlibExt.maxMinMul, MetaMathlibExt.maxMinMul_zero, MetaMathlibExt.maxMinMul_one, MetaMathlibExt.IsMaxMinMonomial, MetaMathlibExt.not_isMaxMinMonomial_zero, MetaMathlibExt.IsMaxMinIndecomposable, MetaMathlibExt.not_isMaxMinIndecomposable_zero, MetaMathlibExt.digitSeq
statement: formalized
---

# Max-min indecomposable sequences and lunar primes

34 results, 22 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html).

## Max-min product

The max-min product of sequences $g, h \colon \mathbb{N} \to \mathbb{N}$
is the sequence $g \otimes h$ with $(g \otimes h)_k = \max_{i + j = k} \min(g_i, h_j)$ for every
$k \in \mathbb{N}$, the maximum running over pairs of natural numbers $(i, j)$. This is the product
of the max-min semiring $(\mathbb{N}, \max, \min)$ on coefficient sequences.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 1 (the max-min semiring and its polynomials).

Formalized by `MetaMathlibExt.maxMinMul`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#max-min-mul).

## Constant coefficient of a max-min product

For all sequences
$g, h \colon \mathbb{N} \to \mathbb{N}$, the max-min product satisfies
$(g \otimes h)_0 = \min(g_0, h_0)$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 1 (the max-min semiring and its polynomials).

Formalized by `MetaMathlibExt.maxMinMul_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#max-min-mul-zero).

## Linear coefficient of a max-min product

For all sequences
$g, h \colon \mathbb{N} \to \mathbb{N}$, the max-min product satisfies
$(g \otimes h)_1 = \max(\min(g_0, h_1), \min(g_1, h_0))$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 1 (the max-min semiring and its polynomials).

Formalized by `MetaMathlibExt.maxMinMul_one`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#max-min-mul-one).

## Monomials over the max-min semiring

A coefficient sequence
$g : \mathbb{N} \to \mathbb{N}$ over the max-min semiring is a monomial when exactly one of its
entries is nonzero, that is, when it is $c x^i$ for some index $i$ and some coefficient $c \neq 0$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 1 (definition of indecomposable).

Formalized by `MetaMathlibExt.IsMaxMinMonomial`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#is-max-min-monomial).

## The zero sequence is not a monomial

The zero coefficient sequence
$\mathbb{N} \to \mathbb{N}$ is not a max-min monomial: a monomial has exactly one nonzero
entry, and the zero sequence has none.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 1 (definition of indecomposable).

Formalized by `MetaMathlibExt.not_isMaxMinMonomial_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#not-is-max-min-monomial-zero).

## Max-min indecomposable sequences

A coefficient sequence $f : \mathbb{N} \to \mathbb{N}$
is indecomposable (in the arXiv version: irreducible) when for all sequences
$g, h : \mathbb{N} \to \mathbb{N}$ with $g \otimes h = f$, where $\otimes$ is the max-min product,
$g$ or $h$ is a max-min monomial, that is, a sequence with exactly one nonzero term.

Factors range over all sequences $\mathbb{N} \to \mathbb{N}$; for a natural number $b$ and $f$
with all terms less than $b$, this is equivalent to factoring over $\{0, \dots, b - 1\}$, by
applying the digit map $x \mapsto \min(x, b - 1)$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 1 (definition of indecomposable).

Formalized by `MetaMathlibExt.IsMaxMinIndecomposable`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#is-max-min-indecomposable).

## The zero sequence is decomposable

The zero coefficient sequence
$\mathbb{N} \to \mathbb{N}$ is not indecomposable over the max-min semiring: it factors as
$0 = 0 \otimes 0$, where $\otimes$ is the max-min product, and the zero sequence is not a
monomial.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 1 (definition of indecomposable).

Formalized by `MetaMathlibExt.not_isMaxMinIndecomposable_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#not-is-max-min-indecomposable-zero).

## Coefficient sequence of a digit string

Let $n$ and $b$ be natural numbers. The
coefficient sequence of a digit string $a = (a_0, \dots, a_{n-1})$ with digits in
$\{0, \dots, b - 1\}$ is the sequence $\mathbb{N} \to \mathbb{N}$ whose $k$-th term is $a_k$ for
$k < n$ and $0$ for $k \ge n$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (lunar numbers `ℒ_b` as polynomials over `ℬ_b = {0, …, b - 1}`).

Formalized by `MetaMathlibExt.digitSeq`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#digit-seq).

## A digit string has no coefficients beyond its length

Let $n$ and $b$ be natural numbers
and let $a = (a_0, \dots, a_{n-1})$ be a digit string with digits in $\{0, \dots, b - 1\}$. Then
for every $k \ge n$, the $k$-th term of the coefficient sequence of $a$ is $0$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (lunar numbers `ℒ_b` as polynomials over `ℬ_b = {0, …, b - 1}`).

Formalized by `MetaMathlibExt.digitSeq_of_le`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#digit-seq-of-le).

## Lunar unit

For a natural number $b$, the lunar unit of base $b$ is the coefficient sequence
$\mathbb{N} \to \mathbb{N}$ whose constant term is $b - 1$ and whose other terms are all $0$, that
is, the constant polynomial $b - 1$ over the max-min semiring. The subtraction is truncated, so
the lunar unit of base $0$ is the zero sequence.

For sequences with all terms less than $b$, the lunar unit is the identity of the max-min product.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (definition of prime lunar numbers).

Formalized by `MetaMathlibExt.lunarUnit`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-unit).

## The lunar unit is a monomial

For every natural number $b \ge 2$, the lunar unit of base
$b$, the sequence with constant term $b - 1$ and all other terms $0$, is a max-min monomial: it
has exactly one nonzero term.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (definition of prime lunar numbers).

Formalized by `MetaMathlibExt.isMaxMinMonomial_lunarUnit`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#is-max-min-monomial-lunar-unit).

## Lunar primes

Let $b$ be a natural number. The lunar unit of base $b$ is the constant
polynomial $b - 1$, the sequence with constant term $b - 1$ and all other terms $0$. A coefficient
sequence $f : \mathbb{N} \to \mathbb{N}$ is a lunar prime of base $b$ (Applegate, LeBrun and
Sloane) when for all sequences $g, h : \mathbb{N} \to \mathbb{N}$ with all terms less than $b$ and
$g \otimes h = f$, where $\otimes$ is the max-min product, $g$ or $h$ is the lunar unit.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (definition of prime lunar numbers).

Formalized by `MetaMathlibExt.IsLunarPrime`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#is-lunar-prime).

## Zero is not a lunar prime

For every integer $b \ge 2$, the zero sequence is not a lunar
prime of base $b$: $0 = 0 \otimes 0$, where $\otimes$ is the max-min product, and $0$ is not the
lunar unit, the constant polynomial $b - 1$ with coefficient sequence $(b - 1, 0, 0, \dots)$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (definition of prime lunar numbers).

Formalized by `MetaMathlibExt.not_isLunarPrime_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#not-is-lunar-prime-zero).

## Lunar prime candidates

Let $b$ be a natural number. A coefficient sequence
$f : \mathbb{N} \to \mathbb{N}$ is a prime candidate in base $b$ when its constant term $f_0$ is
nonzero and some term $f_i$ equals $b - 1$, where the subtraction is truncated, so that
$b - 1 = 0$ when $b = 0$. For $f$ with all terms less than $b$, the second condition says that
the largest coefficient of $f$ is $b - 1$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (definition of prime candidate).

Formalized by `MetaMathlibExt.IsLunarPrimeCandidate`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#is-lunar-prime-candidate).

## The lunar unit is a prime candidate

For every natural number $b \ge 2$, the lunar unit
of base $b$, the sequence with constant term $b - 1$ and all other terms $0$, is a prime candidate
in base $b$: its constant term is nonzero and one of its terms equals $b - 1$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2 (definition of prime candidate).

Formalized by `MetaMathlibExt.isLunarPrimeCandidate_lunarUnit`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#is-lunar-prime-candidate-lunar-unit).

## Shitov's theorem: almost all Boolean polynomials with nonzero constant term are prime

For $n \in \mathbb{N}$, consider the Boolean polynomials of degree exactly $n$ with nonzero
constant term, that is, the base-$2$ lunar numbers given by digit strings
$(a_0, \dots, a_n) \in \{0, 1\}^{n+1}$ with $a_0 \ne 0$ and $a_n \ne 0$. The proportion of
these which are lunar primes in base $2$ tends to $1$ as $n \to \infty$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Theorem 10 (`jis-2025-25.2.7-thm-10`), quoting Shitov (2014), Theorem 2.5.

Stated but not proved: `MetaMathlibExt.shitov_boolean_prime_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#shitov-boolean-prime-density).

## Almost all max-min polynomials are indecomposable

Fix an integer $b \ge 2$. For each
$n$, among the polynomials of degree $n$ with coefficients in $\mathcal{B}_b = \{0, \dots, b - 1\}$,
that is, coefficient strings $(a_0, \dots, a_n)$ with $a_n \ne 0$, the proportion of those that
are indecomposable over the max-min semiring tends to $1$ as $n \to \infty$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Theorem 11 (`jis-2025-25.2.7-thm-11`).

Stated but not proved: `MetaMathlibExt.maxMin_indecomposable_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#max-min-indecomposable-density).

## Asymptotic count of lunar primes

Fix an integer $b \ge 2$. For $n \ge 1$ let $\pi_b(n)$
be the number of digit strings $(a_0, \dots, a_{n-1})$ with $a_k \in \{0, \dots, b - 1\}$ and
leading digit $a_{n-1} \ne 0$ whose coefficient sequence $(a_0, \dots, a_{n-1}, 0, 0, \dots)$ is a
lunar prime of base $b$; these are the prime lunar numbers of base $b$ with $n$ digits. Then
$\pi_b(n) \sim (b - 1)^2 b^{n-2}$ as $n \to \infty$, as conjectured by Applegate, LeBrun and
Sloane.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Corollary 12 (`jis-2025-25.2.7-cor-12`).

Stated but not proved: `MetaMathlibExt.lunar_prime_count_isEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-prime-count-is-equivalent).

## Monotone digit maps are lunar homomorphisms

Let $d : \mathbb{N} \to \mathbb{N}$ be
nondecreasing, and for a coefficient sequence $f : \mathbb{N} \to \mathbb{N}$ write $d(f)$ for the
sequence $k \mapsto d(f_k)$. Write $f \oplus g$ for the pointwise maximum and $f \otimes g$ for the
max-min product of coefficient sequences $f$ and $g$. Then for all $f$ and $g$,
$d(f) \oplus d(g) = d(f \oplus g)$ and $d(f) \otimes d(g) = d(f \otimes g)$.

This is Theorem 15 (Applegate, LeBrun and Sloane, prime promotion), stated for every nondecreasing
map on $\mathbb{N}$; a base-$b$ digit map, a nondecreasing map on the digits, extends to such a map.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Theorem 15 (`jis-2025-25.2.7-thm-15`).

Stated but not proved: `MetaMathlibExt.digitMap_lunar_hom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#digit-map-lunar-hom).

## Counting Boolean factor pairs with a small sumset

Let $n$ and $k$ be natural numbers with
$0 < k \le n$, and let $d > 0$ be a real number. Then the number of pairs $(A, B)$ of finite sets
of natural numbers such that $0 \in A$, the largest element of $A$ is $k$, the largest element of
$B$ is $n - k$, and $|A + B| \le |A| + |B| + d$, where $A + B = \{a + b : a \in A, b \in B\}$ is
the sumset, is at most $n^{2d+2} 2^k$.

This is Lemma 19 for Boolean polynomials $f$ and $g$ recorded by their supports $A$ and $B$: the
conditions say that $f$ has nonzero constant term, $\deg f = k$ and $\deg g = n - k$, and the
support of their max-min product $f \otimes g$ is $A + B$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Lemma 19 (`jis-2025-25.2.7-lem-19`).

Stated but not proved: `MetaMathlibExt.boolean_close_factor_pairs_card_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#boolean-close-factor-pairs-card-le).

## Indecomposable prime candidates are lunar primes

Let $n$ and $b \ge 2$ be natural
numbers, let $a = (a_0, \dots, a_{n-1})$ be a digit string with digits in $\{0, \dots, b - 1\}$,
and let $f$ be its coefficient sequence. If $f$ is a prime candidate in base $b$ and $f$ is
max-min indecomposable, then $f$ is a lunar prime of base $b$.

This is Lemma 30 (Applegate, LeBrun and Sloane).

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Lemma 30 (`jis-2025-25.2.7-lem-30`).

Stated but not proved: `MetaMathlibExt.isLunarPrime_of_indecomposable_candidate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#is-lunar-prime-of-indecomposable-candida).

## Level counts of a lunar number

Let $f$ be a lunar number of base $b$ and degree at most
$n$, with digits $c_0, \dots, c_n \in \{0, \dots, b - 1\}$, and let $i$ be a natural number. The
level count $|f_i|$ is the number of indices $k \le n$ with $c_k \ge i$, that is, the number of
nonzero coefficients of the $i$-level support $f_i = s_i(f)$, the Boolean polynomial with
coefficient $1$ at $x^k$ when $c_k \ge i$ and $0$ otherwise.

A lunar number $f$ is not a monomial $t x^m$ (with $t = 0$ allowed) if and only if $|f_1| \ge 2$,
and $f_i$ is not a monomial if and only if $|f_i| \ge 2$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2, Definitions 13 and 16.

Formalized by `MetaMathlibExt.lunarLevelCount`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-level-count).

## Level counts of $1 \oplus 2x^2$ in base $3$

For the base-$3$ lunar number
$f = 1 \oplus 2x^2$ of degree at most $2$, with digits $1, 0, 2$, exactly two digits are at least
$1$ and exactly one digit is at least $2$: $|f_1| = 2$ and $|f_2| = 1$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2, Definitions 13 and 16.

Formalized by `MetaMathlibExt.lunarLevelCount_example`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-level-count-example).

## Decomposable lunar numbers

For natural numbers $b$ and $n$, let $\mathcal{L}_b^n$ be the
set of lunar numbers of base $b$ and degree at most $n$, that is, polynomials
$c_0 \oplus c_1 x \oplus \dots \oplus c_n x^n$ with digits $c_k \in \{0, \dots, b - 1\}$. The set
$\Sigma_b^n$ of decomposable lunar numbers consists of the $h \in \mathcal{L}_b^n$ that factor as
$h = f \otimes g$ under the max-min product, with $f, g \in \mathcal{L}_b^n$ each having at least
two nonzero digits.

A monomial is $t x^m$ with $t \in \{0, \dots, b - 1\}$, so the factors are exactly the
non-monomials. Every factor of a nonzero lunar number of degree at most $n$ lies in
$\mathcal{L}_b^n$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2, before Proposition 21.

Formalized by `MetaMathlibExt.lunarDecomposableSet`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-decomposable-set).

## Level-decomposable lunar numbers

Let $b$ and $n$ be natural numbers and
$a = \lfloor b/2 \rfloor$. For a lunar number $f$ of base $b$ and degree at most $n$, given by its
digits $f_0, \dots, f_n \in \{0, \dots, b - 1\}$, write $|f_a|$ for the number of indices $k \le n$
with $f_k \ge a$. The set $\mathcal{D}_b^n$ consists of the lunar numbers $h$ of base $b$ and
degree at most $n$ such that $h = f \otimes g$ for some lunar numbers $f$ and $g$ of base $b$ and
degree at most $n$ with $|f_a| \ge 2$ and $|g_a| \ge 2$, where $\otimes$ is the max-min product of
coefficient sequences.

For $b \ge 2$ we have $a \ge 1$, so $|f_a| \ge 2$ implies that $f$ has at least two nonzero
digits; hence $\mathcal{D}_b^n$ is contained in the set $\Sigma_b^n$ of decomposable lunar numbers
of degree at most $n$, and one writes $\mathcal{I}_b^n = \Sigma_b^n \setminus \mathcal{D}_b^n$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2, before Remark 22.

Formalized by `MetaMathlibExt.lunarLevelDecomposableSet`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-level-decomposable-set).

## Hoeffding extremal lunar numbers

Let $b$ and $n$ be natural numbers and $d$ a real
number. Let $\mathcal{L}_b^n$ be the set of lunar numbers of base $b$ and degree at most $n$
(digit strings $c_0, \dots, c_n$ with digits in $\{0, \dots, b - 1\}$), with the max-min product
$\otimes$, and for $f \in \mathcal{L}_b^n$ let $|f_i|$ be the number of its digits that are at
least $i$. The set $\mathcal{H}_b^n(d)$ of $d$-Hoeffding extremal lunar numbers consists of the
$h \in \mathcal{L}_b^n$ for which there is an index $i$ with $1 \le i \le b - 1$ such that either
$\bigl||h_i| - (b - i)n/b\bigr| > d/2$, or $h = f \otimes g$ for some $f, g \in \mathcal{L}_b^n$
with $\bigl||f_i| + |g_i| - (b - i)(n + 1)/b\bigr| > d/2$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Definition 23.

Formalized by `MetaMathlibExt.lunarHoeffdingExtremalSet`, a definition declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-hoeffding-extremal-set).

## A decomposable lunar number in base 2

In base $2$, the lunar number with digit string
$(1, 1, 1)$, that is $1 \oplus x \oplus x^2$ with $\oplus$ the lunar sum (digitwise maximum), lies
both in the set $\Sigma_2^2$ of decomposable lunar numbers of degree at most $2$ and in the set
$\mathcal{D}_2^2$ of level-decomposable lunar numbers of degree at most $2$.

A factorization witnessing both is $1 \oplus x \oplus x^2 = (1 \oplus x) \otimes (1 \oplus x)$,
where $\otimes$ is the max-min product and $1 \oplus x$ has digit string $(1, 1, 0)$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Section 2, before Proposition 21 and Remark 22.

Formalized by `MetaMathlibExt.mem_lunarDecomposableSet_example`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#mem-lunar-decomposable-set-example).

## An example of a Hoeffding extremal lunar number

In base $2$, the zero lunar number of
degree at most $2$ (the digit string $(0, 0, 0)$) lies in the $1$-Hoeffding extremal set
$\mathcal{H}_2^2(1)$: for the level $i = 1$, the number $|0_1|$ of its digits that are at least
$1$ is $0$, and $\left|0 - (2 - 1) \cdot 2 / 2\right| = 1 > 1/2$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Definition 23.

Formalized by `MetaMathlibExt.zero_mem_lunarHoeffdingExtremalSet`, a theorem declared in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#zero-mem-lunar-hoeffding-extremal-set).

## Upper bound on the number of decomposable lunar numbers

Fix an integer $b \ge 2$. There
is a constant $C > 0$ such that for every integer $n \ge 2$ and all reals $d > 0$ and $v > 0$, the
set $\Sigma_b^n$ of decomposable lunar numbers of base $b$ and degree at most $n$ satisfies

$$|\Sigma_b^n| \le C b^{n+1} \Big(n^2 e^{-d^2/(4(n+2))} + n^{2d+4} 2^{d/2-(n+1)/3} +
v n^{2d+2} 2^v b^{d/2-n/b} + n^2 2^{-v}\Big).$$

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Proposition 21 (`jis-2025-25.2.7-prop-21`).

Stated but not proved: `MetaMathlibExt.lunarDecomposableSet_ncard_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-decomposable-set-ncard-le).

## Bound on the number of Hoeffding extremal lunar numbers

Fix an integer $b \ge 2$. There is
a constant $C > 0$ such that for every integer $n \ge 1$ and every real $d > 0$, the set
$\mathcal{H}_b^n(d)$ of $d$-Hoeffding extremal lunar numbers of base $b$ and degree at most $n$
has at most $C n^2 e^{-d^2/(4(n+2))} b^n$ elements.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Lemma 24 (`jis-2025-25.2.7-lem-24`).

Stated but not proved: `MetaMathlibExt.lunarHoeffdingExtremalSet_ncard_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-hoeffding-extremal-set-ncard-le).

## Level counts of a product that is not Hoeffding extremal

Let $b$ and $n$ be natural
numbers, $d$ a real number and $f, g, h$ lunar numbers of base $b$ and degree at most $n$ with
$h = f \otimes g$ under the max-min product. For a natural number $i$ write $|f_i|$, $|g_i|$ and
$|h_i|$ for the numbers of digits of $f$, $g$ and $h$ that are at least $i$. If $h$ is not in the
set $\mathcal{H}_b^n(d)$ of $d$-Hoeffding extremal lunar numbers of base $b$ and degree at most
$n$, then $|h_i| \le |f_i| + |g_i| + d$ for every $i$ with $1 \le i \le b - 1$.

The source also assumes that $h$ lies in the set $\Sigma_b^n$ of decomposable lunar numbers of
base $b$ and degree at most $n$, which is not needed, and prints $|b_i|$ for $|g_i|$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Lemma 25 (`jis-2025-25.2.7-lem-25`).

Stated but not proved: `MetaMathlibExt.lunarLevelCount_le_of_not_mem_lunarHoeffdingExtremalSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-level-count-le-of-not-mem-lunar-ho).

## Bound on level-decomposable lunar numbers that are not Hoeffding extremal

Let $b \ge 2$
and $n$ be natural numbers and $d > 0$ a real number. The number of elements of
$\mathcal{D}_b^n \setminus \mathcal{H}_b^n(d)$ is at most $n^{2d+4} 2^{d/2-n/3} b^{n+1}$, where
$\mathcal{D}_b^n$ is the set of level-decomposable lunar numbers of base $b$ and degree at most
$n$ and $\mathcal{H}_b^n(d)$ is the set of $d$-Hoeffding extremal ones.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Lemma 26 (`jis-2025-25.2.7-lem-26`).

Stated but not proved: `MetaMathlibExt.lunarLevelDecomposableSet_diff_ncard_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-level-decomposable-set-diff-ncard).

## Decomposable lunar numbers with a low-degree factor

Let $b \ge 2$ and $n$ be natural
numbers and let $d > 0$ and $v > 0$ be reals. Count the lunar numbers $h$ of base $b$ and degree at
most $n$ that lie in $\Sigma_b^n \setminus \mathcal{H}_b^n(d)$ (decomposable but not $d$-Hoeffding
extremal) and can be written as $h = f \otimes g$, with $\otimes$ the max-min product, where $f$
and $g$ are lunar numbers of base $b$ and degree at most $n$, each with at least two nonzero
digits, and every digit $f_k$ with $k > v$ is zero. Their number is at most
$v \, n^{2d+3} \, 2^v \, (b - 1)^{(b-1)n/b + d/2}$.

The factorization is required to be nontrivial, as in the source's proof; if trivial
factorizations $h = (b - 1) \otimes h$ counted, the claim would fail at $b = 2$, $n = 2$, $d = 5$,
$v = 10^{-4}$: the lunar number with digit string $(1, 1, 1)$, that is $1 \oplus x \oplus x^2$
with $\oplus$ the lunar sum (digitwise maximum), lies in $\Sigma_2^2 \setminus \mathcal{H}_2^2(5)$,
but the bound is $8192 \cdot 10^{-4} \cdot 2^{10^{-4}} < 1$.

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Lemma 27 (`jis-2025-25.2.7-lem-27`).

Stated but not proved: `MetaMathlibExt.lunar_low_degree_factor_ncard_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-low-degree-factor-ncard-le).

## Bound on decomposable lunar numbers neither level decomposable nor extremal

Fix an integer
$b \ge 2$. For a natural number $n$ let $\mathcal{I}_b^n = \Sigma_b^n \setminus \mathcal{D}_b^n$,
where $\Sigma_b^n$ is the set of decomposable lunar numbers of base $b$ and degree at most $n$ and
$\mathcal{D}_b^n$ the set of level-decomposable ones, and for a real $d$ let $\mathcal{H}_b^n(d)$
be the set of $d$-Hoeffding extremal ones. There is a constant $C > 0$ such that for every natural
number $n$ and all reals $d > 0$ and $v > 0$,

$$|\mathcal{I}_b^n \setminus \mathcal{H}_b^n(d)| \le
C \Big(v n^{2d+2} 2^v b^{(b-1)n/b + d/2} + n^2 2^{-v} b^{n+1}\Big).$$

## Sources

- Baily, Dell, Fleischmann, Jackson, Pesikoff, Miller and Reifenberg, *Indecomposability Over the Max-Min Semiring*, Journal of Integer Sequences 28 (2025), Article 25.2.7, Lemma 28 (`jis-2025-25.2.7-lem-28`).

Stated but not proved: `MetaMathlibExt.lunarIndecomposableLevel_diff_ncard_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/MaxMinIndecomposabilityWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html#lunar-indecomposable-level-diff-ncard-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Max-min indecomposable sequences and lunar primes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/max-min-indecomposable-sequences-and-lunar-prime)
