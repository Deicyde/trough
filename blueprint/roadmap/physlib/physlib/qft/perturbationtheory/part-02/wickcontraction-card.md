---
declaration: module
origin: cited
lean: WickContraction.card_eq_cardFun, WickContraction.wickContraction_card_eq_sum_zero_none_isSome, WickContraction.wickContraction_zero_none_card, WickContraction.wickContraction_zero_some_eq_sum, WickContraction.finset_succAbove_succ_disjoint, WickContraction.consAddContract, WickContraction.consAddContract_getDual?_zero, WickContraction.consAddContract_getDual?_self_succ
statement: formalized
proof: formalized
---

# Cardinality of Wick contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.Card`, [Physlib/QFT/PerturbationTheory/WickContraction/Card.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean): 14 declarations, 3 with a docstring, 1 listed as significant.

**`WickContraction.wickContraction_card_eq_sum_zero_none_isSome`**, a lemma, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L24).

```lean
lemma wickContraction_card_eq_sum_zero_none_isSome : Fintype.card (WickContraction n.succ)
    = Fintype.card {c : WickContraction n.succ // ¬ (c.getDual? 0).isSome} +
    Fintype.card {c : WickContraction n.succ // (c.getDual? 0).isSome}
```

**`WickContraction.wickContraction_zero_none_card`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L33).

```lean
lemma wickContraction_zero_none_card :
    Fintype.card {c : WickContraction n.succ // ¬ (c.getDual? 0).isSome} =
    Fintype.card (WickContraction n)
```

**`WickContraction.wickContraction_zero_some_eq_sum`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L41).

```lean
lemma wickContraction_zero_some_eq_sum :
    Fintype.card {c : WickContraction n.succ // (c.getDual? 0).isSome} =
    ∑ i, Fintype.card {c : WickContraction n.succ // (c.getDual? 0).isSome ∧
      ∀ (h : (c.getDual? 0).isSome), (c.getDual? 0).get h = Fin.succ i}
```

**`WickContraction.finset_succAbove_succ_disjoint`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L59).

```lean
lemma finset_succAbove_succ_disjoint (a : Finset (Fin n)) (i : Fin n.succ) :
    Disjoint ((Finset.map (Fin.succEmb (n + 1))) ((Finset.map i.succAboveEmb) a)) {0, i.succ}
```

**`WickContraction.consAddContract`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L70).

> The Wick contraction in `WickContraction n.succ.succ` formed by a Wick contraction
> `WickContraction n` by inserting at the `0` and `i.succ` and contracting these two.

```lean
def consAddContract (i : Fin n.succ) (c : WickContraction n) :
    WickContraction n.succ.succ
```

**`WickContraction.consAddContract_getDual?_zero`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L112).

```lean
lemma consAddContract_getDual?_zero (i : Fin n.succ) (c : WickContraction n) :
    (consAddContract i c).getDual? 0 = some i.succ
```

**`WickContraction.consAddContract_getDual?_self_succ`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L118).

```lean
lemma consAddContract_getDual?_self_succ (i : Fin n.succ) (c : WickContraction n) :
    (consAddContract i c).getDual? i.succ = some 0
```

**`WickContraction.mem_consAddContract_of_mem_iff`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L123).

```lean
lemma mem_consAddContract_of_mem_iff (i : Fin n.succ) (c : WickContraction n) (a : Finset (Fin n)) :
    a ∈ c.1 ↔ (a.map i.succAboveEmb).map (Fin.succEmb n.succ) ∈ (consAddContract i c).1
```

**`WickContraction.consAddContract_injective`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L144).

```lean
lemma consAddContract_injective (i : Fin n.succ) : Function.Injective (consAddContract i)
```

**`WickContraction.consAddContract_surjective_on_zero_contract`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L162).

```lean
lemma consAddContract_surjective_on_zero_contract (i : Fin n.succ)
    (c : WickContraction n.succ.succ)
    (h : (c.getDual? 0).isSome) (h2 : (c.getDual? 0).get h = i.succ) :
    ∃ c', consAddContract i c' = c
```

**`WickContraction.consAddContract_bijection`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L211).

```lean
lemma consAddContract_bijection (i : Fin n.succ) :
    Function.Bijective (fun c => (⟨(consAddContract i c), by simp⟩ :
    {c : WickContraction n.succ.succ // (c.getDual? 0).isSome ∧
      ∀ (h : (c.getDual? 0).isSome), (c.getDual? 0).get h = Fin.succ i}))
```

**`WickContraction.wickContraction_zero_some_eq_mul`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L224).

```lean
lemma wickContraction_zero_some_eq_mul :
    Fintype.card {c : WickContraction n.succ.succ // (c.getDual? 0).isSome} =
    (n + 1) * Fintype.card (WickContraction n)
```

**`WickContraction.cardFun`**, a def, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L235).

> The cardinality of Wick's contractions as a recursive formula.
> This corresponds to OEIS:A000085.

```lean
def cardFun : ℕ → ℕ
```

**`WickContraction.card_eq_cardFun`**, a theorem, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean#L243). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The number of Wick contractions in `WickContraction n` is equal to the terms in
> Online Encyclopedia of Integer Sequences (OEIS) A000085. That is:
> 1, 1, 2, 4, 10, 26, 76, 232, 764, 2620, 9496, ...

```lean
theorem card_eq_cardFun : (n : ℕ) → Fintype.card (WickContraction n) = cardFun n
```

## Depends on

- [Equivalence extracting element from contraction](wickcontraction-extractequiv.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Card.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Card.lean)
