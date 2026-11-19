---
declaration: theorem
origin: cited
lean: TauCeti.integral_mul_comp_mul_eq_mellinInv
statement: formalized
proof: formalized
---

# TauCeti.integral_mul_comp_mul_eq_mellinInv

DLMF 2.5.5, the Parseval formula: if `𝓜f(1 - z)` and `𝓜h(z)` converge absolutely on the line
`Re z = c`, their product is integrable along that line, and `I(x) = ∫₀^∞ f(t) h(xt) dt` is
continuous at `x > 0`, then `I(x) = (2πi)⁻¹ ∫_{c-i∞}^{c+i∞} x^{-z} 𝓜f(1 - z) 𝓜h(z) dz`.

```lean
TauCeti.integral_mul_comp_mul_eq_mellinInv {f h : ℝ → ℂ} {c x : ℝ} (hx : 0 < x)
  (hconv : ∀ (z : ℂ), z.re = c → MellinConvergent f (1 - z) ∧ MellinConvergent h z)
  (hint :
    Complex.VerticalIntegrable (fun z => mellin f (1 - z) * mellin h z) c MeasureTheory.volume)
  (hcont : ContinuousAt (fun x => ∫ (t : ℝ) in Set.Ioi 0, f t * h (x * t)) x) :
  ∫ (t : ℝ) in Set.Ioi 0, f t * h (x * t) = mellinInv c (fun z => mellin f (1 - z) * mellin h z) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.mellin_eq_integral_exp_smul](tauceti-mellin-eq-integral-exp-smul.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_mul_comp_mul_eq_mellinInv`](https://taucetiproject.org/docs/TauCeti/Analysis/MellinTransform/Convolution.html#TauCeti.integral_mul_comp_mul_eq_mellinInv).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_mul_comp_mul_eq_mellinInv`](https://taucetiproject.org/docs/TauCeti/Analysis/MellinTransform/Convolution.html#TauCeti.integral_mul_comp_mul_eq_mellinInv)
- [Source of `TauCeti.integral_mul_comp_mul_eq_mellinInv` in TauCeti/Analysis/MellinTransform/Convolution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/MellinTransform/Convolution.lean#L161)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
