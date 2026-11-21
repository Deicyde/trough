---
catalog: module
lean: CompPoly.CPolynomial.NTT.Inverse.inttAt, CompPoly.CPolynomial.NTT.Inverse.inverseSpec, CompPoly.CPolynomial.NTT.Inverse.normalize, CompPoly.CPolynomial.NTT.Inverse.size_inverseSpec, CompPoly.CPolynomial.NTT.Inverse.size_normalize, CompPoly.CPolynomial.NTT.Inverse.normalize_forwardSpec_inverse_eq_inverseSpec, CompPoly.CPolynomial.NTT.Inverse.inverseImpl, CompPoly.CPolynomial.NTT.Inverse.inverseImpl_correct
statement: formalized
proof: formalized
---

# Inverse NTT

`CompPoly.Univariate.NTT.Inverse`, in [CompPoly/Univariate/NTT/Inverse.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean), by Salih Erdem Koçak, Doran Pamukçu.

> This file provides inverse NTT APIs and correctness statement.

`CompPoly.CPolynomial.NTT.Inverse.inttAt` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L29))

> Inverse NTT formula at one output index.

```lean
def inttAt (D : Domain R) (v : Array R) (k : D.Idx) : R
```

`CompPoly.CPolynomial.NTT.Inverse.inverseSpec` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L33))

> Full inverse transform on arrays, specified from `inttAt`.

```lean
def inverseSpec (D : Domain R) (v : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Inverse.normalize` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L37))

> Apply the final `n⁻¹` normalization for the inverse transform.

```lean
def normalize (D : Domain R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Inverse.size_inverseSpec` (theorem, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L40))

```lean
theorem size_inverseSpec (D : Domain R) (v : Array R) :
    (inverseSpec D v).size = D.n
```

`CompPoly.CPolynomial.NTT.Inverse.size_normalize` (theorem, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L44))

```lean
theorem size_normalize (D : Domain R) (a : Array R) :
    (normalize D a).size = D.n
```

`CompPoly.CPolynomial.NTT.Inverse.normalize_forwardSpec_inverse_eq_inverseSpec` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L48))

```lean
theorem normalize_forwardSpec_inverse_eq_inverseSpec (D : Domain R) (v : Array R) :
    normalize D (Forward.forwardSpec D.inverse v) = inverseSpec D v
```

`CompPoly.CPolynomial.NTT.Inverse.inverseImpl` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L59))

> Intended fast implementation entry point for inverse NTT.

```lean
def inverseImpl (D : Domain R) (v : Array R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTT.Inverse.inverseImpl_correct` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean#L62))

```lean
theorem inverseImpl_correct (D : Domain R) (v : Array R) :
    inverseImpl D v = inverseSpec D v
```

## Depends on

- [Forward NTT](forward.md)

## Sources

- [CompPoly/Univariate/NTT/Inverse.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Inverse.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Inverse.json)
