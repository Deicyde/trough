---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.ceilDivFallback, CompPoly.PolynomialMatrix.Approximant.modulusDegreeMass, CompPoly.PolynomialMatrix.Approximant.chunkDelta, CompPoly.PolynomialMatrix.Approximant.linearizedOrders, CompPoly.PolynomialMatrix.Approximant.maxShiftDegree, CompPoly.PolynomialMatrix.Approximant.principalShiftOffset, CompPoly.PolynomialMatrix.Approximant.quotientShift, CompPoly.PolynomialMatrix.Approximant.liftedPrincipalShift, CompPoly.PolynomialMatrix.Approximant.exactNullspaceShift, CompPoly.PolynomialMatrix.Approximant.PrincipalChunk, CompPoly.PolynomialMatrix.Approximant.principalChunkCount, CompPoly.PolynomialMatrix.Approximant.principalChunks, CompPoly.PolynomialMatrix.Approximant.principalUnitChunks, CompPoly.PolynomialMatrix.Approximant.fallbackPivotDegree, CompPoly.PolynomialMatrix.Approximant.pivotDegreeAt, CompPoly.PolynomialMatrix.Approximant.principalChunkCountFromPivotDegree, CompPoly.PolynomialMatrix.Approximant.principalChunksFromPivotDegrees, CompPoly.PolynomialMatrix.Approximant.PartialLinearizationPlan, CompPoly.PolynomialMatrix.Approximant.partialLinearizationPlan, CompPoly.PolynomialMatrix.Approximant.partialLinearizationPlanFromPivotDegrees, CompPoly.PolynomialMatrix.Approximant.unchunkedPartialLinearizationPlan, CompPoly.PolynomialMatrix.Approximant.xPowPolynomial, CompPoly.PolynomialMatrix.Approximant.shiftPolynomialX, CompPoly.PolynomialMatrix.Approximant.shiftRowX, CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceShift, CompPoly.PolynomialMatrix.Approximant.compressChunkedPrincipalRow, CompPoly.PolynomialMatrix.Approximant.compressChunkedPrincipalRows
statement: formalized
proof: formalized
---

