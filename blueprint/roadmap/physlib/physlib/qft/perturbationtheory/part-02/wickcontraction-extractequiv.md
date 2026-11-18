---
declaration: module
origin: cited
lean: WickContraction.extractEquiv_equiv, WickContraction.extractEquiv, WickContraction.extractEquiv_symm_none_uncontracted, WickContraction.extractEquiv_apply_congr_symm_apply, WickContraction.fintypeZero, WickContraction.sum_WickContraction_nil, WickContraction.fintypeSucc, WickContraction.sum_extractEquiv_congr
statement: formalized
proof: formalized
---

# Equivalence extracting element from contraction

The module `Physlib.QFT.PerturbationTheory.WickContraction.ExtractEquiv`, [Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean): 10 declarations, 5 with a docstring.

**`WickContraction.extractEquiv_equiv`**, a lemma, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L26).

```lean
lemma extractEquiv_equiv {c1 c2 : (c : WickContraction n) × Option c.uncontracted}
    (h : c1.1 = c2.1) (ho : c1.2 = uncontractedCongr (by rw [h]) c2.2) : c1 = c2
```

**`WickContraction.extractEquiv`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L45).

> The equivalence between `WickContraction n.succ` and the sigma type
> `(c : WickContraction n) × Option c.uncontracted` formed by inserting
> and erasing elements from a contraction.

```lean
def extractEquiv (i : Fin n.succ) : WickContraction n.succ ≃
    (c : WickContraction n) × Option c.uncontracted
```

**`WickContraction.extractEquiv_symm_none_uncontracted`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L58).

```lean
lemma extractEquiv_symm_none_uncontracted (i : Fin n.succ) (c : WickContraction n) :
    ((extractEquiv i).symm ⟨c, none⟩).uncontracted =
    (Insert.insert i (c.uncontracted.map i.succAboveEmb))
```

**`WickContraction.extractEquiv_apply_congr_symm_apply`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L64).

```lean
lemma extractEquiv_apply_congr_symm_apply {n m : ℕ} (k : ℕ)
    (hnk : k < n.succ) (hkm : k < m.succ) (hnm : n = m) (c : WickContraction n)
    (i : c.uncontracted) : congr (by rw [hnm]) ((extractEquiv ⟨k, hkm⟩
    (congr (by rw [hnm]) ((extractEquiv ⟨k, hnk⟩).symm ⟨c, i⟩)))).1 = c
```

**`WickContraction.fintypeZero`**, an instance, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L73).

> The fintype instance of `WickContraction 0` defined through its single
> element `empty`.

```lean
instance fintypeZero : Fintype (WickContraction 0)
```

**`WickContraction.sum_WickContraction_nil`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L89).

```lean
lemma sum_WickContraction_nil (f : WickContraction 0 → M) [AddCommMonoid M] :
    ∑ c, f c = f empty
```

**`WickContraction.fintypeSucc`**, an instance, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L99).

> The fintype instance of `WickContraction n`, for `n.succ` this is defined
> through the equivalence `extractEquiv`.

```lean
instance fintypeSucc : (n : ℕ) → Fintype (WickContraction n)
```

**`WickContraction.sum_extractEquiv_congr`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L105).

```lean
lemma sum_extractEquiv_congr [AddCommMonoid M] {n m : ℕ} (i : Fin n) (f : WickContraction n → M)
    (h : n = m.succ) :
    ∑ c, f c = ∑ (c : WickContraction m), ∑ (k : Option c.uncontracted),
    f (congr h.symm ((extractEquiv (finCongr h i)).symm ⟨c, k⟩))
```

**`WickContraction.mem_three`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L124).

> For `n = 3` there are `4` possible Wick contractions:
>
> - `∅`, corresponding to the case where no fields are contracted.
> - `{{0, 1}}`, corresponding to the case where the field at position `0` and `1` are contracted.
> - `{{0, 2}}`, corresponding to the case where the field at position `0` and `2` are contracted.
> - `{{1, 2}}`, corresponding to the case where the field at position `1` and `2` are contracted.
>
> The proof of this result uses the fact that Lean is an executable programming language
> and can calculate all Wick contractions for a given `n`.

```lean
lemma mem_three (c : WickContraction 3) : c.1 ∈ ({∅, {{0, 1}}, {{0, 2}}, {{1, 2}}} :
    Finset (Finset (Finset (Fin 3))))
```

**`WickContraction.mem_four`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean#L140).

> For `n = 4` there are `10` possible Wick contractions including e.g.
>
> - `∅`, corresponding to the case where no fields are contracted.
> - `{{0, 1}, {2, 3}}`, corresponding to the case where the fields at position `0` and `1` are
>   contracted, and the fields at position `2` and `3` are contracted.
> - `{{0, 2}, {1, 3}}`, corresponding to the case where the fields at position `0` and `2` are
>   contracted, and the fields at position `1` and `3` are contracted.
>
> The proof of this result uses the fact that Lean is an executable programming language
> and can calculate all Wick contractions for a given `n`.

```lean
lemma mem_four (c : WickContraction 4) : c.1 ∈ ({∅,
    {{0, 1}}, {{0, 2}}, {{0, 3}}, {{1, 2}}, {{1, 3}}, {{2,3}},
    {{0, 1}, {2, 3}}, {{0, 2}, {1, 3}}, {{0, 3}, {1, 2}}} :
    Finset (Finset (Finset (Fin 4))))
```

## Depends on

- [Inserting an element into a contraction](wickcontraction-insertandcontractnat.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/ExtractEquiv.lean)
