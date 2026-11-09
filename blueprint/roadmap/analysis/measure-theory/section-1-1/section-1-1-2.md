---
declaration: abbrev
origin: cited
lean: Jordan_inner_measure, Jordan_inner_measure', JordanMeasurable.equiv, JordanMeasurable.union, JordanMeasurable.inter, JordanMeasurable.sdiff, JordanMeasurable.symmDiff, JordanMeasurable.nonneg, JordanMeasurable.measure_of_disjUnion', JordanMeasurable.mono, JordanMeasurable.mes_of_union, JordanMeasurable.measure_of_union', JordanMeasurable.translate, JordanMeasurable.measure_of_translate, JordanMeasurable.graph, JordanMeasurable.measure_of_graph, JordanMeasurable.undergraph, JordanMeasurable.triangle, JordanMeasurable.measure_triangle, IsPolytope, JordanMeasurable.polytope, JordanMeasurable.ball, JordanMeasurable.closedBall, JordanMeasurable.measure_ball, JordanMeasurable.measure_ball_le, JordanMeasurable.le_measure_ball, JordanMeasurable.linear_of_elem, JordanMeasurable.measure_linear_of_elem, JordanMeasurable.linear, JordanMeasurable.measure_linear, JordanMeasurable.measure_linear_det, JordanMeasurable.null_mono, JordanMeasure.measure_eq, JordanMeasure.iff, JordanMeasure.measure_uniq, JordanMeasurable.prod, JordanMeasurable.measure_of_equidecomposable, JordanMeasurable.outer_measure_of_closure, JordanMeasurable.inner_measure_of_interior, JordanMeasurable.iff_boundary_null, JordanMeasurable.caratheodory
statement: formalized
---

# Section 1.1.2: Jordan measure

> A companion to Section 1.1.2 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_1_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 22 labelled items, carried by 41 declarations: 13 proved here, 25 stated without proof (25 of them exercises) and 3 definitions. It also has 57 declarations with no label, counted here but not shown.

## Definition 1.1.4

`Jordan_inner_measure` (abbrev, [line 14](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L14)). A definition.

> Definition 1.1.4.  We intend these concepts to only be applied for bounded sets `E`, but
> it is convenient to permit `E` to be unbounded for the purposes of making the definitions.

```lean
noncomputable abbrev Jordan_inner_measure {d:ℕ} (E: Set (EuclideanSpace' d)) : ℝ
```

`Jordan_inner_measure'` (abbrev, [line 26](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L26)). A definition.

> Definition 1.1.4, extended to unbounded sets.  Exercise 1.2.5 of the text asks for the Jordan
> inner measure "extended to unbounded sets in the obvious manner".  Because
> `Jordan_inner_measure` is real-valued, its supremum returns the junk value zero whenever the
> elementary subsets of a set have unbounded measure, as happens for the whole space; this variant
> takes the supremum in `EReal` instead, so that such a set receives the value infinity.  The
> two agree on bounded sets, by Jordan_inner_measure'_eq_coe below.

```lean
noncomputable abbrev Jordan_inner_measure' {d:ℕ} (E: Set (EuclideanSpace' d)) : EReal
```

## Exercise 1.1.5

`JordanMeasurable.equiv` (theorem, [line 422](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L422)). Proved here.

> Exercise 1.1.5

```lean
theorem JordanMeasurable.equiv {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E) :
 [JordanMeasurable E,
  ∀ ε>0, ∃ A, ∃ B, ∃ hA: IsElementary A, ∃ hB: IsElementary B,
    A ⊆ E ∧ E ⊆ B ∧ (hB.sdiff hA).measure ≤ ε,
  ∀ ε>0, ∃ A, ∃ hA: IsElementary A, Jordan_outer_measure (symmDiff E A) ≤ ε].TFAE
```

## Exercise 1.1.6 (i)

`JordanMeasurable.union` (theorem, [line 519](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L519)). Proved here.

> Exercise 1.1.6 (i) (Boolean closure)

```lean
theorem JordanMeasurable.union {d:ℕ} {E F : Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (hF: JordanMeasurable F) : JordanMeasurable (E ∪ F)
```

`JordanMeasurable.inter` (theorem, [line 575](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L575)). Proved here.

