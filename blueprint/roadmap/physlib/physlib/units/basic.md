---
declaration: module
origin: cited
lean: LTMCTUnitChoices, LTMCTUnitChoices.dimScale, LTMCTUnitChoices.dimScale_apply, LTMCTUnitChoices.dimScale_self, LTMCTUnitChoices.dimScale_one, LTMCTUnitChoices.dimScale_L𝓭, LTMCTUnitChoices.dimScale_T𝓭, LTMCTUnitChoices.dimScale_M𝓭
statement: formalized
proof: formalized
---

# Dimensions and unit

The module `Physlib.Units.Basic`, [Physlib/Units/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean): 47 declarations (3 instances with no name), 19 with a docstring.

> A unit in physics arises from choice of something in physics which is non-canonical.
> An example is the choice of translationally-invariant metric on the time manifold `TimeMan`.
>
> A dimension is a property of a quantity related to how it changes with respect to a
> change in the unit.
>
> The fundamental choices one has in physics are related to:
> - Time
> - Length
> - Mass
> - Charge
> - Temperature
>
> …
>
> From these fundamental choices one can construct all other units and dimensions.

## Implementation details

> Units within Physlib are implemented with the following convention:
> - The fundamental units, and the choices they correspond to, are defined within the
>   appropriate physics directory, in particular:
>   - `Physlib/SpaceAndTime/Time/TimeUnit.lean`
>   - `Physlib/SpaceAndTime/Space/LengthUnit.lean`
>   - `Physlib/ClassicalMechanics/Mass/MassUnit.lean`
>   - `Physlib/Electromagnetism/Charge/ChargeUnit.lean`
>   - `Physlib/Thermodynamics/Temperature/TemperatureUnit.lean`
> - In this `Units` directory, we define the necessary structures and properties
>   to work derived units and dimensions.

## References

> Zulip chats discussing units:
>
> * https://leanprover.zulipchat.com/#narrow/channel/479953-Physlib/topic/physical.20units.
> * https://leanprover.zulipchat.com/#narrow/channel/116395-maths/topic/Dimensional.20Analysis.20Revisited/with/530238303.

## Note

> A lot of the results around units is still experimental and should be adapted based on needs.

## Other implementations of units

> There are other implementations of units in Lean, in particular:
> 1. https://github.com/ATOMSLab/LeanDimensionalAnalysis/tree/main
> 2. https://github.com/teorth/analysis/blob/main/analysis/Analysis/Misc/SI.lean
> 3. https://github.com/ecyrbe/lean-units
> Each of these have their own advantages and specific use-cases.
> For example both (1) and (3) allow for or work in Floats, allowing computability and the use
> of `#eval`. This is currently not possible with the more theoretical implementation here
> in Physlib which is based exclusively on Reals.

## Units

**`LTMCTUnitChoices`**, a structure, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L85).

> The choice of units.

```lean
structure LTMCTUnitChoices where
  /-- The length unit. -/
  length : LengthUnit
  /-- The time unit. -/
  time : TimeUnit
  /-- The mass unit. -/
  mass : MassUnit
  /-- The charge unit. -/
  charge : ChargeUnit
  /-- The temperature unit. -/
  temperature : TemperatureUnit
```

**`LTMCTUnitChoices.dimScale`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L102).

> Given two choices of units `u1` and `u2` and a dimension `d`, the
> element of `ℝ≥0` corresponding to the scaling (by definition) of a quantity of dimension `d`
> when changing from units `u1` to `u2`.

```lean
noncomputable def dimScale (u1 u2 : LTMCTUnitChoices) :Dimension LTMCTDimensionBase →* ℝ≥0
```

