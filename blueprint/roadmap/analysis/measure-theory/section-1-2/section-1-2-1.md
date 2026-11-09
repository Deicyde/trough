---
declaration: theorem
origin: cited
lean: Lebesgue_outer_measure.of_empty, Lebesgue_outer_measure.mono, Lebesgue_outer_measure.union_le, Lebesgue_outer_measure.union_of_separated, dist_of_disj_compact_pos, Lebesgue_outer_measure.elementary, Lebesgue_outer_measure.union_of_almost_disjoint, Box.sum_volume_eq, Lebesgue_outer_measure.eq_Jordan_inner_of_boxes, IsOpen.eq_union_boxes, Lebesgue_outer_measure.eq
statement: formalized
---

# Section 1.2.1: Properties of Lebesgue outer measure

> A companion to (the introduction to) Section 1.2.1 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_2_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 13 labelled items, carried by 14 declarations: 10 proved here and 4 stated without proof (4 of them exercises). It also has 138 declarations and 2 examples with no label, counted here but not shown.

## Exercise 1.2.3(i)

`Lebesgue_outer_measure.of_empty` (theorem, [line 52](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L52)). Proved here.

> Exercise 1.2.3(i) (Empty set)

```lean
theorem Lebesgue_outer_measure.of_empty (d:ℕ) : Lebesgue_outer_measure (∅: Set (EuclideanSpace' d)) = 0
```

## Exercise 1.2.3(ii)

`Lebesgue_outer_measure.mono` (theorem, [line 58](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L58)). Proved here.

> Exercise 1.2.3(ii) (Monotonicity)

```lean
theorem Lebesgue_outer_measure.mono {d: ℕ} {E F : Set (EuclideanSpace' d)} (h : E ⊆ F) :
    Lebesgue_outer_measure E ≤ Lebesgue_outer_measure F
```

## Exercise 1.2.3(iii)

`Lebesgue_outer_measure.union_le` (theorem, [line 86](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L86)). An exercise, stated without proof.

> Exercise 1.2.3(iii) (Countable subadditivity)

```lean
theorem Lebesgue_outer_measure.union_le {d: ℕ} (E : ℕ → Set (EuclideanSpace' d)) :
    Lebesgue_outer_measure (⋃ i, E i) ≤ ∑' i, Lebesgue_outer_measure (E i)
```

## Lemma 1.2.5

`Lebesgue_outer_measure.union_of_separated` (theorem, [line 1925](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L1925)). Proved here.

> Lemma 1.2.5 (Finite additivity for separated sets).
> If E and F are separated (dist(E,F) > 0), then m\*(E ∪ F) = m\*(E) + m\*(F).
>
> Proof strategy (from textbook):
> 1. Direction ≤: Use subadditivity
> 2. Direction ≥: Show m\*(E ∪ F) ≥ m\*(E) + m\*(F)
>    - If m\*(E ∪ F) = ⊤, trivial
>    - If m\*(E ∪ F) < ⊤:
>      \* Get epsilon-close cover of E ∪ F
>      \* Refine cover so all boxes have diameter < dist(E,F)
>      \* Partition boxes into E-intersecting and F-intersecting (disjoint by geometric separation)
>      \* Sum volumes separately: m\*(E) + m\*(F) ≤ sum of refined cover ≤ m\*(E ∪ F) + ε
>      \* Take ε → 0 to conclude

```lean
theorem Lebesgue_outer_measure.union_of_separated {d:ℕ} (hd: 0 < d) {E F : Set (EuclideanSpace' d)}
    (hsep: set_dist E F > 0) :
    Lebesgue_outer_measure (E ∪ F) = Lebesgue_outer_measure E + Lebesgue_outer_measure F
```

## Exercise 1.2.4

`dist_of_disj_compact_pos` (theorem, [line 2172](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L2172)). An exercise, stated without proof.

> Exercise 1.2.4

```lean
theorem dist_of_disj_compact_pos {d:ℕ} (E F: Set (EuclideanSpace' d)) (hEn: E.Nonempty) (hFn: F.Nonempty)
    (hE: IsCompact E) (hF: IsCompact F) (hdisj: E ∩ F = ∅) :
    set_dist E F > 0
```

## Lemma 1.2.6

`Lebesgue_outer_measure.elementary` (theorem, [line 3107](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L3107)). Proved here.

> Lemma 1.2.6 (Outer measure of elementary sets).
> For any elementary set E, Lebesgue outer measure equals elementary measure.

```lean
theorem Lebesgue_outer_measure.elementary {d:ℕ} (E: Set (EuclideanSpace' d)) (hE: IsElementary E) :
    Lebesgue_outer_measure E = hE.measure
```

## Remark 1.2.8

An `example` ([line 3560](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L3560)). Proved here.

> Remark 1.2.8: There exists a bounded open set that is not Jordan measurable.
> Proof sketch: Take U = ⋃\_\{n\} (q\_n - ε/2^\{n+1\}, q\_n + ε/2^\{n+1\}) where \{q\_n\} enumerates ℚ ∩ \[0,1\].
> U is open and bounded. By countable subadditivity, m\*(U) ≤ 2ε.
> By density of ℚ, closure(U) ⊇ \[0,1\], so m\*,J(U) ≥ 1.
> For ε = 1/3, we get m\*(U) ≤ 2/3 < 1 ≤ m\*,J(U), contradicting Jordan measurability.

