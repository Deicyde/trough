---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedAlgebra.Hom, SheafOfModules.DifferentialGradedAlgebra.op, SheafOfModules.DifferentialGradedAlgebra, SheafOfModules.DifferentialGradedAlgebra.pushforwardDifferentialGradedAlgebra, SheafOfModules.DifferentialGradedAlgebra.pullbackDifferentialGradedAlgebra, SheafOfModules.DifferentialGradedAlgebra.differentialGradedAlgebraAdjunction, AlgebraicGeometry.RingedSite.Hom.dgaPushforward, AlgebraicGeometry.RingedSite.Hom.dgaPullback
statement: formalized
proof: formalized
---

# 24.12 Sheaves of differential graded algebras

Section 24.12 of the Stacks Project, [Tag 0FRE](https://stacks.math.columbia.edu/tag/0FRE). 2 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRF, a definition

[Tag 0FRF](https://stacks.math.columbia.edu/tag/0FRF) in the Stacks Project.

**`SheafOfModules.DifferentialGradedAlgebra.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraHom.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraHom.lean#L55). The attribute's comment: “homomorphisms of differential graded algebras”.

> A homomorphism of sheaves of differential graded algebras: a morphism of the underlying
> cochain complexes which respects the graded multiplication.

```lean
structure Hom (A B : DifferentialGradedAlgebra.{t, a} R)
```

**`SheafOfModules.DifferentialGradedAlgebra.op`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeAlgebra.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeAlgebra.lean#L260). The attribute's comment: “the opposite of a sheaf of differential graded algebras”.

> **The opposite sheaf of differential graded algebras.** The underlying complex and the unit
> are those of `A`, and the multiplication interchanges its variables and twists by the Koszul
> sign.

```lean
noncomputable def op : DifferentialGradedAlgebra.{t, a} R
```

**`SheafOfModules.DifferentialGradedAlgebra`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetColimits.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetColimits.lean#L221). The attribute's comment: “sheaves of differential graded algebras”.

> A sheaf of differential graded algebras over a sheaf of rings on a site.

```lean
structure DifferentialGradedAlgebra (R : Sheaf J RingCat.{t})
```

## Tag 0FRG, a remark

[Tag 0FRG](https://stacks.math.columbia.edu/tag/0FRG) in the Stacks Project.

**`SheafOfModules.DifferentialGradedAlgebra.pushforwardDifferentialGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraFunctoriality.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraFunctoriality.lean#L525). The attribute's comment: “part (1): pushforward”.

> **An additive lax monoidal functor between categories of sheaves of modules induces a
> functor between the categories of sheaves of differential graded algebras.** This is part (1)
> of the functoriality of sheaves of differential graded algebras: for a morphism of ringed topoi
> `(f, f♯)` and `F = f_*` — lax monoidal because it is right adjoint to the strong monoidal
> pullback, and additive because it is a right adjoint between abelian categories — it is the
> pushforward `A ↦ (f_*A, f_*d)`.

```lean
noncomputable def pushforwardDifferentialGradedAlgebra :
    DifferentialGradedAlgebra.{w, w} (toRingCat J Osharp) ⥤
      DifferentialGradedAlgebra.{w, w} (toRingCat K Psharp)
```

**`SheafOfModules.DifferentialGradedAlgebra.pullbackDifferentialGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraFunctoriality.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraFunctoriality.lean#L583). The attribute's comment: “part (2): pullback”.

> **An additive strong monoidal functor between categories of sheaves of modules induces a
> functor between the categories of sheaves of differential graded algebras.** This is part (2)
> of the functoriality of sheaves of differential graded algebras: for a morphism of ringed topoi
> `(f, f♯)` and `L = f^*` — strong monoidal for the tensor product of Tag 01CA, and additive
> because it is a left adjoint between abelian categories — it is the pullback
> `B ↦ (f^*B, f^*d)`.

```lean
noncomputable def pullbackDifferentialGradedAlgebra :
    DifferentialGradedAlgebra.{w, w} (toRingCat K Psharp) ⥤
      DifferentialGradedAlgebra.{w, w} (toRingCat J Osharp)
```

**`SheafOfModules.DifferentialGradedAlgebra.differentialGradedAlgebraAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraFunctoriality.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraFunctoriality.lean#L710). The attribute's comment: “part (3): adjunction”.

> **Pullback of sheaves of differential graded algebras is left adjoint to pushforward.**
> This is part (3) of the functoriality of sheaves of differential graded algebras: for a morphism
> of ringed topoi `(f, f♯)`, homomorphisms `f^*B ⟶ A` correspond to homomorphisms `B ⟶ f_*A`,
> naturally in both arguments. The two functors are the constructions of parts (1) and (2), not
> functors merely asserted to exist.

```lean
noncomputable def differentialGradedAlgebraAdjunction :
    pullbackDifferentialGradedAlgebra L hP hO ⊣ pushforwardDifferentialGradedAlgebra G hO hP
```

**`AlgebraicGeometry.RingedSite.Hom.dgaPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean#L256). The attribute's comment: “part (1) at a morphism of ringed sites: `(f_*A, f_*d)`, functorially”.

> **The direct image of a sheaf of differential graded algebras along a morphism of ringed
> sites.** Its underlying sheaf of graded algebras is the direct image of that of `A` and its
> differential is `f_*d`; this is part (1) of the functoriality of sheaves of differential graded
> algebras.

```lean
noncomputable def dgaPushforward :
    SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat X.J X.O) ⥤
      SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat Y.J Y.O)
