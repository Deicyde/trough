---
declaration: theorem
origin: cited
lean: LeftInvariantDerivation.exists_Ad_lie_eq_zero
statement: formalized
proof: formalized
---

# Hunt's lemma

For `X` and `Y` in the Lie algebra of a compact Lie group, some adjoint
translate of `X` brackets to zero with `Y`.

```lean
LeftInvariantDerivation.exists_Ad_lie_eq_zero.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {G : Type u_3}
  [TopologicalSpace G] [ChartedSpace H G] [Group G] [FiniteDimensional ℝ E] [LieGroup I (↑⊤) G]
  [T2Space G] [CompactSpace G] (X Y : LeftInvariantDerivation I G) :
  ∃ g, ⁅(TauCeti.Lie.Ad g) X, Y⁆ = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's identity in the algebra of smooth functions](../manifold/part-01/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma in coordinates](../manifold/part-01/hadamards-lemma-in-coordinates.md)

## Lean

Formalized in Tau Ceti as [`LeftInvariantDerivation.exists_Ad_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Adjoint/InvariantForm.html#LeftInvariantDerivation.exists_Ad_lie_eq_zero).

## Sources

- [Tau Ceti documentation: `LeftInvariantDerivation.exists_Ad_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Adjoint/InvariantForm.html#LeftInvariantDerivation.exists_Ad_lie_eq_zero)
- [Source of `LeftInvariantDerivation.exists_Ad_lie_eq_zero` in TauCeti/Geometry/Lie/Adjoint/InvariantForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Lie/Adjoint/InvariantForm.lean#L144)
