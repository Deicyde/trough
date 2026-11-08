---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_wholeNormalBundle_subset
statement: formalized
proof: formalized
---

# Smooth Euclidean tubular neighbourhood theorem

The whole orthogonal normal bundle
of a smooth immersion inducing the source topology is diffeomorphic to an open neighbourhood
of its image, inside any prescribed open neighbourhood. The identification fixes the core.
Neither compactness nor closedness of the image is required.

```lean
TauCeti.exists_diffeomorph_wholeNormalBundle_subset.{u_1, u_2, u_3, u_4, u_5} {V : Type u_1}
  {E : Type u_2} {F : Type u_3} {H : Type u_4} {M : Type u_5} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {f : M → V}
  (hf : ContMDiff I (modelWithCornersSelf ℝ V) (↑⊤) f)
  (himm : ∀ (x : M), Function.Injective ⇑(mfderiv% f x)) (hind : Topology.IsInducing f)
  (hdim : Module.finrank ℝ F = Module.finrank ℝ V - Module.finrank ℝ E) {O : Set V} (hO : IsOpen O)
  (hfO : Set.range f ⊆ O) :
  ∃ W,
    ↑W ⊆ O ∧
      ∃ Φ, ∀ (x : M), ↑(Φ (Bundle.zeroSection F (fun x => ↥(TauCeti.normalSubspace I f x)) x)) = f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](../part-01/the-inverse-function-theorem-for-manifolds.md)
- [The inverse function theorem produces a `C^n` inverse](../../../../analysis/part-01/calculus/part-01/the-inverse-function-theorem-produces-a-c-n-inve.md)
- [Noncompact Euclidean tubular neighbourhood theorem](noncompact-euclidean-tubular-neighbourhood-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_wholeNormalBundle_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/WholeBundle/Diffeomorph.html#TauCeti.exists_diffeomorph_wholeNormalBundle_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_wholeNormalBundle_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/WholeBundle/Diffeomorph.html#TauCeti.exists_diffeomorph_wholeNormalBundle_subset)
- [Source of `TauCeti.exists_diffeomorph_wholeNormalBundle_subset` in TauCeti/Geometry/Manifold/TubularNeighborhood/WholeBundle/Diffeomorph.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/TubularNeighborhood/WholeBundle/Diffeomorph.lean#L45)
