---
declaration: abbrev
origin: cited
lean: TauCeti.AlgebraicGeometry.projectivePlaneCurve
statement: formalized
---

# The projective plane curve `G = 0` of a homogeneous polynomial `G ∈ R[X₀, X₁, X₂]`

the
`Proj` of the homogeneous coordinate ring `R[X₀, X₁, X₂] ⧸ (G)`, graded by total degree.

```lean
TauCeti.AlgebraicGeometry.projectivePlaneCurve.{u} {R : Type u} [CommRing R]
  {G : MvPolynomial (Fin 3) R} {d : ℕ} (hG : G.IsHomogeneous d) : AlgebraicGeometry.Scheme
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.projectivePlaneCurve`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Basic.html#TauCeti.AlgebraicGeometry.projectivePlaneCurve).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.projectivePlaneCurve`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Basic.html#TauCeti.AlgebraicGeometry.projectivePlaneCurve)
- [Source of `TauCeti.AlgebraicGeometry.projectivePlaneCurve` in TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Basic.lean#L99)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
