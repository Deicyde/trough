---
declaration: theorem
origin: cited
lean: TauCeti.mk_isoClasses_le_aleph_one_of_countable_levels
statement: formalized
proof: formalized
---

# The stratification bound

If every countable back-and-forth level of a set `K` of
configurations on `ℕ` has countably many classes, then `K` meets at most `ℵ₁` isomorphism
classes. The set `K` need not be Borel or isomorphism invariant, and the language need not be
countable.

```lean
TauCeti.mk_isoClasses_le_aleph_one_of_countable_levels.{u, v} {L : FirstOrder.Language}
  [L.IsRelational] (K : Set (TauCeti.RelationalConfiguration L ℕ))
  (hlevels :
    ∀ α < Ordinal.omega 1,
      Countable
        (Quotient
          (Setoid.comap Subtype.val (TauCeti.RelationalConfiguration.bfEquivSetoid L ℕ α)))) :
  Cardinal.mk
      (Quotient (Setoid.comap Subtype.val (TauCeti.RelationalConfiguration.isoSetoid L ℕ))) ≤
    Cardinal.aleph 1
```

## Depends on

- [TauCeti.BFEquiv](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-bfequiv.md)

## Proof depends on

- [The Scott height is an isolating rank](the-scott-height-is-an-isolating-rank.md)
- [TauCeti.IsIsolatingRank](tauceti-isisolatingrank.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mk_isoClasses_le_aleph_one_of_countable_levels`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Stratification.html#TauCeti.mk_isoClasses_le_aleph_one_of_countable_levels).

## Sources

- [Tau Ceti documentation: `TauCeti.mk_isoClasses_le_aleph_one_of_countable_levels`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Stratification.html#TauCeti.mk_isoClasses_le_aleph_one_of_countable_levels)
- [Source of `TauCeti.mk_isoClasses_le_aleph_one_of_countable_levels` in TauCeti/ModelTheory/Counting/Stratification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Counting/Stratification.lean#L236)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CountableModelCounting/STATUS.md)
