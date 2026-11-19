---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.finrank_stableSubspace_eq_finrank_pointSpectralSubspace_Iio
statement: formalized
proof: formalized
---

# The inertia theorem for the stable subspace

If `S` is symmetric and
`c ‖v‖² ≤ ⟪S (A v), v⟫` with `c > 0`, then the dimension of the stable subspace of `A`, on which
`exp (t • A) v → 0` as `t → ∞`, is the number of negative eigenvalues of `S` counted with
multiplicity.

```lean
ContinuousLinearMap.finrank_stableSubspace_eq_finrank_pointSpectralSubspace_Iio.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] {A S : E →L[ℝ] E} {c : ℝ} [FiniteDimensional ℝ E]
  (hS : (↑S).IsSymmetric) (hc : 0 < c) (hcS : ∀ (v : E), c * ‖v‖ ^ 2 ≤ inner ℝ (S (A v)) v) :
  Module.finrank ℝ ↥A.stableSubspace =
    Module.finrank ℝ ↥(Module.End.pointSpectralSubspace (↑S) (Set.Iio 0))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.finrank_stableSubspace_eq_finrank_pointSpectralSubspace_Iio`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.html#ContinuousLinearMap.finrank_stableSubspace_eq_finrank_pointSpectralSubspace_Iio).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.finrank_stableSubspace_eq_finrank_pointSpectralSubspace_Iio`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.html#ContinuousLinearMap.finrank_stableSubspace_eq_finrank_pointSpectralSubspace_Iio)
- [Source of `ContinuousLinearMap.finrank_stableSubspace_eq_finrank_pointSpectralSubspace_Iio` in TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.lean#L294)
