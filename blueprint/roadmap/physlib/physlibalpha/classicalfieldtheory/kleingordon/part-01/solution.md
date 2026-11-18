---
declaration: module
origin: cited
lean: KleinGordon.Solution.retarded, KleinGordon.Solution.advanced, KleinGordon.Solution.retarded_solves, KleinGordon.Solution.advanced_solves, KleinGordon.Solution.retarded_support, KleinGordon.Solution.advanced_support, KleinGordon.Solution.retarded_formula, KleinGordon.Solution.advanced_formula
statement: formalized
proof: formalized
---

# Klein–Gordon fields and causal propagation

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Solution`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean): 32 declarations (1 instance with no name), 32 with a docstring.

> A disturbance of a relativistic field spreads inside the light cone. This file states how the
> Klein–Gordon equation describes this, for massless and massive fields in every spatial dimension.

## i. Overview

> Time and space are measured in units with the speed of light equal to one. For a source `f` of
> compact support the file solves `(∂ₜ² - Δ + m²) u = f` on `SpaceTime d`. The mass parameter `m`
> is any real number. The source and the solution are smooth fields with values in a normed space.
> Sources may also be distributions of compact support.
>
> The retarded solution is supported in the causal future of the source. The advanced solution is
> supported in the causal past. Their difference is the causal propagator. It solves the equation
> without source. Every homogeneous solution with spacelike compact support arises this way.

## ii. Key results

> - `existsUnique_retarded` : a compact source has exactly one solution with support in the causal
>   future of the source.
> - `exact_sequence` : compact sources, the equation of motion and the causal propagator form an
>   exact sequence.
> - `solutionsEquivQuotient` : spacelike compact solutions are the compact sources modulo the
>   equation of motion.
> - `retardedDistribution_unique` : the same uniqueness for distributional sources.
> - `pointSource_solves` and `pointSource_reciprocity` : the point source solves the equation with a
>   delta source, and the retarded kernel seen from `p` is the advanced solution at `p`.

## iv. References

> None.

## A. The problem

> Given a source `f` of compact support, find a field `u` with `(∂ₜ² - Δ + m²) u = f`. The operator
> is `operator m`. A source is a smooth field of compact support, `TestField d F`. A distributional
> source is a compactly supported distribution, `compactDistributions`. A solution is a smooth
> field, `smoothFields d F`, or a distribution, `DistributionField d V`.

## B. The Fourier picture

> Transform in space. Put `f̂(s, ξ) = ∫ e^(-2πi x·ξ) f(s, x) dx` and `ω(ξ) = √(4π²‖ξ‖² + m²)`.
> Each Fourier mode obeys the forced oscillator equation `û'' + ω² û = f̂`. Its solutions use the
> kernel `sin(ω r) / ω`. This is `sincPropagator ω`. It equals `r` at `ω = 0`.
>
> * The retarded solution is `û(t, ξ) = ∫_{s ≤ t} sin(ω (t - s)) / ω · f̂(s, ξ) ds`.
>   Every cause comes before its effect.
> * The advanced solution is `û(t, ξ) = ∫_{s ≥ t} sin(ω (s - t)) / ω · f̂(s, ξ) ds`.
>   Every effect comes before its cause.
> * The difference is the causal propagator `E`. It is
>   `û(t, ξ) = ∫ sin(ω (t - s)) / ω · f̂(s, ξ) ds` over all times.

## C. Smooth sources

> The results `retarded_solves`, `retarded_support` and `retarded_formula` describe the retarded
> solution. The same results hold for the advanced solution. The causal propagator `E` solves the
> equation without source and is supported in the causal future and past of the source. The sequence
> `0 → D → D → Sol → 0` is exact. `D` is the space of compact sources. The first map is the
> operator. The second map is `E`. `Sol` is the space of homogeneous solutions with spacelike
> compact support.

## D. Distributional sources

> Compactly supported distributions have retarded and advanced solutions with the same properties.
> The point source at `p` is the retarded solution of a delta distribution. Reciprocity holds. The
> retarded kernel seen from `p` and tested on `φ` is the advanced solution of `φ` at `p`.

## E. Tempered slices

> At each time the solution is a tempered distribution in space. `fourier_sineEvolution` gives its
> Fourier transform. `retarded_slice_pairing` gives its pairing with Schwartz functions.

## F. Not proved here

> The Fourier transform in time and space, the convolution form `u = K * f` and closed expressions
> for the kernel `K` in a given dimension are not proved here.

**`KleinGordon.Solution.retarded`**, an abbrev, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L115).

> The retarded solution of `operator m u = f`.

```lean
abbrev retarded : TestField d F →ₗ[ℝ] smoothFields d F
```

**`KleinGordon.Solution.advanced`**, an abbrev, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L118).

> The advanced solution of `operator m u = f`.

```lean
abbrev advanced : TestField d F →ₗ[ℝ] smoothFields d F
```

**An instance with no name**, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L123).

> Smooth fields form an additive group, needed to form the quotient.

```lean
local instance : AddCommGroup (smoothFields d F)
```

**`KleinGordon.Solution.retarded_solves`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L126).

> The retarded solution solves the equation.

```lean
lemma retarded_solves (f : TestField d F) : operator m (retarded F m f) = f
```

**`KleinGordon.Solution.advanced_solves`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L130).

> The advanced solution solves the equation.

```lean
lemma advanced_solves (f : TestField d F) : operator m (advanced F m f) = f
```

**`KleinGordon.Solution.retarded_support`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L134).

> The retarded solution vanishes outside the causal future of the source.

```lean
lemma retarded_support (f : TestField d F) :
    tsupport (retarded F m f : SpaceTime d → F) ⊆
      (causalRelation d).causalFuture (tsupport (f : SpaceTime d → F))
