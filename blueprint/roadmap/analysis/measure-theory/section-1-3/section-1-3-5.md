---
declaration: theorem
origin: cited
lean: RealAbsolutelyIntegrable.approx_by_simple, ComplexAbsolutelyIntegrable.approx_by_simple, RealAbsolutelyIntegrable.approx_by_continuous_compact, LocallyUniformlyConvergesTo, LocallyUniformlyConvergesTo.iff, PointwiseAeConvergesTo.locallyUniformlyConverges_outside_small, ComplexAbsolutelyIntegrable.approx_by_continuous_outside_small, LocallyComplexAbsolutelyIntegrable.approx_by_continuous_outside_small, ComplexMeasurable.iff_pointwiseae_of_continuous, UnsignedMeasurable.approx_by_continuous_outside_small, ComplexAbsolutelyIntegrable.almost_bounded_support, ComplexAbsolutelyIntegrable.almost_bounded
statement: formalized
---

# Section 1.3.5: Littlewood's three principles

> A companion to (the introduction to) Section 1.3.5 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_3_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 15 labelled items, carried by 16 declarations: 3 proved here, 12 stated without proof (4 of them exercises) and 1 definition. It also has 13 declarations and 6 examples with no label, counted here but not shown. The docstring labelled Theorem 1.3.20(ii) at line 392 is on a private declaration, which the reading leaves out.

## Theorem 1.3.20(i)

`RealAbsolutelyIntegrable.approx_by_simple` (theorem, [line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L122)). Proved here.

> Theorem 1.3.20(i) Approximation of $L^1$ functions by simple functions (real case)

```lean
theorem RealAbsolutelyIntegrable.approx_by_simple {d:ℕ} {f: EuclideanSpace' d → ℝ} (hf : RealAbsolutelyIntegrable f)
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (g : EuclideanSpace' d → ℝ), RealSimpleFunction g ∧ RealAbsolutelyIntegrable g ∧
    PreL1.norm (f - g) ≤ ε
```

`ComplexAbsolutelyIntegrable.approx_by_simple` (theorem, [line 303](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L303)). Proved here.

> Theorem 1.3.20(i) Approximation of $L^1$ functions by simple functions (complex case)

```lean
theorem ComplexAbsolutelyIntegrable.approx_by_simple {d:ℕ} {f: EuclideanSpace' d → ℂ} (hf : ComplexAbsolutelyIntegrable f)
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (g : EuclideanSpace' d → ℂ), ComplexSimpleFunction g ∧ ComplexAbsolutelyIntegrable g ∧
    PreL1.norm (f - g) ≤ ε
```

## Theorem 1.3.20(iii)

`RealAbsolutelyIntegrable.approx_by_continuous_compact` (theorem, [line 1363](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1363)). Proved here.

> Theorem 1.3.20(iii) Approximation of $L^1$ functions by continuous compactly supported functions

```lean
theorem RealAbsolutelyIntegrable.approx_by_continuous_compact {d:ℕ} {f: EuclideanSpace' d → ℝ} (hf : RealAbsolutelyIntegrable f)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ (g : EuclideanSpace' d → ℝ), Continuous g ∧ CompactlySupported g ∧
        PreL1.norm (f - g) ≤ ε
```

## Definition 1.3.21

`LocallyUniformlyConvergesTo` (def, [line 1488](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1488)). A definition.

> Definition 1.3.21 (Locally uniform convergence)

```lean
def LocallyUniformlyConvergesTo {X Y:Type*} [PseudoMetricSpace X] [PseudoMetricSpace Y] (f: ℕ → X → Y) (g: X → Y) : Prop
```

## Remark 1.3.22

`LocallyUniformlyConvergesTo.iff` (theorem, [line 1492](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1492)). Stated without proof.

> Remark 1.3.22

```lean
theorem LocallyUniformlyConvergesTo.iff {d:ℕ} {Y:Type*} [PseudoMetricSpace Y] (f: ℕ → EuclideanSpace' d → Y) (g: EuclideanSpace' d → Y) :
  LocallyUniformlyConvergesTo f g ↔
  ∀ x₀, ∃ U: Set (EuclideanSpace' d), x₀ ∈ U ∧ IsOpen U ∧ UniformlyConvergesToOn f g U
```

## Example 1.3.23

An `example` ([line 1500](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1500)). Stated without proof.

> Example 1.3.23

```lean
example : LocallyUniformlyConvergesTo (fun n (x:EuclideanSpace' 1) ↦ x.toReal / n) (fun x ↦ 0)
```

## Example 1.3.24

An `example` ([line 1505](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1505)). Stated without proof.

> Example 1.3.24

```lean
example : LocallyUniformlyConvergesTo (fun N (x:EuclideanSpace' 1) ↦ ∑ n ∈ Finset.range N, x.toReal^n / n.factorial) (fun x ↦ x.toReal.exp)
```

## Example 1.3.25

An `example` ([line 1512](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1512)). Stated without proof.

> Example 1.3.25

```lean
example : PointwiseConvergesTo (fun n (x:EuclideanSpace' 1) ↦ if x.toReal > 0 then 1 / (n * x.toReal) else 0) (fun x ↦ 0)
```

## Theorem 1.3.26

`PointwiseAeConvergesTo.locallyUniformlyConverges_outside_small` (theorem, [line 1517](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1517)). Stated without proof.

