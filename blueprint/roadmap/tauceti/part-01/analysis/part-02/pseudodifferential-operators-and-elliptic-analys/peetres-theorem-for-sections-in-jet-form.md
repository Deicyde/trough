---
declaration: theorem
origin: cited
lean: LinearMap.exists_apply_eq_apply_of_sub_mem_smoothVanishingIdeal_pow_smul_top, LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq, LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow, LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow_smul_top
statement: formalized
proof: formalized
---

# Peetre's theorem for sections, in jet form

for every compact `K ⊆ U` there is `r` such
that `(P s) x = (P t) x` whenever `x ∈ K` and `s`, `t` have the same `r`-jet at `x`, that is,
`s - t ∈ I_x ^ (r + 1) Γ(V)`.

```lean
LinearMap.exists_apply_eq_apply_of_sub_mem_smoothVanishingIdeal_pow_smul_top.{u_1, u_2, u_3, u_4,
    u_5, u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {V : M → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] [ContMDiffVectorBundle (↑⊤) F V I] {F' : Type u_6} [NormedAddCommGroup F']
  [NormedSpace ℝ F'] {W : M → Type u_7} [TopologicalSpace (Bundle.TotalSpace F' W)]
  [(x : M) → AddCommGroup (W x)] [(x : M) → _root_.Module ℝ (W x)]
  [(x : M) → TopologicalSpace (W x)] [FiberBundle F' W] [VectorBundle ℝ F' W]
  [BoundarylessManifold I M] (P : ContMDiffSection I F (↑⊤) V →ₗ[ℝ] (x : M) → W x) {U : Set M}
  (hU : IsOpen U)
  (hloc : ∀ (s : ContMDiffSection I F (↑⊤) V), ∀ x ∈ U, (∀ᶠ (y : M) in nhds x, s y = 0) → P s x = 0)
  (hcont : ∀ (s : ContMDiffSection I F (↑⊤) V), ContinuousOn (fun x => ⟨x, P s x⟩) U) {K : Set M}
  (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r,
    ∀ x ∈ K,
      ∀ (s t : ContMDiffSection I F (↑⊤) V),
        s - t ∈ TauCeti.smoothVanishingIdeal I x ^ (r + 1) • ⊤ → P s x = P t x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's lemma](../../../geometry/part-02/manifold/part-02/hadamards-lemma.md)
- [Peetre's theorem](../../part-03/calculus/part-02/peetres-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_apply_of_sub_mem_smoothVanishingIdeal_pow_smul_top`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre/Section.html#LinearMap.exists_apply_eq_apply_of_sub_mem_smoothVanishingIdeal_pow_smul_top).

## Other forms

**Peetre's theorem on manifolds, in jet form.** Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre/Basic.html#LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq).

```lean
LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq.{u_1, u_2, u_3, u_4}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] {G : Type u_4} [NormedAddCommGroup G]
  [NormedSpace ℝ G] [BoundarylessManifold I M]
  (P : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤ →ₗ[ℝ] M → G) {U : Set M} (hU : IsOpen U)
  (hloc :
    ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ∀ x ∈ U, ⇑f =ᶠ[nhds x] 0 → P f x = 0)
  (hcont : ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ContinuousOn (P f) U)
  {K : Set M} (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r,
    ∀ x ∈ K,
      ∀ (f g : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤),
        (∀ k ≤ r,
            iteratedFDeriv ℝ k (⇑f ∘ ↑(extChartAt I x).symm) (↑(extChartAt I x) x) =
              iteratedFDeriv ℝ k (⇑g ∘ ↑(extChartAt I x).symm) (↑(extChartAt I x) x)) →
          P f x = P g x
```

**Peetre's theorem on manifolds.** Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre/Basic.html#LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow).

```lean
LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] {G : Type u_4} [NormedAddCommGroup G]
  [NormedSpace ℝ G] [BoundarylessManifold I M]
  (P : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤ →ₗ[ℝ] M → G) {U : Set M} (hU : IsOpen U)
  (hloc :
    ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ∀ x ∈ U, ⇑f =ᶠ[nhds x] 0 → P f x = 0)
  (hcont : ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ContinuousOn (P f) U)
  {K : Set M} (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r, ∀ x ∈ K, ∀ f ∈ TauCeti.smoothVanishingIdeal I x ^ (r + 1), P f x = 0
```

**Peetre's theorem for operators between sections of vector bundles.** Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow_smul_top`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre/Section.html#LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow_smul_top).

```lean
LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow_smul_top.{u_1, u_2, u_3, u_4, u_5,
    u_6, u_7}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] {F : Type u_4} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {V : M → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F V)] [(x : M) → AddCommGroup (V x)]
  [(x : M) → _root_.Module ℝ (V x)] [(x : M) → TopologicalSpace (V x)] [FiberBundle F V]
  [VectorBundle ℝ F V] [ContMDiffVectorBundle (↑⊤) F V I] {F' : Type u_6} [NormedAddCommGroup F']
  [NormedSpace ℝ F'] {W : M → Type u_7} [TopologicalSpace (Bundle.TotalSpace F' W)]
  [(x : M) → AddCommGroup (W x)] [(x : M) → _root_.Module ℝ (W x)]
  [(x : M) → TopologicalSpace (W x)] [FiberBundle F' W] [VectorBundle ℝ F' W]
  [BoundarylessManifold I M] (P : ContMDiffSection I F (↑⊤) V →ₗ[ℝ] (x : M) → W x) {U : Set M}
  (hU : IsOpen U)
  (hloc : ∀ (s : ContMDiffSection I F (↑⊤) V), ∀ x ∈ U, (∀ᶠ (y : M) in nhds x, s y = 0) → P s x = 0)
  (hcont : ∀ (s : ContMDiffSection I F (↑⊤) V), ContinuousOn (fun x => ⟨x, P s x⟩) U) {K : Set M}
  (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r, ∀ x ∈ K, ∀ s ∈ TauCeti.smoothVanishingIdeal I x ^ (r + 1) • ⊤, P s x = 0
```

## Sources

- [Tau Ceti documentation: `LinearMap.exists_apply_eq_apply_of_sub_mem_smoothVanishingIdeal_pow_smul_top`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre/Section.html#LinearMap.exists_apply_eq_apply_of_sub_mem_smoothVanishingIdeal_pow_smul_top)
- [Source of `LinearMap.exists_apply_eq_apply_of_sub_mem_smoothVanishingIdeal_pow_smul_top` in TauCeti/Geometry/Manifold/DifferentialOperator/Peetre/Section.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre/Section.lean#L186)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
