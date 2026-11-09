---
declaration: theorem
origin: cited
lean: IsOpen.measurable, IsClosed.measurable, IsNull.measurable, LebesgueMeasurable.empty, LebesgueMeasurable.countable_union, LebesgueMeasurable.complement, LebesgueMeasurable.countable_inter, LebesgueMeasurable.TFAE, Jordan_measurable.lebesgue, CantorSet.compact, Lebesgue_measure.empty, Lebesgue_measure.countable_union, Lebesgue_measure.upward_monotone_convergence, Lebesgue_measure.downward_monotone_convergence, Lebesgue_measure.eq, LebesgueMeasurable.finite_TFAE, LebesgueMeasurable.caratheodory, inner_measure.eq, inner_measure.le, inner_measure.eq_iff, LebesgueMeasurable.TFAE', LebesgueMeasurable.translate, LebesgueMeasurable.linear, Lebesgue_measure.linear, Lebesgue_outer_measure.prod, LebesgueMeasurable.prod, Lebesgue_measure.prod, Lebesgue_measure.unique, IsElementary.ae_equiv, IsElementary.dist, IsElementary.measurable_eq_closure_elem, IsElementary.ae_measure_eq_completion, IsCurve.null
statement: formalized
---

# Section 1.2.2: Lebesgue measurability

> A companion to (the introduction to) Section 1.2.2 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_2_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 41 labelled items, carried by 43 declarations: 9 proved here, 32 stated without proof (32 of them exercises) and 2 definitions (2 with a value left as `sorry`). It also has 31 declarations and 1 example with no label, counted here but not shown.

## Lemma 1.2.13(i)

`IsOpen.measurable` (theorem, [line 11](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L11)). Proved here.

> Lemma 1.2.13(i) (Every open set is Lebesgue measurable).

```lean
theorem IsOpen.measurable {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: IsOpen E) : LebesgueMeasurable E
```

## Lemma 1.2.13(ii)

`IsClosed.measurable` (theorem, [line 285](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L285)). Proved here.

> Lemma 1.2.13(ii) (Every closed set is Lebesgue measurable).

```lean
theorem IsClosed.measurable {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: IsClosed E) : LebesgueMeasurable E
```

## Lemma 1.2.13(iii)

`IsNull.measurable` (theorem, [line 359](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L359)). Proved here.

> Lemma 1.2.13(iii) (Every null set is Lebesgue measurable).

```lean
theorem IsNull.measurable {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: IsNull E) : LebesgueMeasurable E
```

## Lemma 1.2.13(iv)

`LebesgueMeasurable.empty` (theorem, [line 522](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L522)). Proved here.

> Lemma 1.2.13(iv) (Empty set is measurable).

```lean
theorem LebesgueMeasurable.empty {d:ℕ} : LebesgueMeasurable (∅: Set (EuclideanSpace' d))
```

## Lemma 1.2.13(vi)

`LebesgueMeasurable.countable_union` (theorem, [line 540](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L540)). Proved here.

> Lemma 1.2.13(vi) (Countable union of measurable sets is measurable).

```lean
theorem LebesgueMeasurable.countable_union {d:ℕ} {E: ℕ → Set (EuclideanSpace' d)} (hE: ∀ n, LebesgueMeasurable (E n)) : LebesgueMeasurable (⋃ n, E n)
```

## Lemma 1.2.13(v)

`LebesgueMeasurable.complement` (theorem, [line 609](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L609)). Proved here.

> Lemma 1.2.13(v) (Complement of a measurable set is measurable).

```lean
theorem LebesgueMeasurable.complement {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E) : LebesgueMeasurable (Eᶜ)
```

## Lemma 1.2.13(vii)

`LebesgueMeasurable.countable_inter` (theorem, [line 773](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L773)). Proved here.

> Lemma 1.2.13(vii) (Countable intersection of measurable sets is measurable).

```lean
theorem LebesgueMeasurable.countable_inter {d:ℕ} {E: ℕ → Set (EuclideanSpace' d)} (hE: ∀ n, LebesgueMeasurable (E n)) : LebesgueMeasurable (⋂ n, E n)
```

## Exercise 1.2.7

`LebesgueMeasurable.TFAE` (theorem, [line 905](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L905)). An exercise, stated without proof.

> Exercise 1.2.7 (Criteria for measurability).

