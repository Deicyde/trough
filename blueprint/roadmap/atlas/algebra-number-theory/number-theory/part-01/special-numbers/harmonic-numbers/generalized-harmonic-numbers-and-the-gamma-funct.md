---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedHarmonic, MetaMathlibExt.generalizedHarmonic_zero, MetaMathlibExt.generalizedHarmonic_succ, MetaMathlibExt.generalizedHarmonic_eq_gamma_expectation, MetaMathlibExt.generalizedHarmonic_sub_eq_gamma_expectation, MetaMathlibExt.sum_choose_mul_generalizedHarmonic, MetaMathlibExt.stirlingFirst_generalizedHarmonic_eq_gamma_expectation
statement: formalized
---

# Generalized harmonic numbers and the Gamma function

7 results, 3 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html).

## Generalized harmonic numbers

For a real number $s$ and a natural number $n$, the
generalized harmonic number of order $s$ is $H_n^{(s)} = \sum_{k=1}^{n} 1/k^s$, where $k^s$ is the
real power.

## Sources

- Toshio Nakata, *A Probabilistic Representation of Generalized Harmonic Numbers and an Identity for Their Sums*, INTEGERS 26 (2026), Article A124, Section 1 (definition of `H_n^{(s)}`).

Formalized by `MetaMathlibExt.generalizedHarmonic`, a definition declared in [WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html#generalized-harmonic).

## The zeroth generalized harmonic number

For every real $s$, the generalized harmonic
number $H_n^{(s)} = \sum_{k=1}^{n} 1/k^s$ vanishes at $n = 0$: $H_0^{(s)} = 0$.

## Sources

- Toshio Nakata, *A Probabilistic Representation of Generalized Harmonic Numbers and an Identity for Their Sums*, INTEGERS 26 (2026), Article A124, Section 1 (definition of `H_n^{(s)}`).

Formalized by `MetaMathlibExt.generalizedHarmonic_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html#generalized-harmonic-zero).

## Recurrence for generalized harmonic numbers

For every real $s$ and every natural number
$n$, the generalized harmonic numbers $H_n^{(s)} = \sum_{k=1}^{n} 1/k^s$ satisfy
$H_{n+1}^{(s)} = H_n^{(s)} + 1/(n+1)^s$.

## Sources

- Toshio Nakata, *A Probabilistic Representation of Generalized Harmonic Numbers and an Identity for Their Sums*, INTEGERS 26 (2026), Article A124, Section 1 (definition of `H_n^{(s)}`).

Formalized by `MetaMathlibExt.generalizedHarmonic_succ`, a theorem declared in [WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html#generalized-harmonic-succ).

## Gamma representation of generalized harmonic numbers

Let $s > 0$ be real, let
$H_n^{(s)} = \sum_{k=1}^{n} 1/k^s$ denote the generalized harmonic numbers, and let $X_s$ be a
random variable with the Gamma distribution $\mathrm{Gamma}(s, 1)$ of shape $s$ and rate $1$. Then
for every natural number $n$,

$$H_n^{(s)} = \sum_{k=0}^{n-1} \mathbb{E}[e^{-k X_s}] =
\mathbb{E}\left[\frac{1 - e^{-n X_s}}{1 - e^{-X_s}}\right].$$

## Sources

- Toshio Nakata, *A Probabilistic Representation of Generalized Harmonic Numbers and an Identity for Their Sums*, INTEGERS 26 (2026), Article A124, Lemma 1, Equation (5).

Stated but not proved: `MetaMathlibExt.generalizedHarmonic_eq_gamma_expectation` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html#generalized-harmonic-eq-gamma-expectatio).

## Shifted Gamma representation of generalized harmonic numbers

For real $t$ and a natural
number $n$, write $H_n^{(t)} = \sum_{k=1}^{n} 1/k^t$ for the generalized harmonic number. Let
$s > 0$ be real and let $X_s$ be a random variable with the Gamma distribution
$\mathrm{Gamma}(s, 1)$ of shape $s$ and rate $1$. Then for every real $u$ and every natural
number $n$,

$$H_n^{(s-u)} = \sum_{k=0}^{n-1} (k+1)^u \, \mathbb{E}[e^{-k X_s}].$$

The source assumes $0 < u < s$; the identity holds for every real $u$.

## Sources

- Toshio Nakata, *A Probabilistic Representation of Generalized Harmonic Numbers and an Identity for Their Sums*, INTEGERS 26 (2026), Article A124, Lemma 2, Equation (7).

Stated but not proved: `MetaMathlibExt.generalizedHarmonic_sub_eq_gamma_expectation` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html#generalized-harmonic-sub-eq-gamma-expect).

## Binomially weighted sums of generalized harmonic numbers

Write $[a, b]$ for the unsigned
Stirling number of the first kind, the number of permutations of $a$ elements with exactly $b$
cycles, and, for real $t$ and a natural number $n$, write $H_n^{(t)} = \sum_{k=1}^{n} 1/k^t$ for
the generalized harmonic number. For all natural numbers $m$ and $n$ and every real $\alpha$,

$$\sum_{j=1}^{n-1} \binom{j}{m} H_j^{(\alpha)} = \binom{n}{m+1} H_n^{(\alpha)} -
\frac{1}{(m+1)!} \sum_{r=0}^{m+1} [m+1, r] (-1)^{m+1-r} H_n^{(\alpha-r)}.$$

## Sources

- Toshio Nakata, *A Probabilistic Representation of Generalized Harmonic Numbers and an Identity for Their Sums*, INTEGERS 26 (2026), Article A124, Proposition 1, Equation (3).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_generalizedHarmonic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html#sum-choose-mul-generalized-harmonic).

## Gamma representation of the Stirling combination of generalized harmonic numbers

Let
$s > 0$ be real and let $X_s$ be a random variable with the Gamma distribution
$\mathrm{Gamma}(s, 1)$ of shape $s$ and rate $1$. Write $[a, b]$ for the unsigned Stirling number
of the first kind, the number of permutations of $a$ elements with exactly $b$ cycles, and, for
real $t$ and a natural number $n$, write $H_n^{(t)} = \sum_{k=1}^{n} 1/k^t$ for the generalized
harmonic number. Then for all natural numbers $m$ and $n$,

$$\frac{1}{(m+1)!} \sum_{j=0}^{m+1} [m+1, j] (-1)^{m+1-j} H_n^{(s-j)} =
\sum_{k=0}^{n-1} \binom{k+1}{m+1} \mathbb{E}[e^{-k X_s}].$$

The source assumes $s > m + 1$; the identity holds for every $s > 0$.

## Sources

- Toshio Nakata, *A Probabilistic Representation of Generalized Harmonic Numbers and an Identity for Their Sums*, INTEGERS 26 (2026), Article A124, Corollary 1, Equation (8).

Stated but not proved: `MetaMathlibExt.stirlingFirst_generalizedHarmonic_eq_gamma_expectation` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedHarmonicGammaWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html#stirling-first-generalized-harmonic-eq-g).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized harmonic numbers and the Gamma function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/generalized-harmonic-numbers-and-the-gamma-funct)
