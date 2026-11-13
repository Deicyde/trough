---
declaration: module
origin: cited
lean: boundedMeasurableSubmodule, BoundedMeasurable, BoundedMeasurable.ext, BoundedMeasurable.measurable, BoundedMeasurable.exists_bound, BoundedMeasurable.mk, BoundedMeasurable.mk_apply, BoundedMeasurable.zero_apply
statement: formalized
proof: formalized
---

# Bounded measurable functions

The module `PhyslibAlpha.Mathematics.MeasureTheory.BoundedMeasurable`, [PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean): 43 declarations (11 instances with no name), 10 with a docstring.

> The vector lattice of bounded measurable functions, staircase approximation and integrability.

## i. Overview

> The bounded measurable functions on a space `Ω` are the observables of a classical system with
> outcomes in `Ω`. They form a vector lattice under the pointwise operations. The least upper bound of
> a sequence bounded above is its pointwise supremum. Every bounded measurable function is uniformly
> approximated from below by a staircase, a finite combination of indicator functions, and it is
> integrable against every finite measure.

## ii. Key results

> - `BoundedMeasurable Ω` is the space of bounded measurable real functions on `Ω`.
> - `BoundedMeasurable.isLUB_range_iff` proves that least upper bounds of sequences are pointwise.
> - `BoundedMeasurable.abs_sub_staircase_le` proves that the staircase approximation is uniform.

## iv. References

> * None.

## A. The vector space

**`boundedMeasurableSubmodule`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L57).

> The bounded measurable real functions on `Ω`, as a subspace of all real functions.

```lean
def boundedMeasurableSubmodule : Submodule ℝ (Ω → ℝ)
```

**`BoundedMeasurable`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L68).

> The bounded measurable real functions on `Ω`.

```lean
def BoundedMeasurable : Type _
```

**An instance with no name**, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L72).

```lean
instance : AddCommGroup (BoundedMeasurable Ω)
```

**An instance with no name**, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L75).

```lean
instance : Module ℝ (BoundedMeasurable Ω)
```

**An instance with no name**, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L78).

```lean
instance : FunLike (BoundedMeasurable Ω) Ω ℝ
```

**`BoundedMeasurable.ext`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L82).

```lean
lemma ext {f g : BoundedMeasurable Ω} (h : ∀ x, f x = g x) : f = g
```

**`BoundedMeasurable.measurable`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L84).

```lean
lemma measurable (f : BoundedMeasurable Ω) : Measurable f
```

**`BoundedMeasurable.exists_bound`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L86).

```lean
lemma exists_bound (f : BoundedMeasurable Ω) : ∃ C, ∀ x, |f x| ≤ C
```

**`BoundedMeasurable.mk`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L90).

> A bounded measurable function.

```lean
def mk (f : Ω → ℝ) (hf : Measurable f) (hb : ∃ C, ∀ x, |f x| ≤ C) : BoundedMeasurable Ω
```

**`BoundedMeasurable.mk_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L93).

```lean
lemma mk_apply (f : Ω → ℝ) (hf) (hb) (x : Ω) : mk f hf hb x = f x
```

**`BoundedMeasurable.zero_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L94).

```lean
lemma zero_apply (x : Ω) : (0 : BoundedMeasurable Ω) x = 0
```

**`BoundedMeasurable.add_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L95).

```lean
lemma add_apply (f g : BoundedMeasurable Ω) (x : Ω) : (f + g) x = f x + g x
```

**`BoundedMeasurable.neg_apply`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L96).

```lean
lemma neg_apply (f : BoundedMeasurable Ω) (x : Ω) : (-f) x = -f x
```

**`BoundedMeasurable.sub_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L97).

```lean
lemma sub_apply (f g : BoundedMeasurable Ω) (x : Ω) : (f - g) x = f x - g x
```

**`BoundedMeasurable.smul_apply`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L98).

```lean
lemma smul_apply (c : ℝ) (f : BoundedMeasurable Ω) (x : Ω) : (c • f) x = c * f x
```

**`BoundedMeasurable.nsmul_apply`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L100).

```lean
lemma nsmul_apply (n : ℕ) (f : BoundedMeasurable Ω) (x : Ω) : (n • f) x = n * f x
```

**`BoundedMeasurable.sum_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L103).

```lean
lemma sum_apply {ι : Type*} (t : Finset ι) (f : ι → BoundedMeasurable Ω) (x : Ω) :
    (∑ i ∈ t, f i) x = ∑ i ∈ t, f i x
