---
declaration: module
origin: cited
lean: WickContraction.insertAndContractNat, WickContraction.insertAndContractNat_of_isSome, WickContraction.self_mem_uncontracted_of_insertAndContractNat_none, WickContraction.self_not_mem_uncontracted_of_insertAndContractNat_some, WickContraction.insertAndContractNat_succAbove_mem_uncontracted_iff, WickContraction.mem_uncontracted_insertAndContractNat_none_iff, WickContraction.insertAndContractNat_none_uncontracted, WickContraction.mem_uncontracted_insertAndContractNat_some_iff
statement: formalized
proof: formalized
---

# Inserting an element into a contraction

The module `Physlib.QFT.PerturbationTheory.WickContraction.InsertAndContractNat`, [Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean): 35 declarations, 3 with a docstring.

## Inserting an element into a contraction

**`WickContraction.insertAndContractNat`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L35).

> Given a Wick contraction `c` for `n`, a position `i : Fin n.succ` and
> an optional uncontracted element `j : Option (c.uncontracted)` of `c`.
> The Wick contraction for `n.succ` formed by 'inserting' `i` into `Fin n`
> and contracting it optionally with `j`.

```lean
def insertAndContractNat (c : WickContraction n) (i : Fin n.succ) (j : Option (c.uncontracted)) :
    WickContraction n.succ
```

**`WickContraction.insertAndContractNat_of_isSome`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L130).

```lean
lemma insertAndContractNat_of_isSome (c : WickContraction n) (i : Fin n.succ)
    (j : Option c.uncontracted) (hj : j.isSome) :
    (insertAndContractNat c i j).1 = Insert.insert {i, i.succAbove (j.get hj)}
    (Finset.map (Finset.mapEmbedding i.succAboveEmb).toEmbedding c.1)
```

**`WickContraction.self_mem_uncontracted_of_insertAndContractNat_none`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L138).

```lean
lemma self_mem_uncontracted_of_insertAndContractNat_none (c : WickContraction n) (i : Fin n.succ) :
    i ∈ (insertAndContractNat c i none).uncontracted
```

**`WickContraction.self_not_mem_uncontracted_of_insertAndContractNat_some`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L158).

```lean
lemma self_not_mem_uncontracted_of_insertAndContractNat_some (c : WickContraction n)
    (i : Fin n.succ) (j : c.uncontracted) :
    i ∉ (insertAndContractNat c i (some j)).uncontracted
```

**`WickContraction.insertAndContractNat_succAbove_mem_uncontracted_iff`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L165).

```lean
lemma insertAndContractNat_succAbove_mem_uncontracted_iff (c : WickContraction n) (i : Fin n.succ)
    (j : Fin n) :
    (i.succAbove j) ∈ (insertAndContractNat c i none).uncontracted ↔ j ∈ c.uncontracted
```

**`WickContraction.mem_uncontracted_insertAndContractNat_none_iff`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L171).

```lean
lemma mem_uncontracted_insertAndContractNat_none_iff (c : WickContraction n) (i : Fin n.succ)
    (k : Fin n.succ) : k ∈ (insertAndContractNat c i none).uncontracted ↔
    k = i ∨ ∃ j, k = i.succAbove j ∧ j ∈ c.uncontracted
```

**`WickContraction.insertAndContractNat_none_uncontracted`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L178).

```lean
lemma insertAndContractNat_none_uncontracted (c : WickContraction n) (i : Fin n.succ) :
    (insertAndContractNat c i none).uncontracted =
    Insert.insert i (c.uncontracted.map i.succAboveEmb)
```

**`WickContraction.mem_uncontracted_insertAndContractNat_some_iff`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L185).

```lean
lemma mem_uncontracted_insertAndContractNat_some_iff (c : WickContraction n) (i : Fin n.succ)
    (k : Fin n.succ) (j : c.uncontracted) :
    k ∈ (insertAndContractNat c i (some j)).uncontracted ↔
    ∃ z, k = i.succAbove z ∧ z ∈ c.uncontracted ∧ z ≠ j
```

**`WickContraction.insertAndContractNat_some_uncontracted`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L235).

```lean
lemma insertAndContractNat_some_uncontracted (c : WickContraction n) (i : Fin n.succ)
    (j : c.uncontracted) :
    (insertAndContractNat c i (some j)).uncontracted =
    (c.uncontracted.erase j).map i.succAboveEmb
```

## Insert and getDual?

