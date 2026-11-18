---
declaration: module
origin: cited
lean: KleinGordon.solutionIntegrand, KleinGordon.contDiff_solutionIntegrand_joint, KleinGordon.contDiff_solutionIntegrand_p, KleinGordon.norm_iteratedFDeriv_solutionIntegrand_le, KleinGordon.exists_char_mul_timeDeriv_bound, KleinGordon.exists_solutionIntegrand_bound, KleinGordon.integrable_solutionIntegrand, KleinGordon.solution_eq_integral_solutionIntegrand
statement: formalized
proof: formalized
---

# Smoothness of the retarded solution

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Smoothness`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean): 11 declarations, 9 with a docstring.

## i. Overview

> The retarded solution is jointly smooth in time and space.

## ii. Key results

> - `solutionIntegrand` : The integrand of the retarded solution in the variables `(r, ξ)`, at the
>   point `p = (t, x)`.
> - `solution_eq_integral_solutionIntegrand` : A fixed propagation interval represents the solution
>   when its lower source time precedes the support.
> - `contDiff_solution` : The retarded Klein–Gordon solution of a smooth compactly supported source is
>   smooth on spacetime.
> - `integrable_solutionIntegrand` : The Fourier integrand is integrable over a bounded propagation
>   interval and all frequencies.

## iv. References

> None.

## A. Smoothness of the retarded solution

> - `solutionIntegrand` : The integrand of the retarded solution in the variables `(r, ξ)`, at the
>   point `p = (t, x)`.
>
> Lemmas: `contDiff_solutionIntegrand_joint`, `contDiff_solutionIntegrand_p`,
> `norm_iteratedFDeriv_solutionIntegrand_le`, `exists_char_mul_timeDeriv_bound`,
> `exists_solutionIntegrand_bound`, `integrable_solutionIntegrand`,
> `solution_eq_integral_solutionIntegrand`, `contDiff_integral_solutionIntegrand`,
> `contDiff_solution`, `contDiff_advancedSolution`.

**`KleinGordon.solutionIntegrand`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L66).

> The integrand of the retarded solution in the variables `(r, ξ)`, at the point `p = (t, x)`.

```lean
def solutionIntegrand (μ : ℝ) (p : ℝ × E) (z : ℝ × E) : F
```

**`KleinGordon.contDiff_solutionIntegrand_joint`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L69).

```lean
lemma contDiff_solutionIntegrand_joint {μ : ℝ} (hμ : 0 ≤ μ) :
    ContDiff ℝ ∞ fun w : (ℝ × E) × (ℝ × E) => solutionIntegrand F f μ w.1 w.2
```

**`KleinGordon.contDiff_solutionIntegrand_p`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L81).

```lean
lemma contDiff_solutionIntegrand_p {μ : ℝ} (hμ : 0 ≤ μ) (z : ℝ × E) :
    ContDiff ℝ ∞ fun p : ℝ × E => solutionIntegrand F f μ p z
```

**`KleinGordon.norm_iteratedFDeriv_solutionIntegrand_le`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L87).

> The Leibniz bound separates the spatial character from the time derivatives of the source.

```lean
lemma norm_iteratedFDeriv_solutionIntegrand_le (μ : ℝ) (k : ℕ) (p z : ℝ × E) :
    ‖iteratedFDeriv ℝ k (fun q => solutionIntegrand F f μ q z) p‖ ≤
      ∑ i ∈ Finset.range (k + 1), (k.choose i : ℝ) * (2 * π * ‖z.2‖) ^ i *
        (|z.1| * ‖iteratedDeriv (k - i) (fun s => 𝓕 (slice F f s) z.2) (p.1 - z.1)‖)
```

**`KleinGordon.exists_char_mul_timeDeriv_bound`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L115).

> Each Leibniz term has arbitrarily rapid frequency decay, uniformly in time.

```lean
lemma exists_char_mul_timeDeriv_bound (i j N : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ (ξ : E) (s : ℝ),
      (2 * π * ‖ξ‖) ^ i * ‖iteratedDeriv j (fun r => 𝓕 (slice F f r) ξ) s‖ ≤
        C * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

**`KleinGordon.exists_solutionIntegrand_bound`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L133).

> All parameter derivatives have rapid frequency decay on bounded propagation intervals.

```lean
lemma exists_solutionIntegrand_bound (μ : ℝ) (k N : ℕ) (R : ℝ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ (p z : ℝ × E), |z.1| ≤ R →
      ‖iteratedFDeriv ℝ k (fun q => solutionIntegrand F f μ q z) p‖ ≤
        C * (1 + ‖z.2‖) ^ (-(N : ℝ))
```

**`KleinGordon.integrable_solutionIntegrand`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L157).

> The Fourier integrand is integrable over a bounded propagation interval and all frequencies.

```lean
lemma integrable_solutionIntegrand {μ : ℝ} (hμ : 0 ≤ μ) (R : ℝ) (p : ℝ × E) :
    Integrable (solutionIntegrand F f μ p)
      ((volume.restrict (Set.Ioc 0 R)).prod volume)
```

**`KleinGordon.solution_eq_integral_solutionIntegrand`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L174).

> A fixed propagation interval represents the solution when its lower source time precedes
> the support.

```lean
lemma solution_eq_integral_solutionIntegrand {μ : ℝ} (hμ : 0 ≤ μ) {R : ℝ} (hR : 0 ≤ R)
    {a : ℝ} (ha : ∀ s ≤ a, s ∉ Prod.fst '' tsupport f) (p : ℝ × E) (hp : p.1 - R ≤ a) :
    solution F f μ p.1 p.2 = ∫ z : ℝ × E, solutionIntegrand F f μ p z
      ∂((volume.restrict (Set.Ioc 0 R)).prod volume)
```

**`KleinGordon.contDiff_integral_solutionIntegrand`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L188).

> Integrating over a fixed bounded propagation interval gives a smooth spacetime field.

```lean
lemma contDiff_integral_solutionIntegrand {μ : ℝ} (hμ : 0 ≤ μ) (R : ℝ) :
    ContDiff ℝ ∞ (fun p : ℝ × E => ∫ z : ℝ × E, solutionIntegrand F f μ p z
      ∂((volume.restrict (Set.Ioc 0 R)).prod volume))
```

**`KleinGordon.contDiff_solution`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L213).

> The retarded Klein–Gordon solution of a smooth compactly supported source is smooth on
> spacetime.

```lean
lemma contDiff_solution {μ : ℝ} (hμ : 0 ≤ μ) :
    ContDiff ℝ ∞ (fun p : ℝ × E => solution F f μ p.1 p.2)
```

**`KleinGordon.contDiff_advancedSolution`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean#L229).

> The advanced Klein–Gordon solution is smooth on spacetime.

```lean
lemma contDiff_advancedSolution {μ : ℝ} (hμ : 0 ≤ μ) :
    ContDiff ℝ ∞ (fun p : ℝ × E => advancedSolution F f μ p.1 p.2)
```

## Depends on

- [The retarded and advanced solution](retardedsolution.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Smoothness.lean)
