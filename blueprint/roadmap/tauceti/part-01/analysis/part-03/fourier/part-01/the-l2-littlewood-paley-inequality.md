---
declaration: theorem
origin: cited
lean: TauCeti.exists_sum_norm_fourierMultiplierCLM_sq_le
statement: formalized
proof: formalized
---

# The `L²` Littlewood–Paley inequality

Let `V` be a finite-dimensional real inner product
space, let `φ` be a smooth bump function on `V`, and let `Δⱼ` be the `L²` Fourier multipliers with
the pieces `ψⱼ` of the inhomogeneous Littlewood–Paley partition as symbols. For every complex
Hilbert space `F` there is a constant `L` such that for every `f ∈ L²(V, F)` and every finite set
`s` of indices,

`∑_{j ∈ s} ‖Δⱼ f‖₂² ≤ L ‖f‖₂²`.

Each symbol enters as any element of `L^∞` almost everywhere equal to `ψⱼ`.

```lean
TauCeti.exists_sum_norm_fourierMultiplierCLM_sq_le.{u_1, u_2} {V : Type u_1} {F : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [NormedAddCommGroup F]
  [InnerProductSpace ℂ F] [MeasurableSpace V] [BorelSpace V] [CompleteSpace F]
  (φ : ContDiffBump 0) :
  ∃ L,
    0 ≤ L ∧
      ∀ (m : ℕ → ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)),
        (∀ (j : ℕ),
            ↑↑(m j) =ᵐ[MeasureTheory.volume] fun ξ => ↑(φ.inhomogeneousLittlewoodPaley j ξ)) →
          ∀ (f : ↥(MeasureTheory.Lp F 2 MeasureTheory.volume)) (s : Finset ℕ),
            ∑ j ∈ s, ‖(MeasureTheory.Lp.fourierMultiplierCLM F (m j)) f‖ ^ 2 ≤ L * ‖f‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_sum_norm_fourierMultiplierCLM_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LittlewoodPaley.html#TauCeti.exists_sum_norm_fourierMultiplierCLM_sq_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_sum_norm_fourierMultiplierCLM_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LittlewoodPaley.html#TauCeti.exists_sum_norm_fourierMultiplierCLM_sq_le)
- [Source of `TauCeti.exists_sum_norm_fourierMultiplierCLM_sq_le` in TauCeti/Analysis/Fourier/LittlewoodPaley.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/LittlewoodPaley.lean#L535)
