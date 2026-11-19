---
catalog: module
lean: CompPoly.CMlPolynomialEval.evalManyMle_eq_map_evalMle, CompPoly.CMlPolynomialEval.evalManyMleByLayers_eq_map_evalMle, CompPoly.CMlPolynomialEval.evalManyMleByLayers_eq_evalManyMle
statement: formalized
proof: formalized
---

# Multilinear Many-Polynomial Evaluation Correctness

`CompPoly.Multilinear.ManyEval.Correctness`, in [CompPoly/Multilinear/ManyEval/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/ManyEval/Correctness.lean), by Valerii Huhnin.

> Correctness theorem statements for many-polynomial multilinear evaluation.

`CompPoly.CMlPolynomialEval.evalManyMle_eq_map_evalMle` (theorem, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/ManyEval/Correctness.lean#L256))

> Iterated many-MLE evaluation agrees with scalar `evalMle` on each table.

```lean
theorem evalManyMle_eq_map_evalMle [CommRing R]
    (polys : Array (CMlPolynomialEval R n)) (x : Vector R n) :
    evalManyMle polys x = polys.map (fun p ↦ evalMle p x)
```

`CompPoly.CMlPolynomialEval.evalManyMleByLayers_eq_map_evalMle` (theorem, [line 263](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/ManyEval/Correctness.lean#L263))

> Layer-by-layer many-MLE evaluation agrees with scalar `evalMle` on each table.

```lean
theorem evalManyMleByLayers_eq_map_evalMle [CommRing R]
    (polys : Array (CMlPolynomialEval R n)) (x : Vector R n) :
    evalManyMleByLayers polys x = polys.map (fun p ↦ evalMle p x)
```

`CompPoly.CMlPolynomialEval.evalManyMleByLayers_eq_evalManyMle` (theorem, [line 290](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/ManyEval/Correctness.lean#L290))

> Layer-by-layer many-MLE evaluation agrees with iterated many-MLE evaluation.

```lean
theorem evalManyMleByLayers_eq_evalManyMle [CommRing R]
    (polys : Array (CMlPolynomialEval R n)) (x : Vector R n) :
    evalManyMleByLayers polys x = evalManyMle polys x
```

## Depends on

- [Many Multilinear Evaluations](basic.md)

## Sources

- [CompPoly/Multilinear/ManyEval/Correctness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multilinear/ManyEval/Correctness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Multilinear.ManyEval.Correctness.json)
