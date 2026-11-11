---
declaration: theorem
origin: cited
lean: TauCeti.WeakDerivStep.isFredholm_trajectoryOperator_of_hasLyapunovForm
statement: formalized
proof: formalized
---

# The trajectory operator with hyperbolic limits is Fredholm

For a continuous family `A`
of operators on a finite-dimensional real inner product space whose limits at `±∞` have Lyapunov
forms, `u ↦ u' + A u` is a Fredholm operator from `W^{1,2}(ℝ, E)` to `L²(ℝ, E)`. Neither symmetry
nor differentiability of `A` is assumed.

```lean
TauCeti.WeakDerivStep.isFredholm_trajectoryOperator_of_hasLyapunovForm.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {A : ℝ → E →L[ℝ] E}
  (hA : Continuous A) {Aminus Aplus : E →L[ℝ] E} (hminus : Aminus.HasLyapunovForm)
  (hplus : Aplus.HasLyapunovForm) (hbot : Filter.Tendsto A Filter.atBot (nhds Aminus))
  (htop : Filter.Tendsto A Filter.atTop (nhds Aplus))
  (AL : ↥(MeasureTheory.Lp (E →L[ℝ] E) ⊤ (MeasureTheory.volume.restrict ↑⊤)))
  (hAL : ↑↑AL =ᵐ[MeasureTheory.volume.restrict ↑⊤] A) :
  (TauCeti.WeakDerivStep.trajectoryOperator AL).IsFredholm
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The endpoint local Morrey estimate](../../part-03/sobolev/part-01/the-endpoint-local-morrey-estimate.md)
- [The fundamental theorem of calculus for weak derivatives on the line](../../part-03/sobolev/part-01/the-fundamental-theorem-of-calculus-for-weak-der-2.md)
- [The local Morrey inequality](../../part-03/sobolev/part-01/the-local-morrey-inequality.md)
- [Rellich–Kondrachov on bounded Lipschitz domains](../../part-03/sobolev/part-02/rellich-kondrachov-on-bounded-lipschitz-domains.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WeakDerivStep.isFredholm_trajectoryOperator_of_hasLyapunovForm`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/EnergyEstimate/Lyapunov.html#TauCeti.WeakDerivStep.isFredholm_trajectoryOperator_of_hasLyapunovForm).

## Sources

- [Tau Ceti documentation: `TauCeti.WeakDerivStep.isFredholm_trajectoryOperator_of_hasLyapunovForm`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/EnergyEstimate/Lyapunov.html#TauCeti.WeakDerivStep.isFredholm_trajectoryOperator_of_hasLyapunovForm)
- [Source of `TauCeti.WeakDerivStep.isFredholm_trajectoryOperator_of_hasLyapunovForm` in TauCeti/Analysis/ODE/EnergyEstimate/Lyapunov.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/ODE/EnergyEstimate/Lyapunov.lean#L190)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
