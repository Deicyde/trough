---
declaration: section
origin: cited
lean: OAI.PolycyclicRecognition.group_recognition, OAI.PolycyclicRecognition.main_uniform_bounded_height, OAI.PolycyclicRecognition.lattice_recognition
statement: formalized
proof: formalized
---

# 255. Quasi-isometric recognition of virtually polycyclic groups

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every finitely generated group quasi-isometric to a finitely generated virtually polycyclic group is virtually polycyclic, resolving the Eskin–Fisher–Whyte lattice-recognition conjecture. Equivalently, a group quasi-isometric to a lattice in a connected simply connected solvable Lie group is virtually a uniform lattice in some such Lie group, possibly a different one.

## Quasi-isometric recognition of virtually polycyclic groups

We prove that every finitely generated group quasi-isometric to a finitely generated virtually polycyclic group is virtually polycyclic. This resolves the lattice-recognition conjecture of Eskin, Fisher and Whyte, which allows the ambient solvable Lie group in the conclusion to differ from the one in the hypothesis.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/quasi-isometric-recognition-of-virtually-polycyclic-groups-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves quasi-isometric recognition of virtually polycyclic groups: every finitely generated group quasi-isometric to a finitely generated virtually polycyclic group is itself virtually polycyclic. It also realizes a finite-index subgroup of the recognized group as a uniform lattice in a simply connected solvable Lie group, which may differ from the original ambient group.

The linked structural estimate controls the height-coordinate behavior of self quasi-isometries of the stated unimodular solvable Lie models, up to bounded error and one of finitely many linear height symmetries.

## Lean: Quasi-isometric recognition of virtually polycyclic groups and solvable lattices

```lean
theorem group_recognition
    {P J : Type} [Group P] [Group J] [Group.FG P] [Group.FG J]
    (e : GroupCoarseEquivalence P J) (hP : IsVirtuallyPolycyclic P) :
    IsVirtuallyPolycyclic J ∧
      ∃ Γ : Subgroup J, Γ.FiniteIndex ∧
        ∃ (S : SimplyConnectedSolvableLieModel) (Λ : Subgroup S.carrier),
          IsUniformLattice Λ ∧ Nonempty (Γ ≃* Λ)
```

Stated in [PolycyclicRecognition.lean, line 209](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PolycyclicRecognition.lean#L209). Proved in [lean/OAI/GroupTheory/PolycyclicRecognition/Recognition.lean, line 24](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/PolycyclicRecognition/Recognition.lean#L24).

```lean
theorem main_uniform_bounded_height
    (R : SimplyConnectedSolvableLieModel) (d : ProperChainMetric R.carrier)
    {a : ℕ} (T : TriangularAdjoint (GroupLieAlgebra (𝓘(ℝ, R.modelSpace)) R.carrier) a)
    (huni : ModelIsUnimodular R)
    {W : Type} [NormedAddCommGroup W] [NormedSpace ℝ W] [FiniteDimensional ℝ W]
    (q : HeightSpace T.character ≃ₗ[ℝ] W)
    (Exp : GroupLieAlgebra (𝓘(ℝ, R.modelSpace)) R.carrier → R.carrier)
    (hExp : IsGroupExponential Exp) (π : R.carrier →* Multiplicative W)
    (hπExp : ∀ x, (π (Exp x)).toAdd = q (heightProjection T.character x)) :
    letI := d.compatibleMetric
    ∃ A : Subgroup (W ≃ₗ[ℝ] W), Set.Finite (A : Set (W ≃ₗ[ℝ] W)) ∧
      ∀ K C : ℝ, 1 ≤ K → 0 ≤ C → ∃ B : ℝ, 0 ≤ B ∧
        ∀ F : SelfQuasiIsometry R.carrier K C, ∃ AF : A, ∀ g,
          ‖(π (F.toFun g)).toAdd - ((π (F.toFun 1)).toAdd + AF.val (π g).toAdd)‖ ≤ B
```

Stated in [PolycyclicRecognition.lean, line 219](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PolycyclicRecognition.lean#L219). Proved in [lean/OAI/GroupTheory/PolycyclicRecognition/Recognition.lean, line 80](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/PolycyclicRecognition/Recognition.lean#L80).

```lean
theorem lattice_recognition
    (S : SimplyConnectedSolvableLieModel) (Λ : Subgroup S.carrier)
    (hΛ : IsFiniteCovolumeLattice Λ)
    {J : Type} [Group J] [Group.FG J] (e : GroupCoarseEquivalence Λ J) :
    ∃ Γ : Subgroup J, Γ.FiniteIndex ∧
      ∃ (R : SimplyConnectedSolvableLieModel) (Δ : Subgroup R.carrier),
        IsUniformLattice Δ ∧ Nonempty (Γ ≃* Δ)
```

Stated in [PolycyclicRecognition.lean, line 236](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PolycyclicRecognition.lean#L236). Proved in [lean/OAI/GroupTheory/PolycyclicRecognition/Recognition.lean, line 63](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/PolycyclicRecognition/Recognition.lean#L63).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/255.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/255.md)