**`WickContraction.insertAndContractNat_none_getDual?_isNone`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L250).

```lean
lemma insertAndContractNat_none_getDual?_isNone (c : WickContraction n) (i : Fin n.succ) :
    ((insertAndContractNat c i none).getDual? i).isNone
```

**`WickContraction.insertAndContractNat_none_getDual?_eq_none`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L255).

```lean
lemma insertAndContractNat_none_getDual?_eq_none (c : WickContraction n) (i : Fin n.succ) :
    (insertAndContractNat c i none).getDual? i = none
```

**`WickContraction.insertAndContractNat_succAbove_getDual?_eq_none_iff`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L261).

```lean
lemma insertAndContractNat_succAbove_getDual?_eq_none_iff (c : WickContraction n) (i : Fin n.succ)
    (j : Fin n) :
    (insertAndContractNat c i none).getDual? (i.succAbove j) = none ↔ c.getDual? j = none
```

**`WickContraction.insertAndContractNat_succAbove_getDual?_isSome_iff`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L267).

```lean
lemma insertAndContractNat_succAbove_getDual?_isSome_iff (c : WickContraction n) (i : Fin n.succ)
    (j : Fin n) :
    ((insertAndContractNat c i none).getDual? (i.succAbove j)).isSome ↔ (c.getDual? j).isSome
```

**`WickContraction.insertAndContractNat_succAbove_getDual?_get`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L273).

```lean
lemma insertAndContractNat_succAbove_getDual?_get (c : WickContraction n) (i : Fin n.succ)
    (j : Fin n) (h : ((insertAndContractNat c i none).getDual? (i.succAbove j)).isSome) :
    ((insertAndContractNat c i none).getDual? (i.succAbove j)).get h =
    i.succAbove ((c.getDual? j).get (by simpa using h))
```

**`WickContraction.insertAndContractNat_some_getDual?_eq`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L284).

```lean
lemma insertAndContractNat_some_getDual?_eq (c : WickContraction n) (i : Fin n.succ)
    (j : c.uncontracted) :
    (insertAndContractNat c i (some j)).getDual? i = some (i.succAbove j)
```

**`WickContraction.insertAndContractNat_some_getDual?_ne_none`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L290).

```lean
lemma insertAndContractNat_some_getDual?_ne_none (c : WickContraction n) (i : Fin n.succ)
    (j : c.uncontracted) (k : Fin n) (hkj : k ≠ j.1) :
    (insertAndContractNat c i (some j)).getDual? (i.succAbove k) = none ↔ c.getDual? k = none
```

**`WickContraction.insertAndContractNat_some_getDual?_ne_isSome`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L295).

```lean
lemma insertAndContractNat_some_getDual?_ne_isSome (c : WickContraction n) (i : Fin n.succ)
    (j : c.uncontracted) (k : Fin n) (hkj : k ≠ j.1) :
    ((insertAndContractNat c i (some j)).getDual? (i.succAbove k)).isSome ↔
    (c.getDual? k).isSome
```

**`WickContraction.insertAndContractNat_some_getDual?_ne_isSome_get`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L301).

```lean
lemma insertAndContractNat_some_getDual?_ne_isSome_get (c : WickContraction n) (i : Fin n.succ)
    (j : c.uncontracted) (k : Fin n) (hkj : k ≠ j.1)
    (h : ((insertAndContractNat c i (some j)).getDual? (i.succAbove k)).isSome) :
    ((insertAndContractNat c i (some j)).getDual? (i.succAbove k)).get h =
    i.succAbove ((c.getDual? k).get
      (by simpa [hkj, insertAndContractNat_some_getDual?_ne_isSome] using h))
```

**`WickContraction.insertAndContractNat_some_getDual?_of_neq`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L315).

```lean
lemma insertAndContractNat_some_getDual?_of_neq (c : WickContraction n) (i : Fin n.succ)
    (j : c.uncontracted) (k : Fin n) (hkj : k ≠ j.1) :
    (insertAndContractNat c i (some j)).getDual? (i.succAbove k) =
    Option.map i.succAbove (c.getDual? k)
```

## Interaction with erase.

**`WickContraction.insertAndContractNat_erase`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L334).

```lean
lemma insertAndContractNat_erase (c : WickContraction n) (i : Fin n.succ)
    (j : Option c.uncontracted) : erase (insertAndContractNat c i j) i = c
```

**`WickContraction.insertAndContractNat_getDualErase`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L347).

