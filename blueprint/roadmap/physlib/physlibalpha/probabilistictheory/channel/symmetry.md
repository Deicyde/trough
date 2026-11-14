---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsOrderAutomorphism, ProbabilisticTheory.isOrderAutomorphism_id, ProbabilisticTheory.IsOrderAutomorphism.inverse, ProbabilisticTheory.IsOrderAutomorphism.inverse_comp, ProbabilisticTheory.IsOrderAutomorphism.comp_inverse, ProbabilisticTheory.IsOrderAutomorphism.inverse_apply_apply, ProbabilisticTheory.IsOrderAutomorphism.apply_inverse_apply, ProbabilisticTheory.IsOrderAutomorphism.inverse_isOrderAutomorphism
statement: formalized
proof: formalized
---

# Symmetries

The module `PhyslibAlpha.ProbabilisticTheory.Channel.Symmetry`, [PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean): 34 declarations (1 instance with no name), 17 with a docstring.

> Symmetries as channels with channel inverses, their group, action on states, and dynamics.

## i. Overview

> A symmetry of a system is a reversible transformation: a channel whose inverse is also a channel.
> Symmetries form a group, and they act on states by `g • ω = ω ∘ g⁻¹`. A group acts by symmetries
> through a homomorphism into the symmetry group. A one-parameter group of symmetries is reversible
> dynamics.

## ii. Key results

> - `IsOrderAutomorphism` : a channel with a channel inverse.
> - `Symmetry` : the group of symmetries.
> - `Symmetry.instMulActionState` : symmetries act on states.
> - `Symmetry.stateSMul` : the action on states of a group acting by symmetries.
> - `OneParameterAutomorphismGroup` : reversible dynamics.

## iv. References

> * None.

## A. Order automorphisms

**`ProbabilisticTheory.IsOrderAutomorphism`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L55).

> `φ` is an order-automorphism of `E`: a channel with a two-sided inverse that is itself a
> channel. Equivalently, `φ` is bijective and both `φ` and `φ⁻¹` are positive and unital
> (`IsOrderAutomorphism.bijective` records the "bijective" half of that equivalence).

```lean
def IsOrderAutomorphism (φ : Channel E E) : Prop
```

**`ProbabilisticTheory.isOrderAutomorphism_id`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L59).

> The identity is trivially an order-automorphism.

```lean
lemma isOrderAutomorphism_id : IsOrderAutomorphism (.id ℝ E : Channel E E)
```

**`ProbabilisticTheory.IsOrderAutomorphism.inverse`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L67).

> A chosen inverse channel witnessing `φ` is an order-automorphism.

```lean
noncomputable def inverse (h : IsOrderAutomorphism φ) : Channel E E
```

**`ProbabilisticTheory.IsOrderAutomorphism.inverse_comp`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L69).

```lean
lemma inverse_comp (h : IsOrderAutomorphism φ) : h.inverse.comp φ = .id ℝ E
```

**`ProbabilisticTheory.IsOrderAutomorphism.comp_inverse`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L71).

```lean
lemma comp_inverse (h : IsOrderAutomorphism φ) : φ.comp h.inverse = .id ℝ E
```

**`ProbabilisticTheory.IsOrderAutomorphism.inverse_apply_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L74).

> Pointwise form of `inverse_comp`: applying `φ` then its chosen inverse is the identity.

```lean
lemma inverse_apply_apply (h : IsOrderAutomorphism φ) (x : E) : h.inverse (φ x) = x
```

**`ProbabilisticTheory.IsOrderAutomorphism.apply_inverse_apply`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L78).

> Pointwise form of `comp_inverse`: applying the chosen inverse then `φ` is the identity.

```lean
lemma apply_inverse_apply (h : IsOrderAutomorphism φ) (x : E) : φ (h.inverse x) = x
```

**`ProbabilisticTheory.IsOrderAutomorphism.inverse_isOrderAutomorphism`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L83).

> The inverse of an order-automorphism is again an order-automorphism, witnessed by `φ` itself.

```lean
lemma inverse_isOrderAutomorphism (h : IsOrderAutomorphism φ) :
    IsOrderAutomorphism h.inverse
