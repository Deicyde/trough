---
declaration: module
origin: cited
lean: GaugeFieldData.covGaugeSectorRealizationEquiv, GaugeFieldData.covGaugeSectorRealizationEquiv_toAlgHom, GaugeFieldData.covGaugeSectorRealizationEquiv_toAlgHom_apply, GaugeFieldData.covGaugeSectorRealizationEquiv_F, GaugeFieldData.covGaugeSectorRealizationEquiv_symm_toAlgHom, GaugeFieldData.covGaugeSectorRealizationEquiv_symm_toAlgHom_apply, GaugeFieldData.covGaugeSectorRealizationEquiv_symm_toAlgHom_covF, GaugeFieldData.covGaugeSectorRealizationEquiv_restrictCovSector
statement: formalized
proof: formalized
---

# Realizations of the covariant gauge sector

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalCovField.GaugeSectorRealization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean): 8 declarations, 4 with a docstring.

## i. Overview

> For a complex algebra `B`, realizations of the covariant gauge sector
> `T.CovSectorAlgebra {FieldCategory.gauge}` are the real realizations of the covariant
> gauge-only algebra `LocalGaugeCovFieldAlgebra 𝔤` in `B`, its gauge and Lorentz actions
> viewed over `ℝ` by restriction of scalars. The correspondence is
> `GaugeFieldData.covGaugeSectorEquiv` composed with `AlgHom.liftEquiv`, and the
> field-strength towers agree on both sides.
>
> `GaugeFieldData.GaugeLorentzCompatible` is carried only to name the source Lorentz action,
> as on the sector realizations themselves. Restricting a realization of the whole local
> field algebra to the covariant gauge sector and passing to the gauge-only side is the
> covariant restriction of its ordinary gauge-only realization.

## ii. Key results

> - `GaugeFieldData.covGaugeSectorRealizationEquiv` : the correspondence, with both round
>   trips.
> - `GaugeFieldData.covGaugeSectorRealizationEquiv_F`,
>   `GaugeFieldData.covGaugeSectorRealizationEquiv_symm_toAlgHom_covF` : the field-strength
>   towers of corresponding realizations.
> - `GaugeFieldData.covGaugeSectorRealizationEquiv_restrictCovSector` : compatibility with
>   restriction from the local field algebra.

## iv. References

> * None.

## A. The correspondence

**`GaugeFieldData.covGaugeSectorRealizationEquiv`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L71).

> Realizations of the covariant gauge sector are the real realizations of the covariant
> gauge-only algebra, the target keeping its complex actions restricted to `ℝ`.

```lean
noncomputable def covGaugeSectorRealizationEquiv (hGL : T.GaugeLorentzCompatible) :
    CovSectorAlgebra.Realization T {FieldCategory.gauge} hGL B repGauge repLorentz
      ≃ LocalGaugeCovFieldAlgebra.Realization jets B (repGauge.restrictScalars ℝ)
          (repLorentz.restrictScalars ℝ)
```

## B. Computation

**`GaugeFieldData.covGaugeSectorRealizationEquiv_toAlgHom`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L90).

```lean
lemma covGaugeSectorRealizationEquiv_toAlgHom
    (k : CovSectorAlgebra.Realization T {FieldCategory.gauge} hGL B repGauge repLorentz) :
    (T.covGaugeSectorRealizationEquiv hGL k).toAlgHom
      = ((k.toAlgHom.comp T.covGaugeSectorEquiv.toAlgHom).restrictScalars ℝ).comp
          Algebra.TensorProduct.includeRight
```

**`GaugeFieldData.covGaugeSectorRealizationEquiv_toAlgHom_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L97).

```lean
lemma covGaugeSectorRealizationEquiv_toAlgHom_apply
    (k : CovSectorAlgebra.Realization T {FieldCategory.gauge} hGL B repGauge repLorentz)
    (x : LocalGaugeCovFieldAlgebra 𝔤) :
    (T.covGaugeSectorRealizationEquiv hGL k).toAlgHom x
      = k.toAlgHom (T.covGaugeSectorEquiv ((1 : ℂ) ⊗ₜ[ℝ] x))
