---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.RowChoiceValid, CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?_some_valid, CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?_degree_le, CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?_some_of_degree, CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeRow?_some_valid
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Row Selection Helpers

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Selection`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean), by Valerii Huhnin.

> Correctness facts for the least-shifted-degree row scan used by the executable backend.

`CompPoly.GuruswamiSudan.LeeOSullivan.RowChoiceValid` (definition, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean#L28))

```lean
def RowChoiceValid (M : PolynomialMatrix F) (shift : Array Nat)
    (choice : RowChoice F) : Prop
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?_some_valid` (theorem, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean#L331))

```lean
theorem leastShiftedDegreeChoice?_some_valid
    {M : PolynomialMatrix F} {shift : Array Nat} {choice : RowChoice F}
    (hchoice : leastShiftedDegreeChoice? M shift = some choice) :
    RowChoiceValid M shift choice
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?_degree_le` (theorem, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean#L343))

```lean
theorem leastShiftedDegreeChoice?_degree_le
    {M : PolynomialMatrix F} {shift : Array Nat}
    {choice : RowChoice F} {i d : Nat}
    (hchoice : leastShiftedDegreeChoice? M shift = some choice)
    (hi : i < M.size)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some d) :
    choice.degree ≤ d
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?_some_of_degree` (theorem, [line 358](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean#L358))

```lean
theorem leastShiftedDegreeChoice?_some_of_degree
    {M : PolynomialMatrix F} {shift : Array Nat} {i d : Nat}
    (hi : i < M.size)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some d) :
    ∃ choice, leastShiftedDegreeChoice? M shift = some choice ∧ choice.degree ≤ d
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeRow?_some_valid` (theorem, [line 379](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean#L379))

```lean
theorem leastShiftedDegreeRow?_some_valid
    {M : PolynomialMatrix F} {shift : Array Nat} {row : PolynomialRow F}
    (hrow : leastShiftedDegreeRow? M shift = some row) :
    ∃ choice,
      leastShiftedDegreeChoice? M shift = some choice ∧
        RowChoiceValid M shift choice ∧ choice.row = row
```

## Depends on

- [Executable Lee-O'Sullivan Interpolation](../algorithm.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Selection.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Selection.json)
