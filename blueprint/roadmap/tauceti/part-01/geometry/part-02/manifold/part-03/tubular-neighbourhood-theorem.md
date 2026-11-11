---
declaration: theorem
origin: cited
lean: TauCeti.exists_isOpenEmbedding_normalTube, TauCeti.exists_isTubularNeighborhood_normalBundle
statement: formalized
proof: formalized
---

# Tubular neighbourhood theorem

**Tubular neighbourhood theorem** for a compact `C²` embedded submanifold of a Euclidean
space: for some `ε > 0`, the map `(x, v) ↦ f x + v` is an open embedding of the normal vectors of
length less than `ε` into `V`.

```lean
TauCeti.exists_isOpenEmbedding_normalTube.{u_1, u_2, u_3, u_4} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {E : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_4}
  [TopologicalSpace M] [ChartedSpace H M] [I.Boundaryless] [IsManifold I 2 M] [CompactSpace M]
  {f : M → V} (hf : ContMDiff I (modelWithCornersSelf ℝ V) 2 f)
  (himm : ∀ (x : M), Function.Injective ⇑(mfderiv% f x)) (hinj : Function.Injective f) :
  ∃ ε > 0, Topology.IsOpenEmbedding ((TauCeti.normalTube I f ε).domRestrict fun p => f p.1 + p.2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem, with a `C^n` inverse on the whole target](../../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isOpenEmbedding_normalTube`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Euclidean.html#TauCeti.exists_isOpenEmbedding_normalTube).

## Other forms

**Tubular neighbourhood theorem.** Formalized in Tau Ceti as [`TauCeti.exists_isTubularNeighborhood_normalBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Euclidean.html#TauCeti.exists_isTubularNeighborhood_normalBundle).

```lean
TauCeti.exists_isTubularNeighborhood_normalBundle.{u_1, u_2, u_3, u_4} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M]
  [I.Boundaryless] [IsManifold I 2 M] [CompactSpace M] {f : M → V}
  (hf : ContMDiff I (modelWithCornersSelf ℝ V) 2 f)
  (himm : ∀ (x : M), Function.Injective ⇑(mfderiv% f x)) (hinj : Function.Injective f) :
  ∃ ε > 0, TauCeti.IsTubularNeighborhood f {p | ‖↑p.snd‖ < ε} fun p => f (↑p).proj + ↑(↑p).snd
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isOpenEmbedding_normalTube`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Euclidean.html#TauCeti.exists_isOpenEmbedding_normalTube)
- [Source of `TauCeti.exists_isOpenEmbedding_normalTube` in TauCeti/Geometry/Manifold/TubularNeighborhood/Euclidean.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/TubularNeighborhood/Euclidean.lean#L431)
