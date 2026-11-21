---
catalog: module
lean: CompPoly.CMlPolynomialEval.evalManyMleLoop, CompPoly.CMlPolynomialEval.evalManyMle, CompPoly.CMlPolynomialEval.valuesByPolynomial, CompPoly.CMlPolynomialEval.foldLayeredPolyLoop, CompPoly.CMlPolynomialEval.foldLayeredLayerLoop, CompPoly.CMlPolynomialEval.evalManyMleByLayersLoop, CompPoly.CMlPolynomialEval.evalManyMleByLayers
statement: formalized
proof: formalized
---

# Many Multilinear Evaluations

`CompPoly.Multilinear.ManyEval.Basic`, in [CompPoly/Multilinear/ManyEval/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean), by Valerii Huhnin.

> Executable evaluators for many dense hypercube-form multilinear polynomials at
> one shared point.

`CompPoly.CMlPolynomialEval.evalManyMleLoop` (definition, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean#L26))

> Evaluate each hypercube table independently with `evalMle`.

```lean
def evalManyMleLoop [CommRing R] (polys : Array (CMlPolynomialEval R n))
    (x : Vector R n) (i : Nat) (acc : Array R) : Array R
```

`CompPoly.CMlPolynomialEval.evalManyMle` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean#L38))

> Evaluate many hypercube tables by running scalar `evalMle` for each table.

```lean
def evalManyMle [CommRing R] (polys : Array (CMlPolynomialEval R n)) (x : Vector R n) :
    Array R
```

`CompPoly.CMlPolynomialEval.valuesByPolynomial` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean#L43))

> Flatten polynomial values in polynomial-major order by hypercube index.

```lean
def valuesByPolynomial (polys : Array (CMlPolynomialEval R n)) : Array R
```

`CompPoly.CMlPolynomialEval.foldLayeredPolyLoop` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean#L52))

> Fold one polynomial row for one MLE layer.

```lean
def foldLayeredPolyLoop [CommRing R] (current : Array R) (width nextWidth : Nat)
    (lo hi : R) (polyIdx pairIdx : Nat) (acc : Array R) : Array R
```

`CompPoly.CMlPolynomialEval.foldLayeredLayerLoop` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean#L66))

> Fold one MLE layer across all polynomials.

```lean
def foldLayeredLayerLoop [CommRing R] (current : Array R)
    (width nextWidth polyCount : Nat) (lo hi : R) (polyIdx : Nat) (acc : Array R) :
    Array R
```

`CompPoly.CMlPolynomialEval.evalManyMleByLayersLoop` (definition, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean#L79))

> Fold all MLE layers over a flattened polynomial-major batch.

```lean
def evalManyMleByLayersLoop [CommRing R] :
    {m : Nat} → Vector R m → Nat → Nat → Array R → Array R
```

`CompPoly.CMlPolynomialEval.evalManyMleByLayers` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean#L92))

> Evaluate many hypercube tables together by folding one MLE layer at a time.

```lean
def evalManyMleByLayers [CommRing R] (polys : Array (CMlPolynomialEval R n))
    (x : Vector R n) : Array R
```

## Depends on

- [Multilinear Polynomials](../basic.md)

## Sources

- [CompPoly/Multilinear/ManyEval/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/ManyEval/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Multilinear.ManyEval.Basic.json)