**`LTMCTUnitChoices.dimScale_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L117).

```lean
lemma dimScale_apply (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScale u1 u2 d =
      (u1.length / u2.length) ^ (d.length : ℝ) *
      (u1.time / u2.time) ^ (d.time : ℝ) *
      (u1.mass / u2.mass) ^ (d.mass : ℝ) *
      (u1.charge / u2.charge) ^ (d.charge : ℝ) *
      (u1.temperature / u2.temperature) ^ (d.temperature : ℝ)
```

**`LTMCTUnitChoices.dimScale_self`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L126).

```lean
lemma dimScale_self (u : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScale u u d = 1
```

**`LTMCTUnitChoices.dimScale_one`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L131).

```lean
lemma dimScale_one (u1 u2 : LTMCTUnitChoices) :
    dimScale u1 u2 1 = 1
```

**`LTMCTUnitChoices.dimScale_L𝓭`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L136).

> The scale factor of the dimension of length is the ratio of the length units.

```lean
lemma dimScale_L𝓭 (u1 u2 : LTMCTUnitChoices) :
    dimScale u1 u2 Dimension.L𝓭 = u1.length / u2.length
```

**`LTMCTUnitChoices.dimScale_T𝓭`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L141).

> The scale factor of the dimension of time is the ratio of the time units.

```lean
lemma dimScale_T𝓭 (u1 u2 : LTMCTUnitChoices) :
    dimScale u1 u2 Dimension.T𝓭 = u1.time / u2.time
```

**`LTMCTUnitChoices.dimScale_M𝓭`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L146).

> The scale factor of the dimension of mass is the ratio of the mass units.

```lean
lemma dimScale_M𝓭 (u1 u2 : LTMCTUnitChoices) :
    dimScale u1 u2 Dimension.M𝓭 = u1.mass / u2.mass
```

**`LTMCTUnitChoices.dimScale_Θ𝓭`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L151).

> The scale factor of the dimension of temperature is the ratio of the temperature units.

```lean
lemma dimScale_Θ𝓭 (u1 u2 : LTMCTUnitChoices) :
    dimScale u1 u2 Dimension.Θ𝓭 = u1.temperature / u2.temperature
```

**`LTMCTUnitChoices.dimScale_transitive`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L155).

```lean
lemma dimScale_transitive (u1 u2 u3 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScale u1 u2 d * dimScale u2 u3 d = dimScale u1 u3 d
```

**`LTMCTUnitChoices.dimScale_mul_symm`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L171).

```lean
lemma dimScale_mul_symm (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScale u1 u2 d * dimScale u2 u1 d = 1
```

**`LTMCTUnitChoices.dimScale_coe_mul_symm`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L176).

```lean
lemma dimScale_coe_mul_symm (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    (toReal (dimScale u1 u2 d)) * (toReal (dimScale u2 u1 d)) = 1
```

**`LTMCTUnitChoices.dimScale_ne_zero`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L183).

```lean
lemma dimScale_ne_zero (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScale u1 u2 d ≠ 0
```

**`LTMCTUnitChoices.dimScale_symm`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L187).

```lean
lemma dimScale_symm (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScale u1 u2 d = (dimScale u2 u1 d)⁻¹
```

**`LTMCTUnitChoices.dimScale_of_inv_eq_swap`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L197).

```lean
lemma dimScale_of_inv_eq_swap (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScale u1 u2 d⁻¹ = dimScale u2 u1 d
```

**`LTMCTUnitChoices.smul_dimScale_injective`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L203).

```lean
lemma smul_dimScale_injective {M : Type} [MulAction ℝ≥0 M] (u1 u2 : LTMCTUnitChoices)
    (d : Dimension LTMCTDimensionBase) (m1 m2 : M) :
    (u1.dimScale u2 d) • m1 = (u1.dimScale u2 d) • m2 ↔ m1 = m2
```

**`LTMCTUnitChoices.dimScale_pos`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L212).

```lean
lemma dimScale_pos (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    0 < (dimScale u1 u2 d)
```

**`LTMCTUnitChoices.dimScaleUnits`**, a def, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L230).

> The scaling factor `dimScale u1 u2 d` regarded as a unit of `ℝ≥0`, that is as a strictly
> positive real. Dimensionful quantities are scaled by this rather than by `dimScale u1 u2 d`
> itself, so that a type whose elements are strictly positive, such as `SpeedOfLight`, can carry
> a dimension: no action of `ℝ≥0` on such a type can be compatible with the magnitude, since
> compatibility at `a = 0` would give `val (0 • m) = 0` while `val` is strictly positive.

```lean
noncomputable def dimScaleUnits (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    ℝ≥0ˣ
```

**`LTMCTUnitChoices.dimScaleUnits_coe`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L235).

```lean
lemma dimScaleUnits_coe (u1 u2 : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    ((dimScaleUnits u1 u2 d : ℝ≥0)) = dimScale u1 u2 d
```

**`LTMCTUnitChoices.dimScaleUnits_transitive`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L239).

```lean
lemma dimScaleUnits_transitive (u1 u2 u3 : LTMCTUnitChoices)
    (d : Dimension LTMCTDimensionBase) :
    dimScaleUnits u1 u2 d * dimScaleUnits u2 u3 d = dimScaleUnits u1 u3 d
```

**`LTMCTUnitChoices.dimScaleUnits_smul`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L247).

> Scaling by `dimScaleUnits` agrees with scaling by `dimScale` whenever the type also carries
> an action of `ℝ≥0`, so that statements phrased either way normalise to the same form.

```lean
lemma dimScaleUnits_smul {M : Type} [MulAction ℝ≥0 M] (u1 u2 : LTMCTUnitChoices)
    (d : Dimension LTMCTDimensionBase) (m : M) :
    dimScaleUnits u1 u2 d • m = dimScale u1 u2 d • m
```

**`LTMCTUnitChoices.dimScaleUnits_mul_dim`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L252).

```lean
lemma dimScaleUnits_mul_dim (u1 u2 : LTMCTUnitChoices)
    (d1 d2 : Dimension LTMCTDimensionBase) :
    dimScaleUnits u1 u2 (d1 * d2) = dimScaleUnits u1 u2 d1 * dimScaleUnits u1 u2 d2
```

**`LTMCTUnitChoices.dimScaleUnits_self`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L259).

```lean
lemma dimScaleUnits_self (u : LTMCTUnitChoices) (d : Dimension LTMCTDimensionBase) :
    dimScaleUnits u u d = 1
```

**`LTMCTUnitChoices.SI`**, a def, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L274).

> The choice of units corresponding to SI units, that is
> - meters,
> - seconds,
> - kilograms,
> - coulombs,
> - kelvin.

```lean
noncomputable def SI : LTMCTUnitChoices
```

**`LTMCTUnitChoices.SI_length`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L282).

```lean
lemma SI_length : SI.length = LengthUnit.meters
```

**`LTMCTUnitChoices.SI_time`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L285).

```lean
lemma SI_time : SI.time = TimeUnit.seconds
```

**`LTMCTUnitChoices.SI_mass`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L288).

```lean
lemma SI_mass : SI.mass = MassUnit.kilograms
```

**`LTMCTUnitChoices.SI_charge`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L291).

```lean
lemma SI_charge : SI.charge = ChargeUnit.coulombs
```

**`LTMCTUnitChoices.SI_temperature`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L294).

```lean
lemma SI_temperature : SI.temperature = TemperatureUnit.kelvin
```

**`LTMCTUnitChoices.SIPrimed`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L299).

> A `LTMCTUnitChoices` which is related to `SI` by a prime scaling of each
> of the underlying units. This is useful in proving that a result is not
> dimensionally correct.

```lean
noncomputable def SIPrimed : LTMCTUnitChoices
```

**`LTMCTUnitChoices.dimScale_SI_SIPrimed`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L307).

```lean
lemma dimScale_SI_SIPrimed (d : Dimension LTMCTDimensionBase) :
    dimScale SI SIPrimed d =
      (2⁻¹ : ℝ≥0) ^ (d.length : ℝ) *
      (3⁻¹ : ℝ≥0) ^ (d.time : ℝ) *
      (5⁻¹ : ℝ≥0) ^ (d.mass : ℝ) *
      (7⁻¹ : ℝ≥0) ^ (d.charge : ℝ) *
      (11⁻¹ : ℝ≥0) ^ (d.temperature : ℝ)
```

**`LTMCTUnitChoices.dimScale_SIPrimed_SI`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L318).

```lean
lemma dimScale_SIPrimed_SI (d : Dimension LTMCTDimensionBase) :
    dimScale SIPrimed SI d =
      (2 : ℝ≥0) ^ (d.length : ℝ) *
      (3 : ℝ≥0) ^ (d.time : ℝ) *
      (5 : ℝ≥0) ^ (d.mass : ℝ) *
      (7 : ℝ≥0) ^ (d.charge : ℝ) *
      (11 : ℝ≥0) ^ (d.temperature : ℝ)
```

## Types carrying dimensions

> Dimensions are assigned to types with the following type-classes
>
> - `HasDim` for any type `M` with an associated dimension
> - `CarriesDimension` for a type that also has an instance of `MulAction ℝ≥0ˣ M`, that is an
>   action of the strictly positive reals
>
> Changing units rescales a quantity by a strictly positive factor: a length in metres is the same
> length in feet times `0.3048`, and no change of units ever scales by zero. The strictly positive
> reals `ℝ≥0ˣ` are therefore the natural scalars here, and `LTMCTUnitChoices.dimScaleUnits` records
> the factor. Taking them rather than `ℝ≥0` is what lets a type whose elements are strictly
> positive, such as `SpeedOfLight`, carry a dimension: on such a type a scaling compatible with
> the magnitude, that is one satisfying `val (a • x) = a * val x`, cannot exist at `a = 0`, since
> `val` is strictly positive.
>
> A type with an action of `ℝ≥0`, such as `ℝ` or any real vector space, obtains the action of
> `ℝ≥0ˣ` by restriction, and so carries a dimension as soon as it has a `HasDim` instance. A
> declaration about such types should assume `[HasDim M]` and `[MulAction ℝ≥0 M]`, never
> `[CarriesDimension M]` and `[MulAction ℝ≥0 M]` together: the latter pair puts two unrelated
> actions of `ℝ≥0ˣ` in scope and proofs about the scaling get stuck. Where both actions genuinely
> coexist, as on `Dimensionful M` below, the declared one and the one restricted from `ℝ≥0` agree
> definitionally.
>
> Several statements below therefore come in two forms: the plain name carries the `ℝ≥0` statement,
> which the concrete unit calculations use, and the suffix `_units` the `ℝ≥0ˣ` statement, which
> holds for every type carrying a dimension.

**`HasDim`**, a class, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L364).

> This typeclass indicates that there is a dimension `dim M : Dimension`
> associated with the type `M`.

```lean
class HasDim (M : Type) where
  /-- The dimension associated with a type `M`. -/
  d : Dimension LTMCTDimensionBase
```

**`dim`**, an alias, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L368).

```lean
alias dim
```

## Terms of the current dimension

> Given a type `M` which carries a dimension `d`,
> we are interested in elements of `M` which depend on a choice of units, i.e. functions
> `LTMCTUnitChoices → M`.
>
> We define both a proposition
> - `HasDimension f` which says that `f` scales correctly with units,
> and a type
> - `Dimensionful M` which is the subtype of functions which `HasDimension`.

**`HasDimension`**, a def, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L392).

> A quantity of type `M` which depends on a choice of units `LTMCTUnitChoices` is said to be
> of dimension `d` if it scales by `LTMCTUnitChoices.dimScaleUnits u1 u2 d` under a change in
> units.

```lean
def HasDimension {M : Type} [CarriesDimension M] (f : LTMCTUnitChoices → M) : Prop
```

**`hasDimension_iff`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L395).

```lean
lemma hasDimension_iff {M : Type} [CarriesDimension M] (f : LTMCTUnitChoices → M) :
    HasDimension f ↔ ∀ u1 u2 : LTMCTUnitChoices, f u2 =
    LTMCTUnitChoices.dimScaleUnits u1 u2 (dim M) • f u1
```

**`Dimensionful`**, a def, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L402).

> The subtype of functions `LTMCTUnitChoices → M`, for which `M` carries a dimension,
> which `HasDimension`.

```lean
def Dimensionful (M : Type) [CarriesDimension M]
```

**An instance with no name**, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L404).

```lean
instance {M : Type} [CarriesDimension M] :
    CoeFun (Dimensionful M) (fun _ => LTMCTUnitChoices → M)
```

**`Dimensionful.ext`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L409).

```lean
lemma Dimensionful.ext {M : Type} [CarriesDimension M] (f1 f2 : Dimensionful M)
    (h : f1.val = f2.val) : f1 = f2
```

**An instance with no name**, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L412).

```lean
instance {M : Type} [CarriesDimension M] : MulAction ℝ≥0ˣ (Dimensionful M)
```

**An instance with no name**, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L427).

> When `M` itself carries an action of `ℝ≥0`, a dimensionful quantity of `M` may be scaled by
> any non-negative real, not only by a strictly positive one.

```lean
instance {M : Type} [HasDim M] [MulAction ℝ≥0 M] :
    MulAction ℝ≥0 (Dimensionful M)
```

**`Dimensionful.smul_apply`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L444).

> The value of a non-negative real scaling of a dimensionful quantity.

```lean
lemma Dimensionful.smul_apply {M : Type} [HasDim M] [MulAction ℝ≥0 M]
    (a : ℝ≥0) (f : Dimensionful M) (u : LTMCTUnitChoices) :
    (a • f).1 u = a • f.1 u
```

**`Dimensionful.smul_apply_units`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L449).

```lean
lemma Dimensionful.smul_apply_units {M : Type} [CarriesDimension M]
    (a : ℝ≥0ˣ) (f : Dimensionful M) (u : LTMCTUnitChoices) :
    (a • f).1 u = a • f.1 u
```

**`CarriesDimension.toDimensionful`**, a def, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L455).

> For `M` carrying a dimension `d`, the equivalence between `M` and `Dimension M`,
> given a choice of units.

```lean
noncomputable def CarriesDimension.toDimensionful {M : Type} [CarriesDimension M]
    (u : LTMCTUnitChoices) :
    M ≃ Dimensionful M
```

**`CarriesDimension.toDimensionful_apply_apply_units`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L473).

> The value of `toDimensionful`, scaled by `dimScaleUnits`. This is the general form, holding
> for every type carrying a dimension.

```lean
lemma CarriesDimension.toDimensionful_apply_apply_units
    {M : Type} [CarriesDimension M] (u1 u2 : LTMCTUnitChoices) (m : M) :
    (toDimensionful u1 m).1 u2 = (u1.dimScaleUnits u2 (dim M)) • m
```

**`CarriesDimension.toDimensionful_apply_apply`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L480).

> The value of `toDimensionful` for a type which also carries an action of `ℝ≥0`, phrased with
> `dimScale` in place of `dimScaleUnits`. This is the form the concrete unit calculations use.

```lean
lemma CarriesDimension.toDimensionful_apply_apply
    {M : Type} [HasDim M] [MulAction ℝ≥0 M] (u1 u2 : LTMCTUnitChoices) (m : M) :
    (toDimensionful u1 m).1 u2 = (u1.dimScale u2 (dim M)) • m
```

**`CarriesDimension.toDimensionful_apply_self`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean#L487).

> Reading a quantity built by `toDimensionful u` back in the same unit choice `u` returns the
> value it was built from.

```lean
lemma CarriesDimension.toDimensionful_apply_self
    {M : Type} [CarriesDimension M] (u : LTMCTUnitChoices) (m : M) :
    toDimensionful u m u = m
```

## Depends on

- [Units on Mass](../classicalmechanics/mass/massunit.md)
- [The units of charge](../electromagnetism/charge/chargeunit.md)
- [Units on Length](../spaceandtime/space/part-01/lengthunit.md)
- [Units on time](../spaceandtime/time/timeunit.md)
- [Units on Temperature](../thermodynamics/temperature/temperatureunits.md)
- [PhysLib's default dimension basis](ltmctdimensionbase.md)

## Sources

- [Physlib/Units/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Basic.lean)
