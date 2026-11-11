---
declaration: theorem
origin: cited
lean: TauCeti.LocalCoefficientSystem.quasiIso_smallTwistedChainComplexι
statement: formalized
proof: formalized
---

# The small-chain theorem with local coefficients

The canonical inclusion of twisted
singular chains subordinate to an open cover induces isomorphisms on homology in every degree,
including degree zero. Coefficient fibres may be arbitrary modules over an arbitrary ring.

```lean
TauCeti.LocalCoefficientSystem.quasiIso_smallTwistedChainComplexι.{u, v, w, u_1} {R : Type u}
  [Ring R] {X : TopCat} (L : TauCeti.LocalCoefficientSystem R X) {ι : Type u_1} (U : ι → Set ↑X)
  (hU : ∀ (i : ι), IsOpen (U i)) (hcov : ⋃ i, U i = Set.univ) :
  QuasiIso (L.smallTwistedChainComplexι U)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalCoefficientSystem.quasiIso_smallTwistedChainComplexι`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Twisted/Small/QuasiIso.html#TauCeti.LocalCoefficientSystem.quasiIso_smallTwistedChainComplex%CE%B9).

## Sources

- [Tau Ceti documentation: `TauCeti.LocalCoefficientSystem.quasiIso_smallTwistedChainComplexι`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Twisted/Small/QuasiIso.html#TauCeti.LocalCoefficientSystem.quasiIso_smallTwistedChainComplex%CE%B9)
- [Source of `TauCeti.LocalCoefficientSystem.quasiIso_smallTwistedChainComplexι` in TauCeti/AlgebraicTopology/Singular/Twisted/Small/QuasiIso.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Twisted/Small/QuasiIso.lean#L44)
