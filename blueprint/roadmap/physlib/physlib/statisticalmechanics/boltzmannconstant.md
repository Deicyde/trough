---
declaration: module
origin: cited
lean: BoltzmannConstant, BoltzmannConstant.instPositiveRealUnitCore, BoltzmannConstant.positiveRealUnitCore_val, BoltzmannConstant.val_pos, BoltzmannConstant.val_nonneg, BoltzmannConstant.val_ne_zero, BoltzmannConstant.instHasDim, boltzmannConstant
statement: formalized
proof: formalized
---

# Boltzmann constant

The module `Physlib.StatisticalMechanics.BoltzmannConstant`, [Physlib/StatisticalMechanics/BoltzmannConstant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean): 12 declarations (2 instances with no name), 3 with a docstring.

> The Boltzmann constant, in the format of `Physlib/Units/Constants.lean`.

## i. Overview

> The Boltzmann constant, named after Ludwig Boltzmann, has the dimension `M L² T⁻² Θ⁻¹` of an energy
> over a temperature, and its value in SI units is exact. Section F adds the instance of one.

## ii. Key results

> - `BoltzmannConstant` : The Boltzmann constant in a chosen but arbitrary system of units.
> - `boltzmannConstant` : The Boltzmann constant in our world, `1.380649 × 10⁻²³ J K⁻¹`.

## iv. References

> * The defining value of the Boltzmann constant. [ref: bipm\_si\_brochure\_2019]

## A. The type

**`BoltzmannConstant`**, a structure, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L50).

> The Boltzmann constant, in a chosen but arbitrary system of units.

```lean
structure BoltzmannConstant where
  /-- The underlying value of the Boltzmann constant. -/
  val : ℝ
  pos : 0 < val
```

## B. Instances

**`BoltzmannConstant.instPositiveRealUnitCore`**, an instance, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L63).

```lean
instance instPositiveRealUnitCore : PositiveRealUnitCore BoltzmannConstant
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L70).

```lean
instance : Coe BoltzmannConstant ℝ
```

**`BoltzmannConstant.positiveRealUnitCore_val`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L73).

```lean
lemma positiveRealUnitCore_val (kB : BoltzmannConstant) :
    PositiveRealUnitCore.val kB = kB.val
```

## C. Positivity

**`BoltzmannConstant.val_pos`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L83).

```lean
lemma val_pos (kB : BoltzmannConstant) : 0 < (kB : ℝ)
```

**`BoltzmannConstant.val_nonneg`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L86).

```lean
lemma val_nonneg (kB : BoltzmannConstant) : 0 ≤ (kB : ℝ)
```

**`BoltzmannConstant.val_ne_zero`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L89).

```lean
lemma val_ne_zero (kB : BoltzmannConstant) : (kB : ℝ) ≠ 0
```

## D. The dimension

**`BoltzmannConstant.instHasDim`**, an instance, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L98).

> The Boltzmann constant has the dimension `M L² T⁻² Θ⁻¹`.

```lean
instance instHasDim : HasDim BoltzmannConstant
```

## E. The value in our world

**`boltzmannConstant`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L110).

> The Boltzmann constant in our world, `1.380649 × 10⁻²³ J K⁻¹`, exact.

```lean
noncomputable def boltzmannConstant : Dimensionful BoltzmannConstant
```

**`boltzmannConstant_in_SI`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L114).

```lean
lemma boltzmannConstant_in_SI : boltzmannConstant SI = ⟨1.380649e-23, by norm_num⟩
```

## F. Specific to the Boltzmann constant

> The Boltzmann constant equal to `1`, for units in which it is one.

**An instance with no name**, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L127).

```lean
instance : One BoltzmannConstant
```

**`BoltzmannConstant.val_one`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean#L130).

```lean
lemma val_one : (1 : BoltzmannConstant).val = 1
```

## Depends on

- [Dimensions and unit](../units/basic.md)

## Sources

- [Physlib/StatisticalMechanics/BoltzmannConstant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StatisticalMechanics/BoltzmannConstant.lean)
