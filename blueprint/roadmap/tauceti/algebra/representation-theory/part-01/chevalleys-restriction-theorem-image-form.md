---
declaration: theorem
origin: cited
lean: LieSubalgebra.map_lieInvariants_lieCartanRestriction, LieSubalgebra.lieCartanRestriction_injOn_lieInvariants
statement: formalized
proof: formalized
---

# Chevalley's restriction theorem, image form

Restriction to `H` maps the invariants
`S(L)^L` onto the Weyl invariants `S(H)^W`.

```lean
LieSubalgebra.map_lieInvariants_lieCartanRestriction.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] (H : LieSubalgebra K L) [H.IsCartanSubalgebra] [IsAlgClosed K] :
  Subalgebra.map (TauCeti.lieCartanRestriction H) (TauCeti.SymmetricAlgebra.lieInvariants K L L) =
    TauCeti.linearInvariants H
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Killing duality is Weyl-equivariant](../../lie/the-killing-duality-is-weyl-equivariant.md)
- [Representation.symmetricAlgebraInvariants](../../../representation-theory/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrainvariants.md)
- [Representation.symmetricAlgebraReynolds](../../../representation-theory/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrareynolds.md)

## Lean

Formalized in Tau Ceti as [`LieSubalgebra.map_lieInvariants_lieCartanRestriction`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.map_lieInvariants_lieCartanRestriction).

## Other forms

**Chevalley's restriction theorem, injectivity.** Formalized in Tau Ceti as [`LieSubalgebra.lieCartanRestriction_injOn_lieInvariants`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/ChevalleyRestriction.html#LieSubalgebra.lieCartanRestriction_injOn_lieInvariants).

```lean
LieSubalgebra.lieCartanRestriction_injOn_lieInvariants.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] (H : LieSubalgebra K L) [H.IsCartanSubalgebra]
  [LieModule.IsTriangularizable K (↥H) L] :
  Set.InjOn ⇑(TauCeti.lieCartanRestriction H) ↑(TauCeti.SymmetricAlgebra.lieInvariants K L L)
```

## Sources

- [Tau Ceti documentation: `LieSubalgebra.map_lieInvariants_lieCartanRestriction`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.map_lieInvariants_lieCartanRestriction)
- [Source of `LieSubalgebra.map_lieInvariants_lieCartanRestriction` in TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean#L134)
