---
declaration: section
origin: cited
lean: OAI.PartitionPilot.Forcing.TransitiveGround.exists_model_partitionPrinciple_without_choice, OAI.PartitionConsistency.main_consistency
statement: formalized
proof: formalized
---

# 244. The Partition Principle does not imply Choice

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Assuming ZF is consistent, constructs a model in which every surjective image of a set injects into that set, yet the axiom of choice fails. Choice for ordinal-indexed families still holds. From any countable transitive model of ZFC, a separate construction gives a transitive symmetric extension with these properties and no new countable sequences of ground-model elements.

## The Partition Principle does not imply Choice

We prove that the Partition Principle does not imply the Axiom of Choice: if ZF is consistent, then so is ZF with the Partition Principle, Choice for ordinal-indexed families, and the negation of the Axiom of Choice. Separately, over every countable transitive model of ZFC, we construct a transitive symmetric model of this theory with the same ordinals and no new countable sequences of ground elements.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/partition-principle-without-choice.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Partition Principle says that every surjection admits an injection in the reverse direction. The formalization proves the relative-consistency implication: if ZF is consistent, then so is ZF with the Partition Principle, Choice for ordinal-indexed families, and failure of the Axiom of Choice.

The linked model-construction result also constructs a transitive model of the Partition Principle without Choice from an externally countable transitive ground model satisfying the stated axioms, including Choice, and containing an internal strongly inaccessible cardinal. The paper's stronger transitive-model preservation assertions are outside that selected construction.

## Lean: Partition Principle without Choice from a ground model

```lean
theorem exists_model_partitionPrinciple_without_choice
    (pairing : Realize M.sets SetFormula.pairing Fin.elim0)
    (unions : Realize M.sets SetFormula.union Fin.elim0)
    (powers : Realize M.sets powerSet Fin.elim0) (separation : SeparationSchema M.sets)
    (collection : CollectionSchema M.sets) (infinite : Realize M.sets infinity Fin.elim0)
    (choice : Realize M.sets SetFormula.choice Fin.elim0)
    (small : M.sets.Countable)
    {K : ZFSet.{u}} (hK : K ∈ M.sets) (standard : GroundStandardInaccessible M K) :
    ∃ N : TransitiveGround.{u}, M.sets ⊆ N.sets ∧ ZFRealization N.sets ∧
      Realize N.sets partitionPrinciple Fin.elim0 ∧
      ¬ Realize N.sets SetFormula.choice Fin.elim0
```

Stated in [PartitionPrinciple.lean, line 262](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PartitionPrinciple.lean#L262). Proved in [lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean, line 34](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean#L34). formalization.yaml lists it as one of the repository's main results.

## Lean: Relative consistency of the Partition Principle with ordinal Choice and failure of Choice

```lean
theorem main_consistency :
    Consistent SetLanguage.ZF → Consistent SetLanguage.targetTheory
```

Stated in [PartitionConsistency.lean, line 318](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PartitionConsistency.lean#L318). Proved in [lean/OAI/SetTheory/PartitionConsistency/Main.lean, line 181](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/SetTheory/PartitionConsistency/Main.lean#L181).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/244.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/244.md)
