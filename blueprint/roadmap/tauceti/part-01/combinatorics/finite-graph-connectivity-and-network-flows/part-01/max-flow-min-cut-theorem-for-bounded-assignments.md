---
declaration: theorem
origin: cited
lean: TauCeti.BoundedFlow.exists_val_eq_cutBound
statement: formalized
proof: formalized
---

# Max-flow/min-cut theorem for bounded assignments

If some bounded `s`–`t` assignment
between distinct terminals exists, then some bounded `s`–`t` assignment has value equal to the cut
bound of some vertex set containing `s` but not `t`. By weak duality
(`TauCeti.BoundedFlow.val_le_cutBound`) this assignment is maximum and this cut bound is
minimum.

```lean
TauCeti.BoundedFlow.exists_val_eq_cutBound.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w}
  [Fintype V] [(v w : V) → Fintype (Q v w)] [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]
  {lo hi : TauCeti.Assignment Q K} {s t : V} [DecidableEq V] (hst : s ≠ t)
  (f : TauCeti.BoundedFlow lo hi s t) : ∃ g S, s ∈ S ∧ t ∉ S ∧ g.val = TauCeti.cutBound lo hi S
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.residualUpdate](tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BoundedFlow.exists_val_eq_cutBound`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/ShortestAugmentation.html#TauCeti.BoundedFlow.exists_val_eq_cutBound).

## Sources

- [Tau Ceti documentation: `TauCeti.BoundedFlow.exists_val_eq_cutBound`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/ShortestAugmentation.html#TauCeti.BoundedFlow.exists_val_eq_cutBound)
- [Source of `TauCeti.BoundedFlow.exists_val_eq_cutBound` in TauCeti/Combinatorics/Network/ShortestAugmentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/ShortestAugmentation.lean#L324)
