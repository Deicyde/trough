---
declaration: def
origin: cited
lean: TauCeti.harishChandraLinearIso
statement: formalized
---

# The linear Harish-Chandra isomorphism `Z(U(L)) ≃ₐ[K] S(H)^W`

the linear Harish-Chandra
projection `TauCeti.hcProjectionLinear b`, with its values in the Weyl invariants.

```lean
TauCeti.harishChandraLinearIso.{v} {K : Type} {L : Type v} [Field K] [CharZero K] [IsAlgClosed K]
  [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  {H : LieSubalgebra K L} [H.IsCartanSubalgebra] [LieModule.IsTriangularizable K (↥H) L]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) :
  ↥(Subalgebra.center K (UniversalEnvelopingAlgebra K L)) ≃ₐ[K] ↥(TauCeti.linearInvariants H)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chevalley's restriction theorem](../../part-02/lie/part-01/chevalleys-restriction-theorem.md)
- [Harish-Chandra surjectivity with a degree bound](../../part-02/lie/part-01/harish-chandra-surjectivity-with-a-degree-bound.md)
- [The linear-independence half of the Poincaré--Birkhoff--Witt theorem](../../part-02/lie/part-01/the-linear-independence-half-of-the-poincare-bir.md)
- [The Poincaré--Birkhoff--Witt theorem](../../part-02/lie/part-02/the-poincare-birkhoff-witt-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harishChandraLinearIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraLinearIso).

## Sources

- [Tau Ceti documentation: `TauCeti.harishChandraLinearIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraLinearIso)
- [Source of `TauCeti.harishChandraLinearIso` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean#L82)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
