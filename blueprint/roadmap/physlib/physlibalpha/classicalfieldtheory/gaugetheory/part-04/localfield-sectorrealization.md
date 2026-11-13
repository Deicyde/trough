---
declaration: module
origin: cited
lean: GaugeFieldData.SectorAlgebra.Realization, GaugeFieldData.SectorAlgebra.Realization.id, GaugeFieldData.SectorAlgebra.Realization.id_toAlgHom, GaugeFieldData.SectorAlgebra.Realization.map_repJet, GaugeFieldData.SectorAlgebra.Realization.map_repLorentz, GaugeFieldData.SectorAlgebra.Realization.repJet_mul, GaugeFieldData.SectorAlgebra.Realization.repLorentz_mul, GaugeFieldData.SectorAlgebra.Realization.ext_generators
statement: formalized
proof: formalized
---

# Realizations of the ordinary sector algebras

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.SectorRealization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean): 23 declarations, 5 with a docstring.

## i. Overview

> A complex algebra `B` carries the ordinary sector `S` of a field datum when the sector
> algebra `T.SectorAlgebra S` maps into it by a complex algebra map equivariant for the jet
> gauge group and the Lorentz group, both acting on `B` by algebra endomorphisms:
> `GaugeFieldData.SectorAlgebra.Realization`. No species condition is involved.
>
> A sector realization is determined by its images of the selected generators
> (`Realization.ext_generators`); nothing asserts that an arbitrary assignment of those images
> extends to a realization. Realizations restrict along `Subalgebra.inclusion` from the local
> field algebra to every sector and from a sector to every smaller one, and successive
> restrictions agree with the direct one.

## ii. Key results

> - `GaugeFieldData.SectorAlgebra.Realization` : an algebra carrying an ordinary sector.
> - `GaugeFieldData.SectorAlgebra.Realization.restrict` : restriction to a smaller sector,
>   with `restrict_restrict`.
> - `GaugeFieldData.Realization.restrictSector` : restriction of a realization of the local
>   field algebra to a sector, with `restrict_restrictSector`.

## iv. References

> * None.

## A. Sector realizations

**`GaugeFieldData.SectorAlgebra.Realization`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L68).

> A complex algebra `B` carrying the ordinary sector `S` of the datum `T`: a complex
> algebra map out of the sector algebra, equivariant for the jet gauge group and the Lorentz
> group, both acting on the whole of `B` by algebra endomorphisms. The lemmas `map_repJet`,
> `map_repLorentz`, `repJet_mul` and `repLorentz_mul` name its fields.

```lean
abbrev Realization (T : GaugeFieldData jets) (S : Finset FieldCategory) (B : Type)
    [Semiring B] [Algebra ℂ B] (repJet : Representation ℂ GJ B)
    (repLorentz : Representation ℂ SL(2,ℂ) B)
```

**`GaugeFieldData.SectorAlgebra.Realization.id`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L81).

> A sector algebra realized in itself, by the identity.

```lean
noncomputable def id :
    Realization T S (T.SectorAlgebra S) (SectorAlgebra.repJet T S)
      (SectorAlgebra.repLorentzGroup T S)
```

**`GaugeFieldData.SectorAlgebra.Realization.id_toAlgHom`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L87).

```lean
lemma id_toAlgHom : (id T S).toAlgHom = AlgHom.id ℂ (T.SectorAlgebra S)
```

**`GaugeFieldData.SectorAlgebra.Realization.map_repJet`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L91).

```lean
lemma map_repJet (U : GJ) (x : T.SectorAlgebra S) :
    h.toAlgHom (SectorAlgebra.repJet T S U x) = repJet U (h.toAlgHom x)
```

**`GaugeFieldData.SectorAlgebra.Realization.map_repLorentz`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L95).

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : T.SectorAlgebra S) :
    h.toAlgHom (SectorAlgebra.repLorentzGroup T S Λ x) = repLorentz Λ (h.toAlgHom x)
```

**`GaugeFieldData.SectorAlgebra.Realization.repJet_mul`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L100).

```lean
lemma repJet_mul (U : GJ) (b₁ b₂ : B) : repJet U (b₁ * b₂) = repJet U b₁ * repJet U b₂
```

**`GaugeFieldData.SectorAlgebra.Realization.repLorentz_mul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L104).

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

**`GaugeFieldData.SectorAlgebra.Realization.ext_generators`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L110).

> A sector realization is determined by its images of the selected generators. Only
> uniqueness is asserted, not the extension of an arbitrary assignment.

```lean
lemma ext_generators {h₁ h₂ : Realization T S B repJet repLorentz}
    (hf : ∀ (hS : FieldCategory.fermion ∈ S) (v : T.FermionGenerators),
      h₁.toAlgHom ⟨T.ιFermionTotal v, ιFermionTotal_mem hS v⟩
        = h₂.toAlgHom ⟨T.ιFermionTotal v, ιFermionTotal_mem hS v⟩)
    (hs : ∀ (hS : FieldCategory.scalar ∈ S) (v : T.BosonGenerators),
      h₁.toAlgHom ⟨T.ιBosonTotal v, ιBosonTotal_mem hS v⟩
        = h₂.toAlgHom ⟨T.ιBosonTotal v, ιBosonTotal_mem hS v⟩)
    (hg : ∀ (hS : FieldCategory.gauge ∈ S) (v : GaugeBoson.JetComponentSpace 𝔤),
      h₁.toAlgHom ⟨T.ιConnection v, ιConnection_mem hS v⟩
        = h₂.toAlgHom ⟨T.ιConnection v, ιConnection_mem hS v⟩) : h₁ = h₂
```

