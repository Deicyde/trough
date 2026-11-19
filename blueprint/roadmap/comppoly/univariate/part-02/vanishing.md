---
catalog: module
lean: CompPoly.CPolynomial.vanishingPolynomialArray, CompPoly.CPolynomial.VanishingPolynomialContext, CompPoly.CPolynomial.VanishingPolynomialContext.direct, CompPoly.CPolynomial.VanishingPolynomialContext.subproduct, CompPoly.CPolynomial.eval_vanishingPolynomialArray_eq_zero_of_mem
statement: formalized
proof: formalized
---

# Vanishing Polynomials for Array Nodes

`CompPoly.Univariate.Vanishing`, in [CompPoly/Univariate/Vanishing.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Vanishing.lean), by Valerii Huhnin.

> Reusable executable construction of `∏ x in xs, (X - x)`.

`CompPoly.CPolynomial.vanishingPolynomialArray` (definition, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Vanishing.lean#L26))

> Direct folded vanishing polynomial `∏ x in xs, (X - x)`.

```lean
def vanishingPolynomialArray (xs : Array F) : CPolynomial F
```

`CompPoly.CPolynomial.VanishingPolynomialContext` (structure, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Vanishing.lean#L116))

> Operation dictionary for array vanishing-polynomial construction.

```lean
structure VanishingPolynomialContext
    (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  vanishingPolynomial : Array F → CPolynomial F
  correct :
    ∀ xs, vanishingPolynomial xs = CPolynomial.vanishingPolynomialArray xs
```

`CompPoly.CPolynomial.VanishingPolynomialContext.direct` (definition, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Vanishing.lean#L125))

> Direct folded vanishing-polynomial context.

```lean
def direct : VanishingPolynomialContext F
```

`CompPoly.CPolynomial.VanishingPolynomialContext.subproduct` (definition, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Vanishing.lean#L132))

> Subproduct-tree-backed vanishing-polynomial context.

```lean
def subproduct (M : CPolynomial.MulContext F) : VanishingPolynomialContext F
```

`CompPoly.CPolynomial.eval_vanishingPolynomialArray_eq_zero_of_mem` (theorem, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Vanishing.lean#L191))

> Every listed node is a root of the direct vanishing polynomial.

```lean
theorem eval_vanishingPolynomialArray_eq_zero_of_mem
    (xs : Array F) {x : F} (hx : x ∈ xs.toList) :
    CPolynomial.eval x (CPolynomial.vanishingPolynomialArray xs) = 0
```

## Depends on

- [Subproduct-Tree Batch Evaluation](../part-01/batcheval/subproducttree.md)

## Sources

- [CompPoly/Univariate/Vanishing.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Vanishing.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Vanishing.json)