```lean
example : ∃ (E: Set (EuclideanSpace' 1)), Bornology.IsBounded E ∧
    IsOpen E ∧ ¬ JordanMeasurable E
```

An `example` ([line 3614](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L3614)). Proved here.

> Remark 1.2.8: The complement of U in \[-2,2\] is compact but not Jordan measurable.

```lean
example : ∃ (E: Set (EuclideanSpace' 1)), Bornology.IsBounded E ∧
    IsCompact E ∧ ¬ JordanMeasurable E
```

## Lemma 1.2.9

`Lebesgue_outer_measure.union_of_almost_disjoint` (theorem, [line 4129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L4129)). Proved here.

> Lemma 1.2.9 (Outer measure of countable unions of almost disjoint boxes).
> For pairwise almost disjoint boxes, m*(⋃ Bᵢ) = ∑' m*(Bᵢ) = ∑' |Bᵢ|.

```lean
theorem Lebesgue_outer_measure.union_of_almost_disjoint {d:ℕ} {B : ℕ → Box d} (h : Pairwise (Function.onFun AlmostDisjoint B)) :
    Lebesgue_outer_measure (⋃ i, (B i).toSet) = ∑' i, Lebesgue_outer_measure (B i).toSet
```

## Remark 1.2.10

`Box.sum_volume_eq` (theorem, [line 4294](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L4294)). Proved here.

> Remark 1.2.10

```lean
theorem Box.sum_volume_eq {d:ℕ} (B B': ℕ → Box d) (hdisj: Pairwise (Function.onFun AlmostDisjoint B)) (hdisj': Pairwise (Function.onFun AlmostDisjoint B')) (hcover: (⋃ n, (B n).toSet) = (⋃ n, (B' n).toSet)) :
    ∑' n, (B n).volume = ∑' n, (B' n).volume
```

## Exercise 1.2.5

`Lebesgue_outer_measure.eq_Jordan_inner_of_boxes` (theorem, [line 4351](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L4351)). An exercise, stated without proof.

> Exercise 1.2.5: For any set that equals a countable union of almost disjoint boxes,
> the Lebesgue outer measure equals the Jordan inner measure.  The text asserts this for
> unbounded sets too, "where we extend the definition of Jordan inner measure to unbounded sets
> in the obvious manner", so `Jordan_inner_measure'` is the notion intended here; stated
> with the real-valued `Jordan_inner_measure` the claim is false, as the whole space
> shows.

```lean
theorem Lebesgue_outer_measure.eq_Jordan_inner_of_boxes {d:ℕ} (E: Set (EuclideanSpace' d)) (B: ℕ → Box d)
    (hE: E = ⋃ n, (B n).toSet) (hdisj: Pairwise (Function.onFun AlmostDisjoint B)) :
    Lebesgue_outer_measure E = Jordan_inner_measure' E
```

## Lemma 1.2.11

`IsOpen.eq_union_boxes` (theorem, [line 4876](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L4876)). Proved here.

> Lemma 1.2.11: Every open set is a countable union of almost disjoint dyadic cubes.
> Note: every dyadic cube is nonempty
>     Proof outline:
>     1. For each x ∈ E, by `IsOpen.exists_dyadic_cube_subset`, there exists a dyadic cube containing x ⊆ E
>     2. The set of all such dyadic cubes is countable (subset of `ℕ × (Fin d → ℤ)`)
>     3. Take maximal cubes (not strictly contained in another cube in the collection)
>     4. By `DyadicCube.nesting`, distinct maximal cubes are almost disjoint
>     5. E equals the union of these maximal cubes

```lean
theorem IsOpen.eq_union_boxes {d:ℕ} (hd : 0 < d) (E: Set (EuclideanSpace' d)) (hE: IsOpen E)
    (hE_nonempty : E.Nonempty) :
    ∃ B: ℕ → Box d, (E = ⋃ n, (B n).toSet) ∧ (∀ n, (B n).IsDyadic) ∧
    Pairwise (Function.onFun AlmostDisjoint B)
```

## Lemma 1.2.12

`Lebesgue_outer_measure.eq` (theorem, [line 5273](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L5273)). Proved here.

> Lemma 1.2.12 (Outer regularity). m\*(E) = inf\{m\*(U) : E ⊆ U, U open\}.

```lean
theorem Lebesgue_outer_measure.eq {d:ℕ} (E: Set (EuclideanSpace' d)) : Lebesgue_outer_measure E = sInf { M | ∃ U, E ⊆ U ∧ IsOpen U ∧ M = Lebesgue_outer_measure U}
```

## Exercise 1.2.6

An `example` ([line 5641](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean#L5641)). An exercise, stated without proof.

> Exercise 1.2.6

```lean
example : ∃ (d:ℕ) (E: Set (EuclideanSpace' d)), Lebesgue_outer_measure E ≠ sSup { M | ∃ U, U ⊆ E ∧ IsOpen U ∧ M = Lebesgue_outer_measure U}
```

## Depends on

- [Section 1.2: Lebesgue measure](section-1-2-0.md)

## Sources

- [Analysis/MeasureTheory/Section_1_2_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_1.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_2_1.html)
