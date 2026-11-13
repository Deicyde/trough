---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.exists_faithfullyFlat_indEtale_extension
statement: formalized
proof: formalized
---

# 61.9 Weakly étale versus pro-étale

Section 61.9 of the Stacks Project, [Tag 097Y](https://stacks.math.columbia.edu/tag/097Y). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 097Z, a proposition

[Tag 097Z](https://stacks.math.columbia.edu/tag/097Z) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_faithfullyFlat_indEtale_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/WeaklyEtaleIndEtaleExtension.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/WeaklyEtaleIndEtaleExtension.lean#L191).

> A weakly étale ring map admits a faithfully flat ind-étale extension of its target after which
> the composite is ind-étale.

```lean
theorem exists_faithfullyFlat_indEtale_extension
    {A B : Type u} [CommRing A] [CommRing B] (f : A →+* B)
    (hf : letI := f.toAlgebra; Algebra.WeaklyEtale A B) :
    ∃ (B' : Type u) (_ : CommRing B') (g : B →+* B'),
      g.FaithfullyFlat ∧
        (ObjectProperty.ind.{u}
          (fun C : Under (CommRingCat.of B) ↦ C.hom.hom.Etale)
          (Under.mk (CommRingCat.ofHom g)) ∧
        ObjectProperty.ind.{u}
          (fun C : Under (CommRingCat.of A) ↦ C.hom.hom.Etale)
          (Under.mk (CommRingCat.ofHom (g.comp f))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.9, Tag 097Y](https://stacks.math.columbia.edu/tag/097Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
