---
declaration: module
origin: cited
lean: WickContraction, WickContraction.empty, WickContraction.card_zero_iff_empty, WickContraction.exists_pair_of_not_eq_empty, WickContraction.congr, WickContraction.congr_refl, WickContraction.card_congr, WickContraction.congr_contractions
statement: formalized
proof: formalized
---

# Wick contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.Basic`, [Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean): 56 declarations (1 instance with no name), 12 with a docstring.

**`WickContraction`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L28).

> Given a natural number `n`, which will correspond to the number of fields needing
> contracting, a Wick contraction
> is a finite set of pairs of `Fin n` (numbers `0`, ..., `n-1`), such that no
> element of `Fin n` occurs in more than one pair. The pairs are the positions of fields we
> 'contract' together.

```lean
def WickContraction (n : ℕ) : Type
```

**An instance with no name**, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L37).

> Wick contractions are decidable.

```lean
instance : DecidableEq (WickContraction n)
```

**`WickContraction.empty`**, a def, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L40).

> The contraction consisting of no contracted pairs.

```lean
def empty : WickContraction n
```

**`WickContraction.card_zero_iff_empty`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L43).

```lean
lemma card_zero_iff_empty (c : WickContraction n) : c.1.card = 0 ↔ c = empty
```

**`WickContraction.exists_pair_of_not_eq_empty`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L46).

```lean
lemma exists_pair_of_not_eq_empty (c : WickContraction n) (h : c ≠ empty) :
    ∃ i j, {i, j} ∈ c.1
```

**`WickContraction.congr`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L54).

> The equivalence between `WickContraction n` and `WickContraction m`
> derived from a propositional equality of `n` and `m`.

```lean
def congr : {n m : ℕ} → (h : n = m) → WickContraction n ≃ WickContraction m
```

**`WickContraction.congr_refl`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L58).

```lean
lemma congr_refl : c.congr rfl = c
```

**`WickContraction.card_congr`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L61).

```lean
lemma card_congr {n m : ℕ} (h : n = m) (c : WickContraction n) :
    (congr h c).1.card = c.1.card
```

**`WickContraction.congr_contractions`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L66).

```lean
lemma congr_contractions {n m : ℕ} (h : n = m) (c : WickContraction n) :
    ((congr h) c).1 = Finset.map (Finset.mapEmbedding (finCongr h)).toEmbedding c.1
```

**`WickContraction.congr_trans`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L76).

```lean
lemma congr_trans {n m o : ℕ} (h1 : n = m) (h2 : m = o) :
    (congr h1).trans (congr h2) = congr (h1.trans h2)
```

**`WickContraction.congr_trans_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L82).

```lean
lemma congr_trans_apply {n m o : ℕ} (h1 : n = m) (h2 : m = o) (c : WickContraction n) :
    (congr h2) ((congr h1) c) = congr (h1.trans h2) c
```

**`WickContraction.mem_congr_iff`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L87).

```lean
lemma mem_congr_iff {n m : ℕ} (h : n = m) {c : WickContraction n } {a : Finset (Fin m)} :
    a ∈ (congr h c).1 ↔ Finset.map (finCongr h.symm).toEmbedding a ∈ c.1
```

**`WickContraction.congrLift`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L94).

> Given a contracted pair in `c : WickContraction n` the contracted pair
> in `congr h c`.

```lean
def congrLift {n m : ℕ} (h : n = m) {c : WickContraction n} (a : c.1) : (congr h c).1
```

**`WickContraction.congrLift_rfl`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L98).

```lean
lemma congrLift_rfl {n : ℕ} {c : WickContraction n} :
    c.congrLift rfl = id
```

**`WickContraction.congrLift_injective`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L103).

```lean
lemma congrLift_injective {n m : ℕ} {c : WickContraction n} (h : n = m) :
    Function.Injective (c.congrLift h)
```

**`WickContraction.congrLift_surjective`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L108).

```lean
lemma congrLift_surjective {n m : ℕ} {c : WickContraction n} (h : n = m) :
    Function.Surjective (c.congrLift h)
```

**`WickContraction.congrLift_bijective`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L113).

```lean
lemma congrLift_bijective {n m : ℕ} {c : WickContraction n} (h : n = m) :
    Function.Bijective (c.congrLift h)
```

**`WickContraction.congrLiftInv`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L119).

> Given a contracted pair in `c : WickContraction n` the contracted pair
> in `congr h c`.

```lean
def congrLiftInv {n m : ℕ} (h : n = m) {c : WickContraction n} (a : (congr h c).1) : c.1
```

**`WickContraction.congrLiftInv_rfl`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L123).

```lean
lemma congrLiftInv_rfl {n : ℕ} {c : WickContraction n} :
    c.congrLiftInv rfl = id
