---
declaration: def
origin: cited
lean: UnsignedMeasurable, UnsignedMeasurable.TFAE, Continuous.UnsignedMeasurable, UnsignedSimpleFunction.unsignedMeasurable, UnsignedMeasurable.sup, UnsignedMeasurable.inf, UnsignedMeasurable.limsup, UnsignedMeasurable.liminf, UnsignedMeasurable.aeEqual, UnsignedMeasurable.aeLimit, UnsignedMeasurable.comp_cts, UnsignedMeasurable.add, UnsignedMeasurable.bounded_iff, UnsignedSimpleFunction.iff, UnsignedMeasurable.measurable_graph, ComplexMeasurable, RealMeasurable.TFAE, Continuous.RealMeasurable, RealSimpleFunction.iff, RealMeasurable.aeEqual, RealMeasurable.aeLimit, RealMeasurable.comp_cts, RealMeasurable.add, RealMeasurable.sub, RealMeasurable.mul, RealMeasurable.riemann_integrable
statement: formalized
---

# Section 1.3.2: Measurable functions

> A companion to (the introduction to) Section 1.3.2 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_3_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 24 labelled items, carried by 27 declarations: 17 proved here, 8 stated without proof (8 of them exercises) and 2 definitions. It also has 59 declarations with no label, counted here but not shown.

## Definition 1.3.8

`UnsignedMeasurable` (def, [line 18](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L18)). A definition.

> Definition 1.3.8 (Unsigned measurable function)

```lean
def UnsignedMeasurable {d:ℕ} (f: EuclideanSpace' d → EReal) : Prop
```

## Lemma 1.3.9

`UnsignedMeasurable.TFAE` (theorem, [line 1683](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1683)). Proved here.

> Lemma 1.3.9 (Equivalent notions of measurability).  Some slight changes to the statement have been made to make the claims cleaner to state

```lean
theorem UnsignedMeasurable.TFAE {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: Unsigned f):
    [
      UnsignedMeasurable f,
      ∃ (g: ℕ → EuclideanSpace' d → EReal), (∀ n, UnsignedSimpleFunction (g n)) ∧ (∀ x, Filter.atTop.Tendsto (fun n ↦ g n x) (nhds (f x))),
      ∃ (g: ℕ → EuclideanSpace' d → EReal), (∀ n, UnsignedSimpleFunction (g n)) ∧ (PointwiseAeConvergesTo g f),
      ∃ (g: ℕ → EuclideanSpace' d → EReal), (∀ n, UnsignedSimpleFunction (g n) ∧  EReal.BoundedFunction (g n) ∧ FiniteMeasureSupport (g n)) ∧ (∀ x, Monotone (fun n ↦ g n x)) ∧ (∀ x, f x = iSup (fun n ↦ g n x)),
      ∀ t, LebesgueMeasurable {x | f x > t},
      ∀ t, LebesgueMeasurable {x | f x ≥ t},
      ∀ t, LebesgueMeasurable {x | f x < t},
      ∀ t, LebesgueMeasurable {x | f x ≤ t},
      ∀ I:BoundedInterval, LebesgueMeasurable (f⁻¹' (Real.toEReal '' I.toSet)),
      ∀ U: Set EReal, IsOpen U → LebesgueMeasurable (f⁻¹' U),
      ∀ K: Set EReal, IsClosed K → LebesgueMeasurable (f⁻¹' K)
    ].TFAE
```

## Exercise 1.3.3(i)

`Continuous.UnsignedMeasurable` (theorem, [line 1717](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1717)). Proved here.

> Exercise 1.3.3(i)

```lean
theorem Continuous.UnsignedMeasurable {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: Continuous f) (hnonneg: Unsigned f): _root_.UnsignedMeasurable f
```

## Exercise 1.3.3(ii)

`UnsignedSimpleFunction.unsignedMeasurable` (theorem, [line 1739](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1739)). Proved here.

> Exercise 1.3.3(ii)

```lean
theorem UnsignedSimpleFunction.unsignedMeasurable {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedSimpleFunction f): UnsignedMeasurable f
```

## Exercise 1.3.3(iii)

`UnsignedMeasurable.sup` (theorem, [line 1743](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1743)). Proved here.

> Exercise 1.3.3(iii)

```lean
theorem UnsignedMeasurable.sup {d:ℕ} {f: ℕ → EuclideanSpace' d → EReal} (hf: ∀ n, UnsignedMeasurable (f n)) : UnsignedMeasurable (fun x ↦ iSup (fun n ↦ f n x))
```

`UnsignedMeasurable.inf` (theorem, [line 1762](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1762)). Proved here.

> Exercise 1.3.3(iii)

```lean
theorem UnsignedMeasurable.inf {d:ℕ} {f: ℕ → EuclideanSpace' d → EReal} (hf: ∀ n, UnsignedMeasurable (f n)) : UnsignedMeasurable (fun x ↦ iInf (fun n ↦ f n x))
```

`UnsignedMeasurable.limsup` (theorem, [line 1782](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1782)). Proved here.

