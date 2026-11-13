---
declaration: module
origin: cited
lean: WickContraction.subContraction, WickContraction.mem_of_mem_subContraction, WickContraction.quotContraction, WickContraction.mem_of_mem_quotContraction, WickContraction.mem_subContraction_or_quotContraction, WickContraction.subContraction_uncontractedList_get, WickContraction.subContraction_fstFieldOfContract, WickContraction.subContraction_sndFieldOfContract
statement: formalized
proof: formalized
---

# Sub contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.SubContraction`, [Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean): 12 declarations, 2 with a docstring.

**`WickContraction.subContraction`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L26).

> Given a Wick contraction `φsΛ`, and a subset of `φsΛ.1`, the Wick contraction
> consisting of contracted pairs within that subset.

```lean
def subContraction (S : Finset (Finset (Fin φs.length))) (ha : S ⊆ φsΛ.1) :
    WickContraction φs.length
```

**`WickContraction.mem_of_mem_subContraction`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L35).

```lean
lemma mem_of_mem_subContraction {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    {a : Finset (Fin φs.length)} (ha : a ∈ (φsΛ.subContraction S hs).1) : a ∈ φsΛ.1
```

**`WickContraction.quotContraction`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L42).

> Given a Wick contraction `φsΛ`, and a subset `S` of `φsΛ.1`, the Wick contraction
> on the uncontracted list `[φsΛ.subContraction S ha]ᵘᶜ`
> consisting of the remaining contracted pairs of `φsΛ` not in `S`.

```lean
def quotContraction (S : Finset (Finset (Fin φs.length))) (ha : S ⊆ φsΛ.1) :
    WickContraction [φsΛ.subContraction S ha]ᵘᶜ.length
```

**`WickContraction.mem_of_mem_quotContraction`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L57).

```lean
lemma mem_of_mem_quotContraction {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    {a : Finset (Fin [φsΛ.subContraction S hs]ᵘᶜ.length)}
    (ha : a ∈ (quotContraction S hs).1) : Finset.map uncontractedListEmd a ∈ φsΛ.1
```

**`WickContraction.mem_subContraction_or_quotContraction`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L63).

```lean
lemma mem_subContraction_or_quotContraction {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    {a : Finset (Fin φs.length)} (ha : a ∈ φsΛ.1) :
    a ∈ (φsΛ.subContraction S hs).1 ∨
    ∃ a', Finset.map uncontractedListEmd a' = a ∧ a' ∈ (quotContraction S hs).1
```

**`WickContraction.subContraction_uncontractedList_get`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L101).

```lean
lemma subContraction_uncontractedList_get {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    {a : Fin [subContraction S hs]ᵘᶜ.length} :
    [subContraction S hs]ᵘᶜ[a.1] = φs[(uncontractedListEmd a).1]
```

**`WickContraction.subContraction_fstFieldOfContract`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L107).

```lean
lemma subContraction_fstFieldOfContract {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    (a : (subContraction S hs).1) :
    (subContraction S hs).fstFieldOfContract a =
    φsΛ.fstFieldOfContract ⟨a.1, mem_of_mem_subContraction a.2⟩
```

**`WickContraction.subContraction_sndFieldOfContract`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L128).

```lean
lemma subContraction_sndFieldOfContract {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    (a : (subContraction S hs).1) :
    (subContraction S hs).sndFieldOfContract a =
    φsΛ.sndFieldOfContract ⟨a.1, mem_of_mem_subContraction a.2⟩
```

**`WickContraction.quotContraction_fstFieldOfContract_uncontractedListEmd`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L149).

```lean
lemma quotContraction_fstFieldOfContract_uncontractedListEmd {S : Finset (Finset (Fin φs.length))}
    {hs : S ⊆ φsΛ.1} (a : (quotContraction S hs).1) :
    uncontractedListEmd ((quotContraction S hs).fstFieldOfContract a) =
    (φsΛ.fstFieldOfContract
    ⟨Finset.map uncontractedListEmd a.1, mem_of_mem_quotContraction a.2⟩)
```

**`WickContraction.quotContraction_sndFieldOfContract_uncontractedListEmd`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L163).

```lean
lemma quotContraction_sndFieldOfContract_uncontractedListEmd {S : Finset (Finset (Fin φs.length))}
    {hs : S ⊆ φsΛ.1} (a : (quotContraction S hs).1) :
    uncontractedListEmd ((quotContraction S hs).sndFieldOfContract a) =
    (φsΛ.sndFieldOfContract
      ⟨Finset.map uncontractedListEmd a.1, mem_of_mem_quotContraction a.2⟩)
```

**`WickContraction.quotContraction_gradingCompliant`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L176).

```lean
lemma quotContraction_gradingCompliant {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    (hsΛ : φsΛ.GradingCompliant) :
    GradingCompliant [φsΛ.subContraction S hs]ᵘᶜ (quotContraction S hs)
```

**`WickContraction.mem_quotContraction_iff`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean#L187).

```lean
lemma mem_quotContraction_iff {S : Finset (Finset (Fin φs.length))} {hs : S ⊆ φsΛ.1}
    {a : Finset (Fin [φsΛ.subContraction S hs]ᵘᶜ.length)} :
    a ∈ (quotContraction S hs).1 ↔ a.map uncontractedListEmd ∈ φsΛ.1
    ∧ a.map uncontractedListEmd ∉ (subContraction S hs).1
```

## Depends on

- [List of uncontracted elements of a Wick contraction](wickcontraction-uncontractedlist.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/SubContraction.lean)
