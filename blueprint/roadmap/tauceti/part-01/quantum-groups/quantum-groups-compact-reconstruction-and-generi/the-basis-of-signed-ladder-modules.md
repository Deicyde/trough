---
declaration: def
origin: cited
lean: TauCeti.UqSl2.repRingBasis
statement: formalized
---

# The basis of signed ladder modules

at a generic parameter, the classes `[L_m^ε]` of the
signed ladder modules, for `m : ℕ` and `ε = ±1`, form a `ℤ`-basis of the representation ring.

```lean
TauCeti.UqSl2.repRingBasis {q : ℂ} [Fact (q ≠ 0)] (hq : TauCeti.IsGenericQuantumParameter q) :
  Module.Basis (ℕ × ℤˣ) ℤ (TauCeti.UqSl2.repRing q)
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)

## Proof depends on

- [The character homomorphism is injective](the-character-homomorphism-is-injective.md)
- [Complete reducibility](complete-reducibility.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.repRingBasis`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/RepresentationRing.html#TauCeti.UqSl2.repRingBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.repRingBasis`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/RepresentationRing.html#TauCeti.UqSl2.repRingBasis)
- [Source of `TauCeti.UqSl2.repRingBasis` in TauCeti/QuantumGroups/UqSl2/RepresentationRing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/UqSl2/RepresentationRing.lean#L238)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
