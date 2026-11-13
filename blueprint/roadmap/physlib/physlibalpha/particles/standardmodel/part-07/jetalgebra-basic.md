---
declaration: module
origin: cited
lean: StandardModel.JetAlgebra, StandardModel.JetAlgebra.includeFermion, StandardModel.JetAlgebra.includeHiggs, StandardModel.JetAlgebra.includeGauge, StandardModel.JetAlgebra.includeGauge_apply, StandardModel.JetAlgebra.includeFermion_apply_equiv, StandardModel.JetAlgebra.includeHiggs_apply_equiv, StandardModel.JetAlgebra.includeGauge_eq_includeConnection
statement: formalized
proof: formalized
---

# The jet algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.Basic`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean): 12 declarations, 11 with a docstring; 1 private, not shown.

## i. Overview

> The full jet algebra of the Standard Model — the algebra in which a Standard Model
> Lagrangian lives — is the local field algebra of its field datum,
> `StandardModel.fieldData.LocalFieldAlgebra`: the exterior algebra on the fermionic
> generators of the datum, tensored with the symmetric algebra on its bosonic generators,
> tensored with the complexified symmetric algebra on the connection generators. The bosonic
> factors commute with everything, so the ordinary tensor product is correct; the
> anticommutativity of the fermions lives entirely inside the fermionic factor, where all
> fifteen species share one exterior algebra.
>
> The three sector inclusions keep their old names and their old sources — the sector
> algebras `FermionJetAlgebra`, `HiggsJetAlgebra` and `LocalGaugeFieldAlgebra GaugeAlgebra` — so
> that every downstream family of field symbols is unchanged. The two matter inclusions
> factor through the sector equivalences of
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Basic`; the connection sector needs
> no equivalence, the two presentations of it being the same type.
>
> This file defines the algebra and its three sector inclusions, and proves that the gauge
> sector is central. The Lorentz action, the jet gauge action, the formal total derivative
> and the mass-dimension scaling are assembled factorwise in the sibling files.

## ii. Key results

> - `JetAlgebra` : the jet algebra of the Standard Model.
> - `JetAlgebra.includeFermion`, `includeHiggs`, `includeGauge` : the sector inclusions.
> - `JetAlgebra.includeGauge_commute` : the gauge sector is central.
> - `JetAlgebra.includeFermion_ι`, `JetAlgebra.includeHiggs_ι`,
>   `JetAlgebra.includeGauge_one_tmul_ι` : the included degree-one elements of the three
>   sectors are the generic generators of the field datum.

## iv. References

> * None.

## A. The jet algebra of the Standard Model

**`StandardModel.JetAlgebra`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L75).

> The jet algebra of the Standard Model: the local field algebra of the Standard
> Model field datum. A Standard Model Lagrangian is an element of this algebra.

```lean
abbrev JetAlgebra : Type
```

### A.1. The sector inclusions

**`StandardModel.JetAlgebra.includeFermion`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L86).

> The inclusion of the fermionic sector.

```lean
noncomputable def includeFermion : FermionJetAlgebra →ₐ[ℂ] JetAlgebra
```

**`StandardModel.JetAlgebra.includeHiggs`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L90).

> The inclusion of the Higgs sector.

```lean
noncomputable def includeHiggs : HiggsJetAlgebra →ₐ[ℂ] JetAlgebra
```

**`StandardModel.JetAlgebra.includeGauge`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L95).

> The inclusion of the gauge sector. The Standard Model gauge bosons are the generic
> ones at `GaugeAlgebra`, so this is the connection inclusion of the datum itself.

```lean
noncomputable def includeGauge :
    (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) →ₐ[ℂ] JetAlgebra
```

**`StandardModel.JetAlgebra.includeGauge_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L99).

```lean
lemma includeGauge_apply (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    includeGauge y = ((1 : fieldData.MatterAlgebra) ⊗ₜ[ℂ] y : JetAlgebra)
```

**`StandardModel.JetAlgebra.includeFermion_apply_equiv`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L105).

> The fermionic sector inclusion factors through the sector equivalence and the generic
> fermionic factor inclusion.

```lean
lemma includeFermion_apply_equiv (a : FermionJetAlgebra) :
    includeFermion a = fieldData.includeFermion (fermionAlgebraEquiv a)
```

**`StandardModel.JetAlgebra.includeHiggs_apply_equiv`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L110).

> The Higgs sector inclusion factors through the sector equivalence and the generic
> bosonic factor inclusion.

```lean
lemma includeHiggs_apply_equiv (h : HiggsJetAlgebra) :
    includeHiggs h = fieldData.includeBoson (higgsAlgebraEquiv h)
```

**`StandardModel.JetAlgebra.includeGauge_eq_includeConnection`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L114).

> The gauge sector inclusion is the generic connection factor inclusion.

```lean
lemma includeGauge_eq_includeConnection :
    includeGauge = fieldData.includeConnection
```

**`StandardModel.JetAlgebra.includeFermion_ι`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L119).

> A degree-one element of the fermionic sector, included, is a total fermionic generator
> of the field datum, read through the fermionic generator identification.

```lean
lemma includeFermion_ι (v : JetComponentSpace fermionMatterField) :
    includeFermion (ExteriorAlgebra.ι ℂ v)
      = fieldData.ιFermionTotal (fermionGeneratorsEquiv.symm v)
```

**`StandardModel.JetAlgebra.includeHiggs_ι`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L129).

> A degree-one element of the Higgs sector, included, is the generator of the one bosonic
> species of the field datum.

```lean
lemma includeHiggs_ι (v : JetComponentSpace HiggsVec.matterField) :
    includeHiggs (SymmetricAlgebra.ι ℂ (JetComponentSpace HiggsVec.matterField) v)
      = fieldData.ιBoson () v
```

**`StandardModel.JetAlgebra.includeGauge_one_tmul_ι`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L143).

> A real degree-one element of the gauge sector, included, is a connection generator of
> the field datum: the connection factors of the two presentations are the same type, and
> the complexification is the scalar one.

```lean
lemma includeGauge_one_tmul_ι (v : GaugeBoson.JetComponentSpace GaugeAlgebra) :
    includeGauge ((1 : ℂ) ⊗ₜ[ℝ]
        SymmetricAlgebra.ι ℝ (GaugeBoson.JetComponentSpace GaugeAlgebra) v)
      = fieldData.ιConnection v
```

### A.2. Centrality of the gauge sector

**`StandardModel.JetAlgebra.includeGauge_commute`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean#L172).

> The image of the gauge sector is central: gauge-boson symbols commute with
> everything, as bosons must.

```lean
lemma includeGauge_commute (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) (x : JetAlgebra) :
    x * includeGauge y = includeGauge y * x
```

## Depends on

- [The sector algebras of the Standard Model inside its local field algebra](../part-08/jetalgebra-sectorequiv-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Basic.lean)
