---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.repRingCharacter_injective
statement: formalized
proof: formalized
---

# The character homomorphism is injective

at a generic parameter, an element of the
representation ring is determined by its character.

```lean
TauCeti.UqSl2.repRingCharacter_injective {q : ℂ} [Fact (q ≠ 0)]
  (hq : TauCeti.IsGenericQuantumParameter q) :
  Function.Injective ⇑(TauCeti.UqSl2.repRingCharacter hq)
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)

## Proof depends on

- [Complete reducibility](complete-reducibility.md)
- [The multiplicity theorem](../../ring-theory/part-02/semisimple/the-multiplicity-theorem.md)
- [Schur's lemma, vanishing form](../../ring-theory/part-02/semisimple/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.repRingCharacter_injective`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/RepresentationRing.html#TauCeti.UqSl2.repRingCharacter_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.repRingCharacter_injective`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/RepresentationRing.html#TauCeti.UqSl2.repRingCharacter_injective)
- [Source of `TauCeti.UqSl2.repRingCharacter_injective` in TauCeti/QuantumGroups/UqSl2/RepresentationRing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/UqSl2/RepresentationRing.lean#L164)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
