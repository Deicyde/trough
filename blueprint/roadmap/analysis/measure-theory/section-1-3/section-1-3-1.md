---
declaration: def
origin: cited
lean: UnsignedSimpleFunction, UnsignedSimpleFunction.integral_eq, AlmostAlways, AlmostEverywhereEqual, Support, UnsignedSimpleFunction.integral_add, UnsignedSimpleFunction.integral_smul, UnsignedSimpleFunction.integral_finite_iff, UnsignedSimpleFunction.integral_eq_zero_iff, UnsignedSimpleFunction.integral_eq_integral_of_aeEqual, UnsignedSimpleFunction.integral_le_integral_of_aeLe, UnsignedSimpleFunction.indicator, UnsignedSimpleFunction.integral_indicator, RealSimpleFunction.AbsolutelyIntegrable, ComplexSimpleFunction.AbsolutelyIntegrable, RealSimpleFunction.integ_add, RealSimpleFunction.integ_smul, ComplexSimpleFunction.integral_conj, RealSimpleFunction.integral_eq_integral_of_aeEqual, RealSimpleFunction.indicator, RealSimpleFunction.integral_indicator
statement: formalized
---

# Section 1.3.1: Integration of simple functions

> A companion to (the introduction to) Section 1.3.1 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_3_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 13 labelled items, carried by 21 declarations: 4 proved here, 11 stated without proof (11 of them exercises) and 6 definitions. It also has 77 declarations with no label, counted here but not shown.

## Definition 1.3.2

`UnsignedSimpleFunction` (def, [line 35](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L35)). A definition.

> Definition 1.3.2

```lean
def UnsignedSimpleFunction {d:ℕ} (f: EuclideanSpace' d → EReal) : Prop
```

## Lemma 1.3.4

`UnsignedSimpleFunction.integral_eq` (lemma, [line 798](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L798)). Proved here.

> Lemma 1.3.4 (Well-definedness of simple integral)

```lean
lemma UnsignedSimpleFunction.integral_eq {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) {k:ℕ} {c: Fin k → EReal}
    {E: Fin k → Set (EuclideanSpace' d)} (hmes: ∀ i, LebesgueMeasurable (E i)) (hnonneg: ∀ i, c i ≥ 0)
    (heq: f = ∑ i, (c i) • (EReal.indicator (E i))) :
    hf.integ = ∑ i, (c i) * Lebesgue_measure (E i)
```

## Definition 1.3.5

`AlmostAlways` (def, [line 825](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L825)). A definition.

> Definition 1.3.5 (almost always)

```lean
def AlmostAlways {d:ℕ} (P: EuclideanSpace' d → Prop) : Prop
```

`AlmostEverywhereEqual` (def, [line 829](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L829)). A definition.

> Definition 1.3.5 (almost everywhere equal)

```lean
def AlmostEverywhereEqual {d:ℕ} {X: Type*} (f g: EuclideanSpace' d → X) : Prop
```

`Support` (def, [line 833](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L833)). A definition.

> Definition 1.3.5 (support)

```lean
def Support {X Y: Type*} [Zero Y] (f: X → Y) : Set X
```

## Exercise 1.3.1 (i)

`UnsignedSimpleFunction.integral_add` (lemma, [line 1033](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1033)). An exercise, stated without proof.

> Exercise 1.3.1 (i) (Unsigned linearity, sum)

```lean
lemma UnsignedSimpleFunction.integral_add {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) (hg: UnsignedSimpleFunction g) :
  (hf.add hg).integ = hf.integ + hg.integ
```

`UnsignedSimpleFunction.integral_smul` (lemma, [line 1038](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1038)). An exercise, stated without proof.

> Exercise 1.3.1 (i) (Unsigned linearity, scalar multiple)

```lean
lemma UnsignedSimpleFunction.integral_smul {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) {c:EReal} (hc: c ≥ 0) :
  (hf.smul hc).integ = c * hf.integ
```

## Exercise 1.3.1 (ii)

`UnsignedSimpleFunction.integral_finite_iff` (lemma, [line 1043](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1043)). An exercise, stated without proof.

> Exercise 1.3.1 (ii) (Finiteness)

```lean
lemma UnsignedSimpleFunction.integral_finite_iff {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) :
  (hf.integ < ⊤) ↔ (AlmostAlways (fun x ↦ f x < ⊤)) ∧ (Lebesgue_measure (Support f)) < ⊤
```

## Exercise 1.3.1 (iii)

`UnsignedSimpleFunction.integral_eq_zero_iff` (lemma, [line 1048](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1048)). An exercise, stated without proof.

> Exercise 1.3.1 (iii) (Vanishing)

```lean
lemma UnsignedSimpleFunction.integral_eq_zero_iff {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) :
  (hf.integ = 0) ↔ AlmostAlways (fun x ↦ f x = 0)
```

## Exercise 1.3.1 (iv)

`UnsignedSimpleFunction.integral_eq_integral_of_aeEqual` (lemma, [line 1053](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1053)). An exercise, stated without proof.

> Exercise 1.3.1 (iv) (Equivalence)

```lean
lemma UnsignedSimpleFunction.integral_eq_integral_of_aeEqual {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) (hg: UnsignedSimpleFunction g)
  (hae: AlmostEverywhereEqual f g) :
  hf.integ = hg.integ
```

