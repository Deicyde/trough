---
declaration: def
origin: cited
lean: TauCeti.isLimitLocalHomologySystemCone
statement: formalized
---

# The top homology of a compact manifold is the module of parallel families of local classes

For a compact Hausdorff space modelled on a real normed space of finite dimension `n`,
the restrictions `Hₙ(M, M ∖ M; N) ⟶ Hₙ(M, M ∖ {x}; N)` exhibit `Hₙ(M, M ∖ M; N)` as the limit of
the local homology system: every transport-invariant family of local classes is the family of
restrictions of exactly one class.

```lean
TauCeti.isLimitLocalHomologySystemCone.{w} {Λ : Type w} [Ring Λ] (N : ModuleCat Λ) (M E : Type w)
  [TopologicalSpace M] [T2Space M] [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [ChartedSpace E M] [CompactSpace M] {n : ℕ} (hn : Module.finrank ℝ E = n) :
  CategoryTheory.Limits.IsLimit (TauCeti.localHomologySystemCone N M E n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isLimitLocalHomologySystemCone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/LocalHomology/TopHomology.html#TauCeti.isLimitLocalHomologySystemCone).

## Sources

- [Tau Ceti documentation: `TauCeti.isLimitLocalHomologySystemCone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/LocalHomology/TopHomology.html#TauCeti.isLimitLocalHomologySystemCone)
- [Source of `TauCeti.isLimitLocalHomologySystemCone` in TauCeti/AlgebraicTopology/Singular/LocalHomology/TopHomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/LocalHomology/TopHomology.lean#L92)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
