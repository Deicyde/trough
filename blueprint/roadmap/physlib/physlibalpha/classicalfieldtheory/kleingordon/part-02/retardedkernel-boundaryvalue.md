---
declaration: module
origin: cited
lean: KleinGordon.dampedKernel, KleinGordon.sineEvolution_zero_eq, KleinGordon.integrable_dampedIntegrand, KleinGordon.dampedKernel_eq, KleinGordon.tendsto_dampedKernel, KleinGordon.dampedKernel_zero_eq, KleinGordon.solution_zero_eq, KleinGordon.resolvent
statement: formalized
proof: formalized
---

# The retarded kernel as a boundary value in the spacetime Fourier variables

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.RetardedKernel.BoundaryValue`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean): 23 declarations, 17 with a docstring.

> The retarded kernel tested against a test function is the limit of an integral of the spacetime
> Fourier transform against `1 / (ω_ξ² - (2π w + i ε)²)`.

## i. Overview

> Time and space are Fourier transformed in this order. The spatial transform of a slice is a
> smooth compactly supported function of the time. Fourier inversion in the time writes it as an
> integral over the frequency `w` (see `TimeSlice.spaceFourier_eq_integral`). The Laplace transform
> of the sine propagation function turns the damped time integral into
> `1 / (ω_ξ² - (2π w + i ε)²)`. The damping is removed by dominated convergence. The result is
> the boundary value `ε → 0+` of the resolvent, as a statement about the pairing of the retarded
> kernel with a test function.

## ii. Key results

> - `dampedKernel_eq` : the damped kernel in the spacetime Fourier variables.
> - `tendsto_dampedKernel` : the damping can be removed.
> - `tendsto_retardedPointSource` : the retarded kernel is the boundary value of the resolvent.
> - `solution_zero_eq_advancedSolution_zero` : off the mass shell the retarded and the advanced
>   solution agree at the origin.
> - `retardedGreen_eq_advancedGreen_of_avoidsShell` : the causal propagator `E = R - A` vanishes at
>   the origin for sources whose transform avoids the mass shell.

## iv. References

> None.

## A. The damped kernel

> - `dampedKernel_eq` : the damped kernel in the spacetime Fourier variables.

## B. The boundary value

> - `tendsto_dampedKernel` : the damping can be removed.
> - `tendsto_retardedPointSource` : the retarded kernel is the boundary value of the resolvent.

## C. The mass shell

> - `dampedKernel_zero_eq_of_avoidsShell` : the kernel off the mass shell.
> - `solution_zero_eq_advancedSolution_zero` : off the mass shell the retarded and the advanced
>   solution agree at the origin.
> - `retardedGreen_eq_advancedGreen_of_avoidsShell` : the causal propagator vanishes at the origin
>   for sources whose transform avoids the mass shell.

**`KleinGordon.dampedKernel`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L80).

> The damped time integral of the sine evolution at the origin.

```lean
def dampedKernel (μ ε : ℝ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) : ℂ
```

**`KleinGordon.sineEvolution_zero_eq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L84).

> The sine evolution at the origin is the integral of the multiplier against the transform.

```lean
lemma sineEvolution_zero_eq {μ : ℝ} (hμ : 0 ≤ μ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (s : ℝ) :
    sineEvolution ℂ s μ (slice ℂ ψ s) 0 = ∫ ξ : E, multiplier s μ ξ * spaceFourier ψ ξ s
```

**`KleinGordon.integrable_dampedIntegrand`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L90).

> The integrand of the damped kernel is integrable in time and frequency.

```lean
lemma integrable_dampedIntegrand {μ : ℝ} (ε : ℝ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) :
    Integrable (fun p : ℝ × E => (Real.exp (-(ε * p.1)) : ℂ) *
      (multiplier p.1 μ p.2 * spaceFourier ψ p.2 p.1))
      ((volume.restrict (Set.Ioi (0 : ℝ))).prod volume)
```

**`KleinGordon.dampedKernel_eq`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L148).

> **The damped kernel in the spacetime Fourier variables.** The damped time integral of the
> sine evolution at the origin is the integral of the transform against
> `1 / (ω_ξ² - (2π w + i ε)²)`.

```lean
lemma dampedKernel_eq {μ ε : ℝ} (hμ : 0 ≤ μ) (hε : 0 < ε)
    (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) :
    dampedKernel μ ε ψ = ∫ ξ : E, ∫ w : ℝ, timeFourier ψ w ξ *
      (1 / ((dispersion μ ξ : ℂ) ^ 2 - (2 * Real.pi * w + ε * Complex.I) ^ 2))
```

**`KleinGordon.tendsto_dampedKernel`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L167).

> **The damping can be removed.** The damped kernel converges to the undamped one.

