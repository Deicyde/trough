---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.rowScaleCoeffX_size, CompPoly.PolynomialMatrix.Approximant.pivotRows_invariant, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_invariant, CompPoly.PolynomialMatrix.Approximant.mem_matrixRows_push, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsIncremental_invariant, CompPoly.PolynomialMatrix.Approximant.rowGet_vectorToPolynomialRow_coeff, CompPoly.PolynomialMatrix.Approximant.vectorToPolynomialRow_approximates, CompPoly.PolynomialMatrix.Approximant.pm_pack_index, CompPoly.PolynomialMatrix.Approximant.rowToCoefficientVector, CompPoly.PolynomialMatrix.Approximant.vectorToPolynomialRow_rowToCoefficientVector, CompPoly.PolynomialMatrix.Approximant.coefficientMatrixRows_dot_eq_zero_of_approximates, CompPoly.PolynomialMatrix.Approximant.kernelLeafBasis_rows
statement: formalized
proof: formalized
---

# Kernel-Leaf Basis Soundness

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.KernelLeafSoundness`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean), by Valerii Huhnin.

> Every row of the kernel-leaf basis satisfies the X-adic approximant
> conditions and has the principal row width: kernel vectors reconstruct to
> solutions, and the reduction, completion, and compaction steps preserve
> soundness.

> ## Kernel-leaf basis soundness

`CompPoly.PolynomialMatrix.Approximant.rowScaleCoeffX_size` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L41))

> Coefficient-shift row scaling preserves the row size.

```lean
theorem rowScaleCoeffX_size (c : F) (d : Nat) (row : PolynomialRow F) :
    (rowScaleCoeffX c d row).size = row.size
```

`CompPoly.PolynomialMatrix.Approximant.pivotRows_invariant` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L114))

> Any predicate holding for all stored pivot rows holds for all extracted rows.

```lean
theorem pivotRows_invariant (Q : PolynomialRow F → Prop)
    {pivots : Array (Option (PolynomialRow F))}
    (hpivots : ∀ p r, pivots.getD p none = some r → Q r)
    {row : PolynomialRow F} (hrow : row ∈ MatrixRows (pivotRows pivots)) :
    Q row
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_invariant` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L130))

> Any predicate closed under leading-term cancellation is preserved by the
> pivot-table reduction.

```lean
theorem reduceKernelLeafRowsByPivots_invariant (Q : PolynomialRow F → Prop)
    (hclosed : ∀ (target reducer : PolynomialRow F) (shift : Array Nat),
      Q target → Q reducer → Q (cancelKernelLeafLeadingTerm target reducer shift))
    {rows : PolynomialMatrix F} (shift : Array Nat)
    (hrows : ∀ row ∈ MatrixRows rows, Q row)
    {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (reduceKernelLeafRowsByPivots rows shift)) :
    Q row
```

`CompPoly.PolynomialMatrix.Approximant.mem_matrixRows_push` (theorem, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L175))

> A row of `rows.push row` is either a row of `rows` or `row` itself.

```lean
theorem mem_matrixRows_push {rows : PolynomialMatrix F}
    {row r : PolynomialRow F} (hr : r ∈ MatrixRows (rows.push row)) :
    r ∈ MatrixRows rows ∨ r = row
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsIncremental_invariant` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L185))

> Any predicate closed under leading-term cancellation is preserved by the
> incremental pivot reduction.

```lean
theorem reduceKernelLeafRowsIncremental_invariant
    (Q : PolynomialRow F → Prop)
    (hclosed : ∀ (target reducer : PolynomialRow F) (shift : Array Nat),
      Q target → Q reducer → Q (cancelKernelLeafLeadingTerm target reducer shift))
    {rows : PolynomialMatrix F} (shift : Array Nat)
    (hrows : ∀ row ∈ MatrixRows rows, Q row)
    {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (reduceKernelLeafRowsIncremental rows shift)) :
    Q row
```

`CompPoly.PolynomialMatrix.Approximant.rowGet_vectorToPolynomialRow_coeff` (theorem, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L295))

> Coefficients of polynomial rows reconstructed from scalar vectors.

```lean
theorem rowGet_vectorToPolynomialRow_coeff (cap width : Nat)
    (v : Array F) (k a : Nat) :
    CPolynomial.coeff (rowGet (vectorToPolynomialRow cap width v) k) a =
      if k < width ∧ a < cap then v.getD (k * cap + a) 0 else 0
