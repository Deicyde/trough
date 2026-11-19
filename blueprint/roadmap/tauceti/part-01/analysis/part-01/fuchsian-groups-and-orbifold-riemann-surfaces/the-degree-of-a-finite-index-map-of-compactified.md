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
- [Rouché's theorem for a disc, classical form](../../part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.degree_compactifiedQuotientMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.html#Subgroup.degree_compactifiedQuotientMap).

## Sources

- [Tau Ceti documentation: `Subgroup.degree_compactifiedQuotientMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.html#Subgroup.degree_compactifiedQuotientMap)
- [Source of `Subgroup.degree_compactifiedQuotientMap` in TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Fuchsian/Compactification/Degree.lean#L127)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
