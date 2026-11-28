---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.PMBasisRuntime, CompPoly.PolynomialMatrix.Approximant.kernelLeafRuntimeWithLowAndCompose, CompPoly.PolynomialMatrix.Approximant.kernelLeafRuntimeWithLow, CompPoly.PolynomialMatrix.Approximant.kernelLeafRuntime, CompPoly.PolynomialMatrix.Approximant.pmBasisWithFuelCore, CompPoly.PolynomialMatrix.Approximant.pmBasisNormalizeRoot, CompPoly.PolynomialMatrix.Approximant.pmBasisWithFuel, CompPoly.PolynomialMatrix.Approximant.pmBasisFuel, CompPoly.PolynomialMatrix.Approximant.pmBasis, CompPoly.PolynomialMatrix.Approximant.completeMissingPivotRows_size_pos, CompPoly.PolynomialMatrix.Approximant.pmBasisNormalizeRoot_size_pos, CompPoly.PolynomialMatrix.Approximant.PMBasisContext
statement: formalized
proof: formalized
---

# Recursive PM-Basis Driver

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.Recursion`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean), by Valerii Huhnin.

> Runtime data for recursive PM-basis computation, the fuel-bounded
> divide-and-conquer driver, root normalization, the `pmBasis` entry point, and
> the `PMBasisContext` contract structure.
>
> ## References
>
> * [Beckermann, B., and Labahn, G., *A uniform approach for the fast
>     computation of matrix-type Pade approximants*][BL94]
> * [Giorgi, P., Jeannerod, C.-P., and Villard, G., *On the complexity of
>     polynomial matrix computations*][GJV03]

`CompPoly.PolynomialMatrix.Approximant.PMBasisRuntime` (structure, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L37))

> Runtime data for recursive PM-basis computation.

```lean
structure PMBasisRuntime (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  mulContext : CPolynomial.MulContext F
  lowMulContext : PolynomialMatrix.MulLowContext F
  composeBasis : PolynomialMatrix F → PolynomialMatrix F → PolynomialMatrix F
  residualProduct :
    Array Nat → PolynomialMatrix F → PolynomialMatrix F → PolynomialMatrix F
  leafCutoff : Nat
  leafBasis : XAdicProblem F → Array Nat → PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafRuntimeWithLowAndCompose` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L48))

> Recursive PM-basis runtime using the scalar dense-kernel routine as its
> small-leaf solver and an independently tuned basis-composition cutoff.

```lean
def kernelLeafRuntimeWithLowAndCompose (mulCtx : CPolynomial.MulContext F)
    (lowCtx : PolynomialMatrix.MulLowContext F)
    (leafCutoff composeLeafCutoff : Nat) :
    PMBasisRuntime F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafRuntimeWithLow` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L62))

> Recursive PM-basis runtime using the scalar dense-kernel routine as its
> small-leaf solver.

```lean
def kernelLeafRuntimeWithLow (mulCtx : CPolynomial.MulContext F)
    (lowCtx : PolynomialMatrix.MulLowContext F) (leafCutoff : Nat) :
    PMBasisRuntime F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafRuntime` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L69))

> Compatibility runtime whose low products are obtained by truncating full
> products.

```lean
def kernelLeafRuntime (mulCtx : CPolynomial.MulContext F) (leafCutoff : Nat) :
    PMBasisRuntime F
```

`CompPoly.PolynomialMatrix.Approximant.pmBasisWithFuelCore` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L82))

> Fuel-bounded recursive PM-basis driver, compacting zero rows after each
> leaf and composition step.
>
> Internal nodes return the composed product `P₂ * P₁` without re-reduction:
> composition of minimal half-bases under the updated shift is itself a basis of
> the full-order approximant module, so re-reducing at every node would only add
> work that is quadratic in the row degrees and outside the PM-basis cost model.
> A single weak-Popov normalization pass runs once at the root entry points.

```lean
def pmBasisWithFuelCore (runtime : PMBasisRuntime F) :
    Nat → XAdicProblem F → Array Nat → PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.pmBasisNormalizeRoot` (definition, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L108))

> Root normalization for a recursively composed approximant basis: one
> weak-Popov reduction pass plus completion rows for any leading position that
> lost its representative.  When the recursion preserved minimality this pass
> performs no cascading cancellations; it is a semantic guard, not part of the
> recursive cost model.

```lean
def pmBasisNormalizeRoot (problem : XAdicProblem F) (shift : Array Nat)
    (basis : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.pmBasisWithFuel` (definition, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L114))

> Fuel-bounded recursive PM-basis driver with root normalization.

```lean
def pmBasisWithFuel (runtime : PMBasisRuntime F)
    (fuel : Nat) (problem : XAdicProblem F) (shift : Array Nat) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.pmBasisFuel` (definition, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L121))

> Default fuel choice, large enough to split each positive order down to the
> leaf cutoff.

```lean
def pmBasisFuel (problem : XAdicProblem F) : Nat
```

`CompPoly.PolynomialMatrix.Approximant.pmBasis` (definition, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L125))

> Recursive PM-basis entry point.

```lean
def pmBasis (runtime : PMBasisRuntime F)
    (problem : XAdicProblem F) (shift : Array Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.Approximant.completeMissingPivotRows_size_pos` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L132))

> Monomial completion never returns an empty matrix for problems with at
> least one module row: an empty candidate set is completed with one monomial
> row per module coordinate.

```lean
theorem completeMissingPivotRows_size_pos
    (problem : XAdicProblem F) (shift : Array Nat) (rows : PolynomialMatrix F)
    (hsize : 0 < problem.matrix.size) :
    0 < (completeMissingPivotRows problem shift rows).size
```

`CompPoly.PolynomialMatrix.Approximant.pmBasisNormalizeRoot_size_pos` (theorem, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L148))

> The root-normalized recursive PM-basis is nonempty for problems with at
> least one module row.

```lean
theorem pmBasisNormalizeRoot_size_pos
    (problem : XAdicProblem F) (shift : Array Nat) (basis : PolynomialMatrix F)
    (hsize : 0 < problem.matrix.size) :
    0 < (pmBasisNormalizeRoot problem shift basis).size
```

`CompPoly.PolynomialMatrix.Approximant.PMBasisContext` (structure, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean#L156))

> Context packaging the executable PM-basis operation with theorem fields.

```lean
structure PMBasisContext (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  runtime : PMBasisRuntime F
  basis : XAdicProblem F → Array Nat → PolynomialMatrix F := pmBasis runtime
  sound :
    ∀ problem shift row,
      row ∈ MatrixRows (basis problem shift) →
        ∀ j, j < problem.orders.size →
          truncateX (problem.orders.getD j 0)
            (rowGet (rowMulMatrixWith runtime.mulContext row problem.matrix) j) = 0
  complete_minimal :
    ∀ problem shift row,
      0 < problem.matrix.size →
      WellFormed problem.matrix →
      (∀ j, j < problem.orders.size →
        truncateX (problem.orders.getD j 0)
          (rowGet (rowMulMatrixWith runtime.mulContext row problem.matrix) j) = 0) →
      rowIsZero row = false →
      row.size ≤ problem.matrix.size →
        ∃ basisRow degree,
          basisRow ∈ MatrixRows (basis problem shift) ∧
          basisRow.size ≤ problem.matrix.size ∧
          rowShiftedDegree? basisRow shift = some degree ∧
          ∀ rowDegree, rowShiftedDegree? row shift = some rowDegree →
            degree ≤ rowDegree
```

## Depends on

- [Scalar Kernel-Leaf PM-Basis Definitions](kernelleaf.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/Recursion.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.Recursion.json)
