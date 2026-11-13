---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.crystalAlgebra, CondensedMatter.Crystal.cellSymmetryAction, CondensedMatter.Crystal.translationHom, CondensedMatter.Crystal.translationAction, CondensedMatter.Crystal.cellSymmetryAction_translation_conj
statement: formalized
proof: formalized
---

# The quasi-local algebra of an infinite crystal

The module `PhyslibAlpha.CondensedMatter.Crystal.QuasiLocal`, [PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean): 5 declarations, 5 with a docstring.

> The quasi-local algebra of a crystal carries an action of its cell symmetries, the translations
> among them.

## i. Overview

> The sites of a crystal are the sites `⟨n, i⟩` of the cells `n`, a countable set, infinite for the
> translation group `ℤ^d`. If every site carries the same finite configuration space `Ω₀`, such as
> the two states of a spin, the observables of a finite set of sites form a matrix algebra, and the
> quasi-local algebra of the crystal is the direct limit over the finite regions.
>
> The group `CellSymmetry G F` of the crystal acts on its sites, so it acts on the quasi-local
> algebra by `*`-automorphisms. This group contains the translations as a normal subgroup, so the
> translations act as a subgroup of the automorphisms. A symmetry `s` and a translation `t_a`
> satisfy `s t_a s⁻¹ = t_{A a}` in the group, and the action respects this relation. Every bond
> preserving symmetry of a periodic graph is among the cell symmetries.

## ii. Key results

> - `crystalAlgebra` : the quasi-local algebra of a crystal.
> - `cellSymmetryAction` : the action of the cell symmetries by `*`-automorphisms.
> - `translationAction` : the action of the translations.
> - `cellSymmetryAction_translation_conj` : a symmetry carries the translation by `a` to the
>   translation by `A a`.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 6.1.

## A. The quasi-local algebra of a crystal

**`CondensedMatter.Crystal.crystalAlgebra`**, an abbrev, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean#L66).

> **The quasi-local algebra of an infinite crystal** whose sites all carry the finite
> configuration space `Ω₀`.

```lean
abbrev crystalAlgebra (G F : Type*) [DecidableEq (CellSite G F)]
```

## B. The symmetries and the translations

**`CondensedMatter.Crystal.cellSymmetryAction`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean#L72).

> **The cell symmetries of a crystal act on its quasi-local algebra** by `*`-automorphisms.

```lean
def cellSymmetryAction : CellSymmetry G F →* (crystalAlgebra Ω₀ G F ≃⋆ₐ[ℂ] crystalAlgebra Ω₀ G F)
```

**`CondensedMatter.Crystal.translationHom`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean#L76).

> The translations as cell symmetries.

```lean
def translationHom (G F : Type*) [AddCommGroup G] : Multiplicative G →* CellSymmetry G F
```

**`CondensedMatter.Crystal.translationAction`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean#L85).

> **The translations act on the quasi-local algebra** by `*`-automorphisms.

```lean
def translationAction : Multiplicative G →* (crystalAlgebra Ω₀ G F ≃⋆ₐ[ℂ] crystalAlgebra Ω₀ G F)
```

**`CondensedMatter.Crystal.cellSymmetryAction_translation_conj`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean#L89).

> **Covariance**: a cell symmetry carries the translation by `a` to the translation by `A a`.

```lean
lemma cellSymmetryAction_translation_conj (s : CellSymmetry G F) (a : G) :
    cellSymmetryAction Ω₀ s * cellSymmetryAction Ω₀ (CellSymmetry.translation a) *
        (cellSymmetryAction Ω₀ s)⁻¹ =
      cellSymmetryAction Ω₀ (CellSymmetry.translation (s.linear a))
```

## Depends on

- [Symmetries of a crystal graph](symmetry.md)
- [Symmetries of the quantum net](../../quasilocal/symmetry.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/QuasiLocal.lean)
