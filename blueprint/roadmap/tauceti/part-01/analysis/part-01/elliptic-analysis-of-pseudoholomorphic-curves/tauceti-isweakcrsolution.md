---
declaration: def
origin: cited
lean: TauCeti.IsWeakCRSolution
statement: formalized
---

# TauCeti.IsWeakCRSolution

`IsWeakCRSolution q Ω J DJ S ξ η` says that `ξ` is a **weak solution** of
`∂_s ξ + J ∂_t ξ + S ξ = η` on the open set `Ω`, with `DJ` standing for the weak derivative of
`J`: `ξ` is locally `L^q` on `Ω`, `η` is locally integrable on `Ω`, and for every test function
`φ ∈ 𝓓(Ω, V)` the pairing `⟪D* φ, ξ⟫` is integrable with

`∫ ⟪D* φ, ξ⟫ = ∫ ⟪φ, η⟫`,

where `D*` is `TauCeti.crFormalAdjoint J DJ S`.

The integrability of `ξ`, `η` and `⟪D* φ, ξ⟫` is part of the definition, since the Bochner
integral of a non-integrable function is `0`. The coefficients are unconstrained here; the
theorems using the weak equation assume `TauCeti.IsSobolevCRCoefficients p Ω J DJ S` and the
Hölder condition `p⁻¹ + q⁻¹ ≤ 1`, under which the pairing is automatically integrable for every
locally `L^q` field `ξ` (`TauCeti.IsSobolevCRCoefficients.integrable_inner_crFormalAdjoint`).

```lean
TauCeti.IsWeakCRSolution.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [CompleteSpace V] (q : ENNReal) (Ω : TopologicalSpace.Opens ℂ) (J : ℂ → V →L[ℝ] V)
  (DJ : ℂ → ℂ →L[ℝ] V →L[ℝ] V) (S : ℂ → V →L[ℝ] V) (ξ η : ℂ → V) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsWeakCRSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.html#TauCeti.IsWeakCRSolution).

## Sources

- [Tau Ceti documentation: `TauCeti.IsWeakCRSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.html#TauCeti.IsWeakCRSolution)
- [Source of `TauCeti.IsWeakCRSolution` in TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.lean#L120)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
