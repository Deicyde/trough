---
declaration: theorem
origin: cited
lean: TauCeti.cauchy_box
statement: formalized
proof: formalized
---

# TauCeti.cauchy_box

The two-sided box Cauchy theorem: the ordered field `g * eᵢ * f` has zero boundary
flux when `g` is right Fueter regular and `f` is left Fueter regular in the open box.
Only continuity on the closed box and pointwise regularity in its interior are required.

```lean
TauCeti.cauchy_box {a b : Fin 4 → ℝ} (hab : a ≤ b) {f g : Quaternion ℝ → Quaternion ℝ}
  (hg : ContinuousOn g (⇑TauCeti.Quaternion.dq '' Set.Icc a b))
  (hf : ContinuousOn f (⇑TauCeti.Quaternion.dq '' Set.Icc a b))
  (hgr :
    TauCeti.RightFueterOn g (⇑TauCeti.Quaternion.dq '' Set.univ.pi fun i => Set.Ioo (a i) (b i)))
  (hfl :
    TauCeti.LeftFueterOn f (⇑TauCeti.Quaternion.dq '' Set.univ.pi fun i => Set.Ioo (a i) (b i))) :
  (TauCeti.boxBoundarySum a b fun i x =>
      g (TauCeti.Quaternion.dq x) * TauCeti.Quaternion.dq (Pi.single i 1) *
        f (TauCeti.Quaternion.dq x)) =
    0
```

## Depends on

- [TauCeti.LeftFueterAt](tauceti-leftfueterat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cauchy_box`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cauchy.html#TauCeti.cauchy_box).

## Sources

- [Tau Ceti documentation: `TauCeti.cauchy_box`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cauchy.html#TauCeti.cauchy_box)
- [Source of `TauCeti.cauchy_box` in TauCeti/Analysis/Quaternion/Cauchy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/Cauchy.lean#L45)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
