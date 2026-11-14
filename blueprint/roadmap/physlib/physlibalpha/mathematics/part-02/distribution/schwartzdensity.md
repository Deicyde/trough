---
declaration: module
origin: cited
lean: SchwartzMap.exists_cutoff, SchwartzMap.exists_bound_dilate, SchwartzMap.iteratedFDeriv_dilate_eq_zero, SchwartzMap.exists_bound_cutoff_sub, SchwartzMap.ofTestFunction, SchwartzMap.ofTestFunction_injective, SchwartzMap.ofTestFunction_apply, SchwartzMap.cutoffTest
statement: formalized
proof: formalized
---

# Test functions are dense in the Schwartz space

The module `PhyslibAlpha.Mathematics.Distribution.SchwartzDensity`, [PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean): 9 declarations, 7 with a docstring.

> A Schwartz function is the limit of its cutoffs by dilated bump functions.

## i. Overview

> Let `b` be a smooth compactly supported function that equals one on the unit ball. The cutoff
> `b (x / R) * f x` of a Schwartz function `f` is a test function. The derivatives of the cutoff
> factor are bounded uniformly in `R ≥ 1` and vanish on the ball of radius `R`. The Schwartz
> seminorms of `f - b (x / R) * f` are therefore bounded by `R⁻¹` times a seminorm of `f`.

## ii. Key results

> - `exists_cutoff` : a smooth compactly supported function that equals one on the unit ball.
> - `exists_bound_cutoff_sub` : the cutoff approximation estimate.
> - `denseRange_ofTestFunction` : test functions are dense in the Schwartz space.

## iv. References

> None.

## A. The cutoff

> - `exists_cutoff` : a smooth compactly supported function that equals one on the unit ball.
> - `exists_bound_cutoff_sub` : the cutoff approximation estimate.

## B. Density

> - `ofTestFunction` : a real test function is a Schwartz function.
> - `cutoffTest` : the cutoff of a Schwartz function as a test function.
> - `denseRange_ofTestFunction` : test functions are dense in the Schwartz space.

**`SchwartzMap.exists_cutoff`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L65).

> A smooth compactly supported function that equals one on the unit ball.

```lean
lemma exists_cutoff : ∃ b : V → ℝ, ContDiff ℝ ∞ b ∧ HasCompactSupport b ∧
    ∀ x : V, ‖x‖ ≤ 1 → b x = 1
```

**`SchwartzMap.exists_bound_dilate`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L73).

> The derivatives of the dilated cutoff minus one are bounded uniformly in the dilation.

```lean
lemma exists_bound_dilate {b : V → ℝ} (hb : ContDiff ℝ ∞ b) (hs : HasCompactSupport b) (j : ℕ) :
    ∃ B : ℝ, 0 ≤ B ∧ ∀ R : ℝ, 1 ≤ R → ∀ x : V,
      ‖iteratedFDeriv ℝ j (fun y => b (R⁻¹ • y) - 1) x‖ ≤ B
```

**`SchwartzMap.iteratedFDeriv_dilate_eq_zero`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L131).

> The dilated cutoff minus one vanishes with all its derivatives inside the ball of radius `R`.

```lean
lemma iteratedFDeriv_dilate_eq_zero {b : V → ℝ} (hone : ∀ x : V, ‖x‖ ≤ 1 → b x = 1) {R : ℝ}
    (hR : 0 < R) (j : ℕ) {x : V} (hx : ‖x‖ < R) :
    iteratedFDeriv ℝ j (fun y => b (R⁻¹ • y) - 1) x = 0
```

**`SchwartzMap.exists_bound_cutoff_sub`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L150).

> **The cutoff approximation estimate.** The weighted derivatives of `(b (R⁻¹ x) - 1) f x` are
> bounded by a constant times `R⁻¹`.

```lean
lemma exists_bound_cutoff_sub {b : V → ℝ} (hb : ContDiff ℝ ∞ b) (hs : HasCompactSupport b)
    (hone : ∀ x : V, ‖x‖ ≤ 1 → b x = 1) (f : 𝓢(V, ℝ)) (k n : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ R : ℝ, 1 ≤ R → ∀ x : V,
      ‖x‖ ^ k * ‖iteratedFDeriv ℝ n (fun y => (b (R⁻¹ • y) - 1) * f y) x‖ ≤ C / R
```

**`SchwartzMap.ofTestFunction`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L211).

> A real test function is a Schwartz function.

```lean
def ofTestFunction : 𝓓((⊤ : Opens V), ℝ) →ₗ[ℝ] 𝓢(V, ℝ)
```

**`SchwartzMap.ofTestFunction_injective`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L217).

```lean
lemma ofTestFunction_injective : Function.Injective (ofTestFunction (V := V))
```

**`SchwartzMap.ofTestFunction_apply`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L222).

```lean
lemma ofTestFunction_apply (φ : 𝓓((⊤ : Opens V), ℝ)) (x : V) :
    ofTestFunction φ x = φ x
```

**`SchwartzMap.cutoffTest`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L226).

> The cutoff of a Schwartz function by the dilated bump function, as a test function.

```lean
def cutoffTest {b : V → ℝ} (hb : ContDiff ℝ ∞ b) (hs : HasCompactSupport b) (f : 𝓢(V, ℝ))
    {R : ℝ} (hR : 0 < R) : 𝓓((⊤ : Opens V), ℝ)
```

**`SchwartzMap.denseRange_ofTestFunction`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean#L237).

> **Test functions are dense in the Schwartz space.**

```lean
lemma denseRange_ofTestFunction : DenseRange (ofTestFunction (V := V))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzDensity.lean)
