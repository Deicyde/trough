---
declaration: module
origin: cited
lean: Channel, Channel.ext, Channel.toPositiveLinearMap_apply, Channel.toPositiveLinearMap_injective, Channel.toLinearMap_injective, Channel.id, Channel.comp, Channel.id_apply
statement: formalized
proof: formalized
---

# Channels between observable spaces

The module `Physlib.ProbabilisticTheory.Channel.Basic`, [Physlib/ProbabilisticTheory/Channel/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean): 20 declarations (7 instances with no name), 8 with a docstring.

> Channels preserve positivity and the certain outcome between observable spaces.

## i. Overview

> In the order-unit-space model used here, a channel is a positive unital transformation: it sends
> observables to observables without turning a possible outcome negative, and it leaves the certain
> outcome certain. This covers time evolution, noise, and measurements whose outcomes are discarded
> using only ordered real observables and a certain outcome. For quantum systems with a specified
> composite structure, physical channels normally require the stronger condition of complete
> positivity, which is not expressible using the order-unit structure alone.
>
> A channel `Φ : Channel P Q` is a unital positive linear map from
> `P.Observables` to `Q.Observables`.

## ii. Key results

> - `Channel` : channels between observable spaces.
> - `Channel.id`, `Channel.comp` : the identity and composition of channels.
> - `Channel.ofLinearMap` : bundle a linear map after checking positivity and unitality.

## iv. References

## A. Channels between observable spaces

**`Channel`**, a structure, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L47).

> A channel preserves positivity and the certain outcome between observable spaces.

```lean
structure Channel (P Q : ProbabilisticTheory) extends P.Observables →ₚ[ℝ] Q.Observables where
  /-- The certain outcome is sent to the certain outcome. -/
  map_one' : toFun 1 = 1
```

**An instance with no name**, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L55).

```lean
instance : FunLike (Channel P Q) P.Observables Q.Observables
```

**`Channel.ext`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L64).

```lean
lemma ext {f g : Channel P Q} (h : ∀ x, f x = g x) : f = g
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L66).

```lean
instance : AddMonoidHomClass (Channel P Q) P.Observables Q.Observables
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L70).

```lean
instance : LinearMapClass (Channel P Q) ℝ P.Observables Q.Observables
```

**An instance with no name**, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L74).

```lean
instance : OrderHomClass (Channel P Q) P.Observables Q.Observables
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L77).

```lean
instance : OneHomClass (Channel P Q) P.Observables Q.Observables
```

**An instance with no name**, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L80).

```lean
instance : Coe (Channel P Q) (P.Observables →ₚ[ℝ] Q.Observables)
```

**`Channel.toPositiveLinearMap_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L83).

```lean
lemma toPositiveLinearMap_apply (f : Channel P Q) (x : P.Observables) :
    f.toPositiveLinearMap x = f x
```

**`Channel.toPositiveLinearMap_injective`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L87).

> Channels are determined by their underlying positive linear map.

```lean
lemma toPositiveLinearMap_injective :
    Function.Injective (toPositiveLinearMap (P := P) (Q := Q))
```

**`Channel.toLinearMap_injective`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L92).

> Channels are determined by their underlying linear map.

```lean
lemma toLinearMap_injective : Function.Injective (fun f : Channel P Q => f.toLinearMap)
```

**`Channel.id`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L96).

> The identity as a channel.

```lean
def id (P : ProbabilisticTheory) : Channel P P
```

**`Channel.comp`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L101).

> The composition of channels.

```lean
def comp (g : Channel Q R) (f : Channel P Q) : Channel P R
```

**`Channel.id_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L105).

```lean
lemma id_apply (x : P.Observables) : Channel.id P x = x
```

**`Channel.comp_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L107).

```lean
lemma comp_apply (g : Channel Q R) (f : Channel P Q) (x : P.Observables) :
    g.comp f x = g (f x)
```

**`Channel.comp_id`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L110).

```lean
lemma comp_id (f : Channel P Q) : f.comp (.id P) = f
```

**`Channel.id_comp`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L112).

```lean
lemma id_comp (f : Channel P Q) : (Channel.id Q).comp f = f
```

**An instance with no name**, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L115).

> Channels on an observable space form a monoid under composition.

```lean
instance : Monoid (Channel P P)
```

**`Channel.ofLinearMap`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L123).

> Bundle a linear map after proving only positivity and preservation of `1`.

```lean
def ofLinearMap (f : P.Observables →ₗ[ℝ] Q.Observables) (hpos : ∀ x, 0 ≤ x → 0 ≤ f x)
    (hone : f 1 = 1) : Channel P Q
```

**`Channel.ofPositiveLinearMap`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean#L129).

> Bundle a positive linear map after proving only that it preserves `1`.

```lean
def ofPositiveLinearMap (f : P.Observables →ₚ[ℝ] Q.Observables) (hone : f 1 = 1) : Channel P Q
```

## Depends on

- [Probabilistic theories](../basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Channel/Basic.lean)
