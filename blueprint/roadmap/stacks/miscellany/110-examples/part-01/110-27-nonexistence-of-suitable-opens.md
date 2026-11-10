---
declaration: section
origin: cited
lean: Stacks.Examples.exists_affine_scheme_punctured_without_quasiCompact_dense_open, Stacks.Examples.exists_affineOpen_without_disjoint_quasiCompact_dense_union, Stacks.Examples.exists_qcqs_without_separated_quasiCompact_dense_open
statement: formalized
proof: formalized
---

# 110.27 Nonexistence of suitable opens

Section 110.27 of the Stacks Project, [Tag 086G](https://stacks.math.columbia.edu/tag/086G). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 086H, a lemma

[Tag 086H](https://stacks.math.columbia.edu/tag/086H) in the Stacks Project.

**`Stacks.Examples.exists_affine_scheme_punctured_without_quasiCompact_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/PuncturedAxes.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Scheme/PuncturedAxes.lean#L265). The attribute's comment: “punctured_affine”.

> There is an affine scheme with a closed point such that its punctured complement contains no
> quasi-compact dense open subset.

```lean
theorem exists_affine_scheme_punctured_without_quasiCompact_dense_open :
    ∃ (S : Scheme.{u}) (_ : IsAffine S) (s : S),
      IsClosed ({s} : Set S) ∧
        ¬ ∃ U : Set {x : S // x ≠ s}, IsOpen U ∧ IsCompact U ∧ Dense U
```

**`Stacks.Examples.exists_affineOpen_without_disjoint_quasiCompact_dense_union`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/PuncturedAxes.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Scheme/PuncturedAxes.lean#L279). The attribute's comment: “disjoint_dense_union”.

> In some affine scheme, an affine open has no disjoint quasi-compact open whose union with it
> is dense.

```lean
theorem exists_affineOpen_without_disjoint_quasiCompact_dense_union :
    ∃ (S : Scheme.{u}) (_ : IsAffine S) (U : S.Opens),
      IsAffineOpen U ∧
        ¬ ∃ V : S.Opens, IsCompact V.1 ∧ (U ⊓ V = ⊥) ∧ Dense (U.1 ∪ V.1)
```

## Tag 086I, a lemma

[Tag 086I](https://stacks.math.columbia.edu/tag/086I) in the Stacks Project.

**`Stacks.Examples.exists_qcqs_without_separated_quasiCompact_dense_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/QcqsWithoutSeparatedDenseOpen.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Scheme/QcqsWithoutSeparatedDenseOpen.lean#L357).

> **Stacks 086I.** There is a quasi-compact quasi-separated scheme with no separated
> quasi-compact dense open.

```lean
theorem exists_qcqs_without_separated_quasiCompact_dense_open :
    ∃ X : Scheme.{u}, CompactSpace X ∧ QuasiSeparatedSpace X ∧
      ¬ ∃ V : X.Opens, IsCompact (V : Set X) ∧ Dense (V : Set X) ∧
        Scheme.IsSeparated V
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.27, Tag 086G](https://stacks.math.columbia.edu/tag/086G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
