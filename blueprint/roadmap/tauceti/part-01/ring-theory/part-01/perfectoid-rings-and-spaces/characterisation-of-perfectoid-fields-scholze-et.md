---
declaration: theorem
origin: cited
lean: TauCeti.Perfectoid.isPerfectoidField_iff
statement: formalized
proof: formalized
---

# Characterisation of perfectoid fields (Scholze, *Étale cohomology of diamonds*, Proposition 3.8)

a complete ultrametric nontrivially normed field `K` is a perfectoid field
exactly when (i) it is not discretely valued, in the sense that its norms accumulate at `1`,
(ii) `‖p‖ < 1`, and (iii) the `p`-th power map on `K° ⧸ p` is surjective. This is Scholze's
definition of a perfectoid field in *Perfectoid spaces*, Definition 3.1. Condition (i) cannot be
dropped: `ℚ_p` satisfies (ii) and (iii).

```lean
TauCeti.Perfectoid.isPerfectoidField_iff.{u_1} {p : ℕ} {K : Type u_1} [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] [Fact (Nat.Prime p)] :
  TauCeti.Perfectoid.IsPerfectoidField p K ↔
    (∀ (ε : ℝ), 1 < ε → ∃ x, 1 < ‖x‖ ∧ ‖x‖ < ε) ∧ ‖↑p‖ < 1 ∧ Function.Surjective fun x => x ^ p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Frobenius surjectivity criterion](../../part-02/other-results/part-01/the-frobenius-surjectivity-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Perfectoid.isPerfectoidField_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/Field.html#TauCeti.Perfectoid.isPerfectoidField_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Perfectoid.isPerfectoidField_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/Field.html#TauCeti.Perfectoid.isPerfectoidField_iff)
- [Source of `TauCeti.Perfectoid.isPerfectoidField_iff` in TauCeti/RingTheory/Perfectoid/Field.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/Field.lean#L200)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
