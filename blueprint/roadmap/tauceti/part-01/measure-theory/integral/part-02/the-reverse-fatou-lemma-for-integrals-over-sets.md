---
declaration: theorem
origin: cited
lean: TauCeti.limsup_setLIntegral_le
statement: formalized
proof: formalized
---

# The reverse Fatou lemma for integrals over sets

Let the sets `s n` be measurable and
contained in a set `t` over which `f` is almost everywhere measurable with finite integral. Then
the limit superior of the integrals of `f` over `s n` is at most the integral of `f` over
`limsup s n`, the set of points that lie in `s n` for infinitely many `n`.

```lean
TauCeti.limsup_setLIntegral_le.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {f : α → ENNReal} {s : ℕ → Set α} {t : Set α}
  (hf : AEMeasurable f (μ.restrict t)) (hs : ∀ (n : ℕ), MeasurableSet (s n))
  (hst : ∀ (n : ℕ), s n ⊆ t) (ht : ∫⁻ (x : α) in t, f x ∂μ ≠ ⊤) :
  Filter.limsup (fun n => ∫⁻ (x : α) in s n, f x ∂μ) Filter.atTop ≤
    ∫⁻ (x : α) in Filter.limsup s Filter.atTop, f x ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.limsup_setLIntegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Lebesgue/DominatedConvergence.html#TauCeti.limsup_setLIntegral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.limsup_setLIntegral_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Lebesgue/DominatedConvergence.html#TauCeti.limsup_setLIntegral_le)
- [Source of `TauCeti.limsup_setLIntegral_le` in TauCeti/MeasureTheory/Integral/Lebesgue/DominatedConvergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Lebesgue/DominatedConvergence.lean#L119)
