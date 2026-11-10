---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_aschbacher_component_type_theorem_5
statement: formalized
proof: formalized
---

# CL_LIT_Aschbacher_component_type_theorem_5

The milestone module `CFSG.Milestones.CL_LIT_Aschbacher_component_type_theorem_5`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_Aschbacher_component_type_theorem_5.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_component_type_theorem_5.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_aschbacher_component_type_theorem_5` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_component_type_theorem_5.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_aschbacher_component_type_theorem_5
    (G : Type) [Group G] [Finite G]
    (D : Subgroup G) (r : ℕ) (hr : 1 ≤ r)
    (Abar : Fin r → Subgroup (D ⧸ aschbacherThm5OddCore D))
    (hdistinct : Function.Injective Abar)
    (hsemisimple : ∀ i, aschbacherThm5IsSemisimple (Abar i))
    (hcomm : ∀ i j, i ≠ j → ∀ x ∈ Abar i, ∀ y ∈ Abar j, x * y = y * x)
    (hgen : ⨆ i, Abar i = ⊤)
    (hperm : ∀ h ∈ Subgroup.normalizer (D : Set G), ∀ i, ∃ j,
      (aschbacherThm5Preimage D (Abar i)).map (MulAut.conj h).toMonoidHom =
        aschbacherThm5Preimage D (Abar j))
    (hi : ∀ (i j : Fin r) (t g : G), (∃ k : ℕ, t ^ (2 ^ k) = 1) → t ∉ Subgroup.center G →
      aschbacherThm5Centralizes (aschbacherThm5Core D) (aschbacherThm5Preimage D (Abar i)) t →
      aschbacherThm5Centralizes (aschbacherThm5Core D) (aschbacherThm5Preimage D (Abar j))
        (g⁻¹ * t * g) →
      g ∈ Subgroup.normalizer (D : Set G))
    (hii : ∀ (i : Fin r) (g : G) (X : Subgroup G),
      X ≤ (Subgroup.normalizer (D : Set G)).map (MulAut.conj g⁻¹).toMonoidHom →
      (∀ a ∈ aschbacherThm5Preimage D (Abar i), ∃ x ∈ X, ∃ o ∈ aschbacherThm5Core D,
        a = x * o) →
      g ∈ Subgroup.normalizer (D : Set G))
    (hH : Subgroup.normalizer (D : Set G) ≠ ⊤) :
    r = 1 ∨
      (r = 2 ∧ ∀ i j : Fin r, i ≠ j →
        (∀ d ∈ D, ∃ a ∈ aschbacherThm5Preimage D (Abar i),
          ∃ b ∈ aschbacherThm5Preimage D (Abar j), d = a * b) ∧
        pRank 2 (aschbacherThm5Preimage D (Abar i)) = 1 ∧
        ∀ a₁ ∈ aschbacherThm5Preimage D (Abar i), ∀ a₂ ∈ aschbacherThm5Preimage D (Abar j),
          orderOf a₁ = 2 → orderOf a₂ = 2 → a₁ * a₂ = a₂ * a₁ →
          aschbacherThm5Centralizes (aschbacherThm5Core D)
            (aschbacherThm5Preimage D (Abar i)) a₁ →
          aschbacherThm5Centralizes (aschbacherThm5Core D)
            (aschbacherThm5Preimage D (Abar j)) a₂ →
          a₁ = a₂ ∨ a₁ * a₂ ∈ Subgroup.center G)
```

The files of 3 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CLS_component_free_involution_odd_cores_trivial](../part-01/cls-component-free-involution-odd-cores-trivial.md)
- [CL_LIT_Walter_abelian_Sylow_two_simple](../part-03/cl-lit-walter-abelian-sylow-two-simple.md)
- [CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input](../part-03/ctgms-bender-1971-even-rank-one-model-and-strong.md)
- [LR_rank_two_isomorphism_types](../part-05/lr-rank-two-isomorphism-types.md)
- [LR_semidihedral_simple_recognition](../part-05/lr-semidihedral-simple-recognition.md)
- [QT_unique_Shult_simple_strongly_closed_TI_models](../part-06/qt-unique-shult-simple-strongly-closed-ti-models.md)

## Sources

- [CFSG/Milestones/CL_LIT_Aschbacher_component_type_theorem_5.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_component_type_theorem_5.lean)
