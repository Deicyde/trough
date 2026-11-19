---
declaration: def
origin: cited
lean: TauCeti.CurrentAlgebra.invariantFormsResidueClassEquiv
statement: formalized
---

# Invariant forms classify the continuous second cohomology of formal loops

For a
finite-dimensional Lie algebra with nondegenerate Killing form over a field of characteristic
zero, for instance a semisimple Lie algebra, `Φ ↦ [c_Φ]` is a linear equivalence from the
invariant symmetric forms on `L` onto the continuous second cohomology of formal currents with
trivial coefficients.

```lean
TauCeti.CurrentAlgebra.invariantFormsResidueClassEquiv.{u_1, u_2} (K : Type u_1) (L : Type u_2)
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] :
  ↥(TauCeti.LieModule.invariantForms K L L) ≃ₗ[K]
    TauCeti.LieModule.Cohomology.continuousSecondCohomology K (TauCeti.currentAlgebra K L)
      (TrivialLieModule K (TauCeti.currentAlgebra K L) K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Whitehead's first lemma](../../part-02/lie/part-02/whiteheads-first-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.invariantFormsResidueClassEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/InvariantForms.html#TauCeti.CurrentAlgebra.invariantFormsResidueClassEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.invariantFormsResidueClassEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/InvariantForms.html#TauCeti.CurrentAlgebra.invariantFormsResidueClassEquiv)
- [Source of `TauCeti.CurrentAlgebra.invariantFormsResidueClassEquiv` in TauCeti/Algebra/Lie/Current/InvariantForms.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Current/InvariantForms.lean#L130)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
