---
declaration: module
origin: cited
lean: StandardModel.CovAlgebraRealization.sectorSubmodule, StandardModel.CovAlgebraRealization.mul_mem_sectorSubmodule, StandardModel.CovAlgebraRealization.sector, StandardModel.CovAlgebraRealization.mem_sector, StandardModel.CovAlgebraRealization.list_prod_mem_sector, StandardModel.CovAlgebraRealization.mul_mem_sector, StandardModel.CovAlgebraRealization.mem_fieldAlgebra_of_mem_sector, StandardModel.CovAlgebraRealization.fieldAlgebra_eq_iSup_sector
statement: formalized
proof: formalized
---

# The sectors of the field algebra

The module `PhyslibAlpha.Particles.StandardModel.CovRealization.Sectors`, [PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean): 49 declarations, 46 with a docstring.

## i. Overview

> Each covariant generator belongs to one of three classes — gauge, Higgs or fermion —
> and a word in the generators realises a set of classes. The sector of a class set `S`
> is the non-unital subalgebra spanned by the words realising exactly `S`; the sectors
> exhaust the field algebra and are preserved by the gauge and Lorentz actions.
>
> Refining by the mass weight, `sectorMassWeight S w` is the span of the words
> realising `S` of total weight `w`; it is exactly the intersection of the sector with
> the mass-weight submodule (`sectorMassWeight_eq_inf`), and for each weight `w` the
> mass-weight submodule decomposes as the join of the sectors' weight-`w` parts
> (`massWeightSubmodule_eq_iSup_sectorMassWeight`).

## ii. Key results

> - `sectorMassWeight_eq_inf` : the weight-`w` part of the sector of `S` is exactly the intersection
>   of the sector with the mass-weight submodule
> - `massWeightSubmodule_eq_iSup_sectorMassWeight` : the decomposition of the mass-weight submodule
>   into sectors: the weight-`w` component of the field algebra is the join over the class sets `S` of
>   the weight-`w` parts of the sectors, since every word realises exactly one class set

## iv. References

> * None.

## A. The different sectors of the Standard Model

> Each covariant generator belongs to one of three classes — gauge, Higgs or fermion —
> and a word in the generators realises a set of classes. The sector of a class set `S`
> is spanned by the words realising exactly `S`. It contains no non-zero scalar, since
> the empty word realises no class at all, and it is closed under multiplication because
> `S ∪ S = S`: it is a non-unital subalgebra. The seven non-empty class sets give the
> seven sectors below.

**`StandardModel.CovAlgebraRealization.sectorSubmodule`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L78).

> The span of the words in the covariant generators realising exactly the classes
> `S`.

```lean
def sectorSubmodule (S : Finset GeneratorClass) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.mul_mem_sectorSubmodule`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L83).

> Multiplication carries the class spans of `S` and `T` into that of `S ∪ T`.

```lean
lemma mul_mem_sectorSubmodule {S T : Finset GeneratorClass} {x y : B}
    (hx : x ∈ h.sectorSubmodule S) (hy : y ∈ h.sectorSubmodule T) :
    x * y ∈ h.sectorSubmodule (S ∪ T)
```

**`StandardModel.CovAlgebraRealization.sector`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L106).

> The sector realising exactly the classes `S`: the span of the words whose
> generators realise `S`. It is a non-unital subalgebra — closed under multiplication
> since `S ∪ S = S`, but containing no non-zero scalar, since the empty word realises
> no class.

```lean
def sector (S : Finset GeneratorClass) : NonUnitalSubalgebra ℂ B
```

**`StandardModel.CovAlgebraRealization.mem_sector`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L112).

```lean
lemma mem_sector {S : Finset GeneratorClass} {x : B} :
    x ∈ h.sector S ↔ x ∈ h.sectorSubmodule S
```

**`StandardModel.CovAlgebraRealization.list_prod_mem_sector`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L116).

> A word lies in the sector of the classes it realises.

```lean
lemma list_prod_mem_sector (gl : List Generators) :
    (gl.map h.generatorVal).prod ∈ h.sector (wordClasses gl)
```

**`StandardModel.CovAlgebraRealization.mul_mem_sector`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L121).

> Multiplication carries the sectors of `S` and `T` into the sector of `S ∪ T`.