```lean
theorem LebesgueMeasurable.TFAE {d:ℕ} (E: Set (EuclideanSpace' d)) :
    [
      LebesgueMeasurable E,
      (∀ ε > 0, ∃ U : Set (EuclideanSpace' d), IsOpen U ∧ E ⊆ U ∧ Lebesgue_outer_measure (U \ E) ≤ ε),
      (∀ ε > 0, ∃ U : Set (EuclideanSpace' d), IsOpen U ∧ Lebesgue_outer_measure (symmDiff U E) ≤ ε),
      (∀ ε > 0, ∃ F: Set (EuclideanSpace' d), IsClosed F ∧ F ⊆ E ∧ Lebesgue_outer_measure (E \ F) ≤ ε),
      (∀ ε > 0, ∃ F: Set (EuclideanSpace' d), IsClosed F ∧ Lebesgue_outer_measure (symmDiff F E) ≤ ε),
      (∀ ε > 0, ∃ E': Set (EuclideanSpace' d), LebesgueMeasurable E' ∧ Lebesgue_outer_measure (symmDiff E' E) ≤ ε)
    ].TFAE
```

## Exercise 1.2.8

`Jordan_measurable.lebesgue` (theorem, [line 917](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L917)). An exercise, stated without proof.

> Exercise 1.2.8

```lean
theorem Jordan_measurable.lebesgue {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: JordanMeasurable E) : LebesgueMeasurable E
```

## Exercise 1.2.9

`CantorSet.compact` (theorem, [line 927](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L927)). An exercise, stated without proof.

> Exercise 1.2.9 (Middle thirds Cantor set )

```lean
theorem CantorSet.compact : IsCompact CantorSet
```

## Exercise 1.2.10

An `example` ([line 936](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L936)). An exercise, stated without proof.

> Exercise 1.2.10 (\[0,1) is not the countable union of pairwise disjoint closed intervals).

```lean
example : ¬ ∃ (I: ℕ → BoundedInterval), (∀ n, IsClosed (I n).toSet) ∧ (Set.univ.PairwiseDisjoint (fun n ↦ (I n).toSet) ) ∧ (⋃ n, (I n).toSet = Set.Ico 0 1)
```

An `example` ([line 940](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L940)). An exercise, stated without proof.

> Exercise 1.2.10, challenge version

```lean
example : ¬ ∃ (E: ℕ → Set ℝ), (∀ n, IsClosed (E n)) ∧ (Set.univ.PairwiseDisjoint (fun n ↦ (E n)) ) ∧ (⋃ n, (E n) = Set.Ico 0 1)
```

## Lemma 1.2.15(a)

`Lebesgue_measure.empty` (theorem, [line 948](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L948)). Proved here.

> Lemma 1.2.15(a) (Empty set has zero Lebesgue measure). The proof is missing.

```lean
theorem Lebesgue_measure.empty {d:ℕ} : Lebesgue_measure (∅: Set (EuclideanSpace' d)) = 0
```

## Lemma 1.2.15(b)

`Lebesgue_measure.countable_union` (theorem, [line 1260](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1260)). Proved here.

> Lemma 1.2.15(b) (Countable additivity).
> Strategy: `m(⋃ E_n) = ∑' m(E_n)` for pairwise disjoint measurable sets.
> - Direction ≤: Countable subadditivity (`Lebesgue_outer_measure.union_le`)
> - Direction ≥: Decompose ℝᵈ into annuli Aₘ, express each `E_n = ⋃_m (E_n ∩ Aₘ)`,
>   apply bounded case to the doubly-indexed family $(E_n ∩ Aₘ)$.

```lean
theorem Lebesgue_measure.countable_union {d:ℕ} {E: ℕ → Set (EuclideanSpace' d)} (hmes: ∀ n, LebesgueMeasurable (E n)) (hdisj: Set.univ.PairwiseDisjoint E) : Lebesgue_measure (⋃ n, E n) = ∑' n, Lebesgue_measure (E n)
```

## Exercise 1.2.11(a)

`Lebesgue_measure.upward_monotone_convergence` (theorem, [line 1640](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1640)). An exercise, stated without proof.

> Exercise 1.2.11(a) (Upward monotone convergence).

```lean
theorem Lebesgue_measure.upward_monotone_convergence {d:ℕ} {E: ℕ → Set (EuclideanSpace' d)} (hE: ∀ n, LebesgueMeasurable (E n)) (hmono: ∀ n, E n ⊆ E (n + 1)) : Filter.atTop.Tendsto (fun n ↦ Lebesgue_measure (E n)) (nhds (Lebesgue_measure (⋃ n, E n)))
```

