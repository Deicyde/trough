---
declaration: module
origin: cited
lean: LocalGaugeFieldAlgebra.derivA, LocalGaugeFieldAlgebra.derivA_apply, LocalGaugeFieldAlgebra.derivA_zero, LocalGaugeFieldAlgebra.derivA_eq_iteratedJetDeriv, LocalGaugeFieldAlgebra.gaugeField_eq_one_tmul_derivA, LocalGaugeFieldAlgebra.algHom_ext, LocalGaugeFieldAlgebra.fieldStrength, LocalGaugeFieldAlgebra.fieldStrength_apply
statement: formalized
proof: formalized
---

# The field strength in the local gauge field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGauge.FieldStrength`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean): 27 declarations, 25 with a docstring.

## i. Overview

> The field strength and its covariant derivatives are built for an arbitrary realization of
> the gauge bosons in `Physlib.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Realization`, as
> families of derivative symbols over a family of gauge-field symbols. Here they are
> specialized to the real algebra `LocalGaugeFieldAlgebra 𝔤` itself, whose symbols are its
> own generators `∂_s A_μ^φ` (`derivA`).
>
> Two facts make the specialization work. The symbols that the families carry are honest
> iterated derivatives of their base values
> (`iteratedCovDerivAdjoint_fieldStrength_derivA`), which turns the symbol-level recursion
> of `iteratedCovDerivAdjoint` into the recursion `covDerivFieldStrength_cons` on elements
> of the algebra. And the gauge law is not reproved: the complexified tower is the image of
> the real one under `x ↦ 1 ⊗ₜ x`, which is injective and intertwines the two gauge actions,
> so the law of the identity realization descends. The Lorentz law is proved directly from
> the recursion.
>
> Everything here is over `ℝ`. The complexification `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤`
> appears only as that bridge; it is never identified with the real algebra.

## ii. Key results

> - `LocalGaugeFieldAlgebra.fieldStrength`, `LocalGaugeFieldAlgebra.covDerivFieldStrength` :
>   the field strength `F_μν^φ` and its ordered covariant derivatives `∇_l F_μν^φ`.
> - `LocalGaugeFieldAlgebra.repJet_covDerivFieldStrength_eval` : the gauge law, through the
>   value of the jet alone.
> - `LocalGaugeFieldAlgebra.repLorentzGroup_covDerivFieldStrength` : the Lorentz law.

## iv. References

> * None.

## A. The derivative symbols of the real algebra

**`LocalGaugeFieldAlgebra.derivA`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L80).

> The derivative symbols `∂_s A_μ^φ` of the local gauge field algebra, as a family over
> the derivative multiset `s` and the spacetime index `μ`: the iterated total derivative of
> the gauge-field generator. The field strength and its covariant derivatives are built
> out of this family.

```lean
noncomputable def derivA (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] LocalGaugeFieldAlgebra 𝔤
```

**`LocalGaugeFieldAlgebra.derivA_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L85).

```lean
lemma derivA_apply (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) : derivA 𝔤 s μ φ = iteratedJetDeriv 𝔤 s (ofA 𝔤 μ φ)
```

**`LocalGaugeFieldAlgebra.derivA_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L90).

```lean
lemma derivA_zero (μ : Fin 1 ⊕ Fin 3) : derivA 𝔤 0 μ = ofA 𝔤 μ
```

**`LocalGaugeFieldAlgebra.derivA_eq_iteratedJetDeriv`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L94).

> The derivative symbols are the iterated derivatives of the undifferentiated symbol.

```lean
lemma derivA_eq_iteratedJetDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) : derivA 𝔤 s μ φ = iteratedJetDeriv 𝔤 s (derivA 𝔤 0 μ φ)
```

**`LocalGaugeFieldAlgebra.gaugeField_eq_one_tmul_derivA`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L99).

> The complexified symbols `gaugeField` are the images of the real symbols.

```lean
lemma gaugeField_eq_one_tmul_derivA (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) : gaugeField 𝔤 s μ φ = (1 : ℂ) ⊗ₜ[ℝ] derivA 𝔤 s μ φ
```

**`LocalGaugeFieldAlgebra.algHom_ext`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L107).

> Two algebra maps out of the local gauge field algebra agreeing on the derivative
> symbols `∂_s A_μ^φ` are equal.

