---
declaration: theorem
origin: cited
lean: Subgroup.isCofinite_iff_exists_convexPolygon_carrier_eq_dirichletDomain
statement: formalized
proof: formalized
---

# Cofiniteness from Dirichlet polygons

A discrete subgroup `Γ ≤ PSL(2, ℝ)` is cofinite
exactly when its Dirichlet domain centred at a point `p` is the carrier of a convex polygon with
finitely many vertices, possibly ideal. The converse direction is the Gauss–Bonnet formula: such
a polygon has finite area, and the translates of the Dirichlet domain cover `ℍ`.

```lean
Subgroup.isCofinite_iff_exists_convexPolygon_carrier_eq_dirichletDomain
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  (p : UpperHalfPlane) :
  Γ.IsCofinite ↔ ∃ n, ∃ (x : NeZero n), ∃ P, P.carrier = TauCeti.dirichletDomain (↥Γ) p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gauss–Bonnet formula](../../part-03/complex/part-02/the-gauss-bonnet-formula.md)
- [Jørgensen's inequality](../../part-03/complex/part-02/jrgensens-inequality.md)
- [The Margulis lemma for Fuchsian groups](../../part-03/complex/part-03/the-margulis-lemma-for-fuchsian-groups.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Shimizu's inequality at two cusps](../../part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.isCofinite_iff_exists_convexPolygon_carrier_eq_dirichletDomain`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.isCofinite_iff_exists_convexPolygon_carrier_eq_dirichletDomain).

## Sources

- [Tau Ceti documentation: `Subgroup.isCofinite_iff_exists_convexPolygon_carrier_eq_dirichletDomain`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.isCofinite_iff_exists_convexPolygon_carrier_eq_dirichletDomain)
- [Source of `Subgroup.isCofinite_iff_exists_convexPolygon_carrier_eq_dirichletDomain` in TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean#L235)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
