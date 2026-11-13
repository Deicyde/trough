---
declaration: module
origin: cited
lean: ClassicalMechanics.Variation, ClassicalMechanics.Variation.nonempty, ClassicalMechanics.Variation.contDiff_comp_vadd, ClassicalMechanics.Variation.exists_bump
statement: formalized
proof: formalized
---

# Variations of curves

The module `Physlib.ClassicalMechanics.ConfigurationSpace.Variation`, [Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean): 4 declarations, 4 with a docstring.

> Smooth variations of a curve in a configuration space fixing the endpoints.

## i. Overview

> Variations probe the action of a Lagrangian system around a curve.

## ii. Key results

> - `Variation` : smooth variations fixing the endpoints.
> - `Variation.contDiff_comp_vadd` : a variation of a curve in a normed space is smooth in
>   coordinates.
> - `Variation.exists_bump` : a bump function gives a variation of a curve in a normed space.

## iv. References

> * I. Terek, Introductory Variational Calculus on Manifolds. [ref: terek\_variational\_manifolds]

## A. Variations

**`ClassicalMechanics.Variation`**, a structure, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean#L55).

> A smooth variation of `γ` on `[t₀, t₁]` fixing `γ t₀` and `γ t₁`.

```lean
structure Variation (γ : Time → M) (t₀ t₁ : Time) where
  /-- The smooth family of curves. -/
  toFun : C^∞⟮𝓘(ℝ, ℝ).prod 𝓘(ℝ, ℝ), ℝ × Time; I, M⟯
  /-- Starts at `γ`. -/
  apply_zero : ∀ s ∈ Set.Icc 0 (t₁ -ᵥ t₀), toFun (0, s +ᵥ t₀) = γ (s +ᵥ t₀)
  /-- Fixes `γ t₀`. -/
  apply_left : ∀ s, toFun (s, t₀) = γ t₀
  /-- Fixes `γ t₁`. -/
  apply_right : ∀ s, toFun (s, t₁) = γ t₁
```

**`ClassicalMechanics.Variation.nonempty`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean#L69).

> A smooth curve admits the constant variation.

```lean
lemma nonempty {γ : Time → M} {t₀ t₁ : Time} (hγ : ContMDiff 𝓘(ℝ, ℝ) I ∞ γ) :
    Nonempty (Variation I γ t₀ t₁)
```

## B. Variations in a normed space

**`ClassicalMechanics.Variation.contDiff_comp_vadd`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean#L78).

> `(s, τ) ↦ h (s, τ +ᵥ t₀)` is smooth.

```lean
lemma contDiff_comp_vadd {γ : Time → E} {t₀ t₁ : Time}
    (h : Variation (M := ⟨E⟩) 𝓘(ℝ, E) γ t₀ t₁) :
    ContDiff ℝ ∞ (fun p : ℝ × ℝ ↦ h.toFun (p.1, p.2 +ᵥ t₀))
```

**`ClassicalMechanics.Variation.exists_bump`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean#L90).

> For a smooth curve `γ`, smooth `ψ` supported in `(0, t₁ -ᵥ t₀)` and `w : E`, there exists a
> variation `h` of `γ` with `h (s, τ +ᵥ t₀) = γ (τ +ᵥ t₀) + s • ψ τ • w`.

```lean
lemma exists_bump {γ : Time → E} {t₀ t₁ : Time} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) ∞ γ)
    {ψ : ℝ → ℝ} (hψ : ContDiff ℝ ∞ ψ) (hs : tsupport ψ ⊆ Ioo 0 (t₁ -ᵥ t₀)) (w : E) :
    ∃ h : Variation (M := ⟨E⟩) 𝓘(ℝ, E) γ t₀ t₁,
      ∀ s τ, h.toFun (s, τ +ᵥ t₀) = γ (τ +ᵥ t₀) + s • (ψ τ • w)
```

## Depends on

- [Configuration spaces](basic.md)
- [Time](../../spaceandtime/time/basic.md)

## Proof depends on

- [Curves in normed spaces over `Time`](../../spaceandtime/time/manifoldcurves.md)

## Sources

- [Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/ConfigurationSpace/Variation.lean)
