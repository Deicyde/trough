---
declaration: theorem
origin: cited
lean: TauCeti.surjective_inclusionInDoubleDual_of_uniformConvexSpace
statement: formalized
proof: formalized
---

# Milman–Pettis theorem

A uniformly convex Banach space is reflexive: its canonical map
into the continuous bidual is surjective.

```lean
TauCeti.surjective_inclusionInDoubleDual_of_uniformConvexSpace.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [UniformConvexSpace E]
  [CompleteSpace E] : Function.Surjective ⇑(NormedSpace.inclusionInDoubleDual 𝕜 E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Goldstine's theorem](../../part-01/banach-space-theory/part-02/goldstines-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.surjective_inclusionInDoubleDual_of_uniformConvexSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Uniform/Basic.html#TauCeti.surjective_inclusionInDoubleDual_of_uniformConvexSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.surjective_inclusionInDoubleDual_of_uniformConvexSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Uniform/Basic.html#TauCeti.surjective_inclusionInDoubleDual_of_uniformConvexSpace)
- [Source of `TauCeti.surjective_inclusionInDoubleDual_of_uniformConvexSpace` in TauCeti/Analysis/Convex/Uniform/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/Uniform/Basic.lean#L145)
