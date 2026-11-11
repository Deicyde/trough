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

- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Rouché's theorem for a disc, classical form](../../part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.degree_compactifiedQuotientMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.html#Subgroup.degree_compactifiedQuotientMap).

## Sources

- [Tau Ceti documentation: `Subgroup.degree_compactifiedQuotientMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.html#Subgroup.degree_compactifiedQuotientMap)
- [Source of `Subgroup.degree_compactifiedQuotientMap` in TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.lean#L127)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
