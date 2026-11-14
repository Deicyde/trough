---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsIntertwining, ProbabilisticTheory.isIntertwining_id, ProbabilisticTheory.IsIntertwining.comp, ProbabilisticTheory.IsIntertwining.comap_isInvariant, ProbabilisticTheory.Reversible.isIntertwining_transport, ProbabilisticTheory.Reversible.isIntertwining_iff_eq_transport
statement: formalized
proof: formalized
---

# Covariant channels

The module `Physlib.ProbabilisticTheory.Channel.Covariant`, [Physlib/ProbabilisticTheory/Channel/Covariant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean): 6 declarations, 6 with a docstring.

> Channels that commute with two group actions by reversible transformations.

## i. Overview

> More general channels may lose information but can still respect the symmetries of a system. This
> is captured by covariance: a channel `Φ` between two spaces carrying group actions `ρ` and `σ` by
> reversible transformations is covariant, or intertwining, if
>
> `Φ ∘ ρ g = σ g ∘ Φ` for every group element `g`.
>
> Covariance preserves invariant states under pullback. A reversible transformation is covariant
> exactly when the target action is the transport of the source action. Together with the reversible
> transformations, this gives a common framework for symmetries and dynamics of observable spaces.

## ii. Key results

> - `IsIntertwining`: Covariance of a channel under two group actions.
> - `IsIntertwining.comap_isInvariant`: Pullback of invariant states along covariant channels.
> - `Reversible.isIntertwining_iff_eq_transport`: Characterization of the transported action.

## iv. References

## A. Covariant channels

### A.1. Definition and closure properties

**`ProbabilisticTheory.IsIntertwining`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L56).

> A channel intertwines two group actions if it commutes with their transformations.

```lean
def IsIntertwining (Φ : Channel P Q) : Prop
```

**`ProbabilisticTheory.isIntertwining_id`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L59).

> The identity channel intertwines a group action with itself.

```lean
lemma isIntertwining_id : IsIntertwining ρ ρ (Channel.id P)
```

**`ProbabilisticTheory.IsIntertwining.comp`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L68).

> The composition of intertwining channels also intertwines the group actions.

```lean
lemma comp {R : ProbabilisticTheory} {τ : G →* Reversible R R}
    {Φ : Channel P Q} {Ψ : Channel Q R} (hΦ : IsIntertwining ρ σ Φ)
    (hΨ : IsIntertwining σ τ Ψ) : IsIntertwining ρ τ (Ψ.comp Φ)
```

### A.2. Invariant states

**`ProbabilisticTheory.IsIntertwining.comap_isInvariant`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L77).

> Pulling back an invariant state along an intertwining channel preserves invariance.

```lean
lemma comap_isInvariant {Φ : Channel P Q} (h : IsIntertwining ρ σ Φ)
    {ω : 𝓢[ℝ, Q.Observables]} (hω : IsInvariant σ ω) :
    IsInvariant ρ (Channel.comap Φ ω)
```

## B. Covariance of transport

**`ProbabilisticTheory.Reversible.isIntertwining_transport`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L98).

> A reversible transformation intertwines an action with its transport.

```lean
lemma isIntertwining_transport :
    IsIntertwining ρ (e.transport ρ) e.toChannel
```

**`ProbabilisticTheory.Reversible.isIntertwining_iff_eq_transport`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean#L105).

> A reversible transformation intertwines two actions exactly when the target action
> is the transport of the source action.

```lean
lemma isIntertwining_iff_eq_transport :
    IsIntertwining ρ σ e.toChannel ↔ σ = e.transport ρ
```

## Depends on

- [Reversible transformations of observables](reversible.md)

## Sources

- [Physlib/ProbabilisticTheory/Channel/Covariant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Channel/Covariant.lean)
