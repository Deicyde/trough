---
declaration: theorem
origin: cited
lean: TauCeti.ModuleTower.finiteReduction_isEquivalence
statement: formalized
proof: formalized
---

# Finite modules are finite adic systems (EGA I, Ch. 0, 7.2.9–7.2.10)

over a noetherian
`I`-adically complete ring, `M ↦ (M ⧸ I^{n+1} M)ₙ` is an equivalence from finite `A`-modules to
`I`-adic systems with finite `M₀`, with quasi-inverse the limit.

```lean
TauCeti.ModuleTower.finiteReduction_isEquivalence.{v, u} {A : Type u} [CommRing A] (I : Ideal A)
  [IsNoetherianRing A] [IsAdicComplete I A] : (TauCeti.ModuleTower.finiteReduction I).IsEquivalence
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModuleTower.finiteReduction_isEquivalence`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/Reduction.html#TauCeti.ModuleTower.finiteReduction_isEquivalence).

## Sources

- [Tau Ceti documentation: `TauCeti.ModuleTower.finiteReduction_isEquivalence`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/Reduction.html#TauCeti.ModuleTower.finiteReduction_isEquivalence)
- [Source of `TauCeti.ModuleTower.finiteReduction_isEquivalence` in TauCeti/Algebra/Category/ModuleCat/Tower/Reduction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/Tower/Reduction.lean#L418)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
