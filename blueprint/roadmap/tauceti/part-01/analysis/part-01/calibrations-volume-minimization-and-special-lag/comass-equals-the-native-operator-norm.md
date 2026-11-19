---
declaration: theorem
origin: cited
lean: ContinuousAlternatingMap.norm_eq_sSup_abs_orthonormal
statement: formalized
proof: formalized
---

# Comass equals the native operator norm

the norm of a real alternating form is
the supremum of its absolute values on orthonormal frames, in every degree.

```lean
ContinuousAlternatingMap.norm_eq_sSup_abs_orthonormal.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {k : ℕ} (ω : E [⋀^Fin k]→L[ℝ] ℝ) :
  ‖ω‖ = sSup {r | ∃ v, Orthonormal ℝ v ∧ r = |ω v|}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ContinuousAlternatingMap.opNorm_le_iff_le_orthonormal](continuousalternatingmap-opnorm-le-iff-le-orthon.md)

## Lean

Formalized in Tau Ceti as [`ContinuousAlternatingMap.norm_eq_sSup_abs_orthonormal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.html#ContinuousAlternatingMap.norm_eq_sSup_abs_orthonormal).

## Sources

- [Tau Ceti documentation: `ContinuousAlternatingMap.norm_eq_sSup_abs_orthonormal`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.html#ContinuousAlternatingMap.norm_eq_sSup_abs_orthonormal)
- [Source of `ContinuousAlternatingMap.norm_eq_sSup_abs_orthonormal` in TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Orthonormal/Alternating.lean#L91)
- [Tau Ceti roadmap status: Calibrations, volume minimization and special Lagrangian geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CalibratedGeometry/STATUS.md)
