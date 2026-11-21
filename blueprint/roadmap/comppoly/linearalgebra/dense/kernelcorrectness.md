---
catalog: module
lean: CompPoly.DenseMatrix.homogeneousWitness_eq_none_iff, CompPoly.DenseMatrix.homogeneousWitness_exists_of_rows_lt_cols, CompPoly.DenseMatrix.homogeneousWitness_width, CompPoly.DenseMatrix.homogeneousWitness_nonzero, CompPoly.DenseMatrix.homogeneousWitness_sound, CompPoly.DenseMatrix.homogeneousWitness_none_complete
statement: formalized
proof: formalized
---

# Dense Homogeneous-Kernel Correctness

`CompPoly.LinearAlgebra.Dense.KernelCorrectness`, in [CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean), by Valerii Huhnin.

> Correctness contracts for executable dense homogeneous-kernel witnesses.

`CompPoly.DenseMatrix.homogeneousWitness_eq_none_iff` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean#L99))

```lean
theorem homogeneousWitness_eq_none_iff [Field F] [BEq F] (M : DenseMatrix F) :
    homogeneousWitness M = none ↔ (homogeneousKernelBasis M).size = 0
```

`CompPoly.DenseMatrix.homogeneousWitness_exists_of_rows_lt_cols` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean#L107))

> A matrix with more columns than rows has an executable homogeneous witness.

```lean
theorem homogeneousWitness_exists_of_rows_lt_cols [Field F] [BEq F] [LawfulBEq F]
    (M : DenseMatrix F) (h : M.rows < M.cols) :
    ∃ v, homogeneousWitness M = some v
```

`CompPoly.DenseMatrix.homogeneousWitness_width` (theorem, [line 560](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean#L560))

> Any homogeneous witness returned by the executable kernel search has matrix-column width.

```lean
theorem homogeneousWitness_width [Field F] [BEq F]
    {M : DenseMatrix F} {v : Array F} (h : homogeneousWitness M = some v) :
    VectorWidth M v
```

`CompPoly.DenseMatrix.homogeneousWitness_nonzero` (theorem, [line 570](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean#L570))

> Any homogeneous witness returned by the executable kernel search is nonzero.

```lean
theorem homogeneousWitness_nonzero [Field F] [BEq F]
    {M : DenseMatrix F} {v : Array F} (h : homogeneousWitness M = some v) :
    NonzeroVector v
```

`CompPoly.DenseMatrix.homogeneousWitness_sound` (theorem, [line 579](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean#L579))

> Soundness of the homogeneous witness returned by Gaussian elimination.

```lean
theorem homogeneousWitness_sound [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {v : Array F}
    (h : homogeneousWitness M = some v) :
    VectorWidth M v /\ IsHomogeneousSolution M v /\ NonzeroVector v
```

`CompPoly.DenseMatrix.homogeneousWitness_none_complete` (theorem, [line 616](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean#L616))

> If no homogeneous witness is returned, the homogeneous kernel is trivial.

```lean
theorem homogeneousWitness_none_complete [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) (h : homogeneousWitness M = none) :
    forall v, VectorWidth M v -> IsHomogeneousSolution M v -> Not (NonzeroVector v)
```

## Depends on

- [Dense Homogeneous Kernels](kernel.md)

## Proof depends on

- [Dense RREF Shape Correctness](rrefshape.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.KernelCorrectness.json)
