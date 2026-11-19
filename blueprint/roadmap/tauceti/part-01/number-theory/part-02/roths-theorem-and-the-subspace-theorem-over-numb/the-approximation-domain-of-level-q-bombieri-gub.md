---
declaration: def
origin: cited
lean: TauCeti.NumberField.approxDomain
statement: formalized
---

# The approximation domain of level `Q` (Bombieri–Gubler 7.5.6)

the points `x` of `Kⁱ`
with `v (L v i x) ≤ Q ^ c v i` at every infinite place and every place of `S₀`, and with
`v (x j) ≤ 1` at every finite place outside `S₀`.

```lean
TauCeti.NumberField.approxDomain.{u_1, u_2} {K : Type u_1} [Field K] {ι : Type u_2} [NumberField K]
  (S₀ : Finset (NumberField.FinitePlace K)) (L : AbsoluteValue K ℝ → ι → Module.Dual K (ι → K))
  (c : AbsoluteValue K ℝ → ι → ℝ) (Q : ℝ) : Set (ι → K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.approxDomain`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproximationDomain.html#TauCeti.NumberField.approxDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.approxDomain`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproximationDomain.html#TauCeti.NumberField.approxDomain)
- [Source of `TauCeti.NumberField.approxDomain` in TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproximationDomain.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproximationDomain.lean#L92)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
