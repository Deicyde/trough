---
declaration: module
origin: cited
lean: Choquet.choquetMetric, Choquet.cdist, Choquet.cdist_pos, Choquet.continuous_cdist, Choquet.ne_of_one_div_le_cdist, Choquet.isCompact_decompositionSet, Choquet.decompositionSpace, Choquet.continuous_fst_decomposition
statement: formalized
proof: formalized
---

# Every point is a mixture of extreme points

The module `PhyslibAlpha.Mathematics.Convex.Choquet.ExtremePointDecomposition`, [PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean): 31 declarations (1 instance with no name), 18 with a docstring.

> Choquet's theorem: each point of a metrizable compact convex set is a mixture of extreme points.

## i. Overview

> Let `S` be a compact convex set that is metrizable and whose points are separated by countably many
> continuous linear functionals. Every point of `S` is a mixture of extreme points: it has a
> representing probability measure that lives on the extreme points. This is Choquet's theorem. For
> states it says that every state is a mixture of pure states.
>
> The measure is any maximal representing measure in the Choquet order. Suppose it gave positive
> weight to the points that are not extreme. Each of them is the midpoint of two different points.
> Moving the weight from the midpoints out to these endpoints would give a strictly higher measure. To
> make this precise, the midpoints are grouped by the distance of their endpoints, and each group is a
> closed set.

## ii. Key results

> - `Choquet.measurableSet_extremePoints` proves that the extreme points form a Borel set.
> - `Choquet.maximal_ae_mem_extremePoints` proves that maximal representing measures live on the
>   extreme points.
> - `Choquet.exists_extreme_representingMeasure` proves Choquet's theorem.

## iv. References

> * None.

## A. The extreme points are Borel

**`Choquet.choquetMetric`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L66).

> A metric inducing the topology of `S`.

```lean
noncomputable def choquetMetric : MetricSpace S
```

**`Choquet.cdist`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L69).

> The distance of `choquetMetric`.

```lean
noncomputable def cdist (x y : S) : ℝ
```

**`Choquet.cdist_pos`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L72).

```lean
lemma cdist_pos {x y : S} (h : x ≠ y) : 0 < cdist x y
```

**`Choquet.continuous_cdist`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L75).

```lean
lemma continuous_cdist : Continuous (fun p : S × S => cdist p.1 p.2)
```

**`Choquet.ne_of_one_div_le_cdist`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L78).

```lean
lemma ne_of_one_div_le_cdist {n : ℕ} {x y : S} (h : 1 / (n + 1 : ℝ) ≤ cdist x y) : x ≠ y
```

**`Choquet.isCompact_decompositionSet`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L83).

```lean
lemma isCompact_decompositionSet [CompactSpace S] (n : ℕ) :
    IsCompact {p : S × S | 1 / (n + 1 : ℝ) ≤ cdist p.1 p.2}
```

**`Choquet.decompositionSpace`**, an abbrev, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L88).

> The pairs of points at distance at least `1 / (n + 1)`.

```lean
noncomputable abbrev decompositionSpace (n : ℕ)
```

**An instance with no name**, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L90).

```lean
instance [CompactSpace S] (n : ℕ) : CompactSpace (decompositionSpace (S := S) n)
```

**`Choquet.continuous_fst_decomposition`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L93).

```lean
lemma continuous_fst_decomposition (n : ℕ) :
    Continuous fun p : decompositionSpace (S := S) n => p.1.1
```

**`Choquet.continuous_snd_decomposition`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L97).

```lean
lemma continuous_snd_decomposition (n : ℕ) :
    Continuous fun p : decompositionSpace (S := S) n => p.1.2
```

**`Choquet.nontrivialMixSet`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L108).

> The midpoints of pairs of points at distance at least `1 / (n + 1)`.

```lean
noncomputable def nontrivialMixSet (n : ℕ) : Set S
```

**`Choquet.isClosed_nontrivialMixSet`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L112).

```lean
lemma isClosed_nontrivialMixSet (n : ℕ) : IsClosed (nontrivialMixSet hS n)
```

**`Choquet.setOf_notMem_extremePoints_eq`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L118).

> The non-extreme points are the union of the sets `nontrivialMixSet n`.

