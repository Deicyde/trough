---
declaration: theorem
origin: cited
lean: PositiveLinearMap.law_eq_map_gns_diagMeasure
statement: formalized
proof: formalized
---

# PositiveLinearMap.law_eq_map_gns_diagMeasure

The C⋆-algebraic law is the scalar spectral measure of the GNS operator at the canonical
cyclic vector, viewed as a measure on the real line. This holds even for nonfaithful states.

```lean
PositiveLinearMap.law_eq_map_gns_diagMeasure.{u_1} {A : Type u_1} [CStarAlgebra A] [PartialOrder A]
  [StarOrderedRing A] (φ : A →ₚ[ℂ] ℂ) {a : A} (ha : IsSelfAdjoint a) :
  have x := ⋯;
  φ.law a =
    MeasureTheory.Measure.map (fun z => (↑z).re) ((φ.gnsStarAlgHom a).diagMeasure φ.gnsVector)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [PositiveLinearMap.eq_law_iff](positivelinearmap-eq-law-iff.md)

## Lean

Formalized in Tau Ceti as [`PositiveLinearMap.law_eq_map_gns_diagMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/GNS.html#PositiveLinearMap.law_eq_map_gns_diagMeasure).

## Sources

- [Tau Ceti documentation: `PositiveLinearMap.law_eq_map_gns_diagMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/GNS.html#PositiveLinearMap.law_eq_map_gns_diagMeasure)
- [Source of `PositiveLinearMap.law_eq_map_gns_diagMeasure` in TauCeti/Probability/FreeProbability/Law/GNS.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Law/GNS.lean#L60)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
