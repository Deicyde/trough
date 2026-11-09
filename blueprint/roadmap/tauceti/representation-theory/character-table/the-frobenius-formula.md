---
declaration: theorem
origin: cited
lean: TauCeti.card_productOneTriples_eq_sum_characterTable
statement: formalized
proof: formalized
---

# The Frobenius formula

The number of triples `(x, y, z)` with `x ∈ C₀`, `y ∈ C₁`,
`z ∈ C∞` and `z * y * x = 1` is

`(|C₀| · |C₁| · |C∞| / |G|) · ∑_χ χ(C₀) χ(C₁) χ(C∞) / χ(1)`,

the sum running over the irreducible characters of `G`.

```lean
TauCeti.card_productOneTriples_eq_sum_characterTable.{u, v} {k : Type u} {G : Type v} [Field k]
  [IsAlgClosed k] [CharZero k] [Group G] [Fintype G] [DecidableEq G] [Invertible ↑(Nat.card G)]
  (C0 C1 Cinf : ConjClasses G) :
  ↑(TauCeti.productOneTriples C0 C1 Cinf).card =
    ↑(Nat.card ↑C0.carrier) * ↑(Nat.card ↑C1.carrier) * ↑(Nat.card ↑Cinf.carrier) / ↑(Nat.card G) *
      ∑ l,
        TauCeti.characterTable k G l C0 * TauCeti.characterTable k G l C1 *
            TauCeti.characterTable k G l Cinf /
          ↑(TauCeti.characterDegree k l)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schur's lemma, vanishing form](../../ring-theory/part-02/semisimple/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.card_productOneTriples_eq_sum_characterTable`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/ProductOne.html#TauCeti.card_productOneTriples_eq_sum_characterTable).

## Sources

- [Tau Ceti documentation: `TauCeti.card_productOneTriples_eq_sum_characterTable`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/ProductOne.html#TauCeti.card_productOneTriples_eq_sum_characterTable)
- [Source of `TauCeti.card_productOneTriples_eq_sum_characterTable` in TauCeti/RepresentationTheory/CharacterTable/ProductOne.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/CharacterTable/ProductOne.lean#L188)
