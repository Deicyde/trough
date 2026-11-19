---
catalog: module
lean: CompPoly.DenseMatrix.scaleRowData_eq, CompPoly.DenseMatrix.addScaledRowData_eq, CompPoly.DenseMatrix.swapRowsData_eq, CompPoly.DenseMatrix.findPivotRowData_eq, CompPoly.DenseMatrix.normalizeAndEliminateData_eq, CompPoly.DenseMatrix.rrefLoopData_eq, CompPoly.DenseMatrix.rrefInPlace_eq, CompPoly.DenseMatrix.homogeneousWitnessInPlace_eq
statement: formalized
proof: formalized
---

# In-Place Dense Kernel Correctness

`CompPoly.LinearAlgebra.Dense.KernelInPlaceCorrectness`, in [CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean), by Valerii Huhnin.

> The in-place homogeneous-kernel backend (`KernelInPlace.lean`) performs the same
> arithmetic, in the same order, as the copying backend (`RowOps.lean`/`Kernel.lean`),
> so it returns the same witness. This file proves that equivalence, culminating in
> `homogeneousWitnessInPlace_eq`, which lets the certified Guruswami-Sudan backend run
> the in-place implementation while reusing every existing correctness theorem.

`CompPoly.DenseMatrix.scaleRowData_eq` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L61))

> The in-place scale of a row produces the same backing array as the copying scale.

```lean
theorem scaleRowData_eq [Field F] (M : DenseMatrix F) (r : Nat) (factor : F) :
    scaleRowData M.cols r factor M.data = (scaleRow M r factor).data
```

`CompPoly.DenseMatrix.addScaledRowData_eq` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L110))

> The in-place add-scaled row produces the same backing array as the copying version,
> when the target and source rows are distinct.

```lean
theorem addScaledRowData_eq [Field F] (M : DenseMatrix F) (target source : Nat)
    (factor : F) (hts : target ≠ source) :
    addScaledRowData M.cols target source factor M.data =
      (addScaledRow M target source factor).data
```

`CompPoly.DenseMatrix.swapRowsData_eq` (theorem, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L154))

> The in-place row swap produces the same backing array as the copying swap.

```lean
theorem swapRowsData_eq [Zero F] (M : DenseMatrix F) (rowA rowB : Nat) :
    swapRowsData M.cols rowA rowB M.data = (swapRows M rowA rowB).data
```

`CompPoly.DenseMatrix.findPivotRowData_eq` (theorem, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L166))

> The in-place pivot search agrees with the copying one.

```lean
theorem findPivotRowData_eq [Zero F] [BEq F] (M : DenseMatrix F) (startRow col : Nat) :
    findPivotRowData M.rows M.cols startRow col M.data = findPivotRow M startRow col
```

`CompPoly.DenseMatrix.normalizeAndEliminateData_eq` (theorem, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L200))

> The in-place normalize-and-eliminate step produces the same backing array.

```lean
theorem normalizeAndEliminateData_eq [Field F] [BEq F] (M : DenseMatrix F)
    (pivotRow pivotCol : Nat) :
    normalizeAndEliminateData M.rows M.cols pivotRow pivotCol M.data
      = (normalizeAndEliminate M pivotRow pivotCol).data
```

`CompPoly.DenseMatrix.rrefLoopData_eq` (theorem, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L226))

> The in-place reduction loop tracks the copying reduction loop, returning the
> same reduced backing array and the same pivot columns.

```lean
theorem rrefLoopData_eq [Field F] [BEq F] :
    ∀ (fuel col row : Nat) (M : DenseMatrix F) (pivots : Array Nat),
      rrefLoopData fuel M.rows M.cols col row M.data pivots
        = ((rrefLoop fuel col row M pivots).matrix.data,
           (rrefLoop fuel col row M pivots).pivots)
```

`CompPoly.DenseMatrix.rrefInPlace_eq` (theorem, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L258))

> The in-place RREF equals the copying RREF.

```lean
theorem rrefInPlace_eq [Field F] [BEq F] (M : DenseMatrix F) : rrefInPlace M = rref M
```

`CompPoly.DenseMatrix.homogeneousWitnessInPlace_eq` (theorem, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean#L270))

> The in-place homogeneous-kernel witness equals the copying witness.

```lean
theorem homogeneousWitnessInPlace_eq [Field F] [BEq F] (M : DenseMatrix F) :
    homogeneousWitnessInPlace M = homogeneousWitness M
```

## Depends on

- [In-Place Dense Homogeneous Kernels](kernelinplace.md)

## Proof depends on

- [Dense RREF Semantic Correctness](rrefsemantics.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelInPlaceCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.KernelInPlaceCorrectness.json)
