---
declaration: section
origin: cited
lean: MetaMathlibExt.almostPrimeCounting, MetaMathlibExt.landau_almostPrimeCounting_isEquivalent
statement: formalized
proof: formalized
---

# Almost primes

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes/index.html).

## Counting almost primes

For natural numbers $k$ and $x$, $\pi_k(x)$ is the number of
integers $n$ with $1 \le n \le x$ that have exactly $k$ prime factors, counted with multiplicity.
This is the counting function in Landau's theorem on almost primes.

## Sources

- Rafael Jakimczuk, "Functions of Slow Increase and Integer Sequences," Journal of Integer Sequences 13 (2010), <https://cs.uwaterloo.ca/journals/JIS/VOL13/Jakimczuk/jakimczuk8.tex>, lines 451-453.

Formalized by `MetaMathlibExt.almostPrimeCounting`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/LandauAlmostPrimeAsymptotic.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/LandauAlmostPrimeAsymptotic.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes/index.html#almost-prime-counting).

## Landau's theorem on almost primes

Let $k \ge 1$ be a natural number and, for a natural
number $x$, let $\pi_k(x)$ be the number of integers $n$ with $1 \le n \le x$ that have exactly
$k$ prime factors, counted with multiplicity. Then, as the natural number $x$ tends to infinity,

$$\pi_k(x) \sim \frac{x \, (\log \log x)^{k-1}}{(k-1)! \, \log x}.$$

## Sources

- Rafael Jakimczuk, "Functions of Slow Increase and Integer Sequences," Journal of Integer Sequences 13 (2010), <https://cs.uwaterloo.ca/journals/JIS/VOL13/Jakimczuk/jakimczuk8.tex>, lines 451-453.

Formalized by `MetaMathlibExt.landau_almostPrimeCounting_isEquivalent`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LandauAlmostPrimeAsymptotic.lean, line 2013](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/LandauAlmostPrimeAsymptotic.lean#L2013). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes/index.html#landau-almost-prime-counting-is-equivale).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Almost primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes)
