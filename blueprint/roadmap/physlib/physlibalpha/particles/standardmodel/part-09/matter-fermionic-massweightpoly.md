---
declaration: module
origin: cited
lean: StandardModel.FermionicAlgebra.monomialₗ, StandardModel.FermionicAlgebra.monomialₗ_apply, StandardModel.FermionicAlgebra.halfPoly, StandardModel.FermionicAlgebra.halfPoly_basis_tmul, StandardModel.FermionicAlgebra.ιFst, StandardModel.FermionicAlgebra.ιSnd, StandardModel.FermionicAlgebra.jetComponentPoly, StandardModel.FermionicAlgebra.jetComponentPoly_apply
statement: formalized
proof: formalized
---

# The mass-weight polynomial on the fermionic algebra

The module `PhyslibAlpha.Particles.StandardModel.Matter.Fermionic.MassWeightPoly`, [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean): 24 declarations, 22 with a docstring; 1 private, not shown.

## i. Overview

> The mass-weight scaling of
> `PhyslibAlpha.Particles.StandardModel.Matter.Fermionic.MassDim` records the mass
> dimension of a homogeneous element in a scalar. Replacing that scalar by a formal variable
> turns the scaling into a grading: `massWeightPoly w` is the algebra map sending a generator
> `∂_s ψ_φ` of a field of mass weight `w` to `X ^ (w + 2 |s|)` times itself, so the
> coefficient of `X ^ n` in `massWeightPoly w a` is the part of `a` of mass weight `n`.
>
> Unlike the bosonic case the target `Polynomial (FermionicAlgebra M)` is not commutative, so
> the universal property of the exterior algebra comes with a side condition: the linear map
> on the jet component space must square to zero. That is proved by the standard bilinear-form
> argument — the symmetrised square vanishes, and two is invertible in `ℂ` — with the
> symmetrised square checked on the derivative monomials, which span the component space.

## ii. Key results

> - `FermionicAlgebra.massWeightPoly` : the mass-weight polynomial grading.
> - `FermionicAlgebra.massWeightPoly_iteratedJetDeriv_ofField` : `∂_s ψ_φ` is a monomial
>   eigenvector of weight `w + 2 |s|`.
> - `FermionicAlgebra.massWeightPoly_iteratedJetDeriv_ofConjField` : the same for the
>   conjugate field.
> - `FermionicAlgebra.massWeightPoly_eval_one` : setting the variable to one recovers the
>   element.

## iv. References

> * None.

## A. The mass-weight polynomial of a component function

**`StandardModel.FermionicAlgebra.monomialₗ`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L71).

> The monomial map into polynomials over the fermionic algebra, as a map of `ℂ`-modules
> rather than of `FermionicAlgebra M`-modules.

```lean
noncomputable def monomialₗ (n : ℕ) :
    FermionicAlgebra M →ₗ[ℂ] Polynomial (FermionicAlgebra M)
```

**`StandardModel.FermionicAlgebra.monomialₗ_apply`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L76).

```lean
lemma monomialₗ_apply (n : ℕ) (x : FermionicAlgebra M) :
    monomialₗ n x = Polynomial.monomial n x
```

**`StandardModel.FermionicAlgebra.halfPoly`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L83).

> One half of the mass-weight polynomial on the jet component space, for a field of mass
> weight `w`: the linear map sending the symbol `∂_s ψ` to `X ^ (w + 2 |s|)` times its image
> under `k`. The two halves of the component space differ only in the inclusion `k` of the
> symbols into the fermionic algebra, so both are instances of this map.

```lean
noncomputable def halfPoly {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] FermionicAlgebra M) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] Polynomial (FermionicAlgebra M)
```

**`StandardModel.FermionicAlgebra.halfPoly_basis_tmul`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L92).

> On the symbol `∂_s ψ` the half mass-weight polynomial is the monomial of degree
> `w + 2 |s|`: the field contributes `w` and each derivative two.

```lean
lemma halfPoly_basis_tmul {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] FermionicAlgebra M)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (x : W) :
    halfPoly w k (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] x) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (k (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] x))
```

**`StandardModel.FermionicAlgebra.ιFst`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L102).

