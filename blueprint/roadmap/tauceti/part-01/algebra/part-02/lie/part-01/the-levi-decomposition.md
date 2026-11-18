---
declaration: theorem
origin: cited
lean: TauCeti.exists_leviDecomposition
statement: formalized
proof: formalized
---

# The Levi decomposition

Over a field of characteristic zero, a finite-dimensional Lie
algebra is the semidirect sum of its solvable radical and a semisimple Lie subalgebra acting on
the radical by the adjoint action.

```lean
TauCeti.exists_leviDecomposition.{u, v} (K : Type u) [Field K] (L : Type v) [LieRing L]
  [LieAlgebra K L] [CharZero K] [FiniteDimensional K L] :
  ∃ S ψ, LieAlgebra.IsSemisimple K ↥S ∧ Nonempty (L ≃ₗ⁅K⁆ ↥(LieAlgebra.radical K L) ⋊⁅ψ⁆ ↥S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Levi's theorem](levis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_leviDecomposition`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.html#TauCeti.exists_leviDecomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_leviDecomposition`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.html#TauCeti.exists_leviDecomposition)
- [Source of `TauCeti.exists_leviDecomposition` in TauCeti/Algebra/Lie/LeviDecomposition/Solvable.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/LeviDecomposition/Solvable.lean#L146)
