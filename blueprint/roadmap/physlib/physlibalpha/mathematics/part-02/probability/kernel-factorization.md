---
declaration: module
origin: cited
lean: ProbabilityTheory.Kernel.FactorsThrough, ProbabilityTheory.Kernel.factorsThrough_refl, ProbabilityTheory.Kernel.factorsThrough_trans, ProbabilityTheory.Kernel.factorsThrough_apply, ProbabilityTheory.Kernel.const_factorsThrough, ProbabilityTheory.Kernel.MutuallyFactor, ProbabilityTheory.Kernel.mutuallyFactor_refl, ProbabilityTheory.Kernel.mutuallyFactor_symm
statement: formalized
proof: formalized
---

# Factorization of Markov kernels

The module `PhyslibAlpha.Mathematics.Probability.Kernel.Factorization`, [PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean): 25 declarations, 25 with a docstring.

> Factoring kernels through Markov kernels, almost everywhere variants, and common refinements.

## i. Overview

> A kernel `K : α → β` factors through a kernel `L : α → γ` when `K = κ ∘ₖ L` for some Markov kernel
> `κ : γ → β`. Factoring through is a preorder on kernels with a common source; the target spaces
> may differ. Relative to a measure `μ` on the source it suffices that the factorization holds at
> `μ`-almost every point, and on a countably generated target, kernels that agree almost everywhere
> on each measurable set agree almost everywhere. Two kernels have a common refinement when both
> factor through a third one.

## ii. Key results

> - `ProbabilityTheory.Kernel.FactorsThrough` : `K = κ ∘ₖ L` for a Markov kernel `κ`.
> - `ProbabilityTheory.Kernel.MutuallyFactor` : factoring in both directions.
> - `ProbabilityTheory.Kernel.FactorsThroughAE` : factoring at almost every point.
> - `ProbabilityTheory.Kernel.ae_eq_of_forall_ae_apply_eq` : on a countably generated target,
>   kernels that agree almost everywhere on each measurable set agree almost everywhere.
> - `ProbabilityTheory.Kernel.HaveCommonRefinement` : both kernels factor through a third one.

## iv. References

> * None.

## A. Factorization

**`ProbabilityTheory.Kernel.FactorsThrough`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L65).

> `K` factors through `L`: `K = κ ∘ₖ L` for a Markov kernel `κ`.

```lean
def FactorsThrough (K : Kernel α β) (L : Kernel α γ) : Prop
```

**`ProbabilityTheory.Kernel.factorsThrough_refl`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L69).

> Every kernel factors through itself.

```lean
lemma factorsThrough_refl (K : Kernel α β) : FactorsThrough K K
```

**`ProbabilityTheory.Kernel.factorsThrough_trans`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L73).

> Factoring through a kernel is transitive.

```lean
lemma factorsThrough_trans {K : Kernel α β} {L : Kernel α γ} {M : Kernel α δ}
    (hKL : FactorsThrough K L) (hLM : FactorsThrough L M) : FactorsThrough K M
```

**`ProbabilityTheory.Kernel.factorsThrough_apply`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L80).

> If `K` factors through `L`, each measure `K a` is the bind of `L a` with a Markov kernel.

```lean
lemma factorsThrough_apply {K : Kernel α β} {L : Kernel α γ}
    (h : FactorsThrough K L) (a : α) :
    ∃ κ : Kernel γ β, IsMarkovKernel κ ∧ K a = (L a).bind κ
```

**`ProbabilityTheory.Kernel.const_factorsThrough`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L87).

> A constant kernel with a probability measure factors through every Markov kernel.

```lean
lemma const_factorsThrough (K : Kernel α γ) [IsMarkovKernel K]
    (μ : MeasureTheory.Measure β) [MeasureTheory.IsProbabilityMeasure μ] :
    FactorsThrough (Kernel.const α μ) K
```

## B. Mutual factorization

**`ProbabilityTheory.Kernel.MutuallyFactor`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L95).

> Two kernels factor through each other.

```lean
def MutuallyFactor (K : Kernel α β) (L : Kernel α γ) : Prop
```

**`ProbabilityTheory.Kernel.mutuallyFactor_refl`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L99).

> Mutual factoring is reflexive.

```lean
lemma mutuallyFactor_refl (K : Kernel α β) : MutuallyFactor K K
```

**`ProbabilityTheory.Kernel.mutuallyFactor_symm`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L103).

> Mutual factoring is symmetric.

```lean
lemma mutuallyFactor_symm {K : Kernel α β} {L : Kernel α γ}
    (h : MutuallyFactor K L) : MutuallyFactor L K
```

**`ProbabilityTheory.Kernel.mutuallyFactor_trans`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L108).

> Mutual factoring is transitive.

```lean
lemma mutuallyFactor_trans {K : Kernel α β} {L : Kernel α γ} {M : Kernel α δ}
    (hKL : MutuallyFactor K L) (hLM : MutuallyFactor L M) : MutuallyFactor K M
```

## C. Factorization almost everywhere

**`ProbabilityTheory.Kernel.FactorsThroughAE`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L115).

> `K` factors through `L` at `μ`-almost every point: `K =ᵐ[μ] κ ∘ₖ L` for a Markov kernel `κ`.

```lean
def FactorsThroughAE (μ : Measure α) (K : Kernel α β) (L : Kernel α γ) : Prop
```

**`ProbabilityTheory.Kernel.FactorsThrough.factorsThroughAE`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L119).

