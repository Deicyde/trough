---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cfsg_classification, CFSG.Milestones.cfsg_classification_and_realization, CFSG.Milestones.cfsg_classification_native_and_realization_of_certificates, CFSG.Milestones.cfsg_classification_native_and_realization
statement: formalized
proof: formalized
---

# CFSG_classification

The milestone module `CFSG.Milestones.CFSG_classification`, one of those CFSG/Milestones.lean imports.

It declares 4 results, quoted from [CFSG/Milestones/CFSG_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CFSG_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cfsg_classification` (theorem, [line 4575](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CFSG_classification.lean#L4575)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cfsg_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G] :
    ∃ i : TauCeti.CFSGIndex, Nonempty (G ≃* i.Group)
```

`CFSG.Milestones.cfsg_classification_and_realization` (theorem, [line 4585](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CFSG_classification.lean#L4585)). Proved here.

```lean
theorem cfsg_classification_and_realization
    :
    (∀ (G : Type) [Group G], Assembly.InCatalog G ↔ Finite G ∧ IsSimpleGroup G) ∧
    (∀ (p : ℕ) [Fact p.Prime],
      Finite (Multiplicative (ZMod p)) ∧ IsSimpleGroup (Multiplicative (ZMod p))) ∧
    (∀ n : ℕ, 5 ≤ n →
      Finite (alternatingGroup (Fin n)) ∧ IsSimpleGroup (alternatingGroup (Fin n))) ∧
    (∀ (t : CFSG.Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ),
      CFSG.Assembly.LowTwoRank.StatedLieAdmissible t n p f →
      ∃ (H : Type) (_ : Group H), Finite H ∧ Nontrivial H ∧ IsSimpleGroup H ∧
        CFSG.Blueprint.LieModel H t n p f) ∧
    (∀ s : TauCeti.SporadicName, Finite (nativeCarrier s) ∧ Nontrivial (nativeCarrier s) ∧
      IsSimpleGroup (nativeCarrier s))
```

`CFSG.Milestones.cfsg_classification_native_and_realization_of_certificates` (theorem, [line 4609](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CFSG_classification.lean#L4609)). Proved here.

```lean
theorem cfsg_classification_native_and_realization_of_certificates
    :
    (∀ (G : Type) [Group G],
      Blueprint.NativeCatalog G ↔ Finite G ∧ Nontrivial G ∧ IsSimpleGroup G) ∧
    (∀ p : ℕ, p.Prime →
      Finite (Multiplicative (ZMod p)) ∧ Nontrivial (Multiplicative (ZMod p)) ∧
        IsSimpleGroup (Multiplicative (ZMod p))) ∧
    (∀ n : ℕ, 5 ≤ n →
      Finite (alternatingGroup (Fin n)) ∧ Nontrivial (alternatingGroup (Fin n)) ∧
        IsSimpleGroup (alternatingGroup (Fin n))) ∧
    (∀ (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ),
      Assembly.LowTwoRank.StatedLieAdmissible t n p f →
      ∃ (H : Type) (_ : Group H), Finite H ∧ Nontrivial H ∧ IsSimpleGroup H ∧
        Blueprint.LieModel H t n p f) ∧
    (∀ s : TauCeti.SporadicName, Finite (nativeCarrier s) ∧ Nontrivial (nativeCarrier s) ∧
      IsSimpleGroup (nativeCarrier s))
```

`CFSG.Milestones.cfsg_classification_native_and_realization` (theorem, [line 4633](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CFSG_classification.lean#L4633)). Proved here.

```lean
theorem cfsg_classification_native_and_realization :
    (∀ (G : Type) [Group G],
      Blueprint.NativeCatalog G ↔ Finite G ∧ Nontrivial G ∧ IsSimpleGroup G) ∧
    (∀ p : ℕ, p.Prime →
      Finite (Multiplicative (ZMod p)) ∧ Nontrivial (Multiplicative (ZMod p)) ∧
        IsSimpleGroup (Multiplicative (ZMod p))) ∧
    (∀ n : ℕ, 5 ≤ n →
      Finite (alternatingGroup (Fin n)) ∧ Nontrivial (alternatingGroup (Fin n)) ∧
        IsSimpleGroup (alternatingGroup (Fin n))) ∧
    (∀ (t : Assembly.LowTwoRank.StatedLieTag) (n p f : ℕ),
      Assembly.LowTwoRank.StatedLieAdmissible t n p f →
      ∃ (H : Type) (_ : Group H), Finite H ∧ Nontrivial H ∧ IsSimpleGroup H ∧
        Blueprint.LieModel H t n p f) ∧
    (∀ s : TauCeti.SporadicName, Finite (nativeCarrier s) ∧ Nontrivial (nativeCarrier s) ∧
      IsSimpleGroup (nativeCarrier s))
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CAT_converse](cat-converse.md)
- [CFSG_exhaustiveness](cfsg-exhaustiveness.md)
- [FAM_sporadic_native_converse](../part-04/fam-sporadic-native-converse.md)

## Sources

- [CFSG/Milestones/CFSG_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CFSG_classification.lean)
