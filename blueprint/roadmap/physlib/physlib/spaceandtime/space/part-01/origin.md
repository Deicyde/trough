---
declaration: module
origin: cited
lean: Space.zero_val, Space.zero_apply, Space.vectorToSpace, Space.vectorToSpace_apply, Space.vectorToSpace_vsub_zero, Space.chartEuclidean, Space.chartEuclidean_apply
statement: formalized
proof: formalized
---

# The origin of `Space` and the Euclidean chart

The module `Physlib.SpaceAndTime.Space.Origin`, [Physlib/SpaceAndTime/Space/Origin.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean): 8 declarations (1 instance with no name), 2 with a docstring.

> The choice of origin for `Space d` is its vector-space zero `(0 : Space d)`. This file provides
> that `Zero` instance and the standard chart, isolated so they can be shared by the full module
> structure (`Space/Module.lean`) and the Euclidean action (`Space/EuclideanGroup/Action.lean`)
> without those depending on each other.
>
> * `(0 : Space d)` — the coordinate origin, the point all of whose coordinates vanish.
> * `Space.chartEuclidean` — the standard affine isometry `Space d ≃ᵃⁱ[ℝ] EuclideanSpace ℝ (Fin d)`,
>   `p ↦ p -ᵥ 0`, identifying a point with its coordinate vector relative to the origin.

**An instance with no name**, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L27).

```lean
instance {d} : Zero (Space d)
```

**`Space.zero_val`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L31).

```lean
lemma zero_val {d : ℕ} : (0 : Space d).val = fun _ => 0
```

**`Space.zero_apply`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L34).

```lean
lemma zero_apply {d : ℕ} (i : Fin d) :
    (0 : Space d) i = 0
```

**`Space.vectorToSpace`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L39).

> A Euclidean vector, based at the chosen origin, viewed as a point of `Space d`.

```lean
noncomputable def vectorToSpace {d : ℕ} (v : EuclideanSpace ℝ (Fin d)) : Space d
```

**`Space.vectorToSpace_apply`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L43).

```lean
lemma vectorToSpace_apply {d : ℕ} (v : EuclideanSpace ℝ (Fin d)) (i : Fin d) :
    vectorToSpace v i = v i
```

**`Space.vectorToSpace_vsub_zero`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L48).

```lean
lemma vectorToSpace_vsub_zero {d : ℕ} (v : EuclideanSpace ℝ (Fin d)) :
    vectorToSpace v -ᵥ (0 : Space d) = v
```

**`Space.chartEuclidean`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L55).

> The standard chart `Space d ≃ᵃⁱ[ℝ] EuclideanSpace ℝ (Fin d)`, `p ↦ p -ᵥ 0`, identifying a point
> with its coordinate vector relative to the origin (the vector-space zero `(0 : Space d)`).

```lean
noncomputable def chartEuclidean (d : ℕ) :
    Space d ≃ᵃⁱ[ℝ] EuclideanSpace ℝ (Fin d)
```

**`Space.chartEuclidean_apply`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean#L59).

```lean
lemma chartEuclidean_apply (d : ℕ) (p : Space d) :
    chartEuclidean d p = p -ᵥ (0 : Space d)
```

## Depends on

- [Space](basic.md)

## Sources

- [Physlib/SpaceAndTime/Space/Origin.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Origin.lean)
