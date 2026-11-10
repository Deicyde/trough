---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_timmesfeld_1978_large_extraspecial, CFSG.Milestones.cl_lit_timmesfeld_1978_large_extraspecial_models
statement: formalized
proof: formalized
---

# CL_LIT_Timmesfeld_1978_large_extraspecial

The milestone module `CFSG.Milestones.CL_LIT_Timmesfeld_1978_large_extraspecial`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_Timmesfeld_1978_large_extraspecial.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_1978_large_extraspecial.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_timmesfeld_1978_large_extraspecial` (theorem, [line 498](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_1978_large_extraspecial.lean#L498)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_timmesfeld_1978_large_extraspecial
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (z : G) (hz : orderOf z = 2)
    (hext : timmesfeldIsExtraspecial (timmesfeldFStar (Subgroup.centralizer ({z} : Set G))))
    (w : ℕ)
    (hw : Nat.card (timmesfeldFStar (Subgroup.centralizer ({z} : Set G))) = 2 ^ (1 + 2 * w))
    (Mbar : Type) [Group Mbar]
    (hMbar : timmesfeldQuotientIso (timmesfeldFStar (Subgroup.centralizer ({z} : Set G))) Mbar) :
    w ≤ 4 ∨
    (Nonempty (G ≃* PSL(w + 2, ZMod 2)) ∨ Nonempty (G ≃* timmesfeldPSU (w + 2))) ∨
    (6 ≤ w ∧ Even w ∧
      ∃ q : QuadraticForm (ZMod 2) (Fin w → ZMod 2), timmesfeldNondegenerate q ∧
        (Nonempty (Mbar ≃* Equiv.Perm (Fin 3) × timmesfeldOmega q) ∨
          Nonempty (Mbar ≃* Equiv.Perm (Fin 3) × timmesfeldIsometries q))) ∨
    (w = 6 ∧ IsQuasisimple (timmesfeldLayer Mbar) ∧ Nat.card (timmesfeldOddCore Mbar) ≤ 3 ∧
      ∃ t : Mbar, orderOf t = 2 ∧
        ∃ R : Subgroup Mbar, R ≤ Subgroup.centralizer ({t} : Set Mbar) ∧
          (R.subgroupOf (Subgroup.centralizer ({t} : Set Mbar))).Normal ∧
          (frattini (pCoreOf 2 R)).map (pCoreOf 2 R).subtype ≤ Subgroup.zpowers t ∧
          (timmesfeldQuotientIso (pCore 2 R) PSL(3, ZMod 2) ∨
            (∃ q : QuadraticForm (ZMod 2) (Fin 4 → ZMod 2), timmesfeldNondegenerate q ∧
              timmesfeldPlusType q ∧ timmesfeldQuotientIso (pCore 2 R) (timmesfeldOmega q)) ∨
            (pCoreOf 2 R = Subgroup.zpowers t ∧
              ∃ q : QuadraticForm (ZMod 2) (Fin 6 → ZMod 2), timmesfeldNondegenerate q ∧
                timmesfeldQuotientIso (pCore 2 R) (timmesfeldOmega q)))) ∨
    (w = 10 ∧ (timmesfeldFStar Mbar).index ≤ 2 ∧
      (Nonempty (timmesfeldFStar Mbar ≃* PSL(6, ZMod 2)) ∨
        Nonempty (timmesfeldFStar Mbar ≃* timmesfeldPSU 6))) ∨
    (w = 11 ∧ IsSimpleGroup Mbar ∧ Nat.card Mbar = timmesfeldOrderCo2) ∨
    (w = 12 ∧ IsSimpleGroup Mbar ∧ Nat.card Mbar = timmesfeldOrderCo1) ∨
    (IsSimpleGroup Mbar ∧ ∃ t : Mbar, orderOf t = 2 ∧
      timmesfeldIsExtraspecial (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar))) ∧
      ((w = 16 ∧ Nat.card (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar))) = 2 ^ 17 ∧
          timmesfeldQuotientIso (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar)))
            (Equiv.Perm (Fin 3) × timmesfeldOmegaPlus 4)) ∨
        (w = 28 ∧ Nat.card (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar))) = 2 ^ 33 ∧
          timmesfeldQuotientIso (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar)))
            (timmesfeldOmegaPlus 6))))
```

