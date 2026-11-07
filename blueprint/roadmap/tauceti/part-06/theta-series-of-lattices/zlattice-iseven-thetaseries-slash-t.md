---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.thetaSeries_slash_T
statement: formalized
proof: formalized
---

# ZLattice.IsEven.thetaSeries\_slash\_T

The theta series of an even lattice is invariant under `T`, in every weight:
`Θ_L ∣[k] T = Θ_L`.

```lean
ZLattice.IsEven.thetaSeries_slash_T.{u_1} {E : Type u_1} [NormedAddCommGroup E] {L : Submodule ℤ E}
  (hL : ZLattice.IsEven L) (k : ℤ) :
  SlashAction.map k ModularGroup.T (ZLattice.thetaSeries L) = ZLattice.thetaSeries L
```

## Depends on

- [ZLattice.IsEven](zlattice-iseven.md)
- [ZLattice.thetaSeries](zlattice-thetaseries.md)

## Proof depends on

- [ZLattice.thetaCoset](zlattice-thetacoset.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.thetaSeries_slash_T`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.html#ZLattice.IsEven.thetaSeries_slash_T).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.thetaSeries_slash_T`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.html#ZLattice.IsEven.thetaSeries_slash_T)
- [Source of `ZLattice.IsEven.thetaSeries_slash_T` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ThetaSeries/Translation.lean#L128)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
