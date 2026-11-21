---
declaration: module
origin: cited
lean: ProbabilisticTheory.Interaction, ProbabilisticTheory.Interaction.labelsIn, ProbabilisticTheory.Interaction.termIn, ProbabilisticTheory.Interaction.incl_termIn, ProbabilisticTheory.Interaction.termIn_add, ProbabilisticTheory.Interaction.termIn_smul
statement: formalized
proof: formalized
---

# Interactions on a local net

The module `Physlib.ProbabilisticTheory.LocalNet.Interaction.Basic`, [Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean): 6 declarations, 6 with a docstring.

> An interaction is a family of local observables, each associated with a region of the net.

## i. Overview

> Extensive observables such as energy, magnetization and particle number can be expressed as
> sums of local terms. An interaction assigns a supporting region and an observable to each
> label. Each term can be included into any larger region and is taken to be zero when its
> support is not contained in the region.

## ii. Key results

> - `Interaction`: A family of local observables with specified supports.
> - `Interaction.termIn`: An interaction term expressed in a given region.
> - `Interaction.incl_termIn`: Compatibility with inclusions of regions.
> - `Interaction.termIn_add`: Compatibility with addition.
> - `Interaction.termIn_smul`: Compatibility with scalar multiplication.

## iv. References

## A. Interactions

**`ProbabilisticTheory.Interaction`**, a structure, [line 46](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L46).

> A family of local observables on `N`, indexed by `ι`, with specified supports.

```lean
structure ProbabilisticTheory.Interaction {R : Type*} [Preorder R]
    {A : R → ProbabilisticTheory} (N : LocalNet R A) (ι : Type*) where
  /-- The supporting region of each term. -/
  supp : ι → R
  /-- The observable associated with each term. -/
  term : ∀ i, (A (supp i)).Observables
```

## B. Interaction terms in a region

**`ProbabilisticTheory.Interaction.labelsIn`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L61).

> The labels of terms supported in `Λ`.

```lean
def labelsIn (Λ : R) : Set ι
```

**`ProbabilisticTheory.Interaction.termIn`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L65).

> The term `i` expressed in `Λ`, or zero if its support is not contained in `Λ`.

```lean
noncomputable def termIn (Λ : R) (i : ι) : (A Λ).Observables
```

**`ProbabilisticTheory.Interaction.incl_termIn`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L70).

> Including a term from `Λ` into `Λ'` agrees with evaluating it in `Λ'` whenever
> its support is contained in `Λ`, and gives zero otherwise.

```lean
lemma incl_termIn {Λ Λ' : R} (h : Λ ≤ Λ') (i : ι) :
    N.incl h (Φ.termIn Λ i) = (Φ.labelsIn Λ).indicator (Φ.termIn Λ') i
```

**`ProbabilisticTheory.Interaction.termIn_add`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L77).

> Evaluating interaction terms in a region preserves addition.

```lean
lemma termIn_add (s : ι → R) (t t' : ∀ i, (A (s i)).Observables) (Λ : R) (i : ι) :
    (⟨s, t + t'⟩ : Interaction N ι).termIn Λ i =
      (⟨s, t⟩ : Interaction N ι).termIn Λ i +
        (⟨s, t'⟩ : Interaction N ι).termIn Λ i
```

**`ProbabilisticTheory.Interaction.termIn_smul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L84).

> Evaluating interaction terms in a region preserves scalar multiplication.

```lean
lemma termIn_smul (s : ι → R) (c : ℝ) (t : ∀ i, (A (s i)).Observables) (Λ : R) (i : ι) :
    (⟨s, c • t⟩ : Interaction N ι).termIn Λ i =
      c • (⟨s, t⟩ : Interaction N ι).termIn Λ i
```

## Depends on

- [Local nets of observables](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean)