```lean
lemma mul_mem_sector {S T : Finset GeneratorClass} {x y : B}
    (hx : x ∈ h.sector S) (hy : y ∈ h.sector T) : x * y ∈ h.sector (S ∪ T)
```

**`StandardModel.CovAlgebraRealization.mem_fieldAlgebra_of_mem_sector`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L126).

> Every sector sits inside the field algebra.

```lean
lemma mem_fieldAlgebra_of_mem_sector {S : Finset GeneratorClass} {x : B}
    (hx : x ∈ h.sector S) : x ∈ h.fieldAlgebra
```

**`StandardModel.CovAlgebraRealization.fieldAlgebra_eq_iSup_sector`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L144).

> **The sectors exhaust the field algebra**: every element of the field algebra is a
> sum of elements of the sectors, since every word realises exactly one class set. The
> unit is supplied by `sector ∅`, the sector of the empty word, so the join is the
> whole of `fieldAlgebra` — read as a non-unital subalgebra, the two sides having
> otherwise different types.

```lean
lemma fieldAlgebra_eq_iSup_sector :
    h.fieldAlgebra.toNonUnitalSubalgebra = ⨆ S : Finset GeneratorClass, h.sector S
```

### A.1. The sectors are preserved by the gauge and Lorentz actions

> Both actions carry a covariant tower into combinations of towers of the same
> species, hence each generator into the sector of its own class, hence — word by
> word — each sector into itself.

**`StandardModel.CovAlgebraRealization.H_mem_sector`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L174).

> Any Higgs tower symbol lies in the Higgs sector.

```lean
lemma H_mem_sector {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ HiggsVec) : h.covH l φ ∈ h.sector {GeneratorClass.higgs}
```

**`StandardModel.CovAlgebraRealization.barH_mem_sector`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L183).

> Any conjugate-Higgs tower symbol lies in the Higgs sector.

```lean
lemma barH_mem_sector {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    h.covBarH l φ ∈ h.sector {GeneratorClass.higgs}
```

**`StandardModel.CovAlgebraRealization.F_mem_sector`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L193).

> Any field-strength tower symbol lies in the gauge sector.

```lean
lemma F_mem_sector {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) : h.covF l μ ν φ ∈ h.sector {GeneratorClass.gauge}
```

**`StandardModel.CovAlgebraRealization.d_mem_sector`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L204).

> Any `d` tower symbol lies in the fermion sector.

```lean
lemma d_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ DownSinglet) : h.covD i l φ ∈ h.sector {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.bard_mem_sector`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L213).

> Any `bard` tower symbol lies in the fermion sector.

```lean
lemma bard_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) : h.covBarD i l φ ∈ h.sector
      {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.u_mem_sector`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L223).

> Any `u` tower symbol lies in the fermion sector.

```lean
lemma u_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ UpSinglet) : h.covU i l φ ∈ h.sector {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.baru_mem_sector`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L232).

> Any `baru` tower symbol lies in the fermion sector.

```lean
lemma baru_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    h.covBarU i l φ ∈ h.sector {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.Q_mem_sector`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L242).

> Any `Q` tower symbol lies in the fermion sector.

```lean
lemma Q_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ QuarkDoublet) : h.covQ i l φ ∈ h.sector {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.barQ_mem_sector`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L251).

> Any `barQ` tower symbol lies in the fermion sector.

```lean
lemma barQ_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) : h.covBarQ i l φ ∈ h.sector
      {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.L_mem_sector`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L261).

> Any `L` tower symbol lies in the fermion sector.

```lean
lemma L_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ LeptonDoubletV) : h.covL i l φ ∈ h.sector {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.barL_mem_sector`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L270).

> Any `barL` tower symbol lies in the fermion sector.

```lean
lemma barL_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) : h.covBarL i l φ ∈ h.sector
      {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.e_mem_sector`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L280).

> Any `e` tower symbol lies in the fermion sector.

```lean
lemma e_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ LeptonSinglet) : h.covE i l φ ∈ h.sector {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.bare_mem_sector`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L289).

> Any `bare` tower symbol lies in the fermion sector.

```lean
lemma bare_mem_sector (i : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) : h.covBarE i l φ ∈ h.sector
      {GeneratorClass.fermion}
```

**`StandardModel.CovAlgebraRealization.repGauge_generatorVal_mem_sector`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L299).

> The gauge action carries a covariant generator into the sector of its class.