```

**`AlgebraicGeometry.RingedSite.Hom.dgaPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean#L266). The attribute's comment: “part (2) at a morphism of ringed sites: `(f^*B, f^*d)`, functorially”.

> **The inverse image of a sheaf of differential graded algebras along a morphism of ringed
> sites.** Its underlying sheaf of graded algebras is the inverse image of that of `B` and its
> differential is `f^*d`; this is part (2) of the functoriality of sheaves of differential graded
> algebras.

```lean
noncomputable def dgaPullback :
    SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat Y.J Y.O) ⥤
      SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat X.J X.O)
```

**`AlgebraicGeometry.RingedSite.Hom.dgaPushforward_obj_complex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean#L295). The attribute's comment: “part (1) at a morphism of ringed sites: `(f_*A, f_*d)`, functorially”.

> **The differential of `f_*A` is `f_*d`**: its cochain complex is the direct image of the
> cochain complex of `A` degreewise.

```lean
theorem dgaPushforward_obj_complex
    (A : SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat X.J X.O)) :
    ((dgaPushforward f hY hX).obj A).complex =
      ((SheafOfModules.pushforward.{u} (Stacks.DifferentialGradedInverseImage.inverseImageRingHom
            (structureMapPresheaf f) hY hX)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        A.complex
```

**`AlgebraicGeometry.RingedSite.Hom.dgaPullback_obj_complex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean#L306). The attribute's comment: “part (2) at a morphism of ringed sites: `(f^*B, f^*d)`, functorially”.

> **The differential of `f^*B` is `f^*d`**: its cochain complex is the inverse image of the
> cochain complex of `B` degreewise.

```lean
theorem dgaPullback_obj_complex
    (B : SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat Y.J Y.O)) :
    ((dgaPullback f hY hX).obj B).complex =
      ((Stacks.DifferentialGradedInverseImage.inverseImageModules
          (structureMapPresheaf f) hY hX).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        B.complex
```

**`AlgebraicGeometry.RingedSite.Hom.dgaPushforward_obj_toGradedAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean#L318). The attribute's comment: “part (1) at a morphism of ringed sites: `(f_*A, f_*d)`, functorially”.

> **The underlying sheaf of graded algebras of `f_*A` is the direct image of that of `A`**, in
> the sense of the functoriality of sheaves of graded algebras: so `f_*A` really is the sheaf of
> graded algebras of that remark, equipped with the differential `f_*d`.

```lean
theorem dgaPushforward_obj_toGradedAlgebra
    (A : SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat X.J X.O)) :
    ((dgaPushforward f hY hX).obj A).toGradedAlgebra =
      SheafOfModules.GradedAlgebra.transport
        (SheafOfModules.pushforward.{u} (Stacks.DifferentialGradedInverseImage.inverseImageRingHom
          (structureMapPresheaf f) hY hX)) A.toGradedAlgebra hX hY
```

**`AlgebraicGeometry.RingedSite.Hom.dgaPullback_obj_toGradedAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean#L330). The attribute's comment: “part (2) at a morphism of ringed sites: `(f^*B, f^*d)`, functorially”.

> **The underlying sheaf of graded algebras of `f^*B` is the inverse image of that of `B`**, in
> the sense of the functoriality of sheaves of graded algebras: so `f^*B` really is the sheaf of
> graded algebras of that remark, equipped with the differential `f^*d`.

```lean
theorem dgaPullback_obj_toGradedAlgebra
    (B : SheafOfModules.DifferentialGradedAlgebra.{u, u} (Sheaf.toRingCat Y.J Y.O)) :
    ((dgaPullback f hY hX).obj B).toGradedAlgebra =
      SheafOfModules.GradedAlgebra.transport
        (Stacks.DifferentialGradedInverseImage.inverseImageModules
          (structureMapPresheaf f) hY hX) B.toGradedAlgebra hY hX
```

**`AlgebraicGeometry.RingedSite.Hom.dgaAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAlgebraRingedSite.lean#L342). The attribute's comment: “part (3) at a morphism of ringed sites: `(f^*B ⟶ A) ≃ (B ⟶ f_*A)`”.

> **The inverse image of sheaves of differential graded algebras along a morphism of ringed
> sites is left adjoint to the direct image.** This is part (3) of the functoriality of sheaves of
> differential graded algebras, its two functors being those of parts (2) and (1).

```lean
noncomputable def dgaAdjunction : dgaPullback f hY hX ⊣ dgaPushforward f hY hX
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.12, Tag 0FRE](https://stacks.math.columbia.edu/tag/0FRE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
