---
declaration: def
origin: cited
lean: TauCeti.cauchyTransformCkCLM
statement: formalized
---

# The Cauchy transform as a bounded operator `C^{k,α}(D_r) → C^{k+1,α}(D_R)`

For
`0 < α < 1`, it sends `C^{k,α}` data supported in `closedBall c r` to the derivative fields
`x ↦ D^i (T f) x` of orders `i ≤ k + 1` on `closedBall c R`, each with the supremum norm, together
with the `α`-Hölder field `D^{k+1} (T f)` on `closedBall c R`. It is real linear and bounded, so
continuous source families give continuous families of derivative fields in these norms.

For `k = 0` it does not replace `TauCeti.cauchyTransformCLM`: that operator acts on the
`C^{0,α}` space `supportedHolderSubmodule`, while the source here is
`supportedCkHolderSubmodule 0`, a different carrier, and its targets are the value and
derivative fields as `0`- and `1`-multilinear maps rather than as values and linear maps.

```lean
TauCeti.cauchyTransformCkCLM.{u_1} {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℂ F]
  [NormedSpace ℝ F] [IsScalarTower ℝ ℂ F] [FiniteDimensional ℂ F] {α : NNReal} {c : ℂ} {r R : ℝ}
  (k : ℕ) (hα : 0 < α) (hα1 : α < 1) (hr : 0 ≤ r) (hR : 0 ≤ R) :
  ↥(TauCeti.supportedCkHolderSubmodule k α (Metric.closedBall c r)) →L[ℝ]
    ((i : Fin (k + 2)) → BoundedContinuousFunction (↑(Metric.closedBall c R)) (ℂ [×↑i]→L[ℝ] F)) ×
      TauCeti.HolderSpace α (↑(Metric.closedBall c R)) (ℂ [×k + 1]→L[ℝ] F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula with a cutoff](../../part-03/complex/part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)
- [The global Schauder estimate](../../part-04/pde/part-01/the-global-schauder-estimate.md)
- [Radial fundamental theorem of calculus](../../../measure-theory/constructions/radial-fundamental-theorem-of-calculus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cauchyTransformCkCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Holder/Higher.html#TauCeti.cauchyTransformCkCLM).

## Sources

- [Tau Ceti documentation: `TauCeti.cauchyTransformCkCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Holder/Higher.html#TauCeti.cauchyTransformCkCLM)
- [Source of `TauCeti.cauchyTransformCkCLM` in TauCeti/Analysis/Complex/Pompeiu/Holder/Higher.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Pompeiu/Holder/Higher.lean#L417)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
