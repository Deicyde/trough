---
declaration: module
origin: cited
lean: GaugeFieldData.CovSectorAlgebra.Realization, GaugeFieldData.CovSectorAlgebra.Realization.id, GaugeFieldData.CovSectorAlgebra.Realization.id_toAlgHom, GaugeFieldData.CovSectorAlgebra.Realization.map_repValue, GaugeFieldData.CovSectorAlgebra.Realization.map_repLorentz, GaugeFieldData.CovSectorAlgebra.Realization.repGauge_mul, GaugeFieldData.CovSectorAlgebra.Realization.repLorentz_mul, GaugeFieldData.CovSectorAlgebra.Realization.ext_towers
statement: formalized
proof: formalized
---

# Realizations of the covariant sector algebras

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalCovField.SectorRealization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean): 31 declarations, 9 with a docstring.

## i. Overview

> A complex algebra `B` carries the covariant sector `S` of a field datum when the covariant
> sector algebra `T.CovSectorAlgebra S` maps into it by a complex algebra map equivariant for
> the ordinary gauge group `G₀` and for the Lorentz group, both acting on `B` by algebra
> endomorphisms: `GaugeFieldData.CovSectorAlgebra.Realization`. The source gauge action is the
> jet action at the constant jets; the source Lorentz action exists under
> `GaugeFieldData.GaugeLorentzCompatible`, which the type carries.
>
> A covariant sector algebra is not free on its towers, so only uniqueness from the tower
> images is asserted (`Realization.ext_towers`). Realizations restrict along
> `Subalgebra.inclusion` into a covariant sector from the covariant field algebra, from a larger
> covariant sector, and from the local field algebra, with `G₀` acting on the target through the
> constant jets; successive restrictions agree with the direct ones. An ordinary sector
> realization does not restrict to the covariant sector of the same selection, which need not
> lie in it.
>
> `GaugeFieldData.PureJetsActTrivially` is used only in `Realization.map_repJet`.

## ii. Key results

> - `GaugeFieldData.CovSectorAlgebra.Realization` : an algebra carrying a covariant sector.
> - `GaugeFieldData.CovSectorAlgebra.Realization.restrict` : restriction to a smaller sector,
>   with `restrict_restrict`.
> - `GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector` : restriction of a
>   realization of the covariant field algebra to a sector, with its tower computation rules
>   and `restrict_restrictSector`.
> - `GaugeFieldData.Realization.restrictCovSector` : restriction of a realization of the local
>   field algebra to a covariant sector, with `restrictSector_restrict` identifying it with
>   the restriction through the covariant field algebra.

## iv. References

> * None.

## A. Sector realizations

**`GaugeFieldData.CovSectorAlgebra.Realization`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L80).

> A complex algebra `B` carrying the covariant sector `S` of the datum `T`: a complex
> algebra map out of the covariant sector algebra, equivariant for the ordinary gauge group
> and the Lorentz group, both acting on the whole of `B` by algebra endomorphisms. The source
> Lorentz action needs `hGL`; no other species condition is used. The lemmas `map_repValue`,
> `map_repLorentz`, `repGauge_mul` and `repLorentz_mul` name its fields.

```lean
abbrev Realization (T : GaugeFieldData jets) (S : Finset FieldCategory)
    (hGL : T.GaugeLorentzCompatible) (B : Type) [Semiring B] [Algebra ℂ B]
    (repGauge : Representation ℂ G₀ B) (repLorentz : Representation ℂ SL(2,ℂ) B)
```

**`GaugeFieldData.CovSectorAlgebra.Realization.id`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L93).

> A covariant sector algebra realized in itself, by the identity.

```lean
noncomputable def id :
    Realization T S hGL (T.CovSectorAlgebra S) (repValue T S) (repLorentzGroup T S hGL)
```

**`GaugeFieldData.CovSectorAlgebra.Realization.id_toAlgHom`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L98).

```lean
lemma id_toAlgHom : (id T S hGL).toAlgHom = AlgHom.id ℂ (T.CovSectorAlgebra S)
```

**`GaugeFieldData.CovSectorAlgebra.Realization.map_repValue`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L102).

```lean
lemma map_repValue (g : G₀) (x : T.CovSectorAlgebra S) :
    k.toAlgHom (repValue T S g x) = repGauge g (k.toAlgHom x)
```

**`GaugeFieldData.CovSectorAlgebra.Realization.map_repLorentz`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L106).

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : T.CovSectorAlgebra S) :
    k.toAlgHom (repLorentzGroup T S hGL Λ x) = repLorentz Λ (k.toAlgHom x)
```

**`GaugeFieldData.CovSectorAlgebra.Realization.repGauge_mul`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L111).

```lean
lemma repGauge_mul (g : G₀) (b₁ b₂ : B) :
    repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂
