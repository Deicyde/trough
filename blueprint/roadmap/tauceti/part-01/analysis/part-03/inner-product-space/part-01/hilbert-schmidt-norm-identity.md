---
declaration: theorem
origin: cited
lean: HilbertBasis.hilbertSchmidtNorm_columnOperator
statement: formalized
proof: formalized
---

# Hilbert–Schmidt norm identity

The Hilbert–Schmidt norm of `T_f` is the `ℓ²` norm of
`f`.

```lean
HilbertBasis.hilbertSchmidtNorm_columnOperator.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} {ι : Type u_4} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F] (b : HilbertBasis ι 𝕜 E)
  [CompleteSpace E] (f : ↥(lp (fun x => F) 2)) : (b.columnOperator f).hilbertSchmidtNorm = ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy–Schwarz for the column series](cauchy-schwarz-for-the-column-series.md)
- [Parseval's identity for a functional](../part-02/parsevals-identity-for-a-functional.md)

## Lean

Formalized in Tau Ceti as [`HilbertBasis.hilbertSchmidtNorm_columnOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.html#HilbertBasis.hilbertSchmidtNorm_columnOperator).

## Sources

- [Tau Ceti documentation: `HilbertBasis.hilbertSchmidtNorm_columnOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.html#HilbertBasis.hilbertSchmidtNorm_columnOperator)
- [Source of `HilbertBasis.hilbertSchmidtNorm_columnOperator` in TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.lean#L246)
