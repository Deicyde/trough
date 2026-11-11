---
declaration: theorem
origin: cited
lean: TauCeti.diagramSchurPoly_mul_alternant, TauCeti.schurPoly_mul_alternant
statement: formalized
proof: formalized
---

# Jacobi's bialternant formula

For a Young diagram `μ` with at most `N` rows, the Schur
polynomial `s_μ` in the alphabet `Fin N` times the Vandermonde alternant `a_δ`, `δ_j = N - 1 - j`,
is the alternant `a_{λ+δ}` of the row lengths `λ_j = μ.rowLen j` shifted by the staircase:
`s_μ · a_δ = a_{λ+δ}`.  This is the division-free form of `s_μ = a_{λ+δ} / a_δ`.

The row bound is necessary: for a taller shape `s_μ` vanishes, while the right-hand side, which
only sees the first `N` rows, need not.

```lean
TauCeti.diagramSchurPoly_mul_alternant.{u_1} {R : Type u_1} [CommRing R] (N : ℕ) (μ : YoungDiagram)
  (hμ : μ.colLen 0 ≤ N) :
  (TauCeti.diagramSchurPoly N R μ * TauCeti.alternant (Fin N) R fun j => N - 1 - ↑j) =
    TauCeti.alternant (Fin N) R fun j => μ.betaNumber N ↑j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.diagramSchurPoly_mul_alternant`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Bialternant.html#TauCeti.diagramSchurPoly_mul_alternant).

## Other forms

**Jacobi's bialternant formula for partitions.** Formalized in Tau Ceti as [`TauCeti.schurPoly_mul_alternant`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Bialternant.html#TauCeti.schurPoly_mul_alternant).

```lean
TauCeti.schurPoly_mul_alternant.{u_1, u_2} {R : Type u_1} [CommRing R] {σ : Type u_2} [Fintype σ]
  {n : ℕ} (μ : n.Partition) (hμ : (YoungDiagram.ofPartition μ).colLen 0 ≤ Fintype.card σ) :
  TauCeti.schurPoly σ R μ *
      (MvPolynomial.rename ⇑(Fintype.equivFin σ).symm)
        (TauCeti.alternant (Fin (Fintype.card σ)) R fun j => Fintype.card σ - 1 - ↑j) =
    (MvPolynomial.rename ⇑(Fintype.equivFin σ).symm)
      (TauCeti.alternant (Fin (Fintype.card σ)) R fun j =>
        (YoungDiagram.ofPartition μ).betaNumber (Fintype.card σ) ↑j)
```

## Sources

- [Tau Ceti documentation: `TauCeti.diagramSchurPoly_mul_alternant`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Bialternant.html#TauCeti.diagramSchurPoly_mul_alternant)
- [Source of `TauCeti.diagramSchurPoly_mul_alternant` in TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Bialternant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPolynomial/Symmetric/Schur/Bialternant.lean#L266)
