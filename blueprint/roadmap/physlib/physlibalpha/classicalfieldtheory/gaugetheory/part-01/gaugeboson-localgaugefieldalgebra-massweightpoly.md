---
declaration: module
origin: cited
lean: LocalGaugeFieldAlgebra.monomialₗ, LocalGaugeFieldAlgebra.monomialₗ_apply, LocalGaugeFieldAlgebra.ιComplex, LocalGaugeFieldAlgebra.ιComplex_apply, LocalGaugeFieldAlgebra.jetComponentPoly, LocalGaugeFieldAlgebra.jetComponentPoly_basisMultiset_tmul, LocalGaugeFieldAlgebra.massWeightPoly, LocalGaugeFieldAlgebra.massWeightPoly_ι
statement: formalized
proof: formalized
---

# The mass-weight polynomial on the gauge-boson jet algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.LocalGaugeFieldAlgebra.MassWeightPoly`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean): 16 declarations, 14 with a docstring.

> The mass-weight grading of the gauge-boson jet algebra, as an algebra map into polynomials.

## i. Overview

> Replacing the scalar of a mass-weight scaling by a formal variable turns the scaling into a
> grading. The generator `∂_s A_μ^φ` is sent to `X ^ (2 + 2 |s|)` times itself, the gauge field
> carrying mass weight two and each derivative two more.
>
> The gauge-boson jet algebra is real, but the jet algebra of the Standard Model uses its
> complexification `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G`. So the grading is built in two steps:
> the universal property of the symmetric algebra gives a real algebra map landing in
> `Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G)`, a commutative target so that there is no
> side condition, and the universal property of the tensor product extends it along the scalars
> to `complexMassWeightPoly`, which is what the ambient theory sees.
>
> Setting the formal variable to one recovers the element, and setting it to a real number `c`
> on a component function gives the mass-weight scaling by `c`.

## ii. Key results

> - `LocalGaugeFieldAlgebra.massWeightPoly` : the mass-weight grading on the real jet algebra.
> - `LocalGaugeFieldAlgebra.massWeightPoly_iteratedJetDeriv_ofA` : `∂_s A_μ^φ` is a monomial
>   eigenvector of weight `2 + 2 |s|`.
> - `LocalGaugeFieldAlgebra.complexMassWeightPoly` : the grading on the complexification.
> - `LocalGaugeFieldAlgebra.complexMassWeightPoly_tmul_iteratedJetDeriv_ofA` : the generator lemma
>   on the complexification.
> - `LocalGaugeFieldAlgebra.complexMassWeightPoly_eval_one` : setting the variable to one recovers
>   the element.
> - `LocalGaugeFieldAlgebra.jetComponentPoly_eval_algebraMap` : setting the variable to a real
>   number `c` on a component function gives its mass-weight scaling by `c`.

## iv. References

> * None.

## A. The mass-weight polynomial of a component function

**`LocalGaugeFieldAlgebra.monomialₗ`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L74).

> The monomial map into polynomials over the complexified jet algebra, as a map of
> `ℝ`-modules rather than of modules over the complexified jet algebra.

```lean
noncomputable def monomialₗ (n : ℕ) :
    (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) →ₗ[ℝ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.monomialₗ_apply`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L80).

```lean
lemma monomialₗ_apply (n : ℕ) (x : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) :
    (monomialₗ (G := G)) n x = Polynomial.monomial n x
```

**`LocalGaugeFieldAlgebra.ιComplex`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L85).

> A component function, viewed inside the complexified jet algebra, the generator
> `∂_s A_μ^φ` tensored with the scalar one.

```lean
noncomputable def ιComplex :
    (GaugeBoson.FieldDerivSpace G) →ₗ[ℝ] ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G
```

**`LocalGaugeFieldAlgebra.ιComplex_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L91).

```lean
lemma ιComplex_apply (x : (GaugeBoson.FieldDerivSpace G)) :
    (ιComplex (G := G)) x =
      (1 : ℂ) ⊗ₜ[ℝ] SymmetricAlgebra.ι ℝ (GaugeBoson.FieldDerivSpace G) x
```

**`LocalGaugeFieldAlgebra.jetComponentPoly`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L98).

> The mass-weight polynomial of a component function, the linear map sending the symbol
> `∂_s A^φ` to `X ^ (2 + 2 |s|)` times itself, read off from the multiset basis of the real
> derivative symbols.

```lean
noncomputable def jetComponentPoly :
    (GaugeBoson.FieldDerivSpace G) →ₗ[ℝ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.jetComponentPoly_basisMultiset_tmul`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L108).

> On the symbol `∂_s A^φ` the component map is the monomial of degree `2 + 2 |s|`. The
> gauge field contributes two and each derivative two more.

```lean
lemma jetComponentPoly_basisMultiset_tmul (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ (GaugeBoson G)) :
    (jetComponentPoly (G := G)) (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] φ) =
      Polynomial.monomial (2 + 2 * Multiset.card s)
        (ιComplex (SpaceTimeDerivAlgebraℝ.basisMultiset s ⊗ₜ[ℝ] φ))
