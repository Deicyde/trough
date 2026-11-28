---
catalog: module
lean: CompPoly.CPolynomial.evalBatch, CompPoly.CPolynomial.evalBatchHorner
statement: formalized
proof: formalized
---

# Naive Batch Evaluation

`CompPoly.Univariate.BatchEval.Naive`, in [CompPoly/Univariate/BatchEval/Naive.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Naive.lean), by Valerii Huhnin.

> Specification-level batch evaluators for canonical univariate polynomials.

`CompPoly.CPolynomial.evalBatch` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Naive.lean#L24))

> Evaluate a polynomial at every point using the direct sum-of-powers evaluator.

```lean
def evalBatch [Semiring R] (p : CPolynomial R) (xs : Array R) : Array R
```

`CompPoly.CPolynomial.evalBatchHorner` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Naive.lean#L29))

> Evaluate a polynomial at every point using Horner evaluation.

```lean
def evalBatchHorner [Semiring R] (p : CPolynomial R) (xs : Array R) : Array R
```

## Depends on

- [Computable Univariate Polynomials](../basic.md)

## Sources

- [CompPoly/Univariate/BatchEval/Naive.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Naive.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.BatchEval.Naive.json)
