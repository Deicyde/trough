---
declaration: module
origin: cited
lean: LocalGaugeFieldAlgebra.derivA, LocalGaugeFieldAlgebra.derivA_apply, LocalGaugeFieldAlgebra.derivA_zero, LocalGaugeFieldAlgebra.gaugeField_eq_one_tmul_derivA, LocalGaugeFieldAlgebra.algHom_ext, LocalGaugeFieldAlgebra.fieldStrength, LocalGaugeFieldAlgebra.fieldStrength_apply, LocalGaugeFieldAlgebra.fieldStrength_swap
statement: formalized
proof: formalized
---

# The field strength in the local gauge field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeFieldAlgebra.FieldStrength`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean): 24 declarations, 22 with a docstring.

> The field strength `F_μν` of the gauge bosons and its covariant derivatives, with their gauge
> and Lorentz laws.

## i. Overview

> The field strength and its covariant derivatives are built for an arbitrary family of
> gauge-field symbols in an arbitrary algebra in the directory
> `PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily`, as
> families of derivative symbols. Here they are
> specialized to the real algebra `LocalGaugeFieldAlgebra G` itself, whose symbols are its
> own generators `∂_s A_μ^φ` (`derivA`).
>
> Two facts make the specialization work. The symbols that the families carry are honest
> iterated derivatives of their base values
> (`iteratedCovDerivAdjoint_fieldStrength_derivA`), which turns the symbol-level recursion
> of `iteratedCovDerivAdjoint` into the recursion `covDerivFieldStrength_cons` on elements
> of the algebra. And the gauge law is not reproved: the complexified tower is the image of
> the real one under `x ↦ 1 ⊗ₜ x`, which is injective and intertwines the two gauge actions,
> so the law of the complexified symbols descends. The Lorentz law is proved directly from
> the recursion.
>
> Everything here is over `ℝ`. The complexification `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G`
> appears only as that bridge, and it is never identified with the real algebra.

## ii. Key results

> - `LocalGaugeFieldAlgebra.fieldStrength`, `LocalGaugeFieldAlgebra.covDerivFieldStrength` :
>   the field strength `F_μν^φ` and its ordered covariant derivatives `∇_l F_μν^φ`.
> - `LocalGaugeFieldAlgebra.repJet_covDerivFieldStrength_eval` : the gauge law, through the
>   value of the jet alone.
> - `LocalGaugeFieldAlgebra.repLorentzGroup_covDerivFieldStrength` : the Lorentz law.

## iv. References

> * None.

## A. The derivative symbols of the real algebra

**`LocalGaugeFieldAlgebra.derivA`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L82).

> The derivative symbols `∂_s A_μ^φ` of the local gauge field algebra, as a family over
> the derivative multiset `s` and the spacetime index `μ`, the iterated total derivative of
> the gauge-field generator. The field strength and its covariant derivatives are built
> out of this family.

```lean
noncomputable def derivA (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] LocalGaugeFieldAlgebra G
```

**`LocalGaugeFieldAlgebra.derivA_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L86).

```lean
lemma derivA_apply (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) : derivA G s μ φ = iteratedJetDeriv G s (ofA G μ φ)
```

**`LocalGaugeFieldAlgebra.derivA_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L90).

```lean
lemma derivA_zero (μ : Fin 1 ⊕ Fin 3) : derivA G 0 μ = ofA G μ
```

**`LocalGaugeFieldAlgebra.gaugeField_eq_one_tmul_derivA`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L93).

> The complexified symbols `gaugeField` are the images of the real symbols.

```lean
lemma gaugeField_eq_one_tmul_derivA (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) : gaugeField G s μ φ = (1 : ℂ) ⊗ₜ[ℝ] derivA G s μ φ
```

**`LocalGaugeFieldAlgebra.algHom_ext`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L100).

> Two algebra maps out of the local gauge field algebra agreeing on the derivative
> symbols `∂_s A_μ^φ` are equal.

```lean
lemma algHom_ext {B : Type} [Semiring B] [Algebra ℝ B] {f g : LocalGaugeFieldAlgebra G →ₐ[ℝ] B}
    (h : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra),
      f (derivA G s μ φ) = g (derivA G s μ φ)) : f = g
```

## B. The field strength and its covariant derivatives

**`LocalGaugeFieldAlgebra.fieldStrength`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L118).

> The field strength `F_μν = ∂_μ A_ν − ∂_ν A_μ + ⁅A_μ, A_ν⁆` of the local gauge field
> algebra, the underived field strength of the family of derivative symbols, in the
> conventions of `GaugeBoson.fieldStrength`, where the bracket of the gauge
> algebra carries the physicists' factor of `i`.

```lean
noncomputable def fieldStrength (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] LocalGaugeFieldAlgebra G
```

**`LocalGaugeFieldAlgebra.fieldStrength_apply`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L123).

> The field strength written in the generators of the algebra.

```lean
lemma fieldStrength_apply (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    fieldStrength G μ ν φ = jetDeriv G μ (ofA G ν φ) - jetDeriv G ν (ofA G μ φ)
      + bracketFam (ofA G μ) (ofA G ν) φ
```

