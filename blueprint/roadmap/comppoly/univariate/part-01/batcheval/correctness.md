---
catalog: module
lean: CompPoly.CPolynomial.evalBatchHorner_eq_evalBatch, CompPoly.CPolynomial.evalBatchSubproduct_eq_evalBatch
statement: formalized
proof: formalized
---

# Batch Evaluation Correctness

`CompPoly.Univariate.BatchEval.Correctness`, in [CompPoly/Univariate/BatchEval/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Correctness.lean), by Valerii Huhnin.

> Correctness theorems for univariate batch-evaluation implementations.

`CompPoly.CPolynomial.evalBatchHorner_eq_evalBatch` (theorem, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Correctness.lean#L291))

> Batched Horner evaluation agrees with the direct batched evaluator.

```lean
theorem evalBatchHorner_eq_evalBatch [Semiring R] (p : CPolynomial R) (xs : Array R) :
    evalBatchHorner p xs = evalBatch p xs
```

`CompPoly.CPolynomial.evalBatchSubproduct_eq_evalBatch` (theorem, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Correctness.lean#L296))

> Subproduct-tree batch evaluation agrees with the direct batched evaluator.

```lean
theorem evalBatchSubproduct_eq_evalBatch [Field R] [BEq R] [LawfulBEq R]
    (M : MulContext R) (D : ModContext R) (p : CPolynomial R) (xs : Array R) :
    evalBatchSubproduct M D p xs = evalBatch p xs
```

## Depends on

- [Naive Batch Evaluation](naive.md)
- [Subproduct-Tree Batch Evaluation](subproducttree.md)

## Sources

- [CompPoly/Univariate/BatchEval/Correctness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Correctness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.BatchEval.Correctness.json)
