---
declaration: section
origin: cited
lean: Module.IsEssentialEpi, Module.IsEssentialMono, Module.isEssentialEpi_comp, Module.isEssentialMono_comp, Module.isEssentialMono_pullback, Module.essentialEpi_epiDesc_cokernel, Module.isEssentialMono_colimit, Module.isEssentialMono_subtype_iff
statement: formalized
proof: formalized
---

# 47.2 Essential surjections and injections

Section 47.2 of the Stacks Project, [Tag 08XI](https://stacks.math.columbia.edu/tag/08XI). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08XJ, a definition

[Tag 08XJ](https://stacks.math.columbia.edu/tag/08XJ) in the Stacks Project.

**`Module.IsEssentialEpi`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L71). The attribute's comment: “essential_surjection”.

> A morphism is an essential epimorphism if it is an epimorphism and the direct image of
> every proper subobject of its source is proper.

```lean
abbrev IsEssentialEpi {C : Type u} [Category.{v} C] [HasImages C] {X Y : C} (f : X ⟶ Y) : Prop
```

**`Module.IsEssentialMono`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L77). The attribute's comment: “essential_injection”.

> A monomorphism is essential if every nonzero subobject of its codomain has nonzero
> intersection with its image.

```lean
abbrev IsEssentialMono {𝒜 : Type u} [Category.{v} 𝒜] [HasZeroObject 𝒜] [HasPullbacks 𝒜]
    {A B : 𝒜} (i : A ⟶ B) [Mono i] : Prop
```

## Tag 08XK, a lemma

[Tag 08XK](https://stacks.math.columbia.edu/tag/08XK) in the Stacks Project.

**`Module.isEssentialEpi_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L112). The attribute's comment: “essential_surjection_comp”.

> The composite of two essential epimorphisms is an essential epimorphism.

```lean
theorem isEssentialEpi_comp [HasImages 𝒜] {A B C : 𝒜} {f : A ⟶ B} {g : B ⟶ C}
    (hf : IsEssentialEpi f) (hg : IsEssentialEpi g) : IsEssentialEpi (f ≫ g)
```

**`Module.isEssentialMono_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L137). The attribute's comment: “essential_extension_trans”.

> The composite of two essential monomorphisms is essential.

```lean
theorem isEssentialMono_comp {A B C : 𝒜} (i : A ⟶ B) (j : B ⟶ C) [Mono i] [Mono j]
    (hi : IsEssentialMono i) (hj : IsEssentialMono j) : IsEssentialMono (i ≫ j)
```

**`Module.isEssentialMono_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L155). The attribute's comment: “essential_extension_intersection”.

> The intersection of an essential subobject with another subobject is essential in that
> subobject.

```lean
theorem isEssentialMono_pullback {B : 𝒜} (A C : Subobject B) (hA : IsEssentialMono A.arrow) :
    IsEssentialMono ((Subobject.pullback C.arrow).obj A).arrow
```

**`Module.essentialEpi_epiDesc_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L258). The attribute's comment: “essential_surjection_quotient”.

> The quotient of an essential epimorphism by the image of the kernel of an epimorphism
> with the same source remains an essential epimorphism.

```lean
theorem essentialEpi_epiDesc_cokernel (hf : IsEssentialEpi f) :
    IsEssentialEpi
      (Abelian.epiDesc q (f ≫ cokernel.π (kernel.ι q ≫ f))
        (by simpa only [Category.assoc] using
          (cokernel.condition (kernel.ι q ≫ f))))
```

## Tag 08XL, a lemma

[Tag 08XL](https://stacks.math.columbia.edu/tag/08XL) in the Stacks Project.

**`Module.isEssentialMono_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L375).

> A compatible filtered system of essential embeddings of a module induces an essential
> embedding into its colimit.

```lean
theorem isEssentialMono_colimit {R : Type u} [Ring R]
    {J : Type v} [SmallCategory J] [IsFiltered J]
    (M : ModuleCat.{max v w u, u} R)
    (E : Functor J (ModuleCat.{max v w u, u} R)) [HasColimit E]
    (ι : (Functor.const J).obj M ⟶ E)
    (hι : ∀ j, ∃ h : Mono (ι.app j),
      let _ : Mono (ι.app j) := h
      IsEssentialMono (ι.app j))
    (j : J) :
    ∃ h : Mono (ι.app j ≫ colimit.ι E j),
      let _ : Mono (ι.app j ≫ colimit.ι E j) := h
      IsEssentialMono (ι.app j ≫ colimit.ι E j)
```

## Tag 08XM, a lemma

[Tag 08XM](https://stacks.math.columbia.edu/tag/08XM) in the Stacks Project.

**`Module.isEssentialMono_subtype_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Essential.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Essential.lean#L232).

> A submodule inclusion is essential if and only if every nonzero element of the ambient
> module has a nonzero scalar multiple lying in the submodule.

```lean
theorem isEssentialMono_subtype_iff {R : Type u} [Ring R]
    {N : ModuleCat.{v} R} (M : Submodule R N) :
    IsEssentialMono (ModuleCat.ofHom M.subtype) ↔
      ∀ x : N, x ≠ 0 → ∃ f : R, (f • x ∈ M ∧ f • x ≠ 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.2, Tag 08XI](https://stacks.math.columbia.edu/tag/08XI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
