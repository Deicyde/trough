---
declaration: theorem
origin: cited
lean: TauCeti.diagramSchurPoly_eq_det_esymmInt, TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt, Nat.Partition.schurPoly_eq_det_esymmInt, TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_esymmInt, TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt_conjugate
statement: formalized
proof: formalized
---

# The dual Jacobi--Trudi identity

The Schur polynomial of a Young diagram `μ` in the
alphabet `Fin N` is the determinant `det (e_{μ'ᵢ - i + j})_{0 ≤ i, j < r}` of elementary symmetric
polynomials, where `μ'ᵢ` is the length of the `i`-th column, for every `r` at least the number of
columns of `μ`.  The index `μ'ᵢ - i + j` is an integer, and `e_m = 0` for `m < 0`
(`TauCeti.esymmInt`).

```lean
TauCeti.diagramSchurPoly_eq_det_esymmInt.{u_1} {R : Type u_1} [CommRing R] (N : ℕ)
  (μ : YoungDiagram) {r : ℕ} (hr : μ.rowLen 0 ≤ r) :
  TauCeti.diagramSchurPoly N R μ =
    (Matrix.of fun i j => TauCeti.esymmInt (Fin N) R (↑(μ.colLen ↑i) - ↑↑i + ↑↑j)).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's complementary-minor identity for the two Toeplitz matrices of symmetric polynomials](jacobis-complementary-minor-identity-for-the-two.md)
- [The Jacobi--Trudi identity](the-jacobi-trudi-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.diagramSchurPoly_eq_det_esymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.html#TauCeti.diagramSchurPoly_eq_det_esymmInt).

## Other forms

**The dual Jacobi--Trudi identity in the symmetric functions.** Formalized in Tau Ceti as [`TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/JacobiTrudi.html#TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt).

```lean
TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt.{u_1} {R : Type u_1} [CommRing R] {n : ℕ}
  (μ : n.Partition) {r : ℕ} (hr : (YoungDiagram.ofPartition μ).rowLen 0 ≤ r) :
  (DirectSum.of (fun n => ↥(TauCeti.stableSymmetricSubmodule R n)) n) (TauCeti.stableSchur R μ) =
    (Matrix.of fun i j =>
        TauCeti.SymmetricFunction.esymmInt R
          (↑((YoungDiagram.ofPartition μ).colLen ↑i) - ↑↑i + ↑↑j)).det
```

**The dual Jacobi--Trudi identity for partitions.** Formalized in Tau Ceti as [`Nat.Partition.schurPoly_eq_det_esymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.html#Nat.Partition.schurPoly_eq_det_esymmInt).

```lean
Nat.Partition.schurPoly_eq_det_esymmInt.{u_1, u_2} {R : Type u_1} [CommRing R] {σ : Type u_2}
  [Fintype σ] {n : ℕ} (μ : n.Partition) {r : ℕ} (hr : (YoungDiagram.ofPartition μ).rowLen 0 ≤ r) :
  TauCeti.schurPoly σ R μ =
    (Matrix.of fun i j =>
        TauCeti.esymmInt σ R (↑((YoungDiagram.ofPartition μ).colLen ↑i) - ↑↑i + ↑↑j)).det
```

**The dual Jacobi--Trudi identity in `Λ_R`, for a Young diagram `μ`.** Formalized in Tau Ceti as [`TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_esymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/JacobiTrudi.html#TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_esymmInt).

```lean
TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_esymmInt.{u_1} {R : Type u_1}
  [CommRing R] (μ : YoungDiagram) {r : ℕ} (hr : μ.rowLen 0 ≤ r) :
  (DirectSum.of (fun n => ↥(TauCeti.stableSymmetricSubmodule R n)) μ.card)
      (TauCeti.stableSchur R (TauCeti.shapePartition μ)) =
    (Matrix.of fun i j => TauCeti.SymmetricFunction.esymmInt R (↑(μ.colLen ↑i) - ↑↑i + ↑↑j)).det
```

**The dual Jacobi--Trudi identity in `Λ_R`, indexed by the parts of the conjugate partition.** Formalized in Tau Ceti as [`TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt_conjugate`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/JacobiTrudi.html#TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt_conjugate).

```lean
TauCeti.SymmetricFunction.of_stableSchur_eq_det_esymmInt_conjugate.{u_1} {R : Type u_1} [CommRing R]
  {n : ℕ} (μ : n.Partition) {r : ℕ} (hr : μ.conjugate.parts.card ≤ r) :
  (DirectSum.of (fun n => ↥(TauCeti.stableSymmetricSubmodule R n)) n) (TauCeti.stableSchur R μ) =
    (Matrix.of fun i j =>
        TauCeti.SymmetricFunction.esymmInt R
          (↑((YoungDiagram.ofPartition μ.conjugate).rowLen ↑i) - ↑↑i + ↑↑j)).det
```

## Sources

- [Tau Ceti documentation: `TauCeti.diagramSchurPoly_eq_det_esymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.html#TauCeti.diagramSchurPoly_eq_det_esymmInt)
- [Source of `TauCeti.diagramSchurPoly_eq_det_esymmInt` in TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.lean#L172)
