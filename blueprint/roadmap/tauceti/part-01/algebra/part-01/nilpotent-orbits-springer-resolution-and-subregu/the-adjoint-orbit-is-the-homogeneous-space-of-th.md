---
declaration: def
origin: cited
lean: TauCeti.fppfHomogeneousQuotientIsoAdjointOrbitPoints
statement: formalized
---

# The adjoint orbit is the homogeneous space of the centralizer

For a reduced affine group
`G` of finite type over an algebraically closed field, the fppf homogeneous quotient `G / C_G(x)`
is isomorphic to the sheaf of points of the adjoint orbit scheme of `x`, the projective orbit
scheme of the line through `(x, 1)` in `P(𝔤 × k)`.

```lean
TauCeti.fppfHomogeneousQuotientIsoAdjointOrbitPoints.{u} {k : Type u} [Field k] [IsAlgClosed k]
  {H : CommHopfAlgCat k} [Algebra.FiniteType k ↑H] [IsReduced ↑H]
  (x : Module.Dual k (TauCeti.Bialgebra.CotangentSpace k ↑H)) :
  H.fppfHomogeneousQuotient (TauCeti.centralizerHopfIdeal (↑H) x) ≅
    TauCeti.Comodule.projectiveOrbitPointsSheaf (x, 1) ⋯
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fppfHomogeneousQuotientIsoAdjointOrbitPoints`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Orbit.html#TauCeti.fppfHomogeneousQuotientIsoAdjointOrbitPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.fppfHomogeneousQuotientIsoAdjointOrbitPoints`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Orbit.html#TauCeti.fppfHomogeneousQuotientIsoAdjointOrbitPoints)
- [Source of `TauCeti.fppfHomogeneousQuotientIsoAdjointOrbitPoints` in TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Orbit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Orbit.lean#L64)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
