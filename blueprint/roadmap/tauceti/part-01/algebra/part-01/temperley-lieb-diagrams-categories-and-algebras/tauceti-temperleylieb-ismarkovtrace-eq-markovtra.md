---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace
statement: formalized
proof: formalized
---

# TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace

Every Markov trace at a loop parameter `δ = -(q + q⁻¹)` is the spin-model trace, by
uniqueness of Markov traces.

```lean
TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace.{u_1} {R : Type u_1} [CommRing R] (q : Rˣ)
  {δ : R} (hδ : δ = -(↑q + ↑q⁻¹)) {tr : (n : ℕ) → TauCeti.TemperleyLieb R δ n →ₗ[R] R}
  (htr : TauCeti.TemperleyLieb.IsMarkovTrace R δ tr) :
  tr = fun x => TauCeti.TemperleyLieb.markovTrace q hδ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The tower normal form](the-tower-normal-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/MarkovTrace.html#TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/MarkovTrace.html#TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace)
- [Source of `TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace` in TauCeti/Algebra/TemperleyLieb/MarkovTrace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TemperleyLieb/MarkovTrace.lean#L536)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
