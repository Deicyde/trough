---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.modularSolutionBasis_sound, CompPoly.PolynomialMatrix.Approximant.modularSolutionBasis_complete_minimal
statement: formalized
proof: formalized
---

# Approximant-Basis Correctness Surface

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.Correctness`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Correctness.lean), by Valerii Huhnin.

> Named theorem surface for X-adic approximant bases and diagonal modular
> solution bases.  The executable contexts carry the current proof obligations.

`CompPoly.PolynomialMatrix.Approximant.modularSolutionBasis_sound` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Correctness.lean#L30))

> Rows returned by a modular solution-basis context satisfy the modular
> equation.

```lean
theorem modularSolutionBasis_sound
    (ctx : ModularSolutionBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (degreeBound? : Option Nat) {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (ctx.solutionBasis equation shift degreeBound?)) :
    rowSatisfiesModularBool ctx.mulContext ctx.modContext row
      equation.matrix equation.moduli = true
```

`CompPoly.PolynomialMatrix.Approximant.modularSolutionBasis_complete_minimal` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Correctness.lean#L42))

> Solution-basis completeness/minimality contract, relative to the
> caller-supplied degree bound: a solution row within the bound (vacuous for
> `none`) is matched by a returned basis row whose shifted degree does not
> exceed the bound — the solution's own degree when no bound is supplied.

```lean
theorem modularSolutionBasis_complete_minimal
    (ctx : ModularSolutionBasisContext F) (equation : ModularEquation F)
    (shift : Array Nat) (degreeBound? : Option Nat) {row : PolynomialRow F}
    {rowDegree : Nat}
    (hmonic : ∀ b, b < equation.moduli.size → (equation.moduli.getD b 0).monic)
    (hcols : equation.moduli.size ≤ MatrixWidth equation.matrix)
    (hshift : shift.size = equation.solutionWidth)
    (hrow :
      rowSatisfiesModularBool ctx.mulContext ctx.modContext row
        equation.matrix equation.moduli = true)
    (hnonzero : rowIsZero row = false)
    (hwidth : row.size ≤ equation.solutionWidth)
    (hdegree : rowShiftedDegree? row shift = some rowDegree)
    (hbound : ∀ bound, degreeBound? = some bound → rowDegree ≤ bound) :
    (∀ basisRow,
      basisRow ∈ MatrixRows (ctx.solutionBasis equation shift degreeBound?) →
        basisRow.size ≤ equation.solutionWidth) ∧
    ∃ basisRow degree,
      basisRow ∈ MatrixRows (ctx.solutionBasis equation shift degreeBound?) ∧
      rowShiftedDegree? basisRow shift = some degree ∧
      degree ≤ degreeBound?.getD rowDegree
```

## Depends on

- [Diagonal Modular Equations](modularequation-2/basic.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Correctness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/Correctness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.Correctness.json)
