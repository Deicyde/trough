---
declaration: module
origin: cited
lean: FTheory.SU5.FluxesFive.mem_mem_finset_of_noExotics, FTheory.SU5.FluxesFive.subset_le_mem_of_card_eq_succ, FTheory.SU5.FluxesFive.noExoticsSubsets, FTheory.SU5.FluxesFive.subset_of_fluxesFive_mem_noExoticsSubsets_of_noExotics, FTheory.SU5.FluxesFive.card_le_six_of_noExotics, FTheory.SU5.FluxesFive.card_mem_range_seven_of_noExotics, FTheory.SU5.FluxesFive.mem_elemsNoExotics_of_noExotics, FTheory.SU5.FluxesFive.noExotics_iff_mem_elemsNoExotics
statement: formalized
proof: formalized
---

# Completeness of `Elems` with regard to the `NoExotics` condition

The module `Physlib.StringTheory.FTheory.SU5.Fluxes.NoExotics.Completeness`, [Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean): 16 declarations, 4 with a docstring.

## i. Overview

> In the module:
>
> - `Physlib.StringTheory.FTheory.SU5.Fluxes.NoExotics.Elems`
>
> we define finite sets of elements of `FluxesFive` and `FluxesTen` which satisfy the
> `NoExotics` and `HasNoZero` conditions.
>
> In this module we prove that these sets are complete, in the sense that every
> element of `FluxesFive` or `FluxesTen` which satisfies the `NoExotics` and
> `HasNoZero` conditions is contained in them.
>
> Our proof follows by building allowed subsets of fluxes by their cardinality, and heavily relies
> on the `decide` tactic.
>
> Note that the `10d` fluxes are much more constrained than the 5-bar fluxes. This is because
> they are constrained by `3` SM representations `Q`, `U`, and `E`, whereas the 5-bar fluxes
> are only constrained by `2` SM representations `D` and `L`.

## ii. Key results

> - `FluxesFive.noExotics_iff_mem_elemsNoExotics` : An element of `FluxesFive` satisfies `NoExotics`
>   and `HasNoZero` if and only if it is an element of `elemsNoExotics`.
> - `FluxesTen.noExotics_iff_mem_elemsNoExotics` : An element of `FluxesTen` satisfies `NoExotics`
>   and `HasNoZero` if and only if it is an element of `elemsNoExotics`.

## iv. References

> * None.

## A. All terms of `FluxesFive` obeying `NoExotics` and `HasNoZero`

### A.1. The allowed fluxes in a `FluxesFive` which obeys `NoExotics` and `HasNoZero`

**`FTheory.SU5.FluxesFive.mem_mem_finset_of_noExotics`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L83).

```lean
lemma mem_mem_finset_of_noExotics (F : FluxesFive) (hF : F.NoExotics)
    (hnZ : F.HasNoZero) (x : Fluxes) (hx : x ∈ F) :
    x ∈ ({⟨0, 1⟩, ⟨0, 2⟩, ⟨0, 3⟩, ⟨1, -1⟩, ⟨1, 0⟩, ⟨1, 1⟩, ⟨1, 2⟩,
      ⟨2, -2⟩, ⟨2, -1⟩, ⟨2, 0⟩, ⟨2, 1⟩, ⟨3, -3⟩, ⟨3, -2⟩, ⟨3, -1⟩, ⟨3, 0⟩} : Finset Fluxes)
```

### A.2. Sufficient condition for a set to contain allowed subsets of card `n.succ` based on `n`

**`FTheory.SU5.FluxesFive.subset_le_mem_of_card_eq_succ`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L112).

