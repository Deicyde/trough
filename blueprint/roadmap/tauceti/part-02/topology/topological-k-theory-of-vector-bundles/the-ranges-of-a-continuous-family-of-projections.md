---
declaration: theorem
origin: cited
lean: TauCeti.rangeVectorBundle
statement: formalized
proof: formalized
---

# The ranges of a continuous family of projections form a vector bundle

with the subspace
topology of `B × F`, the intertwiner trivializations are linear, with continuous coordinate
changes.

```lean
TauCeti.rangeVectorBundle.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {B : Type u_2} [TopologicalSpace B] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  {F' : Type u_4} [NormedAddCommGroup F'] [NormedSpace 𝕜 F'] [CompleteSpace F] {p : B → F →L[𝕜] F}
  (hp : Continuous p) (hidem : ∀ (x : B), IsIdempotentElem (p x))
  (hF' : ∀ (x : B), Nonempty (F' ≃L[𝕜] ↥(↑(p x)).range)) :
  VectorBundle 𝕜 F' fun x => ↥(↑(p x)).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.rangeVectorBundle`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/IdempotentRange.html#TauCeti.rangeVectorBundle).

## Sources

- [Tau Ceti documentation: `TauCeti.rangeVectorBundle`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/IdempotentRange.html#TauCeti.rangeVectorBundle)
- [Source of `TauCeti.rangeVectorBundle` in TauCeti/Topology/VectorBundle/IdempotentRange.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/IdempotentRange.lean#L258)
- [Tau Ceti roadmap status: Topological K-theory of vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TopologicalKTheory/STATUS.md)
