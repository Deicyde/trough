---
declaration: module
origin: cited
lean: SuperSymmetry.SU5.ChargeSpectrum, SuperSymmetry.SU5.ChargeSpectrum.eq_of_parts, SuperSymmetry.SU5.ChargeSpectrum.eq_iff, SuperSymmetry.SU5.ChargeSpectrum.toProd, SuperSymmetry.SU5.ChargeSpectrum.hasSubset, SuperSymmetry.SU5.ChargeSpectrum.hasSSubset, SuperSymmetry.SU5.ChargeSpectrum.subsetDecidable, SuperSymmetry.SU5.ChargeSpectrum.subset_def
statement: formalized
proof: formalized
---

# Charge Spectrum

The module `Physlib.Particles.SuperSymmetry.SU5.ChargeSpectrum.Basic`, [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean): 44 declarations (2 instances with no name), 7 with a docstring.

## i. Overview

> In this module we define the charge spectrum of a `SU(5)` SUSY GUT theory with
> additional charges (usually `U(1)`) valued in `𝓩` satisfying the condition of:
> - The optional existence of a `Hd` particle in the `bar 5` representation.
> - The optional existence of a `Hu` particle in the `5` representation.
> - The optional existence of matter in the `bar 5` representation.
> - The optional existence of matter in the `10` representation.
>
> The charge spectrum contains the information of the *unique* charges of each type of particle
> present in theory. Importantly, the charge spectrum does not contain information
> about the multiplicity of those charges.
>
> With just the charge spectrum of the theory it is possible to put a number of constraints
> on the theory, most notably phenomenological constraints.
>
> By keeping the presence of `Hd` and `Hu` optional, we can define a number of useful properties
> of the charge spectrum, which can help in searching for viable theories.

## ii. Key results

> - `ChargeSpectrum 𝓩` : The type of charge spectra with charges of type `𝓩`, which is usually
>   `ℤ`.

## iv. References

> * None — these charge spectra were created specifically for the purpose of
>   Physlib; there is no external reference.

## A. The definition of the charge spectrum

**`SuperSymmetry.SU5.ChargeSpectrum`**, a structure, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L83).

> The type such that an element corresponds to the collection of
>   charges associated with the matter content of the theory.
>   The order of charges is implicitly taken to be `qHd`, `qHu`, `Q5`, `Q10`.
>
>   The `Q5` and `Q10` charges are represented by `Finset` rather than
>   `Multiset`, so multiplicity is not included.
>
>   This is defined for a general type `𝓩`, which could be e.g.
> - `ℤ` in the case of `U(1)`,
> - `ℤ × ℤ` in the case of `U(1) × U(1)`,
> - `Fin 2` in the case of `ℤ₂` etc.

```lean
structure ChargeSpectrum (𝓩 : Type := ℤ) where
  /-- The charge of the `Hd` particle. -/
  qHd : Option 𝓩
  /-- The negative of the charge of the `Hu` particle. That is to say,
    the charge of the `Hu` when considered in the 5-bar representation. -/
  qHu : Option 𝓩
  /-- The finite set of charges of the matter fields in the `Q5` representation. -/
  Q5 : Finset 𝓩
  /-- The finite set of charges of the matter fields in the `Q10` representation. -/
  Q10 : Finset 𝓩
```

### A.1. Extensionality properties

> We prove extensionality properties for `ChargeSpectrum 𝓩`, that is
> conditions of when two elements of `ChargeSpectrum 𝓩` are equal.
> We also show that when `𝓩` has decidable equality, so does `ChargeSpectrum 𝓩`.

**`SuperSymmetry.SU5.ChargeSpectrum.eq_of_parts`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L108).

```lean
lemma eq_of_parts {x y : ChargeSpectrum 𝓩} (h1 : x.qHd = y.qHd) (h2 : x.qHu = y.qHu)
    (h3 : x.Q5 = y.Q5) (h4 : x.Q10 = y.Q10) : x = y
```

