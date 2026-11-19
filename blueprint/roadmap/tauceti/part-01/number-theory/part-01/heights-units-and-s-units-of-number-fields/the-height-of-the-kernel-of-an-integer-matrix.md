---
declaration: theorem
origin: cited
lean: Matrix.minorGcd_mul_subspaceHeight_ker_mulVecLin
statement: formalized
proof: formalized
---

# The height of the kernel of an integer matrix

The greatest common divisor of the maximal
minors of an integer matrix `A`, times the absolute Euclidean height of the space of rational
solutions of `A y = 0`, is `√det (A Aᵀ)`. If the rows are linearly dependent, both sides
vanish.

```lean
Matrix.minorGcd_mul_subspaceHeight_ker_mulVecLin.{u_1} {ι : Type u_1} [Fintype ι] [LinearOrder ι]
  {p : ℕ} (A : Matrix (Fin p) ι ℤ) :
  ↑A.minorGcd * (A.map Int.cast).mulVecLin.ker.subspaceHeight = √↑(A * A.transpose).det
```

## Depends on

- [Matrix.minorGcd](matrix-minorgcd.md)

## Proof depends on

- [The Cauchy–Binet formula](../../../linear-algebra/part-02/other-results/the-cauchy-binet-formula.md)

## Lean

Formalized in Tau Ceti as [`Matrix.minorGcd_mul_subspaceHeight_ker_mulVecLin`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/IntMatrix.html#Matrix.minorGcd_mul_subspaceHeight_ker_mulVecLin).

## Sources

- [Tau Ceti documentation: `Matrix.minorGcd_mul_subspaceHeight_ker_mulVecLin`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/IntMatrix.html#Matrix.minorGcd_mul_subspaceHeight_ker_mulVecLin)
- [Source of `Matrix.minorGcd_mul_subspaceHeight_ker_mulVecLin` in TauCeti/NumberTheory/Height/Arakelov/IntMatrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Height/Arakelov/IntMatrix.lean#L94)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HeightsAndUnits/STATUS.md)
