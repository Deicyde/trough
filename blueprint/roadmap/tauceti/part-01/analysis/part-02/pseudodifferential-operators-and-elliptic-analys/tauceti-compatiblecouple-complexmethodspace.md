---
declaration: def
origin: cited
lean: TauCeti.CompatibleCouple.ComplexMethodSpace
statement: formalized
---

# TauCeti.CompatibleCouple.ComplexMethodSpace

The complex interpolation space `[X₀, X₁]_θ` of the couple, for `0 ≤ θ ≤ 1`: the quotient of
the space of admissible functions (realised by their boundary traces, `stripTraces`) by those
vanishing at `θ`, with the quotient norm
`‖u‖_θ = inf {‖g‖ | F θ = u for the admissible function F with traces g}`
(`ComplexMethodSpace.norm_lt_iff`). It is a Banach space when `X₀` and `X₁` are, and it embeds
injectively into the sum space by `ComplexMethodSpace.toSum`. For `θ` outside `[0, 1]` the
evaluation `stripEval θ` vanishes, so the space is zero
(`ComplexMethodSpace.eq_zero_of_notMem`).

```lean
TauCeti.CompatibleCouple.ComplexMethodSpace.{u_1, u_2, u_3} {X₀ : Type u_1} {X₁ : Type u_2}
  {V : Type u_3} [NormedAddCommGroup X₀] [NormedSpace ℂ X₀] [NormedAddCommGroup X₁]
  [NormedSpace ℂ X₁] [AddCommGroup V] [_root_.Module ℂ V] [TopologicalSpace V] [ContinuousAdd V]
  [T1Space V] (C : TauCeti.CompatibleCouple ℂ X₀ X₁ V) (θ : ℝ) : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CompatibleCouple.ComplexMethodSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.html#TauCeti.CompatibleCouple.ComplexMethodSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.CompatibleCouple.ComplexMethodSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.html#TauCeti.CompatibleCouple.ComplexMethodSpace)
- [Source of `TauCeti.CompatibleCouple.ComplexMethodSpace` in TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.lean#L407)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
