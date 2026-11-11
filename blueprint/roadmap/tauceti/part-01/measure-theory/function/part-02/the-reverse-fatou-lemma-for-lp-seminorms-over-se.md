---
declaration: theorem
origin: cited
lean: TauCeti.limsup_eLpNorm_restrict_le
statement: formalized
proof: formalized
---

# The reverse Fatou lemma for `Lᵖ` seminorms over sets

Let `0 < p < ∞`, let the sets `s n`
be measurable and contained in `t`, and let `g ∈ Lᵖ(t)`. Then the limit superior of the `Lᵖ`
seminorms of `g` over `s n` is at most its `Lᵖ` seminorm over `limsup s n`.

```lean
TauCeti.limsup_eLpNorm_restrict_le.{u_1, u_2} {α : Type u_1} {E : Type u_2} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} [NormedAddCommGroup E] {g : α → E} {p : ENNReal} (hp0 : p ≠ 0)
  (hptop : p ≠ ⊤) {s : ℕ → Set α} {t : Set α} (hg : MeasureTheory.MemLp g p (μ.restrict t))
  (hs : ∀ (n : ℕ), MeasurableSet (s n)) (hst : ∀ (n : ℕ), s n ⊆ t) :
  Filter.limsup (fun n => MeasureTheory.eLpNorm g p (μ.restrict (s n))) Filter.atTop ≤
    MeasureTheory.eLpNorm g p (μ.restrict (Filter.limsup s Filter.atTop))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The reverse Fatou lemma for integrals over sets](../../integral/part-02/the-reverse-fatou-lemma-for-integrals-over-sets.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.limsup_eLpNorm_restrict_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/DominatedConvergence.html#TauCeti.limsup_eLpNorm_restrict_le).

## Sources

- [Tau Ceti documentation: `TauCeti.limsup_eLpNorm_restrict_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/DominatedConvergence.html#TauCeti.limsup_eLpNorm_restrict_le)
- [Source of `TauCeti.limsup_eLpNorm_restrict_le` in TauCeti/MeasureTheory/Function/Lp/DominatedConvergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Lp/DominatedConvergence.lean#L112)