# Partial-Linearization Parameters

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PartialLinearization`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean), by Valerii Huhnin.

> Small executable helpers used by diagonal modular-equation solvers to size the
> expanded X-adic problem without using one global oversized order.
>
> ## References
>
> * [Storjohann, A., *Notes on computing minimal approximant bases*][Sto06]

`CompPoly.PolynomialMatrix.Approximant.ceilDivFallback` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L33))

> Ceiling division with `1` as the zero-width fallback.

```lean
def ceilDivFallback (n d : Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.modulusDegreeMass` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L37))

> Degree mass of diagonal moduli.

```lean
def modulusDegreeMass [Zero F] (moduli : Array (CPolynomial F)) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.chunkDelta` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L41))

> Chunk size `Delta = ceil(sigma / m)` used for partial linearization.

```lean
def chunkDelta [Zero F] (solutionWidth : Nat)
    (moduli : Array (CPolynomial F)) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.linearizedOrders` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L46))

> X-adic orders for the exact-nullspace lift, using the local chunk size.

```lean
def linearizedOrders [Zero F] (solutionWidth : Nat)
    (moduli : Array (CPolynomial F)) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.maxShiftDegree` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L52))

> Maximum shifted-degree offset in a principal-coordinate shift.

```lean
def maxShiftDegree (shift : Array Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.principalShiftOffset` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L60))

> Offset added to every principal coordinate when lifting to exact-nullspace
> coordinates.  Adding the same positive offset to every principal coordinate
> preserves their relative shifted degrees; quotient coordinates are shifted
> separately above the principal search window.

```lean
def principalShiftOffset (_shift : Array Nat) (delta : Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.quotientShift` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L67))

> Quotient-coordinate shift used by the exact-nullspace lift.  It is kept at
> the chunk degree so quotient coordinates do not dominate the shifted degree of
> principal relation rows.  Rows that compress to zero are removed later by the
> principal-row filter.

```lean
def quotientShift (_shift : Array Nat) (delta : Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.liftedPrincipalShift` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L71))

> Principal-coordinate shift used inside the exact-nullspace lift.

```lean
def liftedPrincipalShift (shift : Array Nat) (delta : Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.exactNullspaceShift` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L75))

> Extend the principal solution shift with low quotient shifts.

```lean
def exactNullspaceShift (shift : Array Nat) (quotientWidth delta : Nat) :
    Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.PrincipalChunk` (structure, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L82))

> One chunk of a principal solution coordinate.  It represents
> `X^offset * chunkPoly` in coordinate `coord`.

```lean
structure PrincipalChunk where
  coord : Nat
  offset : Nat
deriving Repr, BEq, DecidableEq
```

`CompPoly.PolynomialMatrix.Approximant.principalChunkCount` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L89))

> Number of chunks used for one principal coordinate from a shifted-degree
> profile.

```lean
def principalChunkCount (solutionWidth : Nat) (shift : Array Nat)
    (delta j : Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.principalChunks` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L96))

> Principal chunks induced by the known shifted-degree profile.

```lean
def principalChunks (solutionWidth : Nat) (shift : Array Nat)
    (delta : Nat) : Array PrincipalChunk
```

`CompPoly.PolynomialMatrix.Approximant.principalUnitChunks` (definition, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L106))

> One unshifted chunk for each principal coordinate.

```lean
def principalUnitChunks (solutionWidth : Nat) : Array PrincipalChunk
```

`CompPoly.PolynomialMatrix.Approximant.fallbackPivotDegree` (definition, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L112))

> Fallback shifted pivot degree used before discovery has produced a degree for
> one coordinate.

```lean
def fallbackPivotDegree (solutionWidth : Nat) (shift : Array Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.pivotDegreeAt` (definition, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L118))

> Pivot degree for one coordinate, falling back to the shift spread when the
> profile has not discovered that coordinate.

```lean
def pivotDegreeAt (solutionWidth : Nat) (shift : Array Nat)
    (pivotDegrees : Array (Option Nat)) (j : Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.principalChunkCountFromPivotDegree` (definition, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L126))

> Number of chunks for one principal coordinate from a discovered shifted
> pivot-degree profile.

```lean
def principalChunkCountFromPivotDegree (shift : Array Nat)
    (delta j pivotDegree : Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.principalChunksFromPivotDegrees` (definition, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L131))

> Principal chunks induced by a discovered shifted pivot-degree profile.

```lean
def principalChunksFromPivotDegrees (solutionWidth : Nat) (shift : Array Nat)
    (delta : Nat) (pivotDegrees : Array (Option Nat)) :
    Array PrincipalChunk
```

`CompPoly.PolynomialMatrix.Approximant.PartialLinearizationPlan` (structure, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L143))

> Executable partial-linearization plan for the exact-nullspace lift.

```lean
structure PartialLinearizationPlan where
  solutionWidth : Nat
  quotientWidth : Nat
  delta : Nat
  chunks : Array PrincipalChunk
```

`CompPoly.PolynomialMatrix.Approximant.partialLinearizationPlan` (definition, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L150))

> Build a chunk plan from the modular shape and shifted-degree profile.

```lean
def partialLinearizationPlan [Zero F] (solutionWidth quotientWidth : Nat)
    (moduli : Array (CPolynomial F)) (shift : Array Nat) :
    PartialLinearizationPlan
```

`CompPoly.PolynomialMatrix.Approximant.partialLinearizationPlanFromPivotDegrees` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L160))

> Build a chunk plan from a discovered shifted pivot-degree profile.

```lean
def partialLinearizationPlanFromPivotDegrees [Zero F]
    (solutionWidth quotientWidth : Nat) (moduli : Array (CPolynomial F))
    (shift : Array Nat) (pivotDegrees : Array (Option Nat)) :
    PartialLinearizationPlan
```

`CompPoly.PolynomialMatrix.Approximant.unchunkedPartialLinearizationPlan` (definition, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L171))

> Plan with partial linearization disabled for the principal coordinates.

```lean
def unchunkedPartialLinearizationPlan [Zero F]
    (solutionWidth quotientWidth : Nat) (moduli : Array (CPolynomial F)) :
    PartialLinearizationPlan
```

`CompPoly.PolynomialMatrix.Approximant.xPowPolynomial` (definition, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L181))

> Monomial `X^offset` as a canonical polynomial, built without requiring the
> `CPolynomial.X` nontriviality instance.

```lean
def xPowPolynomial [Zero F] [One F] [BEq F] [LawfulBEq F]
    (offset : Nat) : CPolynomial F
```

`CompPoly.PolynomialMatrix.Approximant.shiftPolynomialX` (definition, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L188))

> Multiply a polynomial by `X^offset` by shifting its coefficient array.
> This is an `O(offset + deg p)` array operation; it must not go through generic
> polynomial multiplication, which would cost `O(offset * deg p)`.

```lean
def shiftPolynomialX [Semiring F] [BEq F] [LawfulBEq F]
    (offset : Nat) (p : CPolynomial F) : CPolynomial F
```

`CompPoly.PolynomialMatrix.Approximant.shiftRowX` (definition, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L196))

> Shift every entry of a row by `X^offset`.

```lean
def shiftRowX [Semiring F] [BEq F] [LawfulBEq F]
    (offset : Nat) (row : PolynomialRow F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.Approximant.chunkedExactNullspaceShift` (definition, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L201))

> Shift for the chunked exact-nullspace problem.

```lean
def chunkedExactNullspaceShift (plan : PartialLinearizationPlan)
    (shift : Array Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.Approximant.compressChunkedPrincipalRow` (definition, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L211))

> Compress one row in chunked coordinates back to the principal solution
> coordinates.

```lean
def compressChunkedPrincipalRow [Semiring F] [BEq F] [LawfulBEq F]
    (plan : PartialLinearizationPlan) (row : PolynomialRow F) :
    PolynomialRow F
```

`CompPoly.PolynomialMatrix.Approximant.compressChunkedPrincipalRows` (definition, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean#L226))

> Compress every row in a chunked basis back to the principal coordinates.

```lean
def compressChunkedPrincipalRows [Semiring F] [BEq F] [LawfulBEq F]
    (plan : PartialLinearizationPlan) (basis : PolynomialMatrix F) :
    PolynomialMatrix F
```

## Depends on

- [Polynomial Rows and Matrices](../basic.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PartialLinearization.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PartialLinearization.json)
