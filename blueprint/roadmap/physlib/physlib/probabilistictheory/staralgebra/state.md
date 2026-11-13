---
declaration: module
origin: cited
lean: Observable, UnitalPositiveLinearMap.IsTracial, UnitalPositiveLinearMap.IsTracial.map_mul_comm, UnitalPositiveLinearMap.IsTracial.map_commutator, UnitalPositiveLinearMap.IsTracial.map_conj, UnitalPositiveLinearMap.isTracial_iff_star_mul_self_eq_mul_star_self, UnitalPositiveLinearMap.onObservables, UnitalPositiveLinearMap.coe_onObservables_apply
statement: formalized
proof: formalized
---

# Observables and states of a star algebra

The module `Physlib.ProbabilisticTheory.StarAlgebra.State`, [Physlib/ProbabilisticTheory/StarAlgebra/State.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean): 10 declarations, 10 with a docstring.

> A positive map sends observables to observables. A state gives observables real expectation
> values. A tracial state does not see the order of a product.

## i. Overview

> The observables of a quantum system are the self-adjoint operators of its algebra. A state gives
> every operator a complex expectation value.
>
> A state is tracial if the expectation value of a product does not depend on the order of the
> factors: `ω (a b) = ω (b a)`. Then `ω` vanishes on every commutator. A tracial state gives the
> same expectation value after a change of frame by a unitary `u`: `ω (u x u⋆) = ω x`.
>
> A state has a real expectation value on every observable. Its real part is a state of the
> observables.
>
> A positive map sends the operators of one system to operators of another. It sends observables to
> observables. A unital positive map restricts to a channel between the observables.

## ii. Key results

> - `Observable` : the self-adjoint elements, such as Hermitian operators.
> - `UnitalPositiveLinearMap.IsTracial` : a tracial state.
> - `UnitalPositiveLinearMap.IsTracial.map_commutator` : a tracial state vanishes on commutators.
> - `UnitalPositiveLinearMap.IsTracial.map_conj` : a tracial state is invariant under
>   `x ↦ u * x * u⋆` for a unitary `u`.
> - `UnitalPositiveLinearMap.isTracial_iff_star_mul_self_eq_mul_star_self` : `ω` is tracial if and
>   only if `ω (a⋆ * a) = ω (a * a⋆)` for all `a`.
> - `UnitalPositiveLinearMap.onObservables` : a state restricted to a state of the observables.
> - `UnitalPositiveLinearMap.coe_onObservables_apply` : the expectation value of an observable is
>   real.
> - `UnitalPositiveLinearMap.restrictObservables` : a unital positive map restricted to a channel
>   between observables.

## iv. References

## A. Observables and tracial states

**`Observable`**, an abbrev, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L71).

> An observable: a self-adjoint element, such as a Hermitian operator.

```lean
abbrev Observable (𝒜 : Type*) [AddGroup 𝒜] [StarAddMonoid 𝒜]
```

**`UnitalPositiveLinearMap.IsTracial`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L78).

> A state `ω` is tracial if `ω (a * b) = ω (b * a)` for all `a` and `b`.

```lean
def IsTracial (ω : 𝓢[ℂ, 𝒜]) : Prop
```

**`UnitalPositiveLinearMap.IsTracial.map_mul_comm`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L82).

> A tracial state does not see the order of a product.

```lean
lemma IsTracial.map_mul_comm {ω : 𝓢[ℂ, 𝒜]} (h : ω.IsTracial) (a b : 𝒜) :
    ω (a * b) = ω (b * a)
```

**`UnitalPositiveLinearMap.IsTracial.map_commutator`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L87).

> A tracial state vanishes on commutators.

```lean
lemma IsTracial.map_commutator {ω : 𝓢[ℂ, 𝒜]} (h : ω.IsTracial) (a b : 𝒜) :
    ω (a * b - b * a) = 0
```

**`UnitalPositiveLinearMap.IsTracial.map_conj`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L94).

> A tracial state is invariant under the change of frame `x ↦ u * x * u⋆` by a unitary.

```lean
lemma IsTracial.map_conj {ω : 𝓢[ℂ, 𝒜]} (h : ω.IsTracial) (u : unitary 𝒜) (x : 𝒜) :
    ω (u * x * star (u : 𝒜)) = ω x
```

**`UnitalPositiveLinearMap.isTracial_iff_star_mul_self_eq_mul_star_self`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L105).

> A state is tracial if and only if `ω (a⋆ * a) = ω (a * a⋆)` for all `a`.

```lean
lemma isTracial_iff_star_mul_self_eq_mul_star_self (ω : 𝓢[ℂ, 𝒜]) :
    ω.IsTracial ↔ ∀ a : 𝒜, ω (star a * a) = ω (a * star a)
```

## B. States of observables

**`UnitalPositiveLinearMap.onObservables`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L121).

> The real part of a state is a state of the observables. Its value is the expectation value
> (`coe_onObservables_apply`).

```lean
noncomputable def onObservables (ω : 𝓢[ℂ, 𝒜]) : 𝓢[ℝ, Observable 𝒜]
```

**`UnitalPositiveLinearMap.coe_onObservables_apply`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L130).

> The expectation value of an observable is real. It equals its real part.

```lean
lemma coe_onObservables_apply (ω : 𝓢[ℂ, 𝒜]) (x : Observable 𝒜) :
    ((ω.onObservables x : ℝ) : ℂ) = ω (x : 𝒜)
```

## C. Channels between observables

**`UnitalPositiveLinearMap.restrictObservables`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L144).

> A unital positive map restricts to a channel between observables.

```lean
noncomputable def restrictObservables (f : 𝒜 →ₚ₁[ℂ] ℬ) : Observable 𝒜 →ₚ₁[ℝ] Observable ℬ
```

**`UnitalPositiveLinearMap.coe_restrictObservables_apply`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean#L153).

> The restricted channel acts as the original map.

```lean
lemma coe_restrictObservables_apply (f : 𝒜 →ₚ₁[ℂ] ℬ) (x : Observable 𝒜) :
    (f.restrictObservables x : ℬ) = f x
```

## Depends on

- [Positive unital maps](../channel/basic.md)
- [Tracial functionals](traciality.md)

## Sources

- [Physlib/ProbabilisticTheory/StarAlgebra/State.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/State.lean)
