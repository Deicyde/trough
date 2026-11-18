---
declaration: module
origin: cited
lean: SpaceTime.schwartzAction, SpaceTime.schwartzAction_mul_apply, SpaceTime.schwartzAction_apply, SpaceTime.schwartzAction_injective, SpaceTime.schwartzAction_surjective, SpaceTime.lorentzGroup_smul_dist_apply, SpaceTime.distActionLinearMap
statement: formalized
proof: formalized
---

# Lorentz group actions related to SpaceTime

The module `Physlib.SpaceAndTime.SpaceTime.LorentzAction`, [Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean): 10 declarations (3 instances with no name), 2 with a docstring.

## i. Overview

> We already have a Lorentz group action on `SpaceTime d`, in this module
> we define the induced action on Schwartz functions and distributions.

## ii. Key results

> - `schwartzAction` : Defines the action of the Lorentz group on Schwartz functions.
> - An instance of `DistribMulAction` for the Lorentz group acting on distributions.

## iv. References

> * None.

## A. Lorentz group action on Schwartz functions

### A.1. The definition of the action

**`SpaceTime.schwartzAction`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L69).

> The Lorentz group action on Schwartz functions taking the Lorentz group to
> continuous linear maps.

```lean
def schwartzAction {d} : LorentzGroup d →* 𝓢(SpaceTime d, ℝ) →L[ℝ] 𝓢(SpaceTime d, ℝ)
```

### A.2. Basic properties of the action

**`SpaceTime.schwartzAction_mul_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L94).

```lean
lemma schwartzAction_mul_apply {d} (Λ₁ Λ₂ : LorentzGroup d)
    (η : 𝓢(SpaceTime d, ℝ)) :
    schwartzAction Λ₂ (schwartzAction (Λ₁) η) =
    schwartzAction (Λ₂ * Λ₁) η
```

**`SpaceTime.schwartzAction_apply`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L100).

```lean
lemma schwartzAction_apply {d} (Λ : LorentzGroup d)
    (η : 𝓢(SpaceTime d, ℝ)) (x : SpaceTime d) :
    (schwartzAction Λ η) x = η (Λ⁻¹ • x)
```

### A.3. Injectivity of the action

**`SpaceTime.schwartzAction_injective`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L110).

```lean
lemma schwartzAction_injective {d} (Λ : LorentzGroup d) :
    Function.Injective (schwartzAction Λ)
```

### A.4. Surjectivity of the action

**`SpaceTime.schwartzAction_surjective`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L126).

```lean
lemma schwartzAction_surjective {d} (Λ : LorentzGroup d) :
    Function.Surjective (schwartzAction Λ)
```

## B. Lorentz group action on distributions

### B.1. The SMul instance

**An instance with no name**, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L151).

```lean
instance : SMul (LorentzGroup d) ((SpaceTime d) →d[ℝ] M)
```

**`SpaceTime.lorentzGroup_smul_dist_apply`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L154).

```lean
lemma lorentzGroup_smul_dist_apply (Λ : LorentzGroup d) (f : (SpaceTime d) →d[ℝ] M)
    (η : 𝓢(SpaceTime d, ℝ)) : (Λ • f) η = Λ • (f (schwartzAction Λ⁻¹ η))
```

### B.2. The DistribMulAction instance

**An instance with no name**, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L164).

```lean
instance : DistribMulAction (LorentzGroup d) ((SpaceTime d) →d[ℝ] M)
```

### B.3. The SMulCommClass instance

**An instance with no name**, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L186).

```lean
instance : SMulCommClass ℝ (LorentzGroup d) ((SpaceTime d) →d[ℝ] M)
```

### B.4. Action as a linear map

**`SpaceTime.distActionLinearMap`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean#L199).

> The Lorentz action on distributions as a linear map.

```lean
def distActionLinearMap {d} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M] [Tensorial (realLorentzTensor d) c M] [T2Space M](Λ : LorentzGroup d) :
    ((SpaceTime d) →d[ℝ] M) →ₗ[ℝ] ((SpaceTime d) →d[ℝ] M)
```

## Depends on

- [Distributions](../../mathematics/distribution/tempereddistribution.md)
- [Spacetime](basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/LorentzAction.lean)