> Factoring everywhere implies factoring almost everywhere, for every measure.

```lean
lemma FactorsThrough.factorsThroughAE (μ : Measure α) {K : Kernel α β} {L : Kernel α γ}
    (h : FactorsThrough K L) : FactorsThroughAE μ K L
```

**`ProbabilityTheory.Kernel.factorsThroughAE_refl`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L125).

> Every kernel factors through itself almost everywhere.

```lean
lemma factorsThroughAE_refl (μ : Measure α) (K : Kernel α β) : FactorsThroughAE μ K K
```

**`ProbabilityTheory.Kernel.factorsThroughAE_trans`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L129).

> Factoring almost everywhere is transitive.

```lean
lemma factorsThroughAE_trans (μ : Measure α) {K : Kernel α β} {L : Kernel α γ}
    {M : Kernel α δ} (hKL : FactorsThroughAE μ K L)
    (hLM : FactorsThroughAE μ L M) : FactorsThroughAE μ K M
```

## D. Mutual factorization almost everywhere

**`ProbabilityTheory.Kernel.MutuallyFactorAE`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L141).

> Two kernels factor through each other almost everywhere.

```lean
def MutuallyFactorAE (μ : Measure α) (K : Kernel α β) (L : Kernel α γ) : Prop
```

**`ProbabilityTheory.Kernel.mutuallyFactorAE_refl`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L145).

> Mutual factoring almost everywhere is reflexive.

```lean
lemma mutuallyFactorAE_refl (μ : Measure α) (K : Kernel α β) :
    MutuallyFactorAE μ K K
```

**`ProbabilityTheory.Kernel.mutuallyFactorAE_symm`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L150).

> Mutual factoring almost everywhere is symmetric.

```lean
lemma mutuallyFactorAE_symm (μ : Measure α) {K : Kernel α β} {L : Kernel α γ}
    (h : MutuallyFactorAE μ K L) : MutuallyFactorAE μ L K
```

**`ProbabilityTheory.Kernel.mutuallyFactorAE_trans`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L155).

> Mutual factoring almost everywhere is transitive.

```lean
lemma mutuallyFactorAE_trans (μ : Measure α) {K : Kernel α β} {L : Kernel α γ}
    {M : Kernel α δ} (hKL : MutuallyFactorAE μ K L)
    (hLM : MutuallyFactorAE μ L M) : MutuallyFactorAE μ K M
```

**`ProbabilityTheory.Kernel.mutuallyFactorAE_of_ae_eq`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L161).

> Kernels equal almost everywhere factor through each other almost everywhere.

```lean
lemma mutuallyFactorAE_of_ae_eq (μ : Measure α) {K L : Kernel α β} (h : K =ᵐ[μ] L) :
    MutuallyFactorAE μ K L
```

## E. Kernels equal almost everywhere

**`ProbabilityTheory.Kernel.ae_eq_of_forall_ae_apply_eq`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L173).

> On a countably generated outcome space, two finite kernels which, for each event, give it the
> same measure at almost every input, are equal at almost every input.

```lean
lemma ae_eq_of_forall_ae_apply_eq [MeasurableSpace.CountablyGenerated β] {μ : Measure α}
    {K L : Kernel α β} [IsFiniteKernel K]
    (h : ∀ s, MeasurableSet s → ∀ᵐ x ∂μ, K x s = L x s) : K =ᵐ[μ] L
```

## F. Common refinements

**`ProbabilityTheory.Kernel.HaveCommonRefinement`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L205).

> Two kernels have a common refinement: both factor through one kernel `G`.

```lean
def HaveCommonRefinement (K : Kernel α β) (L : Kernel α γ) : Prop
```

**`ProbabilityTheory.Kernel.haveCommonRefinement_refl`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L209).

> Every kernel is a common refinement of itself and itself.

```lean
lemma haveCommonRefinement_refl (K : Kernel α β) : HaveCommonRefinement K K
```

**`ProbabilityTheory.Kernel.haveCommonRefinement_symm`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L213).

> Having a common refinement is symmetric.

```lean
lemma haveCommonRefinement_symm {K : Kernel α β} {L : Kernel α γ}
    (h : HaveCommonRefinement K L) : HaveCommonRefinement L K
```

**`ProbabilityTheory.Kernel.HaveCommonRefinement.mono`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L219).

> A common refinement of `K` and `L` refines everything that factors through them.

```lean
lemma HaveCommonRefinement.mono {K : Kernel α β} {L : Kernel α γ}
    {K' : Kernel α δ} {L' : Kernel α ε} (h : HaveCommonRefinement K L)
    (hK : FactorsThrough K' K) (hL : FactorsThrough L' L) : HaveCommonRefinement K' L'
```

**`ProbabilityTheory.Kernel.haveCommonRefinement_of_factorsThrough_left`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L226).

> If `K` factors through `L`, then `L` is a common refinement of both.

```lean
lemma haveCommonRefinement_of_factorsThrough_left {K : Kernel α β} {L : Kernel α γ}
    (h : FactorsThrough K L) : HaveCommonRefinement K L
```

**`ProbabilityTheory.Kernel.haveCommonRefinement_of_factorsThrough_right`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean#L231).

> If `L` factors through `K`, then `K` is a common refinement of both.

```lean
lemma haveCommonRefinement_of_factorsThrough_right {K : Kernel α β} {L : Kernel α γ}
    (h : FactorsThrough L K) : HaveCommonRefinement K L
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Probability/Kernel/Factorization.lean)
