---
declaration: module
origin: cited
lean: WickContraction.staticWickTerm, WickContraction.staticWickTerm_empty_nil, WickContraction.staticWickTerm_insert_zero_none, WickContraction.staticWickTerm_insert_zero_some, WickContraction.mul_staticWickTerm_eq_sum
statement: formalized
proof: formalized
---

# Static Wick's terms

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.StaticWickTerm`, [Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean): 5 declarations, 5 with a docstring.

**`WickContraction.staticWickTerm`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean#L36).

> For a list `φs` of `𝓕.FieldOp`, and a Wick contraction `φsΛ` of `φs`, the element
> of `𝓕.WickAlgebra`, `φsΛ.staticWickTerm` is defined as
>
> `φsΛ.sign • φsΛ.staticContract * 𝓝([φsΛ]ᵘᶜ)`.
>
> This is a term which appears in the static version Wick's theorem.

```lean
def staticWickTerm {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) : 𝓕.WickAlgebra
```

**`WickContraction.staticWickTerm_empty_nil`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean#L43).

> For the empty list `[]` of `𝓕.FieldOp`, the `staticWickTerm` of the Wick contraction
> corresponding to the empty set `∅` (the only Wick contraction of `[]`) is `1`.

```lean
lemma staticWickTerm_empty_nil :
    staticWickTerm (empty (n := ([] : List 𝓕.FieldOp).length)) = 1
```

**`WickContraction.staticWickTerm_insert_zero_none`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean#L58).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, and an element `φ` of
>   `𝓕.FieldOp`, then `(φsΛ ↩Λ φ 0 none).staticWickTerm` is equal to
>
> `φsΛ.sign • φsΛ.staticWickTerm * 𝓝(φ :: [φsΛ]ᵘᶜ)`
>
> The proof of this result relies on
> - `staticContract_insert_none` to rewrite the static contract.
> - `sign_insert_none_zero` to rewrite the sign.

```lean
lemma staticWickTerm_insert_zero_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) :
    (φsΛ ↩Λ φ 0 none).staticWickTerm =
    φsΛ.sign • φsΛ.staticContract * 𝓝(ofFieldOpList (φ :: [φsΛ]ᵘᶜ))
```

**`WickContraction.staticWickTerm_insert_zero_some`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean#L80).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
>   `𝓕.FieldOp`, and a `k` in `φsΛ.uncontracted`, `(φsΛ ↩Λ φ 0 (some k)).wickTerm` is equal
>   to the product of
> - the sign `𝓢(φ, φ₀…φᵢ₋₁) `
> - the sign `φsΛ.sign`
> - `φsΛ.staticContract`
> - `s • [anPart φ, ofFieldOp φs[k]]ₛ` where `s` is the sign associated with moving `φ` through
>   uncontracted fields in `φ₀…φₖ₋₁`
> - the normal ordering of `[φsΛ]ᵘᶜ` with the field operator `φs[k]` removed.
>
> The proof of this result ultimately relies on
> - `staticContract_insert_some` to rewrite static contractions.
> - `normalOrder_uncontracted_some` to rewrite normal orderings.
> - `sign_insert_some_zero` to rewrite signs.

```lean
lemma staticWickTerm_insert_zero_some (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (k : { x // x ∈ φsΛ.uncontracted }) :
    (φsΛ ↩Λ φ 0 k).staticWickTerm =
    sign φs φsΛ • (↑φsΛ.staticContract *
    (contractStateAtIndex φ [φsΛ]ᵘᶜ ((uncontractedFieldOpEquiv φs φsΛ) (some k)) *
    𝓝(ofFieldOpList (optionEraseZ [φsΛ]ᵘᶜ φ (uncontractedFieldOpEquiv φs φsΛ k)))))
```

**`WickContraction.mul_staticWickTerm_eq_sum`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean#L127).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, the following relation
> holds
>
> `φ * φsΛ.staticWickTerm = ∑ k, (φsΛ ↩Λ φ 0 k).staticWickTerm`
>
> where the sum is over all `k` in `Option φsΛ.uncontracted`, so `k` is either `none` or `some k`.
>
> The proof proceeds as follows:
> - `ofFieldOp_mul_normalOrder_ofFieldOpList_eq_sum` is used to expand `φ 𝓝([φsΛ]ᵘᶜ)` as
>   a sum over `k` in `Option φsΛ.uncontracted` of terms involving `[anPart φ, φs[k]]ₛ`.
> - Then `staticWickTerm_insert_zero_none` and `staticWickTerm_insert_zero_some` are
>   used to equate terms.

```lean
lemma mul_staticWickTerm_eq_sum (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) :
    ofFieldOp φ * φsΛ.staticWickTerm =
    ∑ (k : Option φsΛ.uncontracted), (φsΛ ↩Λ φ 0 k).staticWickTerm
```

## Depends on

- [Sign associated with a contraction](../part-03/wickcontraction-sign-basic.md)
- [Time contractions](../part-03/wickcontraction-staticcontract.md)

## Proof depends on

- [Normal ordering with relation to Wick contractions](wickalgebra-normalorder-wickcontractions.md)
- [Sign on inserting and not contracting](../part-03/wickcontraction-sign-insertnone.md)
- [Sign on inserting and contracting](../part-03/wickcontraction-sign-insertsome.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTerm.lean)
