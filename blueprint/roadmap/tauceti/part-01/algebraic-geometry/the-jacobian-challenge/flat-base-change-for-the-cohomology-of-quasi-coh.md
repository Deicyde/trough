---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange
statement: formalized
proof: formalized
---

# Flat base change for the cohomology of quasi-coherent sheaves

Let `X` be a
quasi-compact quasi-separated scheme over `R`, let `R → R'` be flat and let `Y = X ×_R R'`,
given as a pullback square with projection `g`. For every quasi-coherent sheaf `M` on `X`
and every `n`, the canonical map `R' ⊗_R Hⁿ(X, M) ⟶ Hⁿ(Y, g^* M)` is bijective.

```lean
TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange.{u} {R : Type u} [CommRing R]
  {X : AlgebraicGeometry.Scheme} [X.Over (AlgebraicGeometry.Spec ↧R)] {R' : Type u} [CommRing R']
  [Algebra R R'] {Y : AlgebraicGeometry.Scheme} [Y.Over (AlgebraicGeometry.Spec ↧R')] {g : Y ⟶ X}
  (H :
    CategoryTheory.IsPullback g (Y ↘ AlgebraicGeometry.Spec ↧R') (X ↘ AlgebraicGeometry.Spec ↧R)
      (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (algebraMap R R'))))
  [Module.Flat R R'] [CompactSpace ↥X] [QuasiSeparatedSpace ↥X] (M : X.Modules)
  [SheafOfModules.IsQuasicoherent M] (n : ℕ) :
  Function.Bijective ⇑(TauCeti.AlgebraicGeometry.cohomologyBaseChange H M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's vanishing theorem on affine opens](../other-results/serres-vanishing-theorem-on-affine-opens.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.html#TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.html#TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange)
- [Source of `TauCeti.AlgebraicGeometry.bijective_cohomologyBaseChange` in TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Cohomology/FlatBaseChange.lean#L533)
- [Tau Ceti roadmap status: The Jacobian challenge](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/JacobianChallenge/STATUS.md)
