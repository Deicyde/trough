---
declaration: module
origin: cited
lean: StandardModel.BosonicAlgebra.monomialₗ, StandardModel.BosonicAlgebra.monomialₗ_apply, StandardModel.BosonicAlgebra.halfPoly, StandardModel.BosonicAlgebra.halfPoly_basis_tmul, StandardModel.BosonicAlgebra.ιFst, StandardModel.BosonicAlgebra.ιSnd, StandardModel.BosonicAlgebra.jetComponentPoly, StandardModel.BosonicAlgebra.jetComponentPoly_apply
statement: formalized
proof: formalized
---

# The mass-weight polynomial on the bosonic algebra

The module `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.MassWeightPoly`, [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean): 20 declarations, 18 with a docstring.

## i. Overview

> The mass-weight scaling of `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.MassDim`
> records the mass dimension of a homogeneous element in a scalar. Replacing that scalar by a
> formal variable turns the scaling into a grading: `massWeightPoly w` is the algebra map
> sending a generator `∂_s ψ_φ` of a field of mass weight `w` to `X ^ (w + 2 |s|)` times
> itself, so the coefficient of `X ^ n` in `massWeightPoly w a` is the part of `a` of mass
> weight `n`.
>
> The target `Polynomial (BosonicAlgebra M)` is commutative, so the universal property of the
> symmetric algebra applies with no side condition: the grading is the lift of a single linear
> map on the jet component space. That map is assembled from the two halves of the component
> space, and on each half from the multiset basis of the derivative symbols, which is where
> the exponent `w + 2 |s|` is read off.

## ii. Key results

> - `BosonicAlgebra.massWeightPoly` : the mass-weight polynomial grading.
> - `BosonicAlgebra.massWeightPoly_iteratedJetDeriv_ofField` : `∂_s ψ_φ` is a monomial
>   eigenvector of weight `w + 2 |s|`.
> - `BosonicAlgebra.massWeightPoly_iteratedJetDeriv_ofConjField` : the same for the conjugate
>   field.
> - `BosonicAlgebra.massWeightPoly_eval_one` : setting the variable to one recovers the
>   element.

## iv. References

> * None.

## A. The mass-weight polynomial of a component function

**`StandardModel.BosonicAlgebra.monomialₗ`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L70).

> The monomial map into polynomials over the bosonic algebra, as a map of `ℂ`-modules
> rather than of `BosonicAlgebra M`-modules.

```lean
noncomputable def monomialₗ (n : ℕ) :
    BosonicAlgebra M →ₗ[ℂ] Polynomial (BosonicAlgebra M)
```

**`StandardModel.BosonicAlgebra.monomialₗ_apply`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L75).

```lean
lemma monomialₗ_apply (n : ℕ) (x : BosonicAlgebra M) :
    monomialₗ n x = Polynomial.monomial n x
```

**`StandardModel.BosonicAlgebra.halfPoly`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L82).

> One half of the mass-weight polynomial on the jet component space, for a field of mass
> weight `w`: the linear map sending the symbol `∂_s φ` to `X ^ (w + 2 |s|)` times its
> image under `k`. The two halves of the component space differ only in the inclusion `k`
> of the symbols into the bosonic algebra, so both are instances of this map.

```lean
noncomputable def halfPoly {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] BosonicAlgebra M) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] Polynomial (BosonicAlgebra M)
```

**`StandardModel.BosonicAlgebra.halfPoly_basis_tmul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L91).

> On the symbol `∂_s φ` the half mass-weight polynomial is the monomial of degree
> `w + 2 |s|`: the field contributes `w` and each derivative two.

```lean
lemma halfPoly_basis_tmul {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] BosonicAlgebra M)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (x : W) :
    halfPoly w k (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] x) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (k (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] x))
```

**`StandardModel.BosonicAlgebra.ιFst`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L101).

> The inclusion of the unconjugated symbols into the bosonic algebra.

```lean
noncomputable def ιFst : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ M.V →ₗ[ℂ] BosonicAlgebra M
```

**`StandardModel.BosonicAlgebra.ιSnd`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L105).

> The inclusion of the conjugate symbols into the bosonic algebra.

```lean
noncomputable def ιSnd :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule M.V) →ₗ[ℂ] BosonicAlgebra M
```

**`StandardModel.BosonicAlgebra.jetComponentPoly`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L111).

> The mass-weight polynomial of a component function of a field of mass weight `w`: the
> sum of the two half maps, one for the field and one for its conjugate.

```lean
noncomputable def jetComponentPoly (w : ℕ) :
    JetComponentSpace M →ₗ[ℂ] Polynomial (BosonicAlgebra M)
```

**`StandardModel.BosonicAlgebra.jetComponentPoly_apply`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L116).

```lean
lemma jetComponentPoly_apply (w : ℕ) (x : JetComponentSpace M) :
    jetComponentPoly w x = halfPoly w ιFst x.1 + halfPoly w ιSnd x.2
