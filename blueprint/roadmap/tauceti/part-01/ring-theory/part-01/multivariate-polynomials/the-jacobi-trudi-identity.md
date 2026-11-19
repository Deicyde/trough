---
declaration: theorem
origin: cited
lean: TauCeti.diagramSchurPoly_eq_det_hsymmInt, TauCeti.SymmetricFunction.of_stableSchur_eq_det_hsymmInt, TauCeti.schurPoly_eq_det_hsymmInt, TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_hsymmInt
statement: formalized
proof: formalized
---

# The Jacobi--Trudi identity

The Schur polynomial of a Young diagram `μ` in the alphabet
`Fin N` is the determinant `det (h_{μᵢ - i + j})_{0 ≤ i, j < r}` of complete homogeneous symmetric
polynomials, for every `r` at least the number of rows of `μ`.  The index `μᵢ - i + j` is an
integer, and `h_m = 0` for `m < 0` (`TauCeti.hsymmInt`).

There is no condition relating `N` to `μ`: when `μ` has more than `N` rows, both sides vanish.

```lean
TauCeti.diagramSchurPoly_eq_det_hsymmInt.{u_1} {R : Type u_1} [CommRing R] (N : ℕ)
  (μ : YoungDiagram) {r : ℕ} (hr : μ.colLen 0 ≤ r) :
  TauCeti.diagramSchurPoly N R μ =
    (Matrix.of fun i j => TauCeti.hsymmInt (Fin N) R (↑(μ.rowLen ↑i) - ↑↑i + ↑↑j)).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's bialternant formula](jacobis-bialternant-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.diagramSchurPoly_eq_det_hsymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/JacobiTrudi.html#TauCeti.diagramSchurPoly_eq_det_hsymmInt).

## Other forms

**The Jacobi--Trudi identity in the symmetric functions.** Formalized in Tau Ceti as [`TauCeti.SymmetricFunction.of_stableSchur_eq_det_hsymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/JacobiTrudi.html#TauCeti.SymmetricFunction.of_stableSchur_eq_det_hsymmInt).

```lean
TauCeti.SymmetricFunction.of_stableSchur_eq_det_hsymmInt.{u_1} {R : Type u_1} [CommRing R] {n : ℕ}
  (μ : n.Partition) {r : ℕ} (hr : μ.parts.card ≤ r) :
  (DirectSum.of (fun n => ↥(TauCeti.stableSymmetricSubmodule R n)) n) (TauCeti.stableSchur R μ) =
    (Matrix.of fun i j =>
        TauCeti.SymmetricFunction.hsymmInt R
          (↑((YoungDiagram.ofPartition μ).rowLen ↑i) - ↑↑i + ↑↑j)).det
```

**The Jacobi--Trudi identity for partitions.** Formalized in Tau Ceti as [`TauCeti.schurPoly_eq_det_hsymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/JacobiTrudi.html#TauCeti.schurPoly_eq_det_hsymmInt).

```lean
TauCeti.schurPoly_eq_det_hsymmInt.{u_1, u_2} {R : Type u_1} [CommRing R] {σ : Type u_2} [Fintype σ]
  [DecidableEq σ] {n : ℕ} (μ : n.Partition) {r : ℕ} (hr : μ.parts.card ≤ r) :
  TauCeti.schurPoly σ R μ =
    (Matrix.of fun i j =>
        TauCeti.hsymmInt σ R (↑((YoungDiagram.ofPartition μ).rowLen ↑i) - ↑↑i + ↑↑j)).det
```

**The Jacobi--Trudi identity in `Λ_R`, for a Young diagram `μ`.** Formalized in Tau Ceti as [`TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_hsymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Stable/JacobiTrudi.html#TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_hsymmInt).

```lean
TauCeti.SymmetricFunction.of_stableSchur_shapePartition_eq_det_hsymmInt.{u_1} {R : Type u_1}
  [CommRing R] (μ : YoungDiagram) {r : ℕ} (hr : μ.colLen 0 ≤ r) :
  (DirectSum.of (fun n => ↥(TauCeti.stableSymmetricSubmodule R n)) μ.card)
      (TauCeti.stableSchur R (TauCeti.shapePartition μ)) =
    (Matrix.of fun i j => TauCeti.SymmetricFunction.hsymmInt R (↑(μ.rowLen ↑i) - ↑↑i + ↑↑j)).det
```

## Sources

- [Tau Ceti documentation: `TauCeti.diagramSchurPoly_eq_det_hsymmInt`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/JacobiTrudi.html#TauCeti.diagramSchurPoly_eq_det_hsymmInt)
- [Source of `TauCeti.diagramSchurPoly_eq_det_hsymmInt` in TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/JacobiTrudi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/JacobiTrudi.lean#L252)
