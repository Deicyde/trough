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
- [Source of `TauCeti.Toric.IsDelzant.isManifold_delzantLevel` in TauCeti/Geometry/Toric/Delzant/Level.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Delzant/Level.lean#L587)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
