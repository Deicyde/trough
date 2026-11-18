---
declaration: module
origin: cited
lean: ClassicalMechanics.LagrangianSystem.IsCriticalPoint, ClassicalMechanics.LagrangianSystem.isCriticalPoint_of_vsub_nonpos, ClassicalMechanics.LagrangianSystem.isCriticalPoint_of_eulerLagrange_eq_zero, ClassicalMechanics.LagrangianSystem.eulerLagrange_eq_zero_of_isCriticalPoint, ClassicalMechanics.LagrangianSystem.isCriticalPoint_iff_eulerLagrange
statement: formalized
proof: formalized
---

# Critical points and Euler-Lagrange equations

The module `Physlib.ClassicalMechanics.Lagrangian.CriticalPoint`, [Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean): 5 declarations, 5 with a docstring.

> Critical points of the action are the solutions of the Euler-Lagrange equations.

## i. Overview

> `γ` is a critical point over `[t₀, t₁]` if it is smooth and every variation has zero first
> variation of the action, which is Hamilton's principle `δS = 0` for variations fixing the
> endpoints. For `t₀ ≠ t₁`, `γ` is a critical point over `[t₀, t₁]` iff the Euler-Lagrange equations
> `eulerLagrange S t₀ q = 0` hold on `[0, t₁ -ᵥ t₀]`, where `q σ = γ (σ +ᵥ t₀)`. This section treats a
> normed space `E` as the configuration space.

## ii. Key results

> - `LagrangianSystem.IsCriticalPoint`: critical points of the action
> - `LagrangianSystem.isCriticalPoint_of_vsub_nonpos`: every smooth curve is critical over an empty
>   or one-point interval
> - `LagrangianSystem.isCriticalPoint_of_eulerLagrange_eq_zero`: equations imply criticality
> - `LagrangianSystem.eulerLagrange_eq_zero_of_isCriticalPoint`: criticality implies equations
> - `LagrangianSystem.isCriticalPoint_iff_eulerLagrange`: the two are equivalent

## iv. References

> * V. I. Arnold, Mathematical Methods of Classical Mechanics. [ref: arnold\_mechanics]
> * I. Terek, Introductory Variational Calculus on Manifolds. [ref: terek\_variational\_manifolds]
> * L. D. Landau and E. M. Lifshitz, Mechanics. [ref: landau\_mechanics]

## A. Critical points

### A.1. The definition

**`ClassicalMechanics.LagrangianSystem.IsCriticalPoint`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean#L70).

> `γ` is smooth and every variation of `γ` fixing the endpoints has zero first variation of the
> action, i.e. `d/ds S[γ_s]` vanishes at `s = 0` (Hamilton's principle).

```lean
def IsCriticalPoint (γ : Time → M) (t₀ t₁ : Time) : Prop
```

**`ClassicalMechanics.LagrangianSystem.isCriticalPoint_of_vsub_nonpos`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean#L75).

> Every smooth curve is critical over an empty or one-point interval.

```lean
lemma isCriticalPoint_of_vsub_nonpos (hγ : ContMDiff 𝓘(ℝ, ℝ) I ∞ γ) (h : t₁ -ᵥ t₀ ≤ 0) :
    S.IsCriticalPoint γ t₀ t₁
```

### A.2. Euler-Lagrange equations

**`ClassicalMechanics.LagrangianSystem.isCriticalPoint_of_eulerLagrange_eq_zero`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean#L89).

> If `q σ = γ (σ +ᵥ t₀)` is smooth and `eulerLagrange S t₀ q = 0` on `(0, t₁ -ᵥ t₀)`, then `γ`
> is a critical point.

```lean
lemma isCriticalPoint_of_eulerLagrange_eq_zero
    (hγ : ContDiff ℝ ∞ (fun σ : ℝ ↦ γ (σ +ᵥ t₀))) (hEq : ∀ τ ∈ Ioo 0 (t₁ -ᵥ t₀),
      eulerLagrange S t₀ (fun σ ↦ γ (σ +ᵥ t₀)) τ = 0) : S.IsCriticalPoint γ t₀ t₁
```

**`ClassicalMechanics.LagrangianSystem.eulerLagrange_eq_zero_of_isCriticalPoint`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean#L111).

> A critical point `γ` has `eulerLagrange S t₀ q = 0` on `[0, t₁ -ᵥ t₀]`, `q σ = γ (σ +ᵥ t₀)`.

```lean
lemma eulerLagrange_eq_zero_of_isCriticalPoint (ht : t₁ -ᵥ t₀ ≠ 0)
    (hc : S.IsCriticalPoint γ t₀ t₁) : ∀ τ ∈ Icc 0 (t₁ -ᵥ t₀),
      eulerLagrange S t₀ (fun σ : ℝ ↦ γ (σ +ᵥ t₀)) τ = 0
```

**`ClassicalMechanics.LagrangianSystem.isCriticalPoint_iff_eulerLagrange`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean#L134).

> For `t₁ -ᵥ t₀ ≠ 0`, `γ` is a critical point iff `q σ = γ (σ +ᵥ t₀)` is smooth and
> `eulerLagrange S t₀ q = 0` on `[0, t₁ -ᵥ t₀]`.

```lean
lemma isCriticalPoint_iff_eulerLagrange (ht : t₁ -ᵥ t₀ ≠ 0) :
    S.IsCriticalPoint γ t₀ t₁ ↔ ContDiff ℝ ∞ (fun σ : ℝ ↦ γ (σ +ᵥ t₀)) ∧
      ∀ τ ∈ Icc 0 (t₁ -ᵥ t₀), eulerLagrange S t₀ (fun σ : ℝ ↦ γ (σ +ᵥ t₀)) τ = 0
```

## Depends on

- [Variations of curves](../configurationspace/variation.md)
- [A. Euler–Lagrange equations](../eulerlagrange.md)

## Proof depends on

- [First variation of the action](firstvariation.md)
- [Fundamental lemma on an interval](../../mathematics/variationalcalculus/interval.md)

## Sources

- [Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/CriticalPoint.lean)
