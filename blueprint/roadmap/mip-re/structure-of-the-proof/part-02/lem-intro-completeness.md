---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.CanonicalComplete.output_hasPerfectPCC
statement: formalized
proof: formalized
---

# Completeness of introspection

If $\mathsf{V}_{2^n}$ has a value-$1$ PCC strategy, then $\mathsf{V}^{\textsc{Intro}}_n$ has one: the players measure their EPR halves in the bases the sampled question prescribes and then play the value-$1$ strategy of $\mathsf{V}_{2^n}$ on the question they have obtained. Every test of the decider accepts with certainty, and the resulting strategy is again projective, consistent and commuting. The Lean proof is that of Lemma [Concrete completeness for the full typed introspection game](../part-05/lem-intro-full-typed-completeness.md), carried to the ambient output verifier: explicit Pauli and auxiliary measurements on a common carrier, rather than the Fourier and commutation argument below.

## Depends on

- [The introspective verifier](def-intro-verifier.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md)
- [A commutation criterion for $X$ and $Z$ measurements](lem-pauli-commute-criterion.md)
- [Honest sampling core and first hiding test](../part-03/lem-intro-honest-core.md)
- [Adaptive honest Read and Hide measurements](../part-03/lem-intro-honest-adaptive.md)
- [Honest hiding marginals and edge compatibility](../part-03/lem-intro-honest-hiding.md)
- [Honest operators on the complete parsed alphabet](../part-03/lem-intro-honest-parsed.md)

## Proof depends on

- [Full question transport and actual QLD extraction](../part-06/lem-intro-numbered-transport.md)
- [The ambient compiler's resources and raw-game bridge](../part-06/lem-intro-ambient-kernel.md)

## Proof

Lemma [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md) identifies the honest sampling measurement with a Pauli measurement, which is what the Pauli test checks; Lemma [A commutation criterion for $X$ and $Z$ measurements](lem-pauli-commute-criterion.md) gives the commutation the hiding test needs, the hypothesis $\ker(R)^\perp \subseteq \ker(L)$ being exactly the nesting of consecutive conditionally linear levels. Consistency and projectivity pass through the construction because each player's measurement is a product of commuting projective measurements.

## Lean

Formalized as [`MIPRE.Introspection.CanonicalComplete.output_hasPerfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CanonicalComplete.output_hasPerfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1290](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1290)
