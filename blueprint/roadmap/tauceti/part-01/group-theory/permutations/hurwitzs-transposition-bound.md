---
declaration: theorem
origin: cited
lean: TauCeti.card_add_orbitCount_le_length_add_two, TauCeti.card_add_orbitCount_add_two_le_length_add_two_mul_card_orbits, TauCeti.card_add_orbitCount_le_length_add_two_mul_card_orbits
statement: formalized
proof: formalized
---

# Hurwitz's transposition bound

If a list of transpositions generates a group acting
transitively on a finite type, its length is at least the number of points plus the number of
cycles of its product, minus two. Equivalently,
`Nat.card α + orbitCount L.prod ≤ L.length + 2`.

```lean
TauCeti.card_add_orbitCount_le_length_add_two.{u_1} {α : Type u_1} [DecidableEq α] [Finite α]
  {L : List (Equiv.Perm α)} (hL : ∀ g ∈ L, g.IsSwap)
  (htrans : MulAction.IsPretransitive (↥(Subgroup.closure {g | g ∈ L})) α) :
  Nat.card α + TauCeti.orbitCount L.prod ≤ L.length + 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.card_add_orbitCount_le_length_add_two`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/SwapFactors.html#TauCeti.card_add_orbitCount_le_length_add_two).

## Other forms

**Hurwitz's transposition bound with a defect.** Formalized in Tau Ceti as [`TauCeti.card_add_orbitCount_add_two_le_length_add_two_mul_card_orbits`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/SwapFactors.html#TauCeti.card_add_orbitCount_add_two_le_length_add_two_mul_card_orbits).

```lean
TauCeti.card_add_orbitCount_add_two_le_length_add_two_mul_card_orbits.{u_1} {α : Type u_1}
  [DecidableEq α] {a b : α} [Finite α] {L M : List (Equiv.Perm α)} (hL : ∀ g ∈ L, g.IsSwap)
  (hM : ∀ g ∈ M, g.IsSwap) (hab : b ∈ MulAction.orbit (↥(Subgroup.closure {g | g ∈ M})) a)
  (h : ¬M.prod.SameCycle a b) :
  Nat.card α + TauCeti.orbitCount (L ++ Equiv.swap a b :: M).prod + 2 ≤
    (L ++ Equiv.swap a b :: M).length +
      2 *
        Nat.card
          (MulAction.orbitRel.Quotient (↥(Subgroup.closure {g | g ∈ L ++ Equiv.swap a b :: M})) α)
```

**Hurwitz's transposition bound, componentwise.** Formalized in Tau Ceti as [`TauCeti.card_add_orbitCount_le_length_add_two_mul_card_orbits`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/SwapFactors.html#TauCeti.card_add_orbitCount_le_length_add_two_mul_card_orbits).

```lean
TauCeti.card_add_orbitCount_le_length_add_two_mul_card_orbits.{u_1} {α : Type u_1} [DecidableEq α]
  [Finite α] {L : List (Equiv.Perm α)} (hL : ∀ g ∈ L, g.IsSwap) :
  Nat.card α + TauCeti.orbitCount L.prod ≤
    L.length + 2 * Nat.card (MulAction.orbitRel.Quotient (↥(Subgroup.closure {g | g ∈ L})) α)
```

## Sources

- [Tau Ceti documentation: `TauCeti.card_add_orbitCount_le_length_add_two`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Perm/SwapFactors.html#TauCeti.card_add_orbitCount_le_length_add_two)
- [Source of `TauCeti.card_add_orbitCount_le_length_add_two` in TauCeti/GroupTheory/Perm/SwapFactors.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Perm/SwapFactors.lean#L583)