## Exercise 1.3.1 (v)

`UnsignedSimpleFunction.integral_le_integral_of_aeLe` (lemma, [line 1059](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1059)). An exercise, stated without proof.

> Exercise 1.3.1 (v) (Monotonicity)

```lean
lemma UnsignedSimpleFunction.integral_le_integral_of_aeLe {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f) (hg: UnsignedSimpleFunction g)
  (hae: AlmostAlways (fun x ↦ f x ≤ g x)) :
  hf.integ ≤ hg.integ
```

## Exercise 1.3.1(vi)

`UnsignedSimpleFunction.indicator` (lemma, [line 1065](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1065)). Proved here.

> Exercise 1.3.1(vi) (Compatibility with Lebesgue measure, indicator)

```lean
lemma UnsignedSimpleFunction.indicator {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E) :
  UnsignedSimpleFunction (Real.toEReal ∘ E.indicator')
```

`UnsignedSimpleFunction.integral_indicator` (lemma, [line 1077](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1077)). Proved here.

> Exercise 1.3.1(vi) (Compatibility with Lebesgue measure, integral of an indicator)

```lean
lemma UnsignedSimpleFunction.integral_indicator {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E) :
  (UnsignedSimpleFunction.indicator hE).integ = Lebesgue_measure E
```

## Definition 1.3.6

`RealSimpleFunction.AbsolutelyIntegrable` (def, [line 1095](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1095)). A definition.

> Definition 1.3.6 (Absolutely convergent simple integral, real)

```lean
def RealSimpleFunction.AbsolutelyIntegrable {d:ℕ} {f: EuclideanSpace' d → ℝ} (hf: RealSimpleFunction f) : Prop
```

`ComplexSimpleFunction.AbsolutelyIntegrable` (def, [line 1099](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1099)). A definition.

> Definition 1.3.6 (Absolutely convergent simple integral, complex)

```lean
def ComplexSimpleFunction.AbsolutelyIntegrable {d:ℕ} {f: EuclideanSpace' d → ℂ} (hf: ComplexSimpleFunction f) : Prop
```

## Exercise 1.3.2 (i)

`RealSimpleFunction.integ_add` (lemma, [line 1292](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1292)). An exercise, stated without proof.

> Exercise 1.3.2 (i) (`*`-linearity, sum)

```lean
lemma RealSimpleFunction.integ_add {d:ℕ} {f g: EuclideanSpace' d → ℝ} {hf: RealSimpleFunction f} {hg: RealSimpleFunction g} (hf_integ: hf.AbsolutelyIntegrable) (hg_integ: hg.AbsolutelyIntegrable) : (hf.add hg).integ = hf.integ + hg.integ
```

`RealSimpleFunction.integ_smul` (lemma, [line 1298](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1298)). An exercise, stated without proof.

> Exercise 1.3.2 (i) (`*`-linearity, scalar multiple)

```lean
lemma RealSimpleFunction.integ_smul {d:ℕ} {f: EuclideanSpace' d → ℝ} {hf: RealSimpleFunction f} (hf_integ: hf.AbsolutelyIntegrable) (a: ℝ) : (hf.smul a).integ = a * hf.integ
```

`ComplexSimpleFunction.integral_conj` (lemma, [line 1305](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1305)). An exercise, stated without proof.

> Exercise 1.3.2 (i) (`*`-linearity, conjugation)

```lean
lemma ComplexSimpleFunction.integral_conj {d:ℕ} {f: EuclideanSpace' d → ℂ} {hf: ComplexSimpleFunction f} (hf_integ: hf.AbsolutelyIntegrable) : (hf.conj).integ = (starRingEnd ℂ) hf.integ
```

## Exercise 1.3.2 (ii)

`RealSimpleFunction.integral_eq_integral_of_aeEqual` (lemma, [line 1309](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1309)). An exercise, stated without proof.

> Exercise 1.3.2 (ii) (equivalence)

```lean
lemma RealSimpleFunction.integral_eq_integral_of_aeEqual {d:ℕ} {f g: EuclideanSpace' d → ℝ} {hf: RealSimpleFunction f} {hg: RealSimpleFunction g} (hf_integ: hf.AbsolutelyIntegrable) (hg_integ: hg.AbsolutelyIntegrable) (h_ae: AlmostEverywhereEqual f g) : hf.integ = hg.integ
```

## Exercise 1.3.2(iii)

`RealSimpleFunction.indicator` (lemma, [line 1316](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1316)). Proved here.

> Exercise 1.3.2(iii) (Compatibility with Lebesgue measure, indicator)

```lean
lemma RealSimpleFunction.indicator {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E) :
  RealSimpleFunction (E.indicator')
```

`RealSimpleFunction.integral_indicator` (lemma, [line 1339](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean#L1339)). An exercise, stated without proof.

> Exercise 1.3.2(iii) (Compatibility with Lebesgue measure, integral of an indicator)

```lean
lemma RealSimpleFunction.integral_indicator {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E) (hfin: Lebesgue_measure E < ⊤): (RealSimpleFunction.indicator hE).integ = (Lebesgue_measure E).toReal
```

## Depends on

- [Section 1.2.3: Non-measurable sets](../section-1-2/section-1-2-3.md)

## Sources

- [Analysis/MeasureTheory/Section_1_3_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_1.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_3_1.html)
