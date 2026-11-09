---
declaration: def
origin: cited
lean: LowerUnsignedLebesgueIntegral, UpperUnsignedLebesgueIntegral, LowerUnsignedLebesgueIntegral.eq_simpleIntegral, LowerUnsignedLebesgueIntegral.mono, LowerUnsignedLebesgueIntegral.hom, LowerUnsignedLebesgueIntegral.integral_eq_integral_of_aeEqual, LowerUnsignedLebesgueIntegral.superadditive, UpperUnsignedLebesgueIntegral.subadditive, LowerUnsignedLebesgueIntegral.eq_add, LowerUnsignedLebesgueIntegral.eq_lim_vert_trunc, LowerUnsignedLebesgueIntegral.eq_lim_horiz_trunc, LowerUnsignedLebesgueIntegral.sum_of_reflect_eq, UnsignedLebesgueIntegral, LowerUnsignedLebesgueIntegral.eq_upperIntegral, LowerUnsignedLebesgueIntegral.add, UpperUnsignedLebesgueIntegral.eq_outer_measure_integral, LowerUnsignedLebesgueIntegral.eq_area, UnsignedLebesgueIntegral.unique, UnsignedLebesgueIntegral.trans, UnsignedLebesgueIntegral.comp_linear, RiemannIntegral.eq_UnsignedLebesgueIntegral, UnsignedLebesgueIntegral.markov_inequality, UnsignedLebesgueIntegral.ae_finite, UnsignedLebesgueIntegral.eq_zero_aeZero
statement: formalized
---

# Section 1.3.3: Unsigned Lebesgue integrals

> A companion to (the introduction to) Section 1.3.3 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_3_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 23 labelled items, carried by 24 declarations: 1 proved here, 20 stated without proof (19 of them exercises) and 3 definitions. It also has 12 declarations with no label, counted here but not shown.

## Definition 1.3.12

`LowerUnsignedLebesgueIntegral` (def, [line 11](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L11)). A definition.

> Definition 1.3.12 (Lower unsigned Lebesgue integral)

```lean
noncomputable def LowerUnsignedLebesgueIntegral {d:ℕ} (f: EuclideanSpace' d → EReal) : EReal
```

`UpperUnsignedLebesgueIntegral` (def, [line 15](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L15)). A definition.

> Definition 1.3.12 (Upper unsigned Lebesgue integral)

```lean
noncomputable def UpperUnsignedLebesgueIntegral {d:ℕ} (f: EuclideanSpace' d → EReal) : EReal
```

## Exercise 1.3.10(i)

`LowerUnsignedLebesgueIntegral.eq_simpleIntegral` (theorem, [line 126](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L126)). An exercise, stated without proof.

> Exercise 1.3.10(i) (Compatibility with the simple integral)

```lean
theorem LowerUnsignedLebesgueIntegral.eq_simpleIntegral {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) :
    LowerUnsignedLebesgueIntegral f = hf.integ
```

## Exercise 1.3.10(ii)

`LowerUnsignedLebesgueIntegral.mono` (theorem, [line 130](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L130)). An exercise, stated without proof.

> Exercise 1.3.10(ii) (Monotonicity)

```lean
theorem LowerUnsignedLebesgueIntegral.mono {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g)
    (hfg: AlmostAlways (fun x ↦ f x ≤ g x)) :
    LowerUnsignedLebesgueIntegral f ≤ LowerUnsignedLebesgueIntegral g
```

## Exercise 1.3.10(iii)

`LowerUnsignedLebesgueIntegral.hom` (theorem, [line 135](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L135)). An exercise, stated without proof.

> Exercise 1.3.10(iii) (Homogeneity)

```lean
theorem LowerUnsignedLebesgueIntegral.hom {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) {c: ℝ} (hc: 0 ≤ c) :
    LowerUnsignedLebesgueIntegral ((c:EReal) • f) = c * LowerUnsignedLebesgueIntegral f
```

## Exercise 1.3.10(iv)

`LowerUnsignedLebesgueIntegral.integral_eq_integral_of_aeEqual` (theorem, [line 139](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L139)). An exercise, stated without proof.

> Exercise 1.3.10(iv) (Equivalence)

```lean
theorem LowerUnsignedLebesgueIntegral.integral_eq_integral_of_aeEqual {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g)
    (heq: AlmostEverywhereEqual f g) :
    LowerUnsignedLebesgueIntegral f = LowerUnsignedLebesgueIntegral g
```

## Exercise 1.3.10(v)

`LowerUnsignedLebesgueIntegral.superadditive` (theorem, [line 144](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L144)). An exercise, stated without proof.

> Exercise 1.3.10(v) (Superadditivity)

```lean
theorem LowerUnsignedLebesgueIntegral.superadditive {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g) :
    LowerUnsignedLebesgueIntegral (f + g) ≥ LowerUnsignedLebesgueIntegral f + LowerUnsignedLebesgueIntegral g
```