`CFSG.Milestones.cl_lit_timmesfeld_1978_large_extraspecial_models` (theorem, [line 548](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_1978_large_extraspecial.lean#L548)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_timmesfeld_1978_large_extraspecial_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (z : G) (hz : orderOf z = 2)
    (hext : timmesfeldIsExtraspecial (timmesfeldFStar (Subgroup.centralizer ({z} : Set G))))
    (w : ℕ)
    (hw : Nat.card (timmesfeldFStar (Subgroup.centralizer ({z} : Set G))) = 2 ^ (1 + 2 * w))
    (Mbar : Type) [Group Mbar]
    (hMbar : timmesfeldQuotientIso (timmesfeldFStar (Subgroup.centralizer ({z} : Set G))) Mbar) :
    w ≤ 4 ∨
    (Nonempty (G ≃* PSL(w + 2, ZMod 2)) ∨ Nonempty (G ≃* timmesfeldPSU (w + 2))) ∨
    (6 ≤ w ∧ Even w ∧
      ∃ q : QuadraticForm (ZMod 2) (Fin w → ZMod 2), timmesfeldNondegenerate q ∧
        (Nonempty (Mbar ≃* Equiv.Perm (Fin 3) × timmesfeldOmega q) ∨
          Nonempty (Mbar ≃* Equiv.Perm (Fin 3) × timmesfeldIsometries q))) ∨
    (w = 6 ∧ IsQuasisimple (timmesfeldLayer Mbar) ∧ Nat.card (timmesfeldOddCore Mbar) ≤ 3 ∧
      ∃ t : Mbar, orderOf t = 2 ∧
        ∃ R : Subgroup Mbar, R ≤ Subgroup.centralizer ({t} : Set Mbar) ∧
          (R.subgroupOf (Subgroup.centralizer ({t} : Set Mbar))).Normal ∧
          (frattini (pCoreOf 2 R)).map (pCoreOf 2 R).subtype ≤ Subgroup.zpowers t ∧
          (timmesfeldQuotientIso (pCore 2 R) PSL(3, ZMod 2) ∨
            (∃ q : QuadraticForm (ZMod 2) (Fin 4 → ZMod 2), timmesfeldNondegenerate q ∧
              timmesfeldPlusType q ∧ timmesfeldQuotientIso (pCore 2 R) (timmesfeldOmega q)) ∨
            (pCoreOf 2 R = Subgroup.zpowers t ∧
              ∃ q : QuadraticForm (ZMod 2) (Fin 6 → ZMod 2), timmesfeldNondegenerate q ∧
                timmesfeldQuotientIso (pCore 2 R) (timmesfeldOmega q)))) ∨
    (w = 10 ∧ (timmesfeldFStar Mbar).index ≤ 2 ∧
      (Nonempty (timmesfeldFStar Mbar ≃* PSL(6, ZMod 2)) ∨
        Nonempty (timmesfeldFStar Mbar ≃* timmesfeldPSU 6)) ∧
      ∃ σ : Mbar, σ * σ = 1 ∧
        timmesfeldFStar Mbar ⊔ Subgroup.zpowers σ = ⊤) ∨
    (w = 11 ∧ Nonempty (Mbar ≃* Blueprint.NativeSporadic.Co2)) ∨
    (w = 12 ∧ Nonempty (Mbar ≃* Blueprint.NativeSporadic.Co1)) ∨
    (IsSimpleGroup Mbar ∧ ∃ t : Mbar, orderOf t = 2 ∧
      timmesfeldIsExtraspecial (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar))) ∧
      ((w = 16 ∧ Nat.card (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar))) = 2 ^ 17 ∧
          timmesfeldQuotientIso (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar)))
            (Equiv.Perm (Fin 3) × timmesfeldOmegaPlus 4)) ∨
        (w = 28 ∧ Nat.card (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar))) = 2 ^ 33 ∧
          timmesfeldQuotientIso (timmesfeldFStar (Subgroup.centralizer ({t} : Set Mbar)))
            (timmesfeldOmegaPlus 6))))
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CL_LIT_Fischer_three_transposition_theorem](../part-02/cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_GH74_sectional_two_rank_four](../part-02/cl-lit-gh74-sectional-two-rank-four.md)

## Sources

- [CFSG/Milestones/CL_LIT_Timmesfeld_1978_large_extraspecial.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_1978_large_extraspecial.lean)