> Exercise 1.1.6 (i) (Boolean closure)

```lean
theorem JordanMeasurable.inter {d:ℕ} {E F : Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (hF: JordanMeasurable F) : JordanMeasurable (E ∩ F)
```

`JordanMeasurable.sdiff` (theorem, [line 628](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L628)). Proved here.

> Exercise 1.1.6 (i) (Boolean closure)

```lean
theorem JordanMeasurable.sdiff {d:ℕ} {E F : Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (hF: JordanMeasurable F) : JordanMeasurable (E \ F)
```

`JordanMeasurable.symmDiff` (theorem, [line 680](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L680)). Proved here.

> Exercise 1.1.6 (i) (Boolean closure)

```lean
theorem JordanMeasurable.symmDiff {d:ℕ} {E F : Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (hF: JordanMeasurable F) : JordanMeasurable (symmDiff E F)
```

## Exercise 1.1.6 (ii)

`JordanMeasurable.nonneg` (theorem, [line 685](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L685)). Proved here.

> Exercise 1.1.6 (ii) (non-negativity)

```lean
theorem JordanMeasurable.nonneg {d:ℕ} {E : Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) : 0 ≤ hE.measure
```

## Exercise 1.1.6 (iii)

`JordanMeasurable.measure_of_disjUnion'` (lemma, [line 768](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L768)). Proved here.

> Exercise 1.1.6 (iii) (finite additivity)

```lean
lemma JordanMeasurable.measure_of_disjUnion' {d:ℕ} {S: Finset (Set (EuclideanSpace' d))}
(hE: ∀ E ∈ S, JordanMeasurable E) (hdisj: (S : Set (Set (EuclideanSpace' d))).PairwiseDisjoint id):
  (JordanMeasurable.union' hE).measure = ∑ E:S, (hE E.val E.property).measure
```

## Exercise 1.1.6 (iv)

`JordanMeasurable.mono` (theorem, [line 800](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L800)). Proved here.

> Exercise 1.1.6 (iv) (monotonicity)

```lean
theorem JordanMeasurable.mono {d:ℕ} {E F : Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (hF: JordanMeasurable F) (hEF: E ⊆ F)
  : hE.measure ≤ hF.measure
```

## Exercise 1.1.6 (v)

`JordanMeasurable.mes_of_union` (theorem, [line 814](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L814)). Proved here.

> Exercise 1.1.6 (v) (finite subadditivity)

```lean
theorem JordanMeasurable.mes_of_union {d:ℕ} {E F : Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (hF: JordanMeasurable F)
  : (hE.union hF).measure ≤ hE.measure + hF.measure
```

`JordanMeasurable.measure_of_union'` (lemma, [line 835](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L835)). Proved here.

> Exercise 1.1.6 (v) (finite subadditivity)

```lean
lemma JordanMeasurable.measure_of_union' {d:ℕ} {S: Finset (Set (EuclideanSpace' d))}
(hE: ∀ E ∈ S, JordanMeasurable E) :
  (JordanMeasurable.union' hE).measure ≤ ∑ E:S, (hE E.val E.property).measure
```

## Exercise 1.1.6 (vi)

`JordanMeasurable.translate` (theorem, [line 850](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L850)). Proved here.

> Exercise 1.1.6 (vi) (translation invariance)

```lean
theorem JordanMeasurable.translate {d:ℕ} {E: Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (x: EuclideanSpace' d) : JordanMeasurable (E + {x})
```

`JordanMeasurable.measure_of_translate` (lemma, [line 901](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L901)). Proved here.

> Exercise 1.1.6 (vi) (translation invariance)

```lean
lemma JordanMeasurable.measure_of_translate {d:ℕ} {E: Set (EuclideanSpace' d)}
(hE: JordanMeasurable E) (x: EuclideanSpace' d):
  (hE.translate x).measure ≤ hE.measure
```

## Exercise 1.1.7 (i)

`JordanMeasurable.graph` (lemma, [line 920](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L920)). An exercise, stated without proof.

> Exercise 1.1.7 (i) (Regions under graphs are Jordan measurable)

