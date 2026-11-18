---
declaration: module
origin: cited
lean: UnitDependent, MulUnitDependent, LinearUnitDependent, ContinuousLinearUnitDependent, UnitDependent.scaleUnit_symm_apply, UnitDependent.scaleUnit_injective, UnitDependent.scaleUnitEquiv, LinearUnitDependent.scaleUnitLinear
statement: formalized
proof: formalized
---

# Physlib.Units.UnitDependent

The module `Physlib.Units.UnitDependent`, [Physlib/Units/UnitDependent.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean): 47 declarations (11 instances with no name), 14 with a docstring.

## Types which depend on dimensions

> In addition to types which carry a dimension, we also have types whose elements
> depend on a choice of a units. For example a function
> `f : M1 → M2` between two types `M1` and `M2` which carry dimensions does not itself
> carry a dimensions, but is dependent on a choice of units.
>
> We define three versions
> - `UnitDependent M` having a function `scaleUnit : LTMCTUnitChoices → LTMCTUnitChoices → M → M`
>   subject to two conditions `scaleUnit_trans` and `scaleUnit_id`
> - `LinearUnitDependent M` extends `UnitDependent M` with additional linearity conditions
>   on `scaleUnit`.
> - `ContinuousLinearUnitDependent M` extends `LinearUnitDependent M` with an additional
>   continuity condition on `scaleUnit`.

**`UnitDependent`**, a class, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L40).

> A type carries the instance `UnitDependent M` if it depends on a choice of units.
> This dependence is manifested in `scaleUnit u1 u2` which describes how elements of `M` change
> under a scaling of units which would take `u1` to `u2`.
>
> This type is used for functions, and propositions etc.

```lean
class UnitDependent (M : Type) where
  /-- `scaleUnit u1 u2` is the map transforming elements of `M` under a
    scaling of units which would take the unit `u1` to the unit `u2`. This is not
    to say that in `scaleUnit u1 u2 m` that `m` should be interpreted as being in the units `u1`,
    although this is often the case.
  -/
  scaleUnit : LTMCTUnitChoices → LTMCTUnitChoices → M → M
  scaleUnit_trans : ∀ u1 u2 u3 m, scaleUnit u2 u3 (scaleUnit u1 u2 m) = scaleUnit u1 u3 m
  scaleUnit_trans' : ∀ u1 u2 u3 m, scaleUnit u1 u2 (scaleUnit u2 u3 m) = scaleUnit u1 u3 m
  scaleUnit_id : ∀ u m, scaleUnit u u m = m
```

**`MulUnitDependent`**, a class, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L55).

> A type `M` with an instance of `UnitDependent M` such that `scaleUnit u1 u2` is compatible
> with the `MulAction ℝ≥0 M` instance on `M`.

```lean
class MulUnitDependent (M : Type) [MulAction ℝ≥0 M] extends
    UnitDependent M where
  scaleUnit_mul : ∀ u1 u2 (r : ℝ≥0) m,
    scaleUnit u1 u2 (r • m) = r • scaleUnit u1 u2 m
```

**`LinearUnitDependent`**, a class, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L64).

> A type `M` with an instance of `UnitDependent M` such that `scaleUnit u1 u2` is compatible
> with the `Module ℝ M` instance on `M`.

```lean
class LinearUnitDependent (M : Type) [AddCommMonoid M] [Module ℝ M] extends UnitDependent M where
  scaleUnit_add : ∀ u1 u2 m1 m2,
    scaleUnit u1 u2 (m1 + m2) = scaleUnit u1 u2 m1 + scaleUnit u1 u2 m2
  scaleUnit_smul : ∀ u1 u2 (r : ℝ) m,
    scaleUnit u1 u2 (r • m) = r • scaleUnit u1 u2 m
```

**`ContinuousLinearUnitDependent`**, a class, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L74).

> A type `M` with an instance of `UnitDependent M` such that `scaleUnit u1 u2` is compatible
> with the `Module ℝ M` instance on `M`, and is continuous.

```lean
class ContinuousLinearUnitDependent (M : Type) [AddCommMonoid M] [Module ℝ M]
    [TopologicalSpace M] extends LinearUnitDependent M where
  scaleUnit_cont : ∀ u1 u2, Continuous (scaleUnit u1 u2)
```

> ## Basic properties of scaleUnit