```lean
lemma repGauge_generatorVal_mem_sector (g : GaugeGroupI) (a : Generators) :
    repGauge g (h.generatorVal a) ∈ h.sector {a.kind}
```

**`StandardModel.CovAlgebraRealization.repLorentz_generatorVal_mem_sector`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L357).

> The Lorentz action carries a covariant generator into the sector of its
> class.

```lean
lemma repLorentz_generatorVal_mem_sector (Λ : SL(2,ℂ)) (a : Generators) :
    repLorentz Λ (h.generatorVal a) ∈ h.sector {a.kind}
```

**`StandardModel.CovAlgebraRealization.repGauge_mem_sector`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L416).

> The action `repGauge` preserves every sector.

```lean
lemma repGauge_mem_sector {S : Finset GeneratorClass} {x : B} (g : GaugeGroupI)
    (hx : x ∈ h.sector S) : repGauge g x ∈ h.sector S
```

**`StandardModel.CovAlgebraRealization.repLorentz_mem_sector`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L437).

> The action `repLorentz` preserves every sector.

```lean
lemma repLorentz_mem_sector {S : Finset GeneratorClass} {x : B} (Λ : SL(2,ℂ))
    (hx : x ∈ h.sector S) : repLorentz Λ x ∈ h.sector S
```

## B. Sectors at a fixed mass weight

**`StandardModel.CovAlgebraRealization.sectorMassWeight`**, a def, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L465).

> The span of the words realising exactly the classes `S` of total mass weight
> `w`.

```lean
def sectorMassWeight (S : Finset GeneratorClass) (w : ℕ) : Submodule ℂ B
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_le_sectorSubmodule`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L470).

```lean
lemma sectorMassWeight_le_sectorSubmodule (S : Finset GeneratorClass) (w : ℕ) :
    h.sectorMassWeight S w ≤ h.sectorSubmodule S
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_le_massWeightSubmodule`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L476).

```lean
lemma sectorMassWeight_le_massWeightSubmodule (S : Finset GeneratorClass) (w : ℕ) :
    h.sectorMassWeight S w ≤ h.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.list_prod_mem_sectorMassWeight`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L483).

> A word lies in the weight part of its sector given by its total weight.

```lean
lemma list_prod_mem_sectorMassWeight (gl : List Generators) :
    (gl.map h.generatorVal).prod
      ∈ h.sectorMassWeight (wordClasses gl) ((gl.map Generators.weight).sum)
```

**`StandardModel.CovAlgebraRealization.mul_mem_sectorMassWeight`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L491).

> Multiplication carries the weight-`w` part of the sector of `S` and the
> weight-`w'` part of the sector of `T` into the weight-`w + w'` part of the sector
> of `S ∪ T`.

```lean
lemma mul_mem_sectorMassWeight {S T : Finset GeneratorClass} {w w' : ℕ} {x y : B}
    (hx : x ∈ h.sectorMassWeight S w) (hy : y ∈ h.sectorMassWeight T w') :
    x * y ∈ h.sectorMassWeight (S ∪ T) (w + w')
```

**`StandardModel.CovAlgebraRealization.coeff_massWeightPoly_mem_sectorMassWeight`**, a lemma, [line 514](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L514).

> Reading off the `X ^ w` coefficient of `massWeightPoly` sends the sector of `S`
> into its weight-`w` part — the projection onto the weight-`w` component, with no
> independence argument needed.

```lean
lemma coeff_massWeightPoly_mem_sectorMassWeight {S : Finset GeneratorClass} {x : B}
    (hx : x ∈ h.sector S) (w : ℕ) :
    (massWeightPoly x).coeff w ∈ h.sectorMassWeight S w
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_eq_inf`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L539).

> The weight-`w` part of the sector of `S` is exactly the intersection of the
> sector with the mass-weight submodule.

```lean
lemma sectorMassWeight_eq_inf (S : Finset GeneratorClass) (w : ℕ) :
    h.sectorMassWeight S w = h.sectorSubmodule S ⊓ h.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.massWeightSubmodule_eq_iSup_sectorMassWeight`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L553).

> **The decomposition of the mass-weight submodule into sectors**: the weight-`w`
> component of the field algebra is the join over the class sets `S` of the
> weight-`w` parts of the sectors, since every word realises exactly one class set.
> The empty class set contributes the scalars, at weight zero only.

