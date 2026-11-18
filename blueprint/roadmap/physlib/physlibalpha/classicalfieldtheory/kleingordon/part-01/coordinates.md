---
declaration: module
origin: cited
lean: KleinGordon.Spacetime.coordinates, KleinGordon.Spacetime.sourceEquiv, KleinGordon.Spacetime.tsupport_sourceEquiv, KleinGordon.Spacetime.sourceOperator, KleinGordon.Spacetime.coordinates_time, KleinGordon.Spacetime.coordinates_space, KleinGordon.Spacetime.precedes_iff_coordinates, KleinGordon.Spacetime.causalFuture_coordinates
statement: formalized
proof: formalized
---

# Coordinates of spacetime

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Coordinates`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean): 18 declarations, 8 with a docstring.

> Spacetime is identified with time and space.

## i. Overview

> Spacetime is identified with time and space. The causal relation and the second derivatives are
> transported along the identification.

## ii. Key results

> - `coordinates` : Time and space coordinates in units with speed of light equal to one.
> - `sourceEquiv` : Compact smooth sources transported to time-space coordinates.
> - `sourceOperator` : The transported compact Klein–Gordon operator on Minkowski test sources.
> - `operator_of_coordinates` : The neighbour's Klein–Gordon operator has the Fourier coordinate
>   differential expression.

## iv. References

> None.

## A. The spatial Fourier Green construction on Minkowski spacetime

> - `coordinates` : Time and space coordinates in units with speed of light equal to one.
> - `sourceEquiv` : Compact smooth sources transported to time-space coordinates.
> - `sourceOperator` : The transported compact Klein–Gordon operator on Minkowski test sources.
>
> Lemmas: `tsupport_sourceEquiv`.

## B. Coordinate form of the Minkowski Klein–Gordon operator

> Lemmas: `coordinates_time`, `coordinates_space`, `precedes_iff_coordinates`,
> `causalFuture_coordinates`, `causalPast_coordinates`, `coordinates_basis_time`,
> `coordinates_basis_space`, `second_spacetime_deriv`, `second_spacetime_deriv_coordinates`,
> `second_time_slice` and more.

**`KleinGordon.Spacetime.coordinates`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L70).

> Time and space coordinates in units with speed of light equal to one.

```lean
def coordinates (d : ℕ) : SpaceTime d ≃L[ℝ] ℝ × Space d
```

**`KleinGordon.Spacetime.sourceEquiv`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L75).

> Compact smooth sources transported to time-space coordinates.

```lean
def sourceEquiv : 𝓓((⊤ : Opens (SpaceTime d)), F) ≃ₗ[ℝ]
    𝓓((⊤ : Opens (ℝ × Space d)), F)
