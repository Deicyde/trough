---
catalog: module
lean: CompPoly.CPolynomial.CLagrange.arrayNode, CompPoly.CPolynomial.CLagrange.arrayValue, CompPoly.CPolynomial.CLagrange.interpolateArrays, CompPoly.CPolynomial.CLagrange.pointNode, CompPoly.CPolynomial.CLagrange.pointValue, CompPoly.CPolynomial.CLagrange.interpolateArray, CompPoly.CPolynomial.CLagrange.DistinctPointNodes, CompPoly.CPolynomial.CLagrange.eval_interpolateArray_at_index, CompPoly.CPolynomial.CLagrange.eval_interpolateArray_at_mem
statement: formalized
proof: formalized
---

# Array Wrappers for Computable Lagrange Interpolation

`CompPoly.Univariate.LagrangeArray`, in [CompPoly/Univariate/LagrangeArray.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean), by Valerii Huhnin.

> Finite-index adapters for `CPolynomial.CLagrange.interpolate`.

`CompPoly.CPolynomial.CLagrange.arrayNode` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L27))

> The `i`th node in an array, exposed through a `Fin` index.

```lean
def arrayNode (xs : Array F) (i : Fin xs.size) : F
```

`CompPoly.CPolynomial.CLagrange.arrayValue` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L31))

> The `i`th value in an array, defaulting only when the value array is shorter.

```lean
def arrayValue (ys : Array F) {n : Nat} (i : Fin n) : F
```

`CompPoly.CPolynomial.CLagrange.interpolateArrays` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L35))

> Lagrange interpolation from separate node and value arrays.

```lean
def interpolateArrays (xs ys : Array F) : CPolynomial F
```

`CompPoly.CPolynomial.CLagrange.pointNode` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L40))

> The `x` coordinate of the `i`th packed point.

```lean
def pointNode (points : Array (F × F)) (i : Fin points.size) : F
```

`CompPoly.CPolynomial.CLagrange.pointValue` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L44))

> The `y` coordinate of the `i`th packed point.

```lean
def pointValue (points : Array (F × F)) (i : Fin points.size) : F
```

`CompPoly.CPolynomial.CLagrange.interpolateArray` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L48))

> Lagrange interpolation from packed `(x, y)` points.

```lean
def interpolateArray (points : Array (F × F)) : CPolynomial F
```

`CompPoly.CPolynomial.CLagrange.DistinctPointNodes` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L53))

> Packed points have pairwise distinct Lagrange nodes.

```lean
def DistinctPointNodes (points : Array (F × F)) : Prop
```

`CompPoly.CPolynomial.CLagrange.eval_interpolateArray_at_index` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L79))

> Evaluating the packed-array interpolant at one indexed node returns the indexed value.

```lean
theorem eval_interpolateArray_at_index
    (points : Array (F × F)) (hdistinct : DistinctPointNodes points)
    (i : Fin points.size) :
    CPolynomial.eval (pointNode points i) (interpolateArray points) =
      pointValue points i
```

`CompPoly.CPolynomial.CLagrange.eval_interpolateArray_at_mem` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean#L93))

> Evaluating the packed-array interpolant at a listed point returns that point's value.

```lean
theorem eval_interpolateArray_at_mem
    (points : Array (F × F)) (hdistinct : DistinctPointNodes points)
    {point : F × F} (hpoint : point ∈ points.toList) :
    CPolynomial.eval point.1 (interpolateArray points) = point.2
```

## Depends on

- [Lagrange Interpolation](lagrange.md)

## Sources

- [CompPoly/Univariate/LagrangeArray.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/LagrangeArray.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.LagrangeArray.json)
