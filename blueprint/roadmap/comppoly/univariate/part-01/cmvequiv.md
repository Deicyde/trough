---
catalog: module
lean: CompPoly.CPolynomial.cmvEquiv, CompPoly.CPolynomial.eval_cmvEquiv_symm, CompPoly.CPolynomial.natDegree_cmvEquiv_symm_sub
statement: formalized
proof: formalized
---

# Equivalence between `CPolynomial` and `CMvPolynomial 1`

`CompPoly.Univariate.CMvEquiv`, in [CompPoly/Univariate/CMvEquiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CMvEquiv.lean), by Andrew Zitek-Estrada.

> This file establishes the ring equivalence
> `CPolynomial.cmvEquiv : CPolynomial R ≃+* CMvPolynomial 1 R`.
>
> The equivalence chain is:
>   `CPolynomial R ≃ R[X] ≃ (CMvPolynomial 0 R)[X] ≃ CMvPolynomial 1 R`
>
> The bridge lemmas expose how the inverse equivalence interacts with evaluation
> and degree, so one-variable results proved for `CPolynomial` can be transported
> to callers that still use `CMvPolynomial 1`.

`CompPoly.CPolynomial.cmvEquiv` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CMvEquiv.lean#L39))

> Ring equivalence between computable univariate polynomials and
> single-variable computable multivariate polynomials.

```lean
noncomputable def cmvEquiv
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R] :
    CPolynomial R ≃+* CMvPolynomial 1 R
```

`CompPoly.CPolynomial.eval_cmvEquiv_symm` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CMvEquiv.lean#L135))

> Evaluation after converting a single-variable `CMvPolynomial` back to
> `CPolynomial` agrees with multivariate evaluation at the constant assignment.

```lean
theorem eval_cmvEquiv_symm
    [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (p : CMvPolynomial 1 R) (x : R) :
    ((cmvEquiv (R := R)).symm p).eval x = p.eval (fun _ ↦ x)
```

`CompPoly.CPolynomial.natDegree_cmvEquiv_symm_sub` (theorem, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CMvEquiv.lean#L142))

> Degree transport for differences through the inverse of `cmvEquiv`.

```lean
theorem natDegree_cmvEquiv_symm_sub
    [CommRing R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (p q : CMvPolynomial 1 R) :
    (((cmvEquiv (R := R)).symm p - (cmvEquiv (R := R)).symm q).natDegree) =
      (fromCMvPolynomial p - fromCMvPolynomial q).degreeOf 0
```

## Depends on

- [`finSuccEquiv` for `CMvPolynomial`](../../multivariate/finsuccequiv.md)

## Sources

- [CompPoly/Univariate/CMvEquiv.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CMvEquiv.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.CMvEquiv.json)