```

**`KleinGordon.Spacetime.tsupport_sourceEquiv`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L100).

> Coordinate transport carries the source support to its coordinate image.

```lean
lemma tsupport_sourceEquiv (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    tsupport (sourceEquiv F f) = coordinates d '' tsupport f
```

**`KleinGordon.Spacetime.sourceOperator`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L107).

> The transported compact Klein–Gordon operator on Minkowski test sources.

```lean
def sourceOperator (μ : ℝ) (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) :
    𝓓((⊤ : Opens (SpaceTime d)), F)
```

**`KleinGordon.Spacetime.coordinates_time`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L115).

```lean
lemma coordinates_time (p : SpaceTime d) : (coordinates d p).1 = (p.time 1).val
```

**`KleinGordon.Spacetime.coordinates_space`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L117).

```lean
lemma coordinates_space (p : SpaceTime d) : (coordinates d p).2 = p.space
```

**`KleinGordon.Spacetime.precedes_iff_coordinates`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L120).

> Minkowski causal precedence is exactly the coordinate light-cone inequality.

```lean
lemma precedes_iff_coordinates (p q : SpaceTime d) :
    (causalRelation d).Precedes p q ↔
      ‖(coordinates d q).2 - (coordinates d p).2‖ ≤ (coordinates d q).1 - (coordinates d p).1
```

**`KleinGordon.Spacetime.causalFuture_coordinates`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L127).

```lean
lemma causalFuture_coordinates (K : Set (SpaceTime d)) :
    (coordinates d) ⁻¹' causalFuture (coordinates d '' K) = (causalRelation d).causalFuture K
```

**`KleinGordon.Spacetime.causalPast_coordinates`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L136).

```lean
lemma causalPast_coordinates (K : Set (SpaceTime d)) :
    (coordinates d) ⁻¹' causalPast (coordinates d '' K) = (causalRelation d).causalPast K
```

**`KleinGordon.Spacetime.coordinates_basis_time`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L146).

```lean
lemma coordinates_basis_time :
    coordinates d (Lorentz.Vector.basis (Sum.inl 0)) = (1, (0 : Space d))
```

**`KleinGordon.Spacetime.coordinates_basis_space`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L151).

```lean
lemma coordinates_basis_space (i : Fin d) :
    coordinates d (Lorentz.Vector.basis (Sum.inr i)) = (0, Space.basis i)
```

**`KleinGordon.Spacetime.second_spacetime_deriv`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L156).

```lean
lemma second_spacetime_deriv (h : SpaceTime d → F) (hh : ContDiff ℝ ∞ h)
    (μ : Fin 1 ⊕ Fin d) (p : SpaceTime d) :
    SpaceTime.deriv μ (SpaceTime.deriv μ h) p =
      iteratedFDeriv ℝ 2 h p ![Lorentz.Vector.basis μ, Lorentz.Vector.basis μ]
```

**`KleinGordon.Spacetime.second_spacetime_deriv_coordinates`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L168).

```lean
lemma second_spacetime_deriv_coordinates (g : ℝ × Space d → F) (hg : ContDiff ℝ ∞ g)
    (μ : Fin 1 ⊕ Fin d) (p : SpaceTime d) :
    SpaceTime.deriv μ (SpaceTime.deriv μ (g ∘ coordinates d)) p =
      iteratedFDeriv ℝ 2 g (coordinates d p)
        ![coordinates d (Lorentz.Vector.basis μ), coordinates d (Lorentz.Vector.basis μ)]
```

**`KleinGordon.Spacetime.second_time_slice`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L183).

```lean
lemma second_time_slice (g : ℝ × Space d → F) (hg : ContDiff ℝ ∞ g)
    (t : ℝ) (x : Space d) :
    deriv (deriv (fun s => g (s, x))) t =
      iteratedFDeriv ℝ 2 g (t, x) ![(1, 0), (1, 0)]
```

**`KleinGordon.Spacetime.second_space_slice`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L203).

```lean
lemma second_space_slice (g : ℝ × Space d → F) (hg : ContDiff ℝ ∞ g)
    (t : ℝ) (x b : Space d) :
    iteratedFDeriv ℝ 2 (fun y => g (t, y)) x ![b, b] =
      iteratedFDeriv ℝ 2 g (t, x) ![(0, b), (0, b)]
```

**`KleinGordon.Spacetime.waveTrace_coordinates`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L221).

> The Minkowski metric trace is the time second derivative minus the spatial Laplacian.

```lean
lemma waveTrace_coordinates (g : ℝ × Space d → F) (hg : ContDiff ℝ ∞ g) (p : SpaceTime d) :
    (∑ μ : Fin 1 ⊕ Fin d, (minkowskiMatrix μ μ : ℝ) •
      SpaceTime.deriv μ (SpaceTime.deriv μ (g ∘ coordinates d)) p) =
      deriv (deriv (fun s => g (s, (coordinates d p).2))) (coordinates d p).1 -
        (Δ (fun y => g ((coordinates d p).1, y))) (coordinates d p).2
```

**`KleinGordon.Spacetime.operator_of_coordinates`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L237).

> The neighbour's Klein–Gordon operator has the Fourier coordinate differential expression.

```lean
lemma operator_of_coordinates (m : ℝ) (g : ℝ × Space d → F) (hg : ContDiff ℝ ∞ g)
    (p : SpaceTime d) :
    (operator m
      ⟨g ∘ coordinates d, hg.comp (coordinates d).contDiff⟩ : SpaceTime d → F) p =
      deriv (deriv (fun s => g (s, (coordinates d p).2))) (coordinates d p).1 -
        (Δ (fun y => g ((coordinates d p).1, y))) (coordinates d p).2 +
          m ^ 2 • g (coordinates d p)
```

**`KleinGordon.Spacetime.sourceOperator_eq_operator`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean#L253).

> The transported compact source operator is the existing Minkowski Klein–Gordon operator.

```lean
lemma sourceOperator_eq_operator (m : ℝ)
    (f : 𝓓((⊤ : Opens (SpaceTime d)), F)) (p : SpaceTime d) :
    sourceOperator F (m ^ 2) f p =
      (operator m ⟨f, f.contDiff⟩ : SpaceTime d → F) p
```

## Depends on

- [The Klein–Gordon equation](basic.md)
- [The retarded and advanced solution](retardedsolution.md)
- [Light cones in time and space](../../../relativity/causality/lightcone.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Coordinates.lean)
