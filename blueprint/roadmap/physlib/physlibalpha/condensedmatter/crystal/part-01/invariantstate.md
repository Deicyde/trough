---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.cubeUltrafilter, CondensedMatter.Crystal.cubeUltrafilter_le, CondensedMatter.Crystal.translationInvariantLimit, CondensedMatter.Crystal.translationInvariantLimit_invariant, CondensedMatter.QuasiLocal.Interaction.translationInvariantState, CondensedMatter.Crystal.translationInvariantState_invariant
statement: formalized
proof: formalized
---

# Translation invariant states of an infinite crystal

The module `PhyslibAlpha.CondensedMatter.Crystal.InvariantState`, [PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean): 6 declarations, 5 with a docstring.

> Every state of the quasi-local algebra of the crystal `ℤ^d` with a finite unit cell has a
> translation invariant limit state, and so does every thermodynamic limit state of an interaction.

## i. Overview

> The translations of the crystal `ℤ^d` act on its quasi-local algebra by `*`-automorphisms
> (`translationAction`). The averages of a state over the translations by the points of the cube
> `{0, …, n}^d` become invariant as `n → ∞`, because the cubes satisfy the Følner condition
> (`isRightFolner_boxes`). A limit point of the averages along an ultrafilter is therefore an
> invariant state of the infinite crystal. Applied to the thermodynamic limit state of a canonical
> ensemble, this gives a translation invariant state of the interacting infinite system, which is
> the input to the reduction of the many-body problem to momentum sectors.

## ii. Key results

> - `exists_translation_invariant_state` : every state has a translation invariant limit state.
> - `Interaction.translationInvariantState` : the translation invariant state of the canonical
>   ensemble of an interaction.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1,
>   Section 4.3.

## A. Invariant states of the crystal

**`CondensedMatter.Crystal.cubeUltrafilter`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean#L62).

> An ultrafilter on the sizes of the cubes, finer than the filter of large cubes.

```lean
def cubeUltrafilter : Ultrafilter ℕ
```

**`CondensedMatter.Crystal.cubeUltrafilter_le`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean#L64).

```lean
lemma cubeUltrafilter_le : (cubeUltrafilter : Filter ℕ) ≤ atTop
```

**`CondensedMatter.Crystal.translationInvariantLimit`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean#L68).

> **The translation invariant limit of a state of the crystal `ℤ^d`**: the limit of its
> averages over the translations by the points of the cubes.

```lean
def translationInvariantLimit (φ : AlgState (crystalAlgebra Ω₀ (Fin d → ℤ) F)) :
    AlgState (crystalAlgebra Ω₀ (Fin d → ℤ) F)
```

**`CondensedMatter.Crystal.translationInvariantLimit_invariant`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean#L76).

> **The translation invariant limit of a state is invariant under the translations.**

```lean
lemma translationInvariantLimit_invariant (φ : AlgState (crystalAlgebra Ω₀ (Fin d → ℤ) F))
    (a : Fin d → ℤ) (x : crystalAlgebra Ω₀ (Fin d → ℤ) F) :
    translationInvariantLimit Ω₀ φ (translationAction Ω₀ (Multiplicative.ofAdd a) x) =
      translationInvariantLimit Ω₀ φ x
```

**`CondensedMatter.QuasiLocal.Interaction.translationInvariantState`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean#L86).

> **The translation invariant state of the canonical ensemble** of an interaction on the crystal
> `ℤ^d`: the translation average of a thermodynamic limit state of the finite boxes.

```lean
def _root_.CondensedMatter.QuasiLocal.Interaction.translationInvariantState [Nonempty Ω₀]
    (I : Interaction (fun _ : CellSite (Fin d → ℤ) F => Ω₀)) (β : ℝ) :
    AlgState (crystalAlgebra Ω₀ (Fin d → ℤ) F)
```

**`CondensedMatter.Crystal.translationInvariantState_invariant`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean#L94).

> The translation invariant state of an interaction is invariant under the translations.

```lean
lemma translationInvariantState_invariant [Nonempty Ω₀]
    (I : Interaction (fun _ : CellSite (Fin d → ℤ) F => Ω₀)) (β : ℝ) (a : Fin d → ℤ)
    (x : crystalAlgebra Ω₀ (Fin d → ℤ) F) :
    I.translationInvariantState β (translationAction Ω₀ (Multiplicative.ofAdd a) x) =
      I.translationInvariantState β x
```

## Depends on

- [Boxes of a lattice are asymptotically translation invariant](folner.md)
- [The quasi-local algebra of an infinite crystal](quasilocal.md)
- [Thermodynamic limit states of an interaction](../../quasilocal/limitstate.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantState.lean)
