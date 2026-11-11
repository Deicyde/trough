---
declaration: def
origin: cited
lean: TauCeti.CurrentAlgebra.residueClassEquiv
statement: formalized
---

# Continuous second cohomology of formal currents with discrete coefficients

Under the
hypotheses of `exists_eq_twoCochainOfBilinearSMulRight_add_d₁₂`, for every vector space `Z` with
trivial action, of arbitrary dimension, the residue class map `z ↦ [c_Ψ ⊗ z]` is a linear
equivalence from `Z` onto the continuous second cohomology of formal currents with coefficients in
`Z`. For `Z = K` it sends `t` to `t • residueClass` (`residueClassMap_self`).

```lean
TauCeti.CurrentAlgebra.residueClassEquiv.{u_4, u_5, u_6} {K : Type u_4} {L : Type u_5} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [LieAlgebra.IsKilling K L]
  (Z : Type u_6) [AddCommGroup Z] [_root_.Module K Z] {Ψ : LinearMap.BilinForm K L}
  (hΨ : LinearMap.BilinForm.lieInvariant L Ψ) (hΨs : Ψ.IsSymm)
  (hspan : ∀ (Φ : LinearMap.BilinForm K L), LinearMap.BilinForm.lieInvariant L Φ → ∃ t, Φ = t • Ψ)
  (hΨ0 : Ψ ≠ 0) :
  Z ≃ₗ[K]
    TauCeti.LieModule.Cohomology.continuousSecondCohomology K (TauCeti.currentAlgebra K L)
      (TrivialLieModule K (TauCeti.currentAlgebra K L) Z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Whitehead's first lemma](../../part-02/lie/part-02/whiteheads-first-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.residueClassEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/ContinuousCohomology.html#TauCeti.CurrentAlgebra.residueClassEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.residueClassEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/ContinuousCohomology.html#TauCeti.CurrentAlgebra.residueClassEquiv)
- [Source of `TauCeti.CurrentAlgebra.residueClassEquiv` in TauCeti/Algebra/Lie/Current/ContinuousCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Current/ContinuousCohomology.lean#L529)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