```

**`ProbabilisticTheory.IsOrderAutomorphism.comp`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L89).

> The composite of two order-automorphisms is again one, witnessed by the composite of their
> inverses in the opposite order.

```lean
lemma comp (hφ : IsOrderAutomorphism φ) (hψ : IsOrderAutomorphism ψ) :
    IsOrderAutomorphism (φ.comp ψ)
```

**`ProbabilisticTheory.IsOrderAutomorphism.bijective`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L99).

> An order-automorphism is, in particular, a bijection of `E` — the "equivalently" half of the
> definition's docstring.

```lean
lemma bijective (h : IsOrderAutomorphism φ) : Function.Bijective φ
```

## B. The symmetry group

**`ProbabilisticTheory.Symmetry`**, an abbrev, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L109).

> A symmetry of `E`: an order-automorphism, bundled with its defining property. Composition
> makes these into a group, `Symmetry.instGroup` below. Reducible, so the underlying channel
> coercion (`Subtype.val`) unifies transparently wherever a `Channel E E` is expected.

```lean
abbrev Symmetry (E : Type*) [OrderUnitSpace E]
```

**`ProbabilisticTheory.Symmetry.ext`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L115).

```lean
lemma ext {φ ψ : Symmetry E} (h : ∀ x, (φ : Channel E E) x = (ψ : Channel E E) x) : φ = ψ
```

**`ProbabilisticTheory.Symmetry.instOne`**, an instance, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L118).

```lean
instance instOne : One (Symmetry E)
```

**`ProbabilisticTheory.Symmetry.instMul`**, an instance, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L120).

```lean
instance instMul : Mul (Symmetry E)
```

**`ProbabilisticTheory.Symmetry.instInv`**, an instance, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L122).

```lean
noncomputable instance instInv : Inv (Symmetry E)
```

**`ProbabilisticTheory.Symmetry.val_one`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L125).

```lean
lemma val_one : (1 : Symmetry E).1 = .id ℝ E
```

**`ProbabilisticTheory.Symmetry.val_mul`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L127).

```lean
lemma val_mul (φ ψ : Symmetry E) : (φ * ψ).1 = φ.1.comp ψ.1
```

**`ProbabilisticTheory.Symmetry.val_inv`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L129).

```lean
lemma val_inv (φ : Symmetry E) : (φ⁻¹ : Symmetry E).1 = φ.2.inverse
```

**`ProbabilisticTheory.Symmetry.instGroup`**, an instance, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L133).

> Order-automorphisms of `E` form a group under composition, with `1` the identity channel and
> `φ⁻¹` the (chosen) inverse channel.

```lean
noncomputable instance instGroup : Group (Symmetry E)
```

**`ProbabilisticTheory.Symmetry.unitsEquiv`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L142).

> The symmetry group is canonically equivalent to the group of units of the monoid of unital
> positive endomorphisms. This identifies the explicit order-automorphism presentation with
> Mathlib's general algebraic notion of an invertible element.

```lean
noncomputable def unitsEquiv : Symmetry E ≃* (Channel E E)ˣ
```

## C. The induced action on states

**`ProbabilisticTheory.Symmetry.instMulActionState`**, an instance, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L160).

> The canonical action of `Symmetry E` on the state space `𝓢[ℝ, E]`: a symmetry `φ` transports a
> state `ω` by pulling it back along the inverse automorphism, `φ • ω = ω ∘ φ⁻¹`. This is exactly
> the Schrödinger-picture pushforward of a state along the channel `φ⁻¹`, so
> it costs nothing beyond `UnitalPositiveLinearMap.comp` — positivity and normalization of `φ • ω`
> are already built into `.comp`.

```lean
noncomputable instance instMulActionState : MulAction (Symmetry E) (𝓢[ℝ, E])
```

**`ProbabilisticTheory.Symmetry.smul_state_def`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L169).

```lean
lemma smul_state_def (φ : Symmetry E) (ω : 𝓢[ℝ, E]) : φ • ω = ω.comp φ⁻¹.1
```

**`ProbabilisticTheory.Symmetry.stateSMul`**, a def, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L172).

> The action on states of a group acting by symmetries.

```lean
noncomputable def stateSMul {G : Type*} [Group G] (ρ : G →* Symmetry E) (g : G) (ω : 𝓢[ℝ, E]) :
    𝓢[ℝ, E]
