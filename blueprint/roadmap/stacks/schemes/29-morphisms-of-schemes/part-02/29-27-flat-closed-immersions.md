---
declaration: section
origin: cited
lean: AlgebraicGeometry.support_bijOn_flat_closedImmersions, AlgebraicGeometry.existsUnique_lift_of_flat_closedImmersion, AlgebraicGeometry.IsOpenImmersion.of_flat_of_mono, AlgebraicGeometry.connectedComponentIdealSheaf, AlgebraicGeometry.Scheme.Modules.forall_isFiniteLocallyFree_iff_forall_isOpen
statement: formalized
proof: formalized
---

# 29.27 Flat closed immersions

Section 29.27 of the Stacks Project, [Tag 04PV](https://stacks.math.columbia.edu/tag/04PV). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04PW, a lemma

[Tag 04PW](https://stacks.math.columbia.edu/tag/04PW) in the Stacks Project.

**`AlgebraicGeometry.support_bijOn_flat_closedImmersions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/ClosedSubscheme.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/ClosedSubscheme.lean#L254). The attribute's comment: “bijection”.

> Taking the support is a bijection from the flat closed subschemes of a scheme to the closed
> subsets stable under generalization.

```lean
public theorem support_bijOn_flat_closedImmersions (X : Scheme.{u}) :
    Set.BijOn (fun I : X.IdealSheafData => I.support)
      {I : X.IdealSheafData | Flat I.subschemeι}
      {Z : Closeds X | StableUnderGeneralization (Z : Set X)}
```

**`AlgebraicGeometry.existsUnique_lift_of_flat_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/ClosedSubscheme.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/ClosedSubscheme.lean#L272). The attribute's comment: “factorization”. References: EGA I (4.1.8), “special case”.

> A morphism whose set-theoretic image lies in a flat closed subscheme factors uniquely
> through it.

```lean
public theorem existsUnique_lift_of_flat_closedImmersion {X Y : Scheme.{u}}
    (I : X.IdealSheafData) [Flat I.subschemeι] (g : Y ⟶ X)
    (hg : Set.range g ⊆ (I.support : Set X)) :
    ∃! h : Y ⟶ I.subscheme, h ≫ I.subschemeι = g
```

## Tag 0819, a lemma

[Tag 0819](https://stacks.math.columbia.edu/tag/0819) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsOpenImmersion.of_flat_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsOpenImmersion.of_flat_of_mono#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L328) (StacksFrontier): “only: f is an open immersion; Mathlib's form assumes flat, locally of finite presentation and mono (a closed immersion is mono). That its image is open and closed is not stated separately”. References: EGA IV (17.9.1), “(b) ⇒ (a)”; EGA IV (17.9.2), “partial”; SGA 1 I (5.1), “special case”; SGA 3 X (3.7), “partial”; SGA 3 XXII (5.4.10), “more general”.

## Tag 04PX, a definition

[Tag 04PX](https://stacks.math.columbia.edu/tag/04PX) in the Stacks Project.

**`AlgebraicGeometry.connectedComponentIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/ClosedSubscheme.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/ClosedSubscheme.lean#L292).

> The canonical closed subscheme structure on the connected component of a point `x` of a
> scheme `X`: the closed subscheme cut out by `connectedComponent x`, which is closed and stable
> under generalization. It is the unique closed subscheme structure on that component whose closed
> immersion into `X` is flat.

```lean
public noncomputable def connectedComponentIdealSheaf {X : Scheme.{u}} (x : X) :
    X.IdealSheafData
```

## Tag 053N, a lemma

[Tag 053N](https://stacks.math.columbia.edu/tag/053N) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.forall_isFiniteLocallyFree_iff_forall_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteFlatLocallyFree.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FiniteFlatLocallyFree.lean#L193).

> **Stacks Project, Tag 053N.** For a scheme `X` the following are equivalent: every
> quasi-coherent `𝒪_X`-module of finite type which is flat is finite locally free; every closed
> subset of `X` stable under generalization is open.

```lean
theorem forall_isFiniteLocallyFree_iff_forall_isOpen (X : Scheme.{u}) :
    (∀ F : X.Modules, _root_.SheafOfModules.IsFiniteType.{u, u, u} F → F.IsQuasicoherent →
        AlgebraicGeometry.SheafOfModules.IsFlat
            (C := TopologicalSpace.Opens X.toTopCat)
            (J := Opens.grothendieckTopology X.toTopCat) (O := X.sheaf) F →
          AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
            (R := X.ringCatSheaf) F) ↔
      ∀ Z : Set X, IsClosed Z → StableUnderGeneralization Z → IsOpen Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.27, Tag 04PV](https://stacks.math.columbia.edu/tag/04PV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
