---
declaration: module
origin: cited
lean: ProbabilisticTheory.EffectValuedMeasure.meshBound, ProbabilisticTheory.EffectValuedMeasure.MeshIndex, ProbabilisticTheory.EffectValuedMeasure.meshWeight, ProbabilisticTheory.EffectValuedMeasure.meshPiece, ProbabilisticTheory.EffectValuedMeasure.mem_meshPiece_iff, ProbabilisticTheory.EffectValuedMeasure.measurableSet_meshPiece, ProbabilisticTheory.EffectValuedMeasure.meshIndexOf, ProbabilisticTheory.EffectValuedMeasure.meshIndexOf_coe
statement: formalized
proof: formalized
---

# Integrating bounded functions against an effect-valued measure

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.BoundedIntegral`, [PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean): 40 declarations, 31 with a docstring.

> The integral of bounded measurable functions against an effect-valued measure.

## i. Overview

> If the observables are complete for the order-unit norm, the integral of simple functions extends to
> bounded measurable functions. A bounded function is uniformly approximated by simple functions on a
> mesh of width `1 / (n + 1)`, and simple functions within `ε` and `ε'` of `f` have integrals within
> `ε + ε'`. So the integrals of the approximations converge, to a limit that does not depend on the
> approximation or the bound. The integral is linear and positive, and agrees with the simple integral
> on simple functions.

## ii. Key results

> - `EffectValuedMeasure.meshPiece`, `EffectValuedMeasure.meshWeight` : the mesh approximation.
> - `EffectValuedMeasure.orderUnitNorm_simpleIntegral_sub_le` : nearby simple functions have nearby
>   integrals.
> - `EffectValuedMeasure.integral` : the integral of a bounded measurable function.
> - `EffectValuedMeasure.tendsto_of_uniformly_approximating` : every uniform approximation gives the
>   integral.
> - `EffectValuedMeasure.integral_add`, `EffectValuedMeasure.nonneg_integral` : linearity and
>   positivity.

## iv. References

> * None.

## A. The mesh approximation of a bounded measurable function

**`ProbabilisticTheory.EffectValuedMeasure.meshBound`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L65).

> The number of width-`1/(n+1)` mesh cells it takes to reach out to `M` on either side of `0`:
> `⌈(n+1)*M⌉₊`. Only depends on `M` and `n`, not on any particular function.

```lean
noncomputable def meshBound (M : ℝ) (n : ℕ) : ℕ
```

**`ProbabilisticTheory.EffectValuedMeasure.MeshIndex`**, an abbrev, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L69).

> The mesh cell label set at scale `n` covering `[-M, M]`: integers from `-meshBound M n` to
> `meshBound M n`.

```lean
abbrev MeshIndex (M : ℝ) (n : ℕ) : Type
```

**`ProbabilisticTheory.EffectValuedMeasure.meshWeight`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L73).

> The weight of mesh cell `k` at scale `n`: `k/(n+1)`, the left endpoint of the cell.

```lean
noncomputable def meshWeight (M : ℝ) (n : ℕ) (k : MeshIndex M n) : ℝ
```

**`ProbabilisticTheory.EffectValuedMeasure.meshPiece`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L77).

> The mesh cell `k` at scale `n`, pulled back along `f`: the points where `f` rounds down to
> `k/(n+1)` at that scale, i.e. `⌊(n+1)*f(x)⌋ = k`.

```lean
noncomputable def meshPiece (f : Ω → ℝ) (M : ℝ) (n : ℕ) (k : MeshIndex M n) : Set Ω
```

**`ProbabilisticTheory.EffectValuedMeasure.mem_meshPiece_iff`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L84).

```lean
lemma mem_meshPiece_iff (n : ℕ) (k : MeshIndex M n) (x : Ω) :
    x ∈ meshPiece f M n k ↔ ⌊((n : ℝ) + 1) * f x⌋ = (k : ℤ)
```

**`ProbabilisticTheory.EffectValuedMeasure.measurableSet_meshPiece`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L90).

```lean
lemma measurableSet_meshPiece (n : ℕ) (k : MeshIndex M n) : MeasurableSet (meshPiece f M n k)
```

**`ProbabilisticTheory.EffectValuedMeasure.meshIndexOf`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L96).