```lean
lemma JordanMeasurable.graph {d:ℕ} {B:Box d} (hB: IsClosed B.toSet) {f: EuclideanSpace' d → ℝ}
  (hf: ContinuousOn f B.toSet) :
  JordanMeasurable { p | ∃ x ∈ B.toSet, EuclideanSpace'.prod_equiv d 1 p = ⟨ x, f x ⟩ }
```

`JordanMeasurable.measure_of_graph` (lemma, [line 926](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L926)). An exercise, stated without proof.

> Exercise 1.1.7 (i) (Regions under graphs are Jordan measurable)

```lean
lemma JordanMeasurable.measure_of_graph {d:ℕ} {B:Box d} (hB: IsClosed B.toSet)
  {f: EuclideanSpace' d → ℝ} (hf: ContinuousOn f B.toSet) :
  (JordanMeasurable.graph hB hf).measure = 0
```

`JordanMeasurable.undergraph` (lemma, [line 932](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L932)). An exercise, stated without proof.

> Exercise 1.1.7 (i) (Regions under graphs are Jordan measurable)

```lean
lemma JordanMeasurable.undergraph {d:ℕ} {B:Box d} (hB: IsClosed B.toSet)
  {f: EuclideanSpace' d → ℝ} (hf: ContinuousOn f B.toSet) :
  JordanMeasurable
    { p | ∃ x ∈ B.toSet, ∃ t:ℝ, EuclideanSpace'.prod_equiv d 1 p = ⟨ x, t ⟩ ∧ 0 ≤ t ∧ t ≤ f x }
```

## Exercise 1.1.8(i)

`JordanMeasurable.triangle` (lemma, [line 939](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L939)). An exercise, stated without proof.

> Exercise 1.1.8(i) (A triangle is Jordan measurable)

```lean
lemma JordanMeasurable.triangle (T: Affine.Triangle ℝ (EuclideanSpace' 2)) : JordanMeasurable T.closedInterior
```

## Exercise 1.1.8(ii)

`JordanMeasurable.measure_triangle` (lemma, [line 946](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L946)). An exercise, stated without proof.

> Exercise 1.1.8(ii) (Jordan measure of a triangle)

```lean
lemma JordanMeasurable.measure_triangle (T: Affine.Triangle ℝ (EuclideanSpace' 2)) : (JordanMeasurable.triangle T).measure = |(T.points 1 - T.points 0).plane_wedge (T.points 2 - T.points 0)| / 2
```

## Exercise 1.1.9

`IsPolytope` (abbrev, [line 950](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L950)). A definition.

> Exercise 1.1.9  A polytope is the convex hull of a finite set of vertices.

```lean
abbrev IsPolytope {d:ℕ} (P: Set (EuclideanSpace' d)) : Prop
```

`JordanMeasurable.polytope` (lemma, [line 954](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L954)). An exercise, stated without proof.

> Exercise 1.1.9: Every polytope is Jordan measurable.

```lean
lemma JordanMeasurable.polytope {d:ℕ} {P: Set (EuclideanSpace' d)} (hP: IsPolytope P) : JordanMeasurable P
```

## Exercise 1.1.10

`JordanMeasurable.ball` (lemma, [line 959](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L959)). An exercise, stated without proof.

> Exercise 1.1.10 (1)

```lean
lemma JordanMeasurable.ball {d:ℕ} (x₀: EuclideanSpace' d) {r: ℝ} (hr: 0 < r) : JordanMeasurable (Metric.ball x₀ r)
```

`JordanMeasurable.closedBall` (lemma, [line 964](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L964)). An exercise, stated without proof.

> Exercise 1.1.10 (1)

```lean
lemma JordanMeasurable.closedBall {d:ℕ} (x₀: EuclideanSpace' d) {r: ℝ} (hr: 0 < r) : JordanMeasurable (Metric.closedBall x₀ r)
```

`JordanMeasurable.measure_ball` (lemma, [line 970](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L970)). An exercise, stated without proof.

> Exercise 1.1.10 (1)

```lean
lemma JordanMeasurable.measure_ball (d:ℕ) : ∃ c, ∀ (x₀: EuclideanSpace' d) (r: ℝ) (hr: 0 < r), (ball x₀ hr).measure = c * r^d
```

`JordanMeasurable.measure_ball_le` (lemma, [line 977](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L977)). An exercise, stated without proof.

