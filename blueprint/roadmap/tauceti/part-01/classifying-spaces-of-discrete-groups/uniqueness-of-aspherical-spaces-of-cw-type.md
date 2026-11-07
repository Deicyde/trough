---
declaration: theorem
origin: cited
lean: TauCeti.IsAspherical.exists_homotopyEquiv
statement: formalized
proof: formalized
---

# Uniqueness of aspherical spaces of CW type

Two aspherical spaces of CW type are homotopy
equivalent by a homotopy equivalence realizing any prescribed isomorphism `φ` of their fundamental
groups: there is a homotopy equivalence `e` and a path `γ` from `e x` to `y` such that the map
induced by `e` on fundamental groups, followed by basepoint change along `γ`, is `φ`.

The hypothesis of CW type on both spaces cannot be dropped: a point and the Warsaw circle are
aspherical with trivial fundamental groups, but they are not homotopy equivalent.

```lean
TauCeti.IsAspherical.exists_homotopyEquiv.{u} {X Y : Type u} [TopologicalSpace X]
  [TopologicalSpace Y] [TauCeti.CWType X] [TauCeti.CWType Y] {x : X} {y : Y}
  (hX : TauCeti.IsAspherical X x) (hY : TauCeti.IsAspherical Y y)
  (φ : FundamentalGroup X x ≃* FundamentalGroup Y y) :
  ∃ e γ,
    ∀ (a : FundamentalGroup X x),
      (FundamentalGroup.fundamentalGroupMulEquivOfPath γ) ((FundamentalGroup.map e.toFun x) a) = φ a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The cellular and the simplicial classifying spaces agree](the-cellular-and-the-simplicial-classifying-spac.md)
- [The cellular classifying space is a CW complex](the-cellular-classifying-space-is-a-cw-complex.md)
- [Circle.fundamentalGroupMulEquiv\_fromPath](../../part-07/universal-covers/circle-fundamentalgroupmulequiv-frompath.md)
- [Whitehead's theorem](../algebraic-topology-of-spaces-and-manifolds/whiteheads-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAspherical.exists_homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Uniqueness.html#TauCeti.IsAspherical.exists_homotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAspherical.exists_homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Uniqueness.html#TauCeti.IsAspherical.exists_homotopyEquiv)
- [Source of `TauCeti.IsAspherical.exists_homotopyEquiv` in TauCeti/AlgebraicTopology/ClassifyingSpace/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ClassifyingSpace/Uniqueness.lean#L66)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
