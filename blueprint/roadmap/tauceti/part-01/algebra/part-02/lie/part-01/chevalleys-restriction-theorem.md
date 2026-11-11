---
declaration: def
origin: cited
lean: LieSubalgebra.lieChevalleyRestrictionIso, LieSubalgebra.map_lieInvariants_lieCartanRestriction, LieSubalgebra.lieCartanRestriction_injOn_lieInvariants
statement: formalized
---

# Chevalley's restriction theorem

Restriction of polynomial functions from `L` to `H`,
`TauCeti.lieCartanRestriction H`, is an isomorphism from the invariants `S(L)^L` onto the Weyl
invariants `S(H)^W`.

```lean
LieSubalgebra.lieChevalleyRestrictionIso.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [LieAlgebra.IsKilling K L]
  (H : LieSubalgebra K L) [H.IsCartanSubalgebra] [IsAlgClosed K] :
  ↥(TauCeti.SymmetricAlgebra.lieInvariants K L L) ≃ₐ[K] ↥(TauCeti.linearInvariants H)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy-Schwarz against a majorant](../../../../linear-algebra/bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [Representation.symmetricAlgebraInvariants](../../../../representation-theory/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrainvariants.md)
- [Representation.symmetricAlgebraReynolds](../../../../representation-theory/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrareynolds.md)

## Lean

Formalized in Tau Ceti as [`LieSubalgebra.lieChevalleyRestrictionIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.lieChevalleyRestrictionIso).

## Other forms

**Chevalley's restriction theorem, image form.** Formalized in Tau Ceti as [`LieSubalgebra.map_lieInvariants_lieCartanRestriction`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.map_lieInvariants_lieCartanRestriction).

```lean
LieSubalgebra.map_lieInvariants_lieCartanRestriction.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] (H : LieSubalgebra K L) [H.IsCartanSubalgebra] [IsAlgClosed K] :
  Subalgebra.map (TauCeti.lieCartanRestriction H) (TauCeti.SymmetricAlgebra.lieInvariants K L L) =
    TauCeti.linearInvariants H
```

**Chevalley's restriction theorem, injectivity.** Formalized in Tau Ceti as [`LieSubalgebra.lieCartanRestriction_injOn_lieInvariants`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/ChevalleyRestriction.html#LieSubalgebra.lieCartanRestriction_injOn_lieInvariants).

```lean
LieSubalgebra.lieCartanRestriction_injOn_lieInvariants.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] (H : LieSubalgebra K L) [H.IsCartanSubalgebra]
  [LieModule.IsTriangularizable K (↥H) L] :
  Set.InjOn ⇑(TauCeti.lieCartanRestriction H) ↑(TauCeti.SymmetricAlgebra.lieInvariants K L L)
```

## Sources

- [Tau Ceti documentation: `LieSubalgebra.lieChevalleyRestrictionIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.lieChevalleyRestrictionIso)
- [Source of `LieSubalgebra.lieChevalleyRestrictionIso` in TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean#L148)
