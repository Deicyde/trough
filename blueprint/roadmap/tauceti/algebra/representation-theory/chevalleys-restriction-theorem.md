---
declaration: def
origin: cited
lean: LieSubalgebra.lieChevalleyRestrictionIso
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

- [Chevalley's restriction theorem, image form](chevalleys-restriction-theorem-image-form.md)

## Lean

Formalized in Tau Ceti as [`LieSubalgebra.lieChevalleyRestrictionIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.lieChevalleyRestrictionIso).

## Sources

- [Tau Ceti documentation: `LieSubalgebra.lieChevalleyRestrictionIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.lieChevalleyRestrictionIso)
- [Source of `LieSubalgebra.lieChevalleyRestrictionIso` in TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean#L148)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
