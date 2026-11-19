---
declaration: theorem
origin: cited
lean: TauCeti.hasApproximationProperty_iff_trace_eq_zero
statement: formalized
proof: formalized
---

# Grothendieck's trace criterion for the approximation property

A normed space `E` over `ℝ`
or `ℂ` has the approximation property iff the tensor trace `E* ⊗̂π E → 𝕜` vanishes on the kernel of
the contraction `E* ⊗̂π E → E* ⊗̂ε E`.

```lean
TauCeti.hasApproximationProperty_iff_trace_eq_zero.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] :
  TauCeti.HasApproximationProperty 𝕜 E ↔
    ∀ (u : TauCeti.CompletedProjectiveTensor 𝕜 (StrongDual 𝕜 E) E),
      (TauCeti.CompletedProjectiveTensor.toCompletedInjectiveTensor 𝕜 (StrongDual 𝕜 E) E) u = 0 →
        (TauCeti.CompletedProjectiveTensor.trace 𝕜 E) u = 0
```

## Depends on

- [TauCeti.CompletedInjectiveTensor](../../../part-01/banach-space-theory/part-01/tauceti-completedinjectivetensor.md)
- [TauCeti.CompletedProjectiveTensor](../../../part-01/banach-space-theory/part-01/tauceti-completedprojectivetensor.md)

## Proof depends on

- [Grothendieck's compactness lemma](../../convex/grothendiecks-compactness-lemma.md)
- [Norm double-annihilator theorem](../part-02/norm-double-annihilator-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasApproximationProperty_iff_trace_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.hasApproximationProperty_iff_trace_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.hasApproximationProperty_iff_trace_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.hasApproximationProperty_iff_trace_eq_zero)
- [Source of `TauCeti.hasApproximationProperty_iff_trace_eq_zero` in TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean#L307)
