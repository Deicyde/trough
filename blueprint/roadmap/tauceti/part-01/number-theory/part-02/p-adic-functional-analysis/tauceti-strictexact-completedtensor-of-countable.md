---
declaration: theorem
origin: cited
lean: TauCeti.strictExact_completedTensor_of_countableType
statement: formalized
proof: formalized
---

# TauCeti.strictExact_completedTensor_of_countableType

Completed tensoring preserves strict short exactness when the middle Banach space is
ultrametric and of countable type. This asserts closed embedding, open surjectivity and
exactness for the native maps, not just for maps conjugated to a chosen product.

```lean
TauCeti.strictExact_completedTensor_of_countableType.{u_1, u_2, u_3, u_4, u_5} {K : Type u_1}
  {E : Type u_2} {M : Type u_3} {N : Type u_4} {W : Type u_5} [NontriviallyNormedField K]
  [CompleteSpace K] [NormedAddCommGroup E] [NormedSpace K E] [IsUltrametricDist E] [CompleteSpace E]
  [AddCommGroup M] [_root_.Module K M] [TopologicalSpace M] [NormedAddCommGroup N] [NormedSpace K N]
  [CompleteSpace N] [AddCommGroup W] [_root_.Module K W] [TopologicalSpace W] {v : ℕ → E}
  (hv : Dense ↑(Submodule.span K (Set.range v))) (i : M →L[K] E) (q : E →L[K] N)
  (hi : Topology.IsEmbedding ⇑i) (hq : Function.Surjective ⇑q) (hiq : (↑i).range = (↑q).ker) :
  Topology.IsClosedEmbedding
      ⇑(TauCeti.Huber.BanachModule.CompletedTensor.map i (ContinuousLinearMap.id K W)) ∧
    IsOpenMap ⇑(TauCeti.Huber.BanachModule.CompletedTensor.map q (ContinuousLinearMap.id K W)) ∧
      Function.Surjective
          ⇑(TauCeti.Huber.BanachModule.CompletedTensor.map q (ContinuousLinearMap.id K W)) ∧
        Function.Exact
          ⇑(TauCeti.Huber.BanachModule.CompletedTensor.map i (ContinuousLinearMap.id K W))
          ⇑(TauCeti.Huber.BanachModule.CompletedTensor.map q (ContinuousLinearMap.id K W))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Strict short exact sequences out of a space of countable type split](strict-short-exact-sequences-out-of-a-space-of-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.strictExact_completedTensor_of_countableType`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/CompletedExtension.html#TauCeti.strictExact_completedTensor_of_countableType).

## Sources

- [Tau Ceti documentation: `TauCeti.strictExact_completedTensor_of_countableType`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/CompletedExtension.html#TauCeti.strictExact_completedTensor_of_countableType)
- [Source of `TauCeti.strictExact_completedTensor_of_countableType` in TauCeti/Analysis/Normed/Module/Bases/CompletedExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Module/Bases/CompletedExtension.lean#L78)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
