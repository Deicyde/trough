---
catalog: module
lean: CompPoly.Extension.ExtensionParams.card_eq, CompPoly.Extension.BinomialParams.card_eq, CompPoly.Extension.Ext.instFinite, CompPoly.Extension.Ext.instFintype, CompPoly.Extension.Ext.card_ext, CompPoly.Extension.Ext.nat_card_ext
statement: formalized
proof: formalized
---

# Finiteness and cardinality of monic quotient presentations

`CompPoly.Fields.Extension.Cardinality`, in [CompPoly/Fields/Extension/Cardinality.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean), by Derek Sorensen.

> The coordinate equivalence gives `Finite (Ext P)` from `Finite F`, and gives an optional
> `Fintype (Ext P)` when an enumeration of the base is available. A separate certificate
> `Fact (Nat.card F = P.q)` identifies the stored exponent parameter with the base cardinality.
> The resulting extension cardinality is `P.q ^ P.d`.
>
> These facts require neither a polynomial quotient bridge nor irreducibility. All finiteness
> and cardinality assumptions used by field laws are propositions, so executable arithmetic
> never receives an enumeration dictionary merely to use those laws.

`CompPoly.Extension.ExtensionParams.card_eq` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean#L29))

> The certified cardinality agrees with any enumeration of the base type.

```lean
theorem ExtensionParams.card_eq {F : Type*} [Fintype F] (P : ExtensionParams F)
    [Fact (Nat.card F = P.q)] : Fintype.card F = P.q
```

`CompPoly.Extension.BinomialParams.card_eq` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean#L35))

> The certified binomial base cardinality agrees with any enumeration.

```lean
theorem BinomialParams.card_eq {F : Type*} [Fintype F] (P : BinomialParams F)
    [Fact (Nat.card F = P.q)] : Fintype.card F = P.q
```

`CompPoly.Extension.Ext.instFinite` (instance, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean#L49))

```lean
instance instFinite [Finite F] : Finite (Ext P)
```

`CompPoly.Extension.Ext.instFintype` (instance, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean#L52))

```lean
instance instFintype [Fintype F] : Fintype (Ext P)
```

`CompPoly.Extension.Ext.card_ext` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean#L55))

> The enumerated extension cardinality is the certified base cardinality to the degree.

```lean
theorem card_ext [Fintype F] [Fact (Nat.card F = P.q)] : Fintype.card (Ext P) = P.q ^ P.d
```

`CompPoly.Extension.Ext.nat_card_ext` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean#L59))

> The extension has `q^d` elements, independently of any chosen enumeration.

```lean
theorem nat_card_ext [Finite F] [Fact (Nat.card F = P.q)] :
    Nat.card (Ext P) = P.q ^ P.d
```

## Depends on

- [Computable arithmetic for monic quotient presentations](arithmetic.md)

## Sources

- [CompPoly/Fields/Extension/Cardinality.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Extension/Cardinality.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Extension.Cardinality.json)