```lean
lemma tendsto_dampedKernel {μ : ℝ} (hμ : 0 ≤ μ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) :
    Filter.Tendsto (fun ε => dampedKernel μ ε ψ) (nhdsWithin 0 (Set.Ioi 0))
      (nhds (dampedKernel μ 0 ψ))
```

**`KleinGordon.dampedKernel_zero_eq`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L237).

> The damped kernel without damping is the advanced solution at the origin.

```lean
lemma dampedKernel_zero_eq {μ : ℝ} (hμ : 0 ≤ μ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) :
    dampedKernel μ 0 ψ = advancedSolution ℂ ψ μ 0 0
```

**`KleinGordon.solution_zero_eq`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L244).

> The retarded solution at the origin is the undamped kernel of the reflected source.

```lean
lemma solution_zero_eq {μ : ℝ} (hμ : 0 ≤ μ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) :
    solution ℂ ψ μ 0 0 = dampedKernel μ 0 (reflect ℂ ψ)
```

**`KleinGordon.resolvent`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L252).

> The resolvent of the Klein–Gordon operator at the complexified frequency `2π w + i ε`.

```lean
def resolvent (μ ε w : ℝ) (ξ : E) : ℂ
```

**`KleinGordon.AvoidsShell`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L256).

> The test function has no Fourier support within `δ` of the mass shell.

```lean
def AvoidsShell (μ δ : ℝ) (χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) : Prop
```

**`KleinGordon.norm_mul_resolvent_le`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L259).

```lean
lemma norm_mul_resolvent_le {μ δ : ℝ} (hδ : 0 < δ) {χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)}
    (hχ : AvoidsShell μ δ χ) {ε : ℝ} (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) (hεδ : ε ≤ δ / 2)
    (w : ℝ) (ξ : E) :
    ‖timeFourier χ w ξ * resolvent μ ε w ξ‖ ≤ ‖timeFourier χ w ξ‖ * (2 / δ)
```

**`KleinGordon.measurable_resolvent`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L273).

```lean
lemma measurable_resolvent (μ ε : ℝ) : Measurable fun p : ℝ × E => resolvent μ ε p.1 p.2
```

**`KleinGordon.aestronglyMeasurable_timeFourier_mul_resolvent`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L283).

```lean
lemma aestronglyMeasurable_timeFourier_mul_resolvent (χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ))
    (μ ε : ℝ) (ξ : E) :
    AEStronglyMeasurable (fun w : ℝ => timeFourier χ w ξ * resolvent μ ε w ξ) volume
```

**`KleinGordon.tendsto_integral_resolvent`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L296).

> Inner dominated convergence: the resolvent integral converges off the mass shell.

```lean
lemma tendsto_integral_resolvent {μ δ : ℝ} (hδ : 0 < δ) {χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)}
    (hχ : AvoidsShell μ δ χ) (ξ : E) :
    Filter.Tendsto (fun ε : ℝ => ∫ w : ℝ, timeFourier χ w ξ * resolvent μ ε w ξ)
      (nhdsWithin 0 (Set.Ioi 0)) (nhds (∫ w : ℝ, timeFourier χ w ξ * resolvent μ 0 w ξ))
```

**`KleinGordon.aestronglyMeasurable_integral_timeFourier_mul_resolvent`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L329).

```lean
lemma aestronglyMeasurable_integral_timeFourier_mul_resolvent
    (χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (μ ε : ℝ) :
    AEStronglyMeasurable (fun ξ : E => ∫ w : ℝ, timeFourier χ w ξ * resolvent μ ε w ξ)
      volume
```

**`KleinGordon.norm_integral_timeFourier_mul_resolvent_le`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L344).

```lean
lemma norm_integral_timeFourier_mul_resolvent_le {μ δ : ℝ} (hδ : 0 < δ)
    {χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)} (hχ : AvoidsShell μ δ χ) {ε : ℝ} (h1 : 0 ≤ ε) (h2 : ε ≤ 1)
    (h3 : ε ≤ δ / 2) (C : ℝ) (n : ℕ)
    (hC : ∀ ξ : E, ∫ w : ℝ, ‖timeFourier χ w ξ‖ ≤ C * (1 + ‖ξ‖) ^ (-(n : ℝ))) (ξ : E) :
    ‖∫ w : ℝ, timeFourier χ w ξ * resolvent μ ε w ξ‖ ≤
      (2 / δ) * (C * (1 + ‖ξ‖) ^ (-(n : ℝ)))
```

**`KleinGordon.dampedKernel_zero_eq_of_avoidsShell`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L364).

> **The kernel off the mass shell.** If the transform of the source vanishes near the mass shell
> then the undamped kernel is the integral of the transform against the unregularised resolvent.

