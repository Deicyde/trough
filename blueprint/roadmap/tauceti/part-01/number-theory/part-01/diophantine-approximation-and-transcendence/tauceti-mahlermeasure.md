---
declaration: def
origin: cited
lean: TauCeti.mahlerMeasure
statement: formalized
---

# TauCeti.mahlerMeasure

The *Mahler measure* `M(x)` of `x`: the Mahler measure of its primitive minimal polynomial
`F_x`, mapped to `ℂ[X]`. For algebraic `x` this is `a₀ ∏ max(1, |x⁽ⁱ⁾|)` over the complex
conjugates of `x` (`mahlerMeasure_eq_leadingCoeff_mul_prod`); for transcendental `x` it is `1`.

```lean
TauCeti.mahlerMeasure.{u_1} {F : Type u_1} [Field F] [CharZero F] (x : F) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mahlerMeasure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/MahlerMeasure.html#TauCeti.mahlerMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.mahlerMeasure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/MahlerMeasure.html#TauCeti.mahlerMeasure)
- [Source of `TauCeti.mahlerMeasure` in TauCeti/NumberTheory/Height/MahlerMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Height/MahlerMeasure.lean#L63)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