```

**`GaugeFieldData.covGaugeSectorRealizationEquiv_F`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L105).

> The field-strength tower of the corresponding real realization is the sector tower,
> with the same derivative labels, spacetime indices and adjoint covector.

```lean
lemma covGaugeSectorRealizationEquiv_F
    (k : CovSectorAlgebra.Realization T {FieldCategory.gauge} hGL B repGauge repLorentz)
    (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (T.covGaugeSectorRealizationEquiv hGL k).F l μ ν φ
      = k.toAlgHom
          (T.covGaugeSectorEquiv ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeCovFieldAlgebra.covF 𝔤 l μ ν φ))
```

**`GaugeFieldData.covGaugeSectorRealizationEquiv_symm_toAlgHom`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L113).

```lean
lemma covGaugeSectorRealizationEquiv_symm_toAlgHom
    (h : LocalGaugeCovFieldAlgebra.Realization jets B (repGauge.restrictScalars ℝ)
      (repLorentz.restrictScalars ℝ)) :
    ((T.covGaugeSectorRealizationEquiv hGL).symm h).toAlgHom
      = (AlgHom.liftEquiv ℝ ℂ (LocalGaugeCovFieldAlgebra 𝔤) B h.toAlgHom).comp
          T.covGaugeSectorEquiv.symm.toAlgHom
```

**`GaugeFieldData.covGaugeSectorRealizationEquiv_symm_toAlgHom_apply`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L121).

```lean
lemma covGaugeSectorRealizationEquiv_symm_toAlgHom_apply
    (h : LocalGaugeCovFieldAlgebra.Realization jets B (repGauge.restrictScalars ℝ)
      (repLorentz.restrictScalars ℝ)) (x : T.CovSectorAlgebra {FieldCategory.gauge}) :
    ((T.covGaugeSectorRealizationEquiv hGL).symm h).toAlgHom x
      = AlgHom.liftEquiv ℝ ℂ (LocalGaugeCovFieldAlgebra 𝔤) B h.toAlgHom
          (T.covGaugeSectorEquiv.symm x)
```

**`GaugeFieldData.covGaugeSectorRealizationEquiv_symm_toAlgHom_covF`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L130).

> The sector towers of the corresponding sector realization are the tower of the real
> realization; at `l = []` this is the field strength.

```lean
lemma covGaugeSectorRealizationEquiv_symm_toAlgHom_covF
    (h : LocalGaugeCovFieldAlgebra.Realization jets B (repGauge.restrictScalars ℝ)
      (repLorentz.restrictScalars ℝ)) (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    ((T.covGaugeSectorRealizationEquiv hGL).symm h).toAlgHom
        (T.covGaugeSectorEquiv ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeCovFieldAlgebra.covF 𝔤 l μ ν φ))
      = h.F l μ ν φ
```

## C. Compatibility with restriction

**`GaugeFieldData.covGaugeSectorRealizationEquiv_restrictCovSector`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean#L155).

> Restricting a realization of the local field algebra to the covariant gauge sector and
> passing to the gauge-only side gives the covariant restriction of its ordinary gauge-only
> realization.

```lean
lemma covGaugeSectorRealizationEquiv_restrictCovSector
    {repJet : Representation ℂ GJ B} (h : Realization T B repJet repLorentz) :
    T.covGaugeSectorRealizationEquiv hGL (h.restrictCovSector hGL {FieldCategory.gauge})
      = (T.gaugeSectorRealizationEquiv (h.restrictSector {FieldCategory.gauge})).restrict
```

## Depends on

- [Realizations of the covariant field algebra (LocalGaugeCov/Realization)](../part-01/gaugeboson-localgaugecov-realization.md)
- [The covariant gauge sector as the complexified covariant gauge-only algebra](localcovfield-gaugesector.md)
- [Realizations of the covariant sector algebras](../part-03/localcovfield-sectorrealization.md)
- [Realizations of the ordinary gauge sector](../part-03/localfield-gaugesectorrealization.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/GaugeSectorRealization.lean)
