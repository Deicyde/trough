---
declaration: structure
origin: cited
lean: TaggedPartition, riemann_integral_of_integrable, riemann_integral_eq_iff_of_integrable, riemann_integral_eq_iff, RiemannIntegrable.of_zero_length, RiemannIntegrable.bounded, PiecewiseConstantFunction.integral_eq, PiecewiseConstantOn.integral_eq, PiecewiseConstantOn.smul, PiecewiseConstantFunction.integral_smul, PiecewiseConstantOn.add, PiecewiseConstantFunction.integral_add, PiecewiseConstantFunction.integral_mono, PiecewiseConstantOn.indicator_of_elem, PiecewiseConstantFunction.integral_of_elem, LowerDarbouxIntegral, UpperDarbouxIntegral, lower_darboux_le_upper_darboux, DarbouxIntegrableOn, UpperDarbouxIntegral.neg, RiemannIntegrableOn.iff_darbouxIntegrable, riemann_integral_eq_darboux_integral, RiemannIntegrableOn.continuous, RiemannIntegrableOn.piecewise_continuous, RiemannIntegrableOn.smul, riemann_integral_smul, RiemannIntegrableOn.add, riemann_integral_add, riemann_integral_mono, RiemannIntegrableOn.indicator_of_elem, riemann_integral_of_elem, riemann_integral_unique, RiemannIntegrableOn.measurable_upper, RiemannIntegrableOn.measurable_lower, JordanMeasurable.iff_integrable, RiemannIntegrableOn.eq_measure
statement: formalized
---

# Section 1.1.3: Connections with the Riemann integral

> A companion to Section 1.1.3 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_1_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 15 labelled items, carried by 36 declarations: 7 proved here, 25 stated without proof (25 of them exercises) and 4 definitions. It also has 34 declarations with no label, counted here but not shown.

## Definition 1.1.5

`TaggedPartition` (structure, [line 15](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L15)). A definition.

> Definition 1.1.5.  (Riemann integrability) The interval `I` should be closed, though we will not enforce this.  We also permit the length to be 0. We index the tags and deltas starting from 0 rather than 1
> in the text as this is slightly more convenient in Lean.

```lean
structure TaggedPartition (I: BoundedInterval) (n:ℕ)
```

## Definition 1.1.15

`riemann_integral_of_integrable` (lemma, [line 269](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L269)). Proved here.

> Definition 1.1.15 (Riemann integrability, Riemann sums converge)

```lean
lemma riemann_integral_of_integrable {f:ℝ → ℝ} {I: BoundedInterval} (h: RiemannIntegrableOn f I) : riemann_integral_eq f I (riemannIntegral f I)
```

`riemann_integral_eq_iff_of_integrable` (lemma, [line 282](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L282)). Proved here.

> Definition 1.1.15 (Riemann integrability, characterization)

```lean
lemma riemann_integral_eq_iff_of_integrable {f:ℝ → ℝ} {I: BoundedInterval} (h: RiemannIntegrableOn f I) (R:ℝ): riemann_integral_eq f I R ↔ R = riemannIntegral f I
```

`riemann_integral_eq_iff` (lemma, [line 318](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L318)). Proved here.

> Definition 1.1.15 (Riemann integrability).

```lean
lemma riemann_integral_eq_iff {f:ℝ → ℝ} {I: BoundedInterval} (R:ℝ): riemann_integral_eq f I R ↔ ∀ ε>0, ∃ δ>0, ∀ n, ∀ P: TaggedPartition I n, P.norm ≤ δ → |P.RiemannSum f - R| ≤ ε
```

`RiemannIntegrable.of_zero_length` (lemma, [line 435](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L435)). Proved here.

> Definition 1.1.15.  (Riemann integrability)

```lean
lemma RiemannIntegrable.of_zero_length (f: ℝ → ℝ) {I: BoundedInterval} {a : ℝ} (h: I = Icc a a) : RiemannIntegrableOn f I ∧ riemannIntegral f I = 0
```

