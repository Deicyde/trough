---
declaration: theorem
origin: cited
lean: ZLattice.exists_basis_span_image_eq_flag
statement: formalized
proof: formalized
---

# Lattice basis with a prescribed flag

Let `e` be an `ℝ`-basis of `E` consisting of vectors
of a discrete subgroup `L`. Then `L` has a `ℤ`-basis `b` with the same real flag as `e`: for every
`k`, the vectors `b 0, …, b (k - 1)` span over `ℝ` the subspace `e.flag k` spanned by
`e 0, …, e (k - 1)`. The vectors `b j` and `e j` differ in general, since the `e j` need not span
`L` over `ℤ`.

```lean
ZLattice.exists_basis_span_image_eq_flag.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L] {n : ℕ} (e : Module.Basis (Fin n) ℝ E)
  (he : ∀ (i : Fin n), e i ∈ L) :
  ∃ b, ∀ (k : Fin (n + 1)), Submodule.span ℝ ((fun j => ↑(b j)) '' {j | j.castSucc < k}) = e.flag k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.exists_basis_span_image_eq_flag`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/AdaptedBasis.html#ZLattice.exists_basis_span_image_eq_flag).

## Sources

- [Tau Ceti documentation: `ZLattice.exists_basis_span_image_eq_flag`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/AdaptedBasis.html#ZLattice.exists_basis_span_image_eq_flag)
- [Source of `ZLattice.exists_basis_span_image_eq_flag` in TauCeti/Algebra/Module/ZLattice/AdaptedBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Module/ZLattice/AdaptedBasis.lean#L185)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
