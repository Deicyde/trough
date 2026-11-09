---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv, TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_of_hasCompactSupport
statement: formalized
proof: formalized
---

# The Calderón–Zygmund inequality for the Cauchy–Riemann operator

Let `1 < p < ∞`. There
is a constant `C` with

`‖Du‖_{Lᵖ} ≤ C ‖\bar∂u‖_{Lᵖ}`

for every Schwartz function `u` on `ℂ` with values in a complex Hilbert space, where `Du` is the
real derivative of `u` and `\bar∂u = (∂ₓu + I ∂ᵧu) / 2` its conjugate Wirtinger derivative.

```lean
TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] {p : ENNReal} (hp : 1 < p)
  (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : SchwartzMap ℂ F),
      MeasureTheory.eLpNorm (fderiv ℝ ⇑u) p MeasureTheory.volume ≤
        ↑C *
          MeasureTheory.eLpNorm (fun z => (TauCeti.conjWirtingerDeriv (⇑u) z) 1) p
            MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mihlin–Hörmander multiplier theorem on `Lᵖ`](../../../part-01/partial-differential-equations/the-mihlin-hormander-multiplier-theorem-on-lp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/CalderonZygmund.html#TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv).

## Other forms

**The Calderón–Zygmund inequality for smooth compactly supported maps.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_of_hasCompactSupport`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/CalderonZygmund.html#TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_of_hasCompactSupport).

```lean
TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv_of_hasCompactSupport.{u_1}
  {F : Type u_1} [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] {p : ENNReal}
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : ℂ → F),
      ContDiff ℝ (↑⊤) u →
        HasCompactSupport u →
          MeasureTheory.eLpNorm (fderiv ℝ u) p MeasureTheory.volume ≤
            ↑C *
              MeasureTheory.eLpNorm (fun z => (TauCeti.conjWirtingerDeriv u z) 1) p
                MeasureTheory.volume
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/CalderonZygmund.html#TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv)
- [Source of `TauCeti.exists_eLpNorm_fderiv_le_eLpNorm_conjWirtingerDeriv` in TauCeti/Analysis/Complex/Wirtinger/CalderonZygmund.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Wirtinger/CalderonZygmund.lean#L142)
