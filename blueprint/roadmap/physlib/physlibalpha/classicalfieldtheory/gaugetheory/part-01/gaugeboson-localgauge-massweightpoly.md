---
declaration: module
origin: cited
lean: LocalGaugeFieldAlgebra.monomialₗ, LocalGaugeFieldAlgebra.monomialₗ_apply, LocalGaugeFieldAlgebra.ιComplex, LocalGaugeFieldAlgebra.ιComplex_apply, LocalGaugeFieldAlgebra.jetComponentPoly, LocalGaugeFieldAlgebra.jetComponentPoly_basisMultiset_tmul, LocalGaugeFieldAlgebra.massWeightPoly, LocalGaugeFieldAlgebra.massWeightPoly_ι
statement: formalized
proof: formalized
---

# The mass-weight polynomial on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGauge.MassWeightPoly`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean): 17 declarations, 15 with a docstring.

## i. Overview

> Replacing the scalar of a mass-weight scaling by a formal variable turns the scaling into a
> grading: the generator `∂_s A_μ^φ` is sent to `X ^ (2 + 2 |s|)` times itself, the gauge field
> carrying mass weight two and each derivative two more.
>
> The gauge-boson jet algebra is real, but the jet algebra of the Standard Model uses its
> complexification `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤`. So the grading is built in two steps:
> the universal property of the symmetric algebra gives a real algebra map landing in
> `Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)` — a commutative target, so there is no
> side condition — and the universal property of the tensor product extends it along the scalars
> to `complexMassWeightPoly`, which is what the ambient theory sees.

## ii. Key results

> - `LocalGaugeFieldAlgebra.massWeightPoly` : the mass-weight grading on the real jet algebra.
> - `LocalGaugeFieldAlgebra.massWeightPoly_iteratedJetDeriv_ofA` : `∂_s A_μ^φ` is a monomial
>   eigenvector of weight `2 + 2 |s|`.
> - `LocalGaugeFieldAlgebra.complexMassWeightPoly` : the grading on the complexification.
> - `LocalGaugeFieldAlgebra.complexMassWeightPoly_tmul_iteratedJetDeriv_ofA` : the generator lemma
>   on the complexification.
> - `LocalGaugeFieldAlgebra.complexMassWeightPoly_eval_one` : setting the variable to one recovers
>   the element.

## iv. References

> * None.

## A. The mass-weight polynomial of a component function

**`LocalGaugeFieldAlgebra.monomialₗ`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L67).

> The monomial map into polynomials over the complexified jet algebra, as a map of
> `ℝ`-modules rather than of modules over the complexified jet algebra.

```lean
noncomputable def monomialₗ (n : ℕ) :
    (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) →ₗ[ℝ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.monomialₗ_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L74).

```lean
lemma monomialₗ_apply (n : ℕ) (x : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) :
    (monomialₗ (𝔤 := 𝔤)) n x = Polynomial.monomial n x
```

**`LocalGaugeFieldAlgebra.ιComplex`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L79).

> A component function, viewed inside the complexified jet algebra: the generator
> `∂_s A_μ^φ` tensored with the scalar one.

```lean
noncomputable def ιComplex :
    (GaugeBoson.JetComponentSpace 𝔤) →ₗ[ℝ] ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤
```

**`LocalGaugeFieldAlgebra.ιComplex_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L86).

```lean
lemma ιComplex_apply (x : (GaugeBoson.JetComponentSpace 𝔤)) :
    (ιComplex (𝔤 := 𝔤)) x =
      (1 : ℂ) ⊗ₜ[ℝ] SymmetricAlgebra.ι ℝ (GaugeBoson.JetComponentSpace 𝔤) x
```

**`LocalGaugeFieldAlgebra.jetComponentPoly`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L93).

> The mass-weight polynomial of a component function: the linear map sending the symbol
> `∂_s A^φ` to `X ^ (2 + 2 |s|)` times itself, read off from the multiset basis of the real
> derivative symbols.

```lean
noncomputable def jetComponentPoly :
    (GaugeBoson.JetComponentSpace 𝔤) →ₗ[ℝ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.jetComponentPoly_basisMultiset_tmul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L104).

> On the symbol `∂_s A^φ` the component map is the monomial of degree `2 + 2 |s|`: the
> gauge field contributes two and each derivative two more.

```lean
lemma jetComponentPoly_basisMultiset_tmul (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ (GaugeBoson 𝔤)) :
    (jetComponentPoly (𝔤 := 𝔤)) (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] φ) =
      Polynomial.monomial (2 + 2 * Multiset.card s)
        (ιComplex (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] φ))
