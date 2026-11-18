---
declaration: def
origin: cited
lean: TauCeti.FormalGroupAdicSystem.completeEquiv
statement: formalized
---

# TauCeti.FormalGroupAdicSystem.completeEquiv

Over an adically complete ring, commutative laws are equivalent to compatible systems
of commutative quotient laws.

```lean
TauCeti.FormalGroupAdicSystem.completeEquiv.{u_1} {R : Type u_1} [CommRing R] (I : Ideal R)
  [IsAdicComplete I R] : { F // F.IsComm } ≃ TauCeti.FormalGroupAdicSystem I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalGroupAdicSystem.completeEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/AdicCompletion.html#TauCeti.FormalGroupAdicSystem.completeEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalGroupAdicSystem.completeEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/AdicCompletion.html#TauCeti.FormalGroupAdicSystem.completeEquiv)
- [Source of `TauCeti.FormalGroupAdicSystem.completeEquiv` in TauCeti/RingTheory/FormalGroup/AdicCompletion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/AdicCompletion.lean#L292)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
