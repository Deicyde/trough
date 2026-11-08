---
declaration: theorem
origin: cited
lean: Representation.finiteType_symmetricAlgebraInvariants
statement: formalized
proof: formalized
---

# Noether's finiteness theorem for the invariants of a finite group acting on a finitely generated module over a Noetherian ring

the invariant subalgebra is of finite type.

```lean
Representation.finiteType_symmetricAlgebraInvariants.{u_1, u_2, u_3} {R : Type u_1} {G : Type u_2}
  {M : Type u_3} [CommRing R] [Group G] [AddCommMonoid M] [_root_.Module R M]
  (ρ : Representation R G M) [Finite G] [IsNoetherianRing R] [Module.Finite R M] :
  Algebra.FiniteType R ↥ρ.symmetricAlgebraInvariants
```

## Depends on

- [Representation.symmetricAlgebraInvariants](representation-symmetricalgebrainvariants.md)

## Proof depends on

- [Noether's finiteness theorem](noethers-finiteness-theorem.md)

## Lean

Formalized in Tau Ceti as [`Representation.finiteType_symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/FiniteType.html#Representation.finiteType_symmetricAlgebraInvariants).

## Sources

- [Tau Ceti documentation: `Representation.finiteType_symmetricAlgebraInvariants`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/FiniteType.html#Representation.finiteType_symmetricAlgebraInvariants)
- [Source of `Representation.finiteType_symmetricAlgebraInvariants` in TauCeti/RepresentationTheory/SymmetricAlgebra/FiniteType.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/SymmetricAlgebra/FiniteType.lean#L73)
