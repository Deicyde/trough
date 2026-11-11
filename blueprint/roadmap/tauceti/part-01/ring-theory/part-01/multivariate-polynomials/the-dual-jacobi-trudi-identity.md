---
declaration: theorem
origin: cited
lean: TauCeti.diagramSchurPoly_eq_det_esymmInt, Nat.Partition.schurPoly_eq_det_esymmInt
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

**The dual Jacobi--Trudi identity for partitions.** Formalized in Tau Ceti as [`Nat.Partition.schurPoly_eq_det_esymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.html#Nat.Partition.schurPoly_eq_det_esymmInt).

```lean
Nat.Partition.schurPoly_eq_det_esymmInt.{u_1, u_2} {R : Type u_1} [CommRing R] {σ : Type u_2}
  [Fintype σ] {n : ℕ} (μ : n.Partition) {r : ℕ} (hr : (YoungDiagram.ofPartition μ).rowLen 0 ≤ r) :
  TauCeti.schurPoly σ R μ =
    (Matrix.of fun i j =>
        TauCeti.esymmInt σ R (↑((YoungDiagram.ofPartition μ).colLen ↑i) - ↑↑i + ↑↑j)).det
```

## Sources

- [Tau Ceti documentation: `TauCeti.diagramSchurPoly_eq_det_esymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.html#TauCeti.diagramSchurPoly_eq_det_esymmInt)
- [Source of `TauCeti.diagramSchurPoly_eq_det_esymmInt` in TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/DualJacobiTrudi.lean#L172)
