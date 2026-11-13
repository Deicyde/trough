---
declaration: module
origin: cited
lean: KleinGordon.radialSource, KleinGordon.radialSource_apply, KleinGordon.integral_tail_sq, KleinGordon.integral_plane_lift, KleinGordon.liftProfile, KleinGordon.deriv_slice_eq, KleinGordon.liftProfile_apply, KleinGordon.radialSource_marginal
statement: formalized
proof: formalized
---

# Smooth radial lifts

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.DimensionRaising.RadialLift`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean): 10 declarations, 6 with a docstring.

> A smooth radial source in `d` space dimensions and its lift to `d + 2` dimensions.

## i. Overview

> A radial test function is a smooth function `P` of the squared norm. Its lift to two more space
> dimensions is `-(1/π) P'` of the squared norm. This is `-(1/(2π ρ)) ∂ρ` of the profile `P(ρ²)`,
> written without the singular factor `1/ρ`. The integral of the lift over the plane is the original
> function.

## ii. Key results

> - `integral_tail_sq` : the tail integral of `u P'(u²)`.
> - `integral_plane_lift` : the integral of the lifted profile over the plane.
> - `radialSource` : the radial source `P(s, ‖x‖²)` as a test function.
> - `liftProfile` : the lift `-(1/π) ∂_q P` of a profile to two more space dimensions.
> - `radialSource_marginal` : the lifted radial source integrates to the original one.
> - `hasDerivAt_solution_radialSource` : dimension raising for a smooth radial source.
> - `transportSource_spaceThree` : a radial source on the Euclidean three-space is radial on
>   `Space 3`.

## iv. References

> None.

## A. The tail integral

> - `integral_tail_sq` : the tail integral of `u P'(u²)`.

## B. The plane integral of the lift

> - `integral_plane_lift` : the integral of the lifted profile over the plane.

## C. Radial sources

> - `radialSource` : the radial source `P(s, ‖x‖²)` as a test function.
> - `liftProfile` : the lift `-(1/π) ∂_q P` of a profile to two more space dimensions.
> - `radialSource_marginal` : the lifted radial source integrates to the original one.

## D. Dimension raising

> - `hasDerivAt_solution_radialSource` : dimension raising for a smooth radial source.
> - `transportSource_spaceThree` : a radial source on the Euclidean three-space is radial on
>   `Space 3`.

**`KleinGordon.radialSource`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L81).

> The radial source `(s, x) ↦ P (s, ‖x‖²)` built from a test function `P` of time and the squared
> radius.

```lean
def radialSource (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) :
    𝓓((⊤ : TopologicalSpace.Opens (ℝ × V)), ℂ)
```

**`KleinGordon.radialSource_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L101).

```lean
lemma radialSource_apply (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (s : ℝ) (x : V) :
    radialSource V P (s, x) = P (s, ‖x‖ ^ 2)
```

**`KleinGordon.integral_tail_sq`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L107).

> The tail integral of `u P'(u²)` is `-P(ρ²) / 2` for a smooth compactly supported profile.

```lean
lemma integral_tail_sq {P : ℝ → ℂ} (hP : ContDiff ℝ ∞ P) (hc : HasCompactSupport P) (ρ : ℝ) :
    ∫ u in Ioi ρ, u • deriv P (u ^ 2) = -(P (ρ ^ 2) / 2)
```

**`KleinGordon.integral_plane_lift`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L152).

> The plane integral of the lift at a given radius: the lifted profile integrates to the
> original profile.

```lean
lemma integral_plane_lift {g : ℝ → ℂ} (hg : ContDiff ℝ ∞ g) (hc : HasCompactSupport g) {ρ : ℝ}
    (hρ : 0 ≤ ρ) :
    ∫ y : EuclideanSpace ℝ (Fin 2), (-(1 / Real.pi : ℝ) : ℝ) • deriv g (ρ ^ 2 + ‖y‖ ^ 2) =
      g (ρ ^ 2)
```

**`KleinGordon.liftProfile`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L199).

> The lift of a profile to two more space dimensions: `-(1/π) ∂_q P`.

```lean
def liftProfile (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) :
    𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)
```

**`KleinGordon.deriv_slice_eq`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L204).

```lean
lemma deriv_slice_eq (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (s q : ℝ) :
    deriv (fun q' : ℝ => P (s, q')) q = lineDeriv ℝ P (s, q) ((0 : ℝ), (1 : ℝ))
```

**`KleinGordon.liftProfile_apply`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L212).

```lean
lemma liftProfile_apply (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (s q : ℝ) :
    liftProfile P (s, q) = (-(1 / Real.pi : ℝ) : ℝ) • deriv (fun q' : ℝ => P (s, q')) q
```

**`KleinGordon.radialSource_marginal`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L228).

> **The lifted radial source integrates to the original one.** The integral over the plane of the
> lift `-(1/π) ∂_q P` is `P`.

```lean
lemma radialSource_marginal (A : WithLp 2 (E × EuclideanSpace ℝ (Fin 2)) ≃ₗᵢ[ℝ] E')
    (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) (s : ℝ) (x : E) :
    radialSource E P (s, x) = ∫ y : EuclideanSpace ℝ (Fin 2),
      radialSource E' (liftProfile P) (s, A (WithLp.toLp 2 (x, y)))
```

**`KleinGordon.hasDerivAt_solution_radialSource`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L250).

> **Dimension raising for a smooth radial source.** The retarded solution in `d + 2` space
> dimensions of the lift `-(1/π) ∂_q P` of the radial source `P(s, ‖x‖²)` is `-(1 / (2π ρ)) ∂ρ` of the
> retarded solution in `d` space dimensions of `P(s, ‖x‖²)`.

```lean
lemma hasDerivAt_solution_radialSource {μ : ℝ} (hμ : 0 ≤ μ) (d : ℕ)
    (P : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) {e : Space d} (he : ‖e‖ = 1) (t : ℝ)
    {ρ : ℝ} (hρ : 0 < ρ) :
    HasDerivAt (fun τ : ℝ => solution ℂ (radialSource (Space d) P) μ t (τ • e))
      (-(2 * Real.pi * ρ : ℝ) • solution ℂ (radialSource (Space (d + 2)) (liftProfile P)) μ t
        ((spaceSplit d).symm (WithLp.toLp 2 (ρ • e, 0)))) ρ
```

**`KleinGordon.transportSource_spaceThree`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean#L263).

```lean
lemma transportSource_spaceThree (Q : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × ℝ)), ℂ)) :
    transportSource spaceThree (radialSource Eucl3 Q) = radialSource (Space 3) Q
```

## Depends on

- [Splitting off two space dimensions](dimensionraising-spacesplit.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/RadialLift.lean)
