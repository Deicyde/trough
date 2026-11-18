---
declaration: def
origin: cited
lean: Matrix.confluentVandermonde
statement: formalized
---

# Matrix.confluentVandermonde

The Hasse confluent Vandermonde matrix: rows indexed by `Fin (∑ i, m i)` in the lexicographic
order `finSigmaFinEquiv ⟨i, k⟩` of the jets `(i, k)`, `k < m i`, columns by the monomials `X ^ j`
in increasing degree, entry `(hasseDeriv k (X ^ j)).eval (a i)`.

```lean
Matrix.confluentVandermonde.{u_1} {R : Type u_1} [CommRing R] {r : ℕ} (a : Fin r → R)
  (m : Fin r → ℕ) : Matrix (Fin (∑ i, m i)) (Fin (∑ i, m i)) R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.confluentVandermonde`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.html#Matrix.confluentVandermonde).

## Sources

- [Tau Ceti documentation: `Matrix.confluentVandermonde`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.html#Matrix.confluentVandermonde)
- [Source of `Matrix.confluentVandermonde` in TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/ConfluentVandermonde.lean#L74)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)
