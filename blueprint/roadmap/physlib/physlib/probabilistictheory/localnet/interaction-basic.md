---
declaration: module
origin: cited
lean: ProbabilisticTheory.Interaction, ProbabilisticTheory.Interaction.labelsIn, ProbabilisticTheory.Interaction.termIn, ProbabilisticTheory.Interaction.incl_termIn, ProbabilisticTheory.Interaction.termIn_add, ProbabilisticTheory.Interaction.termIn_smul
statement: formalized
proof: formalized
---

# Interactions on a local net

The module `Physlib.ProbabilisticTheory.LocalNet.Interaction.Basic`, [Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean): 6 declarations, 6 with a docstring.

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

**`ProbabilisticTheory.Interaction`**, a structure, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L49).

> A family of local observables on `N`, indexed by `ι`, with specified supports.

```lean
structure Interaction (N : LocalNet R A) (ι : Type*) where
  /-- The supporting region of each term. -/
  supp : ι → R
  /-- The observable associated with each term. -/
  term : ∀ i, A (supp i)
```

## B. Interaction terms in a region

**`ProbabilisticTheory.Interaction.labelsIn`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L62).

> The labels of terms supported in `Λ`.

```lean
def labelsIn (Λ : R) : Set ι
```

**`ProbabilisticTheory.Interaction.termIn`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L66).

> The term `i` expressed in `Λ`, or zero if its support is not contained in `Λ`.

```lean
noncomputable def termIn (Λ : R) (i : ι) : A Λ
```

**`ProbabilisticTheory.Interaction.incl_termIn`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L71).

> Including a term from `Λ` into `Λ'` agrees with evaluating it in `Λ'` whenever
> its support is contained in `Λ`, and gives zero otherwise.

```lean
lemma incl_termIn {Λ Λ' : R} (h : Λ ≤ Λ') (i : ι) :
    N.incl h (Φ.termIn Λ i) = (Φ.labelsIn Λ).indicator (Φ.termIn Λ') i
```

**`ProbabilisticTheory.Interaction.termIn_add`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L78).

> Evaluating interaction terms in a region preserves addition.

```lean
lemma termIn_add (s : ι → R) (t t' : ∀ i, A (s i)) (Λ : R) (i : ι) :
    (⟨s, t + t'⟩ : Interaction N ι).termIn Λ i =
      (⟨s, t⟩ : Interaction N ι).termIn Λ i +
        (⟨s, t'⟩ : Interaction N ι).termIn Λ i
```

**`ProbabilisticTheory.Interaction.termIn_smul`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean#L85).

> Evaluating interaction terms in a region preserves scalar multiplication.

```lean
lemma termIn_smul (s : ι → R) (c : ℝ) (t : ∀ i, A (s i)) (Λ : R) (i : ι) :
    (⟨s, c • t⟩ : Interaction N ι).termIn Λ i =
      c • (⟨s, t⟩ : Interaction N ι).termIn Λ i
```

## Depends on

- [Local nets of observables](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Basic.lean)
