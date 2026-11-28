---
catalog: module
lean: CompPoly.Extension.ExtensionParams.poly, CompPoly.Extension.ExtensionParams.degree_lower_lt, CompPoly.Extension.ExtensionParams.degree_poly, CompPoly.Extension.ExtensionParams.monic_poly, CompPoly.Extension.ExtensionParams.natDegree_poly, CompPoly.Extension.BinomialParams.poly, CompPoly.Extension.BinomialParams.natDegree_poly, CompPoly.Extension.BinomialParams.monic_poly, CompPoly.Extension.BinomialParams.toExtensionParams_poly
statement: formalized
proof: formalized
---

# Polynomial specifications for monic quotient presentations

`CompPoly.Fields.Extension.Defs`, in [CompPoly/Fields/Extension/Defs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean), by Derek Sorensen.

> `ExtensionParams.poly` interprets the lower coefficient vector as the monic polynomial
> `X^d + ∑ i, C lower[i] * X^i`. The binomial specification is `X^d - W`; its conversion to
> an arbitrary monic presentation preserves that polynomial.
>
> The carrier and executable operations are defined in `Extension/Arithmetic.lean`. These
> specifications do not certify the cardinality parameter or irreducibility. The quotient bridge
> and field laws are supplied separately in `Extension/Bridge.lean` and `Extension/Field.lean`.

`CompPoly.Extension.ExtensionParams.poly` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L37))

> The monic defining polynomial `X^d + ∑_{i < d} lower[i] · X^i`. Part of the specification
> only; the computable arithmetic on `Ext P` never evaluates it.

```lean
noncomputable def poly : F[X]
```

`CompPoly.Extension.ExtensionParams.degree_lower_lt` (theorem, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L40))

> The lower part of the modulus has degree strictly less than `d`.

```lean
theorem degree_lower_lt :
    (∑ i : Fin P.d, C (P.lowerCoeff i) * X ^ (i : ℕ)).degree < (P.d : WithBot ℕ)
```

`CompPoly.Extension.ExtensionParams.degree_poly` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L47))

```lean
theorem degree_poly : P.poly.degree = (P.d : WithBot ℕ)
```

`CompPoly.Extension.ExtensionParams.monic_poly` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L51))

```lean
theorem monic_poly : P.poly.Monic
```

`CompPoly.Extension.ExtensionParams.natDegree_poly` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L55))

```lean
theorem natDegree_poly : P.poly.natDegree = P.d
```

`CompPoly.Extension.BinomialParams.poly` (definition, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L65))

> The defining polynomial `X^d - W`. Part of the specification only.

```lean
noncomputable def poly : F[X]
```

`CompPoly.Extension.BinomialParams.natDegree_poly` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L67))

```lean
theorem natDegree_poly : P.poly.natDegree = P.d
```

`CompPoly.Extension.BinomialParams.monic_poly` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L69))

```lean
theorem monic_poly : P.poly.Monic
```

`CompPoly.Extension.BinomialParams.toExtensionParams_poly` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean#L72))

> The general-framework polynomial of a binomial agrees with `X^d - W`.

```lean
theorem toExtensionParams_poly : P.toExtensionParams.poly = P.poly
```

## Depends on

- [Computable arithmetic for monic quotient presentations](arithmetic.md)

## Sources

- [CompPoly/Fields/Extension/Defs.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Defs.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Extension.Defs.json)
