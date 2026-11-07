---
declaration: theorem
origin: cited
lean: Subgroup.degree_compactifiedQuotientMap
statement: formalized
proof: formalized
---

# The degree of a finite-index map of compactified Fuchsian quotients is the index

For
`Δ ≤ Γ` discrete of finite index, the map `X(Δ) → X(Γ)` induced by the inclusion has degree
`[Γ : Δ]`.

```lean
Subgroup.degree_compactifiedQuotientMap
  {Δ Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ] (h : Δ ≤ Γ)
  [Δ.IsFiniteRelIndex Γ] :
  TauCeti.RiemannSurface.degree (Subgroup.compactifiedQuotientMap h) = (Δ.subgroupOf Γ).index
```

## Depends on

- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Proof depends on

- [Descent of an invariant map to the orbit space](../../part-02/complex-manifolds-transport-quotients-bundles-an/descent-of-an-invariant-map-to-the-orbit-space.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.degree_compactifiedQuotientMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.html#Subgroup.degree_compactifiedQuotientMap).

## Sources

- [Tau Ceti documentation: `Subgroup.degree_compactifiedQuotientMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.html#Subgroup.degree_compactifiedQuotientMap)
- [Source of `Subgroup.degree_compactifiedQuotientMap` in TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.lean#L127)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
