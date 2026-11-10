---
declaration: theorem
origin: cited
lean: CFSG.Milestones.frobenius_kernel, CFSG.Milestones.frobenius_kernel_existence
statement: formalized
proof: formalized
---

# FROB_kernel_existence

The milestone module `CFSG.Milestones.FROB_kernel_existence`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/FROB_kernel_existence.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FROB_kernel_existence.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.frobenius_kernel` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FROB_kernel_existence.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.frobenius_kernel (G X : Type) [Group G] [Fintype G] [Fintype X]
    [MulAction G X] [FaithfulSMul G X]
    (hcard : 2 ≤ Fintype.card X)
    (htrans : ∀ x y : X, ∃ g : G, g • x = y)
    (hstab : ∀ x : X, MulAction.stabilizer G x ≠ ⊥)
    (hfrob : ∀ g : G, g ≠ 1 → ∀ x y : X, g • x = x → g • y = y → x = y) :
    ∃ N : Subgroup G, N.Normal ∧
      (N : Set G) = {1} ∪ {g : G | ∀ x : X, g • x ≠ x}
```

`CFSG.Milestones.frobenius_kernel_existence` (theorem, [line 26](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FROB_kernel_existence.lean#L26)). Proved here.

```lean
theorem _root_.CFSG.Milestones.frobenius_kernel_existence {G : Type} [Group G] [Finite G] (H : Subgroup G)
    (hH1 : H ≠ ⊥) (hHG : H ≠ ⊤)
    (hfrob : ∀ g : G, g ∉ H → H ⊓ (MulAut.conj g • H) = ⊥) :
    ∃ K : Subgroup G,
      (K : Set G) = {1} ∪ (Set.univ \ ⋃ g : G, ((MulAut.conj g • H : Subgroup G) : Set G)) ∧
      K.Normal ∧ (∀ x : G, ∃ k ∈ K, ∃ h ∈ H, x = k * h) ∧ K ⊓ H = ⊥ ∧
      Nat.card K = H.index
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/FROB_kernel_existence.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FROB_kernel_existence.lean)
