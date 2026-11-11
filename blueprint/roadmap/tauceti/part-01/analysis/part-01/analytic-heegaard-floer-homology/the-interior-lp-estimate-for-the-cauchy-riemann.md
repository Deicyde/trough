---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_add_eLpNorm
statement: formalized
proof: formalized
---

# The interior `Lᵖ` estimate for the Cauchy–Riemann operator

For `1 < p < ∞`, `U ⊆ ℂ`
open and `K ⊆ U` compact, there is a constant `C` such that every map `u` smooth on `U` satisfies
`‖Du‖_{Lᵖ(K)} ≤ C (‖\bar∂u‖_{Lᵖ(U)} + ‖u‖_{Lᵖ(U)})`.

```lean
TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_add_eLpNorm.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] {p : ENNReal} (hp : 1 < p)
  (hp_top : p ≠ ⊤) {U K : Set ℂ} (hU : IsOpen U) (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ C,
    ∀ (u : ℂ → F),
      ContDiffOn ℝ (↑⊤) u U →
        MeasureTheory.eLpNorm (fderiv ℝ u) p (MeasureTheory.volume.restrict K) ≤
          ↑C *
            (MeasureTheory.eLpNorm (fun z => (TauCeti.conjWirtingerDeriv u z) 1) p
                (MeasureTheory.volume.restrict U) +
              MeasureTheory.eLpNorm u p (MeasureTheory.volume.restrict U))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Calderón–Zygmund inequality for the Cauchy–Riemann operator](the-calderon-zygmund-inequality-for-the-cauchy-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_add_eLpNorm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/InteriorEstimate.html#TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_add_eLpNorm).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_add_eLpNorm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/InteriorEstimate.html#TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_add_eLpNorm)
- [Source of `TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_add_eLpNorm` in TauCeti/Analysis/Complex/Wirtinger/InteriorEstimate.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Wirtinger/InteriorEstimate.lean#L256)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
