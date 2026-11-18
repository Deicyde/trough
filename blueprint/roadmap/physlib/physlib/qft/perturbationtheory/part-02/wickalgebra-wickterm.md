---
declaration: module
origin: cited
lean: WickContraction.wickTerm, WickContraction.wickTerm_empty_nil, WickContraction.wickTerm_insert_none, WickContraction.wickTerm_insert_some, WickContraction.mul_wickTerm_eq_sum
statement: formalized
proof: formalized
---

# Wick term

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.WickTerm`, [Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean): 5 declarations, 5 with a docstring.

**`WickContraction.wickTerm`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean#L36).

> For a list `φs` of `𝓕.FieldOp`, and a Wick contraction `φsΛ` of `φs`, the element
> of `𝓕.WickAlgebra`, `φsΛ.wickTerm` is defined as
>
> `φsΛ.sign • φsΛ.timeContract * 𝓝([φsΛ]ᵘᶜ)`.
>
> This is a term which appears in the Wick's theorem.

```lean
def wickTerm {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) : 𝓕.WickAlgebra
```

**`WickContraction.wickTerm_empty_nil`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean#L42).

> For the empty list `[]` of `𝓕.FieldOp`, the `wickTerm` of the Wick contraction
> corresponding to the empty set `∅` (the only Wick contraction of `[]`) is `1`.

```lean
lemma wickTerm_empty_nil :
    wickTerm (empty (n := ([] : List 𝓕.FieldOp).length)) = 1
```

**`WickContraction.wickTerm_insert_none`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean#L58).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
>   `𝓕.FieldOp`, and `i ≤ φs.length`, then `(φsΛ ↩Λ φ i none).wickTerm` is equal to
>
> `𝓢(φ, φ₀…φᵢ₋₁) φsΛ.sign • φsΛ.timeContract * 𝓝(φ :: [φsΛ]ᵘᶜ)`
>
> The proof of this result relies on
> - `normalOrder_uncontracted_none` to rewrite normal orderings.
> - `timeContract_insert_none` to rewrite the time contract.
> - `sign_insert_none` to rewrite the sign.

```lean
lemma wickTerm_insert_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (i : Fin φs.length.succ) (φsΛ : WickContraction φs.length) :
    (φsΛ ↩Λ φ i none).wickTerm =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, (Finset.univ.filter (fun k => i.succAbove k < i))⟩)
    • (φsΛ.sign • φsΛ.timeContract * 𝓝(ofFieldOpList (φ :: [φsΛ]ᵘᶜ)))
```

**`WickContraction.wickTerm_insert_some`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean#L119).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
>   `𝓕.FieldOp`, `i ≤ φs.length` and a `k` in `φsΛ.uncontracted`,
>   such that all `𝓕.FieldOp` in `φ₀…φᵢ₋₁` have time strictly less than `φ` and
>   `φ` has a time greater than or equal to all `FieldOp` in `φ₀…φₙ`, then
>   `(φsΛ ↩Λ φ i (some k)).staticWickTerm`
> is equal to the product of
> - the sign `𝓢(φ, φ₀…φᵢ₋₁) `
> - the sign `φsΛ.sign`
> - `φsΛ.timeContract`
> - `s • [anPart φ, ofFieldOp φs[k]]ₛ` where `s` is the sign associated with moving `φ` through
>   uncontracted fields in `φ₀…φₖ₋₁`
> - the normal ordering `[φsΛ]ᵘᶜ` with the field corresponding to `k` removed.
>
> The proof of this result relies on
> - `timeContract_insert_some_of_not_lt`
>   and `timeContract_insert_some_of_lt` to rewrite time
>   contractions.
> - `normalOrder_uncontracted_some` to rewrite normal orderings.
> - `sign_insert_some_of_not_lt` and `sign_insert_some_of_lt` to rewrite signs.

```lean
lemma wickTerm_insert_some (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (i : Fin φs.length.succ) (φsΛ : WickContraction φs.length) (k : φsΛ.uncontracted)
    (hlt : ∀ (k : Fin φs.length), timeOrderRel φ φs[k])
    (hn : ∀ (k : Fin φs.length), i.succAbove k < i → ¬ timeOrderRel φs[k] φ) :
    (φsΛ ↩Λ φ i (some k)).wickTerm =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, (Finset.univ.filter (fun x => i.succAbove x < i))⟩)
    • (φsΛ.sign • (contractStateAtIndex φ [φsΛ]ᵘᶜ
      ((uncontractedFieldOpEquiv φs φsΛ) (some k)) * φsΛ.timeContract)
    * 𝓝(ofFieldOpList (optionEraseZ [φsΛ]ᵘᶜ φ (uncontractedFieldOpEquiv φs φsΛ k))))
```

**`WickContraction.mul_wickTerm_eq_sum`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean#L195).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
>   `𝓕.FieldOp`, and `i ≤ φs.length`
>   such that all `𝓕.FieldOp` in `φ₀…φᵢ₋₁` have time strictly less than `φ` and
>   `φ` has a time greater than or equal to all `FieldOp` in `φ₀…φₙ`, then
>
> `φ * φsΛ.wickTerm = 𝓢(φ, φ₀…φᵢ₋₁) • ∑ k, (φsΛ ↩Λ φ i k).wickTerm`
>
> where the sum is over all `k` in `Option φsΛ.uncontracted`, so `k` is either `none` or `some k`.
>
> The proof proceeds as follows:
> - `ofFieldOp_mul_normalOrder_ofFieldOpList_eq_sum` is used to expand `φ 𝓝([φsΛ]ᵘᶜ)` as
>   a sum over `k` in `Option φsΛ.uncontracted` of terms involving `[anPart φ, φs[k]]ₛ`.
> - Then `wickTerm_insert_none` and `wickTerm_insert_some` are used to equate terms.

```lean
lemma mul_wickTerm_eq_sum (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (i : Fin φs.length.succ)
    (φsΛ : WickContraction φs.length) (hlt : ∀ (k : Fin φs.length), timeOrderRel φ φs[k])
    (hn : ∀ (k : Fin φs.length), i.succAbove k < i → ¬timeOrderRel φs[k] φ) :
    ofFieldOp φ * φsΛ.wickTerm =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, (Finset.univ.filter (fun x => i.succAbove x < i))⟩) •
    ∑ (k : Option φsΛ.uncontracted), (φsΛ ↩Λ φ i k).wickTerm
```

## Depends on

- [Sign associated with a contraction](../part-03/wickcontraction-sign-basic.md)
- [Time contractions (TimeContract)](../part-03/wickcontraction-timecontract.md)

## Proof depends on

- [Normal ordering with relation to Wick contractions](wickalgebra-normalorder-wickcontractions.md)
- [Sign on inserting and not contracting](../part-03/wickcontraction-sign-insertnone.md)
- [Sign on inserting and contracting](../part-03/wickcontraction-sign-insertsome.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WickTerm.lean)
