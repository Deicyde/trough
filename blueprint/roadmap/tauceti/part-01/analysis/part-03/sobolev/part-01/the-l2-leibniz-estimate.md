---
declaration: theorem
origin: cited
lean: TauCeti.W1p.norm_gradient_contDiffSMul_sq_le
statement: formalized
proof: formalized
---

# The `L²` Leibniz estimate

At exponent two, the gradient `ψ ∇u + u ∇ψ` of `ψ u` satisfies

`‖∇(ψ u)‖₂² ≤ 2 ∫_Ω ψ² ‖∇u‖² + 2 ∫_Ω ‖∇ψ‖² u²`.

Unlike `TauCeti.W1p.norm_contDiffSMul_le`, the two terms keep their weights `ψ²` and `‖∇ψ‖²`,
which is the form in which energy estimates such as Caccioppoli's inequality are applied to a
localized function.

```lean
TauCeti.W1p.norm_gradient_contDiffSMul_sq_le.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {psi : E → ℝ} {M : ℝ} (hpsi : ContDiff ℝ (↑⊤) psi) (hM : 0 ≤ M) (hpsiM : ∀ x ∈ Omega, |psi x| ≤ M)
  (hgradM : ∀ x ∈ Omega, ‖gradient psi x‖ ≤ M) (u : ↥(TauCeti.W1p mu Omega 2)) :
  ‖TauCeti.W1p.gradient (TauCeti.W1p.contDiffSMul psi hpsi hM hpsiM hgradM u)‖ ^ 2 ≤
    2 * ∫ (x : E) in ↑Omega, psi x ^ 2 * ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 ∂mu +
      2 * ∫ (x : E) in ↑Omega, ‖gradient psi x‖ ^ 2 * ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.norm_gradient_contDiffSMul_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/Multiplication.html#TauCeti.W1p.norm_gradient_contDiffSMul_sq_le).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.norm_gradient_contDiffSMul_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/Multiplication.html#TauCeti.W1p.norm_gradient_contDiffSMul_sq_le)
- [Source of `TauCeti.W1p.norm_gradient_contDiffSMul_sq_le` in TauCeti/Analysis/Sobolev/W1p/Multiplication.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/W1p/Multiplication.lean#L261)
