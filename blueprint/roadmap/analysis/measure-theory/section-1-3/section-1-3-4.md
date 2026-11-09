---
declaration: def
origin: cited
lean: UnsignedAbsolutelyIntegrable, L1.integ, RealAbsolutelyIntegrable.trans, RealAbsolutelyIntegrable.comp_linear, RiemannIntegrableOn.realAbsolutelyIntegrable, AbsolutelySummable.realAbsolutelyIntegrable_iff, ComplexAbsolutelyIntegrableOn.glue, RealAbsolutelyIntegrable.abs_integ_le
statement: formalized
---

# Section 1.3.4: Absolute integrability

> A companion to (the introduction to) Section 1.3.4 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_3_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 8 labelled items, carried by 8 declarations: 1 proved here, 5 stated without proof (5 of them exercises) and 2 definitions (1 with a value left as `sorry`). It also has 83 declarations with no label, counted here but not shown.

## Definition 1.3.17

`UnsignedAbsolutelyIntegrable` (def, [line 14](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L14)). A definition.

> Definition 1.3.17

```lean
def UnsignedAbsolutelyIntegrable {d:ℕ} (f: EuclideanSpace' d → EReal) : Prop
```

## Exercise 1.3.19

`L1.integ` (def, [line 989](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L989)). A definition whose value is left as `sorry`.

> Exercise 1.3.19 (Integration is linear)

```lean
noncomputable def L1.integ {d:ℕ} : L1 d →ₗ[ℂ] ℂ
```

## Exercise 1.3.20(i)

`RealAbsolutelyIntegrable.trans` (theorem, [line 1000](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L1000)). An exercise, stated without proof.

> Exercise 1.3.20(i) (Translation invariance).

```lean
theorem RealAbsolutelyIntegrable.trans {d:ℕ} {f: EuclideanSpace' d → ℝ} (hf: RealAbsolutelyIntegrable f) (a: EuclideanSpace' d) : RealAbsolutelyIntegrable (fun x ↦ f (x + a))
```

## Exercise 1.3.20(ii)

`RealAbsolutelyIntegrable.comp_linear` (theorem, [line 1009](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L1009)). An exercise, stated without proof.

> Exercise 1.3.20(ii) (Linear change of variables).

```lean
theorem RealAbsolutelyIntegrable.comp_linear {d:ℕ} {f: EuclideanSpace' d → ℝ} (hf: RealAbsolutelyIntegrable f) {A: EuclideanSpace' d →ₗ[ℝ] EuclideanSpace' d} (hA: A.det ≠ 0) :
    RealAbsolutelyIntegrable (fun x ↦ f (A x))
```

## Exercise 1.3.20(iii)

`RiemannIntegrableOn.realAbsolutelyIntegrable` (theorem, [line 1022](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L1022)). An exercise, stated without proof.

> Exercise 1.3.20(iii) (Compatibility with the Riemann integral).

```lean
theorem RiemannIntegrableOn.realAbsolutelyIntegrable {I: BoundedInterval} {f: ℝ → ℝ} (hf: RiemannIntegrableOn f I) : RealAbsolutelyIntegrable ((fun x ↦ (f x) * (I.toSet.indicator' x)) ∘ EuclideanSpace'.equiv_Real)
```

## Exercise 1.3.21

`AbsolutelySummable.realAbsolutelyIntegrable_iff` (theorem, [line 1028](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L1028)). An exercise, stated without proof.

> Exercise 1.3.21 (Absolute summability is a special case of absolute integrability)

```lean
theorem AbsolutelySummable.realAbsolutelyIntegrable_iff {a: ℤ → ℝ} : ∑' n, |a n|.toEReal < ⊤ ↔ RealAbsolutelyIntegrable (fun x ↦ a ⌊EuclideanSpace'.equiv_Real x⌋)
```

## Exercise 1.3.22

`ComplexAbsolutelyIntegrableOn.glue` (theorem, [line 1038](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L1038)). An exercise, stated without proof.

> Exercise 1.3.22

```lean
theorem ComplexAbsolutelyIntegrableOn.glue {d:ℕ} {f: EuclideanSpace' d → ℂ} {E F: Set (EuclideanSpace' d)}
    (hE: LebesgueMeasurable E) (hF: LebesgueMeasurable F) (hdisj: Disjoint E F)
    (hf: ComplexAbsolutelyIntegrableOn f (E ∪ F)) :
    ∃ hE : ComplexAbsolutelyIntegrableOn f E, ∃ hF: ComplexAbsolutelyIntegrableOn f F, hf.integ = hE.integ + hF.integ
```

## Lemma 1.3.19

`RealAbsolutelyIntegrable.abs_integ_le` (lemma, [line 1052](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean#L1052)). Proved here.

> Lemma 1.3.19 (Triangle inequality)

```lean
lemma RealAbsolutelyIntegrable.abs_integ_le {d:ℕ} {f: EuclideanSpace' d → ℝ}
    (hf: RealAbsolutelyIntegrable f) : |hf.integ| ≤ hf.abs.integ
```

## Depends on

- [Section 1.3.3: Unsigned Lebesgue integrals](section-1-3-3.md)

## Sources

- [Analysis/MeasureTheory/Section_1_3_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_4.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_3_4.html)