```

**`KleinGordon.Solution.advanced_support`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L140).

> The advanced solution vanishes outside the causal past of the source.

```lean
lemma advanced_support (f : TestField d F) :
    tsupport (advanced F m f : SpaceTime d → F) ⊆
      (causalRelation d).causalPast (tsupport (f : SpaceTime d → F))
```

**`KleinGordon.Solution.retarded_formula`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L147).

> The retarded solution in time and space coordinates. At time `t` and position `x` it adds
> the sine evolution of the source slice at every earlier time `s`.

```lean
lemma retarded_formula (f : TestField d F) (p : SpaceTime d) :
    (retarded F m f : SpaceTime d → F) p = ∫ s in Set.Iic (coordinates d p).1,
      sineEvolution F ((coordinates d p).1 - s) (m ^ 2)
        (slice F (sourceEquiv F (testFieldEquiv F f)) s) (coordinates d p).2
```

**`KleinGordon.Solution.advanced_formula`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L155).

> The advanced solution in time and space coordinates. It adds the sine evolution of the
> source slice at every later time.

```lean
lemma advanced_formula (f : TestField d F) (p : SpaceTime d) :
    (advanced F m f : SpaceTime d → F) p = ∫ s in Set.Ioi (coordinates d p).1,
      sineEvolution F (s - (coordinates d p).1) (m ^ 2)
        (slice F (sourceEquiv F (testFieldEquiv F f)) s) (coordinates d p).2
```

**`KleinGordon.Solution.propagator`**, an abbrev, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L163).

> The causal propagator `E`: the retarded minus the advanced solution.

```lean
abbrev propagator : TestField d F →ₗ[ℝ] smoothFields d F
```

**`KleinGordon.Solution.propagator_eq`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L166).

> The causal propagator is the retarded minus the advanced solution.

```lean
lemma propagator_eq (f : TestField d F) :
    propagator F m f = retarded F m f - advanced F m f