`RiemannIntegrable.bounded` (theorem, [line 583](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L583)). Proved here.

> Definition 1.1.15

```lean
theorem RiemannIntegrable.bounded {f: ℝ → ℝ} {I: BoundedInterval} (h: RiemannIntegrableOn f I) : ∃ M, ∀ x ∈ I, |f x| ≤ M
```

## Exercise 1.1.20

`PiecewiseConstantFunction.integral_eq` (theorem, [line 757](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L757)). An exercise, stated without proof.

> Exercise 1.1.20 (Piecewise constant functions, integral well-defined)

```lean
theorem PiecewiseConstantFunction.integral_eq (f: ℝ → ℝ) {I: BoundedInterval} (F F': PiecewiseConstantFunction I) (hF: F.agreesWith f) (hF': F'.agreesWith f) : F.integral = F'.integral
```

`PiecewiseConstantOn.integral_eq` (theorem, [line 764](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L764)). An exercise, stated without proof.

> Exercise 1.1.20 (Piecewise constant functions, integral of a representation)

```lean
theorem PiecewiseConstantOn.integral_eq (f: ℝ → ℝ) {I: BoundedInterval} (h: PiecewiseConstantOn f I) (F: PiecewiseConstantFunction I) (hF: F.agreesWith f) : h.integral = F.integral
```

## Exercise 1.1.21 (a)

`PiecewiseConstantOn.smul` (theorem, [line 768](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L768)). An exercise, stated without proof.

> Exercise 1.1.21 (a) (Linearity, scalar multiple is piecewise constant)

```lean
theorem PiecewiseConstantOn.smul {I: BoundedInterval} (c:ℝ) {f: ℝ → ℝ} (h: PiecewiseConstantOn f I) : PiecewiseConstantOn (c • f) I
```

`PiecewiseConstantFunction.integral_smul` (theorem, [line 772](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L772)). An exercise, stated without proof.

> Exercise 1.1.21 (a) (Linearity, integral of a scalar multiple)

```lean
theorem PiecewiseConstantFunction.integral_smul {I:BoundedInterval} (c:ℝ) {f: ℝ → ℝ} (h: PiecewiseConstantOn f I) : (h.smul c).integral = c • h.integral
```

`PiecewiseConstantOn.add` (theorem, [line 776](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L776)). An exercise, stated without proof.

> Exercise 1.1.21 (a) (Linearity, sum is piecewise constant)

```lean
theorem PiecewiseConstantOn.add {I: BoundedInterval} {f g: ℝ → ℝ} (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) : PiecewiseConstantOn (f + g) I
```

`PiecewiseConstantFunction.integral_add` (theorem, [line 780](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L780)). An exercise, stated without proof.

> Exercise 1.1.21 (a) (Linearity, integral of a sum)

```lean
theorem PiecewiseConstantFunction.integral_add {I: BoundedInterval} {f g: ℝ → ℝ} (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) : (hf.add hg).integral = hf.integral + hg.integral
```

## Exercise 1.1.21 (b)

`PiecewiseConstantFunction.integral_mono` (theorem, [line 784](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L784)). An exercise, stated without proof.

> Exercise 1.1.21 (b) (Monotonicity of the piecewise constant integral)

```lean
theorem PiecewiseConstantFunction.integral_mono {I: BoundedInterval} {f g: ℝ → ℝ} (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) (hmono: ∀ x ∈ I.toSet, f x ≤ g x): hf.integral ≤ hg.integral
```

## Exercise 1.1.21 (c)

`PiecewiseConstantOn.indicator_of_elem` (theorem, [line 788](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L788)). An exercise, stated without proof.

> Exercise 1.1.21 (c) (Indicator functions, indicator is piecewise constant)

```lean
theorem PiecewiseConstantOn.indicator_of_elem (I: BoundedInterval) {E:Set ℝ} (hE: IsElementary (Real.equiv_EuclideanSpace' '' E) ) : PiecewiseConstantOn E.indicator' I
```

