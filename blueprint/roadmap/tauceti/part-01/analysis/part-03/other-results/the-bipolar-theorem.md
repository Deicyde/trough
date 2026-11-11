---
declaration: theorem
origin: cited
lean: AbsConvex.bipolar_eq_closure
statement: formalized
proof: formalized
---

# The bipolar theorem

the bipolar of a nonempty absolutely convex set equals
its closure in the original locally convex topology.

```lean
AbsConvex.bipolar_eq_closure.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [AddCommGroup E]
  [_root_.Module 𝕜 E] [TopologicalSpace E] [_root_.Module ℝ E] [IsScalarTower ℝ 𝕜 E]
  [IsTopologicalAddGroup E] [ContinuousSMul 𝕜 E] [LocallyConvexSpace ℝ E] {s : Set E}
  (hs : AbsConvex 𝕜 s) (hne : s.Nonempty) :
  (topDualPairing 𝕜 E).polar (StrongDual.polar 𝕜 s) = closure s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbsConvex.bipolar_eq_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/Bipolar.html#AbsConvex.bipolar_eq_closure).

## Sources

- [Tau Ceti documentation: `AbsConvex.bipolar_eq_closure`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/Bipolar.html#AbsConvex.bipolar_eq_closure)
- [Source of `AbsConvex.bipolar_eq_closure` in TauCeti/Analysis/LocallyConvex/Bipolar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/LocallyConvex/Bipolar.lean#L69)
