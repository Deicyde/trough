---
declaration: theorem
origin: cited
lean: TauCeti.vermaCentralCharacter_eq_iff
statement: formalized
proof: formalized
---

# Harish-Chandra's theorem on central characters

two weights `lam` and `mu` have the same
central character, `χ_lam = χ_mu`, exactly when `mu` lies in the dot orbit of `lam`, that is
`mu = w · lam = w (lam + ρ) - ρ` for an element `w` of the Weyl group.

```lean
TauCeti.vermaCentralCharacter_eq_iff.{v} {K : Type} {L : Type v} [Field K] [CharZero K]
  [IsAlgClosed K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [FiniteDimensional K L]
  {H : LieSubalgebra K L} [H.IsCartanSubalgebra] [LieModule.IsTriangularizable K (↥H) L]
  (b : (LieAlgebra.IsKilling.rootSystem H).Base) {lam mu : Module.Dual K ↥H} :
  TauCeti.vermaCentralCharacter b lam = TauCeti.vermaCentralCharacter b mu ↔
    ∃ w, TauCeti.dotAction (LieAlgebra.IsKilling.rootSystem H) b w lam = mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Representation.symmetricAlgebraInvariants](../../part-03/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrainvariants.md)
- [Representation.symmetricAlgebraReynolds](../../part-03/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrareynolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.vermaCentralCharacter_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.vermaCentralCharacter_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.vermaCentralCharacter_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.vermaCentralCharacter_eq_iff)
- [Source of `TauCeti.vermaCentralCharacter_eq_iff` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean#L156)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
