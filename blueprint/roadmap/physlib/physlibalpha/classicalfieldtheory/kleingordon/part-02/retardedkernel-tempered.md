---
declaration: module
origin: cited
lean: KleinGordon.norm_sineEvolution_zero_le, KleinGordon.weighted_seminorm_slice_le, KleinGordon.exists_norm_integral_sineEvolution_le, KleinGordon.exists_weighted_bound_sourceEquiv, KleinGordon.exists_abs_retardedPointSource_le, KleinGordon.exists_seminorm_weighted_le, KleinGordon.exists_tempered_extension, KleinGordon.tempered_ext
statement: formalized
proof: formalized
---

# A Schwartz bound for the retarded kernel

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.RetardedKernel.Tempered`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean): 11 declarations, 10 with a docstring.

> The retarded kernel tested against a test function is bounded by a finite number of weighted
> derivative bounds of the test function. The bound does not depend on the test function.

## i. Overview

> The retarded kernel at the origin applied to `ψ` is the integral over the positive times of the
> sine evolution of the slice `ψ(s, ·)` evaluated at the origin. The multiplier of the sine
> evolution is bounded by the time. The `L¹` norm of the Fourier transform of the slice is bounded
> by Schwartz seminorms of the slice. The seminorms of the slice are bounded by weighted derivative
> bounds of `ψ`. The weight in the time makes the time integral converge.

## ii. Key results

> - `norm_sineEvolution_zero_le` : the sine evolution at the origin is bounded by the time and the
>   `L¹` norm of the Fourier transform.
> - `weighted_seminorm_slice_le` : weighted bounds of `ψ` bound the seminorms of its slices.
> - `exists_norm_integral_sineEvolution_le` : the bound of the time integral.
> - `exists_abs_retardedPointSource_le` : the retarded kernel applied to a test function is bounded
>   by weighted derivative bounds of the test function.
> - `exists_tempered_extension` : the retarded kernel extends to a continuous linear functional on
>   the Schwartz space of spacetime, so it is a tempered distribution.

## iv. References

> None.

## A. The sine evolution at the origin

> - `norm_sineEvolution_zero_le` : the sine evolution at the origin is bounded by the time and the
>   `L¹` norm of the Fourier transform.

## B. The slices

> - `weighted_seminorm_slice_le` : weighted bounds of `ψ` bound the seminorms of its slices.

## C. The time integral

> - `exists_norm_integral_sineEvolution_le` : the bound of the time integral.

## D. The retarded kernel

> - `exists_abs_retardedPointSource_le` : the bound for the retarded kernel.

## E. The tempered extension

> - `exists_tempered_extension` : the retarded kernel is a tempered distribution.
> - `temperedKernel` : the retarded kernel as a tempered distribution.
> - `temperedKernel_unique` : the tempered extension is unique.

**`KleinGordon.norm_sineEvolution_zero_le`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L94).

> The sine evolution at the origin is bounded by the time and the `L¹` norm of the transform.

```lean
lemma norm_sineEvolution_zero_le [MeasurableSpace E] [BorelSpace E] [FiniteDimensional ℝ E]
    (r : ℝ) {μ : ℝ} (hμ : 0 ≤ μ) (g : 𝓢(E, F)) :
    ‖sineEvolution F r μ g 0‖ ≤ |r| * ∫ ξ : E, ‖𝓕 g ξ‖
```

**`KleinGordon.weighted_seminorm_slice_le`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L113).

> **Weighted bounds of `ψ` bound the seminorms of its slices.** If `(1 + ‖y‖)^N` times the
> derivatives of `ψ` up to the order `N` are bounded by `M`, then the seminorm `(k, p)` of the slice
> at the time `s` is at most `M / (1 + |s|)^3` for `k + 3 ≤ N` and `p ≤ N`.

```lean
lemma weighted_seminorm_slice_le (ψ : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × E)), F)) {N k p : ℕ}
    {M : ℝ} (hM : ∀ n ≤ N, ∀ y : ℝ × E, (1 + ‖y‖) ^ N * ‖iteratedFDeriv ℝ n ψ y‖ ≤ M)
    (hk : k + 3 ≤ N) (hp : p ≤ N) (s : ℝ) :
    SchwartzMap.seminorm ℂ k p (TimeSlice.slice F ψ s) ≤ M / (1 + |s|) ^ 3
```

**`KleinGordon.exists_norm_integral_sineEvolution_le`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L142).

> **The time integral is bounded.** There are an order `N` and a constant `C` such that weighted
> bounds of the derivatives of `ψ` by `M` bound the damped time integral of the sine evolution of
> the slices at the origin by `C * M`. The bound does not depend on the damping `ε ≥ 0`.

```lean
lemma exists_norm_integral_sineEvolution_le {μ : ℝ} (hμ : 0 ≤ μ) :
    ∃ (N : ℕ) (C : ℝ), 0 ≤ C ∧ ∀ (ψ : 𝓓((⊤ : TopologicalSpace.Opens (ℝ × E)), ℂ)) (M ε : ℝ),
      0 ≤ ε → (∀ n ≤ N, ∀ y : ℝ × E, (1 + ‖y‖) ^ N * ‖iteratedFDeriv ℝ n ψ y‖ ≤ M) →
      ‖∫ s in Set.Ioi (0 : ℝ), (Real.exp (-(ε * s)) : ℂ) *
        sineEvolution ℂ s μ (TimeSlice.slice ℂ ψ s) 0‖ ≤ C * M