```

**`KleinGordon.Solution.propagator_solves`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L170).

> The causal propagator solves the equation without source.

```lean
lemma propagator_solves (f : TestField d F) : operator m (propagator F m f) = 0
```

**`KleinGordon.Solution.propagator_support`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L174).

> The causal propagator is supported in the causal future and past of the source.

```lean
lemma propagator_support (f : TestField d F) :
    tsupport (propagator F m f : SpaceTime d → F) ⊆
      (causalRelation d).causalHull (tsupport (f : SpaceTime d → F))
```

**`KleinGordon.Solution.propagator_operator`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L180).

> The causal propagator kills every source that is an equation of motion.

```lean
lemma propagator_operator (f : TestField d F) :
    propagator F m (compactOperator (equation m) f) = 0
```

**`KleinGordon.Solution.existsUnique_retarded`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L185).

> A source has exactly one solution with support in the causal future of the source.

```lean
lemma existsUnique_retarded (f : TestField d F) :
    ∃! u : smoothFields d F, operator m u = f ∧
      tsupport (u : SpaceTime d → F) ⊆
        (causalRelation d).causalFuture (tsupport (f : SpaceTime d → F))
```

**`KleinGordon.Solution.exact_sequence`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L193).

> Compact sources, the equation of motion and the retarded minus advanced solution form an
> exact sequence ending in the spacelike compact fields.

```lean
lemma exact_sequence :
    let P := equation (d := d) (V := F) m
    Function.Injective P.compactOperator ∧
      Function.Exact P.compactOperator (greenOperators F m).toSpacelikeCompact ∧
      Function.Exact (greenOperators F m).toSpacelikeCompact
        (P.spacelikeCompactOperator (causalRelation d)) ∧
      Function.Surjective (P.spacelikeCompactOperator (causalRelation d))
```

**`KleinGordon.Solution.solutionsEquivQuotient`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L203).

> Spacelike compact solutions are the compact sources modulo the equation of motion.

```lean
def solutionsEquivQuotient :
    let P := equation (d := d) (V := F) m
    P.spacelikeCompactSolution (causalRelation d) ≃ₗ[ℝ]
      (P.compactSources ⧸ LinearMap.range P.compactOperator)
```

**`KleinGordon.Solution.retardedDistribution`**, an abbrev, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L216).

> The retarded solution for a compactly supported distribution.

```lean
abbrev retardedDistribution (T : compactDistributions (SpaceTime d) V) : DistributionField d V
```

**`KleinGordon.Solution.advancedDistribution`**, an abbrev, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L220).

> The advanced solution for a compactly supported distribution.

```lean
abbrev advancedDistribution (T : compactDistributions (SpaceTime d) V) : DistributionField d V
```

**`KleinGordon.Solution.retardedDistribution_solves`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L226).

> The retarded solution of a distribution solves the equation.

```lean
lemma retardedDistribution_solves (T : compactDistributions (SpaceTime d) V) :
    distributionOperator m (retardedDistribution m T) = T
```

**`KleinGordon.Solution.advancedDistribution_solves`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L231).

> The advanced solution of a distribution solves the equation.

```lean
lemma advancedDistribution_solves (T : compactDistributions (SpaceTime d) V) :
    distributionOperator m (advancedDistribution m T) = T
```

**`KleinGordon.Solution.retardedDistribution_support`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L236).

> The retarded solution vanishes outside the causal future of the support of the source.

```lean
lemma retardedDistribution_support (T : compactDistributions (SpaceTime d) V) :
    IsVanishingOn (retardedDistribution m T)
      ((causalRelation d).causalFuture (compactDistributionBound T))ᶜ
```

**`KleinGordon.Solution.advancedDistribution_support`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L242).

> The advanced solution vanishes outside the causal past of the support of the source.

```lean
lemma advancedDistribution_support (T : compactDistributions (SpaceTime d) V) :
    IsVanishingOn (advancedDistribution m T)
      ((causalRelation d).causalPast (compactDistributionBound T))ᶜ
