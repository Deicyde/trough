---
declaration: theorem
origin: cited
lean: Setoid.countable_or_hasCantorAntichainOn_of_measurableSet
statement: formalized
proof: formalized
---

# Silver's theorem relative to a Borel subset

Let `A` be a Borel subset of a Polish space
`X`, `F` a Borel equivalence relation on `A`, and `R` any equivalence relation on `X` whose
restriction to `A` refines `F`. Then `F` has countably many classes, or `A` carries a Cantor
antichain for `R`, continuous for the topology of `X`.

```lean
Setoid.countable_or_hasCantorAntichainOn_of_measurableSet.{u_1} {X : Type u_1} [TopologicalSpace X]
  [PolishSpace X] [MeasurableSpace X] [BorelSpace X] {A : Set X} (hA : MeasurableSet A)
  (R : Setoid X) (F : Setoid ↑A) (hRF : ∀ (x y : ↑A), R ↑x ↑y → F x y)
  (hF : MeasurableSet {p | F p.1 p.2}) : Countable (Quotient F) ∨ R.HasCantorAntichainOn A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The perfect set theorem for Borel sets (Alexandrov–Hausdorff)](../../measure-theory/constructions/the-perfect-set-theorem-for-borel-sets-alexandro.md)
- [Silver's theorem](silvers-theorem.md)

## Lean

Formalized in Tau Ceti as [`Setoid.countable_or_hasCantorAntichainOn_of_measurableSet`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.countable_or_hasCantorAntichainOn_of_measurableSet).

## Sources

- [Tau Ceti documentation: `Setoid.countable_or_hasCantorAntichainOn_of_measurableSet`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.countable_or_hasCantorAntichainOn_of_measurableSet)
- [Source of `Setoid.countable_or_hasCantorAntichainOn_of_measurableSet` in TauCeti/SetTheory/Descriptive/Silver.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/Silver.lean#L159)
