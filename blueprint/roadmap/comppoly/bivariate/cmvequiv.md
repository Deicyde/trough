---
catalog: module
lean: CMvPolynomial.isEmptyRingEquiv_symm_apply, CMvPolynomial.finSuccEquiv_symm_C, CMvPolynomial.finSuccEquiv_symm_X, CompPoly.CBivariate.bivariateEquiv, CompPoly.CBivariate.bivariateEquiv_add, CompPoly.CBivariate.bivariateEquiv_mul, CompPoly.CBivariate.bivariateEquiv_zero, CompPoly.CBivariate.bivariateEquiv_CC, CompPoly.CBivariate.bivariateEquiv_X, CompPoly.CBivariate.bivariateEquiv_Y, CompPoly.CBivariate.bivariateEquiv_symm_C, CompPoly.CBivariate.bivariateEquiv_symm_X0, CompPoly.CBivariate.bivariateEquiv_symm_X1
statement: formalized
proof: formalized
---

# Equivalence between `CBivariate` and `CMvPolynomial 2`

`CompPoly.Bivariate.CMvEquiv`, in [CompPoly/Bivariate/CMvEquiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean), by Dimitris Mitsios.

> This file establishes the ring equivalence
> `bivariateEquiv : CBivariate R ≃+* CMvPolynomial 2 R`
> by composing `CBivariate.ringEquiv` with `CMvPolynomial.finSuccEquiv`
> and `CMvPolynomial.isEmptyRingEquiv`.
>
> The equivalence chain is:
>   `CBivariate R ≃ R[X][Y] ≃ (CMvPolynomial 0 R)[X][Y]
>     ≃ (CMvPolynomial 1 R)[Y] ≃ CMvPolynomial 2 R`
>
> ## Main definitions
>
> * `bivariateEquiv` — ring equivalence `CBivariate R ≃+* CMvPolynomial 2 R`
>
> ## Bridge lemmas
>
> * `bivariateEquiv_CC` — `bivariateEquiv (CC r) = C r`
> * `bivariateEquiv_X` — `bivariateEquiv X = CMvPolynomial.X 1`
> * `bivariateEquiv_Y` — `bivariateEquiv Y = CMvPolynomial.X 0`
> * `bivariateEquiv_symm_C` — `bivariateEquiv.symm (C r) = CC r`
> * `bivariateEquiv_symm_X0` — `bivariateEquiv.symm (X 0) = Y`
> * `bivariateEquiv_symm_X1` — `bivariateEquiv.symm (X 1) = X`
>
> ## Helper lemmas (for `CMvPolynomial.finSuccEquiv`)
>
> * `CMvPolynomial.isEmptyRingEquiv_symm_apply` —
>   `isEmptyRingEquiv.symm r = C r`
> * `CMvPolynomial.finSuccEquiv_symm_C` —
>   `finSuccEquiv.symm (Polynomial.C x) = rename Fin.succ x`
> * `CMvPolynomial.finSuccEquiv_symm_X` —
>   `finSuccEquiv.symm Polynomial.X = CMvPolynomial.X 0`

`CMvPolynomial.isEmptyRingEquiv_symm_apply` (lemma, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L58))

> `isEmptyRingEquiv.symm` maps scalars to constants.

```lean
lemma isEmptyRingEquiv_symm_apply
    {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R] (r : R) :
    CMvPolynomial.isEmptyRingEquiv.symm r = CMvPolynomial.C r
```

`CMvPolynomial.finSuccEquiv_symm_C` (lemma, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L67))

> `finSuccEquiv.symm` maps `Polynomial.C` to `rename Fin.succ`.

```lean
lemma finSuccEquiv_symm_C
    {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    {n : ℕ} (x : CMvPolynomial n R) :
    CMvPolynomial.finSuccEquiv.symm (Polynomial.C x) =
      CMvPolynomial.rename Fin.succ x
```

`CMvPolynomial.finSuccEquiv_symm_X` (lemma, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L97))

> `finSuccEquiv.symm` maps `Polynomial.X` to the zeroth variable.

