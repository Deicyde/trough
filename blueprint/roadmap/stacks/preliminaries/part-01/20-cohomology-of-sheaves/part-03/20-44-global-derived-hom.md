---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.globalDerivedHom, Stacks.SheafOfModules.globalDerivedHomDegreeZeroEquiv
statement: formalized
proof: formalized
---

# 20.44 Global derived hom

Section 20.44 of the Stacks Project, [Tag 0B6A](https://stacks.math.columbia.edu/tag/0B6A). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B6A, the section

[Tag 0B6A](https://stacks.math.columbia.edu/tag/0B6A) in the Stacks Project.

**`Stacks.SheafOfModules.globalDerivedHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean#L52). The attribute's comment: “the global derived hom RHom_X(K, L) = RΓ(X, RSheafHom(K, L)) in D(Γ(X, O_X)) of a ringed space”.

> The global derived hom `RHom_X(K, L) = RΓ(X, RSheafHom(K, L))` of a ringed space: the derived
> internal Hom of two objects of `D(O_X)`, followed by derived global sections valued in modules over
> the ring `Γ(X, O_X)` of global sections of the structure sheaf.

```lean
def globalDerivedHom :
    (DerivedCategory (StructureSheafModules Rc))ᵒᵖ ⥤
      DerivedCategory (StructureSheafModules Rc) ⥤
        DerivedCategory (ModuleCat.{u} (GlobalSectionRing (structureSheaf Rc)))
```

**`Stacks.SheafOfModules.globalDerivedHomDegreeZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean#L69). The attribute's comment: “the degree-zero cohomology of RHom_X(K, L) is Hom_{D(O_X)}(K, L)”.

> The degree-zero cohomology of `RHom_X(K, L)`, read on its underlying complex of abelian groups,
> is the group of morphisms `K ⟶ L` in the derived category of `O_X`-modules.

```lean
def globalDerivedHomDegreeZeroEquiv (K L : DerivedCategory (StructureSheafModules Rc)) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((RingedSite.underlyingDerivedGroup (ringedSite Rc)).obj
          (((globalDerivedHom Rc).obj (op K)).obj L)) : Type u) ≃+ (K ⟶ L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.44, Tag 0B6A](https://stacks.math.columbia.edu/tag/0B6A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
