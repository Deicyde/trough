---
declaration: module
origin: cited
lean: TauCeti.positiveDefiniteKernelOperator, TauCeti.positiveDefiniteKernelOperator_apply, TauCeti.posSemidef_positiveDefiniteKernelOperator, Matrix.PosSemidef.KolmogorovSpace, Matrix.PosSemidef.kolmogorovFeature, Matrix.PosSemidef.inner_kolmogorovFeature, Matrix.PosSemidef.norm_kolmogorovFeature_sq, Matrix.PosSemidef.norm_kolmogorovFeature_sub_sq
statement: formalized
proof: formalized
---

# Kolmogorov decomposition of a positive-definite kernel

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Kernel.Kolmogorov`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean): 15 declarations, 14 with a docstring; 1 private, not shown.

> This file constructs the canonical Hilbert-space realization of a scalar-valued positive-definite
> kernel.

## i. Overview

> This file constructs the canonical Hilbert-space realization of a scalar-valued
> positive-definite kernel.  A kernel `K : α → α → 𝕜` is first regarded as the operator-valued
> kernel whose `(a, b)` entry is multiplication by `K a b` on the one-dimensional Hilbert space
> `𝕜`.  Mathlib's `RKHS.OfKernel` construction then gives a Hilbert space and kernel vectors
> `Φ a` satisfying
>
> `⟪Φ a, Φ b⟫_𝕜 = K a b`.
>
> The span of the kernel vectors is dense, so this is the minimal Kolmogorov decomposition rather
> than an arbitrary realization.  Its universal property gives a unique linear isometry into any
> other realization, and a linear isometric equivalence when that realization is also minimal.
>
> The completion and reproducing-kernel construction are Mathlib's `RKHS.OfKernel`; this file
> supplies the scalar-kernel bridge and its characteristic API.

## ii. Key results

> * `TauCeti.positiveDefiniteKernelOperator`: regard a scalar kernel as an operator-valued kernel.
> * `TauCeti.posSemidef_positiveDefiniteKernelOperator`: positivity of that
>   operator kernel.
> * `Matrix.PosSemidef.KolmogorovSpace`: the canonical Hilbert space.
> * `Matrix.PosSemidef.kolmogorovFeature`: its canonical feature map.
> * `Matrix.PosSemidef.inner_kolmogorovFeature`: the Kolmogorov identity.
> * `Matrix.PosSemidef.kolmogorovFeature_dense`: minimality of the decomposition.
> * `Matrix.PosSemidef.kolmogorovIsometry`: the universal comparison isometry.
> * `Matrix.PosSemidef.kolmogorovEquiv`: equivalence with any other minimal
>   realization.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups*,
>   Springer GTM 100 (1984), Chapter 3.

## A. Development

**`TauCeti.positiveDefiniteKernelOperator`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L73).

> A scalar kernel regarded as an operator-valued kernel on the one-dimensional Hilbert space
> `𝕜`: the entry at `(a, b)` is left multiplication by `K a b`.

```lean
noncomputable def positiveDefiniteKernelOperator (K : α → α → 𝕜) :
    Matrix α α (𝕜 →L[𝕜] 𝕜)
```

**`TauCeti.positiveDefiniteKernelOperator_apply`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L78).

```lean
lemma positiveDefiniteKernelOperator_apply (K : α → α → 𝕜) (a b : α) (z : 𝕜) :
    positiveDefiniteKernelOperator K a b z = K a b * z
```

**`TauCeti.posSemidef_positiveDefiniteKernelOperator`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L88).

> The operator-valued kernel obtained from a scalar positive-definite kernel is positive
> semidefinite.  This is the bridge needed by Mathlib's `RKHS.OfKernel` construction.

```lean
lemma posSemidef_positiveDefiniteKernelOperator (hK : Matrix.PosSemidef K) :
    (positiveDefiniteKernelOperator K).PosSemidef
```

**`Matrix.PosSemidef.KolmogorovSpace`**, an abbrev, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L135).

> The canonical Hilbert space in the Kolmogorov decomposition of `K`.
>
> This is an abbreviation because Mathlib's `RKHS.OfKernel` currently has to be an abbreviation in
> order for its normed-group and inner-product instances to reduce.

```lean
noncomputable abbrev KolmogorovSpace (hK : Matrix.PosSemidef K)
```

**`Matrix.PosSemidef.kolmogorovFeature`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L142).

> The canonical feature map into the Kolmogorov space.  It sends `a` to the reproducing-kernel
> vector at `a`, evaluated on the scalar `1`.

```lean
noncomputable def kolmogorovFeature (hK : Matrix.PosSemidef K) (a : α) :
    KolmogorovSpace hK
```

**`Matrix.PosSemidef.inner_kolmogorovFeature`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L151).

> **Kolmogorov identity.** Inner products of the canonical feature vectors recover the
> original kernel.

```lean
lemma inner_kolmogorovFeature (hK : Matrix.PosSemidef K) (a b : α) :
    ⟪kolmogorovFeature hK a, kolmogorovFeature hK b⟫_𝕜 = K a b
```

**`Matrix.PosSemidef.norm_kolmogorovFeature_sq`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L165).

> The squared norm of a canonical feature vector is the real part of the corresponding
> diagonal kernel value.

```lean
lemma norm_kolmogorovFeature_sq (hK : Matrix.PosSemidef K) (a : α) :
    ‖kolmogorovFeature hK a‖ ^ 2 = RCLike.re (K a a)