> The label the mesh assigns to the point `x`, together with the proof that it lies in range:
> `⌊(n+1)*f(x)⌋` always lies in `[-meshBound M n, meshBound M n]` once `|f x| ≤ M`.

```lean
noncomputable def meshIndexOf (n : ℕ) (x : Ω) : MeshIndex M n
```

**`ProbabilisticTheory.EffectValuedMeasure.meshIndexOf_coe`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L122).

```lean
lemma meshIndexOf_coe (n : ℕ) (x : Ω) :
    ((meshIndexOf hM n x : MeshIndex M n) : ℤ) = ⌊((n : ℝ) + 1) * f x⌋
```

**`ProbabilisticTheory.EffectValuedMeasure.mem_meshPiece_meshIndexOf`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L127).

```lean
lemma mem_meshPiece_meshIndexOf (n : ℕ) (x : Ω) : x ∈ meshPiece f M n (meshIndexOf hM n x)
```

**`ProbabilisticTheory.EffectValuedMeasure.isPartition_meshPiece`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L131).

> The mesh pieces at scale `n` form a finite measurable partition of `Ω`.

```lean
lemma isPartition_meshPiece (n : ℕ) : IsPartition (meshPiece f M n)
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue_meshWeight_meshPiece`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L145).

> The value of the mesh simple function at `x` is the label `f` is assigned, over `(n+1)`.

```lean
lemma simpleValue_meshWeight_meshPiece (n : ℕ) (x : Ω) :
    simpleValue (meshWeight M n) (meshPiece f M n) x =
      (⌊((n : ℝ) + 1) * f x⌋ : ℝ) / ((n : ℝ) + 1)
```

**`ProbabilisticTheory.EffectValuedMeasure.abs_simpleValue_meshWeight_meshPiece_sub_le`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L155).

> **Uniform convergence of the mesh approximation.** At scale `n`, the mesh simple function
> never differs from `f` by more than the mesh width `1/(n+1)`, at any point.

```lean
lemma abs_simpleValue_meshWeight_meshPiece_sub_le (n : ℕ) (x : Ω) :
    |simpleValue (meshWeight M n) (meshPiece f M n) x - f x| ≤ 1 / ((n : ℝ) + 1)
```

## B. Linear operations on simple values

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue_add`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L179).

> `simpleValue` is additive in the weights, pointwise.

```lean
lemma simpleValue_add (a b : ι → ℝ) (s : ι → Set Ω) (x : Ω) :
    simpleValue (a + b) s x = simpleValue a s x + simpleValue b s x
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue_smul`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L187).

> `simpleValue` is homogeneous in the weights, pointwise.

```lean
lemma simpleValue_smul (r : ℝ) (c : ι → ℝ) (s : ι → Set Ω) (x : Ω) :
    simpleValue (r • c) s x = r * simpleValue c s x
```

## C. Comparing the simple integrals of two approximations

> The key ingredient for both the Cauchy property and the independence of the eventual integral
> from the choice of approximating sequence: if two simple functions (over possibly different
> partitions) both stay within `ε`, resp. `ε'`, of the same `f` everywhere, their integrals against
> `μ` stay within `ε + ε'` of each other, in the order-unit norm.

**`ProbabilisticTheory.EffectValuedMeasure.isPartition_inter`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L211).

> The pairwise intersections of two partitions again form a partition, indexed by the product of
> their labels.

```lean
lemma isPartition_inter {ι ι' : Type*} [Fintype ι] [Fintype ι'] {s : ι → Set Ω} {s' : ι' → Set Ω}
    (hs : IsPartition s) (hs' : IsPartition s') :
    IsPartition (fun p : ι × ι' => s p.1 ∩ s' p.2)
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue_eq_simpleValue_inter_fst`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L232).

```lean
lemma simpleValue_eq_simpleValue_inter_fst {ι ι' : Type*} [Fintype ι] [Fintype ι']
    {c : ι → ℝ} {s : ι → Set Ω} (hs : IsPartition s) {s' : ι' → Set Ω} (hs' : IsPartition s')
    (x : Ω) :
    simpleValue c s x = simpleValue (fun p : ι × ι' => c p.1) (fun p => s p.1 ∩ s' p.2) x
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue_eq_simpleValue_inter_snd`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L244).

