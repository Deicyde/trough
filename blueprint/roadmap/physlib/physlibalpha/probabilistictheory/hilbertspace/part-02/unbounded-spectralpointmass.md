---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_fst_le_snd, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_sub, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_fst_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_snd_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_subset, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_fst_le_snd
statement: formalized
proof: formalized
---

# Spectral measures taking values `0` and `1`

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.SpectralPointMass`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean): 31 declarations, 9 with a docstring.

> A `{0, 1}`-valued spectral measure on `ℝ` with bounded support is a point mass.

## i. Overview

> A measure on `ℝ` with bounded support that only takes the values `0` and `1` is a point mass.
> Bisecting the support and keeping the half of measure `1` gives nested intervals shrinking to the
> point. As a consequence, a bounded self-adjoint operator all of whose spectral projections are `0`
> or `1` is a scalar multiple of the identity.

## ii. Key results

> - `WOTSpectralMeasure.bisect` : the nested bisection intervals.
> - `WOTSpectralMeasure.bisectPoint` : the point the bisection intervals shrink to.
> - `WOTSpectralMeasure.exists_forall_notMem_measure_eq_zero` : such a measure vanishes on every set
>   avoiding some point `r`.
> - `eq_smul_one_of_forall_spectralMeasure_eq_zero_or_one` : a bounded self-adjoint operator with
>   only trivial spectral projections is a scalar multiple of the identity.

## iv. References

> * None.

## A. Bisection intervals

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L70).

> One bisection step: split `[p.1, p.2]` at its midpoint and keep the left half if it has measure
> `1`, otherwise the right half.

```lean
noncomputable def bisectStep (p : ℝ × ℝ) : ℝ × ℝ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L75).

> The `n`-th bisection interval's endpoints, starting from `(a, b)`.

```lean
noncomputable def bisect (a b : ℝ) : ℕ → ℝ × ℝ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_fst_le_snd`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L79).

```lean
lemma bisectStep_fst_le_snd {p : ℝ × ℝ} (h : p.1 ≤ p.2) :
    (bisectStep μ p).1 ≤ (bisectStep μ p).2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_sub`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L84).

```lean
lemma bisectStep_sub (p : ℝ × ℝ) :
    (bisectStep μ p).2 - (bisectStep μ p).1 = (p.2 - p.1) / 2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_fst_le`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L89).

```lean
lemma bisectStep_fst_le {p : ℝ × ℝ} (h : p.1 ≤ p.2) : p.1 ≤ (bisectStep μ p).1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_snd_le`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L92).

```lean
lemma bisectStep_snd_le {p : ℝ × ℝ} (h : p.1 ≤ p.2) : (bisectStep μ p).2 ≤ p.2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_subset`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L95).

```lean
lemma bisectStep_subset {p : ℝ × ℝ} (h : p.1 ≤ p.2) :
    Icc (bisectStep μ p).1 (bisectStep μ p).2 ⊆ Icc p.1 p.2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_fst_le_snd`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L99).

```lean
lemma bisect_fst_le_snd {a b : ℝ} (hab : a ≤ b) :
    ∀ n, (bisect μ a b n).1 ≤ (bisect μ a b n).2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_sub`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L104).

```lean
lemma bisect_sub (a b : ℝ) :
    ∀ n, (bisect μ a b n).2 - (bisect μ a b n).1 = (b - a) / 2 ^ n
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_fst_mono`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L112).

```lean
lemma bisect_fst_mono {a b : ℝ} (hab : a ≤ b) (n : ℕ) :
    (bisect μ a b n).1 ≤ (bisect μ a b (n + 1)).1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_snd_mono`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L116).

```lean
lemma bisect_snd_mono {a b : ℝ} (hab : a ≤ b) (n : ℕ) :
    (bisect μ a b (n + 1)).2 ≤ (bisect μ a b n).2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_subset`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L120).

```lean
lemma bisect_subset {a b : ℝ} (hab : a ≤ b) (n : ℕ) :
    Icc (bisect μ a b (n + 1)).1 (bisect μ a b (n + 1)).2 ⊆
      Icc (bisect μ a b n).1 (bisect μ a b n).2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectStep_measure_one`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L127).

> If the whole interval has measure `1`, the bisected interval does too: whichever half
> `bisectStep` keeps is forced to have measure `1` by additivity across the (disjoint) split.

```lean
lemma bisectStep_measure_one (h01 : ∀ E : Set ℝ, MeasurableSet E → μ E = 0 ∨ μ E = 1)
    {p : ℝ × ℝ} (h : p.1 ≤ p.2) (hμ : μ (Icc p.1 p.2) = 1) :
    μ (Icc (bisectStep μ p).1 (bisectStep μ p).2) = 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_measure_one`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L155).

```lean
lemma bisect_measure_one (h01 : ∀ E : Set ℝ, MeasurableSet E → μ E = 0 ∨ μ E = 1)
    {a b : ℝ} (hab : a ≤ b) (hμ : μ (Icc a b) = 1) :
    ∀ n, μ (Icc (bisect μ a b n).1 (bisect μ a b n).2) = 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisect_diff_measure_zero`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L163).

> The half discarded at each bisection step has measure `0`.

