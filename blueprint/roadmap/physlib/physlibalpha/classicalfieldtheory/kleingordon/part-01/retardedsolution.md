---
declaration: module
origin: cited
lean: KleinGordon.sourceHat, KleinGordon.continuous_sourceHat, KleinGordon.freqSolution, KleinGordon.freqSolution_eq, KleinGordon.freqSolution1, KleinGordon.hasDerivAt_freqSolution, KleinGordon.hasDerivAt_freqSolution1, KleinGordon.norm_freqSolution1_le
statement: formalized
proof: formalized
---

# The retarded and advanced solution

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.RetardedSolution`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean): 35 declarations, 19 with a docstring.

> The retarded solution of a test function source is the Duhamel integral of the sine evolution.

## i. Overview

> The retarded solution of a test function source is the Duhamel integral of the sine evolution. It
> solves the equation and is linear in the source.

## ii. Key results

> - `sourceHat` : The Fourier transform of the source at the frequency `ξ`, as a function of the time.
> - `freqSolution` : The retarded solution at the spatial frequency `ξ`, with zero data at the time
>   `a`.
> - `freqSolution1` : The time derivative of the per-frequency solution.
> - `solution` : The retarded solution of the Klein–Gordon equation with the source `f`.
> - `advancedSolution` : The advanced solution: the retarded solution of the time-reflected source,
>   reflected back.
> - `testOperator` : The Klein–Gordon operator `∂ₜ² - Δ + μ` on compact spacetime test fields.

## iv. References

> None.

## A. The retarded Klein–Gordon solution of a test-function source

> - `sourceHat` : The Fourier transform of the source at the frequency `ξ`, as a function of the time.
> - `freqSolution` : The retarded solution at the spatial frequency `ξ`, with zero data at the time
>   `a`.
> - `freqSolution1` : The time derivative of the per-frequency solution.
> - `solution` : The retarded solution of the Klein–Gordon equation with the source `f`.
>
> Lemmas: `continuous_sourceHat`, `freqSolution_eq`, `hasDerivAt_freqSolution`,
> `hasDerivAt_freqSolution1`, `norm_freqSolution1_le`, `norm_freqSolution_le`,
> `continuous_freqSolution_xi`, `continuous_freqSolution1_xi`, `hasDerivAt_solution_time`,
> `hasDerivAt_solution_time1` and more.

## B. Causal support of the retarded solution

> - `advancedSolution` : The advanced solution: the retarded solution of the time-reflected source,
>   reflected back.
>
> Lemmas: `propagatedSlice_eq_sineEvolution`, `advancedSolution_equation`,
> `integrableOn_sineEvolution_slice`, `solution_eq_integral`, `solution_add`, `solution_smul`.

## C. The two-sided Klein–Gordon inverse on compact test fields

> - `testOperator` : The Klein–Gordon operator `∂ₜ² - Δ + μ` on compact spacetime test fields.
>
> Lemmas: `slice_testOperator`, `testOperator_apply`, `fourier_frequencySqOperator`,
> `sourceHat_testOperator`, `freqSolution_testOperator`, `solution_testOperator`,
> `solution_equation_at`, `testOperator_reflect`, `advancedSolution_testOperator`.

**`KleinGordon.sourceHat`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L91).

> The Fourier transform of the source at the frequency `ξ`, as a function of the time.

```lean
def sourceHat (ξ : E) (s : ℝ) : F
```

**`KleinGordon.continuous_sourceHat`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L94).

```lean
lemma continuous_sourceHat (ξ : E) : Continuous (sourceHat F f ξ)
```

**`KleinGordon.freqSolution`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L98).

> The retarded solution at the spatial frequency `ξ`, with zero data at the time `a`.

```lean
def freqSolution (μ a : ℝ) (ξ : E) (t : ℝ) : F
```

**`KleinGordon.freqSolution_eq`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L102).

```lean
lemma freqSolution_eq (μ a : ℝ) (ξ : E) (t : ℝ) :
    freqSolution F f μ a ξ t = duhamelOsc (dispersion μ ξ) a (sourceHat F f ξ) t