```lean
lemma algHom_ext {B : Type} [Semiring B] [Algebra ℝ B] {f g : LocalGaugeFieldAlgebra 𝔤 →ₐ[ℝ] B}
    (h : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤),
      f (derivA 𝔤 s μ φ) = g (derivA 𝔤 s μ φ)) : f = g
```

## B. The field strength and its covariant derivatives

**`LocalGaugeFieldAlgebra.fieldStrength`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L125).

> The field strength `F_μν = ∂_μ A_ν − ∂_ν A_μ + ⁅A_μ, A_ν⁆` of the local gauge field
> algebra: the underived field strength of the family of derivative symbols, in the
> conventions of `GaugeAlgebraRealization.fieldStrength`, where the bracket of the gauge
> algebra carries the physicists' factor of `i`.

```lean
noncomputable def fieldStrength (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] LocalGaugeFieldAlgebra 𝔤
```

**`LocalGaugeFieldAlgebra.fieldStrength_apply`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L130).

> The field strength written in the generators of the algebra.

```lean
lemma fieldStrength_apply (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    fieldStrength 𝔤 μ ν φ = jetDeriv 𝔤 μ (ofA 𝔤 ν φ) - jetDeriv 𝔤 ν (ofA 𝔤 μ φ)
      + bracketFam (ofA 𝔤 μ) (ofA 𝔤 ν) φ
```

**`LocalGaugeFieldAlgebra.fieldStrength_swap`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L139).

> The field strength is antisymmetric in its two covector indices.

```lean
lemma fieldStrength_swap (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength 𝔤 ν μ = - fieldStrength 𝔤 μ ν
```

**`LocalGaugeFieldAlgebra.covDerivFieldStrength`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L148).

> The iterated covariant derivative `∇_{l₁} ⋯ ∇_{lₙ} F_μν` of the field strength along an
> ordered list of directions, with `∇_ρ F = ∂_ρ F + ⁅A_ρ, F⁆` the covariant derivative in
> the adjoint. Covariant derivatives do not commute, so the iteration is indexed by a list
> and not by a multiset; the empty list gives the field strength itself.

```lean
noncomputable def covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] LocalGaugeFieldAlgebra 𝔤
```

**`LocalGaugeFieldAlgebra.covDerivFieldStrength_nil`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L154).

> Zero covariant derivatives: the field strength itself.

```lean
lemma covDerivFieldStrength_nil (μ ν : Fin 1 ⊕ Fin 3) :
    covDerivFieldStrength 𝔤 [] μ ν = fieldStrength 𝔤 μ ν
```

## C. The derivative symbols of the covariant tower are iterated derivatives

> The families of `GaugeAlgebraRealization` carry the derivative symbols `∂_s F` of a
> covariant expression as data. Here the Leibniz convolutions defining the derived brackets
> really are the Leibniz rule of the total derivative, so those symbols are the iterated
> total derivatives `∂_s` of the value at `0`.

**`LocalGaugeFieldAlgebra.iteratedJetDeriv_bracketFam`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L170).

> The Leibniz rule of the iterated total derivative on a bracket of families: the
> antidiagonal convolution of the iterated derivatives of the two factors.

```lean
lemma iteratedJetDeriv_bracketFam (s : Multiset (Fin 1 ⊕ Fin 3))
    (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] LocalGaugeFieldAlgebra 𝔤) (φ : Module.Dual ℝ 𝔤) :
    iteratedJetDeriv 𝔤 s (bracketFam f g φ) = (s.antidiagonal.map fun p =>
      bracketFam (iteratedJetDeriv 𝔤 p.1 ∘ₗ f) (iteratedJetDeriv 𝔤 p.2 ∘ₗ g) φ).sum
```

**`LocalGaugeFieldAlgebra.bracketFamConv_derivA`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L200).

> If a family consists of the iterated derivatives of its base value, so does its derived
> bracket against the gauge field: the Leibniz convolution is the iterated derivative of the
> bracket of the base values.

```lean
lemma bracketFamConv_derivA (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ]
    LocalGaugeFieldAlgebra 𝔤)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤),
      F s φ = iteratedJetDeriv 𝔤 s (F 0 φ))
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤) :
    bracketFamConv (derivA 𝔤) ρ F s φ
      = iteratedJetDeriv 𝔤 s (bracketFam (ofA 𝔤 ρ) (F 0) φ)
```

