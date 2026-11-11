---
declaration: theorem
origin: cited
lean: TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn
statement: formalized
proof: formalized
---

# TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn

A left Fueter regular function of class `C²` on an open set is harmonic there.

```lean
TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn {f : Quaternion ℝ → Quaternion ℝ}
  {s : Set (Quaternion ℝ)} {q : Quaternion ℝ} (hf : TauCeti.LeftFueterOn f s) (hs : IsOpen s)
  (h₂ : ContDiffOn ℝ 2 f s) (hq : q ∈ s) : Laplacian.laplacian f q = 0
```

## Depends on

- [TauCeti.LeftFueterAt](tauceti-leftfueterat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Harmonic.html#TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn).

## Sources

- [Tau Ceti documentation: `TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Harmonic.html#TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn)
- [Source of `TauCeti.LeftFueterOn.laplacian_eq_zero_of_contDiffOn` in TauCeti/Analysis/Quaternion/Harmonic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/Harmonic.lean#L123)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
