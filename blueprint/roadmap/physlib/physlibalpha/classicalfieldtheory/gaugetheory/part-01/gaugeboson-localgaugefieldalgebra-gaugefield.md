---
declaration: module
origin: cited
lean: LocalGaugeFieldAlgebra.gaugeField, LocalGaugeFieldAlgebra.gaugeField_apply, LocalGaugeFieldAlgebra.repLorentz_gaugeField, LocalGaugeFieldAlgebra.repJet_gaugeField, LocalGaugeFieldAlgebra.transformsAsGaugeField_gaugeField, LocalGaugeFieldAlgebra.mapGaugeField, LocalGaugeFieldAlgebra.mapGaugeField_apply, LocalGaugeFieldAlgebra.commute_mapGaugeField
statement: formalized
proof: formalized
---

# The gauge-field symbols of the jet algebra and their laws

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeFieldAlgebra.GaugeField`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean): 10 declarations, 8 with a docstring.

> The derivative symbols `∂_s A_μ^φ` of the complexified gauge-boson jet algebra, with their
> Lorentz and gauge laws.

## i. Overview

> The derivative symbols `∂_s A_μ^φ` of the complexified gauge-boson jet algebra are packaged as
> a family over the derivative multiset, the spacetime index and the dual of the gauge
> algebra, `LocalGaugeFieldAlgebra.gaugeField`. They satisfy two transformation laws. In the
> Lorentz law the symbol carries one covector index and each derivative slot transforms as a
> covector. In the gauge law a jet acts by the Leibniz convolution of its adjoint Taylor
> coefficients plus the Maurer–Cartan shift.
>
> An algebra map `f` out of the complexified jet algebra carries the symbols into any complex
> algebra `B`, as `mapGaugeField f`. When `f` intertwines the gauge and Lorentz actions, the
> carried symbols satisfy the same two laws, `GaugeBoson.TransformsAsGaugeField` and
> `GaugeBoson.LorentzTransformsAsGaugeField`, and they commute with each other whatever `B` is
> (`commute_mapGaugeField`). This is how the gauge fields of the local field algebra of a field
> datum, and of any realization of it, inherit their laws, and with them every consequence
> proved in the directory `PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily`.
> The identity of the jet algebra is the case `transformsAsGaugeField_gaugeField`.

## ii. Key results

> - `LocalGaugeFieldAlgebra.gaugeField` : the gauge-field symbols of the jet algebra.
> - `LocalGaugeFieldAlgebra.repLorentz_gaugeField` : the Lorentz law.
> - `LocalGaugeFieldAlgebra.repJet_gaugeField` : the gauge law.
> - `LocalGaugeFieldAlgebra.mapGaugeField` : the symbols carried into another algebra.
> - `LocalGaugeFieldAlgebra.transformsAsGaugeField_mapGaugeField`,
>   `LocalGaugeFieldAlgebra.lorentzTransformsAsGaugeField_mapGaugeField` : the two laws along an
>   equivariant algebra map.

## iv. References

> * None.

## A. The gauge-field symbols and their laws

**`LocalGaugeFieldAlgebra.gaugeField`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L76).

> The gauge-field derivative symbols of the complexified gauge-boson jet algebra, as a
> family over the derivative multiset, the spacetime index and the dual of the gauge
> algebra, the form consumed by the abstract covariance machinery.

```lean
noncomputable def gaugeField (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.gaugeField_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L82).

```lean
lemma gaugeField_apply (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    (gaugeField G) s μ φ = Lorentz.iteratedD (complexJetDeriv G) complexJetDeriv_comm s
      ((1 : ℂ) ⊗ₜ[ℝ] (ofA G) μ φ)
```

**`LocalGaugeFieldAlgebra.repLorentz_gaugeField`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L89).

> The Lorentz law of the jet algebra. The symbol `∂_s A_μ^φ` carries one covector index,
> and each derivative slot transforms as a covector, by `IsLorentzDeriv`.

```lean
lemma repLorentz_gaugeField (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (complexRepLorentzGroup G) Λ (gaugeField G (List.ofFn l) μ φ) =
      ∑ (p : Fin n → (Fin 1 ⊕ Fin 3)),
        (∏ (i : Fin n), (((SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ) : ℂ)) •
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        gaugeField G (List.ofFn p) a φ
```

