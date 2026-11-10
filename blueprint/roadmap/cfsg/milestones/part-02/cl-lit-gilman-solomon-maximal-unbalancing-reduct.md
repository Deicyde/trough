---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction, CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction_native, CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction_models
statement: formalized
proof: formalized
---

# CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction

The milestone module `CFSG.Milestones.CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction`, one of those CFSG/Milestones.lean imports.

It declares 3 results, quoted from [CFSG/Milestones/CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction` (theorem, [line 2449](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction.lean#L2449)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction
    (X : Type) [Group X] [Finite X] [IsSimpleGroup X]
    (hnonab : ∃ a b : X, a * b ≠ b * a)
    (hK : IsKProper X)
    (hunbal : ∃ z : X, orderOf z = 2 ∧
      fusionOddCore (Subgroup.centralizer ({z} : Set X)) ≠ ⊥)
    (hnotLie : ∀ p : ℕ, p.Prime → p ≠ 2 → Nat.card X ∉ lieOrdersChar p)
    (hnotAlt : ∀ n : ℕ, 7 ≤ n → n % 4 = 3 → IsEmpty (X ≃* alternatingGroup (Fin n)))
    (htriple : ∃ (a b : X) (J : Subgroup X), fusionUnbalancingTriple a b J) :
    ∃ (x y : X) (L : Subgroup X),
      fusionMaximalUnbalancingTriple x y L ∧ fusionMaximalComponent L ∧
      ((Nonempty (L ⧸ fusionOddCore L ≃* alternatingGroup (Fin 7)) ∨
          ∃ (p f : ℕ) (_ : Fact p.Prime), p ≠ 2 ∧ 1 ≤ f ∧ 5 ≤ p ^ f ∧
            Nonempty (L ⧸ fusionOddCore L ≃* PSL(2, GaloisField p f))) ∨
        (Nonempty (L ⧸ fusionOddCore L ≃* fusionHe) ∨
          Nonempty (L ⧸ fusionZStar L ≃* PSL(3, GaloisField 2 2))))
```

`CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction_native` (theorem, [line 2494](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction.lean#L2494)). Proved here.

```lean
theorem cl_lit_gilman_solomon_maximal_unbalancing_reduction_native
    (X : Type) [Group X] [Finite X] [IsSimpleGroup X]
    (hnonab : ∃ a b : X, a * b ≠ b * a)
    (hK : Assembly.KProper Blueprint.Catalog X)
    (hunbal : ∃ z : X, orderOf z = 2 ∧
      oddCore (Subgroup.centralizer ({z} : Set X)) ≠ ⊥)
    (hnotOutcome : ¬ OutcomeLocal.UOutcome X)
    (htriple : ∃ (a b : X) (J : Subgroup X), GSUnbalancingTriple a b J) :
    ∃ (x y : X) (L : Subgroup X), GSMaximalUnbalancingTriple x y L ∧
      GSMaximalComponent L ∧
      ((Nonempty (L ⧸ pPrimeCore 2 L ≃* alternatingGroup (Fin 7)) ∨
        ∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ 5 ≤ p ^ f ∧
          Blueprint.LieModel (L ⧸ pPrimeCore 2 L) .PSL 2 p f) ∨
       (Nonempty (L ⧸ pPrimeCore 2 L ≃* Blueprint.NativeSporadic.He) ∨
         Blueprint.LieModel (L ⧸ Open.fusionZStar L) .PSL 3 2 2))
```

`CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction_models` (theorem, [line 2531](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction.lean#L2531)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_gilman_solomon_maximal_unbalancing_reduction_models
    (X : Type) [Group X] [Finite X] [IsSimpleGroup X]
    (hnonab : ∃ a b : X, a * b ≠ b * a)
    (hK : IsKProper X)
    (hunbal : ∃ z : X, orderOf z = 2 ∧
      fusionOddCore (Subgroup.centralizer ({z} : Set X)) ≠ ⊥)
    (hnotOutcome : ¬ (Models.OddLieType X ∨
      ∃ n : ℕ, 7 ≤ n ∧ n % 4 = 3 ∧ Nonempty (X ≃* alternatingGroup (Fin n))))
    (htriple : ∃ (a b : X) (J : Subgroup X), fusionUnbalancingTriple a b J) :
    ∃ (x y : X) (L : Subgroup X), fusionMaximalUnbalancingTriple x y L ∧
      fusionMaximalComponent L ∧
      ((Nonempty (L ⧸ fusionOddCore L ≃* alternatingGroup (Fin 7)) ∨
        ∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ 5 ≤ p ^ f ∧
          Models.LieModel (L ⧸ fusionOddCore L) .PSL 2 p f) ∨
       (Blueprint.NativeSporadic.IsSporadic (L ⧸ fusionOddCore L) .He ∨
         Models.LieModel (L ⧸ fusionZStar L) .PSL 3 2 2))
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CL_LIT_Curtis_Tits_presentation_theorem](cl-lit-curtis-tits-presentation-theorem.md)
- [CL_LIT_Fischer_three_transposition_theorem](cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_GMS_Monster_uniqueness](cl-lit-gms-monster-uniqueness.md)
- [CL_LIT_Monster_existence_Griess_Conway](cl-lit-monster-existence-griess-conway.md)
- [CL_LIT_classical_involution_theorem](../part-03/cl-lit-classical-involution-theorem.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gilman_Solomon_maximal_unbalancing_reduction.lean)
