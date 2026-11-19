---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.singularValue_dualBallEmbedding_comp
statement: formalized
proof: formalized
---

# Pietsch's embedding identity

Gelfand numbers are the approximation numbers after
evaluation on the dual unit ball of the target.

```lean
ContinuousLinearMap.singularValue_dualBallEmbedding_comp.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [SeminormedAddCommGroup F] [NormedSpace 𝕜 F] (T : E →L[𝕜] F) (n : ℕ) :
  ((TauCeti.dualBallEmbedding 𝕜 F).toContinuousLinearMap ∘SL T).singularValue n = T.gelfandNumber n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.singularValue_dualBallEmbedding_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Embedding.html#ContinuousLinearMap.singularValue_dualBallEmbedding_comp).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.singularValue_dualBallEmbedding_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SNumbers/Embedding.html#ContinuousLinearMap.singularValue_dualBallEmbedding_comp)
- [Source of `ContinuousLinearMap.singularValue_dualBallEmbedding_comp` in TauCeti/Analysis/Normed/Operator/SNumbers/Embedding.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/SNumbers/Embedding.lean#L65)
