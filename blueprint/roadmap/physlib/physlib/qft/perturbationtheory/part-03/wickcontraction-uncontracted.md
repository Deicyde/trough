---
declaration: module
origin: cited
lean: WickContraction.uncontracted, WickContraction.congr_uncontracted, WickContraction.getDual?_eq_none_iff_mem_uncontracted, WickContraction.uncontractedCongr, WickContraction.uncontractedCongr_none, WickContraction.uncontractedCongr_some, WickContraction.mem_uncontracted_iff_not_contracted, WickContraction.mem_uncontracted_empty
statement: formalized
proof: formalized
---

# Uncontracted elements

The module `Physlib.QFT.PerturbationTheory.WickContraction.Uncontracted`, [Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean): 12 declarations, 2 with a docstring.

**`WickContraction.uncontracted`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L25).

> For a Wick contraction `c`, `c.uncontracted` is defined as the finset of elements of `Fin n`
> which are not in any contracted pair.

```lean
def uncontracted : Finset (Fin n)
```

**`WickContraction.congr_uncontracted`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L27).

```lean
lemma congr_uncontracted {n m : ℕ} (c : WickContraction n) (h : n = m) :
    (c.congr h).uncontracted = Finset.map (finCongr h).toEmbedding c.uncontracted
```

**`WickContraction.getDual?_eq_none_iff_mem_uncontracted`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L32).

```lean
lemma getDual?_eq_none_iff_mem_uncontracted (i : Fin n) :
    c.getDual? i = none ↔ i ∈ c.uncontracted
```

**`WickContraction.uncontractedCongr`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L37).

> The equivalence of `Option c.uncontracted` for two propositionally equal Wick contractions.

```lean
def uncontractedCongr {c c': WickContraction n} (h : c = c') :
    Option c.uncontracted ≃ Option c'.uncontracted
```

**`WickContraction.uncontractedCongr_none`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L42).

```lean
lemma uncontractedCongr_none {c c': WickContraction n} (h : c = c') :
    (uncontractedCongr h) none = none
```

**`WickContraction.uncontractedCongr_some`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L47).

```lean
lemma uncontractedCongr_some {c c': WickContraction n} (h : c = c') (i : c.uncontracted) :
    (uncontractedCongr h) (some i) = some (Equiv.subtypeEquivRight (by rw [h]; simp) i)
```

**`WickContraction.mem_uncontracted_iff_not_contracted`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L52).

```lean
lemma mem_uncontracted_iff_not_contracted (i : Fin n) :
    i ∈ c.uncontracted ↔ ∀ p ∈ c.1, i ∉ p
```

**`WickContraction.mem_uncontracted_empty`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L79).

```lean
lemma mem_uncontracted_empty (i : Fin n) : i ∈ empty.uncontracted
```

**`WickContraction.getDual?_empty_eq_none`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L85).

```lean
lemma getDual?_empty_eq_none (i : Fin n) : empty.getDual? i = none
```

**`WickContraction.uncontracted_empty`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L89).

```lean
lemma uncontracted_empty {n : ℕ} : (@empty n).uncontracted = Finset.univ
```

**`WickContraction.uncontracted_card_le`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L92).

```lean
lemma uncontracted_card_le (c : WickContraction n) : c.uncontracted.card ≤ n
```

**`WickContraction.uncontracted_card_eq_iff`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean#L97).

```lean
lemma uncontracted_card_eq_iff (c : WickContraction n) :
    c.uncontracted.card = n ↔ c = empty
```

## Depends on

- [Wick contractions](../part-02/wickcontraction-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Uncontracted.lean)
