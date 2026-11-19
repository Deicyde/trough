---
catalog: module
lean: CompPoly.CPolynomial.evalManyHorner_eq_map_eval, CompPoly.CPolynomial.evalManySharedPowers_eq_map_eval
statement: formalized
proof: formalized
---

# Many-Polynomial Evaluation Correctness

`CompPoly.Univariate.ManyEval.Correctness`, in [CompPoly/Univariate/ManyEval/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ManyEval/Correctness.lean), by Valerii Huhnin.

> Correctness theorem statements for many-polynomial evaluation backends.

`CompPoly.CPolynomial.evalManyHorner_eq_map_eval` (theorem, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ManyEval/Correctness.lean#L213))

> Many-polynomial Horner evaluation agrees with scalar evaluation.

```lean
theorem evalManyHorner_eq_map_eval [Semiring R]
    (polys : Array (CPolynomial R)) (x : R) :
    evalManyHorner polys x = polys.map (fun p ↦ p.eval x)
```

`CompPoly.CPolynomial.evalManySharedPowers_eq_map_eval` (theorem, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ManyEval/Correctness.lean#L219))

> Shared-powers evaluation agrees with scalar evaluation.

```lean
theorem evalManySharedPowers_eq_map_eval [Semiring R]
    (polys : Array (CPolynomial R)) (x : R) :
    evalManySharedPowers polys x = polys.map (fun p ↦ p.eval x)
```

## Depends on

- [Many-Polynomial Evaluation](basic.md)

## Sources

- [CompPoly/Univariate/ManyEval/Correctness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/ManyEval/Correctness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ManyEval.Correctness.json)
