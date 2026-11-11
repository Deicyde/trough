---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.cohomologyBaseChangeLinearEquiv
statement: formalized
---

# Flat base change for the cohomology of quasi-coherent sheaves

**Flat base change for the cohomology of quasi-coherent sheaves**, as the canonical linear
equivalence `R' ⊗_R Hⁿ(X, M) ≃ₗ[R'] Hⁿ(Y, g^* M)` for a quasi-coherent sheaf `M` on a quasi-compact
scheme `X` with affine diagonal over `R` and a flat ring map `R → R'`.

```lean
TauCeti.AlgebraicGeometry.cohomologyBaseChangeLinearEquiv.{u} {R : Type u} [CommRing R]
  {X : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧R)] {R' : Type u} [CommRing R']
  [Algebra R R'] {Y : AlgebraicGeometry.Scheme} [Y.Over (AlgebraicGeometry.Spec ↧R')] {g : Y ⟶ X}
  (H :
    CategoryTheory.IsPullback g (Y ↘ AlgebraicGeometry.Spec ↧R') (X ↘ AlgebraicGeometry.Spec ↧R)
      (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (algebraMap R R'))))
  [Module.Flat R R'] [CompactSpace ↥X]
  [AlgebraicGeometry.IsAffineHom
      (CategoryTheory.Limits.pullback.diagonal (CategoryTheory.Limits.terminal.from X))]
  (M : X.Modules) [SheafOfModules.IsQuasicoherent M] (n : ℕ) :
  TensorProduct R R' (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology M n) ≃ₗ[R']
    TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
      ((AlgebraicGeometry.Scheme.Modules.pullback g).obj M) n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Leray's theorem](../../topology/other-results/lerays-theorem.md)
- [Serre's vanishing theorem on affine opens](../other-results/serres-vanishing-theorem-on-affine-opens.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.cohomologyBaseChangeLinearEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.html#TauCeti.AlgebraicGeometry.cohomologyBaseChangeLinearEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.cohomologyBaseChangeLinearEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.html#TauCeti.AlgebraicGeometry.cohomologyBaseChangeLinearEquiv)
- [Source of `TauCeti.AlgebraicGeometry.cohomologyBaseChangeLinearEquiv` in TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.lean#L285)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)
