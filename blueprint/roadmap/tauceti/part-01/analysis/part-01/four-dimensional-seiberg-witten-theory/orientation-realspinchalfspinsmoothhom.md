---
declaration: def
origin: cited
lean: Orientation.realSpinCHalfSpinSmoothHom
statement: formalized
---

# Orientation.realSpinCHalfSpinSmoothHom

The smooth weight-one half-spin representation of compact Spinᶜ(4), after comparison
with the negative-metric Clifford model in the frame `b`.

```lean
Orientation.realSpinCHalfSpinSmoothHom.{u_1, u_2} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [Fact (Module.finrank ℝ V = 4)] {Q : QuadraticForm ℝ V}
  (o : Orientation ℝ V (Fin 4)) (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) (b : OrthonormalBasis (Fin 4) ℝ V)
  {W : Type u_2} [NormedAddCommGroup W] [NormedSpace ℂ W] [FiniteDimensional ℂ W]
  (ρ : CliffordAlgebra Q →ₐ[ℝ] Module.End ℂ W) (ε : ℂ) :
  ContMDiffMonoidMorphism
    ((modelWithCornersSelf ℝ ↥(TauCeti.CliffordAlgebra.realSpinLieModel 4)).prod
      (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 1))))
    (modelWithCornersSelf ℝ
      (↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace ε) →L[ℂ]
        ↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace ε)))
    (↑⊤) (CliffordAlgebra.spinCGroup (TauCeti.realCliffordForm 4 0) ⋯)
    (↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace ε) →L[ℂ]
      ↥((ρ (CliffordAlgebra.chirality Q o)).eigenspace ε))
```

## Depends on

- [The group `Spinᶜ(Q)`](the-group-spinc-q.md)

## Proof depends on

- [The closed-subgroup theorem, with its model space](../../../geometry/part-02/lie/the-closed-subgroup-theorem-with-its-model-space.md)
- [Hadamard's identity in the algebra of smooth functions](../../../geometry/part-02/manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../../../geometry/part-02/manifold/part-02/hadamards-lemma.md)

## Lean

Formalized in Tau Ceti as [`Orientation.realSpinCHalfSpinSmoothHom`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/CliffordAlgebra/SpinC/HalfSpin.html#Orientation.realSpinCHalfSpinSmoothHom).

## Sources

- [Tau Ceti documentation: `Orientation.realSpinCHalfSpinSmoothHom`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/CliffordAlgebra/SpinC/HalfSpin.html#Orientation.realSpinCHalfSpinSmoothHom)
- [Source of `Orientation.realSpinCHalfSpinSmoothHom` in TauCeti/Geometry/Lie/CliffordAlgebra/SpinC/HalfSpin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Lie/CliffordAlgebra/SpinC/HalfSpin.lean#L60)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
