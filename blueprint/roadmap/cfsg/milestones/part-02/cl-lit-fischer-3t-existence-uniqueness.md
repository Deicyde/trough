---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_fischer_3t_existence_uniqueness, CFSG.Milestones.cl_lit_fischer_3t_existence_uniqueness_full
statement: formalized
proof: formalized
---

# CL_LIT_Fischer_3T_existence_uniqueness

The milestone module `CFSG.Milestones.CL_LIT_Fischer_3T_existence_uniqueness`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_Fischer_3T_existence_uniqueness.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_3T_existence_uniqueness.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_fischer_3t_existence_uniqueness` (theorem, [line 15](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_3T_existence_uniqueness.lean#L15)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_fischer_3t_existence_uniqueness :
    ∀ k ∈ ({22, 23, 24} : Set ℕ),
      (∃ (G : Type) (_ : Group G) (_ : Finite G) (D : Set G),
        fischerEUIsCenterlessPair D ∧ fischerEUType k D ∧
        (∀ D' : Set G, fischerEUIsPair D' → D' = D) ∧
        ∀ d ∈ D, fischerEULocalStructure k d) ∧
      (∀ (G H : Type) [Group G] [Group H] [Finite G] [Finite H] (D : Set G) (E : Set H),
        fischerEUIsCenterlessPair D → fischerEUType k D →
        fischerEUIsCenterlessPair E → fischerEUType k E →
        ∃ φ : G ≃* H, φ '' D = E)
```

`CFSG.Milestones.cl_lit_fischer_3t_existence_uniqueness_full` (theorem, [line 34](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_3T_existence_uniqueness.lean#L34)). Proved here.

```lean
theorem cl_lit_fischer_3t_existence_uniqueness_full :
    ∀ k : Fin 3, Subgroup.center (Carrier k) = ⊥ ∧ IsSimpleGroup (commutator (Carrier k)) ∧
      ∃ D : Set (Carrier k), HasType k (Carrier k) D ∧
        (∀ E : Set (Carrier k), Pair (Carrier k) E → E = D) ∧ LocalStructure k D ∧
        ∀ (X : Type) [Group X] (E : Set X), Pair X E →
          Subgroup.center X = ⊥ → IsSimpleGroup (commutator X) → HasType k X E →
          ∃ iso : X ≃* Carrier k, iso '' E = D
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/CL_LIT_Fischer_3T_existence_uniqueness.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_3T_existence_uniqueness.lean)
