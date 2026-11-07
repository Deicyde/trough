---
declaration: theorem
origin: cited
lean: TauCeti.IsNondegenerateCriticalPoint.exists_stableSet_isManifold
statement: formalized
proof: formalized
---

# TauCeti.IsNondegenerateCriticalPoint.exists\_stableSet\_isManifold

The global stable set of a Morse critical point of a globally `C^(n+1)` function has a `C^n`
manifold structure modelled on the stable Hessian subspace, with its subspace topology and a
`C^n` inclusion into the ambient space. The dimension of the model plus the Morse index equals
the ambient dimension.

```lean
TauCeti.IsNondegenerateCriticalPoint.exists_stableSet_isManifold.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → ℝ} {x : E}
  {K : NNReal} (h : TauCeti.IsNondegenerateCriticalPoint f x) {n : ℕ} (hn : 1 ≤ n)
  (hfs : ContDiff ℝ (↑n + 1) f) (hf : LipschitzWith K (gradient f)) :
  ∃ C,
    IsManifold (modelWithCornersSelf ℝ ↥⋯.stableLinearSubspace) ↑n
        ↑((TauCeti.negativeGradientFlow f hf).stableSet x) ∧
      ContMDiff (modelWithCornersSelf ℝ ↥⋯.stableLinearSubspace) (modelWithCornersSelf ℝ E) (↑n)
        Subtype.val
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNondegenerateCriticalPoint.exists_stableSet_isManifold`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Manifold.html#TauCeti.IsNondegenerateCriticalPoint.exists_stableSet_isManifold).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNondegenerateCriticalPoint.exists_stableSet_isManifold`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Manifold.html#TauCeti.IsNondegenerateCriticalPoint.exists_stableSet_isManifold)
- [Source of `TauCeti.IsNondegenerateCriticalPoint.exists_stableSet_isManifold` in TauCeti/Analysis/Calculus/Morse/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/Manifold.lean#L47)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
