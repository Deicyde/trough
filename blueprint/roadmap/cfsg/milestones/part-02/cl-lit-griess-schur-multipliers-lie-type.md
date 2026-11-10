---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_griess_schur_multipliers_lie_type, CFSG.Milestones.cl_lit_griess_schur_multipliers_all_models, CFSG.Milestones.cl_lit_griess_schur_multipliers_all_models_statement, CFSG.Milestones.cl_lit_griess_schur_multipliers_central_covers, CFSG.Milestones.cl_lit_griess_schur_multipliers_all_native_models, CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers, CFSG.Milestones.cl_lit_griess_schur_multipliers_central_covers_z2, CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers_z2, CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers_unrestricted, CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers_z2_unrestricted, CFSG.Milestones.cl_lit_griess_schur_multipliers_g2_four_root_lifts
statement: formalized
proof: formalized
---

# CL_LIT_Griess_Schur_multipliers_Lie_type

The milestone module `CFSG.Milestones.CL_LIT_Griess_Schur_multipliers_Lie_type`, one of those CFSG/Milestones.lean imports.

It declares 11 results, quoted from [CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_griess_schur_multipliers_lie_type` (theorem, [line 22](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L22)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_griess_schur_multipliers_lie_type
    (p k n : ℕ) [Fact p.Prime] (hk : 0 < k) (hn : 2 ≤ n) (hsmall : n = 2 → 4 ≤ p ^ k) :
    commutator PSL(n, GaloisField p k) = ⊤ ∧
      Nonempty (griessHopfMultiplier PSL(n, GaloisField p k) ≃*
        Multiplicative (ZMod (Nat.gcd n (p ^ k - 1)) ×
          ZMod (griessPSLExceptional n (p ^ k)).1 × ZMod (griessPSLExceptional n (p ^ k)).2))
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_all_models` (theorem, [line 37](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L37)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_all_models
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (hmodel : Models.LieModel X t n p f) :
    commutator X = ⊤ ∧
      Nonempty (griessHopfMultiplier X ≃* generic t n p f × exceptional t n p f)
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_all_models_statement` (theorem, [line 45](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L45)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_all_models_statement :
    GriessAllModelsStatement
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_central_covers` (theorem, [line 49](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L49)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_central_covers
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (hmodel : Models.LieModel X t n p f) :
    ((∀ S : Sylow 2 (griessHopfMultiplier X), Nat.card S ≤ 2) →
      ∀ (L : Type) [Group L] [Finite L], IsQuasisimple L →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        ∀ S : Sylow 2 (Subgroup.center L), Nat.card S ≤ 2) ∧
    ((∀ S : Sylow 2 (griessHopfMultiplier X), Nat.card S = 2) →
      ∀ (L L' : Type) [Group L] [Group L'] [Finite L] [Finite L'],
        IsQuasisimple L → IsQuasisimple L' →
        Nat.card (Subgroup.center L) = 2 → Nat.card (Subgroup.center L') = 2 →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        Nonempty ((L' ⧸ Subgroup.center L') ≃* X) → Nonempty (L ≃* L'))
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_all_native_models` (theorem, [line 66](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L66)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_all_native_models
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (hmodel : Blueprint.LieModel X t n p f) :
    commutator X = ⊤ ∧
      Nonempty (griessHopfMultiplier X ≃* generic t n p f × exceptional t n p f)
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers` (theorem, [line 74](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L74)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_native_central_covers
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (_hmodel : Blueprint.LieModel X t n p f) :
    ((∀ S : Sylow 2 (griessHopfMultiplier X), Nat.card S ≤ 2) →
      ∀ (L : Type) [Group L] [Finite L], IsQuasisimple L →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        ∀ S : Sylow 2 (Subgroup.center L), Nat.card S ≤ 2) ∧
    ((∀ S : Sylow 2 (griessHopfMultiplier X), Nat.card S = 2) →
      ∀ (L L' : Type) [Group L] [Group L'] [Finite L] [Finite L'],
        IsQuasisimple L → IsQuasisimple L' →
        Nat.card (Subgroup.center L) = 2 → Nat.card (Subgroup.center L') = 2 →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        Nonempty ((L' ⧸ Subgroup.center L') ≃* X) → Nonempty (L ≃* L'))
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_central_covers_z2` (theorem, [line 91](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L91)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_central_covers_z2
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (hmodel : Models.LieModel X t n p f)
    (ht : t = .PSp ∧ n = 3 ∧ p = 2 ∧ f = 1 ∨ t = .G2 ∧ n = 0 ∧ p = 2 ∧ f = 2 ∨
      t = .F4 ∧ n = 0 ∧ p = 2 ∧ f = 1) :
    Nonempty (griessHopfMultiplier X ≃* Multiplicative (ZMod 2)) ∧
    (∀ (L : Type) [Group L] [Finite L], IsQuasisimple L →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        ∀ S : Sylow 2 (Subgroup.center L), Nat.card S ≤ 2) ∧
    (∀ (L L' : Type) [Group L] [Group L'] [Finite L] [Finite L'],
        IsQuasisimple L → IsQuasisimple L' →
        Nat.card (Subgroup.center L) = 2 → Nat.card (Subgroup.center L') = 2 →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        Nonempty ((L' ⧸ Subgroup.center L') ≃* X) → Nonempty (L ≃* L'))
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers_z2` (theorem, [line 107](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L107)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_native_central_covers_z2
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (hmodel : Blueprint.LieModel X t n p f)
    (ht : t = .PSp ∧ n = 3 ∧ p = 2 ∧ f = 1 ∨ t = .G2 ∧ n = 0 ∧ p = 2 ∧ f = 2 ∨
      t = .F4 ∧ n = 0 ∧ p = 2 ∧ f = 1) :
    Nonempty (griessHopfMultiplier X ≃* Multiplicative (ZMod 2)) ∧
    (∀ (L : Type) [Group L] [Finite L], IsQuasisimple L →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        ∀ S : Sylow 2 (Subgroup.center L), Nat.card S ≤ 2) ∧
    (∀ (L L' : Type) [Group L] [Group L'] [Finite L] [Finite L'],
        IsQuasisimple L → IsQuasisimple L' →
        Nat.card (Subgroup.center L) = 2 → Nat.card (Subgroup.center L') = 2 →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        Nonempty ((L' ⧸ Subgroup.center L') ≃* X) → Nonempty (L ≃* L'))
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers_unrestricted` (theorem, [line 123](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L123)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_native_central_covers_unrestricted
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (hmodel : Blueprint.LieModel X t n p f) :
    ((∀ S : Sylow 2 (griessHopfMultiplier X), Nat.card S ≤ 2) →
      ∀ (L : Type) [Group L], CFSG.IsQuasisimple L →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        ∀ S : Sylow 2 (Subgroup.center L), Nat.card S ≤ 2) ∧
    ((∀ S : Sylow 2 (griessHopfMultiplier X), Nat.card S = 2) →
      ∀ (L L' : Type) [Group L] [Group L'],
        CFSG.IsQuasisimple L → CFSG.IsQuasisimple L' →
        Nat.card (Subgroup.center L) = 2 → Nat.card (Subgroup.center L') = 2 →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        Nonempty ((L' ⧸ Subgroup.center L') ≃* X) → Nonempty (L ≃* L'))
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_native_central_covers_z2_unrestricted` (theorem, [line 139](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L139)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_native_central_covers_z2_unrestricted
    (X : Type) [Group X] (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (hmodel : Blueprint.LieModel X t n p f)
    (ht : t = .PSp ∧ n = 3 ∧ p = 2 ∧ f = 1 ∨ t = .G2 ∧ n = 0 ∧ p = 2 ∧ f = 2 ∨
      t = .F4 ∧ n = 0 ∧ p = 2 ∧ f = 1) :
    Nonempty (griessHopfMultiplier X ≃* Multiplicative (ZMod 2)) ∧
    (∀ (L : Type) [Group L], CFSG.IsQuasisimple L →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        ∀ S : Sylow 2 (Subgroup.center L), Nat.card S ≤ 2) ∧
    (∀ (L L' : Type) [Group L] [Group L'],
        CFSG.IsQuasisimple L → CFSG.IsQuasisimple L' →
        Nat.card (Subgroup.center L) = 2 → Nat.card (Subgroup.center L') = 2 →
        Nonempty ((L ⧸ Subgroup.center L) ≃* X) →
        Nonempty ((L' ⧸ Subgroup.center L') ≃* X) → Nonempty (L ≃* L'))
```

`CFSG.Milestones.cl_lit_griess_schur_multipliers_g2_four_root_lifts` (theorem, [line 171](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean#L171)). Proved here.

```lean
theorem cl_lit_griess_schur_multipliers_g2_four_root_lifts
    (L : Type) [Group L] (hL : IsQuasisimple L) (hZ : Nat.card (Subgroup.center L) = 2)
    (hmodel : Blueprint.LieModel (L ⧸ Subgroup.center L) .G2 0 2 2) :
    (∀ x : L, IsG2FourLongRootInvolution (x : L ⧸ Subgroup.center L) → orderOf x = 2) ∧
      (∀ x : L, IsG2FourShortRootInvolution (x : L ⧸ Subgroup.center L) → orderOf x = 4)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CL_LIT_SQTK_simple_listBase](../part-03/cl-lit-sqtk-simple-listbase.md)
- [CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition](../part-03/cl-lit-stroth-leon-sims-baby-monster-recognition.md)
- [LC_GL_local_rank_bounds](../part-05/lc-gl-local-rank-bounds.md)

## Sources

- [CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Griess_Schur_multipliers_Lie_type.lean)
