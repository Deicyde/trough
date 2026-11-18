---
declaration: module
origin: cited
lean: LadderSystem.HasVacuum, LadderSystem.word, LadderSystem.word_cons, LadderSystem.word_perm, LadderSystem.word_peel, LadderSystem.E_word, LadderSystem.N_word, LadderSystem.countWord
statement: formalized
proof: formalized
---

# Vacuum states and creation-operator words

The module `PhyslibAlpha.Mathematics.LadderSystem.Vacuum`, [PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean): 17 declarations, 14 with a docstring.

> Vacuum states of a ladder system, creation-operator words, and the `n`-particle sector.

## i. Overview

> A vacuum `Ω` of a `LadderSystem` is a nonzero vector killed by every annihilation operator. This
> file develops creation-operator words `acᵢ₁acᵢ₂⋯acᵢₙΩ` and the excitation-number sector they span,
> `vacuumSpan`. This sector is bundled as a `gl(d)` Lie submodule. Its occupation-number basis is
> constructed in `OccupationBasis.lean`, and its irreducibility is proved in `Irreducibility.lean`.

## ii. Key results

> Definitions:
> - `LadderSystem.HasVacuum` : `Ω` is nonzero and killed by every `a i`.
> - `LadderSystem.word` : a word of creation operators applied to a vector.
> - `LadderSystem.vacuumSpan` : the span of all length-`n` words over a vacuum -- the
>     `n`-particle sector.
> - `LadderSystem.vacuumSpanLieSubmodule` : `vacuumSpan`, bundled as a `gl(d)` Lie submodule.
>
> Theorems:
> - `LadderSystem.word_perm` : a word depends only on the multiset of colors it represents.
> - `LadderSystem.word_peel` : `aᵢ` applied to a word removes one occurrence of color `i`, scaled
>     by its count.
> - `LadderSystem.E_word`, `LadderSystem.N_word` : how `E i j`/`N i` act on a word.
> - `LadderSystem.E_mem_vacuumSpan` : `vacuumSpan` is closed under every `gl(d)` generator `E i j`.

## iv. References

> * None.

## A. Vacuum states

**`LadderSystem.HasVacuum`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L65).

> A vacuum: a nonzero vector killed by every annihilation operator.

```lean
structure HasVacuum (Ω : V) : Prop where
  /-- A vacuum is nonzero. -/
  ne_zero : Ω ≠ 0
  /-- A vacuum is killed by every annihilation operator. -/
  ann : ∀ i, L.a i Ω = 0
```

## B. Words

**`LadderSystem.word`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L80).

> A word of creation operators applied to a fixed vector.

```lean
def word (L : LadderSystem K V d) (v : List (Fin d)) (x : V) : V
```

**`LadderSystem.word_cons`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L83).

```lean
lemma word_cons (L : LadderSystem K V d) (i : Fin d) (v : List (Fin d)) (x : V) :
    L.word (i :: v) x = L.ac i (L.word v x)
```

**`LadderSystem.word_perm`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L88).

> A word depends only on the multiset of colors it represents, not their order.

```lean
lemma word_perm (L : LadderSystem K V d) {v v' : List (Fin d)} (h : v.Perm v') (x : V) :
    L.word v x = L.word v' x
```

**`LadderSystem.word_peel`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L102).

> Peeling: `a i` applied to a word removes one occurrence of color `i`, scaled by its count.

```lean
lemma word_peel (L : LadderSystem K V d) (i : Fin d) {x : V} (hx : L.a i x = 0) :
    ∀ v : List (Fin d), L.a i (L.word v x) = (v.count i) • L.word (v.erase i) x
```

**`LadderSystem.E_word`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L132).

> How `E i j` acts on a word: removes one occurrence of `j`, adds one of `i`, scaled by `j`'s
> count.

```lean
lemma E_word (L : LadderSystem K V d) {x : V} (hx : ∀ i, L.a i x = 0) (i j : Fin d)
    (v : List (Fin d)) :
    (L.E i j) (L.word v x) = (v.count j) • L.word (i :: v.erase j) x
```

**`LadderSystem.N_word`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L139).

