---
declaration: module
origin: cited
lean: TensorProduct.map_derivation_left, TensorProduct.map_derivation_right
statement: formalized
proof: formalized
---

# Derivations of one factor of a tensor product of algebras

The module `PhyslibAlpha.Mathematics.ForMathlib.RingTheory.TensorProduct.Derivation`, [PhyslibAlpha/Mathematics/ForMathlib/RingTheory/TensorProduct/Derivation.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/RingTheory/TensorProduct/Derivation.lean): 2 declarations, 2 with a docstring.

> A derivation of one factor of a tensor product of algebras extends to the tensor product.

## i. Overview

> A linear map `D` of an algebra `A` satisfying the Leibniz rule
> `D (x * y) = D x * y + x * D y` extends to the tensor product `A ⊗[R] B` as `D ⊗ id`, and the
> extension satisfies the Leibniz rule again. On pure tensors this is the Leibniz rule of `D`
> in the first factor, the second factor being carried along, and the general case follows by
> additivity. The same holds for a derivation of the right factor, extended as `id ⊗ D`.

## ii. Key results

> - `TensorProduct.map_derivation_left` : a derivation of the left factor extends to a
>   derivation of the tensor product.
> - `TensorProduct.map_derivation_right` : a derivation of the right factor extends to a
>   derivation of the tensor product.

## iv. References

> * None.

## A. Derivations of one factor

**`TensorProduct.map_derivation_left`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/RingTheory/TensorProduct/Derivation.lean#L50).

> A derivation of the left factor extends to a derivation of the tensor product.

```lean
lemma map_derivation_left {R A B : Type*} [CommRing R] [Ring A] [Algebra R A]
    [Ring B] [Algebra R B] (D : A →ₗ[R] A)
    (hD : ∀ x y, D (x * y) = D x * y + x * D y) (x y : A ⊗[R] B) :
    TensorProduct.map D LinearMap.id (x * y)
      = TensorProduct.map D LinearMap.id x * y
        + x * TensorProduct.map D LinearMap.id y
```

**`TensorProduct.map_derivation_right`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/RingTheory/TensorProduct/Derivation.lean#L72).

> A derivation of the right factor extends to a derivation of the tensor product.

```lean
lemma map_derivation_right {R A B : Type*} [CommRing R] [Ring A] [Algebra R A]
    [Ring B] [Algebra R B] (D : B →ₗ[R] B)
    (hD : ∀ x y, D (x * y) = D x * y + x * D y) (x y : A ⊗[R] B) :
    TensorProduct.map LinearMap.id D (x * y)
      = TensorProduct.map LinearMap.id D x * y
        + x * TensorProduct.map LinearMap.id D y
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/RingTheory/TensorProduct/Derivation.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/RingTheory/TensorProduct/Derivation.lean)
