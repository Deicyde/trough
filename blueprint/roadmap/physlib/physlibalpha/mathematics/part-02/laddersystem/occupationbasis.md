---
declaration: module
origin: cited
lean: LadderSystem.linearIndependent_word_countFun, LadderSystem.finrank_vacuumSpan_eq_choose, CountFun, countFunEquivSym, instFintypeCountFun, card_countFun, LadderSystem.pow_a_comm_ac, LadderSystem.word_peel_eq_count
statement: formalized
proof: formalized
---

# The occupation-number basis

The module `PhyslibAlpha.Mathematics.LadderSystem.OccupationBasis`, [PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean): 23 declarations, 16 with a docstring, 2 listed as significant.

> The occupation-number states form a basis of `vacuumSpan L Ω n`, of dimension `(d+n-1).choose n`.

## i. Overview

> The occupation-number states `word (countWord d α) Ω`, indexed by degree-`n` count functions
> `α : CountFun d n`, form a basis of `vacuumSpan L Ω n`. For linear independence, each state is
> viewed as a nonzero eigenvector of the diagonal operator
> `M := ∑ᵢ (n+1)^i • Nᵢ`, at the pairwise-distinct eigenvalue `countEncode n α` (a positional
> encoding of `α`), so Mathlib's general "eigenvectors at distinct eigenvalues are independent" fact
> applies. It follows that `vacuumSpan` is finite-dimensional and has dimension
> `(d+n-1).choose n`, the degeneracy of the `n`-th level of a `d`-dimensional bosonic oscillator.

## ii. Key results

> Definitions:
> - `CountFun d n` : a degree-`n` count function on `d` colors.
> - `LadderSystem.vacuumBasis` : the occupation-number basis of `vacuumSpan L Ω n`.
>
> Theorems:
> - `LadderSystem.linearIndependent_word_countFun` : the occupation-number states are linearly
>     independent.
> - `LadderSystem.finrank_vacuumSpan_eq_choose` : `vacuumSpan L Ω n` has dimension
>     `(d+n-1).choose n`.

## iv. References

> * None.

## A. Count functions

**`CountFun`**, an abbrev, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L65).

> A degree-`n` count function on `d` colors.

```lean
abbrev CountFun (d n : ℕ)
```

**`countFunEquivSym`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L68).

> Degree-`n` count functions on `d` colors biject with `Sym (Fin d) n`.

```lean
noncomputable def countFunEquivSym (d n : ℕ) : CountFun d n ≃ Sym (Fin d) n
```

**`instFintypeCountFun`**, an instance, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L71).

```lean
noncomputable instance instFintypeCountFun {d n : ℕ} : Fintype (CountFun d n)
```

**`card_countFun`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L75).

> There are exactly `(d + n - 1).choose n` degree-`n` count functions on `d` colors.

```lean
lemma card_countFun (d n : ℕ) : Fintype.card (CountFun d n) = (d + n - 1).choose n
```

## B. Exact annihilation

**`LadderSystem.pow_a_comm_ac`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L93).

> Annihilation and creation operators of different colors commute at any power.

```lean
lemma pow_a_comm_ac {i c : Fin d} (hic : i ≠ c) (k : ℕ) (y : V) :
    ((L.a i) ^ k) (L.ac c y) = L.ac c (((L.a i) ^ k) y)
```

**`LadderSystem.word_peel_eq_count`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L104).

> Exact annihilation: applying `a i` exactly `count i` times removes every `i`, scaled by the
> factorial.

```lean
lemma word_peel_eq_count (L : LadderSystem K V d) (i : Fin d) {x : V} (hx : L.a i x = 0) :
    ∀ v : List (Fin d),
      ((L.a i) ^ (v.count i)) (L.word v x) = (v.count i).factorial • L.word (v.filter (· != i)) x
```

**`LadderSystem.annMono`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L122).

> The joint annihilation monomial for a list of colors `cs` and exponents `α`:
> `∏_{c ∈ cs} (a c)^{α c}`.

```lean
def annMono (cs : List (Fin d)) (α : Fin d → ℕ) : Module.End K V
```

**`LadderSystem.annMono_nil`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L126).

```lean
lemma annMono_nil (α : Fin d → ℕ) : L.annMono [] α = 1
```

**`LadderSystem.annMono_cons`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L129).

```lean
lemma annMono_cons (c : Fin d) (cs : List (Fin d)) (α : Fin d → ℕ) :
    L.annMono (c :: cs) α = (L.a c) ^ (α c) * L.annMono cs α
```

**`LadderSystem.annMono_eq_count`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L134).

> Exact annihilation of every color in the list produces the product of factorials.

```lean
lemma annMono_eq_count (L : LadderSystem K V d) {x : V} (hx : ∀ i, L.a i x = 0) :
    ∀ (cs : List (Fin d)), cs.Nodup → ∀ (α : Fin d → ℕ) (v : List (Fin d)),
      (∀ c ∈ cs, v.count c = α c) →
      (L.annMono cs α) (L.word v x)
        = ((cs.map (fun c => (α c).factorial)).prod) •
            L.word (v.filter (fun y => !cs.contains y)) x
  | [], _, _, _, _ => by simp
  | c :: cs', hnodup, α, v, hmatch => by
    obtain ⟨hcnotmem, hnodup'⟩
```

