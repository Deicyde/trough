---
declaration: theorem
origin: cited
lean: TauCeti.HasApproximationProperty.of_strongDual
statement: formalized
proof: formalized
---

# Grothendieck's dual approximation property theorem

If the strong dual `E*` of a normed
space `E` over `ℝ` or `ℂ` has the approximation property, then `E` itself has the approximation
property.

```lean
TauCeti.HasApproximationProperty.of_strongDual.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  (h : TauCeti.HasApproximationProperty 𝕜 (StrongDual 𝕜 E)) : TauCeti.HasApproximationProperty 𝕜 E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's compactness lemma](../../convex/grothendiecks-compactness-lemma.md)
- [Norm double-annihilator theorem](../part-02/norm-double-annihilator-theorem.md)
- [TauCeti.CompletedInjectiveTensor](../../../part-01/banach-space-theory/part-01/tauceti-completedinjectivetensor.md)
- [TauCeti.CompletedProjectiveTensor](../../../part-01/banach-space-theory/part-01/tauceti-completedprojectivetensor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasApproximationProperty.of_strongDual`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.HasApproximationProperty.of_strongDual).

## Sources

- [Tau Ceti documentation: `TauCeti.HasApproximationProperty.of_strongDual`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.html#TauCeti.HasApproximationProperty.of_strongDual)
- [Source of `TauCeti.HasApproximationProperty.of_strongDual` in TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/ApproximationProperty/TensorProduct.lean#L338)
