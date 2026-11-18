---
declaration: theorem
origin: cited
lean: ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal
statement: formalized
proof: formalized
---

# ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal

A nonnegative bound for an alternating map on all orthonormal frames is a bound for
its operator norm, even when the degree exceeds the dimension.

```lean
ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ}
  {ω : E [⋀^Fin k]→L[ℝ] F} {C : ℝ} (hC : 0 ≤ C) :
  ‖ω‖ ≤ C ↔ ∀ (v : Fin k → E), Orthonormal ℝ v → ‖ω v‖ ≤ C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's inequality](../../../number-theory/part-02/successive-minima-and-minkowskis-theorems/hadamards-inequality.md)

## Lean

Formalized in Tau Ceti as [`ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.html#ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal).

## Sources

- [Tau Ceti documentation: `ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.html#ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal)
- [Source of `ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal` in TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.lean#L38)
- [Tau Ceti roadmap status: Calibrations, volume minimization and special Lagrangian geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CalibratedGeometry/STATUS.md)
