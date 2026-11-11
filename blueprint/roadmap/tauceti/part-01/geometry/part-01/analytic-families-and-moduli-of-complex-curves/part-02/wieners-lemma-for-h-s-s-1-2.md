---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.isUnit_iff_forall_ne_zero, TauCeti.CircleSobolev.isUnit_iff_forall_isUnit
statement: formalized
proof: formalized
---

# Wiener's lemma for `H^s`, `s > 1/2`

An element of `H^s(ℂ)` is a unit if and only if its
continuous representative vanishes nowhere.

```lean
TauCeti.CircleSobolev.isUnit_iff_forall_ne_zero {s : ℝ} [hs : Fact (1 / 2 < s)] (T : ℝ)
  [Fact (0 < T)] {a : TauCeti.CircleSobolev s ℂ} :
  IsUnit a ↔ ∀ (x : AddCircle T), ((TauCeti.CircleSobolev.toContinuousMap T ⋯) a) x ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for unconditional sums in `ℝ≥0∞`](../../../../analysis/part-03/mean-inequalities/holders-inequality-for-unconditional-sums-in-r0.md)
- [Young's inequality](../../../../analysis/part-03/normed/part-02/youngs-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.isUnit_iff_forall_ne_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Spectrum.html#TauCeti.CircleSobolev.isUnit_iff_forall_ne_zero).

## Other forms

**Wiener's lemma for `H^s(A)`, `s > 1/2`.** Formalized in Tau Ceti as [`TauCeti.CircleSobolev.isUnit_iff_forall_isUnit`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Spectrum.html#TauCeti.CircleSobolev.isUnit_iff_forall_isUnit).

```lean
TauCeti.CircleSobolev.isUnit_iff_forall_isUnit.{u_1} {s : ℝ} {A : Type u_1} [NormedCommRing A]
  [NormedAlgebra ℂ A] [CompleteSpace A] [hs : Fact (1 / 2 < s)] (T : ℝ) [Fact (0 < T)]
  {a : TauCeti.CircleSobolev s A} :
  IsUnit a ↔ ∀ (x : AddCircle T), IsUnit (((TauCeti.CircleSobolev.toContinuousMap T ⋯) a) x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.isUnit_iff_forall_ne_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Spectrum.html#TauCeti.CircleSobolev.isUnit_iff_forall_ne_zero)
- [Source of `TauCeti.CircleSobolev.isUnit_iff_forall_ne_zero` in TauCeti/Analysis/Sobolev/Circle/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Circle/Spectrum.lean#L305)
