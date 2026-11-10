---
declaration: theorem
origin: cited
lean: CFSG.FeitThompson.isSolvable_of_odd_natCard
statement: formalized
proof: formalized
---

# CFSG.FeitThompson.isSolvable_of_odd_natCard

The case `hodd : OddOrderStatement` of [`CFSG.Assembly.classification`](reduction.md). What it asserts, defined in [CFSG/Assembly/Reduction.lean, line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L16):

```lean
@[expose] def OddOrderStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G], Odd (Nat.card G) → Group.IsSolvable G
```

The theorem the top theorem's proof gives for it, quoted from [CFSG/FeitThompson/OddOrderTheorem.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/FeitThompson/OddOrderTheorem.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.FeitThompson.isSolvable_of_odd_natCard` (theorem, [line 14](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/FeitThompson/OddOrderTheorem.lean#L14)). Proved here.

```lean
theorem isSolvable_of_odd_natCard (G : Type*) [Group G] [Finite G] (hG : Odd (Nat.card G)) :
    Group.IsSolvable G
```

Its file imports none of the milestone modules, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/FeitThompson/OddOrderTheorem.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/FeitThompson/OddOrderTheorem.lean#L14)
