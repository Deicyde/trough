---
declaration: module
origin: cited
lean: BoundedMeasurable.comap, BoundedMeasurable.comap_apply, BoundedMeasurable.isNormal_comap, BoundedMeasurable.kernelAverage, BoundedMeasurable.kernelAverage_apply, BoundedMeasurable.ofKernel, BoundedMeasurable.ofKernel_apply, BoundedMeasurable.isNormal_ofKernel
statement: formalized
proof: formalized
---

# Classical channels

The module `PhyslibAlpha.ProbabilisticTheory.Classical.Channel`, [PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean): 16 declarations (1 instance with no name), 6 with a docstring.

> Normal channels between classical systems of observables are exactly Markov kernels.

## i. Overview

> A channel between two classical systems sends observables of the target system `Ω` to observables
> of the source system `Ω'`. At each outcome `x` of `Ω'` it gives a normal state of `Ω` when it is
> normal, that is a probability distribution over `Ω`. So a normal classical channel is exactly a
> Markov kernel from `Ω'` to `Ω`: the observable `f` is sent to its average `x ↦ ∫ f d(κ x)`.
> Relabeling outcomes along a measurable map is the deterministic case.
>
> In a normal state of `Ω'`, the channel turns the outcome distribution into its composite with the
> kernel.

## ii. Key results

> - `BoundedMeasurable.comap` : relabeling outcomes along a measurable map.
> - `BoundedMeasurable.ofKernel` : the channel of a Markov kernel.
> - `BoundedMeasurable.toKernel` : the Markov kernel of a normal channel.
> - `BoundedMeasurable.kernelEquiv` : **normal classical channels are Markov kernels**.
> - `BoundedMeasurable.toMeasure_comp` : a normal channel acts on outcome distributions by composing
>   with its kernel.

## iv. References

> * None.

## A. Relabeling outcomes

**`BoundedMeasurable.comap`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L63).

> Relabeling outcomes along a measurable map `g : Ω' → Ω`: the observable `f` of `Ω` becomes
> the observable `f ∘ g` of `Ω'`.

```lean
def comap (g : Ω' → Ω) (hg : Measurable g) : Channel (BoundedMeasurable Ω) (BoundedMeasurable Ω')
```

**`BoundedMeasurable.comap_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L68).

```lean
lemma comap_apply (g : Ω' → Ω) (hg : Measurable g) (f : BoundedMeasurable Ω) (x : Ω') :
    comap g hg f x = f (g x)
```

**`BoundedMeasurable.isNormal_comap`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L71).

```lean
lemma isNormal_comap (g : Ω' → Ω) (hg : Measurable g) : (comap g hg).IsNormal
```

## B. The channel of a Markov kernel

**`BoundedMeasurable.kernelAverage`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L81).

> The average `x ↦ ∫ f d(κ x)` of an observable `f` against a Markov kernel.

```lean
noncomputable def kernelAverage (f : BoundedMeasurable Ω) : BoundedMeasurable Ω'
```

**`BoundedMeasurable.kernelAverage_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L85).

```lean
lemma kernelAverage_apply (f : BoundedMeasurable Ω) (x : Ω') :
    kernelAverage κ f x = ∫ y, f y ∂(κ x)
```

**`BoundedMeasurable.ofKernel`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L90).

> The channel of a Markov kernel `κ` from `Ω'` to `Ω`: the observable `f` becomes its average
> `x ↦ ∫ f d(κ x)`.

```lean
noncomputable def ofKernel : Channel (BoundedMeasurable Ω) (BoundedMeasurable Ω')
```

**`BoundedMeasurable.ofKernel_apply`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L98).

```lean
lemma ofKernel_apply (f : BoundedMeasurable Ω) (x : Ω') :
    ofKernel κ f x = ∫ y, f y ∂(κ x)
```

**`BoundedMeasurable.isNormal_ofKernel`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L101).

```lean
lemma isNormal_ofKernel : (ofKernel κ).IsNormal
```

## C. The Markov kernel of a normal channel

**`BoundedMeasurable.isNormal_eval_comp`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L114).

```lean
lemma isNormal_eval_comp (x : Ω') : ((eval x).comp K).IsNormal
```

**`BoundedMeasurable.toKernel`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L119).

> The Markov kernel of a normal channel: at `x`, the outcome distribution of the state
> `f ↦ K f x`.

```lean
noncomputable def toKernel : Kernel Ω' Ω
```

**`BoundedMeasurable.toKernel_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L125).

```lean
lemma toKernel_apply {s : Set Ω} (hs : MeasurableSet s) (x : Ω') :
    toKernel K hK x s = ENNReal.ofReal (K (indicator s hs) x)
```

**An instance with no name**, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L129).

```lean
instance : IsMarkovKernel (toKernel K hK)
```

**`BoundedMeasurable.toMeasure_comp`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L133).

> A normal channel acts on outcome distributions by composing with its kernel.

```lean
lemma toMeasure_comp (σ : 𝓢[ℝ, BoundedMeasurable Ω']) (hσ : σ.IsNormal) :
    (toMeasure (σ.comp K) (UnitalPositiveLinearMap.IsNormal.comp hK hσ) : Measure Ω) =
      toKernel K hK ∘ₘ toMeasure σ hσ
```

## D. The correspondence

**`BoundedMeasurable.ofKernel_toKernel`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L149).

```lean
lemma ofKernel_toKernel (K : Channel (BoundedMeasurable Ω) (BoundedMeasurable Ω'))
    (hK : K.IsNormal) :
    ofKernel (toKernel K hK) = K
```

**`BoundedMeasurable.toKernel_ofKernel`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L155).

```lean
lemma toKernel_ofKernel (κ : Kernel Ω' Ω) [IsMarkovKernel κ] :
    toKernel (ofKernel κ) (isNormal_ofKernel κ) = κ
```

**`BoundedMeasurable.kernelEquiv`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean#L163).

> **Normal classical channels are Markov kernels.**

```lean
noncomputable def kernelEquiv :
    {K : Channel (BoundedMeasurable Ω) (BoundedMeasurable Ω') // K.IsNormal} ≃
      {κ : Kernel Ω' Ω // IsMarkovKernel κ}
```

## Depends on

- [States of a classical system](normalstates.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Channel.lean)
