---
declaration: theorem
origin: cited
lean: LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul, IsSelfAdjoint.existsUnique_isUnitary_complexGenerator_eq_I_smul, IsSelfAdjoint.exists_isUnitary_complexGenerator_eq_I_smul
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

## Proof depends on

- [Lumer--Phillips in duality-map form](../../part-04/semigroups/lumer-phillips-in-duality-map-form.md)

## Lean

Formalized in Tau Ceti as [`LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.html#LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul).

## Other forms

**Stone's theorem, converse direction.** Formalized in Tau Ceti as [`IsSelfAdjoint.existsUnique_isUnitary_complexGenerator_eq_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.html#IsSelfAdjoint.existsUnique_isUnitary_complexGenerator_eq_I_smul).

```lean
IsSelfAdjoint.existsUnique_isUnitary_complexGenerator_eq_I_smul.{u_1} {H : Type u_1}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] {A : H →ₗ.[ℂ] H}
  (hA : IsSelfAdjoint A) : ∃! U, ∃ (hU : U.IsUnitary), U.complexGenerator hU = Complex.I • A
```

**Stone's theorem, converse direction (existence).** Formalized in Tau Ceti as [`IsSelfAdjoint.exists_isUnitary_complexGenerator_eq_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.html#IsSelfAdjoint.exists_isUnitary_complexGenerator_eq_I_smul).

```lean
IsSelfAdjoint.exists_isUnitary_complexGenerator_eq_I_smul.{u_1} {H : Type u_1}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] {A : H →ₗ.[ℂ] H}
  (hA : IsSelfAdjoint A) : ∃ U, ∃ (hU : U.IsUnitary), U.complexGenerator hU = Complex.I • A
```

## Sources

- [Tau Ceti documentation: `LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.html#LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul)
- [Source of `LinearPMap.isSelfAdjoint_iff_exists_isUnitary_complexGenerator_eq_I_smul` in TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Semigroups/Group/Stone/Unbounded.lean#L113)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OneParameterSemigroups/STATUS.md)
