---
declaration: section
origin: cited
lean: Stacks.Examples.QcohPushforward.exists_quasiCompact_not_quasiSeparated_pushforward_not_isQuasicoherent, Stacks.Examples.QcohPushforward.exists_isSeparated_not_quasiCompact_pushforward_not_isQuasicoherent
statement: formalized
proof: formalized
---

# 110.30 Pushforward of quasi-coherent modules

Section 110.30 of the Stacks Project, [Tag 078C](https://stacks.math.columbia.edu/tag/078C). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 078D, a lemma

[Tag 078D](https://stacks.math.columbia.edu/tag/078D) in the Stacks Project.

**`Stacks.Examples.QcohPushforward.exists_quasiCompact_not_quasiSeparated_pushforward_not_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/QuasiCoherentPushforward/NotQuasiSeparated.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/QuasiCoherentPushforward/NotQuasiSeparated.lean#L521). The attribute's comment: “non\_quasi\_separated”.

> **Stacks Project, Tag 078D (non-quasi-separated case).** A quasi-compact morphism need not
> be quasi-separated, and may send its quasi-coherent structure sheaf to a module which is not
> quasi-coherent.

```lean
theorem exists_quasiCompact_not_quasiSeparated_pushforward_not_isQuasicoherent :
    ∃ (X Y : Scheme.{u}) (f : X ⟶ Y),
      QuasiCompact f ∧
      ¬ QuasiSeparated f ∧
      (SheafOfModules.unit X.ringCatSheaf).IsQuasicoherent ∧
      ¬ ((Scheme.Modules.pushforward f).obj
        (SheafOfModules.unit X.ringCatSheaf)).IsQuasicoherent
```

**`Stacks.Examples.QcohPushforward.exists_isSeparated_not_quasiCompact_pushforward_not_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/QuasiCoherentPushforward/SeparatedNotQuasiCompact.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/QuasiCoherentPushforward/SeparatedNotQuasiCompact.lean#L263). The attribute's comment: “non\_quasi\_compact”.

> **Stacks Project, Tag 078D (non-quasi-compact case).** Over `Spec ℤ`, a separated,
> non-quasi-compact morphism can push a quasi-coherent structure sheaf to a sheaf which is not
> quasi-coherent.

```lean
theorem exists_isSeparated_not_quasiCompact_pushforward_not_isQuasicoherent :
    ∃ (X : Scheme) (f : X ⟶ Spec (.of ℤ)),
      IsSeparated f ∧ ¬ QuasiCompact f ∧
        (SheafOfModules.unit X.ringCatSheaf).IsQuasicoherent ∧
          ¬ ((Scheme.Modules.pushforward f).obj
            (SheafOfModules.unit X.ringCatSheaf)).IsQuasicoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.30, Tag 078C](https://stacks.math.columbia.edu/tag/078C)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
