---
declaration: class
origin: cited
lean: ConcreteSigmaAlgebra, ConcreteBooleanAlgebra.isAtomic.isSigmaAlgebra, LebesgueMeasurable.boolean_algebra.isSigmaAlgebra, ConcreteSigmaAlgebra.restrict_is_sigma, ConcreteSigmaAlgebra.instInfSet, ConcreteSigmaAlgebra.instSupSet, ConcreteSigmaAlgebra.induction, BorelSigmaAlgebra, BorelSigmaAlgebra.generated_by_open, BorelSigmaAlgebra.generated_by_closed, BorelSigmaAlgebra.generated_by_compact, BorelSigmaAlgebra.generated_by_open_balls, BorelSigmaAlgebra.generated_by_boxes, BorelSigmaAlgebra.generated_by_elementary, ConcreteSigmaAlgebra.generated_by_eq, ConcreteSigmaAlgebra.card_of_generated_by, BorelSigmaAlgebra.prod, BorelSigmaAlgebra.slice_fst, BorelSigmaAlgebra.slice_snd, LebesgueMeasurable.sigmaAlgebra_generated_by
statement: formalized
---

# Section 1.4.2: $\sigma$-algebras and measurable spaces

> A companion to (the introduction to) Section 1.4.2 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_4_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 20 labelled items, carried by 21 declarations: 3 proved here, 12 stated without proof (11 of them exercises) and 6 definitions (2 with a value left as `sorry`). It also has 22 declarations and 1 example with no label, counted here but not shown.

## Definition 1.4.12

`ConcreteSigmaAlgebra` (class, [line 11](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L11)). A definition.

> Definition 1.4.12 (Sigma algebra)

```lean
class ConcreteSigmaAlgebra (X:Type*) extends ConcreteBooleanAlgebra X
```

## Exercise 1.4.10

`ConcreteBooleanAlgebra.isAtomic.isSigmaAlgebra` (def, [line 23](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L23)). A definition whose value is left as `sorry`.

> Exercise 1.4.10

```lean
def ConcreteBooleanAlgebra.isAtomic.isSigmaAlgebra {X: Type*} {B: ConcreteBooleanAlgebra X} (h: B.isAtomic) : B.isSigmaAlgebra
```

## Exercise 1.4.11

`LebesgueMeasurable.boolean_algebra.isSigmaAlgebra` (theorem, [line 27](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L27)). Proved here.

> Exercise 1.4.11

```lean
theorem LebesgueMeasurable.boolean_algebra.isSigmaAlgebra (d:ℕ) : (LebesgueMeasurable.boolean_algebra d).isSigmaAlgebra
```

## Exercise 1.4.12

`ConcreteSigmaAlgebra.restrict_is_sigma` (theorem, [line 44](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L44)). Proved here.

> Exercise 1.4.12

```lean
theorem ConcreteSigmaAlgebra.restrict_is_sigma {X:Type*} (B: ConcreteSigmaAlgebra X) (A:Set X): (B.restrict A).isSigmaAlgebra
```

## Exercise 1.4.13

`ConcreteSigmaAlgebra.instInfSet` (instance, [line 113](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L113)). A definition.

> Exercise 1.4.13 (Intersection of sigma-algebras)

```lean
instance ConcreteSigmaAlgebra.instInfSet {X:Type*} : InfSet (ConcreteSigmaAlgebra X)
```

## Definition 1.4.14

`ConcreteSigmaAlgebra.instSupSet` (instance, [line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L129)). A definition.

> Definition 1.4.14 (Generation of σ-algebras)

```lean
instance ConcreteSigmaAlgebra.instSupSet {X:Type*} : SupSet (ConcreteSigmaAlgebra X)
```

## Remark 1.4.15

`ConcreteSigmaAlgebra.induction` (theorem, [line 157](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L157)). Stated without proof.

> Remark 1.4.15

```lean
theorem ConcreteSigmaAlgebra.induction {X:Type*} {F: Set (Set X)} {P: Set X → Prop}
  (h1: P ∅) (h2: ∀ E ∈ F, P E) (h3: ∀ E, P E → P Eᶜ)
  (h4: ∀ (E : ℕ → Set X), (∀ n, P (E n)) → P (⋃ n, E n)) : ∀ E, (ConcreteSigmaAlgebra.generated_by F).measurable E → P E
```

