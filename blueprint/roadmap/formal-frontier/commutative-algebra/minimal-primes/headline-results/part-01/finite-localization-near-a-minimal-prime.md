---
declaration: theorem
origin: cited
lean: Algebra.FiniteType.exists_finite_awayMap_of_mem_minimalPrimes
statement: formalized
proof: formalized
---

# Finite localization near a minimal prime

For a finite-type algebra over any commutative ring, module finiteness of the
residue-field fibre at a minimal prime gives finiteness after inverting an element
outside that prime. The map is the canonical localization of the given algebra map.
[`Algebra.FiniteType.exists_finite_awayMap_of_mem_minimalPrimes`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/MinimalPrimeLocalization.lean)
requires no reducedness or Noetherian hypothesis and includes the zero algebra.
The supporting [nil-integrality lemmas](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/IntegralNilpotent.lean)
lift monic relations using individual nilpotence rather than a uniformly nilpotent ideal.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Algebra.FiniteType.exists_finite_awayMap_of_mem_minimalPrimes` (theorem), declared in [MinimalPrimes/RingTheory/Ideal/MinimalPrimeLocalization.lean, line 197](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/MinimalPrimeLocalization.lean#L197).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Algebra.FiniteType.exists_finite_awayMap_of_mem_minimalPrimes` in MinimalPrimes/RingTheory/Ideal/MinimalPrimeLocalization.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Ideal/MinimalPrimeLocalization.lean#L197)
