---
declaration: abbrev
origin: cited
lean: BoundedInterval.length, Box.volume, IsElementary.union, IsElementary.inter, IsElementary.sdiff, IsElementary.symmDiff, IsElementary.translate, Box.partition, Box.sum_vol_eq, Box.measure_uniq, Box.measure_uniq', IsElementary.measure_uniq, IsElementary.prod
statement: formalized
---

# Section 1.1.1: Elementary measure

> A companion to Section 1.1.1 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_1_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 7 labelled items, carried by 13 declarations: 9 proved here, 2 stated without proof (2 of them exercises) and 2 definitions. It also has 107 declarations and 1 example with no label, counted here but not shown.

## Definition 1.1.1

`BoundedInterval.length` (abbrev, [line 504](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L504)). A definition.

> Definition 1.1.1 (boxes): The length of an interval is max(b - a, 0).

```lean
abbrev BoundedInterval.length (I: BoundedInterval) : ℝ
```

`Box.volume` (abbrev, [line 563](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L563)). A definition.

> Definition 1.1.1 (boxes): The volume of a box is the product of its side lengths.

```lean
abbrev Box.volume {d:ℕ} (B: Box d) : ℝ
```

## Exercise 1.1.1

`IsElementary.union` (theorem, [line 683](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L683)). Proved here.

> Exercise 1.1.1 (Boolean closure): The union of two elementary sets is elementary.

```lean
theorem IsElementary.union {d:ℕ} {E F: Set (EuclideanSpace' d)}
  (hE: IsElementary E) (hF: IsElementary F) : IsElementary (E ∪ F)
```

`IsElementary.inter` (theorem, [line 721](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L721)). Proved here.

> Exercise 1.1.1 (Boolean closure): The intersection of two elementary sets is elementary.

```lean
theorem IsElementary.inter {d:ℕ} {E F: Set (EuclideanSpace' d)}
  (hE: IsElementary E) (hF: IsElementary F) : IsElementary (E ∩ F)
```

`IsElementary.sdiff` (theorem, [line 852](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L852)). Proved here.

> Exercise 1.1.1 (Boolean closure): The set difference of two elementary sets is elementary.

```lean
theorem IsElementary.sdiff {d:ℕ} {E F: Set (EuclideanSpace' d)}
  (hE: IsElementary E) (hF: IsElementary F) : IsElementary (E \ F)
```

`IsElementary.symmDiff` (theorem, [line 884](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L884)). Proved here.

> Exercise 1.1.1 (Boolean closure): The symmetric difference of two elementary sets is elementary.

```lean
theorem IsElementary.symmDiff {d:ℕ} {E F: Set (EuclideanSpace' d)}
  (hE: IsElementary E) (hF: IsElementary F) : IsElementary (symmDiff E F)
```

`IsElementary.translate` (theorem, [line 939](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L939)). Proved here.

> Exercise 1.1.1 (Boolean closure): Translation of an elementary set is elementary.

```lean
theorem IsElementary.translate {d:ℕ} {E: Set (EuclideanSpace' d)}
  (hE: IsElementary E) (x: EuclideanSpace' d) : IsElementary (E + {x})
```

## Lemma 1.1.2(i)

`Box.partition` (theorem, [line 1039](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L1039)). Proved here.

> Lemma 1.1.2(i): Any finset of boxes admits a common refinement into pairwise disjoint sub-boxes.

```lean
theorem Box.partition {d:ℕ} (S: Finset (Box d)) : ∃ T: Finset (Box d), (T : Set (Box d)).PairwiseDisjoint Box.toSet ∧ ∀ I ∈ S, ∃ U : Set T, I = ⋃ J ∈ U, J.val.toSet
```

## Lemma 1.1.2(ii)

`Box.sum_vol_eq` (theorem, [line 1160](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L1160)). Proved here.

> Lemma 1.1.2(ii), helper lemma: Sum of volumes equals limit of lattice counts over a disjoint union.