`PiecewiseConstantFunction.integral_of_elem` (theorem, [line 792](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L792)). An exercise, stated without proof.

> Exercise 1.1.21 (c) (Indicator functions, integral of an indicator)

```lean
theorem PiecewiseConstantFunction.integral_of_elem {I: BoundedInterval} {E:Set ℝ} (hE: IsElementary (Real.equiv_EuclideanSpace' '' E) ) (hsub: E ⊆ I.toSet) : (PiecewiseConstantOn.indicator_of_elem I hE).integral = hE.measure
```

## Definition 1.1.6

`LowerDarbouxIntegral` (def, [line 796](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L796)). A definition.

> Definition 1.1.6 (Darboux integral, lower)

```lean
noncomputable def LowerDarbouxIntegral (f:ℝ → ℝ) (I: BoundedInterval) : ℝ
```

`UpperDarbouxIntegral` (def, [line 800](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L800)). A definition.

> Definition 1.1.6 (Darboux integral, upper)

```lean
noncomputable def UpperDarbouxIntegral (f:ℝ → ℝ) (I: BoundedInterval) : ℝ
```

`lower_darboux_le_upper_darboux` (lemma, [line 911](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L911)). Proved here.

> Definition 1.1.6 (Darboux integral, lower is at most upper)

```lean
lemma lower_darboux_le_upper_darboux {f:ℝ → ℝ} {I: BoundedInterval} (hbound: ∃ M, ∀ x ∈ I, |f x| ≤ M) : LowerDarbouxIntegral f I ≤ UpperDarbouxIntegral f I
```

`DarbouxIntegrableOn` (def, [line 948](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L948)). A definition.

> Definition 1.1.6 (Darboux integral, integrability)

```lean
noncomputable def DarbouxIntegrableOn (f:ℝ → ℝ) (I: BoundedInterval) : Prop
```

`UpperDarbouxIntegral.neg` (lemma, [line 978](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L978)). Proved here.

> Definition 1.1.6 (Darboux integral, negation)

```lean
lemma UpperDarbouxIntegral.neg {f:ℝ → ℝ} {I: BoundedInterval} (hbound: ∃ M, ∀ x ∈ I, |f x| ≤ M) : UpperDarbouxIntegral (-f) I = -LowerDarbouxIntegral f I
```

## Exercise 1.1.22

`RiemannIntegrableOn.iff_darbouxIntegrable` (lemma, [line 1039](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1039)). An exercise, stated without proof.

> Exercise 1.1.22 (Riemann and Darboux integrability agree)

```lean
lemma RiemannIntegrableOn.iff_darbouxIntegrable {f:ℝ → ℝ} {I: BoundedInterval} (hbound: ∃ M, ∀ x ∈ I, |f x| ≤ M) : RiemannIntegrableOn f I ↔ DarbouxIntegrableOn f I
```

`riemann_integral_eq_darboux_integral` (lemma, [line 1043](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1043)). An exercise, stated without proof.

> Exercise 1.1.22 (the two integrals agree)

```lean
lemma riemann_integral_eq_darboux_integral {f:ℝ → ℝ} {I: BoundedInterval} (hf: RiemannIntegrableOn f I) : riemannIntegral f I = darbouxIntegral f I
```

## Exercise 1.1.23

`RiemannIntegrableOn.continuous` (lemma, [line 1047](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1047)). An exercise, stated without proof.

> Exercise 1.1.23

```lean
lemma RiemannIntegrableOn.continuous {f:ℝ → ℝ} {I: BoundedInterval} (hI: I = Icc I.a I.b)
    (hnonempty : I.toSet.Nonempty) (hcont: ContinuousOn f I.toSet) : RiemannIntegrableOn f I
```

## Exercise 1.1.23'

`RiemannIntegrableOn.piecewise_continuous` (lemma, [line 1054](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1054)). An exercise, stated without proof.

> Exercise 1.1.23'

