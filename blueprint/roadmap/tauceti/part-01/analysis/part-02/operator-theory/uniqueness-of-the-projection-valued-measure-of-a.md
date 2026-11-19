---
declaration: theorem
origin: cited
lean: TauCeti.ProjValMeasure.eq_ofRepresentation_iff
statement: formalized
proof: formalized
---

# Uniqueness of the projection-valued measure of a representation

A projection-valued
measure on `K` whose diagonal measures are regular is the projection-valued measure of `π` iff
integrating every continuous function against it gives its image under `π`.

```lean
TauCeti.ProjValMeasure.eq_ofRepresentation_iff.{u_1, u_2} {K : Type u_1} [TopologicalSpace K]
  [CompactSpace K] [T2Space K] [MeasurableSpace K] [BorelSpace K] {H : Type u_2}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] (π : C(K, ℂ) →⋆ₐ[ℂ] H →L[ℂ] H)
  (P : TauCeti.ProjValMeasure K H) (hP : ∀ (ξ : H), (P.diag ξ).Regular) :
  P = TauCeti.ProjValMeasure.ofRepresentation π ↔
    ∀ (f : C(K, ℂ)), P.integral (TauCeti.BoundedBorelFunction.ofContinuousMap f) = π f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ProjValMeasure.eq_ofRepresentation_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Representation/OfRepresentation.html#TauCeti.ProjValMeasure.eq_ofRepresentation_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ProjValMeasure.eq_ofRepresentation_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Representation/OfRepresentation.html#TauCeti.ProjValMeasure.eq_ofRepresentation_iff)
- [Source of `TauCeti.ProjValMeasure.eq_ofRepresentation_iff` in TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Representation/OfRepresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Representation/OfRepresentation.lean#L129)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorTheory/STATUS.md)
