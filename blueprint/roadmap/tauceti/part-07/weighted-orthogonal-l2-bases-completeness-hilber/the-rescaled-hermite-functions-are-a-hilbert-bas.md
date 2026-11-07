---
declaration: def
origin: cited
lean: TauCeti.twoPiHermiteHilbertBasis
statement: formalized
---

# The rescaled Hermite functions are a Hilbert basis of `L²(ℝ)`

This is the Hermite basis in
the normalization Mathlib's `e^{-2πixξ}` Fourier convention forces: the same bridge
`TauCeti.hilbertBasisOfOrthogonalSystem`, run at the weight `e^{-2πx²}` and the polynomials
`Hₙ(2√π·x)`.

```lean
TauCeti.twoPiHermiteHilbertBasis.{u_1} (𝕜 : Type u_1) [RCLike 𝕜] :
  HilbertBasis ℕ 𝕜 ↥(MeasureTheory.Lp 𝕜 2 MeasureTheory.volume)
```

## Depends on

- [The weight ↔ measure isometry](the-weight-measure-isometry.md)
- [The weighted-measure basis](the-weighted-measure-basis.md)

## Proof depends on

- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.twoPiHermiteHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.html#TauCeti.twoPiHermiteHilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.twoPiHermiteHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.html#TauCeti.twoPiHermiteHilbertBasis)
- [Source of `TauCeti.twoPiHermiteHilbertBasis` in TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Fourier/HilbertBasis.lean#L229)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalL2Bases/STATUS.md)
