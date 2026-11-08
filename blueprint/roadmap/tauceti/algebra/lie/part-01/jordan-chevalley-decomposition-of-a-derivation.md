---
declaration: theorem
origin: cited
lean: LieDerivation.exists_isNilpotent_isSemisimple, LieDerivation.exists_isNilpotent_isSemisimple_of_iSup_maxGenEigenspace_eq_top
statement: formalized
proof: formalized
---

# Jordan–Chevalley decomposition of a derivation

Over an algebraically closed field, the
nilpotent and semisimple parts of a derivation of a finite-dimensional Lie algebra are
derivations. They are polynomials in the original derivation.

```lean
LieDerivation.exists_isNilpotent_isSemisimple.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [IsAlgClosed K] (D : LieDerivation K L L) :
  ∃ N S, ↑N ∈ K[↑D] ∧ ↑S ∈ K[↑D] ∧ IsNilpotent ↑N ∧ Module.End.IsSemisimple ↑S ∧ D = N + S
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LieDerivation.exists_isNilpotent_isSemisimple`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Derivation/JordanChevalley.html#LieDerivation.exists_isNilpotent_isSemisimple).

## Other forms

**Jordan–Chevalley decomposition of a split derivation.** Formalized in Tau Ceti as [`LieDerivation.exists_isNilpotent_isSemisimple_of_iSup_maxGenEigenspace_eq_top`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Derivation/JordanChevalley.html#LieDerivation.exists_isNilpotent_isSemisimple_of_iSup_maxGenEigenspace_eq_top).

```lean
LieDerivation.exists_isNilpotent_isSemisimple_of_iSup_maxGenEigenspace_eq_top.{u_1, u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  (D : LieDerivation K L L) (hD : ⨆ μ, Module.End.maxGenEigenspace (↑D) μ = ⊤) :
  ∃ N S, ↑N ∈ K[↑D] ∧ ↑S ∈ K[↑D] ∧ IsNilpotent ↑N ∧ Module.End.IsSemisimple ↑S ∧ D = N + S
```

## Sources

- [Tau Ceti documentation: `LieDerivation.exists_isNilpotent_isSemisimple`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Derivation/JordanChevalley.html#LieDerivation.exists_isNilpotent_isSemisimple)
- [Source of `LieDerivation.exists_isNilpotent_isSemisimple` in TauCeti/Algebra/Lie/Derivation/JordanChevalley.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Derivation/JordanChevalley.lean#L170)
