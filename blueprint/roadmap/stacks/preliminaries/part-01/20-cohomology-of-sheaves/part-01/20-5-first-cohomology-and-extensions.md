---
declaration: section
origin: cited
lean: Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology, Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology_extClass, Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology_unique, Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology_naturality
statement: formalized
proof: formalized
---

# 20.5 First cohomology and extensions

Section 20.5 of the Stacks Project, [Tag 0B39](https://stacks.math.columbia.edu/tag/0B39). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B3A, a lemma

[Tag 0B3A](https://stacks.math.columbia.edu/tag/0B3A) in the Stacks Project.

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean#L179). The attribute's comment: “canonical bijection”.

> **Stacks 0B3A.** For a ringed space `(X, O_X)` and a sheaf of `O_X`-modules `F`, first
> extensions of the structure sheaf by `F` are canonically first cohomology.

```lean
def extOneEquivFirstCohomology (M : SheafOfModules.{u} R) :
    Abelian.Ext (SheafOfModules.unit R) M 1 ≃+ Hgroup R ⊤ 1 M
```

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology_extClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean#L194). The attribute's comment: “image of an extension”.

> **Stacks 0B3A.** The class of the extension `0 → F → E → O_X → 0` goes to the image of the
> unit global section `1 ∈ Γ(X, O_X)` under the connecting morphism of the extension.

```lean
theorem extOneEquivFirstCohomology_extClass (M E : SheafOfModules.{u} R) (f : M ⟶ E)
    (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
    (hS : (ShortComplex.mk f g w).ShortExact) :
    extOneEquivFirstCohomology R M hS.extClass =
      connectingMap R hS 0 (oneCohomologyClass R)
```

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean#L213). The attribute's comment: “uniqueness”.

> **Stacks 0B3A.** The connecting-image formula determines the identification uniquely.

```lean
theorem extOneEquivFirstCohomology_unique (M : SheafOfModules.{u} R)
    (e : Abelian.Ext (SheafOfModules.unit R) M 1 ≃+ Hgroup R ⊤ 1 M)
    (he : ∀ (E : SheafOfModules.{u} R) (f : M ⟶ E)
      (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
      (hS : (ShortComplex.mk f g w).ShortExact),
      e hS.extClass = connectingMap R hS 0 (oneCohomologyClass R)) :
    e = extOneEquivFirstCohomology R M
```

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomology_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/FirstCohomologyAndExtensions.lean#L229). The attribute's comment: “naturality”.

> **Stacks 0B3A.** The identification is natural in the coefficient module sheaf.

```lean
theorem extOneEquivFirstCohomology_naturality {M N : SheafOfModules.{u} R} (f : M ⟶ N)
    (e : Abelian.Ext (SheafOfModules.unit R) M 1) :
    extOneEquivFirstCohomology R N
        ((Abelian.Ext.mk₀ f).postcomp (SheafOfModules.unit R) (Nat.add_zero 1) e) =
      (Hfunctor R ⊤ 1).map f (extOneEquivFirstCohomology R M e)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.5, Tag 0B39](https://stacks.math.columbia.edu/tag/0B39)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