```lean
lemma dampedKernel_zero_eq_of_avoidsShell {μ δ : ℝ} (hμ : 0 ≤ μ) (hδ : 0 < δ)
    {χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)} (hχ : AvoidsShell μ δ χ) :
    dampedKernel μ 0 χ = ∫ ξ : E, ∫ w : ℝ, timeFourier χ w ξ * resolvent μ 0 w ξ
```

**`KleinGordon.avoidsShell_reflect`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L390).

```lean
lemma avoidsShell_reflect {μ δ : ℝ} {χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)} (h : AvoidsShell μ δ χ) :
    AvoidsShell μ δ (reflect ℂ χ)
```

**`KleinGordon.solution_zero_eq_advancedSolution_zero`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L398).

> **The retarded and the advanced solution agree off the mass shell.** If the transform of the
> source vanishes within `δ` of the mass shell then the retarded and the advanced solution have the
> same value at the origin.

```lean
lemma solution_zero_eq_advancedSolution_zero {μ δ : ℝ} (hμ : 0 ≤ μ) (hδ : 0 < δ)
    {χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)} (hχ : AvoidsShell μ δ χ) :
    solution ℂ χ μ 0 0 = advancedSolution ℂ χ μ 0 0
```

**`KleinGordon.Spacetime.retardedPointSource_zero_eq`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L419).

> The retarded kernel is the real part of the undamped kernel of the transported source.

```lean
lemma retardedPointSource_zero_eq (m : ℝ) (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    retardedPointSource m (0 : SpaceTime d) φ =
      (dampedKernel (m ^ 2) 0
        (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ))).re
```

**`KleinGordon.Spacetime.advancedPointSource_zero_eq`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L432).

> The advanced kernel is the real part of the retarded solution of the transported source.

```lean
lemma advancedPointSource_zero_eq (m : ℝ) (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    advancedPointSource m (0 : SpaceTime d) φ =
      (solution ℂ (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ)) (m ^ 2) 0
        0).re
```

**`KleinGordon.Spacetime.advancedPointSource_eq_retardedPointSource_of_avoidsShell`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L443).

> **On the mass shell.** If the spacetime Fourier transform of a test function vanishes within
> `δ` of the mass shell then the retarded and the advanced kernel give the same value. So the
> Fourier transform of the causal propagator `E = R - A` is supported on the mass shell.

```lean
lemma advancedPointSource_eq_retardedPointSource_of_avoidsShell (m δ : ℝ) (hδ : 0 < δ)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (h : AvoidsShell (m ^ 2) δ (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ))) :
    advancedPointSource m (0 : SpaceTime d) φ = retardedPointSource m (0 : SpaceTime d) φ
```

**`KleinGordon.Spacetime.tendsto_retardedPointSource`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L453).

> **The retarded kernel is the boundary value of the resolvent.** The retarded kernel tested
> against a real test function `φ` is the limit for `ε → 0+` of the integral of the spacetime Fourier
> transform of `φ` against `1 / (ω_ξ² - (2π w + i ε)²)`.

```lean
lemma tendsto_retardedPointSource (m : ℝ) (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    Filter.Tendsto (fun ε : ℝ => (∫ ξ : Space d, ∫ w : ℝ,
      timeFourier (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ)) w ξ *
        (1 / ((dispersion (m ^ 2) ξ : ℂ) ^ 2 - (2 * Real.pi * w + ε * Complex.I) ^ 2))).re)
      (nhdsWithin 0 (Set.Ioi 0)) (nhds (retardedPointSource m (0 : SpaceTime d) φ))
```

**`KleinGordon.Spacetime.retardedGreen_eq_advancedGreen_of_avoidsShell`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean#L477).

> **The causal propagator vanishes off the mass shell.** If the Fourier transform of a real
> test source vanishes within `δ` of the mass shell then the retarded and the advanced solution
> agree at the origin. So `E f = R f - A f` vanishes at the origin.

```lean
lemma retardedGreen_eq_advancedGreen_of_avoidsShell (m δ : ℝ) (hδ : 0 < δ) (f : TestField d ℝ)
    (h : AvoidsShell (m ^ 2) δ
      (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM (testFieldEquiv ℝ f)))) :
    ((realRetardedGreenOperator m).toLinearMap f).val 0 =
      ((realAdvancedGreenOperator m).toLinearMap f).val 0
```

## Depends on

- [Distributional sources](../part-01/distributionsources.md)
- [The space and time Fourier transform of a test function](../../../mathematics/part-02/distribution/timeslicefourier.md)

## Proof depends on

- [A Schwartz bound for the retarded kernel](retardedkernel-tempered.md)
- [Resolvent estimates for the sine propagation function](../../../mathematics/part-02/specialfunctions/sincpropagator-resolvent.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/BoundaryValue.lean)
