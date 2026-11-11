---
declaration: section
origin: cited
lean: MetaMathlibExt.PrimeNumberTheorem.prime_number_theorem_chebyshev_theta_error, MetaMathlibExt.dusart2016_tail_theorem
statement: formalized
---

# Error term in the prime number theorem

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/error-term-in-the-prime-number-theorem/index.html).

## Prime number theorem with error term for Chebyshev's $\theta$

Let
$\theta(x) = \sum_{p \le x} \log p$ be the sum of $\log p$ over the primes $p \le x$. For every
real $\varepsilon > 0$, $\theta(x) - x = O(x \exp(-(\log x)^{3/5 - \varepsilon}))$ as
$x \to \infty$.

## Sources

- Julian Ransford, "A Sum of Gcd's over Friable Numbers", Journal of Integer Sequences 19 (2016), Prime Number Theorem at lines 288–292; URL: https://cs.uwaterloo.ca/journals/JIS/VOL19/Ransford/ransford2.tex

Stated but not proved: `MetaMathlibExt.PrimeNumberTheorem.prime_number_theorem_chebyshev_theta_error` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/ChebyshevThetaPNTErrorWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/ChebyshevThetaPNTErrorWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/error-term-in-the-prime-number-theorem/index.html#prime-number-theorem-chebyshev-theta-err).

## Dusart's bound for $\vartheta$ and $\psi$ from a zero-free region

Let $R = 5.69693$, let
$\log$ be the natural logarithm, and let $\vartheta(x) = \sum_{p \le x} \log p$ (over primes $p$)
and $\psi(x) = \sum_{n \le x} \Lambda(n)$, with $\Lambda$ the von Mangoldt function, be
Chebyshev's functions. Suppose the Riemann zeta function has no zero $s$ with
$|\operatorname{Im} s| \ge 2\pi$ and
$\operatorname{Re} s \ge 1 - \frac{1}{R \log |\operatorname{Im} s|}$. Then for every real
number $x \ge \exp\bigl(R \max(8.36, 8/R)^2\bigr)$, writing $X = \sqrt{(\log x)/R}$,

$$\max\bigl(|\vartheta(x) - x|, |\psi(x) - x|\bigr) < x \sqrt{8/\pi}\, X^{1/2} e^{-X}.$$

## Sources

- Pierre Dusart, *Estimates of ψ, θ for large values of x without the Riemann hypothesis*, Math. Comp. 85 (2016), 875–888, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.dusart2016_tail_theorem` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/Dusart2016TailWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/Dusart2016TailWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/error-term-in-the-prime-number-theorem/index.html#dusart2016-tail-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Error term in the prime number theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/error-term-in-the-prime-number-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/error-term-in-the-prime-number-theorem)
