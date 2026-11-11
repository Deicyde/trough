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

- [The Gauss–Bonnet formula](../../part-02/complex/part-01/the-gauss-bonnet-formula.md)
- [Jørgensen's inequality](../../part-02/complex/part-02/jrgensens-inequality.md)
- [The Margulis lemma for Fuchsian groups](../../part-02/complex/part-02/the-margulis-lemma-for-fuchsian-groups.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.IsCofinite.compactSpace_compactifiedQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.IsCofinite.compactSpace_compactifiedQuotient).

## Sources

- [Tau Ceti documentation: `Subgroup.IsCofinite.compactSpace_compactifiedQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.IsCofinite.compactSpace_compactifiedQuotient)
- [Source of `Subgroup.IsCofinite.compactSpace_compactifiedQuotient` in TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean#L157)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
