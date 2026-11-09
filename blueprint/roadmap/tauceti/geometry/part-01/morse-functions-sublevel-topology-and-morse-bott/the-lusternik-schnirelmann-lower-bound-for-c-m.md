---
declaration: theorem
origin: cited
lean: TauCeti.lsCategoryCount_univ_le_minCriticalCount
statement: formalized
proof: formalized
---

# The Lusternik–Schnirelmann lower bound for `c(M)`

On a compact boundaryless manifold,
every smooth function has at least as many critical points as the Lusternik–Schnirelmann count of
`M`, so `c(M)` is bounded below by that count.

```lean
TauCeti.lsCategoryCount_univ_le_minCriticalCount.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [I.Boundaryless] [CompactSpace M] [FiniteDimensional ℝ E] [T2Space M] [IsManifold I (↑⊤) M] :
  TauCeti.lsCategoryCount M Set.univ ≤ TauCeti.minCriticalCount I M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Lusternik–Schnirelmann theorem](the-lusternik-schnirelmann-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_univ_le_minCriticalCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/MinCriticalCount.html#TauCeti.lsCategoryCount_univ_le_minCriticalCount).

## Sources

- [Tau Ceti documentation: `TauCeti.lsCategoryCount_univ_le_minCriticalCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/MinCriticalCount.html#TauCeti.lsCategoryCount_univ_le_minCriticalCount)
- [Source of `TauCeti.lsCategoryCount_univ_le_minCriticalCount` in TauCeti/Geometry/Manifold/Morse/MinCriticalCount.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/MinCriticalCount.lean#L119)
