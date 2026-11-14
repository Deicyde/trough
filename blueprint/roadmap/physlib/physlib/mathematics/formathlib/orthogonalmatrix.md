---
declaration: module
origin: cited
lean: Matrix.dotProduct_mulVec_orthogonal
statement: formalized
proof: formalized
---

# Orthogonal matrices and the dot product

The module `Physlib.Mathematics.ForMathlib.OrthogonalMatrix`, [Physlib/Mathematics/ForMathlib/OrthogonalMatrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OrthogonalMatrix.lean): 1 declaration, 1 with a docstring.

> An orthogonal matrix — a square matrix `A` with `Aᵀ A = 1` — preserves the dot product of vectors,
> and in particular their squared lengths. This is the algebraic content behind the
> frame-independence of the *rotational* kinetic energy in rigid-body dynamics: rotating a velocity
> does not change its speed.

**`Matrix.dotProduct_mulVec_orthogonal`**, a lemma, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OrthogonalMatrix.lean#L26).

> An orthogonal matrix preserves the dot product: if `Aᵀ A = 1` then `(A v) ⬝ᵥ (A w) = v ⬝ᵥ w`.
> Taking `w = v` shows orthogonal matrices preserve squared lengths, `(A v) ⬝ᵥ (A v) = v ⬝ᵥ v`.

```lean
lemma dotProduct_mulVec_orthogonal {R : Type*} [CommRing R] {n : Type*} [Fintype n]
    [DecidableEq n] {A : Matrix n n R} (hA : Aᵀ * A = 1) (v w : n → R) :
    (A *ᵥ v) ⬝ᵥ (A *ᵥ w) = v ⬝ᵥ w
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/OrthogonalMatrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OrthogonalMatrix.lean)
