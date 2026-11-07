---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.isUnit_iff_forall_isUnit
statement: formalized
proof: formalized
---

# Wiener's lemma for `H^s(A)`, `s > 1/2`

An element of `H^s(A)` is a unit if and only if
its continuous representative takes invertible values at every point of the circle.

```lean
TauCeti.CircleSobolev.isUnit_iff_forall_isUnit.{u_1} {s : ℝ} {A : Type u_1} [NormedCommRing A]
  [NormedAlgebra ℂ A] [CompleteSpace A] [hs : Fact (1 / 2 < s)] (T : ℝ) [Fact (0 < T)]
  {a : TauCeti.CircleSobolev s A} :
  IsUnit a ↔ ∀ (x : AddCircle T), IsUnit (((TauCeti.CircleSobolev.toContinuousMap T ⋯) a) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.isUnit_iff_forall_isUnit`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Spectrum.html#TauCeti.CircleSobolev.isUnit_iff_forall_isUnit).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.isUnit_iff_forall_isUnit`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Spectrum.html#TauCeti.CircleSobolev.isUnit_iff_forall_isUnit)
- [Source of `TauCeti.CircleSobolev.isUnit_iff_forall_isUnit` in TauCeti/Analysis/Sobolev/Circle/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Circle/Spectrum.lean#L247)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
