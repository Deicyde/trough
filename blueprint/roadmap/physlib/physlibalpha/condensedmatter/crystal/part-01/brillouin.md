---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.BrillouinZone, CondensedMatter.Crystal.dualMap, CondensedMatter.Crystal.dualMap_apply, CondensedMatter.Crystal.dualMap_refl, CondensedMatter.Crystal.dualMap_trans, CondensedMatter.Crystal.smul_apply, CondensedMatter.Crystal.translation_smul_brillouin, CondensedMatter.Crystal.PeriodicGraph.symmetryAction
statement: formalized
proof: formalized
---

# Symmetries of a crystal acting on its Brillouin zone

The module `PhyslibAlpha.CondensedMatter.Crystal.Brillouin`, [PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean): 20 declarations (2 instances with no name), 11 with a docstring.

> The symmetries of a crystal act on the crystal momenta, the translations trivially.

## i. Overview

> The crystal momenta of a crystal with translation group `G` are the characters of `G`: the
> Brillouin zone. A symmetry `s = (A, σ, b)` sends a plane wave of momentum `χ` to a plane wave of
> momentum `χ ∘ A⁻¹`, so the symmetries act on the Brillouin zone through their linear parts. This
> is an action of the whole group `CellSymmetry G F` of the crystal, for any number of sites per
> cell. Translations have the trivial linear part and act trivially, so the action descends to the
> point group, the quotient by the translations.
>
> The stabilizer of a momentum `χ` in the group of symmetries is the *little group* of `χ`. It
> contains all translations. Its image in the point group is the *little co-group*. At a generic
> momentum the little co-group is trivial, and at a high-symmetry momentum it is large. The orbits of
> the point group in the Brillouin zone are the classes of equivalent momenta. The orbit space is the
> irreducible Brillouin zone: a band structure of a symmetric crystal is a function on it.

## ii. Key results

> - `BrillouinZone` : the group of characters of the translations.
> - `CellSymmetry.instMulActionBrillouinZone` : the action of the symmetries on crystal momenta.
> - `PeriodicGraph.pointAction` : the action of the point group on the Brillouin zone.
> - `PeriodicGraph.littleGroup` : the stabilizer of a momentum among the bond-preserving symmetries.
> - `PeriodicGraph.IrreducibleZone` : the orbit space of the Brillouin zone under the point group.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. The action of the symmetries

**`CondensedMatter.Crystal.BrillouinZone`**, an abbrev, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L62).

> The Brillouin zone of a crystal with translation group `G`: the crystal momenta, which are the
> characters of `G`.

```lean
abbrev BrillouinZone (G : Type*) [AddCommGroup G] [TopologicalSpace G]
```

**`CondensedMatter.Crystal.dualMap`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L66).

> A lattice automorphism acts on a character by precomposition.

```lean
noncomputable def dualMap (A : G ≃+ G) (χ : BrillouinZone G) : BrillouinZone G
```

**`CondensedMatter.Crystal.dualMap_apply`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L76).

```lean
lemma dualMap_apply (A : G ≃+ G) (χ : BrillouinZone G) (a : G) :
    dualMap A χ (Multiplicative.ofAdd a) = χ (Multiplicative.ofAdd (A a))
```

**`CondensedMatter.Crystal.dualMap_refl`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L79).

```lean
lemma dualMap_refl (χ : BrillouinZone G) : dualMap (AddEquiv.refl G) χ = χ
```

**`CondensedMatter.Crystal.dualMap_trans`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L81).

```lean
lemma dualMap_trans (A B : G ≃+ G) (χ : BrillouinZone G) :
    dualMap B (dualMap A χ) = dualMap (B.trans A) χ
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L86).

> The symmetries of a crystal act on the crystal momenta: a symmetry with linear part `A` sends
> `χ` to `χ ∘ A⁻¹`.

```lean
noncomputable instance : MulAction (CellSymmetry G F) (BrillouinZone G)
```

**`CondensedMatter.Crystal.smul_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L94).

