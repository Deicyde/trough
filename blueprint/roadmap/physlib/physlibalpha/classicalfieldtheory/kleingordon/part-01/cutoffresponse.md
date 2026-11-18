---
declaration: module
origin: cited
lean: KleinGordon.exists_solution_supported_seminorm, KleinGordon.solutionEvaluation, KleinGordon.solutionEvaluation_apply, KleinGordon.advancedSolutionEvaluation, KleinGordon.advancedSolutionEvaluation_apply, KleinGordon.exists_integrand_derivative_supported_seminorm, KleinGordon.exists_integral_derivative_supported_seminorm, KleinGordon.exists_solution_derivative_supported_seminorm
statement: formalized
proof: formalized
---

# Cutoff responses of compact sources

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.CutoffResponse`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean): 13 declarations, 9 with a docstring.

## i. Overview

> Cutting the response off by a test function is continuous in the source.

## ii. Key results

> - `solutionEvaluation` : Evaluation of the retarded response at a fixed event is continuous in the
>   native LF topology.
> - `advancedSolutionEvaluation` : Evaluation of the advanced response is continuous in the native LF
>   source topology.
> - `cutoffSolutionSupported` : A compactly cut off retarded response is continuous between
>   fixed-support source and target spaces in every derivative seminorm.
> - `cutoffSolution` : Multiplying the retarded Fourier response by a compact smooth cutoff is
>   continuous on the native LF test-function space.
> - `cutoffAdvancedSolution` : A compactly cut off advanced response is continuous on native smooth
>   tests.

## iv. References

> None.

## A. Continuous seminorm bounds for Fourier sources

> - `solutionEvaluation` : Evaluation of the retarded response at a fixed event is continuous in the
>   native LF topology.
> - `advancedSolutionEvaluation` : Evaluation of the advanced response is continuous in the native LF
>   source topology.
>
> Lemmas: `exists_solution_supported_seminorm`, `solutionEvaluation_apply`,
> `advancedSolutionEvaluation_apply`.

## B. Continuous source bounds for parameter derivatives

> Lemmas: `exists_integrand_derivative_supported_seminorm`,
> `exists_integral_derivative_supported_seminorm`, `exists_solution_derivative_supported_seminorm`.

## C. Continuous compactly cut off Green responses

> - `cutoffSolutionSupported` : A compactly cut off retarded response is continuous between
>   fixed-support source and target spaces in every derivative seminorm.
> - `cutoffSolution` : Multiplying the retarded Fourier response by a compact smooth cutoff is
>   continuous on the native LF test-function space.
>
> Lemmas: `cutoffSolution_apply`.

## D. Continuous compactly cut off advanced response

> - `cutoffAdvancedSolution` : A compactly cut off advanced response is continuous on native smooth
>   tests.
>
> Lemmas: `cutoffAdvancedSolution_apply`.

**`KleinGordon.exists_solution_supported_seminorm`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L92).

> On bounded time intervals the response is controlled by a continuous source seminorm,
> uniformly over every spatial observation point.

```lean
lemma exists_solution_supported_seminorm (K : Compacts (ℝ × E)) {μ : ℝ} (hμ : 0 ≤ μ)
    (T : ℝ) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (p : ℝ × E), |p.1| ≤ T →
        ‖solution F (supportedSource F K f) μ p.1 p.2‖ ≤ q f
```

**`KleinGordon.solutionEvaluation`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L141).

> Evaluation of the retarded response at a fixed event is continuous in the native LF topology.

```lean
def solutionEvaluation {μ : ℝ} (hμ : 0 ≤ μ) (p : ℝ × E) :
    𝓓((⊤ : Opens (ℝ × E)), F) →L[ℝ] F
```

**`KleinGordon.solutionEvaluation_apply`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L164).

```lean
lemma solutionEvaluation_apply {μ : ℝ} (hμ : 0 ≤ μ) (p : ℝ × E)
    (f : 𝓓((⊤ : Opens (ℝ × E)), F)) :
    solutionEvaluation F hμ p f = solution F f μ p.1 p.2
```

**`KleinGordon.advancedSolutionEvaluation`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L169).

> Evaluation of the advanced response is continuous in the native LF source topology.

```lean
def advancedSolutionEvaluation {μ : ℝ} (hμ : 0 ≤ μ) (p : ℝ × E) :
    𝓓((⊤ : Opens (ℝ × E)), F) →L[ℝ] F
```

**`KleinGordon.advancedSolutionEvaluation_apply`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L174).

```lean
lemma advancedSolutionEvaluation_apply {μ : ℝ} (hμ : 0 ≤ μ) (p : ℝ × E)
    (f : 𝓓((⊤ : Opens (ℝ × E)), F)) :
    advancedSolutionEvaluation F hμ p f = advancedSolution F f μ p.1 p.2
