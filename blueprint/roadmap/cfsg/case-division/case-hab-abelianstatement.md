---
declaration: theorem
origin: cited
lean: CFSG.Assembly.abelian_simple
statement: formalized
proof: formalized
---

# CFSG.Assembly.abelian_simple

The case `hab : AbelianStatement` of [`CFSG.Assembly.classification`](reduction.md). What it asserts, defined in [CFSG/Assembly/Reduction.lean, line 19](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L19):

```lean
@[expose] def AbelianStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∀ a b : G, a * b = b * a) → C G
```

The theorem the top theorem's proof gives for it, quoted from [CFSG/Assembly/InCatalog.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/InCatalog.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Assembly.abelian_simple` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/InCatalog.lean#L12)). Proved here.

```lean
theorem abelian_simple (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hcomm : ∀ a b : G, a * b = b * a) : InCatalog G
```

Its file imports none of the milestone modules, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Assembly/InCatalog.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/InCatalog.lean#L12)
