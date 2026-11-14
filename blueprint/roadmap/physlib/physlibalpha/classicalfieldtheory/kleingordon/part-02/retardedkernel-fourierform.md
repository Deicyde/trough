---
declaration: module
origin: cited
lean: KleinGordon.SplitSpace, KleinGordon.splitResolvent, KleinGordon.norm_splitResolvent_le, KleinGordon.continuous_splitResolvent, KleinGordon.splitEquiv, KleinGordon.splitSource, KleinGordon.splitSource_apply, KleinGordon.spacetimeFourier
statement: formalized
proof: formalized
---

# The Fourier form of the tempered retarded kernel

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.RetardedKernel.FourierForm`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean): 21 declarations, 14 with a docstring.

> The retarded kernel on Schwartz functions is the boundary value of the resolvent integrated
> against the spacetime Fourier transform.

## i. Overview

> The pairing of the spacetime Fourier transform with the resolvent at the complexified frequency
> `2π w + i ε` is continuous on Schwartz space for each `ε > 0`. The bound is `2 / ε²` times the
> `L¹` norm of the transform. For test functions the pairing is the damped kernel. The damped kernel
> is bounded by a Schwartz seminorm that does not depend on `ε`. So the pairings converge on all
> Schwartz functions to the tempered kernel. No principal value analysis near the mass shell is
> needed.

## ii. Key results

> - `fourierPairing` : the pairing of the spacetime Fourier transform with the resolvent.
> - `norm_fourierPairing_le` : the pairing is bounded by `2 / ε²` times the `L¹` norm of the
>   transform.
> - `fourierPairing_eq_integral_integral` : the pairing as an iterated integral over `ξ` and `w`.
> - `fourierPairing_ofTestFunction` : on test functions the pairing is the damped kernel.
> - `exists_abs_dampedKernel_le` : the damped kernel is bounded by a Schwartz seminorm uniformly in
>   `ε`.
> - `exists_abs_fourierPairing_le` : the same bound on all Schwartz functions.
> - `tendsto_fourierPairing` : the tempered kernel is the boundary value `ε → 0+` of the pairing
>   for every real Schwartz function.

## iv. References

> None.

## A. The split space and the resolvent

> - `SplitSpace` : time and space with the Euclidean product norm.

## B. The pairing

> - `splitSource` : a real Schwartz function of spacetime as a complex one of the split space.
> - `spacetimeFourier` : the spacetime Fourier transform.
> - `fourierPairing` : the pairing with the resolvent.
> - `continuous_pairingRe` : the pairing is continuous on Schwartz space for each `ε > 0`.

## C. Test functions

> - `fourierPairing_ofTestFunction` : on test functions the pairing is the damped kernel.
> - `exists_abs_dampedKernel_le` : the uniform bound.

## D. The boundary value on Schwartz space

> - `exists_abs_fourierPairing_le` : the uniform bound on Schwartz space by closure.
> - `tendsto_fourierPairing` : the boundary value.

**`KleinGordon.SplitSpace`**, an abbrev, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L83).

> Time and space with the Euclidean product norm.

```lean
abbrev SplitSpace (d : ℕ)
```

**`KleinGordon.splitResolvent`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L88).

> The resolvent as a function on the split space.

```lean
def splitResolvent (μ ε : ℝ) (p : SplitSpace d) : ℂ
```

**`KleinGordon.norm_splitResolvent_le`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L90).

```lean
lemma norm_splitResolvent_le {μ : ℝ} {ε : ℝ} (hε : 0 < ε) (p : SplitSpace d) :
    ‖splitResolvent μ ε p‖ ≤ 2 / ε ^ 2
```

**`KleinGordon.continuous_splitResolvent`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L98).

```lean
lemma continuous_splitResolvent {μ : ℝ} {ε : ℝ} (hε : 0 < ε) :
    Continuous (splitResolvent (d := d) μ ε)
```

**`KleinGordon.splitEquiv`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L117).

> Split space and spacetime are the same vector space.

```lean
def splitEquiv (d : ℕ) : SplitSpace d ≃L[ℝ] SpaceTime d
```

**`KleinGordon.splitSource`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L121).

> A real Schwartz function of spacetime as a complex Schwartz function of the split space.

```lean
def splitSource (d : ℕ) : 𝓢(SpaceTime d, ℝ) →L[ℝ] 𝓢(SplitSpace d, ℂ)
```

**`KleinGordon.splitSource_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L125).

```lean
lemma splitSource_apply (φ : 𝓢(SpaceTime d, ℝ)) (p : SplitSpace d) :
    splitSource d φ p = (φ (splitEquiv d p) : ℂ)
```

**`KleinGordon.spacetimeFourier`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L129).

> The spacetime Fourier transform of a real Schwartz function.

```lean
def spacetimeFourier (d : ℕ) : 𝓢(SpaceTime d, ℝ) →L[ℝ] 𝓢(SplitSpace d, ℂ)
```

**`KleinGordon.spacetimeFourier_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L132).

```lean
lemma spacetimeFourier_apply (φ : 𝓢(SpaceTime d, ℝ)) (p : SplitSpace d) :
    spacetimeFourier d φ p = 𝓕 (splitSource d φ) p