> The inclusion of the unconjugated symbols into the fermionic algebra.

```lean
noncomputable def ιFst : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ M.V →ₗ[ℂ] FermionicAlgebra M
```

**`StandardModel.FermionicAlgebra.ιSnd`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L106).

> The inclusion of the conjugate symbols into the fermionic algebra.

```lean
noncomputable def ιSnd :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule M.V) →ₗ[ℂ] FermionicAlgebra M
```

**`StandardModel.FermionicAlgebra.jetComponentPoly`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L112).

> The mass-weight polynomial of a component function of a field of mass weight `w`: the
> sum of the two half maps, one for the field and one for its conjugate.

```lean
noncomputable def jetComponentPoly (w : ℕ) :
    JetComponentSpace M →ₗ[ℂ] Polynomial (FermionicAlgebra M)
```

**`StandardModel.FermionicAlgebra.jetComponentPoly_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L117).

```lean
lemma jetComponentPoly_apply (w : ℕ) (x : JetComponentSpace M) :
    jetComponentPoly w x = halfPoly w ιFst x.1 + halfPoly w ιSnd x.2
```

**`StandardModel.FermionicAlgebra.jetComponentPoly_inl`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L122).

> On an unconjugated derivative monomial the component map is a monomial eigenvector.

```lean
lemma jetComponentPoly_inl (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ M.V) :
    jetComponentPoly w ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace M) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (ExteriorAlgebra.ι ℂ
          ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) : JetComponentSpace M))
```

**`StandardModel.FermionicAlgebra.jetComponentPoly_inr`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L132).

> On a conjugate derivative monomial the component map is a monomial eigenvector.

```lean
lemma jetComponentPoly_inr (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule M.V)) :
    jetComponentPoly w ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace M) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (ExteriorAlgebra.ι ℂ
          ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) : JetComponentSpace M))
```

## B. The square-zero condition

**`StandardModel.FermionicAlgebra.generators`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L170).

> The set of derivative monomials in the jet component space: the unconjugated symbols
> `∂_s ψ_φ` together with the conjugate symbols `∂_s ψ̄_φ`.

```lean
def generators (M : MatterField jets) : Set (JetComponentSpace M)
```

**`StandardModel.FermionicAlgebra.span_generators_eq_top`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L178).

> The derivative monomials span the jet component space: every component function is the
> sum of its two halves, and each half is spanned by derivative monomials.

```lean
lemma span_generators_eq_top : Submodule.span ℂ (generators M) = ⊤
```

**`StandardModel.FermionicAlgebra.exists_jetComponentPoly_eq_monomial`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L206).

> Every derivative monomial is a monomial eigenvector of the component map: this is the
> only property of the component map that the square-zero argument uses.

```lean
lemma exists_jetComponentPoly_eq_monomial (w : ℕ) {v : JetComponentSpace M}
    (hv : v ∈ generators M) :
    ∃ n : ℕ, jetComponentPoly w v = Polynomial.monomial n (ExteriorAlgebra.ι ℂ v)
```

**`StandardModel.FermionicAlgebra.jetComponentPoly_mul_self`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L218).

> The component map squares to zero, as the universal property of the exterior algebra
> demands. The symmetrised square is a bilinear form, so it is enough to check that it
> vanishes on the derivative monomials, where it is a monomial multiple of
> `ExteriorAlgebra.ι_add_mul_swap`; halving then gives the square itself.

```lean
lemma jetComponentPoly_mul_self (w : ℕ) (v : JetComponentSpace M) :
    jetComponentPoly w v * jetComponentPoly w v = 0
```

## C. The mass-weight polynomial on the fermionic algebra

**`StandardModel.FermionicAlgebra.massWeightPoly`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L252).

> The mass-weight polynomial on the fermionic algebra of a field of mass weight `w`: the
> `ℂ`-algebra map sending a generator of mass weight `n` to `X ^ n` times itself. It is
> `FermionicAlgebra.massWeightScale` with the scalar replaced by the formal variable `X`.

```lean
noncomputable def massWeightPoly (w : ℕ) :
    FermionicAlgebra M →ₐ[ℂ] Polynomial (FermionicAlgebra M)