## Definition 1.4.16

`BorelSigmaAlgebra` (def, [line 163](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L163)). A definition.

> Definition 1.4.16 (Borel σ-algebra)

```lean
def BorelSigmaAlgebra (X:Type*) [TopologicalSpace X] : ConcreteSigmaAlgebra X
```

## Exercise 1.4.14 (i)

`BorelSigmaAlgebra.generated_by_open` (theorem, [line 167](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L167)). Proved here.

> Exercise 1.4.14 (i)

```lean
theorem BorelSigmaAlgebra.generated_by_open (d:ℕ) : BorelSigmaAlgebra (EuclideanSpace' d) = ConcreteSigmaAlgebra.generated_by { U : Set (EuclideanSpace' d) | IsOpen U }
```

## Exercise 1.4.14 (ii)

`BorelSigmaAlgebra.generated_by_closed` (theorem, [line 170](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L170)). An exercise, stated without proof.

> Exercise 1.4.14 (ii)

```lean
theorem BorelSigmaAlgebra.generated_by_closed (d:ℕ) : BorelSigmaAlgebra (EuclideanSpace' d) = ConcreteSigmaAlgebra.generated_by { F : Set (EuclideanSpace' d) | IsClosed F }
```

## Exercise 1.4.14 (iii)

`BorelSigmaAlgebra.generated_by_compact` (theorem, [line 173](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L173)). An exercise, stated without proof.

> Exercise 1.4.14 (iii)

```lean
theorem BorelSigmaAlgebra.generated_by_compact (d:ℕ) : BorelSigmaAlgebra (EuclideanSpace' d) = ConcreteSigmaAlgebra.generated_by { K : Set (EuclideanSpace' d) | IsCompact K }
```

## Exercise 1.4.14 (iv)

`BorelSigmaAlgebra.generated_by_open_balls` (theorem, [line 176](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L176)). An exercise, stated without proof.

> Exercise 1.4.14 (iv)

```lean
theorem BorelSigmaAlgebra.generated_by_open_balls (d:ℕ) : BorelSigmaAlgebra (EuclideanSpace' d) = ConcreteSigmaAlgebra.generated_by { B : Set (EuclideanSpace' d) | ∃ x₀ r, B = Metric.ball x₀ r }
```

## Exercise 1.4.14 (v)

`BorelSigmaAlgebra.generated_by_boxes` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L179)). An exercise, stated without proof.

> Exercise 1.4.14 (v)

```lean
theorem BorelSigmaAlgebra.generated_by_boxes (d:ℕ) : BorelSigmaAlgebra (EuclideanSpace' d) = ConcreteSigmaAlgebra.generated_by (Box.toSet '' Set.univ)
```

## Exercise 1.4.14 (vi)

`BorelSigmaAlgebra.generated_by_elementary` (theorem, [line 182](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L182)). An exercise, stated without proof.

> Exercise 1.4.14 (vi)

```lean
theorem BorelSigmaAlgebra.generated_by_elementary (d:ℕ) : BorelSigmaAlgebra (EuclideanSpace' d) = ConcreteSigmaAlgebra.generated_by { E : Set (EuclideanSpace' d) | IsElementary E }
```

## Exercise 1.4.15

`ConcreteSigmaAlgebra.generated_by_eq` (def, [line 186](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L186)). A definition whose value is left as `sorry`.

> Exercise 1.4.15 (Recursive definition of generated sigma-algebra).

```lean
def ConcreteSigmaAlgebra.generated_by_eq {X:Type*} (F: Set (Set X)) :
  (ConcreteSigmaAlgebra.generated_by F).measurableSets =
  ⋃ α < ω₁,
  Ordinal.limitRecOn (motive := fun _ ↦ Set (Set X)) α F (fun n G ↦ { E: Set X | (∃ S: Set G, Countable S ∧ E = ⋃ (H:S), H) ∨ (∃ S: Set G, Countable S ∧ E = (⋃ (H:S), H)ᶜ) }) (fun α _ G ↦ ⋃ (β : Ordinal) (h : β < α), G β h)
```