> Exercise 1.3.3(iii)

```lean
theorem UnsignedMeasurable.limsup {d:ℕ} {f: ℕ → EuclideanSpace' d → EReal} (hf: ∀ n, UnsignedMeasurable (f n)) : UnsignedMeasurable (fun x ↦ Filter.atTop.limsup (fun n ↦ f n x) )
```

`UnsignedMeasurable.liminf` (theorem, [line 1787](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1787)). Proved here.

> Exercise 1.3.3(iii)

```lean
theorem UnsignedMeasurable.liminf {d:ℕ} {f: ℕ → EuclideanSpace' d → EReal} (hf: ∀ n, UnsignedMeasurable (f n)) : UnsignedMeasurable (fun x ↦ Filter.atTop.liminf (fun n ↦ f n x) )
```

## Exercise 1.3.3(iv)

`UnsignedMeasurable.aeEqual` (theorem, [line 1792](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1792)). Proved here.

> Exercise 1.3.3(iv)

```lean
theorem UnsignedMeasurable.aeEqual {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg : Unsigned g) (heq: AlmostEverywhereEqual f g) : UnsignedMeasurable g
```

## Exercise 1.3.3(v)

`UnsignedMeasurable.aeLimit` (theorem, [line 1800](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1800)). Proved here.

> Exercise 1.3.3(v)

```lean
theorem UnsignedMeasurable.aeLimit {d:ℕ} {f: EuclideanSpace' d → EReal} (g: ℕ → EuclideanSpace' d → EReal) (hf: ∀ n, UnsignedMeasurable (g n)) (hfn : Unsigned f) (heq: PointwiseAeConvergesTo g f) : UnsignedMeasurable f
```

## Exercise 1.3.3(vi)

`UnsignedMeasurable.comp_cts` (theorem, [line 1807](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1807)). Proved here.

> Exercise 1.3.3(vi)

```lean
theorem UnsignedMeasurable.comp_cts {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) {φ: EReal → EReal} (hφ: Continuous φ) (hφnn : ∀ x ≥ 0, φ x ≥ 0) : UnsignedMeasurable (φ ∘ f)
```

## Exercise 1.3.3(vii)

`UnsignedMeasurable.add` (theorem, [line 1816](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1816)). Proved here.

> Exercise 1.3.3(vii)

```lean
theorem UnsignedMeasurable.add {d:ℕ} {f g: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) (hg: UnsignedMeasurable g) : UnsignedMeasurable (f + g)
```

## Exercise 1.3.4

`UnsignedMeasurable.bounded_iff` (theorem, [line 1830](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1830)). An exercise, stated without proof.

> Exercise 1.3.4

```lean
theorem UnsignedMeasurable.bounded_iff {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: Unsigned f) : UnsignedMeasurable f ∧ EReal.BoundedFunction f ↔ ∃ g : ℕ → EuclideanSpace' d → EReal, (∀ n, UnsignedSimpleFunction (g n) ∧ EReal.BoundedFunction (g n)) ∧ UniformConvergesTo g f
```

## Exercise 1.3.5

`UnsignedSimpleFunction.iff` (theorem, [line 1833](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1833)). An exercise, stated without proof.

> Exercise 1.3.5

```lean
theorem UnsignedSimpleFunction.iff {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: Unsigned f) : UnsignedSimpleFunction f ↔ UnsignedMeasurable f ∧ Finite (f '' Set.univ)
```

## Exercise 1.3.6

`UnsignedMeasurable.measurable_graph` (theorem, [line 1836](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L1836)). An exercise, stated without proof.

> Exercise 1.3.6

```lean
theorem UnsignedMeasurable.measurable_graph {d:ℕ} {f: EuclideanSpace' d → EReal} (hf: UnsignedMeasurable f) : LebesgueMeasurable { p | ∃ x, ∃ t:ℝ, EuclideanSpace'.prod_equiv d 1 p = ⟨ x, t ⟩ ∧ 0 ≤ t ∧ t ≤ f x }
```

## Remark 1.3.10

An `example` ([line 3183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3183)). Proved here.

> Remark 1.3.10: The inverse image of a Lebesgue measurable set by a measurable function
> need not be Lebesgue measurable.
> Proof: Let f = `Remark_1_3_10.binaryToTernary` (maps \[0,1\] → Cantor set), F ⊆ \[0,1\] non-measurable (Vitali).
> Set E = f(F) ⊆ Cantor set. Then E is null (⊆ null set) hence measurable, but f⁻¹(E) = F
> is non-measurable. (Uses injectivity of f on non-dyadic rationals A ⊇ F.)

```lean
example : ∃ (f: EuclideanSpace' 1 → EReal) (_hf: UnsignedMeasurable f) (E: Set (EuclideanSpace' 1)) (_hE: LebesgueMeasurable E), ¬ LebesgueMeasurable (f⁻¹' ((Real.toEReal ∘ EuclideanSpace'.equiv_Real) '' E))
```

## Definition 1.3.11

`ComplexMeasurable` (def, [line 3279](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3279)). A definition.