```

**`KleinGordon.freqSolution1`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L109).

> The time derivative of the per-frequency solution.

```lean
def freqSolution1 (μ a : ℝ) (ξ : E) (t : ℝ) : F
```

**`KleinGordon.hasDerivAt_freqSolution`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L112).

```lean
lemma hasDerivAt_freqSolution (μ a : ℝ) (ξ : E) (t : ℝ) :
    HasDerivAt (freqSolution F f μ a ξ) (freqSolution1 F f μ a ξ t) t
```

**`KleinGordon.hasDerivAt_freqSolution1`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L119).

```lean
lemma hasDerivAt_freqSolution1 (μ a : ℝ) (ξ : E) (t : ℝ) :
    HasDerivAt (freqSolution1 F f μ a ξ)
      (sourceHat F f ξ t - (dispersion μ ξ ^ 2) • freqSolution F f μ a ξ t) t
```

**`KleinGordon.norm_freqSolution1_le`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L133).

```lean
lemma norm_freqSolution1_le {K N : ℝ} (hK : ∀ (ξ : E) s, ‖sourceHat F f ξ s‖ ≤ K * (1 + ‖ξ‖) ^ (-N))
    (μ a : ℝ) (ξ : E) (t : ℝ) :
    ‖freqSolution1 F f μ a ξ t‖ ≤ K * (1 + ‖ξ‖) ^ (-N) * |t - a|
```

**`KleinGordon.norm_freqSolution_le`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L146).

```lean
lemma norm_freqSolution_le {K N : ℝ} (hK : ∀ (ξ : E) s, ‖sourceHat F f ξ s‖ ≤ K * (1 + ‖ξ‖) ^ (-N))
    (μ a : ℝ) (ξ : E) (t : ℝ) :
    ‖freqSolution F f μ a ξ t‖ ≤ K * (1 + ‖ξ‖) ^ (-N) * |t - a| * |t - a|
```

**`KleinGordon.continuous_freqSolution_xi`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L173).

```lean
lemma continuous_freqSolution_xi (μ a t : ℝ) : Continuous fun ξ : E => freqSolution F f μ a ξ
    t
```

**`KleinGordon.continuous_freqSolution1_xi`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L185).

```lean
lemma continuous_freqSolution1_xi (μ a t : ℝ) : Continuous fun ξ : E => freqSolution1 F f μ a ξ
    t
```

**`KleinGordon.hasDerivAt_solution_time`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L197).

> The first time derivative of the Fourier integral of the retarded solution.

```lean
lemma hasDerivAt_solution_time {μ : ℝ} (a t : ℝ) (x : E) :
    HasDerivAt (fun t' => ∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) • freqSolution F f μ a ξ t')
      (∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) • freqSolution1 F f μ a ξ t) t
```

**`KleinGordon.hasDerivAt_solution_time1`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L250).

> The second time derivative of the Fourier integral: the source minus `ω²` times the solution.

```lean
lemma hasDerivAt_solution_time1 {μ : ℝ} (hμ : 0 ≤ μ) (a t : ℝ) (x : E) :
    HasDerivAt (fun t' => ∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) • freqSolution1 F f μ a ξ t')
      (∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) •
        (sourceHat F f ξ t - (dispersion μ ξ ^ 2) • freqSolution F f μ a ξ t)) t
```

**`KleinGordon.integral_sourceHat`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L353).

> Fourier inversion for the source: the inverse Fourier integral of the Fourier transformed
> slice is the source.

```lean
lemma integral_sourceHat (t : ℝ) (x : E) :
    ∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) • sourceHat F f ξ t = f (t, x)
