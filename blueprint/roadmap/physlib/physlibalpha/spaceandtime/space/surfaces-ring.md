---
declaration: module
origin: cited
lean: Space.ring, Space.ring_eq, Space.ring_injective, Space.ring_continuous, Space.ring_measurableEmbedding, Space.ringMeasure, Space.ringMeasure_hasTemperateGrowth, Space.ringMeasure_prod_volume_hasTemperateGrowth
statement: formalized
proof: formalized
---

# Ring surface in `Space 3`

The module `PhyslibAlpha.SpaceAndTime.Space.Surfaces.Ring`, [PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean): 17 declarations, 3 with a docstring.

> The unit ring in `Space 3` with its measure and the distribution of integration around it.

## i. Overview

> The ring surface is the unit circle `S¹` of `Space 2`, embedded into `Space 3` by `ring`. Pushing
> forward the measure on the sphere gives the finite measure `ringMeasure`, of total mass `2π`, and
> integrating against it gives the distribution `ringDist`. The file also gives integrability
> criteria for continuous functions and the invariance of `ringMeasure.prod volume` under a shear.

## ii. Key results

> - `ring` : the embedding of the unit circle into `Space 3`.
> - `ringMeasure` : the measure corresponding to integration around the ring.
> - `ringMeasure_univ` : the total mass of the ring measure is `2π`.
> - `integrable_ringMeasure_of_continuous` : continuous functions on the ring are integrable.
> - `ringDist` : the distribution corresponding to integration around the ring.
> - `ringDist_eq_integral_delta` : `ringDist` as an integral of Dirac deltas over the ring.

## iv. References

> * None.

## A. The definition of the ring surface

**`Space.ring`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L60).

> The embedding of the unit ring (a circle `S¹` in `Space 2`) into `Space 3`.

```lean
def ring : Metric.sphere (0 : Space 2) 1 → Space 3
```

**`Space.ring_eq`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L63).

```lean
lemma ring_eq : ring = (slice 2).symm ∘ (fun x => (0, sphericalShell 2 x))
```

**`Space.ring_injective`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L65).

```lean
lemma ring_injective : Function.Injective ring
```

**`Space.ring_continuous`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L71).

```lean
lemma ring_continuous : Continuous ring
```

**`Space.ring_measurableEmbedding`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L76).

```lean
lemma ring_measurableEmbedding : MeasurableEmbedding ring
```

## B. The measure associated with the ring

**`Space.ringMeasure`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L87).

> The measure on `Space 3` corresponding to integration around a ring.

```lean
def ringMeasure : Measure (Space 3)
```

**`Space.ringMeasure_hasTemperateGrowth`**, an instance, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L90).

```lean
instance ringMeasure_hasTemperateGrowth :
    ringMeasure.HasTemperateGrowth
```

**`Space.ringMeasure_prod_volume_hasTemperateGrowth`**, an instance, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L97).

```lean
instance ringMeasure_prod_volume_hasTemperateGrowth :
    (ringMeasure.prod (volume (α := Space))).HasTemperateGrowth
```

**`Space.ringMeasure_sFinite`**, an instance, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L101).

```lean
instance ringMeasure_sFinite: SFinite ringMeasure
```

**`Space.ringMeasure_finite`**, an instance, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L105).

```lean
instance ringMeasure_finite: IsFiniteMeasure ringMeasure
```

**`Space.integrable_ringMeasure_of_continuous`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L109).

```lean
lemma integrable_ringMeasure_of_continuous (f : Space → ℝ) (hf : Continuous (f ∘ ring)) :
    Integrable f ringMeasure
```

**`Space.integrable_ringMeasure_of_continuous_euclid`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L118).

```lean
lemma integrable_ringMeasure_of_continuous_euclid (f : Space → EuclideanSpace ℝ (Fin n))
    (hf : Continuous (f ∘ ring)) :
    Integrable f ringMeasure
```

**`Space.ringMeasure_prod_volume_map`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L127).

```lean
lemma ringMeasure_prod_volume_map :
    (ringMeasure.prod (volume (α := Space))).map (fun x : Space × Space => (x.1, x.2 + x.1))
     = (ringMeasure.prod (volume (α := Space)))
```

**`Space.ringMeasure_univ`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L138).

```lean
lemma ringMeasure_univ : ringMeasure Set.univ = ENNReal.ofReal ((2 : ℝ) * π)
```

## C. The distribution associated with the ring

**`Space.ringDist`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L153).

> The distribution on `Space 3` corresponding to integration around a ring.

```lean
def ringDist : (Space 3) →d[ℝ] ℝ
```

**`Space.ringDist_apply_eq_integral_ringMeasure`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L156).

```lean
lemma ringDist_apply_eq_integral_ringMeasure (f : 𝓢(Space 3, ℝ)) :
    ringDist f = ∫ x, f x ∂ringMeasure
```

**`Space.ringDist_eq_integral_delta`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean#L160).

```lean
lemma ringDist_eq_integral_delta (f : 𝓢(Space 3, ℝ)) :
    ringDist f = ∫ z, diracDelta ℝ z f ∂ringMeasure
```

## Depends on

- [Slices of space](../../../physlib/spaceandtime/space/part-01/slice.md)
- [Spherical surfaces on Space](surfaces-sphericalshell.md)

## Proof depends on

- [Functions on `Space d` which can be made into distributions](../../../physlib/spaceandtime/space/part-01/isdistbounded.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Ring.lean)
