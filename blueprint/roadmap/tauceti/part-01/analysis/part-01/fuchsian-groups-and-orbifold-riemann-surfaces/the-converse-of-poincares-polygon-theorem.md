---
declaration: theorem
origin: cited
lean: Subgroup.IsCofinite.exists_sidePairing_closure_range_map_eq
statement: formalized
proof: formalized
---

# The converse of Poincaré's polygon theorem

Every cofinite `Γ ≤ PSL(2, ℝ)` arises from
Poincaré's polygon theorem. For a centre `p` with trivial stabilizer, the Dirichlet domain of `Γ`
centred at `p` is the carrier of a convex polygon with finitely many vertices and a side pairing
whose maps generate `Γ`. The cycle transformation of each finite vertex has finite order `m` and
the interior angles along its cycle add up to `2π / m`, and the cycle transformation of each ideal
vertex is parabolic. These are the hypotheses of
`TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.isCofinite_of_isParabolic`.

```lean
Subgroup.IsCofinite.exists_sidePairing_closure_range_map_eq
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (hΓ : Γ.IsCofinite)
  {p : UpperHalfPlane} (hp : p ∈ TauCeti.freeLocus (↥Γ) UpperHalfPlane) :
  ∃ n,
    ∃ (x : NeZero n),
      ∃ P σ,
        P.carrier = TauCeti.dirichletDomain (↥Γ) p ∧
          Subgroup.closure (Set.range σ.map) = Γ ∧
            (∀ (j : Fin n) (z : UpperHalfPlane),
                P.vertex j = Sum.inl z →
                  ↑(orderOf (σ.cycleMap j)) * σ.cycleAngleSum j = 2 * Real.pi) ∧
              ∀ (j : Fin n) (ξ : OnePoint ℝ), P.vertex j = Sum.inr ξ → (σ.cycleMap j).IsParabolic
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gauss–Bonnet formula](../../part-02/complex/part-01/the-gauss-bonnet-formula.md)
- [Jørgensen's inequality](../../part-02/complex/part-02/jrgensens-inequality.md)
- [The Margulis lemma for Fuchsian groups](../../part-02/complex/part-02/the-margulis-lemma-for-fuchsian-groups.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.IsCofinite.exists_sidePairing_closure_range_map_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.IsCofinite.exists_sidePairing_closure_range_map_eq).

## Sources

- [Tau Ceti documentation: `Subgroup.IsCofinite.exists_sidePairing_closure_range_map_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.html#Subgroup.IsCofinite.exists_sidePairing_closure_range_map_eq)
- [Source of `Subgroup.IsCofinite.exists_sidePairing_closure_range_map_eq` in TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/Cofinite.lean#L198)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
