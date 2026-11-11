---
declaration: section
origin: cited
lean: DifferentialGradedModule.homModuleFunctor, DifferentialGradedModule.homHomotopyCategoryFunctor_isTriangulated, DifferentialGradedModule.derivedHomData, DifferentialGraded.Bimodule.derivedPrecomp, DifferentialGraded.Bimodule.derivedPrecomp_comparison, DifferentialGraded.Bimodule.derivedPrecomp_isIso, DifferentialGradedModule.extIso, DifferentialGradedModule.extLinearEquiv_naturality
statement: formalized
proof: formalized
---

# 22.31 Derived Hom

Section 22.31 of the Stacks Project, [Tag 09LF](https://stacks.math.columbia.edu/tag/09LF). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09LG, an equation

[Tag 09LG](https://stacks.math.columbia.edu/tag/09LG) in the Stacks Project.

**`DifferentialGradedModule.homModuleFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomFunctor.lean#L477). The attribute's comment: “the induced functor `Mod_(B,d) → Mod_(A,d)`”.

> **Stacks 0FQQ.** The internal hom functor on the categories of differential graded
> modules.

```lean
noncomputable def homModuleFunctor :
    DifferentialGradedModule B ⥤ DifferentialGradedModule A
```

## Tag 09LH, a lemma

[Tag 09LH](https://stacks.math.columbia.edu/tag/09LH) in the Stacks Project.

**`DifferentialGradedModule.homHomotopyCategoryFunctor_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomCommShift.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomCommShift.lean#L577).

> **Stacks 09LH.** The internal hom functor out of a differential graded bimodule is an exact
> functor of the homotopy categories, for the commutation with the translation of Tag 0FQR.

```lean
instance homHomotopyCategoryFunctor_isTriangulated :
    (homHomotopyCategoryFunctor A B N L).IsTriangulated
```

## Tag 09LI, a lemma

[Tag 09LI](https://stacks.math.columbia.edu/tag/09LI) in the Stacks Project.

**`DifferentialGradedModule.derivedHomData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean#L223).

> **Stacks 09LI.** *The right derived functor of `F` exists; we denote it
> `RHom(N, -) : D(B, d) ⥤ D(A, d)`.* Here `F` is internal Hom out of the differential graded
> `(A, B)`-bimodule `N` read on homotopy categories and followed by localization
> (`DifferentialGradedModule.homToDerivedCategory`), and a right derived functor of it, with its
> comparison map and the everywhere-definedness of Tag 05SV, is exactly a
> `DifferentialGradedModule.DerivedHomData`; so the source's assertion that the derived functor
> exists is the construction of one such datum, which this is.
>
> It is `DifferentialGradedModule.DerivedHomData.ofPropertyIResolutions` — the Stacks proof, Tag
> 06XN applied to the modules with property (I), whose orthogonality to the acyclic modules is
> Tag 09KS — fed the existence of the resolutions, Tag 09KU
> (`DifferentialGradedModule.exists_propertyI_resolution`). Nothing is assumed.
>
> The functor is determined by this up to the canonical isomorphism
> `DifferentialGradedModule.DerivedHomData.functorIso`, so a consumer that only needs *some*
> `RHom(N, -)` should take an arbitrary datum rather than this one.

```lean
def derivedHomData (A B : DifferentialGradedAlgebra R) (N : DifferentialGradedModule B)
    (L : BimoduleStructure A B N) : DerivedHomData A B N L
```

## Tag 0BYV, a lemma

[Tag 0BYV](https://stacks.math.columbia.edu/tag/0BYV) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedPrecomp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomPrecomposition.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomPrecomposition.lean#L114). The attribute's comment: “the natural transformation”.

> Precomposition with a homomorphism `f : M ⟶ N` of differential graded `(A, B)`-bimodules
> induces a natural transformation `RHom(N, -) ⟹ RHom(M, -)` of derived Hom functors
> `D(B, d) ⥤ D(A, d)`.

```lean
def derivedPrecomp (f : M ⟶ N) : DN.functor ⟶ DM.functor
```

**`DifferentialGraded.Bimodule.derivedPrecomp_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomPrecomposition.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomPrecomposition.lean#L122). The attribute's comment: “compatibility with the comparison maps”.

> The derived transformation is compatible with the canonical comparison maps from ordinary
> internal hom to derived Hom.

```lean
theorem derivedPrecomp_comparison (f : M ⟶ N) :
    DN.comparison ≫
        Functor.whiskerLeft (quasiIsomorphisms' B).Q (derivedPrecomp DN DM f) =
      precompToDerivedNatTrans f ≫ DM.comparison
```

**`DifferentialGraded.Bimodule.derivedPrecomp_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomPrecompositionIso.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomPrecompositionIso.lean#L141). The attribute's comment: “quasi-isomorphisms induce natural isomorphisms”.

> **Stacks 0BYV**, the last assertion. If a homomorphism `f : M ⟶ N` of differential graded
> `(A, B)`-bimodules is a quasi-isomorphism of the underlying right differential graded
> `B`-modules, then the induced transformation `RHom(N, -) ⟹ RHom(M, -)` of derived Hom functors
> is an isomorphism.
>
> Nothing is assumed: `DN` and `DM` range over all right derived functors of internal Hom out of
> the two bimodules, of which the ones of Tag 09LI
> (`DifferentialGradedModule.derivedHomData`) are instances.

```lean
theorem derivedPrecomp_isIso
    (DN : DerivedHomData A B N.rightModule N.leftAction)
    (DM : DerivedHomData A B M.rightModule M.leftAction)
    (f : M ⟶ N) (hf : QuasiIso ((forgetToCochainComplex B).map f.rightHom)) :
    IsIso (derivedPrecomp DN DM f)
```

## Tag 0CS5, a lemma

[Tag 0CS5](https://stacks.math.columbia.edu/tag/0CS5) in the Stacks Project.

**`DifferentialGradedModule.extIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExtIso.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExtIso.lean#L161). The attribute's comment: “the identification of the cohomology of derived Hom with Ext”.

> Degree-`n` cohomology of derived Hom out of `N` is
> `Ext^n_{D(B,d)}(N, -) = Hom_{D(B,d)}(N, (-)[n])`, as functors on `D(B, d)`.

```lean
def extIso (D : DerivedHomData A B N L) (n : ℤ) :
    D.functor ⋙ extCohomologyFunctor A n ≅ extFunctor B N n
```

**`DifferentialGradedModule.extLinearEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExtIso.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExtIso.lean#L225). The attribute's comment: “the identification is natural in the target”.

> The identification `DifferentialGradedModule.extLinearEquiv` is natural in the target: a
> cohomology class of derived Hom pushed forward along `g` is sent to the `Ext`-class followed by
> the `n`-shift of `g`.

```lean
theorem extLinearEquiv_naturality (D : DerivedHomData A B N L) (n : ℤ)
    {M M' : derivedCategory' B} (g : M ⟶ M')
    (x : (degreeZeroCohomologyOnLocalization' A).obj ((D.functor.obj M)⟦n⟧)) :
    extLinearEquiv A B N L D n M'
        ((degreeZeroCohomologyOnLocalization' A).map ((D.functor.map g)⟦n⟧') x) =
      extLinearEquiv A B N L D n M x ≫ g⟦n⟧'
```

**`DifferentialGraded.Bimodule.extLinearEquiv_derivedPrecomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExtIsoPrecomp.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomExtIsoPrecomp.lean#L374). The attribute's comment: “the identification is natural in the bimodule, with respect to Tag 0BYV”.

> **Stacks 0CS5, the clause asserting compatibility with Tag 0BYV.** For a homomorphism
> `f : M ⟶ N` of differential graded `(A, B)`-bimodules, the identification of Tag 0CS5 carries the
> pullback along `f` of a degree-`n` cohomology class of derived Hom out of `N` — the transformation
> of Tag 0BYV, `DifferentialGraded.Bimodule.derivedPrecomp` — to the `Ext`-class of `N` composed
> with the image of `f` in `D(B, d)`.
>
> Together with `DifferentialGradedModule.extIso` and
> `DifferentialGradedModule.extLinearEquiv_naturality` this completes Tag 0CS5.

```lean
theorem extLinearEquiv_derivedPrecomp (DN : DerivedHomData A B N.rightModule N.leftAction)
    (DM : DerivedHomData A B M.rightModule M.leftAction) (f : M ⟶ N) (n : ℤ)
    (P : derivedCategory' B)
    (x : (degreeZeroCohomologyOnLocalization' A).obj ((DN.functor.obj P)⟦n⟧)) :
    extLinearEquiv A B M.rightModule M.leftAction DM n P
        ((degreeZeroCohomologyOnLocalization' A).map
          (((derivedPrecomp DN DM f).app P)⟦n⟧') x) =
      (quasiIsomorphisms' B).Q.map ((toHomotopyCategory B).map f.rightHom) ≫
        extLinearEquiv A B N.rightModule N.leftAction DN n P x
```

**`DifferentialGradedModule.General.homComplexExtEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean#L437). The attribute's comment: “the cohomology of ordinary differential graded Hom is Ext out of a module orthogonal to the acyclics, at independent universes”.

> **`H^n(Hom^•_{(A, d)}(L, M)) = Ext^n_{D(A, d)}(L, M)`**, at independent universes, for `L`
> orthogonal on the left to the acyclic modules.
>
> This is the content that Tag 0CS5 and Tag 0BYW together provide, in the form Tag 0CS6 asks for:
> Tag 09LC identifies the cohomology of the Hom complex with the morphism groups of `K(A, d)`
> (`DifferentialGradedModule.General.homComplexHomologyEquiv`), and the localization functor is
> bijective on the morphisms out of a left-orthogonal object
> (`DifferentialGradedModule.General.bijective_q_map_of_leftOrthogonal`), which is the mechanism of
> Tag 09KY; the shift is moved across the localization by its commutation with the translation.
>
> With `Ext^n_{D(A, d)}(L, M) = Hom_{D(A, d)}(L, M[n])`, as everywhere in Tag 0CS6, the right-hand
> side is that `Ext`-group.

```lean
def homComplexExtEquiv (n : ℤ)
    (hL : (acyclic.{u, v, w} A).leftOrthogonal ((toHomotopyCategory A).obj L)) :
    ↥((homComplex A L M).homology n) ≃+
      ((quasiIsomorphisms.{u, v, w} A).Q.obj ((toHomotopyCategory A).obj L) ⟶
        ((quasiIsomorphisms.{u, v, w} A).Q.obj ((toHomotopyCategory A).obj M))⟦n⟧)
```

## Tag 0BYW, a lemma

[Tag 0BYW](https://stacks.math.columbia.edu/tag/0BYW) in the Stacks Project.

**`DifferentialGradedModule.DerivedHomData.isIso_comparison_of_bijective_q_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomLeftOrthogonal.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomLeftOrthogonal.lean#L217). The attribute's comment: “the comparison under the Hom hypothesis”.

> If `Hom_{D(B,d)}(N, N') = Hom_{K(Mod_{(B,d)})}(N, N')` for all `N' ∈ K(B, d)`, then
> `RHom(N, M) = Hom_{Mod^{dg}_{(B,d)}}(N, M)` functorially in `M` in `D(B, d)`.
>
> The equality of morphism modules is the hypothesis `hN`, that the localization
> `Q : K(B, d) ⥤ D(B, d)` is bijective on the morphisms out of `N`. The functorial equality of the
> conclusion is the invertibility of the comparison natural transformation of Tag 09LI, from
> ordinary differential graded Hom out of `N` read in `D(A, d)` to derived Hom precomposed with the
> localization; `DifferentialGradedModule.DerivedHomData.comparisonNatIso` is the resulting
> isomorphism of functors.
>
> Under the hypothesis the functor being derived already inverts the quasi-isomorphisms
> (`DifferentialGradedModule.isInvertedBy_homToDerivedCategory_of_bijective_q_map`), and the
> comparison of any right derived functor of a functor that inverts them is invertible.

```lean
theorem isIso_comparison_of_bijective_q_map (D : DerivedHomData A B N L)
    (hN : ∀ P : HomotopyCategory B, Function.Bijective
      ((quasiIsomorphisms' B).Q.map : ((toHomotopyCategory B).obj N ⟶ P) → _)) :
    IsIso D.comparison
```

**`DifferentialGradedModule.DerivedHomData.isIso_comparison_of_propertyP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomLeftOrthogonal.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomLeftOrthogonal.lean#L232). The attribute's comment: “the property-(P) sufficient condition”.

> A differential graded `(A, B)`-bimodule whose underlying `B`-module has property (P) computes
> derived Hom by ordinary differential graded Hom, canonically and naturally in the second argument.
>
> A module with property (P) is orthogonal on the left to the acyclic modules, which is Tag 09KM,
> and the localization is bijective on the morphisms out of such a module, which is the mechanism of
> Tag 09KY; so the hypothesis of the previous statement holds.

```lean
theorem isIso_comparison_of_propertyP (D : DerivedHomData A B N L)
    (hN : Nonempty (PropertyPFiltration N)) :
    IsIso D.comparison
```

**`DifferentialGradedModule.DerivedHomData.comparisonNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomLeftOrthogonal.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomLeftOrthogonal.lean#L242). The attribute's comment: “as an identification of functors”.

> **`RHom(N, -) = Hom_{Mod^{dg}_{(B,d)}}(N, -)` as functors.** Ordinary differential graded Hom
> out of `N`, read in `D(A, d)`, is derived Hom out of `N` precomposed with the localization, by the
> comparison map of Tag 09LI and naturally in the second argument.

```lean
def comparisonNatIso (D : DerivedHomData A B N L)
    (hN : ∀ P : HomotopyCategory B, Function.Bijective
      ((quasiIsomorphisms' B).Q.map : ((toHomotopyCategory B).obj N ⟶ P) → _)) :
    homToDerivedCategory A B N L ≅ (quasiIsomorphisms' B).Q ⋙ D.functor
```

**`DifferentialGradedModule.General.homComplexExtEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean#L437). The attribute's comment: “ordinary differential graded Hom out of a left-orthogonal module computes derived Hom, read on cohomology, at independent universes”.

> **`H^n(Hom^•_{(A, d)}(L, M)) = Ext^n_{D(A, d)}(L, M)`**, at independent universes, for `L`
> orthogonal on the left to the acyclic modules.
>
> This is the content that Tag 0CS5 and Tag 0BYW together provide, in the form Tag 0CS6 asks for:
> Tag 09LC identifies the cohomology of the Hom complex with the morphism groups of `K(A, d)`
> (`DifferentialGradedModule.General.homComplexHomologyEquiv`), and the localization functor is
> bijective on the morphisms out of a left-orthogonal object
> (`DifferentialGradedModule.General.bijective_q_map_of_leftOrthogonal`), which is the mechanism of
> Tag 09KY; the shift is moved across the localization by its commutation with the translation.
>
> With `Ext^n_{D(A, d)}(L, M) = Hom_{D(A, d)}(L, M[n])`, as everywhere in Tag 0CS6, the right-hand
> side is that `Ext`-group.

```lean
def homComplexExtEquiv (n : ℤ)
    (hL : (acyclic.{u, v, w} A).leftOrthogonal ((toHomotopyCategory A).obj L)) :
    ↥((homComplex A L M).homology n) ≃+
      ((quasiIsomorphisms.{u, v, w} A).Q.obj ((toHomotopyCategory A).obj L) ⟶
        ((quasiIsomorphisms.{u, v, w} A).Q.obj ((toHomotopyCategory A).obj M))⟦n⟧)
```

**`DifferentialGradedModule.General.homComplexExtEquivOfPropertyP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/HomComplexExtGeneral.lean#L457). The attribute's comment: “the property-(P) sufficient condition, read on cohomology, at independent universes”.

> **`H^n(Hom^•_{(A, d)}(L, M)) = Ext^n_{D(A, d)}(L, M)` for `L` with property (P)**, at
> independent universes.
>
> A differential graded module with property (P) is orthogonal on the left to the acyclic modules,
> which is Tag 09KM at independent universes
> (`DifferentialGradedModule.General.leftOrthogonal_acyclic_of_propertyP`), so the previous
> identification applies. This is the source's own sufficient condition in Tag 0BYW.

```lean
def homComplexExtEquivOfPropertyP {L M : DifferentialGradedModule.{u, v, max v w} A} (n : ℤ)
    (hL : Nonempty (PropertyPFiltration L)) :
    ↥((homComplex A L M).homology n) ≃+
      ((quasiIsomorphisms.{u, v, max v w} A).Q.obj ((toHomotopyCategory A).obj L) ⟶
        ((quasiIsomorphisms.{u, v, max v w} A).Q.obj ((toHomotopyCategory A).obj M))⟦n⟧)
```

**`DifferentialGradedModule.propertyPModelExtEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/PropertyPDerivedModel.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/PropertyPDerivedModel.lean#L173). The attribute's comment: “the cohomology of the differential graded Hom complex of chosen property-(P) representatives is Ext between the objects they represent, at independent universes”.

> **`H^n(Hom^•_{(A, d)}(P_M, P_N)) = Ext^n_{D(A, d)}(M, N)` for arbitrary `M`, `N` in
> `D(A, d)`**, where `P_M` and `P_N` are the chosen property-(P) representatives.
>
> This is the content of Tag 0BYW with no hypothesis on `M` or `N`: the property-(P) reduction is
> performed by the choice of representative rather than assumed. On the representatives it is
> `DifferentialGradedModule.General.homComplexExtEquivOfPropertyP`, and the two isomorphisms
> `DifferentialGradedModule.propertyPModelIso` transport the `Ext`-group from the representatives
> to the objects, the shift being moved across by the commutation of the shift functor with an
> isomorphism.

```lean
def propertyPModelExtEquiv (M N : derivedCategory.{u, v, max v w} A) (n : ℤ) :
    ↥((General.homComplex A (propertyPModel.{u, v, w} A M)
        (propertyPModel.{u, v, w} A N)).homology n) ≃+ (M ⟶ N⟦n⟧)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.31, Tag 09LF](https://stacks.math.columbia.edu/tag/09LF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