```lean
theorem Box.sum_vol_eq {d:ℕ} {T: Finset (Box d)}
 (hT: (T : Set (Box d)).PairwiseDisjoint Box.toSet) :
  Filter.atTop.Tendsto (fun N:ℕ ↦ (N:ℝ)^(-d:ℝ) * Nat.card ↥((⋃ B ∈ T, B.toSet) ∩ (Set.range (fun (n:Fin d → ℤ) ↦ .toLp 2 (fun i ↦ (N:ℝ)⁻¹*(n i))))))
  (nhds (∑ B ∈ T, |B|ᵥ))
```

`Box.measure_uniq` (theorem, [line 1195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L1195)). Proved here.

> Lemma 1.1.2(ii): Two disjoint partitions of the same set have equal sums of volumes.

```lean
theorem Box.measure_uniq {d:ℕ} {T₁ T₂: Finset (Box d)}
 (hT₁: (T₁ : Set (Box d)).PairwiseDisjoint Box.toSet)
 (hT₂: (T₂ : Set (Box d)).PairwiseDisjoint Box.toSet)
 (heq: ⋃ B ∈ T₁, B.toSet = ⋃ B ∈ T₂, B.toSet) :
 ∑ B ∈ T₁, |B|ᵥ = ∑ B ∈ T₂, |B|ᵥ
```

## Exercise 1.1.2

`Box.measure_uniq'` (theorem, [line 1219](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L1219)). An exercise, stated without proof.

> Exercise 1.1.2: give an alternate proof of this proposition by showing that
> the two partitions `T₁`, `T₂` admit a mutual refinement into boxes arising from
> taking Cartesian products of elements from finite collections of disjoint intervals.

```lean
theorem Box.measure_uniq' {d:ℕ} {T₁ T₂: Finset (Box d)}
 (hT₁: (T₁ : Set (Box d)).PairwiseDisjoint Box.toSet)
 (hT₂: (T₂ : Set (Box d)).PairwiseDisjoint Box.toSet)
 (heq: ⋃ B ∈ T₁, B.toSet = ⋃ B ∈ T₂, B.toSet) :
 ∑ B ∈ T₁, |B|ᵥ = ∑ B ∈ T₂, |B|ᵥ
```

## Exercise 1.1.3

`IsElementary.measure_uniq` (theorem, [line 1832](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L1832)). An exercise, stated without proof.

> Exercise 1.1.3 (uniqueness of elementary measure): Any non-negative, additive, translation-invariant
> function on elementary sets is a scalar multiple of the standard elementary measure.

```lean
theorem IsElementary.measure_uniq {d:ℕ} {m': (E: Set (EuclideanSpace' d)) → (IsElementary E) → ℝ}
  (hnonneg: ∀ E: Set (EuclideanSpace' d), ∀ hE: IsElementary E, m' E hE ≥ 0)
  (hadd: ∀ E F: Set (EuclideanSpace' d), ∀ (hE: IsElementary E) (hF: IsElementary F),
   Disjoint E F → m' (E ∪ F) (hE.union hF) = m' E hE + m' F hF)
  (htrans: ∀ E: Set (EuclideanSpace' d), ∀ (hE: IsElementary E) (x: EuclideanSpace' d), m' (E + {x}) (hE.translate x) = m' E hE) : ∃ c, c ≥ 0 ∧ ∀ E: Set (EuclideanSpace' d), ∀ hE: IsElementary E, m' E hE = c * hE.measure
```

## Exercise 1.1.4

`IsElementary.prod` (theorem, [line 1956](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean#L1956)). Proved here.

> Exercise 1.1.4: The Cartesian product of two elementary sets is elementary.

```lean
theorem IsElementary.prod {d₁ d₂:ℕ} {E₁: Set (EuclideanSpace' d₁)} {E₂: Set (EuclideanSpace' d₂)}
  (hE₁: IsElementary E₁) (hE₂: IsElementary E₂) : IsElementary (EuclideanSpace'.prod E₁ E₂)
```

## Depends on

- [Chapter 0: Notation](../notation.md)
- [Section 9.1: Subsets of the real line](../../analysis-i/chapter-9/section-9-1.md)

## Sources

- [Analysis/MeasureTheory/Section_1_1_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_1.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_1_1.html)
