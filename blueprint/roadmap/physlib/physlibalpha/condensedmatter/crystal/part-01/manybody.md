---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.manyBodyRep, CondensedMatter.Crystal.translationIn, CondensedMatter.Crystal.manyBodyTranslation, CondensedMatter.Crystal.manyBodyTranslation_apply, CondensedMatter.Crystal.linearAut, CondensedMatter.Crystal.manyBodyRep_covariant, CondensedMatter.Crystal.commute_manyBodyRep, CondensedMatter.Crystal.commute_manyBodyTranslation
statement: formalized
proof: formalized
---

# Symmetry reduction of a many-body dynamics on an infinite crystal

The module `PhyslibAlpha.CondensedMatter.Crystal.ManyBody`, [PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean): 9 declarations, 8 with a docstring.

> The dynamics of an infinite crystal in a symmetric state is reduced by the sectors of total
> momentum, and the point symmetries relate the sectors in an orbit.

## i. Overview

> Take the quasi-local algebra `𝔄` of an infinite crystal, with its action of the cell symmetries
> by `*`-automorphisms, and a state `ω` invariant under a subgroup `H` of the cell symmetries that
> contains the translations. The GNS construction represents `H` unitarily on the Hilbert space of
> `ω`. The translations are a subgroup of `H` acting by `π`, and `H` acts by `ρ`; a symmetry `s`
> carries the translation by `a` to the translation by `A a`, which is the covariance required by
> the sector reduction of `SectorReduction`.
>
> Let a group `Δ`, such as the time translations, act on `𝔄` by `*`-automorphisms preserving `ω`
> and commuting with `H`: a translation invariant dynamics with the point symmetries. It acts on
> the GNS space by unitaries commuting with `π` and `ρ`. Therefore each unitary of the dynamics is
> reduced by the sectors of total momentum, and its restrictions to the sector of the momenta in `S`
> and to the sector of the momenta in `s • S` are unitarily equivalent, with the same spectrum, for
> every symmetry `s` in `H`. The statement is about arbitrary interacting many-body dynamics: it
> uses nothing but the symmetry.

## ii. Key results

> - `manyBodyRep` : the unitary representation of the symmetries on the GNS space.
> - `manyBodyRep_covariant` : the translations and the symmetries are covariant.
> - `spectrum_sectorOp_eq_manyBody` : the symmetry reduction of the spectrum of an invariant dynamics
>   to the sectors of total momentum.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1,
>   Section 2.3.

## A. The representation on the GNS space

**`CondensedMatter.Crystal.manyBodyRep`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L76).

> **The unitary representation of the symmetries on the GNS space** of an invariant state.

```lean
def manyBodyRep : H →* unitary (ω.GNS →L[ℂ] ω.GNS)
```

**`CondensedMatter.Crystal.translationIn`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L82).

> The translations as elements of the symmetry subgroup.

```lean
def translationIn : Multiplicative G →* H
```

**`CondensedMatter.Crystal.manyBodyTranslation`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L87).

> The translation representation on the GNS space.

```lean
def manyBodyTranslation : Multiplicative G →* unitary (ω.GNS →L[ℂ] ω.GNS)
```

**`CondensedMatter.Crystal.manyBodyTranslation_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L95).

```lean
lemma manyBodyTranslation_apply (a : Multiplicative G) :
    manyBodyTranslation H ω hω htrans a = manyBodyRep H ω hω (translationIn H htrans a)
```

**`CondensedMatter.Crystal.linearAut`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L99).

> The action of a symmetry on the lattice of translations, through its linear part.

```lean
def linearAut : H →* MulAut (Multiplicative G)
```

**`CondensedMatter.Crystal.manyBodyRep_covariant`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L110).

> **The translations and the symmetries are covariant on the GNS space.**

```lean
lemma manyBodyRep_covariant :
    UnitaryRep.IsCovariantRep (linearAut H) (manyBodyTranslation H ω hω htrans)
      (manyBodyRep H ω hω)
```

## B. The symmetry reduction

**`CondensedMatter.Crystal.commute_manyBodyRep`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L136).

> A dynamics commuting with a symmetry is implemented by an operator commuting with the
> unitary implementing the symmetry.

```lean
lemma commute_manyBodyRep (s : H) :
    Commute ((manyBodyRep H ω hω s : unitary (ω.GNS →L[ℂ] ω.GNS)) : ω.GNS →L[ℂ] ω.GNS)
      (AlgState.gnsAut τ hτ)
```

**`CondensedMatter.Crystal.commute_manyBodyTranslation`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L147).

> A dynamics commuting with the symmetries commutes with the translation representation.

```lean
lemma commute_manyBodyTranslation (a : Multiplicative G) :
    Commute ((manyBodyTranslation H ω hω htrans a : unitary (ω.GNS →L[ℂ] ω.GNS)) :
      ω.GNS →L[ℂ] ω.GNS) (AlgState.gnsAut τ hτ)
```

**`CondensedMatter.Crystal.spectrum_sectorOp_eq_manyBody`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean#L161).

> **Symmetry reduction of a many-body dynamics on an infinite crystal.** Let `ω` be a state of the
> quasi-local algebra invariant under a group `H` of cell symmetries containing the translations,
> and `τ` an automorphism preserving `ω` and commuting with `H`: a time evolution. Then the unitary
> implementing `τ` is reduced by the sectors of total momentum, and its restriction to the sector of
> the momenta in a set `S` has the same spectrum as its restriction to the sector of the momenta in
> the image of `S` under any symmetry `s` in `H`.

```lean
lemma spectrum_sectorOp_eq_manyBody (s : H)
    {S : Set (PontryaginDual (Multiplicative G))} (hS : MeasurableSet S) :
    spectrum ℂ (UnitaryRep.sectorOp
        (commute_manyBodyTranslation H ω hω htrans τ hτ hcomm) S) =
      spectrum ℂ (UnitaryRep.sectorOp
        (commute_manyBodyTranslation H ω hω htrans τ hτ hcomm)
        (UnitaryRep.dualAct (linearAut H) s '' S))
```

## Depends on

- [The quasi-local algebra of an infinite crystal](quasilocal.md)
- [Symmetry reduction of translation-invariant operators to momentum sectors](../../../probabilistictheory/representation/sectorreduction.md)
- [The GNS representation of a state on a unital `*`-algebra](../../../probabilistictheory/staralgebra/gns.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/ManyBody.lean)
