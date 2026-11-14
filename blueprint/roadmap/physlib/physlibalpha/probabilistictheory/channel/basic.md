---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap, ProbabilisticTheory.UnitalPositiveLinearMap.ext, ProbabilisticTheory.UnitalPositiveLinearMap.toLinearMap_injective, ProbabilisticTheory.UnitalPositiveLinearMap.ofLinearMap, ProbabilisticTheory.UnitalPositiveLinearMap.id, ProbabilisticTheory.UnitalPositiveLinearMap.id_apply, ProbabilisticTheory.UnitalPositiveLinearMap.comp, ProbabilisticTheory.UnitalPositiveLinearMap.comp_apply
statement: formalized
proof: formalized
---

# Channels

The module `PhyslibAlpha.ProbabilisticTheory.Channel.Basic`, [PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean): 17 declarations (4 instances with no name), 7 with a docstring.

> Channels as unital positive linear maps between order-unit spaces, and their composition.

## i. Overview

> A channel is a transformation of a system, described by what it does to observables: it sends
> observables of the output system to observables of the input system, keeps nonnegative
> observables nonnegative, and keeps the certain outcome certain. This covers time evolution, noise,
> and measurements. Quantum channels additionally stay positive on composite systems; they are
> `QuantumChannel`.

## ii. Key results

> - `UnitalPositiveLinearMap` : a positive linear map preserving `1`, notated `E →ₚ₁[R] F`.
> - `Channel E F` : a channel between order-unit spaces, a unital positive map `E →ₚ₁[ℝ] F`.
> - `UnitalPositiveLinearMap.ofLinearMap` : bundle a linear map after checking positivity and
>   unitality.

## iv. References

> * None.

## A. Unital positive linear maps

**`ProbabilisticTheory.UnitalPositiveLinearMap`**, a structure, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L54).

> A positive linear map preserving `1`.

```lean
structure UnitalPositiveLinearMap (R E F : Type*) [Semiring R]
    [AddCommMonoid E] [PartialOrder E] [AddCommMonoid F] [PartialOrder F]
    [Module R E] [Module R F] [One E] [One F] extends E →ₚ[R] F where
  /-- A unital positive linear map preserves the order unit. -/
  map_one' : toPositiveLinearMap 1 = 1
```

**An instance with no name**, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L69).

```lean
instance : FunLike (E →ₚ₁[R] F) E F
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L77).

```lean
instance : LinearMapClass (E →ₚ₁[R] F) R E F
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L81).

```lean
instance : OrderHomClass (E →ₚ₁[R] F) E F
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L84).

```lean
instance : OneHomClass (E →ₚ₁[R] F) E F
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.ext`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L88).

```lean
lemma ext {f g : E →ₚ₁[R] F} (h : ∀ x, f x = g x) : f = g
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.toLinearMap_injective`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L92).

> Unital positive linear maps are determined by their underlying linear map.

```lean
lemma toLinearMap_injective : Function.Injective (fun f : E →ₚ₁[R] F => f.toLinearMap)
```

## B. Constructing unital positive linear maps

**`ProbabilisticTheory.UnitalPositiveLinearMap.ofLinearMap`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L111).

> Bundle a linear map after proving only positivity and preservation of `1`.

```lean
def ofLinearMap (f : E →ₗ[R] F) (hpos : ∀ x, 0 ≤ x → 0 ≤ f x) (hone : f 1 = 1) : E →ₚ₁[R] F
```

## C. Composing channels

**`ProbabilisticTheory.UnitalPositiveLinearMap.id`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L132).

> The identity channel.

```lean
protected def id : E →ₚ₁[R] E
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.id_apply`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L137).

```lean
lemma id_apply (x : E) : UnitalPositiveLinearMap.id R E x = x
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.comp`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L140).

> The composite of two channels.

```lean
def comp (g : F →ₚ₁[R] G) (f : E →ₚ₁[R] F) : E →ₚ₁[R] G
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.comp_apply`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L145).

```lean
lemma comp_apply (g : F →ₚ₁[R] G) (f : E →ₚ₁[R] F) (x : E) : g.comp f x = g (f x)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.comp_id`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L148).

```lean
lemma comp_id (f : E →ₚ₁[R] F) : f.comp (.id R E) = f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.id_comp`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L152).

```lean
lemma id_comp (f : E →ₚ₁[R] F) : (UnitalPositiveLinearMap.id R F).comp f = f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.comp_assoc`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L155).

```lean
lemma comp_assoc {H : Type*} [AddCommMonoid H] [PartialOrder H] [Module R H] [One H]
    (h : G →ₚ₁[R] H) (g : F →ₚ₁[R] G) (f : E →ₚ₁[R] F) :
    h.comp (g.comp f) = (h.comp g).comp f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.instMonoid`**, an instance, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L161).

> Positive unital endomorphisms form a monoid under composition.

```lean
instance instMonoid : Monoid (E →ₚ₁[R] E)
```

## D. Channels

**`ProbabilisticTheory.Channel`**, an abbrev, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean#L177).

> A channel between two systems: a unital positive map between their order-unit spaces.

```lean
abbrev Channel (E F : Type*) [OrderUnitSpace E] [OrderUnitSpace F]
```

## Depends on

- [Ordered vector spaces and order units](../../../physlib/probabilistictheory/orderunit/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Basic.lean)