```lean
lemma massWeightSubmodule_eq_iSup_sectorMassWeight (w : ℕ) :
    h.massWeightSubmodule w = ⨆ S : Finset GeneratorClass, h.sectorMassWeight S w
```

**`StandardModel.CovAlgebraRealization.repGauge_mem_sectorMassWeight`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L562).

> The action `repGauge` preserves the weight parts of every sector.

```lean
lemma repGauge_mem_sectorMassWeight {S : Finset GeneratorClass} {w : ℕ} {x : B}
    (g : GaugeGroupI) (hx : x ∈ h.sectorMassWeight S w) :
    repGauge g x ∈ h.sectorMassWeight S w
```

**`StandardModel.CovAlgebraRealization.repLorentz_mem_sectorMassWeight`**, a lemma, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L572).

> The action `repLorentz` preserves the weight parts of every sector.

```lean
lemma repLorentz_mem_sectorMassWeight {S : Finset GeneratorClass} {w : ℕ} {x : B}
    (Λ : SL(2,ℂ)) (hx : x ∈ h.sectorMassWeight S w) :
    repLorentz Λ x ∈ h.sectorMassWeight S w
```

## C. The Higgs sector and the Higgs-sector mass-weight submodules

> The Higgs class-set piece of the sector decomposition matches the mass-weight
> submodules of the Higgs sector `h.isHiggsSector`: at a non-zero weight `w` the two
> agree exactly. At weight zero they differ only by the scalars, which the Higgs-sector
> submodule contains (through the unit of `higgsAlgebra`) while the `{higgs}` sector,
> being spanned by non-empty words, does not — the scalars are the `∅` sector.

**`StandardModel.CovAlgebraRealization.sectorMassWeight_empty_of_ne_zero`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L596).

> At a non-zero weight the `∅` sector has no weight part: its only word is the
> empty word, of weight zero.

```lean
lemma sectorMassWeight_empty_of_ne_zero {w : ℕ} (hw : w ≠ 0) :
    h.sectorMassWeight ∅ w = ⊥
```

**`StandardModel.CovAlgebraRealization.higgsAlgebra_le_sup_sectorSubmodule`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L607).

> The algebra generated by the Higgs towers decomposes into the `{higgs}` sector
> and the scalar `∅` sector.

```lean
lemma higgsAlgebra_le_sup_sectorSubmodule :
    Subalgebra.toSubmodule h.isHiggsSector.higgsAlgebra
      ≤ h.sectorSubmodule {GeneratorClass.higgs} ⊔ h.sectorSubmodule ∅
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_higgs_le`**, a lemma, [line 636](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L636).

> The weight-`w` part of the `{higgs}` sector lies in the Higgs-sector mass-weight
> submodule: its words are products of Higgs towers of total weight `w`.

```lean
lemma sectorMassWeight_higgs_le (w : ℕ) :
    h.sectorMassWeight {GeneratorClass.higgs} w
      ≤ h.isHiggsSector.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_higgs_eq`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L679).

> **The Higgs-sector mass-weight submodules are the weight parts of the `{higgs}`
> sector**, at any non-zero weight. (At weight zero the Higgs-sector submodule also
> contains the scalars, which the sector decomposition files under the `∅` sector.)

```lean
lemma sectorMassWeight_higgs_eq {w : ℕ} (hw : w ≠ 0) :
    h.sectorMassWeight {GeneratorClass.higgs} w
      = h.isHiggsSector.massWeightSubmodule w
```

## D. The gauge and fermion sectors and their mass-weight submodules

> The same relation as for the Higgs sector: at a non-zero weight `w`, the `{gauge}`
> and `{fermion}` pieces of the sector decomposition are exactly the mass-weight
> submodules of `h.isGaugeSector` and `h.isFermionSector`; at weight zero the sector
> submodules also contain the scalars, which the decomposition files under `∅`.

**`StandardModel.CovAlgebraRealization.gaugeAlgebra_le_sup_sectorSubmodule`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L710).

> The algebra generated by the field-strength towers decomposes into the `{gauge}` sector
> and the scalar `∅` sector.

```lean
lemma gaugeAlgebra_le_sup_sectorSubmodule :
    Subalgebra.toSubmodule h.isGaugeSector.gaugeAlgebra
      ≤ h.sectorSubmodule {GeneratorClass.gauge} ⊔ h.sectorSubmodule ∅
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_le`**, a lemma, [line 738](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L738).

