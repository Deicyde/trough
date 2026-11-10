---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.tensorWithComplexDG, AlgebraicGeometry.RingedSite.tensorWithComplexDG_regular, AlgebraicGeometry.RingedSite.tensorWithComplexDG_preservesCoproducts, AlgebraicGeometry.RingedSite.tensorWithComplexToDerivedCategory_negMor₃_distinguished, AlgebraicGeometry.RingedSite.tensorWithComplexHomotopy, AlgebraicGeometry.RingedSite.tensorWithComplexHomotopy_spec, AlgebraicGeometry.RingedSite.tensorWithComplexHomotopy_isTriangulated, AlgebraicGeometry.RingedSite.tensorWithComplexToDerivedCategory_isLeftDerivable
statement: formalized
proof: formalized
---

# 22.35 Variant of derived tensor product

Section 22.35 of the Stacks Project, [Tag 09LU](https://stacks.math.columbia.edu/tag/09LU). 6 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09LV, a lemma

[Tag 09LV](https://stacks.math.columbia.edu/tag/09LV) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.tensorWithComplexDG`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplex/TensorHomAdjunction.lean, line 998](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplex/TensorHomAdjunction.lean#L998). The attribute's comment: “the differential graded tensor functor”.

> Tensoring with `K`, as the DG left adjoint to the representable DG functor
> `Hom(K, -)`.

```lean
public noncomputable def tensorWithComplexDG
    (K : CochainComplex (ModO.{u, v, w, t} X) ℤ) : TensorWithComplexData.{u, v, w, t, s, o} X R K
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDG_regular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplex/TensorHomAdjunction.lean, line 1039](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplex/TensorHomAdjunction.lean#L1039). The attribute's comment: “the image of the regular module”.

> Tensoring the regular endomorphism module with `K` returns `K`.

```lean
public noncomputable def tensorWithComplexDG_regular
    (K : CochainComplex (ModO.{u, v, w, t} X) ℤ) :
    letI : Category (CompDG.{u, v, w, t, s, o} X R).Obj := (CompDG.{u, v, w, t, s, o} X
      R).instCategoryComp
    (((tensorWithComplexDG.{u, v, w, t, s, o} X R K).functor.obj
      ((Rep.{u, v, w, t, s, o} X R K).functor.obj (liftComplex.{u, v, w, t, s} X K)) :
        (CompDG.{u, v, w, t, s, o} X R).Comp) ≅
      (liftComplex.{u, v, w, t, s} X K : (CompDG.{u, v, w, t, s, o} X R).Comp))
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDG_preservesCoproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplex/TensorHomAdjunction.lean, line 1066](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplex/TensorHomAdjunction.lean#L1066). The attribute's comment: “preservation of direct sums”.

> Tensoring with `K` commutes with all small direct sums.

```lean
public theorem tensorWithComplexDG_preservesCoproducts
    (K : CochainComplex (ModO.{u, v, w, t} X) ℤ) (I : Type i) :
    PreservesColimitsOfShape (Discrete I)
      (tensorWithComplexDG.{u, v, w, t, s, o} X R K).functor.onComp
```

## Tag 09LW, a lemma

[Tag 09LW](https://stacks.math.columbia.edu/tag/09LW) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.tensorWithComplexToDerivedCategory_negMor₃_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexConeExactness.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexConeExactness.lean#L50). The attribute's comment: “exactness against the cone triangles, up to the sign of the third arrow”.

> The image in `D(O)` of a triangle isomorphic to a cone triangle of `K(Mod_(E, d))` is
> distinguished once its third arrow is negated: that negation turns a cone triangle into the
> triangle of an admissible short exact sequence, which tensoring with `K` keeps distinguished.

```lean
theorem tensorWithComplexToDerivedCategory_negMor₃_distinguished
    (T : Triangle (DifferentialGradedModule.HomotopyCategory.{0, max u v w t s, max u v w t s}
      (Rep.{u, v, w, t, s, 0} X ℤ K).algebra))
    (hT : T ∈ distinguishedConeTriangles.{0, max u v w t s, max u v w t s}
      (A := (Rep.{u, v, w, t, s, 0} X ℤ K).algebra)) :
    (tensorWithComplexToDerivedCategory.{u, v, w, t, s, 0} X ℤ K).mapTriangle.obj
        (Triangle.mk T.mor₁ T.mor₂ (-T.mor₃)) ∈
      distTriang (DerivedCategory (TensorModO.{u, v, w, t, s} X))
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexHomotopy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexHomotopy.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexHomotopy.lean#L102). The attribute's comment: “the induced functor on homotopy categories”.

> **Stacks 09LW.** The functor `K(Mod_(E, d)) ⥤ K(O)` induced on homotopy categories by
> tensoring differential graded modules over the endomorphism differential graded algebra of `K`
> with `K`.

```lean
public noncomputable def tensorWithComplexHomotopy
    (K : CochainComplex (ModO.{u, v, w, t} X) ℤ) :
    DifferentialGradedModule.HomotopyCategory (Rep.{u, v, w, t, s, o} X R K).algebra ⥤
      _root_.HomotopyCategory (TensorModO.{u, v, w, t, s} X) (ComplexShape.up ℤ)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexHomotopy_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexHomotopy.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexHomotopy.lean#L118). The attribute's comment: “compatibility with the differential graded functor”.

> The induced functor on homotopy categories is the lift, along the two quotient functors, of
> the ordinary functor on complexes attached to the differential graded tensor functor.

```lean
public theorem tensorWithComplexHomotopy_spec
    (K : CochainComplex (ModO.{u, v, w, t} X) ℤ) :
    DifferentialGradedModule.toHomotopyCategory (Rep.{u, v, w, t, s, o} X R K).algebra ⋙
        tensorWithComplexHomotopy.{u, v, w, t, s, o} X R K =
      DifferentialGradedModule.dgFunctorToComplexes
          (tensorWithComplexDG.{u, v, w, t, s, o} X R K).functor ⋙
        HomotopyCategory.quotient (TensorModO.{u, v, w, t, s} X) (ComplexShape.up ℤ)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexHomotopy_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexHomotopy.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexHomotopy.lean#L154). The attribute's comment: “exactness of the induced functor”.

> **Stacks 09LW.** Tensoring with `K` is an exact functor of triangulated categories
> `K(Mod_(E, d)) ⥤ K(O)`: it commutes with the translation and carries distinguished triangles to
> distinguished triangles.

```lean
public theorem tensorWithComplexHomotopy_isTriangulated
    (K : CochainComplex (ModO.{u, v, w, t} X) ℤ) :
    (tensorWithComplexHomotopy.{u, v, w, t, s, o} X R K).IsTriangulated
```

## Tag 09LX, a lemma

[Tag 09LX](https://stacks.math.columbia.edu/tag/09LX) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.tensorWithComplexToDerivedCategory_isLeftDerivable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean#L146). The attribute's comment: “existence in the pro-object sense”.

> **Stacks 09LX**, in the source's own sense. The left derived functor of tensoring with `K`,
> followed by localization of the target, is defined at every object of `K(Mod_(E, d))`: the
> pro-object of its values along the quasi-isomorphisms into an object is essentially constant.

```lean
theorem tensorWithComplexToDerivedCategory_isLeftDerivable :
    (tensorWithComplexToDerivedCategory.{u, v, w, t, s, o} X R K).IsLeftDerivable
      (quasiIsomorphisms (Rep.{u, v, w, t, s, o} X R K).algebra)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexToDerivedCategory_hasLeftDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean#L159). The attribute's comment: “existence of the total left derived functor”.

> **Stacks 09LX**, in the Kan extension sense. Tensoring with `K`, followed by localization of
> the target, has a total left derived functor on `D(E, d)`.

```lean
theorem tensorWithComplexToDerivedCategory_hasLeftDerivedFunctor :
    (tensorWithComplexToDerivedCategory.{u, v, w, t, s, o} X R K).HasLeftDerivedFunctor
      (quasiIsomorphisms (Rep.{u, v, w, t, s, o} X R K).algebra)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean#L170). The attribute's comment: “the derived tensor functor”.

> **Stacks 09LX.** The derived tensor product `- ⊗_E^𝐋 K : D(E, d) ⥤ D(O)`: the total left
> derived functor of tensoring with `K` followed by localization of the target.

```lean
def tensorWithComplexDerived :
    DifferentialGradedModule.derivedCategory (Rep.{u, v, w, t, s, o} X R K).algebra ⥤
      DerivedCategory (TensorModO.{u, v, w, t, s} X)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerived_isLeftDerivedFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean#L192). The attribute's comment: “universal property”.

> The universal property of **Stacks 09LX**: the comparison exhibits `- ⊗_E^𝐋 K` as the left
> derived functor of tensoring with `K` followed by localization of the target.

```lean
instance tensorWithComplexDerived_isLeftDerivedFunctor :
    (tensorWithComplexDerived.{u, v, w, t, s, o} X R K).IsLeftDerivedFunctor
      (tensorWithComplexDerivedCounit.{u, v, w, t, s, o} X R K)
      (quasiIsomorphisms (Rep.{u, v, w, t, s, o} X R K).algebra)
```

## Tag 0CS6, a lemma

[Tag 0CS6](https://stacks.math.columbia.edu/tag/0CS6) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerivedExtMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean#L343). The attribute's comment: “the induced maps on Ext”.

> **Stacks 0CS6.** *The maps
> `Ext^n_{D(E, d)}(M, N) → Ext^n_{D(𝒪)}(M ⊗_E^𝐋 K^•, N ⊗_E^𝐋 K^•)` induced by the functor
> `- ⊗_E^𝐋 K^•`.* With `Ext^n_{D(C)}(X, Y) = Hom_{D(C)}(X, Y[n])`, the map induced by a functor
> is its action on morphisms followed by its commutation with the translation, here that of
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedCommShift`.

```lean
def tensorWithComplexDerivedExtMap
    {M N : DifferentialGradedModule.derivedCategory (Rep.{u, v, w, t, s, o} X R K).algebra} (n : ℤ)
    (f : M ⟶ N⟦n⟧) :
    (tensorWithComplexDerived.{u, v, w, t, s, o} X R K).obj M ⟶
      ((tensorWithComplexDerived.{u, v, w, t, s, o} X R K).obj N)⟦n⟧
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerivedExtMap_q`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerived.lean#L378). The attribute's comment: “the maps on Ext are those induced by tensoring with K”.

> **Stacks 0CS6, the maps on `Ext` are those induced by tensoring with `K`.** On a class coming
> from `K(Mod_(E, d))`, the map induced by `- ⊗_E^𝐋 K` agrees, through the comparison
> `- ⊗_E^𝐋 K → - ⊗_E K` of Tag 09LX, with the map induced by the differential graded tensor
> functor of Tag 09LV read on homotopy categories. This is the compatibility of that comparison
> with the translation.

```lean
theorem tensorWithComplexDerivedExtMap_q
    {P Y : DifferentialGradedModule.HomotopyCategory.{o, max u v w t s, max u v w t s}
      (Rep.{u, v, w, t, s, o} X R K).algebra} (n : ℤ) (f : P ⟶ Y⟦n⟧) :
    (tensorWithComplexDerivedCounit.{u, v, w, t, s, o} X R K).app P ≫
        tensorWithComplexToDerivedCategoryExtMap.{u, v, w, t, s, o} X R K n f =
      tensorWithComplexDerivedExtMap.{u, v, w, t, s, o} X R K n
          ((quasiIsomorphisms (Rep.{u, v, w, t, s, o} X R K).algebra).Q.map f ≫
            (((quasiIsomorphisms (Rep.{u, v, w, t, s, o} X R K).algebra).Q).commShiftIso n).hom.app
              Y) ≫
        ((tensorWithComplexDerivedCounit.{u, v, w, t, s, o} X R K).app Y)⟦n⟧'
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomSourceExtEquivOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedExtClauseOver.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedExtClauseOver.lean#L230). The attribute's comment: “the source of the canonical map in D(R) is RHom(M, N), read on cohomology, for every M, N in D(E, d)”.

> **Stacks 0CS6, the source of the canonical map in `D(R)`**, read on cohomology and *for
> every* `M`, `N` *in* `D(E, d)`. The degree-`n` cohomology of the source of
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapDerivedModulesOver` is the
> `Ext`-group
>
> `Ext^n_{D(E, d)}(M, N) = Hom_{D(E, d)}(M, N[n])`,
>
> so that source really is `RHom(M, N)` read on cohomology. It is
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomSourceExtEquiv` read through
> `AlgebraicGeometry.RingedSite.homologyForgetEquiv` and
> `AlgebraicGeometry.RingedSite.dgHomComplexModulesDerivedForgetIso`, which say that forgetting the
> `R`-action changes neither the cohomology group nor the complex it is taken of. There is no
> hypothesis on `M` or `N`.

```lean
def tensorWithComplexDerivedHomSourceExtEquivOver
    (M N : DifferentialGradedModule.derivedCategory (Rep.{u, u, u, u, u, o} X R K).algebra)
    (n : ℤ) :
    ↥((DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).obj
        (DerivedCategory.Q.obj ((DifferentialGradedModule.dgCategory.{_, _, u}
            (Rep.{u, u, u, u, u, o} X R K).algebra).homComplexModules
          (DifferentialGradedModule.propertyPModel.{o, u, 0}
            (Rep.{u, u, u, u, u, o} X R K).algebra M)
          (DifferentialGradedModule.propertyPModel.{o, u, 0}
            (Rep.{u, u, u, u, u, o} X R K).algebra N)))) ≃+ (M ⟶ N⟦n⟧)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomTargetExtEquivOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedExtClauseOver.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedExtClauseOver.lean#L263). The attribute's comment: “the target of the canonical map in D(R) read on cohomology: its degree-n cohomology is Ext^n_{D(O)}(M ⊗_E^𝐋 K, N ⊗_E^𝐋 K), for every M, N in D(E, d)”.

> **Stacks 0CS6, the target of the canonical map in `D(R)`**, read on cohomology and *for
> every* `M`, `N` *in* `D(E, d)`. The degree-`n` cohomology of the target of
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapDerivedModulesOver` is the
> `Ext`-group
>
> `Ext^n_{D(O)}(M ⊗_E^𝐋 K^•, N ⊗_E^𝐋 K^•) = Hom_{D(O)}(M ⊗_E^𝐋 K^•, (N ⊗_E^𝐋 K^•)[n])`.
>
> It is `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomTargetExtEquiv` read through
> `AlgebraicGeometry.RingedSite.homologyForgetEquiv` and
> `AlgebraicGeometry.RingedSite.globalDerivedHomForgetAppOver`. Together with
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomSourceExtEquivOver` it exhibits both
> cohomology modules of the clause as the `Ext`-groups the clause compares; that the *map* between
> them is the one induced by `- ⊗_E^𝐋 K^•` is
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapDerivedModulesOver_homology`.
>
> There is no hypothesis on `M` or `N`, and none on the site.

```lean
def tensorWithComplexDerivedHomTargetExtEquivOver
    (M N : DifferentialGradedModule.derivedCategory (Rep.{u, u, u, u, u, o} X R K).algebra)
    (n : ℤ) :
    ↥((DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).obj
        ((scalarRestriction X R).mapDerivedCategory.obj
          (((globalDerivedHomModules X).obj
              (op ((tensorWithComplexDerived.{u, u, u, u, u, o} X R K).obj M))).obj
            ((tensorWithComplexDerived.{u, u, u, u, u, o} X R K).obj N)))) ≃+
      ((tensorWithComplexDerived.{u, u, u, u, u, o} X R K).obj M ⟶
        ((tensorWithComplexDerived.{u, u, u, u, u, o} X R K).obj N)⟦n⟧)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapDerivedModulesOver_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedExtClauseOver.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedExtClauseOver.lean#L299). The attribute's comment: “H^n of the canonical map is the Ext map induced by - ⊗_E^𝐋 K, for every M, N in D(E, d) and every n, in the source's D(R)”.

> **Stacks 0CS6, the central clause, in the source's `D(R)`.** The degree-`n` cohomology of
> the canonical map
>
> `RHom(M, N) ⟶ RHom_O(M ⊗_E^𝐋 K^•, N ⊗_E^𝐋 K^•)`
>
> of `D(R)` is the map on `Ext` induced by the derived tensor product with `K`, for every `M`, `N`
> in `D(E, d)` and every `n`, with both sides read as the `Ext`-groups they are by
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomSourceExtEquivOver` and
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomTargetExtEquivOver`.
>
> There is no hypothesis on `M` or `N`: the statement is quantified over every object of
> `D(E, d)`, as the source's is, and the property-(P) reduction of the source's proof is performed
> by the choice of representative `DifferentialGradedModule.propertyPModel`. Nor is anything
> assumed about the site.
>
> This is `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapDerived_homology` read over
> the source's base ring: the canonical map in `D(R)` forgets to the `D(ℤ)`-valued one by
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapDerivedModulesOver_forget`, and
> forgetting the scalars changes neither the cohomology groups nor the map between them.

```lean
theorem tensorWithComplexDerivedHomMapDerivedModulesOver_homology
    (M N : DifferentialGradedModule.derivedCategory (Rep.{u, u, u, u, u, o} X R K).algebra)
    (n : ℤ)
    (η : ↥((DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).obj
      (DerivedCategory.Q.obj ((DifferentialGradedModule.dgCategory.{_, _, u}
          (Rep.{u, u, u, u, u, o} X R K).algebra).homComplexModules
        (DifferentialGradedModule.propertyPModel.{o, u, 0}
          (Rep.{u, u, u, u, u, o} X R K).algebra M)
        (DifferentialGradedModule.propertyPModel.{o, u, 0}
          (Rep.{u, u, u, u, u, o} X R K).algebra N))))) :
    tensorWithComplexDerivedHomTargetExtEquivOver X R K M N n
        (ModuleCat.Hom.hom ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).map
          (tensorWithComplexDerivedHomMapDerivedModulesOver X R K M N)) η) =
      tensorWithComplexDerivedExtMap.{u, u, u, u, u, o} X R K n
        (tensorWithComplexDerivedHomSourceExtEquivOver X R K M N n η)
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapModulesOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedHomModulesOver.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedHomModulesOver.lean#L213). The attribute's comment: “the canonical map out of the differential graded Hom complex, into RHom_O(M ⊗_E K, N ⊗_E K), in the source's D(R)”.

> **The canonical map in `D(R)`.** The differential graded functor of Tag 09LV acts on the
> `R`-module-valued differential graded Hom complexes, and the Hom complex of two complexes of
> `O`-modules over `R` maps canonically to their global derived hom of Tag 0B6E read over `R`
> (`AlgebraicGeometry.RingedSite.homComplexToGlobalDerivedHomModulesOver`); the composite is this
> morphism of `D(R)`.
>
> Its source is the differential graded Hom complex of two differential graded modules, and its
> target is the global derived hom of the ordinary tensor products.

```lean
def tensorWithComplexDerivedHomMapModulesOver
    (M N : (DifferentialGradedModule.dgCategory.{_, _, u}
      (Rep.{u, u, u, u, u, o} X R K).algebra).Obj) :
    DerivedCategory.Q.obj ((DifferentialGradedModule.dgCategory.{_, _, u}
        (Rep.{u, u, u, u, u, o} X R K).algebra).homComplexModules M N) ⟶
      (scalarRestriction X R).mapDerivedCategory.obj
        (((globalDerivedHomModules X).obj (op (DerivedCategory.Q.obj
              ((tensorWithComplexDG.{u, u, u, u, u, o} X R K).functor.obj M)))).obj
          (DerivedCategory.Q.obj
            ((tensorWithComplexDG.{u, u, u, u, u, o} X R K).functor.obj N)))
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapDerivedModulesOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedHomModulesOver.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedHomModulesOver.lean#L330). The attribute's comment: “the canonical map RHom(M, N) ⟶ RHom_O(M ⊗_E^𝐋 K, N ⊗_E^𝐋 K) in the source's D(R), for every M, N in D(E, d)”.

> **The canonical map `RHom(M, N) ⟶ RHom_O(M ⊗_E^𝐋 K^•, N ⊗_E^𝐋 K^•)` in `D(R)`**, *for every*
> `M`, `N` *in* `D(E, d)`. The canonical map of
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedHomMapModulesOver`, taken at the chosen
> property-(P) representatives of `M` and `N`, is read into the global derived hom of the *derived*
> tensor products,
>
> `RHom(M, N) ⟶ RHom_O(M ⊗_E^𝐋 K^•, N ⊗_E^𝐋 K^•)`,
>
> by transporting both arguments along
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedRepIso`: in the contravariant argument the
> isomorphism is used as it stands, and in the covariant one it is inverted.
>
> There is no hypothesis on `M` or `N`.

```lean
def tensorWithComplexDerivedHomMapDerivedModulesOver
    (M N : DifferentialGradedModule.derivedCategory (Rep.{u, u, u, u, u, o} X R K).algebra) :
    DerivedCategory.Q.obj
        ((DifferentialGradedModule.dgCategory.{_, _, u}
            (Rep.{u, u, u, u, u, o} X R K).algebra).homComplexModules
          (DifferentialGradedModule.propertyPModel.{o, u, 0}
            (Rep.{u, u, u, u, u, o} X R K).algebra M)
          (DifferentialGradedModule.propertyPModel.{o, u, 0}
            (Rep.{u, u, u, u, u, o} X R K).algebra N)) ⟶
      (scalarRestriction X R).mapDerivedCategory.obj
        (((globalDerivedHomModules X).obj
            (op ((tensorWithComplexDerived.{u, u, u, u, u, o} X R K).obj M))).obj
          ((tensorWithComplexDerived.{u, u, u, u, u, o} X R K).obj N))
```

## Tag 09LY, a lemma

[Tag 09LY](https://stacks.math.columbia.edu/tag/09LY) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerived_adj_derivedHomWithComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedAdjunction.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedAdjunction.lean#L286).

> **The derived tensor--Hom adjunction**: the derived tensor product
> `- ⊗_E^𝐋 K^• : D(E, d) ⥤ D(O)` of Tag 09LX is left adjoint to derived Hom
> `RHom(K^•, -) : D(O) ⥤ D(E, d)`.

```lean
def tensorWithComplexDerived_adj_derivedHomWithComplex :
    tensorWithComplexDerived.{u, v, w, t, s, 0} X ℤ K ⊣
      derivedHomWithComplex.{u, v, w, t, s} X K
```

## Tag 09LZ, a lemma

[Tag 09LZ](https://stacks.math.columbia.edu/tag/09LZ) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.tensorWithComplexDerived_fullyFaithful_of_ext`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedFullyFaithfulDerivedHom.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexDerivedFullyFaithfulDerivedHom.lean#L192). The attribute's comment: “exactly the source's two hypotheses and nothing else: (1) is compactness of K in D(O), stated as such, and (2) is bijectivity of the functor on Hom(E, E[n]). The adjunction of Tag 09LY, the dévissage of Tag 0FQE, the direct sums and the weak generation of D(E, d), the commutation of RHom(K, -) with direct sums and the exactness of both functors (Tag 09LW, read through the sign-twisted identity of D(O)) are supplied by carriers of this library”.

> **Stacks 09LZ.** *"Let `(C, O)` be a ringed site. Let `K` be a complex of `O`-modules.
> Assume (1) `K` represents a compact object of `D(O)`, and (2)
> `E = Hom_{Comp^dg(O)}(K, K)` computes the ext groups of `K` in `D(O)`. Then the functor
> `- ⊗_E^𝐋 K : D(E, d) ⥤ D(O)` of Lemma 09LX is fully faithful."*
>
> The functor is the one Tag 09LX constructs,
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerived`, and the right adjoint through which the
> source's proof runs is the derived Hom `RHom(K, -)` of Tag 09LK, the adjunction between them
> being the unconditional
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerived_adj_derivedHomWithComplex` of Tag 09LY.
>
> The source's two hypotheses are its two hypotheses here: `hcompact` is (1), that `K` represents a
> compact object of `D(O)`, and `hExt` is (2), read as the bijectivity of the functor on the
> morphism groups `Hom_{D(E, d)}(E, E[n])`. The source's proof uses (1) only through the
> commutation of the right adjoint with direct sums, and that commutation is derived here rather
> than assumed: the regular module `E` is a compact weak generator of `D(E, d)` and
> `- ⊗_E^𝐋 K` sends it to `K`, so
> `CategoryTheory.Pretriangulated.preservesCoproducts_of_isCompactObject_map` applies.
>
> Exactness of neither functor is assumed. The exactness of `- ⊗_E^𝐋 K` in the pretriangulated
> structure in force on `D(E, d)` is false, by a sign; what holds, unconditionally, is the
> exactness of its composite with the sign-twisted identity of `D(O)`
> (`AlgebraicGeometry.RingedSite.tensorWithComplexDerived_signTwist_isTriangulated`), and the
> adjunction read between the twisted composites carries that to the right adjoint. Since
> `CategoryTheory.signTwist` is the identity on objects and on morphisms, the full faithfulness
> obtained is full faithfulness of `- ⊗_E^𝐋 K` itself. See the module's implementation notes.
>
> Everything else that
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerived_fullyFaithful` takes as an argument is
> supplied here — the adjunction of Tag 09LY and its commutation
> with the translation, the dévissage of Tag 0FQE, the direct sums of `D(E, d)` and the weak
> generation of `D(E, d)` by the regular module. See the module's implementation notes.
>
> Full faithfulness is data, a chosen inverse to the action on morphism groups, so this is a
> definition.

```lean
def tensorWithComplexDerived_fullyFaithful_of_ext
    (hcompact : IsCompactObject.{max u v w t s}
      (DerivedCategory.Q.obj (liftComplex.{u, v, w, t, s} X K)))
    (hExt : ∀ n : ℤ, Function.Bijective
      (fun f : repRegularDerived.{u, v, w, t, s} X K ⟶
          (repRegularDerived.{u, v, w, t, s} X K)⟦n⟧ =>
        (tensorWithComplexDerived.{u, v, w, t, s, 0} X ℤ K).map f)) :
    (tensorWithComplexDerived.{u, v, w, t, s, 0} X ℤ K).FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.35, Tag 09LU](https://stacks.math.columbia.edu/tag/09LU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
