---
declaration: theorem
origin: cited
lean: MeasureTheory.exists_ne_zero_int_vec_mem_of_two_pow_le_volume
statement: formalized
proof: formalized
---

# Minkowski's convex body theorem for the integer lattice

A compact convex set
`s ⊆ η → ℝ`, symmetric about the origin, of volume at least `2 ^ |η|` contains a nonzero integer
vector.

```lean
MeasureTheory.exists_ne_zero_int_vec_mem_of_two_pow_le_volume.{u_1} {η : Type u_1} [Fintype η]
  [Nonempty η] {s : Set (η → ℝ)} (h_symm : ∀ x ∈ s, -x ∈ s) (h_conv : Convex ℝ s)
  (h_cpt : IsCompact s) (h : 2 ^ Fintype.card η ≤ MeasureTheory.volume s) :
  ∃ z, z ≠ 0 ∧ (fun k => ↑(z k)) ∈ s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.exists_ne_zero_int_vec_mem_of_two_pow_le_volume`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/GeometryOfNumbers.html#MeasureTheory.exists_ne_zero_int_vec_mem_of_two_pow_le_volume).

## Sources

- [Tau Ceti documentation: `MeasureTheory.exists_ne_zero_int_vec_mem_of_two_pow_le_volume`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/GeometryOfNumbers.html#MeasureTheory.exists_ne_zero_int_vec_mem_of_two_pow_le_volume)
- [Source of `MeasureTheory.exists_ne_zero_int_vec_mem_of_two_pow_le_volume` in TauCeti/MeasureTheory/Group/GeometryOfNumbers.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Group/GeometryOfNumbers.lean#L31)