```

**`Matrix.PosSemidef.norm_kolmogorovFeature_sub_sq`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L172).

> The squared distance between two canonical feature vectors, expressed entirely in terms of
> the original kernel.

```lean
lemma norm_kolmogorovFeature_sub_sq (hK : Matrix.PosSemidef K) (a b : α) :
    ‖kolmogorovFeature hK a - kolmogorovFeature hK b‖ ^ 2 =
      RCLike.re (K a a) - 2 * RCLike.re (K a b) + RCLike.re (K b b)
```

**`Matrix.PosSemidef.kolmogorovFeature_dense`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L180).

> The canonical feature vectors have dense linear span in the Kolmogorov space.  Thus the
> construction is minimal: it contains no orthogonal summand invisible to the kernel.

```lean
lemma kolmogorovFeature_dense (hK : Matrix.PosSemidef K) :
    (Submodule.span 𝕜 (Set.range (kolmogorovFeature hK))).topologicalClosure = ⊤
```

**`Matrix.PosSemidef.kolmogorovIsometry`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L218).

> The unique linear isometry from the canonical Kolmogorov space into any Hilbert-space
> realization of `K`.  It sends each canonical feature vector to the corresponding vector in the
> given realization.

```lean
noncomputable def kolmogorovIsometry {E : Type w} [NormedAddCommGroup E]
    [InnerProductSpace 𝕜 E] [CompleteSpace E] (hK : Matrix.PosSemidef K) (φ : α → E)
    (hφ : ∀ a b, ⟪φ a, φ b⟫_𝕜 = K a b) : KolmogorovSpace hK →ₗᵢ[𝕜] E
```

**`Matrix.PosSemidef.kolmogorovIsometry_apply`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L241).

> The universal comparison isometry sends canonical feature vectors to the vectors of the
> given realization.

```lean
lemma kolmogorovIsometry_apply {E : Type w} [NormedAddCommGroup E]
    [InnerProductSpace 𝕜 E] [CompleteSpace E] (hK : Matrix.PosSemidef K) (φ : α → E)
    (hφ : ∀ a b, ⟪φ a, φ b⟫_𝕜 = K a b) (a : α) :
    kolmogorovIsometry hK φ hφ (kolmogorovFeature hK a) = φ a
```

**`Matrix.PosSemidef.kolmogorovIsometry_unique`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L259).

> A linear isometry out of the canonical Kolmogorov space is uniquely determined by its values
> on the canonical feature vectors.

```lean
lemma kolmogorovIsometry_unique {E : Type w} [NormedAddCommGroup E]
    [InnerProductSpace 𝕜 E] [CompleteSpace E] (hK : Matrix.PosSemidef K) (φ : α → E)
    (hφ : ∀ a b, ⟪φ a, φ b⟫_𝕜 = K a b) (T : KolmogorovSpace hK →ₗᵢ[𝕜] E)
    (hT : ∀ a, T (kolmogorovFeature hK a) = φ a) : T = kolmogorovIsometry hK φ hφ
```

**`Matrix.PosSemidef.kolmogorovIsometry_surjective`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L272).

> If the vectors in a realization of `K` have dense linear span, the universal comparison
> isometry is surjective.

```lean
lemma kolmogorovIsometry_surjective {E : Type w} [NormedAddCommGroup E]
    [InnerProductSpace 𝕜 E] [CompleteSpace E] (hK : Matrix.PosSemidef K) (φ : α → E)
    (hφ : ∀ a b, ⟪φ a, φ b⟫_𝕜 = K a b)
    (hφdense : (Submodule.span 𝕜 (Set.range φ)).topologicalClosure = ⊤) :
    Function.Surjective (kolmogorovIsometry hK φ hφ)
```

**`Matrix.PosSemidef.kolmogorovEquiv`**, a def, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L288).

> The canonical Kolmogorov space is linearly isometric to every other minimal realization of
> the same kernel.

```lean
noncomputable def kolmogorovEquiv {E : Type w} [NormedAddCommGroup E]
    [InnerProductSpace 𝕜 E] [CompleteSpace E] (hK : Matrix.PosSemidef K) (φ : α → E)
    (hφ : ∀ a b, ⟪φ a, φ b⟫_𝕜 = K a b)
    (hφdense : (Submodule.span 𝕜 (Set.range φ)).topologicalClosure = ⊤) :
    KolmogorovSpace hK ≃ₗᵢ[𝕜] E
```

**`Matrix.PosSemidef.kolmogorovEquiv_apply`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean#L299).

> The equivalence with another minimal realization sends canonical feature vectors to the
> vectors of that realization.

```lean
lemma kolmogorovEquiv_apply {E : Type w} [NormedAddCommGroup E]
    [InnerProductSpace 𝕜 E] [CompleteSpace E] (hK : Matrix.PosSemidef K) (φ : α → E)
    (hφ : ∀ a b, ⟪φ a, φ b⟫_𝕜 = K a b)
    (hφdense : (Submodule.span 𝕜 (Set.range φ)).topologicalClosure = ⊤) (a : α) :
    kolmogorovEquiv hK φ hφ hφdense (kolmogorovFeature hK a) = φ a
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Comparing linear combinations by their Gram kernels](../part-01/analysis-innerproductspace-linearcombination.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Kernel/Kolmogorov.lean)
