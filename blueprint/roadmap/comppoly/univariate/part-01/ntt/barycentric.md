---
catalog: module
lean: CompPoly.CPolynomial.NTT.Domain.node_injective, CompPoly.CPolynomial.NTT.Domain.node_pow_n, CompPoly.CPolynomial.NTT.Domain.nodal_eq_X_pow_sub_one, CompPoly.CPolynomial.NTT.Domain.nodalWeight_eq, CompPoly.CPolynomial.NTT.Domain.barycentric, CompPoly.CPolynomial.NTT.Domain.barycentric_nodes, CompPoly.CPolynomial.NTT.Domain.barycentric_eval_eq_interpolatePow_eval
statement: formalized
proof: formalized
---

# Barycentric Interpolation on an NTT Domain

`CompPoly.Univariate.NTT.Barycentric`, in [CompPoly/Univariate/NTT/Barycentric.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean), by Derek Sorensen.

> On the full group of `n`-th roots of unity the nodal polynomial is `Xⁿ - 1`, so the
> barycentric weight of the node `ωⁱ` has the closed form `ωⁱ / n`. This file builds the
> `BarycentricDomain` of an NTT domain from that formula, in `O(n)` field operations and one
> inversion, rather than through the generic `O(n²)` product of `BarycentricDomain.mk'`.
>
> ## Main definitions
>
> * `NTT.Domain.barycentric`: the barycentric domain of `D`, with weights `ωⁱ · n⁻¹`.
>
> ## Main results
>
> * `NTT.Domain.nodal_eq_X_pow_sub_one`: the nodal polynomial of the domain is `Xⁿ - 1`.
> * `NTT.Domain.nodalWeight_eq`: the barycentric weight of `ωⁱ` is `ωⁱ · n⁻¹`.
> * `NTT.Domain.barycentric_eval_eq_interpolatePow_eval`: evaluating through the domain is
>   evaluating `CLagrange.interpolatePow D.omega`.

`CompPoly.CPolynomial.NTT.Domain.node_injective` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean#L43))

> The nodes of an NTT domain are pairwise distinct.

```lean
theorem node_injective (D : Domain R) : Function.Injective D.node
```

`CompPoly.CPolynomial.NTT.Domain.node_pow_n` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean#L47))

> Every node of an NTT domain is an `n`-th root of unity.

```lean
theorem node_pow_n (D : Domain R) (i : D.Idx) : D.node i ^ D.n = 1
```

`CompPoly.CPolynomial.NTT.Domain.nodal_eq_X_pow_sub_one` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean#L52))

> The nodal polynomial of an NTT domain is `Xⁿ - 1`.

```lean
theorem nodal_eq_X_pow_sub_one (D : Domain R) :
    Lagrange.nodal Finset.univ D.node = Polynomial.X ^ D.n - 1
```

`CompPoly.CPolynomial.NTT.Domain.nodalWeight_eq` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean#L68))

> The barycentric weight of the node `ωⁱ` of an NTT domain is `ωⁱ / n`.

```lean
theorem nodalWeight_eq (D : Domain R) (i : D.Idx) :
    Lagrange.nodalWeight Finset.univ D.node i = D.node i * D.nInv
```

`CompPoly.CPolynomial.NTT.Domain.barycentric` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean#L82))

> The barycentric domain of an NTT domain, with the closed-form weights `ωⁱ · n⁻¹`.

```lean
def barycentric [DecidableEq R] (D : Domain R) : CLagrange.BarycentricDomain R D.n
```

`CompPoly.CPolynomial.NTT.Domain.barycentric_nodes` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean#L95))

```lean
theorem barycentric_nodes [DecidableEq R] (D : Domain R) (i : D.Idx) :
    D.barycentric.nodes i = D.node i
```

`CompPoly.CPolynomial.NTT.Domain.barycentric_eval_eq_interpolatePow_eval` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean#L100))

> Barycentric evaluation on an NTT domain is evaluation of `CLagrange.interpolatePow`.

```lean
theorem barycentric_eval_eq_interpolatePow_eval [DecidableEq R] [BEq R] [LawfulBEq R]
    (D : Domain R) (values : Vector R D.n) (z : R) :
    D.barycentric.eval values.get z =
      (CLagrange.interpolatePow D.omega values).eval z
```

## Depends on

- [Barycentric Interpolation](../barycentric.md)
- [NTT Domain](domain.md)

## Sources

- [CompPoly/Univariate/NTT/Barycentric.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Barycentric.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Barycentric.json)
