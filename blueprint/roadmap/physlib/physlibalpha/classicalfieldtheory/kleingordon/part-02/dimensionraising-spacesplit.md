---
declaration: module
origin: cited
lean: KleinGordon.transportSource, KleinGordon.transportSource_apply, KleinGordon.slice_transportSource, KleinGordon.solution_transportSource, KleinGordon.spaceSplit, KleinGordon.hasDerivAt_solution_radial_space, KleinGordon.hasDerivAt_sineEvolution_radial_space, KleinGordon.hasDerivAt_retardedResponse_radial
statement: formalized
proof: formalized
---

# Splitting off two space dimensions

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.DimensionRaising.SpaceSplit`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean): 10 declarations, 8 with a docstring.

> `Space (d + 2)` is isometric to the Euclidean product of `Space d` and the plane.

## i. Overview

> Dimension raising compares the sine evolution in `d + 2` space dimensions with the one in `d`
> dimensions. The statements `hasDerivAt_sineEvolution_radial` and `hasDerivAt_solution_radial` live
> on the Euclidean product `WithLp 2 (E × EuclideanSpace ℝ (Fin 2))`. This file transports them to
> `Space (d + 2)` along a linear isometry.

## ii. Key results

> - `spaceSplit` : the isometry `Space (d + 2) ≃ₗᵢ WithLp 2 (Space d × EuclideanSpace ℝ (Fin 2))`.
> - `solution_transportSource` : the retarded solution commutes with isometries of space.
> - `hasDerivAt_sineEvolution_radial_space` : dimension raising on the slices of `Space (d + 2)`.
> - `hasDerivAt_solution_radial_space` : dimension raising on `Space (d + 2)`.
> - `hasDerivAt_retardedResponse_radial` : dimension raising for the retarded response on spacetime.
> - `spaceThree` : `Space 3` is isometric to the Euclidean three-space.

## iv. References

> None.

## A. The isometry

> - `spaceSplit` : the isometry `Space (d + 2) ≃ₗᵢ WithLp 2 (Space d × EuclideanSpace ℝ (Fin 2))`.
> - `transportSource` : a source pulled back along an isometry of space.
> - `solution_transportSource` : the retarded solution commutes with isometries of space.

## B. Dimension raising

> - `hasDerivAt_sineEvolution_radial_space` : dimension raising on the slices of `Space (d + 2)`.
> - `hasDerivAt_solution_radial_space` : dimension raising on `Space (d + 2)`.
> - `hasDerivAt_retardedResponse_radial` : dimension raising for the retarded response on spacetime.

## C. Three space dimensions

> - `Eucl3` : the Euclidean three-space as a product of the line and the plane.
> - `spaceThree` : `Space 3` is isometric to the Euclidean three-space.

**`KleinGordon.transportSource`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L76).

> A source on time and `W` pulled back along an isometry `V ≃ W` of space.

```lean
def transportSource (A : V ≃ₗᵢ[ℝ] W) :
    𝓓((⊤ : Opens (ℝ × W)), ℂ) →L[ℝ] 𝓓((⊤ : Opens (ℝ × V)), ℂ)
```

**`KleinGordon.transportSource_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L83).

```lean
lemma transportSource_apply (A : V ≃ₗᵢ[ℝ] W) (ψ : 𝓓((⊤ : Opens (ℝ × W)), ℂ)) (s : ℝ) (x : V) :
    transportSource A ψ (s, x) = ψ (s, A x)
```

**`KleinGordon.slice_transportSource`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L88).

```lean
lemma slice_transportSource (A : V ≃ₗᵢ[ℝ] W) (ψ : 𝓓((⊤ : Opens (ℝ × W)), ℂ)) (s : ℝ) :
    slice ℂ (transportSource A ψ) s =
      SchwartzMap.compCLMOfContinuousLinearEquiv ℂ A.toContinuousLinearEquiv (slice ℂ ψ s)
```

**`KleinGordon.solution_transportSource`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L93).

> **The retarded solution commutes with isometries of space.**

```lean
lemma solution_transportSource {μ : ℝ} (hμ : 0 ≤ μ) (A : V ≃ₗᵢ[ℝ] W)
    (ψ : 𝓓((⊤ : Opens (ℝ × W)), ℂ)) (t : ℝ) (x : V) :
    solution ℂ (transportSource A ψ) μ t x = solution ℂ ψ μ t (A x)
```

**`KleinGordon.spaceSplit`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L104).

> `Space (d + 2)` is isometric to the Euclidean product of `Space d` and the plane.

```lean
def spaceSplit (d : ℕ) :
    Space (d + 2) ≃ₗᵢ[ℝ] WithLp 2 (Space d × EuclideanSpace ℝ (Fin 2))
```