```lean
lemma simpleValue_eq_simpleValue_inter_snd {ι ι' : Type*} [Fintype ι] [Fintype ι']
    {c' : ι' → ℝ} {s : ι → Set Ω} (hs : IsPartition s) {s' : ι' → Set Ω} (hs' : IsPartition s')
    (x : Ω) :
    simpleValue c' s' x = simpleValue (fun p : ι × ι' => c' p.2) (fun p => s p.1 ∩ s' p.2) x
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleValue_add_inter`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L259).

> The pointwise sum of two simple functions, over possibly different partitions, is the simple
> function of their common refinement with pointwise-summed weights. Used to build an admissible
> approximating sequence for `f + g` out of ones for `f` and `g`.

```lean
lemma simpleValue_add_inter {ι ι' : Type*} [Fintype ι] [Fintype ι'] {a : ι → ℝ} {s : ι → Set Ω}
    (hs : IsPartition s) {b : ι' → ℝ} {s' : ι' → Set Ω} (hs' : IsPartition s') (x : Ω) :
    simpleValue a s x + simpleValue b s' x =
      simpleValue (fun p : ι × ι' => a p.1 + b p.2) (fun p => s p.1 ∩ s' p.2) x
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_eq_simpleIntegral_inter_fst`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L267).

```lean
lemma simpleIntegral_eq_simpleIntegral_inter_fst {ι ι' : Type*} [Fintype ι] [Fintype ι']
    [DecidableEq ι] [DecidableEq ι'] (μ : EffectValuedMeasure Ω E) {c : ι → ℝ} {s : ι → Set Ω}
    (hs : IsPartition s) {s' : ι' → Set Ω} (hs' : IsPartition s') :
    simpleIntegral μ c s hs =
      simpleIntegral μ (fun p : ι × ι' => c p.1) (fun p => s p.1 ∩ s' p.2)
        (isPartition_inter hs hs')
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_eq_simpleIntegral_inter_snd`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L276).

```lean
lemma simpleIntegral_eq_simpleIntegral_inter_snd {ι ι' : Type*} [Fintype ι] [Fintype ι']
    [DecidableEq ι] [DecidableEq ι'] (μ : EffectValuedMeasure Ω E) {c' : ι' → ℝ} {s : ι → Set Ω}
    (hs : IsPartition s) {s' : ι' → Set Ω} (hs' : IsPartition s') :
    simpleIntegral μ c' s' hs' =
      simpleIntegral μ (fun p : ι × ι' => c' p.2) (fun p => s p.1 ∩ s' p.2)
        (isPartition_inter hs hs')
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_sub_simpleIntegral`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L288).

> The difference of two simple integrals, over possibly different partitions, is itself a simple
> integral over their common refinement, with weights the pointwise difference of the two original
> weights. This is what lets the difference be bounded termwise.

```lean
lemma simpleIntegral_sub_simpleIntegral {ι ι' : Type*} [Fintype ι] [Fintype ι'] [DecidableEq ι]
    [DecidableEq ι'] (μ : EffectValuedMeasure Ω E) {c : ι → ℝ} {s : ι → Set Ω}
    (hs : IsPartition s) {c' : ι' → ℝ} {s' : ι' → Set Ω} (hs' : IsPartition s') :
    simpleIntegral μ c s hs - simpleIntegral μ c' s' hs' =
      simpleIntegral μ (fun p : ι × ι' => c p.1 - c' p.2) (fun p => s p.1 ∩ s' p.2)
        (isPartition_inter hs hs')
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_add_simpleIntegral`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L305).

> The sum of two simple integrals, over possibly different partitions, is itself a simple
> integral over their common refinement, with weights the pointwise sum of the two original
> weights. Used to build an admissible approximating sequence for `f + g` out of ones for `f` and
> `g`.

```lean
lemma simpleIntegral_add_simpleIntegral {ι ι' : Type*} [Fintype ι] [Fintype ι'] [DecidableEq ι]
    [DecidableEq ι'] (μ : EffectValuedMeasure Ω E) {c : ι → ℝ} {s : ι → Set Ω}
    (hs : IsPartition s) {c' : ι' → ℝ} {s' : ι' → Set Ω} (hs' : IsPartition s') :
    simpleIntegral μ c s hs + simpleIntegral μ c' s' hs' =
      simpleIntegral μ (fun p : ι × ι' => c p.1 + c' p.2) (fun p => s p.1 ∩ s' p.2)
        (isPartition_inter hs hs')
```