> Exercise 1.1.10 (2)

```lean
lemma JordanMeasurable.measure_ball_le (d:ℕ) : (measure_ball d).choose ≤ 2^d
```

`JordanMeasurable.le_measure_ball` (lemma, [line 981](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L981)). An exercise, stated without proof.

> Exercise 1.1.10 (2)

```lean
lemma JordanMeasurable.le_measure_ball (d:ℕ) : 2^d/d.factorial ≤ (measure_ball d).choose
```

## Exercise 1.1.11

`JordanMeasurable.linear_of_elem` (lemma, [line 985](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L985)). An exercise, stated without proof.

> Exercise 1.1.11 (1)

```lean
lemma JordanMeasurable.linear_of_elem {d:ℕ} (T: EuclideanSpace' d ≃ₗ[ℝ] EuclideanSpace' d)
{E: Set (EuclideanSpace' d)} (hE: IsElementary E): JordanMeasurable (T '' E)
```

`JordanMeasurable.measure_linear_of_elem` (lemma, [line 991](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L991)). An exercise, stated without proof.

> Exercise 1.1.11 (1)

```lean
lemma JordanMeasurable.measure_linear_of_elem {d:ℕ} (T: EuclideanSpace' d ≃ₗ[ℝ] EuclideanSpace' d) : ∃ D > 0, ∀ (E: Set (EuclideanSpace' d)) (hE: IsElementary E), (linear_of_elem T hE).measure = D * hE.measure
```

`JordanMeasurable.linear` (lemma, [line 995](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L995)). An exercise, stated without proof.

> Exercise 1.1.11 (2)

```lean
lemma JordanMeasurable.linear {d:ℕ} (T: EuclideanSpace' d ≃ₗ[ℝ] EuclideanSpace' d)
{E: Set (EuclideanSpace' d)} (hE: JordanMeasurable E): JordanMeasurable (T '' E)
```

`JordanMeasurable.measure_linear` (lemma, [line 1001](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1001)). An exercise, stated without proof.

> Exercise 1.1.11 (2)

```lean
lemma JordanMeasurable.measure_linear {d:ℕ} (T: EuclideanSpace' d ≃ₗ[ℝ] EuclideanSpace' d) :
∃ D > 0, ∀ (E: Set (EuclideanSpace' d)) (hE: JordanMeasurable E), (linear T hE).measure = D * hE.measure
```

`JordanMeasurable.measure_linear_det` (lemma, [line 1020](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1020)). An exercise, stated without proof.

> Exercise 1.1.11 (3)

```lean
lemma JordanMeasurable.measure_linear_det {d:ℕ} (A: Matrix (Fin d) (Fin d) ℝ) [Invertible A] :
(measure_linear A.linear_equiv).choose = |A.det|
```

## Exercise 1.1.12

`JordanMeasurable.null_mono` (lemma, [line 1032](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1032)). An exercise, stated without proof.

> Exercise 1.1.12

```lean
lemma JordanMeasurable.null_mono {d:ℕ} {E F: Set (EuclideanSpace' d)} (h: null E) (hEF: F ⊆ E) : null F
```

## Exercise 1.1.13

`JordanMeasure.measure_eq` (theorem, [line 1037](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1037)). An exercise, stated without proof.

> Exercise 1.1.13

```lean
theorem JordanMeasure.measure_eq {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: JordanMeasurable E):
  Filter.atTop.Tendsto (fun N:ℕ ↦ (N:ℝ)^(-d:ℝ) * Nat.card ↥(E ∩ (Set.range (fun (n:Fin d → ℤ) ↦ .toLp 2 (fun i ↦ (N:ℝ)⁻¹*(n i))))))
  (nhds hE.measure)
```

## Exercise 1.1.14

`JordanMeasure.iff` (theorem, [line 1053](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1053)). An exercise, stated without proof.

> Exercise 1.1.14

```lean
theorem JordanMeasure.iff {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E) :
  JordanMeasurable E ↔ Filter.atTop.Tendsto (fun n ↦ (2:ℝ)^(-(d*n:ℤ)) * ((metric_entropy_upper E n - metric_entropy_lower E n))) (nhds 0)
```

## Exercise 1.1.15