## B. Restriction to a smaller sector

**`GaugeFieldData.SectorAlgebra.Realization.restrict`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L131).

> The restriction of a sector realization to a smaller sector.

```lean
noncomputable def restrict (h : Realization T S' B repJet repLorentz) (hS : S ⊆ S') :
    Realization T S B repJet repLorentz
```

**`GaugeFieldData.SectorAlgebra.Realization.restrict_toAlgHom`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L135).

```lean
lemma restrict_toAlgHom (h : Realization T S' B repJet repLorentz) (hS : S ⊆ S') :
    (h.restrict hS).toAlgHom = h.toAlgHom.comp (Subalgebra.inclusion (mono T hS))
```

**`GaugeFieldData.SectorAlgebra.Realization.restrict_toAlgHom_apply`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L139).

```lean
lemma restrict_toAlgHom_apply (h : Realization T S' B repJet repLorentz) (hS : S ⊆ S')
    (x : T.SectorAlgebra S) :
    (h.restrict hS).toAlgHom x = h.toAlgHom (Subalgebra.inclusion (mono T hS) x)
```

**`GaugeFieldData.SectorAlgebra.Realization.restrict_toAlgHom_mk`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L143).

```lean
lemma restrict_toAlgHom_mk (h : Realization T S' B repJet repLorentz) (hS : S ⊆ S')
    (x : T.LocalFieldAlgebra) (hx : x ∈ T.SectorAlgebra S) :
    (h.restrict hS).toAlgHom ⟨x, hx⟩ = h.toAlgHom ⟨x, mono T hS hx⟩
```

**`GaugeFieldData.SectorAlgebra.Realization.restrict_id_toAlgHom`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L147).

```lean
lemma restrict_id_toAlgHom (hS : S ⊆ S') :
    ((id T S').restrict hS).toAlgHom = Subalgebra.inclusion (mono T hS)
```

**`GaugeFieldData.SectorAlgebra.Realization.restrict_restrict`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L151).

```lean
lemma restrict_restrict {S'' : Finset FieldCategory} (h : Realization T S'' B repJet repLorentz)
    (hS' : S' ⊆ S'') (hS : S ⊆ S') :
    (h.restrict hS').restrict hS = h.restrict (hS.trans hS')
```

## C. Restriction from the local field algebra

**`GaugeFieldData.Realization.restrictSector`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L175).

> The restriction of a realization of the local field algebra to a sector.

```lean
noncomputable def restrictSector : SectorAlgebra.Realization T S B repJet repLorentz
```

**`GaugeFieldData.Realization.restrictSector_toAlgHom`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L179).

```lean
lemma restrictSector_toAlgHom :
    (h.restrictSector S).toAlgHom = h.toAlgHom.comp (T.SectorAlgebra S).val
```

**`GaugeFieldData.Realization.restrictSector_toAlgHom_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L183).

```lean
lemma restrictSector_toAlgHom_apply (x : T.SectorAlgebra S) :
    (h.restrictSector S).toAlgHom x = h.toAlgHom x
```

**`GaugeFieldData.Realization.restrictSector_id_toAlgHom`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L186).

```lean
lemma restrictSector_id_toAlgHom :
    ((id T).restrictSector S).toAlgHom = (T.SectorAlgebra S).val
```

**`GaugeFieldData.Realization.restrictSector_fermionSymbol`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L190).

```lean
lemma restrictSector_fermionSymbol (hS : FieldCategory.fermion ∈ S) (i : T.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    (h.restrictSector S).toAlgHom ⟨T.fermionSymbol i s φ, SectorAlgebra.fermionSymbol_mem hS i s φ⟩
      = h.fermionSymbol i s φ
```

**`GaugeFieldData.Realization.restrictSector_conjFermionSymbol`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L195).

```lean
lemma restrictSector_conjFermionSymbol (hS : FieldCategory.fermion ∈ S)
    (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    (h.restrictSector S).toAlgHom
      ⟨T.conjFermionSymbol i s φ, SectorAlgebra.conjFermionSymbol_mem hS i s φ⟩
      = h.conjFermionSymbol i s φ
```

**`GaugeFieldData.Realization.restrictSector_bosonSymbol`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L202).

```lean
lemma restrictSector_bosonSymbol (hS : FieldCategory.scalar ∈ S) (j : T.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)) :
    (h.restrictSector S).toAlgHom ⟨T.bosonSymbol j s φ, SectorAlgebra.bosonSymbol_mem hS j s φ⟩
      = h.bosonSymbol j s φ
```

**`GaugeFieldData.Realization.restrictSector_conjBosonSymbol`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L207).

```lean
lemma restrictSector_conjBosonSymbol (hS : FieldCategory.scalar ∈ S) (j : T.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    (h.restrictSector S).toAlgHom
      ⟨T.conjBosonSymbol j s φ, SectorAlgebra.conjBosonSymbol_mem hS j s φ⟩
      = h.conjBosonSymbol j s φ
```

**`GaugeFieldData.Realization.restrict_restrictSector`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean#L213).

```lean
lemma restrict_restrictSector {S' : Finset FieldCategory} (hS : S ⊆ S') :
    (h.restrictSector S').restrict hS = h.restrictSector S
```

## Depends on

- [Realizations of the local field algebra](../part-03/localfield-realization.md)
- [The ordinary sector algebras of the local field algebra](localfield-sector.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/SectorRealization.lean)