**`ProbabilisticTheory.EffectValuedMeasure.sum_apply_eq_one`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L316).

> The total measure of a partition is the certain outcome.

```lean
lemma sum_apply_eq_one {ι : Type*} [Fintype ι] [DecidableEq ι] (μ : EffectValuedMeasure Ω E)
    {s : ι → Set Ω} (hs : IsPartition s) :
    ∑ i, (μ (s i) (hs.measurable i) : E) = 1
```

**`ProbabilisticTheory.EffectValuedMeasure.orderUnitNorm_simpleIntegral_le`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L326).

> A simple integral whose weights are bounded by `δ`, on every piece the underlying measure sees
> (i.e. every nonempty piece), has order-unit norm at most `δ`: every term is sandwiched between
> `±δ` times a nonnegative effect, and those effects sum to the certain outcome.

```lean
lemma orderUnitNorm_simpleIntegral_le {ι : Type*} [Fintype ι] [DecidableEq ι]
    (μ : EffectValuedMeasure Ω E) {c : ι → ℝ} {s : ι → Set Ω} (hs : IsPartition s) {δ : ℝ}
    (hδ : 0 ≤ δ) (hc : ∀ i, (s i).Nonempty → |c i| ≤ δ) :
    orderUnitNorm (simpleIntegral μ c s hs) ≤ δ
```

**`ProbabilisticTheory.EffectValuedMeasure.simpleIntegral_nonneg'`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L363).

> A simple integral is nonnegative as soon as its weights are nonnegative on every piece the
> underlying measure sees (i.e. every nonempty piece) — the same "only nonempty pieces matter"
> relaxation of `simpleIntegral_nonneg` used above for the norm bound.

```lean
lemma simpleIntegral_nonneg' {ι : Type*} [Fintype ι] (μ : EffectValuedMeasure Ω E) {c : ι → ℝ}
    {s : ι → Set Ω} (hs : IsPartition s) (hc : ∀ i, (s i).Nonempty → 0 ≤ c i) :
    0 ≤ simpleIntegral μ c s hs
```

**`ProbabilisticTheory.EffectValuedMeasure.orderUnitNorm_simpleIntegral_sub_le`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L378).

> **The key comparison lemma.** Two simple functions that both stay within `ε`, resp. `ε'`, of
> the same bounded function `f` everywhere give integrals against `μ` that are within `ε + ε'` of
> each other, in the order-unit norm — regardless of which partitions were used to build them.

```lean
lemma orderUnitNorm_simpleIntegral_sub_le {ι ι' : Type*} [Fintype ι] [Fintype ι']
    [DecidableEq ι] [DecidableEq ι'] (μ : EffectValuedMeasure Ω E) {f : Ω → ℝ}
    {c : ι → ℝ} {s : ι → Set Ω} (hs : IsPartition s) {ε : ℝ} (hε : 0 ≤ ε)
    (hc : ∀ x, |simpleValue c s x - f x| ≤ ε)
    {c' : ι' → ℝ} {s' : ι' → Set Ω} (hs' : IsPartition s') {ε' : ℝ} (hε' : 0 ≤ ε')
    (hc' : ∀ x, |simpleValue c' s' x - f x| ≤ ε') :
    orderUnitNorm (simpleIntegral μ c s hs - simpleIntegral μ c' s' hs') ≤ ε + ε'
```

**`ProbabilisticTheory.EffectValuedMeasure.le_smul_one_of_orderUnitNorm_lt`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L404).

> Any real strictly above the order-unit norm of `y` is itself an order-unit bound of `y`: since
> `orderUnitBounds y` is an up-set with infimum `orderUnitNorm y`, anything strictly past that
> infimum is already in the set. The positivity argument below needs this to turn a norm estimate
> into an actual order bound.

```lean
lemma le_smul_one_of_orderUnitNorm_lt {y : E} {r : ℝ} (h : orderUnitNorm y < r) :
    y ≤ r • (1 : E)
```

## D. The integral, via completeness