> Definition 1.3.11 (Complex measurability).

```lean
def ComplexMeasurable {d:ℕ} (f: EuclideanSpace' d → ℂ) : Prop
```

## Exercise 1.3.7

`RealMeasurable.TFAE` (theorem, [line 3336](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3336)). An exercise, stated without proof.

> Exercise 1.3.7

```lean
theorem RealMeasurable.TFAE {d:ℕ} {f: EuclideanSpace' d → ℝ}:
    [
      RealMeasurable f,
      ∃ (g: ℕ → EuclideanSpace' d → ℝ), (∀ n, RealSimpleFunction (g n)) ∧ (PointwiseAeConvergesTo g f),
      UnsignedMeasurable (EReal.pos_fun f) ∧ UnsignedMeasurable (EReal.neg_fun f),
      ∀ U: Set ℝ, IsOpen U → LebesgueMeasurable (f⁻¹' U),
      ∀ K: Set ℝ, IsClosed K → LebesgueMeasurable (f⁻¹' K)
    ].TFAE
```

## Exercise 1.3.8(i)

`Continuous.RealMeasurable` (theorem, [line 3358](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3358)). Proved here.

> Exercise 1.3.8(i)

```lean
theorem Continuous.RealMeasurable {d:ℕ} {f: EuclideanSpace' d → ℝ} (hf: Continuous f) : RealMeasurable f
```

## Exercise 1.3.8(ii)

`RealSimpleFunction.iff` (theorem, [line 3369](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3369)). An exercise, stated without proof.

> Exercise 1.3.8(ii)

```lean
theorem RealSimpleFunction.iff {d:ℕ} {f: EuclideanSpace' d → ℝ} : RealSimpleFunction f ↔ RealMeasurable f ∧ Finite (f '' Set.univ)
```

## Exercise 1.3.8(iii)

`RealMeasurable.aeEqual` (theorem, [line 3374](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3374)). Proved here.

> Exercise 1.3.8(iii)

```lean
theorem RealMeasurable.aeEqual {d:ℕ} {f g: EuclideanSpace' d → ℝ} (hf: RealMeasurable f)
    (heq: AlmostEverywhereEqual f g) : RealMeasurable g
```

## Exercise 1.3.8(iv)

`RealMeasurable.aeLimit` (theorem, [line 3391](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3391)). An exercise, stated without proof.

> Exercise 1.3.8(iv)

```lean
theorem RealMeasurable.aeLimit {d:ℕ} {f: EuclideanSpace' d → ℝ} (g: ℕ → EuclideanSpace' d → ℝ)
    (hf : ∀ n, RealMeasurable (g n))
    (heq: PointwiseAeConvergesTo g f) : RealMeasurable f
```

## Exercise 1.3.8(v)

`RealMeasurable.comp_cts` (theorem, [line 3400](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3400)). Proved here.

> Exercise 1.3.8(v)

```lean
theorem RealMeasurable.comp_cts {d:ℕ} {f: EuclideanSpace' d → ℝ} (hf: RealMeasurable f) {φ: ℝ → ℝ} (hφ: Continuous φ)  : RealMeasurable (φ ∘ f)
```

## Exercise 1.3.8(vi)

`RealMeasurable.add` (theorem, [line 3415](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3415)). Proved here.

> Exercise 1.3.8(vi) (Sum of measurable functions)

```lean
theorem RealMeasurable.add {d:ℕ} {f g: EuclideanSpace' d → ℝ} (hf: RealMeasurable f) (hg: RealMeasurable g) : RealMeasurable (f + g)
```

## Exercise 1.3.8(vi')

`RealMeasurable.sub` (theorem, [line 3430](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3430)). Proved here.

> Exercise 1.3.8(vi') (Difference of measurable functions)

```lean
theorem RealMeasurable.sub {d:ℕ} {f g: EuclideanSpace' d → ℝ} (hf: RealMeasurable f) (hg: RealMeasurable g) : RealMeasurable (f - g)
```

## Exercise 1.3.8(vi'')

`RealMeasurable.mul` (theorem, [line 3447](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3447)). An exercise, stated without proof.

> Exercise 1.3.8(vi'') (Product of measurable functions)

```lean
theorem RealMeasurable.mul {d:ℕ} {f g: EuclideanSpace' d → ℝ} (hf: RealMeasurable f) (hg: RealMeasurable g) : RealMeasurable (f * g)
```

## Exercise 1.3.9

`RealMeasurable.riemann_integrable` (theorem, [line 3454](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean#L3454)). An exercise, stated without proof.

> Exercise 1.3.9

```lean
theorem RealMeasurable.riemann_integrable {f: ℝ → ℝ} {I: BoundedInterval} (hf: RiemannIntegrableOn f I) : RealMeasurable ((fun x ↦ if x ∈ I.toSet then f x else 0) ∘ EuclideanSpace'.equiv_Real)
```

## Depends on

- [Section 1.3.1: Integration of simple functions](section-1-3-1.md)

## Sources

- [Analysis/MeasureTheory/Section_1_3_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_3_2.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_3_2.html)
