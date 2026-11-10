---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_signalizer_functor_theorem_1, CFSG.Milestones.cl_lit_signalizer_functor_theorem_2
statement: formalized
proof: formalized
---

# CL_LIT_signalizer_functor_theorem

The milestone module `CFSG.Milestones.CL_LIT_signalizer_functor_theorem`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_signalizer_functor_theorem.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_signalizer_functor_theorem.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_signalizer_functor_theorem_1` (theorem, [line 18](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_signalizer_functor_theorem.lean#L18)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_signalizer_functor_theorem_1
    (G : Type) [Group G] [Finite G]
    (p : ℕ) (hp : p.Prime) (k : ℕ) (hk : 1 ≤ k)
    (A : Subgroup G) (hA : IsElemAbelian p A) (hrank : p ^ (k + 2) ≤ Nat.card A)
    (Θ : Subgroup G → Subgroup G)
    (hcent : ∀ S ∈ signalizerFunctorEk p k A, Θ S ≤ Subgroup.centralizer (S : Set G))
    (hcop : ∀ S ∈ signalizerFunctorEk p k A, Nat.Coprime p (Nat.card (Θ S)))
    (hinv : ∀ S ∈ signalizerFunctorEk p k A, A ≤ Subgroup.normalizer (Θ S : Set G))
    (hbal : ∀ S ∈ signalizerFunctorEk p k A, ∀ S' ∈ signalizerFunctorEk p k A,
      Θ S ⊓ Subgroup.centralizer (S' : Set G) ≤ Θ S')
    (hK : ∀ S ∈ signalizerFunctorEk p k A, CFSG.SectionRank.IsKGroupCat ↥(Θ S)) :
    let W : Subgroup G := ⨆ (S : Subgroup G) (_ : S ∈ signalizerFunctorEk p k A), Θ S
    (Nat.Coprime p (Nat.card W) ∧ A ≤ Subgroup.normalizer (W : Set G)) ∧
    (∀ S ∈ signalizerFunctorEk p k A, W ⊓ Subgroup.centralizer (S : Set G) = Θ S) ∧
    (∀ Y : Subgroup G, A ≤ Subgroup.normalizer (Y : Set G) →
      (∀ S ∈ signalizerFunctorEk p k A, Y ⊓ Subgroup.centralizer (S : Set G) ≤ Θ S) →
      Y ≤ W) ∧
    ((∀ S ∈ signalizerFunctorEk p k A, Group.IsSolvable (Θ S)) → Group.IsSolvable W)
```

`CFSG.Milestones.cl_lit_signalizer_functor_theorem_2` (theorem, [line 46](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_signalizer_functor_theorem.lean#L46)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_signalizer_functor_theorem_2
    (G : Type) [Group G] [Finite G]
    (p : ℕ) (hp : p.Prime)
    (A : Subgroup G) (hA : IsMulCommutative A) (hexp : ∀ a ∈ A, a ^ p = 1)
    (hrank : p ^ 3 ∣ Nat.card A)
    (θ : G → Subgroup G) (hθ : IsSolvableSignalizerFunctor p A θ) :
    let W : Subgroup G := ⨆ (a : G) (_ : a ∈ A) (_ : a ≠ 1), θ a
    Nat.Coprime p (Nat.card W) ∧ Group.IsSolvable W ∧
      ∀ a ∈ A, a ≠ 1 → θ a = W ⊓ Subgroup.centralizer {a}
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CLS_component_free_centralizer_quotient_characteristic_two](../part-01/cls-component-free-centralizer-quotient-characte.md)
- [CLS_connectivity_MacWilliams_four_generator](../part-01/cls-connectivity-macwilliams-four-generator.md)
- [CL_LIT_SQTK_simple_list](../part-02/cl-lit-sqtk-simple-list.md)
- [CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input](ctgms-bender-1971-even-rank-one-model-and-strong.md)
- [LC_GL_local_rank_bounds](../part-05/lc-gl-local-rank-bounds.md)
- [LR_Glauberman_Z_star_central_Sylow_involution](../part-05/lr-glauberman-z-star-central-sylow-involution.md)
- [OO_odd_order_solvable](../part-05/oo-odd-order-solvable.md)

## Sources

- [CFSG/Milestones/CL_LIT_signalizer_functor_theorem.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_signalizer_functor_theorem.lean)
