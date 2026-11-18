---
declaration: theorem
origin: cited
lean: IsTopologicalAddGroup.metrizableSpace, IsTopologicalAddGroup.pseudoMetrizableSpace, IsTopologicalGroup.metrizableSpace, IsTopologicalGroup.pseudoMetrizableSpace
statement: formalized
proof: formalized
---

# Birkhoff–Kakutani theorem

a `T₀` topological additive group whose zero has
a countably generated neighbourhood filter is metrizable.

```lean
IsTopologicalAddGroup.metrizableSpace.{u_1} (G : Type u_1) [AddGroup G] [TopologicalSpace G]
  [IsTopologicalAddGroup G] [T0Space G] [(nhds 0).IsCountablyGenerated] :
  TopologicalSpace.MetrizableSpace G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsTopologicalAddGroup.metrizableSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Metrizable.html#IsTopologicalAddGroup.metrizableSpace).

## Other forms

**Birkhoff–Kakutani theorem (pseudometrizable form).** Formalized in Tau Ceti as [`IsTopologicalAddGroup.pseudoMetrizableSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Metrizable.html#IsTopologicalAddGroup.pseudoMetrizableSpace).

```lean
IsTopologicalAddGroup.pseudoMetrizableSpace.{u_1} (G : Type u_1) [AddGroup G] [TopologicalSpace G]
  [IsTopologicalAddGroup G] [(nhds 0).IsCountablyGenerated] :
  TopologicalSpace.PseudoMetrizableSpace G
```

**Birkhoff–Kakutani theorem.** Formalized in Tau Ceti as [`IsTopologicalGroup.metrizableSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Metrizable.html#IsTopologicalGroup.metrizableSpace).

```lean
IsTopologicalGroup.metrizableSpace.{u_1} (G : Type u_1) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [T0Space G] [(nhds 1).IsCountablyGenerated] :
  TopologicalSpace.MetrizableSpace G
```

**Birkhoff–Kakutani theorem (pseudometrizable form).** Formalized in Tau Ceti as [`IsTopologicalGroup.pseudoMetrizableSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Metrizable.html#IsTopologicalGroup.pseudoMetrizableSpace).

```lean
IsTopologicalGroup.pseudoMetrizableSpace.{u_1} (G : Type u_1) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [(nhds 1).IsCountablyGenerated] : TopologicalSpace.PseudoMetrizableSpace G
```

## Sources

- [Tau Ceti documentation: `IsTopologicalAddGroup.metrizableSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Metrizable.html#IsTopologicalAddGroup.metrizableSpace)
- [Source of `IsTopologicalAddGroup.metrizableSpace` in TauCeti/Topology/Algebra/Group/Metrizable.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Metrizable.lean#L68)
