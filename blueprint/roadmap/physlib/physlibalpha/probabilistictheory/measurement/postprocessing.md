---
declaration: module
origin: cited
lean: ProbabilisticTheory.Measurement.IsPostprocessing, ProbabilisticTheory.Measurement.postprocessing_refl, ProbabilisticTheory.Measurement.postprocessing_trans, ProbabilisticTheory.Measurement.isPostprocessing_iff_kernel, ProbabilisticTheory.Measurement.PostprocessEquiv, ProbabilisticTheory.Measurement.postprocessEquiv_refl, ProbabilisticTheory.Measurement.postprocessEquiv_symm, ProbabilisticTheory.Measurement.postprocessEquiv_trans
statement: formalized
proof: formalized
---

# Post-processing of measurements

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Postprocessing`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean): 14 declarations, 10 with a docstring.

> Post-processing of measurements through Markov kernels, the information preorder, and Born laws.

## i. Overview

> A measurement `M` is a post-processing of a measurement `N` when `M` can be simulated by performing
> `N` and processing its outcome classically: `M = N ∘ K` for a normal channel `K` between the
> classical systems of outcomes. Thus `M ≤ₚ N` means that `N` is at least as informative as `M`.
> Normal classical channels are Markov kernels, so the processing is a random relabeling of the
> outcome; relabeling along a measurable map is the deterministic case. In every normal state, the
> Born law of `M` is the Born law of `N` composed with the kernel.

## ii. Key results

> - `Measurement.IsPostprocessing` : the information preorder on measurements.
> - `Measurement.isPostprocessing_iff_kernel` : post-processing through a Markov kernel.
> - `Measurement.mapOutcome` : deterministic relabeling of measurement outcomes.
> - `Measurement.IsPostprocessing.probabilityLaw_eq` : the Born law of a post-processing is the
>   Born law of the original measurement composed with a Markov kernel.

## iv. References

> * None.

## A. Post-processing

**`ProbabilisticTheory.Measurement.IsPostprocessing`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L62).

> `M` is a post-processing of `N`: `M = N ∘ K` for a normal channel `K` between the classical
> systems of outcomes.

```lean
def IsPostprocessing (M : Measurement Ω E) (N : Measurement Ω' E) : Prop
```

**`ProbabilisticTheory.Measurement.postprocessing_refl`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L70).

> Every measurement is a post-processing of itself.

```lean
lemma postprocessing_refl (M : Measurement Ω E) : M ≤ₚ M
```

**`ProbabilisticTheory.Measurement.postprocessing_trans`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L74).

> Post-processing is transitive.

```lean
lemma postprocessing_trans {M : Measurement Ω E} {N : Measurement Ω' E}
    {P : Measurement Ω'' E} (hMN : M ≤ₚ N) (hNP : N ≤ₚ P) : M ≤ₚ P
```

**`ProbabilisticTheory.Measurement.isPostprocessing_iff_kernel`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L81).

> Post-processing is post-processing through a Markov kernel.

```lean
lemma isPostprocessing_iff_kernel {M : Measurement Ω E} {N : Measurement Ω' E} :
    M ≤ₚ N ↔ ∃ (κ : Kernel Ω' Ω) (_ : IsMarkovKernel κ),
      M.toChannel = N.toChannel.comp (ofKernel κ)
```

**`ProbabilisticTheory.Measurement.PostprocessEquiv`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L88).

> Two measurements are post-processing equivalent when each is a post-processing of the other.

```lean
def PostprocessEquiv (M : Measurement Ω E) (N : Measurement Ω' E) : Prop
```

**`ProbabilisticTheory.Measurement.postprocessEquiv_refl`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L91).

```lean
lemma postprocessEquiv_refl (M : Measurement Ω E) : PostprocessEquiv M M
```

**`ProbabilisticTheory.Measurement.postprocessEquiv_symm`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L94).

```lean
lemma postprocessEquiv_symm {M : Measurement Ω E} {N : Measurement Ω' E}
    (h : PostprocessEquiv M N) : PostprocessEquiv N M
```

**`ProbabilisticTheory.Measurement.postprocessEquiv_trans`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L98).

```lean
lemma postprocessEquiv_trans {M : Measurement Ω E} {N : Measurement Ω' E}
    {P : Measurement Ω'' E} (hMN : PostprocessEquiv M N) (hNP : PostprocessEquiv N P) :
    PostprocessEquiv M P
```

## B. Relabeling outcomes

**`ProbabilisticTheory.Measurement.mapOutcome`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L106).

> Relabel the outcomes of a measurement along a measurable map.

```lean
def mapOutcome (N : Measurement Ω' E) (f : Ω' → Ω) (hf : Measurable f) : Measurement Ω E
```

**`ProbabilisticTheory.Measurement.coe_mapOutcome_apply`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L111).

```lean
lemma coe_mapOutcome_apply (N : Measurement Ω' E) (f : Ω' → Ω) (hf : Measurable f)
    (s : Set Ω) (hs : MeasurableSet s) : (N.mapOutcome f hf s hs : E) = N (f ⁻¹' s) (hf hs)
```

**`ProbabilisticTheory.Measurement.mapOutcome_isPostprocessing`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L116).

> Measurable relabeling is deterministic post-processing.

```lean
lemma mapOutcome_isPostprocessing (N : Measurement Ω' E) (f : Ω' → Ω) (hf : Measurable f) :
    N.mapOutcome f hf ≤ₚ N
```

## C. Born laws

**`ProbabilisticTheory.Measurement.probabilityLaw_comp`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L124).

> The Born law of a post-processing through `K` is the Born law of the original measurement
> composed with the kernel of `K`.

```lean
lemma probabilityLaw_comp {M : Measurement Ω E} {N : Measurement Ω' E}
    {K : Channel (BoundedMeasurable Ω) (BoundedMeasurable Ω')} (hK : K.IsNormal)
    (h : M.toChannel = N.toChannel.comp K) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) :
    (M.probabilityLaw ω hω : Measure Ω) = toKernel K hK ∘ₘ N.probabilityLaw ω hω
```

**`ProbabilisticTheory.Measurement.IsPostprocessing.probabilityLaw_eq`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L136).

> The Born law of a post-processing is the Born law of the original measurement composed with a
> Markov kernel, the same for every state.

```lean
lemma IsPostprocessing.probabilityLaw_eq {M : Measurement Ω E} {N : Measurement Ω' E}
    (h : M ≤ₚ N) : ∃ (κ : Kernel Ω' Ω) (_ : IsMarkovKernel κ), ∀ (ω : 𝓢[ℝ, E])
      (hω : ω.IsNormal), (M.probabilityLaw ω hω : Measure Ω) = κ ∘ₘ N.probabilityLaw ω hω
```

**`ProbabilisticTheory.Measurement.probabilityLaw_mapOutcome`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean#L143).

> Relabeling outcomes pushes each Born law forward along the relabeling map.

```lean
lemma probabilityLaw_mapOutcome (N : Measurement Ω' E) (f : Ω' → Ω) (hf : Measurable f)
    (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) :
    (N.mapOutcome f hf).probabilityLaw ω hω = (N.probabilityLaw ω hω).map f
```

## Depends on

- [Classical channels](../classical/channel.md)
- [Measurements](basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Postprocessing.lean)
