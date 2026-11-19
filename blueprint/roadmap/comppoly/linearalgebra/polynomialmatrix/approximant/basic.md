---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.XAdicProblem, CompPoly.PolynomialMatrix.Approximant.maxOrder, CompPoly.PolynomialMatrix.Approximant.totalOrder, CompPoly.PolynomialMatrix.Approximant.lowerOrders, CompPoly.PolynomialMatrix.Approximant.residualOrders, CompPoly.PolynomialMatrix.Approximant.updateShiftByRows, CompPoly.PolynomialMatrix.Approximant.residualMatrixWithProduct, CompPoly.PolynomialMatrix.Approximant.residualMatrix
statement: formalized
proof: formalized
---

# X-Adic Approximant Problems

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.Basic`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean), by Valerii Huhnin.

> Basic data structures for approximant-basis computations over polynomial
> matrices.
>
> ## References
>
> * [Beckermann, B., and Labahn, G., *A uniform approach for the fast
>     computation of matrix-type Pade approximants*][BL94]
> * [Giorgi, P., Jeannerod, C.-P., and Villard, G., *On the complexity of
>     polynomial matrix computations*][GJV03]

`CompPoly.PolynomialMatrix.Approximant.XAdicProblem` (structure, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L36))

> A row approximant problem `p * matrix = 0 mod X^orders`.

```lean
structure XAdicProblem (F : Type*) [Zero F] where
  orders : Array Nat
  matrix : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.maxOrder` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L41))

> Maximum X-adic order in a problem.

```lean
def maxOrder [Zero F] (problem : XAdicProblem F) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.totalOrder` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L45))

> Sum of X-adic orders.

```lean
def totalOrder [Zero F] (problem : XAdicProblem F) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.lowerOrders` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L49))

> Truncate every problem order to at most `d`.

```lean
def lowerOrders [Zero F] (problem : XAdicProblem F) (d : Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.residualOrders` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L53))

> Remaining orders after the first `d` coefficients have been consumed.

```lean
def residualOrders [Zero F] (problem : XAdicProblem F) (d : Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.updateShiftByRows` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L57))

> Shift update used by the second recursive PM-basis call.

```lean
def updateShiftByRows [Zero F] [BEq F]
    (basis : PolynomialMatrix F) (shift : Array Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.residualMatrixWithProduct` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L67))

> Residual matrix `(P * A) div X^d`, using an explicit product kernel and
> truncating to the requested residual orders columnwise.

```lean
def residualMatrixWithProduct [Semiring F] [BEq F] [LawfulBEq F]
    (productKernel :
      Array Nat → PolynomialMatrix F → PolynomialMatrix F → PolynomialMatrix F)
    (basis : PolynomialMatrix F) (matrix : PolynomialMatrix F)
    (d : Nat) (orders : Array Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.residualMatrix` (definition, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean#L79))

> Residual matrix `(P * A) div X^d`, truncated to the requested residual
> orders columnwise, using the direct low-product row-column kernel.

```lean
def residualMatrix [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : PolynomialMatrix.MulLowContext F)
    (basis : PolynomialMatrix F) (matrix : PolynomialMatrix F)
    (d : Nat) (orders : Array Nat) : PolynomialMatrix F
```

## Depends on

- [Polynomial-Matrix Operations](../operations.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Basic.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.Basic.json)
