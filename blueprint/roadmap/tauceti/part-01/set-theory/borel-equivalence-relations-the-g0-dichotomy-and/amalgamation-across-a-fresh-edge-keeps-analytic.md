---
declaration: theorem
origin: cited
lean: SetRel.not_isSmallFamily_comb_cross
statement: formalized
proof: formalized
---

# Amalgamation across a fresh edge keeps analytic families from being small

Let `X` be a
Hausdorff space with its Borel σ-algebra, `G` an analytic relation, `ι` countable, and `Φ` an
analytic family that is not small. If `comb φ₀ φ₁` takes only values of `φ₀` and `φ₁`, then for
every index `s` the family of combinations `comb φ₀ φ₁` of members `φ₀, φ₁ ∈ Φ` with
`(φ₀ s, φ₁ s) ∈ G` is not small.

```lean
SetRel.not_isSmallFamily_comb_cross.{u_1, u_2, u_3} {X : Type u_1} {ι : Type u_2} {κ : Type u_3}
  [MeasurableSpace X] {G : SetRel X X} {Φ : Set (ι → X)} [TopologicalSpace X] [T2Space X]
  [BorelSpace X] [Countable ι] (hG : MeasureTheory.AnalyticSet G)
  (hΦa : MeasureTheory.AnalyticSet Φ) (hΦ : ¬G.IsSmallFamily Φ) (s : ι)
  {comb : (ι → X) → (ι → X) → κ → X}
  (hcomb : ∀ (φ₀ φ₁ : ι → X), Set.range (comb φ₀ φ₁) ⊆ Set.range φ₀ ∪ Set.range φ₁) :
  ¬G.IsSmallFamily {ψ | ∃ φ₀ ∈ Φ, ∃ φ₁ ∈ Φ, (φ₀ s, φ₁ s) ∈ G ∧ comb φ₀ φ₁ = ψ}
```

## Depends on

- [SetRel.IsSmallFamily](setrel-issmallfamily.md)

## Proof depends on

- [The Kechris–Solecki–Todorcevic lemma](../descriptive/the-kechris-solecki-todorcevic-lemma.md)

## Lean

Formalized in Tau Ceti as [`SetRel.not_isSmallFamily_comb_cross`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/SmallFamily/Basic.html#SetRel.not_isSmallFamily_comb_cross).

## Sources

- [Tau Ceti documentation: `SetRel.not_isSmallFamily_comb_cross`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/SmallFamily/Basic.html#SetRel.not_isSmallFamily_comb_cross)
- [Source of `SetRel.not_isSmallFamily_comb_cross` in TauCeti/SetTheory/Descriptive/SmallFamily/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/SmallFamily/Basic.lean#L198)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