```lean
lemma bisect_diff_measure_zero
    (h01 : ∀ E : Set ℝ, MeasurableSet E → μ E = 0 ∨ μ E = 1)
    {a b : ℝ} (hab : a ≤ b) (hμ : μ (Icc a b) = 1) (n : ℕ) :
    μ (Icc (bisect μ a b n).1 (bisect μ a b n).2 \
        Icc (bisect μ a b (n + 1)).1 (bisect μ a b (n + 1)).2) = 0
```

## B. The limit point of the bisection

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectFst_mono`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L183).

```lean
lemma bisectFst_mono (hab : a ≤ b) : Monotone (fun n => (bisect μ a b n).1)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectSnd_anti`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L186).

```lean
lemma bisectSnd_anti (hab : a ≤ b) : Antitone (fun n => (bisect μ a b n).2)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectSnd_le_start`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L189).

```lean
lemma bisectSnd_le_start (hab : a ≤ b) (n : ℕ) : (bisect μ a b n).2 ≤ b
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectFst_ge_start`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L192).

```lean
lemma bisectFst_ge_start (hab : a ≤ b) (n : ℕ) : a ≤ (bisect μ a b n).1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bddAbove_bisectFst`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L195).

```lean
lemma bddAbove_bisectFst (hab : a ≤ b) :
    BddAbove (Set.range (fun n => (bisect μ a b n).1))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bddBelow_bisectSnd`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L199).

```lean
lemma bddBelow_bisectSnd (hab : a ≤ b) :
    BddBelow (Set.range (fun n => (bisect μ a b n).2))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectPoint`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L204).

> The limit point of the bisection.

```lean
noncomputable def bisectPoint (_hab : a ≤ b) : ℝ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.tendsto_bisectFst`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L206).

```lean
lemma tendsto_bisectFst (hab : a ≤ b) :
    Tendsto (fun n => (bisect μ a b n).1) atTop (𝓝 (bisectPoint μ hab))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.tendsto_bisectSub`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L210).

```lean
lemma tendsto_bisectSub (a b : ℝ) :
    Tendsto (fun n => (bisect μ a b n).2 - (bisect μ a b n).1) atTop (𝓝 0)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.tendsto_bisectSnd`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L218).

```lean
lemma tendsto_bisectSnd (hab : a ≤ b) :
    Tendsto (fun n => (bisect μ a b n).2) atTop (𝓝 (bisectPoint μ hab))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectFst_le_bisectPoint`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L225).

```lean
lemma bisectFst_le_bisectPoint (hab : a ≤ b) (n : ℕ) :
    (bisect μ a b n).1 ≤ bisectPoint μ hab
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bisectPoint_le_bisectSnd`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L229).

```lean
lemma bisectPoint_le_bisectSnd (hab : a ≤ b) (n : ℕ) :
    bisectPoint μ hab ≤ (bisect μ a b n).2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.iInter_bisectIcc`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L236).

> The bisection intervals shrink to exactly the bisection point.

```lean
lemma iInter_bisectIcc (hab : a ≤ b) :
    ⋂ n, Icc (bisect μ a b n).1 (bisect μ a b n).2 = {bisectPoint μ hab}
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measure_singleton_bisectPoint`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L255).

> **The bisection point carries the full measure.** Since every bisection interval has measure
> `1` and the intervals shrink to exactly `{bisectPoint}`, continuity from above (`Mathlib`'s
> `tendsto_vectorMeasure_iInter_atTop_nat`) forces `μ {bisectPoint} = 1`.

```lean
lemma measure_singleton_bisectPoint
    (h01 : ∀ E : Set ℝ, MeasurableSet E → μ E = 0 ∨ μ E = 1) (hab : a ≤ b)
    (hμ : μ (Icc a b) = 1) :
    μ {bisectPoint μ hab} = 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.exists_forall_notMem_measure_eq_zero`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L272).

> **A `{0, 1}`-valued measure with bounded support is a point mass**: every measurable set
> avoiding some point `r` has measure `0`.

```lean
lemma exists_forall_notMem_measure_eq_zero
    (h01 : ∀ E : Set ℝ, MeasurableSet E → μ E = 0 ∨ μ E = 1) (hab : a ≤ b)
    (hμ : μ (Icc a b) = 1) :
    ∃ r : ℝ, μ {r} = 1 ∧ ∀ E : Set ℝ, MeasurableSet E → r ∉ E → μ E = 0
```

## C. Operators with trivial spectral projections

**`ProbabilisticTheory.QuantumMechanics.eq_smul_one_of_forall_spectralMeasure_eq_zero_or_one`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean#L305).

> **Schur's-lemma capstone.** If every Borel spectral projection of a bounded self-adjoint
> operator `S` is trivial (`0` or `1`), `S` is a scalar multiple of the identity — without ever
> separately identifying `spectrum ℝ S`. Combined with irreducibility forcing every spectral
> projection to be `0` or `1`, this finishes Schur's lemma for a Weyl-family representation.

```lean
lemma eq_smul_one_of_forall_spectralMeasure_eq_zero_or_one
    (S : H →L[ℂ] H) (hSA : IsSelfAdjoint S)
    (h01 : ∀ E : Set ℝ, MeasurableSet E →
      boundedSelfAdjointSpectralMeasure S hSA E = 0 ∨
        boundedSelfAdjointSpectralMeasure S hSA E = 1) :
    ∃ c : ℂ, S = c • (1 : H →L[ℂ] H)
```

## Depends on

- [Spectral measures of bounded self-adjoint operators](unbounded-boundedselfadjointdata.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralPointMass.lean)
