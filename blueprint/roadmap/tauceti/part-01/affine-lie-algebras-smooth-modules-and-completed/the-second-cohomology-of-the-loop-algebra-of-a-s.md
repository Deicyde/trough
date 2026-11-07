---
declaration: theorem
origin: cited
lean: TauCeti.LieAlgebra.LoopAlgebra.twoCocycle_eq_span_killingForm_sup_range_d₁₂
statement: formalized
proof: formalized
---

# The second cohomology of the loop algebra of a simple Lie algebra is spanned by the residue class of the Killing form

Here `L` is a finite-dimensional Lie algebra over an algebraically
closed field of characteristic zero whose adjoint module is irreducible and whose Killing form is
nondegenerate, for instance a simple Lie algebra. Together with
`smul_twoCochainOfBilinear_mem_range_d₁₂_iff`, this says that the second cohomology of
`loopAlgebra K ℤ L` with trivial coefficients is one-dimensional.

```lean
TauCeti.LieAlgebra.LoopAlgebra.twoCocycle_eq_span_killingForm_sup_range_d₁₂.{u_1, u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [CharZero K] [LieRing L] [LieAlgebra K L]
  [FiniteDimensional K L] [LieAlgebra.IsKilling K L] [IsAlgClosed K]
  [LieModule.IsIrreducible K L L] :
  LieModule.Cohomology.twoCocycle K (LieAlgebra.loopAlgebra K ℤ L)
      (TrivialLieModule K (LieAlgebra.loopAlgebra K ℤ L) K) =
    K ∙ LieAlgebra.LoopAlgebra.twoCochainOfBilinear K ℤ L (killingForm K L) ⋯ ⊔
      (LieModule.Cohomology.d₁₂ K (LieAlgebra.loopAlgebra K ℤ L)
          (TrivialLieModule K (LieAlgebra.loopAlgebra K ℤ L) K)).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.LieAlgebra.exists\_eq\_smul\_killingForm](tauceti-liealgebra-exists-eq-smul-killingform.md)
- [Whitehead's first lemma](whiteheads-first-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieAlgebra.LoopAlgebra.twoCocycle_eq_span_killingForm_sup_range_d₁₂`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Loop/Cocycle.html#TauCeti.LieAlgebra.LoopAlgebra.twoCocycle_eq_span_killingForm_sup_range_d%E2%82%81%E2%82%82).

## Sources

- [Tau Ceti documentation: `TauCeti.LieAlgebra.LoopAlgebra.twoCocycle_eq_span_killingForm_sup_range_d₁₂`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Loop/Cocycle.html#TauCeti.LieAlgebra.LoopAlgebra.twoCocycle_eq_span_killingForm_sup_range_d%E2%82%81%E2%82%82)
- [Source of `TauCeti.LieAlgebra.LoopAlgebra.twoCocycle_eq_span_killingForm_sup_range_d₁₂` in TauCeti/Algebra/Lie/Loop/Cocycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Loop/Cocycle.lean#L497)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