```

**`KleinGordon.integrable_norm_pow_mul_freqSolution`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L363).

> The weighted per-frequency solution is integrable in the frequency.

```lean
lemma integrable_norm_pow_mul_freqSolution (μ a t : ℝ) {n : ℕ} (hn : n ≤ 2) :
    MeasureTheory.Integrable (fun ξ : E => ‖ξ‖ ^ n * ‖freqSolution F f μ a ξ t‖)
      MeasureTheory.volume
```

**`KleinGordon.solution`**, a def, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L397).

> The retarded solution of the Klein–Gordon equation with the source `f`.

```lean
def solution (μ : ℝ) (t : ℝ) (x : E) : F
```

**`KleinGordon.solution_eq`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L401).

```lean
lemma solution_eq {μ : ℝ} {a : ℝ} (ha : ∀ s ≤ a, s ∉ Prod.fst '' tsupport f) {t : ℝ}
    (hat : a ≤ t) (x : E) :
    solution F f μ t x = ∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) • freqSolution F f μ a ξ t
```

**`KleinGordon.solution_equation`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L411).

> The retarded solution solves the Klein–Gordon equation `(∂ₜ² - Δ + μ) u = f`.

```lean
lemma solution_equation {μ : ℝ} (hμ : 0 ≤ μ) {a : ℝ}
    (ha : ∀ s ≤ a, s ∉ Prod.fst '' tsupport f) {t : ℝ} (hat : a < t) (x : E) :
    deriv (deriv fun τ => solution F f μ τ x) t - Δ (fun y => solution F f μ t y) x +
        μ • solution F f μ t x = f (t, x)
```

**`KleinGordon.propagatedSlice_eq_sineEvolution`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L527).

```lean
lemma propagatedSlice_eq_sineEvolution {μ : ℝ} (hμ : 0 ≤ μ) (r s : ℝ) (x : E) :
    propagatedSlice F f (fun r ξ => multiplier r μ ξ) r s x =
      sineEvolution F r μ (slice F f s) x
```

**`KleinGordon.advancedSolution`**, a def, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L534).

> The advanced solution: the retarded solution of the time-reflected source, reflected back.

```lean
def advancedSolution (μ : ℝ) (t : ℝ) (x : E) : F
```

**`KleinGordon.advancedSolution_equation`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L537).

> The advanced solution solves the Klein–Gordon equation `(∂ₜ² - Δ + μ) u = f`.

```lean
lemma advancedSolution_equation {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (x : E) :
    deriv (deriv fun τ => advancedSolution F f μ τ x) t -
      Δ (fun y => advancedSolution F f μ t y) x + μ • advancedSolution F f μ t x = f (t, x)
```

**`KleinGordon.integrableOn_sineEvolution_slice`**, a lemma, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L557).

```lean
lemma integrableOn_sineEvolution_slice {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (x : E) :
    MeasureTheory.IntegrableOn (fun s => sineEvolution F (t - s) μ (slice F f s) x)
      (Set.Iic t)
```

**`KleinGordon.solution_eq_integral`**, a lemma, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L567).

```lean
lemma solution_eq_integral {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (x : E) :
    solution F f μ t x = ∫ s in Set.Iic t, sineEvolution F (t - s) μ (slice F f s) x
```

**`KleinGordon.solution_add`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L573).

```lean
lemma solution_add {μ : ℝ} (hμ : 0 ≤ μ) (g : 𝓓((⊤ : Opens (ℝ × E)), F)) (t : ℝ) (x : E) :
    solution F (f + g) μ t x = solution F f μ t x + solution F g μ t x
```

**`KleinGordon.solution_smul`**, a lemma, [line 580](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L580).

```lean
lemma solution_smul {μ : ℝ} (hμ : 0 ≤ μ) (c : ℝ) (t : ℝ) (x : E) :
    solution F (c • f) μ t x = c • solution F f μ t x
```

**`KleinGordon.testOperator`**, a def, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L588).

> The Klein–Gordon operator `∂ₜ² - Δ + μ` on compact spacetime test fields.

```lean
def testOperator (μ : ℝ) : 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`KleinGordon.slice_testOperator`**, a lemma, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L591).

```lean
lemma slice_testOperator (μ s : ℝ) :
    slice F (testOperator F f μ) s = slice F (dt F (dt F f)) s +
      frequencySqOperator F μ (slice F f s)
```

**`KleinGordon.testOperator_apply`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L603).

> The compact source operator agrees pointwise with the Klein–Gordon differential expression.

```lean
lemma testOperator_apply (μ t : ℝ) (x : E) :
    testOperator F f μ (t, x) = deriv (deriv (fun s => f (s, x))) t -
      (Δ (fun y => f (t, y))) x + μ • f (t, x)
```

**`KleinGordon.fourier_frequencySqOperator`**, a lemma, [line 616](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L616).

```lean
lemma fourier_frequencySqOperator (μ : ℝ) (g : 𝓢(E, F)) (ξ : E) :
    𝓕 (frequencySqOperator F μ g) ξ = frequencySq μ ξ • 𝓕 g ξ
```

**`KleinGordon.sourceHat_testOperator`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L623).

