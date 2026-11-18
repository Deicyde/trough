---
declaration: def
origin: cited
lean: Module.Basis.flagCellEquiv
statement: formalized
---

# Module.Basis.flagCellEquiv

The Schubert cell of the flag `b.flag` with pivot set `S`, that is the set of subspaces `W`
with `b.flagPivots W = S`, is in bijection with the affine space `K ^ S.echelonFreeEntries`: a
subspace corresponds to the free entries of its reduced echelon basis.

```lean
Module.Basis.flagCellEquiv.{u_1, u_2} {K : Type u_1} {V : Type u_2} [DivisionRing K]
  [AddCommGroup V] [_root_.Module K V] {n : ℕ} (b : Module.Basis (Fin n) K V) (S : Finset (Fin n)) :
  { W // b.flagPivots W = S } ≃ (↥S.echelonFreeEntries → K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.Basis.flagCellEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Basis/Flag.html#Module.Basis.flagCellEquiv).

## Sources

- [Tau Ceti documentation: `Module.Basis.flagCellEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Basis/Flag.html#Module.Basis.flagCellEquiv)
- [Source of `Module.Basis.flagCellEquiv` in TauCeti/LinearAlgebra/Basis/Flag.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Basis/Flag.lean#L464)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