```

**`WickContraction.eq_filter_mem_self`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L128).

```lean
lemma eq_filter_mem_self : c.1 = Finset.filter (fun x => x ∈ c.1) Finset.univ
```

**`WickContraction.getDual?`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L133).

> For a contraction `c : WickContraction n` and `i : Fin n` the `j` such that
> `{i, j}` is a contracted pair in `c`. If such an `j` does not exist, this returns `none`.

```lean
def getDual? (i : Fin n) : Option (Fin n)
```

**`WickContraction.getDual?_congr`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L135).

```lean
lemma getDual?_congr {n m : ℕ} (h : n = m) (c : WickContraction n) (i : Fin m) :
    (congr h c).getDual? i = Option.map (finCongr h) (c.getDual? (finCongr h.symm i))
```

**`WickContraction.getDual?_congr_get`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L140).

```lean
lemma getDual?_congr_get {n m : ℕ} (h : n = m) (c : WickContraction n) (i : Fin m)
    (hg : ((congr h c).getDual? i).isSome) :
    ((congr h c).getDual? i).get hg =
    (finCongr h ((c.getDual? (finCongr h.symm i)).get (by simpa [getDual?_congr] using hg)))
```

**`WickContraction.getDual?_eq_some_iff_mem`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L146).

```lean
lemma getDual?_eq_some_iff_mem (i j : Fin n) :
    c.getDual? i = some j ↔ {i, j} ∈ c.1
```

**`WickContraction.getDual?_one_eq_none`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L160).

```lean
lemma getDual?_one_eq_none (c : WickContraction 1) (i : Fin 1) : c.getDual? i = none
```

**`WickContraction.getDual?_get_self_mem`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L167).

```lean
lemma getDual?_get_self_mem (i : Fin n) (h : (c.getDual? i).isSome) :
    {(c.getDual? i).get h, i} ∈ c.1
```

**`WickContraction.self_getDual?_get_mem`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L172).

```lean
lemma self_getDual?_get_mem (i : Fin n) (h : (c.getDual? i).isSome) :
    {i, (c.getDual? i).get h} ∈ c.1
```

**`WickContraction.getDual?_eq_some_neq`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L176).

```lean
lemma getDual?_eq_some_neq (i j : Fin n) (h : c.getDual? i = some j) :
    ¬ i = j
```

**`WickContraction.self_ne_getDual?_get`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L183).

```lean
lemma self_ne_getDual?_get (i : Fin n) (h : (c.getDual? i).isSome) :
    ¬ i = (c.getDual? i).get h
```

**`WickContraction.getDual?_get_self_neq`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L188).

```lean
lemma getDual?_get_self_neq (i : Fin n) (h : (c.getDual? i).isSome) :
    ¬ (c.getDual? i).get h = i
```

**`WickContraction.getDual?_isSome_iff`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L192).

```lean
lemma getDual?_isSome_iff (i : Fin n) : (c.getDual? i).isSome ↔ ∃ (a : c.1), i ∈ a.1
```

**`WickContraction.getDual?_isSome_of_mem`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L203).

```lean
lemma getDual?_isSome_of_mem (a : c.1) (i : a.1) : (c.getDual? i).isSome
```

**`WickContraction.getDual?_getDual?_get_get`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L207).

```lean
lemma getDual?_getDual?_get_get (i : Fin n) (h : (c.getDual? i).isSome) :
    c.getDual? ((c.getDual? i).get h) = some i
```

**`WickContraction.getDual?_getDual?_get_isSome`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L211).

```lean
lemma getDual?_getDual?_get_isSome (i : Fin n) (h : (c.getDual? i).isSome) :
    (c.getDual? ((c.getDual? i).get h)).isSome
```

**`WickContraction.getDual?_getDual?_get_not_none`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L215).

```lean
lemma getDual?_getDual?_get_not_none (i : Fin n) (h : (c.getDual? i).isSome) :
    ¬ (c.getDual? ((c.getDual? i).get h)) = none
```

## Extracting parts from a contraction.

**`WickContraction.fstFieldOfContract`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L226).

> The smallest of the two positions in a contracted pair given a Wick contraction.

```lean
def fstFieldOfContract (c : WickContraction n) (a : c.1) : Fin n
```

**`WickContraction.fstFieldOfContract_congr`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L233).

```lean
lemma fstFieldOfContract_congr {n m : ℕ} (h : n = m) (c : WickContraction n) (a : c.1) :
    (congr h c).fstFieldOfContract (c.congrLift h a) = (finCongr h) (c.fstFieldOfContract a)
```

**`WickContraction.sndFieldOfContract`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L239).

> The largest of the two positions in a contracted pair given a Wick contraction.

```lean
def sndFieldOfContract (c : WickContraction n) (a : c.1) : Fin n
```

**`WickContraction.sndFieldOfContract_congr`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L247).

```lean
lemma sndFieldOfContract_congr {n m : ℕ} (h : n = m) (c : WickContraction n) (a : c.1) :
    (congr h c).sndFieldOfContract (c.congrLift h a) = (finCongr h) (c.sndFieldOfContract a)
```

**`WickContraction.finset_eq_fstFieldOfContract_sndFieldOfContract`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L252).

```lean
lemma finset_eq_fstFieldOfContract_sndFieldOfContract (c : WickContraction n) (a : c.1) :
    a.1 = {c.fstFieldOfContract a, c.sndFieldOfContract a}
