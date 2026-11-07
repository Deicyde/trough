---
declaration: def
origin: cited
lean: AbstractMeasure.extendCoefficients
statement: formalized
---

# Extension of coefficients from the unit ball

For a ring homomorphism `j : O →+* K`
into the closed unit ball of a complete ultrametric field, `extendCoefficients j hj μ` is the
`K`-valued measure on the profinite space `X` whose coefficient on each fibre of a map to a finite
discrete space is the image under `j` of the coefficient of `μ`
(`finiteProjection_extendCoefficients`). When `j` is continuous it is the unique `K`-valued measure
with `ι_j(μ)(j ∘ f) = j(μ(f))` for all `f ∈ C(X, O)` (`extendCoefficients_apply_comp`,
`eq_extendCoefficients_of_apply_comp`).

```lean
AbstractMeasure.extendCoefficients.{u_1, u_2, u_3} {X : Type u_1} [TopologicalSpace X]
  {K : Type u_2} {O : Type u_3} [NormedField K] [CommRing O] [TopologicalSpace O]
  [IsTopologicalRing O] (j : O →+* K) [CompactSpace X] [IsUltrametricDist K] [T2Space X]
  [TotallyDisconnectedSpace X] [CompleteSpace K] (hj : ∀ (a : O), ‖j a‖ ≤ 1) :
  AbstractMeasure X O O →+ AbstractMeasure X K K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.extendCoefficients`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/ExtendCoefficients/Basic.html#AbstractMeasure.extendCoefficients).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.extendCoefficients`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/ExtendCoefficients/Basic.html#AbstractMeasure.extendCoefficients)
- [Source of `AbstractMeasure.extendCoefficients` in TauCeti/NumberTheory/Padics/Measure/ExtendCoefficients/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Measure/ExtendCoefficients/Basic.lean#L232)
- [Tau Ceti roadmap status: P-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
