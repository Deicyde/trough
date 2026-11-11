---
declaration: theorem
origin: cited
lean: TauCeti.Huber.exists_tateSeminorm
statement: formalized
proof: formalized
---

# TauCeti.Huber.exists_tateSeminorm

A ring with separately continuous multiplication in which the sets `ϖ ^ n A₀`, `n ≥ 0`, form
a neighbourhood basis of zero carries an ultrametric ring seminorm, equal to the Tate gauge, whose
open balls about zero form a neighbourhood basis of zero.

```lean
TauCeti.Huber.exists_tateSeminorm.{u_1} {A : Type u_1} [CommRing A] {A₀ : Subring A} {ϖ : Aˣ}
  {a : ℝ} [TopologicalSpace A]
  (hb : (nhds 0).HasBasis (fun x => True) fun n => {x | ↑(ϖ ^ (-↑n)) * x ∈ A₀})
  [SeparatelyContinuousMul A] (ha : 1 < a) (hϖ : ↑ϖ ∈ A₀) :
  ∃ α,
    (∀ (x : A), α x = TauCeti.Huber.tateGauge A₀ ϖ a x) ∧
      IsNonarchimedean ⇑α ∧ (nhds 0).HasBasis (fun ε => 0 < ε) fun ε => {x | α x < ε}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.exists_tateSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TateGauge/Basic.html#TauCeti.Huber.exists_tateSeminorm).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.exists_tateSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TateGauge/Basic.html#TauCeti.Huber.exists_tateSeminorm)
- [Source of `TauCeti.Huber.exists_tateSeminorm` in TauCeti/RingTheory/Huber/TateGauge/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Huber/TateGauge/Basic.lean#L353)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
