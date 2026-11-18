---
declaration: module
origin: cited
lean: StandardModel.FermionicAlgebra.massWeightScale, StandardModel.FermionicAlgebra.massWeightScale_ι, StandardModel.FermionicAlgebra.massWeightScale_ofField, StandardModel.FermionicAlgebra.massWeightScale_ofConjField, StandardModel.FermionicAlgebra.massWeightScale_jetDeriv, StandardModel.FermionicAlgebra.massWeightScale_iteratedJetDeriv
statement: formalized
proof: formalized
---

# Mass dimension on the fermionic algebra

The module `PhyslibAlpha.Particles.StandardModel.Matter.Fermionic.MassDim`, [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean): 6 declarations, 5 with a docstring.

## i. Overview

> The mass dimension of a fermionic matter field is tracked multiplicatively through the
> *mass-weight scaling*: the algebra endomorphism multiplying each generator `∂_s ψ_α` by
> `c ^ (w + 2 |s|)`, where `w` is the mass weight of the field — twice its mass dimension,
> kept integral because a fermion has mass dimension `3/2` and hence mass weight `3`. A
> monomial of total mass weight `n` is scaled by `c ^ n`, so the scaling records the
> mass-weight grading of the algebra, and its interaction with the total derivative says
> that a derivative carries mass weight two. This mirrors
> `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.MassDim`.

## ii. Key results

> - `FermionicAlgebra.massWeightScale` : the mass-weight scaling.
> - `FermionicAlgebra.massWeightScale_ofField` : the field carries its own mass weight.
> - `FermionicAlgebra.massWeightScale_jetDeriv` : a derivative adds mass weight two.
> - `FermionicAlgebra.massWeightScale_iteratedJetDeriv` : `∂_s` adds mass weight `2 |s|`.

## iv. References

> * None.

## A. The mass-weight scaling

**`StandardModel.FermionicAlgebra.massWeightScale`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean#L62).

> **The mass-weight scaling on the fermionic algebra** of a field of mass weight `w`:
> the algebra endomorphism scaling the generator `∂_s ψ_α` by `c ^ (w + 2 |s|)`, the
> functorial lift of the scaling on the jet component space.

```lean
noncomputable def massWeightScale (w : ℕ) (c : ℂ) :
    FermionicAlgebra M →ₐ[ℂ] FermionicAlgebra M
```

**`StandardModel.FermionicAlgebra.massWeightScale_ι`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean#L67).

```lean
lemma massWeightScale_ι (w : ℕ) (c : ℂ) (x : JetComponentSpace M) :
    massWeightScale w c (ExteriorAlgebra.ι ℂ x)
      = ExteriorAlgebra.ι ℂ (JetComponentSpace.massWeightScale w c x)
```

## B. The mass weight of the field and its derivatives

**`StandardModel.FermionicAlgebra.massWeightScale_ofField`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean#L80).

> The undifferentiated field carries its own mass weight.

```lean
lemma massWeightScale_ofField (w : ℕ) (c : ℂ) (φ : Module.Dual ℂ M.V) :
    massWeightScale w c (ofField φ) = c ^ w • ofField φ
```

**`StandardModel.FermionicAlgebra.massWeightScale_ofConjField`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean#L93).

> The undifferentiated conjugate field carries the same mass weight as the field.

```lean
lemma massWeightScale_ofConjField (w : ℕ) (c : ℂ) (φ : Module.Dual ℂ (ConjModule M.V)) :
    massWeightScale w c (ofConjField φ) = c ^ w • ofConjField φ
```

**`StandardModel.FermionicAlgebra.massWeightScale_jetDeriv`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean#L106).

> **A total derivative adds mass weight two**: the scaling intertwines the total
> derivative up to a factor `c ^ 2`.

```lean
lemma massWeightScale_jetDeriv (w : ℕ) (c : ℂ) (μ : Fin 1 ⊕ Fin 3)
    (x : FermionicAlgebra M) :
    massWeightScale w c (jetDeriv μ x) = c ^ 2 • jetDeriv μ (massWeightScale w c x)
```

**`StandardModel.FermionicAlgebra.massWeightScale_iteratedJetDeriv`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean#L122).

> **The iterated derivative `∂_s` adds mass weight `2 |s|`.**

```lean
lemma massWeightScale_iteratedJetDeriv (w : ℕ) (c : ℂ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (x : FermionicAlgebra M) :
    massWeightScale w c (iteratedJetDeriv s x)
      = c ^ (2 * Multiset.card s) • iteratedJetDeriv s (massWeightScale w c x)
```

## Depends on

- [The formal total derivative on the fermionic algebra](matter-fermionic-jetderiv.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Fermionic/MassDim.lean)
