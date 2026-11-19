---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsNondegenerate.exists_mem_periodicSolutions_tendstoUniformly_of_floer
statement: formalized
proof: formalized
---

# Periodic orbits at the end of a finite-energy Floer half-cylinder in a closed manifold

Let
`ω` be a nondegenerate two-form on a compact manifold `M`, `H` a `C¹` Hamiltonian, `1`-periodic in
time, and let `u` be `C¹` on the half-cylinder `s > a`, with `1`-periodic loops `t ↦ u(s, t)`,
solving the Floer equation `∂_s u + J (∂_t u - X_{H_t}(u)) = 0` on `(a, ∞) × [0, 1]`. Let
`e : M → F` be a `C¹` injective map with injective differential into a finite-dimensional normed
space, and suppose that the almost complex structures are uniformly tame with respect to `e`:
`c ‖d e v‖² ≤ ω(v, J z v)` with `c > 0`. If the energy of `u` over `(a, ∞) × [0, 1]` is finite,
then there are `s_n → ∞`, with `s_n > a`, such that the loops `t ↦ u(s_n, t)` converge to a
`1`-periodic orbit `x` of the Hamiltonian vector field, pointwise in `M` and uniformly after
applying `e`, and the `L²` norms of their defects `d e (∂_t u - X_{H_t}(u))` tend to `0`.

```lean
TauCeti.SmoothTwoForm.IsNondegenerate.exists_mem_periodicSolutions_tendstoUniformly_of_floer.{u_1,
    u_2, u_3, u_4}
  {E : Type u_1} {HM : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace HM] {I : ModelWithCorners ℝ E HM} [TopologicalSpace M] [ChartedSpace HM M]
  {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] {e : M → F} [IsManifold I (↑⊤) M]
  {ω : TauCeti.SmoothTwoForm I M} {H : ℝ → M → ℝ} [FiniteDimensional ℝ E] [FiniteDimensional ℝ F]
  [CompactSpace M] (hω : ω.IsNondegenerate)
  (hH :
    ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) 1 (Function.uncurry H))
  (hHper : Function.Periodic H 1) (he : ContMDiff I (modelWithCornersSelf ℝ F) 1 e)
  (he_inj : Function.Injective e) (hde : ∀ (p : M), Function.Injective ⇑(d% e p)) {u : ℝ × ℝ → M}
  {a : ℝ} (hu : ContMDiffOn (modelWithCornersSelf ℝ (ℝ × ℝ)) I 1 u (Set.Ioi a ×ˢ Set.univ))
  (hper : ∀ (s : ℝ), a < s → Function.Periodic (fun t => u (s, t)) 1)
  (J : (z : ℝ × ℝ) → TauCeti.AlmostComplexStructure (TangentSpace I (u z))) {c : ℝ} (hc : 0 < c)
  (hJc :
    ∀ z ∈ Set.Ioi a ×ˢ Set.Icc 0 1,
      ∀ (v : TangentSpace I (u z)),
        c * ‖(d% e (u z)) v‖ ^ 2 ≤
          (fun v w => ((hω.symplecticFormAt (u z)).toBilinForm v) w) v ((J z).toLinearMap v))
  (hfloer :
    ∀ z ∈ Set.Ioi a ×ˢ Set.Icc 0 1,
      (mfderiv% u z) TauCeti.stdComplexLineReal +
          (J z).toLinearMap
            ((mfderiv% u z) TauCeti.stdComplexLineImag - ω.hamiltonianVectorField (H z.2) (u z)) =
        0)
  (hE :
    ∫⁻ (z : ℝ × ℝ) in Set.Ioi a ×ˢ Set.Icc 0 1,
        ENNReal.ofReal (ω.floerEnergyDensity (fun x x_1 => 0) (fun w => H w.2) u z) ≠
      ⊤) :
  ∃ x ∈ TauCeti.periodicSolutions (fun t => ω.hamiltonianVectorField (H t)) 1,
    ∃ φ,
      (∀ (n : ℕ), a < φ n) ∧
        Filter.Tendsto φ Filter.atTop Filter.atTop ∧
          TendstoUniformly (fun n t => e (u (φ n, t))) (e ∘ x) Filter.atTop ∧
            (∀ (t : ℝ), Filter.Tendsto (fun n => u (φ n, t)) Filter.atTop (nhds (x t))) ∧
              Filter.Tendsto
                (fun n =>
                  ∫ (t : ℝ) in 0..1,
                    ‖(d% e (u (φ n, t)))
                          ((mfderiv% u (φ n, t)) TauCeti.stdComplexLineImag -
                            ω.hamiltonianVectorField (H t) (u (φ n, t)))‖ ^
                      2)
                Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Arzelà–Ascoli along exhausting bands](../../../../part-02/topology/other-results/arzela-ascoli-along-exhausting-bands.md)
- [The Cauchy–Schwarz inequality](../../../measure-theory/integral/part-01/the-cauchy-schwarz-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsNondegenerate.exists_mem_periodicSolutions_tendstoUniformly_of_floer`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/HalfCylinder/Manifold.html#TauCeti.SmoothTwoForm.IsNondegenerate.exists_mem_periodicSolutions_tendstoUniformly_of_floer).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsNondegenerate.exists_mem_periodicSolutions_tendstoUniformly_of_floer`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/HalfCylinder/Manifold.html#TauCeti.SmoothTwoForm.IsNondegenerate.exists_mem_periodicSolutions_tendstoUniformly_of_floer)
- [Source of `TauCeti.SmoothTwoForm.IsNondegenerate.exists_mem_periodicSolutions_tendstoUniformly_of_floer` in TauCeti/Geometry/Symplectic/Floer/HalfCylinder/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/HalfCylinder/Manifold.lean#L264)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
