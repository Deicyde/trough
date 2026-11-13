---
declaration: module
origin: cited
lean: WithDim, WithDim.ext, WithDim.dim_apply, WithDim.val_zero, WithDim.val_add, WithDim.val_neg, WithDim.val_sub, WithDim.le_def
statement: formalized
proof: formalized
---

# Physlib.Units.WithDim.Basic

The module `Physlib.Units.WithDim.Basic`, [Physlib/Units/WithDim/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean): 50 declarations (20 instances with no name), 7 with a docstring.

## WithDim

> WithDim is the type `M` which carrying the dimension `d`.
>
> The dimension `d : Dimension B` may be taken over any basis `B` of base dimensions.
> The *algebraic* structure of `WithDim d M` (its additive, order, scalar-action,
> multiplication, division and casting instances) is available for every basis `B`.
> The *unit-scaling* structure (`HasDim`, `DMul`, and the `scaleUnit` lemmas), which
> routes through `LTMCTUnitChoices.dimScale`, is provided for the standard basis
> `LTMCTDimensionBase`.
>
> Real scalar multiplication acts on numerical values. Import
> `Physlib.Units.WithDim.Analysis` for the normed-space structures and explicit
> coordinate equivalences used to reuse existing analytic results.

**`WithDim`**, a structure, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L33).

> The type `M` carrying an instance of a dimension `d`.

```lean
structure WithDim {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) where
  /-- The underlying value of `M`. -/
  val : M
```

**`WithDim.ext`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L40).

```lean
lemma ext {B : Type} [DimensionBasis B] {d : Dimension B} {M}
    (x1 x2 : WithDim d M) (h : x1.val = x2.val) :
    x1 = x2
```

**An instance with no name**, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L47).

```lean
instance (d : Dimension LTMCTDimensionBase) (M : Type) : HasDim (WithDim d M)
```

**`WithDim.dim_apply`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L51).

```lean
lemma dim_apply (d : Dimension LTMCTDimensionBase) (M : Type) :
    dim (WithDim d M) = d
```

## Inherited instances

**An instance with no name**, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L58).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [Inhabited M] :
    Inhabited (WithDim d M)
```

**An instance with no name**, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L62).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [Zero M] :
    Zero (WithDim d M)
```

**`WithDim.val_zero`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L67).

```lean
lemma val_zero {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} [Zero M] :
    (0 : WithDim d M).val = 0
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L70).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [Add M] :
    Add (WithDim d M)
```

**`WithDim.val_add`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L75).

```lean
lemma val_add {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} [Add M]
    (m1 m2 : WithDim d M) :
    (m1 + m2).val = m1.val + m2.val
```

**An instance with no name**, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L79).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [Neg M] :
    Neg (WithDim d M)
```

**`WithDim.val_neg`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L84).

```lean
lemma val_neg {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} [Neg M]
    (m : WithDim d M) :
    (-m).val = -m.val
```

**An instance with no name**, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L88).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [Sub M] :
    Sub (WithDim d M)
```

**`WithDim.val_sub`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L93).

```lean
lemma val_sub {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} [Sub M]
    (m1 m2 : WithDim d M) :
    (m1 - m2).val = m1.val - m2.val
```

**An instance with no name**, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L97).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [AddSemigroup M] :
    AddSemigroup (WithDim d M)
```

**An instance with no name**, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L103).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [AddCommSemigroup M] :
    AddCommSemigroup (WithDim d M)
```

**An instance with no name**, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L109).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [AddMonoid M] :
    AddMonoid (WithDim d M)
```

**An instance with no name**, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L119).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [AddCommMonoid M] :
    AddCommMonoid (WithDim d M)
```

**An instance with no name**, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L125).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [AddGroup M] :
    AddGroup (WithDim d M)
```

**An instance with no name**, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L135).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [AddCommGroup M] :
    AddCommGroup (WithDim d M)
```

**An instance with no name**, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L141).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [LE M] :
    LE (WithDim d M)
```

**`WithDim.le_def`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L146).

```lean
lemma le_def {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} [LE M]
    (m1 m2 : WithDim d M) :
    m1 ≤ m2 ↔ m1.val ≤ m2.val
```

**An instance with no name**, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L150).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [LT M] :
    LT (WithDim d M)
```

**`WithDim.lt_def`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L155).

```lean
lemma lt_def {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} [LT M]
    (m1 m2 : WithDim d M) :
    m1 < m2 ↔ m1.val < m2.val
```

**An instance with no name**, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L159).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [Preorder M] :
    Preorder (WithDim d M)
