---
catalog: module
lean: CompPoly.CPolynomial.NTT.Inverse.inverseSpec_eval_node_eq, CompPoly.CPolynomial.NTT.Inverse.inverseSpec_evalOnDomain_eq, CompPoly.CPolynomial.NTT.Inverse.inverseSpec_interpolatePow_eq, CompPoly.CPolynomial.NTT.Inverse.inverseImpl_interpolatePow_eq, CompPoly.CPolynomial.NTT.Inverse.inverseImpl_eval_node_eq, CompPoly.CPolynomial.NTT.Inverse.inverseImpl_evalOnDomain_eq, CompPoly.CPolynomial.NTT.loadNaturalVector_toArray, CompPoly.CPolynomial.NTT.interpolate, CompPoly.CPolynomial.NTT.interpolate_eq_interpolatePow, CompPoly.CPolynomial.NTT.eval_interpolate_node
statement: formalized
proof: formalized
---

# NTT and Interpolation

`CompPoly.Univariate.NTT.Interpolation`, in [CompPoly/Univariate/NTT/Interpolation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean), by Valerii Huhnin.

> Bridge theorem declarations connecting the NTT specification layer to power-domain
> interpolation.

`CompPoly.CPolynomial.NTT.Inverse.inverseSpec_eval_node_eq` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L107))

> Pointwise form of `inverseSpec_interpolatePow_eq`.

```lean
theorem inverseSpec_eval_node_eq (D : Domain R) (values : Array R) (k : D.Idx) :
    CPolynomial.Raw.eval (D.node k) (inverseSpec D values) = values.getD k.1 0
```

`CompPoly.CPolynomial.NTT.Inverse.inverseSpec_evalOnDomain_eq` (theorem, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L119))

> The inverse NTT specification evaluates back to the input values on the NTT domain.

```lean
theorem inverseSpec_evalOnDomain_eq (D : Domain R) (values : Array R) :
    evalOnDomain D (inverseSpec D values) = loadNaturalArray D values
```

`CompPoly.CPolynomial.NTT.Inverse.inverseSpec_interpolatePow_eq` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L128))

> The inverse NTT specification interpolates the input values on the NTT domain.

```lean
theorem inverseSpec_interpolatePow_eq [BEq R] [LawfulBEq R]
    (D : Domain R) (values : Array R) :
    CPolynomial.Raw.trim (inverseSpec D values) =
      (CLagrange.interpolatePow D.omega (loadNaturalVector D values)).val
```

`CompPoly.CPolynomial.NTT.Inverse.inverseImpl_interpolatePow_eq` (theorem, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L187))

> The inverse NTT implementation interpolates the input values on the NTT domain.

```lean
theorem inverseImpl_interpolatePow_eq [BEq R] [LawfulBEq R]
    (D : Domain R) (values : Array R) :
    CPolynomial.Raw.trim (inverseImpl D values) =
      (CLagrange.interpolatePow D.omega (loadNaturalVector D values)).val
```

`CompPoly.CPolynomial.NTT.Inverse.inverseImpl_eval_node_eq` (theorem, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L195))

> Pointwise form of `inverseImpl_interpolatePow_eq`.

```lean
theorem inverseImpl_eval_node_eq (D : Domain R) (values : Array R) (k : D.Idx) :
    CPolynomial.Raw.eval (D.node k) (inverseImpl D values) = values.getD k.1 0
```

`CompPoly.CPolynomial.NTT.Inverse.inverseImpl_evalOnDomain_eq` (theorem, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L201))

> The inverse NTT implementation evaluates back to the input values on the NTT domain.

```lean
theorem inverseImpl_evalOnDomain_eq (D : Domain R) (values : Array R) :
    evalOnDomain D (inverseImpl D values) = loadNaturalArray D values
```

`CompPoly.CPolynomial.NTT.loadNaturalVector_toArray` (theorem, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L210))

> Loading a domain-sized vector back from its array is the identity.

```lean
theorem loadNaturalVector_toArray [Field R] (D : Domain R) (values : Vector R D.n) :
    loadNaturalVector D values.toArray = values
```

`CompPoly.CPolynomial.NTT.interpolate` (definition, [line 220](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L220))

> Interpolate natural-order values on the NTT domain through the inverse transform.
>
> This is `CLagrange.interpolatePow D.omega` (`interpolate_eq_interpolatePow`) computed with
> `O(n log n)` field operations rather than the Lagrange formula's `O(n²)` per basis
> polynomial.

```lean
def interpolate [BEq R] [LawfulBEq R] (D : Domain R) (values : Vector R D.n) :
    CPolynomial R
```

`CompPoly.CPolynomial.NTT.interpolate_eq_interpolatePow` (theorem, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L226))

> NTT interpolation is Lagrange interpolation on the powers of the domain root.

```lean
theorem interpolate_eq_interpolatePow [BEq R] [LawfulBEq R]
    (D : Domain R) (values : Vector R D.n) :
    interpolate D values = CLagrange.interpolatePow D.omega values
```

`CompPoly.CPolynomial.NTT.eval_interpolate_node` (theorem, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean#L233))

> NTT interpolation takes each value at its domain node.

```lean
theorem eval_interpolate_node [BEq R] [LawfulBEq R]
    (D : Domain R) (values : Vector R D.n) (k : D.Idx) :
    (interpolate D values).eval (D.node k) = values.get k
```

## Depends on

- [Lagrange Interpolation](../lagrange.md)
- [NTT and Evaluation](evaluation.md)
- [Inverse NTT](inverse.md)

## Proof depends on

- [NTT Kernel Identities](kernel.md)

## Sources

- [CompPoly/Univariate/NTT/Interpolation.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Interpolation.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Interpolation.json)