**`LocalGaugeFieldAlgebra.covDerivAdjoint_derivA`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L216).

> The covariant derivative of a family of iterated derivatives is again a family of
> iterated derivatives.

```lean
lemma covDerivAdjoint_derivA (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ]
    LocalGaugeFieldAlgebra 𝔤)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤),
      F s φ = iteratedJetDeriv 𝔤 s (F 0 φ))
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤) :
    covDerivAdjoint (derivA 𝔤) F ρ s φ
      = iteratedJetDeriv 𝔤 s (covDerivAdjoint (derivA 𝔤) F ρ 0 φ)
```

**`LocalGaugeFieldAlgebra.fieldStrength_derivA`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L232).

> The derivative symbols of the field strength are the iterated derivatives of the field
> strength.

```lean
lemma fieldStrength_derivA (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ 𝔤) :
    GaugeAlgebraRealization.fieldStrength (derivA 𝔤) μ ν s φ
      = iteratedJetDeriv 𝔤 s (fieldStrength 𝔤 μ ν φ)
```

**`LocalGaugeFieldAlgebra.iteratedCovDerivAdjoint_fieldStrength_derivA`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L250).

> The derivative symbols of the covariant derivatives of the field strength are the
> iterated derivatives of their base values.

```lean
lemma iteratedCovDerivAdjoint_fieldStrength_derivA (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤) :
    iteratedCovDerivAdjoint (derivA 𝔤) l (GaugeAlgebraRealization.fieldStrength (derivA 𝔤) μ ν)
        s φ
      = iteratedJetDeriv 𝔤 s (covDerivFieldStrength 𝔤 l μ ν φ)
```

**`LocalGaugeFieldAlgebra.covDerivFieldStrength_cons`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L261).

> The covariant derivative `∇_ρ F = ∂_ρ F + ⁅A_ρ, F⁆` peeled off the front of the list:
> the recursion on elements of the algebra.

```lean
lemma covDerivFieldStrength_cons (ρ : Fin 1 ⊕ Fin 3) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    covDerivFieldStrength 𝔤 (ρ :: l) μ ν φ
      = jetDeriv 𝔤 ρ (covDerivFieldStrength 𝔤 l μ ν φ)
        + bracketFam (ofA 𝔤 ρ) (covDerivFieldStrength 𝔤 l μ ν) φ
```

## D. The gauge law, by descent from the complexification

> The gauge law is proved in
> `Physlib.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Realization` for a realization in a
> complex algebra, and `GaugeAlgebraRealization.id` realizes the real algebra in its
> complexification. Injectivity of `x ↦ 1 ⊗ₜ x` reads the real law off the complex one; no
> reality argument beyond that is involved.

**`LocalGaugeFieldAlgebra.one_tmul_iteratedCovDerivAdjoint_fieldStrength`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L288).

> The complexified covariant tower of the identity realization is the image of the real
> one.

```lean
lemma one_tmul_iteratedCovDerivAdjoint_fieldStrength (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤) :
    (1 : ℂ) ⊗ₜ[ℝ] iteratedCovDerivAdjoint (derivA 𝔤) l
        (GaugeAlgebraRealization.fieldStrength (derivA 𝔤) μ ν) s φ
      = iteratedCovDerivAdjoint (gaugeField 𝔤) l
        (GaugeAlgebraRealization.fieldStrength (gaugeField 𝔤) μ ν) s φ
```

**`LocalGaugeFieldAlgebra.repJet_iteratedCovDerivAdjoint_fieldStrength`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L313).

> The gauge law of the covariant derivatives of the field strength at every derivative
> order: a jet acts by the Leibniz convolution of the dual adjoint Taylor coefficients of
> `U⁻¹` against lower derivative symbols, with no Maurer–Cartan shift.

```lean
lemma repJet_iteratedCovDerivAdjoint_fieldStrength (U : GJ) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ 𝔤) :
    repJet jets U (iteratedCovDerivAdjoint (derivA 𝔤) l
        (GaugeAlgebraRealization.fieldStrength (derivA 𝔤) μ ν) s φ)
      = (s.antidiagonal.map fun p => iteratedCovDerivAdjoint (derivA 𝔤) l
          (GaugeAlgebraRealization.fieldStrength (derivA 𝔤) μ ν) p.2
          (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
```

**`LocalGaugeFieldAlgebra.repJet_covDerivFieldStrength`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L332).