## Exercise 1.2.11(b)

`Lebesgue_measure.downward_monotone_convergence` (theorem, [line 1644](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1644)). An exercise, stated without proof.

> Exercise 1.2.11(b) (Downward monotone convergence).

```lean
theorem Lebesgue_measure.downward_monotone_convergence {d:ℕ} {E: ℕ → Set (EuclideanSpace' d)} (hE: ∀ n, LebesgueMeasurable (E n)) (hmono: ∀ n, E (n+1) ⊆ E n) (hfin: ∃ n, Lebesgue_measure (E n) < ⊤) : Filter.atTop.Tendsto (fun n ↦ Lebesgue_measure (E n)) (nhds (Lebesgue_measure (⋂ n, E n)))
```

## Exercise 1.2.11 (c)

An `example` ([line 1648](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1648)). An exercise, stated without proof.

> Exercise 1.2.11 (c) (counterexample).

```lean
example : ∃ (d:ℕ) (E: ℕ → Set (EuclideanSpace' d)) (hE: ∀ n, LebesgueMeasurable (E n)) (hmono: ∀ n, E (n+1) ⊆ E n), ¬ Filter.atTop.Tendsto (fun n ↦ Lebesgue_measure (E n)) (nhds (Lebesgue_measure (⋂ n, E n)))
```

## Exercise 1.2.12(i)

An `example` ([line 1651](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1651)). An exercise, stated without proof.

> Exercise 1.2.12(i) (Monotonicity)

```lean
example {d:ℕ} (m: Set (EuclideanSpace' d) → EReal) (h_empty: m ∅ = 0) (h_pos: ∀ E, 0 ≤ m E) (hadd: ∀ E: ℕ → Set (EuclideanSpace' d), (Set.univ.PairwiseDisjoint E) → (∀ n, LebesgueMeasurable (E n)) → m (⋃ n, E n) = ∑' n, m (E n)) {E F: Set (EuclideanSpace' d)}
(hsub: E ⊆ F) (hE: LebesgueMeasurable E) (hF: LebesgueMeasurable F) : m E ≤ m F
```

## Exercise 1.2.12(ii)

An `example` ([line 1656](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1656)). An exercise, stated without proof.

> Exercise 1.2.12(ii) (σ-subadditivity)

```lean
example {d:ℕ} (m: Set (EuclideanSpace' d) → EReal) (h_empty: m ∅ = 0) (h_pos: ∀ E, 0 ≤ m E) (hadd: ∀ E: ℕ → Set (EuclideanSpace' d), (Set.univ.PairwiseDisjoint E) → (∀ n, LebesgueMeasurable (E n)) → m (⋃ n, E n) = ∑' n, m (E n)) {E: ℕ → Set (EuclideanSpace' d)} (hE: ∀ n, LebesgueMeasurable (E n)):  m (⋃ n, E n) ≤ ∑' n, m (E n)
```

## Exercise 1.2.13(i)

An `example` ([line 1660](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1660)). An exercise, stated without proof.

> Exercise 1.2.13(i)

```lean
example {d:ℕ} {E: ℕ → Set (EuclideanSpace' d)} {E₀: Set (EuclideanSpace' d)} (hE: ∀ n, LebesgueMeasurable (E n)) (hpoint: ∀ x, Filter.atTop.Tendsto (fun n ↦ (E n).indicator' x) (nhds (E₀.indicator' x))) : LebesgueMeasurable E₀
```

## Exercise 1.2.13(ii)

An `example` ([line 1663](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1663)). An exercise, stated without proof.

> Exercise 1.2.13(ii)

```lean
example {d:ℕ} {E: ℕ → Set (EuclideanSpace' d)} {E₀ F: Set (EuclideanSpace' d)}
  (hE: ∀ n, LebesgueMeasurable (E n))
  (hpoint: ∀ x, Filter.atTop.Tendsto (fun n ↦ (E n).indicator' x) (nhds (E₀.indicator' x)))
  (hsub: ∀ n, E n ⊆ F) (hFmes: LebesgueMeasurable F) (hfin: Lebesgue_measure F < ⊤) : Filter.atTop.Tendsto (fun n ↦ Lebesgue_measure (E n)) (nhds (Lebesgue_measure E₀))
```

## Exercise 1.2.13(iii)

An `example` ([line 1669](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1669)). An exercise, stated without proof.

> Exercise 1.2.13(iii)

