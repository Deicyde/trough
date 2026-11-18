---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.normalOrder_uncontracted_none, FieldSpecification.WickAlgebra.normalOrder_uncontracted_some
statement: formalized
proof: formalized
---

# Normal ordering with relation to Wick contractions

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.NormalOrder.WickContractions`, [Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/WickContractions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/WickContractions.lean): 2 declarations, 2 with a docstring.

## Normal order of uncontracted terms within proto-algebra.

**`FieldSpecification.WickAlgebra.normalOrder_uncontracted_none`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/WickContractions.lean#L42).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, and a `i ≤ φs.length`, then the following relation holds:
>
> `𝓝([φsΛ ↩Λ φ i none]ᵘᶜ) = s • 𝓝(φ :: [φsΛ]ᵘᶜ)`
>
> where `s` is the exchange sign for `φ` and the uncontracted fields in `φ₀…φᵢ₋₁`.
>
> The proof of this result ultimately is a consequence of `normalOrder_superCommute_eq_zero`.

```lean
lemma normalOrder_uncontracted_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (i : Fin φs.length.succ) (φsΛ : WickContraction φs.length) :
    𝓝(ofFieldOpList [φsΛ ↩Λ φ i none]ᵘᶜ)
    = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, φsΛ.uncontracted.filter (fun x => i.succAbove x < i)⟩) •
    𝓝(ofFieldOpList (φ :: [φsΛ]ᵘᶜ))
```

**`FieldSpecification.WickAlgebra.normalOrder_uncontracted_some`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/WickContractions.lean#L89).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, a `i ≤ φs.length` and a `k` in `φsΛ.uncontracted`, then
> `𝓝([φsΛ ↩Λ φ i (some k)]ᵘᶜ)` is equal to the normal ordering of `[φsΛ]ᵘᶜ` with the `𝓕.FieldOp`
> corresponding to `k` removed.
>
> The proof of this result ultimately is a consequence of definitions.

```lean
lemma normalOrder_uncontracted_some (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (i : Fin φs.length.succ) (φsΛ : WickContraction φs.length) (k : φsΛ.uncontracted) :
    𝓝(ofFieldOpList [φsΛ ↩Λ φ i (some k)]ᵘᶜ)
    = 𝓝(ofFieldOpList (optionEraseZ [φsΛ]ᵘᶜ φ ((uncontractedFieldOpEquiv φs φsΛ) k)))
```

## Depends on

- [Normal Ordering on Field operator algebra](wickalgebra-normalorder-basic.md)
- [Inserting an element into a contraction based on a list](wickcontraction-insertandcontract.md)

## Proof depends on

- [Basic properties of normal ordering](wickalgebra-normalorder-lemmas.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/WickContractions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/WickContractions.lean)