```

**`KleinGordon.fourierPairing`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L136).

> **The pairing of the transform with the resolvent.**

```lean
def fourierPairing (μ ε : ℝ) (φ : 𝓢(SpaceTime d, ℝ)) : ℂ
```

**`KleinGordon.integrable_mul_splitResolvent`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L139).

```lean
lemma integrable_mul_splitResolvent {μ ε : ℝ} (hε : 0 < ε) (g : 𝓢(SplitSpace d, ℂ)) :
    Integrable fun p : SplitSpace d => g p * splitResolvent μ ε p
```

**`KleinGordon.pairingRe`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L149).

> The real part of the pairing as a real linear functional.

```lean
def pairingRe (μ : ℝ) {ε : ℝ} (hε : 0 < ε) : 𝓢(SpaceTime d, ℝ) →ₗ[ℝ] ℝ
```

**`KleinGordon.pairingRe_apply`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L159).

```lean
lemma pairingRe_apply (μ : ℝ) {ε : ℝ} (hε : 0 < ε) (φ : 𝓢(SpaceTime d, ℝ)) :
    pairingRe μ hε φ = (fourierPairing μ ε φ).re
```

**`KleinGordon.norm_fourierPairing_le`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L162).

```lean
lemma norm_fourierPairing_le {μ ε : ℝ} (hε : 0 < ε) (φ : 𝓢(SpaceTime d, ℝ)) :
    ‖fourierPairing μ ε φ‖ ≤ (2 / ε ^ 2) * ∫ p : SplitSpace d, ‖𝓕 (splitSource d φ) p‖
```

**`KleinGordon.timeFourier_eq_fourier`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L171).

> The transform of the transported test function is the transform on split space.

```lean
lemma timeFourier_eq_fourier (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) (w : ℝ) (ξ : Space d) :
    timeFourier (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ)) w ξ =
      𝓕 (splitSource d (ofTestFunction φ)) (WithLp.toLp 2 (w, ξ))
```

**`KleinGordon.fourierPairing_eq_integral_integral`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L181).

> **The pairing as an iterated integral.**

```lean
lemma fourierPairing_eq_integral_integral {μ ε : ℝ} (hε : 0 < ε) (φ : 𝓢(SpaceTime d, ℝ)) :
    fourierPairing μ ε φ = ∫ ξ : Space d, ∫ w : ℝ,
      spacetimeFourier d φ (WithLp.toLp 2 (w, ξ)) * resolvent μ ε w ξ
```

**`KleinGordon.fourierPairing_ofTestFunction`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L192).

> **For test functions the pairing is the damped kernel.**

```lean
lemma fourierPairing_ofTestFunction {m ε : ℝ} (hε : 0 < ε)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    fourierPairing (m ^ 2) ε (ofTestFunction φ) =
      dampedKernel (m ^ 2) ε (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ))
```

**`KleinGordon.exists_abs_dampedKernel_le`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L202).

> **The damped kernel is bounded uniformly in the damping.**

```lean
lemma exists_abs_dampedKernel_le (d : ℕ) (m : ℝ) :
    ∃ (q : Seminorm ℝ 𝓢(SpaceTime d, ℝ)) (C : ℝ), Continuous q ∧ 0 ≤ C ∧
      ∀ (ε : ℝ), 0 ≤ ε → ∀ φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ),
        |(dampedKernel (m ^ 2) ε
          (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ))).re| ≤
          C * q (ofTestFunction φ)
```

**`KleinGordon.continuous_pairingRe`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L220).

> The test functions are dense in Schwartz space.

```lean
lemma continuous_pairingRe (μ : ℝ) {ε : ℝ} (hε : 0 < ε) :
    Continuous fun φ : 𝓢(SpaceTime d, ℝ) => (fourierPairing μ ε φ).re
```

**`KleinGordon.exists_abs_fourierPairing_le`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L243).

> **The pairing is bounded on all Schwartz functions uniformly in `ε`.**

```lean
lemma exists_abs_fourierPairing_le (d : ℕ) (m : ℝ) :
    ∃ (q : Seminorm ℝ 𝓢(SpaceTime d, ℝ)) (C : ℝ), Continuous q ∧ 0 ≤ C ∧
      ∀ (ε : ℝ), 0 < ε → ∀ φ : 𝓢(SpaceTime d, ℝ),
        |(fourierPairing (m ^ 2) ε φ).re| ≤ C * q φ
```

**`KleinGordon.tendsto_fourierPairing`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean#L263).

> **Fourier form of the tempered retarded kernel.** For every real Schwartz function `φ` the
> tempered kernel is the limit for `ε → 0+` of the integral of the spacetime Fourier transform of
> `φ` against `1 / (ω_ξ² - (2π w + i ε)²)`.

```lean
lemma tendsto_fourierPairing (m : ℝ) (φ : 𝓢(SpaceTime d, ℝ)) :
    Filter.Tendsto (fun ε : ℝ => (fourierPairing (m ^ 2) ε φ).re) (nhdsWithin 0 (Set.Ioi 0))
      (nhds (temperedKernel d m φ))
```

## Depends on

- [The retarded kernel as a boundary value in the spacetime Fourier variables](retardedkernel-boundaryvalue.md)
- [A Schwartz bound for the retarded kernel](retardedkernel-tempered.md)

## Proof depends on

- [The marginal of a Schwartz function on a Euclidean product](../../../mathematics/part-02/fourier/marginal.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/FourierForm.lean)