**`SuperSymmetry.SU5.ChargeSpectrum.eq_iff`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L114).

```lean
lemma eq_iff {x y : ChargeSpectrum 𝓩} :
    x = y ↔ x.qHd = y.qHd ∧ x.qHu = y.qHu ∧ x.Q5 = y.Q5 ∧ x.Q10 = y.Q10
```

**An instance with no name**, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L119).

```lean
instance [DecidableEq 𝓩] : DecidableEq (ChargeSpectrum 𝓩)
```

### A.2. Relation to products

> We show that `ChargeSpectrum 𝓩` is equivalent to the product
> `Option 𝓩 × Option 𝓩 × Finset 𝓩 × Fin 𝓩`.
>
> In an old implementation this was definitionally true, it is not so now.

**`SuperSymmetry.SU5.ChargeSpectrum.toProd`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L135).

> The explicit casting of a term of type `Charges 𝓩` to a term of
> `Option 𝓩 × Option 𝓩 × Finset 𝓩 × Finset 𝓩`.

```lean
def toProd : ChargeSpectrum 𝓩 ≃ Option 𝓩 × Option 𝓩 × Finset 𝓩 × Finset 𝓩
```

### A.3. Rendering

**An instance with no name**, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L147).

```lean
unsafe instance [Repr 𝓩] : Repr (ChargeSpectrum 𝓩)
```

## B. The subset relation

> We define a `HasSubset` and `HasSSubset` instance on `ChargeSpectrum 𝓩`.

**`SuperSymmetry.SU5.ChargeSpectrum.hasSubset`**, an instance, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L164).

```lean
instance hasSubset : HasSubset (ChargeSpectrum 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.hasSSubset`**, an instance, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L171).

```lean
instance hasSSubset : HasSSubset (ChargeSpectrum 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.subsetDecidable`**, an instance, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L174).

```lean
instance subsetDecidable [DecidableEq 𝓩] (x y : ChargeSpectrum 𝓩) : Decidable (x ⊆ y)
```

**`SuperSymmetry.SU5.ChargeSpectrum.subset_def`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L177).

```lean
lemma subset_def {x y : ChargeSpectrum 𝓩} : x ⊆ y ↔ x.qHd.toFinset ⊆ y.qHd.toFinset ∧
    x.qHu.toFinset ⊆ y.qHu.toFinset ∧ x.Q5 ⊆ y.Q5 ∧ x.Q10 ⊆ y.Q10
```

**`SuperSymmetry.SU5.ChargeSpectrum.subset_refl`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L182).

```lean
lemma subset_refl (x : ChargeSpectrum 𝓩) : x ⊆ x
```

**`Option.toFinset_inj`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L184).

```lean
lemma _root_.Option.toFinset_inj {x y : Option 𝓩} :
    x = y ↔ x.toFinset = y.toFinset
```

**`SuperSymmetry.SU5.ChargeSpectrum.subset_trans`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L188).

```lean
lemma subset_trans {x y z : ChargeSpectrum 𝓩} (hxy : x ⊆ y) (hyz : y ⊆ z) : x ⊆ z
```

**`SuperSymmetry.SU5.ChargeSpectrum.subset_antisymm`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L193).

```lean
lemma subset_antisymm {x y : ChargeSpectrum 𝓩} (hxy : x ⊆ y) (hyx : y ⊆ x) : x = y
```

## C. The empty charge spectrum

**`SuperSymmetry.SU5.ChargeSpectrum.emptyInst`**, an instance, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L206).

```lean
instance emptyInst : EmptyCollection (ChargeSpectrum 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.empty_eq`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L209).

```lean
lemma empty_eq : (∅ : ChargeSpectrum 𝓩) = ⟨none, none, {}, {}⟩
```

**`SuperSymmetry.SU5.ChargeSpectrum.empty_subset`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L212).

```lean
lemma empty_subset (x : ChargeSpectrum 𝓩) : ∅ ⊆ x
```