> The compact test-field operator becomes the forced oscillator operator at each frequency.

```lean
lemma sourceHat_testOperator {μ : ℝ} (hμ : 0 ≤ μ) (ξ : E) (s : ℝ) :
    sourceHat F (testOperator F f μ) ξ s =
      sourceHat F (dt F (dt F f)) ξ s + dispersion μ ξ ^ 2 • sourceHat F f ξ s
```

**`KleinGordon.freqSolution_testOperator`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L633).

> The retarded Fourier mode recovers a test field with vanishing initial Cauchy data.

```lean
lemma freqSolution_testOperator {μ : ℝ} (hμ : 0 ≤ μ) (ξ : E) (a t : ℝ)
    (ha : a ∉ Prod.fst '' tsupport f) (ha' : a ∉ Prod.fst '' tsupport (dt F f)) :
    freqSolution F (testOperator F f μ) μ a ξ t = sourceHat F f ξ t
```

**`KleinGordon.solution_testOperator`**, a lemma, [line 650](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L650).

> Applying the retarded Green operator to the Klein–Gordon source of a compact test field
> recovers that field.

```lean
lemma solution_testOperator {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (x : E) :
    solution F (testOperator F f μ) μ t x = f (t, x)
```

**`KleinGordon.solution_equation_at`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L669).

> The retarded field solves the sourced equation at every spacetime point.

```lean
lemma solution_equation_at {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (x : E) :
    deriv (deriv (fun s => solution F f μ s x)) t -
      (Δ (fun y => solution F f μ t y)) x + μ • solution F f μ t x = f (t, x)
```

**`KleinGordon.testOperator_reflect`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L680).

> Time reflection commutes with the compact Klein–Gordon operator.

```lean
lemma testOperator_reflect (μ : ℝ) :
    testOperator F (reflect F f) μ = reflect F (testOperator F f μ)
```

**`KleinGordon.advancedSolution_testOperator`**, a lemma, [line 688](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean#L688).

> Applying the advanced Green operator to the Klein–Gordon source of a compact test field
> recovers that field.

```lean
lemma advancedSolution_testOperator {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (x : E) :
    advancedSolution F (testOperator F f μ) μ t x = f (t, x)
```

## Depends on

- [The free evolution](freeevolution.md)
- [The Duhamel integral of Fourier multiplied slices](../../../mathematics/part-02/distribution/duhamel.md)
- [The harmonic oscillator](../../../mathematics/part-02/specialfunctions/sincpropagator-oscillator.md)

## Proof depends on

- [Smoothness and bounds of time slices](../../../mathematics/part-02/distribution/timeslicesmooth.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/RetardedSolution.lean)
