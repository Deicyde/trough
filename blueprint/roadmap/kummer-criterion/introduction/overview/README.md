# Overview

Let $p$ be an odd prime, let $\zeta_p$ be a primitive $p$th root of unity, and let $K=\mathbb{Q}(\zeta_p)$ be the $p$th cyclotomic field. Kummer (kummer1850) proved that Fermat's Last Theorem holds for the exponent $p$ whenever $p$ is *regular*, that is, whenever $p$ does not divide the class number $h(K)$. Regularity is a condition on an invariant that is notoriously difficult to compute; Kummer's second fundamental insight is that it can be detected by a finite, purely arithmetic test on Bernoulli numbers.

This document is the blueprint of a formalisation, in Lean 4 and building on mathlib, of *Kummer's criterion*: an odd prime $p$ is regular if and only if

$$
p \nmid \operatorname{num}(B_{2k})
\qquad\text{for all } k \text{ with } 1 \le k,\ 2k \le p-3,
$$

where $B_n$ denotes the $n$th Bernoulli number and $\operatorname{num}$ the numerator of a rational number in lowest terms. The final statement is [Theorem kummer-criterion](../../final-assembly/kummers-criterion/thm-kummer-criterion.md); the formal counterpart is the Lean declaration `KummerCriterion`.

The criterion makes regularity decidable in practice. Running the Bernoulli test on the primes below $100$ shows that the irregular primes in that range are exactly $37$, $59$ and $67$; combined with the `flt-regular` formalisation of Kummer's theorem on Fermat's Last Theorem for regular prime exponents, this yields Fermat's Last Theorem for every exponent $2 < n \le 100$ outside $\{37, 59, 67, 74\}$.

Irregular primes are not a finite accident. Jensen (jensen1915) proved that there are infinitely many irregular primes (indeed, infinitely many congruent to $3$ modulo $4$), and Carlitz (carlitz1954) gave the short argument formalised here, which combines the criterion with the unrestricted Kummer congruence for divided Bernoulli numbers and the archimedean growth of $|B_{2k}/2k|$. The final statement is [Theorem infinitely-many-irregular](../../infinitely-many-irregular-primes/the-carlitz-escape-argument/thm-infinitely-many-irregular.md); the formal counterpart is `KummerCriterion.infinite_not_isRegularPrime`.

Standard references for all of this material are Washington (washington) and Ireland–Rosen (ireland-rosen).

- [regular-prime](def-regular-prime.md)