```

**An instance with no name**, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L170).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [PartialOrder M] :
    PartialOrder (WithDim d M)
```

**An instance with no name**, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L176).

```lean
instance {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type) [MulAction ℝ≥0 M] :
    MulAction ℝ≥0 (WithDim d M)
```

**`WithDim.smul_val`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L185).

```lean
lemma smul_val {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} [MulAction ℝ≥0 M]
    (a : ℝ≥0) (m : WithDim d M) :
    (a • m).val = a • m.val
```

**`WithDim.smul_val_units`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L191).

> The underlying value of a scaling by a unit of `ℝ≥0`, that is by a strictly positive real.

```lean
lemma smul_val_units {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type}
    [MulAction ℝ≥0 M] (a : ℝ≥0ˣ) (m : WithDim d M) :
    (a • m).val = (a : ℝ≥0) • m.val
```

**`WithDim.ofPositiveRealUnit`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L198).

> A positive-real quantity which carries a dimension, regarded as a dimension-tagged real, so
> that it can be used alongside the other dimension-tagged quantities. The dimension is read off
> the `HasDim` instance, so the two cannot drift apart.

```lean
def ofPositiveRealUnit {U : Type} [PositiveRealUnitCore U] [HasDim U] (x : U) :
    WithDim (dim U) ℝ
```

**`WithDim.ofPositiveRealUnit_val`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L203).

```lean
lemma ofPositiveRealUnit_val {U : Type} [PositiveRealUnitCore U] [HasDim U] (x : U) :
    (ofPositiveRealUnit x).val = PositiveRealUnitCore.val x
```

**`WithDim.ofPositiveRealUnit_units_smul`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L207).

```lean
lemma ofPositiveRealUnit_units_smul {U : Type} [PositiveRealUnitCore U] [HasDim U]
    (a : ℝ≥0ˣ) (x : U) :
    ofPositiveRealUnit (a • x) = a • ofPositiveRealUnit x
```

**`WithDim.ofPositiveRealUnit_of_scaleUnit`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L216).

> A dimensionful positive-real quantity, such as the speed of light, may be tagged with its
> dimension either before or after a change of units: `ofPositiveRealUnit` commutes with
> `scaleUnit`.

```lean
lemma ofPositiveRealUnit_of_scaleUnit {U : Type} [PositiveRealUnitCore U] [HasDim U]
    {u1 u2 u : LTMCTUnitChoices} (c : Dimensionful U) :
    ofPositiveRealUnit (c.1 (UnitDependent.scaleUnit u1 u2 u)) =
    UnitDependent.scaleUnit u1 u2 (ofPositiveRealUnit (c.1 u))
```

**`WithDim.instModuleReal`**, an instance, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L232).

> Dimensionless real scalars act on the numerical value of a tagged quantity.

```lean
instance instModuleReal {B : Type} [DimensionBasis B] (d : Dimension B) (M : Type)
    [AddCommMonoid M] [Module ℝ M] : Module ℝ (WithDim d M)
```

**`WithDim.real_smul_val`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L243).

```lean
lemma real_smul_val {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type}
    [AddCommMonoid M] [Module ℝ M] (r : ℝ) (x : WithDim d M) :
    (r • x).val = r • x.val
```

**An instance with no name**, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L247).

```lean
instance {B : Type} [DimensionBasis B] {d1 d2 : Dimension B} :
    HMul (WithDim d1 ℝ) (WithDim d2 ℝ) (WithDim (d1 * d2) ℝ)
```

**`WithDim.withDim_hMul_val`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L251).

```lean
lemma withDim_hMul_val {B : Type} [DimensionBasis B] {d1 d2 : Dimension B}
    (m1 : WithDim d1 ℝ) (m2 : WithDim d2 ℝ) :
    (m1 * m2).val = m1.val * m2.val
```

**An instance with no name**, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L255).

```lean
instance {d1 d2 : Dimension LTMCTDimensionBase} :
    DMul (WithDim d1 ℝ) (WithDim d2 ℝ) (WithDim (d1 * d2) ℝ)
```

**`WithDim.val_mul_eq_mul`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L272).

```lean
lemma val_mul_eq_mul {B : Type} [DimensionBasis B] {d1 d2 : Dimension B}
    (m1 : WithDim d1 ℝ) (m2 : WithDim d2 ℝ) :
    m1.val * m2.val = (m1 * m2).val
```

**`WithDim.val_pow_two_eq_mul`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L278).

```lean
lemma val_pow_two_eq_mul {B : Type} [DimensionBasis B] {d1 : Dimension B}
    (m1 : WithDim d1 ℝ) :
    m1.val ^ 2 = (m1 * m1).val
```

