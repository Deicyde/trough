---
declaration: class
origin: cited
lean: FinitelyAdditiveMeasure, FinitelyAdditiveMeasure.lebesgue, FinitelyAdditiveMeasure.restrict_alg, FinitelyAdditiveMeasure.jordan, FinitelyAdditiveMeasure.null, FinitelyAdditiveMeasure.elem, FinitelyAdditiveMeasure.dirac, FinitelyAdditiveMeasure.instZero, FinitelyAdditiveMeasure.instAdd, FinitelyAdditiveMeasure.restrict, FinitelyAdditiveMeasure.counting, FinitelyAdditiveMeasure.mono, FinitelyAdditiveMeasure.finite_additivity, FinitelyAdditiveMeasure.finite_subadditivity, FinitelyAdditiveMeasure.mes_union_add_mes_inter, FinitelyAdditiveMeasure.finite_atomic_eq, CountablyAdditiveMeasure, FinitelyAdditiveMeasure.lebesgue_isCountablyAdditive, FinitelyAdditiveMeasure.dirac_isCountablyAdditive, FinitelyAdditiveMeasure.counting_isCountablyAdditive, CountablyAdditiveMeasure.restrict, CountablyAdditiveMeasure.instSmul, CountablyAdditiveMeasure.sum, Measure.countable_subadditivity, Measure.upwards_mono, Measure.downwards_mono, Measure.measurable_of_lim, Measure.measure_of_lim, Measure.measure_of_lim_counter, Measure.on_countable, Measure.completion_lt, EuclideanSpace'.borel_completion_eq_lebesgue, BooleanAlgebra.approx_finite, BooleanAlgebra.approx_sigma_finite
statement: formalized
---

# Section 1.4.3: Countably additive measures and measure spaces

> A companion to (the introduction to) Section 1.4.3 of the book "An introduction to Measure Theory".
>
> Note: initially this section will use custom-notions of concrete sigma algebras and countably additive measures, but will transition to the Mathlib notions of `Measurable` and `MeasureTheory.Measure`, which will be in use going forward. In particular, exercises past this point will be easier
> to solve using the Mathlib library for measure theory than the custom results defined here.

