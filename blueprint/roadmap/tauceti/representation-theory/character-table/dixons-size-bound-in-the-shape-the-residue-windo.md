---
declaration: theorem
origin: cited
lean: TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt
statement: formalized
proof: formalized
---

# Dixon's size bound in the shape the residue window asks for

An integer of absolute value
at most `⌊√|G|⌋` lies strictly inside the window of half-width `p / 2`, since `2⌊√|G|⌋ < p`.

```lean
TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt.{u_1} {G : Type u_1} [Group G] {p : ℕ}
  (hp : TauCeti.IsGoodDixonPrime G p) {z : ℤ} (hz : z.natAbs ≤ (Nat.card G).sqrt) : 2 * z.natAbs < p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt).

## Sources

- [Tau Ceti documentation: `TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt)
- [Source of `TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt` in TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean#L189)
