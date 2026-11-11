---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.lintegral_floerEnergyDensity_pairOfPantsPerturbation_eq
statement: formalized
proof: formalized
---

# The energy of a pair of pants

Let `K` be the pair-of-pants perturbation of period-one
`C¹` Hamiltonians `H_q` on the three ends of `S = ℂ ∖ {0, 1}`, and let `u` be a map which is `C²`
on `S` and solves the Floer equation `(du - X_K)^{0,1} = 0` there for almost complex structures
`J(z)` tamed by `ω`. If the actions of the loops `ℓ_q(t) = u(φ_q(±R + i t))` along the circles
`±s = R` of the ends converge to `a_q` as `R → ∞`, then the energy of `u` is

`E(u) = a_0 + a_1 - a_∞ - ∫_S R_K(u)`.

```lean
TauCeti.SymplecticForm.lintegral_floerEnergyDensity_pairOfPantsPerturbation_eq.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {H : TauCeti.ThricePuncturedSphere.Puncture → ℝ → V → ℝ} (ω : TauCeti.SymplecticForm V)
  (hH : ∀ (q : TauCeti.ThricePuncturedSphere.Puncture), Function.Periodic (H q) 1)
  (hHs : ∀ (q : TauCeti.ThricePuncturedSphere.Puncture), ContDiff ℝ 1 (Function.uncurry (H q)))
  {u : ℝ × ℝ → V}
  (hu :
    ContDiffOn ℝ 2 u
      {z | Complex.equivRealProdCLM.symm z ≠ 0 ∧ Complex.equivRealProdCLM.symm z ≠ 1})
  {J : ℝ × ℝ → TauCeti.AlmostComplexStructure V}
  (hJ :
    ∀ z ∈ {z | Complex.equivRealProdCLM.symm z ≠ 0 ∧ Complex.equivRealProdCLM.symm z ≠ 1},
      ω.Tames (J z))
  (hfloer :
    ∀ z ∈ {z | Complex.equivRealProdCLM.symm z ≠ 0 ∧ Complex.equivRealProdCLM.symm z ≠ 1},
      TauCeti.IsComplexLinearMap (TauCeti.AlmostComplexStructure.product ℝ) (J z)
        ↑(ω.perturbedFDeriv
            (fun z x =>
              (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) 1)
            (fun z x =>
              (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x)
                Complex.I)
            u z))
  {a : TauCeti.ThricePuncturedSphere.Puncture → ℝ}
  (ha :
    ∀ (q : TauCeti.ThricePuncturedSphere.Puncture),
      Filter.Tendsto
        (fun R =>
          ω.hamiltonianAction (H q) fun t =>
            u (Complex.equivRealProdCLM (q.cylindricalEndLift (↑(q.endSign * R) + ↑t * Complex.I))))
        Filter.atTop (nhds (a q))) :
  ∫⁻ (z : ℝ × ℝ) in {z | Complex.equivRealProdCLM.symm z ≠ 0 ∧ Complex.equivRealProdCLM.symm z ≠ 1},
      ENNReal.ofReal
        (ω.floerEnergyDensity
          (fun z x =>
            (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) 1)
          (fun z x =>
            (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) Complex.I)
          u z) =
    ENNReal.ofReal
      (∑ q, q.endSign * a q -
        ∫ (z : ℝ × ℝ) in
          {z | Complex.equivRealProdCLM.symm z ≠ 0 ∧ Complex.equivRealProdCLM.symm z ≠ 1},
          ω.hamiltonianCurvature
            (fun z x =>
              (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x) 1)
            (fun z x =>
              (TauCeti.Floer.pairOfPantsPerturbation H (Complex.equivRealProdCLM.symm z) x)
                Complex.I)
            z (u z))
```

## Depends on

- [TauCeti.Floer.pairOfPantsPerturbation](tauceti-floer-pairofpantsperturbation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.lintegral_floerEnergyDensity_pairOfPantsPerturbation_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Action.html#TauCeti.SymplecticForm.lintegral_floerEnergyDensity_pairOfPantsPerturbation_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.lintegral_floerEnergyDensity_pairOfPantsPerturbation_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Action.html#TauCeti.SymplecticForm.lintegral_floerEnergyDensity_pairOfPantsPerturbation_eq)
- [Source of `TauCeti.SymplecticForm.lintegral_floerEnergyDensity_pairOfPantsPerturbation_eq` in TauCeti/Geometry/Symplectic/Floer/PairOfPants/Action.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Floer/PairOfPants/Action.lean#L197)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
