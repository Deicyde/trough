---
declaration: module
origin: cited
lean: Channel.mix, Channel.mix_apply, Channel.toLinearMap_mix, Channel.mix_symm, Channel.channelSpace, Channel.channelSpace_convex, Channel.mem_openSegment_iff_exists_mix
statement: formalized
proof: formalized
---

# Convex spaces of channels

The module `Physlib.ProbabilisticTheory.Channel.Convex`, [Physlib/ProbabilisticTheory/Channel/Convex.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean): 7 declarations, 7 with a docstring.

> Random choice between channels and convexity of the resulting space of linear maps.

## i. Overview

> A random choice between two channels is again a channel: their convex combination preserves
> positivity and the certain outcome. Channels therefore form a convex set inside the real
> linear maps between their observable spaces. States inherit this construction as channels
> into ℝ.

## ii. Key results

> - `Channel.mix` : choose between two channels with a specified probability.
> - `Channel.channelSpace_convex` : channels form a convex set of linear maps.
> - `Channel.mem_openSegment_iff_exists_mix` : genuine mixtures describe open segments.

## iv. References

## A. Mixing channels

**`Channel.mix`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean#L50).

> Choose the first channel with probability `t` and the second with probability `1 - t`.

```lean
def mix (Φ Ψ : Channel P Q) (t : unitInterval) : Channel P Q
```

**`Channel.mix_apply`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean#L57).

> A channel mixture acts by the corresponding convex combination of outputs.

```lean
lemma mix_apply (Φ Ψ : Channel P Q) (t : unitInterval) (A : P.Observables) :
    mix Φ Ψ t A = (t : ℝ) • Φ A + (1 - (t : ℝ)) • Ψ A
```

**`Channel.toLinearMap_mix`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean#L61).

> The linear map of a channel mixture is the same convex combination of linear maps.

```lean
lemma toLinearMap_mix (Φ Ψ : Channel P Q) (t : unitInterval) :
    (mix Φ Ψ t).toLinearMap = (t : ℝ) • Φ.toLinearMap + (1 - (t : ℝ)) • Ψ.toLinearMap
```

**`Channel.mix_symm`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean#L65).

> Swapping the channels swaps their probabilities.

```lean
lemma mix_symm (Φ Ψ : Channel P Q) (t : unitInterval) : mix Φ Ψ t = mix Ψ Φ (σ t)
```

## B. The convex channel space

**`Channel.channelSpace`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean#L72).

> Channels viewed as a subset of the real linear maps between observable spaces.

```lean
def channelSpace : Set (P.Observables →ₗ[ℝ] Q.Observables)
```

**`Channel.channelSpace_convex`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean#L76).

> Channels form a convex set in the space of real linear maps.

```lean
lemma channelSpace_convex : Convex ℝ (channelSpace (P := P) (Q := Q))
```

**`Channel.mem_openSegment_iff_exists_mix`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean#L84).

> Open segments between channels consist exactly of their genuine mixtures.

```lean
lemma mem_openSegment_iff_exists_mix (Φ Ψ Χ : Channel P Q) :
    Φ.toLinearMap ∈ openSegment ℝ Ψ.toLinearMap Χ.toLinearMap ↔
      ∃ t : unitInterval, 0 < t ∧ t < 1 ∧ mix Ψ Χ t = Φ
```

## Depends on

- [Channels between observable spaces](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Convex.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Convex.lean)