```

**`GaugeFieldData.CovSectorAlgebra.Realization.repLorentz_mul`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L116).

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

**`GaugeFieldData.CovSectorAlgebra.Realization.ext_towers`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L122).

> A sector realization is determined by its images of the selected towers; uniqueness
> only, the algebra not being free on its towers.

```lean
lemma ext_towers {k₁ k₂ : Realization T S hGL B repGauge repLorentz}
    (hF : ∀ (hS : FieldCategory.gauge ∈ S) (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
      (φ : Module.Dual ℝ 𝔤),
      k₁.toAlgHom ⟨T.covDerivFieldStrength l μ ν φ, covDerivFieldStrength_mem hS l μ ν φ⟩
        = k₂.toAlgHom ⟨T.covDerivFieldStrength l μ ν φ, covDerivFieldStrength_mem hS l μ ν φ⟩)
    (hψ : ∀ (hS : FieldCategory.fermion ∈ S) (i : T.FermionSpecies) {n : ℕ}
      (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)),
      k₁.toAlgHom ⟨T.covDerivFermion i l φ, covDerivFermion_mem hS i l φ⟩
        = k₂.toAlgHom ⟨T.covDerivFermion i l φ, covDerivFermion_mem hS i l φ⟩)
    (hψc : ∀ (hS : FieldCategory.fermion ∈ S) (i : T.FermionSpecies) {n : ℕ}
      (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))),
      k₁.toAlgHom ⟨T.covDerivConjFermion i l φ, covDerivConjFermion_mem hS i l φ⟩
        = k₂.toAlgHom ⟨T.covDerivConjFermion i l φ, covDerivConjFermion_mem hS i l φ⟩)
    (hφ : ∀ (hS : FieldCategory.scalar ∈ S) (j : T.BosonSpecies) {n : ℕ}
      (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)),
      k₁.toAlgHom ⟨T.covDerivBoson j l φ, covDerivBoson_mem hS j l φ⟩
        = k₂.toAlgHom ⟨T.covDerivBoson j l φ, covDerivBoson_mem hS j l φ⟩)
    (hφc : ∀ (hS : FieldCategory.scalar ∈ S) (j : T.BosonSpecies) {n : ℕ}
      (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))),
      k₁.toAlgHom ⟨T.covDerivConjBoson j l φ, covDerivConjBoson_mem hS j l φ⟩
        = k₂.toAlgHom ⟨T.covDerivConjBoson j l φ, covDerivConjBoson_mem hS j l φ⟩) :
    k₁ = k₂
```

**`GaugeFieldData.CovSectorAlgebra.Realization.map_repJet`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L148).

> Under `GaugeFieldData.PureJetsActTrivially` the jet action factors through evaluation:
> a jet acts on the realized image as its value.

```lean
lemma map_repJet (hP : T.PureJetsActTrivially) (U : GJ) (x : T.CovSectorAlgebra S) :
    k.toAlgHom (repJet T S U x) = repGauge (jets.eval U) (k.toAlgHom x)
```

## B. Restriction to a smaller sector

**`GaugeFieldData.CovSectorAlgebra.Realization.restrict`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L161).

> The restriction of a covariant sector realization to a smaller sector.

```lean
noncomputable def restrict (k : Realization T S' hGL B repGauge repLorentz) (hS : S ⊆ S') :
    Realization T S hGL B repGauge repLorentz
```

**`GaugeFieldData.CovSectorAlgebra.Realization.restrict_toAlgHom`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L166).

```lean
lemma restrict_toAlgHom (k : Realization T S' hGL B repGauge repLorentz) (hS : S ⊆ S') :
    (k.restrict hS).toAlgHom = k.toAlgHom.comp (Subalgebra.inclusion (mono T hS))
```

**`GaugeFieldData.CovSectorAlgebra.Realization.restrict_toAlgHom_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L170).

```lean
lemma restrict_toAlgHom_apply (k : Realization T S' hGL B repGauge repLorentz) (hS : S ⊆ S')
    (x : T.CovSectorAlgebra S) :
    (k.restrict hS).toAlgHom x = k.toAlgHom (Subalgebra.inclusion (mono T hS) x)
```

**`GaugeFieldData.CovSectorAlgebra.Realization.restrict_toAlgHom_mk`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L174).

```lean
lemma restrict_toAlgHom_mk (k : Realization T S' hGL B repGauge repLorentz) (hS : S ⊆ S')
    (x : T.LocalFieldAlgebra) (hx : x ∈ T.CovSectorAlgebra S) :
    (k.restrict hS).toAlgHom ⟨x, hx⟩ = k.toAlgHom ⟨x, mono T hS hx⟩
```

**`GaugeFieldData.CovSectorAlgebra.Realization.restrict_id_toAlgHom`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L178).

```lean
lemma restrict_id_toAlgHom (hS : S ⊆ S') :
    ((id T S' hGL).restrict hS).toAlgHom = Subalgebra.inclusion (mono T hS)
```

**`GaugeFieldData.CovSectorAlgebra.Realization.restrict_restrict`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L182).

```lean
lemma restrict_restrict {S'' : Finset FieldCategory}
    (k : Realization T S'' hGL B repGauge repLorentz) (hS' : S' ⊆ S'') (hS : S ⊆ S') :
    (k.restrict hS').restrict hS = k.restrict (hS.trans hS')
```

## C. Restriction from the covariant field algebra

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L206).

> The restriction of a realization of the covariant field algebra to a covariant sector.