**`UnitDependent.scaleUnit_symm_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L85).

```lean
lemma UnitDependent.scaleUnit_symm_apply {M : Type} [UnitDependent M]
    (u1 u2 : LTMCTUnitChoices) (m : M) :
    scaleUnit u2 u1 (scaleUnit u1 u2 m) = m
```

**`UnitDependent.scaleUnit_injective`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L91).

```lean
lemma UnitDependent.scaleUnit_injective {M : Type} [UnitDependent M]
    (u1 u2 : LTMCTUnitChoices) (m1 m2 : M) :
    scaleUnit u1 u2 m1 = scaleUnit u1 u2 m2 ↔ m1 = m2
```

> ### Variations on the map scaleUnit

**`UnitDependent.scaleUnitEquiv`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L104).

> For an `M` with an instance of `UnitDependent M`, `scaleUnit u1 u2` as an equivalence.

```lean
def UnitDependent.scaleUnitEquiv {M : Type} [UnitDependent M]
    (u1 u2 : LTMCTUnitChoices) : M ≃ M
```

**`LinearUnitDependent.scaleUnitLinear`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L113).

> For an `M` with an instance of `LinearUnitDependent M`, `scaleUnit u1 u2` as a
> linear map.

```lean
def LinearUnitDependent.scaleUnitLinear
    {M : Type} [AddCommMonoid M] [Module ℝ M] [LinearUnitDependent M]
    (u1 u2 : LTMCTUnitChoices) :
    M →ₗ[ℝ] M
```

**`LinearUnitDependent.scaleUnitLinearEquiv`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L123).

> For an `M` with an instance of `LinearUnitDependent M`, `scaleUnit u1 u2` as a
> linear equivalence.

```lean
def LinearUnitDependent.scaleUnitLinearEquiv {M : Type} [AddCommMonoid M]
    [Module ℝ M] [LinearUnitDependent M] (u1 u2 : LTMCTUnitChoices) :
    M ≃ₗ[ℝ] M
```

**`ContinuousLinearUnitDependent.scaleUnitContLinear`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L132).

> For an `M` with an instance of `ContinuousLinearUnitDependent M`, `scaleUnit u1 u2` as a
> continuous linear map.

```lean
def ContinuousLinearUnitDependent.scaleUnitContLinear {M : Type} [AddCommMonoid M] [Module ℝ M]
    [TopologicalSpace M] [ContinuousLinearUnitDependent M]
    (u1 u2 : LTMCTUnitChoices) : M →L[ℝ] M
```

**`ContinuousLinearUnitDependent.scaleUnitContLinearEquiv`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L140).

> For an `M` with an instance of `ContinuousLinearUnitDependent M`, `scaleUnit u1 u2` as a
> continuous linear equivalence.

```lean
def ContinuousLinearUnitDependent.scaleUnitContLinearEquiv {M : Type} [AddCommMonoid M] [Module ℝ M]
    [TopologicalSpace M] [ContinuousLinearUnitDependent M]
    (u1 u2 : LTMCTUnitChoices) : M ≃L[ℝ] M
```

**`ContinuousLinearUnitDependent.scaleUnitContLinearEquiv_apply`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L148).

```lean
lemma ContinuousLinearUnitDependent.scaleUnitContLinearEquiv_apply
    {M : Type} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    [ContinuousLinearUnitDependent M]
    (u1 u2 : LTMCTUnitChoices) (m : M) :
    (ContinuousLinearUnitDependent.scaleUnitContLinearEquiv u1 u2) m =
      scaleUnit u1 u2 m
```

**`ContinuousLinearUnitDependent.scaleUnitContLinearEquiv_symm_apply`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L156).

```lean
lemma ContinuousLinearUnitDependent.scaleUnitContLinearEquiv_symm_apply
    {M : Type} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    [ContinuousLinearUnitDependent M]
    (u1 u2 : LTMCTUnitChoices) (m : M) :
    (ContinuousLinearUnitDependent.scaleUnitContLinearEquiv u1 u2).symm m =
      scaleUnit u2 u1 m
