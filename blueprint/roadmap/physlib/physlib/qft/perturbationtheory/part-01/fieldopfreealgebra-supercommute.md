---
declaration: module
origin: cited
lean: FieldSpecification.FieldOpFreeAlgebra.superCommuteF, FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofCrAnListF, FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnOpF_ofCrAnOpF, FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofFieldOpFsList, FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofFieldOpListF_ofFieldOpFsList, FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofFieldOpF_ofFieldOpFsList, FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofFieldOpListF_ofFieldOpF, FieldSpecification.FieldOpFreeAlgebra.superCommuteF_anPartF_crPartF
statement: formalized
proof: formalized
---

# Super Commute

The module `Physlib.QFT.PerturbationTheory.FieldOpFreeAlgebra.SuperCommute`, [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean): 49 declarations, 2 with a docstring.

## The super commutator on the FieldOpFreeAlgebra.

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L37).

> For a field specification `𝓕`, the super commutator `superCommuteF` is defined as the linear
> map `𝓕.FieldOpFreeAlgebra →ₗ[ℂ] 𝓕.FieldOpFreeAlgebra →ₗ[ℂ] 𝓕.FieldOpFreeAlgebra`
> which on the lists `φs` and `φs'` of `𝓕.CrAnFieldOp` gives
>
> `superCommuteF φs φs' = φs * φs' - 𝓢(φs, φs') • φs' * φs`.
>
> The notation `[a, b]ₛF` can be used for `superCommuteF a b`.

```lean
noncomputable def superCommuteF : 𝓕.FieldOpFreeAlgebra →ₗ[ℂ] 𝓕.FieldOpFreeAlgebra →ₗ[ℂ]
    𝓕.FieldOpFreeAlgebra
```

