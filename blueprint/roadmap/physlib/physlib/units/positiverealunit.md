---
declaration: module
origin: cited
lean: PositiveRealUnitCore, PositiveRealUnitCore.instInhabited, PositiveRealUnitCore.val_ne_zero, PositiveRealUnitCore.ratio, PositiveRealUnitCore.instHDiv, PositiveRealUnitCore.div_eq_val, PositiveRealUnitCore.div_pos, PositiveRealUnitCore.div_ne_zero
statement: formalized
proof: formalized
---

# A. Shared arithmetic for positive-real unit types

The module `Physlib.Units.PositiveRealUnit`, [Physlib/Units/PositiveRealUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean): 25 declarations, 17 with a docstring.

> `PositiveRealUnitCore` records a unit magnitude and its inverse construction.
> Each concrete unit declares this instance explicitly and keeps its own structure.
> The inhabited and same-type division instances, rescaling operation, and arithmetic
> laws are provided generically. No command or type-specific lemma wrappers are needed.
>
> The arithmetic is adapted from the existing unit modules by Joseph Tooby-Smith.
> This interface describes an individual unit type, independently of the selection
> and combination of units by `UnitMagnitudeCatalog` and `UnitSystem`.

## A.1. Representation and instances

**`PositiveRealUnitCore`**, a class, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L33).

> Common representation API for unit types whose magnitude is a positive real.

```lean
class PositiveRealUnitCore (U : Type) where
  /-- The underlying real magnitude of a unit. -/
  val : U → ℝ
  /-- Every unit has a strictly positive magnitude. -/
  pos : ∀ x, 0 < val x
  /-- Construct a unit from a positive real magnitude. -/
  ofVal : (r : ℝ) → 0 < r → U
  /-- Construction preserves the supplied magnitude. -/
  val_ofVal : ∀ r hr, val (ofVal r hr) = r
  /-- Reconstructing a unit from its magnitude returns that unit. -/
  ofVal_val : ∀ x, ofVal (val x) (pos x) = x
```

**`PositiveRealUnitCore.instInhabited`**, an instance, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L50).

> The unit of magnitude one supplies a default unit.

```lean
instance (priority := 100) instInhabited : Inhabited U
```

**`PositiveRealUnitCore.val_ne_zero`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L54).

```lean
lemma val_ne_zero (x : U) : val x ≠ 0
```

**`PositiveRealUnitCore.ratio`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L58).

> The ratio of the magnitudes of two units of the same type.

```lean
noncomputable def ratio (x y : U) : NNReal
```

**`PositiveRealUnitCore.instHDiv`**, an instance, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L62).

> Division of two units of the same type is their nonnegative real ratio.

```lean
noncomputable instance (priority := 100) instHDiv : HDiv U U NNReal
```

## A.2. Unit ratios

**`PositiveRealUnitCore.div_eq_val`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L70).

> Unit division agrees with the ratio of the two magnitudes.

```lean
lemma div_eq_val (x y : U) :
    x / y = (⟨val x / val y, _root_.div_nonneg (pos x).le (pos y).le⟩ : NNReal)
```

**`PositiveRealUnitCore.div_pos`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L74).

```lean
lemma div_pos (x y : U) : (0 : NNReal) < x / y
```

**`PositiveRealUnitCore.div_ne_zero`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L80).

```lean
lemma div_ne_zero (x y : U) : x / y ≠ (0 : NNReal)
```

**`PositiveRealUnitCore.div_self`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L84).

```lean
lemma div_self (x : U) : x / x = (1 : NNReal)
```

**`PositiveRealUnitCore.div_symm`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L89).

```lean
lemma div_symm (x y : U) : x / y = (y / x : NNReal)⁻¹
```

**`PositiveRealUnitCore.div_mul_div`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L95).

> Unit ratios compose along an intermediate choice of unit.

```lean
lemma div_mul_div (x y z : U) : (x / y : NNReal) * (y / z) = x / z
```

**`PositiveRealUnitCore.div_mul_div_coe`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L102).

```lean
lemma div_mul_div_coe (x y z : U) :
    (x / y : ℝ) * (y / z : ℝ) = x / z
```

## A.3. Positive rescaling

**`PositiveRealUnitCore.scale`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L112).

> Rescale a unit by a strictly positive real factor.

```lean
def scale (r : ℝ) (x : U) (hr : 0 < r := by norm_num) : U
```

