---
declaration: theorem
origin: cited
lean: Setoid.silver_dichotomy, Setoid.borelReducible_bot_iff_not_countable_quotient, Setoid.silver_dichotomy_standardBorel, Setoid.countable_or_hasCantorAntichainOn_of_measurableSet
statement: formalized
proof: formalized
---

# Silver's theorem

A Borel equivalence relation on a Polish space has countably many
classes, or a Cantor antichain on the whole space: a continuous map of Cantor space sending
distinct points to inequivalent points.

```lean
Setoid.silver_dichotomy.{u_1} {X : Type u_1} [TopologicalSpace X] [PolishSpace X]
  [MeasurableSpace X] [BorelSpace X] (E : Setoid X) (hE : MeasurableSet {p | E p.1 p.2}) :
  Countable (Quotient E) ∨ E.HasCantorAntichainOn Set.univ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The category route to Silver's theorem](the-category-route-to-silvers-theorem.md)
- [The Kechris–Solecki–Todorcevic lemma](the-kechris-solecki-todorcevic-lemma.md)
- [The perfect set theorem for Borel sets (Alexandrov–Hausdorff)](../../measure-theory/constructions/the-perfect-set-theorem-for-borel-sets-alexandro.md)

## Lean

Formalized in Tau Ceti as [`Setoid.silver_dichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.silver_dichotomy).

## Other forms

**Silver's theorem in reducibility form.** Formalized in Tau Ceti as [`Setoid.borelReducible_bot_iff_not_countable_quotient`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.borelReducible_bot_iff_not_countable_quotient).

```lean
Setoid.borelReducible_bot_iff_not_countable_quotient.{u_1} {X : Type u_1} [MeasurableSpace X]
  [StandardBorelSpace X] (E : Setoid X) (hE : MeasurableSet {p | E p.1 p.2}) :
  ⊥.BorelReducible E ↔ ¬Countable (Quotient E)
```

**Silver's theorem on a standard Borel space.** Formalized in Tau Ceti as [`Setoid.silver_dichotomy_standardBorel`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.silver_dichotomy_standardBorel).

```lean
Setoid.silver_dichotomy_standardBorel.{u_1} {X : Type u_1} [MeasurableSpace X]
  [StandardBorelSpace X] (E : Setoid X) (hE : MeasurableSet {p | E p.1 p.2}) :
  Countable (Quotient E) ∨ ∃ f, MeasurableEmbedding f ∧ ∀ (a b : ℕ → Bool), a ≠ b → ¬E (f a) (f b)
```

**Silver's theorem relative to a Borel subset.** Formalized in Tau Ceti as [`Setoid.countable_or_hasCantorAntichainOn_of_measurableSet`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.countable_or_hasCantorAntichainOn_of_measurableSet).

```lean
Setoid.countable_or_hasCantorAntichainOn_of_measurableSet.{u_1} {X : Type u_1} [TopologicalSpace X]
  [PolishSpace X] [MeasurableSpace X] [BorelSpace X] {A : Set X} (hA : MeasurableSet A)
  (R : Setoid X) (F : Setoid ↑A) (hRF : ∀ (x y : ↑A), R ↑x ↑y → F x y)
  (hF : MeasurableSet {p | F p.1 p.2}) : Countable (Quotient F) ∨ R.HasCantorAntichainOn A
```

## Sources

- [Tau Ceti documentation: `Setoid.silver_dichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.silver_dichotomy)
- [Source of `Setoid.silver_dichotomy` in TauCeti/SetTheory/Descriptive/Silver.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/Silver.lean#L127)
