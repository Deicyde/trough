---
declaration: theorem
origin: cited
lean: Convex.isClosed_iff_forall_isClosed_inter_closedBall
statement: formalized
proof: formalized
---

# Krein–Šmulian theorem

A convex subset of the dual of a Banach space is weak-star closed if
and only if its intersection with every closed ball centred at zero is weak-star closed.

```lean
Convex.isClosed_iff_forall_isClosed_inter_closedBall.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] {C : Set (WeakDual 𝕜 E)}
  (hC : Convex ℝ C) :
  IsClosed C ↔ ∀ (r : ℝ), IsClosed (C ∩ ⇑WeakDual.toStrongDual ⁻¹' Metric.closedBall 0 r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Separation lemma of the Krein–Šmulian theorem](separation-lemma-of-the-krein-smulian-theorem.md)

## Lean

Formalized in Tau Ceti as [`Convex.isClosed_iff_forall_isClosed_inter_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.html#Convex.isClosed_iff_forall_isClosed_inter_closedBall).

## Sources

- [Tau Ceti documentation: `Convex.isClosed_iff_forall_isClosed_inter_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.html#Convex.isClosed_iff_forall_isClosed_inter_closedBall)
- [Source of `Convex.isClosed_iff_forall_isClosed_inter_closedBall` in TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.lean#L263)