**`LocalGaugeFieldAlgebra.fieldStrength_swap`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L132).

> The field strength is antisymmetric in its two covector indices.

```lean
lemma fieldStrength_swap (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength G ν μ = - fieldStrength G μ ν
```

**`LocalGaugeFieldAlgebra.covDerivFieldStrength`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L141).

> The iterated covariant derivative `∇_{l₁} ⋯ ∇_{lₙ} F_μν` of the field strength along an
> ordered list of directions, with `∇_ρ F = ∂_ρ F + ⁅A_ρ, F⁆` the covariant derivative in
> the adjoint. Covariant derivatives do not commute, so the iteration is indexed by a list
> and not by a multiset; the empty list gives the field strength itself.

```lean
noncomputable def covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] LocalGaugeFieldAlgebra G
```

**`LocalGaugeFieldAlgebra.covDerivFieldStrength_nil`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L147).

> With zero covariant derivatives this is the field strength itself.

```lean
lemma covDerivFieldStrength_nil (μ ν : Fin 1 ⊕ Fin 3) :
    covDerivFieldStrength G [] μ ν = fieldStrength G μ ν
```

## C. The derivative symbols of the covariant tower are iterated derivatives

> The adjoint families carry the derivative symbols `∂_s F` of a
> covariant expression as data. Here the Leibniz convolutions defining the derived brackets
> really are the Leibniz rule of the total derivative, so those symbols are the iterated
> total derivatives `∂_s` of the value at `0`.

**`LocalGaugeFieldAlgebra.iteratedJetDeriv_bracketFam`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L163).

> The Leibniz rule of the iterated total derivative on a bracket of families, as the
> antidiagonal convolution of the iterated derivatives of the two factors.

```lean
lemma iteratedJetDeriv_bracketFam (s : Multiset (Fin 1 ⊕ Fin 3))
    (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] LocalGaugeFieldAlgebra G)
      (φ : Module.Dual ℝ G.lieSubalgebra) :
    iteratedJetDeriv G s (bracketFam f g φ) = (s.antidiagonal.map fun p =>
      bracketFam (iteratedJetDeriv G p.1 ∘ₗ f) (iteratedJetDeriv G p.2 ∘ₗ g) φ).sum
```

**`LocalGaugeFieldAlgebra.bracketFamConv_derivA`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L194).

> If a family consists of the iterated derivatives of its base value, so does its derived
> bracket against the gauge field. The Leibniz convolution is the iterated derivative of the
> bracket of the base values.

```lean
lemma bracketFamConv_derivA (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ]
    LocalGaugeFieldAlgebra G)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra),
      F s φ = iteratedJetDeriv G s (F 0 φ))
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    bracketFamConv (derivA G) ρ F s φ
      = iteratedJetDeriv G s (bracketFam (ofA G ρ) (F 0) φ)
```

**`LocalGaugeFieldAlgebra.covDerivAdjoint_derivA`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L210).

> The covariant derivative of a family of iterated derivatives is again a family of
> iterated derivatives.

```lean
lemma covDerivAdjoint_derivA (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ]
    LocalGaugeFieldAlgebra G)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra),
      F s φ = iteratedJetDeriv G s (F 0 φ))
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    covDerivAdjoint (derivA G) F ρ s φ
      = iteratedJetDeriv G s (covDerivAdjoint (derivA G) F ρ 0 φ)
```

**`LocalGaugeFieldAlgebra.fieldStrength_derivA`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L226).

> The derivative symbols of the field strength are the iterated derivatives of the field
> strength.

```lean
lemma fieldStrength_derivA (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    GaugeBoson.fieldStrength (derivA G) μ ν s φ
      = iteratedJetDeriv G s (fieldStrength G μ ν φ)
```

**`LocalGaugeFieldAlgebra.iteratedCovDerivAdjoint_fieldStrength_derivA`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L244).

> The derivative symbols of the covariant derivatives of the field strength are the
> iterated derivatives of their base values.

```lean
lemma iteratedCovDerivAdjoint_fieldStrength_derivA (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    iteratedCovDerivAdjoint (derivA G) l (GaugeBoson.fieldStrength (derivA G) μ ν)
        s φ
      = iteratedJetDeriv G s (covDerivFieldStrength G l μ ν φ)
```

**`LocalGaugeFieldAlgebra.covDerivFieldStrength_cons`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L255).

> The covariant derivative `∇_ρ F = ∂_ρ F + ⁅A_ρ, F⁆` peeled off the front of the list,
> giving the recursion on elements of the algebra.

```lean
lemma covDerivFieldStrength_cons (ρ : Fin 1 ⊕ Fin 3) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    covDerivFieldStrength G (ρ :: l) μ ν φ
      = jetDeriv G ρ (covDerivFieldStrength G l μ ν φ)
        + bracketFam (ofA G ρ) (covDerivFieldStrength G l μ ν) φ
```

## D. The gauge law, by descent from the complexification

