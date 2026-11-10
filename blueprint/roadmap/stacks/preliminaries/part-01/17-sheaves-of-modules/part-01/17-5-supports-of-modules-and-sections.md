---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpace.ModuleSheaf.supp, AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection, AlgebraicGeometry.RingedSpace.ModuleSheaf.isClosed_suppSection, AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection_smul_subset, AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection_add_subset, AlgebraicGeometry.RingedSpace.ModuleSheaf.mem_supp_iff, AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection_map_subset, isClosed_sheafRingSupport
statement: formalized
proof: formalized
---

# 17.5 Supports of modules and sections

Section 17.5 of the Stacks Project, [Tag 01AS](https://stacks.math.columbia.edu/tag/01AS). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01AT, a definition

[Tag 01AT](https://stacks.math.columbia.edu/tag/01AT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSpace.ModuleSheaf.supp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean#L101), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/Support.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Support.lean#L66) (StacksFrontier): “parts (1) and (2): sheaf support”.
- [`AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/Support.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Support.lean#L68) (StacksFrontier): “part (3): section support”.

## Tag 01AU, a lemma

[Tag 01AU](https://stacks.math.columbia.edu/tag/01AU) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.ModuleSheaf.isClosed_suppSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean#L130). The attribute's comment: “(1)”.

> The support of a section `s : F(U)` is closed in `U`, for the subspace topology on `U`.

```lean
theorem isClosed_suppSection (F : ModuleSheaf X) (U : Opens X.carrier)
    (s : F.toPresheaf.obj (Opposite.op U)) :
    IsClosed {x : U | (x : X.carrier) ∈ F.suppSection U s}
```

**`AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection_smul_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean#L155). The attribute's comment: “(2)”.

> For `f : O_X(U)` and `s : F(U)`, `Supp(f • s) ⊆ Supp(f) ∩ Supp(s)`.

```lean
theorem suppSection_smul_subset (F : ModuleSheaf X) (U : Opens X.carrier)
    (f : (X.presheafRing).obj (Opposite.op U)) (s : F.toPresheaf.obj (Opposite.op U)) :
    F.suppSection U (f • s) ⊆ X.suppRingSection U f ∩ F.suppSection U s
```

**`AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection_add_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean#L172). The attribute's comment: “(3)”.

> For `s s' : F(U)`, `Supp(s + s') ⊆ Supp(s) ∪ Supp(s')`.

```lean
theorem suppSection_add_subset (F : ModuleSheaf X) (U : Opens X.carrier)
    (s s' : F.toPresheaf.obj (Opposite.op U)) :
    F.suppSection U (s + s') ⊆ F.suppSection U s ∪ F.suppSection U s'
```

**`AlgebraicGeometry.RingedSpace.ModuleSheaf.mem_supp_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean#L187). The attribute's comment: “(4)”.

> A point `x` lies in `Supp(F)` if and only if there exist an open set `U` with `x ∈ U` and a
> section `s : F(U)` with `x ∈ Supp(s)`. Equivalently, `Supp(F)` is the union over all `(U, s)` of
> `Supp(s)`.

```lean
theorem mem_supp_iff (F : ModuleSheaf X) (x : X.carrier) :
    x ∈ F.supp ↔ ∃ (U : Opens X.carrier) (s : F.toPresheaf.obj (Opposite.op U)),
      x ∈ F.suppSection U s
```

**`AlgebraicGeometry.RingedSpace.ModuleSheaf.suppSection_map_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportSection.lean#L200). The attribute's comment: “(5)”.

> For a morphism `φ : F ⟶ G` of `O_X`-modules and `s : F(U)`, `Supp(φ(s)) ⊆ Supp(s)`.

```lean
theorem suppSection_map_subset (F G : ModuleSheaf X)
    (φ : PresheafOfModules.Hom F.toPresheaf G.toPresheaf) (U : Opens X.carrier)
    (s : F.toPresheaf.obj (Opposite.op U)) :
    G.suppSection U ((φ.app (Opposite.op U)) s) ⊆ F.suppSection U s
```

## Tag 01AV, a lemma

[Tag 01AV](https://stacks.math.columbia.edu/tag/01AV) in the Stacks Project.

**`isClosed_sheafRingSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/SupportStructureSheaf.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportStructureSheaf.lean#L81). References: EGA 0 (5.2.2), “special case”; EGA I (4.1.2), “more general”; EGA IV (19.1.7), “closed support of O_X/J”; SGA 3 VIA (2.1.3), “more general”.

> The support of a sheaf of commutative rings on `X` is a closed subset of `X`.

```lean
theorem isClosed_sheafRingSupport {X : TopCat} (F : TopCat.Sheaf CommRingCat X) :
    IsClosed (sheafRingSupport F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.5, Tag 01AS](https://stacks.math.columbia.edu/tag/01AS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
