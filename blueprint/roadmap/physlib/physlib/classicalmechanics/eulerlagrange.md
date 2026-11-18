---
declaration: module
origin: cited
lean: ClassicalMechanics.euler_lagrange_varGradient, ClassicalMechanics.eulerLagrangeOp, ClassicalMechanics.eulerLagrangeOp_eq, ClassicalMechanics.eulerLagrangeOp_zero, ClassicalMechanics.canonicalMomentum, ClassicalMechanics.eulerLagrange, ClassicalMechanics.contDiff_eulerLagrange, ClassicalMechanics.eulerLagrange_congr
statement: formalized
proof: formalized
---

# A. Euler–Lagrange equations

The module `Physlib.ClassicalMechanics.EulerLagrange`, [Physlib/ClassicalMechanics/EulerLagrange.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean): 9 declarations, 7 with a docstring, 1 listed as significant.

> The Euler–Lagrange equations characterize stationary trajectories of an action functional. For a
> Lagrangian `L t q v`, they compare the gradient with respect to position to the time derivative of
> the gradient with respect to velocity.

## A.1. Mathematical setting

> Trajectories take values in a complete real inner-product space `X`. The Lagrangian has type
> `Time → X → X → ℝ`, and the corresponding action is the time integral of
> `L t (q t) (∂ₜ q t)`.

## A.2. Main definitions and results

> - `eulerLagrangeOp` defines the Euler–Lagrange operator
>   `∂L/∂q - ∂ₜ (∂L/∂v)` along a trajectory.
> - `eulerLagrangeOp_eq` exposes its pointwise formula.
> - `eulerLagrangeOp_zero` evaluates the operator for the zero Lagrangian.
> - `euler_lagrange_varGradient` proves that the variational gradient of the action equals the
>   Euler–Lagrange operator for smooth trajectories and Lagrangians.
> - `canonicalMomentum` and `eulerLagrange` give the covector form `∂L/∂q - dₜ(∂L/∂q̇)` for a
>   Lagrangian system `S` on a normed space `E` and time origin `t₀`, with `contDiff_eulerLagrange`,
>   `eulerLagrange_congr` and `eulerLagrange_congr_lagrangian`.

## A.3. Current scope

> The result is formulated for smooth data and Hilbert-space-valued trajectories. Applications to
> specific mechanical systems are developed in their corresponding modules, where vanishing of the
> operator becomes the system's equation of motion.

**`ClassicalMechanics.eulerLagrangeOp`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L56).

> The Euler Lagrange operator, for a trajectory `q : Time → X`,
> and a lagrangian `Time → X → X → ℝ`, the Euler-Lagrange operator is
>   `∂L/∂q - dₜ(∂L/∂(dₜ q))`.

```lean
noncomputable def eulerLagrangeOp (L : Time → X → X → ℝ) (q : Time → X) : Time → X
```

**`ClassicalMechanics.eulerLagrangeOp_eq`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L59).

```lean
lemma eulerLagrangeOp_eq (L : Time → X → X → ℝ) (q : Time → X) :
    eulerLagrangeOp L q = fun t => gradient (L t · (∂ₜ q t)) (q t)
    - ∂ₜ (fun t' => gradient (L t' (q t') ·) (∂ₜ q t')) t
```

**`ClassicalMechanics.eulerLagrangeOp_zero`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L63).

```lean
lemma eulerLagrangeOp_zero (q : Time → X) :
    eulerLagrangeOp (fun _ _ _ => 0) q = fun _ => 0
```

**`ClassicalMechanics.euler_lagrange_varGradient`**, a theorem, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L69). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The variational derivative of the action `∫ t, L t (q' t) (deriv q' t)` for a Lagrangian `L`
> is equal to the `eulerLagrangeOp`.

```lean
theorem euler_lagrange_varGradient
    (L : Time → X → X → ℝ) (q : Time → X)
    (hq : ContDiff ℝ ∞ q) (hL : ContDiff ℝ ∞ ↿L) :
    (δ (q':=q), ∫ t, L t (q' t) (fderiv ℝ q' t 1)) = eulerLagrangeOp L q
```

**`ClassicalMechanics.canonicalMomentum`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L112).

> The canonical momentum `∂L/∂q̇` of a curve `q`.

```lean
noncomputable def canonicalMomentum (q : ℝ → E) (τ : ℝ) : E →L[ℝ] ℝ
```

**`ClassicalMechanics.eulerLagrange`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L117).

> The Euler-Lagrange covector `∂L/∂q - dₜ(∂L/∂q̇)` of a curve `q`; the covector counterpart of
> `eulerLagrangeOp`.

```lean
noncomputable def eulerLagrange (q : ℝ → E) (τ : ℝ) : E →L[ℝ] ℝ
```

**`ClassicalMechanics.contDiff_eulerLagrange`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L123).

> The Euler-Lagrange covector of a smooth curve is smooth.

```lean
lemma contDiff_eulerLagrange {q : ℝ → E} (hq : ContDiff ℝ ∞ q) :
    ContDiff ℝ ∞ (eulerLagrange S t₀ q)
```

**`ClassicalMechanics.eulerLagrange_congr`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L132).

> The Euler-Lagrange covector at `τ` depends only on the germ of the curve at `τ`.

```lean
lemma eulerLagrange_congr {q g : ℝ → E} {τ : ℝ} (h : q =ᶠ[𝓝 τ] g) :
    eulerLagrange S t₀ q τ = eulerLagrange S t₀ g τ
```

**`ClassicalMechanics.eulerLagrange_congr_lagrangian`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean#L142).

> The Euler-Lagrange covector only depends on the Lagrangian near the curve.

```lean
lemma eulerLagrange_congr_lagrangian {S' : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩} {q : ℝ → E} {τ : ℝ}
    {N : Set E} (hN : IsOpen N) (hq : ∀ᶠ σ in 𝓝 τ, q σ ∈ N)
    (h : ∀ p : ℝ × E × E, p.2.1 ∈ N → S.coord t₀ p = S'.coord t₀ p) :
    eulerLagrange S t₀ q τ = eulerLagrange S' t₀ q τ
```

## Depends on

- [Lagrangian systems](lagrangian/basic.md)
- [Variational gradient](../mathematics/variationalcalculus/hasvargradient.md)
- [Time Derivatives](../spaceandtime/time/derivatives.md)

## Sources

- [Physlib/ClassicalMechanics/EulerLagrange.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/EulerLagrange.lean)
