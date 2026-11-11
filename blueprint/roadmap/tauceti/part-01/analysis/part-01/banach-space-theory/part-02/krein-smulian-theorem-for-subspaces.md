---
declaration: theorem
origin: cited
lean: Submodule.isClosed_iff_isClosed_inter_closedBall_zero_one
statement: formalized
proof: formalized
---

# Krein–Šmulian theorem for subspaces

A subspace of the dual of a Banach space is weak-star
closed if and only if its intersection with the closed unit ball is weak-star closed.

```lean
Submodule.isClosed_iff_isClosed_inter_closedBall_zero_one.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E]
  (G : Submodule 𝕜 (WeakDual 𝕜 E)) :
  IsClosed ↑G ↔ IsClosed (↑G ∩ ⇑WeakDual.toStrongDual ⁻¹' Metric.closedBall 0 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krein–Šmulian theorem](../part-01/krein-smulian-theorem.md)

## Lean

Formalized in Tau Ceti as [`Submodule.isClosed_iff_isClosed_inter_closedBall_zero_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.html#Submodule.isClosed_iff_isClosed_inter_closedBall_zero_one).

## Sources

- [Tau Ceti documentation: `Submodule.isClosed_iff_isClosed_inter_closedBall_zero_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.html#Submodule.isClosed_iff_isClosed_inter_closedBall_zero_one)
- [Source of `Submodule.isClosed_iff_isClosed_inter_closedBall_zero_one` in TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.lean#L284)
