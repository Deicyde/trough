---
declaration: module
origin: cited
lean: UnitExamples.meters400, UnitExamples.EnergyMassWithDim', UnitExamples.energyMassWithDim'_isDimensionallyCorrect, UnitExamples.NewtonsSecondWithDim', UnitExamples.newtonsSecondWithDim'_isDimensionallyCorrect, UnitExamples.SpeedEq, UnitExamples.speedEq_isDimensionallyCorrect, UnitExamples.OddDimensions
statement: formalized
proof: formalized
---

# Examples of units in Physlib

The module `Physlib.Units.Examples`, [Physlib/Units/Examples.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean): 22 declarations, 12 with a docstring.

> In this module we give some examples of how to use the units system in Physlib.
> This module should not be imported into any other module, and the results here
> should not be used in the proofs of any other results other then those in this file.

## Defining a length dependent on units

**`UnitExamples.meters400`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L32).

> The length corresponding to 400 meters.

```lean
noncomputable def meters400 : Dimensionful (WithDim L𝓭 ℝ)
```

## Proving propositions are dimensionally correct

## Cases with only WithDim

**`UnitExamples.EnergyMassWithDim'`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L58).

> An example of dimensions corresponding to `E = m c^2` using `WithDim`.

```lean
def EnergyMassWithDim' (m : WithDim M𝓭 ℝ) (E : WithDim (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ)
    (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ) : Prop
```

**`UnitExamples.energyMassWithDim'_isDimensionallyCorrect`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L61).

```lean
lemma energyMassWithDim'_isDimensionallyCorrect :
    IsDimensionallyCorrect EnergyMassWithDim'
```

**`UnitExamples.NewtonsSecondWithDim'`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L65).

> An example of dimensions corresponding to `F = m a` using `WithDim`.

```lean
def NewtonsSecondWithDim' (m : WithDim M𝓭 ℝ) (F : WithDim (M𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ)
    (a : WithDim (L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ) : Prop
```

**`UnitExamples.newtonsSecondWithDim'_isDimensionallyCorrect`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L69).

```lean
lemma newtonsSecondWithDim'_isDimensionallyCorrect :
    IsDimensionallyCorrect NewtonsSecondWithDim'
```

**`UnitExamples.SpeedEq`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L73).

> An example of dimensions corresponding to `s = d/t` using `WithDim`.

```lean
def SpeedEq (s : WithDim (L𝓭 * T𝓭⁻¹) ℝ) (d : WithDim L𝓭 ℝ) (t : WithDim T𝓭 ℝ) : Prop
```

**`UnitExamples.speedEq_isDimensionallyCorrect`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L76).

```lean
lemma speedEq_isDimensionallyCorrect : IsDimensionallyCorrect SpeedEq
```

**`UnitExamples.OddDimensions`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L80).

> An example with complicated dimensions.

```lean
def OddDimensions (m1 m2 : WithDim (M𝓭) ℝ)
    (θ : WithDim Θ𝓭 ℝ) (I1 I2 : WithDim (C𝓭/T𝓭) ℝ) (d : WithDim L𝓭 ℝ) (t : WithDim T𝓭 ℝ)
    (X : WithDim (L𝓭 * T𝓭⁻¹ ^ 3 * Θ𝓭⁻¹ * C𝓭 ^2) ℝ) : Prop
```

**`UnitExamples.oddDimensions_isDimensionallyCorrect`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L85).

```lean
lemma oddDimensions_isDimensionallyCorrect : IsDimensionallyCorrect OddDimensions
```

**`UnitExamples.EnergyMassWithDim`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L89).

> An example of dimensions corresponding to `E = m c^2` using `WithDim` with `.val`.

```lean
def EnergyMassWithDim (m : WithDim M𝓭 ℝ) (E : WithDim (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ)
    (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ) : Prop
```

**`UnitExamples.energyMassWithDim_isDimensionallyCorrect`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L93).

```lean
lemma energyMassWithDim_isDimensionallyCorrect : IsDimensionallyCorrect EnergyMassWithDim
```

**`UnitExamples.NewtonsSecondWithDim`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L99).

> An example of dimensions corresponding to `F = m a` using `WithDim` with `.val`.

```lean
def NewtonsSecondWithDim (m : WithDim M𝓭 ℝ) (F : WithDim (M𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ)
    (a : WithDim (L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ) : Prop
```

**`UnitExamples.newtonsSecondWithDim_isDimensionallyCorrect`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L103).

```lean
lemma newtonsSecondWithDim_isDimensionallyCorrect :
    IsDimensionallyCorrect NewtonsSecondWithDim
```

**`UnitExamples.EnergyMassWithDimNot`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L111).

> An example of dimensions corresponding to `E = m c` using `WithDim` with `.val`,
> which is not dimensionally correct.

```lean
def EnergyMassWithDimNot (m : WithDim M𝓭 ℝ) (E : WithDim (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ)
    (c : WithDim (L𝓭 * T𝓭⁻¹) ℝ) : Prop
```

**`UnitExamples.energyMassWithDimNot_not_isDimensionallyCorrect`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L115).

```lean
lemma energyMassWithDimNot_not_isDimensionallyCorrect :
    ¬ IsDimensionallyCorrect EnergyMassWithDimNot
```

## Cases with Dimensionful

**`UnitExamples.EnergyMass`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L132).

> The equation `E = m c^2`, in this equation we `E` and `m` are implicitly in the
> units `u`, while the speed of light is explicitly written in those units.

```lean
def EnergyMass (m : WithDim M𝓭 ℝ) (E : WithDim (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ)
    (u : LTMCTUnitChoices) : Prop
```

**`UnitExamples.EnergyMass'`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L138).

> The equation `E = m c^2`, in this version everything is written explicitly in
> terms of a choice of units.

```lean
def EnergyMass' (m : Dimensionful (WithDim M𝓭 ℝ))
    (E : Dimensionful (WithDim (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ))
    (u : LTMCTUnitChoices) : Prop
```

**`UnitExamples.energyMass_isDimensionallyCorrect`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L144).

> The lemma that the proposition `EnergyMass` is dimensionally correct

```lean
lemma energyMass_isDimensionallyCorrect :
    IsDimensionallyCorrect EnergyMass
```

## Examples of using `isDimensionallyCorrect`

> We now explore the consequences of `energyMass_isDimensionallyCorrect` and how we can use it.

**`UnitExamples.example1_energyMass`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L163).

```lean
lemma example1_energyMass : EnergyMass ⟨2⟩ ⟨2 * 299792458 ^ 2⟩ SI
```

**`UnitExamples.example2_energyMass`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L169).

```lean
lemma example2_energyMass (u : LTMCTUnitChoices) :
    EnergyMass (scaleUnit SI u ⟨2⟩) (scaleUnit SI u ⟨2 * 299792458 ^ 2⟩) u
```

> ## Examples with other functions

**`UnitExamples.CosDim`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L183).

> An example of a dimensionally correct result using functions.

```lean
def CosDim (t : WithDim T𝓭 ℝ) (ω : WithDim T𝓭⁻¹ ℝ) (a : ℝ) : Prop
```

**`UnitExamples.cosDim_isDimensionallyCorrect`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean#L186).

```lean
lemma cosDim_isDimensionallyCorrect : IsDimensionallyCorrect CosDim
```

> ## An example involving derivatives

## Depends on

- [The Speed of Light](../relativity/speedoflight.md)

## Sources

- [Physlib/Units/Examples.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Examples.lean)
