---
declaration: theorem
origin: cited
lean: Matrix.exists_ne_zero_int_abs_sum_mul_le
statement: formalized
proof: formalized
---

# Minkowski's linear forms theorem

Let `A` be an invertible real square matrix indexed by
a nonempty finite type `ι`, and let `a i ≥ 0` be bounds whose product is at least `|det A|`. Then
some nonzero integer vector `z` satisfies `|∑ j, A i j * z j| ≤ a i` for every `i`.

```lean
Matrix.exists_ne_zero_int_abs_sum_mul_le.{u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  [Nonempty ι] (A : Matrix ι ι ℝ) (hA : A.det ≠ 0) {a : ι → ℝ} (ha : 0 ≤ a)
  (h : |A.det| ≤ ∏ i, a i) : ∃ z, z ≠ 0 ∧ ∀ (i : ι), |∑ j, A i j * ↑(z j)| ≤ a i
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Minkowski's convex body theorem for the integer lattice](../../../measure-theory/group/minkowskis-convex-body-theorem-for-the-integer-l.md)

## Lean

Formalized in Tau Ceti as [`Matrix.exists_ne_zero_int_abs_sum_mul_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/LinearForms.html#Matrix.exists_ne_zero_int_abs_sum_mul_le).

## Sources

- [Tau Ceti documentation: `Matrix.exists_ne_zero_int_abs_sum_mul_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/LinearForms.html#Matrix.exists_ne_zero_int_abs_sum_mul_le)
- [Source of `Matrix.exists_ne_zero_int_abs_sum_mul_le` in TauCeti/NumberTheory/GeometryOfNumbers/LinearForms.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/GeometryOfNumbers/LinearForms.lean#L47)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
