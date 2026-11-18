---
declaration: module
origin: cited
lean: GaugeFieldData.gaugeSectorRealizationEquiv, GaugeFieldData.gaugeSectorRealizationEquiv_toAlgHom, GaugeFieldData.gaugeSectorRealizationEquiv_toAlgHom_apply, GaugeFieldData.gaugeSectorRealizationEquiv_A, GaugeFieldData.gaugeSectorRealizationEquiv_symm_toAlgHom, GaugeFieldData.gaugeSectorRealizationEquiv_symm_toAlgHom_apply, GaugeFieldData.gaugeSectorRealizationEquiv_symm_toAlgHom_gaugeField
statement: formalized
proof: formalized
---

# Realizations of the ordinary gauge sector

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.GaugeSectorRealization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean): 7 declarations, 3 with a docstring.

## i. Overview

> For a complex algebra `B`, realizations of the ordinary gauge sector
> `T.SectorAlgebra {FieldCategory.gauge}` are the real realizations of the gauge-only algebra
> `LocalGaugeFieldAlgebra 𝔤` in `B`, its two actions viewed over `ℝ` by restriction of
> scalars. The correspondence is the algebra equivalence `GaugeFieldData.gaugeSectorEquiv`
> composed with the universal property of base change `AlgHom.liftEquiv`; the gauge symbols
> `∂_s A_μ^φ` agree on both sides.

## ii. Key results

> - `GaugeFieldData.gaugeSectorRealizationEquiv` : the correspondence, with both round trips.
> - `GaugeFieldData.gaugeSectorRealizationEquiv_A`,
>   `GaugeFieldData.gaugeSectorRealizationEquiv_symm_toAlgHom_gaugeField` : the gauge symbols
>   of corresponding realizations.

## iv. References

> * None.

## A. The correspondence

**`GaugeFieldData.gaugeSectorRealizationEquiv`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean#L61).

> Realizations of the ordinary gauge sector are the real realizations of the gauge-only
> algebra, the target keeping its complex actions restricted to `ℝ`.

```lean
noncomputable def gaugeSectorRealizationEquiv :
    SectorAlgebra.Realization T {FieldCategory.gauge} B repJet repLorentz
      ≃ LocalGaugeFieldAlgebra.Realization jets B (repJet.restrictScalars ℝ)
          (repLorentz.restrictScalars ℝ)
```

## B. Computation

**`GaugeFieldData.gaugeSectorRealizationEquiv_toAlgHom`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean#L77).

```lean
lemma gaugeSectorRealizationEquiv_toAlgHom
    (f : SectorAlgebra.Realization T {FieldCategory.gauge} B repJet repLorentz) :
    (T.gaugeSectorRealizationEquiv f).toAlgHom
      = ((f.toAlgHom.comp T.gaugeSectorEquiv.toAlgHom).restrictScalars ℝ).comp
          Algebra.TensorProduct.includeRight
```

**`GaugeFieldData.gaugeSectorRealizationEquiv_toAlgHom_apply`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean#L84).

```lean
lemma gaugeSectorRealizationEquiv_toAlgHom_apply
    (f : SectorAlgebra.Realization T {FieldCategory.gauge} B repJet repLorentz)
    (x : LocalGaugeFieldAlgebra 𝔤) :
    (T.gaugeSectorRealizationEquiv f).toAlgHom x
      = f.toAlgHom (T.gaugeSectorEquiv ((1 : ℂ) ⊗ₜ[ℝ] x))
```

**`GaugeFieldData.gaugeSectorRealizationEquiv_A`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean#L91).

> The gauge symbols of the corresponding real realization are the sector symbols.

```lean
lemma gaugeSectorRealizationEquiv_A
    (f : SectorAlgebra.Realization T {FieldCategory.gauge} B repJet repLorentz)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (T.gaugeSectorRealizationEquiv f).A s μ φ
      = f.toAlgHom (T.gaugeSectorEquiv (LocalGaugeFieldAlgebra.gaugeField 𝔤 s μ φ))
```

**`GaugeFieldData.gaugeSectorRealizationEquiv_symm_toAlgHom`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean#L99).

```lean
lemma gaugeSectorRealizationEquiv_symm_toAlgHom
    (h : LocalGaugeFieldAlgebra.Realization jets B (repJet.restrictScalars ℝ)
      (repLorentz.restrictScalars ℝ)) :
    (T.gaugeSectorRealizationEquiv.symm h).toAlgHom
      = (AlgHom.liftEquiv ℝ ℂ (LocalGaugeFieldAlgebra 𝔤) B h.toAlgHom).comp
          T.gaugeSectorEquiv.symm.toAlgHom
```

**`GaugeFieldData.gaugeSectorRealizationEquiv_symm_toAlgHom_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean#L107).

```lean
lemma gaugeSectorRealizationEquiv_symm_toAlgHom_apply
    (h : LocalGaugeFieldAlgebra.Realization jets B (repJet.restrictScalars ℝ)
      (repLorentz.restrictScalars ℝ)) (x : T.SectorAlgebra {FieldCategory.gauge}) :
    (T.gaugeSectorRealizationEquiv.symm h).toAlgHom x
      = AlgHom.liftEquiv ℝ ℂ (LocalGaugeFieldAlgebra 𝔤) B h.toAlgHom
          (T.gaugeSectorEquiv.symm x)
```

**`GaugeFieldData.gaugeSectorRealizationEquiv_symm_toAlgHom_gaugeField`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean#L115).

> The sector symbols of the corresponding sector realization are the gauge symbols.

```lean
lemma gaugeSectorRealizationEquiv_symm_toAlgHom_gaugeField
    (h : LocalGaugeFieldAlgebra.Realization jets B (repJet.restrictScalars ℝ)
      (repLorentz.restrictScalars ℝ)) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    (T.gaugeSectorRealizationEquiv.symm h).toAlgHom
        (T.gaugeSectorEquiv (LocalGaugeFieldAlgebra.gaugeField 𝔤 s μ φ)) = h.A s μ φ
```

## Depends on

- [Realizations of the local gauge field algebra](../part-01/gaugeboson-localgauge-realization.md)
- [The gauge sector as the complexified gauge-only algebra](localfield-gaugesector.md)
- [Realizations of the ordinary sector algebras](../part-04/localfield-sectorrealization.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeSectorRealization.lean)
