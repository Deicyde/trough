---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_as_vol_i_background_1, CFSG.Milestones.cl_lit_as_vol_i_background_2, CFSG.Milestones.cl_lit_as_vol_i_background_3, CFSG.Milestones.cl_lit_as_vol_i_background_4, CFSG.Milestones.cl_lit_as_vol_i_background_partial, CFSG.Milestones.cl_lit_as_vol_i_background
statement: formalized
proof: formalized
---

# CL_LIT_AS_vol_I_background

The milestone module `CFSG.Milestones.CL_LIT_AS_vol_I_background`, one of those CFSG/Milestones.lean imports.

It declares 6 results, quoted from [CFSG/Milestones/CL_LIT_AS_vol_I_background.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_as_vol_i_background_1` (theorem, [line 19](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean#L19)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_as_vol_i_background_1
    (p f : ℕ) [Fact p.Prime] (hf : 1 ≤ f) (H : Subgroup PSL(2, GaloisField p f)) :
    (IsElemAbelian p H ∧ ∃ m : ℕ, m ≤ f ∧ Nat.card H = p ^ m) ∨
    (IsCyclic H ∧ (Nat.card H ∣ (p ^ f + 1) / Nat.gcd 2 (p ^ f - 1) ∨
      Nat.card H ∣ (p ^ f - 1) / Nat.gcd 2 (p ^ f - 1))) ∨
    (∃ z : ℕ, (z ∣ (p ^ f + 1) / Nat.gcd 2 (p ^ f - 1) ∨
      z ∣ (p ^ f - 1) / Nat.gcd 2 (p ^ f - 1)) ∧ Nonempty (H ≃* DihedralGroup z)) ∨
    ((p ≠ 2 ∨ Even f) ∧ Nonempty (H ≃* alternatingGroup (Fin 4))) ∨
    (16 ∣ p ^ (2 * f) - 1 ∧ Nonempty (H ≃* Equiv.Perm (Fin 4))) ∨
    ((p = 5 ∨ 5 ∣ p ^ (2 * f) - 1) ∧ Nonempty (H ≃* alternatingGroup (Fin 5))) ∨
    (∃ (m t : ℕ) (P : Subgroup H) (_ : P.Normal), IsElemAbelian p P ∧
      Nat.card P = p ^ m ∧ IsCyclic (H ⧸ P) ∧ Nat.card (H ⧸ P) = t ∧ t ∣ p ^ m - 1 ∧
      t ∣ (p ^ f - 1) / Nat.gcd 2 (p ^ f - 1)) ∨
    (∃ m : ℕ, m ∣ f ∧ Nonempty (H ≃* PSL(2, GaloisField p m))) ∨
    (∃ m : ℕ, 2 * m ∣ f ∧ Nonempty (H ≃* PGL(2, GaloisField p m)))
```

`CFSG.Milestones.cl_lit_as_vol_i_background_2` (theorem, [line 43](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean#L43)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_as_vol_i_background_2 :
    (∀ n : ℕ, 2 ≤ n → quasithinH1CardSL 2 (GaloisField 2 n) = 2 ^ n) ∧
    (∀ n : ℕ, 2 ≤ n → quasithinH1CardSL 3 (GaloisField 2 n) = 1) ∧
    quasithinH1CardSL 3 (ZMod 2) = 2 ∧
    (∀ n : ℕ, 2 ≤ n →
      Nat.card (groupCohomology (Rep.of (quasithinH1MatrixRep
        (Matrix.symplecticGroup (Fin 2) (GaloisField 2 n)).subtype)) 1) = 2 ^ n) ∧
    quasithinH1CardSL 4 (ZMod 2) = 1 ∧
    quasithinH1CardSL 5 (ZMod 2) = 1
```

`CFSG.Milestones.cl_lit_as_vol_i_background_3` (theorem, [line 61](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean#L61)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_as_vol_i_background_3 :
    quasithinMultiplierCyclic (alternatingGroup (Fin 9)) 2 ∧
    (∀ (p k : ℕ) [Fact p.Prime], p ≠ 2 → 9 < p ^ k →
      quasithinMultiplierCyclic PSL(2, GaloisField p k) 2) ∧
    quasithinMultiplierCyclic (quasithinPSU 4 2 1) 2 ∧
    quasithinMultiplierCyclic PSL(4, ZMod 3) 2 ∧
    quasithinMultiplierCyclic quasithinJ3 3 ∧
    quasithinMultiplierCyclic quasithinMcL 3 ∧
    quasithinMultiplierCyclic (quasithinG2 (ZMod 3)) 3 ∧
    (∀ (p k : ℕ) [Fact p.Prime], p ≠ 2 → 0 < k → 3 ∣ p ^ k - 1 →
      quasithinMultiplierCyclic PSL(3, GaloisField p k) 3) ∧
    (∀ (p k : ℕ) [Fact p.Prime], p ≠ 2 → 0 < k → 3 ∣ p ^ k + 1 →
      quasithinMultiplierCyclic (PSU3 p k) 3) ∧
    (∀ (r m : ℕ) [Fact r.Prime], r = 2 ^ 2 ^ m + 1 → 3 < r →
      quasithinMultiplierCyclic PSL(4, ZMod r) 4) ∧
    (∀ (s m : ℕ) [Fact s.Prime], s = 2 ^ m - 1 → 3 < s →
      quasithinMultiplierCyclic (quasithinPSU 4 s 1) 4) ∧
    quasithinMultiplierCyclic (quasithinPSU 5 2 2) 5 ∧
    Nonempty (quasithinHopfMultiplier (quasithinPSU 4 3 1) ≃*
      Multiplicative (ZMod 3 × ZMod 3 × ZMod 4)) ∧
    quasithinMultiplierCyclic (Matrix.symplecticGroup (Fin 3) (ZMod 2)) 2 ∧
    (∀ (p : ℕ) [Fact p.Prime], 5 ≤ p → quasithinMultiplierCyclic (quasithinPSp 2 (ZMod p)) 2)
```

`CFSG.Milestones.cl_lit_as_vol_i_background_4` (theorem, [line 92](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean#L92)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_as_vol_i_background_4 :
    quasithinMultiplierCyclic PSL(4, ZMod 2) 2 ∧
    quasithinMultiplierCyclic (quasithinG2 (GaloisField 2 2)) 2 ∧
    quasithinMultiplierCyclic quasithinM12 2 ∧
    quasithinMultiplierCyclic quasithinJ2 2 ∧
    quasithinMultiplierCyclic quasithinHS 2 ∧
    quasithinMultiplierCyclic quasithinRu 2 ∧
    (∀ (p k : ℕ) [Fact p.Prime], p ≠ 2 → 0 < k → p ^ k ≠ 3 → p ^ k ≠ 9 →
      quasithinMultiplierCyclic PSL(2, GaloisField p k) 2) ∧
    (∀ (p k : ℕ) [Fact p.Prime], 0 < k → 3 ∣ p ^ k - 1 → p ^ k ≠ 4 →
      quasithinMultiplierCyclic PSL(3, GaloisField p k) 3) ∧
    (∀ (p k : ℕ) [Fact p.Prime], 0 < k → 3 ∣ p ^ k + 1 → p ^ k ≠ 2 →
      quasithinMultiplierCyclic (PSU3 p k) 3) ∧
    quasithinMultiplierCyclic (alternatingGroup (Fin 6)) 6 ∧
    quasithinMultiplierCyclic (alternatingGroup (Fin 7)) 6 ∧
    quasithinMultiplierCyclic quasithinM22 12 ∧
    Nonempty (quasithinHopfMultiplier (Sz 1) ≃* Multiplicative (ZMod 2 × ZMod 2)) ∧
    Nonempty (quasithinHopfMultiplier PSL(3, GaloisField 2 2) ≃*
      Multiplicative (ZMod 4 × ZMod 4 × ZMod 3))
```

`CFSG.Milestones.cl_lit_as_vol_i_background_partial` (theorem, [line 120](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean#L120)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_as_vol_i_background_partial
    : CFSG.ASVolI.Statement
```

`CFSG.Milestones.cl_lit_as_vol_i_background` (theorem, [line 127](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean#L127)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_as_vol_i_background
    : CFSG.ASVolI.Statement
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_Curtis_Tits_presentation_theorem](cl-lit-curtis-tits-presentation-theorem.md)
- [CL_LIT_Fischer_three_transposition_theorem](cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_GH74_sectional_two_rank_four](cl-lit-gh74-sectional-two-rank-four.md)
- [CL_LIT_GMS_Monster_uniqueness](cl-lit-gms-monster-uniqueness.md)
- [CL_LIT_Monster_existence_Griess_Conway](cl-lit-monster-existence-griess-conway.md)

## Sources

- [CFSG/Milestones/CL_LIT_AS_vol_I_background.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_AS_vol_I_background.lean)
