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

- [Harish-Chandra surjectivity with a degree bound](../../part-02/lie/part-01/harish-chandra-surjectivity-with-a-degree-bound.md)
- [The linear-independence half of the Poincaré--Birkhoff--Witt theorem](../../part-02/lie/part-01/the-linear-independence-half-of-the-poincare-bir.md)
- [The Poincaré--Birkhoff--Witt theorem](../../part-02/lie/part-01/the-poincare-birkhoff-witt-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.vermaCentralCharacter_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.vermaCentralCharacter_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.vermaCentralCharacter_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.html#TauCeti.vermaCentralCharacter_eq_iff)
- [Source of `TauCeti.vermaCentralCharacter_eq_iff` in TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/HighestWeight/CentralCharacter/Isomorphism.lean#L156)