## Exercise 1.4.16

`ConcreteSigmaAlgebra.card_of_generated_by` (theorem, [line 193](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L193)). An exercise, stated without proof.

> Exercise 1.4.16

```lean
theorem ConcreteSigmaAlgebra.card_of_generated_by {X:Type*} {F: Set (Set X)} [Infinite F] :
  Cardinal.mk (ConcreteSigmaAlgebra.generated_by F).measurableSets ≤ (Cardinal.mk F) ^ ℵ₀
```

## Exercise 1.4.17

`BorelSigmaAlgebra.prod` (theorem, [line 205](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L205)). An exercise, stated without proof.

> Exercise 1.4.17

```lean
theorem BorelSigmaAlgebra.prod {d₁ d₂:ℕ} {E : Set (EuclideanSpace' d₁)} {F : Set (EuclideanSpace' d₂)}
  (hE: (BorelSigmaAlgebra (EuclideanSpace' d₁)).measurable E)
  (hF: (BorelSigmaAlgebra (EuclideanSpace' d₂)).measurable F) :
  (BorelSigmaAlgebra (EuclideanSpace' (d₁ + d₂))).measurable ((EuclideanSpace'.prod_equiv d₁ d₂).symm '' (E ×ˢ F))
```

## Exercise 1.4.18(i)

`BorelSigmaAlgebra.slice_fst` (theorem, [line 213](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L213)). An exercise, stated without proof.

> Exercise 1.4.18(i) (slice along first factor).

```lean
theorem BorelSigmaAlgebra.slice_fst {d₁ d₂:ℕ} {E : Set (EuclideanSpace' (d₁+d₂))}
  (hE: (BorelSigmaAlgebra (EuclideanSpace' (d₁+d₂))).measurable E)
  (x₂ : EuclideanSpace' d₂ ) :
  (BorelSigmaAlgebra (EuclideanSpace' d₁)).measurable { x₁ | (EuclideanSpace'.prod_equiv d₁ d₂).symm ⟨ x₁, x₂ ⟩ ∈ E }
```

`BorelSigmaAlgebra.slice_snd` (theorem, [line 221](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L221)). An exercise, stated without proof.

> Exercise 1.4.18(i) (slice along second factor).

```lean
theorem BorelSigmaAlgebra.slice_snd {d₁ d₂:ℕ} {E : Set (EuclideanSpace' (d₁+d₂))}
  (hE: (BorelSigmaAlgebra (EuclideanSpace' (d₁+d₂))).measurable E)
  (x₁ : EuclideanSpace' d₁ ) :
  (BorelSigmaAlgebra (EuclideanSpace' d₂)).measurable { x₂ | (EuclideanSpace'.prod_equiv d₁ d₂).symm ⟨ x₁, x₂ ⟩ ∈ E }
```

## Exercise 1.4.18(ii)

An `example` ([line 229](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L229)). An exercise, stated without proof.

> Exercise 1.4.18(ii)

```lean
example : ∃ (d₁ d₂ : ℕ) (E : Set (EuclideanSpace' (d₁+d₂))) (x₂ : EuclideanSpace' d₂),
  LebesgueMeasurable E ∧
  ¬ LebesgueMeasurable { x₁ | (EuclideanSpace'.prod_equiv d₁ d₂).symm ⟨ x₁, x₂ ⟩ ∈ E }
```

## Exercise 1.4.19

`LebesgueMeasurable.sigmaAlgebra_generated_by` (theorem, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean#L234)). An exercise, stated without proof.

> Exercise 1.4.19

```lean
theorem LebesgueMeasurable.sigmaAlgebra_generated_by {d:ℕ} :
  LebesgueMeasurable.sigmaAlgebra d = ConcreteSigmaAlgebra.generated_by ( (BorelSigmaAlgebra (EuclideanSpace' d)).measurableSets ∪ (IsNull.sigmaAlgebra d).measurableSets)
```

## Depends on

- [Section 1.4.1: Boolean algebras](section-1-4-1.md)

## Sources

- [Analysis/MeasureTheory/Section_1_4_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_4_2.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_4_2.html)
