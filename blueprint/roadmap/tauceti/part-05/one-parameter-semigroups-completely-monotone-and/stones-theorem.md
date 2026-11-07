---
declaration: theorem
origin: cited
lean: LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul
statement: formalized
proof: formalized
---

# Stone's theorem

An operator `A` on a complex Hilbert space is self-adjoint if and only if
`i • A` is the complex generator of a unitary C₀-group.

```lean
LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul.{u_1} {H : Type u_1}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] (A : H →ₗ.[ℂ] H) :
  IsSelfAdjoint A ↔ ∃ U, ∃ (hU : U.IsUnitary), U.complexGenerator hU = Complex.I • A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.html#LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul).

## Sources

- [Tau Ceti documentation: `LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.html#LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul)
- [Source of `LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul` in TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.lean#L113)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