*Quoted from [Analysis/MeasureTheory/Section_1_4_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 29 labelled items, carried by 34 declarations: 5 proved here, 14 stated without proof (12 of them exercises) and 15 definitions (4 with a value left as `sorry`). It also has 23 declarations with no label, counted here but not shown.

## Definition 1.4.19

`FinitelyAdditiveMeasure` (class, [line 13](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L13)). A definition.

> Definition 1.4.19 (Finitely additive measure)

```lean
class FinitelyAdditiveMeasure {X:Type*} (B: ConcreteBooleanAlgebra X)
```

## Example 1.4.21

`FinitelyAdditiveMeasure.lebesgue` (def, [line 32](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L32)). A definition whose value is left as `sorry`.

> Example 1.4.21 (Lebesgue measure)

```lean
noncomputable def FinitelyAdditiveMeasure.lebesgue (d:ℕ) : FinitelyAdditiveMeasure (LebesgueMeasurable.boolean_algebra d)
```

`FinitelyAdditiveMeasure.restrict_alg` (def, [line 41](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L41)). A definition.

> Example 1.4.21 (restriction to a subalgebra)

```lean
def FinitelyAdditiveMeasure.restrict_alg {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: FinitelyAdditiveMeasure B) {B':ConcreteBooleanAlgebra X} (hBB': B' ≤ B) : FinitelyAdditiveMeasure B'
```

`FinitelyAdditiveMeasure.jordan` (def, [line 51](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L51)). A definition.

> Example 1.4.21 (Jordan measure)

```lean
noncomputable def FinitelyAdditiveMeasure.jordan (d:ℕ) : FinitelyAdditiveMeasure (JordanMeasurable.boolean_algebra d)
```

`FinitelyAdditiveMeasure.null` (def, [line 55](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L55)). A definition.

> Example 1.4.21 (null sets)

```lean
noncomputable def FinitelyAdditiveMeasure.null (d:ℕ) : FinitelyAdditiveMeasure (IsNull.boolean_algebra d)
```

`FinitelyAdditiveMeasure.elem` (def, [line 59](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L59)). A definition.

> Example 1.4.21 (elementary sets)

```lean
noncomputable def FinitelyAdditiveMeasure.elem (d:ℕ) : FinitelyAdditiveMeasure (EuclideanSpace'.elementary_boolean_algebra d)
```

## Example 1.4.22

`FinitelyAdditiveMeasure.dirac` (def, [line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L66)). A definition.

> Example 1.4.22 (Dirac measure)

```lean
noncomputable def FinitelyAdditiveMeasure.dirac {X:Type*} (x₀:X) (B: ConcreteBooleanAlgebra X) : FinitelyAdditiveMeasure B
```

## Example 1.4.23

`FinitelyAdditiveMeasure.instZero` (instance, [line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L90)). A definition.

> Example 1.4.23 (Zero measure)

```lean
noncomputable instance FinitelyAdditiveMeasure.instZero {X:Type*} (B: ConcreteBooleanAlgebra X) : Zero (FinitelyAdditiveMeasure B)
```

## Example 1.4.24

`FinitelyAdditiveMeasure.instAdd` (instance, [line 101](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L101)). A definition.

> Example 1.4.24 (linear combinations of measures)

```lean
noncomputable instance FinitelyAdditiveMeasure.instAdd {X:Type*} {B: ConcreteBooleanAlgebra X} : Add (FinitelyAdditiveMeasure B)
```

## Example 1.4.25

`FinitelyAdditiveMeasure.restrict` (def, [line 175](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L175)). A definition.

> Example 1.4.25 (Restriction of a measure)

```lean
def FinitelyAdditiveMeasure.restrict {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: FinitelyAdditiveMeasure B) (A:Set X) (hA:B.measurable A) : FinitelyAdditiveMeasure (B.restrict A)
```

## Example 1.4.26

`FinitelyAdditiveMeasure.counting` (def, [line 190](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L190)). A definition.

> Example 1.4.26 (Counting a measure)

```lean
noncomputable def FinitelyAdditiveMeasure.counting (X:Type*) : FinitelyAdditiveMeasure (⊤  : ConcreteBooleanAlgebra X)
```

## Exercise 1.4.20(i)

`FinitelyAdditiveMeasure.mono` (theorem, [line 224](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L224)). Proved here.

> Exercise 1.4.20(i)

```lean
theorem FinitelyAdditiveMeasure.mono {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: FinitelyAdditiveMeasure B) {E F : Set X} (hE : B.measurable E) (hF : B.measurable F) (hsub : E ⊆ F) : μ.measure E ≤ μ.measure F
```

## Exercise 1.4.20(ii)

`FinitelyAdditiveMeasure.finite_additivity` (theorem, [line 233](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L233)). Proved here.

> Exercise 1.4.20(ii)

```lean
theorem FinitelyAdditiveMeasure.finite_additivity {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: FinitelyAdditiveMeasure B) {J:Type*} {I: Finset J} {E: J → Set X} (hE: ∀ j:J, B.measurable (E j)) (hdisj: Set.univ.PairwiseDisjoint E) :
  μ.measure (⋃ j ∈ I, E j) = ∑ j ∈ I, μ.measure (E j)
```

## Exercise 1.4.20(iii)

`FinitelyAdditiveMeasure.finite_subadditivity` (theorem, [line 248](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L248)). Proved here.

> Exercise 1.4.20(iii)

```lean
theorem FinitelyAdditiveMeasure.finite_subadditivity {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: FinitelyAdditiveMeasure B) {J:Type*} {I: Finset J} {E: J → Set X} (hE: ∀ j:J, B.measurable (E j)) :
  μ.measure (⋃ j ∈ I, E j) ≤ ∑ j ∈ I, μ.measure (E j)
```

## Exercise 1.4.20(iv)

`FinitelyAdditiveMeasure.mes_union_add_mes_inter` (theorem, [line 267](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L267)). Proved here.

> Exercise 1.4.20(iv)

```lean
theorem FinitelyAdditiveMeasure.mes_union_add_mes_inter {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: FinitelyAdditiveMeasure B) {E F : Set X}
    (hE: B.measurable E) (hF: B.measurable F) :
  μ.measure (E ∪ F) + μ.measure (E ∩ F) = μ.measure E + μ.measure F
```

## Exercise 1.4.21

`FinitelyAdditiveMeasure.finite_atomic_eq` (theorem, [line 286](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L286)). An exercise, stated without proof.

> Exercise 1.4.21

```lean
theorem FinitelyAdditiveMeasure.finite_atomic_eq {I X: Type*} [Fintype I] {atoms: I → Set X} (h_part: IsPartition atoms) (μ : FinitelyAdditiveMeasure h_part.to_ConcreteBooleanAlgebra) : ∃! c : I → ENNReal, ∀ E, h_part.to_ConcreteBooleanAlgebra.measurable E → μ.measure E = ∑ i ∈ Finset.univ.filter (fun i => atoms i ⊆ E), c i
```

## Definition 1.4.27

`CountablyAdditiveMeasure` (class, [line 289](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L289)). A definition.

> Definition 1.4.27 (Countably additive measure)

```lean
class CountablyAdditiveMeasure {X:Type*} (B: ConcreteSigmaAlgebra X) extends FinitelyAdditiveMeasure B.toConcreteBooleanAlgebra
```

## Example 1.4.28

`FinitelyAdditiveMeasure.lebesgue_isCountablyAdditive` (theorem, [line 319](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L319)). Proved here.

> Example 1.4.28

```lean
theorem FinitelyAdditiveMeasure.lebesgue_isCountablyAdditive (d:ℕ) : (FinitelyAdditiveMeasure.lebesgue d).isCountablyAdditive
```

## Example 1.4.29

`FinitelyAdditiveMeasure.dirac_isCountablyAdditive` (theorem, [line 335](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L335)). Stated without proof.

> Example 1.4.29 (Dirac measure)

```lean
theorem FinitelyAdditiveMeasure.dirac_isCountablyAdditive {X:Type*} (x₀:X) (B: ConcreteBooleanAlgebra X) (hB: B.isSigmaAlgebra) : (FinitelyAdditiveMeasure.dirac x₀ B).isCountablyAdditive
```

`FinitelyAdditiveMeasure.counting_isCountablyAdditive` (theorem, [line 339](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L339)). Stated without proof.

> Example 1.4.29 (Counting measure)

```lean
theorem FinitelyAdditiveMeasure.counting_isCountablyAdditive {X:Type*} : (FinitelyAdditiveMeasure.counting X).isCountablyAdditive
```

## Example 1.4.30

`CountablyAdditiveMeasure.restrict` (def, [line 343](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L343)). A definition whose value is left as `sorry`.

> Example 1.4.30

```lean
def CountablyAdditiveMeasure.restrict {X:Type*} {B: ConcreteSigmaAlgebra X} (μ: CountablyAdditiveMeasure B) (A:Set X) (hA:B.measurable A) : CountablyAdditiveMeasure (B.restrict A)
```

## Exercise 1.4.22(i)

`CountablyAdditiveMeasure.instSmul` (instance, [line 388](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L388)). A definition whose value is left as `sorry`.

> Exercise 1.4.22(i)

```lean
noncomputable instance CountablyAdditiveMeasure.instSmul {X:Type*} {B: ConcreteSigmaAlgebra X} : SMul ENNReal (CountablyAdditiveMeasure B)
```

## Exercise 1.4.22(ii)

`CountablyAdditiveMeasure.sum` (def, [line 423](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L423)). A definition whose value is left as `sorry`.

> Exercise 1.4.22(ii)

```lean
noncomputable def CountablyAdditiveMeasure.sum {X:Type*} {B: ConcreteSigmaAlgebra X} (μ: ℕ → CountablyAdditiveMeasure B) : CountablyAdditiveMeasure B
```

## Exercise 1.4.23(i)

`Measure.countable_subadditivity` (theorem, [line 463](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L463)). An exercise, stated without proof.

> Exercise 1.4.23(i)

```lean
theorem Measure.countable_subadditivity {X:Type*} [MeasurableSpace X] (μ: Measure X) {E : ℕ → Set X} (hE: ∀ n, Measurable (E n)) :
  μ.measureOf (⋃ n, E n) ≤ ∑' n, μ.measureOf (E n)
```

## Exercise 1.4.23(ii)

`Measure.upwards_mono` (theorem, [line 467](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L467)). An exercise, stated without proof.

> Exercise 1.4.23(ii)

```lean
theorem Measure.upwards_mono {X:Type*} [MeasurableSpace X] (μ: Measure X) {E : ℕ → Set X} (hE: ∀ n, Measurable (E n))
  (hmono : Monotone E) : μ (⋃ n, E n) = ⨆ n, μ.measureOf (E n)
```

## Exercise 1.4.23(iii)

`Measure.downwards_mono` (theorem, [line 471](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L471)). An exercise, stated without proof.

> Exercise 1.4.23(iii)

```lean
theorem Measure.downwards_mono {X:Type*} [MeasurableSpace X] (μ: Measure X) {E : ℕ → Set X} (hE: ∀ n, Measurable (E n))
  (hmono : Antitone E) (hfin : ∃ n, μ (E n) < ⊤) : μ (⋂ n, E n) = ⨅ n, μ.measureOf (E n)
```

## Exercise 1.4.24 (i)

`Measure.measurable_of_lim` (theorem, [line 478](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L478)). An exercise, stated without proof.

> Exercise 1.4.24 (i) (Dominated convergence for sets)

```lean
theorem Measure.measurable_of_lim {X:Type*} [MeasurableSpace X] (μ: Measure X) {E : ℕ → Set X} (hE: ∀ n, Measurable (E n))
  {E' : Set X} (hlim : PointwiseConvergesTo E E') : Measurable E'
```

## Exercise 1.4.24 (ii)

`Measure.measure_of_lim` (theorem, [line 482](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L482)). An exercise, stated without proof.

> Exercise 1.4.24 (ii) (Dominated convergence for sets)

```lean
theorem Measure.measure_of_lim {X:Type*} [MeasurableSpace X] (μ: Measure X) {E : ℕ → Set X} (hE: ∀ n, Measurable (E n))
  {E' F : Set X} (hlim : PointwiseConvergesTo E E') (hF : Measurable F) (hfin : μ F < ⊤) (hcon : ∀ n, E n ⊆ F) :
  Filter.atTop.Tendsto (fun n ↦ μ (E n)) (nhds (μ E'))
```

## Exercise 1.4.24 (iii)

`Measure.measure_of_lim_counter` (theorem, [line 487](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L487)). An exercise, stated without proof.

> Exercise 1.4.24 (iii) (Dominated convergence for sets)

```lean
theorem Measure.measure_of_lim_counter : ∃ (X:Type) (M:MeasurableSpace X) (μ: Measure X) (E : ℕ → Set X) (hE: ∀ n, Measurable (E n))
  (E' F : Set X) (hlim : PointwiseConvergesTo E E') (hF : Measurable F) (hcon : ∀ n, E n ⊆ F),
  ¬ Filter.atTop.Tendsto (fun n ↦ μ (E n)) (nhds (μ E'))
```

## Exercise 1.4.25

`Measure.on_countable` (theorem, [line 492](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L492)). An exercise, stated without proof.

> Exercise 1.4.25

```lean
theorem Measure.on_countable {X:Type*} [Countable X] [M: MeasurableSpace X] (hM: M = ⊤) (μ: Measure X) :
  ∃! c : X → ENNReal, ∀ E : Set X, μ E = ∑' x : E, c x
```

## Exercise 1.4.26

`Measure.completion_lt` (theorem, [line 503](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L503)). An exercise, stated without proof.

> Exercise 1.4.26 (Completion)

```lean
theorem Measure.completion_lt {X:Type*} [M : MeasurableSpace X] (μ: Measure X) (M' : MeasurableSpace X) (μ' : @Measure X M')
  (hcomplete : μ'.IsComplete) (hMM' : M ≤ M') (hμ : ∀ E, M.MeasurableSet' E → μ E = μ' E) : ∀ E : Set X, @NullMeasurableSet X M E μ → (M'.MeasurableSet' E ∧ μ' E = μ.completion E)
```

## Exercise 1.4.27

`EuclideanSpace'.borel_completion_eq_lebesgue` (theorem, [line 514](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L514)). An exercise, stated without proof.

> Exercise 1.4.27

```lean
theorem EuclideanSpace'.borel_completion_eq_lebesgue {d:ℕ} :
  Measure.equiv (EuclideanSpace'.borelMeasure d).completion (EuclideanSpace'.lebesgueMeasure d)
```

## Exercise 1.4.28(i)

`BooleanAlgebra.approx_finite` (theorem, [line 518](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L518)). An exercise, stated without proof.

> Exercise 1.4.28(i) (Approximation by an algebra)

```lean
theorem BooleanAlgebra.approx_finite {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: @Measure X (ConcreteSigmaAlgebra.generated_by B.measurableSets).measurableSpace) (hfin: μ Set.univ < ⊤) : ∀ (ε : ℝ) (hε: ε>0) (E : Set X) (hE: (ConcreteSigmaAlgebra.generated_by B.measurableSets).measurable E),
  ∃ F : Set X, B.measurable F ∧ μ (symmDiff E F) < ENNReal.ofReal ε
```

## Exercise 1.4.28(ii)

`BooleanAlgebra.approx_sigma_finite` (theorem, [line 522](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean#L522)). An exercise, stated without proof.

> Exercise 1.4.28(ii) (Approximation by an algebra)

```lean
theorem BooleanAlgebra.approx_sigma_finite {X:Type*} {B: ConcreteBooleanAlgebra X} (μ: @Measure X (ConcreteSigmaAlgebra.generated_by B.measurableSets).measurableSpace) (hσfin: ∃ A : ℕ → Set X, (∀ n, B.measurable (A n) ∧ μ (A n) < ⊤) ∧ ⋃ n, A n = ⊤) : ∀ (ε : ℝ) (hε: ε>0) (E : Set X) (hE: (ConcreteSigmaAlgebra.generated_by B.measurableSets).measurable E) (hEfin: μ E < ⊤),
  ∃ F : Set X, B.measurable F ∧ μ (symmDiff E F) < ENNReal.ofReal ε
```

## Depends on

- [Section 1.4.2: $\sigma$-algebras and measurable spaces](section-1-4-2.md)

## Sources

- [Analysis/MeasureTheory/Section_1_4_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_3.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_4_3.html)
