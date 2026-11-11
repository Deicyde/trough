---
declaration: theorem
origin: cited
lean: TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift
statement: formalized
proof: formalized
---

# TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift

The nonzero scalar residue extension is initial among extensions represented by
continuous two-cocycles with arbitrary trivial coefficients. The unique map lies over
the identity on currents; no condition on its map of kernels is imposed.

```lean
TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift.{u_1, u_2, u_3} {K : Type u_1}
  {L : Type u_2} {Z : Type u_3} [Field K] [CharZero K] [LieRing L] [LieAlgebra K L]
  [FiniteDimensional K L] [LieAlgebra.IsKilling K L] [AddCommGroup Z] [_root_.Module K Z]
  {Φ : LinearMap.BilinForm K L} (hΦ : LinearMap.BilinForm.lieInvariant L Φ) (hΦs : Φ.IsSymm)
  (hspan : ∀ (Ψ : LinearMap.BilinForm K L), LinearMap.BilinForm.lieInvariant L Ψ → ∃ t, Ψ = t • Φ)
  (hΦ0 : Φ ≠ 0)
  (c :
    ↥(LieModule.Cohomology.twoCocycle K (TauCeti.currentAlgebra K L)
        (TrivialLieModule K (TauCeti.currentAlgebra K L) Z)))
  (hc :
    ↑c ∈
      TauCeti.LieModule.Cohomology.continuousTwoCocycle K (TauCeti.currentAlgebra K L)
        (TrivialLieModule K (TauCeti.currentAlgebra K L) Z)) :
  ∃! F,
    (LieAlgebra.ofTwoCocycle.proj c).comp F =
      LieAlgebra.ofTwoCocycle.proj (TauCeti.CurrentAlgebra.twoCocycleOfBilinear K L Φ hΦ hΦs)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Whitehead's first lemma](../../part-02/lie/part-02/whiteheads-first-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Universal.html#TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Universal.html#TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift)
- [Source of `TauCeti.CurrentAlgebra.existsUnique_residueExtensionLift` in TauCeti/Algebra/Lie/Current/Universal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Current/Universal.lean#L88)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