```

**An instance with no name**, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L108).

```lean
instance : One (BoundedMeasurable Ω)
```

**`BoundedMeasurable.one_apply`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L110).

```lean
lemma one_apply (x : Ω) : (1 : BoundedMeasurable Ω) x = 1
```

## B. The lattice order

**An instance with no name**, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L118).

```lean
instance : LE (BoundedMeasurable Ω)
```

**An instance with no name**, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L119).

```lean
instance : LT (BoundedMeasurable Ω)
```

**An instance with no name**, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L121).

```lean
instance : Max (BoundedMeasurable Ω)
```

**An instance with no name**, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L127).

```lean
instance : Min (BoundedMeasurable Ω)
```

**An instance with no name**, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L133).

```lean
instance : Lattice (BoundedMeasurable Ω)
```

**`BoundedMeasurable.le_def`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L136).

```lean
lemma le_def {f g : BoundedMeasurable Ω} : f ≤ g ↔ ∀ x, f x ≤ g x
```

**`BoundedMeasurable.sup_apply`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L138).

```lean
lemma sup_apply (f g : BoundedMeasurable Ω) (x : Ω) : (f ⊔ g) x = max (f x) (g x)
```

**`BoundedMeasurable.inf_apply`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L139).

```lean
lemma inf_apply (f g : BoundedMeasurable Ω) (x : Ω) : (f ⊓ g) x = min (f x) (g x)
```

**`BoundedMeasurable.posPart_apply`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L141).

```lean
lemma posPart_apply (f : BoundedMeasurable Ω) (x : Ω) : f⁺ x = max (f x) 0
```

**`BoundedMeasurable.negPart_apply`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L142).

```lean
lemma negPart_apply (f : BoundedMeasurable Ω) (x : Ω) : f⁻ x = max (-f x) 0
```

**An instance with no name**, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L144).

```lean
instance : IsOrderedAddMonoid (BoundedMeasurable Ω)
```

**An instance with no name**, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L147).

```lean
instance : PosSMulMono ℝ (BoundedMeasurable Ω)
```

## C. Least upper bounds of sequences

**`BoundedMeasurable.iSup'`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L158).

> The pointwise supremum of a sequence bounded above by `g`.

```lean
noncomputable def iSup' (f : ℕ → BoundedMeasurable Ω) (g : BoundedMeasurable Ω)
    (hfg : ∀ n, f n ≤ g) : BoundedMeasurable Ω
```

**`BoundedMeasurable.isLUB_range_iff`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L173).

> A sequence has least upper bound `g` exactly when `g` is its pointwise supremum.

```lean
lemma isLUB_range_iff {f : ℕ → BoundedMeasurable Ω} {g : BoundedMeasurable Ω} :
    IsLUB (range f) g ↔ ∀ x, IsLUB (range fun n => f n x) (g x)
```

## D. Indicators and staircases

**`BoundedMeasurable.indicator`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L193).

> The indicator function of a measurable set.

```lean
noncomputable def indicator (s : Set Ω) (hs : MeasurableSet s) : BoundedMeasurable Ω
```

**`BoundedMeasurable.indicator_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L197).

```lean
lemma indicator_apply (s : Set Ω) (hs : MeasurableSet s) (x : Ω) :
    indicator s hs x = s.indicator 1 x
```

**`BoundedMeasurable.indicator_nonneg`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L200).

```lean
lemma indicator_nonneg (s : Set Ω) (hs : MeasurableSet s) : 0 ≤ indicator s hs
```

**`BoundedMeasurable.indicator_le_one`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L203).

```lean
lemma indicator_le_one (s : Set Ω) (hs : MeasurableSet s) : indicator s hs ≤ 1
```

**`BoundedMeasurable.hasSum_indicator_apply`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L208).

> The indicators of disjoint sets sum to the indicator of their union.

```lean
lemma hasSum_indicator_apply {s : ℕ → Set Ω} (hd : Pairwise (Function.onFun Disjoint s)) (x : Ω) :
    HasSum (fun n => (s n).indicator (1 : Ω → ℝ) x) ((⋃ n, s n).indicator 1 x)
```

**`BoundedMeasurable.isLUB_sum_indicator`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L222).

> The indicators of disjoint measurable sets have the indicator of their union as least upper
> bound of their partial sums.

```lean
lemma isLUB_sum_indicator {s : ℕ → Set Ω} (hs : ∀ n, MeasurableSet (s n))
    (hd : Pairwise (Function.onFun Disjoint s)) :
    IsLUB (range fun N => ∑ n ∈ Finset.range N, indicator (s n) (hs n))
      (indicator (⋃ n, s n) (.iUnion hs))
```

**`BoundedMeasurable.staircase`**, a def, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L234).

> The staircase `⌊N g⌋ / N` below a nonnegative function `g ≤ K`, as a combination of
> indicators of superlevel sets.

```lean
noncomputable def staircase (g : BoundedMeasurable Ω) (N K : ℕ) : BoundedMeasurable Ω
```

**`BoundedMeasurable.staircase_apply`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L238).

```lean
lemma staircase_apply {g : BoundedMeasurable Ω} {N K : ℕ} (hN : 0 < N) {x : Ω} (h0 : 0 ≤ g x)
    (hK : g x ≤ K) : staircase g N K x = ⌊N * g x⌋₊ / N
```

**`BoundedMeasurable.abs_sub_staircase_le`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L256).

> The staircase approximates a nonnegative bounded measurable function uniformly.

```lean
lemma abs_sub_staircase_le {g : BoundedMeasurable Ω} {N K : ℕ} (hN : 0 < N) (h0 : 0 ≤ g)
    (hK : ∀ x, g x ≤ K) (x : Ω) : |(g - staircase g N K) x| ≤ (N : ℝ)⁻¹
```

## E. Integrability

**`BoundedMeasurable.integrable`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean#L275).

```lean
lemma integrable (f : BoundedMeasurable Ω) (μ : Measure Ω) [IsFiniteMeasure μ] :
    Integrable f μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/BoundedMeasurable.lean)
