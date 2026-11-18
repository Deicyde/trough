---
declaration: module
origin: cited
lean: StandardModel.BosonicAlgebra.repLorentzGroup, StandardModel.BosonicAlgebra.repLorentzGroup_apply, StandardModel.BosonicAlgebra.repLorentzGroup_apply_one, StandardModel.BosonicAlgebra.repLorentzGroup_apply_mul, StandardModel.BosonicAlgebra.repLorentzGroup_ι, StandardModel.BosonicAlgebra.repLorentzGroupAlgHom, StandardModel.BosonicAlgebra.repLorentzGroup_ofField, StandardModel.BosonicAlgebra.repLorentzGroup_ofConjField
statement: formalized
proof: formalized
---

# The Lorentz action on the bosonic algebra

The module `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.LorentzAction`, [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean): 10 declarations, 7 with a docstring.

## i. Overview

> Given a representation of `SL(2,ℂ)` on the target space `V` of a bosonic matter field, the
> Lorentz group acts on the bosonic algebra by the symmetric-algebra functor applied to its
> action on the jet component space. On a component function `∂_s φ_α` the derivative labels
> transform by the Lorentz matrix and the target index contragrediently by `V`.
>
> The formal total derivative is a Lorentz vector for this action, which is exactly the
> content of the class `Lorentz.IsLorentzDeriv`; the instance is registered here, so all the
> boost-weight machinery of `PhyslibAlpha.Relativity.IsLorentzDeriv` applies to the bosonic
> algebra of any matter field.

## ii. Key results

> - `BosonicAlgebra.repLorentzGroup` : the Lorentz action on the bosonic algebra.
> - `BosonicAlgebra.repLorentzGroupAlgHom` : the action as an algebra homomorphism.
> - `BosonicAlgebra.repLorentzGroup_ofField` : `ofField` is `SL(2,ℂ)`-equivariant.
> - `BosonicAlgebra.repLorentzGroup_jetDeriv` : the total derivative is a Lorentz vector.
> - `BosonicAlgebra.instIsLorentzDeriv` : the resulting `Lorentz.IsLorentzDeriv` instance.

## iv. References

> * None.

## A. The action of the Lorentz group

**`StandardModel.BosonicAlgebra.repLorentzGroup`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L65).

> **The Lorentz action on the bosonic algebra** of the matter field `M`, induced
> from a representation `M.repLorentz` of `SL(2,ℂ)` on `V`: the symmetric-algebra functor applied
> to the Lorentz action on the jet component space.

```lean
noncomputable def repLorentzGroup :
    Representation ℂ SL(2,ℂ) (BosonicAlgebra M)
```

**`StandardModel.BosonicAlgebra.repLorentzGroup_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L74).

```lean
lemma repLorentzGroup_apply (Λ : SL(2,ℂ))
    (x : BosonicAlgebra M) :
    repLorentzGroup M Λ x =
      SymmetricAlgebra.map (JetComponentSpace.repLorentzGroup M Λ) x
```

**`StandardModel.BosonicAlgebra.repLorentzGroup_apply_one`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L80).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    repLorentzGroup M Λ (1 : BosonicAlgebra M) = 1
```

**`StandardModel.BosonicAlgebra.repLorentzGroup_apply_mul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L84).

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ))
    (x y : BosonicAlgebra M) :
    repLorentzGroup M Λ (x * y)
      = repLorentzGroup M Λ x * repLorentzGroup M Λ y
```

**`StandardModel.BosonicAlgebra.repLorentzGroup_ι`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L92).

> On a component function the Lorentz action is the action on the component space.

```lean
lemma repLorentzGroup_ι (Λ : SL(2,ℂ))
    (v : JetComponentSpace M) :
    repLorentzGroup M Λ (SymmetricAlgebra.ι ℂ _ v) =
      SymmetricAlgebra.ι ℂ _ (JetComponentSpace.repLorentzGroup M Λ v)
```

**`StandardModel.BosonicAlgebra.repLorentzGroupAlgHom`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L100).

> The Lorentz action as an algebra homomorphism: it preserves the symmetric product, so a
> Lorentz transformation acts on a Lagrangian term factor by factor.

```lean
noncomputable def repLorentzGroupAlgHom (Λ : SL(2,ℂ)) :
    BosonicAlgebra M →ₐ[ℂ] BosonicAlgebra M
```

### A.1. Equivariance of the field and its conjugate

**`StandardModel.BosonicAlgebra.repLorentzGroup_ofField`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L120).

> **`ofField` is `SL(2,ℂ)`-equivariant.** The undifferentiated component functions carry
> the contragredient of the representation on the target space, and no derivative labels
> are generated: `ofField` intertwines `M.repLorentz.dual` with the action on the bosonic
> algebra.

```lean
lemma repLorentzGroup_ofField (Λ : SL(2,ℂ))
    (φ : Module.Dual ℂ M.V) :
    repLorentzGroup M Λ (ofField φ) = ofField (M.repLorentz.dual Λ φ)
```

**`StandardModel.BosonicAlgebra.repLorentzGroup_ofConjField`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L136).

> **`ofConjField` is `SL(2,ℂ)`-equivariant**, for the conjugate of the representation on
> the target space: the conjugate component functions transform by `star` of the spinor
> matrix.

```lean
lemma repLorentzGroup_ofConjField (Λ : SL(2,ℂ))
    (φ : Module.Dual ℂ (ConjModule M.V)) :
    repLorentzGroup M Λ (ofConjField φ) = ofConjField (M.repLorentz.conj.dual Λ φ)
```

## B. Lorentz covariance of the total derivative

**`StandardModel.BosonicAlgebra.repLorentzGroup_jetDeriv`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L158).

> **The total derivative on the bosonic algebra is a Lorentz vector.** The four
> derivations `∂_μ` transform into each other by the columns of the Lorentz matrix of `Λ`,
> exactly as the covector index `μ` should.

```lean
lemma repLorentzGroup_jetDeriv (Λ : SL(2,ℂ))
    (μ : Fin 1 ⊕ Fin 3) (x : BosonicAlgebra M) :
    repLorentzGroup M Λ (jetDeriv μ x) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        jetDeriv a (repLorentzGroup M Λ x)
```

**`StandardModel.BosonicAlgebra.instIsLorentzDeriv`**, an instance, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean#L184).

> The total derivatives on the bosonic algebra form a Lorentz derivative, giving access
> to the boost-weight machinery of `PhyslibAlpha.Relativity.IsLorentzDeriv`.

```lean
instance instIsLorentzDeriv :
    Lorentz.IsLorentzDeriv (repLorentzGroup M) (jetDeriv (M := M))
```

## Depends on

- [The formal total derivative on the bosonic algebra](matter-bosonic-jetderiv.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/LorentzAction.lean)
