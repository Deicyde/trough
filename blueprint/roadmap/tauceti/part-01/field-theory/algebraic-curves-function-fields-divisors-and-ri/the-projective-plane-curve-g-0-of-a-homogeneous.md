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
- [Source of `TauCeti.AlgebraicGeometry.projectivePlaneCurve` in TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Curves/PlaneCurve/Basic.lean#L99)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
