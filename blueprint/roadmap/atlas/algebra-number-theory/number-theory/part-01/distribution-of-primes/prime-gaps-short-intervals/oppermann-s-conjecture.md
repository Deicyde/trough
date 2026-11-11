---
declaration: section
origin: cited
lean: MetaMathlibExt.oppermannLowerPrimeCount, MetaMathlibExt.oppermannUpperPrimeCount, MetaMathlibExt.oppermannAsymptotic
statement: formalized
proof: formalized
---

# Oppermann's conjecture

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/oppermann-s-conjecture/index.html).

## Primes in the lower Oppermann interval

For a natural number $n$, this is the number of
primes $p$ with $n^2 - n \le p \le n^2$.

Formalized by `MetaMathlibExt.oppermannLowerPrimeCount`, a definition declared in [MathlibExt/NumberTheory/CountingOppermannPrimes.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CountingOppermannPrimes.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/oppermann-s-conjecture/index.html#oppermann-lower-prime-count).

## Primes in the upper Oppermann interval

For a natural number $n$, this is the number of
primes $p$ with $n^2 \le p \le n^2 + n$.

Formalized by `MetaMathlibExt.oppermannUpperPrimeCount`, a definition declared in [MathlibExt/NumberTheory/CountingOppermannPrimes.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CountingOppermannPrimes.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/oppermann-s-conjecture/index.html#oppermann-upper-prime-count).

## Main term for the Oppermann prime counts

For a natural number $n$, this is the real
number $n / (2 \log n)$, where $\log$ is the natural logarithm. It is used as the asymptotic main
term for the number of primes in each of the intervals $[n^2 - n, n^2]$ and $[n^2, n^2 + n]$.

For $n \le 1$ we have $\log n = 0$, and the value is $0$ by the convention that division by zero
gives zero; this does not affect the asymptotics.

Formalized by `MetaMathlibExt.oppermannAsymptotic`, a definition declared in [MathlibExt/NumberTheory/CountingOppermannPrimes.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CountingOppermannPrimes.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/oppermann-s-conjecture/index.html#oppermann-asymptotic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Oppermann's conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/oppermann-s-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/oppermann-s-conjecture)
