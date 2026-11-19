---
declaration: theorem
origin: cited
lean: Matrix.det_gram_matrix_smul
statement: formalized
proof: formalized
---

# The real Gram determinant under a change of family

For `w i = ∑ j, U i j • v j` in a real
inner product space, `det (gram ℝ w) = det U ^ 2 * det (gram ℝ v)`, with no independence or
dimension hypothesis.

```lean
Matrix.det_gram_matrix_smul.{u_1, u_4} {ι : Type u_1} [Fintype ι] [DecidableEq ι] {F : Type u_4}
  [SeminormedAddCommGroup F] [InnerProductSpace ℝ F] (U : Matrix ι ι ℝ) (v : ι → F) :
  (Matrix.gram ℝ fun i => ∑ j, U i j • v j).det = U.det ^ 2 * (Matrix.gram ℝ v).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.det_gram_matrix_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/ChangeOfFamily.html#Matrix.det_gram_matrix_smul).

## Sources

- [Tau Ceti documentation: `Matrix.det_gram_matrix_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/ChangeOfFamily.html#Matrix.det_gram_matrix_smul)
- [Source of `Matrix.det_gram_matrix_smul` in TauCeti/Analysis/InnerProductSpace/Gram/ChangeOfFamily.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Gram/ChangeOfFamily.lean#L79)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)