```

**`KleinGordon.exists_integrand_derivative_supported_seminorm`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L183).

> Every parameter derivative of the Fourier integrand has a continuous source bound.

```lean
lemma exists_integrand_derivative_supported_seminorm (K : Compacts (ℝ × E))
    (μ : ℝ) (k N : ℕ) (R : ℝ≥0) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (p z : ℝ × E), |z.1| ≤ R →
        ‖iteratedFDeriv ℝ k (fun w => solutionIntegrand F (supportedSource F K f) μ w z) p‖ ≤
          q f * (1 + ‖z.2‖) ^ (-(N : ℝ))
```

**`KleinGordon.exists_integral_derivative_supported_seminorm`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L212).

> Every derivative of a fixed-interval Fourier response is controlled continuously by the source.

```lean
lemma exists_integral_derivative_supported_seminorm (K : Compacts (ℝ × E))
    {μ : ℝ} (hμ : 0 ≤ μ) (k : ℕ) (R : ℝ≥0) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (p : ℝ × E),
        ‖iteratedFDeriv ℝ k (fun w => ∫ z : ℝ × E, solutionIntegrand F (supportedSource F K f) μ w z
          ∂((volume.restrict (Set.Ioc 0 (R : ℝ))).prod volume)) p‖ ≤ q f
```

**`KleinGordon.exists_solution_derivative_supported_seminorm`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L251).

> Every spacetime derivative of the retarded field is controlled by a continuous source seminorm
> on bounded time intervals, uniformly in the spatial observation point.

```lean
lemma exists_solution_derivative_supported_seminorm (K : Compacts (ℝ × E))
    {μ : ℝ} (hμ : 0 ≤ μ) (k : ℕ) (T : ℝ) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (p : ℝ × E), |p.1| ≤ T →
        ‖iteratedFDeriv ℝ k (fun w => solution F (supportedSource F K f) μ w.1 w.2) p‖ ≤ q f
```

**`KleinGordon.cutoffSolutionSupported`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L284).

> A compactly cut off retarded response is continuous between fixed-support source and target
> spaces in every derivative seminorm.

```lean
def cutoffSolutionSupported {μ : ℝ} (hμ : 0 ≤ μ) (K₁ K₂ : Compacts (ℝ × E))
    (χ : ContDiffMapSupportedIn (ℝ × E) ℝ ⊤ K₂) :
    ContDiffMapSupportedIn (ℝ × E) F ⊤ K₁ →L[ℝ] ContDiffMapSupportedIn (ℝ × E) F ⊤ K₂
```

**`KleinGordon.cutoffSolution`**, a def, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L326).

> Multiplying the retarded Fourier response by a compact smooth cutoff is continuous on the
> native LF test-function space.

```lean
def cutoffSolution {μ : ℝ} (hμ : 0 ≤ μ) (χ : 𝓓((⊤ : Opens (ℝ × E)), ℝ)) :
    𝓓((⊤ : Opens (ℝ × E)), F) →L[ℝ] 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`KleinGordon.cutoffSolution_apply`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L351).

```lean
lemma cutoffSolution_apply {μ : ℝ} (hμ : 0 ≤ μ) (χ : 𝓓((⊤ : Opens (ℝ × E)), ℝ))
    (f : 𝓓((⊤ : Opens (ℝ × E)), F)) (p : ℝ × E) :
    cutoffSolution F hμ χ f p = χ p • solution F f μ p.1 p.2
```

**`KleinGordon.cutoffAdvancedSolution`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L356).

> A compactly cut off advanced response is continuous on native smooth tests.

```lean
def cutoffAdvancedSolution {μ : ℝ} (hμ : 0 ≤ μ) (χ : 𝓓((⊤ : Opens (ℝ × E)), ℝ)) :
    𝓓((⊤ : Opens (ℝ × E)), F) →L[ℝ] 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`KleinGordon.cutoffAdvancedSolution_apply`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean#L363).

```lean
lemma cutoffAdvancedSolution_apply {μ : ℝ} (hμ : 0 ≤ μ) (χ : 𝓓((⊤ : Opens (ℝ × E)), ℝ))
    (f : 𝓓((⊤ : Opens (ℝ × E)), F)) (p : ℝ × E) :
    cutoffAdvancedSolution F hμ χ f p = χ p • advancedSolution F f μ p.1 p.2
```

## Depends on

- [Smoothness of the retarded solution](smoothness.md)
- [Smoothness and bounds of time slices](../../../mathematics/part-02/distribution/timeslicesmooth.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/CutoffResponse.lean)
