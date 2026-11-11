---
declaration: theorem
origin: cited
lean: TauCeti.PDCode.card_circlesAt_add_card_circlesAt_le_three
statement: formalized
proof: formalized
---

# Two states differing exactly at a crossing do not both have two circles through it

So
along an edge of the cube of resolutions two circles merge into one, one circle splits into two,
or one circle through the crossing is replaced by one circle.

```lean
TauCeti.PDCode.card_circlesAt_add_card_circlesAt_le_three {n : ℕ} (D : TauCeti.PDCode n)
  {s t : Fin n → Bool} {c : Fin n} (hst : ∀ (j : Fin n), j ≠ c → s j = t j) (hc : s c ≠ t c) :
  (D.circlesAt s c).card + (D.circlesAt t c).card ≤ 3
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.card_circlesAt_add_card_circlesAt_le_three`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/ResolvedCircle/Adjacent.html#TauCeti.PDCode.card_circlesAt_add_card_circlesAt_le_three).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.card_circlesAt_add_card_circlesAt_le_three`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/ResolvedCircle/Adjacent.html#TauCeti.PDCode.card_circlesAt_add_card_circlesAt_le_three)
- [Source of `TauCeti.PDCode.card_circlesAt_add_card_circlesAt_le_three` in TauCeti/KnotTheory/PDCode/ResolvedCircle/Adjacent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/PDCode/ResolvedCircle/Adjacent.lean#L322)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KhovanovHomology/STATUS.md)
