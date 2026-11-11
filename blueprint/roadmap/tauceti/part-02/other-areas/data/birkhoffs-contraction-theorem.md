---
declaration: theorem
origin: cited
lean: Matrix.hilbertProjectiveDist_mulVec_le
statement: formalized
proof: formalized
---

# Birkhoff's contraction theorem

A matrix `K` with strictly positive entries contracts
Hilbert's projective metric between strictly positive vectors by the factor
`tanh (K.projectiveDiameter / 4)`, which is strictly less than `1`.

```lean
Matrix.hilbertProjectiveDist_mulVec_le.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Finite ι]
  [Fintype κ] {K : Matrix ι κ ℝ} (hK : ∀ (i : ι) (j : κ), 0 < K i j) {x y : κ → ℝ}
  (hx : ∀ (j : κ), 0 < x j) (hy : ∀ (j : κ), 0 < y j) :
  TauCeti.hilbertProjectiveDist (K.mulVec x) (K.mulVec y) ≤
    Real.tanh (K.projectiveDiameter / 4) * TauCeti.hilbertProjectiveDist x y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.hilbertProjectiveDist_mulVec_le`](https://taucetiproject.org/docs/TauCeti/Data/Matrix/BirkhoffContraction.html#Matrix.hilbertProjectiveDist_mulVec_le).

## Sources

- [Tau Ceti documentation: `Matrix.hilbertProjectiveDist_mulVec_le`](https://taucetiproject.org/docs/TauCeti/Data/Matrix/BirkhoffContraction.html#Matrix.hilbertProjectiveDist_mulVec_le)
- [Source of `Matrix.hilbertProjectiveDist_mulVec_le` in TauCeti/Data/Matrix/BirkhoffContraction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Data/Matrix/BirkhoffContraction.lean#L430)
