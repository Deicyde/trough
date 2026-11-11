---
declaration: section
origin: cited
lean: MetaMathlibExt.summatory_moebius_div_bound, MetaMathlibExt.prime_power_factorization_sum_eq_iff
statement: formalized
---

# Multiplicative functions and mean values: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/index.html).

Dirichlet and unitary convolution, completely multiplicative and additive functions, Wintner and Euler-product mean values, additive uniqueness sets, Mertens bounds.

## Explicit bounds for the summatory function of $\mu(n)/n$

Let $\mu$ be the Möbius function.
For every real $x \ge 33$,

$$\Bigl| \sum_{1 \le n \le x} \frac{\mu(n)}{n} \Bigr| < \frac{0.19}{\log x},$$

and for every real $x > 1$,

$$\Bigl| \sum_{1 \le n \le x} \frac{\mu(n)}{n} \Bigr| < \frac{546}{(\log x)^2}.$$

These bounds improve the estimates $0.2185/\log x$ and $726/(\log x)^2$ of the source's
equation (e4).

## Sources

- Olivier Bordellès, "Some Explicit Estimates for the Möbius Function," Journal of Integer Sequences 18 (2015), Article 15.11.1, Theorem, items (a) and (b), lines 118–127, https://cs.uwaterloo.ca/journals/JIS/VOL18/Bordelles2/bordelles21.tex

Stated but not proved: `MetaMathlibExt.summatory_moebius_div_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ExplicitMertensBoundWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ExplicitMertensBoundWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/index.html#summatory-moebius-div-bound).

## Prime powers fixed by a uniform power sum of their prime factors

For positive integers $y$
and $s$, let $T_s(y) = \sum_q e_q q^s$, where $q$ runs over the primes dividing $y$ and $e_q$ is
the exponent of $q$ in $y$, so that each prime factor is counted with multiplicity. Let $p$ be a
prime, let $m$ be a positive integer and let $y = p^m$. Then for every positive integer $s$,
$T_s(y) = y$ if and only if $m = p^k$ and $s = p^k - k$ for some natural number $k$.

For $y = p^m$ one has $T_s(y) = m p^s$, and $m p^s = p^m$ forces $m$ to be a power of $p$.

## Sources

- Spencer P. Hurd and Judson S. McCranie, "Integers That Are Sums of Uniform Powers of All Their Prime Factors: The Sequence A068916," Journal of Integer Sequences 22 (2019), Article 19.3.4, Theorem 1, lines 187–189, https://cs.uwaterloo.ca/journals/JIS/VOL22/Hurd/hurd1.tex

Formalized by `MetaMathlibExt.prime_power_factorization_sum_eq_iff`, a theorem declared in [MathlibExt/NumberTheory/PrimePowerFactorizationSum.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimePowerFactorizationSum.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/index.html#prime-power-factorization-sum-eq-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiplicative functions and mean values](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions)
