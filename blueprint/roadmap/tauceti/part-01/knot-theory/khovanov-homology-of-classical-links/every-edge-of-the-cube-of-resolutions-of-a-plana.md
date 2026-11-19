---
declaration: theorem
origin: cited
lean: TauCeti.PDCode.IsPlanar.card_circlesAt_eq_two_or_card_circlesAt_eq_two
statement: formalized
proof: formalized
---

# Every edge of the cube of resolutions of a planar code is a merge or a split

If two
states differ exactly at the crossing `c` of a planar code, then two circles pass through `c` in
one of the two smoothings: two circles of `s` merge into one circle of `t`, or one circle of `s`
splits into two circles of `t`.

```lean
TauCeti.PDCode.IsPlanar.card_circlesAt_eq_two_or_card_circlesAt_eq_two {n : ℕ}
  {D : TauCeti.PDCode n} {s t : Fin n → Bool} {c : Fin n} (hD : D.IsPlanar)
  (hst : ∀ (j : Fin n), j ≠ c → s j = t j) (hc : s c ≠ t c) :
  (D.circlesAt s c).card = 2 ∨ (D.circlesAt t c).card = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler's formula for a PD-code](../other-results/eulers-formula-for-a-pd-code.md)
- [Hurwitz's transposition bound](../../group-theory/permutations/hurwitzs-transposition-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.IsPlanar.card_circlesAt_eq_two_or_card_circlesAt_eq_two`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/ResolvedCircle/Planar.html#TauCeti.PDCode.IsPlanar.card_circlesAt_eq_two_or_card_circlesAt_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.IsPlanar.card_circlesAt_eq_two_or_card_circlesAt_eq_two`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/ResolvedCircle/Planar.html#TauCeti.PDCode.IsPlanar.card_circlesAt_eq_two_or_card_circlesAt_eq_two)
- [Source of `TauCeti.PDCode.IsPlanar.card_circlesAt_eq_two_or_card_circlesAt_eq_two` in TauCeti/KnotTheory/PDCode/ResolvedCircle/Planar.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/PDCode/ResolvedCircle/Planar.lean#L375)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
