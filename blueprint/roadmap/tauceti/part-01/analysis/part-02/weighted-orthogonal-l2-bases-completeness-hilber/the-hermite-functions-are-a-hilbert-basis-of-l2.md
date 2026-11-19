---
declaration: def
origin: cited
lean: TauCeti.hermiteHilbertBasis
statement: formalized
---

# The Hermite functions are a Hilbert basis of `L²(ℝ)`

Orthonormality comes from the
weighted-measure machinery and completeness from moment determinacy
(`TauCeti.orthogonal_span_range_bareNormalizedLp_eq_bot`), applied to the exact-degree family
`Hₙ(x√2)` against the Gaussian weight `e^{-x²}`.

```lean
TauCeti.hermiteHilbertBasis.{u_1} (𝕜 : Type u_1) [RCLike 𝕜] :
  HilbertBasis ℕ 𝕜 ↥(MeasureTheory.Lp 𝕜 2 MeasureTheory.volume)
```

## Depends on

- [The weight ↔ measure isometry](the-weight-measure-isometry.md)
- [The weighted-measure basis](the-weighted-measure-basis.md)

## Proof depends on

- [Moment determinacy, exponential-moment form](moment-determinacy-exponential-moment-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hermiteHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/HilbertBasis.html#TauCeti.hermiteHilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.hermiteHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/HilbertBasis.html#TauCeti.hermiteHilbertBasis)
- [Source of `TauCeti.hermiteHilbertBasis` in TauCeti/Analysis/SpecialFunctions/Hermite/Function/HilbertBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hermite/Function/HilbertBasis.lean#L97)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalL2Bases/STATUS.md)
