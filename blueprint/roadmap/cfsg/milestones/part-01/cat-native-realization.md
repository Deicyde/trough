---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cat_native_realization_cyclic, CFSG.Milestones.cat_native_realization_alternating, CFSG.Milestones.cat_native_realization_lie, CFSG.Milestones.native_carrier_finite_simple_of_ne_B, CFSG.Milestones.cat_native_realization_cyclic', CFSG.Milestones.cat_native_realization_alternating', CFSG.Milestones.cat_native_realization_sporadic, CFSG.Milestones.cat_native_realization
statement: formalized
proof: formalized
---

# CAT_native_realization

The milestone module `CFSG.Milestones.CAT_native_realization`, one of those CFSG/Milestones.lean imports.

It declares 8 results, quoted from [CFSG/Milestones/CAT_native_realization.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cat_native_realization_cyclic` (theorem, [line 34](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L34)). Proved here.

```lean
theorem cat_native_realization_cyclic (p : ℕ) [Fact p.Prime] :
    Finite (Multiplicative (ZMod p)) ∧ IsSimpleGroup (Multiplicative (ZMod p))
```

`CFSG.Milestones.cat_native_realization_alternating` (theorem, [line 39](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L39)). Proved here.

```lean
theorem cat_native_realization_alternating (n : ℕ) (hn : 5 ≤ n) :
    Finite (alternatingGroup (Fin n)) ∧ IsSimpleGroup (alternatingGroup (Fin n))
```

`CFSG.Milestones.cat_native_realization_lie` (theorem, [line 43](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L43)). Proved here.

```lean
theorem cat_native_realization_lie
    (t : CFSG.Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ)
    (h : CFSG.Assembly.LowTwoRank.StatedLieAdmissible t n p f) :
    ∃ (G : Type) (_ : Group G), Finite G ∧ Nontrivial G ∧ IsSimpleGroup G ∧
      CFSG.Blueprint.LieModel G t n p f
```

`CFSG.Milestones.native_carrier_finite_simple_of_ne_B` (theorem, [line 51](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L51)). Proved here.

```lean
theorem native_carrier_finite_simple_of_ne_B
    (s : TauCeti.SporadicName) (hs : s ≠ .B) :
    Finite (nativeCarrier s) ∧ Nontrivial (nativeCarrier s) ∧ IsSimpleGroup (nativeCarrier s)
```

`CFSG.Milestones.cat_native_realization_cyclic'` (theorem, [line 89](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L89)). Proved here.

```lean
theorem cat_native_realization_cyclic' (p : ℕ) (hp : p.Prime) :
    Finite (Multiplicative (ZMod p)) ∧ Nontrivial (Multiplicative (ZMod p)) ∧
      IsSimpleGroup (Multiplicative (ZMod p))
```

`CFSG.Milestones.cat_native_realization_alternating'` (theorem, [line 96](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L96)). Proved here.

```lean
theorem cat_native_realization_alternating' (n : ℕ) (hn : 5 ≤ n) :
    Finite (alternatingGroup (Fin n)) ∧ Nontrivial (alternatingGroup (Fin n)) ∧
      IsSimpleGroup (alternatingGroup (Fin n))
```

`CFSG.Milestones.cat_native_realization_sporadic` (theorem, [line 103](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L103)). Proved here.

```lean
theorem cat_native_realization_sporadic
    (s : TauCeti.SporadicName) :
    Finite (nativeCarrier s) ∧ Nontrivial (nativeCarrier s) ∧ IsSimpleGroup (nativeCarrier s)
```

`CFSG.Milestones.cat_native_realization` (theorem, [line 113](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean#L113)). Proved here.

```lean
theorem cat_native_realization :
    (∀ p : ℕ, p.Prime → Finite (Multiplicative (ZMod p)) ∧ Nontrivial (Multiplicative (ZMod p)) ∧
      IsSimpleGroup (Multiplicative (ZMod p))) ∧
    (∀ n : ℕ, 5 ≤ n → Finite (alternatingGroup (Fin n)) ∧ Nontrivial (alternatingGroup (Fin n)) ∧
      IsSimpleGroup (alternatingGroup (Fin n))) ∧
    (∀ (t : CFSG.Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ),
      CFSG.Assembly.LowTwoRank.StatedLieAdmissible t n p f →
      ∃ (G : Type) (_ : Group G), Finite G ∧ Nontrivial G ∧ IsSimpleGroup G ∧
        CFSG.Blueprint.LieModel G t n p f) ∧
    (∀ s : TauCeti.SporadicName, Finite (nativeCarrier s) ∧ Nontrivial (nativeCarrier s) ∧
      IsSimpleGroup (nativeCarrier s))
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [FAM_Th_simplicity](../part-04/fam-th-simplicity.md)
- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)

## Sources

- [CFSG/Milestones/CAT_native_realization.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CAT_native_realization.lean)
