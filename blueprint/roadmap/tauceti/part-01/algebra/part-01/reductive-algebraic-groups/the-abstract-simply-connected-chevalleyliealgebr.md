---
declaration: def
origin: cited
lean: TauCeti.DynkinType.simplyConnectedChevalleyLieEquiv
statement: formalized
---

# The abstract simply connected `ChevalleyLieAlgebra` of type `t` is canonically isomorphic over `ℤ` to the Chevalley lattice of the pinned rational Lie algebra

```lean
TauCeti.DynkinType.simplyConnectedChevalleyLieEquiv (t : TauCeti.DynkinType) (ht : t.Valid) :
  RootPairing.ChevalleyLieAlgebra (t.simplyConnectedChevalleyConstants ht) ≃ₗ⁅ℤ⁆
    ↥⋯.chevalleyLieLattice
```

## Depends on

- [The integral Chevalley Lie algebra](the-integral-chevalley-lie-algebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.simplyConnectedChevalleyLieEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Chevalley/Semisimple.html#TauCeti.DynkinType.simplyConnectedChevalleyLieEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.simplyConnectedChevalleyLieEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Chevalley/Semisimple.html#TauCeti.DynkinType.simplyConnectedChevalleyLieEquiv)
- [Source of `TauCeti.DynkinType.simplyConnectedChevalleyLieEquiv` in TauCeti/Algebra/Lie/Chevalley/Semisimple.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Chevalley/Semisimple.lean#L351)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
