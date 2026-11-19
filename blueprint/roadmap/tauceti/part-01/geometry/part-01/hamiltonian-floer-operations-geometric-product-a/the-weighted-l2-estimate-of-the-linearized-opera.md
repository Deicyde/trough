---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.eventually_exists_mem_forall_setIntegral_exp_mul_le_mul_setIntegral_floerLinearization
statement: formalized
proof: formalized
---

# The weighted `L²` estimate of the linearized operator on an end

Under the hypotheses of
`eventually_exists_mem_forall_setIntegral_le_mul_setIntegral_floerLinearization_sub_smul`, for
every weight `δ` close enough to `0` there are a constant `C ≥ 0` and a
set `U ∈ l` of slices such that every `C²` map `η` of period one in `t`, vanishing on the slices
`s = a` and `s = b` with `[a, b] ⊆ U`, satisfies

`∫ e^{2 δ s} (g(∂s η, ∂s η) + g(∂t η - S η, ∂t η - S η) + g(η, η)) ≤ C ∫ e^{2 δ s} g(D_u η, D_u η)`

over `[a, b] × [0, 1]`, for the linearized Floer operator `D_u` of the datum `K = H_t dt`,
`S_t = dX_{H_t}(x(t))` and `g_t = ω(·, J_t(x(t)) ·)`. This is the estimate of `D_u` in the
`L²` norm with weight `e^{δ s}`; for `δ > 0` on a positive end (`l = atTop`), or `δ < 0` on a
negative end (`l = atBot`), the weight forces exponential decay. The constant does not depend on
`a`, `b` or `η`.

```lean
TauCeti.SymplecticForm.eventually_exists_mem_forall_setIntegral_exp_mul_le_mul_setIntegral_floerLinearization.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  (ω : TauCeti.SymplecticForm V) {H : ℝ → V → ℝ} {K : NNReal}
  (hX : LipschitzWith K (ω.timeDependentHamiltonianSuspension H))
  (hH : ContDiff ℝ 2 (Function.uncurry H)) {x : ℝ → V}
  (hx : ∀ (t : ℝ), HasDerivAt x (ω.hamiltonianVectorField (H t) (x t)) t)
  (hnd :
    TauCeti.IsNondegenerateFixedPt (modelWithCornersSelf ℝ V)
      (ω.timeDependentHamiltonianFlow H hX 0 1) (x 0))
  {J : ℝ → V → TauCeti.AlmostComplexStructure V}
  (hJ : ContDiff ℝ 1 fun p => LinearMap.toContinuousLinearMap (J p.1 p.2).toLinearMap)
  (hJx : ∀ (t : ℝ), ω.Compatible (J t (x t))) {l : Filter ℝ} {u : ℝ × ℝ → V}
  (hu : ∀ᶠ (s : ℝ) in l, ∀ t ∈ Set.Icc 0 1, ContDiffAt ℝ 1 u (s, t))
  (hux : TendstoUniformlyOn (fun s t => u (s, t)) x l (Set.Icc 0 1))
  (hδ :
    TendstoUniformlyOn
      (fun s t => TauCeti.sliceDefect (fun t => ω.hamiltonianVectorField (H t)) u (s, t)) 0 l
      (Set.Icc 0 1)) :
  ∀ᶠ (δ : ℝ) in nhds 0,
    ∃ C,
      0 ≤ C ∧
        ∃ U ∈ l,
          ∀ ⦃η : ℝ × ℝ → V⦄,
            ContDiff ℝ 2 η →
              (∀ (s t : ℝ), η (s, t + 1) = η (s, t)) →
                ∀ ⦃a b : ℝ⦄,
                  a ≤ b →
                    Set.Icc a b ⊆ U →
                      (∀ (t : ℝ), η (a, t) = 0) →
                        (∀ (t : ℝ), η (b, t) = 0) →
                          ∫ (z : ℝ × ℝ) in Set.Icc a b ×ˢ Set.Icc 0 1,
                              Real.exp (2 * δ * z.1) *
                                (((ω.associatedBilinForm (J z.2 (x z.2)))
                                        ((fderiv ℝ η z) TauCeti.stdComplexLineReal))
                                      ((fderiv ℝ η z) TauCeti.stdComplexLineReal) +
                                    ((ω.associatedBilinForm (J z.2 (x z.2)))
                                        ((fderiv ℝ η z) TauCeti.stdComplexLineImag -
                                          (fderiv ℝ (ω.hamiltonianVectorField (H z.2)) (x z.2))
                                            (η z)))
                                      ((fderiv ℝ η z) TauCeti.stdComplexLineImag -
                                        (fderiv ℝ (ω.hamiltonianVectorField (H z.2)) (x z.2))
                                          (η z)) +
                                  ((ω.associatedBilinForm (J z.2 (x z.2))) (η z)) (η z)) ≤
                            C *
                              ∫ (z : ℝ × ℝ) in Set.Icc a b ×ˢ Set.Icc 0 1,
                                Real.exp (2 * δ * z.1) *
                                  ((ω.associatedBilinForm (J z.2 (x z.2)))
                                      (ω.floerLinearization
                                        (fun w y =>
                                          LinearMap.toContinuousLinearMap (J w.2 y).toLinearMap)
                                        (fun x x_1 => 0) (fun w => H w.2) u η z))
                                    (ω.floerLinearization
                                      (fun w y =>
                                        LinearMap.toContinuousLinearMap (J w.2 y).toLinearMap)
                                      (fun x x_1 => 0) (fun w => H w.2) u η z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus in the first coordinate](../../../measure-theory/integral/part-01/the-fundamental-theorem-of-calculus-in-the-first.md)
- [The fundamental theorem of calculus in the second coordinate](../../../measure-theory/integral/part-01/the-fundamental-theorem-of-calculus-in-the-secon.md)
- [TauCeti.dysonSeries](../../../analysis/part-02/operator-algebra-dynamics-crossed-products-and-e/tauceti-dysonseries.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.eventually_exists_mem_forall_setIntegral_exp_mul_le_mul_setIntegral_floerLinearization`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/EndLinearization.html#TauCeti.SymplecticForm.eventually_exists_mem_forall_setIntegral_exp_mul_le_mul_setIntegral_floerLinearization).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.eventually_exists_mem_forall_setIntegral_exp_mul_le_mul_setIntegral_floerLinearization`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/EndLinearization.html#TauCeti.SymplecticForm.eventually_exists_mem_forall_setIntegral_exp_mul_le_mul_setIntegral_floerLinearization)
- [Source of `TauCeti.SymplecticForm.eventually_exists_mem_forall_setIntegral_exp_mul_le_mul_setIntegral_floerLinearization` in TauCeti/Geometry/Symplectic/Floer/EndLinearization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/EndLinearization.lean#L423)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
