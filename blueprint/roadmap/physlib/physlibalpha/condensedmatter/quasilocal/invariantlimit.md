---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.invariantLimit, CondensedMatter.QuasiLocal.invariantLimit_invariant, CondensedMatter.QuasiLocal.exists_invariant_state, CondensedMatter.QuasiLocal.Interaction.invariantLimitState, CondensedMatter.QuasiLocal.Interaction.invariantLimitState_invariant
statement: formalized
proof: formalized
---

# Symmetric thermodynamic limit states

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.InvariantLimit`, [PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean): 5 declarations, 5 with a docstring.

> Averaging the thermodynamic limit state of a lattice system over a group of site symmetries gives
> a state of the infinite system that is invariant under the group.

## i. Overview

> The Gibbs states of finite boxes break the symmetries of the lattice, because a box has a
> boundary. Their limit points need not be invariant, and indeed are not in a phase with broken
> symmetry. A limit point that is invariant is obtained by averaging over the group before taking
> the limit: if the finite sets `F i` of group elements are asymptotically invariant (a Følner
> condition), the limit of the averages of any state over them is invariant under the group.
>
> For a lattice system with site symmetry group `Γ`, for instance the translations of a crystal, the
> quasi-local algebra carries the action `symAction` of `Γ` by `*`-automorphisms. This gives a
> translation invariant state of the infinite crystal, which is the hypothesis of the reduction of
> the many-body problem to momentum sectors.

## ii. Key results

> - `exists_invariant_state` : every state of the quasi-local algebra of a uniform lattice system has
>   an invariant limit state.
> - `Interaction.invariantLimitState` : the invariant state obtained from the canonical ensemble of
>   an interaction.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 6.2.3.

## A. Invariant states of a uniform lattice system

**`CondensedMatter.QuasiLocal.invariantLimit`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean#L69).

> **The invariant limit of a state of a uniform lattice system**: the Følner limit of its
> averages over the site symmetries.

```lean
def invariantLimit (φ : AlgState (uniformNet (S := S) Ω₀).Quasilocal) (F : ι → Finset Γ)
    (hne : ∀ i, (F i).Nonempty) (𝒰 : Ultrafilter ι) :
    AlgState (uniformNet (S := S) Ω₀).Quasilocal
```

**`CondensedMatter.QuasiLocal.invariantLimit_invariant`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean#L76).

> **The invariant limit of a state is invariant under the site symmetries.**

```lean
lemma invariantLimit_invariant (φ : AlgState (uniformNet (S := S) Ω₀).Quasilocal)
    (F : ι → Finset Γ) (hne : ∀ i, (F i).Nonempty) (𝒰 : Ultrafilter ι)
    (hF : IsRightFolner F 𝒰) (γ : Γ) (a : (uniformNet (S := S) Ω₀).Quasilocal) :
    invariantLimit φ F hne 𝒰 (symAction (Ω₀ := Ω₀) γ a) = invariantLimit φ F hne 𝒰 a
```

**`CondensedMatter.QuasiLocal.exists_invariant_state`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean#L84).

> **Existence of invariant states**: if the finite sets of site symmetries are asymptotically
> invariant, every state of the quasi-local algebra has an invariant limit state.

```lean
lemma exists_invariant_state (φ : AlgState (uniformNet (S := S) Ω₀).Quasilocal)
    (F : ι → Finset Γ) (hne : ∀ i, (F i).Nonempty) (𝒰 : Ultrafilter ι)
    (hF : IsRightFolner F 𝒰) :
    ∃ ψ : AlgState (uniformNet (S := S) Ω₀).Quasilocal,
      ∀ (γ : Γ) a, ψ (symAction (Ω₀ := Ω₀) γ a) = ψ a
```

## B. The ensembles of an interaction

**`CondensedMatter.QuasiLocal.Interaction.invariantLimitState`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean#L97).

> **The symmetric thermodynamic limit state of the canonical ensemble** of an interaction on a
> uniform lattice system.

```lean
def Interaction.invariantLimitState (I : Interaction (fun _ : S => Ω₀)) (β : ℝ)
    (𝒰₀ : Ultrafilter (Finset S)) (h𝒰₀ : (𝒰₀ : Filter (Finset S)) ≤ atTop) (F : ι → Finset Γ)
    (hne : ∀ i, (F i).Nonempty) (𝒰 : Ultrafilter ι) :
    AlgState (uniformNet (S := S) Ω₀).Quasilocal
```

**`CondensedMatter.QuasiLocal.Interaction.invariantLimitState_invariant`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean#L104).

> The symmetric limit state of an interaction is invariant under the site symmetries.

```lean
lemma Interaction.invariantLimitState_invariant (I : Interaction (fun _ : S => Ω₀)) (β : ℝ)
    (𝒰₀ : Ultrafilter (Finset S)) (h𝒰₀ : (𝒰₀ : Filter (Finset S)) ≤ atTop) (F : ι → Finset Γ)
    (hne : ∀ i, (F i).Nonempty) (𝒰 : Ultrafilter ι) (hF : IsRightFolner F 𝒰) (γ : Γ)
    (a : (uniformNet (S := S) Ω₀).Quasilocal) :
    I.invariantLimitState β 𝒰₀ h𝒰₀ F hne 𝒰 (symAction (Ω₀ := Ω₀) γ a) =
      I.invariantLimitState β 𝒰₀ h𝒰₀ F hne 𝒰 a
```

## Depends on

- [Thermodynamic limit states of an interaction](limitstate.md)
- [Symmetries of the quantum net](symmetry.md)
- [Invariant states by Følner averaging](../../probabilistictheory/staralgebra/invariant.md)

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/InvariantLimit.lean)
