---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.globalDerivedHom, Stacks.SheafOfModules.globalDerivedHomDegreeZeroEquiv, Stacks.SheafOfModules.globalDerivedHomHomologyZeroEquiv, Stacks.SheafOfModules.globalDerivedHomHomologyEquiv, Stacks.SheafOfModules.globalDerivedHomPullbackMap
statement: formalized
proof: formalized
---

# 20.44 Global derived hom

Section 20.44 of the Stacks Project, [Tag 0B6A](https://stacks.math.columbia.edu/tag/0B6A). 1 tag here is carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B6A, the section

[Tag 0B6A](https://stacks.math.columbia.edu/tag/0B6A) in the Stacks Project.

**`Stacks.SheafOfModules.globalDerivedHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean#L52). The attribute's comment: “the global derived hom RHom\_X(K, L) = RΓ(X, RSheafHom(K, L)) in D(Γ(X, O\_X)) of a ringed space”.

> The global derived hom `RHom_X(K, L) = RΓ(X, RSheafHom(K, L))` of a ringed space: the derived
> internal Hom of two objects of `D(O_X)`, followed by derived global sections valued in modules over
> the ring `Γ(X, O_X)` of global sections of the structure sheaf.

```lean
def globalDerivedHom :
    (DerivedCategory (StructureSheafModules Rc))ᵒᵖ ⥤
      DerivedCategory (StructureSheafModules Rc) ⥤
        DerivedCategory (ModuleCat.{u} (GlobalSectionRing (structureSheaf Rc)))
```

**`Stacks.SheafOfModules.globalDerivedHomDegreeZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpace.lean#L69). The attribute's comment: “the degree-zero cohomology of RHom\_X(K, L) is Hom\_\{D(O\_X)}(K, L)”.

> The degree-zero cohomology of `RHom_X(K, L)`, read on its underlying complex of abelian groups,
> is the group of morphisms `K ⟶ L` in the derived category of `O_X`-modules.

```lean
def globalDerivedHomDegreeZeroEquiv (K L : DerivedCategory (StructureSheafModules Rc)) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((RingedSite.underlyingDerivedGroup (ringedSite Rc)).obj
          (((globalDerivedHom Rc).obj (op K)).obj L)) : Type u) ≃+ (K ⟶ L)
```

**`Stacks.SheafOfModules.globalDerivedHomHomologyZeroEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpaceDegrees.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpaceDegrees.lean#L70). The attribute's comment: “H^0(RHom\_X(K, L)) = Hom\_\{D(O\_X)}(K, L), for an arbitrary ringed space”.

> **The degree-zero cohomology of the global derived hom of a ringed space**, with no
> hypothesis: `H^0(RHom_X(K, L))`, read on its underlying complex of abelian groups, is the group
> of morphisms `K ⟶ L` in `D(O_X)`.

```lean
def globalDerivedHomHomologyZeroEquiv (K L : DerivedCategory (StructureSheafModules Rc)) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((RingedSite.underlyingDerivedGroup (ringedSite Rc)).obj
          (((globalDerivedHom Rc).obj (op K)).obj L)) : Type u) ≃+ (K ⟶ L)
```

**`Stacks.SheafOfModules.globalDerivedHomHomologyEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpaceDegrees.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpaceDegrees.lean#L81). The attribute's comment: “H^p(RHom\_X(K, L)) = Ext^p\_\{D(O\_X)}(K, L) = Hom\_\{D(O\_X)}(K, L[p]) for every p ∈ ℤ, for an arbitrary ringed space”.

> **The cohomology of the global derived hom of a ringed space in every degree**, with no
> hypothesis: for every integer `p`, `H^p(RHom_X(K, L))`, read on its underlying complex of abelian
> groups, is the group `Ext^p_{D(O_X)}(K, L) = Hom_{D(O_X)}(K, L[p])`.

```lean
def globalDerivedHomHomologyEquiv (K L : DerivedCategory (StructureSheafModules Rc)) (p : ℤ) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} p).obj
        ((RingedSite.underlyingDerivedGroup (ringedSite Rc)).obj
          (((globalDerivedHom Rc).obj (op K)).obj L)) : Type u) ≃+ (K ⟶ L⟦p⟧)
```

**`Stacks.SheafOfModules.globalDerivedHomPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpacePullback.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/GlobalDerivedHomOnASpacePullback.lean#L321). The attribute's comment: “the canonical map RHom\_X(K, L) → RHom\_Y(Lf^*K, Lf^*L) in D(Γ(X, O\_X)) of a morphism of ringed spaces f : Y → X, by global sections of the map of Remark 08I3”.

> **Stacks 0B6A, the canonical map `RHom_X(K, L) ⟶ RHom_Y(Lf^*K, Lf^*L)`** in `D(Γ(X, O_X))`
> for a morphism of ringed spaces `f : (Y, O_Y) ⟶ (X, O_X)` and objects `K`, `L` of `D(O_X)`; the
> target, an object of `D(Γ(Y, O_Y))`, is read in `D(Γ(X, O_X))` by restriction of scalars along
> the ring map `ringedSpaceGlobalSectionRingMap f : Γ(X, O_X) ⟶ Γ(Y, O_Y)`.
>
> It is obtained by taking global sections of the map
> `Lf^* RSheafHom(K, L) ⟶ RSheafHom(Lf^*K, Lf^*L)` of Stacks 08I3
> (`Stacks.Cohomology.DerivedInternalHomPullback.derivedPullbackSheafHomMap`), preceded by the
> canonical map `RΓ(X, N) ⟶ RΓ(Y, Lf^*N)` at `N = RSheafHom(K, L)`
> (`Stacks.Cohomology.DerivedSectionsPullback.sectionsPullback`: derived global sections of the unit
> of `Lf^* ⊣ Rf_*`, then `RΓ(X, Rf_* -) = RΓ(Y, -)`). Derived global sections are passed between
> the ringed site and the open `X` (resp. `Y`) of the space by `derivedGlobalSectionsTopIso`, and the
> scalars of `Γ(Y, O_Y)` are restricted to `Γ(X, O_X)` by
> `Stacks.Cohomology.DerivedSectionsPullback.changeScalarsIso`.

```lean
def globalDerivedHomPullbackMap
    (K L : DerivedCategory (StructureSheafModules X.sheaf)) :
    ((globalDerivedHom X.sheaf).obj (op K)).obj L ⟶
      (derivedRestrictScalars (ringedSpaceGlobalSectionRingMap f)).obj
        (((globalDerivedHom Y.sheaf).obj
            (op ((derivedPullback f).obj K))).obj ((derivedPullback f).obj L))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.44, Tag 0B6A](https://stacks.math.columbia.edu/tag/0B6A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
