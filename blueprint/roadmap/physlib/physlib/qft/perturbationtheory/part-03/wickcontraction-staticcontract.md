---
declaration: module
origin: cited
lean: WickContraction.staticContract, WickContraction.staticContract_insert_none, WickContraction.staticContract_insert_some, WickContraction.staticContract_insert_some_of_lt, WickContraction.staticContract_of_not_gradingCompliant
statement: formalized
proof: formalized
---

# Time contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.StaticContract`, [Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean): 5 declarations, 3 with a docstring.

**`WickContraction.staticContract`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean#L30).

> For a list `φs` of `𝓕.FieldOp` and a Wick contraction `φsΛ`, the
> element of the center of `𝓕.WickAlgebra`, `φsΛ.staticContract` is defined as the product
> of `[anPart φs[j], φs[k]]ₛ` over contracted pairs `{j, k}` in `φsΛ`
> with `j < k`.

```lean
noncomputable def staticContract {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) :
    Subalgebra.center ℂ 𝓕.WickAlgebra
```

**`WickContraction.staticContract_insert_none`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean#L45).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, and a `i ≤ φs.length`, then the following relation holds:
>
> `(φsΛ ↩Λ φ i none).staticContract = φsΛ.staticContract`
>
> The proof of this result ultimately is a consequence of definitions.

```lean
lemma staticContract_insert_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) :
    (φsΛ ↩Λ φ i none).staticContract = φsΛ.staticContract
```

**`WickContraction.staticContract_insert_some`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean#L61).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp`, a `i ≤ φs.length` and a `k` in `φsΛ.uncontracted`, then
> `(φsΛ ↩Λ φ i (some k)).staticContract` is equal to the product of
> - `[anPart φ, φs[k]]ₛ` if `i ≤ k` or `[anPart φs[k], φ]ₛ` if `k < i`
> - `φsΛ.staticContract`.
>
> The proof of this result ultimately is a consequence of definitions.

```lean
lemma staticContract_insert_some
    (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    (φsΛ ↩Λ φ i (some j)).staticContract =
    (if i < i.succAbove j then
      ⟨[anPart φ, ofFieldOp φs[j.1]]ₛ, superCommute_anPart_ofFieldOp_mem_center _ _⟩
    else ⟨[anPart φs[j.1], ofFieldOp φ]ₛ, superCommute_anPart_ofFieldOp_mem_center _ _⟩) *
    φsΛ.staticContract
```

**`WickContraction.staticContract_insert_some_of_lt`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean#L80).

```lean
lemma staticContract_insert_some_of_lt
    (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (k : φsΛ.uncontracted)
    (hik : i < i.succAbove k) :
    (φsΛ ↩Λ φ i (some k)).staticContract =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, (φsΛ.uncontracted.filter (fun x => x < k))⟩)
    • (contractStateAtIndex φ [φsΛ]ᵘᶜ ((uncontractedFieldOpEquiv φs φsΛ) (some k)) *
      φsΛ.staticContract)
```

**`WickContraction.staticContract_of_not_gradingCompliant`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean#L105).

```lean
lemma staticContract_of_not_gradingCompliant (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (h : ¬ GradingCompliant φs φsΛ) :
    φsΛ.staticContract = 0
```

## Depends on

- [Basic properties of normal ordering](../part-02/wickalgebra-normalorder-lemmas.md)
- [Inserting an element into a contraction based on a list](../part-02/wickcontraction-insertandcontract.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/StaticContract.lean)