```lean
noncomputable def restrictSector : CovSectorAlgebra.Realization T S hGL B repGauge repLorentz
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_toAlgHom`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L211).

```lean
lemma restrictSector_toAlgHom :
    (k.restrictSector S).toAlgHom
      = k.toAlgHom.comp (Subalgebra.inclusion (CovSectorAlgebra.le_localCovFieldAlgebra T S))
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_toAlgHom_apply`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L217).

```lean
lemma restrictSector_toAlgHom_apply (x : T.CovSectorAlgebra S) :
    (k.restrictSector S).toAlgHom x
      = k.toAlgHom (Subalgebra.inclusion (CovSectorAlgebra.le_localCovFieldAlgebra T S) x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_id_toAlgHom`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L222).

```lean
lemma restrictSector_id_toAlgHom :
    ((id T hGL).restrictSector S).toAlgHom
      = Subalgebra.inclusion (CovSectorAlgebra.le_localCovFieldAlgebra T S)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_fieldStrength`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L227).

```lean
lemma restrictSector_fieldStrength (hS : FieldCategory.gauge ∈ S) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (k.restrictSector S).toAlgHom
      ⟨T.covDerivFieldStrength l μ ν φ, CovSectorAlgebra.covDerivFieldStrength_mem hS l μ ν φ⟩
      = k.fieldStrength l μ ν φ
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_fermion`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L233).

```lean
lemma restrictSector_fermion (hS : FieldCategory.fermion ∈ S) (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    (k.restrictSector S).toAlgHom
      ⟨T.covDerivFermion i l φ, CovSectorAlgebra.covDerivFermion_mem hS i l φ⟩
      = k.fermion i l φ
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_conjFermion`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L239).

```lean
lemma restrictSector_conjFermion (hS : FieldCategory.fermion ∈ S) (i : T.FermionSpecies)
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    (k.restrictSector S).toAlgHom
      ⟨T.covDerivConjFermion i l φ, CovSectorAlgebra.covDerivConjFermion_mem hS i l φ⟩
      = k.conjFermion i l φ
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_boson`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L245).

```lean
lemma restrictSector_boson (hS : FieldCategory.scalar ∈ S) (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)) :
    (k.restrictSector S).toAlgHom
      ⟨T.covDerivBoson j l φ, CovSectorAlgebra.covDerivBoson_mem hS j l φ⟩
      = k.boson j l φ
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrictSector_conjBoson`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L251).

```lean
lemma restrictSector_conjBoson (hS : FieldCategory.scalar ∈ S) (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    (k.restrictSector S).toAlgHom
      ⟨T.covDerivConjBoson j l φ, CovSectorAlgebra.covDerivConjBoson_mem hS j l φ⟩
      = k.conjBoson j l φ
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.restrict_restrictSector`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L257).

```lean
lemma restrict_restrictSector {S' : Finset FieldCategory} (hS : S ⊆ S') :
    (k.restrictSector S').restrict hS = k.restrictSector S
```

## D. Restriction from the local field algebra

**`GaugeFieldData.Realization.restrictCovSector`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L279).

> The restriction of a realization of the local field algebra to a covariant sector; the
> ordinary gauge group acts on the target through the constant jets.

```lean
noncomputable def restrictCovSector :
    CovSectorAlgebra.Realization T S hGL B (repJet.comp jets.ofConstant) repLorentz
```

**`GaugeFieldData.Realization.restrictCovSector_toAlgHom`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L285).

```lean
lemma restrictCovSector_toAlgHom :
    (h.restrictCovSector hGL S).toAlgHom = h.toAlgHom.comp (T.CovSectorAlgebra S).val
```

**`GaugeFieldData.Realization.restrictCovSector_toAlgHom_apply`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L289).

```lean
lemma restrictCovSector_toAlgHom_apply (x : T.CovSectorAlgebra S) :
    (h.restrictCovSector hGL S).toAlgHom x = h.toAlgHom x
```

**`GaugeFieldData.Realization.restrictCovSector_map_repJet`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L293).

> Jet equivariance survives restriction without `PureJetsActTrivially`.

```lean
lemma restrictCovSector_map_repJet (U : GJ) (x : T.CovSectorAlgebra S) :
    (h.restrictCovSector hGL S).toAlgHom (CovSectorAlgebra.repJet T S U x)
      = repJet U ((h.restrictCovSector hGL S).toAlgHom x)
```

**`GaugeFieldData.Realization.restrictSector_restrict`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L299).

> Restriction through the covariant field algebra is the direct restriction.

```lean
lemma restrictSector_restrict :
    (h.restrict hGL).restrictSector S = h.restrictCovSector hGL S
```

**`GaugeFieldData.Realization.restrict_restrictCovSector`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean#L305).

```lean
lemma restrict_restrictCovSector {S' : Finset FieldCategory} (hS : S ⊆ S') :
    (h.restrictCovSector hGL S').restrict hS = h.restrictCovSector hGL S
```

## Depends on

- [Realizations of the covariant field algebra (LocalCovField/Realization)](../part-02/localcovfield-realization.md)
- [The covariant sector algebras of the local field algebra](localcovfield-sector.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/SectorRealization.lean)
