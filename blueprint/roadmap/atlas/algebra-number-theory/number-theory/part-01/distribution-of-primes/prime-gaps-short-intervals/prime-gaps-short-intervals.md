---
declaration: section
origin: cited
lean: MetaMathlibExt.dusart_prime_gap, MathlibExt.NumberTheory.BreuschWanted.ramanujan_two_primes_between
statement: formalized
---

# Prime gaps and primes in short intervals: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/index.html).

Bertrand-type and Breusch theorems, Ramanujan primes, prime gaps, bounded gaps, Sylvester–Schur on prime factors of consecutive products.

## Dusart's short-interval prime gap bound

Let $\log$ be the natural logarithm. For every
real number $x \ge 468991632$ there is a prime $p$ with $x < p \le x + \frac{x}{5000 (\log x)^2}$.

## Sources

- Pierre Dusart, *Explicit estimates of some functions over primes*, Ramanujan J. 45(1) (2018), 227–251, <https://doi.org/10.1007/s11139-016-9839-4>, Corollary 5.5.

Stated but not proved: `MetaMathlibExt.dusart_prime_gap` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/DusartPrimeGapWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/DusartPrimeGapWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/index.html#dusart-prime-gap).

## Ramanujan's two-primes refinement of Bertrand's postulate

For every natural number
$n \ge 6$ there are primes $p$ and $q$ with $n < p < q < 2n$; that is, the open interval
$(n, 2n)$ contains two distinct primes.

For $n \ge 48$ this follows from Breusch's theorem applied at $n$ and at $9n/8$; the remaining
finitely many cases are checked by direct computation.

## Sources

- Nathaniel Benjamin, Grant Fickes, Eugene Fiorini, Edgar Jaramillo Rodriguez, Eric Jovinelly, and Tony W. H. Wong, "Primes and Perfect Powers in the Catalan Triangle", Journal of Integer Sequences 22 (2019), Article 19.7.6, proof sentence at line 153 (inside the proof of the theorem labeled `c_nn not power`), attributed there to Ramanujan, <https://cs.uwaterloo.ca/journals/JIS/VOL22/Fiorini/fiorini3.tex>.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.ramanujan_two_primes_between`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/RamanujanTwoPrimes.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/RamanujanTwoPrimes.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/index.html#ramanujan-two-primes-between).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime gaps and primes in short intervals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals)