```

### Instances of the type classes

> We construct instance of the `UnitDependent`, `LinearUnitDependent` and
>   `ContinuousLinearUnitDependent` type classes based on `CarriesDimension`
>   and functions.

**An instance with no name**, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L174).

```lean
noncomputable instance : UnitDependent LTMCTUnitChoices
```

**`LTMCTUnitChoices.scaleUnit_apply_fst`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L193).

```lean
lemma LTMCTUnitChoices.scaleUnit_apply_fst (u1 u2 : LTMCTUnitChoices) :
    (scaleUnit u1 u2 u1) = u2
```

**`LTMCTUnitChoices.dimScale_scaleUnit`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L198).

```lean
lemma LTMCTUnitChoices.dimScale_scaleUnit {u1 u2 u : LTMCTUnitChoices}
    (d : Dimension LTMCTDimensionBase) :
    u.dimScale (scaleUnit u1 u2 u) d = u1.dimScale u2 d
```

**`LTMCTUnitChoices.dimScaleUnits_scaleUnit`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L205).

```lean
lemma LTMCTUnitChoices.dimScaleUnits_scaleUnit {u1 u2 u : LTMCTUnitChoices}
    (d : Dimension LTMCTDimensionBase) :
    u.dimScaleUnits (scaleUnit u1 u2 u) d = u1.dimScaleUnits u2 d
```

**`Dimensionful.of_scaleUnit_units`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L211).

```lean
lemma Dimensionful.of_scaleUnit_units {M : Type} [CarriesDimension M] {u1 u2 u : LTMCTUnitChoices}
    (c : Dimensionful M) :
    c.1 (scaleUnit u1 u2 u) =
    u1.dimScaleUnits u2 (dim M) • c.1 (u)
```

**An instance with no name**, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L217).

```lean
noncomputable instance {M1 : Type} [CarriesDimension M1] : UnitDependent M1
```

**`HasDim.scaleUnit_apply_units`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L229).

```lean
lemma HasDim.scaleUnit_apply_units {M : Type} [CarriesDimension M]
    (u1 u2 : LTMCTUnitChoices) (m : M) :
    scaleUnit u1 u2 m = (u1.dimScaleUnits u2 (dim M)) • m
```

**`HasDim.scaleUnit_apply`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L236).

> The scaling of a type carrying a dimension which also has an action of `ℝ≥0`, phrased with
> `dimScale` in place of `dimScaleUnits`.

```lean
lemma HasDim.scaleUnit_apply {M : Type} [HasDim M] [MulAction ℝ≥0 M]
    (u1 u2 : LTMCTUnitChoices) (m : M) :
    scaleUnit u1 u2 m = (u1.dimScale u2 (dim M)) • m
```

**An instance with no name**, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L244).

> A type carrying a dimension which also has a `MulAction ℝ≥0` compatible with the scaling by
> units is `MulUnitDependent`. A type whose elements are strictly positive carries no action of
> `ℝ≥0` compatible with its magnitude, and so is `UnitDependent` only.

```lean
noncomputable instance {M1 : Type} [HasDim M1] [MulAction ℝ≥0 M1] : MulUnitDependent M1
```

**An instance with no name**, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L249).

```lean
noncomputable instance {M : Type} [AddCommMonoid M] [Module ℝ M] [HasDim M] :
    LinearUnitDependent M
```

**An instance with no name**, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L254).

```lean
noncomputable instance {M : Type} [AddCommMonoid M] [Module ℝ M]
    [HasDim M] [TopologicalSpace M]
    [ContinuousConstSMul ℝ M] : ContinuousLinearUnitDependent M
```

### Functions

**An instance with no name**, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L271).

```lean
noncomputable instance {M1 M2 : Type} [UnitDependent M2] :
    UnitDependent (M1 → M2)
```

**`UnitDependent.scaleUnit_apply_fun_right`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L285).

```lean
lemma UnitDependent.scaleUnit_apply_fun_right {M1 M2 : Type} [UnitDependent M2]
    (u1 u2 : LTMCTUnitChoices) (f : M1 → M2) (m1 : M1) :
    scaleUnit u1 u2 f m1 = scaleUnit u1 u2 (f m1)
```

**An instance with no name**, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L290).

```lean
noncomputable instance {M1 M2 : Type} [AddCommMonoid M1] [Module ℝ M1]
    [AddCommMonoid M2] [Module ℝ M2] [LinearUnitDependent M2] :
    LinearUnitDependent (M1 →ₗ[ℝ] M2)