**`LocalGaugeFieldAlgebra.repJet_gaugeField`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L114).

> The gauge law of the jet algebra. A jet `U` acts on `∂_s A_μ^φ` by the Leibniz
> convolution of the dual adjoint Taylor coefficients of `U⁻¹` against lower symbols, plus
> the base-point value of the `s`-th derivative of the Maurer–Cartan form of `U⁻¹`.

```lean
lemma repJet_gaugeField (U : G.gaugeJetGroup) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    complexRepJet G U (gaugeField G s μ φ) =
      (s.antidiagonal.map fun p => gaugeField G p.2 μ (G.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + algebraMap ℂ (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G)
          (φ (G.evalLie (G.iteratedDerivJ s
            (-G.maurerCartan U⁻¹ μ))))
```

**`LocalGaugeFieldAlgebra.transformsAsGaugeField_gaugeField`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L125).

> The symbols of the jet algebra transform as a gauge field.

```lean
lemma transformsAsGaugeField_gaugeField :
    GaugeBoson.TransformsAsGaugeField G (complexRepJet G) (gaugeField G)
```

## B. The gauge-field symbols along an algebra map

**`LocalGaugeFieldAlgebra.mapGaugeField`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L141).

> The gauge-field symbols `∂_s A_μ^φ` carried into a complex algebra `B` by an algebra map
> out of the complexified gauge-boson jet algebra.

```lean
noncomputable def mapGaugeField (f : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G →ₐ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

**`LocalGaugeFieldAlgebra.mapGaugeField_apply`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L147).

```lean
lemma mapGaugeField_apply (f : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G →ₐ[ℂ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    mapGaugeField f s μ φ = f (gaugeField G s μ φ)
```

**`LocalGaugeFieldAlgebra.commute_mapGaugeField`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L153).

> The carried gauge-field symbols commute with each other, being images of a commutative
> algebra.

```lean
lemma commute_mapGaugeField (f : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G →ₐ[ℂ] B)
    (p q : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ ψ : Module.Dual ℝ G.lieSubalgebra) :
    Commute (mapGaugeField f p μ φ) (mapGaugeField f q ν ψ)
```

**`LocalGaugeFieldAlgebra.transformsAsGaugeField_mapGaugeField`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L167).

> The gauge law along an algebra map intertwining the gauge actions. A jet `U` acts on the
> carried symbol `∂_s A_μ^φ` by the Leibniz convolution of the dual adjoint Taylor coefficients
> of `U⁻¹` against lower symbols, plus the base-point value of the `s`-th derivative of the
> Maurer–Cartan form of `U⁻¹`.

```lean
lemma transformsAsGaugeField_mapGaugeField (f : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G →ₐ[ℂ] B)
    (hf : ∀ (U : G.gaugeJetGroup) (x : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G),
      f (complexRepJet G U x) = repGauge U (f x)) :
    GaugeBoson.TransformsAsGaugeField G repGauge (mapGaugeField f)
```

**`LocalGaugeFieldAlgebra.lorentzTransformsAsGaugeField_mapGaugeField`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean#L181).

> The Lorentz law along an algebra map intertwining the Lorentz actions. The carried symbol
> carries one covector index, and each derivative slot transforms as a covector.

```lean
lemma lorentzTransformsAsGaugeField_mapGaugeField (f : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G →ₐ[ℂ] B)
    (hf : ∀ (Λ : SL(2,ℂ)) (x : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G),
      f (complexRepLorentzGroup G Λ x) = repLorentz Λ (f x)) :
    GaugeBoson.LorentzTransformsAsGaugeField repLorentz (mapGaugeField f)
```

## Depends on

- [The gauge law of a gauge field and of its covariant expressions](gaugeboson-adjointfamily-gaugelaw.md)
- [The gauge action on the gauge-boson jet algebra](gaugeboson-localgaugefieldalgebra-gaugeaction.md)
- [The Lorentz action on the gauge-boson jet algebra](gaugeboson-localgaugefieldalgebra-lorentzaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/GaugeField.lean)
