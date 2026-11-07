---
declaration: theorem
origin: cited
lean: TauCeti.LieAlgebra.exists_eq_smul_killingForm
statement: formalized
proof: formalized
---

# TauCeti.LieAlgebra.exists\_eq\_smul\_killingForm

**Every invariant bilinear form on a Lie algebra is a multiple of the Killing form**, for a
finite-dimensional Lie algebra over an algebraically closed field whose adjoint module is
irreducible and whose Killing form is nondegenerate, such as a simple Lie algebra in
characteristic zero.

```lean
TauCeti.LieAlgebra.exists_eq_smul_killingForm.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [IsAlgClosed K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieModule.IsIrreducible K L L] [LieAlgebra.IsKilling K L] {Φ : LinearMap.BilinForm K L}
  (hΦ : LinearMap.BilinForm.lieInvariant L Φ) : ∃ c, Φ = c • killingForm K L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LieAlgebra.exists_eq_smul_killingForm`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/InvariantForm.html#TauCeti.LieAlgebra.exists_eq_smul_killingForm).

## Sources

- [Tau Ceti documentation: `TauCeti.LieAlgebra.exists_eq_smul_killingForm`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/InvariantForm.html#TauCeti.LieAlgebra.exists_eq_smul_killingForm)
- [Source of `TauCeti.LieAlgebra.exists_eq_smul_killingForm` in TauCeti/Algebra/Lie/Killing/InvariantForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Killing/InvariantForm.lean#L55)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