**`SuperSymmetry.SU5.ChargeSpectrum.subset_of_empty_iff_empty`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L216).

```lean
lemma subset_of_empty_iff_empty {x : ChargeSpectrum 𝓩} :
    x ⊆ ∅ ↔ x = ∅
```

**`SuperSymmetry.SU5.ChargeSpectrum.empty_qHd`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L223).

```lean
lemma empty_qHd : (∅ : ChargeSpectrum 𝓩).qHd = none
```

**`SuperSymmetry.SU5.ChargeSpectrum.empty_qHu`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L227).

```lean
lemma empty_qHu : (∅ : ChargeSpectrum 𝓩).qHu = none
```

**`SuperSymmetry.SU5.ChargeSpectrum.empty_Q5`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L231).

```lean
lemma empty_Q5 : (∅ : ChargeSpectrum 𝓩).Q5 = ∅
```

**`SuperSymmetry.SU5.ChargeSpectrum.empty_Q10`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L235).

```lean
lemma empty_Q10 : (∅ : ChargeSpectrum 𝓩).Q10 = ∅
```

## D. The cardinality of a charge spectrum

**`SuperSymmetry.SU5.ChargeSpectrum.card`**, a def, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L246).

> The cardinality of a `Charges` is defined to be the sum of the cardinalities
> of each of the underlying finite sets of charges, with `Option ℤ` turned to finsets.

```lean
def card (x : ChargeSpectrum 𝓩) : Nat
```

**`SuperSymmetry.SU5.ChargeSpectrum.card_empty`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L250).

```lean
lemma card_empty : card (∅ : ChargeSpectrum 𝓩) = 0
```

**`SuperSymmetry.SU5.ChargeSpectrum.card_mono`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L253).

```lean
lemma card_mono {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) : card x ≤ card y
```

**`SuperSymmetry.SU5.ChargeSpectrum.eq_of_subset_card`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L261).

```lean
lemma eq_of_subset_card {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) (hcard : card x = card y) : x = y
```

## E. The power set of a charge spectrum

**`Option.powerset`**, a def, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L283).

> The powerset of `x : Option 𝓩` defined as `{none}` if `x` is `none`
> and `{none, some y}` is `x` is `some y`.

```lean
def _root_.Option.powerset (x : Option 𝓩) : Finset (Option 𝓩)
```

**`Option.mem_powerset_iff`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L289).

```lean
lemma _root_.Option.mem_powerset_iff {x : Option 𝓩} (y : Option 𝓩) :
    y ∈ x.powerset ↔ y.toFinset ⊆ x.toFinset
```

**`SuperSymmetry.SU5.ChargeSpectrum.powerset`**, a def, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L295).

> The powerset of a charge spectrum. Given a charge spectrum `x : ChargeSpectrum 𝓩`
> its powerset is the finite set of all `ChargeSpectrum 𝓩` which are subsets of `x`.

```lean
def powerset (x : ChargeSpectrum 𝓩) : Finset (ChargeSpectrum 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_powerset_iff`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L299).

```lean
lemma mem_powerset_iff {x y : ChargeSpectrum 𝓩} :
    x ∈ powerset y ↔
    x.qHd ∈ y.qHd.powerset ∧
    x.qHu ∈ y.qHu.powerset ∧
    x.Q5 ∈ y.Q5.powerset ∧
    x.Q10 ∈ y.Q10.powerset
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_powerset_iff_subset`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L308).

```lean
lemma mem_powerset_iff_subset {x y : ChargeSpectrum 𝓩} :
    x ∈ powerset y ↔ x ⊆ y
```

**`SuperSymmetry.SU5.ChargeSpectrum.self_mem_powerset`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L312).

```lean
lemma self_mem_powerset (x : ChargeSpectrum 𝓩) :
    x ∈ powerset x
```

**`SuperSymmetry.SU5.ChargeSpectrum.empty_mem_powerset`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L315).