## Exercise 1.3.10(vi)

`UpperUnsignedLebesgueIntegral.subadditive` (theorem, [line 148](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L148)). An exercise, stated without proof.

> Exercise 1.3.10(vi) (Subadditivity of upper integral).

```lean
theorem UpperUnsignedLebesgueIntegral.subadditive {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g) :
    UpperUnsignedLebesgueIntegral (f + g) ≤ UpperUnsignedLebesgueIntegral f + UpperUnsignedLebesgueIntegral g
```

## Exercise 1.3.10(vii)

`LowerUnsignedLebesgueIntegral.eq_add` (theorem, [line 152](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L152)). An exercise, stated without proof.

> Exercise 1.3.10(vii) (Divisibility)

```lean
theorem LowerUnsignedLebesgueIntegral.eq_add {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E) :
    LowerUnsignedLebesgueIntegral f = LowerUnsignedLebesgueIntegral (f * Real.toEReal ∘ E.indicator') +
      LowerUnsignedLebesgueIntegral (f * Real.toEReal ∘ Eᶜ.indicator')
```

## Exercise 1.3.10(viii)

`LowerUnsignedLebesgueIntegral.eq_lim_vert_trunc` (theorem, [line 157](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L157)). An exercise, stated without proof.

> Exercise 1.3.10(viii) (Vertical truncation).

```lean
theorem LowerUnsignedLebesgueIntegral.eq_lim_vert_trunc {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) : Filter.atTop.Tendsto (fun n:ℕ ↦ LowerUnsignedLebesgueIntegral (fun x ↦ min (f x) n)) (nhds (LowerUnsignedLebesgueIntegral f))
```

## Exercise 1.3.10(ix)

`LowerUnsignedLebesgueIntegral.eq_lim_horiz_trunc` (theorem, [line 164](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L164)). An exercise, stated without proof.

> Exercise 1.3.10(ix) (Horizontal truncation).

```lean
theorem LowerUnsignedLebesgueIntegral.eq_lim_horiz_trunc {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) : Filter.atTop.Tendsto (fun n:ℕ ↦ LowerUnsignedLebesgueIntegral (f * Real.toEReal ∘ (Metric.ball 0 n).indicator')) (nhds (LowerUnsignedLebesgueIntegral f))
```

## Exercise 1.3.10(x)

`LowerUnsignedLebesgueIntegral.sum_of_reflect_eq` (theorem, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L171)). An exercise, stated without proof.

> Exercise 1.3.10(x) (Reflection)

```lean
theorem LowerUnsignedLebesgueIntegral.sum_of_reflect_eq {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g)
    (hfg: UnsignedSimpleFunction (f+g)) (hbound: EReal.BoundedFunction (f + g)) (hsupport: FiniteMeasureSupport (f + g)) :
    hfg.integ = LowerUnsignedLebesgueIntegral f + LowerUnsignedLebesgueIntegral g
```

## Definition 1.3.13

`UnsignedLebesgueIntegral` (def, [line 176](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L176)). A definition.

> Definition 1.3.13 (Unsigned Lebesgue integral).  For Lean purposes it is convenient to assign a "junk" value to this integral when f is not unsigned measurable.

```lean
noncomputable def UnsignedLebesgueIntegral {d:ℕ} (f: EuclideanSpace' d → EReal): EReal
```

## Exercise 1.3.11

`LowerUnsignedLebesgueIntegral.eq_upperIntegral` (theorem, [line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L181)). An exercise, stated without proof.

> Exercise 1.3.11

```lean
theorem LowerUnsignedLebesgueIntegral.eq_upperIntegral {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hbound: EReal.BoundedFunction f) (hsupp: FiniteMeasureSupport f) :
    LowerUnsignedLebesgueIntegral f = UpperUnsignedLebesgueIntegral f
```

## Corollary 1.3.14

`LowerUnsignedLebesgueIntegral.add` (theorem, [line 245](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L245)). Proved here.

> Corollary 1.3.14 (Finite additivity of Lebesgue integral ).

```lean
theorem LowerUnsignedLebesgueIntegral.add {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g)
    (hfg: UnsignedMeasurable (f + g)) :
    LowerUnsignedLebesgueIntegral (f + g) = LowerUnsignedLebesgueIntegral f + LowerUnsignedLebesgueIntegral g
```

## Exercise 1.3.12

`UpperUnsignedLebesgueIntegral.eq_outer_measure_integral` (theorem, [line 299](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L299)). An exercise, stated without proof.

> Exercise 1.3.12 (Upper Lebesgue integral and outer measure).

```lean
theorem UpperUnsignedLebesgueIntegral.eq_outer_measure_integral {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E) :
    UpperUnsignedLebesgueIntegral (Real.toEReal ∘ E.indicator') = Lebesgue_outer_measure E
```

