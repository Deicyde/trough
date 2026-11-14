---
declaration: module
origin: cited
lean: EuclideanGroup.smul_apply, EuclideanGroup.smul_vsub_smul, EuclideanGroup.dist_smul, EuclideanGroup.rotation_smul_eq, EuclideanGroup.rotation_smul_origin, EuclideanGroup.rotation_smul_vsub_origin, EuclideanGroup.rotation_dist_smul, EuclideanGroup.chartEuclidean_smul
statement: formalized
proof: formalized
---

# The action of the Euclidean group on `Space`

The module `Physlib.SpaceAndTime.Space.EuclideanGroup.Action`, [Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean): 9 declarations (1 instance with no name), 9 with a docstring.

> The Euclidean group `EuclideanGroup d = ℝᵈ ⋊ O(d)` (`Space/EuclideanGroup/Basic.lean`) is the group
> of rigid motions of `d`-dimensional space. This file makes that geometric meaning literal: it
> endows the affine space of points `Space d` (`Space/Basic.lean`) with a `MulAction` of
> `EuclideanGroup d` **by isometries**, and specialises it to the rotations.

## Main results

> * `EuclideanGroup.smul_vsub_smul` — displacements transform by the linear part alone.
> * `EuclideanGroup.dist_smul` — the action preserves distance.
> * `EuclideanGroup.rotation_smul_origin` / `rotation_smul_vsub_origin` — rotations fix the origin
>   and act about it by their orthogonal part.
> * `EuclideanGroup.chartEuclidean_smul` — agreement with the affine-isometry model
>   (`AffineGroup.lean`); the rest of the file does not depend on it.

## Implementation notes

> `Space d` is an affine space (`NormedAddTorsor`) with no canonical origin, so the action uses its
> vector-space zero `(0 : Space d)` as the basepoint:
>
> `g • p = (g.linear • (p -ᵥ (0 : Space d)) + g.translation) +ᵥ (0 : Space d)`.
>
> The `Zero` instance and the chart `Space.chartEuclidean` are defined in `Space/Origin.lean`.

## Part 1: the action of the Euclidean group on `Space`

> The motion `g = ⟨t, Q⟩` acts by `g • p = (Q • (p -ᵥ origin) + t) +ᵥ origin`. The `MulAction` laws
> reduce to the semidirect-product group law of `EuclideanGroup`.

**An instance with no name**, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L51).

> The action of the Euclidean group on the affine space of points `Space d`: `g = ⟨t, Q⟩` rotates
> `p` about the coordinate origin by the orthogonal part `Q` and then translates by `t`.

```lean
noncomputable instance : MulAction (EuclideanGroup d) (Space d)
```

**`EuclideanGroup.smul_apply`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L64).

> Coordinate formula for the action: `(g • p) i = (Q • (p -ᵥ origin)) i + t i`.

```lean
lemma smul_apply (g : EuclideanGroup d) (p : Space d) (i : Fin d) :
    (g • p) i = (g.linear • (p -ᵥ (0 : Space d))) i + g.translation i
```

**`EuclideanGroup.smul_vsub_smul`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L72).

> The displacement between two points transforms by the **orthogonal part alone**: the
> translation cancels. This is the key lemma behind `dist_smul`.

```lean
lemma smul_vsub_smul (g : EuclideanGroup d) (p q : Space d) :
    (g • p) -ᵥ (g • q) = g.linear • (p -ᵥ q)
```

**`EuclideanGroup.dist_smul`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L82).

> The Euclidean group acts on `Space d` **by isometries**: every rigid motion preserves distance.

```lean
lemma dist_smul (g : EuclideanGroup d) (p q : Space d) :
    dist (g • p) (g • q) = dist p q
```

## Part 2: specialisation to rotations

> The `RotationGroup d` action is the restriction of the Euclidean action along
> `RotationGroup d ≤ EuclideanGroup d` (`RotationGroup` elements have zero translation). The lemmas
> below record that rotations fix the origin, act by their orthogonal part about the origin, and
> preserve distance.

**`EuclideanGroup.rotation_smul_eq`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L97).

> The rotation-group action is the restriction of the Euclidean action: `r • p = ↑r • p`
> (definitional).

```lean
lemma rotation_smul_eq (r : RotationGroup d) (p : Space d) :
    r • p = (r : EuclideanGroup d) • p
```

**`EuclideanGroup.rotation_smul_origin`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L103).

> A rotation fixes the origin: its translation part vanishes
> (`RotationGroup ≤ OriginStabilizer`), so `↑r • 0 = 0`. Stated in the `↑r` form (the simp normal
> form of `r • _`, via `rotation_smul_eq`) so it is a well-formed `simp` lemma.

```lean
lemma rotation_smul_origin (r : RotationGroup d) :
    (r : EuclideanGroup d) • (0 : Space d) = (0 : Space d)
```

**`EuclideanGroup.rotation_smul_vsub_origin`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L116).

> A rotation acts on the displacement from the origin by its orthogonal part, for every `p`:
> `(r • p) -ᵥ origin = Q • (p -ᵥ origin)`.

```lean
lemma rotation_smul_vsub_origin (r : RotationGroup d) (p : Space d) :
    (r • p) -ᵥ (0 : Space d) = (r : EuclideanGroup d).linear • (p -ᵥ (0 : Space d))
```

**`EuclideanGroup.rotation_dist_smul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L123).

> The rotation group acts on `Space d` **by isometries** (inherited from `dist_smul`).

```lean
lemma rotation_dist_smul (r : RotationGroup d) (p q : Space d) :
    dist (r • p) (r • q) = dist p q
```

## Part 3: relation to the affine isometry action (optional bridge)

> `chartEuclidean_smul` records that, under the chart `Space.chartEuclidean` (`Space/Origin.lean`),
> `p ↦ p -ᵥ origin`, the Part 1 action is the transport of `toAffineIsometryMulEquiv`
> (`AffineGroup.lean`) from `EuclideanSpace` to `Space`. Nothing in Parts 1–2 depends on it.

**`EuclideanGroup.chartEuclidean_smul`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean#L136).

> Under the standard chart, the Euclidean action on `Space d` is the
> transport of `toAffineIsometryMulEquiv` acting on `EuclideanSpace`:
> `chart (g • p) = (toAffineIsometryMulEquiv g) (chart p)`.

```lean
lemma chartEuclidean_smul (g : EuclideanGroup d) (p : Space d) :
    Space.chartEuclidean d (g • p) = toAffineIsometryMulEquiv g (Space.chartEuclidean d p)
```

## Depends on

- [The inclusion of the Euclidean group into the affine automorphism group](euclideangroup-affinegroup.md)
- [The origin of `Space` and the Euclidean chart](../part-01/origin.md)

## Sources

- [Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Action.lean)