```

**`KleinGordon.Solution.retardedDistribution_unique`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L249).

> A distribution solution supported in the causal future of a compact set is the retarded
> solution.

```lean
lemma retardedDistribution_unique (T : compactDistributions (SpaceTime d) V)
    (u : DistributionField d V) {K : Set (SpaceTime d)} (hK : IsCompact K)
    (hu : IsVanishingOn u ((causalRelation d).causalFuture K)ᶜ)
    (hT : distributionOperator m u = T) : u = retardedDistribution m T
```

**`KleinGordon.Solution.retardedDistribution_inverse`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L256).

> Solving and then applying the operator returns the source.

```lean
lemma retardedDistribution_inverse (T : compactDistributions (SpaceTime d) V) :
    retardedDistribution m (compactDistributionOperator m T) = T
```

**`KleinGordon.Solution.pointSource`**, an abbrev, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L261).

> The point source at `p`: the retarded solution of a delta distribution.

```lean
abbrev pointSource (p : SpaceTime d)
```

**`KleinGordon.Solution.pointSource_solves`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L264).

> The point source solves the equation with the delta distribution at `p` as source.

```lean
lemma pointSource_solves (p : SpaceTime d) :
    distributionOperator m (pointSource (m := m) p) = Distribution.delta p
```

**`KleinGordon.Solution.pointSource_support`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L269).

> The point source vanishes outside the causal future of `p`.

```lean
lemma pointSource_support (p : SpaceTime d) :
    IsVanishingOn (pointSource (m := m) p) ((causalRelation d).causalFuture {p})ᶜ
```

**`KleinGordon.Solution.pointSource_reciprocity`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L275).

> Reciprocity. The retarded kernel seen from `p` and tested on `f` is the advanced solution for
> `f`, evaluated at `p`.

```lean
lemma pointSource_reciprocity (p : SpaceTime d) (f : TestField d ℝ) :
    pointSource (m := m) p (testFieldEquiv ℝ f) =
      ((realAdvancedGreenOperator m).toLinearMap f : SpaceTime d → ℝ) p
```

**`KleinGordon.Solution.pointSource_apply`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L282).

> The point source at `p` applied to a test function `φ`. It integrates the sine evolution of
> the delta distribution at the position of `p` against the slices of `φ` over later times.

```lean
lemma pointSource_apply (p : SpaceTime d) (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    pointSource (m := m) p φ =
      (∫ s in Set.Ioi (coordinates d p).1,
        KleinGordon.sineEvolutionTempered ℂ (s - (coordinates d p).1) (m ^ 2)
          (TemperedDistribution.delta (coordinates d p).2)
          (slice ℂ (sourceEquiv ℂ (_root_.TestFunction.postcompCLM Complex.ofRealCLM φ)) s)).re
```

**`KleinGordon.Solution.fourier_sineEvolution`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L299).

> In Fourier space the sine evolution multiplies by `sin(ω r) / ω`.

```lean
lemma fourier_sineEvolution {μ : ℝ} (hμ : 0 ≤ μ) (r : ℝ) (g : 𝓢(E, F)) (ξ : E) :
    𝓕 (sineEvolution F r μ g) ξ = (Real.sincPropagator r (dispersion μ ξ) : ℂ) • 𝓕 g ξ
```

**`KleinGordon.Solution.retarded_slice_pairing`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean#L308).

> At time `t` the retarded solution is a tempered distribution in space. Tested against a
> Schwartz function it is the integral over earlier times `s` of the sine evolution of the source
> slice at time `s`.

```lean
lemma retarded_slice_pairing {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (g : 𝓢(E, ℂ)) :
    (solutionSlice F f hμ t : 𝓢'(E, F)) g =
      ∫ s in Set.Iic t, sineEvolutionTempered F (t - s) μ (slice F f s : 𝓢'(E, F)) g
```

## Depends on

- [Distributional sources](distributionsources.md)
- [The solution as a tempered distribution in space](temperedslice.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Solution.lean)