```lean
lemma subset_le_mem_of_card_eq_succ {n : ℕ} {F : FluxesFive} (hF : F.NoExotics) (hnZ : F.HasNoZero)
    (S : Multiset Fluxes) (hcard : S.card = n.succ) (hS : S ≤ F) {Y X : Finset (Multiset Fluxes)}
    (hY : ∀ (S : Multiset Fluxes), S.card = n → S ≤ F → S ∈ Y)
    (hX : ∀ a ∈ ({⟨0, 1⟩, ⟨0, 2⟩, ⟨0, 3⟩, ⟨1, -1⟩, ⟨1, 0⟩, ⟨1, 1⟩, ⟨1, 2⟩,
      ⟨2, -2⟩, ⟨2, -1⟩, ⟨2, 0⟩, ⟨2, 1⟩, ⟨3, -3⟩, ⟨3, -2⟩, ⟨3, -1⟩, ⟨3, 0⟩} : Finset Fluxes),
      ∀ y ∈ Y,
      (Multiset.map (fun x => x.M + x.N) (a ::ₘ y)).sum ≤ 3 →
      (Multiset.map (fun x => x.M) (a ::ₘ y)).sum ≤ 3 →
      a ::ₘ y ∈ X) :
    S ∈ X
```

### A.3. Statement of the allowed subsets of each cardinality

**`FTheory.SU5.FluxesFive.noExoticsSubsets`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L141).

> The allowed subsets of a `FluxesFive` which has no exotics or zeros.

```lean
def noExoticsSubsets : (n : ℕ) → Finset (Multiset Fluxes)
```

### A.4. Lemma that stated allowed subsets are complete

**`FTheory.SU5.FluxesFive.subset_of_fluxesFive_mem_noExoticsSubsets_of_noExotics`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L190).

```lean
lemma subset_of_fluxesFive_mem_noExoticsSubsets_of_noExotics {F : FluxesFive} (hF : F.NoExotics)
    (hnZ : F.HasNoZero) (S : Multiset Fluxes) (hS : S ≤ F) :
    S ∈ noExoticsSubsets S.card
```

### A.5. Terms of `FluxesFive` obeying `NoExotics` and `HasNoZero` have card ≤ 6

**`FTheory.SU5.FluxesFive.card_le_six_of_noExotics`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L222).

```lean
lemma card_le_six_of_noExotics {F : FluxesFive} (hF : F.NoExotics) (hnZ : F.HasNoZero) :
    F.card ≤ 6
```

**`FTheory.SU5.FluxesFive.card_mem_range_seven_of_noExotics`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L237).

```lean
lemma card_mem_range_seven_of_noExotics {F : FluxesFive} (hF : F.NoExotics) (hnZ : F.HasNoZero) :
    F.card ∈ Finset.range 7
```

### A.6. Terms of `FluxesFive` obeying `NoExotics` and `HasNoZero` are in `elemsNoExotics`

**`FTheory.SU5.FluxesFive.mem_elemsNoExotics_of_noExotics`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L248).

```lean
lemma mem_elemsNoExotics_of_noExotics (F : FluxesFive) (hNE : F.NoExotics) (hnZ : F.HasNoZero) :
    F ∈ elemsNoExotics
```

### A.7. Terms of `FluxesFive` obey `NoExotics` and `HasNoZero` if and only if in `elemsNoExotics`

**`FTheory.SU5.FluxesFive.noExotics_iff_mem_elemsNoExotics`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L273).

> Completeness of `elemsNoExotics`, that is, every element of `FluxesFive`
> which obeys `NoExotics` is an element of `elemsNoExotics`, and every
> element of `elemsNoExotics` obeys `NoExotics`.

```lean
lemma noExotics_iff_mem_elemsNoExotics (F : FluxesFive) :
    F.NoExotics ∧ F.HasNoZero ↔ F ∈ elemsNoExotics
```

## B. All terms of `FluxesTen` obeying `NoExotics` and `HasNoZero`

### B.1. The allowed fluxes in a `FluxesTen` which obeys `NoExotics` and `HasNoZero`

**`FTheory.SU5.FluxesTen.mem_mem_finset_of_noExotics`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L295).

```lean
lemma mem_mem_finset_of_noExotics (F : FluxesTen) (hF : F.NoExotics) (hnZ : F.HasNoZero)
    (x : Fluxes) (hx : x ∈ F) :
    x ∈ ({⟨1, -1⟩, ⟨1, 0⟩, ⟨1, 1⟩, ⟨2, -1⟩, ⟨2, 0⟩, ⟨2, 1⟩, ⟨3, 0⟩} : Finset Fluxes)
```

### B.2. Sufficient condition for a set to contain allowed subsets of card `n.succ` based on `n`

