---
declaration: theorem
origin: cited
lean: TauCeti.isDemushkin_iff_nondegenerate_degreeOneForm, TauCeti.isDemushkin_of_nondegenerate_degreeOneForm
statement: formalized
proof: formalized
---

# Labute's criterion

Let `F` be the free pro-`p` group on a finite type `X`, let `r ∈ Φ(F)`,
and let `G ≅ ⟨X ∣ r⟩`. Then `G` is a Demushkin group exactly when `X` is nonempty and the degree-one
form of the class of `r` in `gr_1(F)` is nondegenerate.

```lean
TauCeti.isDemushkin_iff_nondegenerate_degreeOneForm.{u, v} {p : ℕ} [Fact (Nat.Prime p)] {X : Type u}
  [Finite X] {r : TauCeti.freeProP p X} {G : Type v} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (hr : r ∈ TauCeti.proPFrattini p (TauCeti.freeProP p X))
  (e : TauCeti.presentedProP p X {r} ≃ₜ* G) :
  TauCeti.IsDemushkin p G ↔
    Nonempty X ∧
      (TauCeti.freeProP.degreeOneForm
          (TauCeti.gradedMk p (TauCeti.freeProP p X) 1 ⟨r, ⋯⟩)).Nondegenerate
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isDemushkin_iff_nondegenerate_degreeOneForm`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Criterion.html#TauCeti.isDemushkin_iff_nondegenerate_degreeOneForm).

## Other forms

**Labute's criterion, sufficiency.** Formalized in Tau Ceti as [`TauCeti.isDemushkin_of_nondegenerate_degreeOneForm`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Criterion.html#TauCeti.isDemushkin_of_nondegenerate_degreeOneForm).

```lean
TauCeti.isDemushkin_of_nondegenerate_degreeOneForm.{u, v} {p : ℕ} [Fact (Nat.Prime p)] {X : Type u}
  [Finite X] {r : TauCeti.freeProP p X} {G : Type v} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (hr : r ∈ TauCeti.proPFrattini p (TauCeti.freeProP p X)) (e : TauCeti.presentedProP p X {r} ≃ₜ* G)
  [Nonempty X]
  (hnd :
    (TauCeti.freeProP.degreeOneForm
        (TauCeti.gradedMk p (TauCeti.freeProP p X) 1 ⟨r, ⋯⟩)).Nondegenerate) :
  TauCeti.IsDemushkin p G
```

## Sources

- [Tau Ceti documentation: `TauCeti.isDemushkin_iff_nondegenerate_degreeOneForm`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Criterion.html#TauCeti.isDemushkin_iff_nondegenerate_degreeOneForm)
- [Source of `TauCeti.isDemushkin_iff_nondegenerate_degreeOneForm` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Criterion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Criterion.lean#L212)