```

**`ProbabilisticTheory.Symmetry.stateSMul_one`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L176).

```lean
lemma stateSMul_one {G : Type*} [Group G] (ρ : G →* Symmetry E) (ω : 𝓢[ℝ, E]) :
    stateSMul ρ 1 ω = ω
```

**`ProbabilisticTheory.Symmetry.stateSMul_mul`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L180).

```lean
lemma stateSMul_mul {G : Type*} [Group G] (ρ : G →* Symmetry E) (g h : G) (ω : 𝓢[ℝ, E]) :
    stateSMul ρ (g * h) ω = stateSMul ρ g (stateSMul ρ h ω)
```

## D. One-parameter automorphism groups

**`ProbabilisticTheory.OneParameterAutomorphismGroup`**, a structure, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L190).

> A one-parameter group of order-automorphisms of `E`, indexed by time: `α t` is the
> automorphism of "let `t` units of time pass".

```lean
structure OneParameterAutomorphismGroup (E : Type*) [OrderUnitSpace E] where
  /-- The automorphism of `E` after time `t` has passed. -/
  toFun : ℝ → Channel E E
  /-- Letting no time pass does nothing. -/
  map_zero' : toFun 0 = .id ℝ E
  /-- Letting `s + t` units of time pass is the same as letting `t` pass, then `s`. -/
  map_add' : ∀ s t, toFun (s + t) = (toFun s).comp (toFun t)
```

**An instance with no name**, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L200).

```lean
instance : CoeFun (OneParameterAutomorphismGroup E) (fun _ => ℝ → Channel E E)
```

**`ProbabilisticTheory.OneParameterAutomorphismGroup.coe_map_zero`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L202).

```lean
lemma coe_map_zero (α : OneParameterAutomorphismGroup E) : α 0 = .id ℝ E
```

**`ProbabilisticTheory.OneParameterAutomorphismGroup.coe_map_add`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L204).

```lean
lemma coe_map_add (α : OneParameterAutomorphismGroup E) (s t : ℝ) :
    α (s + t) = (α s).comp (α t)
```

**`ProbabilisticTheory.OneParameterAutomorphismGroup.isOrderAutomorphism`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L208).

> Every map of a one-parameter group of symmetries is a symmetry, with inverse `α (-t)`.

```lean
lemma isOrderAutomorphism (α : OneParameterAutomorphismGroup E) (t : ℝ) :
    IsOrderAutomorphism (α t)
```

**`ProbabilisticTheory.OneParameterAutomorphismGroup.toSymmetryHom`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L217).

> A one-parameter automorphism group organizes into a homomorphism from `Multiplicative ℝ` into
> the automorphism group `Symmetry E` — reconnecting to the general group action of
> `Symmetry.stateSMul` above, with `G = Multiplicative ℝ`.

```lean
noncomputable def toSymmetryHom (α : OneParameterAutomorphismGroup E) :
    Multiplicative ℝ →* Symmetry E
```

**`ProbabilisticTheory.OneParameterAutomorphismGroup.stateEvolution`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L227).

> The state evolution induced by a one-parameter automorphism group: `α.stateEvolution t` moves
> a state forward by time `t`, and composes correctly in `t` (`Symmetry.stateSMul_mul` specialized
> along `toSymmetryHom`).

```lean
noncomputable def stateEvolution (α : OneParameterAutomorphismGroup E) (t : ℝ) (ω : 𝓢[ℝ, E]) :
    𝓢[ℝ, E]
```

**`ProbabilisticTheory.OneParameterAutomorphismGroup.stateEvolution_zero`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L231).

```lean
lemma stateEvolution_zero (α : OneParameterAutomorphismGroup E) (ω : 𝓢[ℝ, E]) :
    α.stateEvolution 0 ω = ω
```

**`ProbabilisticTheory.OneParameterAutomorphismGroup.stateEvolution_add`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean#L235).

```lean
lemma stateEvolution_add (α : OneParameterAutomorphismGroup E) (s t : ℝ) (ω : 𝓢[ℝ, E]) :
    α.stateEvolution (s + t) ω = α.stateEvolution s (α.stateEvolution t ω)
```

## Depends on

- [Channels](basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Symmetry.lean)
