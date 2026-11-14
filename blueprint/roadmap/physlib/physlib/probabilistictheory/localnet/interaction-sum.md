---
declaration: module
origin: cited
lean: ProbabilisticTheory.Interaction.norm_termIn_le, ProbabilisticTheory.Interaction.sumIn, ProbabilisticTheory.Interaction.norm_sumIn_le, ProbabilisticTheory.Interaction.sumIn_add, ProbabilisticTheory.Interaction.sumIn_smul, ProbabilisticTheory.Interaction.setIntegral_labelsIn, ProbabilisticTheory.Interaction.coupling, ProbabilisticTheory.Interaction.sumIn_split
statement: formalized
proof: formalized
---

# Integrating interactions over local regions

The module `Physlib.ProbabilisticTheory.LocalNet.Interaction.Sum`, [Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean): 12 declarations, 12 with a docstring.

> An interaction defines a local observable by integrating its terms over a region.

## i. Overview

> The integral of an interaction gives an observable in each region. The choice of measure allows
> both discrete sums and continuum integrals.
>
> For nested regions, the observable in the larger region decomposes into the observable of the
> smaller region and the remaining interaction terms. For two regions with disjoint sets of
> supported terms, the observable decomposes into their contributions and the terms supported
> in neither region.

## ii. Key results

> - `Interaction.sumIn`: The integral of interaction terms in a region.
> - `Interaction.norm_sumIn_le`: A norm bound for the integral.
> - `Interaction.sumIn_add`, `Interaction.sumIn_smul`: Linearity of integration.
> - `Interaction.sumIn_split`: Decomposition for nested regions.
> - `Interaction.sumIn_disjoint`: Decomposition for regions with disjoint sets of terms.
> - `Interaction.sumIn_count`, `Interaction.sumIn_count_tsum`: Discrete sums over finite or
>   countable labels.

## iv. References

**`ProbabilisticTheory.Interaction.norm_termIn_le`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L63).

> The norm of a term cannot increase when included into another region.

```lean
lemma norm_termIn_le (Λ : R) (i : ι) : ‖Φ.termIn Λ i‖ ≤ ‖Φ.term i‖
```

## A. Integration over a region

**`ProbabilisticTheory.Interaction.sumIn`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L73).

> The observable in `Λ` obtained by integrating the interaction terms supported there.

```lean
noncomputable def sumIn (Λ : R) : A Λ
```

**`ProbabilisticTheory.Interaction.norm_sumIn_le`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L76).

> The norm of the integral is bounded by the integral of the norms.

```lean
lemma norm_sumIn_le (Λ : R) : ‖Φ.sumIn μ Λ‖ ≤ ∫ i, ‖Φ.termIn Λ i‖ ∂μ
```

**`ProbabilisticTheory.Interaction.sumIn_add`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L80).

> Integration preserves addition of interaction terms with the same supports.

```lean
lemma sumIn_add (s : ι → R) (t t' : ∀ i, A (s i)) {Λ : R}
    (h : Integrable ((⟨s, t⟩ : Interaction N ι).termIn Λ) μ)
    (h' : Integrable ((⟨s, t'⟩ : Interaction N ι).termIn Λ) μ) :
    (⟨s, t + t'⟩ : Interaction N ι).sumIn μ Λ =
      (⟨s, t⟩ : Interaction N ι).sumIn μ Λ + (⟨s, t'⟩ : Interaction N ι).sumIn μ Λ
```

**`ProbabilisticTheory.Interaction.sumIn_smul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L89).

> Integration preserves scalar multiplication of interaction terms.

```lean
lemma sumIn_smul (s : ι → R) (c : ℝ) (t : ∀ i, A (s i)) (Λ : R) :
    (⟨s, c • t⟩ : Interaction N ι).sumIn μ Λ =
      c • (⟨s, t⟩ : Interaction N ι).sumIn μ Λ
