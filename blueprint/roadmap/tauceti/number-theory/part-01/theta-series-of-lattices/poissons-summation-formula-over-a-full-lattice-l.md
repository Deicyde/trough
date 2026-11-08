---
declaration: theorem
origin: cited
lean: SchwartzMap.tsum_eq_tsum_dual_fourier, SchwartzMap.tsum_eq_tsum_fourier_span_orthonormalBasis
statement: formalized
proof: formalized
---

# Poisson's summation formula over a full lattice `L` of a finite-dimensional real inner product space

for a Schwartz function `f` and `v : E`,
`∑' ℓ : L, f (v + ℓ) = (covolume L)⁻¹ * ∑' m : L^∨, 𝓕 f m * exp (2πi ⟪v, m⟫)`.
The sign of the phase is the one forced by Mathlib's `𝓕 f w = ∫ x, exp (-2πi ⟪x, w⟫) f x`.

```lean
SchwartzMap.tsum_eq_tsum_dual_fourier.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  (f : SchwartzMap E ℂ) (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L] (v : E) :
  ∑' (ℓ : ↥L), f (v + ↑ℓ) =
    (↑(ZLattice.covolume L MeasureTheory.volume))⁻¹ *
      ∑' (m : ↥(ZLattice.dual L)),
        FourierTransform.fourier ⇑f ↑m * Complex.exp (2 * ↑Real.pi * Complex.I * ↑(inner ℝ v ↑m))
```

## Depends on

- [ZLattice.dual](zlattice-dual.md)

## Lean

Formalized in Tau Ceti as [`SchwartzMap.tsum_eq_tsum_dual_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/PoissonSummation.html#SchwartzMap.tsum_eq_tsum_dual_fourier).

## Other forms

**Poisson's summation formula over the lattice `L` spanned by an orthonormal basis `o` of a finite-dimensional real inner product space.** Formalized in Tau Ceti as [`SchwartzMap.tsum_eq_tsum_fourier_span_orthonormalBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/PoissonSummation.html#SchwartzMap.tsum_eq_tsum_fourier_span_orthonormalBasis).

```lean
SchwartzMap.tsum_eq_tsum_fourier_span_orthonormalBasis.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] {ι : Type u_2} [Fintype ι] (f : SchwartzMap E ℂ)
  (o : OrthonormalBasis ι ℝ E) [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (v : E) :
  ∑' (ℓ : ↥(Submodule.span ℤ (Set.range ⇑o))), f (v + ↑ℓ) =
    ∑' (m : ↥(Submodule.span ℤ (Set.range ⇑o))),
      FourierTransform.fourier ⇑f ↑m * Complex.exp (2 * ↑Real.pi * Complex.I * ↑(inner ℝ v ↑m))
```

## Sources

- [Tau Ceti documentation: `SchwartzMap.tsum_eq_tsum_dual_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/PoissonSummation.html#SchwartzMap.tsum_eq_tsum_dual_fourier)
- [Source of `SchwartzMap.tsum_eq_tsum_dual_fourier` in TauCeti/Analysis/Fourier/PoissonSummation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/PoissonSummation.lean#L305)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
