---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.finrank_unstableSubspace_eq_finrank_pointSpectralSubspace_Ioi
statement: formalized
proof: formalized
---

# The inertia theorem for the unstable subspace

If `S` is symmetric and
`c ‖v‖² ≤ ⟪S (A v), v⟫` with `c > 0`, then the dimension of the unstable subspace of `A`, on which
`exp (t • A) v → 0` as `t → -∞`, is the number of positive eigenvalues of `S` counted with
multiplicity.

```lean
ContinuousLinearMap.finrank_unstableSubspace_eq_finrank_pointSpectralSubspace_Ioi.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] {A S : E →L[ℝ] E} {c : ℝ}
  [FiniteDimensional ℝ E] (hS : (↑S).IsSymmetric) (hc : 0 < c)
  (hcS : ∀ (v : E), c * ‖v‖ ^ 2 ≤ inner ℝ (S (A v)) v) :
  Module.finrank ℝ ↥A.unstableSubspace =
    Module.finrank ℝ ↥(Module.End.pointSpectralSubspace (↑S) (Set.Ioi 0))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inertia theorem for the stable subspace](../part-01/the-inertia-theorem-for-the-stable-subspace.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.finrank_unstableSubspace_eq_finrank_pointSpectralSubspace_Ioi`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.html#ContinuousLinearMap.finrank_unstableSubspace_eq_finrank_pointSpectralSubspace_Ioi).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.finrank_unstableSubspace_eq_finrank_pointSpectralSubspace_Ioi`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.html#ContinuousLinearMap.finrank_unstableSubspace_eq_finrank_pointSpectralSubspace_Ioi)
- [Source of `ContinuousLinearMap.finrank_unstableSubspace_eq_finrank_pointSpectralSubspace_Ioi` in TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/LyapunovForm/Inertia.lean#L322)