```lean
lemma RiemannIntegrableOn.piecewise_continuous {f:ℝ → ℝ} {I: BoundedInterval} (hI: I = Icc I.a I.b)
    (hnonempty : I.toSet.Nonempty) (hbound: ∃ M, ∀ x ∈ I, |f x| ≤ M)
    (T: Finset BoundedInterval)  (hdisjoint: (T : Set BoundedInterval).PairwiseDisjoint BoundedInterval.toSet)
    (hcover : I.toSet = ⋃ J ∈ T, J.toSet) (hcont: ∀ J ∈ T, ContinuousOn f J.toSet) :
    RiemannIntegrableOn f I
```

## Exercise 1.1.24 (a)

`RiemannIntegrableOn.smul` (theorem, [line 1062](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1062)). An exercise, stated without proof.

> Exercise 1.1.24 (a) (scalar multiple, integrability).

```lean
theorem RiemannIntegrableOn.smul {I: BoundedInterval} (c:ℝ) {f: ℝ → ℝ} (h: RiemannIntegrableOn f I) : RiemannIntegrableOn (c • f) I
```

`riemann_integral_smul` (theorem, [line 1066](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1066)). An exercise, stated without proof.

> Exercise 1.1.24 (a) (scalar multiple, integral).

```lean
theorem riemann_integral_smul {I:BoundedInterval} (c:ℝ) {f: ℝ → ℝ} (h: RiemannIntegrableOn f I) : riemannIntegral (c • f) I = c • (riemannIntegral f I)
```

`RiemannIntegrableOn.add` (theorem, [line 1070](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1070)). An exercise, stated without proof.

> Exercise 1.1.24 (a) (sum, integrability).

```lean
theorem RiemannIntegrableOn.add {I: BoundedInterval} {f g: ℝ → ℝ} (hf: RiemannIntegrableOn f I) (hg: RiemannIntegrableOn g I) : RiemannIntegrableOn (f + g) I
```

`riemann_integral_add` (theorem, [line 1074](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1074)). An exercise, stated without proof.

> Exercise 1.1.24 (a) (sum, integral).

```lean
theorem riemann_integral_add {I: BoundedInterval} {f g: ℝ → ℝ} (hf: RiemannIntegrableOn f I) (hg: RiemannIntegrableOn g I) : riemannIntegral (f+g) I = riemannIntegral f I + riemannIntegral g I
```

## Exercise 1.1.24 (b)

`riemann_integral_mono` (theorem, [line 1078](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1078)). An exercise, stated without proof.

> Exercise 1.1.24 (b) (Monotonicity of the piecewise constant integral)

```lean
theorem riemann_integral_mono {I: BoundedInterval} {f g: ℝ → ℝ} (hf: RiemannIntegrableOn f I) (hg: RiemannIntegrableOn g I) (hmono: ∀ x ∈ I.toSet, f x ≤ g x): riemannIntegral f I ≤ riemannIntegral g I
```

## Exercise 1.1.24 (c)

`RiemannIntegrableOn.indicator_of_elem` (theorem, [line 1082](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1082)). An exercise, stated without proof.

> Exercise 1.1.24 (c) (Indicator functions)

```lean
theorem RiemannIntegrableOn.indicator_of_elem {I: BoundedInterval} (hI: I = Icc I.a I.b)
    (hnonempty : I.toSet.Nonempty) {E:Set ℝ}
    (hE: JordanMeasurable (Real.equiv_EuclideanSpace' '' E)) :
    RiemannIntegrableOn E.indicator' I
```

`riemann_integral_of_elem` (theorem, [line 1089](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1089)). An exercise, stated without proof.

> Exercise 1.1.24 (c) (Piecewise constant integral of indicator functions)

```lean
theorem riemann_integral_of_elem {I: BoundedInterval} (hI: I = Icc I.a I.b)
    (hnonempty : I.toSet.Nonempty) {E:Set ℝ}
    (hE: JordanMeasurable (Real.equiv_EuclideanSpace' '' E)) (hsub: E ⊆ I.toSet) :
    riemannIntegral E.indicator' I = hE.measure
```

