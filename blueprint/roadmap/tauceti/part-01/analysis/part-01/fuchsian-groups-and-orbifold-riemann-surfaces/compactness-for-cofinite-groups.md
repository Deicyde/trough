---
declaration: theorem
origin: cited
lean: Subgroup.IsCofinite.compactSpace_compactifiedQuotient
statement: formalized
proof: formalized
---

# Compactness for cofinite groups

For a cofinite `Γ ≤ PSL(2, ℝ)`, the quotient `Γ \ ℍ`
with its finitely many cusp orbits adjoined is compact. Together with
`Subgroup.CompactifiedQuotient.instT2Space` and
`Subgroup.CompactifiedQuotient.instSecondCountableTopology`, it is a compact Hausdorff
second-countable space. The discreteness instance is part of `Γ.IsCofinite`; it is assumed
separately only because the topology on `Γ.CompactifiedQuotient` is defined from it.

```lean
Subgroup.IsCofinite.compactSpace_compactifiedQuotient
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  (hΓ : Γ.IsCofinite) : CompactSpace Γ.CompactifiedQuotient
```

## Depends on

- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Proof depends on

- [The Gauss–Bonnet formula](../../part-03/complex/part-02/the-gauss-bonnet-formula.md)
- [Jørgensen's inequality](../../part-03/complex/part-02/jrgensens-inequality.md)
- [The Margulis lemma for Fuchsian groups](../../part-03/complex/part-03/the-margulis-lemma-for-fuchsian-groups.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Shimizu's inequality at two cusps](../../part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.IsCofinite.compactSpace_compactifiedQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.IsCofinite.compactSpace_compactifiedQuotient).

## Sources

- [Tau Ceti documentation: `Subgroup.IsCofinite.compactSpace_compactifiedQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.IsCofinite.compactSpace_compactifiedQuotient)
- [Source of `Subgroup.IsCofinite.compactSpace_compactifiedQuotient` in TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean#L156)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