```lean
lemma setOf_notMem_extremePoints_eq :
    {x : S | (x : V) ∉ S.extremePoints ℝ} = ⋃ n, nontrivialMixSet hS n
```

**`Choquet.measurableSet_extremePoints`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L132).

> The extreme points form a Borel set.

```lean
lemma measurableSet_extremePoints : MeasurableSet {x : S | (x : V) ∈ S.extremePoints ℝ}
```

## B. Splitting mass between endpoints

**`Choquet.decompositionMidpoint`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L143).

> The midpoint of a pair in `decompositionSpace (S := S) n`.

```lean
noncomputable def decompositionMidpoint (n : ℕ) (p : decompositionSpace (S := S) n) : S
```

**`Choquet.continuous_decompositionMidpoint`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L147).

```lean
lemma continuous_decompositionMidpoint (n : ℕ) : Continuous (decompositionMidpoint hS n)
```

**`Choquet.exists_decomposition_lift`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L152).

> The conditional law on `nontrivialMixSet n` is the pushforward of a law on
> `decompositionSpace (S := S) n` under the midpoint map.

```lean
lemma exists_decomposition_lift (mu : ProbabilityMeasure S) (n : ℕ)
    (hpos : (mu : Measure S) (nontrivialMixSet hS n) ≠ 0) :
    ∃ rho : ProbabilityMeasure (decompositionSpace (S := S) n),
      rho.map (decompositionMidpoint hS n) =
        ProbabilityMeasure.condition mu (nontrivialMixSet hS n) hpos
```

**`Choquet.integrable_comp_decomposition`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L170).

```lean
lemma integrable_comp_decomposition {n : ℕ}
    (rho : ProbabilityMeasure (decompositionSpace (S := S) n)) (f : C(S, ℝ))
    {g : decompositionSpace (S := S) n → S} (hg : Continuous g) :
    Integrable (fun p => f (g p)) (rho : Measure _)
```

**`Choquet.integral_eq_integral_decompositionMidpoint`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L177).

```lean
lemma integral_eq_integral_decompositionMidpoint {n : ℕ}
    {rho : ProbabilityMeasure (decompositionSpace (S := S) n)} {nu : ProbabilityMeasure S}
    (h : rho.map (decompositionMidpoint hS n) = nu) (f : C(S, ℝ)) :
    ∫ w, f w ∂(nu : Measure S) = ∫ p, f (decompositionMidpoint hS n p) ∂(rho : Measure _)
```

**`Choquet.endpointMeasure`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L186).

> The law on `S` putting half the mass of `rho` on first points and half on second points.

```lean
noncomputable def endpointMeasure (n : ℕ)
    (rho : ProbabilityMeasure (decompositionSpace (S := S) n)) : ProbabilityMeasure S
```

**`Choquet.integral_endpointMeasure`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L193).

```lean
lemma integral_endpointMeasure (n : ℕ)
    (rho : ProbabilityMeasure (decompositionSpace (S := S) n)) (f : C(S, ℝ)) :
    ∫ w, f w ∂(endpointMeasure n rho : Measure _) =
      ∫ p : decompositionSpace (S := S) n, (1 / 2 * f p.1.1 + 1 / 2 * f p.1.2)
        ∂(rho : Measure _)
```

**`Choquet.condition_choquetLE_endpointMeasure`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L208).

> The conditional law on `nontrivialMixSet n` lies below the endpoint law in the Choquet
> order.

```lean
lemma condition_choquetLE_endpointMeasure (mu : ProbabilityMeasure S) (n : ℕ)
    (hpos : (mu : Measure S) (nontrivialMixSet hS n) ≠ 0)
    (rho : ProbabilityMeasure (decompositionSpace (S := S) n))
    (hrho : rho.map (decompositionMidpoint hS n) =
      ProbabilityMeasure.condition mu (nontrivialMixSet hS n) hpos) :
    ChoquetLE hS (ProbabilityMeasure.condition mu (nontrivialMixSet hS n) hpos)
      (endpointMeasure n rho)
```

**`Choquet.choquetLE_replacePart`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L227).

> Replacing the mass on `T` by a law above the conditional law on `T` moves up the Choquet
> order.

