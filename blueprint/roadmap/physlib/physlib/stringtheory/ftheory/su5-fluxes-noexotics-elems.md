---
declaration: module
origin: cited
lean: FTheory.SU5.FluxesFive.elemsNoExotics, FTheory.SU5.FluxesFive.elemsNoExotics_card, FTheory.SU5.FluxesFive.elemsNoExotics_nodup, FTheory.SU5.FluxesFive.noExotics_of_mem_elemsNoExotics, FTheory.SU5.FluxesFive.toFinset_card_le_four_mem_elemsNoExotics, FTheory.SU5.FluxesFive.card_le_six_mem_elemsNoExotics, FTheory.SU5.FluxesFive.sum_of_mem_elemsNoExotics, FTheory.SU5.FluxesFive.hasNoZero_of_mem_elemsNoExotics
statement: formalized
proof: formalized
---

# Terms of `FluxesFive` and `FluxesTen` with no chiral exotics

The module `Physlib.StringTheory.FTheory.SU5.Fluxes.NoExotics.Elems`, [Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean): 16 declarations, 2 with a docstring.

## i. Overview

> In this module we give the terms of type `FluxesFive` and `FluxesTen`
> which obey the `NoExotics` and `HasNoZero` propositions.
>
> In each case, there is only a finite set of such elements, which we give explicitly.
> We show that these sets are complete in the module
> `StringTheory.FTheory.SU5.Fluxes.NoExotics.Completeness`.
>
> This module is reserved for the explicit sets of elements, and simple lemmas about the
> elements of those elements.

## ii. Key results

> - `FluxesFive.elemsNoExotics` : The multiset of elements of `FluxesFive` which obey `NoExotics`
>   and `HasNoZero`.
> - `FluxesTen.elemsNoExotics` : The multiset of elements of `FluxesTen` which obey `NoExotics`
>   and `HasNoZero`.

## iv. References

> * None.

## A. The multiset sets of `FluxesFive` with no chiral exotics and no zero fluxes

### A.1. The definition of the multiset

**`FTheory.SU5.FluxesFive.elemsNoExotics`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L81).

> The elements of `FluxesFive` for which the `NoExotics` condition holds.

```lean
def elemsNoExotics : Multiset FluxesFive
```

### A.2. The cardinality of the multiset is 31

**`FTheory.SU5.FluxesFive.elemsNoExotics_card`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L111).

```lean
lemma elemsNoExotics_card : elemsNoExotics.card = 31
```

### A.3. The multiset has no duplicates

**`FTheory.SU5.FluxesFive.elemsNoExotics_nodup`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L120).

```lean
lemma elemsNoExotics_nodup : elemsNoExotics.Nodup
```

### A.4. Every element of the multiset obeys `NoExotics`

**`FTheory.SU5.FluxesFive.noExotics_of_mem_elemsNoExotics`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L129).

```lean
lemma noExotics_of_mem_elemsNoExotics (F : FluxesFive) (h : F ∈ elemsNoExotics) :
    NoExotics F
```

### A.5. Every element of the multiset has at most 4 distinct flux pairs

**`FTheory.SU5.FluxesFive.toFinset_card_le_four_mem_elemsNoExotics`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L140).

```lean
lemma toFinset_card_le_four_mem_elemsNoExotics (F : FluxesFive) (h : F ∈ elemsNoExotics) :
    F.toFinset.card ≤ 4
```

### A.6. Every element of the multiset has at most 6 flux pairs

**`FTheory.SU5.FluxesFive.card_le_six_mem_elemsNoExotics`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L151).

```lean
lemma card_le_six_mem_elemsNoExotics (F : FluxesFive) (h : F ∈ elemsNoExotics) :
    F.card ≤ 6
```

### A.7. The sum of all flux-pairs in any element of the multiset is (3, 0)

**`FTheory.SU5.FluxesFive.sum_of_mem_elemsNoExotics`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L162).

```lean
lemma sum_of_mem_elemsNoExotics (F : FluxesFive) (h : F ∈ elemsNoExotics) :
    F.sum = ⟨3, 0⟩
```

### A.8. Every element of the multiset obeys `HasNoZero`

**`FTheory.SU5.FluxesFive.hasNoZero_of_mem_elemsNoExotics`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L173).

```lean
lemma hasNoZero_of_mem_elemsNoExotics (F : FluxesFive) (h : F ∈ elemsNoExotics) :
    F.HasNoZero
```

### A.9. A sum relation for subsets of elements of the multiset

**`FTheory.SU5.FluxesFive.map_sum_add_of_mem_powerset_elemsNoExotics`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L184).

```lean
lemma map_sum_add_of_mem_powerset_elemsNoExotics (F S : FluxesFive)
    (hf : F ∈ FluxesFive.elemsNoExotics)
    (hS: S ∈ Multiset.powerset F) :
    (S.map (fun x => ⟨|x.1|, -|x.1|⟩)).sum +
    (S.map (fun x => ⟨(0 : ℤ), |x.1 + x.2|⟩)).sum = S.sum
```

## B. The multiset sets of `FluxesFive` with no chiral exotics and no zero fluxes

### B.1. The definition of the multiset

**`FTheory.SU5.FluxesTen.elemsNoExotics`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L207).

> The elements of `FluxesTen` for which the `NoExotics` condition holds.

```lean
def elemsNoExotics : Multiset FluxesTen
```

### B.2. The cardinality of the multiset is 6

**`FTheory.SU5.FluxesTen.elemsNoExotics_card`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L218).

```lean
lemma elemsNoExotics_card : elemsNoExotics.card = 6
```

### B.3. The multiset has no duplicates

**`FTheory.SU5.FluxesTen.elemsNoExotics_nodup`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L227).

```lean
lemma elemsNoExotics_nodup : elemsNoExotics.Nodup
```

### B.4. Every element of the multiset obeys `NoExotics`

**`FTheory.SU5.FluxesTen.noExotics_of_mem_elemsNoExotics`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L236).

```lean
lemma noExotics_of_mem_elemsNoExotics (F : FluxesTen) (h : F ∈ elemsNoExotics) :
    NoExotics F
```

### B.5. Every element of the multiset has at most 3 distinct flux pairs

**`FTheory.SU5.FluxesTen.toFinset_card_le_three_mem_elemsNoExotics`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L247).

```lean
lemma toFinset_card_le_three_mem_elemsNoExotics (F : FluxesTen) (h : F ∈ elemsNoExotics) :
    F.toFinset.card ≤ 3
```

### B.6. The sum of all flux-pairs in any element of the multiset is (3, 0)

**`FTheory.SU5.FluxesTen.sum_of_mem_elemsNoExotics`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L258).

```lean
lemma sum_of_mem_elemsNoExotics (F : FluxesTen) (h : F ∈ elemsNoExotics) :
    F.sum = ⟨3, 0⟩
```

### B.7. Every element of the multiset obeys `HasNoZero`

**`FTheory.SU5.FluxesTen.hasNoZero_of_mem_elemsNoExotics`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean#L269).

```lean
lemma hasNoZero_of_mem_elemsNoExotics (F : FluxesTen) (h : F ∈ elemsNoExotics) :
    F.HasNoZero
```

## Depends on

- [Fluxes of representations](su5-fluxes-basic.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Elems.lean)
