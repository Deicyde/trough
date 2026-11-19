---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.leafDegreeCap, CompPoly.PolynomialMatrix.Approximant.coefficientEquationIndices, CompPoly.PolynomialMatrix.Approximant.coefficientMatrix, CompPoly.PolynomialMatrix.Approximant.coefficientMatrixRow, CompPoly.PolynomialMatrix.Approximant.coefficientMatrixRows, CompPoly.PolynomialMatrix.Approximant.vectorToPolynomialRow, CompPoly.PolynomialMatrix.Approximant.coeffXPower, CompPoly.PolynomialMatrix.Approximant.polynomialScaleCoeffX, CompPoly.PolynomialMatrix.Approximant.rowScaleCoeffX, CompPoly.PolynomialMatrix.Approximant.monomialUnitRow, CompPoly.PolynomialMatrix.Approximant.kernelLeafCompletionRows, CompPoly.PolynomialMatrix.Approximant.rowsContainLeadingPosition, CompPoly.PolynomialMatrix.Approximant.missingCompletionRows, CompPoly.PolynomialMatrix.Approximant.completeMissingPivotRows, CompPoly.PolynomialMatrix.Approximant.cancelKernelLeafLeadingTerm, CompPoly.PolynomialMatrix.Approximant.kernelLeafConflictInRowStep?, CompPoly.PolynomialMatrix.Approximant.kernelLeafConflictInRow?, CompPoly.PolynomialMatrix.Approximant.kernelLeafConflictFrom?, CompPoly.PolynomialMatrix.Approximant.kernelLeafConflict?, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafStep, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafFuel, CompPoly.PolynomialMatrix.Approximant.pivotRows, CompPoly.PolynomialMatrix.Approximant.insertKernelLeafPivotRowWithFuel, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafWithFuel, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRows, CompPoly.PolynomialMatrix.Approximant.insertKernelLeafRowIncremental, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsIncremental, CompPoly.PolynomialMatrix.Approximant.kernelLeafBasis, CompPoly.PolynomialMatrix.Approximant.compactNonzeroRows
statement: formalized
proof: formalized
---

# Scalar Kernel-Leaf PM-Basis Definitions

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.KernelLeaf`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean), by Valerii Huhnin.

> Executable definitions for the classical scalar-kernel PM-basis leaf: the
> dense coefficient matrix and its row-array RREF kernel, reconstruction of
> polynomial rows from kernel vectors, monomial completion rows, and the
> shifted pivot-table reduction used to compact leaf bases.

`CompPoly.PolynomialMatrix.Approximant.leafDegreeCap` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L35))

> Coefficient degree cap used by the classical scalar-kernel PM-basis leaf.

```lean
def leafDegreeCap (problem : XAdicProblem F) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.coefficientEquationIndices` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L39))

> Coefficient-equation indices `(column, coefficientDegree)`.

```lean
def coefficientEquationIndices (orders : Array Nat) : Array (Nat × Nat)
```

`CompPoly.PolynomialMatrix.Approximant.coefficientMatrix` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L47))

> Dense scalar coefficient matrix for the bounded leaf problem.

```lean
def coefficientMatrix (problem : XAdicProblem F) : DenseMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.coefficientMatrixRow` (definition, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L64))

> One scalar coefficient row for the bounded leaf problem.

```lean
def coefficientMatrixRow (problem : XAdicProblem F) (degreeCap : Nat)
    (equation : Nat × Nat) : Array F
```

`CompPoly.PolynomialMatrix.Approximant.coefficientMatrixRows` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L82))

> Scalar coefficient rows for the bounded leaf problem.  This is the same
> matrix as `coefficientMatrix`, represented directly as row arrays for the tiny
> leaf RREF routine.

```lean
def coefficientMatrixRows (problem : XAdicProblem F) : Array (Array F)
```

`CompPoly.PolynomialMatrix.Approximant.vectorToPolynomialRow` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L88))

> Convert one scalar kernel vector back into a polynomial row.

```lean
def vectorToPolynomialRow (degreeCap solutionWidth : Nat) (v : Array F) :
    PolynomialRow F
```

`CompPoly.PolynomialMatrix.Approximant.coeffXPower` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L98))

> Polynomial `c * X^d`, built without the `CPolynomial.monomial`
> `DecidableEq` assumption.

```lean
def coeffXPower (c : F) (d : Nat) : CPolynomial F
```

`CompPoly.PolynomialMatrix.Approximant.polynomialScaleCoeffX` (definition, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L102))

> Multiply a row by `c * X^d`, using the coefficient-array monomial builder.

```lean
def polynomialScaleCoeffX (c : F) (d : Nat) (p : CPolynomial F) :
    CPolynomial F
```

`CompPoly.PolynomialMatrix.Approximant.rowScaleCoeffX` (definition, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L114))

> Multiply a row by `c * X^d`, using coefficient shifting instead of generic
> polynomial multiplication by a monomial.

```lean
def rowScaleCoeffX (c : F) (d : Nat) (row : PolynomialRow F) :
    PolynomialRow F