> The weight-`w` part of the `{gauge}` sector lies in the gauge sector's
> mass-weight submodule.

```lean
lemma sectorMassWeight_gauge_le (w : ℕ) :
    h.sectorMassWeight {GeneratorClass.gauge} w
      ≤ h.isGaugeSector.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_gauge_eq`**, a lemma, [line 780](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L780).

> **The gauge sector's mass-weight submodules are the weight parts of the
> `{gauge}` sector**, at any non-zero weight. (At weight zero the sector's
> submodule also contains the scalars, which the sector decomposition files under the
> `∅` sector.)

```lean
lemma sectorMassWeight_gauge_eq {w : ℕ} (hw : w ≠ 0) :
    h.sectorMassWeight {GeneratorClass.gauge} w
      = h.isGaugeSector.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.fermionAlgebra_le_sup_sectorSubmodule`**, a lemma, [line 799](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L799).

> The algebra generated by the fermion towers decomposes into the `{fermion}` sector
> and the scalar `∅` sector.

```lean
lemma fermionAlgebra_le_sup_sectorSubmodule :
    Subalgebra.toSubmodule h.isFermionSector.fermionAlgebra
      ≤ h.sectorSubmodule {GeneratorClass.fermion} ⊔ h.sectorSubmodule ∅
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_fermion_le`**, a lemma, [line 837](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L837).

> The weight-`w` part of the `{fermion}` sector lies in the fermion sector's
> mass-weight submodule.

```lean
lemma sectorMassWeight_fermion_le (w : ℕ) :
    h.sectorMassWeight {GeneratorClass.fermion} w
      ≤ h.isFermionSector.massWeightSubmodule w
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_fermion_eq`**, a lemma, [line 909](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L909).

> **The fermion sector's mass-weight submodules are the weight parts of the
> `{fermion}` sector**, at any non-zero weight. (At weight zero the sector's
> submodule also contains the scalars, which the sector decomposition files under the
> `∅` sector.)

```lean
lemma sectorMassWeight_fermion_eq {w : ℕ} (hw : w ≠ 0) :
    h.sectorMassWeight {GeneratorClass.fermion} w
      = h.isFermionSector.massWeightSubmodule w
```

## E. Two-class sectors

> A word realising exactly two classes splits, up to reordering, into the part of the
> first class and the part of the second.  When the two classes' algebras commute, the
> weight-`w` piece of the two-class sector is therefore contained in the join of the
> products of the two sectors' own mass-weight submodules, over the splittings of `w`
> into two non-zero parts.  The hypotheses are stated abstractly so that the three
> pairs of sectors can each instantiate them.

**`StandardModel.CovAlgebraRealization.generatorVal_mem_of_kind`**, a lemma, [line 941](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L941).

> A single generator's value lies in any family of submodules dominating its own
> class's sector.

```lean
lemma generatorVal_mem_of_kind {c : GeneratorClass} {M : ℕ → Submodule ℂ B}
    (hM : ∀ w, h.sectorMassWeight {c} w ≤ M w) {g : Generators} (hg : g.kind = c) :
    h.generatorVal g ∈ M g.weight
```

**`StandardModel.CovAlgebraRealization.list_prod_mem_mul_of_forall_kind`**, a lemma, [line 951](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L951).

> **The two-class word decomposition.** A word all of whose generators lie in one of
> two classes is a product of an element of weight `classWeight c₁` from the first
> class's family and an element of weight `classWeight c₂` from the second.

```lean
lemma list_prod_mem_mul_of_forall_kind {c₁ c₂ : GeneratorClass} (hne : c₁ ≠ c₂)
    {M₁ M₂ : ℕ → Submodule ℂ B}
    (hM₁ : ∀ w, h.sectorMassWeight {c₁} w ≤ M₁ w)
    (hM₂ : ∀ w, h.sectorMassWeight {c₂} w ≤ M₂ w)
    (hone₁ : (1 : Submodule ℂ B) ≤ M₁ 0) (hone₂ : (1 : Submodule ℂ B) ≤ M₂ 0)
    (hmul₁ : ∀ a b, M₁ a * M₁ b ≤ M₁ (a + b))
    (hmul₂ : ∀ a b, M₂ a * M₂ b ≤ M₂ (a + b))
    (hcomm : ∀ a b, M₂ a * M₁ b ≤ M₁ b * M₂ a)
    (gl : List Generators) (hgl : ∀ g ∈ gl, g.kind = c₁ ∨ g.kind = c₂) :
    (gl.map h.generatorVal).prod
      ∈ M₁ (classWeight c₁ gl) * M₂ (classWeight c₂ gl)
```

