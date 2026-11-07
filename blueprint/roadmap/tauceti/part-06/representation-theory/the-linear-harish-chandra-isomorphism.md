---
declaration: def
origin: cited
lean: TauCeti.harishChandraLinearIso
statement: formalized
---

# The linear Harish-Chandra isomorphism

`Z(U(L)) ≃ₐ[K] S(H)^W`: the linear Harish-Chandra
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

- [Representation.symmetricAlgebraInvariants](../../part-03/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrainvariants.md)
- [Representation.symmetricAlgebraReynolds](../../part-03/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrareynolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harishChandraLinearIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraLinearIso).

## Sources

- [Tau Ceti documentation: `TauCeti.harishChandraLinearIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.harishChandraLinearIso)
- [Source of `TauCeti.harishChandraLinearIso` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean#L82)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
