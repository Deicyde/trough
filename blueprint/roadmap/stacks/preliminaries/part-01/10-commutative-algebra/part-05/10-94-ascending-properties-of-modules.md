---
declaration: section
origin: cited
lean: Module.baseChange_flat_and_mittagLeffler_and_exists_sSupIndep_countable_span_and_projective
statement: formalized
proof: formalized
---

# 10.94 Ascending properties of modules

Section 10.94 of the Stacks Project, [Tag 05A2](https://stacks.math.columbia.edu/tag/05A2). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05A3, a lemma

[Tag 05A3](https://stacks.math.columbia.edu/tag/05A3) in the Stacks Project.

**`Module.baseChange_flat_and_mittagLeffler_and_exists_sSupIndep_countable_span_and_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/BaseChange.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/BaseChange.lean#L83). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E and "direct sum of countably generated modules" as an independent set of countably spanned submodules with supremum `⊤`, as in 059M, 05A5 and 058W. The source's `M ⊗_R S` is written `S ⊗[R] M`.”.

> Base change along a ring map `R → S` preserves flatness, the Mittag-Leffler condition, being
> a direct sum of countably generated modules, and projectivity.

```lean
theorem baseChange_flat_and_mittagLeffler_and_exists_sSupIndep_countable_span_and_projective
    [Small.{v} R] :
    (Module.Flat R M → Module.Flat S (S ⊗[R] M)) ∧
    ((∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module R N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) →
      ∀ (P : Type v) [AddCommGroup P] [Module S P] [Module.FinitePresentation S P]
      (f : P →ₗ[S] S ⊗[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module S Q)
        (_ : Module.FinitePresentation S Q) (g : P →ₗ[S] Q), ∀ (N : Type v) [AddCommGroup N]
          [Module S N], LinearMap.ker (f.rTensor N) = LinearMap.ker (g.rTensor N)) ∧
    ((∃ 𝒮 : Set (Submodule R M), sSupIndep 𝒮 ∧ sSup 𝒮 = ⊤ ∧
        ∀ N ∈ 𝒮, ∃ t : Set M, t.Countable ∧ Submodule.span R t = N) →
      ∃ 𝒮 : Set (Submodule S (S ⊗[R] M)), sSupIndep 𝒮 ∧ sSup 𝒮 = ⊤ ∧
        ∀ N ∈ 𝒮, ∃ t : Set (S ⊗[R] M), t.Countable ∧ Submodule.span S t = N) ∧
    (Module.Projective R M → Module.Projective S (S ⊗[R] M))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.94, Tag 05A2](https://stacks.math.columbia.edu/tag/05A2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