> Words are eigenvectors of the number operator, with eigenvalue their own color count.

```lean
lemma N_word (L : LadderSystem K V d) {x : V} (hx : ∀ i, L.a i x = 0) (i : Fin d)
    (v : List (Fin d)) : (L.N i) (L.word v x) = (v.count i) • L.word v x
```

## C. The excitation-number sector

**`LadderSystem.countWord`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L154).

> The canonical word representing a count function `α`: `α c` copies of color `c`, in
> increasing order.

```lean
def countWord (d : ℕ) (α : Fin d → ℕ) : List (Fin d)
```

**`LadderSystem.count_countWord`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L158).

> `countWord α` has exactly `α i` copies of color `i`.

```lean
lemma count_countWord {d : ℕ} (α : Fin d → ℕ) (i : Fin d) :
    (countWord d α).count i = α i
```

**`LadderSystem.sum_count_eq_length`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L184).

> A word's length is the sum of its per-color counts.

```lean
lemma sum_count_eq_length {d : ℕ} : ∀ v : List (Fin d), (∑ c : Fin d, v.count c) = v.length
```

**`LadderSystem.vacuumSpan`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L200).

> The `n`-th excitation-number sector generated by a vacuum: the span of all length-`n`
> creation words.

```lean
def vacuumSpan (L : LadderSystem K V d) (Ω : V) (n : ℕ) : Submodule K V
```

**`LadderSystem.exists_ofFn_eq_of_length_eq`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L203).

```lean
lemma exists_ofFn_eq_of_length_eq {l : List (Fin d)} {n : ℕ} (h : l.length = n) :
    ∃ w : Fin n → Fin d, List.ofFn w = l
```

**`LadderSystem.word_mem_vacuumSpan_of_length_eq`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L211).

> Any word of the right length lies in `vacuumSpan`.

```lean
lemma word_mem_vacuumSpan_of_length_eq (L : LadderSystem K V d) (Ω : V) {n : ℕ}
    {l : List (Fin d)} (h : l.length = n) : L.word l Ω ∈ vacuumSpan L Ω n
```

### C.1. `gl(d)`-invariance

**`LadderSystem.forall_toGlHomLinear_mem_of_forall_E_mem`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L224).

> `E`-invariance of a submodule extends to full `gl(d)`-invariance, by linearity off the
> matrix-unit basis.

```lean
lemma forall_toGlHomLinear_mem_of_forall_E_mem (L : LadderSystem K V d) {W : Submodule K V}
    (hW : ∀ i j, ∀ w ∈ W, (L.E i j) w ∈ W) (x : Matrix (Fin d) (Fin d) K) {w : V}
    (hw : w ∈ W) : L.toGlHomLinear x w ∈ W
```

**`LadderSystem.E_mem_vacuumSpan`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L240).

> `vacuumSpan` is closed under every `gl(d)` generator `E i j`. Unconditional: no
> `FiniteDimensional`/spanning hypothesis on the ambient `V` is used or needed.

```lean
lemma E_mem_vacuumSpan (L : LadderSystem K V d) {Ω : V} (P : L.HasVacuum Ω) (n : ℕ)
    (i j : Fin d) : ∀ v ∈ vacuumSpan L Ω n, (L.E i j) v ∈ vacuumSpan L Ω n
```

**`LadderSystem.vacuumSpanLieSubmodule`**, a def, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L261).

> `vacuumSpan`, bundled as a genuine `gl(d)` Lie submodule.

```lean
def vacuumSpanLieSubmodule (L : LadderSystem K V d) {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) :
    haveI := L.toLieRingModule
    LieSubmodule K (Matrix (Fin d) (Fin d) K) V
```

**`LadderSystem.coe_vacuumSpanLieSubmodule`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean#L272).

```lean
lemma coe_vacuumSpanLieSubmodule (L : LadderSystem K V d) {Ω : V} (P : L.HasVacuum Ω)
    (n : ℕ) : (vacuumSpanLieSubmodule L P n : Submodule K V) = vacuumSpan L Ω n
```

## Depends on

- [Ladder systems](basic.md)

## Sources

- [PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/Vacuum.lean)
