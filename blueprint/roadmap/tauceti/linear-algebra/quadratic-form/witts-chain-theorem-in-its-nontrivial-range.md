---
declaration: theorem
origin: cited
lean: TauCeti.diagonalChain_iff_equivalent
statement: formalized
proof: formalized
---

# Witt's chain theorem in its nontrivial range

two diagonal forms of rank at least two are
isometric if and only if their coefficient families are connected by a diagonal chain.

```lean
TauCeti.diagonalChain_iff_equivalent.{u} {K : Type u} [Field K] [Invertible 2] {n : ℕ}
  {w w' : Fin (n + 2) → Kˣ} :
  TauCeti.DiagonalChain w w' ↔
    (QuadraticMap.weightedSumSquares K fun i => ↑(w i)).Equivalent
      (QuadraticMap.weightedSumSquares K fun i => ↑(w' i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.diagonalChain_iff_equivalent`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Diagonal/WittChain.html#TauCeti.diagonalChain_iff_equivalent).

## Sources

- [Tau Ceti documentation: `TauCeti.diagonalChain_iff_equivalent`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Diagonal/WittChain.html#TauCeti.diagonalChain_iff_equivalent)
- [Source of `TauCeti.diagonalChain_iff_equivalent` in TauCeti/LinearAlgebra/QuadraticForm/Diagonal/WittChain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/QuadraticForm/Diagonal/WittChain.lean#L165)
