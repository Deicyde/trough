---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_interpolatePow_eq, CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_eval_node_eq, CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_evalOnDomain_eq, CompPoly.CPolynomial.NTTFast.Plan.interpolate, CompPoly.CPolynomial.NTTFast.Plan.interpolate_eq_ntt_interpolate, CompPoly.CPolynomial.NTTFast.Plan.interpolate_eq_interpolatePow
statement: formalized
proof: formalized
---

# NTTFast and Interpolation

`CompPoly.Univariate.NTTFast.Interpolation`, in [CompPoly/Univariate/NTTFast/Interpolation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean), by Valerii Huhnin.

> Bridge theorem declarations deriving NTTFast interpolation facts from the shared
> NTT specification layer.

`CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_interpolatePow_eq` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean#L32))

> …

```lean
theorem inverseImpl_interpolatePow_eq [BEq R] [LawfulBEq R]
    (P : Plan R) (hP : WellFormed P) (values : Array R) :
    CPolynomial.Raw.trim (inverseImpl P (NTT.Transform.bitRevPermute P.domain values)) =
      (CLagrange.interpolatePow P.domain.omega
        (NTT.loadNaturalVector P.domain values)).val
```

`CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_eval_node_eq` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean#L41))

> …

```lean
theorem inverseImpl_eval_node_eq
    (P : Plan R) (hP : WellFormed P) (values : Array R) (k : P.domain.Idx) :
    CPolynomial.Raw.eval (P.domain.node k)
      (inverseImpl P (NTT.Transform.bitRevPermute P.domain values)) = values.getD k.1 0
```

`CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_evalOnDomain_eq` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean#L49))

> …

```lean
theorem inverseImpl_evalOnDomain_eq
    (P : Plan R) (hP : WellFormed P) (values : Array R) :
    NTT.evalOnDomain P.domain (inverseImpl P (NTT.Transform.bitRevPermute P.domain values)) =
      NTT.loadNaturalArray P.domain values
```

`CompPoly.CPolynomial.NTTFast.Plan.interpolate` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean#L60))

> Interpolate natural-order values on the plan's domain with the cached inverse transform.
>
> …

```lean
def interpolate [BEq R] [LawfulBEq R] (P : Plan R) (values : Vector R P.domain.n) :
    CPolynomial R
```

`CompPoly.CPolynomial.NTTFast.Plan.interpolate_eq_ntt_interpolate` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean#L66))

> A well-formed plan's interpolation agrees with the unplanned `NTT.interpolate`.

```lean
theorem interpolate_eq_ntt_interpolate [BEq R] [LawfulBEq R]
    (P : Plan R) (hP : WellFormed P) (values : Vector R P.domain.n) :
    interpolate P values = NTT.interpolate P.domain values
```

`CompPoly.CPolynomial.NTTFast.Plan.interpolate_eq_interpolatePow` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean#L74))

> A well-formed plan interpolates by Lagrange's formula on the powers of the domain root.

```lean
theorem interpolate_eq_interpolatePow [BEq R] [LawfulBEq R]
    (P : Plan R) (hP : WellFormed P) (values : Vector R P.domain.n) :
    interpolate P values = CLagrange.interpolatePow P.domain.omega values
```

## Depends on

- [NTT and Interpolation](../ntt/interpolation.md)
- [Basic NTTFast correctness facts](correctness/basic.md)

## Proof depends on

- [NTTFast multiplication correctness](correctness/pipeline.md)

## Sources

- [CompPoly/Univariate/NTTFast/Interpolation.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Interpolation.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Interpolation.json)
