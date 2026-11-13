---
declaration: module
origin: cited
lean: Space.line, Space.line_eq_smul_basis, Space.line_injective, Space.line_continuous, Space.line_measurableEmbedding, Space.norm_line, Space.lineMeasure, Space.lineMeasure_hasTemperateGrowth
statement: formalized
proof: formalized
---

# Line surfaces in `Space d`

The module `PhyslibAlpha.SpaceAndTime.Space.Surfaces.Line`, [PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean): 16 declarations, 4 with a docstring.

> The coordinate line in `Space d` with its measure, distribution and vanishing ambient volume.

## i. Overview

> The line surface is the coordinate line in `Space d`, the image of `ℝ` under the embedding
> `line d`. Pushing forward the volume on `ℝ` gives the measure `lineMeasure d`, and integrating
> against it gives the distribution `lineDist d`, roughly the integral of a test function against a
> density concentrated on a line. For `2 ≤ d` the line lies in a proper linear subspace, so it has
> ambient volume zero.

## ii. Key results

> - `line` : the coordinate line embedded in `Space d`.
> - `lineMeasure` : the measure corresponding to integration along the line.
> - `lineDist` : the distribution corresponding to integration along the line.
> - `lineSubmodule` : the linear subspace spanned by the line.
> - `volume_line_range` : for `2 ≤ d` the line has ambient volume zero.

## iv. References

> * None.

## A. The definition of the line surface

**`Space.line`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L60).

> The coordinate line embedded in `Space d`.

```lean
def line (d : ℕ) [NeZero d] : ℝ → Space d
```

**`Space.line_eq_smul_basis`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L63).

```lean
lemma line_eq_smul_basis (d : ℕ) [NeZero d] :
    line d = fun r => r • basis (0 : Fin d)
```

**`Space.line_injective`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L66).

```lean
lemma line_injective (d : ℕ) [NeZero d] : Function.Injective (line d)
```

**`Space.line_continuous`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L72).

```lean
lemma line_continuous (d : ℕ) [NeZero d] : Continuous (line d)
```

**`Space.line_measurableEmbedding`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L76).

```lean
lemma line_measurableEmbedding (d : ℕ) [NeZero d] : MeasurableEmbedding (line d)
```

**`Space.norm_line`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L80).

```lean
lemma norm_line (d : ℕ) [NeZero d] (r : ℝ) : ‖line d r‖ = ‖r‖
```

## B. The measure associated with the line

**`Space.lineMeasure`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L91).

> The measure on `Space d` corresponding to integration along a coordinate line.

```lean
def lineMeasure (d : ℕ) [NeZero d] : Measure (Space d)
```

**`Space.lineMeasure_hasTemperateGrowth`**, an instance, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L94).

```lean
instance lineMeasure_hasTemperateGrowth (d : ℕ) [NeZero d] :
    (lineMeasure d).HasTemperateGrowth
```

## C. The distribution associated with the line

**`Space.lineDist`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L115).

> The distribution on `Space d` corresponding to integration along a coordinate line.
> One can roughly think of this distribution as taking a test function `f` to its integral against
> a mass, charge or current density concentrated on a line.

```lean
def lineDist (d : ℕ) [NeZero d] : (Space d) →d[ℝ] ℝ
```

**`Space.lineDist_apply_eq_integral_lineMeasure`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L118).

```lean
lemma lineDist_apply_eq_integral_lineMeasure (d : ℕ) [NeZero d] (f : 𝓢(Space d, ℝ)) :
    lineDist d f = ∫ x, f x ∂lineMeasure d
```

**`Space.lineDist_apply_eq_integral_volume`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L122).

```lean
lemma lineDist_apply_eq_integral_volume (d : ℕ) [NeZero d] (f : 𝓢(Space d, ℝ)) :
    lineDist d f = ∫ r : ℝ, f (line d r)
```

## D. The line has ambient volume zero

**`Space.lineSubmodule`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L134).

> The linear subspace spanned by the coordinate line in `Space d`.

```lean
def lineSubmodule (d : ℕ) [NeZero d] : Submodule ℝ (Space d)
```

**`Space.line_mem_lineSubmodule`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L137).

```lean
lemma line_mem_lineSubmodule (d : ℕ) [NeZero d] (r : ℝ) : line d r ∈ lineSubmodule d
```

**`Space.range_line_subset_lineSubmodule`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L141).

```lean
lemma range_line_subset_lineSubmodule (d : ℕ) [NeZero d] :
    Set.range (line d) ⊆ (lineSubmodule d : Set (Space d))
```

**`Space.lineSubmodule_ne_top`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L146).

```lean
lemma lineSubmodule_ne_top (d : ℕ) [NeZero d] (hd : 2 ≤ d) : lineSubmodule d ≠ ⊤
```

**`Space.volume_line_range`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean#L156).

```lean
lemma volume_line_range (d : ℕ) [NeZero d] (hd : 2 ≤ d) :
    volume (Set.range (line d) : Set (Space d)) = 0
```

## Depends on

- [Distributions](../../../physlib/mathematics/distribution/tempereddistribution.md)
- [The structure of a module on Space](../../../physlib/spaceandtime/space/part-01/module.md)

## Proof depends on

- [Integrals in Space](../../../physlib/spaceandtime/space/part-02/integrals-basic.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/Line.lean)