## The super commutator of different types of elements

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofCrAnListF`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L52).

```lean
lemma superCommuteF_ofCrAnListF_ofCrAnListF (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnListF φs, ofCrAnListF φs']ₛF =
    ofCrAnListF (φs ++ φs') - 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofCrAnListF (φs' ++ φs)
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnOpF_ofCrAnOpF`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L57).

```lean
lemma superCommuteF_ofCrAnOpF_ofCrAnOpF (φ φ' : 𝓕.CrAnFieldOp) :
    [ofCrAnOpF φ, ofCrAnOpF φ']ₛF =
    ofCrAnOpF φ * ofCrAnOpF φ' - 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • ofCrAnOpF φ' * ofCrAnOpF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofFieldOpFsList`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L64).

```lean
lemma superCommuteF_ofCrAnListF_ofFieldOpFsList (φcas : List 𝓕.CrAnFieldOp) (φs : List 𝓕.FieldOp) :
    [ofCrAnListF φcas, ofFieldOpListF φs]ₛF = ofCrAnListF φcas * ofFieldOpListF φs -
    𝓢(𝓕 |>ₛ φcas, 𝓕 |>ₛ φs) • ofFieldOpListF φs * ofCrAnListF φcas
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofFieldOpListF_ofFieldOpFsList`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L77).

```lean
lemma superCommuteF_ofFieldOpListF_ofFieldOpFsList (φ : List 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [ofFieldOpListF φ, ofFieldOpListF φs]ₛF = ofFieldOpListF φ * ofFieldOpListF φs -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • ofFieldOpListF φs * ofFieldOpListF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofFieldOpF_ofFieldOpFsList`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L89).

```lean
lemma superCommuteF_ofFieldOpF_ofFieldOpFsList (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [ofFieldOpF φ, ofFieldOpListF φs]ₛF = ofFieldOpF φ * ofFieldOpListF φs -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • ofFieldOpListF φs * ofFieldOpF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofFieldOpListF_ofFieldOpF`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L96).

```lean
lemma superCommuteF_ofFieldOpListF_ofFieldOpF (φs : List 𝓕.FieldOp) (φ : 𝓕.FieldOp) :
    [ofFieldOpListF φs, ofFieldOpF φ]ₛF = ofFieldOpListF φs * ofFieldOpF φ -
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φ) • ofFieldOpF φ * ofFieldOpListF φs
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_anPartF_crPartF`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L104).

```lean
lemma superCommuteF_anPartF_crPartF (φ φ' : 𝓕.FieldOp) :
    [anPartF φ, crPartF φ']ₛF = anPartF φ * crPartF φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • crPartF φ' * anPartF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_crPartF_anPartF`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L127).

```lean
lemma superCommuteF_crPartF_anPartF (φ φ' : 𝓕.FieldOp) :
    [crPartF φ, anPartF φ']ₛF = crPartF φ * anPartF φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • anPartF φ' * crPartF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_crPartF_crPartF`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L150).

```lean
lemma superCommuteF_crPartF_crPartF (φ φ' : 𝓕.FieldOp) :
    [crPartF φ, crPartF φ']ₛF = crPartF φ * crPartF φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • crPartF φ' * crPartF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_anPartF_anPartF`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L173).

```lean
lemma superCommuteF_anPartF_anPartF (φ φ' : 𝓕.FieldOp) :
    [anPartF φ, anPartF φ']ₛF =
    anPartF φ * anPartF φ' - 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • anPartF φ' * anPartF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_crPartF_ofFieldOpListF`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L195).

```lean
lemma superCommuteF_crPartF_ofFieldOpListF (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [crPartF φ, ofFieldOpListF φs]ₛF =
    crPartF φ * ofFieldOpListF φs - 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • ofFieldOpListF φs *
    crPartF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_anPartF_ofFieldOpListF`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L210).

```lean
lemma superCommuteF_anPartF_ofFieldOpListF (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [anPartF φ, ofFieldOpListF φs]ₛF =
    anPartF φ * ofFieldOpListF φs - 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) •
    ofFieldOpListF φs * anPartF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_crPartF_ofFieldOpF`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L224).

```lean
lemma superCommuteF_crPartF_ofFieldOpF (φ φ' : 𝓕.FieldOp) :
    [crPartF φ, ofFieldOpF φ']ₛF =
    crPartF φ * ofFieldOpF φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • ofFieldOpF φ' * crPartF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_anPartF_ofFieldOpF`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L231).

```lean
lemma superCommuteF_anPartF_ofFieldOpF (φ φ' : 𝓕.FieldOp) :
    [anPartF φ, ofFieldOpF φ']ₛF =
    anPartF φ * ofFieldOpF φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • ofFieldOpF φ' * anPartF φ
```

## Mul equal superCommuteF

> Lemmas which rewrite a multiplication of two elements of the algebra as their commuted
> multiplication with a sign plus the super commutator.

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_mul_ofCrAnListF_eq_superCommuteF`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L246).

```lean
lemma ofCrAnListF_mul_ofCrAnListF_eq_superCommuteF (φs φs' : List 𝓕.CrAnFieldOp) :
    ofCrAnListF φs * ofCrAnListF φs' = 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofCrAnListF φs' * ofCrAnListF φs
    + [ofCrAnListF φs, ofCrAnListF φs']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnOpF_mul_ofCrAnListF_eq_superCommuteF`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L252).

```lean
lemma ofCrAnOpF_mul_ofCrAnListF_eq_superCommuteF (φ : 𝓕.CrAnFieldOp) (φs' : List 𝓕.CrAnFieldOp) :
    ofCrAnOpF φ * ofCrAnListF φs' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs') • ofCrAnListF φs' * ofCrAnOpF φ
    + [ofCrAnOpF φ, ofCrAnListF φs']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.ofFieldOpListF_mul_ofFieldOpListF_eq_superCommuteF`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L258).

```lean
lemma ofFieldOpListF_mul_ofFieldOpListF_eq_superCommuteF (φs φs' : List 𝓕.FieldOp) :
    ofFieldOpListF φs * ofFieldOpListF φs' =
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofFieldOpListF φs' * ofFieldOpListF φs
    + [ofFieldOpListF φs, ofFieldOpListF φs']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.ofFieldOpF_mul_ofFieldOpListF_eq_superCommuteF`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L265).

```lean
lemma ofFieldOpF_mul_ofFieldOpListF_eq_superCommuteF (φ : 𝓕.FieldOp) (φs' : List 𝓕.FieldOp) :
    ofFieldOpF φ * ofFieldOpListF φs' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs') • ofFieldOpListF φs' * ofFieldOpF φ
    + [ofFieldOpF φ, ofFieldOpListF φs']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.ofFieldOpListF_mul_ofFieldOpF_eq_superCommuteF`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L270).

```lean
lemma ofFieldOpListF_mul_ofFieldOpF_eq_superCommuteF (φs : List 𝓕.FieldOp) (φ : 𝓕.FieldOp) :
    ofFieldOpListF φs * ofFieldOpF φ = 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φ) • ofFieldOpF φ * ofFieldOpListF φs
    + [ofFieldOpListF φs, ofFieldOpF φ]ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.crPartF_mul_anPartF_eq_superCommuteF`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L275).

```lean
lemma crPartF_mul_anPartF_eq_superCommuteF (φ φ' : 𝓕.FieldOp) :
    crPartF φ * anPartF φ' =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • anPartF φ' * crPartF φ +
    [crPartF φ, anPartF φ']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.anPartF_mul_crPartF_eq_superCommuteF`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L282).

```lean
lemma anPartF_mul_crPartF_eq_superCommuteF (φ φ' : 𝓕.FieldOp) :
    anPartF φ * crPartF φ' =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') •
    crPartF φ' * anPartF φ +
    [anPartF φ, crPartF φ']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.crPartF_mul_crPartF_eq_superCommuteF`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L290).

```lean
lemma crPartF_mul_crPartF_eq_superCommuteF (φ φ' : 𝓕.FieldOp) :
    crPartF φ * crPartF φ' =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • crPartF φ' * crPartF φ +
    [crPartF φ, crPartF φ']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.anPartF_mul_anPartF_eq_superCommuteF`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L297).

```lean
lemma anPartF_mul_anPartF_eq_superCommuteF (φ φ' : 𝓕.FieldOp) :
    anPartF φ * anPartF φ' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • anPartF φ' * anPartF φ +
    [anPartF φ, anPartF φ']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_mul_ofFieldOpListF_eq_superCommuteF`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L303).

```lean
lemma ofCrAnListF_mul_ofFieldOpListF_eq_superCommuteF (φs : List 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.FieldOp) : ofCrAnListF φs * ofFieldOpListF φs' =
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofFieldOpListF φs' * ofCrAnListF φs
    + [ofCrAnListF φs, ofFieldOpListF φs']ₛF
```

## Symmetry of the super commutator.

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofCrAnListF_symm`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L316).

```lean
lemma superCommuteF_ofCrAnListF_ofCrAnListF_symm (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnListF φs, ofCrAnListF φs']ₛF =
    (- 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs')) • [ofCrAnListF φs', ofCrAnListF φs]ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnOpF_ofCrAnOpF_symm`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L328).

```lean
lemma superCommuteF_ofCrAnOpF_ofCrAnOpF_symm (φ φ' : 𝓕.CrAnFieldOp) :
    [ofCrAnOpF φ, ofCrAnOpF φ']ₛF =
    (- 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ')) • [ofCrAnOpF φ', ofCrAnOpF φ]ₛF
```

## Splitting the super commutator on lists into sums.

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofCrAnListF_cons`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L346).

```lean
lemma superCommuteF_ofCrAnListF_ofCrAnListF_cons (φ : 𝓕.CrAnFieldOp) (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnListF φs, ofCrAnListF (φ :: φs')]ₛF =
    [ofCrAnListF φs, ofCrAnOpF φ]ₛF * ofCrAnListF φs' +
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φ)
    • ofCrAnOpF φ * [ofCrAnListF φs, ofCrAnListF φs']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofFieldOpListF_cons`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L367).

```lean
lemma superCommuteF_ofCrAnListF_ofFieldOpListF_cons (φ : 𝓕.FieldOp) (φs : List 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.FieldOp) : [ofCrAnListF φs, ofFieldOpListF (φ :: φs')]ₛF =
    [ofCrAnListF φs, ofFieldOpF φ]ₛF * ofFieldOpListF φs' +
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φ) • ofFieldOpF φ * [ofCrAnListF φs, ofFieldOpListF φs']ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofCrAnListF_eq_sum`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L395).

> For a field specification `𝓕`, and two lists `φs = φ₀…φₙ` and `φs'` of `𝓕.CrAnFieldOp`
> the following super commutation relation holds:
>
> `[φs', φ₀…φₙ]ₛF = ∑ i, 𝓢(φs', φ₀…φᵢ₋₁) • φ₀…φᵢ₋₁ * [φs', φᵢ]ₛF * φᵢ₊₁ … φₙ`
>
> The proof of this relation is via induction on the length of `φs`.

```lean
lemma superCommuteF_ofCrAnListF_ofCrAnListF_eq_sum (φs : List 𝓕.CrAnFieldOp) :
    (φs' : List 𝓕.CrAnFieldOp) → [ofCrAnListF φs, ofCrAnListF φs']ₛF =
    ∑ (n : Fin φs'.length), 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs'.take n) •
    ofCrAnListF (φs'.take n) * [ofCrAnListF φs, ofCrAnOpF (φs'.get n)]ₛF *
    ofCrAnListF (φs'.drop (n + 1))
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofFieldOpListF_eq_sum`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L412).

```lean
lemma superCommuteF_ofCrAnListF_ofFieldOpListF_eq_sum (φs : List 𝓕.CrAnFieldOp) :
    (φs' : List 𝓕.FieldOp) →
    [ofCrAnListF φs, ofFieldOpListF φs']ₛF =
    ∑ (n : Fin φs'.length), 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs'.take n) •
      ofFieldOpListF (φs'.take n) * [ofCrAnListF φs, ofFieldOpF (φs'.get n)]ₛF *
      ofFieldOpListF (φs'.drop (n + 1))
```

**`FieldSpecification.FieldOpFreeAlgebra.summerCommute_jacobi_ofCrAnListF`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L430).

```lean
lemma summerCommute_jacobi_ofCrAnListF (φs1 φs2 φs3 : List 𝓕.CrAnFieldOp) :
    [ofCrAnListF φs1, [ofCrAnListF φs2, ofCrAnListF φs3]ₛF]ₛF =
    𝓢(𝓕 |>ₛ φs1, 𝓕 |>ₛ φs3) •
    (- 𝓢(𝓕 |>ₛ φs2, 𝓕 |>ₛ φs3) • [ofCrAnListF φs3, [ofCrAnListF φs1, ofCrAnListF φs2]ₛF]ₛF -
    𝓢(𝓕 |>ₛ φs1, 𝓕 |>ₛ φs2) • [ofCrAnListF φs2, [ofCrAnListF φs3, ofCrAnListF φs1]ₛF]ₛF)
```

## Interaction with grading.

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_grade`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L453).

```lean
lemma superCommuteF_grade {a b : 𝓕.FieldOpFreeAlgebra} {f1 f2 : FieldStatistic}
    (ha : a ∈ statisticSubmodule f1) (hb : b ∈ statisticSubmodule f2) :
    [a, b]ₛF ∈ statisticSubmodule (f1 + f2)
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_bosonic_bosonic`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L494).

```lean
lemma superCommuteF_bosonic_bosonic {a b : 𝓕.FieldOpFreeAlgebra}
    (ha : a ∈ statisticSubmodule bosonic) (hb : b ∈ statisticSubmodule bosonic) :
    [a, b]ₛF = a * b - b * a
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_bosonic_fermionic`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L525).

```lean
lemma superCommuteF_bosonic_fermionic {a b : 𝓕.FieldOpFreeAlgebra}
    (ha : a ∈ statisticSubmodule bosonic) (hb : b ∈ statisticSubmodule fermionic) :
    [a, b]ₛF = a * b - b * a
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_fermionic_bonsonic`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L556).

```lean
lemma superCommuteF_fermionic_bonsonic {a b : 𝓕.FieldOpFreeAlgebra}
    (ha : a ∈ statisticSubmodule fermionic) (hb : b ∈ statisticSubmodule bosonic) :
    [a, b]ₛF = a * b - b * a
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_bonsonic`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L587).

```lean
lemma superCommuteF_bonsonic {a b : 𝓕.FieldOpFreeAlgebra} (hb : b ∈ statisticSubmodule bosonic) :
    [a, b]ₛF = a * b - b * a
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonic_superCommuteF`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L595).

```lean
lemma bosonic_superCommuteF {a b : 𝓕.FieldOpFreeAlgebra} (ha : a ∈ statisticSubmodule bosonic) :
    [a, b]ₛF = a * b - b * a
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_bonsonic_symm`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L603).

```lean
lemma superCommuteF_bonsonic_symm {a b : 𝓕.FieldOpFreeAlgebra}
    (hb : b ∈ statisticSubmodule bosonic) :
    [a, b]ₛF = - [b, a]ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.bonsonic_superCommuteF_symm`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L609).

```lean
lemma bonsonic_superCommuteF_symm {a b : 𝓕.FieldOpFreeAlgebra}
    (ha : a ∈ statisticSubmodule bosonic) :
    [a, b]ₛF = - [b, a]ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_fermionic_fermionic`**, a lemma, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L615).

```lean
lemma superCommuteF_fermionic_fermionic {a b : 𝓕.FieldOpFreeAlgebra}
    (ha : a ∈ statisticSubmodule fermionic) (hb : b ∈ statisticSubmodule fermionic) :
    [a, b]ₛF = a * b + b * a
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_fermionic_fermionic_symm`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L646).

```lean
lemma superCommuteF_fermionic_fermionic_symm {a b : 𝓕.FieldOpFreeAlgebra}
    (ha : a ∈ statisticSubmodule fermionic) (hb : b ∈ statisticSubmodule fermionic) :
    [a, b]ₛF = [b, a]ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_expand_bosonicProjF_fermionicProjF`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L653).

```lean
lemma superCommuteF_expand_bosonicProjF_fermionicProjF (a b : 𝓕.FieldOpFreeAlgebra) :
    [a, b]ₛF = bosonicProjF a * bosonicProjF b - bosonicProjF b * bosonicProjF a +
    bosonicProjF a * fermionicProjF b - fermionicProjF b * bosonicProjF a +
    fermionicProjF a * bosonicProjF b - bosonicProjF b * fermionicProjF a +
    fermionicProjF a * fermionicProjF b + fermionicProjF b * fermionicProjF a
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnListF_ofCrAnListF_bosonic_or_fermionic`**, a lemma, [line 666](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L666).

```lean
lemma superCommuteF_ofCrAnListF_ofCrAnListF_bosonic_or_fermionic (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnListF φs, ofCrAnListF φs']ₛF ∈ statisticSubmodule bosonic ∨
    [ofCrAnListF φs, ofCrAnListF φs']ₛF ∈ statisticSubmodule fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_ofCrAnOpF_ofCrAnOpF_bosonic_or_fermionic`**, a lemma, [line 687](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L687).

```lean
lemma superCommuteF_ofCrAnOpF_ofCrAnOpF_bosonic_or_fermionic (φ φ' : 𝓕.CrAnFieldOp) :
    [ofCrAnOpF φ, ofCrAnOpF φ']ₛF ∈ statisticSubmodule bosonic ∨
    [ofCrAnOpF φ, ofCrAnOpF φ']ₛF ∈ statisticSubmodule fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_superCommuteF_ofCrAnOpF_bosonic_or_fermionic`**, a lemma, [line 693](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L693).

```lean
lemma superCommuteF_superCommuteF_ofCrAnOpF_bosonic_or_fermionic (φ1 φ2 φ3 : 𝓕.CrAnFieldOp) :
    [ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF ∈ statisticSubmodule bosonic ∨
    [ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF ∈ statisticSubmodule fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_bosonic_ofCrAnListF_eq_sum`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L711).

```lean
lemma superCommuteF_bosonic_ofCrAnListF_eq_sum (a : 𝓕.FieldOpFreeAlgebra) (φs : List 𝓕.CrAnFieldOp)
    (ha : a ∈ statisticSubmodule bosonic) :
    [a, ofCrAnListF φs]ₛF = ∑ (n : Fin φs.length),
      ofCrAnListF (φs.take n) * [a, ofCrAnOpF (φs.get n)]ₛF *
      ofCrAnListF (φs.drop (n + 1))
```

**`FieldSpecification.FieldOpFreeAlgebra.superCommuteF_fermionic_ofCrAnListF_eq_sum`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L740).

```lean
lemma superCommuteF_fermionic_ofCrAnListF_eq_sum (a : 𝓕.FieldOpFreeAlgebra)
    (φs : List 𝓕.CrAnFieldOp) (ha : a ∈ statisticSubmodule fermionic) :
    [a, ofCrAnListF φs]ₛF = ∑ (n : Fin φs.length), 𝓢(fermionic, 𝓕 |>ₛ φs.take n) •
      ofCrAnListF (φs.take n) * [a, ofCrAnOpF (φs.get n)]ₛF *
      ofCrAnListF (φs.drop (n + 1))
```

**`FieldSpecification.FieldOpFreeAlgebra.statistic_ne_of_superCommuteF_fermionic`**, a lemma, [line 774](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean#L774).

```lean
lemma statistic_ne_of_superCommuteF_fermionic {φs φs' : List 𝓕.CrAnFieldOp}
    (h : [ofCrAnListF φs, ofCrAnListF φs']ₛF ∈ statisticSubmodule fermionic) :
    (𝓕 |>ₛ φs) ≠ (𝓕 |>ₛ φs') ∨ [ofCrAnListF φs, ofCrAnListF φs']ₛF = 0
```

## Depends on

- [Grading on the FieldOpFreeAlgebra](fieldopfreealgebra-grading.md)
- [Exchange sign for field statistics](fieldstatistics-exchangesign.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/SuperCommute.lean)
