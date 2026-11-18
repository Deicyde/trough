---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.normalize, ProbabilisticTheory.UnitalPositiveLinearMap.normalize_apply, ProbabilisticTheory.UnitalPositiveLinearMap.toPositiveLinearMap_apply, ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.apply_eq_of_le_of_pos, ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.apply_eq_of_le, ProbabilisticTheory.UnitalPositiveLinearMap.weighted, ProbabilisticTheory.UnitalPositiveLinearMap.weighted_apply, ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.apply_eq_of_le_weighted
statement: formalized
proof: formalized
---

# Pure states

The module `PhyslibAlpha.ProbabilisticTheory.Classical.PureState`, [PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean): 16 declarations, 11 with a docstring.

> Pure states, the functionals below them, and the space of pure states.

## i. Overview

> A pure state is a state of maximal knowledge. It cannot be prepared by mixing two different states.
> In quantum mechanics the pure states are the vector states. In classical mechanics they are the
> points of phase space.
>
> Mixing shows up in the order of positive functionals. A weighted state below a pure state is a
> fraction of that same pure state. Two different pure states have nothing in common: only zero lies
> below weighted copies of both.
>
> The pure states form a space, `PureState E`, on which all other states are decomposed. They see
> every observable: by the Krein–Milman theorem, an observable with nonnegative expectation value in
> every pure state is nonnegative.

## ii. Key results

> - `UnitalPositiveLinearMap.IsPure.apply_eq_of_le` proves that a positive functional below a pure
>   state is a multiple of it.
> - `UnitalPositiveLinearMap.eq_zero_of_le_weighted` proves that only zero lies below weighted copies
>   of two different pure states.
> - `PureState E` is the space of pure states.
> - `PureState.nonneg_of_forall_pure` proves that an observable nonnegative in every pure state is
>   nonnegative.
> - `PureState.evalPure_le_iff` proves that observables are ordered by their values on pure states.

## iv. References

> * None.

## A. Functionals below a pure state

**`ProbabilisticTheory.UnitalPositiveLinearMap.normalize`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L77).

> The state `φ / φ 1` of a positive functional with `φ 1 > 0`.

```lean
noncomputable def normalize (φ : E →ₚ[ℝ] ℝ) (h : 0 < φ 1) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.normalize_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L82).

```lean
lemma normalize_apply (φ : E →ₚ[ℝ] ℝ) (h : 0 < φ 1) (f : E) :
    normalize φ h f = (φ 1)⁻¹ * φ f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.toPositiveLinearMap_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L85).

```lean
lemma toPositiveLinearMap_apply (ω : 𝓢[ℝ, E]) (f : E) :
    ω.toPositiveLinearMap f = ω f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.apply_eq_of_le_of_pos`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L89).

> A positive functional below a pure state `ω` with `0 < φ 1 < 1` is `φ 1` times `ω`.

```lean
lemma IsPure.apply_eq_of_le_of_pos {ω : 𝓢[ℝ, E]} (hω : ω.IsPure) {φ : E →ₚ[ℝ] ℝ}
    (hφ : φ ≤ ω.toPositiveLinearMap) (h0 : 0 < φ 1) (h1 : φ 1 < 1) (f : E) :
    φ f = φ 1 * ω f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.apply_eq_of_le`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L105).

> A pure state dominates only multiples of itself.

```lean
lemma IsPure.apply_eq_of_le {ω : 𝓢[ℝ, E]} (hω : ω.IsPure) {φ : E →ₚ[ℝ] ℝ}
    (hφ : φ ≤ ω.toPositiveLinearMap) (f : E) : φ f = φ 1 * ω f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.weighted`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L120).

> The state `ω` with weight `c`, as a positive functional.

```lean
def weighted (ω : 𝓢[ℝ, E]) (c : ℝ≥0) : E →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.weighted_apply`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L123).

```lean
lemma weighted_apply (ω : 𝓢[ℝ, E]) (c : ℝ≥0) (f : E) : ω.weighted c f = c * ω f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.apply_eq_of_le_weighted`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L126).

> A positive functional below a weighted pure state is a multiple of that state.

```lean
lemma IsPure.apply_eq_of_le_weighted {ω : 𝓢[ℝ, E]} (hω : ω.IsPure) {γ : E →ₚ[ℝ] ℝ} {c : ℝ≥0}
    (h : γ ≤ ω.weighted c) (f : E) : γ f = γ 1 * ω f
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.eq_zero_of_le_weighted`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L145).

> A positive functional below weighted copies of two distinct pure states vanishes.

```lean
lemma eq_zero_of_le_weighted {ω₁ ω₂ : 𝓢[ℝ, E]} (h₁ : ω₁.IsPure) (h₂ : ω₂.IsPure) (hne : ω₁ ≠ ω₂)
    {γ : E →ₚ[ℝ] ℝ} {c₁ c₂ : ℝ≥0} (hγ₁ : γ ≤ ω₁.weighted c₁) (hγ₂ : γ ≤ ω₂.weighted c₂) :
    γ = 0
```

**`ProbabilisticTheory.StateSpace.exists_apply_eq_apply`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L158).

> Two distinct states take any two prescribed values on a common observable.

```lean
lemma StateSpace.exists_apply_eq_apply {E : Type*} [ArchimedeanOrderUnitSpace E]
    {x y : stateSpace E} (p q : ℝ) (h : x = y → p = q) :
    ∃ a : E, toState x a = p ∧ toState y a = q
```

## B. The space of pure states

**`ProbabilisticTheory.PureState`**, an abbrev, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L184).

> The pure states, with the weak-star topology.

```lean
abbrev PureState : Type _
```

**`ProbabilisticTheory.PureState.evalPure`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L191).

> An observable as the continuous function of its values on the pure states.

```lean
noncomputable def evalPure : E →ₗ[ℝ] C(PureState E, ℝ)
```

**`ProbabilisticTheory.PureState.evalPure_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L197).

```lean
lemma evalPure_apply (f : E) (ω : PureState E) : evalPure f ω = toState ω.1 f
```

**`ProbabilisticTheory.PureState.evalPure_one`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L199).

```lean
lemma evalPure_one : evalPure (1 : E) = 1
```

**`ProbabilisticTheory.PureState.nonneg_of_forall_pure`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L202).

> **Krein–Milman**: an observable nonnegative in every pure state is nonnegative.

```lean
lemma nonneg_of_forall_pure {f : E} (h : ∀ ω : PureState E, 0 ≤ toState ω.1 f) : 0 ≤ f
```

**`ProbabilisticTheory.PureState.evalPure_le_iff`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean#L215).

> Pure states determine the order.

```lean
lemma evalPure_le_iff {f g : E} : evalPure f ≤ evalPure g ↔ f ≤ g
```

## Depends on

- [Positive functionals](../../mathematics/part-02/order/positivedual-basic.md)
- [The unit of an order-unit space as an order unit](../orderunit/positivedual.md)
- [The state space](../state/statespace.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/PureState.lean)
