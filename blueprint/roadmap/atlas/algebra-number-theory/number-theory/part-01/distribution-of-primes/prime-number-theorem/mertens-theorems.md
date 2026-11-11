---
declaration: section
origin: cited
lean: MetaMathlibExt.mertensConstant, MetaMathlibExt.dusart_log_prime_sum, MetaMathlibExt.meisselMertensConstant, MetaMathlibExt.dusart_reciprocal_prime_sum
statement: formalized
---

# Mertens' theorems

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/mertens-theorems/index.html).

## The constant in Mertens' first theorem

With $p$ ranging over the primes and $\log$ the
natural logarithm, this is the real number

$$M = \lim_{n \to \infty} \Bigl(\sum_{p \le n} \frac{\log p}{p} - \log n\Bigr),$$

the limit taken over natural numbers $n$.

Formalized by `MetaMathlibExt.mertensConstant`, a definition declared in [WantedExt/NumberTheory/PrimeCounting/DusartMertensLogSumWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartMertensLogSumWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/mertens-theorems/index.html#mertens-constant).

## Dusart's explicit Mertens first theorem

Let $p$ range over the primes, let $\log$ be the
natural logarithm, and let
$M = \lim_{n \to \infty} \bigl(\sum_{p \le n} \frac{\log p}{p} - \log n\bigr)$ be the constant in
Mertens' first theorem. For every real number $x \ge 912560$ there is a real number $E$ with
$|E| \le \frac{0.3}{(\log x)^2}$ such that

$$\sum_{p \le x} \frac{\log p}{p} = \log x + M + E.$$

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Theorem 5.7.

Stated but not proved: `MetaMathlibExt.dusart_log_prime_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartMertensLogSumWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartMertensLogSumWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/mertens-theorems/index.html#dusart-log-prime-sum).

## The Meissel–Mertens constant

With $p$ ranging over the primes and $\log$ the natural
logarithm, the Meissel–Mertens constant is the real number

$$B = \lim_{n \to \infty} \Bigl(\sum_{p \le n} \frac{1}{p} - \log \log n\Bigr),$$

the limit taken over natural numbers $n$. Numerically, $B \approx 0.2614972128$.

Formalized by `MetaMathlibExt.meisselMertensConstant`, a definition declared in [WantedExt/NumberTheory/PrimeCounting/DusartMertensReciprocalSumWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartMertensReciprocalSumWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/mertens-theorems/index.html#meissel-mertens-constant).

## Dusart's explicit Mertens second theorem

Let $p$ range over the primes, let $\log$ be
the natural logarithm, and let
$B = \lim_{n \to \infty} \bigl(\sum_{p \le n} \frac{1}{p} - \log \log n\bigr)$ be the
Meissel–Mertens constant. For every real number $x \ge 2278383$ there is a real number $E$ with
$|E| \le \frac{0.2}{(\log x)^3}$ such that

$$\sum_{p \le x} \frac{1}{p} = \log \log x + B + E.$$

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Theorem 5.6.

Stated but not proved: `MetaMathlibExt.dusart_reciprocal_prime_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartMertensReciprocalSumWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/DusartMertensReciprocalSumWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/mertens-theorems/index.html#dusart-reciprocal-prime-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mertens' theorems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/mertens-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/mertens-theorems)
