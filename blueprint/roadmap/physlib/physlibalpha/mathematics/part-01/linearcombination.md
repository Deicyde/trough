---
declaration: module
origin: cited
lean: Submodule.map_span_range, Fintype.sum_sum_mul_smul, LinearMap.map_sum_smul_of_forall_eq, LinearMap.map_sum_smul_eq_sum_mulVec_smul, Fintype.exists_invariant_coeff_of_adjoint_mem, Fintype.exists_mulVec_eq_of_conjTranspose_mem, LinearMap.range_eq_span_range_basis, Submodule.mul_le_of_le_span_range
statement: formalized
proof: formalized
---

# Finite linear combinations under a linear map

The module `PhyslibAlpha.Mathematics.LinearCombination`, [PhyslibAlpha/Mathematics/LinearCombination.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean): 9 declarations, 9 with a docstring.

## i. Overview

> A family `T : ι → B` of vectors of an `R`-module spans Mathlib's
> `Submodule.span R (Set.range T)`. The index type is arbitrary and may be empty. When it is
> finite, the elements of the span are exactly the combinations `∑ i, c i • T i`, for
> coefficients `c : ι → R` that need not be unique (`Submodule.mem_span_range_iff_exists_fun`).
> The one fact added here is that a linear map carries this span to the span of the images of
> the family (`Submodule.map_span_range`).
>
> Two bookkeeping identities about these combinations: contracting
> against coefficients moved by a matrix regroups as the same combination of the matrix-moved
> components, and a linear map given on the family by a matrix moves a combination by that matrix
> acting on the coefficients.
>
> Over `ℂ`, when linear maps on `B` move combinations by moving their coefficients, a combination
> fixed by all the maps is the combination of fixed coefficients, provided the coefficient maps
> have their adjoints among themselves: `Fintype.exists_invariant_coeff_of_adjoint_mem`. When the
> coefficient maps are matrices, the condition is that the conjugate transpose of each matrix is
> again one of them: `Fintype.exists_mulVec_eq_of_conjTranspose_mem`.
>
> Spans are bounded through their members: the range of a linear map is the span of the images
> of a basis, and a product of submodules lying in spans of families lies in any submodule
> containing the products of their members.

## ii. Key results

> - `Submodule.map_span_range` : the image of the span of a family is the span of the images
> - `Fintype.exists_invariant_coeff_of_adjoint_mem` : a vector of the span of `T` fixed by every `φ g`
>   is the combination of coefficients fixed by every `A g`, where `φ g` moves combinations by moving
>   their coefficients with `A g`
> - `Fintype.exists_mulVec_eq_of_conjTranspose_mem`

## iv. References

> * None.

## A. The image of the span of a family

**`Submodule.map_span_range`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L66).

> The image of the span of a family is the span of the images.

```lean
lemma Submodule.map_span_range {R B B' : Type*} [Semiring R] [AddCommMonoid B] [Module R B]
    [AddCommMonoid B'] [Module R B'] {ι : Sort*} (f : B →ₗ[R] B') (T : ι → B) :
    (Submodule.span R (Set.range T)).map f = Submodule.span R (Set.range fun i => f (T i))
```

## B. Combinations moved by linear maps

**`Fintype.sum_sum_mul_smul`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L82).

> Contracting the components against coefficients moved by a matrix is the original
> combination of the matrix-moved components.

```lean
lemma Fintype.sum_sum_mul_smul (M : ι → κ → R) (c : κ → R) (T : ι → B) :
    ∑ a, (∑ d, c d * M a d) • T a = ∑ d, c d • ∑ a, M a d • T a
```

**`LinearMap.map_sum_smul_of_forall_eq`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L89).

> A linear map that moves each component of a family by a matrix moves a combination of the
> components by that matrix acting on the coefficients, with the free index first.

```lean
lemma LinearMap.map_sum_smul_of_forall_eq (φ : B →ₗ[R] B') (T : ι → B) (T' : κ → B')
    (M : κ → ι → R) (hT : ∀ l, φ (T l) = ∑ a, M a l • T' a) (c : ι → R) :
    φ (∑ l, c l • T l) = ∑ a, (∑ l, c l * M a l) • T' a
```

**`LinearMap.map_sum_smul_eq_sum_mulVec_smul`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L99).

> The matrix form of `LinearMap.map_sum_smul_of_forall_eq`: a linear map moving `T l` to
> `∑ a, M a l • T' a` moves the combination with coefficients `c` to the combination with
> coefficients `M *ᵥ c`.

```lean
lemma LinearMap.map_sum_smul_eq_sum_mulVec_smul (φ : B →ₗ[R] B') (T : ι → B) (T' : κ → B')
    (M : Matrix κ ι R) (hT : ∀ l, φ (T l) = ∑ a, M a l • T' a) (c : ι → R) :
    φ (∑ l, c l • T l) = ∑ a, (M *ᵥ c) a • T' a
```

