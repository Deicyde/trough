---
catalog: module
lean: CompPoly.CPolynomial.BatchEvalContext, CompPoly.CPolynomial.BatchEvalContext.horner, CompPoly.CPolynomial.BatchEvalContext.subproduct
statement: formalized
proof: formalized
---

# Batch-Evaluation Contexts

`CompPoly.Univariate.BatchEval.Context`, in [CompPoly/Univariate/BatchEval/Context.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/Context.lean), by Valerii Huhnin.

> Explicit context wrappers for reusable univariate batch-evaluation backends.

`CompPoly.CPolynomial.BatchEvalContext` (structure, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/Context.lean#L23))

> Contract wrapper for batch evaluation backends.

```lean
structure BatchEvalContext (R : Type*) [Semiring R] where
  evalBatchWith : CPolynomial R → Array R → Array R
  correct : ∀ p xs, evalBatchWith p xs = CPolynomial.evalBatch p xs
```

`CompPoly.CPolynomial.BatchEvalContext.horner` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/Context.lean#L30))

> Horner-backed batch evaluation context.

```lean
def horner (R : Type*) [Semiring R] : BatchEvalContext R
```

`CompPoly.CPolynomial.BatchEvalContext.subproduct` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/Context.lean#L37))

> Subproduct-tree-backed batch evaluation context.

```lean
def subproduct (R : Type*) [Field R] [BEq R] [LawfulBEq R]
    (M : CPolynomial.MulContext R) (D : CPolynomial.ModContext R) :
    BatchEvalContext R
```

## Depends on

- [Naive Batch Evaluation](naive.md)
- [Subproduct-Tree Batch Evaluation](subproducttree.md)

## Proof depends on

- [Batch Evaluation Correctness](correctness.md)

## Sources

- [CompPoly/Univariate/BatchEval/Context.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/Context.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.BatchEval.Context.json)
