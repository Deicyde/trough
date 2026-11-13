---
declaration: module
origin: cited
lean: WickContraction.erase, WickContraction.mem_erase_uncontracted_iff, WickContraction.mem_not_eq_erase_of_isSome, WickContraction.mem_not_eq_erase_of_isNone, WickContraction.getDualErase, WickContraction.getDualErase_isSome_iff_getDual?_isSome, WickContraction.getDualErase_one
statement: formalized
proof: formalized
---

# Erasing an element from a contraction

The module `Physlib.QFT.PerturbationTheory.WickContraction.Erase`, [Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean): 7 declarations, 2 with a docstring.

**`WickContraction.erase`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean#L29).

> Given a Wick contraction `WickContraction n.succ` and a `i : Fin n.succ` the
> Wick contraction associated with `n` obtained by removing `i`.
> If `i` is contracted with `j` in the new Wick contraction `j` will be uncontracted.

```lean
def erase (c : WickContraction n.succ) (i : Fin n.succ) : WickContraction n
```

**`WickContraction.mem_erase_uncontracted_iff`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean#L39).

```lean
lemma mem_erase_uncontracted_iff (c : WickContraction n.succ) (i : Fin n.succ) (j : Fin n) :
    j ∈ (c.erase i).uncontracted ↔
    i.succAbove j ∈ c.uncontracted ∨ c.getDual? (i.succAbove j) = some i
```

**`WickContraction.mem_not_eq_erase_of_isSome`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean#L74).

```lean
lemma mem_not_eq_erase_of_isSome (c : WickContraction n.succ) (i : Fin n.succ)
    (h : (c.getDual? i).isSome) (ha : a ∈ c.1) (ha2 : a ≠ {i, (c.getDual? i).get h}) :
    ∃ a', a' ∈ (c.erase i).1 ∧ a = Finset.map i.succAboveEmb a'
```

**`WickContraction.mem_not_eq_erase_of_isNone`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean#L103).

```lean
lemma mem_not_eq_erase_of_isNone (c : WickContraction n.succ) (i : Fin n.succ)
    (h : (c.getDual? i).isNone) (ha : a ∈ c.1) :
    ∃ a', a' ∈ (c.erase i).1 ∧ a = Finset.map i.succAboveEmb a'
```

**`WickContraction.getDualErase`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean#L134).

> Given a Wick contraction `c : WickContraction n.succ` and a `i : Fin n.succ` the (optional)
> element of `(erase c i).uncontracted` which comes from the element in `c` contracted
> with `i`.

```lean
def getDualErase {n : ℕ} (c : WickContraction n.succ) (i : Fin n.succ) :
    Option ((erase c i).uncontracted)
```

**`WickContraction.getDualErase_isSome_iff_getDual?_isSome`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean#L149).

```lean
lemma getDualErase_isSome_iff_getDual?_isSome (c : WickContraction n.succ) (i : Fin n.succ) :
    (c.getDualErase i).isSome ↔ (c.getDual? i).isSome
```

**`WickContraction.getDualErase_one`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean#L160).

```lean
lemma getDualErase_one (c : WickContraction 1) (i : Fin 1) :
    c.getDualErase i = none
```

## Depends on

- [Fin lemmas](../../../mathematics/formathlib/fin.md)
- [Uncontracted elements](../part-03/wickcontraction-uncontracted.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Erase.lean)
