---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.globalDerivedHomModules, AlgebraicGeometry.RingedSite.globalDerivedHomModulesDegreeZeroEquiv, AlgebraicGeometry.RingedSite.globalDerivedHomDegreeEquiv, AlgebraicGeometry.RingedSite.globalDerivedHomModulesDegreeEquiv, AlgebraicGeometry.RingedSite.derivedStructureSheafGlobalSectionsDegreeEquiv
statement: formalized
proof: formalized
---

# 21.36 Global derived hom

Section 21.36 of the Stacks Project, [Tag 0B6E](https://stacks.math.columbia.edu/tag/0B6E). 1 tag here is carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B6E, the section

[Tag 0B6E](https://stacks.math.columbia.edu/tag/0B6E) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.globalDerivedHomModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHom.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHom.lean#L312). The attribute's comment: “the global derived hom RHom_O(K, L) = RΓ(C, RHom(K, L)) in D(Γ(C, O))”.

> **Stacks 0B6E.** *Applying the construction of the internal hom in the derived category we
> get the object* `RHom_O(K, L) = RΓ(C, RHom(K, L))` *in* `D(Γ(C, O))`: the derived internal Hom of
> two objects of `D(O)`, followed by derived global sections valued in modules over the ring of
> global sections of the structure sheaf.

```lean
def globalDerivedHomModules :
    (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))ᵒᵖ ⥤
      DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ⥤
        DerivedCategory
          (ModuleCat.{u} (GlobalSectionRing (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
```

**`AlgebraicGeometry.RingedSite.globalDerivedHomModulesDegreeZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHom.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHom.lean#L355). The attribute's comment: “the degree-zero cohomology of RHom_O(K, L) is Hom_{D(O)}(K, L)”.

> **Stacks 0B6E, the cohomology of the global derived hom.** The degree-zero cohomology of
> `RHom_O(K, L)` is the group of morphisms `K ⟶ L` in `D(O)`. This is Stacks 08JA, which is the
> statement the source cites for the cohomology modules of the global derived hom, transported to
> `RHom_O(K, L)` of `D(Γ(C, O))` along
> `AlgebraicGeometry.RingedSite.derivedGlobalSectionsModulesForget`; the cohomology is read on the
> underlying complex of abelian groups, as Stacks 08JA states it.

```lean
def globalDerivedHomModulesDegreeZeroEquiv
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((underlyingDerivedGroup X).obj
          (((globalDerivedHomModules X).obj (op K)).obj L)) : Type u) ≃+ (K ⟶ L)
```

**`AlgebraicGeometry.RingedSite.globalDerivedHomDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHomShift.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHomShift.lean#L186). The attribute's comment: “the degree-n cohomology of RHom_O(K, L) is Hom_{D(O)}(K, L[n])”.

> **Stacks 0B6E, the cohomology of the global derived hom in every degree.** The degree-`n`
> cohomology of `RHom_O(K, L)` is the group of morphisms `K ⟶ L[n]` in `D(O)`, that is the
> `Ext`-group `Ext^n_{D(O)}(K, L)`. This is the abelian-group-valued reading
> `AlgebraicGeometry.RingedSite.globalDerivedHom` of the global derived hom.
>
> The degree is moved into the covariant variable: the homology functors of the derived category
> form a shift sequence, derived global sections commute with the translation, and the derived
> internal Hom commutes with the translation in its covariant variable by
> `AlgebraicGeometry.RingedSite.derivedSheafHomTargetShiftIso`; in degree zero the cohomology is
> the morphism group by Stacks 08JA, which is
> `AlgebraicGeometry.RingedSite.derivedSheafHomGlobalSectionsEquiv`.

```lean
def globalDerivedHomDegreeEquiv
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (n : ℤ) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} n).obj
        (((globalDerivedHom X).obj (op K)).obj L) : Type u) ≃+ (K ⟶ L⟦n⟧)
```

**`AlgebraicGeometry.RingedSite.globalDerivedHomModulesDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHomShift.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHomShift.lean#L211). The attribute's comment: “the degree-n cohomology of RHom_O(K, L) in D(Γ(C, O)) is Hom_{D(O)}(K, L[n])”.

> **Stacks 0B6E, the cohomology of the global derived hom in every degree**, for the
> `D(Γ(C, O))`-valued global derived hom `AlgebraicGeometry.RingedSite.globalDerivedHomModules`:
> the degree-`n` cohomology of `RHom_O(K, L)`, read on the underlying complex of abelian groups as
> Stacks 08JA states it, is the group of morphisms `K ⟶ L[n]` of `D(O)`.
>
> This is `AlgebraicGeometry.RingedSite.globalDerivedHomDegreeEquiv` transported along
> `AlgebraicGeometry.RingedSite.derivedGlobalSectionsModulesForget`, and it is the degree-`n` form
> of `AlgebraicGeometry.RingedSite.globalDerivedHomModulesDegreeZeroEquiv`.

```lean
def globalDerivedHomModulesDegreeEquiv
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (n : ℤ) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} n).obj
        ((underlyingDerivedGroup X).obj
          (((globalDerivedHomModules X).obj (op K)).obj L)) : Type u) ≃+ (K ⟶ L⟦n⟧)
```

**`AlgebraicGeometry.RingedSite.derivedStructureSheafGlobalSectionsDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/StructureSheafHypercohomology.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/StructureSheafHypercohomology.lean#L72). The attribute's comment: “the case K = O[0], where RHom_O(O[0], Z) is RGamma(C, Z)”.

> **Hypercohomology in every degree is morphisms out of the structure sheaf.** For an object
> `Z` of `D(O)` the hypercohomology group `H^n(C, Z)`, the degree-`n` homology of unbounded derived
> global sections, is the group `Hom_{D(O)}(O[0], Z[n])`.
>
> This is Tag 08JA at source the structure sheaf in every degree: derived global sections of the
> identification `RSheafHom(O[0], Z) ≅ Z` of
> `AlgebraicGeometry.RingedSite.derivedStructureSheafHomIso` turn `H^n(C, Z)` into the degree-`n`
> cohomology of the global derived hom `RHom_O(O[0], Z)`, which is `Hom(O[0], Z[n])` by Tag 0B6E
> (`AlgebraicGeometry.RingedSite.globalDerivedHomDegreeEquiv`). In degree zero it is
> `AlgebraicGeometry.RingedSite.derivedStructureSheafGlobalSectionsEquiv`.

```lean
def derivedStructureSheafGlobalSectionsDegreeEquiv
    (Z : DerivedCategory (SheafOfModules.{u} (ringSheaf X.O))) (n : ℤ) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} n).obj
        ((derivedModuleGlobalSections X).obj Z) : Type u) ≃+
      (derivedStructureSheaf X ⟶ Z⟦n⟧)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.36, Tag 0B6E](https://stacks.math.columbia.edu/tag/0B6E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
