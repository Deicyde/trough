---
declaration: theorem
origin: cited
lean: TauCeti.mellin_eq_integral_exp_smul
statement: formalized
proof: formalized
---

# TauCeti.mellin_eq_integral_exp_smul

The Mellin transform in logarithmic coordinates: `𝓜f(s) = ∫_ℝ e^{-su} f(e^{-u}) du`.

```lean
TauCeti.mellin_eq_integral_exp_smul.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  (f : ℝ → E) (s : ℂ) : mellin f s = ∫ (u : ℝ), Complex.exp (-s * ↑u) • f (Real.exp (-u))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mellin_eq_integral_exp_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/MellinTransform/Basic.html#TauCeti.mellin_eq_integral_exp_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.mellin_eq_integral_exp_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/MellinTransform/Basic.html#TauCeti.mellin_eq_integral_exp_smul)
- [Source of `TauCeti.mellin_eq_integral_exp_smul` in TauCeti/Analysis/MellinTransform/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/MellinTransform/Basic.lean#L86)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
