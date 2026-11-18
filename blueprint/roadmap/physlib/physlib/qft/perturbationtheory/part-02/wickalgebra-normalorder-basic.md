---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnListF_eq_zero, FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_eq_zero, FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnOpF_eq_zero_mul, FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnOpF_ofCrAnListF_eq_zero_mul, FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnOpF_eq_zero_mul, FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnListF_eq_zero_mul, FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_eq_zero_mul, FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_eq_zero_mul
statement: formalized
proof: formalized
---

# Normal Ordering on Field operator algebra

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.NormalOrder.Basic`, [Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean): 15 declarations, 1 with a docstring.

## Normal order on super-commutators.

> The main result of this is
> `ι_normalOrderF_superCommuteF_eq_zero_mul`
> which states that applying `ι` to the normal order of something containing a super-commutator
> is zero.

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnListF_eq_zero`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L37).

```lean
lemma ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnListF_eq_zero
    (φa φa' : 𝓕.CrAnFieldOp) (φs φs' : List 𝓕.CrAnFieldOp) :
    ι 𝓝ᶠ(ofCrAnListF φs * [ofCrAnOpF φa, ofCrAnOpF φa']ₛF * ofCrAnListF φs') = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_eq_zero`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L57).

```lean
lemma ι_normalOrderF_superCommuteF_ofCrAnListF_eq_zero
    (φa φa' : 𝓕.CrAnFieldOp) (φs : List 𝓕.CrAnFieldOp)
    (a : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(ofCrAnListF φs * [ofCrAnOpF φa, ofCrAnOpF φa']ₛF * a) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnOpF_eq_zero_mul`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L73).

```lean
lemma ι_normalOrderF_superCommuteF_ofCrAnOpF_eq_zero_mul (φa φa' : 𝓕.CrAnFieldOp)
    (a b : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(a * [ofCrAnOpF φa, ofCrAnOpF φa']ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnOpF_ofCrAnListF_eq_zero_mul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L91).

```lean
lemma ι_normalOrderF_superCommuteF_ofCrAnOpF_ofCrAnListF_eq_zero_mul (φa : 𝓕.CrAnFieldOp)
    (φs : List 𝓕.CrAnFieldOp) (a b : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(a * [ofCrAnOpF φa, ofCrAnListF φs]ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnOpF_eq_zero_mul`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L103).

```lean
lemma ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnOpF_eq_zero_mul (φa : 𝓕.CrAnFieldOp)
    (φs : List 𝓕.CrAnFieldOp) (a b : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(a * [ofCrAnListF φs, ofCrAnOpF φa]ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnListF_eq_zero_mul`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L112).

```lean
lemma ι_normalOrderF_superCommuteF_ofCrAnListF_ofCrAnListF_eq_zero_mul
    (φs φs' : List 𝓕.CrAnFieldOp) (a b : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(a * [ofCrAnListF φs, ofCrAnListF φs']ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_ofCrAnListF_eq_zero_mul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L123).

```lean
lemma ι_normalOrderF_superCommuteF_ofCrAnListF_eq_zero_mul
    (φs : List 𝓕.CrAnFieldOp)
    (a b c : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(a * [ofCrAnListF φs, c]ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_eq_zero_mul`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L141).

```lean
lemma ι_normalOrderF_superCommuteF_eq_zero_mul
    (a b c d : 𝓕.FieldOpFreeAlgebra) : ι 𝓝ᶠ(a * [d, c]ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrder_superCommuteF_eq_zero_mul_right`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L157).

```lean
lemma ι_normalOrder_superCommuteF_eq_zero_mul_right (b c d : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ([d, c]ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_eq_zero_mul_left`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L163).

```lean
lemma ι_normalOrderF_superCommuteF_eq_zero_mul_left (a c d : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(a * [d, c]ₛF) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_eq_zero_mul_mul_right`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L169).

```lean
lemma ι_normalOrderF_superCommuteF_eq_zero_mul_mul_right (a b1 b2 c d: 𝓕.FieldOpFreeAlgebra) :
    ι 𝓝ᶠ(a * [d, c]ₛF * b1 * b2) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_superCommuteF_eq_zero`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L176).

```lean
lemma ι_normalOrderF_superCommuteF_eq_zero (c d : 𝓕.FieldOpFreeAlgebra) : ι 𝓝ᶠ([d, c]ₛF) = 0
```

## Defining normal order for `FiedOpAlgebra`.

**`FieldSpecification.WickAlgebra.ι_normalOrderF_zero_of_mem_ideal`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L186).

```lean
lemma ι_normalOrderF_zero_of_mem_ideal (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet) : ι 𝓝ᶠ(a) = 0
```

**`FieldSpecification.WickAlgebra.ι_normalOrderF_eq_of_equiv`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L219).

```lean
lemma ι_normalOrderF_eq_of_equiv (a b : 𝓕.FieldOpFreeAlgebra) (h : a ≈ b) :
    ι 𝓝ᶠ(a) = ι 𝓝ᶠ(b)
```

**`FieldSpecification.WickAlgebra.normalOrder`**, a def, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean#L235).

> For a field specification `𝓕`, `normalOrder` is the linear map
>
> `WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕`
>
> defined as the descent of `ι ∘ₗ normalOrderF : FieldOpFreeAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕`
> from `FieldOpFreeAlgebra 𝓕` to `WickAlgebra 𝓕`.
> This descent exists because `ι ∘ₗ normalOrderF` is well-defined on equivalence classes.
>
> The notation `𝓝(a)` is used for `normalOrder a` for `a` an element of `WickAlgebra 𝓕`.

```lean
noncomputable def normalOrder : WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕
```

## Depends on

- [Normal Ordering in the FieldOpFreeAlgebra](../part-01/fieldopfreealgebra-normalorder.md)
- [The Wick Algebra](wickalgebra-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Basic.lean)
