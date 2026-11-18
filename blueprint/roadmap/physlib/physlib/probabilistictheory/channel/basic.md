---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap, UnitalPositiveLinearMap.toPositiveLinearMap_apply, UnitalPositiveLinearMap.toPositiveLinearMap_injective, UnitalPositiveLinearMap.toLinearMap_injective, UnitalPositiveLinearMap.id, UnitalPositiveLinearMap.comp, UnitalPositiveLinearMap.id_apply, UnitalPositiveLinearMap.comp_apply
statement: formalized
proof: formalized
---

# Positive unital maps

The module `Physlib.ProbabilisticTheory.Channel.Basic`, [Physlib/ProbabilisticTheory/Channel/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean): 40 declarations (14 instances with no name), 16 with a docstring.

## i. Overview

> In the order-unit-space model used here, a channel is a positive unital transformation: it sends
> observables to observables without turning a possible outcome negative, and it leaves the certain
> outcome certain. This covers time evolution, noise, and measurements whose outcomes are discarded
> at the level of a general probabilistic theory. For quantum systems with a specified composite
> structure, physical channels normally require the stronger condition of complete positivity,
> which is not expressible using the order-unit structure alone.
>
> A channel `Φ : Channel P Q` between probabilistic theories is a unital positive linear map from
> `P.Observables` to `Q.Observables`. States and local nets still use unital positive linear maps
> between bare order-unit spaces.

## ii. Key results

> - `UnitalPositiveLinearMap` : a positive linear map preserving `1`, notated `E →ₚ₁[R] F`.
> - `PositiveLinearMap` scalar action : positive linear maps can be scaled by nonnegative reals.
> - `UnitalPositiveLinearMap.ofLinearMap` : bundle a linear map after checking positivity and
>   unitality.
> - `UnitalPositiveLinearMap.ofPositiveLinearMap` : bundle a positive linear map after checking
>   unitality.
> - `UnitalPositiveLinearMap.id`, `UnitalPositiveLinearMap.comp` : the identity and composition of
>   unital positive linear maps.
> - `Channel` : channels between probabilistic theories.
> - `Channel.id`, `Channel.comp` : the identity and composition of channels.

## iv. References

## A. Unital positive linear maps

**`UnitalPositiveLinearMap`**, a structure, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L62).

> A positive linear map preserving `1`.

```lean
structure UnitalPositiveLinearMap (R E F : Type*) [Semiring R]
    [AddCommMonoid E] [PartialOrder E] [AddCommMonoid F] [PartialOrder F]
    [Module R E] [Module R F] [One E] [One F] extends E →ₚ[R] F, OneHom E F
```

**An instance with no name**, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L80).

```lean
instance : FunLike (E →ₚ₁[R] F) E F
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L84).

```lean
instance : LinearMapClass (E →ₚ₁[R] F) R E F
```

**An instance with no name**, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L88).

```lean
instance : OrderHomClass (E →ₚ₁[R] F) E F
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L91).

```lean
instance : OneHomClass (E →ₚ₁[R] F) E F
```

**An instance with no name**, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L94).

```lean
instance : Coe (E →ₚ₁[R] F) (E →ₚ[R] F)
```

**`UnitalPositiveLinearMap.toPositiveLinearMap_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L97).

```lean
lemma toPositiveLinearMap_apply (f : E →ₚ₁[R] F) (x : E) : f.toPositiveLinearMap x = f x
```

**`UnitalPositiveLinearMap.toPositiveLinearMap_injective`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L100).

> Unital positive linear maps are determined by their underlying positive linear map.

```lean
lemma toPositiveLinearMap_injective :
    Function.Injective (toPositiveLinearMap (R := R) (E := E) (F := F))
```

**`UnitalPositiveLinearMap.toLinearMap_injective`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L105).

> Unital positive linear maps are determined by their underlying linear map.

```lean
lemma toLinearMap_injective : Function.Injective (fun f : E →ₚ₁[R] F => f.toLinearMap)
```

**`UnitalPositiveLinearMap.id`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L111).

> The identity as a unital positive linear map.

```lean
def id : E →ₚ₁[R] E
```

**`UnitalPositiveLinearMap.comp`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L116).

> The composition of unital positive linear maps.

```lean
def comp (g : F →ₚ₁[R] G) (f : E →ₚ₁[R] F) : E →ₚ₁[R] G
```

**`UnitalPositiveLinearMap.id_apply`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L120).

```lean
lemma id_apply (x : E) : UnitalPositiveLinearMap.id R E x = x
```

**`UnitalPositiveLinearMap.comp_apply`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L122).

```lean
lemma comp_apply (g : F →ₚ₁[R] G) (f : E →ₚ₁[R] F) (x : E) : g.comp f x = g (f x)
```

**`UnitalPositiveLinearMap.comp_id`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L124).

```lean
lemma comp_id (f : E →ₚ₁[R] F) : f.comp (.id R E) = f
```

**`UnitalPositiveLinearMap.id_comp`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L126).

```lean
lemma id_comp (f : E →ₚ₁[R] F) : (UnitalPositiveLinearMap.id R F).comp f = f
```

**An instance with no name**, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L130).

> Unital positive linear maps from a space to itself form a monoid under composition, with the
> identity as unit.

```lean
instance : Monoid (E →ₚ₁[R] E)
```

## B. Constructing unital positive linear maps

**`UnitalPositiveLinearMap.ofLinearMap`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L153).

> Bundle a linear map after proving only positivity and preservation of `1`.

```lean
def ofLinearMap (f : E →ₗ[R] F) (hpos : ∀ x, 0 ≤ x → 0 ≤ f x) (hone : f 1 = 1) : E →ₚ₁[R] F
```

**`UnitalPositiveLinearMap.ofPositiveLinearMap`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L158).

> Bundle a positive linear map after proving only that it preserves `1`.

```lean
def ofPositiveLinearMap (f : E →ₚ[R] F) (hone : f 1 = 1) : E →ₚ₁[R] F
```

**`UnitalPositiveLinearMap.ofPositiveLinearMap_apply`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L164).

```lean
lemma ofPositiveLinearMap_apply (f : E →ₚ[R] F) (hone : f 1 = 1) (x : E) :
    ofPositiveLinearMap f hone x = f x
