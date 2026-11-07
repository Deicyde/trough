---
declaration: theorem
origin: cited
lean: TauCeti.WeakDerivStep.index_trajectoryOperator_eq_finrank_pointSpectralSubspace_sub_finrank
statement: formalized
proof: formalized
---

# The index of the trajectory operator is a difference of Morse indices

Let `A` be a
continuous family of operators on a finite-dimensional real inner product space with invertible
symmetric limits `A±` at `±∞`. Then the index of the
trajectory operator `u ↦ u' + A u` from `W^{1,2}(ℝ, E)` to `L²(ℝ, E)` is the number of negative
eigenvalues of `A⁻` minus the number of negative eigenvalues of `A⁺`, counted with multiplicity:
the dimensions of the sums of their eigenspaces at negative eigenvalues.

```lean
TauCeti.WeakDerivStep.index_trajectoryOperator_eq_finrank_pointSpectralSubspace_sub_finrank.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  {A : ℝ → E →L[ℝ] E} (hA : Continuous A) {Aminus Aplus : E →L[ℝ] E}
  (hsymminus : (↑Aminus).IsSymmetric) (hsymplus : (↑Aplus).IsSymmetric) {α : ℝ} (hα : 0 < α)
  (hminus : ∀ (v : E), α * ‖v‖ ≤ ‖Aminus v‖) (hplus : ∀ (v : E), α * ‖v‖ ≤ ‖Aplus v‖)
  (hbot : Filter.Tendsto A Filter.atBot (nhds Aminus))
  (htop : Filter.Tendsto A Filter.atTop (nhds Aplus))
  (AL : ↥(MeasureTheory.Lp (E →L[ℝ] E) ⊤ (MeasureTheory.volume.restrict ↑⊤)))
  (hAL : ↑↑AL =ᵐ[MeasureTheory.volume.restrict ↑⊤] A) :
  (TauCeti.WeakDerivStep.trajectoryOperator AL).index =
    ↑(Module.finrank ℝ ↥(Module.End.pointSpectralSubspace (↑Aminus) (Set.Iio 0))) -
      ↑(Module.finrank ℝ ↥(Module.End.pointSpectralSubspace (↑Aplus) (Set.Iio 0)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.WeakDerivStep.index_trajectoryOperator_eq_finrank_pointSpectralSubspace_sub_finrank`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/EnergyEstimate/Index.html#TauCeti.WeakDerivStep.index_trajectoryOperator_eq_finrank_pointSpectralSubspace_sub_finrank).

## Sources

- [Tau Ceti documentation: `TauCeti.WeakDerivStep.index_trajectoryOperator_eq_finrank_pointSpectralSubspace_sub_finrank`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/EnergyEstimate/Index.html#TauCeti.WeakDerivStep.index_trajectoryOperator_eq_finrank_pointSpectralSubspace_sub_finrank)
- [Source of `TauCeti.WeakDerivStep.index_trajectoryOperator_eq_finrank_pointSpectralSubspace_sub_finrank` in TauCeti/Analysis/ODE/EnergyEstimate/Index.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/ODE/EnergyEstimate/Index.lean#L526)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
