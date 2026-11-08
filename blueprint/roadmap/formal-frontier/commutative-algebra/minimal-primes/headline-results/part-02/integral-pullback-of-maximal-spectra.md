---
declaration: def
origin: cited
lean: MaximalSpectrum.comapOfIsIntegral
statement: formalized
---

# Integral pullback of maximal spectra

For an integral homomorphism `f : R →+* S` of commutative rings in independent
universes,
[`MaximalSpectrum.comapOfIsIntegral`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Spectrum/Maximal/Map.lean)
maps `MaximalSpectrum S` to `MaximalSpectrum R` by ideal contraction. Its image
is exactly the maximal ideals containing `RingHom.ker f`, and it is surjective
when `f` is injective. The API gives the underlying-ideal equation, agreement
with prime-spectrum pullback, identity and contravariant composition.

For the existing Zariski topologies, this function is
[continuous and closed](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Spectrum/Maximal/Topology.lean).
It sends the maximal-spectrum trace of `V(I)` to the trace of `V(I.comap f)`
for every ideal `I` of `S`. Zero rings are allowed; no chosen algebra structure,
domain, Jacobson, Noetherian or finite-type assumption is imposed. Integral
pullback need not be injective, even when the ring homomorphism is injective.

For surjective `f`, the same function is the embedding
`MaximalSpectrum.comapEmbeddingOfSurjective`, with all the same compatibility
laws. The
[product-projection client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/RingTheory/Spectrum/Maximal/Map.lean)
uses this embedding to transport infinitude of the maximal spectrum from a factor
to the product ring with `Infinite.of_injective`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MaximalSpectrum.comapOfIsIntegral` (def), declared in [MinimalPrimes/RingTheory/Spectrum/Maximal/Map.lean, line 46](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Spectrum/Maximal/Map.lean#L46).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `MaximalSpectrum.comapOfIsIntegral` in MinimalPrimes/RingTheory/Spectrum/Maximal/Map.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/RingTheory/Spectrum/Maximal/Map.lean#L46)
