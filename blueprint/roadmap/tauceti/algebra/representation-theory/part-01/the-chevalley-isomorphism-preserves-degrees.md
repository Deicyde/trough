---
declaration: theorem
origin: cited
lean: LieSubalgebra.lieChevalleyRestrictionIso_mem_homogeneousSubmodule_iff
statement: formalized
proof: formalized
---

# The Chevalley isomorphism preserves degrees

an invariant is homogeneous of degree `m`
exactly when its restriction to `H` is.

```lean
LieSubalgebra.lieChevalleyRestrictionIso_mem_homogeneousSubmodule_iff.{u_1, u_2} {K : Type u_1}
  {L : Type u_2} [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] (H : LieSubalgebra K L) [H.IsCartanSubalgebra] [IsAlgClosed K]
  {p : ↥(TauCeti.SymmetricAlgebra.lieInvariants K L L)} {m : ℕ} :
  ↑(H.lieChevalleyRestrictionIso p) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K (↥H) m ↔
    ↑p ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K L m
```

## Depends on

- [Chevalley's restriction theorem](chevalleys-restriction-theorem.md)

## Proof depends on

- [Chevalley's restriction theorem, image form](chevalleys-restriction-theorem-image-form.md)
- [The Killing duality is Weyl-equivariant](../../lie/the-killing-duality-is-weyl-equivariant.md)
- [Representation.symmetricAlgebraInvariants](../../../representation-theory/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrainvariants.md)
- [Representation.symmetricAlgebraReynolds](../../../representation-theory/finite-reflection-invariants-degrees-and-weyl-ex/representation-symmetricalgebrareynolds.md)

## Lean

Formalized in Tau Ceti as [`LieSubalgebra.lieChevalleyRestrictionIso_mem_homogeneousSubmodule_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.lieChevalleyRestrictionIso_mem_homogeneousSubmodule_iff).

## Sources

- [Tau Ceti documentation: `LieSubalgebra.lieChevalleyRestrictionIso_mem_homogeneousSubmodule_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.html#LieSubalgebra.lieChevalleyRestrictionIso_mem_homogeneousSubmodule_iff)
- [Source of `LieSubalgebra.lieChevalleyRestrictionIso_mem_homogeneousSubmodule_iff` in TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/HighestWeight/ChevalleyRestriction.lean#L175)
