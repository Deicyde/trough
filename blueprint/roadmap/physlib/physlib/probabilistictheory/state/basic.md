---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap.comap, UnitalPositiveLinearMap.comap_apply, Channel.comap, Channel.comap_apply
statement: formalized
proof: formalized
---

# States

The module `Physlib.ProbabilisticTheory.State.Basic`, [Physlib/ProbabilisticTheory/State/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Basic.lean): 4 declarations, 2 with a docstring.

## i. Overview

> A state assigns each observable its expectation value: a positive linear functional
> (`0 ≤ A ⟹ 0 ≤ ω A`), normalized so the certain outcome reads `ω 1 = 1`. In quantum mechanics,
> `ω A = tr(ρA)` for a density matrix `ρ`.

## ii. Key results

> - `𝓢[𝕜, A]` : states on an ordered `𝕜`-vector space with a distinguished unit.
> - `UnitalPositiveLinearMap.comap` : the state on the input of a channel that evaluates an
>   observable by first sending it through the channel.
> - `Channel.comap` : the same pullback of states along a channel between probabilistic theories.

## iv. References

## A. Notation for positive functionals and states

## B. Transporting states along channels

**`UnitalPositiveLinearMap.comap`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Basic.lean#L64).

> The state on `E` that evaluates an observable by first sending it through a channel `f` and
> then evaluating the state `ω` on the result.

```lean
def comap (f : E →ₚ₁[ℝ] F) (ω : 𝓢[ℝ, F]) : 𝓢[ℝ, E]
```

**`UnitalPositiveLinearMap.comap_apply`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Basic.lean#L69).

```lean
lemma comap_apply (f : E →ₚ₁[ℝ] F) (ω : 𝓢[ℝ, F]) (x : E) : comap f ω x = ω (f x)
```

**`Channel.comap`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Basic.lean#L78).

> Pull back a state by applying the channel before evaluating each observable.

```lean
def comap (f : Channel P Q) (ω : 𝓢[ℝ, Q.Observables]) : 𝓢[ℝ, P.Observables]
```

**`Channel.comap_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Basic.lean#L83).

```lean
lemma comap_apply (f : Channel P Q) (ω : 𝓢[ℝ, Q.Observables]) (x : P.Observables) :
    comap f ω x = ω (f x)
```

## Depends on

- [Positive unital maps](../channel/basic.md)
- [Ordered vector spaces and order units](../orderunit/basic.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Basic.lean)
