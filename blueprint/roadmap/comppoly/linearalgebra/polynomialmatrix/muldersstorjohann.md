---
catalog: module
lean: CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowStep?, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?, CompPoly.PolynomialMatrix.shiftedLeadingConflictFromStep?, CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?, CompPoly.PolynomialMatrix.shiftedLeadingConflict?, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm, CompPoly.PolynomialMatrix.muldersStorjohannStep, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel, CompPoly.PolynomialMatrix.matrixShiftedDegree?, CompPoly.PolynomialMatrix.muldersStorjohannFuel, CompPoly.PolynomialMatrix.muldersStorjohannReduce, CompPoly.PolynomialMatrix.rowLeadingPositions, CompPoly.PolynomialMatrix.cachedLeadingConflictInRowStep?, CompPoly.PolynomialMatrix.cachedLeadingConflictInRow?, CompPoly.PolynomialMatrix.cachedLeadingConflict?, CompPoly.PolynomialMatrix.cancelShiftedLeadingTermFast, CompPoly.PolynomialMatrix.muldersStorjohannStepFast, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuelFast, CompPoly.PolynomialMatrix.muldersStorjohannReduceFast
statement: formalized
proof: formalized
---

# Mulders-Storjohann Shifted Row Reduction

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohann`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean), by Valerii Huhnin.

> Direct executable shifted row reduction over polynomial rows.
>
> ## References
>
> * [Mulders, T., and Storjohann, A., *On lattice reduction for polynomial
>     matrices*][MS03]

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowStep?` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L30))

> One inner-loop update for shifted-leading-position conflict search.

```lean
def shiftedLeadingConflictInRowStep?
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat)
    (found : Option (Nat × Nat)) (j : Nat) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L43))

> Scan one row index `i` for a shifted-leading-position conflict.

```lean
def shiftedLeadingConflictInRow?
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat)
    (found : Option (Nat × Nat)) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFromStep?` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L51))

> One outer-loop update for shifted-leading-position conflict search.

```lean
def shiftedLeadingConflictFromStep?
    (M : PolynomialMatrix F) (shift : Array Nat)
    (found : Option (Nat × Nat)) (i : Nat) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L57))

> Scan all row pairs for the first shifted-leading-position conflict.

```lean
def shiftedLeadingConflictFrom?
    (M : PolynomialMatrix F) (shift : Array Nat)
    (found : Option (Nat × Nat)) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflict?` (definition, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L65))

> First pair of nonzero rows with the same shifted leading position.

```lean
def shiftedLeadingConflict? (M : PolynomialMatrix F) (shift : Array Nat) :
    Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L70))

> Cancel the shifted leading term of `target` using `reducer`, when possible.

```lean
def cancelShiftedLeadingTerm
    (target reducer : PolynomialRow F) (shift : Array Nat) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.muldersStorjohannStep` (definition, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L85))

> One Mulders-Storjohann cancellation step for a chosen conflicting pair.

```lean
def muldersStorjohannStep
    (M : PolynomialMatrix F) (shift : Array Nat) (i j : Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L98))

> Fuel-bounded Mulders-Storjohann reduction loop.

```lean
def muldersStorjohannReduceWithFuel :
    Nat → PolynomialMatrix F → Array Nat → PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.matrixShiftedDegree?` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L109))

> Maximum shifted row degree among the rows of a matrix.

```lean
def matrixShiftedDegree? (M : PolynomialMatrix F) (shift : Array Nat) : Option Nat
```

`CompPoly.PolynomialMatrix.muldersStorjohannFuel` (definition, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L118))

> Executable fuel used by the direct reducer.

```lean
def muldersStorjohannFuel (M : PolynomialMatrix F) (shift : Array Nat) : Nat
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce` (definition, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L123))

> Direct executable Mulders-Storjohann shifted row reducer.

```lean
def muldersStorjohannReduce (M : PolynomialMatrix F) (shift : Array Nat) :
    PolynomialMatrix F
```

> ### Fast variants
>
> The loop above recomputes every row's shifted leading position for every
> scanned row pair, and cancels leading terms through a generic
> monomial-times-row multiplication. The variants below compute each row's
> leading position once per scan and use the fused `rowSubScaledShift` update.
> They are proved extensionally equal to the direct definitions in
> `MuldersStorjohannCorrectness/Fast.lean`, so all correctness results transfer.

`CompPoly.PolynomialMatrix.rowLeadingPositions` (definition, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L139))

> Shifted leading positions of all rows, computed once per conflict scan.

```lean
def rowLeadingPositions
    (M : PolynomialMatrix F) (shift : Array Nat) : Array (Option Nat)
```

`CompPoly.PolynomialMatrix.cachedLeadingConflictInRowStep?` (definition, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L144))

> One inner-loop update for cached shifted-leading-position conflict search.

```lean
def cachedLeadingConflictInRowStep?
    (positions : Array (Option Nat)) (i : Nat)
    (found : Option (Nat × Nat)) (j : Nat) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.cachedLeadingConflictInRow?` (definition, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L156))

> Scan one row index `i` for a cached shifted-leading-position conflict.

```lean
def cachedLeadingConflictInRow?
    (positions : Array (Option Nat)) (i : Nat)
    (found : Option (Nat × Nat)) : Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.cachedLeadingConflict?` (definition, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L164))

> First pair of rows with the same cached shifted leading position.

```lean
def cachedLeadingConflict? (positions : Array (Option Nat)) :
    Option (Nat × Nat)
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTermFast` (definition, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L171))

> `cancelShiftedLeadingTerm` with the fused row update.

```lean
def cancelShiftedLeadingTermFast
    (target reducer : PolynomialRow F) (shift : Array Nat) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.muldersStorjohannStepFast` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L185))

> One fast Mulders-Storjohann cancellation step.

```lean
def muldersStorjohannStepFast
    (M : PolynomialMatrix F) (shift : Array Nat) (i j : Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuelFast` (definition, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L198))

> Fuel-bounded fast Mulders-Storjohann reduction loop.

```lean
def muldersStorjohannReduceWithFuelFast :
    Nat → PolynomialMatrix F → Array Nat → PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceFast` (definition, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean#L210))

> Fast executable Mulders-Storjohann shifted row reducer. Agrees with
> `muldersStorjohannReduce`; see `muldersStorjohannReduceFast_eq`.

```lean
def muldersStorjohannReduceFast (M : PolynomialMatrix F) (shift : Array Nat) :
    PolynomialMatrix F
```

## Depends on

- [Shifted Degrees for Polynomial Rows](shifted.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohann.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohann.json)
