---
declaration: module
origin: cited
lean: TimeAndSpace.schwartzEuclideanAction, TimeAndSpace.schwartzEuclideanAction_apply, TimeAndSpace.instMulActionSchwartzMap, TimeAndSpace.smul_schwartzMap_apply, TimeAndSpace.schwartzEuclideanAction_mul_apply, TimeAndSpace.schwartzEuclideanAction_injective, TimeAndSpace.schwartzEuclideanAction_surjective
statement: formalized
proof: formalized
---

# The Euclidean group action on Schwartz maps over `TimeAndSpace`

The module `Physlib.SpaceAndTime.TimeAndSpace.EuclideanGroup.SchwartzAction`, [Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean): 7 declarations, 7 with a docstring.

## i. Overview

> In this file we define the pullback action of the Euclidean group on Schwartz maps over
> `TimeAndSpace d`. The action is
> `g • η = fun tx => η (g⁻¹ • tx)`.

## ii. Key results

> - `TimeAndSpace.schwartzEuclideanAction` : The Euclidean group action on Schwartz maps as a
>   continuous representation (`ContRepresentation`).
> - `TimeAndSpace.instMulActionSchwartzMap` : The induced `MulAction` instance on Schwartz maps.
> - `TimeAndSpace.smul_schwartzMap_apply` : Pointwise formula for the action.

## iv. References

> * None.

## A. The pullback action on Schwartz maps

**`TimeAndSpace.schwartzEuclideanAction`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean#L61).

> The Euclidean-group pullback action on Schwartz maps over `TimeAndSpace d`, as a continuous
> representation `ContRepresentation ℝ (EuclideanGroup d) 𝓢(TimeAndSpace d, F)`.
>
> `ContRepresentation R G V` unfolds to the monoid homomorphism `G →* V →L[R] V` into the
> *continuous*-linear maps: the builder `SchwartzMap.compCLMOfAntilipschitz` already yields a
> continuous-linear map for free, and the `→L` codomain lets the action compose under `∘L`. The
> plain mathlib `Representation` (`G →* V →ₗ[ℝ] V`) is recovered via
> `ContRepresentation.toRepresentation`.

```lean
noncomputable def schwartzEuclideanAction {d : ℕ} :
    ContRepresentation ℝ (EuclideanGroup d) 𝓢(TimeAndSpace d, F)
```

**`TimeAndSpace.schwartzEuclideanAction_apply`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean#L81).

> Pointwise formula for the monoid-homomorphism form of the Schwartz-map pullback action.

```lean
lemma schwartzEuclideanAction_apply {d : ℕ} (g : EuclideanGroup d) (η : 𝓢(TimeAndSpace d, F))
    (tx : TimeAndSpace d) :
    (schwartzEuclideanAction g η) tx = η (g⁻¹ • tx)
```

**`TimeAndSpace.instMulActionSchwartzMap`**, an instance, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean#L86).

> The Euclidean group acts on Schwartz maps over `TimeAndSpace d` by pullback.

```lean
noncomputable instance instMulActionSchwartzMap {d : ℕ} :
    MulAction (EuclideanGroup d) 𝓢(TimeAndSpace d, F)
```

**`TimeAndSpace.smul_schwartzMap_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean#L103).

> Pointwise formula for the `MulAction` instance on Schwartz maps.

```lean
lemma smul_schwartzMap_apply {d : ℕ} (g : EuclideanGroup d) (η : 𝓢(TimeAndSpace d, F))
    (tx : TimeAndSpace d) :
    (g • η) tx = η (g⁻¹ • tx)
```

**`TimeAndSpace.schwartzEuclideanAction_mul_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean#L108).

> Applying `g` and then `h` to a Schwartz map is the pullback action of `h * g`.

```lean
lemma schwartzEuclideanAction_mul_apply {d : ℕ} (g h : EuclideanGroup d)
    (η : 𝓢(TimeAndSpace d, F)) :
    schwartzEuclideanAction h (schwartzEuclideanAction g η) =
      schwartzEuclideanAction (h * g) η
```

**`TimeAndSpace.schwartzEuclideanAction_injective`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean#L117).

> Each Euclidean-group pullback action on Schwartz maps is injective.

```lean
lemma schwartzEuclideanAction_injective {d : ℕ} (g : EuclideanGroup d) :
    Function.Injective (schwartzEuclideanAction (F := F) g)
```

**`TimeAndSpace.schwartzEuclideanAction_surjective`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean#L125).

> Each Euclidean-group pullback action on Schwartz maps is surjective.

```lean
lemma schwartzEuclideanAction_surjective {d : ℕ} (g : EuclideanGroup d) :
    Function.Surjective (schwartzEuclideanAction (F := F) g)
```

## Depends on

- [The action of the Euclidean group on `TimeAndSpace`](euclideangroup-action.md)

## Sources

- [Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/SchwartzAction.lean)
