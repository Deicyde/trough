---
declaration: theorem
origin: cited
lean: TauCeti.Toric.IsDelzant.isManifold_delzantLevel
statement: formalized
proof: formalized
---

# The level is a smooth manifold

**The level is a smooth manifold** of dimension `d + n`, indeed a `C^m` manifold for every `m`,
including the analytic case `m = ω`, for the atlas
`TauCeti.Toric.IsDelzant.delzantLevelChartedSpace`.

```lean
TauCeti.Toric.IsDelzant.isManifold_delzantLevel.{u_1, u_2, u_3} {ι : Type u_1} {N : Type u_2}
  {V : Type u_3} [Fintype ι] [AddCommGroup N] [NormedAddCommGroup V] [NormedSpace ℝ V] {i : N →+ V}
  {u : ι → N} {c : ι → ℝ} [FiniteDimensional ℝ V] (hΔ : TauCeti.Toric.IsDelzant i u c)
  (hi : TauCeti.Toric.IsIntegralLattice i) (m : WithTop ℕ∞) :
  IsManifold (modelWithCornersSelf ℝ (Fin (Fintype.card ι + Module.finrank ℝ V) → ℝ)) m
    ↑(TauCeti.Toric.delzantLevel i u c)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.IsDelzant.isManifold_delzantLevel`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Delzant/Level.html#TauCeti.Toric.IsDelzant.isManifold_delzantLevel).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.IsDelzant.isManifold_delzantLevel`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Delzant/Level.html#TauCeti.Toric.IsDelzant.isManifold_delzantLevel)
- [Source of `TauCeti.Toric.IsDelzant.isManifold_delzantLevel` in TauCeti/Geometry/Toric/Delzant/Level.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Toric/Delzant/Level.lean#L485)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