`JordanMeasure.measure_uniq` (theorem, [line 1065](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1065)). An exercise, stated without proof.

> Exercise 1.1.15 (Uniqueness of Jordan measure)

```lean
theorem JordanMeasure.measure_uniq {d:ℕ} {m': (E: Set (EuclideanSpace' d)) → (JordanMeasurable E) → ℝ}
  (hnonneg: ∀ E: Set (EuclideanSpace' d), ∀ hE: JordanMeasurable E, m' E hE ≥ 0)
  (hadd: ∀ E F: Set (EuclideanSpace' d), ∀ (hE: JordanMeasurable E) (hF: JordanMeasurable F),
   Disjoint E F → m' (E ∪ F) (hE.union hF) = m' E hE + m' F hF)
  (htrans: ∀ E: Set (EuclideanSpace' d), ∀ (hE: JordanMeasurable E) (x: EuclideanSpace' d), m' (E + {x}) (hE.translate x) = m' E hE) : ∃ c, c ≥ 0 ∧ ∀ E: Set (EuclideanSpace' d), ∀ hE: JordanMeasurable E, m' E hE = c * hE.measure
```

## Exercise 1.1.16

`JordanMeasurable.prod` (theorem, [line 1225](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1225)). Proved here.

> Exercise 1.1.16

```lean
theorem JordanMeasurable.prod {d₁ d₂:ℕ} {E₁: Set (EuclideanSpace' d₁)} {E₂: Set (EuclideanSpace' d₂)}
  (hE₁: JordanMeasurable E₁) (hE₂: JordanMeasurable E₂) : JordanMeasurable (EuclideanSpace'.prod E₁ E₂)
```

## Exercise 1.1.17

`JordanMeasurable.measure_of_equidecomposable` (theorem, [line 1250](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1250)). An exercise, stated without proof.

> Exercise 1.1.17

```lean
theorem JordanMeasurable.measure_of_equidecomposable {d n:ℕ} {E F: Set (EuclideanSpace' d)}
  (hE: JordanMeasurable E) (hF: JordanMeasurable F)
  {P Q: Fin n → Set (EuclideanSpace' d)} (hPQ: ∀ i, Isometric (P i) (Q i))
  (hPE: E = ⋃ i, P i) (hQF: F = ⋃ i, Q i) (hPdisj: Set.PairwiseDisjoint .univ P)
  (hQdisj: Set.PairwiseDisjoint .univ (fun i ↦ (interior (Q i)))) : hE.measure = hF.measure
```

## Exercise 1.1.18

`JordanMeasurable.outer_measure_of_closure` (theorem, [line 1259](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1259)). An exercise, stated without proof.

> Exercise 1.1.18 (1)

```lean
theorem JordanMeasurable.outer_measure_of_closure {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E) :
  Jordan_outer_measure (closure E) = Jordan_outer_measure E
```

`JordanMeasurable.inner_measure_of_interior` (theorem, [line 1264](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1264)). An exercise, stated without proof.

> Exercise 1.1.18 (2)

```lean
theorem JordanMeasurable.inner_measure_of_interior {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E) :
  Jordan_inner_measure (interior E) = Jordan_inner_measure E
```

`JordanMeasurable.iff_boundary_null` (theorem, [line 1269](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1269)). An exercise, stated without proof.

> Exercise 1.1.18 (3)

```lean
theorem JordanMeasurable.iff_boundary_null {d:ℕ} {E: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E) :
  JordanMeasurable E ↔ JordanMeasurable.null (frontier E)
```

## Exercise 1.1.19

`JordanMeasurable.caratheodory` (theorem, [line 1297](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean#L1297)). An exercise, stated without proof.

> Exercise 1.1.19 (Caratheodory property)

```lean
theorem JordanMeasurable.caratheodory {d:ℕ} {E F: Set (EuclideanSpace' d)} (hE: Bornology.IsBounded E) (hF: IsElementary F) :
  Jordan_outer_measure E = Jordan_outer_measure (E ∩ F) + Jordan_outer_measure (E \ F)
```

## Depends on

- [Section 1.1.1: Elementary measure](section-1-1-1.md)

## Sources

- [Analysis/MeasureTheory/Section_1_1_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_1_2.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_1_2.html)