**`FTheory.SU5.FluxesTen.subset_le_mem_of_card_eq_succ`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L327).

```lean
lemma subset_le_mem_of_card_eq_succ {n : ℕ} {F : FluxesTen} (hF : F.NoExotics) (hnZ : F.HasNoZero)
    (S : Multiset Fluxes) (hcard : S.card = n.succ) (hS : S ≤ F) {Y X : Finset (Multiset Fluxes)}
    (hY : ∀ (S : Multiset Fluxes), S.card = n → S ≤ F → S ∈ Y)
    (hX : ∀ a ∈ ({⟨1, -1⟩, ⟨1, 0⟩, ⟨1, 1⟩, ⟨2, -1⟩, ⟨2, 0⟩, ⟨2, 1⟩, ⟨3, 0⟩} : Finset Fluxes),
      ∀ y ∈ Y,
      (Multiset.map (fun x => x.M) (a ::ₘ y)).sum ≤ 3 →
      (Multiset.map (fun x => x.M - x.N) (a ::ₘ y)).sum ≤ 3 →
      (Multiset.map (fun x => x.M + x.N) (a ::ₘ y)).sum ≤ 3 →
      a ::ₘ y ∈ X) :
    S ∈ X
```

### B.3. Statement of the allowed subsets of each cardinality

**`FTheory.SU5.FluxesTen.noExoticsSubsets`**, a def, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L357).

> The allowed subsets of a `FluxesTen` which has no exotics or zeros.

```lean
def noExoticsSubsets : (n : ℕ) → Finset (Multiset Fluxes)
```

### B.4. Lemma that stated allowed subsets are complete

**`FTheory.SU5.FluxesTen.subset_of_fluxesTen_mem_noExoticsSubsets_of_noExotics`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L371).

```lean
lemma subset_of_fluxesTen_mem_noExoticsSubsets_of_noExotics {F : FluxesTen} (hF : F.NoExotics)
    (hnZ : F.HasNoZero) (S : Multiset Fluxes) (hS : S ≤ F) :
    S ∈ noExoticsSubsets S.card
```

### B.5. Terms of `FluxesTen` obeying `NoExotics` and `HasNoZero` have card ≤ 3

**`FTheory.SU5.FluxesTen.card_le_three_of_noExotics`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L397).

```lean
lemma card_le_three_of_noExotics {F : FluxesTen} (hF : F.NoExotics) (hnZ : F.HasNoZero) :
    F.card ≤ 3
```

**`FTheory.SU5.FluxesTen.card_mem_range_four_of_noExotics`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L409).

```lean
lemma card_mem_range_four_of_noExotics {F : FluxesTen} (hF : F.NoExotics) (hnZ : F.HasNoZero) :
    F.card ∈ Finset.range 4
```

### B.6. Terms of `FluxesTen` obeying `NoExotics` and `HasNoZero` are in `elemsNoExotics`

**`FTheory.SU5.FluxesTen.mem_elemsNoExotics_of_noExotics`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L420).

```lean
lemma mem_elemsNoExotics_of_noExotics (F : FluxesTen) (hNE : F.NoExotics) (hnZ : F.HasNoZero) :
    F ∈ elemsNoExotics
```

### B.7. Terms of `FluxesTen` obey `NoExotics` and `HasNoZero` if and only if in `elemsNoExotics`

**`FTheory.SU5.FluxesTen.noExotics_iff_mem_elemsNoExotics`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean#L445).

> Completeness of `elemsNoExotics`, that is, every element of `FluxesTen`
> which obeys `NoExotics` is an element of `elemsNoExotics`, and every
> element of `elemsNoExotics` obeys `NoExotics`.

```lean
lemma noExotics_iff_mem_elemsNoExotics (F : FluxesTen) :
    F.NoExotics ∧ F.HasNoZero ↔ F ∈ elemsNoExotics
```

## Depends on

- [Terms of `FluxesFive` and `FluxesTen` with no chiral exotics](su5-fluxes-noexotics-elems.md)

## Proof depends on

- [Constraints on chiral indices from the condition of no chiral exotics](su5-fluxes-noexotics-chiralindices.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/Completeness.lean)
