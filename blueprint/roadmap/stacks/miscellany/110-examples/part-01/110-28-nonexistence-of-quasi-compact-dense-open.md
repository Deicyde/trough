---
declaration: section
origin: cited
lean: Stacks.Examples.AxesReflection.exists_quasiCompact_quasiSeparated_without_quasiCompact_dense_open_subscheme
statement: formalized
proof: formalized
---

# 110.28 Nonexistence of quasi-compact dense open subscheme

Section 110.28 of the Stacks Project, [Tag 087H](https://stacks.math.columbia.edu/tag/087H). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 087I, a lemma

[Tag 087I](https://stacks.math.columbia.edu/tag/087I) in the Stacks Project.

**`Stacks.Examples.AxesReflection.exists_quasiCompact_quasiSeparated_without_quasiCompact_dense_open_subscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/QcqsWithoutQuasiCompactDenseOpen.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/QcqsWithoutQuasiCompactDenseOpen.lean#L421). The attribute's comment: “a quasi-compact quasi-separated algebraic space with no quasi-compact dense open subscheme: the quotient of a line glued to countably many axes by a reflection”.

> **Stacks 087I.** There exists a quasi-compact and quasi-separated algebraic space which
> does not contain a quasi-compact dense open subscheme.
>
> The space is the quotient of `Spec k[x, z₁, z₂, …]/(x zᵢ, zᵢ zⱼ)` by the reflection
> `x ↦ -x` over the punctured line, for `k` of characteristic different from two.
>
> The space is an algebraic space by Stacks 02WW, through Stacks 0265 and the effective descent
> along the covering sieves at the monomorphisms locally of finite type that it consumes. The big
> fppf site carrying it is produced inside the proof, and so is existentially quantified.

```lean
theorem exists_quasiCompact_quasiSeparated_without_quasiCompact_dense_open_subscheme :
    ∃ (B : BigFppfSite.{u}) (hZ : B.Contains (⊤_ Scheme.{u}))
      (F : (BigFppfOver B (⊤_ Scheme.{u}) hZ)ᵒᵖ ⥤ Type u)
      (_ : IsAlgebraicSpace B (⊤_ Scheme.{u}) hZ F),
      Space.IsQuasiCompactSpace B (⊤_ Scheme.{u}) hZ F ∧
      Space.IsAbsolutelyQuasiSeparated B (⊤_ Scheme.{u}) hZ hZ F ∧
      ¬ ∃ (V : BigFppfOver B (⊤_ Scheme.{u}) hZ) (f : yoneda.obj V ⟶ F),
        CompactSpace ((BigFppfOver.toScheme B (⊤_ Scheme.{u}) hZ).obj V) ∧
        Space.IsOpenImmersion B (⊤_ Scheme.{u}) hZ f ∧
        Dense (Set.range (Space.pointsMap B (⊤_ Scheme.{u}) hZ (yoneda.obj V) f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.28, Tag 087H](https://stacks.math.columbia.edu/tag/087H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
