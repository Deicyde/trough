---
catalog: module
lean: CPoly.eval₂_equiv, CPoly.eval_equiv, CPoly.totalDegree_equiv, CPoly.degreeOf_equiv, CPoly.CMvPolynomial.eval₂Hom, CPoly.CMvPolynomial.eval₂Hom_apply
statement: formalized
proof: formalized
---

# `CMvPolynomial`/`MvPolynomial` Evaluation

`CompPoly.Multivariate.MvPolyEquiv.Eval`, in [CompPoly/Multivariate/MvPolyEquiv/Eval.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa, Dimitris Mitsios.

> Evaluation lemmas for the `CMvPolynomial` and `MvPolynomial` conversions.

`CPoly.eval₂_equiv` (lemma, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean#L29))

```lean
lemma eval₂_equiv {S : Type*} {p : CMvPolynomial n R} [CommSemiring S] {f : (R →+* S)}
    {vals : Fin n → S} : p.eval₂ f vals = (fromCMvPolynomial p).eval₂ f vals
```

`CPoly.eval_equiv` (lemma, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean#L53))

```lean
lemma eval_equiv {p : CMvPolynomial n R} {vals : Fin n → R} :
    p.eval vals = (fromCMvPolynomial p).eval vals
```

`CPoly.totalDegree_equiv` (lemma, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean#L60))

```lean
lemma totalDegree_equiv {S : Type*} {p : CMvPolynomial n R} [CommSemiring S] :
    p.totalDegree = (fromCMvPolynomial p).totalDegree
```

`CPoly.degreeOf_equiv` (lemma, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean#L64))

```lean
lemma degreeOf_equiv {S : Type*} {p : CMvPolynomial n R} [CommSemiring S] :
    p.degreeOf = (fromCMvPolynomial p).degreeOf
```

`CPoly.CMvPolynomial.eval₂Hom` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean#L88))

> `eval₂` as a ring homomorphism.

```lean
def eval₂Hom {S : Type*} [CommSemiring S]
    (f : R →+* S) (vs : Fin n → S) : CMvPolynomial n R →+* S
```

`CPoly.CMvPolynomial.eval₂Hom_apply` (lemma, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean#L97))

```lean
lemma eval₂Hom_apply {S : Type*} [CommSemiring S]
    (f : R →+* S) (vs : Fin n → S) (p : CMvPolynomial n R) :
    eval₂Hom f vs p = eval₂ f vs p
```

## Depends on

- [`CMvPolynomial`/`MvPolynomial` Instances](instances.md)

## Sources

- [CompPoly/Multivariate/MvPolyEquiv/Eval.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multivariate/MvPolyEquiv/Eval.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Multivariate.MvPolyEquiv.Eval.json)
