---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.integral_abs_hamiltonianCurvature_neckStretch_le
statement: formalized
proof: formalized
---

# Uniform curvature bound for neck-stretching

Let `K` be cylindrical near the line `s = c`,
that is `K_s = 0` and `K_t` independent of `s` there, and let `M` bound the curvature of `K`
pointwise over the rectangle `[a₁, b₁] × [a₂, b₂]` containing that line. Then for every neck length
`L ≥ 0` and every map `u`, the integrated curvature of the stretched datum along `u` over the
stretched rectangle `[a₁, b₁ + L] × [a₂, b₂]` is at most `∫ M` over the original rectangle.

```lean
TauCeti.SymplecticForm.integral_abs_hamiltonianCurvature_neckStretch_le.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] {Ks Kt : ℝ × ℝ → V → ℝ} {c L : ℝ}
  (ω : TauCeti.SymplecticForm V) (hL : 0 ≤ L) (hKs : ∀ᶠ (s : ℝ) in nhds c, ∀ (t : ℝ), Ks (s, t) = 0)
  (hKt : ∀ᶠ (s : ℝ) in nhds c, ∀ (t : ℝ), Kt (s, t) = Kt (c, t)) (u : ℝ × ℝ → V) {M : ℝ × ℝ → ℝ}
  {a b : ℝ × ℝ} (hac : a.1 ≤ c) (hcb : c ≤ b.1)
  (hM : ∀ z ∈ Set.Icc a b, ∀ (x : V), |ω.hamiltonianCurvature Ks Kt z x| ≤ M z)
  (hMi : MeasureTheory.IntegrableOn M (Set.Icc a b) MeasureTheory.volume) :
  ∫ (z : ℝ × ℝ) in Set.Icc a (b.1 + L, b.2),
      |ω.hamiltonianCurvature (TauCeti.Floer.neckStretch c L Ks) (TauCeti.Floer.neckStretch c L Kt)
          z (u z)| ≤
    ∫ (z : ℝ × ℝ) in Set.Icc a b, M z
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_abs_hamiltonianCurvature_neckStretch_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Neck.html#TauCeti.SymplecticForm.integral_abs_hamiltonianCurvature_neckStretch_le).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.integral_abs_hamiltonianCurvature_neckStretch_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Neck.html#TauCeti.SymplecticForm.integral_abs_hamiltonianCurvature_neckStretch_le)
- [Source of `TauCeti.SymplecticForm.integral_abs_hamiltonianCurvature_neckStretch_le` in TauCeti/Geometry/Symplectic/Floer/Neck.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Floer/Neck.lean#L422)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
