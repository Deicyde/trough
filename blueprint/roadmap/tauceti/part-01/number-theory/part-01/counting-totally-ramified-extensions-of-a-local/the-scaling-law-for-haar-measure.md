---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.addHaar_image_mulVec
statement: formalized
proof: formalized
---

# The scaling law for Haar measure

If the determinant of a square matrix `A` over `𝒪[K]`
is associated to `ϖ ^ k` for a uniformizer `ϖ`, then for every additive Haar measure `μ`
on `ι → K` and every set `s`, `μ (A '' s) = q ^ (-k) * μ s`, where `q = Nat.card 𝓀[K]`. This is
the nonarchimedean analogue of `MeasureTheory.Measure.addHaar_image_linearMap`.

```lean
MeasureTheory.Measure.addHaar_image_mulVec.{u_1, u_2} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {ι : Type u_2} [Fintype ι] [DecidableEq ι]
  [MeasurableSpace (ι → K)] [BorelSpace (ι → K)] (μ : MeasureTheory.Measure (ι → K))
  [μ.IsAddHaarMeasure] {A : Matrix ι ι ↥(ValuativeRel.valuation K).integer}
  {ϖ : ↥(ValuativeRel.valuation K).integer} (hϖ : Irreducible ϖ) {k : ℕ}
  (hk : Associated A.det (ϖ ^ k)) (s : Set (ι → K)) :
  μ ((A.map ⇑(algebraMap (↥(ValuativeRel.valuation K).integer) K)).mulVec '' s) =
    1 / ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^ k * μ s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.addHaar_image_mulVec`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/LocalFieldScaling.html#MeasureTheory.Measure.addHaar_image_mulVec).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.addHaar_image_mulVec`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/LocalFieldScaling.html#MeasureTheory.Measure.addHaar_image_mulVec)
- [Source of `MeasureTheory.Measure.addHaar_image_mulVec` in TauCeti/MeasureTheory/Group/LocalFieldScaling.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Group/LocalFieldScaling.lean#L304)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