**`WithDim.scaleUnit_val_eq_scaleUnit_val`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L285).

```lean
lemma scaleUnit_val_eq_scaleUnit_val {d : Dimension LTMCTDimensionBase} (M : Type) [MulAction ℝ≥0 M]
    (u1 u2 : LTMCTUnitChoices) (m1 m2 : WithDim d M) :
    (scaleUnit u1 u2 m1).val = (scaleUnit u1 u2 m2).val ↔ m1.val = m2.val
```

**`WithDim.scaleUnit_val_eq_scaleUnit_val_of_dim_eq`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L292).

```lean
lemma scaleUnit_val_eq_scaleUnit_val_of_dim_eq {d1 d2 : Dimension LTMCTDimensionBase} {M : Type}
    [MulAction ℝ≥0 M]
    {u1 u2 : LTMCTUnitChoices} {m1 : WithDim d1 M} {m2 : WithDim d2 M}
    (h : d1 = d2 := by ext <;> {simp; try ring}) :
    (scaleUnit u1 u2 m1).val = (scaleUnit u1 u2 m2).val ↔ m1.val = m2.val
```

**`WithDim.scaleUnit_val`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L300).

```lean
lemma scaleUnit_val {d : Dimension LTMCTDimensionBase} (M : Type) [MulAction ℝ≥0 M]
    (u1 u2 : LTMCTUnitChoices) (m1 : WithDim d M) :
    (scaleUnit u1 u2 m1).val = u1.dimScale u2 d • m1.val
```

**`WithDim.scaleUnit_val_pos`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L306).

> Scaling by a change of units preserves positivity of the value of a dimensionful
> quantity.

```lean
lemma scaleUnit_val_pos {d : Dimension LTMCTDimensionBase} (m : WithDim d ℝ≥0) (hm : 0 < m.val)
    (u1 u2 : LTMCTUnitChoices) : 0 < (scaleUnit u1 u2 m).val
```

## Division

**An instance with no name**, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L317).

```lean
noncomputable instance {B : Type} [DimensionBasis B] (d1 d2 : Dimension B) :
    HDiv (WithDim d1 ℝ) (WithDim d2 ℝ) (WithDim (d1 * d2⁻¹) ℝ)
```

**`WithDim.val_div_val`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L322).

```lean
lemma val_div_val {B : Type} [DimensionBasis B] {d1 d2 : Dimension B}
    (m1 : WithDim d1 ℝ) (m2 : WithDim d2 ℝ) :
    (m1.val / m2.val) = (m1 / m2).val
```

**`WithDim.div_scaleUnit`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L327).

```lean
lemma div_scaleUnit {d1 d2 : Dimension LTMCTDimensionBase} (m1 : WithDim d1 ℝ) (m2 : WithDim d2 ℝ)
    (u1 u2 : LTMCTUnitChoices) :
    (scaleUnit u1 u2 m1) / (scaleUnit u1 u2 m2) = scaleUnit u1 u2 (m1 / m2)
```

**`WithDim.scaleUnit_dim_eq_zero`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L341).

```lean
lemma scaleUnit_dim_eq_zero {d : Dimension LTMCTDimensionBase} (m : WithDim d ℝ)
    (u1 u2 : LTMCTUnitChoices) (h : d = 1 := by ext <;> {simp; try ring}) :
    scaleUnit u1 u2 m = m
```

## Casting

**`WithDim.cast`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L356).

> The casting from `WithDim d M` to `WithDim d2 M` when `d = d2`.

```lean
def cast {B : Type} [DimensionBasis B] {d d2 : Dimension B} {M : Type} (m : WithDim d M)
    (h : d = d2 := by ext <;> {simp; try ring}) : WithDim d2 M
```

**`WithDim.cast_refl`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L360).

```lean
lemma cast_refl {B : Type} [DimensionBasis B] {d : Dimension B} {M : Type} (m : WithDim d M) :
    cast m rfl = m
```

**`WithDim.cast_scaleUnit`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean#L364).

```lean
lemma cast_scaleUnit {d d2 : Dimension LTMCTDimensionBase} {M : Type} [MulAction ℝ≥0 M]
    (m : WithDim d M)
    (h : d = d2) (u1 u2 : LTMCTUnitChoices) :
    cast (scaleUnit u1 u2 m) h = scaleUnit u1 u2 (cast m h)
```

## Depends on

- [Physlib.Units.UnitDependent](../unitdependent.md)

## Sources

- [Physlib/Units/WithDim/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Basic.lean)
