---
declaration: theorem
origin: cited
lean: ContinuousLinearMapWOT.isCompact_image_ofCLM_closedBall
statement: formalized
proof: formalized
---

# Weak operator compactness of operator balls

Every closed norm ball of bounded operators
from a normed space to a complete inner product space is compact in the weak operator
topology.

```lean
ContinuousLinearMapWOT.isCompact_image_ofCLM_closedBall.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F] (A : E →L[𝕜] F) (r : ℝ) :
  IsCompact (ContinuousLinearMapWOT.ofCLM '' Metric.closedBall A r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMapWOT.isCompact_image_ofCLM_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/WeakOperatorTopology/Compact.html#ContinuousLinearMapWOT.isCompact_image_ofCLM_closedBall).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMapWOT.isCompact_image_ofCLM_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/WeakOperatorTopology/Compact.html#ContinuousLinearMapWOT.isCompact_image_ofCLM_closedBall)
- [Source of `ContinuousLinearMapWOT.isCompact_image_ofCLM_closedBall` in TauCeti/Analysis/InnerProductSpace/WeakOperatorTopology/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/WeakOperatorTopology/Compact.lean#L92)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
