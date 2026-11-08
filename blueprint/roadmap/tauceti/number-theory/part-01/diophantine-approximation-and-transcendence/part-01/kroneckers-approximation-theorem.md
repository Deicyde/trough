---
declaration: theorem
origin: cited
lean: TauCeti.kronecker_approximation, TauCeti.kronecker_approximation_nat
statement: formalized
proof: formalized
---

# Kronecker's approximation theorem

If `1` and the real numbers `αᵢ` satisfy no
nontrivial integer relation, that is, if they are linearly independent over `ℚ`, then for every
`θ ∈ ℝ^ι` and `ε > 0` there are infinitely many integer pairs `(x, y)`, `x ∈ ℤ^ι`, `y ∈ ℤ`, with
`|y αᵢ - xᵢ - θᵢ| ≤ ε` for every `i`.

```lean
TauCeti.kronecker_approximation.{u_1} {ι : Type u_1} [Fintype ι] {α : ι → ℝ}
  (hα : ∀ (x : ℤ × (ι → ℤ)), ↑x.1 + ∑ i, ↑(x.2 i) * α i = 0 → x = 0) (θ : ι → ℝ) {ε : ℝ}
  (hε : 0 < ε) : {p | ∀ (i : ι), |α i * ↑p.2 - ↑(p.1 i) - θ i| ≤ ε}.Infinite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kronecker's theorem for projective tuples](../../heights-units-and-s-units-of-number-fields/part-01/kroneckers-theorem-for-projective-tuples.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.kronecker_approximation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.html#TauCeti.kronecker_approximation).

## Other forms

**Kronecker's approximation theorem with positive multipliers.** Formalized in Tau Ceti as [`TauCeti.kronecker_approximation_nat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.html#TauCeti.kronecker_approximation_nat).

```lean
TauCeti.kronecker_approximation_nat.{u_1} {ι : Type u_1} [Fintype ι] {α : ι → ℝ}
  (hα : ∀ (x : ℤ × (ι → ℤ)), ↑x.1 + ∑ i, ↑(x.2 i) * α i = 0 → x = 0) (θ : ι → ℝ) {ε : ℝ}
  (hε : 0 < ε) : {n | ∃ x, ∀ (i : ι), |α i * ↑n - ↑(x i) - θ i| ≤ ε}.Infinite
```

## Sources

- [Tau Ceti documentation: `TauCeti.kronecker_approximation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.html#TauCeti.kronecker_approximation)
- [Source of `TauCeti.kronecker_approximation` in TauCeti/NumberTheory/DiophantineApproximation/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.lean#L91)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