> Theorem 1.3.26 (Egorov's theorem).

```lean
theorem PointwiseAeConvergesTo.locallyUniformlyConverges_outside_small {d:ℕ} {f : ℕ → EuclideanSpace' d → ℂ} {g : EuclideanSpace' d → ℂ}
  (hf: ∀ n, ComplexMeasurable (f n))
  (hfg: PointwiseAeConvergesTo f g)
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (E: Set (EuclideanSpace' d)), LebesgueMeasurable E ∧
    Lebesgue_measure E ≤ ε ∧
    LocallyUniformlyConvergesToOn f g Eᶜ
```

## Remark 1.3.27

An `example` ([line 1534](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1534)). Stated without proof.

> Remark 1.3.27: Local uniform convergence in Egorov's theorem cannot be upgraded to uniform convergence

```lean
example : ∃ (d:ℕ) (f : ℕ → EuclideanSpace' d → ℝ) (g : EuclideanSpace' d → ℝ),
    (∀ n, RealMeasurable (f n)) ∧
    PointwiseAeConvergesTo f g ∧
    ∃ (ε : ℝ) (hε : 0 < ε),
      ∀ (E: Set (EuclideanSpace' d)), LebesgueMeasurable E ∧
        Lebesgue_measure E ≤ ε →
        ¬ UniformlyConvergesToOn f g Eᶜ
```

## Theorem 1.3.28

`ComplexAbsolutelyIntegrable.approx_by_continuous_outside_small` (theorem, [line 1555](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1555)). Stated without proof.

> Theorem 1.3.28 (Lusin's theorem)

```lean
theorem ComplexAbsolutelyIntegrable.approx_by_continuous_outside_small {d:ℕ} {f : EuclideanSpace' d → ℂ}
  (hf: ComplexAbsolutelyIntegrable f)
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (g : EuclideanSpace' d → ℂ) (E: Set (EuclideanSpace' d)), ContinuousOn g Eᶜ ∧ LebesgueMeasurable E ∧
      Lebesgue_measure E ≤ ε ∧
      ∀ x ∉ E, g x = f x
```

## Exercise 1.3.23

`LocallyComplexAbsolutelyIntegrable.approx_by_continuous_outside_small` (theorem, [line 1572](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1572)). An exercise, stated without proof.

> Exercise 1.3.23 (Lusin's theorem only requires local absolute integrability).

```lean
theorem LocallyComplexAbsolutelyIntegrable.approx_by_continuous_outside_small {d:ℕ} {f : EuclideanSpace' d → ℂ}
  (hf: LocallyComplexAbsolutelyIntegrable f)
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (g : EuclideanSpace' d → ℂ) (E: Set (EuclideanSpace' d)), ContinuousOn g Eᶜ ∧ LebesgueMeasurable E ∧
      Lebesgue_measure E ≤ ε ∧
      ∀ x ∉ E, g x = f x
```

## Exercise 1.3.24

`ComplexMeasurable.iff_pointwiseae_of_continuous` (theorem, [line 1587](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1587)). An exercise, stated without proof.

> Exercise 1.3.24

```lean
theorem ComplexMeasurable.iff_pointwiseae_of_continuous {d:ℕ} {f : EuclideanSpace' d → ℂ} :
  ComplexMeasurable f ↔
  ∃ (g : ℕ → EuclideanSpace' d → ℂ), (∀ n, Continuous (g n)) ∧ PointwiseAeConvergesTo g f
```

## Remark 1.3.29

`UnsignedMeasurable.approx_by_continuous_outside_small` (theorem, [line 1592](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1592)). Stated without proof.

> Remark 1.3.29

```lean
theorem UnsignedMeasurable.approx_by_continuous_outside_small {d:ℕ} {f : EuclideanSpace' d → EReal}
  (hf: UnsignedMeasurable f) (hfin: AlmostAlways (fun x ↦ f x < ⊤))
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (g : EuclideanSpace' d → ℝ) (E: Set (EuclideanSpace' d)), ContinuousOn g Eᶜ ∧ LebesgueMeasurable E ∧
      Lebesgue_measure E ≤ ε ∧
      ∀ x ∉ E, g x = f x
```

## Exercise 1.3.25 (a)

`ComplexAbsolutelyIntegrable.almost_bounded_support` (theorem, [line 1600](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1600)). An exercise, stated without proof.

> Exercise 1.3.25 (a) (Littlewood-like principle)

```lean
theorem ComplexAbsolutelyIntegrable.almost_bounded_support {d:ℕ} {f : EuclideanSpace' d → ℂ}
  (hf: ComplexAbsolutelyIntegrable f)
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (R: ℝ), PreL1.norm (f * Complex.indicator (Metric.ball 0 R)ᶜ) ≤ ε
```

## Exercise 1.3.25 (b)

`ComplexAbsolutelyIntegrable.almost_bounded` (theorem, [line 1608](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean#L1608)). An exercise, stated without proof.

> Exercise 1.3.25 (b) (Littlewood-like principle)

```lean
theorem ComplexAbsolutelyIntegrable.almost_bounded {d:ℕ} {f : EuclideanSpace' d → ℂ}
  (hf: ComplexAbsolutelyIntegrable f)
  (ε : ℝ) (hε : 0 < ε) :
  ∃ (E: Set (EuclideanSpace' d)), LebesgueMeasurable E ∧
    Lebesgue_measure E ≤ ε ∧
    BoundedOn f Eᶜ
```

## Depends on

- [Section 1.3.4: Absolute integrability](section-1-3-4.md)

## Sources

- [Analysis/MeasureTheory/Section_1_3_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_5.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_3_5.html)
