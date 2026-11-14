---
declaration: module
origin: cited
lean: LocalGaugeFieldAlgebra.gaugeField, LocalGaugeFieldAlgebra.gaugeField_apply, LocalGaugeFieldAlgebra.repLorentz_gaugeField, LocalGaugeFieldAlgebra.repJet_gaugeField
statement: formalized
proof: formalized
---

# The gauge-field symbols of the jet algebra and their laws

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGauge.GaugeField`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean): 4 declarations, 3 with a docstring.

## i. Overview

> The derivative symbols `∂_s A_μ^φ` of the complexified gauge-boson jet algebra, packaged as
> a family over the derivative multiset, the spacetime index and the dual of the gauge
> algebra, `LocalGaugeFieldAlgebra.gaugeField`, and the two transformation laws they satisfy: the
> Lorentz law, in which the symbol carries one covector index and each derivative slot
> transforms as a covector, and the gauge law, in which a jet acts by the Leibniz convolution
> of its adjoint Taylor coefficients plus the Maurer–Cartan shift. These are the laws that a
> realization of the jet algebra in another algebra inherits.
>
>
> - `LocalGaugeFieldAlgebra.gaugeField` : the gauge-field symbols of the jet algebra.
> - `LocalGaugeFieldAlgebra.repLorentz_gaugeField` : the Lorentz law.
> - `LocalGaugeFieldAlgebra.repJet_gaugeField` : the gauge law.

## ii. Key results

> - `gaugeField` : the gauge-field derivative symbols of the complexified gauge-boson jet algebra, as
>   a family over the derivative multiset, the spacetime index and the dual of the gauge algebra — the
>   form consumed by the abstract covariance machinery
> - `gaugeField_apply`
> - `repLorentz_gaugeField` : the Lorentz law of the jet algebra: the symbol `∂_s A_μ^φ` carries one
>   covector index, and each derivative slot transforms as a covector, by `IsLorentzDeriv`
> - `repJet_gaugeField` : the gauge law of the jet algebra: a jet `U` acts on `∂_s A_μ^φ` by the
>   Leibniz convolution of the dual adjoint Taylor coefficients of `U⁻¹` against lower symbols, plus
>   the base-point value of the `s`-th derivative of the Maurer–Cartan form of `U⁻¹`

## iv. References

> * None.

## A. The gauge-field symbols and their laws

**`LocalGaugeFieldAlgebra.gaugeField`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean#L72).

> The gauge-field derivative symbols of the complexified gauge-boson jet algebra, as a
> family over the derivative multiset, the spacetime index and the dual of the gauge
> algebra — the form consumed by the abstract covariance machinery.

```lean
noncomputable def gaugeField (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.gaugeField_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean#L79).

```lean
lemma gaugeField_apply (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    (gaugeField 𝔤) s μ φ = Lorentz.iteratedD (complexJetDeriv 𝔤) complexJetDeriv_comm s
      ((1 : ℂ) ⊗ₜ[ℝ] (ofA 𝔤) μ φ)
```

**`LocalGaugeFieldAlgebra.repLorentz_gaugeField`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean#L87).

> The Lorentz law of the jet algebra: the symbol `∂_s A_μ^φ` carries one covector index,
> and each derivative slot transforms as a covector, by `IsLorentzDeriv`.

```lean
lemma repLorentz_gaugeField (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (complexRepLorentzGroup 𝔤) Λ (gaugeField 𝔤 (List.ofFn l) μ φ) =
      ∑ (p : Fin n → (Fin 1 ⊕ Fin 3)),
        (∏ (i : Fin n), (((SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ) : ℂ)) •
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        gaugeField 𝔤 (List.ofFn p) a φ
```

**`LocalGaugeFieldAlgebra.repJet_gaugeField`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean#L113).

> The gauge law of the jet algebra: a jet `U` acts on `∂_s A_μ^φ` by the Leibniz
> convolution of the dual adjoint Taylor coefficients of `U⁻¹` against lower symbols, plus
> the base-point value of the `s`-th derivative of the Maurer–Cartan form of `U⁻¹`.

```lean
lemma repJet_gaugeField (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    complexRepJet jets U (gaugeField 𝔤 s μ φ) =
      (s.antidiagonal.map fun p => gaugeField 𝔤 p.2 μ (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + algebraMap ℂ (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)
          (φ (jets.evalLie (jets.iteratedDeriv s (jets.maurerCartan U⁻¹ μ))))
```

## Depends on

- [The gauge action on the gauge-boson jet algebra](gaugeboson-localgauge-gaugeaction.md)
- [The Lorentz action on the gauge-boson jet algebra](gaugeboson-localgauge-lorentzaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/GaugeField.lean)