```lean
example : ∃ (d:ℕ) (E: ℕ → Set (EuclideanSpace' d)) (E₀ F: Set (EuclideanSpace' d))
  (hE: ∀ n, LebesgueMeasurable (E n))
  (hpoint: ∀ x, Filter.atTop.Tendsto (fun n ↦ (E n).indicator' x) (nhds (E₀.indicator' x)))
  (hsub: ∀ n, E n ⊆ F) (hFmes: LebesgueMeasurable F), ¬ Filter.atTop.Tendsto (fun n ↦ Lebesgue_measure (E n)) (nhds (Lebesgue_measure E₀))
```

## Exercise 1.2.14

An `example` ([line 1675](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1675)). An exercise, stated without proof.

> Exercise 1.2.14

```lean
example {d:ℕ} (E: Set (EuclideanSpace' d)) : ∃ (F: Set (EuclideanSpace' d)), E ⊆ F ∧ LebesgueMeasurable F ∧ Lebesgue_measure F = Lebesgue_outer_measure E
```

## Exercise 1.2.15

`Lebesgue_measure.eq` (theorem, [line 1678](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1678)). An exercise, stated without proof.

> Exercise 1.2.15 (Inner regularity).

```lean
theorem Lebesgue_measure.eq {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E): Lebesgue_measure E = sSup { M | ∃ K, K ⊆ E ∧ IsCompact K ∧ M = Lebesgue_measure K}
```

## Exercise 1.2.16

`LebesgueMeasurable.finite_TFAE` (theorem, [line 1682](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1682)). An exercise, stated without proof.

> Exercise 1.2.16 (Criteria for finite measure).

```lean
theorem LebesgueMeasurable.finite_TFAE {d:ℕ} (E: Set (EuclideanSpace' d)) :
    [
      LebesgueMeasurable E ∧ Lebesgue_measure E < ⊤,
      (∀ ε > 0, ∃ U : Set (EuclideanSpace' d), IsOpen U ∧ E ⊆ U ∧ Lebesgue_measure U < ⊤ ∧ Lebesgue_outer_measure (U \ E) ≤ ε),
      (∀ ε > 0, ∃ U : Set (EuclideanSpace' d), IsOpen U ∧ Bornology.IsBounded U ∧ Lebesgue_outer_measure (symmDiff U E) ≤ ε),
      (∀ ε > 0, ∃ F: Set (EuclideanSpace' d), IsCompact F ∧ F ⊆ E ∧ Lebesgue_outer_measure (E \ F) ≤ ε),
      (∀ ε > 0, ∃ F: Set (EuclideanSpace' d), IsCompact F ∧ Lebesgue_outer_measure (symmDiff F E) ≤ ε),
      (∀ ε > 0, ∃ E': Set (EuclideanSpace' d), LebesgueMeasurable E' ∧ Lebesgue_measure E' < ⊤ ∧ Lebesgue_outer_measure (symmDiff E' E) ≤ ε),
      (∀ ε > 0, ∃ E': Set (EuclideanSpace' d), LebesgueMeasurable E' ∧ Bornology.IsBounded E' ∧ Lebesgue_outer_measure (symmDiff E' E) ≤ ε),
      (∀ ε > 0, ∃ E': Set (EuclideanSpace' d), IsElementary E' ∧ Lebesgue_outer_measure (symmDiff E' E) ≤ ε),
      (∀ ε > 0, ∃ (n:ℤ) (F: Finset (Box d)), (∀ B ∈ F, B.IsDyadicAtScale n) ∧ Lebesgue_outer_measure (symmDiff (⋃ B ∈ F, B.toSet) E) ≤ ε)
    ].TFAE
```

## Exercise 1.2.17

`LebesgueMeasurable.caratheodory` (theorem, [line 1697](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1697)). An exercise, stated without proof.

> Exercise 1.2.17 (Caratheodory criterion one direction).

```lean
theorem LebesgueMeasurable.caratheodory {d:ℕ} (E: Set (EuclideanSpace' d)) :
    [
      LebesgueMeasurable E,
      (∀ A: Set (EuclideanSpace' d), IsElementary A → Lebesgue_outer_measure A = Lebesgue_outer_measure (A ∩ E) + Lebesgue_outer_measure (A \ E)),
      (∀ (B:Box d),  Lebesgue_outer_measure B.toSet = Lebesgue_outer_measure (B.toSet ∩ E) + Lebesgue_outer_measure (B.toSet \ E))
    ].TFAE
```

