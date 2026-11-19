---
declaration: theorem
origin: cited
lean: TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq
statement: formalized
proof: formalized
---

# TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq

For a separable source, approximate unitary equivalence is equivalent to pointwise
convergence of conjugates along a sequence of target unitaries.

```lean
TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq.{u_1, u_2} {A : Type u_1}
  {B : Type u_2} [NonUnitalCStarAlgebra A] [CStarAlgebra B] {φ ψ : A →⋆ₙₐ[ℂ] B}
  [TopologicalSpace.SeparableSpace A] :
  TauCeti.ApproximatelyUnitarilyEquivalent φ ψ ↔
    ∃ u, ∀ (a : A), Filter.Tendsto (fun n => ↑(u n) * φ a * star ↑(u n)) Filter.atTop (nhds (ψ a))
```

## Depends on

- [TauCeti.ApproximatelyUnitarilyEquivalent](tauceti-approximatelyunitarilyequivalent.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Sequential.html#TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq).

## Sources

- [Tau Ceti documentation: `TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Sequential.html#TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq)
- [Source of `TauCeti.ApproximatelyUnitarilyEquivalent.iff_exists_unitary_seq` in TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Sequential.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/ApproximateUnitaryEquivalence/Sequential.lean#L50)
- [Tau Ceti roadmap status: Classification of AF and purely infinite simple C*-algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CStarClassification/STATUS.md)
