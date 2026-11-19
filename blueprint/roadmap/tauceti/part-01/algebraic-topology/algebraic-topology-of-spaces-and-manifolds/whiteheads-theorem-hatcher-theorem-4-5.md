---
declaration: def
origin: cited
lean: ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv
statement: formalized
---

# Whitehead's theorem (Hatcher, Theorem 4.5)

A weak homotopy equivalence `f` between spaces
of CW type is a homotopy equivalence. This is the homotopy equivalence whose forward map is `f`
itself (`ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv_toFun`); its homotopy inverse is a
lift of the identity through `f` given by
`ContinuousMap.IsWeakHomotopyEquivalence.exists_comp_homotopic`.

```lean
ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv.{u_1, u_2} {X : Type u_1} [TopologicalSpace X]
  {Y : Type u_2} [TopologicalSpace Y] {f : C(X, Y)} [TauCeti.CWType X] [TauCeti.CWType Y]
  (hf : f.IsWeakHomotopyEquivalence) : ContinuousMap.HomotopyEquiv X Y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Whitehead.html#ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv).

## Sources

- [Tau Ceti documentation: `ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Whitehead.html#ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv)
- [Source of `ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv` in TauCeti/AlgebraicTopology/Homotopy/Whitehead.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Homotopy/Whitehead.lean#L260)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