> The gauge law is proved in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.AdjointFamily.GaugeLaw` for any
> family transforming as a gauge field in a complex algebra, such as the symbols of the
> complexification (`transformsAsGaugeField_gaugeField`). Injectivity of `x ↦ 1 ⊗ₜ x` reads the
> real law off the complex one, and no reality argument beyond that is involved.

**`LocalGaugeFieldAlgebra.one_tmul_iteratedCovDerivAdjoint_fieldStrength`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L282).

> The complexified covariant tower is the image of the real
> one.

```lean
lemma one_tmul_iteratedCovDerivAdjoint_fieldStrength (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (1 : ℂ) ⊗ₜ[ℝ] iteratedCovDerivAdjoint (derivA G) l
        (GaugeBoson.fieldStrength (derivA G) μ ν) s φ
      = iteratedCovDerivAdjoint (gaugeField G) l
        (GaugeBoson.fieldStrength (gaugeField G) μ ν) s φ
```

**`LocalGaugeFieldAlgebra.repJet_iteratedCovDerivAdjoint_fieldStrength`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L307).

> The gauge law of the covariant derivatives of the field strength at every derivative
> order. A jet acts by the Leibniz convolution of the dual adjoint Taylor coefficients of
> `U⁻¹` against lower derivative symbols, with no Maurer–Cartan shift.

```lean
lemma repJet_iteratedCovDerivAdjoint_fieldStrength (U : G.gaugeJetGroup) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repJet G U (iteratedCovDerivAdjoint (derivA G) l
        (GaugeBoson.fieldStrength (derivA G) μ ν) s φ)
      = (s.antidiagonal.map fun p => iteratedCovDerivAdjoint (derivA G) l
          (GaugeBoson.fieldStrength (derivA G) μ ν) p.2
          (G.adjointDualCoeff U⁻¹ p.1 φ)).sum
```

**`LocalGaugeFieldAlgebra.repJet_covDerivFieldStrength`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L327).

> The gauge law of the covariant derivatives of the field strength. A jet acts through
> the zeroth dual adjoint Taylor coefficient of `U⁻¹` on the adjoint index alone.

```lean
lemma repJet_covDerivFieldStrength (U : G.gaugeJetGroup) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repJet G U (covDerivFieldStrength G l μ ν φ)
      = covDerivFieldStrength G l μ ν (G.adjointDualCoeff U⁻¹ 0 φ)
```

**`LocalGaugeFieldAlgebra.repJet_covDerivFieldStrength_eval`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L339).

> On the covariant derivatives of the field strength the local gauge action factors
> through evaluation. A jet `U` acts through the dual base-point adjoint action of the
> value `G.evalGaugeJet U⁻¹` of its inverse, and the derivatives of the jet are not seen. The
> covariant expressions are gauge covariant, not gauge invariant.

```lean
lemma repJet_covDerivFieldStrength_eval (U : G.gaugeJetGroup) (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repJet G U (covDerivFieldStrength G l μ ν φ)
      = covDerivFieldStrength G l μ ν ((G.adjointRep
        (G.evalGaugeJet U⁻¹)).dualMap φ)
```

## E. The Lorentz law

**`LocalGaugeFieldAlgebra.repLorentzGroup_comp_ofA`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L357).

> The Lorentz action on the gauge-field generator, as a linear map.

```lean
lemma repLorentzGroup_comp_ofA (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    (repLorentzGroup G Λ) ∘ₗ ofA G μ = ∑ a, L[Λ] a μ • ofA G a
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_bracketFam_ofA`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L365).

> The Lorentz action passes through the bracket of a gauge-field generator against a
> family, mixing the covector index of the generator.

```lean
lemma repLorentzGroup_bracketFam_ofA (Λ : SL(2,ℂ)) (ρ : Fin 1 ⊕ Fin 3)
    (F : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] LocalGaugeFieldAlgebra G)
      (φ : Module.Dual ℝ G.lieSubalgebra) :
    repLorentzGroup G Λ (bracketFam (ofA G ρ) F φ)
      = ∑ a, L[Λ] a ρ • bracketFam (ofA G a) ((repLorentzGroup G Λ) ∘ₗ F) φ
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_fieldStrength`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L379).

> The Lorentz law of the field strength. Both covector indices mix by the columns of the
> Lorentz matrix, and the adjoint index is untouched.

```lean
lemma repLorentzGroup_fieldStrength (Λ : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repLorentzGroup G Λ (fieldStrength G μ ν φ)
      = ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • fieldStrength G a b φ
```

**`LocalGaugeFieldAlgebra.repLorentzGroup_covDerivFieldStrength`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean#L409).

> The Lorentz law of the covariant derivatives of the field strength. Every covariant
> slot and both covector indices of the field strength mix by the columns of the Lorentz
> matrix, and the adjoint index is untouched.

```lean
lemma repLorentzGroup_covDerivFieldStrength (Λ : SL(2,ℂ)) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    repLorentzGroup G Λ (covDerivFieldStrength G (List.ofFn l) μ ν φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ i, L[Λ] (p i) (l i)) •
          ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • covDerivFieldStrength G (List.ofFn p) a b φ
```

## Depends on

- [The gauge-field symbols of the jet algebra and their laws](gaugeboson-localgaugefieldalgebra-gaugefield.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/FieldStrength.lean)