```

**`StandardModel.FermionicAlgebra.massWeightPoly_ι`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L258).

> On a component function the mass-weight polynomial is the component-function map.

```lean
lemma massWeightPoly_ι (w : ℕ) (x : JetComponentSpace M) :
    massWeightPoly w (ExteriorAlgebra.ι ℂ x) = jetComponentPoly w x
```

## D. The mass weight of the field and its derivatives

**`StandardModel.FermionicAlgebra.massWeightPoly_iteratedJetDeriv_ofField`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L270).

> The generator `∂_s ψ_φ` is a monomial eigenvector of mass weight `w + 2 |s|`: the field
> carries its own mass weight and each derivative adds two.

```lean
lemma massWeightPoly_iteratedJetDeriv_ofField (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ M.V) :
    massWeightPoly w (iteratedJetDeriv s (ofField φ)) =
      Polynomial.monomial (w + 2 * Multiset.card s) (iteratedJetDeriv s (ofField φ))
```

**`StandardModel.FermionicAlgebra.massWeightPoly_iteratedJetDeriv_ofConjField`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L278).

> The conjugate generator `∂_s ψ̄_φ` is a monomial eigenvector of the same mass weight
> `w + 2 |s|` as the generator it conjugates.

```lean
lemma massWeightPoly_iteratedJetDeriv_ofConjField (w : ℕ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule M.V)) :
    massWeightPoly w (iteratedJetDeriv s (ofConjField φ)) =
      Polynomial.monomial (w + 2 * Multiset.card s)
        (iteratedJetDeriv s (ofConjField φ))
```

**`StandardModel.FermionicAlgebra.massWeightPoly_ofField`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L286).

> The undifferentiated field has mass weight `w`.

```lean
lemma massWeightPoly_ofField (w : ℕ) (φ : Module.Dual ℂ M.V) :
    massWeightPoly w (ofField φ) = Polynomial.monomial w (ofField φ)
```

**`StandardModel.FermionicAlgebra.massWeightPoly_ofConjField`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L293).

> The undifferentiated conjugate field has mass weight `w`.

```lean
lemma massWeightPoly_ofConjField (w : ℕ) (φ : Module.Dual ℂ (ConjModule M.V)) :
    massWeightPoly w (ofConjField φ) = Polynomial.monomial w (ofConjField φ)
```

## E. Recovering an element from its mass-weight polynomial

**`StandardModel.FermionicAlgebra.halfPoly_eval_one`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L308).

> Setting the formal variable to one collapses a half mass-weight polynomial back to the
> symbol it graded. The derivative monomials span, so it is enough to check this on the
> multiset basis.

```lean
lemma halfPoly_eval_one {W : Type} [AddCommGroup W] [Module ℂ W] (w : ℕ)
    (k : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W →ₗ[ℂ] FermionicAlgebra M)
    (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] W) : (halfPoly w k y).eval 1 = k y
```

**`StandardModel.FermionicAlgebra.jetComponentPoly_eval_one`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L328).

> Setting the formal variable to one recovers the component function.

```lean
lemma jetComponentPoly_eval_one (w : ℕ) (x : JetComponentSpace M) :
    (jetComponentPoly w x).eval 1 = ExteriorAlgebra.ι ℂ x
```

**`StandardModel.FermionicAlgebra.massWeightPoly_eval_one`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L337).

> Setting the formal variable to one recovers the original element: the mass-weight
> pieces of an element sum back to it.

```lean
lemma massWeightPoly_eval_one (w : ℕ) (a : FermionicAlgebra M) :
    (massWeightPoly w a).eval 1 = a
```

**`StandardModel.FermionicAlgebra.massWeightPoly_injective`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean#L353).

> The mass-weight polynomial is injective: an element is recovered from its graded
> pieces. It is not surjective, since a monomial of the wrong degree is not the grading of
> anything.

```lean
lemma massWeightPoly_injective (w : ℕ) :
    Function.Injective (massWeightPoly (M := M) w)
```

## Depends on

- [The formal total derivative on the fermionic algebra](matter-fermionic-jetderiv.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassWeightPoly.lean)
