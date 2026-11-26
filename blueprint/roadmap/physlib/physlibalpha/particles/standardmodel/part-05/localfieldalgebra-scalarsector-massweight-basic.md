---
declaration: module
origin: cited
lean: StandardModel.ScalarSector.derivSubmodule_le_massWeightSubmodule, StandardModel.ScalarSector.massWeightSubmodule_eq_iSup_derivSubmodule_mul, StandardModel.ScalarSector.massWeightSubmodule_two_eq_deriv, StandardModel.ScalarSector.massWeightSubmodule_four_eq_deriv, StandardModel.ScalarSector.massWeightSubmodule_six_eq_deriv, StandardModel.ScalarSector.massWeightSubmodule_eight_eq_deriv
statement: formalized
proof: formalized
---

# The mass-weight grading of the scalar sector, in derivative submodules

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.ScalarSector.MassWeight.Basic`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean): 6 declarations, 6 with a docstring.

> The mass-weight submodules of the scalar sector up to weight eight, written with the derivative
> submodules.

## i. Overview

> The mass-weight submodules of the scalar sector are described in
> `ScalarSector/Basic.lean` in terms of the Higgs and conjugate-Higgs submodules
> separately. Since the two always occur together, the description is cleaner in terms
> of the derivative submodules `derivSubmodule n = higgsSubmodule n ⊔ barHiggsSubmodule n`.
> A Higgs tower with `n` derivatives has mass weight `2 * (1 + n)`, twice its mass dimension
> `1 + n`, only even weights are non-zero, and the mass weights up to eight (mass dimension
> at most four) are the partitions of the weight into such towers.

## ii. Key results

> - `derivSubmodule_le_massWeightSubmodule` : the derivative submodule sits in the mass-weight
>   submodule of weight `2 * (1 + n)`.
> - `massWeightSubmodule_eq_iSup_derivSubmodule_mul` : removing the leftmost Higgs tower, a term
>   of positive weight `w` is a sum of products of a tower `derivSubmodule n`, of weight
>   `2 * (1 + n) ≤ w`, with a term of the remaining weight.
> - `massWeightSubmodule_two_eq_deriv` up to `massWeightSubmodule_eight_eq_deriv` : the mass
>   weights up to eight.

## iv. References

> * None.

## A. The mass-weight grading in derivative submodules

**`StandardModel.ScalarSector.derivSubmodule_le_massWeightSubmodule`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean#L61).

> The derivative submodule sits in the mass-weight submodule of weight `2 * (1 + n)`.

```lean
lemma derivSubmodule_le_massWeightSubmodule (n : ℕ) :
    derivSubmodule n ≤ massWeightSubmodule (2 * (1 + n))
```

**`StandardModel.ScalarSector.massWeightSubmodule_eq_iSup_derivSubmodule_mul`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean#L69).

> Removing the leftmost Higgs tower, written with the derivative submodules. A term of
> positive weight `w` is a sum of products of a tower `derivSubmodule n`, of weight
> `2 * (1 + n) ≤ w`, with a term of the remaining weight.

```lean
lemma massWeightSubmodule_eq_iSup_derivSubmodule_mul (w : ℕ) (hw : 0 < w) :
    massWeightSubmodule w
      = ⨆ n ∈ (Finset.range (w + 1)).filter (fun n => 2 * (1 + n) ≤ w),
          derivSubmodule n * massWeightSubmodule (w - 2 * (1 + n))
```

**`StandardModel.ScalarSector.massWeightSubmodule_two_eq_deriv`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean#L76).

> Weight two is the underived Higgs symbols.

```lean
lemma massWeightSubmodule_two_eq_deriv :
    massWeightSubmodule 2 = derivSubmodule 0
```

**`StandardModel.ScalarSector.massWeightSubmodule_four_eq_deriv`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean#L82).

> Weight four. The leftmost tower is underived, leaving weight two, which is an underived
> tower, or once-derived, leaving weight zero.

```lean
lemma massWeightSubmodule_four_eq_deriv :
    massWeightSubmodule 4
      = derivSubmodule 1 ⊔ derivSubmodule 0 * derivSubmodule 0
```

**`StandardModel.ScalarSector.massWeightSubmodule_six_eq_deriv`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean#L93).

> Weight six. The leftmost tower leaves weight four, two or zero. The product of an
> underived tower with a once-derived one occurs in both orders, which agree by
> `derivSubmodule_mul_comm`.

```lean
lemma massWeightSubmodule_six_eq_deriv :
    massWeightSubmodule 6
      = derivSubmodule 2 ⊔ derivSubmodule 1 * derivSubmodule 0
        ⊔ derivSubmodule 0 * derivSubmodule 0 * derivSubmodule 0
```

**`StandardModel.ScalarSector.massWeightSubmodule_eight_eq_deriv`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean#L110).

> Weight eight. The leftmost tower leaves weight six, four, two or zero. Products that
> differ only in the order of commuting towers agree by `derivSubmodule_mul_comm`.

```lean
lemma massWeightSubmodule_eight_eq_deriv :
    massWeightSubmodule 8
      = derivSubmodule 3 ⊔ derivSubmodule 2 * derivSubmodule 0
        ⊔ derivSubmodule 1 * derivSubmodule 1
        ⊔ derivSubmodule 1 * derivSubmodule 0 * derivSubmodule 0
        ⊔ derivSubmodule 0 * derivSubmodule 0 * derivSubmodule 0
          * derivSubmodule 0
```

## Depends on

- [The derivative submodules of the scalar sector](localfieldalgebra-scalarsector-derivsubmodule-ba.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/ScalarSector/MassWeight/Basic.lean)
