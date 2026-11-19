---
declaration: theorem
origin: cited
lean: TauCeti.spectrum_holomorphicCalculus, TauCeti.spectrum_holomorphicCalculus_ofFun
statement: formalized
proof: formalized
---

# Spectral mapping theorem for the holomorphic calculus

the spectrum of `f(a)` is the set
of values of the germ `f` on the spectrum of `a`.

```lean
TauCeti.spectrum_holomorphicCalculus.{u_1} {A : Type u_1} [NormedRing A] [NormedAlgebra ℂ A]
  [CompleteSpace A] (a : A) (g : ↥(TauCeti.holomorphicGerms (spectrum ℂ a))) :
  spectrum ℂ ((TauCeti.holomorphicCalculus a) g) =
    {c | ∃ x, ∃ (hx : x ∈ spectrum ℂ a), (TauCeti.holomorphicGerms.eval x hx) g = c}
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [Piecewise `C¹` on the interval between `a` and `b`](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/piecewise-c1-on-the-interval-between-a-and-b.md)
- [TauCeti.Contour.Cycle](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-cycle.md)
- [TauCeti.holomorphicGerms](../../../part-01/banach-algebras/tauceti-holomorphicgerms.md)

## Proof depends on

- [Cauchy's integral formula, homology form](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/cauchys-integral-formula-homology-form.md)
- [Fubini's theorem for cycles](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/fubinis-theorem-for-cycles.md)
- [Fundamental theorem for absolutely continuous curves, integrability](../../../../measure-theory/function/part-01/fundamental-theorem-for-absolutely-continuous-cu.md)
- [The homology Cauchy theorem](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.spectrum_holomorphicCalculus`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/HolomorphicFunctionalCalculus/Spectrum.html#TauCeti.spectrum_holomorphicCalculus).

## Other forms

**Spectral mapping theorem for a holomorphic representative.** Formalized in Tau Ceti as [`TauCeti.spectrum_holomorphicCalculus_ofFun`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/HolomorphicFunctionalCalculus/Spectrum.html#TauCeti.spectrum_holomorphicCalculus_ofFun).

```lean
TauCeti.spectrum_holomorphicCalculus_ofFun.{u_1} {A : Type u_1} [NormedRing A] [NormedAlgebra ℂ A]
  [CompleteSpace A] (a : A) (f : ℂ → ℂ) (hf : AnalyticOnNhd ℂ f (spectrum ℂ a)) :
  spectrum ℂ ((TauCeti.holomorphicCalculus a) (TauCeti.holomorphicGerms.ofFun f hf)) =
    f '' spectrum ℂ a
```

## Sources

- [Tau Ceti documentation: `TauCeti.spectrum_holomorphicCalculus`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/HolomorphicFunctionalCalculus/Spectrum.html#TauCeti.spectrum_holomorphicCalculus)
- [Source of `TauCeti.spectrum_holomorphicCalculus` in TauCeti/Analysis/Normed/Algebra/HolomorphicFunctionalCalculus/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Algebra/HolomorphicFunctionalCalculus/Spectrum.lean#L63)
