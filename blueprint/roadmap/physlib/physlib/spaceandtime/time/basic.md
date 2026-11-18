---
declaration: module
origin: cited
lean: Time, Time.val_injective, Time.vadd_val, Time.vsub_eq_val, Time.chartAt_apply, Time.chartAt_symm_apply, Time.extChartAt_apply, Time.contMDiff_vadd
statement: formalized
proof: formalized
---

# Time

The module `Physlib.SpaceAndTime.Time.Basic`, [Physlib/SpaceAndTime/Time/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean): 17 declarations (8 instances with no name), 6 with a docstring.

> `Time` represents instants with a fixed but arbitrary unit and orientation. It is an
> affine space over `ℝ`: two instants determine a real-valued elapsed time, and adding
> such a duration to an instant produces another instant. There is no distinguished zero.
>
> The field `Time.val` is an implementation coordinate, not a frame-relative time
> coordinate. A reference frame chooses its own time origin. Import
> `Physlib.SpaceAndTime.Time.InnerProductSpace` to use the inner product space structure with the
> implicit origin `Time.mk 0`, including addition of instants, norms, and derivatives.

## A. The `Time` type

**`Time`**, a structure, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L33).

> An instant in time with a given unit and orientation, but no distinguished origin.

```lean
structure Time where
  /-- The implementation coordinate associated with an instant. -/
  val : ℝ
```

**`Time.val_injective`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L39).

```lean
lemma val_injective : Function.Injective val
```

**An instance with no name**, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L41).

```lean
instance : Nonempty Time
```

## B. The affine structure

**An instance with no name**, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L47).

```lean
instance : VAdd ℝ Time
```

**`Time.vadd_val`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L51).

```lean
lemma vadd_val (dt : ℝ) (t : Time) : (dt +ᵥ t).val = dt + t.val
```

**An instance with no name**, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L53).

```lean
instance : VSub ℝ Time
```

**`Time.vsub_eq_val`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L57).

```lean
lemma vsub_eq_val (t₁ t₂ : Time) : t₁ -ᵥ t₂ = t₁.val - t₂.val
```

**An instance with no name**, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L59).

```lean
instance : AddTorsor ℝ Time
```

## C. The metric and manifold structure

**An instance with no name**, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L69).

```lean
instance : MetricSpace Time
```

**An instance with no name**, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L71).

```lean
instance : NormedAddTorsor ℝ Time
```

**An instance with no name**, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L74).

```lean
instance : ChartedSpace ℝ Time
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L81).

```lean
instance : IsManifold 𝓘(ℝ, ℝ) ω Time
```

**`Time.chartAt_apply`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L88).

> The chart of `Time` at `t₀` is `t ↦ t -ᵥ t₀`.

```lean
lemma chartAt_apply (t₀ t : Time) : chartAt ℝ t₀ t = t -ᵥ t₀
```

**`Time.chartAt_symm_apply`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L92).

> The inverse of the chart of `Time` at `t₀` is `τ ↦ τ +ᵥ t₀`.

```lean
lemma chartAt_symm_apply (t₀ : Time) (τ : ℝ) : (chartAt ℝ t₀).symm τ = τ +ᵥ t₀
```

**`Time.extChartAt_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L95).

> The extended chart of `Time` at `t₀` is `t ↦ t -ᵥ t₀`.

```lean
lemma extChartAt_apply (t₀ t : Time) : extChartAt 𝓘(ℝ, ℝ) t₀ t = t -ᵥ t₀
```

**`Time.contMDiff_vadd`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L98).

> The map `τ ↦ τ +ᵥ t₀` from `ℝ` to `Time` is smooth.

```lean
lemma contMDiff_vadd (t₀ : Time) (n : ℕ∞ω) :
    ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) n (fun τ : ℝ ↦ τ +ᵥ t₀)
```

**`Time.contMDiff_vsub`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean#L106).

> The map `t ↦ t -ᵥ t₀` from `Time` to `ℝ` is smooth.

```lean
lemma contMDiff_vsub (t₀ : Time) (n : ℕ∞ω) :
    ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) n (fun t : Time ↦ t -ᵥ t₀)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/SpaceAndTime/Time/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/Basic.lean)
