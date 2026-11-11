---
declaration: theorem
origin: cited
lean: TauCeti.exists_forall_dual_pos_iff
statement: formalized
proof: formalized
---

# Gordan's theorem

Some linear functional is strictly positive on every vector of a finite
family exactly when the only nonnegative linear relation among the vectors is the trivial one.

```lean
TauCeti.exists_forall_dual_pos_iff.{u_1, u_2, u_3} {ι : Type u_1} {K : Type u_2} {V : Type u_3}
  [Field K] [LinearOrder K] [IsStrictOrderedRing K] [AddCommGroup V] [_root_.Module K V] [Fintype ι]
  (a : ι → V) : (∃ y, ∀ (j : ι), 0 < y (a j)) ↔ ∀ (x : ι → K), 0 ≤ x → ∑ j, x j • a j = 0 → x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's theorem](tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_forall_dual_pos_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#TauCeti.exists_forall_dual_pos_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_forall_dual_pos_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#TauCeti.exists_forall_dual_pos_iff)
- [Source of `TauCeti.exists_forall_dual_pos_iff` in TauCeti/Geometry/Convex/Cone/Alternative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Convex/Cone/Alternative.lean#L164)
