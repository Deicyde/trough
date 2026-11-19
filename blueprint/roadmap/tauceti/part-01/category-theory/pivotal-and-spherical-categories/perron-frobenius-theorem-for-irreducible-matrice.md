---
declaration: theorem
origin: cited
lean: Matrix.IsIrreducible.exists_mulVec_eq_smul, Matrix.exists_mulVec_eq_smul_of_nonneg, Matrix.exists_mulVec_eq_smul_of_pos
statement: formalized
proof: formalized
---

# Perron–Frobenius theorem for irreducible matrices, existence

an irreducible real square
matrix has an eigenvector whose entries are all strictly positive, for a strictly positive
eigenvalue.

When `n` is nonempty, this eigenvalue is the spectral radius
(`Matrix.spectralRadius_eq_of_mulVec_eq_smul`), its eigenspace is spanned by the eigenvector
(`Matrix.IsIrreducible.exists_eq_smul_of_mulVec_eq_smul`), and it is a simple root of the
characteristic polynomial (`Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one`).  For empty `n`
the statement holds trivially, with the zero vector.

```lean
Matrix.IsIrreducible.exists_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  (hA : A.IsIrreducible) : ∃ r, 0 < r ∧ ∃ v, (∀ (i : n), 0 < v i) ∧ A.mulVec v = r • v
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Collatz–Wielandt bound](collatz-wielandt-bound.md)

## Lean

Formalized in Tau Ceti as [`Matrix.IsIrreducible.exists_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.html#Matrix.IsIrreducible.exists_mulVec_eq_smul).

## Other forms

**Perron–Frobenius theorem for nonnegative matrices.** Formalized in Tau Ceti as [`Matrix.exists_mulVec_eq_smul_of_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Nonnegative.html#Matrix.exists_mulVec_eq_smul_of_nonneg).

```lean
Matrix.exists_mulVec_eq_smul_of_nonneg.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  [Nonempty n] (hA : ∀ (i j : n), 0 ≤ A i j) :
  ∃ r,
    0 ≤ r ∧
      spectralRadius ℂ (A.map Complex.ofReal) = ENNReal.ofReal r ∧
        ∃ v, 0 ≤ v ∧ v ≠ 0 ∧ A.mulVec v = r • v
```

**Perron–Frobenius theorem for positive matrices, existence.** Formalized in Tau Ceti as [`Matrix.exists_mulVec_eq_smul_of_pos`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.html#Matrix.exists_mulVec_eq_smul_of_pos).

```lean
Matrix.exists_mulVec_eq_smul_of_pos.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  (hA : ∀ (i j : n), 0 < A i j) : ∃ r, 0 < r ∧ ∃ v, (∀ (i : n), 0 < v i) ∧ A.mulVec v = r • v
```

## Sources

- [Tau Ceti documentation: `Matrix.IsIrreducible.exists_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.html#Matrix.IsIrreducible.exists_mulVec_eq_smul)
- [Source of `Matrix.IsIrreducible.exists_mulVec_eq_smul` in TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.lean#L149)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