**`StandardModel.CovAlgebraRealization.sectorMassWeight_pair_le`**, a lemma, [line 999](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L999).

> **The two-class sector decomposition.** The weight-`w` piece of the sector of two
> classes is contained in the join, over the splittings of `w` into two non-zero
> parts, of the products of the two classes' mass-weight submodules.

```lean
lemma sectorMassWeight_pair_le {c₁ c₂ : GeneratorClass} (hne : c₁ ≠ c₂)
    {M₁ M₂ : ℕ → Submodule ℂ B}
    (hM₁ : ∀ w, h.sectorMassWeight {c₁} w ≤ M₁ w)
    (hM₂ : ∀ w, h.sectorMassWeight {c₂} w ≤ M₂ w)
    (hone₁ : (1 : Submodule ℂ B) ≤ M₁ 0) (hone₂ : (1 : Submodule ℂ B) ≤ M₂ 0)
    (hmul₁ : ∀ a b, M₁ a * M₁ b ≤ M₁ (a + b))
    (hmul₂ : ∀ a b, M₂ a * M₂ b ≤ M₂ (a + b))
    (hcomm : ∀ a b, M₂ a * M₁ b ≤ M₁ b * M₂ a) (w : ℕ) :
    h.sectorMassWeight {c₁, c₂} w
      ≤ ⨆ (p : ℕ × ℕ) (_ : p.1 + p.2 = w) (_ : p.1 ≠ 0) (_ : p.2 ≠ 0), M₁ p.1 * M₂ p.2
```

## F. Invariance in terms of sectors

> Both actions preserve every weight part of every sector
> (`repGauge_mem_sectorMassWeight`, `repLorentz_mem_sectorMassWeight`), and the
> weight-`w` submodule is the join of those parts
> (`massWeightSubmodule_eq_iSup_sectorMassWeight`), so an element of the weight-`w`
> submodule is a sum of sector pieces and each action carries one such sum to
> another. Reading off from that alone that the pieces are themselves invariant is
> not possible: it needs the pieces to be determined by their sum, that is, needs
> the family of weight parts to be independent, and that is the hypothesis of
> `sector_invariant_of_iSupIndep`. Independence does not follow from
> `CovAlgebraRealization`, and the classification of the invariants in
> `MassWeight/Invariants.lean` does not use it: it joins reductions of the sectors instead.

**`StandardModel.CovAlgebraRealization.sector_invariant_of_iSupIndep`**, a lemma, [line 1047](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean#L1047).

> An element of the weight-`w` submodule fixed by both actions is a sum of
> weight-`w` sector pieces, each of them fixed by both actions, provided the weight
> parts of the sectors are independent. Independence is what turns the two
> decompositions `x = ∑ s, f s` and `x = ∑ s, repGauge g (f s)` into an equality
> piece by piece; without it the pieces are not determined by their sum.

```lean
lemma sector_invariant_of_iSupIndep {w : ℕ}
    (hind : iSupIndep fun S : Finset GeneratorClass => h.sectorMassWeight S w)
    (x : B) (x_gauge_invariant : ∀ g, repGauge g x = x)
    (x_lorentz_invariant : ∀ g, repLorentz g x = x)
    (x_mass_dim : x ∈ h.massWeightSubmodule w) :
    ∃ f : Finset GeneratorClass → B,
      x = ∑ s, f s ∧ (∀ s, f s ∈ h.sectorMassWeight s w ∧
      (∀ g, repGauge g (f s) = (f s)) ∧ (∀ g, repLorentz g (f s) = (f s)))
```

## Depends on

- [The mass-weight grading of the field algebra](covrealization-massweight.md)
- [The mass-weight grading of the fermion sector](../part-05/isfermionsector-massweight-basic.md)
- [The mass-weight grading of the gauge sector](../part-06/isgaugesector-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/CovRealization/Sectors.lean)
