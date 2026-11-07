---
declaration: theorem
origin: cited
lean: Subgroup.compactSpace_compactifiedQuotient_of_isBounded_truncation
statement: formalized
proof: formalized
---

# Compactness from a Dirichlet domain with a bounded cusp truncation

If a discrete
subgroup `Γ` has finitely many cusp orbits, and some Dirichlet domain of `Γ` is bounded after
removing finitely many cusp horodiscs of positive heights, then the quotient `Γ \ ℍ` with its cusp
orbits adjoined is compact.

```lean
Subgroup.compactSpace_compactifiedQuotient_of_isBounded_truncation.{u_1}
  (Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)) [DiscreteTopology ↥Γ]
  {ι : Type u_1} [Finite ι] [Finite Γ.CuspOrbit] (p : UpperHalfPlane) (D : ι → Γ.CuspDatum)
  {A : ι → ℝ} (hA : ∀ (i : ι), 0 < A i)
  (hb :
    Bornology.IsBounded
      (TauCeti.dirichletDomain (↥Γ) p \ ⋃ i, TauCeti.Subgroup.CuspDatum.horodisc (D i) (A i))) :
  CompactSpace Γ.CompactifiedQuotient
```

## Depends on

- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.compactSpace_compactifiedQuotient_of_isBounded_truncation`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Polygon.html#Subgroup.compactSpace_compactifiedQuotient_of_isBounded_truncation).

## Sources

- [Tau Ceti documentation: `Subgroup.compactSpace_compactifiedQuotient_of_isBounded_truncation`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Polygon.html#Subgroup.compactSpace_compactifiedQuotient_of_isBounded_truncation)
- [Source of `Subgroup.compactSpace_compactifiedQuotient_of_isBounded_truncation` in TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Polygon.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Polygon.lean#L73)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