```

**`ProbabilisticTheory.Interaction.setIntegral_labelsIn`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L101).

> Integrating the terms supported in `Λ` in a larger region `Λ'` agrees with including
> the integral over `Λ` into `Λ'`.

```lean
lemma setIntegral_labelsIn {Λ Λ' : R} (h : Λ ≤ Λ') (hS : MeasurableSet (Φ.labelsIn Λ))
    (h1 : Integrable (Φ.termIn Λ) μ) :
    ∫ i in Φ.labelsIn Λ, Φ.termIn Λ' i ∂μ = N.incl h (Φ.sumIn μ Λ)
```

## B. Nested regions

**`ProbabilisticTheory.Interaction.coupling`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L111).

> The contribution in `Λ'` from terms not supported in `Λ`.

```lean
noncomputable def coupling (Λ Λ' : R) : A Λ'
```

**`ProbabilisticTheory.Interaction.sumIn_split`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L116).

> The observable in a larger region is the included observable of the smaller region
> plus the remaining interaction terms.

```lean
lemma sumIn_split {Λ Λ' : R} (h : Λ ≤ Λ') (hS : MeasurableSet (Φ.labelsIn Λ))
    (h1 : Integrable (Φ.termIn Λ) μ) (h2 : Integrable (Φ.termIn Λ') μ) :
    Φ.sumIn μ Λ' = N.incl h (Φ.sumIn μ Λ) + Φ.coupling μ Λ Λ'
```

## C. Disjoint regions

**`ProbabilisticTheory.Interaction.crossingIn`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L125).

> The contribution in `Λ` from terms supported in neither `Λ₁` nor `Λ₂`.

```lean
noncomputable def crossingIn (Λ₁ Λ₂ Λ : R) : A Λ
```

**`ProbabilisticTheory.Interaction.sumIn_disjoint`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L130).

> For regions with disjoint sets of supported terms, the observable in a common larger
> region is the sum of their included observables and the remaining interaction terms.

```lean
lemma sumIn_disjoint {Λ₁ Λ₂ Λ : R} (h₁ : Λ₁ ≤ Λ) (h₂ : Λ₂ ≤ Λ)
    (hd : Disjoint (Φ.labelsIn Λ₁) (Φ.labelsIn Λ₂)) (m₁ : MeasurableSet (Φ.labelsIn Λ₁))
    (m₂ : MeasurableSet (Φ.labelsIn Λ₂)) (g₁ : Integrable (Φ.termIn Λ₁) μ)
    (g₂ : Integrable (Φ.termIn Λ₂) μ) (g : Integrable (Φ.termIn Λ) μ) :
    Φ.sumIn μ Λ = N.incl h₁ (Φ.sumIn μ Λ₁) + N.incl h₂ (Φ.sumIn μ Λ₂) +
      Φ.crossingIn μ Λ₁ Λ₂ Λ
```

## D. Discrete interactions

**`ProbabilisticTheory.Interaction.sumIn_count`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L146).

> With finitely many labels, integration against the counting measure is a finite sum.

```lean
lemma sumIn_count [Fintype ι] (Λ : R) :
    Φ.sumIn Measure.count Λ = ∑ i, Φ.termIn Λ i
```

**`ProbabilisticTheory.Interaction.sumIn_count_tsum`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean#L152).

> With countably many labels, integration against the counting measure is an infinite sum,
> provided the terms are integrable.

```lean
lemma sumIn_count_tsum [Countable ι] {Λ : R}
    (h : Integrable (Φ.termIn Λ) Measure.count) :
    Φ.sumIn Measure.count Λ = ∑' i, Φ.termIn Λ i
```

## Depends on

- [Interactions on a local net](interaction-basic.md)
- [Archimedean order-unit spaces](../orderunit/archimedean.md)

## Proof depends on

- [Channels are contractions](../channel/norm.md)

## Sources

- [Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/Interaction/Sum.lean)