```

## B. The mass-weight polynomial on the real jet algebra

**`LocalGaugeFieldAlgebra.massWeightPoly`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L121).

> The mass-weight polynomial on the gauge-boson jet algebra: the `ℝ`-algebra map sending
> a generator of mass weight `n` to `X ^ n` times its image in the complexification. It
> needs no side condition because the target is commutative.

```lean
noncomputable def massWeightPoly :
    LocalGaugeFieldAlgebra 𝔤 →ₐ[ℝ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.massWeightPoly_ι`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L130).

> On a component function the mass-weight polynomial is the component-function map.

```lean
lemma massWeightPoly_ι (x : (GaugeBoson.JetComponentSpace 𝔤)) :
    (massWeightPoly (𝔤 := 𝔤)) (SymmetricAlgebra.ι ℝ (GaugeBoson.JetComponentSpace 𝔤) x) =
      jetComponentPoly x
```

**`LocalGaugeFieldAlgebra.massWeightPoly_iteratedJetDeriv_ofA`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L138).

> The generator `∂_s A_μ^φ` is a monomial eigenvector of mass weight `2 + 2 |s|`.

```lean
lemma massWeightPoly_iteratedJetDeriv_ofA (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (massWeightPoly (𝔤 := 𝔤)) (LocalGaugeFieldAlgebra.iteratedJetDeriv 𝔤 s
        (LocalGaugeFieldAlgebra.ofA 𝔤 μ φ)) =
      Polynomial.monomial (2 + 2 * Multiset.card s) ((1 : ℂ) ⊗ₜ[ℝ]
        LocalGaugeFieldAlgebra.iteratedJetDeriv 𝔤 s
          (LocalGaugeFieldAlgebra.ofA 𝔤 μ φ))
```

**`LocalGaugeFieldAlgebra.massWeightPoly_ofA`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L150).

> The undifferentiated gauge field has mass weight two — mass dimension one.

```lean
lemma massWeightPoly_ofA (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (massWeightPoly (𝔤 := 𝔤)) (LocalGaugeFieldAlgebra.ofA 𝔤 μ φ) =
      Polynomial.monomial 2 ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.ofA 𝔤 μ φ)
```

## C. The mass-weight polynomial on the complexification

**`LocalGaugeFieldAlgebra.complexMassWeightPoly`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L167).

> The mass-weight polynomial on the complexified gauge-boson jet algebra: the `ℂ`-algebra
> map obtained from the real one by extending the scalars, the grading the jet algebra of
> the Standard Model sees on its gauge sector.

```lean
noncomputable def complexMassWeightPoly :
    (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) →ₐ[ℂ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤)
```

**`LocalGaugeFieldAlgebra.complexMassWeightPoly_tmul`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L179).

> On a pure tensor the complexified grading is the scalar times the real grading.

```lean
lemma complexMassWeightPoly_tmul (z : ℂ) (x : LocalGaugeFieldAlgebra 𝔤) :
    (complexMassWeightPoly (𝔤 := 𝔤)) (z ⊗ₜ[ℝ] x) =
      Polynomial.C (z ⊗ₜ[ℝ] (1 : LocalGaugeFieldAlgebra 𝔤)) * massWeightPoly x
```

**`LocalGaugeFieldAlgebra.complexMassWeightPoly_tmul_iteratedJetDeriv_ofA`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L190).

> The generator `∂_s A_μ^φ` of the complexified jet algebra, with any complex coefficient,
> is a monomial eigenvector of mass weight `2 + 2 |s|`.

```lean
lemma complexMassWeightPoly_tmul_iteratedJetDeriv_ofA (z : ℂ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (complexMassWeightPoly (𝔤 := 𝔤)) (z ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.iteratedJetDeriv 𝔤 s
        (LocalGaugeFieldAlgebra.ofA 𝔤 μ φ)) =
      Polynomial.monomial (2 + 2 * Multiset.card s) (z ⊗ₜ[ℝ]
        LocalGaugeFieldAlgebra.iteratedJetDeriv 𝔤 s
          (LocalGaugeFieldAlgebra.ofA 𝔤 μ φ))
```

## D. Recovering an element from its mass-weight polynomial

**`LocalGaugeFieldAlgebra.jetComponentPoly_eval_one`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L211).

> Setting the formal variable to one collapses the component map back to the component
> function it graded. The derivative monomials span, so it is enough to check this on the
> multiset basis.

```lean
lemma jetComponentPoly_eval_one (x : (GaugeBoson.JetComponentSpace 𝔤)) :
    ((jetComponentPoly (𝔤 := 𝔤)) x).eval 1 = ιComplex x
```

**`LocalGaugeFieldAlgebra.massWeightPoly_eval_one`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L233).

> Setting the formal variable to one recovers the original element, viewed in the
> complexification.

```lean
lemma massWeightPoly_eval_one (x : LocalGaugeFieldAlgebra 𝔤) :
    ((massWeightPoly (𝔤 := 𝔤)) x).eval 1 =
      Algebra.TensorProduct.includeRight (R := ℝ) (A := ℂ)
        (B := LocalGaugeFieldAlgebra 𝔤) x
```

**`LocalGaugeFieldAlgebra.complexMassWeightPoly_eval_one`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L252).

> Setting the formal variable to one recovers the original element of the complexified
> jet algebra: the mass-weight pieces sum back to it.

```lean
lemma complexMassWeightPoly_eval_one (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) :
    ((complexMassWeightPoly (𝔤 := 𝔤)) y).eval 1 = y
```

**`LocalGaugeFieldAlgebra.complexMassWeightPoly_injective`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean#L264).

> The mass-weight polynomial on the complexification is injective: an element is
> recovered from its graded pieces.

```lean
lemma complexMassWeightPoly_injective : Function.Injective (complexMassWeightPoly (𝔤 := 𝔤))
```

## Depends on

- [The formal total derivative on the gauge-boson jet algebra](gaugeboson-localgauge-jetderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGauge/MassWeightPoly.lean)