```

**An instance with no name**, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L314).

```lean
noncomputable instance {M1 M2 : Type} [AddCommGroup M1] [Module ℝ M1]
    [TopologicalSpace M1]
    [AddCommGroup M2] [Module ℝ M2] [TopologicalSpace M2] [ContinuousConstSMul ℝ M2]
    [IsTopologicalAddGroup M2]
    [ContinuousLinearUnitDependent M2] :
    ContinuousLinearUnitDependent (M1 →L[ℝ] M2)
```

**An instance with no name**, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L337).

```lean
noncomputable instance {M1 M2 : Type} [UnitDependent M1] :
    UnitDependent (M1 → M2)
```

**`UnitDependent.scaleUnit_apply_fun_left`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L351).

```lean
lemma UnitDependent.scaleUnit_apply_fun_left {M1 M2 : Type} [UnitDependent M1]
    (u1 u2 : LTMCTUnitChoices) (f : M1 → M2) (m1 : M1) :
    scaleUnit u1 u2 f m1 = f (scaleUnit u2 u1 m1)
```

**`instUnitDependentTwoSided`**, an instance, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L355).

```lean
noncomputable instance instUnitDependentTwoSided
    {M1 M2 : Type} [UnitDependent M1] [UnitDependent M2] :
    UnitDependent (M1 → M2)
```

**`UnitDependent.scaleUnit_apply_fun`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L370).

```lean
lemma UnitDependent.scaleUnit_apply_fun {M1 M2 : Type} [UnitDependent M1]
    [UnitDependent M2] (u1 u2 : LTMCTUnitChoices) (f : M1 → M2) (m1 : M1) :
    scaleUnit u1 u2 f m1 = scaleUnit u1 u2 (f (scaleUnit u2 u1 m1))
```

**`instUnitDependentTwoSidedMul`**, an instance, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L374).

```lean
noncomputable instance instUnitDependentTwoSidedMul
    {M1 M2 : Type} [UnitDependent M1] [MulAction ℝ≥0 M2] [MulUnitDependent M2] :
    MulUnitDependent (M1 → M2)
```

**`instContinuousLinearUnitDependentMap`**, an instance, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L392).

```lean
noncomputable instance instContinuousLinearUnitDependentMap
    {M1 M2 : Type} [AddCommGroup M1] [Module ℝ M1]
    [TopologicalSpace M1] [ContinuousLinearUnitDependent M1]
    [AddCommGroup M2] [Module ℝ M2] [TopologicalSpace M2] [ContinuousConstSMul ℝ M2]
    [IsTopologicalAddGroup M2]
    [ContinuousLinearUnitDependent M2] :
    ContinuousLinearUnitDependent (M1 →L[ℝ] M2)
```

**`ContinuousLinearUnitDependent.scaleUnit_apply_fun`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L417).

```lean
lemma ContinuousLinearUnitDependent.scaleUnit_apply_fun {M1 M2 : Type}
    [AddCommGroup M1] [Module ℝ M1]
    [TopologicalSpace M1] [ContinuousLinearUnitDependent M1]
    [AddCommGroup M2] [Module ℝ M2] [TopologicalSpace M2] [ContinuousConstSMul ℝ M2]
    [IsTopologicalAddGroup M2]
    [ContinuousLinearUnitDependent M2]
    (u1 u2 : LTMCTUnitChoices) (f : M1 →L[ℝ] M2) (m1 : M1) :
    scaleUnit u1 u2 f m1 =
      scaleUnit u1 u2 (f (scaleUnit u2 u1 m1))
```

### isDimensionallyCorrect

**`IsDimensionallyCorrect`**, a def, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L443).

> A term of type `M` carrying an instance of `UnitDependent M` is said to be
> dimensionally correct if under a change of units it remains the same.
>
> More colloquially, something is dimensionally correct if it (e.g. it's value or its truth
> for a proposition) does not depend on the units it is written in.
>
> For the case of `m : M` with `CarriesDimension M` then `IsDimensionallyCorrect m`
> corresponds to the statement that `m` does not depend on units, e.g. is zero
> or the dimension of `M` is zero.

```lean
def IsDimensionallyCorrect {M : Type} [UnitDependent M] (m : M) : Prop
```

**`isDimensionallyCorrect_iff`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L446).

```lean
lemma isDimensionallyCorrect_iff {M : Type} [UnitDependent M] (m : M) :
    IsDimensionallyCorrect m ↔ ∀ u1 u2 : LTMCTUnitChoices,
      scaleUnit u1 u2 m = m