**`countWord_filter_finRange`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L168).

> `countWord α` contains only colors from `List.finRange d`, i.e. everything.

```lean
lemma countWord_filter_finRange {d : ℕ} (α : Fin d → ℕ) :
    (LadderSystem.countWord d α).filter (fun y => !(List.finRange d).contains y) = []
```

## C. The occupation-number basis

### C.1. A positional encoding of count functions

**`encode_injOn_aux`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L185).

> A base-`b` positional encoding is injective on tuples with digits `< b`.

```lean
lemma encode_injOn_aux : ∀ (d b : ℕ), 0 < b → ∀ γ γ' : Fin d → ℕ,
    (∀ c, γ c < b) → (∀ c, γ' c < b) →
    (∑ i : Fin d, γ i * b ^ (i : ℕ)) = (∑ i : Fin d, γ' i * b ^ (i : ℕ)) → γ = γ'
```

**`countEncode`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L219).

> The base-`(n+1)` positional encoding of a degree-`n` count function; injective on such
> functions.

```lean
def countEncode (n : ℕ) {d : ℕ} (γ : Fin d → ℕ) : ℕ
```

**`countEncode_injOn`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L221).

```lean
lemma countEncode_injOn {d n : ℕ} {γ γ' : Fin d → ℕ}
    (hγ : ∑ c, γ c = n) (hγ' : ∑ c, γ' c = n) (heq : countEncode n γ = countEncode n γ') :
    γ = γ'
```

### C.2. Linear independence

**`LadderSystem.word_countWord_ne_zero`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L243).

> Every occupation-number state is nonzero: peeling every color's annihilation operator down to
> the vacuum leaves a nonzero factorial multiple of `Ω`.

```lean
lemma word_countWord_ne_zero {Ω : V} (hΩ : L.HasVacuum Ω) (α : Fin d → ℕ) :
    L.word (countWord d α) Ω ≠ 0
```

**`LadderSystem.hasEigenvector_word_countWord`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L264).

> The occupation-number states are the eigenvectors, at pairwise-distinct eigenvalues, of the
> single diagonal operator `M := ∑ᵢ (n+1)^i • Nᵢ`.

```lean
lemma hasEigenvector_word_countWord {Ω : V} (hΩ : L.HasVacuum Ω) (n : ℕ) (α : CountFun d n) :
    Module.End.HasEigenvector (∑ i : Fin d, ((n + 1 : K)) ^ (i : ℕ) • L.N i)
      (countEncode n α.1 : K) (L.word (countWord d α.1) Ω)
```

**`LadderSystem.linearIndependent_word_countFun`**, a theorem, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L284). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The occupation-number family is linearly independent because its elements are eigenvectors at
> pairwise-distinct eigenvalues (`Module.End.eigenvectors_linearIndependent'`).

```lean
theorem linearIndependent_word_countFun {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) :
    LinearIndependent K (fun α : CountFun d n => L.word (countWord d α.1) Ω)
```

### C.3. The basis and its dimension

**`LadderSystem.span_word_countFun_eq_vacuumSpan`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L305).

> The occupation-number family spans `vacuumSpan L Ω n`.

```lean
lemma span_word_countFun_eq_vacuumSpan (Ω : V) (n : ℕ) :
    Submodule.span K (Set.range fun α : CountFun d n => L.word (countWord d α.1) Ω)
      = L.vacuumSpan Ω n
```

**`LadderSystem.vacuumBasis`**, a def, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L326).

> A basis of `vacuumSpan L Ω n` indexed by degree-`n` occupation-count functions.

```lean
noncomputable def vacuumBasis {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) :
    Basis (CountFun d n) K (L.vacuumSpan Ω n)
```

**`LadderSystem.vacuumBasis_apply`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L331).

```lean
lemma vacuumBasis_apply {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) (α : CountFun d n) :
    (vacuumBasis L P n α : V) = L.word (countWord d α.1) Ω
```

**`LadderSystem.finrank_vacuumSpan_eq_choose`**, a theorem, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L338). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dimension of `vacuumSpan L Ω n` is `(d+n-1).choose n`, the degeneracy of the `n`-th level
> of a `d`-mode bosonic system.

```lean
theorem finrank_vacuumSpan_eq_choose {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) :
    Module.finrank K (L.vacuumSpan Ω n) = (d + n - 1).choose n
```

**`LadderSystem.finiteDimensional_vacuumSpan`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L342).

```lean
lemma finiteDimensional_vacuumSpan {Ω : V} (P : L.HasVacuum Ω) (n : ℕ) :
    FiniteDimensional K (L.vacuumSpan Ω n)
```

**`LadderSystem.vacuumSpan_ne_bot`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean#L346).

```lean
lemma vacuumSpan_ne_bot {Ω : V} (P : L.HasVacuum Ω) (hd : 0 < d) (n : ℕ) :
    L.vacuumSpan Ω n ≠ ⊥
```

## Depends on

- [Vacuum states and creation-operator words](vacuum.md)

## Sources

- [PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LadderSystem/OccupationBasis.lean)