```

**`WickContraction.fstFieldOfContract_ne_sndFieldOfContract`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L267).

```lean
lemma fstFieldOfContract_ne_sndFieldOfContract (c : WickContraction n) (a : c.1) :
    c.fstFieldOfContract a ≠ c.sndFieldOfContract a
```

**`WickContraction.fstFieldOfContract_le_sndFieldOfContract`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L272).

```lean
lemma fstFieldOfContract_le_sndFieldOfContract (c : WickContraction n) (a : c.1) :
    c.fstFieldOfContract a ≤ c.sndFieldOfContract a
```

**`WickContraction.fstFieldOfContract_lt_sndFieldOfContract`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L276).

```lean
lemma fstFieldOfContract_lt_sndFieldOfContract (c : WickContraction n) (a : c.1) :
    c.fstFieldOfContract a < c.sndFieldOfContract a
```

**`WickContraction.fstFieldOfContract_mem`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L282).

```lean
lemma fstFieldOfContract_mem (c : WickContraction n) (a : c.1) :
    c.fstFieldOfContract a ∈ a.1
```

**`WickContraction.fstFieldOfContract_getDual?_isSome`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L286).

```lean
lemma fstFieldOfContract_getDual?_isSome (c : WickContraction n) (a : c.1) :
    (c.getDual? (c.fstFieldOfContract a)).isSome
```

**`WickContraction.fstFieldOfContract_getDual?`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L291).

```lean
lemma fstFieldOfContract_getDual? (c : WickContraction n) (a : c.1) :
    c.getDual? (c.fstFieldOfContract a) = some (c.sndFieldOfContract a)
```

**`WickContraction.sndFieldOfContract_mem`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L296).

```lean
lemma sndFieldOfContract_mem (c : WickContraction n) (a : c.1) :
    c.sndFieldOfContract a ∈ a.1
```

**`WickContraction.sndFieldOfContract_getDual?_isSome`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L300).

```lean
lemma sndFieldOfContract_getDual?_isSome (c : WickContraction n) (a : c.1) :
    (c.getDual? (c.sndFieldOfContract a)).isSome
```

**`WickContraction.sndFieldOfContract_getDual?`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L305).

```lean
lemma sndFieldOfContract_getDual? (c : WickContraction n) (a : c.1) :
    c.getDual? (c.sndFieldOfContract a) = some (c.fstFieldOfContract a)
```

**`WickContraction.eq_fstFieldOfContract_of_mem`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L310).

```lean
lemma eq_fstFieldOfContract_of_mem (c : WickContraction n) (a : c.1) (i j : Fin n)
    (hi : i ∈ a.1) (hj : j ∈ a.1) (hij : i < j) :
    c.fstFieldOfContract a = i
```

**`WickContraction.eq_sndFieldOfContract_of_mem`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L318).

```lean
lemma eq_sndFieldOfContract_of_mem (c : WickContraction n) (a : c.1) (i j : Fin n)
    (hi : i ∈ a.1) (hj : j ∈ a.1) (hij : i < j) :
    c.sndFieldOfContract a = j
```

**`WickContraction.contractEquivFinTwo`**, a def, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L329).

> As a type, any pair of contractions is equivalent to `Fin 2`
> with `0` being associated with `c.fstFieldOfContract a` and `1` being associated with
> `c.sndFieldOfContract`.

```lean
def contractEquivFinTwo (c : WickContraction n) (a : c.1) :
    a ≃ Fin 2
```

**`WickContraction.prod_finset_eq_mul_fst_snd`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L354).

```lean
lemma prod_finset_eq_mul_fst_snd (c : WickContraction n) (a : c.1)
    (f : a.1 → M) [CommMonoid M] :
    ∏ (x : a), f x = f (⟨c.fstFieldOfContract a, fstFieldOfContract_mem c a⟩)
    * f (⟨c.sndFieldOfContract a, sndFieldOfContract_mem c a⟩)
```

**`WickContraction.GradingCompliant`**, a def, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L366).

> For a field specification `𝓕`, `φs` a list of `𝓕.FieldOp` and a Wick contraction
> `φsΛ` of `φs`, the Wick contraction `φsΛ` is said to be `GradingCompliant` if
> for every pair in `φsΛ` the contracted fields are either both `fermionic` or both `bosonic`.
> In other words, in a `GradingCompliant` Wick contraction if
> no contracted pairs occur between `fermionic` and `bosonic` fields.

```lean
def GradingCompliant (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
```

**`WickContraction.gradingCompliant_congr`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L369).

```lean
lemma gradingCompliant_congr {φs φs' : List 𝓕.FieldOp} (h : φs = φs')
    (φsΛ : WickContraction φs.length) :
    GradingCompliant φs φsΛ ↔ GradingCompliant φs' (congr (by simp [h]) φsΛ)
```

**`WickContraction.sigmaContractedEquiv`**, a def, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean#L377).

> An equivalence from the sigma type `(a : c.1) × a` to the subtype of `Fin n` consisting of
> those positions which are contracted.

```lean
def sigmaContractedEquiv : (a : c.1) × a ≃ {x : Fin n // (c.getDual? x).isSome}
```

## Depends on

- [Field specification](../part-01/fieldspecification-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Basic.lean)