**`KleinGordon.hasDerivAt_solution_radial_space`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L116).

> **Dimension raising on `Space (d + 2)`.** Let `ψ'` be a source on time and `Space (d + 2)` that
> is radial in space at each time and let `ψb` be its integral over the plane. The massive retarded
> solution of `ψb` along a ray in `Space d` has the derivative `-(2π ρ)` times the retarded
> solution of `ψ'` at distance `ρ`. This is `G_{d+2} = -(1 / (2π r)) ∂ᵣ G_d`.

```lean
lemma hasDerivAt_solution_radial_space {μ : ℝ} (hμ : 0 ≤ μ) (d : ℕ)
    (ψ' : 𝓓((⊤ : Opens (ℝ × Space (d + 2))), ℂ)) (ψb : 𝓓((⊤ : Opens (ℝ × Space d)), ℂ))
    (hrad : ∀ s, Function.IsRadial (slice ℂ ψ' s))
    (hψb : ∀ s x, ψb (s, x) = ∫ y : EuclideanSpace ℝ (Fin 2),
      ψ' (s, (spaceSplit d).symm (WithLp.toLp 2 (x, y))))
    {e : Space d} (he : ‖e‖ = 1) (t : ℝ) {ρ : ℝ} (hρ : 0 < ρ) :
    HasDerivAt (fun τ : ℝ => solution ℂ ψb μ t (τ • e))
      (-(2 * Real.pi * ρ : ℝ) •
        solution ℂ ψ' μ t ((spaceSplit d).symm (WithLp.toLp 2 (ρ • e, 0)))) ρ
```

**`KleinGordon.hasDerivAt_sineEvolution_radial_space`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L135).

> **Dimension raising on the slices of `Space (d + 2)`.**

```lean
lemma hasDerivAt_sineEvolution_radial_space {μ : ℝ} (hμ : 0 ≤ μ) (d : ℕ) (r : ℝ)
    (g' : 𝓢(Space (d + 2), ℂ)) (hrad : Function.IsRadial g') (gb : 𝓢(Space d, ℂ))
    (hgb : ∀ x, gb x = ∫ y : EuclideanSpace ℝ (Fin 2),
      g' ((spaceSplit d).symm (WithLp.toLp 2 (x, y))))
    {e : Space d} (he : ‖e‖ = 1) {ρ : ℝ} (hρ : 0 < ρ) :
    HasDerivAt (fun t : ℝ => sineEvolution ℂ r μ gb (t • e))
      (-(2 * Real.pi * ρ : ℝ) •
        sineEvolution ℂ r μ g' ((spaceSplit d).symm (WithLp.toLp 2 (ρ • e, 0)))) ρ
```

**`KleinGordon.hasDerivAt_retardedResponse_radial`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L154).

> **Dimension raising for the retarded response on spacetime.** The sources are transported to
> time and space by `sourceEquiv`.

```lean
lemma hasDerivAt_retardedResponse_radial {μ : ℝ} (hμ : 0 ≤ μ) (d : ℕ)
    (f' : 𝓓((⊤ : Opens (SpaceTime (d + 2))), ℂ)) (f : 𝓓((⊤ : Opens (SpaceTime d)), ℂ))
    (hrad : ∀ s, Function.IsRadial (slice ℂ (sourceEquiv ℂ f') s))
    (hmarg : ∀ s x, sourceEquiv ℂ f (s, x) = ∫ y : EuclideanSpace ℝ (Fin 2),
      sourceEquiv ℂ f' (s, (spaceSplit d).symm (WithLp.toLp 2 (x, y))))
    {e : Space d} (he : ‖e‖ = 1) (t : ℝ) {ρ : ℝ} (hρ : 0 < ρ) :
    HasDerivAt (fun τ : ℝ => retardedResponse ℂ μ f ((coordinates d).symm (t, τ • e)))
      (-(2 * Real.pi * ρ : ℝ) • retardedResponse ℂ μ f'
        ((coordinates (d + 2)).symm (t, (spaceSplit d).symm (WithLp.toLp 2 (ρ • e, 0))))) ρ
```

**`KleinGordon.Eucl3`**, an abbrev, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L167).

> The Euclidean three-space.

```lean
abbrev Eucl3 : Type
```

**`KleinGordon.spaceThree`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean#L170).

> `Space 3` is isometric to the Euclidean three-space.

```lean
def spaceThree : Space 3 ≃ₗᵢ[ℝ] Eucl3
```

## Depends on

- [Green operators on spacetime](../part-01/greenoperators.md)

## Proof depends on

- [Dimension raising for the retarded solution](dimensionraising-retarded.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/SpaceSplit.lean)