## C. Fixed vectors of the span

**`Fintype.exists_invariant_coeff_of_adjoint_mem`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L120).

> A vector of the span of `T` fixed by every `φ g` is the combination of coefficients fixed
> by every `A g`, where `φ g` moves combinations by moving their coefficients with `A g`. The
> one condition on `A` is that for every `g` some `g'` acts as the adjoint of `g` for the
> standard inner product on coefficients; neither the `φ g` nor the `A g` need form a
> representation, and `B` carries no inner product. The components may be dependent, so the
> coefficients need not be unique: the proof takes the part of any coefficients orthogonal to
> those contracting to `0`.

```lean
lemma Fintype.exists_invariant_coeff_of_adjoint_mem {ι G B : Type*} [Fintype ι]
    [AddCommGroup B] [Module ℂ B] (T : ι → B) (φ : G → B →ₗ[ℂ] B)
    (A : G → (ι → ℂ) →ₗ[ℂ] (ι → ℂ))
    (hφ : ∀ (g : G) (c : ι → ℂ), φ g (∑ i, c i • T i) = ∑ i, A g c i • T i)
    (hA : ∀ g : G, ∃ g' : G, ∀ u v : EuclideanSpace ℂ ι,
      ⟪u, WithLp.toLp 2 (A g v.ofLp)⟫_ℂ = ⟪WithLp.toLp 2 (A g' u.ofLp), v⟫_ℂ)
    {x : B} (hx : x ∈ Submodule.span ℂ (Set.range T)) (hinv : ∀ g, φ g x = x) :
    ∃ c : ι → ℂ, x = ∑ i, c i • T i ∧ ∀ g, A g c = c
```

**`Fintype.exists_mulVec_eq_of_conjTranspose_mem`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L160).

> The matrix form of `Fintype.exists_invariant_coeff_of_adjoint_mem`: when each `φ g` moves
> the family by a matrix `M g`, and the conjugate transpose of each `M g` is some `M g'`, a
> vector of the span fixed by every `φ g` is the combination of a coefficient vector fixed by
> every `M g`.

```lean
lemma Fintype.exists_mulVec_eq_of_conjTranspose_mem {ι G B : Type*} [Fintype ι]
    [AddCommGroup B] [Module ℂ B] (T : ι → B) (φ : G → B →ₗ[ℂ] B) (M : G → Matrix ι ι ℂ)
    (hT : ∀ g l, φ g (T l) = ∑ a, M g a l • T a) (hM : ∀ g, ∃ g', M g' = (M g)ᴴ)
    {x : B} (hx : x ∈ Submodule.span ℂ (Set.range T)) (hinv : ∀ g, φ g x = x) :
    ∃ c : ι → ℂ, x = ∑ i, c i • T i ∧ ∀ g, M g *ᵥ c = c
```

## D. Spans bounded through their members

**`LinearMap.range_eq_span_range_basis`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L182).

> The range of a linear map is the span of the images of a basis.

```lean
lemma LinearMap.range_eq_span_range_basis {ι R M N : Type*} [Semiring R] [AddCommMonoid M]
    [Module R M] [AddCommMonoid N] [Module R N] (b : Module.Basis ι R M) (f : M →ₗ[R] N) :
    LinearMap.range f = Submodule.span R (Set.range fun i => f (b i))
```

**`Submodule.mul_le_of_le_span_range`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L189).

> A product of two submodules, each inside the span of a family, lies in any submodule
> containing the products of the members of the two families.

```lean
lemma Submodule.mul_le_of_le_span_range {ι κ R A : Type*} [CommSemiring R] [Semiring A]
    [Algebra R A] {V V' X : Submodule R A} {a : ι → A} {b : κ → A}
    (hV : V ≤ Submodule.span R (Set.range a)) (hV' : V' ≤ Submodule.span R (Set.range b))
    (hX : ∀ i j, a i * b j ∈ X) : V * V' ≤ X
```

**`Submodule.mul_mul_le_of_le_span_range`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean#L199).

> The three-factor form of `Submodule.mul_le_of_le_span_range`.

```lean
lemma Submodule.mul_mul_le_of_le_span_range {ι κ ν R A : Type*} [CommSemiring R] [Semiring A]
    [Algebra R A] {V V' V'' X : Submodule R A} {a : ι → A} {b : κ → A} {c : ν → A}
    (hV : V ≤ Submodule.span R (Set.range a)) (hV' : V' ≤ Submodule.span R (Set.range b))
    (hV'' : V'' ≤ Submodule.span R (Set.range c)) (hX : ∀ i j k, a i * (b j * c k) ∈ X) :
    V * (V' * V'') ≤ X
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/LinearCombination.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LinearCombination.lean)
