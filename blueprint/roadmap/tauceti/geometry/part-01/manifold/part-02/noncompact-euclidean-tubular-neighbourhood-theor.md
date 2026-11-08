---
declaration: theorem
origin: cited
lean: TauCeti.exists_isOpenEmbedding_normalTubeOfRadius
statement: formalized
proof: formalized
---

# Noncompact Euclidean tubular neighbourhood theorem

A `C²` immersion inducing
the source topology admits a positive continuous radius on which its normal addition
map is an open embedding.

```lean
TauCeti.exists_isOpenEmbedding_normalTubeOfRadius.{u_1, u_2, u_3, u_4} {V : Type u_1} {E : Type u_2}
  {H : Type u_3} {M : Type u_4} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ V] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I 2 M] {f : M → V} (hf : ContMDiff I (modelWithCornersSelf ℝ V) 2 f)
  (himm : ∀ (x : M), Function.Injective ⇑(mfderiv% f x)) (hind : Topology.IsInducing f) :
  ∃ r,
    (∀ (x : M), 0 < r x) ∧
      Topology.IsOpenEmbedding
        ((TauCeti.normalTubeOfRadius I f ⇑r).domRestrict fun p => f p.1 + p.2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem, with a `C^n` inverse on the whole target](../../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isOpenEmbedding_normalTubeOfRadius`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Noncompact.html#TauCeti.exists_isOpenEmbedding_normalTubeOfRadius).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isOpenEmbedding_normalTubeOfRadius`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Noncompact.html#TauCeti.exists_isOpenEmbedding_normalTubeOfRadius)
- [Source of `TauCeti.exists_isOpenEmbedding_normalTubeOfRadius` in TauCeti/Geometry/Manifold/TubularNeighborhood/Noncompact.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/TubularNeighborhood/Noncompact.lean#L45)
