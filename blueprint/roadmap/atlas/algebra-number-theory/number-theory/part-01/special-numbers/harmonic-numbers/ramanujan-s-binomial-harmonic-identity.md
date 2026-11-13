---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_choose_sub_choose_mul_harmonic_succ_eq, MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_choose_sub_choose_mul_harmonic_eq_add, MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.hasSum_ringChoose_mul_sin, MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_two_pow_choose_sub_mul_cos_pow_sin, MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_neg_one_pow_div_mul_choose_eq, MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.eq_lambda_mul_harmonic_of_sum_choose_sub_mul_eq
statement: formalized
---

# Ramanujan's binomial–harmonic identity

6 results, 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html).

## Shifted binomial–harmonic convolution (Alzer–Kwong, Corollary 1)

For natural numbers $k$
and $n$ with $2 \le k \le n$,

$$
\sum_{\nu=1}^{n+1} \Bigl(\binom{n+k-\nu-1}{n} - \binom{n+k-\nu-1}{k-2}\Bigr) H_\nu =
\binom{n+k}{k-1} (H_k - H_{n+1}) - \frac{1}{n+1} \binom{n+k}{k},
$$

where $H_m = \sum_{j=1}^{m} 1/j$ is the $m$-th harmonic number.

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_choose_sub_choose_mul_harmonic_succ_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html#sum-choose-sub-choose-mul-harmonic-succ).

## Shifted binomial–harmonic convolution (Alzer–Kwong, Corollary 2)

For natural numbers $k$
and $n$ with $1 \le k \le n - 1$,

$$
\sum_{\nu=1}^{n} \Bigl(\binom{n+k-\nu-1}{n-2} - \binom{n+k-\nu-1}{k}\Bigr) H_\nu =
\binom{n+k}{k+1} (H_k - H_n) + \frac{1}{k+1} \binom{n+k+1}{k+1},
$$

where $H_m = \sum_{j=1}^{m} 1/j$ is the $m$-th harmonic number.

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_choose_sub_choose_mul_harmonic_eq_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html#sum-choose-sub-choose-mul-harmonic-eq-ad).

## Ramanujan's binomial sine series

Let $a$, $N$ and $\theta$ be real numbers with
$N \ge 0$ and $|\theta| \le \pi / 2$. Then the series
$\sum_{\nu=0}^{\infty} \binom{N}{\nu} \sin((a + 2\nu)\theta)$ converges unconditionally to
$2^N (\cos \theta)^N \sin((a + N)\theta)$. Here $\binom{N}{\nu} = N(N-1)\cdots(N-\nu+1)/\nu!$
is the generalized binomial coefficient, and $2^N$ and $(\cos \theta)^N$ are real powers.

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.hasSum_ringChoose_mul_sin` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html#has-sum-ring-choose-mul-sin).

## The Rung-Obaid trigonometric identity

Let $k$ and $n$ be natural numbers with
$1 \le k \le n$, and let $\theta$ be a real number. Then

$$\sum_{\nu=1}^{n} 2^\nu \left( \binom{n+k-\nu-1}{k-1} - \binom{n+k-\nu-1}{n-1} \right)
\cos^\nu \theta \, \sin(\nu\theta) = 2^{n+k} \cos^{n+k} \theta \, \sin((n-k)\theta).$$

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_two_pow_choose_sub_mul_cos_pow_sin` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html#sum-two-pow-choose-sub-mul-cos-pow-sin).

## Gould's reciprocal binomial identity (Alzer–Kwong, Lemma 4)

Let $N$ be a natural number
and $x$ a real number with $x \ne \nu$ for every $\nu \in \{0, 1, \dots, N\}$. Then

$$
\sum_{\nu=0}^{N} \frac{(-1)^\nu}{x - \nu} \binom{N}{\nu} = \frac{(-1)^N}{(x - N) \binom{x}{N}},
$$

where $\binom{x}{N} = x(x-1)\cdots(x-N+1)/N!$ is the generalized binomial coefficient.

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers", Lemma 4.

Stated but not proved: `MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.sum_neg_one_pow_div_mul_choose_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html#sum-neg-one-pow-div-mul-choose-eq).

## Uniqueness of the harmonic solution of the diagonal Ramanujan identity

Let
$K : \mathbb{N} \to \mathbb{C}$ be a sequence such that for every integer $n \ge 2$

$$
\sum_{\nu=2}^{n} \Bigl(\binom{2n-\nu-2}{n-1} - \binom{2n-\nu-2}{n-2}\Bigr) K(\nu) =
\binom{2n-1}{n-1} \bigl(K(n-1) - K(n)\bigr).
$$

Then there is a constant $\lambda \in \mathbb{C}$ such that $K(r) = \lambda H_r$ for every integer
$r \ge 1$, where $H_r = \sum_{j=1}^{r} 1/j$ is the $r$-th harmonic number.

## Sources

- Horst Alzer and Man Kam Kwong, "Ramanujan and a Combinatorial Identity Involving Harmonic Numbers", Theorem 8.

Stated but not proved: `MathlibExt.NumberTheory.RamanujanHarmonicIdentityWanted.eq_lambda_mul_harmonic_of_sum_choose_sub_mul_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamanujanHarmonicIdentityWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html#eq-lambda-mul-harmonic-of-sum-choose-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan's binomial–harmonic identity](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/ramanujan-s-binomial-harmonic-identity)