> The order-unit norm makes `E` a normed group, assumed complete. Most order-unit spaces are not
> complete.

**`ProbabilisticTheory.EffectValuedMeasure.instNormedAddCommGroup`**, an instance, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L425).

> The order-unit norm supplies the ambient normed additive-group structure for this section.

```lean
noncomputable local instance instNormedAddCommGroup : NormedAddCommGroup E
```

**`ProbabilisticTheory.EffectValuedMeasure.instCompleteSpace`**, an instance, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L432).

> Completeness of the order-unit-norm copy, read on `E` itself.

```lean
local instance instCompleteSpace : CompleteSpace E
```

**`ProbabilisticTheory.EffectValuedMeasure.dist_eq_orderUnitNorm`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L435).

```lean
lemma dist_eq_orderUnitNorm (x y : E) : dist x y = orderUnitNorm (x - y)
```

**`ProbabilisticTheory.EffectValuedMeasure.tendsto_const_smul_of_tendsto`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L442).

> Scalar multiplication by a fixed real is continuous, established by hand from
> `orderUnitNorm_smul_le` since no `NormedSpace ℝ E` instance is assumed at this generality.

```lean
lemma tendsto_const_smul_of_tendsto {a : ℕ → E} {L : E} (c : ℝ)
    (ha : Filter.Tendsto a atTop (𝓝 L)) : Filter.Tendsto (fun n => c • a n) atTop (𝓝 (c • L))
```

**`ProbabilisticTheory.EffectValuedMeasure.cauchySeq_meshSimpleIntegral`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L459).

> **The mesh approximation is Cauchy.** Refining the mesh from scale `n` to scale `m`, both past
> `N`, moves the simple integral by at most `2/(N+1)` in the order-unit norm — the sum of the two
> meshes' uniform error bounds, via `orderUnitNorm_simpleIntegral_sub_le`.

```lean
lemma cauchySeq_meshSimpleIntegral (μ : EffectValuedMeasure Ω E) :
    CauchySeq (fun n : ℕ => simpleIntegral μ (meshWeight M n) (meshPiece f M n)
      (isPartition_meshPiece hf hM n))
```

**`ProbabilisticTheory.EffectValuedMeasure.integral`**, a def, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L489).

> **The integral of a bounded measurable function against `μ`.** The limit of the mesh
> approximation's simple integrals, which exists by completeness of `E` since the sequence is
> Cauchy.

```lean
noncomputable def integral (μ : EffectValuedMeasure Ω E) : E
```

**`ProbabilisticTheory.EffectValuedMeasure.integral_tendsto`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L494).

> The mesh approximation's simple integrals converge to `integral hf hM μ`, by construction.

```lean
lemma integral_tendsto (μ : EffectValuedMeasure Ω E) :
    Tendsto (fun n : ℕ => simpleIntegral μ (meshWeight M n) (meshPiece f M n)
      (isPartition_meshPiece hf hM n)) atTop (𝓝 (integral hf hM μ))
```

**`ProbabilisticTheory.EffectValuedMeasure.tendsto_of_uniformly_approximating`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L502).

> **The integral does not depend on the approximation.** For every sequence of simple functions
> converging uniformly to `f`, their integrals converge to the integral of `f`.

```lean
lemma tendsto_of_uniformly_approximating (μ : EffectValuedMeasure Ω E) {ι : ℕ → Type*}
    [∀ n, Fintype (ι n)] [∀ n, DecidableEq (ι n)] {c : ∀ n, ι n → ℝ} {s : ∀ n, ι n → Set Ω}
    (hs : ∀ n, IsPartition (s n)) {ε : ℕ → ℝ} (hε0 : ∀ n, 0 ≤ ε n)
    (hεtendsto : Tendsto ε atTop (𝓝 0)) (happrox : ∀ n x, |simpleValue (c n) (s n) x - f x| ≤ ε n) :
    Tendsto (fun n => simpleIntegral μ (c n) (s n) (hs n)) atTop (𝓝 (integral hf hM μ))
```

**`ProbabilisticTheory.EffectValuedMeasure.integral_indep_of_bound`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L524).

> **Independence from the choice of bound.** `integral` doesn't depend on which valid bound `M`
> was used to build it: swapping in another bound `M'` only changes the *range* of mesh cells, not
> their width, so the `M'`-mesh sequence is itself uniformly approximating for the `M`-built
> `integral hf hM μ` too, and `tendsto_nhds_unique` identifies the two limits.