```lean
lemma choquetLE_replacePart (mu eta : ProbabilityMeasure S) (T : Set S) (hT : MeasurableSet T)
    (hpos : (mu : Measure S) T ≠ 0)
    (hle : ChoquetLE hS (ProbabilityMeasure.condition mu T hpos) eta) :
    ChoquetLE hS mu (ProbabilityMeasure.replacePart mu eta T hT)
```

**`Choquet.integral_lt_replacePart`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L241).

> Replacing the mass on `T` by a law with strictly larger integral than the conditional law on
> `T` strictly raises the integral.

```lean
lemma integral_lt_replacePart (mu eta : ProbabilityMeasure S) (T : Set S) (hT : MeasurableSet T)
    (hpos : (mu : Measure S) T ≠ 0) (f : C(S, ℝ))
    (hlt : ∫ w, f w ∂(ProbabilityMeasure.condition mu T hpos : Measure S) <
      ∫ w, f w ∂(eta : Measure S)) :
    ∫ w, f w ∂(mu : Measure S) <
      ∫ w, f w ∂(ProbabilityMeasure.replacePart mu eta T hT : Measure S)
```

**`Choquet.squaredEvaluation`**, a def, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L255).

> The square of a continuous linear functional, on `S`.

```lean
noncomputable def squaredEvaluation (ℓ : V →L[ℝ] ℝ) : C(S, ℝ)
```

**`Choquet.isConvexFunction_squaredEvaluation`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L260).

```lean
lemma isConvexFunction_squaredEvaluation (ℓ : V →L[ℝ] ℝ) :
    IsConvexFunction hS (squaredEvaluation ℓ)
```

**`Choquet.exists_index_positive_separation`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L273).

> Some functional of the sequence tells the two points of a pair apart with positive
> probability.

```lean
lemma exists_index_positive_separation (n : ℕ)
    (rho : ProbabilityMeasure (decompositionSpace (S := S) n)) :
    ∃ i, (rho : Measure _) {p : decompositionSpace (S := S) n | ℓ i p.1.1 ≠ ℓ i p.1.2} ≠ 0
```

**`Choquet.exists_squaredEvaluation_strict`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L287).

> Splitting the mass of `rho` between endpoints strictly raises the integral of some squared
> functional of the sequence.

```lean
lemma exists_squaredEvaluation_strict (n : ℕ)
    (rho : ProbabilityMeasure (decompositionSpace (S := S) n)) :
    ∃ i, ∫ p, squaredEvaluation (S := S) (ℓ i) (decompositionMidpoint hS n p) ∂(rho : Measure _) <
      ∫ w, squaredEvaluation (S := S) (ℓ i) w ∂(endpointMeasure n rho : Measure _)
```

## C. The boundary theorem

**`Choquet.maximal_nontrivialMixSet_null`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L324).

> A Choquet-maximal measure gives `nontrivialMixSet n` no mass.

```lean
lemma maximal_nontrivialMixSet_null {x : S} {mu : ProbabilityMeasure S}
    (hmu : IsChoquetMaximalAt hS x mu) (n : ℕ) :
    (mu : Measure S) (nontrivialMixSet hS n) = 0
```

**`Choquet.maximal_ae_mem_extremePoints`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L338).

> A Choquet-maximal measure is concentrated on the extreme points.

```lean
lemma maximal_ae_mem_extremePoints {x : S} {mu : ProbabilityMeasure S}
    (hmu : IsChoquetMaximalAt hS x mu) :
    ∀ᵐ y : S ∂(mu : Measure S), (y : V) ∈ S.extremePoints ℝ
```

**`Choquet.exists_extreme_representingMeasure`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean#L347).

> **The Choquet boundary theorem.** Every point has a representing probability measure
> concentrated on the extreme points.

```lean
lemma exists_extreme_representingMeasure (x : S) :
    ∃ mu : ProbabilityMeasure S,
      IsRepresentingMeasure x mu ∧ ∀ᵐ y : S ∂(mu : Measure S), (y : V) ∈ S.extremePoints ℝ
```

## Depends on

- [Representing measures and the Choquet order](choquet-representingmeasure.md)
- [Lifting, averaging and conditioning probability measures](../../part-02/measuretheory/liftingandconditioning.md)

## Sources

- [PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/Choquet/ExtremePointDecomposition.lean)
