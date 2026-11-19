---
declaration: theorem
origin: cited
lean: TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified
statement: formalized
proof: formalized
---

# TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified

For compatible extensions of nonarchimedean local fields, tameness with respect to the
valuation ring is equivalent to valuation-theoretic tameness. No separability hypothesis on
`L/K` is needed: the residue extension is separable because both residue fields are finite.

```lean
TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified.{u_1, u_2} (K : Type u_1) (L : Type u_2) [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L]
  [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] :
  TauCeti.Algebra.IsTamelyRamifiedWRT (↥(ValuativeRel.valuation K).integer) L ↔
    TauCeti.IsTamelyRamified K L
```

## Depends on

- [TauCeti.Algebra.IsTamelyRamifiedWRT](tauceti-algebra-istamelyramifiedwrt.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../../../number-theory/part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/TamelyRamified/Comparison.html#TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified).

## Sources

- [Tau Ceti documentation: `TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/TamelyRamified/Comparison.html#TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified)
- [Source of `TauCeti.isTamelyRamifiedWRT_iff_isTamelyRamified` in TauCeti/NumberTheory/LocalField/TamelyRamified/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/TamelyRamified/Comparison.lean#L43)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