```

## C. Scaling positive linear maps

> Positive linear maps are closed under addition and under scaling by nonnegative reals, but
> unital ones are not closed under scaling.

**An instance with no name**, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L186).

```lean
instance : SMul NNReal (E →ₚ[R] F)
```

**`PositiveLinearMap.nnreal_smul_apply`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L191).

```lean
lemma nnreal_smul_apply (c : NNReal) (f : E →ₚ[R] F) (x : E) : (c • f) x = c • f x
```

## D. Channels between probabilistic theories

**`Channel`**, a structure, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L203).

> A channel preserves positivity and the certain outcome between observable spaces.

```lean
structure Channel (P Q : ProbabilisticTheory) extends P.Observables →ₚ[ℝ] Q.Observables where
  /-- The certain outcome is sent to the certain outcome. -/
  map_one' : toFun 1 = 1
```

**An instance with no name**, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L211).

```lean
instance : FunLike (Channel P Q) P.Observables Q.Observables
```

**An instance with no name**, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L215).

```lean
instance : AddMonoidHomClass (Channel P Q) P.Observables Q.Observables
```

**An instance with no name**, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L219).

```lean
instance : LinearMapClass (Channel P Q) ℝ P.Observables Q.Observables
```

**An instance with no name**, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L223).

```lean
instance : OrderHomClass (Channel P Q) P.Observables Q.Observables
```

**An instance with no name**, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L226).

```lean
instance : OneHomClass (Channel P Q) P.Observables Q.Observables
```

**An instance with no name**, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L229).

```lean
instance : Coe (Channel P Q) (P.Observables →ₚ[ℝ] Q.Observables)
```

**`Channel.toPositiveLinearMap_apply`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L232).

```lean
lemma toPositiveLinearMap_apply (f : Channel P Q) (x : P.Observables) :
    f.toPositiveLinearMap x = f x
```

**`Channel.toPositiveLinearMap_injective`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L236).

> Channels are determined by their underlying positive linear map.

```lean
lemma toPositiveLinearMap_injective :
    Function.Injective (toPositiveLinearMap (P := P) (Q := Q))
```

**`Channel.toLinearMap_injective`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L241).

> Channels are determined by their underlying linear map.

```lean
lemma toLinearMap_injective : Function.Injective (fun f : Channel P Q => f.toLinearMap)
```

**`Channel.id`**, a def, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L246).

> The identity as a channel.

```lean
def id : Channel P P
```

**`Channel.comp`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L251).

> The composition of channels.

```lean
def comp (g : Channel Q R) (f : Channel P Q) : Channel P R
```

**`Channel.id_apply`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L255).

```lean
lemma id_apply (x : P.Observables) : Channel.id P x = x
```

**`Channel.comp_apply`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L257).

```lean
lemma comp_apply (g : Channel Q R) (f : Channel P Q) (x : P.Observables) :
    g.comp f x = g (f x)
```

**`Channel.comp_id`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L260).

```lean
lemma comp_id (f : Channel P Q) : f.comp (.id P) = f
```

**`Channel.id_comp`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L262).

```lean
lemma id_comp (f : Channel P Q) : (Channel.id Q).comp f = f
```

**An instance with no name**, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L265).

> Channels on an observable space form a monoid under composition.

```lean
instance : Monoid (Channel P P)
```

**`Channel.ofLinearMap`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L273).

> Bundle a linear map after proving only positivity and preservation of `1`.

```lean
def ofLinearMap (f : P.Observables →ₗ[ℝ] Q.Observables) (hpos : ∀ x, 0 ≤ x → 0 ≤ f x)
    (hone : f 1 = 1) : Channel P Q
```

**`Channel.ofPositiveLinearMap`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean#L279).

> Bundle a positive linear map after proving only that it preserves `1`.

```lean
def ofPositiveLinearMap (f : P.Observables →ₚ[ℝ] Q.Observables) (hone : f 1 = 1) : Channel P Q
```

## Depends on

- [Probabilistic theories](../basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Basic.lean)
