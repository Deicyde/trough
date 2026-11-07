---
declaration: theorem
origin: cited
lean: ContinuousMap.IsWeakHomotopyEquivalence.isIso_twistedHomologyMap
statement: formalized
proof: formalized
---

# ContinuousMap.IsWeakHomotopyEquivalence.isIso\_twistedHomologyMap

**A weak homotopy equivalence induces isomorphisms on singular homology with local
coefficients**, the local-coefficient form of Hatcher, Proposition 4.21: for every local
coefficient system `L` on `Y`, the map `H_n(X; f⁎L) ⟶ H_n(Y; L)` is an isomorphism.

```lean
ContinuousMap.IsWeakHomotopyEquivalence.isIso_twistedHomologyMap.{u, v} {X Y : Type v}
  [TopologicalSpace X] [TopologicalSpace Y] {f : C(X, Y)} {R : Type u} [Ring R]
  (hf : f.IsWeakHomotopyEquivalence) (L : TauCeti.LocalCoefficientSystem R ↧Y) (n : ℕ) :
  CategoryTheory.IsIso (TauCeti.LocalCoefficientSystem.twistedHomologyMap (TopCat.ofHom f) L n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cubical and simplicial chains with local coefficients are chain homotopy equivalent](cubical-and-simplicial-chains-with-local-coeffic.md)

## Lean

Formalized in Tau Ceti as [`ContinuousMap.IsWeakHomotopyEquivalence.isIso_twistedHomologyMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Homotopy/WeakHomotopyEquivalence.html#ContinuousMap.IsWeakHomotopyEquivalence.isIso_twistedHomologyMap).

## Sources

- [Tau Ceti documentation: `ContinuousMap.IsWeakHomotopyEquivalence.isIso_twistedHomologyMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Homotopy/WeakHomotopyEquivalence.html#ContinuousMap.IsWeakHomotopyEquivalence.isIso_twistedHomologyMap)
- [Source of `ContinuousMap.IsWeakHomotopyEquivalence.isIso_twistedHomologyMap` in TauCeti/AlgebraicTopology/Singular/Homotopy/WeakHomotopyEquivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/Homotopy/WeakHomotopyEquivalence.lean#L163)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
