---
declaration: theorem
origin: cited
lean: CFSG.Assembly.disconnected_involution_graph
statement: formalized
proof: formalized
---

# CFSG.Assembly.disconnected_involution_graph

The case `hdisc : DisconnectedStatement` of [`CFSG.Assembly.classification`](reduction.md). What it asserts, defined in [CFSG/Assembly/Reduction.lean, line 22](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L22):

```lean
@[expose] def DisconnectedStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    Even (Nat.card G) → ¬ (involutionGraph G).Preconnected → C G
```

The theorem the top theorem's proof gives for it, quoted from [CFSG/Assembly/Disconnected.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Disconnected.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Assembly.disconnected_involution_graph` (theorem, [line 65](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Disconnected.lean#L65)). Proved here.

```lean
theorem disconnected_involution_graph (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (heven : Even (Nat.card G))
    (hdisc : ¬ (involutionGraph G).Preconnected) : InCatalog G
```

Its file imports none of the milestone modules, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Assembly/Disconnected.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Disconnected.lean#L65)
