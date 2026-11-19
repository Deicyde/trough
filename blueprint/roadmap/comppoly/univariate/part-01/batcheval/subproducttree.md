---
catalog: module
lean: CompPoly.CPolynomial.SubproductTree, CompPoly.CPolynomial.SubproductTree.poly, CompPoly.CPolynomial.SubproductTree.leafFor, CompPoly.CPolynomial.SubproductTree.combine, CompPoly.CPolynomial.SubproductTree.combinePairs, CompPoly.CPolynomial.SubproductTree.buildFromTrees, CompPoly.CPolynomial.SubproductTree.buildList, CompPoly.CPolynomial.SubproductTree.buildArray, CompPoly.CPolynomial.SubproductTree.evalList, CompPoly.CPolynomial.evalBatchSubproduct
statement: formalized
proof: formalized
---

# Subproduct-Tree Batch Evaluation

`CompPoly.Univariate.BatchEval.SubproductTree`, in [CompPoly/Univariate/BatchEval/SubproductTree.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean), by Valerii Huhnin.

> Executable subproduct-tree construction and descent for univariate batch
> evaluation.

`CompPoly.CPolynomial.SubproductTree` (inductive type, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L26))

> A subproduct tree stores the product polynomial at every node.

```lean
inductive SubproductTree (R : Type*) [Zero R] where
  /-- A leaf for one evaluation point. The polynomial is `X - C x`. -/
  | leaf (x : R) (poly : CPolynomial R)
  /-- An internal node stores the product of its children. -/
  | node (poly : CPolynomial R) (left right : SubproductTree R)
```

`CompPoly.CPolynomial.SubproductTree.poly` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L35))

> The product polynomial stored at the root of a subproduct tree.

```lean
def poly [Zero R] : SubproductTree R → CPolynomial R
```

`CompPoly.CPolynomial.SubproductTree.leafFor` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L40))

> Build a leaf for one evaluation point.

```lean
def leafFor [Field R] [BEq R] [LawfulBEq R] (x : R) : SubproductTree R
```

`CompPoly.CPolynomial.SubproductTree.combine` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L44))

> Combine two neighboring trees using the selected multiplication backend.

```lean
def combine [Field R] [BEq R] [LawfulBEq R] (M : MulContext R)
    (left right : SubproductTree R) : SubproductTree R
```

`CompPoly.CPolynomial.SubproductTree.combinePairs` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L49))

> Pair adjacent trees into the next subproduct-tree level.

```lean
def combinePairs [Field R] [BEq R] [LawfulBEq R] (M : MulContext R) :
    List (SubproductTree R) → List (SubproductTree R)
```

`CompPoly.CPolynomial.SubproductTree.buildFromTrees` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L56))

> Repeatedly combine tree levels, bounded by fuel for straightforward termination.

```lean
def buildFromTrees [Field R] [BEq R] [LawfulBEq R] (M : MulContext R) :
    Nat → List (SubproductTree R) → Option (SubproductTree R)
```

`CompPoly.CPolynomial.SubproductTree.buildList` (definition, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L65))

> Build a subproduct tree from an ordered list of evaluation points.

```lean
def buildList [Field R] [BEq R] [LawfulBEq R] (M : MulContext R)
    (xs : List R) : Option (SubproductTree R)
```

`CompPoly.CPolynomial.SubproductTree.buildArray` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L71))

> Build a subproduct tree from an ordered array of evaluation points.

```lean
def buildArray [Field R] [BEq R] [LawfulBEq R] (M : MulContext R)
    (xs : Array R) : Option (SubproductTree R)
```

`CompPoly.CPolynomial.SubproductTree.evalList` (definition, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L76))

> Descend a subproduct tree with remainders and return values in leaf order.

```lean
def evalList [Field R] [BEq R] [LawfulBEq R] (D : ModContext R)
    (p : CPolynomial R) : SubproductTree R → List R
```

`CompPoly.CPolynomial.evalBatchSubproduct` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean#L88))

> Evaluate a polynomial at many points using a subproduct tree.

```lean
def evalBatchSubproduct [Field R] [BEq R] [LawfulBEq R]
    (M : MulContext R) (D : ModContext R) (p : CPolynomial R) (xs : Array R) : Array R
```

## Depends on

- [Univariate Algorithm Contexts](../context.md)

## Sources

- [CompPoly/Univariate/BatchEval/SubproductTree.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/BatchEval/SubproductTree.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.BatchEval.SubproductTree.json)