## Exercise 1.2.18(i)

`inner_measure.eq` (theorem, [line 1711](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1711)). An exercise, stated without proof.

> Exercise 1.2.18(i) (Inner measure).

```lean
theorem inner_measure.eq {d:ℕ} {E A: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E)
  (hA: IsElementary A) (hsub: E ⊆ A) : inner_measure hE = Lebesgue_measure A - Lebesgue_outer_measure (A \ E)
```

## Exercise 1.2.18(ii)

`inner_measure.le` (theorem, [line 1716](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1716)). An exercise, stated without proof.

> Exercise 1.2.18(ii) (Inner measure).

```lean
theorem inner_measure.le {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E)
  : inner_measure hE ≤ Lebesgue_outer_measure E
```

## Exercise 1.2.18(ii')

`inner_measure.eq_iff` (theorem, [line 1721](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1721)). An exercise, stated without proof.

> Exercise 1.2.18(ii') (Inner measure).

```lean
theorem inner_measure.eq_iff {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E)
  : inner_measure hE = Lebesgue_outer_measure E ↔ LebesgueMeasurable E
```

## Exercise 1.2.19

`LebesgueMeasurable.TFAE'` (theorem, [line 1729](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1729)). An exercise, stated without proof.

> Exercise 1.2.19

```lean
theorem LebesgueMeasurable.TFAE' {d:ℕ} (E: Set (EuclideanSpace' d)) :
    [
      LebesgueMeasurable E,
      (∃ F, ∃ N, IsGδ F ∧ IsNull N ∧ E = F \ N),
      (∃ F, ∃ N, IsFσ F ∧ IsNull N ∧ E = F ∪ N)
    ].TFAE
```

## Exercise 1.2.20

`LebesgueMeasurable.translate` (theorem, [line 1740](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1740)). An exercise, stated without proof.

> Exercise 1.2.20 (Translation invariance)

```lean
theorem LebesgueMeasurable.translate {d:ℕ} (E: Set (EuclideanSpace' d)) (x: EuclideanSpace' d) :
    LebesgueMeasurable E ↔ LebesgueMeasurable (E + {x})
```

## Exercise 1.2.21

`LebesgueMeasurable.linear` (lemma, [line 1749](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1749)). An exercise, stated without proof.

> Exercise 1.2.21 (Change of variables, measurability)

```lean
lemma LebesgueMeasurable.linear {d:ℕ} (T: EuclideanSpace' d ≃ₗ[ℝ] EuclideanSpace' d)
{E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E): LebesgueMeasurable (T '' E)
```

`Lebesgue_measure.linear` (lemma, [line 1754](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1754)). An exercise, stated without proof.

> Exercise 1.2.21 (Change of variables, the measure scales by the determinant)

```lean
lemma Lebesgue_measure.linear {d:ℕ} (A: Matrix (Fin d) (Fin d) ℝ) [Invertible A]
 {E: Set (EuclideanSpace' d)} (hE: LebesgueMeasurable E): Lebesgue_measure (A.linear_equiv '' E) = |A.det| * Lebesgue_measure E
```

## Exercise 1.2.22(i)

`Lebesgue_outer_measure.prod` (theorem, [line 1759](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1759)). An exercise, stated without proof.

> Exercise 1.2.22(i) (Outer measure product bound)

```lean
theorem Lebesgue_outer_measure.prod {d₁ d₂:ℕ} {E₁: Set (EuclideanSpace' d₁)} {E₂: Set (EuclideanSpace' d₂)}
  : Lebesgue_outer_measure (EuclideanSpace'.prod E₁ E₂) ≤ Lebesgue_outer_measure E₁ * Lebesgue_outer_measure E₂
```

## Exercise 1.2.22(ii)

`LebesgueMeasurable.prod` (theorem, [line 1763](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1763)). An exercise, stated without proof.

> Exercise 1.2.22(ii) (Measurability of product)

```lean
theorem LebesgueMeasurable.prod {d₁ d₂:ℕ} {E₁: Set (EuclideanSpace' d₁)} {E₂: Set (EuclideanSpace' d₂)}
  (hE₁: LebesgueMeasurable E₁) (hE₂: LebesgueMeasurable E₂) : LebesgueMeasurable (EuclideanSpace'.prod E₁ E₂)
```

## Exercise 1.2.22(ii')

`Lebesgue_measure.prod` (theorem, [line 1767](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1767)). An exercise, stated without proof.

> Exercise 1.2.22(ii') (Product measure formula)

```lean
theorem Lebesgue_measure.prod {d₁ d₂:ℕ} {E₁: Set (EuclideanSpace' d₁)} {E₂: Set (EuclideanSpace' d₂)}
  (hE₁: LebesgueMeasurable E₁) (hE₂: LebesgueMeasurable E₂)
  : Lebesgue_measure (EuclideanSpace'.prod E₁ E₂) = Lebesgue_measure E₁ * Lebesgue_measure E₂
```

## Exercise 1.2.23

`Lebesgue_measure.unique` (theorem, [line 1772](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1772)). An exercise, stated without proof.

> Exercise 1.2.23 (Uniqueness of Lebesgue measure)

```lean
theorem Lebesgue_measure.unique {d:ℕ} (m: Set (EuclideanSpace' d) → EReal)
  (h_empty: m ∅ = 0) (h_pos: ∀ E, 0 ≤ m E)
  (h_add: ∀ E: ℕ → Set (EuclideanSpace' d), (Set.univ.PairwiseDisjoint E) → (∀ n, LebesgueMeasurable (E n)) → m (⋃ n, E n) = ∑' n, m (E n))
  (h_transl: ∀ (x : EuclideanSpace' d) (E : Set (EuclideanSpace' d)), m (E + {x}) = m E)
  (hnorm: m (Box.unit_cube d) = 1)
  : ∀ E, LebesgueMeasurable E → m E = Lebesgue_measure E
```

## Exercise 1.2.24(i)

`IsElementary.ae_equiv` (instance, [line 1780](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1780)). A definition whose value is left as `sorry`.

> Exercise 1.2.24(i) (Lebesgue measure as the completion of elementary measure).

```lean
instance IsElementary.ae_equiv {d:ℕ} {A: Set (EuclideanSpace' d)} (hA: IsElementary A):
Setoid (Set A)
```

## Exercise 1.2.24(ii)

`IsElementary.dist` (def, [line 1791](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1791)). A definition whose value is left as `sorry`.

> Exercise 1.2.24(ii) (Lebesgue measure as the completion of elementary measure).

```lean
noncomputable def IsElementary.dist {d:ℕ} {A: Set (EuclideanSpace' d)} (hA: IsElementary A) : hA.ae_subsets → hA.ae_subsets → ℝ
```

## Exercise 1.2.24(iii)

`IsElementary.measurable_eq_closure_elem` (theorem, [line 1809](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1809)). An exercise, stated without proof.

> Exercise 1.2.24(iii) (Lebesgue measure as the completion of elementary measure).

```lean
theorem IsElementary.measurable_eq_closure_elem {d:ℕ} {A: Set (EuclideanSpace' d)} (hA: IsElementary A) : closure hA.ae_elem = hA.ae_measurable
```

## Exercise 1.2.24(iv)

`IsElementary.ae_measure_eq_completion` (theorem, [line 1817](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1817)). An exercise, stated without proof.

> Exercise 1.2.24(iv) (Lebesgue measure as the completion of elementary measure).

```lean
theorem IsElementary.ae_measure_eq_completion {d:ℕ} {A: Set (EuclideanSpace' d)} (hA: IsElementary A) (m: hA.ae_subsets → ℝ) :
ContinuousOn m hA.ae_measurable ∧ (∀ (E:hA.ae_elem), m E.val = hA.ae_elem_measure E)
↔ (∀ (E:hA.ae_measurable), m E.val = hA.ae_measure E)
```

## Exercise 1.2.25(i)

`IsCurve.null` (theorem, [line 1824](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1824)). An exercise, stated without proof.

> Exercise 1.2.25(i)

```lean
theorem IsCurve.null {d:ℕ} (hd: d ≥ 2) {C: Set (EuclideanSpace' d)} (hC: IsCurve C) : IsNull C
```

## Exercise 1.2.25

An `example` ([line 1830](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean#L1830)). An exercise, stated without proof.

> Exercise 1.2.25

```lean
example {d:ℕ} (hd: d ≥ 2) : ¬ ∃ C: ℕ → Set (EuclideanSpace' d), (∀ n, IsCurve (C n)) ∧ (⋃ n, C n = (Box.unit_cube d).toSet)
```

## Depends on

- [Section 1.2.1: Properties of Lebesgue outer measure](section-1-2-1.md)

## Sources

- [Analysis/MeasureTheory/Section_1_2_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_2.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_2_2.html)
