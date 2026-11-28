---
catalog: module
lean: CPoly.fromCMvPolynomial, CPoly.toCMvPolynomial, CPoly.toCMvPolynomial_fromCMvPolynomial, CPoly.fromCMvPolynomial_toCMvPolynomial, CPoly.fromCMvPolynomial_injective, CPoly.coeff_eq, CPoly.eq_iff_fromCMvPolynomial, CPoly.polyEquiv
statement: formalized
proof: formalized
---

# `CMvPolynomial`/`MvPolynomial` Core

`CompPoly.Multivariate.MvPolyEquiv.Core`, in [CompPoly/Multivariate/MvPolyEquiv/Core.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa, Dimitris Mitsios.

> Core conversions between `CMvPolynomial` and `MvPolynomial`.

`CPoly.fromCMvPolynomial` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L35))

```lean
def fromCMvPolynomial  (p : CMvPolynomial n R) : MvPolynomial (Fin n) R
```

`CPoly.toCMvPolynomial` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L41))

```lean
noncomputable def toCMvPolynomial (p : MvPolynomial (Fin n) R) : CMvPolynomial n R
```

`CPoly.toCMvPolynomial_fromCMvPolynomial` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L73))

```lean
theorem toCMvPolynomial_fromCMvPolynomial {p : CMvPolynomial n R} :
    toCMvPolynomial (fromCMvPolynomial p) = p
```

`CPoly.fromCMvPolynomial_toCMvPolynomial` (theorem, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L91))

```lean
theorem fromCMvPolynomial_toCMvPolynomial {p : MvPolynomial (Fin n) R} :
    fromCMvPolynomial (toCMvPolynomial p) = p
```

`CPoly.fromCMvPolynomial_injective` (lemma, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L115))

```lean
lemma fromCMvPolynomial_injective : Function.Injective (@fromCMvPolynomial n R _)
```

`CPoly.coeff_eq` (lemma, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L121))

```lean
lemma coeff_eq {m} (a : CMvPolynomial n R) :
    (fromCMvPolynomial a).coeff m = a.coeff (CMvMonomial.ofFinsupp m)
```

`CPoly.eq_iff_fromCMvPolynomial` (lemma, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L126))

```lean
lemma eq_iff_fromCMvPolynomial {u v: CMvPolynomial n R} :
    u = v ↔ fromCMvPolynomial u = fromCMvPolynomial v
```

`CPoly.polyEquiv` (definition, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean#L134))

```lean
noncomputable def polyEquiv :
    Equiv (CMvPolynomial n R) (MvPolynomial (Fin n) R)
```

## Depends on

- [Computable multivariate polynomials](../basic.md)

## Proof depends on

- [Auxiliary lemmas for `List`](../../data/list/lemmas.md)

## Sources

- [CompPoly/Multivariate/MvPolyEquiv/Core.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Core.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Multivariate.MvPolyEquiv.Core.json)
