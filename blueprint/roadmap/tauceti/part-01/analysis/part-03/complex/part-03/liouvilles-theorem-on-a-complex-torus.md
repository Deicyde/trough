---
declaration: theorem
origin: cited
lean: Differentiable.apply_eq_apply_of_norm_add_eq, TauCeti.OrderLE.isConst, Differentiable.eq_zero_of_eq_neg_inv_sq_smul
statement: formalized
proof: formalized
---

# Liouville's theorem on a complex torus

An entire map whose norm is invariant under
translation by a full lattice `L` is constant: its norm is the norm of a continuous function on the
compact torus `V ⧸ L`, so it is bounded.

```lean
Differentiable.apply_eq_apply_of_norm_add_eq.{u_1, u_2} {V : Type u_1} {F : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [FiniteDimensional ℂ V] [NormedAddCommGroup F]
  [NormedSpace ℂ F] {f : V → F} (hf : Differentiable ℂ f) (L : Submodule ℤ V) [DiscreteTopology ↥L]
  [IsZLattice ℝ L] (h : ∀ (z ω : V), ω ∈ L → ‖f (z + ω)‖ = ‖f z‖) (z w : V) : f z = f w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Differentiable.apply_eq_apply_of_norm_add_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/QuasiPeriodic.html#Differentiable.apply_eq_apply_of_norm_add_eq).

## Other forms

**Liouville's theorem for functions of negative order.** Formalized in Tau Ceti as [`TauCeti.OrderLE.isConst`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder.html#TauCeti.OrderLE.isConst).

```lean
TauCeti.OrderLE.isConst {f : ℂ → ℂ} {A : ℝ} (h : TauCeti.OrderLE f A) (hf : Differentiable ℂ f)
  (hA : A < 0) : Function.IsConst f
```

**Liouville's theorem for the transformation law of a one-form under `t ↦ 1 / t`.** Formalized in Tau Ceti as [`Differentiable.eq_zero_of_eq_neg_inv_sq_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Liouville.html#Differentiable.eq_zero_of_eq_neg_inv_sq_smul).

```lean
Differentiable.eq_zero_of_eq_neg_inv_sq_smul.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℂ F] {f g : ℂ → F} (hf : Differentiable ℂ f) (hg : ContinuousAt g 0)
  (h : ∀ (s : ℂ), s ≠ 0 → f s = -(s ^ 2)⁻¹ • g s⁻¹) (t : ℂ) : f t = 0
```

## Sources

- [Tau Ceti documentation: `Differentiable.apply_eq_apply_of_norm_add_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/QuasiPeriodic.html#Differentiable.apply_eq_apply_of_norm_add_eq)
- [Source of `Differentiable.apply_eq_apply_of_norm_add_eq` in TauCeti/Analysis/Complex/QuasiPeriodic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/QuasiPeriodic.lean#L103)
