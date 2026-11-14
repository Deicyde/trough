---
declaration: module
origin: cited
lean: Matrix.star_scalar, Matrix.map_scalar, Matrix.scalar_smul, Matrix.scalar_eq_conj, Matrix.scalarSelfAdjoint, Matrix.scalarSelfAdjoint_apply, Matrix.eq_scalar_fin_one
statement: formalized
proof: formalized
---

# Scalar matrices

The module `PhyslibAlpha.Mathematics.ForMathlib.DataStructures.Matrix.Scalar`, [PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean): 7 declarations, 6 with a docstring.

## i. Overview

> Lemmas on the scalar matrices `Matrix.scalar n x` of a commutative `*`-ring: they commute
> with the conjugate transpose, with entrywise maps fixing zero and with scalar actions; they
> are fixed by conjugation with a unitary scalar; and a self-adjoint element gives a scalar
> matrix real-linearly. A `1 × 1` matrix is the scalar matrix of its entry.

## ii. Key results

> - `Matrix.star_scalar`, `Matrix.map_scalar`, `Matrix.scalar_smul` : compatibilities.
> - `Matrix.scalar_eq_conj` : conjugation by a unitary scalar fixes a scalar matrix.
> - `Matrix.scalarSelfAdjoint` : self-adjoint elements as scalar matrices.
> - `Matrix.eq_scalar_fin_one` : a `1 × 1` matrix is scalar.

## iv. References

> * None.

## A. Scalar matrices

**`Matrix.star_scalar`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean#L50).

> The conjugate transpose of a scalar matrix is the scalar matrix of the star.

```lean
lemma star_scalar [StarRing R] (x : R) : star (scalar n x) = scalar n (star x)
```

**`Matrix.map_scalar`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean#L55).

> An entrywise map fixing zero sends a scalar matrix to a scalar matrix.

```lean
lemma map_scalar {S : Type*} [CommRing S] (f : R → S) (hf : f 0 = 0) (x : R) :
    (scalar n x).map f = scalar n (f x)
```

**`Matrix.scalar_smul`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean#L60).

> A scalar action passes into a scalar matrix.

```lean
lemma scalar_smul {M : Type*} [Monoid M] [DistribMulAction M R] (c : M) (x : R) :
    scalar n (c • x) = c • scalar n x
```

**`Matrix.scalar_eq_conj`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean#L66).

> Conjugation by a unitary scalar fixes a scalar matrix.

```lean
lemma scalar_eq_conj [StarRing R] {u : R} (hu : u * star u = 1) (x : R) :
    scalar n x = scalar n u * scalar n x * star (scalar n u)
```

**`Matrix.scalarSelfAdjoint`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean#L71).

> A self-adjoint element as a scalar matrix, real-linearly.

```lean
noncomputable def scalarSelfAdjoint [StarRing R] [Algebra ℝ R] [StarModule ℝ R] :
    ↥(selfAdjoint R) →ₗ[ℝ] Matrix n n R
```

**`Matrix.scalarSelfAdjoint_apply`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean#L78).

```lean
lemma scalarSelfAdjoint_apply [StarRing R] [Algebra ℝ R] [StarModule ℝ R]
    (a : ↥(selfAdjoint R)) : (scalarSelfAdjoint (n := n)) a = scalar n a.1
```

**`Matrix.eq_scalar_fin_one`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean#L82).

> A `1 × 1` matrix is the scalar matrix of its entry.

```lean
lemma eq_scalar_fin_one (A : Matrix (Fin 1) (Fin 1) R) : A = scalar (Fin 1) (A 0 0)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/Scalar.lean)
