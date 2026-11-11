---
declaration: theorem
origin: cited
lean: Finset.exists_injective_of_mul_card_le_card_smul
statement: formalized
proof: formalized
---

# Hall's theorem for expanding sets

If a finite set `D` acting on `β` satisfies
`k · |F| ≤ |D • F|` for every finite `F ⊆ β`, then there is an injective map
`j : β × Fin k → β` moving each point by an element of `D`: `j (x, i) = d • x` for some `d ∈ D`.

This applies Hall's marriage theorem to the neighbour sets `D • {x}` indexed by `β × Fin k`.

```lean
Finset.exists_injective_of_mul_card_le_card_smul.{u_1, u_2} {α : Type u_1} {β : Type u_2} [SMul α β]
  [DecidableEq β] {D : Finset α} {k : ℕ} (h : ∀ (F : Finset β), k * F.card ≤ (D • F).card) :
  ∃ j, Function.Injective j ∧ ∀ (p : β × Fin k), ∃ d ∈ D, d • p.1 = j p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Finset.exists_injective_of_mul_card_le_card_smul`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Additive/Expansion.html#Finset.exists_injective_of_mul_card_le_card_smul).

## Sources

- [Tau Ceti documentation: `Finset.exists_injective_of_mul_card_le_card_smul`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Additive/Expansion.html#Finset.exists_injective_of_mul_card_le_card_smul)
- [Source of `Finset.exists_injective_of_mul_card_le_card_smul` in TauCeti/Combinatorics/Additive/Expansion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Additive/Expansion.lean#L69)
