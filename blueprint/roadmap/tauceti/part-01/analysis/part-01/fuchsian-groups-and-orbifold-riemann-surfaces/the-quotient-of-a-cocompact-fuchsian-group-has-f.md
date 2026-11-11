---
declaration: theorem
origin: cited
lean: Subgroup.finiteCWType_orbitRel_quotient
statement: formalized
proof: formalized
---

# The quotient of a cocompact Fuchsian group has finite CW type

**The quotient of a cocompact Fuchsian group has finite CW type**, through the cell structure
induced by a compact Dirichlet polygon.

```lean
Subgroup.finiteCWType_orbitRel_quotient
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  [CompactSpace (MulAction.orbitRel.Quotient (↥Γ) UpperHalfPlane)] :
  TauCeti.FiniteCWType (MulAction.orbitRel.Quotient (↥Γ) UpperHalfPlane)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gauss–Bonnet formula](../../part-02/complex/part-01/the-gauss-bonnet-formula.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.finiteCWType_orbitRel_quotient`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.html#Subgroup.finiteCWType_orbitRel_quotient).

## Sources

- [Tau Ceti documentation: `Subgroup.finiteCWType_orbitRel_quotient`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.html#Subgroup.finiteCWType_orbitRel_quotient)
- [Source of `Subgroup.finiteCWType_orbitRel_quotient` in TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.lean#L93)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
