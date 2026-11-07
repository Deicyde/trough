---
declaration: theorem
origin: cited
lean: TauCeti.CurrentAlgebra.derivedSeries_ofTwoCocycle_eq_top_iff
statement: formalized
proof: formalized
---

# TauCeti.CurrentAlgebra.derivedSeries\_ofTwoCocycle\_eq\_top\_iff

The residue central extension of a perfect Lie algebra over a field is perfect if and
only if its form is nonzero. No finite-dimensionality or characteristic assumption is needed.

```lean
TauCeti.CurrentAlgebra.derivedSeries_ofTwoCocycle_eq_top_iff.{u_2, u_3} (L : Type u_2) [LieRing L]
  {K : Type u_3} [Field K] [LieAlgebra K L] (Ψ : LinearMap.BilinForm K L)
  (hΨ : LinearMap.BilinForm.lieInvariant L Ψ) (hΨs : Ψ.IsSymm)
  (hperfect : LieAlgebra.derivedSeries K L 1 = ⊤) :
  LieAlgebra.derivedSeries K
        (LieAlgebra.ofTwoCocycle (TauCeti.CurrentAlgebra.twoCocycleOfBilinear K L Ψ hΨ hΨs)) 1 =
      ⊤ ↔
    Ψ ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.derivedSeries_ofTwoCocycle_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Perfect.html#TauCeti.CurrentAlgebra.derivedSeries_ofTwoCocycle_eq_top_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.derivedSeries_ofTwoCocycle_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Perfect.html#TauCeti.CurrentAlgebra.derivedSeries_ofTwoCocycle_eq_top_iff)
- [Source of `TauCeti.CurrentAlgebra.derivedSeries_ofTwoCocycle_eq_top_iff` in TauCeti/Algebra/Lie/Current/Perfect.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Current/Perfect.lean#L127)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
