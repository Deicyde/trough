---
declaration: module
origin: cited
lean: ClassicalMechanics.LagrangianSystem, ClassicalMechanics.LagrangianSystem.ofNormedSpace, ClassicalMechanics.LagrangianSystem.coord, ClassicalMechanics.LagrangianSystem.contDiff_coord, ClassicalMechanics.LagrangianSystem.coord_ofNormedSpace, ClassicalMechanics.LagrangianSystem.action, ClassicalMechanics.LagrangianSystem.action_eq_zero_of_vsub_nonpos, ClassicalMechanics.LagrangianSystem.action_eq_integral_coord
statement: formalized
proof: formalized
---

# Lagrangian systems

The module `Physlib.ClassicalMechanics.Lagrangian.Basic`, [Physlib/ClassicalMechanics/Lagrangian/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean): 9 declarations (1 instance with no name), 7 with a docstring.

> Lagrangians on `TM` and their action.

## i. Overview

> The motions of a Lagrangian system are the critical points of its action, see
> `LagrangianSystem.IsCriticalPoint`.

## ii. Key results

> - `LagrangianSystem` : smooth time-dependent Lagrangians on `TM`.
> - `LagrangianSystem.coord` : `L` in a time coordinate.
> - `LagrangianSystem.action` : the action of a curve.
> - `LagrangianSystem.action_eq_integral_coord` : the action of a curve in a normed space in
>   coordinates.

## iv. References

> * V. I. Arnold, Mathematical Methods of Classical Mechanics. [ref: arnold\_mechanics]
> * I. Terek, Introductory Variational Calculus on Manifolds. [ref: terek\_variational\_manifolds]

## A. Lagrangian systems

**`ClassicalMechanics.LagrangianSystem`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L60).

> A smooth time-dependent Lagrangian on `TM`, depending on first-order derivatives only.

```lean
structure LagrangianSystem where
  /-- `L(t, q, q̇)`. -/
  toFun : Time × TangentBundle I M → ℝ
  /-- `L` is smooth. -/
  contMDiff : ContMDiff (𝓘(ℝ, ℝ).prod I.tangent) 𝓘(ℝ, ℝ) ∞ toFun
```

### A.1. Basic instances

**An instance with no name**, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L74).

```lean
instance : FunLike (LagrangianSystem I M) (Time × TangentBundle I M) ℝ
```

### A.2. The coordinate form

**`ClassicalMechanics.LagrangianSystem.ofNormedSpace`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L90).

> The Lagrangian system on a normed space `E` given by a smooth `L(t, q, q̇)`.

```lean
def ofNormedSpace (L : Time × E × E → ℝ)
    (hL : ContMDiff (𝓘(ℝ, ℝ).prod 𝓘(ℝ, E × E)) 𝓘(ℝ, ℝ) ∞ L) :
    LagrangianSystem 𝓘(ℝ, E) ⟨E⟩
```

**`ClassicalMechanics.LagrangianSystem.coord`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L97).

> `L` in the time coordinate `τ ↦ τ +ᵥ t₀`.

```lean
noncomputable def coord (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) (t₀ : Time) (p : ℝ × E × E) : ℝ
```

**`ClassicalMechanics.LagrangianSystem.contDiff_coord`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L101).

> `S.coord t₀` is smooth.

```lean
lemma contDiff_coord (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) (t₀ : Time) :
    ContDiff ℝ ∞ (S.coord t₀)
```

**`ClassicalMechanics.LagrangianSystem.coord_ofNormedSpace`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L112).

```lean
lemma coord_ofNormedSpace (L : Time × E × E → ℝ)
    (hL : ContMDiff (𝓘(ℝ, ℝ).prod 𝓘(ℝ, E × E)) 𝓘(ℝ, ℝ) ∞ L) (t₀ : Time) (p : ℝ × E × E) :
    (ofNormedSpace L hL).coord t₀ p = L (p.1 +ᵥ t₀, p.2)
```

### A.3. The action

**`ClassicalMechanics.LagrangianSystem.action`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L125).

> The action `∫ L(t, γ, γ̇) dt` over `[t₀, t₁]`.

```lean
noncomputable def action (γ : Time → M) (t₀ t₁ : Time) : ℝ
```

**`ClassicalMechanics.LagrangianSystem.action_eq_zero_of_vsub_nonpos`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L129).

> The action over an empty or one-point interval vanishes.

```lean
lemma action_eq_zero_of_vsub_nonpos (h : t₁ -ᵥ t₀ ≤ 0) : S.action γ t₀ t₁ = 0
```

**`ClassicalMechanics.LagrangianSystem.action_eq_integral_coord`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean#L134).

> The action is the integral over `[0, t₁ -ᵥ t₀]` of `S.coord t₀ (s, q s, q' s)`, where
> `q τ = γ (τ +ᵥ t₀)` and `q' = deriv q`.

```lean
lemma action_eq_integral_coord (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) (γ : Time → E) (t₀ t₁ : Time) :
    S.action γ t₀ t₁ = ∫ s in Set.Icc 0 (t₁ -ᵥ t₀),
      S.coord t₀ (s, γ (s +ᵥ t₀), deriv (fun τ : ℝ ↦ γ (τ +ᵥ t₀)) s)
```

## Depends on

- [Configuration spaces](../configurationspace/basic.md)
- [Time](../../spaceandtime/time/basic.md)

## Proof depends on

- [Curves in normed spaces over `Time`](../../spaceandtime/time/manifoldcurves.md)

## Sources

- [Physlib/ClassicalMechanics/Lagrangian/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/Basic.lean)