```lean
lemma integral_indep_of_bound {M' : ℝ} (hM' : ∀ x, |f x| ≤ M') (μ : EffectValuedMeasure Ω E) :
    integral hf hM μ = integral hf hM' μ
```

**`ProbabilisticTheory.EffectValuedMeasure.integral_eq_simpleIntegral`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L538).

> **Consistency with the simple case.** When `f` already *is* a simple function against some
> partition, `integral` agrees with `simpleIntegral` on it — the general construction extends the
> special case rather than computing something else. The constant sequence `(c, s, hs)` is itself
> (trivially) uniformly approximating, with error `0`, so `tendsto_of_uniformly_approximating`
> applies directly.

```lean
lemma integral_eq_simpleIntegral {ι : Type*} [Fintype ι] [DecidableEq ι] {c : ι → ℝ}
    {s : ι → Set Ω} (hs : IsPartition s) (hcs : ∀ x, simpleValue c s x = f x)
    (μ : EffectValuedMeasure Ω E) : integral hf hM μ = simpleIntegral μ c s hs
```

**`ProbabilisticTheory.EffectValuedMeasure.nonneg_integral`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L553).

> **Positivity.** A nonnegative `f` integrates to a nonnegative value: every mesh approximation
> of a nonnegative `f` has nonnegative weight on every piece it actually sees (a piece labelled `k`
> that meets `f`'s graph forces `k ≥ 0`, since `f ≥ 0` there), so every term of the mesh sequence is
> `≥ 0` (`simpleIntegral_nonneg'`); pass that bound to the limit using that
> `-integral hf hM μ ≤ ε • 1` for every `ε > 0`, which is exactly what
> `ArchimedeanOrderUnitSpace.le_zero_of_forall_pos_smul_one_le` needs to conclude `-integral ≤ 0`.

```lean
lemma nonneg_integral (hf0 : ∀ x, 0 ≤ f x) (μ : EffectValuedMeasure Ω E) :
    0 ≤ integral hf hM μ
```

**`ProbabilisticTheory.EffectValuedMeasure.integral_add`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L594).

> **Additivity.** `integral (f + g) = integral f + integral g`, built by combining the two
> canonical mesh sequences into one admissible sequence for `f + g` (pieces the pairwise
> intersections, weights the pointwise sums — `simpleValue_add_inter` for the uniform bound,
> `simpleIntegral_add_simpleIntegral` for the exact algebraic identity) and matching limits: the
> combined sequence tends to `integral hfg hMfg μ` by `tendsto_of_uniformly_approximating`, and its
> terms equal `mesh_f + mesh_g` exactly at every stage, so it also tends to
> `integral f + integral g` (continuity of `+`, free in any normed group).

```lean
lemma integral_add {g : Ω → ℝ} (hg : Measurable g) {M' : ℝ} (hM' : ∀ x, |g x| ≤ M')
    {hfg : Measurable (f + g)} {hMfg : ∀ x, |(f + g) x| ≤ M + M'} (μ : EffectValuedMeasure Ω E) :
    integral hfg hMfg μ = integral hf hM μ + integral hg hM' μ
```

**`ProbabilisticTheory.EffectValuedMeasure.integral_smul`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean#L646).

> **Homogeneity.** `integral (c • f) = c • integral f`, built from the canonical mesh sequence
> for `f` with weights rescaled by `c` (same partition, so `simpleIntegral_smul` gives the exact
> algebraic identity at every stage, no refinement needed); matching limits needs scalar
> multiplication's continuity, established from `orderUnitNorm_smul_le` since no `NormedSpace ℝ E`
> instance is assumed at this generality.

```lean
lemma integral_smul (c : ℝ) {hcf : Measurable (c • f)} {hMcf : ∀ x, |(c • f) x| ≤ |c| * M}
    (μ : EffectValuedMeasure Ω E) : integral hcf hMcf μ = c • integral hf hM μ
```

## Depends on

- [Integrating simple functions against an effect-valued measure](integral.md)
- [The canonical normed copy of an order-unit space](../orderunit/normed.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedIntegral.lean)
