---
declaration: section
origin: cited
lean: MetaMathlibExt.dilcher_finite_multiple_harmonic_identity_general, MetaMathlibExt.dilcher_finite_multiple_harmonic_identity, MetaMathlibExt.multipleHarmonic, MetaMathlibExt.multiple_harmonic_polynomial_congruence
statement: formalized
proof: formalized
---

# Multiple harmonic sums

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/multiple-harmonic-sums/index.html).

## Dilcher's finite multiple harmonic identity for every exponent

For every natural number
$m$ (including $m = 0$) and every positive integer $n$,

$$
\sum_{k=1}^{n} \frac{(-1)^{k-1} \binom{n}{k}}{k^m}
= \sum_{1 \le j_1 \le \cdots \le j_m \le n} \frac{1}{j_1 \cdots j_m},
$$

where the right side sums over all weakly increasing tuples $(j_1, \ldots, j_m)$ of integers
between $1$ and $n$; for $m = 0$ there is only the empty tuple, whose term is $1$.

Formalized by `MetaMathlibExt.dilcher_finite_multiple_harmonic_identity_general`, a theorem declared in [MathlibExt/NumberTheory/DilcherFiniteMultipleHarmonic.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DilcherFiniteMultipleHarmonic.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/multiple-harmonic-sums/index.html#dilcher-finite-multiple-harmonic-identit).

## Dilcher's finite multiple harmonic identity

For all positive integers $m$ and $n$,

$$
\sum_{k=1}^{n} \frac{(-1)^{k-1} \binom{n}{k}}{k^m}
= \sum_{1 \le j_1 \le \cdots \le j_m \le n} \frac{1}{j_1 \cdots j_m},
$$

where the right side sums over all weakly increasing tuples $(j_1, \ldots, j_m)$ of integers
between $1$ and $n$.

## Sources

- Khristo N. Boyadzhiev, "Harmonic Number Identities Via Euler's Transform", Journal of Integer Sequences 12 (2009), Article 09.6.1, <https://cs.uwaterloo.ca/journals/JIS/VOL12/Boyadzhiev/boyadzhiev3.tex>, controlling statement equation (26), lines 323–331. Boyadzhiev attributes the identity to Karl Dilcher, "Some q-series identities related to divisor functions", Discrete Mathematics 145 (1995), 83–93, DOI 10.1016/0012-365X(95)00092-B (the JIS bibliography prints "divisor factors").

Formalized by `MetaMathlibExt.dilcher_finite_multiple_harmonic_identity`, a theorem declared in [MathlibExt/NumberTheory/DilcherFiniteMultipleHarmonic.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DilcherFiniteMultipleHarmonic.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/multiple-harmonic-sums/index.html#dilcher-finite-multiple-harmonic-identit-2).

## Multiple harmonic sums

For natural numbers $p$, $r$ and $n$, the multiple harmonic sum
$H_r^{(n)}$ modulo $p$ is the element

$$H_r^{(n)} = \sum_{0 < k_1 < \cdots < k_n \le r} k_1^{-1} \cdots k_n^{-1}$$

of $\mathbb{Z}/p\mathbb{Z}$, where the sum runs over the strictly increasing $n$-tuples of
integers, equivalently over the $n$-element subsets of $\{1, \dots, r\}$, and $k^{-1}$ is the
inverse of $k$ in $\mathbb{Z}/p\mathbb{Z}$ (Mathlib's total inverse, which is the true inverse
whenever $k$ is a unit modulo $p$). In particular $H_r^{(0)} = 1$, and $H_r^{(n)} = 0$ when $n > r$.

## Sources

- Mattarei–Tauraso, "Congruences of Multiple Sums Involving Sequences Invariant Under the Binomial Transform", J. Integer Sequences, <https://cs.uwaterloo.ca/journals/JIS/VOL13/Tauraso/tauraso22.tex>, Lemma.

Formalized by `MetaMathlibExt.multipleHarmonic`, a definition declared in [MathlibExt/NumberTheory/MultipleHarmonic.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleHarmonic.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/multiple-harmonic-sums/index.html#multiple-harmonic).

## Mattarei–Tauraso polynomial congruence for multiple harmonic sums

Let $n \ge 1$ and let
$p$ be a prime with $p > n + 1$, write $H_r^{(m)}$ for the multiple harmonic sum modulo $p$, and
write $k^{-1}$ for the inverse of $k$ in $\mathbb{Z}/p\mathbb{Z}$. Then, as polynomials in $x$
over $\mathbb{Z}/p\mathbb{Z}$,

$$\sum_{k=1}^{p-1} H_{k-1}^{(n-1)} k^{-1} x^k = (-1)^{n-1} \sum_{k=1}^{p-1} (k^{-1})^n (1 - x)^k.$$

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL13/Tauraso/tauraso22.tex>, Lemma `Gg`.

Formalized by `MetaMathlibExt.multiple_harmonic_polynomial_congruence`, a theorem declared in [MathlibExt/NumberTheory/MultipleHarmonicPolynomialCongruence.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleHarmonicPolynomialCongruence.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/multiple-harmonic-sums/index.html#multiple-harmonic-polynomial-congruence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiple harmonic sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/multiple-harmonic-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/multiple-harmonic-sums)
