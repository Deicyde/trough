---
declaration: def
origin: cited
lean: TauCeti.UqSl2.polynomialAlgEquivCenter
statement: formalized
---

# TauCeti.UqSl2.polynomialAlgEquivCenter

At a generic parameter, the center of `U_q(sl₂)` is a polynomial algebra in one variable:
evaluation at the Casimir element is an isomorphism `ℂ[X] ≃ₐ[ℂ] Z(U_q(sl₂))`.

```lean
TauCeti.UqSl2.polynomialAlgEquivCenter {q : ℂ} (hq : TauCeti.IsGenericQuantumParameter q) :
  Polynomial ℂ ≃ₐ[ℂ] ↥(Subalgebra.center ℂ (TauCeti.UqSl2 q))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.OreExtension](tauceti-oreextension.md)
- [TauCeti.UqSl2.pbwBasis](tauceti-uqsl2-pbwbasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.polynomialAlgEquivCenter`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Center.html#TauCeti.UqSl2.polynomialAlgEquivCenter).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.polynomialAlgEquivCenter`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Center.html#TauCeti.UqSl2.polynomialAlgEquivCenter)
- [Source of `TauCeti.UqSl2.polynomialAlgEquivCenter` in TauCeti/QuantumGroups/UqSl2/Center.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/QuantumGroups/UqSl2/Center.lean#L185)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuantumGroups/STATUS.md)
