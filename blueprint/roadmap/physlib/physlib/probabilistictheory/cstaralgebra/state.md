---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.extend, ProbabilisticTheory.State.extend_apply, ProbabilisticTheory.State.extend_one, ProbabilisticTheory.State.extend_comap, ProbabilisticTheory.State.complexEquiv, ProbabilisticTheory.State.IsTracial, ProbabilisticTheory.State.isTracial_iff_extend_map_mul_comm, ProbabilisticTheory.State.IsTracial.map_mul_comm
statement: formalized
proof: formalized
---

# States of a C⋆-algebra

The module `Physlib.ProbabilisticTheory.CStarAlgebra.State`, [Physlib/ProbabilisticTheory/CStarAlgebra/State.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean): 11 declarations, 11 with a docstring.

> States inherit complex extension from channels and can be characterized by traciality.

## i. Overview

> A state assigns real expectation values to self-adjoint operators, the observables.
> Every operator has a decomposition into self-adjoint parts, its real and imaginary part.
> Applying states onto these two parts is a unique extension to a complex-linear map and vice versa.
> Therefore complex-linear maps are in bijection with their restriction to self-adjoint operators.
>
> A state is a channel into ℝ. The scalar identification
> `realEquivComplex` lets it inherit complex extension from the channel construction.
> A tracial state assigns the same expectation to the positive observables `a⋆a` and `aa⋆`.
> Equivalently its complex extension is cyclic on products.

## ii. Key results

> - `ProbabilisticTheory.State.extend` : complex expectation values on all operators.
> - `ProbabilisticTheory.State.complexEquiv` : states correspond to normalized positive
>   complex-linear functionals.
> - `ProbabilisticTheory.State.extend_comap` : extension respects state pullback.
> - `ProbabilisticTheory.State.IsTracial` : equality of expectations on `a⋆a` and `aa⋆`.
> - `ProbabilisticTheory.State.isTracial_iff_extend_map_mul_comm` : traciality is equivalent to
>   cyclicity of the complex extension.

## iv. References

## A. States on all operators

**`ProbabilisticTheory.State.extend`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L60).

> Extend the expectation values of observables to all operators.

```lean
noncomputable def extend (ω : (ofCStarAlgebra 𝒜).State) : 𝒜 →ₚ[ℂ] ℂ
```

**`ProbabilisticTheory.State.extend_apply`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L65).

> Extension preserves the expectation value of every observable.

```lean
lemma extend_apply (ω : (ofCStarAlgebra 𝒜).State) (A : selfAdjoint 𝒜) :
    ω.extend (A : 𝒜) = (ω A : ℂ)
```

**`ProbabilisticTheory.State.extend_one`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L71).

> The extended state is normalized.

```lean
lemma extend_one (ω : (ofCStarAlgebra 𝒜).State) : ω.extend 1 = 1
```

**`ProbabilisticTheory.State.extend_comap`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L75).

> Extending a pulled-back state agrees with composing the extensions.

```lean
lemma extend_comap (Φ : Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ))
    (ω : (ofCStarAlgebra ℬ).State) : (ω.comap Φ).extend = ω.extend.comp Φ.extend
```

**`ProbabilisticTheory.State.complexEquiv`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L81).

> States of a quantum system are the same as normalized positive functionals on all its
> operators.

```lean
noncomputable def complexEquiv (𝒜 : Type*) [CStarAlgebra 𝒜] [PartialOrder 𝒜]
    [StarOrderedRing 𝒜] : (ofCStarAlgebra 𝒜).State ≃ {f : 𝒜 →ₚ[ℂ] ℂ // f 1 = 1}
```

## B. Tracial states

**`ProbabilisticTheory.State.IsTracial`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L93).

> A state is tracial when `a⋆a` and `aa⋆` have the same expectation for every operator `a`.

```lean
def IsTracial (ω : (ofCStarAlgebra 𝒜).State) : Prop
```

**`ProbabilisticTheory.State.isTracial_iff_extend_map_mul_comm`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L97).

> A state is tracial exactly when its complex extension is cyclic on products.

```lean
lemma isTracial_iff_extend_map_mul_comm (ω : (ofCStarAlgebra 𝒜).State) :
    ω.IsTracial ↔ ∀ a b : 𝒜, ω.extend (a * b) = ω.extend (b * a)
```

**`ProbabilisticTheory.State.IsTracial.map_mul_comm`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L107).

> A tracial state does not see the order of a product.

```lean
lemma IsTracial.map_mul_comm {ω : (ofCStarAlgebra 𝒜).State} (h : ω.IsTracial) (a b : 𝒜) :
    ω.extend (a * b) = ω.extend (b * a)
```

**`ProbabilisticTheory.State.IsTracial.map_commutator`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L112).

> A tracial state vanishes on commutators.

```lean
lemma IsTracial.map_commutator {ω : (ofCStarAlgebra 𝒜).State} (h : ω.IsTracial) (a b : 𝒜) :
    ω.extend (a * b - b * a) = 0
```

**`ProbabilisticTheory.State.IsTracial.map_conj`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L117).

> A tracial state is invariant under the change of frame `x ↦ u * x * u⋆` by a unitary.

```lean
lemma IsTracial.map_conj {ω : (ofCStarAlgebra 𝒜).State} (h : ω.IsTracial) (u : unitary 𝒜)
    (x : 𝒜) : ω.extend (u * x * star (u : 𝒜)) = ω.extend x
```

**`ProbabilisticTheory.State.isTracial_iff_star_mul_self_eq_mul_star_self`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean#L122).

> A state is tracial if and only if `ω (a⋆ * a) = ω (a * a⋆)` for all `a`.

```lean
lemma isTracial_iff_star_mul_self_eq_mul_star_self (ω : (ofCStarAlgebra 𝒜).State) :
    ω.IsTracial ↔ ∀ a : 𝒜, ω.extend (star a * a) = ω.extend (a * star a)
```

## Depends on

- [Channels of C⋆-algebras](channel.md)
- [States](../state/basic.md)

## Proof depends on

- [Tracial functionals](traciality.md)

## Sources

- [Physlib/ProbabilisticTheory/CStarAlgebra/State.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/CStarAlgebra/State.lean)