```lean
lemma smul_apply (s : CellSymmetry G F) (χ : BrillouinZone G) (a : G) :
    (s • χ) (Multiplicative.ofAdd a) = χ (Multiplicative.ofAdd (s.linear.symm a))
```

**`CondensedMatter.Crystal.translation_smul_brillouin`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L98).

> Translations act trivially on crystal momenta.

```lean
lemma translation_smul_brillouin (a : G) (χ : BrillouinZone G) :
    (CellSymmetry.translation a : CellSymmetry G F) • χ = χ
```

## B. The point group and the little groups

**`CondensedMatter.Crystal.PeriodicGraph.symmetryAction`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L107).

> The bond-preserving symmetries act on the Brillouin zone by permutations.

```lean
noncomputable def symmetryAction : g.symmetries →* Equiv.Perm (BrillouinZone G)
```

**`CondensedMatter.Crystal.PeriodicGraph.translations_le_ker_symmetryAction`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L110).

```lean
lemma translations_le_ker_symmetryAction :
    (CellSymmetry.translations G F).subgroupOf g.symmetries ≤ (symmetryAction g).ker
```

**`CondensedMatter.Crystal.PeriodicGraph.pointAction`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L118).

> **The point group acts on the Brillouin zone.**

```lean
noncomputable def pointAction : g.pointGroup →* Equiv.Perm (BrillouinZone G)
```

**An instance with no name**, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L121).

```lean
noncomputable instance : MulAction g.pointGroup (BrillouinZone G)
```

**`CondensedMatter.Crystal.PeriodicGraph.mk_smul`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L124).

```lean
lemma mk_smul (s : g.symmetries) (χ : BrillouinZone G) :
    (QuotientGroup.mk s : g.pointGroup) • χ = s • χ
```

**`CondensedMatter.Crystal.PeriodicGraph.littleGroup`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L129).

> The little group of a momentum: the bond-preserving symmetries that fix it. It contains all
> translations.

```lean
noncomputable def littleGroup (χ : BrillouinZone G) : Subgroup g.symmetries
```

**`CondensedMatter.Crystal.PeriodicGraph.littleCoGroup`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L133).

> The little co-group of a momentum: the elements of the point group that fix it.

```lean
noncomputable def littleCoGroup (χ : BrillouinZone G) : Subgroup g.pointGroup
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_littleGroup`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L136).

```lean
lemma mem_littleGroup (χ : BrillouinZone G) (s : g.symmetries) :
    s ∈ g.littleGroup χ ↔ s • χ = χ
```

**`CondensedMatter.Crystal.PeriodicGraph.translation_mem_littleGroup`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L139).

```lean
lemma translation_mem_littleGroup (χ : BrillouinZone G) (a : G) :
    (⟨CellSymmetry.translation a, g.translation_mem_symmetries a⟩ : g.symmetries) ∈
      g.littleGroup χ
```

**`CondensedMatter.Crystal.PeriodicGraph.littleGroup_eq_comap`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L145).

> The little group is the preimage of the little co-group.

```lean
lemma littleGroup_eq_comap (χ : BrillouinZone G) :
    g.littleGroup χ = (g.littleCoGroup χ).comap (QuotientGroup.mk' _)
```

## C. The irreducible zone

**`CondensedMatter.Crystal.PeriodicGraph.IrreducibleZone`**, an abbrev, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L155).

> The irreducible Brillouin zone: the momenta modulo the point group.

```lean
abbrev IrreducibleZone
```

**`CondensedMatter.Crystal.PeriodicGraph.irreducibleZone_mk_eq_iff`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean#L158).

> Momenta in the same orbit of the point group are identified in the irreducible zone.

```lean
lemma irreducibleZone_mk_eq_iff (χ ψ : BrillouinZone G) :
    (Quotient.mk (MulAction.orbitRel g.pointGroup (BrillouinZone G)) χ : g.IrreducibleZone) =
      Quotient.mk _ ψ ↔ ∃ p : g.pointGroup, p • ψ = χ
```

## Depends on

- [Symmetries of a crystal graph](symmetry.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Brillouin.lean)
