---
declaration: module
origin: cited
lean: TimeAndSpace.instMulActionEuclideanGroup, TimeAndSpace.smul_mk, TimeAndSpace.fst_smul, TimeAndSpace.snd_smul, TimeAndSpace.time_smul, TimeAndSpace.space_smul, TimeAndSpace.dist_smul, TimeAndSpace.actionLinearMap
statement: formalized
proof: formalized
---

# The action of the Euclidean group on `TimeAndSpace`

The module `Physlib.SpaceAndTime.TimeAndSpace.EuclideanGroup.Action`, [Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean): 13 declarations, 12 with a docstring.

## i. Overview

> In this file we define the action of the Euclidean group on `TimeAndSpace d`. The action fixes
> the time coordinate and acts on the space coordinate by the usual Euclidean-group action on
> `Space d`.

## ii. Key results

> - `TimeAndSpace.instMulActionEuclideanGroup` : The action of the Euclidean group on
>   `TimeAndSpace d`.
> - `TimeAndSpace.dist_smul` : The Euclidean group action on `TimeAndSpace d` preserves distance.
> - `TimeAndSpace.smul_hasTemperateGrowth` : The Euclidean group action has temperate growth.
> - `TimeAndSpace.antilipschitz_smul` : The Euclidean group action is antilipschitz.

## iv. References

> * None.

## A. The Euclidean group action

**`TimeAndSpace.instMulActionEuclideanGroup`**, an instance, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L51).

> The Euclidean group acts on `TimeAndSpace d` by fixing time and acting on space.

```lean
noncomputable instance instMulActionEuclideanGroup :
    MulAction (EuclideanGroup d) (TimeAndSpace d)
```

**`TimeAndSpace.smul_mk`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L65).

> Coordinate formula for the Euclidean-group action on `TimeAndSpace d`.

```lean
lemma smul_mk (g : EuclideanGroup d) (t : Time) (x : Space d) :
    g • ((t, x) : TimeAndSpace d) = (t, g • x)
```

**`TimeAndSpace.fst_smul`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L72).

> The Euclidean-group action fixes the first coordinate.

```lean
lemma fst_smul (g : EuclideanGroup d) (tx : TimeAndSpace d) :
    (g • tx).1 = tx.1
```

**`TimeAndSpace.snd_smul`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L79).

> The Euclidean-group action applies to the second coordinate.

```lean
lemma snd_smul (g : EuclideanGroup d) (tx : TimeAndSpace d) :
    (g • tx).2 = g • tx.2
```

**`TimeAndSpace.time_smul`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L85).

> The Euclidean-group action fixes the time projection.

```lean
lemma time_smul (g : EuclideanGroup d) (tx : TimeAndSpace d) :
    time (g • tx) = time tx
```

**`TimeAndSpace.space_smul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L90).

> The Euclidean-group action applies to the space projection.

```lean
lemma space_smul (g : EuclideanGroup d) (tx : TimeAndSpace d) :
    space (g • tx) = g • space tx
```

**`TimeAndSpace.dist_smul`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L95).

> The Euclidean-group action on `TimeAndSpace d` preserves product distance.

```lean
lemma dist_smul (g : EuclideanGroup d) (tx ty : TimeAndSpace d) :
    dist (g • tx) (g • ty) = dist tx ty
```

## B. Temperate growth of the coordinate action

**`TimeAndSpace.actionLinearMap`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L109).

> The linear part of the Euclidean-group action on `TimeAndSpace d`.

```lean
noncomputable def actionLinearMap (g : EuclideanGroup d) :
    TimeAndSpace d →L[ℝ] TimeAndSpace d
```

**`TimeAndSpace.actionTranslation`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L118).

> The translation part of the Euclidean-group action on `TimeAndSpace d`.

```lean
noncomputable def actionTranslation (g : EuclideanGroup d) : TimeAndSpace d
```

**`TimeAndSpace.smul_eq_actionLinearMap_add`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L121).

```lean
lemma smul_eq_actionLinearMap_add (g : EuclideanGroup d) (tx : TimeAndSpace d) :
    g • tx = actionLinearMap g tx + actionTranslation g
```

**`TimeAndSpace.smul_hasTemperateGrowth`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L133).

> The Euclidean-group action on `TimeAndSpace d` has temperate growth.

```lean
lemma smul_hasTemperateGrowth (g : EuclideanGroup d) :
    Function.HasTemperateGrowth (fun tx : TimeAndSpace d => g • tx)
```

**`TimeAndSpace.isometry_smul`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L144).

> The Euclidean-group action on `TimeAndSpace d` is an isometry.

```lean
lemma isometry_smul (g : EuclideanGroup d) :
    Isometry (fun tx : TimeAndSpace d => g • tx)
```

**`TimeAndSpace.antilipschitz_smul`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean#L149).

> The Euclidean-group action on `TimeAndSpace d` is antilipschitz.

```lean
lemma antilipschitz_smul (g : EuclideanGroup d) :
    AntilipschitzWith 1 (fun tx : TimeAndSpace d => g • tx)
```

## Depends on

- [The action of the Euclidean group on `Space`](../space/part-02/euclideangroup-action.md)
- [Functions and distributions on Time and Space d](basic.md)

## Sources

- [Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/EuclideanGroup/Action.lean)