> The gauge law of the covariant derivatives of the field strength: a jet acts through
> the zeroth dual adjoint Taylor coefficient of `U⁻¹` on the adjoint index alone.

```lean
lemma repJet_covDerivFieldStrength (U : GJ) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repJet jets U (covDerivFieldStrength 𝔤 l μ ν φ)
      = covDerivFieldStrength 𝔤 l μ ν (jets.adjointDualCoeff U⁻¹ 0 φ)
```

**`LocalGaugeFieldAlgebra.repJet_covDerivFieldStrength_eval`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L344).

> On the covariant derivatives of the field strength the local gauge action factors
> through evaluation: a jet `U` acts through the dual base-point adjoint action of the
> value `jets.eval U⁻¹` of its inverse, and the derivatives of the jet are not seen. The
> covariant expressions are gauge covariant, not gauge invariant.

```lean
lemma repJet_covDerivFieldStrength_eval (U : GJ) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repJet jets U (covDerivFieldStrength 𝔤 l μ ν φ)
      = covDerivFieldStrength 𝔤 l μ ν ((jets.adjoint (jets.eval U⁻¹)).dualMap φ)
```

**`LocalGaugeFieldAlgebra.repJet_fieldStrength`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L351).

> The field strength transforms in the adjoint.

```lean
lemma repJet_fieldStrength (U : GJ) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repJet jets U (fieldStrength 𝔤 μ ν φ)
      = fieldStrength 𝔤 μ ν ((jets.adjoint (jets.eval U⁻¹)).dualMap φ)
```

## E. The Lorentz law

**`LocalGaugeFieldAlgebra.repLorentzGroup_comp_ofA`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L368).

> The Lorentz action on the gauge-field generator, as a linear map.

```lean
lemma repLorentzGroup_comp_ofA (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    (repLorentzGroup 𝔤 Λ) ∘ₗ ofA 𝔤 μ = ∑ a, L[Λ] a μ • ofA 𝔤 a
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_derivA`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L376).

> The Lorentz law of the derivative symbols, read off the complexified law
> `repLorentz_gaugeField` along the injective `x ↦ 1 ⊗ₜ x`.

```lean
lemma repLorentzGroup_derivA (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repLorentzGroup 𝔤 Λ (derivA 𝔤 (List.ofFn l) μ φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, L[Λ] (p i) (l i)) •
          ∑ a, L[Λ] a μ • derivA 𝔤 (List.ofFn p) a φ
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_bracketFam_ofA`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L396).

> The Lorentz action passes through the bracket of a gauge-field generator against a
> family, mixing the covector index of the generator.

```lean
lemma repLorentzGroup_bracketFam_ofA (Λ : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    (F : Module.Dual ℝ 𝔤 →ₗ[ℝ] LocalGaugeFieldAlgebra 𝔤) (φ : Module.Dual ℝ 𝔤) :
    repLorentzGroup 𝔤 Λ (bracketFam (ofA 𝔤 ρ) F φ)
      = ∑ a, L[Λ] a ρ • bracketFam (ofA 𝔤 a) ((repLorentzGroup 𝔤 Λ) ∘ₗ F) φ
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_fieldStrength`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L409).

> The Lorentz law of the field strength: both covector indices mix by the columns of the
> Lorentz matrix, the adjoint index is untouched.

```lean
lemma repLorentzGroup_fieldStrength (Λ : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repLorentzGroup 𝔤 Λ (fieldStrength 𝔤 μ ν φ)
      = ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • fieldStrength 𝔤 a b φ
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_covDerivFieldStrength`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean#L439).

> The Lorentz law of the covariant derivatives of the field strength: every covariant
> slot and both covector indices of the field strength mix by the columns of the Lorentz
> matrix, the adjoint index is untouched.

```lean
lemma repLorentzGroup_covDerivFieldStrength (Λ : SL(2,ℂ)) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repLorentzGroup 𝔤 Λ (covDerivFieldStrength 𝔤 (List.ofFn l) μ ν φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, L[Λ] (p i) (l i)) •
          ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • covDerivFieldStrength 𝔤 (List.ofFn p) a b φ
```

## Depends on

- [The symmetrized derivatives of a gauge field and the classification of invariants](../part-02/gaugeboson-realization-symmetrized.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/FieldStrength.lean)
