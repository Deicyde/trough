---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty
statement: formalized
proof: formalized
---

# Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property

```lean
TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty.{v} {p : ℕ} [Fact (Nat.Prime p)]
  {G : Type v} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (hG : TauCeti.IsDemushkin p G) :
  ∃! χ, TauCeti.HasPrescriptionProperty χ
```

## Depends on

- [The Demushkin predicate](../../profinite-and-pro-p-groups/the-demushkin-predicate.md)

## Proof depends on

- [Burnside's basis theorem, cardinal form](burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Character/Basic.html#TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Character/Basic.html#TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty)
- [Source of `TauCeti.IsDemushkin.existsUnique_hasPrescriptionProperty` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Character/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Character/Basic.lean#L207)
