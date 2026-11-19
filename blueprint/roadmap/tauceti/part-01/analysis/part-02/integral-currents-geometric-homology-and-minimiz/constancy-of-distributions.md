---
declaration: theorem
origin: cited
lean: Distribution.existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero
statement: formalized
proof: formalized
---

# Constancy of distributions

A Banach-valued distribution on a connected nonempty open
subset of a finite-dimensional real normed space whose directional derivatives all vanish is
integration against a unique constant, for any additive Haar measure `μ`.

```lean
Distribution.existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {Ω : TopologicalSpace.Opens E} (T : Distribution Ω F ⊤) (μ : MeasureTheory.Measure E)
  [μ.IsAddHaarMeasure] (hΩ : IsConnected ↑Ω) (hT : ∀ (v : E), LineDeriv.lineDerivOp v T = 0) :
  ∃! c, T = Distribution.ofFun Ω (fun x => c) μ ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Uniform first-order Taylor estimate in a parameter](../../part-03/calculus/part-02/uniform-first-order-taylor-estimate-in-a-paramet.md)

## Lean

Formalized in Tau Ceti as [`Distribution.existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Basic.html#Distribution.existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero).

## Sources

- [Tau Ceti documentation: `Distribution.existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Basic.html#Distribution.existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero)
- [Source of `Distribution.existsUnique_eq_ofFun_const_of_forall_lineDerivOp_eq_zero` in TauCeti/Analysis/Distribution/Constancy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/Constancy/Basic.lean#L141)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