```

**`KleinGordon.exists_weighted_bound_sourceEquiv`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L203).

> Transporting a complexified spacetime test function to time-space coordinates keeps the
> weighted derivative bounds up to a constant.

```lean
lemma exists_weighted_bound_sourceEquiv (d N : ℕ) :
    ∃ A : ℝ, 0 ≤ A ∧ ∀ (φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ)) (M : ℝ),
      (∀ n ≤ N, ∀ y : SpaceTime d, (1 + ‖y‖) ^ N * ‖iteratedFDeriv ℝ n φ y‖ ≤ M) →
      ∀ n ≤ N, ∀ y : ℝ × Space d, (1 + ‖y‖) ^ N *
        ‖iteratedFDeriv ℝ n (sourceEquiv ℂ (TestFunction.postcompCLM Complex.ofRealCLM φ)) y‖ ≤
          A * M
```

**`KleinGordon.exists_abs_retardedPointSource_le`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L250).

> **The retarded kernel is bounded by Schwartz-type seminorms.** There are an order `N` and a
> constant `C` such that weighted derivative bounds of a test function by `M` bound the retarded
> kernel applied to it by `C * M`.

```lean
lemma exists_abs_retardedPointSource_le (d : ℕ) (m : ℝ) :
    ∃ (N : ℕ) (C : ℝ), 0 ≤ C ∧ ∀ (φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ))
      (M : ℝ), (∀ n ≤ N, ∀ y : SpaceTime d, (1 + ‖y‖) ^ N * ‖iteratedFDeriv ℝ n φ y‖ ≤ M) →
      |retardedPointSource m (0 : SpaceTime d) φ| ≤ C * M
```

**`KleinGordon.exists_seminorm_weighted_le`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L279).

> **Weighted bounds from Schwartz seminorms.** There is a continuous seminorm `q` on Schwartz
> space such that `q` of a test function bounds its weighted derivatives of order up to `N`.

```lean
lemma exists_seminorm_weighted_le (d N : ℕ) :
    ∃ q : Seminorm ℝ 𝓢(SpaceTime d, ℝ), Continuous q ∧
      ∀ φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ), ∀ n ≤ N, ∀ y : SpaceTime d,
        (1 + ‖y‖) ^ N * ‖iteratedFDeriv ℝ n φ y‖ ≤ 2 ^ (N + 1) * q (ofTestFunction φ)
```

**`KleinGordon.exists_tempered_extension`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L334).

> **The retarded kernel is a tempered distribution.** The retarded kernel extends to a
> continuous linear functional on the Schwartz space of spacetime.

```lean
lemma exists_tempered_extension (d : ℕ) (m : ℝ) :
    ∃ T : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ, ∀ φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ),
      T (ofTestFunction φ) = retardedPointSource m (0 : SpaceTime d) φ
```

**`KleinGordon.tempered_ext`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L372).

> Two tempered distributions that agree on test functions are equal.

```lean
lemma tempered_ext (d : ℕ) {T T' : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ}
    (h : ∀ φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ),
      T (ofTestFunction φ) = T' (ofTestFunction φ)) : T = T'
```

**`KleinGordon.temperedKernel`**, a def, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L381).

> The retarded kernel as a tempered distribution on spacetime.

```lean
def temperedKernel (d : ℕ) (m : ℝ) : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ
```

**`KleinGordon.temperedKernel_apply`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L384).

```lean
lemma temperedKernel_apply (d : ℕ) (m : ℝ)
    (φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ)) :
    temperedKernel d m (ofTestFunction φ) = retardedPointSource m (0 : SpaceTime d) φ
```

**`KleinGordon.temperedKernel_unique`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean#L390).

> **The tempered extension is unique.**

```lean
lemma temperedKernel_unique (d : ℕ) (m : ℝ) {T : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ}
    (h : ∀ φ : 𝓓((⊤ : TopologicalSpace.Opens (SpaceTime d)), ℝ),
      T (ofTestFunction φ) = retardedPointSource m (0 : SpaceTime d) φ) :
    T = temperedKernel d m
```

## Depends on

- [Distributional sources](../part-01/distributionsources.md)
- [Test functions are dense in the Schwartz space](../../../mathematics/part-02/distribution/schwartzdensity.md)

## Proof depends on

- [Bounds on iterated derivatives](../../../mathematics/part-01/calculus/iteratedfderivbounds.md)
- [The integral of a Fourier transform is bounded by Schwartz seminorms](../../../mathematics/part-02/fourier/schwartzdecay.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedKernel/Tempered.lean)