```lean
lemma empty_mem_powerset (x : ChargeSpectrum 𝓩) :
    ∅ ∈ powerset x
```

**`SuperSymmetry.SU5.ChargeSpectrum.powerset_of_empty`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L319).

```lean
lemma powerset_of_empty :
    powerset (∅ : ChargeSpectrum 𝓩) = {∅}
```

**`SuperSymmetry.SU5.ChargeSpectrum.powerset_mono`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L324).

```lean
lemma powerset_mono {x y : ChargeSpectrum 𝓩} :
    powerset x ⊆ powerset y ↔ x ⊆ y
```

**`SuperSymmetry.SU5.ChargeSpectrum.min_exists_inductive`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L335).

```lean
lemma min_exists_inductive (S : Finset (ChargeSpectrum 𝓩)) (hS : S ≠ ∅) :
    (n : ℕ) → (hn : S.card = n) →
    ∃ y ∈ S, powerset y ∩ S = {y}
```

**`SuperSymmetry.SU5.ChargeSpectrum.min_exists`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L349).

```lean
lemma min_exists (S : Finset (ChargeSpectrum 𝓩)) (hS : S ≠ ∅) :
    ∃ y ∈ S, powerset y ∩ S = {y}
```

## F. Finite sets of charge spectra with values

> We define the finite set of `ChargeSpectrum` with 5-bar and 10d representation
> charges in a given finite set.

**`SuperSymmetry.SU5.ChargeSpectrum.ofFinset`**, a def, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L364).

> Given `S5 S10 : Finset 𝓩` the finite set of charges associated with
> for which the 5-bar representation charges sit in `S5` and
> the 10d representation charges sit in `S10`.

```lean
def ofFinset (S5 S10 : Finset 𝓩) : Finset (ChargeSpectrum 𝓩)
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_ofFinset_iff`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L371).

```lean
lemma mem_ofFinset_iff {S5 S10 : Finset 𝓩} {x : ChargeSpectrum 𝓩} :
    x ∈ ofFinset S5 S10 ↔ x.qHd.toFinset ⊆ S5 ∧ x.qHu.toFinset ⊆ S5 ∧
      x.Q5 ⊆ S5 ∧ x.Q10 ⊆ S10
```

**`SuperSymmetry.SU5.ChargeSpectrum.mem_ofFinset_antitone`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L380).

```lean
lemma mem_ofFinset_antitone (S5 S10 : Finset 𝓩)
    {x y : ChargeSpectrum 𝓩} (h : x ⊆ y) (hy : y ∈ ofFinset S5 S10) :
    x ∈ ofFinset S5 S10
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofFinset_subset_of_subset`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L386).

```lean
lemma ofFinset_subset_of_subset {S5 S5' S10 S10' : Finset 𝓩}
    (h5 : S5 ⊆ S5') (h10 : S10 ⊆ S10') :
    ofFinset S5 S10 ⊆ ofFinset S5' S10'
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofFinset_univ`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L393).

```lean
lemma ofFinset_univ [Fintype 𝓩] (x : ChargeSpectrum 𝓩) :
    x ∈ ofFinset (Finset.univ : Finset 𝓩) (Finset.univ : Finset 𝓩)
```

### F.1. Cardinality of finite sets of charge spectra with values

**`SuperSymmetry.SU5.ChargeSpectrum.ofFinsetCard`**, a def, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L405).

> The cardinality of `ofFinset S5 S10`.

```lean
def ofFinsetCard (S5 S10 : Finset 𝓩) : ℕ
```

**`SuperSymmetry.SU5.ChargeSpectrum.ofFinset_card_eq_ofFinsetCard`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean#L408).

```lean
lemma ofFinset_card_eq_ofFinsetCard (S5 S10 : Finset 𝓩) :
    (ofFinset S5 S10).card = ofFinsetCard S5 S10
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/SU5/ChargeSpectrum/Basic.lean)
