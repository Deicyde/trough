---
catalog: module
lean: CompPoly.PolynomialMatrix.RowChoiceValid, CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?_some_valid, CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?_degree_le, CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?_some_of_degree, CompPoly.PolynomialMatrix.leastShiftedDegreeRow?_some_valid
statement: formalized
proof: formalized
---

# Least-Shifted-Degree Row Selection Helpers

`CompPoly.LinearAlgebra.PolynomialMatrix.RowSelection`, in [CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean), by Valerii Huhnin.

> Correctness facts for the generic least-shifted-degree row scan in
> `PolynomialMatrix.Operations`.

`CompPoly.PolynomialMatrix.RowChoiceValid` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean#L30))

```lean
def RowChoiceValid (M : PolynomialMatrix F) (shift : Array Nat)
    (choice : RowChoice F) : Prop
```

`CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?_some_valid` (theorem, [line 333](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean#L333))

```lean
theorem leastShiftedDegreeChoice?_some_valid
    {M : PolynomialMatrix F} {shift : Array Nat} {choice : RowChoice F}
    (hchoice : leastShiftedDegreeChoice? M shift = some choice) :
    RowChoiceValid M shift choice
```

`CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?_degree_le` (theorem, [line 345](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean#L345))

```lean
theorem leastShiftedDegreeChoice?_degree_le
    {M : PolynomialMatrix F} {shift : Array Nat}
    {choice : RowChoice F} {i d : Nat}
    (hchoice : leastShiftedDegreeChoice? M shift = some choice)
    (hi : i < M.size)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some d) :
    choice.degree ≤ d
```

`CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?_some_of_degree` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean#L360))

```lean
theorem leastShiftedDegreeChoice?_some_of_degree
    {M : PolynomialMatrix F} {shift : Array Nat} {i d : Nat}
    (hi : i < M.size)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some d) :
    ∃ choice, leastShiftedDegreeChoice? M shift = some choice ∧ choice.degree ≤ d
```

`CompPoly.PolynomialMatrix.leastShiftedDegreeRow?_some_valid` (theorem, [line 381](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean#L381))

```lean
theorem leastShiftedDegreeRow?_some_valid
    {M : PolynomialMatrix F} {shift : Array Nat} {row : PolynomialRow F}
    (hrow : leastShiftedDegreeRow? M shift = some row) :
    ∃ choice,
      leastShiftedDegreeChoice? M shift = some choice ∧
        RowChoiceValid M shift choice ∧ choice.row = row
```

## Depends on

- [Polynomial-Matrix Operations](operations.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/RowSelection.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.RowSelection.json)
