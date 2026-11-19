---
declaration: theorem
origin: cited
lean: TauCeti.Huber.PairOfDefinition.isStronglyNoetherian_completion
statement: formalized
proof: formalized
---

# A rational localisation of a strongly noetherian Tate ring is strongly noetherian

**A rational localisation of a strongly noetherian Tate ring is strongly noetherian**,
whenever the numerators together with the denominator `s` generate the unit ideal.

Strong noetherianity of `A` alone suffices: nothing is assumed of the localisation, and the
hypothesis on the numerators is the rational-subset condition, which holds by definition wherever
`A⟨T/s⟩` is the ring of a rational subset.

This is the form Wedhorn's §8.2 needs in order to iterate: it makes strong noetherianity stable
under passing to a rational localisation, so the argument may be repeated inside `A⟨T/s⟩`.

```lean
TauCeti.Huber.PairOfDefinition.isStronglyNoetherian_completion.{u_1, u_2} {A : Type u_1}
  [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsTateRing A]
  [TauCeti.Huber.IsStronglyNoetherian A] (P : TauCeti.Huber.PairOfDefinition A) (T : Finset A)
  (s : A) (S : Type u_2) [CommRing S] [Algebra A S] [IsLocalization.Away s S]
  (hden : P.HasDenominatorPower (↑T) s S) (hspan : Ideal.span (insert s ↑T) = ⊤) :
  TauCeti.Huber.IsStronglyNoetherian (UniformSpace.Completion S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The open mapping theorem over a Tate ring](the-open-mapping-theorem-over-a-tate-ring.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.PairOfDefinition.isStronglyNoetherian_completion`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/LocalizationTopology/StronglyNoetherian.html#TauCeti.Huber.PairOfDefinition.isStronglyNoetherian_completion).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.PairOfDefinition.isStronglyNoetherian_completion`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/LocalizationTopology/StronglyNoetherian.html#TauCeti.Huber.PairOfDefinition.isStronglyNoetherian_completion)
- [Source of `TauCeti.Huber.PairOfDefinition.isStronglyNoetherian_completion` in TauCeti/RingTheory/Huber/LocalizationTopology/StronglyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/LocalizationTopology/StronglyNoetherian.lean#L95)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AdicSpaces/STATUS.md)
