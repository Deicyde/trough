---
declaration: module
origin: cited
lean: StandardModel.BosonicAlgebra.massWeightScale, StandardModel.BosonicAlgebra.massWeightScale_ι, StandardModel.BosonicAlgebra.massWeightScale_ofField, StandardModel.BosonicAlgebra.massWeightScale_ofConjField, StandardModel.BosonicAlgebra.massWeightScale_jetDeriv, StandardModel.BosonicAlgebra.massWeightScale_iteratedJetDeriv
statement: formalized
proof: formalized
---

# Mass dimension on the bosonic algebra

The module `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.MassDim`, [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean): 6 declarations, 5 with a docstring.

## i. Overview

> The mass dimension of a bosonic matter field is tracked multiplicatively through the
> *mass-weight scaling*: the algebra endomorphism multiplying each generator `∂_s φ_α` by
> `c ^ (w + 2 |s|)`, where `w` is the mass weight of the field — twice its mass dimension,
> kept integral so the same machinery serves the fermions of dimension `3/2`. A monomial of
> total mass weight `n` is scaled by `c ^ n`, so the scaling records the mass-weight grading
> of the algebra, and its interaction with the total derivative says that a derivative
> carries mass weight two.

## ii. Key results

> - `BosonicAlgebra.massWeightScale` : the mass-weight scaling.
> - `BosonicAlgebra.massWeightScale_ofField` : the field carries its own mass weight.
> - `BosonicAlgebra.massWeightScale_jetDeriv` : a derivative adds mass weight two.
> - `BosonicAlgebra.massWeightScale_iteratedJetDeriv` : `∂_s` adds mass weight `2 |s|`.

## iv. References

> * None.

## A. The mass-weight scaling

**`StandardModel.BosonicAlgebra.massWeightScale`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean#L61).

> **The mass-weight scaling on the bosonic algebra** of a field of mass weight `w`:
> the algebra endomorphism scaling the generator `∂_s φ_α` by `c ^ (w + 2 |s|)`, the
> functorial lift of the scaling on the jet component space.

```lean
noncomputable def massWeightScale (w : ℕ) (c : ℂ) : BosonicAlgebra M →ₐ[ℂ] BosonicAlgebra M
```

**`StandardModel.BosonicAlgebra.massWeightScale_ι`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean#L65).

```lean
lemma massWeightScale_ι (w : ℕ) (c : ℂ) (x : JetComponentSpace M) :
    massWeightScale w c (SymmetricAlgebra.ι ℂ _ x)
      = SymmetricAlgebra.ι ℂ _ (JetComponentSpace.massWeightScale w c x)
```

## B. The mass weight of the field and its derivatives

**`StandardModel.BosonicAlgebra.massWeightScale_ofField`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean#L78).

> The undifferentiated field carries its own mass weight.

```lean
lemma massWeightScale_ofField (w : ℕ) (c : ℂ) (φ : Module.Dual ℂ M.V) :
    massWeightScale w c (ofField φ) = c ^ w • ofField φ
```

**`StandardModel.BosonicAlgebra.massWeightScale_ofConjField`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean#L91).

> The undifferentiated conjugate field carries the same mass weight as the field.

```lean
lemma massWeightScale_ofConjField (w : ℕ) (c : ℂ) (φ : Module.Dual ℂ (ConjModule M.V)) :
    massWeightScale w c (ofConjField φ) = c ^ w • ofConjField φ
```

**`StandardModel.BosonicAlgebra.massWeightScale_jetDeriv`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean#L104).

> **A total derivative adds mass weight two**: the scaling intertwines the total
> derivative up to a factor `c ^ 2`.

```lean
lemma massWeightScale_jetDeriv (w : ℕ) (c : ℂ) (μ : Fin 1 ⊕ Fin 3) (x : BosonicAlgebra M) :
    massWeightScale w c (jetDeriv μ x) = c ^ 2 • jetDeriv μ (massWeightScale w c x)
```

**`StandardModel.BosonicAlgebra.massWeightScale_iteratedJetDeriv`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean#L119).

> **The iterated derivative `∂_s` adds mass weight `2 |s|`.**

```lean
lemma massWeightScale_iteratedJetDeriv (w : ℕ) (c : ℂ) (s : Multiset (Fin 1 ⊕ Fin 3))
    (x : BosonicAlgebra M) :
    massWeightScale w c (iteratedJetDeriv s x)
      = c ^ (2 * Multiset.card s) • iteratedJetDeriv s (massWeightScale w c x)
```

## Depends on

- [The formal total derivative on the bosonic algebra](matter-bosonic-jetderiv.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/MassDim.lean)
