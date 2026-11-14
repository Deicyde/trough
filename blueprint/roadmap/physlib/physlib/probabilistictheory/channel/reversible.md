---
declaration: module
origin: cited
lean: ProbabilisticTheory.Reversible, ProbabilisticTheory.Reversible.ext, ProbabilisticTheory.Reversible.refl, ProbabilisticTheory.Reversible.symm, ProbabilisticTheory.Reversible.trans, ProbabilisticTheory.Reversible.refl_apply, ProbabilisticTheory.Reversible.symm_apply_apply, ProbabilisticTheory.Reversible.apply_symm_apply
statement: formalized
proof: formalized
---

# Reversible transformations of observables

The module `Physlib.ProbabilisticTheory.Channel.Reversible`, [Physlib/ProbabilisticTheory/Channel/Reversible.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean): 23 declarations (1 instance with no name), 11 with a docstring.

> Reversible transformations of observable spaces, their group structure, their action on states and
> the transport of group actions.

## i. Overview

> Time evolution, spatial symmetries and changes of reference frame all have something in common:
> they transform observables in a way that can be undone.
>
> This motivates reversible transformations, defined as unital linear order isomorphisms of
> observable spaces. They form a group and naturally act on states. A group representation by
> reversible transformations describes symmetries or reversible dynamics. For example, time evolution
> is represented by the additive group of real numbers. A reversible transformation also transports a
> group action from one observable space to another by conjugation.

## ii. Key results

> - `Reversible`: Reversible transformations, i.e. unital linear order isomorphisms of
>   observable spaces.
> - `Reversible.toChannelHom`: Reversible transformations embed in the monoid of channels.
> - `Reversible.instMulActionState`: The induced action on states.
> - `Reversible.transport`: Transport of a group action along a reversible transformation.
> - `IsInvariant`: A state fixed by every transformation of a group action.

## iv. References

## A. Reversible transformations

### A.1. Definition

**`ProbabilisticTheory.Reversible`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L63).

> A reversible transformation between observable spaces: a linear bijection that preserves and
> reflects the order and preserves the order unit. Both it and its inverse are channels.

```lean
structure Reversible (P Q : ProbabilisticTheory)
    extends P.Observables ≃ₗ[ℝ] Q.Observables where
  /-- The equivalence preserves and reflects the order. -/
  map_le_map_iff' : ∀ {x y : P.Observables}, toLinearEquiv x ≤ toLinearEquiv y ↔ x ≤ y
  /-- The order unit is preserved. -/
  map_one' : toLinearEquiv 1 = 1
```

**An instance with no name**, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L74).

```lean
instance : FunLike (Reversible P Q) P.Observables Q.Observables
```

**`ProbabilisticTheory.Reversible.ext`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L83).

```lean
lemma ext {e f : Reversible P Q} (h : ∀ x, e x = f x) : e = f
```

### A.2. Group structure

**`ProbabilisticTheory.Reversible.refl`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L88).

> The identity reversible transformation.

```lean
def refl (P : ProbabilisticTheory) : Reversible P P
```

**`ProbabilisticTheory.Reversible.symm`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L94).

> The inverse of a reversible transformation.

```lean
def symm (e : Reversible P Q) : Reversible Q P
```

**`ProbabilisticTheory.Reversible.trans`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L101).

> Composition of reversible transformations, applying `e₁` before `e₂`.

```lean
def trans (e₁ : Reversible P Q) (e₂ : Reversible Q R) : Reversible P R
```

**`ProbabilisticTheory.Reversible.refl_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L109).

```lean
lemma refl_apply (x : P.Observables) : refl P x = x
```

**`ProbabilisticTheory.Reversible.symm_apply_apply`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L111).

```lean
lemma symm_apply_apply (e : Reversible P Q) (x : P.Observables) : e.symm (e x) = x
```

**`ProbabilisticTheory.Reversible.apply_symm_apply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L114).

```lean
lemma apply_symm_apply (e : Reversible P Q) (y : Q.Observables) : e (e.symm y) = y
```

**`ProbabilisticTheory.Reversible.trans_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L117).

```lean
lemma trans_apply (e₁ : Reversible P Q) (e₂ : Reversible Q R) (x : P.Observables) :
    e₁.trans e₂ x = e₂ (e₁ x)
```

**`ProbabilisticTheory.Reversible.automorphismGroup`**, an instance, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L121).

> Reversible transformations of a single space form a group under composition.

```lean
instance automorphismGroup : Group (Reversible P P)
```

**`ProbabilisticTheory.Reversible.mul_apply`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L130).

```lean
lemma mul_apply (f g : Reversible P P) (x : P.Observables) : (f * g) x = f (g x)
```

**`ProbabilisticTheory.Reversible.one_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L132).

```lean
lemma one_apply (x : P.Observables) : (1 : Reversible P P) x = x
```

**`ProbabilisticTheory.Reversible.inv_apply`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L134).

```lean
lemma inv_apply (f : Reversible P P) (x : P.Observables) : f⁻¹ x = f.symm x
```

### A.3. As channels

**`ProbabilisticTheory.Reversible.toChannel`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L139).

> A reversible transformation regarded as a channel.

```lean
def toChannel (e : Reversible P Q) : Channel P Q
```

**`ProbabilisticTheory.Reversible.toChannel_apply`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L143).

```lean
lemma toChannel_apply (e : Reversible P Q) (x : P.Observables) : e.toChannel x = e x
```

**`ProbabilisticTheory.Reversible.toChannelHom`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L146).

> Regarding reversible transformations as channels is a homomorphism of monoids.

```lean
def toChannelHom : Reversible P P →* Channel P P
```

**`ProbabilisticTheory.Reversible.toChannelHom_apply`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L151).

```lean
lemma toChannelHom_apply (e : Reversible P P) (x : P.Observables) :
    toChannelHom e x = e x
```

## B. Action on states

**`ProbabilisticTheory.Reversible.instMulActionState`**, an instance, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L157).

> The action on states induced by the inverse of a reversible transformation.

```lean
instance instMulActionState : MulAction (Reversible P P) (𝓢[ℝ, P.Observables])
```

**`ProbabilisticTheory.Reversible.smul_state_apply`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L162).

```lean
lemma smul_state_apply (φ : Reversible P P) (ω : 𝓢[ℝ, P.Observables]) (x : P.Observables) :
    (φ • ω) x = ω (φ.symm x)
```

## C. Transport of group actions

### C.1. Conjugation

**`ProbabilisticTheory.Reversible.conj`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L170).

> Conjugation transports reversible dynamics between observable spaces.

```lean
def conj (e : Reversible P Q) : Reversible P P →* Reversible Q Q
```

### C.2. Transported actions

**`ProbabilisticTheory.Reversible.transport`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L178).

> Transport a group action between observable spaces along a reversible transformation.

```lean
def transport (ρ : G →* Reversible P P) (e : Reversible P Q) :
    G →* Reversible Q Q
```

## D. Invariant states

**`ProbabilisticTheory.IsInvariant`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean#L186).

> A state is invariant if it is fixed by every transformation of the group action.

```lean
def IsInvariant {G : Type*} [Group G] {P : ProbabilisticTheory} (ρ : G →* Reversible P P)
    (ω : 𝓢[ℝ, P.Observables]) : Prop
```

## Depends on

- [States](../state/basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Reversible.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Reversible.lean)
