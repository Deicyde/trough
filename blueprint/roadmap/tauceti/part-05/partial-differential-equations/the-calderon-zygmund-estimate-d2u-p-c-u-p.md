---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian
statement: formalized
proof: formalized
---

# The Calderón–Zygmund estimate `‖D²u‖_p ≤ C ‖Δu‖_p`

Let `1 < p < ∞`, and let `V` be a
finite-dimensional real inner product space with its volume measure. There is a constant `C` with

`‖D²u‖_{Lᵖ} ≤ C ‖Δu‖_{Lᵖ}`

for every Schwartz function `u` on `V` with values in a complex Hilbert space, where `D²u` is the
second Fréchet derivative of `u`.

```lean
TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian.{u_1, u_2} {F : Type u_1}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] {V : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : SchwartzMap V F),
      MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 ⇑u) p MeasureTheory.volume ≤
        ↑C * MeasureTheory.eLpNorm (⇑(Laplacian.laplacian u)) p MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.html#TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.html#TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian)
- [Source of `TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian` in TauCeti/Analysis/PDE/Regularity/Hessian/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.lean#L444)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
