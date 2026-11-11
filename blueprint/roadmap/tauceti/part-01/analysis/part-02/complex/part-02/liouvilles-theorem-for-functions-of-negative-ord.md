---
declaration: theorem
origin: cited
lean: TauCeti.OrderLE.isConst, Differentiable.eq_zero_of_eq_neg_inv_sq_smul
statement: formalized
proof: formalized
---

# Liouville's theorem for functions of negative order

An entire function of order at most
`A < 0` is constant.

```lean
TauCeti.OrderLE.isConst {f : ℂ → ℂ} {A : ℝ} (h : TauCeti.OrderLE f A) (hf : Differentiable ℂ f)
  (hA : A < 0) : Function.IsConst f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OrderLE.isConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder.html#TauCeti.OrderLE.isConst).

## Other forms

**Liouville's theorem for the transformation law of a one-form under `t ↦ 1 / t`.** Formalized in Tau Ceti as [`Differentiable.eq_zero_of_eq_neg_inv_sq_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Liouville.html#Differentiable.eq_zero_of_eq_neg_inv_sq_smul).

```lean
Differentiable.eq_zero_of_eq_neg_inv_sq_smul.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℂ F] {f g : ℂ → F} (hf : Differentiable ℂ f) (hg : ContinuousAt g 0)
  (h : ∀ (s : ℂ), s ≠ 0 → f s = -(s ^ 2)⁻¹ • g s⁻¹) (t : ℂ) : f t = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.OrderLE.isConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder.html#TauCeti.OrderLE.isConst)
- [Source of `TauCeti.OrderLE.isConst` in TauCeti/Analysis/Complex/GrowthOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/GrowthOrder.lean#L160)
