---
declaration: theorem
origin: cited
lean: TauCeti.IsGoodDixonPrime.eq_of_intCast_eq_of_natAbs_le_sqrt, TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt
statement: formalized
proof: formalized
---

# Dixon's size bound opens a wide enough residue window

Two integers of absolute value at
most `⌊√|G|⌋` that agree modulo `p` are equal, so an integer of that size is determined by its
residue. This is why the lift is unambiguous.

```lean
TauCeti.IsGoodDixonPrime.eq_of_intCast_eq_of_natAbs_le_sqrt.{u_1} {G : Type u_1} [Group G] {p : ℕ}
  (hp : TauCeti.IsGoodDixonPrime G p) {z w : ℤ} (hz : z.natAbs ≤ (Nat.card G).sqrt)
  (hw : w.natAbs ≤ (Nat.card G).sqrt) (h : ↑z = ↑w) : z = w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsGoodDixonPrime.eq_of_intCast_eq_of_natAbs_le_sqrt`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.eq_of_intCast_eq_of_natAbs_le_sqrt).

## Other forms

**Dixon's size bound in the shape the residue window asks for.** Formalized in Tau Ceti as [`TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt).

```lean
TauCeti.IsGoodDixonPrime.two_mul_natAbs_lt_of_natAbs_le_sqrt.{u_1} {G : Type u_1} [Group G] {p : ℕ}
  (hp : TauCeti.IsGoodDixonPrime G p) {z : ℤ} (hz : z.natAbs ≤ (Nat.card G).sqrt) : 2 * z.natAbs < p
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsGoodDixonPrime.eq_of_intCast_eq_of_natAbs_le_sqrt`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.html#TauCeti.IsGoodDixonPrime.eq_of_intCast_eq_of_natAbs_le_sqrt)
- [Source of `TauCeti.IsGoodDixonPrime.eq_of_intCast_eq_of_natAbs_le_sqrt` in TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/CharacterTable/Dixon/Prime.lean#L204)