```

## B. The mass-weight polynomial on the real jet algebra

**`LocalGaugeFieldAlgebra.massWeightPoly`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L125).

> The mass-weight polynomial on the gauge-boson jet algebra, the `ℝ`-algebra map sending
> a generator of mass weight `n` to `X ^ n` times its image in the complexification. It
> needs no side condition because the target is commutative.

```lean
noncomputable def massWeightPoly :
    LocalGaugeFieldAlgebra G →ₐ[ℝ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.massWeightPoly_ι`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L133).

> On a component function the mass-weight polynomial is the component-function map.

```lean
lemma massWeightPoly_ι (x : (GaugeBoson.FieldDerivSpace G)) :
    (massWeightPoly (G := G)) (SymmetricAlgebra.ι ℝ (GaugeBoson.FieldDerivSpace G) x) =
      jetComponentPoly x
```

**`LocalGaugeFieldAlgebra.massWeightPoly_iteratedJetDeriv_ofA`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L140).

> The generator `∂_s A_μ^φ` is a monomial eigenvector of mass weight `2 + 2 |s|`.

```lean
lemma massWeightPoly_iteratedJetDeriv_ofA (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (massWeightPoly (G := G)) (LocalGaugeFieldAlgebra.iteratedJetDeriv G s
        (LocalGaugeFieldAlgebra.ofA G μ φ)) =
      Polynomial.monomial (2 + 2 * Multiset.card s) ((1 : ℂ) ⊗ₜ[ℝ]
        LocalGaugeFieldAlgebra.iteratedJetDeriv G s
          (LocalGaugeFieldAlgebra.ofA G μ φ))
```

## C. The mass-weight polynomial on the complexification

**`LocalGaugeFieldAlgebra.complexMassWeightPoly`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L159).

> The mass-weight polynomial on the complexified gauge-boson jet algebra, the `ℂ`-algebra
> map obtained from the real one by extending the scalars, the grading the jet algebra of
> the Standard Model sees on its gauge sector.

```lean
noncomputable def complexMassWeightPoly :
    (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) →ₐ[ℂ]
      Polynomial (ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G)
```

**`LocalGaugeFieldAlgebra.complexMassWeightPoly_tmul`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L170).

> On a pure tensor the complexified grading is the scalar times the real grading.

```lean
lemma complexMassWeightPoly_tmul (z : ℂ) (x : LocalGaugeFieldAlgebra G) :
    (complexMassWeightPoly (G := G)) (z ⊗ₜ[ℝ] x) =
      Polynomial.C (z ⊗ₜ[ℝ] (1 : LocalGaugeFieldAlgebra G)) * massWeightPoly x
```

**`LocalGaugeFieldAlgebra.complexMassWeightPoly_tmul_iteratedJetDeriv_ofA`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L179).

> The generator `∂_s A_μ^φ` of the complexified jet algebra, with any complex coefficient,
> is a monomial eigenvector of mass weight `2 + 2 |s|`.

```lean
lemma complexMassWeightPoly_tmul_iteratedJetDeriv_ofA (z : ℂ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (complexMassWeightPoly (G := G)) (z ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.iteratedJetDeriv G s
        (LocalGaugeFieldAlgebra.ofA G μ φ)) =
      Polynomial.monomial (2 + 2 * Multiset.card s) (z ⊗ₜ[ℝ]
        LocalGaugeFieldAlgebra.iteratedJetDeriv G s
          (LocalGaugeFieldAlgebra.ofA G μ φ))
```

## D. Evaluating the mass-weight polynomial

**`LocalGaugeFieldAlgebra.jetComponentPoly_eval_one`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L199).

> Setting the formal variable to one collapses the component map back to the component
> function it graded. The derivative monomials span, so it is enough to check this on the
> multiset basis.

```lean
lemma jetComponentPoly_eval_one (x : (GaugeBoson.FieldDerivSpace G)) :
    ((jetComponentPoly (G := G)) x).eval 1 = ιComplex x
```

**`LocalGaugeFieldAlgebra.jetComponentPoly_eval_algebraMap`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L220).

> Setting the formal variable to a real number `c` turns the component map into the
> mass-weight scaling by `c`. It is enough to check this on the multiset basis, where both
> sides are `c ^ (2 + 2 |s|)` times the symbol.

```lean
lemma jetComponentPoly_eval_algebraMap (c : ℝ) (x : GaugeBoson.FieldDerivSpace G) :
    ((jetComponentPoly (G := G)) x).eval (algebraMap ℝ _ c) =
      ιComplex (GaugeBoson.FieldDerivSpace.massWeightScale G c x)
```

**`LocalGaugeFieldAlgebra.massWeightPoly_eval_one`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L240).

> Setting the formal variable to one recovers the original element, viewed in the
> complexification.

```lean
lemma massWeightPoly_eval_one (x : LocalGaugeFieldAlgebra G) :
    ((massWeightPoly (G := G)) x).eval 1 =
      Algebra.TensorProduct.includeRight (R := ℝ) (A := ℂ)
        (B := LocalGaugeFieldAlgebra G) x
```

**`LocalGaugeFieldAlgebra.complexMassWeightPoly_eval_one`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean#L258).

> Setting the formal variable to one recovers the original element of the complexified
> jet algebra. The mass-weight pieces sum back to it.

```lean
lemma complexMassWeightPoly_eval_one (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) :
    ((complexMassWeightPoly (G := G)) y).eval 1 = y
```

## Depends on

- [Mass dimension on the gauge-boson jet algebra](gaugeboson-localgaugefieldalgebra-massdim.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/LocalGaugeFieldAlgebra/MassWeightPoly.lean)
