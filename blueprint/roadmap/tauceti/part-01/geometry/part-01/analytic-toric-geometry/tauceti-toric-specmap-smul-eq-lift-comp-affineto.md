---
declaration: theorem
origin: cited
lean: TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction
statement: formalized
proof: formalized
---

# TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction

On complex points, the affine scheme action is the character action. The two points of the
action domain are paired by the fibre-product universal property over `Spec ℂ`.

The comparison is intended for explicit rewrites: applying it again to the translated torus point
in the pairing would produce an infinite expansion.

```lean
TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction.{u_3} {N : Type} {V : Type u_3}
  [AddCommGroup N] [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V}
  (hi : TauCeti.Toric.IsIntegralLattice i) (σ : PointedCone ℝ V) (t : TauCeti.Toric.ComplexTorus N)
  (x : TauCeti.Toric.AffineSemigroupComplexPoint ↥(TauCeti.Toric.dualSemigroup hi σ)) :
  AlgebraicGeometry.Spec.map (CommRingCat.ofHom (t • x).toRingHom) =
    CategoryTheory.CategoryStruct.comp
      (CategoryTheory.Limits.pullback.lift
        (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (t • default).toRingHom))
        (AlgebraicGeometry.Spec.map (CommRingCat.ofHom x.toRingHom)) ⋯)
      (TauCeti.Toric.affineToricSchemeAction hi σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Cone/TorusAction/Coaction.html#TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Cone/TorusAction/Coaction.html#TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction)
- [Source of `TauCeti.Toric.specMap_smul_eq_lift_comp_affineToricSchemeAction` in TauCeti/Geometry/Toric/Analytic/Cone/TorusAction/Coaction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Toric/Analytic/Cone/TorusAction/Coaction.lean#L51)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AnalyticToricGeometry/STATUS.md)