**`PositiveRealUnitCore.scale_val`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L116).

```lean
lemma scale_val (r : ℝ) (x : U) (hr : 0 < r) :
    val (scale r x hr) = r * val x
```

**`PositiveRealUnitCore.ext`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L121).

> Units with equal magnitudes are equal.

```lean
lemma ext {x y : U} (h : val x = val y) : x = y
```

**`PositiveRealUnitCore.unitsSMul`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L128).

> The rescaling of a unit magnitude by a strictly positive real, given as a unit of `ℝ≥0`.
> This is `scale` at a factor known to be positive, so the `scale` lemmas may be applied to
> `u • x` after rewriting with `units_smul_eq_scale`.

```lean
def unitsSMul (u : ℝ≥0ˣ) (x : U) : U
```

**`PositiveRealUnitCore.instMulActionUnitsNNReal`**, an instance, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L137).

> A unit magnitude may be rescaled by a strictly positive real, that is by a unit of `ℝ≥0`.
> No action of `ℝ≥0` on `U` can be compatible with the magnitude: taking `a > 0` and `b = 0` in
> `mul_smul` would force `0 • x` to be a fixed point of every rescaling, and no element of `U`
> is.

```lean
instance instMulActionUnitsNNReal : MulAction ℝ≥0ˣ U
```

**`PositiveRealUnitCore.units_smul_eq_scale`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L152).

> A rescaling by a unit of `ℝ≥0` is the rescaling by its underlying positive factor. Rewriting
> with this makes the `scale` lemmas applicable; `simp` does not see through `HSMul.hSMul` on its
> own.

```lean
lemma units_smul_eq_scale (u : ℝ≥0ˣ) (x : U) :
    u • x = scale ((u : ℝ≥0) : ℝ) x (by
      have hu : ((u : ℝ≥0) : ℝ) ≠ 0 := by simp [Units.ne_zero u]
      exact lt_of_le_of_ne (by positivity) (Ne.symm hu))
```

**`PositiveRealUnitCore.val_units_smul`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L159).

> The magnitude of a rescaling by a unit of `ℝ≥0`.

```lean
lemma val_units_smul (u : ℝ≥0ˣ) (x : U) :
    val (u • x) = ((u : ℝ≥0) : ℝ) * val x
```

**`PositiveRealUnitCore.scale_div_self`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L165).

> The ratio of a rescaled unit to the original is the scaling factor.

```lean
lemma scale_div_self (x : U) (r : ℝ) (hr : 0 < r) :
    scale r x hr / x = (⟨r, le_of_lt hr⟩ : NNReal)
```

**`PositiveRealUnitCore.self_div_scale`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L174).

> The reverse ratio is the reciprocal of the scaling factor.

```lean
lemma self_div_scale (x : U) (r : ℝ) (hr : 0 < r) :
    x / scale r x hr =
      (⟨1 / r, _root_.div_nonneg (by simp) (le_of_lt hr)⟩ : NNReal)
```

**`PositiveRealUnitCore.scale_one`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L183).

```lean
lemma scale_one (x : U) : scale 1 x = x
```

**`PositiveRealUnitCore.scale_div_scale`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L189).

> Rescaling two units multiplies their ratio by the ratio of the factors.

```lean
lemma scale_div_scale (x1 x2 : U) {r1 r2 : ℝ} (hr1 : 0 < r1) (hr2 : 0 < r2) :
    scale r1 x1 hr1 / scale r2 x2 hr2 =
      (⟨r1, le_of_lt hr1⟩ / ⟨r2, le_of_lt hr2⟩ : NNReal) * (x1 / x2)
```

**`PositiveRealUnitCore.scale_scale`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L200).

> Successive rescalings compose by multiplication of their factors.

```lean
lemma scale_scale (x : U) (r1 r2 : ℝ) (hr1 : 0 < r1) (hr2 : 0 < r2) :
    scale r1 (scale r2 x hr2) hr1 =
      scale (r1 * r2) x (mul_pos hr1 hr2)
```

**`PositiveRealUnitCore.scale_div`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean#L208).

> Rescaling a unit by the ratio to a target unit produces that target.

```lean
lemma scale_div (x y : U) (hr : 0 < (y / x : ℝ)) :
    scale (y / x) x hr = y
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Units/PositiveRealUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/PositiveRealUnit.lean)
