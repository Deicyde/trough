---
declaration: def
origin: cited
lean: ZLattice.IsEven.nebentypus
statement: formalized
---

# ZLattice.IsEven.nebentypus

The **nebentypus** `χ_L` of an even full lattice `L` of even rank: the primitive character of
the Kronecker character `(D_L / ·)` of the signed discriminant `D_L = signedDiscr L`, induced up to
modulus `level L`. This is legitimate because the conductor of `(D_L / ·)` divides the level
(`ZLattice.IsEven.conductor_kroneckerChar_signedDiscr_dvd_level`). On integers `a` coprime to the
level, `χ_L a = (D_L / a)` (`ZLattice.IsEven.nebentypus_intCast`).

```lean
ZLattice.IsEven.nebentypus.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L] [IsZLattice ℝ L] (R : Type u_2)
  [CommRing R] [NeZero 2] (hL : ZLattice.IsEven L) (hE : Even (Module.finrank ℝ E)) :
  DirichletCharacter R (ZLattice.level L)
```

## Depends on

- [ZLattice.level](zlattice-level.md)

## Proof depends on

- [ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym](zlattice-iseven-gausssum-eq-sqrt-card-mul-jacobi.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.nebentypus`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Nebentypus.html#ZLattice.IsEven.nebentypus).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.nebentypus`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Nebentypus.html#ZLattice.IsEven.nebentypus)
- [Source of `ZLattice.IsEven.nebentypus` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Nebentypus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/Nebentypus.lean#L75)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
