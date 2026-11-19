---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd
statement: formalized
proof: formalized
---

# TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd

The real Fréchet derivative of `Q₀` at `ψ` is `B(ψ, ·)`, that is
`DQ₀|_ψ (φ) = φψ* + ψφ* - Re⟪ψ, φ⟫ Id`; this holds in the strict sense.

```lean
TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℂ E] (ψ : E) :
  HasStrictFDerivAt TauCeti.SeibergWitten.quadraticEnd (TauCeti.SeibergWitten.quadraticEndPolar ψ) ψ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/QuadraticEnd.html#TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/QuadraticEnd.html#TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd)
- [Source of `TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd` in TauCeti/Analysis/PDE/SeibergWitten/QuadraticEnd.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/QuadraticEnd.lean#L312)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