```

**`StandardModel.BosonicAlgebra.jetComponentPoly_inl`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L121).

> On an unconjugated derivative monomial the component map is a monomial eigenvector.

```lean
lemma jetComponentPoly_inl (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ M.V) :
    jetComponentPoly w ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace M) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (SymmetricAlgebra.ι ℂ (JetComponentSpace M)
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace M))
```

**`StandardModel.BosonicAlgebra.jetComponentPoly_inr`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L131).

> On a conjugate derivative monomial the component map is a monomial eigenvector.

```lean
lemma jetComponentPoly_inr (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule M.V)) :
    jetComponentPoly w ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace M) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (SymmetricAlgebra.ι ℂ (JetComponentSpace M)
          ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace M))
```

## B. The mass-weight polynomial on the bosonic algebra

**`StandardModel.BosonicAlgebra.massWeightPoly`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L150).

> The mass-weight polynomial on the bosonic algebra of a field of mass weight `w`: the
> `ℂ`-algebra map sending a generator of mass weight `n` to `X ^ n` times itself. It is
> `BosonicAlgebra.massWeightScale` with the scalar replaced by the formal variable `X`, and
> needs no side condition because `Polynomial (BosonicAlgebra M)` is commutative.

```lean
noncomputable def massWeightPoly (w : ℕ) :
    BosonicAlgebra M →ₐ[ℂ] Polynomial (BosonicAlgebra M)
```

**`StandardModel.BosonicAlgebra.massWeightPoly_ι`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L156).

> On a component function the mass-weight polynomial is the component-function map.

```lean
lemma massWeightPoly_ι (w : ℕ) (x : JetComponentSpace M) :
    massWeightPoly w (SymmetricAlgebra.ι ℂ (JetComponentSpace M) x) =
      jetComponentPoly w x
```

## C. The mass weight of the field and its derivatives

**`StandardModel.BosonicAlgebra.massWeightPoly_iteratedJetDeriv_ofField`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L169).

> The generator `∂_s ψ_φ` is a monomial eigenvector of mass weight `w + 2 |s|`: the field
> carries its own mass weight and each derivative adds two.

```lean
lemma massWeightPoly_iteratedJetDeriv_ofField (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ M.V) :
    massWeightPoly w (iteratedJetDeriv s (ofField φ)) =
      Polynomial.monomial (w + 2 * Multiset.card s) (iteratedJetDeriv s (ofField φ))
```

**`StandardModel.BosonicAlgebra.massWeightPoly_iteratedJetDeriv_ofConjField`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L177).

> The conjugate generator `∂_s ψ̄_φ` is a monomial eigenvector of the same mass weight
> `w + 2 |s|` as the generator it conjugates.

```lean
lemma massWeightPoly_iteratedJetDeriv_ofConjField (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule M.V)) :
    massWeightPoly w (iteratedJetDeriv s (ofConjField φ)) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (iteratedJetDeriv s (ofConjField φ))
```

**`StandardModel.BosonicAlgebra.massWeightPoly_ofField`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L185).

> The undifferentiated field has mass weight `w`.

```lean
lemma massWeightPoly_ofField (w : ℕ) (φ : Module.Dual ℂ M.V) :
    massWeightPoly w (ofField φ) = Polynomial.monomial w (ofField φ)
```

**`StandardModel.BosonicAlgebra.massWeightPoly_ofConjField`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L192).

> The undifferentiated conjugate field has mass weight `w`.

```lean
lemma massWeightPoly_ofConjField (w : ℕ) (φ : Module.Dual ℂ (ConjModule M.V)) :
    massWeightPoly w (ofConjField φ) = Polynomial.monomial w (ofConjField φ)
```

## D. Recovering an element from its mass-weight polynomial

**`StandardModel.BosonicAlgebra.halfPoly_eval_one`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L207).

> Setting the formal variable to one collapses a half mass-weight polynomial back to the
> symbol it graded. The derivative monomials span, so it is enough to check this on the
> multiset basis.

```lean
lemma halfPoly_eval_one {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] BosonicAlgebra M)
    (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W) : (halfPoly w k y).eval 1 = k y
```

**`StandardModel.BosonicAlgebra.jetComponentPoly_eval_one`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L227).

> Setting the formal variable to one recovers the component function.

```lean
lemma jetComponentPoly_eval_one (w : ℕ) (x : JetComponentSpace M) :
    (jetComponentPoly w x).eval 1 = SymmetricAlgebra.ι ℂ (JetComponentSpace M) x
```

**`StandardModel.BosonicAlgebra.massWeightPoly_eval_one`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L236).

> Setting the formal variable to one recovers the original element: the mass-weight
> pieces of an element sum back to it.

```lean
lemma massWeightPoly_eval_one (w : ℕ) (a : BosonicAlgebra M) :
    (massWeightPoly w a).eval 1 = a
```

**`StandardModel.BosonicAlgebra.massWeightPoly_injective`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean#L252).

> The mass-weight polynomial is injective: an element is recovered from its graded
> pieces. It is not surjective, since a monomial of the wrong degree is not the grading of
> anything.

```lean
lemma massWeightPoly_injective (w : ℕ) :
    Function.Injective (massWeightPoly (M := M) w)
```

## Depends on

- [The formal total derivative on the bosonic algebra](matter-bosonic-jetderiv.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassWeightPoly.lean)