```lean
lemma insertAndContractNat_getDualErase (c : WickContraction n) (i : Fin n.succ)
    (j : Option c.uncontracted) : (insertAndContractNat c i j).getDualErase i =
    uncontractedCongr (c := c) (c' := (c.insertAndContractNat i j).erase i) (by simp) j
```

**`WickContraction.erase_insert`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L365).

```lean
lemma erase_insert (c : WickContraction n.succ) (i : Fin n.succ) :
    insertAndContractNat (erase c i) i (getDualErase c i) = c
```

**`WickContraction.insertLift`**, a def, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L410).

> Lifts a contraction in `c` to a contraction in `(c.insert i j)`.

```lean
def insertLift {c : WickContraction n} (i : Fin n.succ) (j : Option (c.uncontracted))
    (a : c.1) : (c.insertAndContractNat i j).1
```

**`WickContraction.insertLift_injective`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L426).

```lean
lemma insertLift_injective {c : WickContraction n} (i : Fin n.succ) (j : Option (c.uncontracted)) :
    Function.Injective (insertLift i j)
```

**`WickContraction.insertLift_none_surjective`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L430).

```lean
lemma insertLift_none_surjective {c : WickContraction n} (i : Fin n.succ) :
    Function.Surjective (c.insertLift i none)
```

**`WickContraction.insertLift_none_bijective`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L436).

```lean
lemma insertLift_none_bijective {c : WickContraction n} (i : Fin n.succ) :
    Function.Bijective (c.insertLift i none)
```

**`WickContraction.insertAndContractNat_fstFieldOfContract`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L441).

```lean
lemma insertAndContractNat_fstFieldOfContract (c : WickContraction n) (i : Fin n.succ)
    (j : Option (c.uncontracted)) (a : c.1) :
    (c.insertAndContractNat i j).fstFieldOfContract (insertLift i j a) =
      i.succAbove (c.fstFieldOfContract a)
```

**`WickContraction.insertAndContractNat_sndFieldOfContract`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L452).

```lean
lemma insertAndContractNat_sndFieldOfContract (c : WickContraction n) (i : Fin n.succ)
    (j : Option (c.uncontracted)) (a : c.1) :
    (c.insertAndContractNat i j).sndFieldOfContract (insertLift i j a) =
    i.succAbove (c.sndFieldOfContract a)
```

**`WickContraction.insertLiftSome`**, a def, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L465).

> Given a contracted pair for a Wick contraction `WickContraction n`, the
> corresponding contracted pair of a wick contraction `(c.insert i (some j))` formed
> by inserting an element `i` into the contraction.

```lean
def insertLiftSome {c : WickContraction n} (i : Fin n.succ) (j : c.uncontracted)
    (a : Unit ⊕ c.1) : (c.insertAndContractNat i (some j)).1
```

**`WickContraction.insertLiftSome_injective`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L472).

```lean
lemma insertLiftSome_injective {c : WickContraction n} (i : Fin n.succ) (j : c.uncontracted) :
    Function.Injective (insertLiftSome i j)
```

**`WickContraction.insertLiftSome_surjective`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L484).

```lean
lemma insertLiftSome_surjective {c : WickContraction n} (i : Fin n.succ) (j : c.uncontracted) :
    Function.Surjective (insertLiftSome i j)
```

**`WickContraction.insertLiftSome_bijective`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L492).

```lean
lemma insertLiftSome_bijective {c : WickContraction n} (i : Fin n.succ) (j : c.uncontracted) :
    Function.Bijective (insertLiftSome i j)
```

## insertAndContractNat c i none and injection

**`WickContraction.insertAndContractNat_injective`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L502).

```lean
lemma insertAndContractNat_injective (i : Fin n.succ) :
    Function.Injective (fun c => insertAndContractNat c i none)
```

**`WickContraction.insertAndContractNat_surjective_on_nodual`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L506).

```lean
lemma insertAndContractNat_surjective_on_nodual (i : Fin n.succ)
    (c : WickContraction n.succ) (hc : c.getDual? i = none) :
    ∃ c', insertAndContractNat c' i none = c
```

**`WickContraction.insertAndContractNat_bijective`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean#L512).

```lean
lemma insertAndContractNat_bijective (i : Fin n.succ) :
    Function.Bijective (fun c => (⟨insertAndContractNat c i none, by simp⟩ :
      {c : WickContraction n.succ // c.getDual? i = none}))
```

## Depends on

- [Erasing an element from a contraction](wickcontraction-erase.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContractNat.lean)
