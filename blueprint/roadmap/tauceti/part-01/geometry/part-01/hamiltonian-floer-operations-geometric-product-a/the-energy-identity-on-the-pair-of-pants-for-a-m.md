---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_pairOfPantsPerturbation
statement: formalized
proof: formalized
---

# The energy identity on the pair of pants, for a manifold target

Let `K` be the
pair-of-pants perturbation of bounded period-one `C¹` Hamiltonians `H_q` on a finite-dimensional
manifold with a nondegenerate two-form, with components `K_s(z) = K(z)(1)` and `K_t(z) = K(z)(i)`
in the global coordinate `z = s + i t` of `ℂ`. Let `u` be a map which is `C¹` on `S`, whose loops
`t ↦ u(φ_q(±R + i t))` along the circles of the end `q` converge pointwise to loops `x_q` as
`R → ∞`, and whose Floer energy density and symplectic area density are integrable over `S`. Then

`∫_S E = ∫_S u^*ω + ∑ q, ±∫₀¹ H_q(t, x_q(t)) dt - ∫_S R_K(u)`,

with the sign `+` on the input ends `0`, `1` and `-` on the output end `∞`. The middle term is the
boundary integral `∫_∂ K(u)` at the asymptotic orbits, and the curvature term is integrable
(`SmoothTwoForm.integrableOn_hamiltonianCurvature_pairOfPantsPerturbation`).

```lean
TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_pairOfPantsPerturbation.{u_1, u_2,
    u_3}
  {E : Type u_1} {G : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace G] {I : ModelWithCorners ℝ E G} [TopologicalSpace M] [ChartedSpace G M]
  [IsManifold I ⊤ M] [FiniteDimensional ℝ E] {ω : TauCeti.SmoothTwoForm I M}
  {H : TauCeti.ThricePuncturedSphere.Puncture → ℝ → M → ℝ} (hω : ω.IsNondegenerate)
  (hH : ∀ (q : TauCeti.ThricePuncturedSphere.Puncture), Function.Periodic (H q) 1)
  (hHs :
    ∀ (q : TauCeti.ThricePuncturedSphere.Puncture),
      ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (modelWithCornersSelf ℝ ℝ) 1
        (Function.uncurry (H q)))
  {B : TauCeti.ThricePuncturedSphere.Puncture → ℝ}
  (hB : ∀ (q : TauCeti.ThricePuncturedSphere.Puncture) (t : ℝ) (x : M), |H q t x| ≤ B q)
  {u : ℝ × ℝ → M}
  (hu : ContMDiffOn (modelWithCornersSelf ℝ (ℝ × ℝ)) I 1 u TauCeti.Floer.thricePuncturedSphereReal)
  {x : TauCeti.ThricePuncturedSphere.Puncture → ℝ → M}
  (hx :
    ∀ (q : TauCeti.ThricePuncturedSphere.Puncture) (t : ℝ),
      Filter.Tendsto
        (fun R =>
          u (Complex.equivRealProdCLM (q.cylindricalEndLift (↑(q.endSign * R) + ↑t * Complex.I))))
        Filter.atTop (nhds (x q t)))
  (hE :
    MeasureTheory.IntegrableOn
      (ω.floerEnergyDensity
        (fun z x => (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) 1)
        (fun z x =>
          (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) Complex.I)
        u)
      TauCeti.Floer.thricePuncturedSphereReal MeasureTheory.volume)
  (hA :
    MeasureTheory.IntegrableOn
      (fun z =>
        TauCeti.SmoothBundleForm.eval₂ ω (u z) ((mfderiv% u z) TauCeti.stdComplexLineReal)
          ((mfderiv% u z) TauCeti.stdComplexLineImag))
      TauCeti.Floer.thricePuncturedSphereReal MeasureTheory.volume) :
  ∫ (z : ℝ × ℝ) in TauCeti.Floer.thricePuncturedSphereReal,
      ω.floerEnergyDensity
        (fun z x => (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) 1)
        (fun z x =>
          (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) Complex.I)
        u z =
    ((∫ (z : ℝ × ℝ) in TauCeti.Floer.thricePuncturedSphereReal,
          TauCeti.SmoothBundleForm.eval₂ ω (u z) ((mfderiv% u z) TauCeti.stdComplexLineReal)
            ((mfderiv% u z) TauCeti.stdComplexLineImag)) +
        ∑ q, q.endSign * ∫ (t : ℝ) in 0..1, H q t (x q t)) -
      ∫ (z : ℝ × ℝ) in TauCeti.Floer.thricePuncturedSphereReal,
        ω.hamiltonianCurvature
          (fun z x =>
            (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) 1)
          (fun z x =>
            (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) Complex.I)
          z (u z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_pairOfPantsPerturbation`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Energy/Asymptotic.html#TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_pairOfPantsPerturbation).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_pairOfPantsPerturbation`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Energy/Asymptotic.html#TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_pairOfPantsPerturbation)
- [Source of `TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity_pairOfPantsPerturbation` in TauCeti/Geometry/Symplectic/Floer/PairOfPants/Energy/Asymptotic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Energy/Asymptotic.lean#L125)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
