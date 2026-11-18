---
declaration: module
origin: cited
lean: StandardModel.HiggsAlgebraCovRealization.derivSubmodule_le_massWeightSubmodule, StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eq_derivSubmodule, StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eq_iSup_derivSubmodule_mul, StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_two_eq_deriv, StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_four_eq_deriv, StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_six_eq_deriv, StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eight_eq_deriv
statement: formalized
proof: formalized
---

# The mass-weight grading of the Higgs sector, in derivative submodules

The module `PhyslibAlpha.Particles.StandardModel.Realization.HiggsCov.MassWeight.Basic`, [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean): 7 declarations, 7 with a docstring.

## i. Overview

> The mass-weight submodules of the Higgs sector are described in
> `HiggsAlgebraCovRealization.Basic` in terms of the Higgs and conjugate-Higgs submodules
> separately.  Since the two always occur together, the description is cleaner in terms
> of the derivative submodules `derivSubmodule n = higgsSubmodule n ⊔ barHiggsSubmodule n`:
> a Higgs tower with `n` derivatives has mass weight `2 * (1 + n)`, twice its mass dimension
> `1 + n`, only even weights are non-zero, and the mass weights up to eight (mass dimension
> at most four) are the partitions of the weight into such towers.

## ii. Key results

> - `derivSubmodule_le_massWeightSubmodule` : the derivative submodule sits in the mass-weight
>   submodule of weight `2 * (1 + n)`
> - `massWeightSubmodule_eq_derivSubmodule` : the weight recursion, with the single-symbol part
>   written as a derivative submodule
> - `massWeightSubmodule_eq_iSup_derivSubmodule_mul` : removing the leftmost Higgs tower, written with
>   the derivative submodules: a term of positive weight `w` is a sum of products of a tower
>   `derivSubmodule n`, of weight `2 * (1 + n) ≤ w`, with a term of the remaining weight
> - `massWeightSubmodule_two_eq_deriv` : weight two is the underived Higgs symbols

## iv. References

> * None.

## A. The mass-weight grading in derivative submodules

**`StandardModel.HiggsAlgebraCovRealization.derivSubmodule_le_massWeightSubmodule`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean#L66).

> The derivative submodule sits in the mass-weight submodule of weight `2 * (1 + n)`.

```lean
lemma derivSubmodule_le_massWeightSubmodule (n : ℕ) :
    h.derivSubmodule n ≤ h.massWeightSubmodule (2 * (1 + n))
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eq_derivSubmodule`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean#L73).

> The weight recursion, with the single-symbol part written as a derivative
> submodule.

```lean
lemma massWeightSubmodule_eq_derivSubmodule (i : ℕ) (hi : 0 < i) :
    h.massWeightSubmodule i
      = (⨆ k ∈ Finset.univ.filter (fun k : Fin i => 2 * (1 + (k : ℕ)) = i),
          h.derivSubmodule (k : ℕ))
        ⊔ (⨆ p ∈ Finset.univ.filter (fun p : Fin i × Fin i => (p.1 : ℕ) + (p.2 : ℕ) = i),
            h.massWeightSubmodule (p.1 : ℕ) * h.massWeightSubmodule (p.2 : ℕ))
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eq_iSup_derivSubmodule_mul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean#L84).

> Removing the leftmost Higgs tower, written with the derivative submodules: a term of
> positive weight `w` is a sum of products of a tower `derivSubmodule n`, of weight
> `2 * (1 + n) ≤ w`, with a term of the remaining weight.

```lean
lemma massWeightSubmodule_eq_iSup_derivSubmodule_mul (w : ℕ) (hw : 0 < w) :
    h.massWeightSubmodule w
      = ⨆ n ∈ (Finset.range (w + 1)).filter (fun n => 2 * (1 + n) ≤ w),
          h.derivSubmodule n * h.massWeightSubmodule (w - 2 * (1 + n))
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_two_eq_deriv`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean#L91).

> Weight two is the underived Higgs symbols.

```lean
lemma massWeightSubmodule_two_eq_deriv :
    h.massWeightSubmodule 2 = h.derivSubmodule 0
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_four_eq_deriv`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean#L97).

> Weight four: the leftmost tower is underived, leaving weight two, which is an underived
> tower, or once-derived, leaving weight zero.

```lean
lemma massWeightSubmodule_four_eq_deriv :
    h.massWeightSubmodule 4
      = h.derivSubmodule 1 ⊔ h.derivSubmodule 0 * h.derivSubmodule 0
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_six_eq_deriv`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean#L108).

> Weight six: the leftmost tower leaves weight four, two or zero. The product of an
> underived tower with a once-derived one occurs in both orders, which agree by
> `derivSubmodule_mul_comm`.

```lean
lemma massWeightSubmodule_six_eq_deriv :
    h.massWeightSubmodule 6
      = h.derivSubmodule 2 ⊔ h.derivSubmodule 1 * h.derivSubmodule 0
        ⊔ h.derivSubmodule 0 * h.derivSubmodule 0 * h.derivSubmodule 0
```

**`StandardModel.HiggsAlgebraCovRealization.massWeightSubmodule_eight_eq_deriv`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean#L122).

> Weight eight: the leftmost tower leaves weight six, four, two or zero. Products that
> differ only in the order of commuting towers agree by `derivSubmodule_mul_comm`.

```lean
lemma massWeightSubmodule_eight_eq_deriv :
    h.massWeightSubmodule 8
      = h.derivSubmodule 3 ⊔ h.derivSubmodule 2 * h.derivSubmodule 0
        ⊔ h.derivSubmodule 1 * h.derivSubmodule 1
        ⊔ h.derivSubmodule 1 * h.derivSubmodule 0 * h.derivSubmodule 0
        ⊔ h.derivSubmodule 0 * h.derivSubmodule 0 * h.derivSubmodule 0
          * h.derivSubmodule 0
```

## Depends on

- [The derivative submodules of the Higgs sector](realization-higgscov-derivsubmodule-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/HiggsCov/MassWeight/Basic.lean)
