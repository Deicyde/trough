---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_timmesfeld_root_involutions, CFSG.Milestones.cl_lit_timmesfeld_root_involutions_models
statement: formalized
proof: formalized
---

# CL_LIT_Timmesfeld_root_involutions

The milestone module `CFSG.Milestones.CL_LIT_Timmesfeld_root_involutions`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_Timmesfeld_root_involutions.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_root_involutions.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_timmesfeld_root_involutions` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_root_involutions.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_timmesfeld_root_involutions
    (G : Type) [Group G] [Finite G] (D : Set G)
    (hclass : ∃ d₀ : G, D = {g | IsConj d₀ g})
    (hinv : ∀ d ∈ D, orderOf d = 2)
    (hgen : Subgroup.closure D = ⊤)
    (hcenter : Subgroup.center G = ⊥)
    (hodd : ∀ N : Subgroup G, N.Normal → Odd (Nat.card N) → N = ⊥)
    (hO2 : ∀ N : Subgroup G, N.Normal → IsPGroup 2 N → N = ⊥)
    (hprod : ∀ d ∈ D, ∀ e ∈ D,
      orderOf (d * e) = 2 ∨ orderOf (d * e) = 4 ∨ Odd (orderOf (d * e)))
    (hfour : ∀ d ∈ D, ∀ e ∈ D, orderOf (d * e) = 4 → (d * e) ^ 2 ∈ D)
    (hnondeg : ∃ d ∈ D, ∃ e ∈ D, orderOf (d * e) = 4) :
    IsSimpleGroup G ∧
      ((Nat.card G ∈ lieOrdersChar 2 ∧
          (∀ n f : ℕ, 2 ≤ n → 1 ≤ f → Nat.card G ≠ ordTwistedA n (2 ^ f)) ∧
          (∀ f : ℕ, 1 ≤ f → Nat.card G ≠ ordBC 2 (2 ^ f))) ∨
        Nonempty (G ≃* PSU3 3 1) ∨
        Nonempty (G ≃* alternatingGroup (Fin 6)) ∨
        Nat.card G = 2 ^ 7 * 3 ^ 3 * 5 ^ 2 * 7)
```

`CFSG.Milestones.cl_lit_timmesfeld_root_involutions_models` (theorem, [line 39](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_root_involutions.lean#L39)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_timmesfeld_root_involutions_models
    (G : Type) [Group G] [Finite G] (D : Set G)
    (hclass : ∃ d₀ : G, D = {g | IsConj d₀ g})
    (hinv : ∀ d ∈ D, orderOf d = 2)
    (hgen : Subgroup.closure D = ⊤)
    (hcenter : Subgroup.center G = ⊥)
    (hodd : ∀ N : Subgroup G, N.Normal → Odd (Nat.card N) → N = ⊥)
    (hO2 : ∀ N : Subgroup G, N.Normal → IsPGroup 2 N → N = ⊥)
    (hprod : ∀ d ∈ D, ∀ e ∈ D,
      orderOf (d * e) = 2 ∨ orderOf (d * e) = 4 ∨ Odd (orderOf (d * e)))
    (hfour : ∀ d ∈ D, ∀ e ∈ D, orderOf (d * e) = 4 → (d * e) ^ 2 ∈ D)
    (hnondeg : ∃ d ∈ D, ∃ e ∈ D, orderOf (d * e) = 4) :
    (Blueprint.EvenLieType G ∧
      (∀ n f : ℕ, 3 ≤ n → 1 ≤ f → ¬ Blueprint.LieModel G .PSU n 2 f) ∧
      (∀ f : ℕ, 1 ≤ f → ¬ Blueprint.LieModel G .PSp 2 2 f)) ∨
    Blueprint.LieModel G .PSU 3 3 1 ∨ Nonempty (G ≃* alternatingGroup (Fin 6)) ∨
      Blueprint.NativeSporadic.IsSporadic G .J2
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CFSG.FeitThompson.isSolvable_of_odd_natCard](../../case-division/case-hodd-oddorderstatement.md)
- [CLS_connectivity_MacWilliams_four_generator](../part-01/cls-connectivity-macwilliams-four-generator.md)
- [CL_LIT_SQTK_simple_listBase](cl-lit-sqtk-simple-listbase.md)
- [LR_Glauberman_Z_star_central_Sylow_involution](../part-05/lr-glauberman-z-star-central-sylow-involution.md)

## Sources

- [CFSG/Milestones/CL_LIT_Timmesfeld_root_involutions.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Timmesfeld_root_involutions.lean)
