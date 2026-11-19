---
declaration: def
origin: cited
lean: TauCeti.HomologicalOrientation.cupInsertionForm
statement: formalized
---

# The insertion form

**The insertion form** of a class `β` of degree `q` along a compact oriented `n`-manifold
`f : N → X`, for `q + r = n`: the alternating `ℤ`-multilinear form
`(a₁, …, a_r) ↦ ⟨a₁ ⌣ ⋯ ⌣ a_r ⌣ β, f_*[N]⟩` on `H¹(X; ℤ)`.

```lean
TauCeti.HomologicalOrientation.cupInsertionForm {N E : Type} [TopologicalSpace N] [T2Space N]
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [ChartedSpace E N]
  [CompactSpace N] {n : ℕ} (o : TauCeti.HomologicalOrientation N E n) (hn : Module.finrank ℝ E = n)
  {X : Type} [TopologicalSpace X] (f : C(N, X)) {q : ℕ} (β : ↑((↧X).integralCohomology q)) (r : ℕ)
  (h : r + q = n) : ↑((↧X).integralCohomology 1) [⋀^Fin r]→ₗ[ℤ] ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.cupInsertionForm`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/InsertionForm.html#TauCeti.HomologicalOrientation.cupInsertionForm).

## Sources

- [Tau Ceti documentation: `TauCeti.HomologicalOrientation.cupInsertionForm`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/InsertionForm.html#TauCeti.HomologicalOrientation.cupInsertionForm)
- [Source of `TauCeti.HomologicalOrientation.cupInsertionForm` in TauCeti/AlgebraicTopology/Cohomology/InsertionForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/InsertionForm.lean#L87)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