```

`CompPoly.PolynomialMatrix.Approximant.vectorToPolynomialRow_approximates` (theorem, [line 317](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L317))

> Polynomial rows reconstructed from scalar kernel vectors satisfy the
> X-adic conditions of the bounded leaf problem.

```lean
theorem vectorToPolynomialRow_approximates (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) {v : Array F}
    (hv : v ∈ (homogeneousKernelBasisRows (coefficientMatrixRows problem)
      (problem.matrix.size * leafDegreeCap problem)).toList) :
    RowApproximates mulCtx problem
      (vectorToPolynomialRow (leafDegreeCap problem) problem.matrix.size v)
```

`CompPoly.PolynomialMatrix.Approximant.pm_pack_index` (theorem, [line 376](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L376))

> Arithmetic of the packed index `k * cap + a`.

```lean
theorem pm_pack_index {cap : Nat} (hcap : 0 < cap) {size k a : Nat}
    (hk : k < size) (ha : a < cap) :
    k * cap + a < size * cap ∧ (k * cap + a) / cap = k ∧
      (k * cap + a) % cap = a
```

`CompPoly.PolynomialMatrix.Approximant.rowToCoefficientVector` (definition, [line 393](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L393))

> Pack the coefficients below the leaf degree cap of a polynomial row into
> one flat scalar vector: coefficient `a` of coordinate `k` is stored at index
> `k * leafDegreeCap problem + a`.  This is the coefficient-side inverse of
> `vectorToPolynomialRow`.

```lean
def rowToCoefficientVector (problem : XAdicProblem F) (row : PolynomialRow F) :
    Array F
```

`CompPoly.PolynomialMatrix.Approximant.vectorToPolynomialRow_rowToCoefficientVector` (theorem, [line 414](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L414))

> Reconstructing a polynomial row from its packed coefficient vector is the
> identity on rows of the principal width whose coefficients respect the leaf
> degree cap.

```lean
theorem vectorToPolynomialRow_rowToCoefficientVector
    (problem : XAdicProblem F) {row : PolynomialRow F}
    (hsize : row.size = problem.matrix.size)
    (hdeg : ∀ k, k < row.size → ∀ a, leafDegreeCap problem ≤ a →
      CPolynomial.coeff (rowGet row k) a = 0) :
    vectorToPolynomialRow (leafDegreeCap problem) problem.matrix.size
      (rowToCoefficientVector problem row) = row
```

`CompPoly.PolynomialMatrix.Approximant.coefficientMatrixRows_dot_eq_zero_of_approximates` (theorem, [line 478](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L478))

> **Converse coefficient bridge.**  A polynomial row of a well-formed
> bounded leaf problem that satisfies the X-adic conditions yields a packed
> coefficient vector orthogonal to every scalar coefficient row.

```lean
theorem coefficientMatrixRows_dot_eq_zero_of_approximates
    (mulCtx : CPolynomial.MulContext F) (problem : XAdicProblem F)
    {row : PolynomialRow F}
    (happrox : RowApproximates mulCtx problem row)
    (hwf : WellFormed problem.matrix) :
    ∀ r ∈ (coefficientMatrixRows problem).toList,
      ∑ c ∈ Finset.range (problem.matrix.size * leafDegreeCap problem),
        r.getD c 0 * (rowToCoefficientVector problem row).getD c 0 = 0
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafBasis_rows` (theorem, [line 570](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean#L570))

> Every kernel-leaf basis row approximates the problem and has the principal
> row width.

```lean
theorem kernelLeafBasis_rows (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) (shift : Array Nat) :
    ∀ row ∈ MatrixRows (kernelLeafBasis problem shift),
      RowApproximates mulCtx problem row ∧ row.size = problem.matrix.size
```

## Depends on

- [X-Adic Row Soundness Toolkit](xadicsoundness.md)

## Proof depends on

- [Row-Array Homogeneous-Kernel Correctness](../../../dense/rowarraycorrectness.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSoundness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.KernelLeafSoundness.json)
