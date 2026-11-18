---
declaration: module
origin: cited
lean: StandardModel.FermionicAlgebra.repLorentzGroup, StandardModel.FermionicAlgebra.repLorentzGroup_apply, StandardModel.FermionicAlgebra.repLorentzGroup_apply_one, StandardModel.FermionicAlgebra.repLorentzGroup_apply_mul, StandardModel.FermionicAlgebra.repLorentzGroup_ι, StandardModel.FermionicAlgebra.repLorentzGroupAlgHom, StandardModel.FermionicAlgebra.repLorentzGroup_ofField, StandardModel.FermionicAlgebra.repLorentzGroup_ofConjField
statement: formalized
proof: formalized
---

# The Lorentz action on the fermionic algebra

The module `PhyslibAlpha.Particles.StandardModel.Matter.Fermionic.LorentzAction`, [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean): 10 declarations, 7 with a docstring.

## i. Overview

> Given a representation of `SL(2,ℂ)` on the target space `V` of a matter field, the Lorentz
> group acts on the fermionic algebra by the exterior-algebra functor applied to its action
> on the jet component space. On a component function `∂_s ψ_α` the derivative labels
> transform by the Lorentz matrix and the target index contragrediently by `V`.
>
> The formal total derivative is a Lorentz vector for this action, which is exactly the
> content of the class `Lorentz.IsLorentzDeriv`; the instance is registered here, so all the
> boost-weight machinery of `PhyslibAlpha.Relativity.IsLorentzDeriv` applies to the fermionic
> algebra of any matter field.

## ii. Key results

> - `FermionicAlgebra.repLorentzGroup` : the Lorentz action on the fermionic algebra.
> - `FermionicAlgebra.repLorentzGroupAlgHom` : the action as an algebra homomorphism.
> - `FermionicAlgebra.repLorentzGroup_ofField` : `ofField` is `SL(2,ℂ)`-equivariant.
> - `FermionicAlgebra.repLorentzGroup_jetDeriv` : the total derivative is a Lorentz vector.
> - `FermionicAlgebra.instIsLorentzDeriv` : the resulting `Lorentz.IsLorentzDeriv` instance.

## iv. References

> * None.

## A. The action of the Lorentz group

**`StandardModel.FermionicAlgebra.repLorentzGroup`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L65).

> **The Lorentz action on the fermionic algebra** of the matter field `M`, induced
> from a representation `M.repLorentz` of `SL(2,ℂ)` on `V`: the exterior-algebra functor applied to
> the Lorentz action on the jet component space.

```lean
noncomputable def repLorentzGroup :
    Representation ℂ SL(2,ℂ) (FermionicAlgebra M)
```

**`StandardModel.FermionicAlgebra.repLorentzGroup_apply`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L75).

```lean
lemma repLorentzGroup_apply (Λ : SL(2,ℂ))
    (x : FermionicAlgebra M) :
    repLorentzGroup M Λ x =
      ExteriorAlgebra.map (JetComponentSpace.repLorentzGroup M Λ) x
```

**`StandardModel.FermionicAlgebra.repLorentzGroup_apply_one`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L81).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    repLorentzGroup M Λ (1 : FermionicAlgebra M) = 1
```

**`StandardModel.FermionicAlgebra.repLorentzGroup_apply_mul`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L85).

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ))
    (x y : FermionicAlgebra M) :
    repLorentzGroup M Λ (x * y)
      = repLorentzGroup M Λ x * repLorentzGroup M Λ y
```

**`StandardModel.FermionicAlgebra.repLorentzGroup_ι`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L93).

> On a component function the Lorentz action is the action on the component space.

```lean
lemma repLorentzGroup_ι (Λ : SL(2,ℂ))
    (v : JetComponentSpace M) :
    repLorentzGroup M Λ (ExteriorAlgebra.ι ℂ v) =
      ExteriorAlgebra.ι ℂ (JetComponentSpace.repLorentzGroup M Λ v)
```

**`StandardModel.FermionicAlgebra.repLorentzGroupAlgHom`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L101).

> The Lorentz action as an algebra homomorphism: it preserves the exterior product, so a
> Lorentz transformation acts on a Lagrangian term factor by factor.

```lean
noncomputable def repLorentzGroupAlgHom (Λ : SL(2,ℂ)) :
    FermionicAlgebra M →ₐ[ℂ] FermionicAlgebra M
```

### A.1. Equivariance of the field and its conjugate

**`StandardModel.FermionicAlgebra.repLorentzGroup_ofField`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L121).

> **`ofField` is `SL(2,ℂ)`-equivariant.** The undifferentiated component functions carry
> the contragredient of the representation on the target space, and no derivative labels
> are generated: `ofField` intertwines `M.repLorentz.dual` with the action on the fermionic
> algebra.

```lean
lemma repLorentzGroup_ofField (Λ : SL(2,ℂ))
    (φ : Module.Dual ℂ M.V) :
    repLorentzGroup M Λ (ofField φ) = ofField (M.repLorentz.dual Λ φ)
```

**`StandardModel.FermionicAlgebra.repLorentzGroup_ofConjField`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L137).

> **`ofConjField` is `SL(2,ℂ)`-equivariant**, for the conjugate of the representation on
> the target space: the conjugate component functions transform by `star` of the spinor
> matrix.

```lean
lemma repLorentzGroup_ofConjField (Λ : SL(2,ℂ))
    (φ : Module.Dual ℂ (ConjModule M.V)) :
    repLorentzGroup M Λ (ofConjField φ) = ofConjField (M.repLorentz.conj.dual Λ φ)
```

## B. Lorentz covariance of the total derivative

**`StandardModel.FermionicAlgebra.repLorentzGroup_jetDeriv`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L159).

> **The total derivative on the fermionic algebra is a Lorentz vector.** The four
> derivations `∂_μ` transform into each other by the columns of the Lorentz matrix of `Λ`,
> exactly as the covector index `μ` should.

```lean
lemma repLorentzGroup_jetDeriv (Λ : SL(2,ℂ))
    (μ : Fin 1 ⊕ Fin 3) (x : FermionicAlgebra M) :
    repLorentzGroup M Λ (jetDeriv μ x) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        jetDeriv a (repLorentzGroup M Λ x)
```

**`StandardModel.FermionicAlgebra.instIsLorentzDeriv`**, an instance, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean#L185).

> The total derivatives on the fermionic algebra form a Lorentz derivative, giving access
> to the boost-weight machinery of `PhyslibAlpha.Relativity.IsLorentzDeriv`.

```lean
instance instIsLorentzDeriv :
    Lorentz.IsLorentzDeriv (repLorentzGroup M) (jetDeriv (M := M))
```

## Depends on

- [The formal total derivative on the fermionic algebra](matter-fermionic-jetderiv.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/LorentzAction.lean)