## Exercise 1.1.24

`riemann_integral_unique` (theorem, [line 1096](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1096)). An exercise, stated without proof.

> Exercise 1.1.24 (Uniqueness)

```lean
theorem riemann_integral_unique {I: BoundedInterval} (integ: (ℝ → ℝ) → ℝ)
  (hsmul: ∀ (c:ℝ) (f: ℝ → ℝ) (hf: RiemannIntegrableOn f I), integ (c • f) = c • (integ f))
  (hadd: ∀ (f g: ℝ → ℝ) (hf: RiemannIntegrableOn f I) (hg: RiemannIntegrableOn g I), integ (f + g) = integ f + integ g)
  (hmono: ∀ (f g: ℝ → ℝ) (hf: RiemannIntegrableOn f I) (hg: RiemannIntegrableOn g I) (hmono: ∀ x ∈ I.toSet, f x ≤ g x), integ f ≤ integ g)
  (hindicator: ∀ (E:Set ℝ) (hE: JordanMeasurable (Real.equiv_EuclideanSpace' '' E) ) (hsub: E ⊆ I.toSet), integ E.indicator' = hE.measure) :
  ∀ f, RiemannIntegrableOn f I → integ f = riemannIntegral f I
```

## Exercise 1.1.25

`RiemannIntegrableOn.measurable_upper` (theorem, [line 1105](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1105)). An exercise, stated without proof.

> Exercise 1.1.25 (Area interpretation, region under the graph)

```lean
theorem RiemannIntegrableOn.measurable_upper {I: BoundedInterval}
  {f: ℝ → ℝ} (hfint: RiemannIntegrableOn f I) :
  JordanMeasurable { p:EuclideanSpace' 2 | p 0 ∈ I.toSet ∧ 0 ≤ p 1 ∧ p 1 ≤ f (p 0) }
```

`RiemannIntegrableOn.measurable_lower` (theorem, [line 1111](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1111)). An exercise, stated without proof.

> Exercise 1.1.25 (Area interpretation, region below the graph)

```lean
theorem RiemannIntegrableOn.measurable_lower {I: BoundedInterval}
  {f: ℝ → ℝ} (hfint: RiemannIntegrableOn f I) :
  JordanMeasurable { p:EuclideanSpace' 2 | p 0 ∈ I.toSet ∧ f (p 0) ≤ p 1 ∧ p 1 ≤ 0 }
```

`JordanMeasurable.iff_integrable` (theorem, [line 1117](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1117)). An exercise, stated without proof.

> Exercise 1.1.25 (Area interpretation, integrability criterion)

```lean
theorem JordanMeasurable.iff_integrable {I: BoundedInterval} (hI: I = Icc I.a I.b)
  {f: ℝ → ℝ} (hf: ∃ M, ∀ x ∈ I.toSet, |f x| ≤ M) : RiemannIntegrableOn f I ↔
  JordanMeasurable { p:EuclideanSpace' 2 | p 0 ∈ I.toSet ∧ 0 ≤ p 1 ∧ p 1 ≤ f (p 0) } ∧
  JordanMeasurable { p:EuclideanSpace' 2 | p 0 ∈ I.toSet ∧ f (p 0) ≤ p 1 ∧ p 1 ≤ 0 }
```

`RiemannIntegrableOn.eq_measure` (theorem, [line 1125](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean#L1125)). An exercise, stated without proof.

> Exercise 1.1.25 (Area interpretation, integral as a difference of measures)

```lean
theorem RiemannIntegrableOn.eq_measure {I: BoundedInterval}
  {f: ℝ → ℝ} (hfint: RiemannIntegrableOn f I) :
  riemannIntegral f I = hfint.measurable_upper.measure - hfint.measurable_lower.measure
```

## Depends on

- [Section 1.1.2: Jordan measure](section-1-1-2.md)

## Sources

- [Analysis/MeasureTheory/Section_1_1_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_3.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_1_3.html)
