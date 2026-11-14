---
declaration: module
origin: cited
lean: CondensedMatter.measurePreserving_count, CondensedMatter.SiteSpace, CondensedMatter.siteTranslationPerm, CondensedMatter.siteTranslation, CondensedMatter.siteSymmetryPerm, CondensedMatter.siteSymmetry, CondensedMatter.latticeAut, CondensedMatter.siteSymmetryPerm_translation
statement: formalized
proof: formalized
---

# The translations and symmetries of a crystal on `ℓ²` of its sites

The module `PhyslibAlpha.CondensedMatter.Bloch.SiteRepresentation`, [PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean): 13 declarations (3 instances with no name), 11 with a docstring.

> The space of square-summable functions on the sites of a crystal carries the translations and the
> bond-preserving symmetries as a covariant unitary representation.

## i. Overview

> The Hilbert space `ℓ²(C.Site)` of a crystal is `L²` of the counting measure on its sites. The
> translations act on the sites by permutations, and so do the bond-preserving symmetries. Every
> permutation preserves the counting measure, so each group acts unitarily by composition: the
> Koopman representation. The two actions are compatible: a symmetry with linear part `A` carries
> the translation by `a` to the translation by `A a`. This is exactly the covariance of
> `PointCovariance`. The Hilbert space needs no choice of orbitals, and covers any number of sites
> per cell.
>
> Consequently the sector reduction of `SectorReduction` applies to every bounded operator on
> `ℓ²(C.Site)` that commutes with the translations and the symmetries: the adjacency operator of the
> bond graph, any hopping Hamiltonian with symmetric amplitudes, or the unitary group of a
> Schrödinger evolution.

## ii. Key results

> - `siteTranslation`, `siteSymmetry` : the actions on `ℓ²(C.Site)`.
> - `siteTranslation_covariant` : the covariance of the two representations.
> - `spectrum_sectorOp_eq_site` : the symmetry reduction of the spectrum of an invariant operator
>   to the sectors of momentum.

## iv. References

> * None.

## A. Counting measure on the sites

**An instance with no name**, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L67).

> Every set of sites is measurable.

```lean
instance : MeasurableSpace (CellSite G F)
```

**An instance with no name**, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L69).

```lean
instance : MeasurableSingletonClass (CellSite G F)
```

**An instance with no name**, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L71).

```lean
instance [Countable G] [Countable F] : Countable (CellSite G F)
```

**`CondensedMatter.measurePreserving_count`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L76).

> A permutation of a countable set preserves the counting measure.

```lean
lemma measurePreserving_count {X : Type*} [MeasurableSpace X] [MeasurableSingletonClass X]
    [Countable X] (e : Equiv.Perm X) :
    MeasurePreserving e (Measure.count : Measure X) Measure.count
```

## B. The representations

**`CondensedMatter.SiteSpace`**, an abbrev, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L97).

> The square-summable functions on the sites of a crystal built from a unit cell.

```lean
abbrev SiteSpace (G F : Type*)
```

**`CondensedMatter.siteTranslationPerm`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L101).

> The translations act on the sites by permutations.

```lean
def siteTranslationPerm (G F : Type*) [AddCommGroup G] :
    Multiplicative G →* Equiv.Perm (CellSite G F)
```

**`CondensedMatter.siteTranslation`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L106).

> **The translation representation** on `ℓ²` of the sites: `(U_a ψ)(x) = ψ(-a + x)`.

```lean
def siteTranslation (G F : Type*) [AddCommGroup G] [Countable G] [Countable F] :
    Multiplicative G →* unitary (SiteSpace G F →L[ℂ] SiteSpace G F)
```

**`CondensedMatter.siteSymmetryPerm`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L114).

> The bond-preserving symmetries act on the sites by permutations.

```lean
def siteSymmetryPerm : g.symmetries →* Equiv.Perm (CellSite G F)
```

**`CondensedMatter.siteSymmetry`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L118).

> **The symmetry representation** on `ℓ²` of the sites: `(U_s ψ)(x) = ψ(s⁻¹ • x)`.

```lean
def siteSymmetry : g.symmetries →* unitary (SiteSpace G F →L[ℂ] SiteSpace G F)
```

**`CondensedMatter.latticeAut`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L123).

> The action of a symmetry on the lattice of translations, through its linear part.

```lean
def latticeAut : g.symmetries →* MulAut (Multiplicative G)
```

**`CondensedMatter.siteSymmetryPerm_translation`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L133).

> A symmetry moves a translated site to the correspondingly translated image: the permutations
> of the sites satisfy `s ∘ τ_a = τ_{A a} ∘ s`.

```lean
lemma siteSymmetryPerm_translation (s : g.symmetries) (a : Multiplicative G) :
    siteSymmetryPerm g s * siteTranslationPerm G F a =
      siteTranslationPerm G F (latticeAut g s a) * siteSymmetryPerm g s
```

**`CondensedMatter.siteTranslation_covariant`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L149).

> **The translations and the bond-preserving symmetries form a covariant representation on
> `ℓ²` of the sites.**

```lean
lemma siteTranslation_covariant :
    UnitaryRep.IsCovariantRep (latticeAut g) (siteTranslation G F) (siteSymmetry g)
```

## C. Symmetry reduction

**`CondensedMatter.spectrum_sectorOp_eq_site`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean#L183).

> **Symmetry reduction on a crystal.** Let `T` be a bounded operator on `ℓ²` of the sites of a
> crystal, commuting with the translations and with the bond-preserving symmetries. Its restriction
> to the sector of total momenta in a set `S` of characters is unitarily equivalent to its restriction
> to the sector of momenta in the image of `S` under any symmetry, by the symmetry itself. In
> particular their spectra agree.

```lean
lemma spectrum_sectorOp_eq_site {T : SiteSpace G F →L[ℂ] SiteSpace G F}
    (hTπ : ∀ a, Commute ((siteTranslation G F a : unitary _) : SiteSpace G F →L[ℂ] SiteSpace G F) T)
    (hTρ : ∀ s, Commute ((siteSymmetry g s : unitary _) : SiteSpace G F →L[ℂ] SiteSpace G F) T)
    (s : g.symmetries) {S : Set (PontryaginDual (Multiplicative G))} (hS : MeasurableSet S) :
    spectrum ℂ (UnitaryRep.sectorOp hTπ S) =
      spectrum ℂ (UnitaryRep.sectorOp hTπ (UnitaryRep.dualAct (latticeAut g) s '' S))
```

## Depends on

- [Symmetries of a crystal graph](../crystal/part-01/symmetry.md)
- [The Koopman representation of a measure-preserving action](../../probabilistictheory/representation/koopman.md)
- [Symmetry reduction of translation-invariant operators to momentum sectors](../../probabilistictheory/representation/sectorreduction.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/SiteRepresentation.lean)
