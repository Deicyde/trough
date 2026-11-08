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
- [Source of `TauCeti.Huber.exists_tateSeminorm` in TauCeti/RingTheory/Huber/TateGauge/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/TateGauge/Basic.lean#L352)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
