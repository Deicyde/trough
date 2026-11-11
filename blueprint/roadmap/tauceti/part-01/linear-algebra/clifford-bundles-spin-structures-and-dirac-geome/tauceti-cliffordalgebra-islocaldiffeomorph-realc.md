---
declaration: theorem
origin: cited
lean: TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange
statement: formalized
proof: formalized
---

# TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange

The smooth compact real Spin projection is a local diffeomorphism on the native
units-range Lie-group carriers. This includes the native trivial group in dimension zero.

```lean
TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange (n : ℕ) :
  IsLocalDiffeomorph
    (modelWithCornersSelf ℝ
      ↥(TauCeti.Lie.lieSubalgebraOfSubgroup spinGroup.toUnits.range).toSubmodule)
    (modelWithCornersSelf ℝ
      ↥(TauCeti.Lie.lieSubalgebraOfSubgroup
            (QuadraticMap.specialOrthogonalToGeneralLinear
                (TauCeti.realCliffordForm n 0)).range).toSubmodule)
    ↑⊤ ⇑(TauCeti.CliffordAlgebra.realCliffordSpinToSpecialOrthogonalSmoothRange n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The closed-subgroup theorem, with its model space](../../geometry/part-02/lie/the-closed-subgroup-theorem-with-its-model-space.md)
- [Hadamard's identity in the algebra of smooth functions](../../geometry/part-02/manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../../geometry/part-02/manifold/part-02/hadamards-lemma.md)
- [The inverse function theorem for manifolds](../../geometry/part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/CliffordAlgebra/Spin/LocalDiffeomorph.html#TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange).

## Sources

- [Tau Ceti documentation: `TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/CliffordAlgebra/Spin/LocalDiffeomorph.html#TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange)
- [Source of `TauCeti.CliffordAlgebra.isLocalDiffeomorph_realCliffordSpinToSpecialOrthogonalSmoothRange` in TauCeti/Geometry/Lie/CliffordAlgebra/Spin/LocalDiffeomorph.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Lie/CliffordAlgebra/Spin/LocalDiffeomorph.lean#L113)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
