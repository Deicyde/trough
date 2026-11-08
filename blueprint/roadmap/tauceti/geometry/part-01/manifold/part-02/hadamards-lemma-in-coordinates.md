---
declaration: theorem
origin: cited
lean: ContMDiffMap.exists_hadamard_coords, OpenPartialHomeomorph.exists_eq_sum_holomorphicLinearCoordinateGerm_mul, TauCeti.mem_smoothVanishingIdeal_sq_of_mvfderiv_eq_zero
statement: formalized
proof: formalized
---

# Hadamard's lemma in coordinates

Subtracting its value at `x` writes a smooth real
function as a combination of the coordinate functions of any finitely-indexed basis, each taken
relative to its own value at `x`, with smooth coefficients. At the base point those coefficients
are the directional derivatives along the basis.

```lean
ContMDiffMap.exists_hadamard_coords.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {ι : Type u_2} [Fintype ι]
  (f : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ ℝ) E ℝ ↑⊤) (x : E)
  (b : Module.Basis ι ℝ E) :
  ∃ a,
    (∀ (i : ι), (a i) x = (fderiv ℝ (⇑f) x) (b i)) ∧
      ∀ (y : E), f y - f x = ∑ i, (a i) y * ((b.coord i) y - (b.coord i) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's lemma along a graph](../../../../analysis/part-01/analytic/hadamards-lemma-along-a-graph.md)

## Lean

Formalized in Tau Ceti as [`ContMDiffMap.exists_hadamard_coords`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.html#ContMDiffMap.exists_hadamard_coords).

## Other forms

**Hadamard's lemma for holomorphic germs.** Formalized in Tau Ceti as [`OpenPartialHomeomorph.exists_eq_sum_holomorphicLinearCoordinateGerm_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/MaximalIdeal.html#OpenPartialHomeomorph.exists_eq_sum_holomorphicLinearCoordinateGerm_mul).

```lean
OpenPartialHomeomorph.exists_eq_sum_holomorphicLinearCoordinateGerm_mul.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {X : Type} [TopologicalSpace X] [ChartedSpace E X]
  (e : OpenPartialHomeomorph X E) (he : e ∈ IsManifold.maximalAtlas (modelWithCornersSelf ℂ E) ⊤ X)
  {x : X} [FiniteDimensional ℂ E] {ι : Type u_2} (b : Module.Basis ι ℂ E) [Fintype ι]
  (hx : x ∈ e.source)
  {s : ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ E) X).presheaf.stalk x)}
  (hs : (TauCeti.holomorphicStructureSheaf.eval (modelWithCornersSelf ℂ E) X x) s = 0) {φ : X → ℂ}
  (hφ :
    (TauCeti.holomorphicStructureSheaf.toFilterGerm (modelWithCornersSelf ℂ E) X x (nhds x) ⋯) s =
      ↑φ) :
  ∃ q,
    s =
        ∑ i,
          e.holomorphicLinearCoordinateGerm he x (LinearMap.toContinuousLinearMap (b.coord i)) hx *
            q i ∧
      ∀ (i : ι),
        (TauCeti.holomorphicStructureSheaf.eval (modelWithCornersSelf ℂ E) X x) (q i) =
          (fderiv ℂ (φ ∘ ↑e.symm) (↑e x)) (b i)
```

**Hadamard's lemma for the vanishing ideal.** Formalized in Tau Ceti as [`TauCeti.mem_smoothVanishingIdeal_sq_of_mvfderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Algebra/VanishingIdeal/Basic.html#TauCeti.mem_smoothVanishingIdeal_sq_of_mvfderiv_eq_zero).

```lean
TauCeti.mem_smoothVanishingIdeal_sq_of_mvfderiv_eq_zero.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M] [T2Space M] {x : M} (hx : I.IsInteriorPoint x)
  {f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤} (hf₀ : f x = 0) (hf₁ : d% ⇑f x = 0) :
  f ∈ TauCeti.smoothVanishingIdeal I x ^ 2
```

## Sources

- [Tau Ceti documentation: `ContMDiffMap.exists_hadamard_coords`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.html#ContMDiffMap.exists_hadamard_coords)
- [Source of `ContMDiffMap.exists_hadamard_coords` in TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/ContMDiffMap/Hadamard.lean#L32)
