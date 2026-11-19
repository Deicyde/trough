---
declaration: def
origin: cited
lean: Representation.symmetricAlgebraInvariantsBaseChangeEquiv
statement: formalized
---

# Polynomial invariants commute with flat scalar extension

For a finite group `G` and a
flat `R`-algebra `S`, the scalar extension of the invariant subalgebra `Sym(M)^G` is the invariant
subalgebra of the scalar-extended representation. The equivalence is the scalar extension of the
inclusion `Sym(M)^G → Sym M`, followed by the canonical equivalence
`S ⊗[R] Sym M ≃ Sym (S ⊗[R] M)`.

```lean
Representation.symmetricAlgebraInvariantsBaseChangeEquiv.{u_1, u_2, u_3, u_4} {R : Type u_1}
  {S : Type u_2} {G : Type u_3} {M : Type u_4} [CommRing R] [CommRing S] [Algebra R S] [Group G]
  [AddCommGroup M] [_root_.Module R M] (ρ : Representation R G M) [Module.Flat R S] [Finite G] :
  TensorProduct R S ↥ρ.symmetricAlgebraInvariants ≃ₐ[S]
    ↥(Representation.baseChange S ρ).symmetricAlgebraInvariants
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Representation.symmetricAlgebraInvariantsBaseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/BaseChange.html#Representation.symmetricAlgebraInvariantsBaseChangeEquiv).

## Sources

- [Tau Ceti documentation: `Representation.symmetricAlgebraInvariantsBaseChangeEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/BaseChange.html#Representation.symmetricAlgebraInvariantsBaseChangeEquiv)
- [Source of `Representation.symmetricAlgebraInvariantsBaseChangeEquiv` in TauCeti/RepresentationTheory/SymmetricAlgebra/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SymmetricAlgebra/BaseChange.lean#L162)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
