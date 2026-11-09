---
declaration: theorem
origin: cited
lean: TauCeti.Contour.Cycle.integral_integral_swap
statement: formalized
proof: formalized
---

# Fubini's theorem for cycles

For a function `F` continuous on the product of the traces of
two cycles `C` and `D`,

`∫_C (∫_D F z w dw) dz = ∫_D (∫_C F z w dz) dw`.

```lean
TauCeti.Contour.Cycle.integral_integral_swap.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {F : ℂ → ℂ → E} {C D : TauCeti.Contour.Cycle}
  (hF : ContinuousOn (Function.uncurry F) (C.trace ×ˢ D.trace)) :
  (TauCeti.Contour.Cycle.integral fun z => (TauCeti.Contour.Cycle.integral (F z)) D) C =
    (TauCeti.Contour.Cycle.integral fun w => (TauCeti.Contour.Cycle.integral fun z => F z w) C) D
```

## Depends on

- [TauCeti.Contour.Cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-cycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.integral_integral_swap`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Fubini.html#TauCeti.Contour.Cycle.integral_integral_swap).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.Cycle.integral_integral_swap`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Fubini.html#TauCeti.Contour.Cycle.integral_integral_swap)
- [Source of `TauCeti.Contour.Cycle.integral_integral_swap` in TauCeti/Analysis/Contour/Cycle/Fubini.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cycle/Fubini.lean#L111)
