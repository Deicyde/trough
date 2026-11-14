---
declaration: module
origin: cited
lean: KleinGordon.timeCLM, KleinGordon.timeCLM_symm, KleinGordon.slice_twist, KleinGordon.kernel_twist, KleinGordon.realAdvancedCutoff_eq, KleinGordon.tsupport_realAdvancedCutoff_subset, KleinGordon.precompTranslationCLM_twistCLM, KleinGordon.twisted_apply
statement: formalized
proof: formalized
---

# The boundary value formula for compactly supported distributional sources

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.RetardedKernel.DistributionSource`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean): 13 declarations, 7 with a docstring.

> The retarded response of a compactly supported distribution is the limit of the responses to its
> damped advanced solutions.

## i. Overview

> By transposition the retarded response of a compactly supported distribution `T` against a test
> function `φ` is `T` applied to the cut off advanced solution of `φ`
> (`retardedDistribution_apply`). For `ε > 0` the cut off advanced solution is replaced by
> `x ↦ χ x * Re ⟨φ̂ translated by x, resolvent at 2π w + i ε⟩`. This is the cut off damped kernel
> centred at `x`, the boundary value pairing of the kernel for the translate of `φ`. It equals the
> conjugate `M_ε C M_{-ε} φ` of the cut off advanced solution `C` by the multiplication with
> `exp (ε t)`. Finite order of `T` and the estimates for the twist give that the pairings converge
> to the response for every compactly supported distribution.

## ii. Key results

> - `timeCLM` : the time coordinate.
> - `kernel_twist` : the kernel applied to a twisted test function is the damped kernel.
> - `twisted_apply_fourier` : the twisted cut off advanced solution is the cut off resolvent
>   pairing of the translate.
> - `tendsto_distribution_boundary_value` : the boundary value formula for compactly supported
>   distributions.

## iv. References

> None.

## A. The twist in time

> - `timeCLM` : the time coordinate.
> - `slice_twist` : the slices of a twisted test function.
> - `kernel_twist` : the kernel applied to a twisted test function is the damped kernel.

## B. The damped kernel centred at a point

> - `realAdvancedCutoff_eq` : the cut off advanced solution through the point source.
> - `twisted_apply` : the twisted cut off advanced solution is the damped kernel at the translate.
> - `twisted_apply_fourier` : the same as a resolvent pairing.

## C. Compactly supported distributions

> - `tendsto_distribution_boundary_value` : the boundary value formula.

**`KleinGordon.timeCLM`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L79).

> The time coordinate as a continuous linear functional.

```lean
def timeCLM (d : ℕ) : SpaceTime d →L[ℝ] ℝ
```

**`KleinGordon.timeCLM_symm`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L82).

```lean
lemma timeCLM_symm (s : ℝ) (x : Space d) : timeCLM d ((coordinates d).symm (s, x)) = s
```

**`KleinGordon.slice_twist`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L85).

```lean
lemma slice_twist (ε : ℝ) (ψ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) (s : ℝ) :
    slice ℂ (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM
      (ExpTwist.twistCLM (timeCLM d) (-ε) ψ))) s =
      (Real.exp (-(ε * s)) : ℂ) • slice ℂ (sourceEquiv ℂ
        (TestFunction.postcompCLM Complex.ofRealCLM ψ)) s
```

**`KleinGordon.kernel_twist`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L99).

> The kernel at the origin applied to a twisted test function is the damped kernel.

```lean
lemma kernel_twist (m ε : ℝ) (ψ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    retardedPointSource m (0 : SpaceTime d) (ExpTwist.twistCLM (timeCLM d) (-ε) ψ) =
      (dampedKernel (m ^ 2) ε
        (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM ψ))).re