```

**`isDimensionallyCorrect_fun_iff`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L451).

```lean
lemma isDimensionallyCorrect_fun_iff {M1 M2 : Type} [UnitDependent M1] [UnitDependent M2]
    {f : M1 → M2} :
    IsDimensionallyCorrect f ↔
    ∀ u1 u2 : LTMCTUnitChoices, ∀ m, scaleUnit u1 u2 (f (scaleUnit u2 u1 m)) = f m
```

**`isDimensionallyCorrect_fun_left`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L458).

```lean
lemma isDimensionallyCorrect_fun_left {M1 M2 : Type} [UnitDependent M1]
    {f : M1 → M2} :
    IsDimensionallyCorrect f ↔
    ∀ u1 u2 : LTMCTUnitChoices, ∀ m, (f (scaleUnit u2 u1 m)) = f m
```

**`isDimensionallyCorrect_fun_right`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L465).

```lean
lemma isDimensionallyCorrect_fun_right {M1 M2 : Type} [UnitDependent M2]
    {f : M1 → M2} :
    IsDimensionallyCorrect f ↔
    ∀ u1 u2 : LTMCTUnitChoices, ∀ m, scaleUnit u1 u2 (f m) = f m
```

## Some type classes to help track dimensions

**`DMul`**, a class, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L478).

> The multiplication of an element of `M1` with an element of `M2` to get an element
> of `M3` in such a way that dimensions are preserved.

```lean
class DMul (M1 M2 M3 : Type) [CarriesDimension M1] [CarriesDimension M2] [CarriesDimension M3]
    extends HMul M1 M2 M3 where
  mul_dim : ∀ (m1 : Dimensionful M1) (m2 : Dimensionful M2),
    HasDimension (fun u => hMul (m1.1 u) (m2.1 u))
```

**`DMul.hMul_scaleUnit`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L484).

```lean
lemma DMul.hMul_scaleUnit {M1 M2 M3 : Type} [CarriesDimension M1] [CarriesDimension M2]
    [CarriesDimension M3]
    [DMul M1 M2 M3] (m1 : M1) (m2 : M2) (u1 u2 : LTMCTUnitChoices) :
    (scaleUnit u1 u2 m1) * (scaleUnit u1 u2 m2) =
    scaleUnit u1 u2 (m1 * m2)
```

## Dim Subtype

**`DimSet`**, a def, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L501).

> Given a type `M` that depends on units, e.g. the function type `M1 → M2` between two types
> carrying a dimension, the subtype of `M` which scales according to the dimension `d`.

```lean
def DimSet (M : Type) [MulAction ℝ≥0 M] [MulUnitDependent M] (d : Dimension LTMCTDimensionBase) :
    Set M
```

**An instance with no name**, [line 505](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L505).

```lean
instance (M : Type) [MulAction ℝ≥0 M] [MulUnitDependent M] (d : Dimension LTMCTDimensionBase) :
    MulAction ℝ≥0 (DimSet M d)
```

**An instance with no name**, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L519).

```lean
instance (M : Type) [MulAction ℝ≥0 M] [MulUnitDependent M] (d : Dimension LTMCTDimensionBase) :
    CarriesDimension (DimSet M d)
```

**`scaleUnit_dimSet_val`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L524).

```lean
lemma scaleUnit_dimSet_val {M : Type} [MulAction ℝ≥0 M] [MulUnitDependent M]
    (d : Dimension LTMCTDimensionBase) (m : DimSet M d) (u1 u2 : LTMCTUnitChoices) :
    (scaleUnit u1 u2 m).1 = scaleUnit u1 u2 m.1
```

**`DimSet.mem_iff`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean#L528).

```lean
lemma DimSet.mem_iff {M : Type} [MulAction ℝ≥0 M] [MulUnitDependent M]
    (d : Dimension LTMCTDimensionBase) (m : M) :
    m ∈ DimSet M d ↔ ∀ u1 u2, scaleUnit u1 u2 m = (LTMCTUnitChoices.dimScale u1 u2 d) • m
```

## Depends on

- [Dimensions and unit](basic.md)

## Sources

- [Physlib/Units/UnitDependent.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/UnitDependent.lean)