## Exercise 1.3.13

`LowerUnsignedLebesgueIntegral.eq_area` (theorem, [line 309](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L309)). An exercise, stated without proof.

> Exercise 1.3.13 (Area interpretation of integral).

```lean
theorem LowerUnsignedLebesgueIntegral.eq_area {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) :
    LowerUnsignedLebesgueIntegral f = Lebesgue_measure { p | ∃ x, ∃ t:ℝ, EuclideanSpace'.prod_equiv d 1 p = ⟨ x, t ⟩ ∧ 0 ≤ t ∧ t ≤ f x }
```

## Exercise 1.3.14

`UnsignedLebesgueIntegral.unique` (theorem, [line 313](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L313)). An exercise, stated without proof.

> Exercise 1.3.14 (Uniqueness)

```lean
theorem UnsignedLebesgueIntegral.unique {d:ℕ} (integ: (EuclideanSpace' d → EReal) → EReal)
  (hsimple : ∀ f (hf: UnsignedSimpleFunction f), integ f = hf.integ)
  (hadd: ∀ f g (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g), integ (f + g) = integ f + integ g)
  (hvert: ∀ f (hf: UnsignedMeasurable f), Filter.atTop.Tendsto (fun n:ℕ ↦ integ (fun x ↦ min (f x) n)) (nhds (integ f)))
  (hhoriz: ∀ f (hf: UnsignedMeasurable f), Filter.atTop.Tendsto (fun n:ℕ ↦ integ (f * Real.toEReal ∘ (Metric.ball 0 n).indicator')) (nhds (integ f)))
  : ∀ f, UnsignedMeasurable f → integ f = UnsignedLebesgueIntegral f
```

## Exercise 1.3.15

`UnsignedLebesgueIntegral.trans` (theorem, [line 321](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L321)). An exercise, stated without proof.

> Exercise 1.3.15 (Translation invariance).

```lean
theorem UnsignedLebesgueIntegral.trans {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (a: EuclideanSpace' d) :
    UnsignedLebesgueIntegral (fun x ↦ f (x + a)) = hf.integ
```

## Exercise 1.3.16

`UnsignedLebesgueIntegral.comp_linear` (theorem, [line 325](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L325)). An exercise, stated without proof.

> Exercise 1.3.16 (Linear change of variables).

```lean
theorem UnsignedLebesgueIntegral.comp_linear {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (A: EuclideanSpace' d →ₗ[ℝ] EuclideanSpace' d) (hA: A.det ≠ 0) :
    UnsignedLebesgueIntegral (fun x ↦ f (A x)) = |A.det|⁻¹ * hf.integ
```

## Exercise 1.3.17

`RiemannIntegral.eq_UnsignedLebesgueIntegral` (theorem, [line 329](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L329)). An exercise, stated without proof.

> Exercise 1.3.17 (Compatibility with the Riemann integral).

```lean
theorem RiemannIntegral.eq_UnsignedLebesgueIntegral {I: BoundedInterval} {f: ℝ → ℝ}
    (hf: RiemannIntegrableOn f I) (hnonneg: ∀ x ∈ I.toSet, 0 ≤ f x) :
    (riemannIntegral f I : EReal) = UnsignedLebesgueIntegral (Real.toEReal ∘ (fun x ↦ (f x) * (I.toSet.indicator' x)) ∘ EuclideanSpace'.equiv_Real)
```

## Lemma 1.3.15

`UnsignedLebesgueIntegral.markov_inequality` (theorem, [line 334](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L334)). Stated without proof.

> Lemma 1.3.15 (Markov's inequality)

```lean
theorem UnsignedLebesgueIntegral.markov_inequality {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) {t:ℝ} (ht: 0 < t) :
    Lebesgue_measure { x | f x ≥ t } ≤ hf.integ / (t:EReal)
```

## Exercise 1.3.18 (ii)

`UnsignedLebesgueIntegral.ae_finite` (theorem, [line 339](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L339)). An exercise, stated without proof.

> Exercise 1.3.18 (ii)

```lean
theorem UnsignedLebesgueIntegral.ae_finite {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hfin: UnsignedLebesgueIntegral f < ⊤) :
    AlmostAlways (fun x ↦ f x < ⊤)
```

## Exercise 1.3.18 (iii)

`UnsignedLebesgueIntegral.eq_zero_aeZero` (theorem, [line 345](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean#L345)). An exercise, stated without proof.

> Exercise 1.3.18 (iii)

```lean
theorem UnsignedLebesgueIntegral.eq_zero_aeZero {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) :
     hf.integ = 0 ↔ AlmostAlways (fun x ↦ f x = 0)
```

## Depends on

- [Section 1.3.2: Measurable functions](section-1-3-2.md)

## Sources

- [Analysis/MeasureTheory/Section_1_3_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_3.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_3_3.html)
