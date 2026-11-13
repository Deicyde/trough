---
declaration: module
origin: cited
lean: WickContraction.timeContract, WickContraction.timeContract_insert_none, WickContraction.timeContract_insertAndContract_some, WickContraction.timeContract_empty, WickContraction.timeContract_insert_some_of_lt, WickContraction.timeContract_insert_some_of_not_lt, WickContraction.timeContract_of_not_gradingCompliant
statement: formalized
proof: formalized
---

# Time contractions (TimeContract)

The module `Physlib.QFT.PerturbationTheory.WickContraction.TimeContract`, [Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean): 7 declarations, 5 with a docstring.

**`WickContraction.timeContract`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean#L30).

> For a list `φs` of `𝓕.FieldOp` and a Wick contraction `φsΛ` the
> element of the center of `𝓕.WickAlgebra`, `φsΛ.timeContract` is defined as the product
> of `timeContract φs[j] φs[k]` over contracted pairs `{j, k}` in `φsΛ`
> with `j < k`.

```lean
noncomputable def timeContract {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) :
    Subalgebra.center ℂ 𝓕.WickAlgebra
```

**`WickContraction.timeContract_insert_none`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean#L44).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, and a `i ≤ φs.length` the following relation holds
>
> `(φsΛ ↩Λ φ i none).timeContract = φsΛ.timeContract`
>
> The proof of this result ultimately is a consequence of definitions.

```lean
lemma timeContract_insert_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) :
    (φsΛ ↩Λ φ i none).timeContract = φsΛ.timeContract
```

**`WickContraction.timeContract_insertAndContract_some`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean#L59).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, a `i ≤ φs.length` and a `k` in `φsΛ.uncontracted`, then
> `(φsΛ ↩Λ φ i (some k)).timeContract` is equal to the product of
> - `timeContract φ φs[k]` if `i ≤ k` or `timeContract φs[k] φ` if `k < i`
> - `φsΛ.timeContract`.
>
> The proof of this result ultimately is a consequence of definitions.

```lean
lemma timeContract_insertAndContract_some
    (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    (φsΛ ↩Λ φ i (some j)).timeContract =
    (if i < i.succAbove j then
      ⟨WickAlgebra.timeContract φ φs[j.1], timeContract_mem_center _ _⟩
    else ⟨WickAlgebra.timeContract φs[j.1] φ, timeContract_mem_center _ _⟩) *
    φsΛ.timeContract
```

**`WickContraction.timeContract_empty`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean#L79).

```lean
lemma timeContract_empty (φs : List 𝓕.FieldOp) :
    (@empty φs.length).timeContract = 1
```

**`WickContraction.timeContract_insert_some_of_lt`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean#L98).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, a `i ≤ φs.length` and a `k` in `φsΛ.uncontracted` such that `i ≤ k`, with the
> condition that `φ` has greater or equal time to `φs[k]`, then
> `(φsΛ ↩Λ φ i (some k)).timeContract` is equal to the product of
> - `[anPart φ, φs[k]]ₛ`
> - `φsΛ.timeContract`
> - two copies of the exchange sign of `φ` with the uncontracted fields in `φ₀…φₖ₋₁`.
>   These two exchange signs cancel each other out but are included for convenience.
>
> The proof of this result ultimately is a consequence of definitions and
> `timeContract_of_timeOrderRel`.

```lean
lemma timeContract_insert_some_of_lt
    (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (k : φsΛ.uncontracted)
    (ht : 𝓕.timeOrderRel φ φs[k.1]) (hik : i < i.succAbove k) :
    (φsΛ ↩Λ φ i (some k)).timeContract =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, (φsΛ.uncontracted.filter (fun x => x < k))⟩)
    • (contractStateAtIndex φ [φsΛ]ᵘᶜ ((uncontractedFieldOpEquiv φs φsΛ) (some k)) *
      φsΛ.timeContract)
```

**`WickContraction.timeContract_insert_some_of_not_lt`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean#L143).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, a `i ≤ φs.length` and a `k` in `φsΛ.uncontracted` such that `k < i`, with the
> condition that `φs[k]` does not have time greater or equal to `φ`, then
> `(φsΛ ↩Λ φ i (some k)).timeContract` is equal to the product of
> - `[anPart φ, φs[k]]ₛ`
> - `φsΛ.timeContract`
> - the exchange sign of `φ` with the uncontracted fields in `φ₀…φₖ₋₁`.
> - the exchange sign of `φ` with the uncontracted fields in `φ₀…φₖ`.
>
> The proof of this result ultimately is a consequence of definitions and
> `timeContract_of_not_timeOrderRel_expand`.

```lean
lemma timeContract_insert_some_of_not_lt
    (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (k : φsΛ.uncontracted)
    (ht : ¬ 𝓕.timeOrderRel φs[k.1] φ) (hik : ¬ i < i.succAbove k) :
    (φsΛ ↩Λ φ i (some k)).timeContract =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, (φsΛ.uncontracted.filter (fun x => x ≤ k))⟩)
    • (contractStateAtIndex φ [φsΛ]ᵘᶜ
      ((uncontractedFieldOpEquiv φs φsΛ) (some k)) * φsΛ.timeContract)
```

**`WickContraction.timeContract_of_not_gradingCompliant`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean#L195).

```lean
lemma timeContract_of_not_gradingCompliant (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (h : ¬ GradingCompliant φs φsΛ) :
    φsΛ.timeContract = 0
```

## Depends on

- [Basic properties of normal ordering](../part-02/wickalgebra-normalorder-lemmas.md)
- [Time contractions (TimeContraction)](../part-02/wickalgebra-timecontraction.md)
- [Inserting an element into a contraction based on a list](../part-02/wickcontraction-insertandcontract.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/TimeContract.lean)
