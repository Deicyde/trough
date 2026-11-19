---
declaration: module
origin: cited
lean: Channel.IsIntertwining, Channel.isIntertwining_id, Channel.IsIntertwining.comp, Channel.isIntertwining_transport, Channel.isIntertwining_iff_eq_transport
statement: formalized
proof: formalized
---

# Covariant channels

The module `Physlib.ProbabilisticTheory.Channel.Covariant`, [Physlib/ProbabilisticTheory/Channel/Covariant.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Covariant.lean): 5 declarations, 5 with a docstring.

> Channels that commute with two group actions by reversible transformations.

## i. Overview

> More general channels may lose information but can still respect the symmetries of a system. This
> is captured by covariance: a channel `Φ` between two spaces carrying group actions `ρ` and `σ` by
> reversible transformations is covariant, or intertwining, if
>
> `Φ ∘ ρ g = σ g ∘ Φ` for every group element `g`.
>
> A reversible transformation is covariant
> exactly when the target action is the transport of the source action. Together with the reversible
> transformations, this gives a common framework for symmetries and dynamics of observable spaces.

## ii. Key results

> - `Channel.IsIntertwining`: Covariance of a channel under two group actions.
> - `Channel.isIntertwining_iff_eq_transport`: Characterization of the transported action.

## iv. References

## A. Covariant channels

### A.1. Definition and closure properties

**`Channel.IsIntertwining`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L56).

> A channel intertwines two group actions if it commutes with their transformations.

```lean
def IsIntertwining (Φ : Channel P Q) (ρ : G →* Reversible P P)
    (σ : G →* Reversible Q Q) : Prop
```

**`Channel.isIntertwining_id`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L60).

> The identity channel intertwines a group action with itself.

```lean
lemma isIntertwining_id (ρ : G →* Reversible P P) : (Channel.id P).IsIntertwining ρ ρ
```

**`Channel.IsIntertwining.comp`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L65).

> The composition of intertwining channels also intertwines the group actions.

```lean
lemma IsIntertwining.comp {R : ProbabilisticTheory} {τ : G →* Reversible R R}
    {Φ : Channel P Q} {Ψ : Channel Q R} (hΦ : Φ.IsIntertwining ρ σ)
    (hΨ : Ψ.IsIntertwining σ τ) : (Ψ.comp Φ).IsIntertwining ρ τ
```

## B. Covariance of transport

**`Channel.isIntertwining_transport`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L74).

> A reversible transformation intertwines an action with its transport.

```lean
lemma isIntertwining_transport (ρ : G →* Reversible P P) (e : Reversible P Q) :
    e.toChannel.IsIntertwining ρ (e.transport ρ)
```

**`Channel.isIntertwining_iff_eq_transport`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L81).

> A reversible transformation intertwines two actions exactly when the target action
> is the transport of the source action.

```lean
lemma isIntertwining_iff_eq_transport (ρ : G →* Reversible P P)
    (σ : G →* Reversible Q Q) (e : Reversible P Q) :
    e.toChannel.IsIntertwining ρ σ ↔ σ = e.transport ρ
```

## Depends on

- [Reversible transformations of observables](reversible.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Covariant.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Channel/Covariant.lean)
