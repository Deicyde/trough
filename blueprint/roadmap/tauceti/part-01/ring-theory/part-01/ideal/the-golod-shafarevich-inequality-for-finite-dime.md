---
declaration: theorem
origin: cited
lean: TauCeti.card_sq_lt_four_mul_card_of_relations_le_span
statement: formalized
proof: formalized
---

# The Golod–Shafarevich inequality for finite-dimensional algebras

Let `A` be a
finite-dimensional algebra over a field `k` and `I` a proper two-sided ideal of `A`, generated as
a left ideal by a nonempty finite family `x`. If every relation `∑ aᵢ xᵢ = 0` among the generators
is an `A`-linear combination of a finite family `y` of vectors in `A^ι` with all entries in `I`,
then `(#x)² < 4 · #y`.

```lean
TauCeti.card_sq_lt_four_mul_card_of_relations_le_span.{u_1, u_2, u_3, u_4} {A : Type u_1} [Ring A]
  {ι : Type u_2} {κ : Type u_3} [Fintype ι] [Fintype κ] (k : Type u_4) [Field k] [Algebra k A]
  [FiniteDimensional k A] [Nonempty ι] (I : Ideal A) [I.IsTwoSided] (hI : I ≠ ⊤) (x : ι → A)
  (hx : Submodule.span A (Set.range x) = I) (y : κ → ι → A) (hy : ∀ (j : κ) (i : ι), y j i ∈ I)
  (hker : ∀ (a : ι → A), ∑ i, a i * x i = 0 → a ∈ Submodule.span A (Set.range y)) :
  Fintype.card ι ^ 2 < 4 * Fintype.card κ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.card_sq_lt_four_mul_card_of_relations_le_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/GolodShafarevich.html#TauCeti.card_sq_lt_four_mul_card_of_relations_le_span).

## Sources

- [Tau Ceti documentation: `TauCeti.card_sq_lt_four_mul_card_of_relations_le_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/Ideal/GolodShafarevich.html#TauCeti.card_sq_lt_four_mul_card_of_relations_le_span)
- [Source of `TauCeti.card_sq_lt_four_mul_card_of_relations_le_span` in TauCeti/RingTheory/Ideal/GolodShafarevich.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Ideal/GolodShafarevich.lean#L65)