```lean
lemma finSuccEquiv_symm_X
    {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R]
    {n : ℕ} :
    CMvPolynomial.finSuccEquiv.symm
      (Polynomial.X : Polynomial (CMvPolynomial n R)) =
      CMvPolynomial.X 0
```

`CompPoly.CBivariate.bivariateEquiv` (definition, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L128))

> Ring equivalence between `CBivariate R` and `CMvPolynomial 2 R`.

```lean
noncomputable def bivariateEquiv :
    CBivariate R ≃+* CMvPolynomial 2 R
```

`CompPoly.CBivariate.bivariateEquiv_add` (lemma, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L142))

> `bivariateEquiv` preserves addition.

```lean
lemma bivariateEquiv_add (p q : CBivariate R) :
    bivariateEquiv (p + q) =
      bivariateEquiv p + bivariateEquiv q
```

`CompPoly.CBivariate.bivariateEquiv_mul` (lemma, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L149))

> `bivariateEquiv` preserves multiplication.

```lean
lemma bivariateEquiv_mul (p q : CBivariate R) :
    bivariateEquiv (p * q) =
      bivariateEquiv p * bivariateEquiv q
```

`CompPoly.CBivariate.bivariateEquiv_zero` (lemma, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L156))

> `bivariateEquiv` maps zero to zero.

```lean
lemma bivariateEquiv_zero :
    bivariateEquiv (0 : CBivariate R) = 0
```

`CompPoly.CBivariate.bivariateEquiv_CC` (lemma, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L162))

> `bivariateEquiv` maps bivariate constants to multivariate constants.

```lean
lemma bivariateEquiv_CC (r : R) :
    bivariateEquiv (CBivariate.CC r) = CMvPolynomial.C r
```

`CompPoly.CBivariate.bivariateEquiv_X` (lemma, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L171))

> `bivariateEquiv` maps `CBivariate.X` to the second variable.

```lean
lemma bivariateEquiv_X :
    bivariateEquiv (CBivariate.X : CBivariate R) =
      CMvPolynomial.X 1
```

`CompPoly.CBivariate.bivariateEquiv_Y` (lemma, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L179))

> `bivariateEquiv` maps `CBivariate.Y` to the first variable.

```lean
lemma bivariateEquiv_Y :
    bivariateEquiv (CBivariate.Y : CBivariate R) =
      CMvPolynomial.X 0
```

`CompPoly.CBivariate.bivariateEquiv_symm_C` (lemma, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L187))

> `bivariateEquiv.symm` maps multivariate constants to bivariate constants.

```lean
lemma bivariateEquiv_symm_C (r : R) :
    bivariateEquiv.symm (CMvPolynomial.C r) =
      CBivariate.CC r
```

`CompPoly.CBivariate.bivariateEquiv_symm_X0` (lemma, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L195))

> `bivariateEquiv.symm` maps the first variable to `CBivariate.Y`.

```lean
lemma bivariateEquiv_symm_X0 :
    bivariateEquiv.symm (CMvPolynomial.X 0 : CMvPolynomial 2 R) =
      CBivariate.Y
```

`CompPoly.CBivariate.bivariateEquiv_symm_X1` (lemma, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean#L203))

> `bivariateEquiv.symm` maps the second variable to `CBivariate.X`.

```lean
lemma bivariateEquiv_symm_X1 :
    bivariateEquiv.symm (CMvPolynomial.X 1 : CMvPolynomial 2 R) =
      CBivariate.X
```

## Depends on

- [Equivalence with Mathlib Bivariate Polynomials](topoly.md)
- [`finSuccEquiv` for `CMvPolynomial`](../multivariate/finsuccequiv.md)
- [Computable multivariate polynomials (extended operations)](../multivariate/operations.md)

## Proof depends on

- [Properties of variable renaming for `CMvPolynomial`](../multivariate/rename.md)

## Sources

- [CompPoly/Bivariate/CMvEquiv.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/CMvEquiv.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.CMvEquiv.json)
