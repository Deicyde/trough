---
declaration: section
origin: cited
lean: MetaMathlibExt.alternating_binomial_transform_harmonic_numbers, MetaMathlibExt.binomial_harmonic_convolution, MetaMathlibExt.binomial_harmonic_interchange_identity, MetaMathlibExt.binomial_transform_second_order_harmonic_numbers, MetaMathlibExt.binomial_transform_sq_harmonic
statement: formalized
proof: formalized
---

# Binomial identities for harmonic numbers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers/index.html).

## Alternating binomial transform of the harmonic numbers

Let $s$ be a complex number that
is not a negative integer, let $n$ be a positive integer, and let $H_k = \sum_{j=1}^{k} 1/j$
be the $k$-th harmonic number. For complex $z$ and natural $k$ write
$\binom{z}{k} = \Gamma(z + 1) / (\Gamma(k + 1)\,\Gamma(z - k + 1))$, with $1/\Gamma$ taken to
be $0$ at the poles of $\Gamma$. Then

$$
\sum_{k=1}^{n} (-1)^k \binom{n+s}{k} H_k = (-1)^n \binom{s+n-1}{n} H_n +
\frac{(-1)^n}{s+n} \binom{s+n-1}{n} - \frac{1}{s+n}.
$$

The generalized binomial coefficients are written as Gamma-function quotients, and the
assumption that $s$ is not a negative integer is the source condition
$s \in \mathbb{C} \setminus \mathbb{Z}^-$.

## Sources

- Necdet Batır, "Finite Binomial Sum Identities with Harmonic Numbers," Journal of Integer Sequences 24 (2021), Article 21.4.3, Corollary 3, lines 220–226, https://cs.uwaterloo.ca/journals/JIS/VOL24/Batir2/batir13.tex

Formalized by `MetaMathlibExt.alternating_binomial_transform_harmonic_numbers`, a theorem declared in [MathlibExt/NumberTheory/AlternatingBinomialTransformHarmonic.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/AlternatingBinomialTransformHarmonic.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers/index.html#alternating-binomial-transform-harmonic).

## Binomial-harmonic convolution identity

Let $H_m = \sum_{i=1}^{m} 1/i$ denote the $m$-th
harmonic number. For natural numbers $k$ and $n$ with $1 \le k \le n$,

$$\sum_{\nu=1}^{n} \left(\binom{n+k-\nu-1}{n-1} - \binom{n+k-\nu-1}{k-1}\right) H_\nu =
\binom{n+k}{k} (H_k - H_n).$$

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers," Journal of Integer Sequences 29 (2026), Article 26.4.8, Theorem 1, equation (1.1), lines 135–141, https://cs.uwaterloo.ca/journals/JIS/VOL29/Alzer/alzer22.tex

Formalized by `MetaMathlibExt.binomial_harmonic_convolution`, a theorem declared in [MathlibExt/NumberTheory/BinomialHarmonicConvolution.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinomialHarmonicConvolution.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers/index.html#binomial-harmonic-convolution).

## Binomial interchange identity with harmonic weights

Let $K$ be a field of
characteristic zero. For every natural number $n$ and every sequence $a : \mathbb{N} \to K$,

$$\sum_{k=1}^{n} \frac{1}{k} \sum_{j=1}^{k} \binom{k}{j} a_j =
\sum_{k=1}^{n} \binom{n}{k} \frac{a_k}{k}.$$

The source notes a generalization in Boyadzhiev, attributed to 't Woord. The statement
generalizes the source's real or complex sequences to any field of characteristic zero.

## Sources

- Necdet Batır and Anthony Sofo, "A Unified Treatment of Certain Classes of Combinatorial Identities," Journal of Integer Sequences 24 (2021), Article 21.3.2, Lemma A, lines 150–156, https://cs.uwaterloo.ca/journals/JIS/VOL24/Batir/batir7.tex

Formalized by `MetaMathlibExt.binomial_harmonic_interchange_identity`, a theorem declared in [MathlibExt/NumberTheory/BinomialHarmonicInterchangeIdentity.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinomialHarmonicInterchangeIdentity.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers/index.html#binomial-harmonic-interchange-identity).

## Alternating binomial transform of second-order harmonic numbers

For a natural number
$m$ let $H_m = \sum_{j=1}^{m} 1/j$ and $H_m^{(2)} = \sum_{j=1}^{m} 1/j^2$, and for
$z \in \mathbb{C}$ and a natural number $r$ let $\binom{z}{r} = z(z-1)\cdots(z-r+1)/r!$, the
empty product for $r = 0$ being $1$. Let $s \in \mathbb{C}$ with $s \ne -m$ for every positive
integer $m$, and let $n \ge 1$. Then

$$\sum_{k=1}^{n} (-1)^k \binom{s+n}{k} H_k^{(2)} =
(-1)^n \binom{s+n-1}{n} H_n^{(2)} -
\frac{1}{s+n} \Bigl(H_n -
s \sum_{k=1}^{n} \frac{(-1)^k \binom{s+k-1}{k-1}}{k^2 \binom{n}{k}}\Bigr).$$

## Sources

- Necdet Batır, "Finite Binomial Sum Identities with Harmonic Numbers," Journal of Integer Sequences 24 (2021), Article 21.4.3, Proposition 6, equation (2.8), lines 260–267, https://cs.uwaterloo.ca/journals/JIS/VOL24/Batir2/batir13.tex

Formalized by `MetaMathlibExt.binomial_transform_second_order_harmonic_numbers`, a theorem declared in [MathlibExt/NumberTheory/BinomialTransformSecondOrderHarmonic.lean, line 934](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinomialTransformSecondOrderHarmonic.lean#L934). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers/index.html#binomial-transform-second-order-harmonic).

## Alternating binomial transform of the squared harmonic numbers

For a complex number
$z$ and $k \in \mathbb{N}$ write $\binom{z}{k} = z(z-1)\cdots(z-k+1)/k!$ (the empty product
being $1$), and let $H_k = 1 + \frac{1}{2} + \cdots + \frac{1}{k}$ be the $k$-th harmonic number.
Let $s$ be a complex number that is not a negative integer, and let $n \ge 1$. Then

$$
\sum_{k=1}^{n} (-1)^k \binom{s+n}{k} H_k^2 =
(-1)^n \binom{s+n-1}{n} \left(H_n^2 + \frac{2 H_n}{s+n} + \frac{2}{(s+n)^2}\right) +
\frac{H_n}{s+n} - \frac{2}{(s+n)^2} -
\frac{s}{s+n} \sum_{k=1}^{n} \frac{(-1)^k \binom{s+k-1}{k-1}}{k^2 \binom{n}{k}}.
$$

## Sources

- Necdet Batır, "Finite Binomial Sum Identities with Harmonic Numbers," Journal of Integer Sequences 24 (2021), Article 21.4.3, Theorem 7, equation (2.12), lines 287–293, https://cs.uwaterloo.ca/journals/JIS/VOL24/Batir2/batir13.tex

Formalized by `MetaMathlibExt.binomial_transform_sq_harmonic`, a theorem declared in [MathlibExt/NumberTheory/BinomialTransformSquaredHarmonic.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinomialTransformSquaredHarmonic.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers/index.html#binomial-transform-sq-harmonic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial identities for harmonic numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/binomial-identities-for-harmonic-numbers)
