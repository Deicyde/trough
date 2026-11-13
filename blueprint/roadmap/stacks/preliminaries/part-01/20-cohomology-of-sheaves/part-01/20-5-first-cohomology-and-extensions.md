---
declaration: section
origin: cited
lean: Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical, Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical_extClass, Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical_unique, Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical_naturality
statement: formalized
proof: formalized
---

# 20.5 First cohomology and extensions

Section 20.5 of the Stacks Project, [Tag 0B39](https://stacks.math.columbia.edu/tag/0B39). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B3A, a lemma

[Tag 0B3A](https://stacks.math.columbia.edu/tag/0B3A) in the Stacks Project.

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean#L115). The attribute's comment: “the canonical bijection, as an isomorphism of abelian groups”.

> **Stacks 0B3A.** For a ringed space `(X, O_X)` and a sheaf of `O_X`-modules `F`, the
> canonical bijection `Ext^1_{Mod(O_X)}(O_X, F) → H^1(X, F)`, an isomorphism of abelian groups.

```lean
def extOneEquivFirstCohomologyCanonical (M : SheafOfModules.{u} R) :
    Abelian.Ext (SheafOfModules.unit R) M 1 ≃+ Hgroup R ⊤ 1 M
```

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical_extClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean#L154). The attribute's comment: “image of an extension: the boundary of `1` in the long exact cohomology sequence”.

> **Stacks 0B3A.** The canonical bijection sends the class of the extension
> `0 → F → E → O_X → 0` to the image of `1 ∈ Γ(X, O_X)` under the boundary map
> `H^0(X, O_X) → H^1(X, F)` of the long exact cohomology sequence of the extension.

```lean
theorem extOneEquivFirstCohomologyCanonical_extClass (M E : SheafOfModules.{u} R) (f : M ⟶ E)
    (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
    (hS : (ShortComplex.mk f g w).ShortExact) :
    extOneEquivFirstCohomologyCanonical R M hS.extClass =
      (DerivedIndexing.rightDerivedDeltaFunctorOfEnoughInjectives (secF R ⊤)).δ hS 0
        (oneCohomologyClass R)
```

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean#L178). The attribute's comment: “uniqueness: the boundary formula determines the bijection”.

> **Stacks 0B3A.** The boundary formula determines the canonical bijection uniquely.

```lean
theorem extOneEquivFirstCohomologyCanonical_unique (M : SheafOfModules.{u} R)
    (e : Abelian.Ext (SheafOfModules.unit R) M 1 ≃+ Hgroup R ⊤ 1 M)
    (he : ∀ (E : SheafOfModules.{u} R) (f : M ⟶ E)
      (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
      (hS : (ShortComplex.mk f g w).ShortExact),
      e hS.extClass =
        (DerivedIndexing.rightDerivedDeltaFunctorOfEnoughInjectives (secF R ⊤)).δ hS 0
          (oneCohomologyClass R)) :
    e = extOneEquivFirstCohomologyCanonical R M
```

**`Stacks.Cohomology.SpaceModules.extOneEquivFirstCohomologyCanonical_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Extensions/ExtOneCanonicalBoundary.lean#L196). The attribute's comment: “naturality in the coefficient module sheaf”.

> **Stacks 0B3A.** The canonical bijection is natural in the coefficient module sheaf.

```lean
theorem extOneEquivFirstCohomologyCanonical_naturality {M N : SheafOfModules.{u} R}
    (f : M ⟶ N) (e : Abelian.Ext (SheafOfModules.unit R) M 1) :
    extOneEquivFirstCohomologyCanonical R N
        ((Abelian.Ext.mk₀ f).postcomp (SheafOfModules.unit R) (Nat.add_zero 1) e) =
      (Hfunctor R ⊤ 1).map f (extOneEquivFirstCohomologyCanonical R M e)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.5, Tag 0B39](https://stacks.math.columbia.edu/tag/0B39)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