```

**`KleinGordon.realAdvancedCutoff_eq`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L110).

```lean
lemma realAdvancedCutoff_eq (m : ℝ) (χ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (g : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) (p : SpaceTime d) :
    realAdvancedCutoff m χ g p = χ p * retardedPointSource m p g
```

**`KleinGordon.tsupport_realAdvancedCutoff_subset`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L117).

```lean
lemma tsupport_realAdvancedCutoff_subset (m : ℝ) (χ g : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    tsupport ⇑(realAdvancedCutoff m χ g) ⊆ tsupport χ
```

**`KleinGordon.precompTranslationCLM_twistCLM`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L124).

```lean
lemma precompTranslationCLM_twistCLM (a : ℝ) (p : SpaceTime d)
    (g : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    precompTranslationCLM p (ExpTwist.twistCLM (timeCLM d) a g) =
      Real.exp (a * timeCLM d p) • ExpTwist.twistCLM (timeCLM d) a (precompTranslationCLM p g)
```

**`KleinGordon.twisted_apply`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L135).

> **The twisted advanced response is the damped kernel centred at `p`.**

```lean
lemma twisted_apply (m ε : ℝ) (χ φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) (p : SpaceTime d) :
    ExpTwist.twistCLM (timeCLM d) ε (realAdvancedCutoff m χ
        (ExpTwist.twistCLM (timeCLM d) (-ε) φ)) p =
      χ p * (dampedKernel (m ^ 2) ε
        (sourceEquiv ℂ
          (TestFunction.postcompCLM Complex.ofRealCLM (precompTranslationCLM p φ)))).re
```

**`KleinGordon.twisted_apply_fourier`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L152).

> For `ε > 0` the twisted advanced response is the cut off resolvent pairing of the translate.

```lean
lemma twisted_apply_fourier (m : ℝ) {ε : ℝ} (hε : 0 < ε) (χ φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (p : SpaceTime d) :
    ExpTwist.twistCLM (timeCLM d) ε (realAdvancedCutoff m χ
        (ExpTwist.twistCLM (timeCLM d) (-ε) φ)) p =
      χ p * (fourierPairing (m ^ 2) ε (ofTestFunction (precompTranslationCLM p φ))).re
```

**`KleinGordon.splitSource_translate`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L159).

```lean
lemma splitSource_translate (p : SpaceTime d) (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    ⇑(splitSource d (ofTestFunction (precompTranslationCLM p φ))) =
      fun v => splitSource d (ofTestFunction φ) (v + (splitEquiv d).symm p)
```

**`KleinGordon.fourierPairing_translate`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L168).

> **The pairing of a translate in Fourier variables.** The resolvent pairing of the translate of
> `φ` by `p` is the integral of the phase `𝐞 ⟨p, ζ⟩` times the transform of `φ` times the
> resolvent.

```lean
lemma fourierPairing_translate (μ ε : ℝ) (p : SpaceTime d)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    fourierPairing μ ε (ofTestFunction (precompTranslationCLM p φ)) =
      ∫ ζ : SplitSpace d, (𝐞 (inner ℝ ((splitEquiv d).symm p) ζ) : ℂ) *
        (𝓕 (splitSource d (ofTestFunction φ)) ζ * splitResolvent μ ε ζ)
```

**`KleinGordon.twisted_apply_phase`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L183).

> **The twisted advanced response in Fourier variables.** For `ε > 0` it is
> `x ↦ χ x * Re ∫ 𝐞 ⟨x, ζ⟩ φ̂ (ζ) / (ω_ξ² - (2π w + i ε)²) dζ`.

```lean
lemma twisted_apply_phase (m : ℝ) {ε : ℝ} (hε : 0 < ε) (χ φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ))
    (p : SpaceTime d) :
    ExpTwist.twistCLM (timeCLM d) ε (realAdvancedCutoff m χ
        (ExpTwist.twistCLM (timeCLM d) (-ε) φ)) p =
      χ p * (∫ ζ : SplitSpace d, (𝐞 (inner ℝ ((splitEquiv d).symm p) ζ) : ℂ) *
        (𝓕 (splitSource d (ofTestFunction φ)) ζ * splitResolvent (m ^ 2) ε ζ)).re
```

**`KleinGordon.tendsto_distribution_boundary_value`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean#L192).

> **The boundary value formula for compactly supported distributional sources.**

```lean
lemma tendsto_distribution_boundary_value (m : ℝ) (T : compactDistributions (SpaceTime d) ℝ)
    (f : TestField d ℝ) :
    Filter.Tendsto (fun ε : ℝ => T.val (ExpTwist.twistCLM (timeCLM d) ε
      (realAdvancedCutoff m (compactCutoff (compactDistributionBound T))
        (ExpTwist.twistCLM (timeCLM d) (-ε) (testFieldEquiv ℝ f)))))
      (nhdsWithin 0 (Set.Ioi 0))
      (nhds (retardedDistribution m T (testFieldEquiv ℝ f)))
```

## Depends on

- [The Fourier form of the tempered retarded kernel](retardedkernel-fourierform.md)
- [Klein–Gordon fields and causal propagation](../part-01/solution.md)
- [Exponential twists on test functions](../../../mathematics/part-02/distribution/exptwistclm.md)
- [Translation of test functions](../../../mathematics/part-02/distribution/translation.md)

## Proof depends on

- [The retarded solution as a convolution with the retarded kernel](retardedkernel-convolution.md)
- [The boundary value formula for point sources](retardedkernel-pointsource.md)
- [The Fourier transform under a linear change of variables](../../../mathematics/part-02/fourier/linearchange.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/DistributionSource.lean)
