---
declaration: module
origin: cited
lean: Channel.complexExtension, Channel.complexExtension_apply, Channel.complexExtension_coe, Channel.complexExtension_unique, Channel.extend, Channel.extend_apply, Channel.extend_one, Channel.ofComplex
statement: formalized
proof: formalized
---

# Channels of C⋆-algebras

The module `Physlib.ProbabilisticTheory.CStarAlgebra.Channel`, [Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean): 13 declarations, 12 with a docstring.

> Channels between the self-adjoint parts of C⋆-algebras extend uniquely to all operators.

## i. Overview

> A channel acts on self-adjoint observables. Every operator decomposes into self-adjoint
> real and imaginary parts, so a channel extends uniquely to a complex-linear map on all
> operators. This extension is positive and preserves the identity. Restricting a unital positive
> complex-linear map to observables recovers a channel.

## ii. Key results

> - `Channel.complexExtension` : extend a real-linear map on self-adjoint elements.
> - `Channel.complexExtension_unique` : uniqueness of the complex-linear extension.
> - `Channel.extend` : a channel extended to all operators.
> - `Channel.ofComplex` : a unital positive map restricted to a channel.
> - `Channel.complexEquiv` : channels are the same as unital positive maps between all operators.
> - `Channel.extend_comp` : extension respects composition.

## iv. References

## A. Complex extension

### A.1. The extension

**`Channel.complexExtension`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L64).

> The complex-linear extension of a real-linear map on self-adjoint operators to all
> operators: `a ↦ φ (ℜ a) + i φ (ℑ a)`.

```lean
noncomputable def complexExtension (φ : selfAdjoint A →ₗ[ℝ] B) : A →ₗ[ℂ] B
```

**`Channel.complexExtension_apply`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L77).

```lean
lemma complexExtension_apply (φ : selfAdjoint A →ₗ[ℝ] B) (a : A) :
    complexExtension φ a = φ (ℜ a) + Complex.I • φ (ℑ a)
```

### A.2. Agreement and uniqueness

**`Channel.complexExtension_coe`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L88).

> On self-adjoint operators the extension is the original map.

```lean
lemma complexExtension_coe (φ : selfAdjoint A →ₗ[ℝ] B) (a : selfAdjoint A) :
    complexExtension φ (a : A) = φ a
```

**`Channel.complexExtension_unique`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L93).

> A complex-linear map is determined by its values on self-adjoint operators.

```lean
lemma complexExtension_unique (φ : selfAdjoint A →ₗ[ℝ] B) (f : A →ₗ[ℂ] B)
    (h : ∀ a : selfAdjoint A, f a = φ a) : f = complexExtension φ
```

## B. Channels on all operators

**`Channel.extend`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L108).

> Extend a channel between observables to a positive map between all operators.

```lean
noncomputable def extend (Φ : Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ)) : 𝒜 →ₚ[ℂ] ℬ
```

**`Channel.extend_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L117).

> Extension agrees with the channel on every observable.

```lean
lemma extend_apply (Φ : Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ)) (A : selfAdjoint 𝒜) :
    Φ.extend (A : 𝒜) = (Φ A : ℬ)
```

**`Channel.extend_one`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L123).

> The extended channel preserves the identity.

```lean
lemma extend_one (Φ : Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ)) : Φ.extend 1 = 1
```

**`Channel.ofComplex`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L127).

> A unital positive map between all operators restricts to a channel between observables.

```lean
noncomputable def ofComplex (f : 𝒜 →ₚ[ℂ] ℬ) (h : f 1 = 1) :
    Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ)
```

**`Channel.coe_ofComplex_apply`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L137).

> The restricted channel acts as the original map.

```lean
lemma coe_ofComplex_apply (f : 𝒜 →ₚ[ℂ] ℬ) (h : f 1 = 1) (x : selfAdjoint 𝒜) :
    (ofComplex f h x : ℬ) = f x
```

**`Channel.ofComplex_extend`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L142).

> Restricting an extended channel recovers the original channel.

```lean
lemma ofComplex_extend (Φ : Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ)) :
    ofComplex Φ.extend Φ.extend_one = Φ
```

**`Channel.extend_ofComplex`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L148).

> A unital positive map is determined by its restriction to observables.

```lean
lemma extend_ofComplex (f : 𝒜 →ₚ[ℂ] ℬ) (h : f 1 = 1) : (ofComplex f h).extend = f
```

**`Channel.complexEquiv`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L154).

> Channels between two systems are the same as unital positive maps between all their
> operators.

```lean
noncomputable def complexEquiv :
    Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ) ≃ {f : 𝒜 →ₚ[ℂ] ℬ // f 1 = 1}
```

**`Channel.extend_comp`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean#L162).

> Extending a composite channel agrees with composing the extensions.

```lean
lemma extend_comp (Ψ : Channel (ofCStarAlgebra ℬ) (ofCStarAlgebra 𝒞))
    (Φ : Channel (ofCStarAlgebra 𝒜) (ofCStarAlgebra ℬ)) :
    (Ψ.comp Φ).extend = Ψ.extend.comp Φ.extend
```

## Depends on

- [The observables of a C⋆-algebra (Physlib)](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Channel.lean)
