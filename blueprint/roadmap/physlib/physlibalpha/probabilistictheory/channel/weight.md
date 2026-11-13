---
declaration: module
origin: cited
lean: ProbabilisticTheory.Weight.comp, ProbabilisticTheory.Weight.comp_apply, ProbabilisticTheory.Weight.comp_id, ProbabilisticTheory.Weight.comp_comp, ProbabilisticTheory.Weight.IsFinite.comp, ProbabilisticTheory.Weight.IsState.comp
statement: formalized
proof: formalized
---

# Weight pushforward along a channel

The module `PhyslibAlpha.ProbabilisticTheory.Channel.Weight`, [PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean): 6 declarations, 3 with a docstring.

> Pushing weights and states forward along a channel, functorially in the channel.

## i. Overview

> A channel from system `A` to system `B` is, in the Schrödinger picture, an affine map on states.
> Dualizing gives a unital positive linear map on effects in the other direction (the Heisenberg
> picture): that map is already `UnitalPositiveLinearMap`, so a channel's adjoint needs no new
> structure. What *is* new is pushing a weight forward along that adjoint, and the fact that a
> state pushes forward to a state.
>
> Read `φ : Channel E₂ E₁` here as the adjoint of a channel `A → B` with effect algebras
> `E₁ = E_A`, `E₂ = E_B`: it pulls an effect of `B` back to an effect of `A`. Precomposing a weight
> on `A` with `φ` gives a weight on `B` — the Schrödinger-picture pushforward — and `Weight.comp_id`,
> `Weight.comp_comp` show this assignment respects identities and composition, so pushforward is a
> functor from unital positive linear maps to weights, contravariant in `φ`.

## ii. Key results

> - `Weight.comp` : the pushforward of a weight along a channel.
> - `Weight.comp_id`, `Weight.comp_comp` : pushforward respects identities and composition.
> - `Weight.IsFinite.comp`, `Weight.IsState.comp` : finite weights and states push forward to
>   finite weights and states.

## iv. References

> * None.

## A. Pushforward of weights

**`ProbabilisticTheory.Weight.comp`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean#L64).

> Precompose a weight on `E₁` with the adjoint `φ : Channel E₂ E₁` of a channel `E₁ → E₂`,
> giving a weight on `E₂`: the Schrödinger-picture pushforward of `w` along the channel.

```lean
noncomputable def comp (w : Weight E₁) (φ : Channel E₂ E₁) : Weight E₂
```

**`ProbabilisticTheory.Weight.comp_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean#L85).

```lean
lemma comp_apply (w : Weight E₁) (φ : Channel E₂ E₁) (y : PosCone E₂) :
    w.comp φ y = w ⟨φ (y : E₂), φ.map_nonneg y.2⟩
```

## B. Functoriality

**`ProbabilisticTheory.Weight.comp_id`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean#L91).

```lean
lemma comp_id (w : Weight E₁) : w.comp (.id ℝ E₁) = w
```

**`ProbabilisticTheory.Weight.comp_comp`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean#L95).

```lean
lemma comp_comp (w : Weight E₁) (φ : Channel E₂ E₁) (ψ : Channel E₃ E₂) :
    w.comp (φ.comp ψ) = (w.comp φ).comp ψ
```

## C. Preservation of finite weights and states

**`ProbabilisticTheory.Weight.IsFinite.comp`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean#L104).

> Pushing a finite weight forward along a channel's adjoint stays finite: `φ` never sends the
> cone anywhere `w` is infinite.

```lean
lemma IsFinite.comp {w : Weight E₁} (hw : w.IsFinite) (φ : Channel E₂ E₁) :
    (w.comp φ).IsFinite
```

**`ProbabilisticTheory.Weight.IsState.comp`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean#L114).

> Pushing a state forward along a channel's adjoint gives a state: finiteness survives
> (`IsFinite.comp`) and normalization survives because the adjoint is unital.

```lean
lemma IsState.comp {w : Weight F₁} (hw : w.IsState) (φ : Channel F₂ F₁) :
    (w.comp φ).IsState
```

## Depends on

- [Channels](basic.md)
- [Weights](../weight/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Weight.lean)