```

`CompPoly.PolynomialMatrix.Approximant.monomialUnitRow` (definition, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L120))

> Monomial row `X^d * e_i`, used to complete bounded-kernel leaves to a full
> approximant basis.

```lean
def monomialUnitRow (width i d : Nat) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafCompletionRows` (definition, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L127))

> Trivial high-degree approximants present in every X-adic problem.  These
> rows are essential when the bounded scalar kernel has fewer rows than the module
> rank.

```lean
def kernelLeafCompletionRows (problem : XAdicProblem F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.rowsContainLeadingPosition` (definition, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L135))

> Whether a row set already contains a row with a given shifted leading
> position.

```lean
def rowsContainLeadingPosition (rows : PolynomialMatrix F)
    (shift : Array Nat) (position : Nat) : Bool
```

`CompPoly.PolynomialMatrix.Approximant.missingCompletionRows` (definition, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L145))

> High monomial rows for shifted leading positions not represented by `rows`.
> These rows are always valid approximants and keep recursive residual problems
> from losing coordinates after compact row reduction.

```lean
def missingCompletionRows (problem : XAdicProblem F)
    (shift : Array Nat) (rows : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.completeMissingPivotRows` (definition, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L157))

> Add high monomial approximants for missing pivot positions.

```lean
def completeMissingPivotRows (problem : XAdicProblem F)
    (shift : Array Nat) (rows : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.cancelKernelLeafLeadingTerm` (definition, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L166))

> Cancel the shifted leading term of `target` by `reducer`, when their shifted
> leading positions agree.  This is the small-leaf analogue of polynomial-matrix
> row reduction; it is used only after the bounded scalar kernel has already been
> computed.

```lean
def cancelKernelLeafLeadingTerm
    (target reducer : PolynomialRow F) (shift : Array Nat) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafConflictInRowStep?` (definition, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L181))

> One inner-loop update for finding a leading-position conflict in a bounded
> kernel leaf.

```lean
def kernelLeafConflictInRowStep? (rows : PolynomialMatrix F) (shift : Array Nat)
    (i : Nat) (found : Option (Nat × Nat)) (j : Nat) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafConflictInRow?` (definition, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L193))

> Scan one row for a shifted-leading-position conflict in a bounded kernel
> leaf.

```lean
def kernelLeafConflictInRow? (rows : PolynomialMatrix F) (shift : Array Nat)
    (i : Nat) (found : Option (Nat × Nat)) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafConflictFrom?` (definition, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L199))

> Scan all row pairs for the first shifted-leading-position conflict.

```lean
def kernelLeafConflictFrom? (rows : PolynomialMatrix F) (shift : Array Nat)
    (found : Option (Nat × Nat)) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafConflict?` (definition, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L206))

> First pair of nonzero bounded-kernel rows with the same shifted leading
> position.

```lean
def kernelLeafConflict? (rows : PolynomialMatrix F) (shift : Array Nat) :
    Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafStep` (definition, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L211))

> One shifted-reduction step for bounded scalar-kernel rows.

```lean
def reduceKernelLeafStep (rows : PolynomialMatrix F) (shift : Array Nat)
    (i j : Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafFuel` (definition, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L225))

> Fuel for bounded-kernel shifted reduction.  The scalar leaf is already a
> small base case, so this conservative degree-width bound is acceptable here.

```lean
def reduceKernelLeafFuel (rows : PolynomialMatrix F) (shift : Array Nat) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.pivotRows` (definition, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L235))

> Extract the nonempty pivot rows from a leading-position table.

```lean
def pivotRows (pivots : Array (Option (PolynomialRow F))) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.insertKernelLeafPivotRowWithFuel` (definition, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L242))

> Insert one row into a shifted weak-Popov pivot table.  Conflicts are resolved
> only at the current leading position, avoiding the repeated global pair scans
> used by the simple reference reducer.

```lean
def insertKernelLeafPivotRowWithFuel :
    Nat → Array (Option (PolynomialRow F)) → Array Nat → PolynomialRow F →
      Array (Option (PolynomialRow F))
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots` (definition, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L265))

> Pivot-table shifted reduction for bounded scalar-kernel rows.

```lean
def reduceKernelLeafRowsByPivots (rows : PolynomialMatrix F) (shift : Array Nat) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafWithFuel` (definition, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L276))

> Shift-reduce the bounded scalar-kernel rows before compacting them.  This
> keeps one low representative per shifted leading position instead of selecting
> arbitrary low-degree kernel vectors.

```lean
def reduceKernelLeafWithFuel :
    Nat → PolynomialMatrix F → Array Nat → PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRows` (definition, [line 286](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L286))

> Shift-reduced bounded scalar-kernel rows for the PM-basis leaf.

```lean
def reduceKernelLeafRows (rows : PolynomialMatrix F) (shift : Array Nat) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.insertKernelLeafRowIncremental` (definition, [line 293](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L293))

> Insert one bounded-kernel row into a small shifted-reduced leaf basis.  This
> keeps the live reduction matrix near the module width instead of reducing the
> entire scalar kernel at once.

```lean
def insertKernelLeafRowIncremental (basis : PolynomialMatrix F)
    (shift : Array Nat) (row : PolynomialRow F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsIncremental` (definition, [line 300](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L300))

> Shift-reduce all bounded scalar-kernel rows incrementally.  The dense scalar
> kernel can have many rows, but after every insertion the weak-Popov conflict loop
> works on the current reduced basis plus one candidate row.

```lean
def reduceKernelLeafRowsIncremental (rows : PolynomialMatrix F)
    (shift : Array Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafBasis` (definition, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L305))

> Classical scalar-kernel leaf for small X-adic approximant problems.

```lean
def kernelLeafBasis (problem : XAdicProblem F) (shift : Array Nat) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.compactNonzeroRows` (definition, [line 317](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean#L317))

> Remove zero rows before a recursively computed approximant basis is used as
> the coordinate system for the next residual problem.

```lean
def compactNonzeroRows (rows : PolynomialMatrix F) : PolynomialMatrix F
```

## Depends on

- [Row-Array Homogeneous Kernels](../../../dense/rowarray.md)
- [X-Adic Approximant Problems](../basic.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeaf.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.KernelLeaf.json)
