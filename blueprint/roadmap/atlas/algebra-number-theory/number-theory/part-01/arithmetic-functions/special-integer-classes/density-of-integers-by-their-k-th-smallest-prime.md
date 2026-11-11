---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem690Wanted.IsKthSmallestPrimeFactor, MathlibExt.NumberTheory.ErdosProblem690Wanted.kthPrimeFactorDensity, MathlibExt.NumberTheory.ErdosProblem690Wanted.IsUnimodalOnPrimes, MathlibExt.NumberTheory.ErdosProblem690Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem690Wanted.conjecture_refuted
statement: formalized
---

# Density of integers by their k-th smallest prime factor

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime/index.html).

## The $k$-th smallest prime factor

For natural numbers $k$, $n$ and $p$, $p$ is the $k$-th
smallest prime factor of $n$ when $n \ne 0$, $p$ is a prime dividing $n$, and exactly $k - 1$
primes dividing $n$ are smaller than $p$.

For $k = 0$ the count $k - 1$ is read as $0$ (truncated subtraction), so $k = 0$ and $k = 1$
agree.

Formalized by `MathlibExt.NumberTheory.ErdosProblem690Wanted.IsKthSmallestPrimeFactor`, a definition declared in [WantedExt/NumberTheory/ErdosProblem690Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem690Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime/index.html#is-kth-smallest-prime-factor).

## The $k$-th prime-factor density

For natural numbers $k$ and $p$, let $S_{k,p}$ be the set
of natural numbers whose $k$-th smallest prime factor is $p$. The $k$-th prime-factor density
$d_k(p)$ is the natural density of $S_{k,p}$, that is, the limit of
$\lvert S_{k,p} \cap \{0, 1, \dots, N - 1\} \rvert / N$ as $N \to \infty$, when this limit
exists; otherwise $d_k(p)$ is an unspecified real number.

Formalized by `MathlibExt.NumberTheory.ErdosProblem690Wanted.kthPrimeFactorDensity`, a definition declared in [WantedExt/NumberTheory/ErdosProblem690Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem690Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime/index.html#kth-prime-factor-density).

## Unimodality on the primes

A function $f \colon \mathbb{N} \to \mathbb{R}$ is unimodal on
the primes if there is a prime $p_0$ such that $f(p) \le f(q)$ for all primes $p$ and $q$ with
$p \le q \le p_0$, and $f(q) \le f(p)$ for all primes $p$ and $q$ with $p_0 \le p \le q$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem690Wanted.IsUnimodalOnPrimes`, a definition declared in [WantedExt/NumberTheory/ErdosProblem690Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem690Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime/index.html#is-unimodal-on-primes).

## Erdős Problem 690

The proposition that for every natural number $k \ge 1$ the $k$-th
prime-factor density $d_k$ is unimodal on the primes: there is a prime $p_0$ such that
$d_k(p) \le d_k(q)$ for all primes $p$ and $q$ with $p \le q \le p_0$, and $d_k(q) \le d_k(p)$ for
all primes $p$ and $q$ with $p_0 \le p \le q$. Here $d_k(p)$ is the natural density of the set of
natural numbers whose $k$-th smallest prime factor is $p$ (an unspecified real number if this
density does not exist).

Formalized by `MathlibExt.NumberTheory.ErdosProblem690Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem690Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem690Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime/index.html#conjecture).

## Erdős Problem 690 is false

There is a natural number $k \ge 1$ such that the $k$-th
prime-factor density $d_k$ is not unimodal on the primes, that is, there is no prime $p_0$ such
that $d_k(p) \le d_k(q)$ for all primes $p$ and $q$ with $p \le q \le p_0$ and
$d_k(q) \le d_k(p)$ for all primes $p$ and $q$ with $p_0 \le p \le q$. Here $d_k(p)$ is the
natural density of the set of natural numbers whose $k$-th smallest prime factor is $p$ (an
unspecified real number if this density does not exist).

Cambie (Theorem 5) proves that $d_k$ is unimodal for $k = 1, 2, 3$ and not unimodal for
$4 \le k \le 20$; for example $d_4(13) = 31/5005 > d_4(17) = 206/36465 < d_4(19) = 1308/230945$.

## Sources

- S. Cambie, Resolution of Erdős' problems about unimodularity, arXiv preprint (2025), arXiv:2501.10333, https://arxiv.org/abs/2501.10333.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem690Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem690Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem690Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Density of integers by their k-th smallest prime factor](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/density-of-integers-by-their-k-th-smallest-prime)
