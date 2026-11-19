---
declaration: instance
origin: cited
lean: TauCeti.Toric.Fan.algebraicRealizationModObj
statement: formalized
---

# TauCeti.Toric.Fan.algebraicRealizationModObj

The dense torus acts on the fan scheme over `Spec ℂ` by the glued affine torus actions.

```lean
TauCeti.Toric.Fan.algebraicRealizationModObj.{u_1} {N : Type} {V : Type u_1} [AddCommGroup N]
  [AddCommGroup V] [_root_.Module ℝ V] {i : N →+ V} (Φ : TauCeti.Toric.Fan i) :
  CategoryTheory.ModObj ((TauCeti.Toric.affineToricScheme ⋯ ⊥).asOver (AlgebraicGeometry.Spec ↧ℂ))
    (Φ.algebraicRealization.asOver (AlgebraicGeometry.Spec ↧ℂ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.algebraicRealizationModObj`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/Fan/TorusAction/Action.html#TauCeti.Toric.Fan.algebraicRealizationModObj).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.algebraicRealizationModObj`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/Fan/TorusAction/Action.html#TauCeti.Toric.Fan.algebraicRealizationModObj)
- [Source of `TauCeti.Toric.Fan.algebraicRealizationModObj` in TauCeti/Geometry/Toric/Algebraic/Fan/TorusAction/Action.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Algebraic/Fan/TorusAction/Action.lean#L169)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AnalyticToricGeometry/STATUS.md)
