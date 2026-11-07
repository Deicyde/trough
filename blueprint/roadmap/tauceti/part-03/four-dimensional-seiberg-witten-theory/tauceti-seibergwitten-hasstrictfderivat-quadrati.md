---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd
statement: formalized
proof: formalized
---

# TauCeti.SeibergWitten.hasStrictFDerivAt\_quadraticEnd

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
- [Source of `TauCeti.SeibergWitten.hasStrictFDerivAt_quadraticEnd` in TauCeti/Analysis/PDE/SeibergWitten/QuadraticEnd.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/SeibergWitten/QuadraticEnd.lean#L312)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
