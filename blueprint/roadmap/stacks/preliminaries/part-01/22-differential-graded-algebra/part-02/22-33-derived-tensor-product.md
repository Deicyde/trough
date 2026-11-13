---
declaration: section
origin: cited
lean: DifferentialGraded.Bimodule.tensorCompFunctor, DifferentialGraded.Bimodule.tensorHomotopyFunctor_isTriangulated', DifferentialGraded.Bimodule.tensorFunctorToDerivedCategory_isLeftDerivable, DifferentialGraded.Bimodule.tensorFunctorToDerivedCategory_hasLeftDerivedFunctor, DifferentialGraded.Bimodule.derivedTensorFunctor, DifferentialGraded.Bimodule.derivedTensorFunctor_isLeftDerivedFunctor, DifferentialGraded.Bimodule.derivedTensorNatTrans, DifferentialGraded.Bimodule.isIso_derivedTensorNatTrans_app_shift_regularModule
statement: formalized
proof: formalized
---

# 22.33 Derived tensor product

Section 22.33 of the Stacks Project, [Tag 09LP](https://stacks.math.columbia.edu/tag/09LP). 10 tags here are carried by 50 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09LQ, an equation

[Tag 09LQ](https://stacks.math.columbia.edu/tag/09LQ) in the Stacks Project.

**`DifferentialGraded.Bimodule.tensorCompFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean, line 1266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean#L1266). The attribute's comment: “the functor Mod\_(A,d) -> Mod\_(B,d), M |-> M (x)\_A N”.

> **Stacks 09LM.** The induced functor on the categories of differential graded modules.

```lean
noncomputable abbrev tensorCompFunctor (N : Bimodule A B) :
    DifferentialGradedModule A ⥤ DifferentialGradedModule B
```

## Tag 09LR, a lemma

[Tag 09LR](https://stacks.math.columbia.edu/tag/09LR) in the Stacks Project.

**`DifferentialGraded.Bimodule.tensorHomotopyFunctor_isTriangulated'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorTriangulated.lean, line 660](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorTriangulated.lean#L660).

> **Stacks 09LR.** Tensoring with a differential graded `(A, B)`-bimodule is an exact functor
> from the homotopy category of differential graded `A`-modules to that of differential graded
> `B`-modules: it commutes with translation and carries distinguished triangles to distinguished
> triangles.

```lean
theorem tensorHomotopyFunctor_isTriangulated' (N : Bimodule A B) :
    ∃ h : (tensorHomotopyFunctor N).CommShift ℤ,
      letI := h
      (tensorHomotopyFunctor N).IsTriangulated
```

## Tag 09LS, a lemma

[Tag 09LS](https://stacks.math.columbia.edu/tag/09LS) in the Stacks Project.

**`DifferentialGraded.Bimodule.tensorFunctorToDerivedCategory_isLeftDerivable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean#L110). The attribute's comment: “existence in the pro-object sense”.

> **Stacks Tag 09LS**, in the source's own sense. Tensoring with the bimodule `N`, followed by
> localization of the target, is left derivable with respect to the quasi-isomorphisms: its left
> derived functor is defined at every object of `K(A, d)`, meaning that the pro-object
> `Qis(A)/X ⥤ D(B, d)` is essentially constant (Tag 05SV).

```lean
theorem tensorFunctorToDerivedCategory_isLeftDerivable (N : Bimodule A B) :
    (tensorFunctorToDerivedCategory N).IsLeftDerivable (quasiIsomorphisms' A)
```

**`DifferentialGraded.Bimodule.tensorFunctorToDerivedCategory_hasLeftDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean#L120). The attribute's comment: “existence of the total left derived functor”.

> **Stacks Tag 09LS**, in Mathlib's Kan extension sense. Tensoring with the bimodule `N`,
> followed by localization of the target, has a total left derived functor: a right Kan extension
> along the localization of `K(A, d)` at the quasi-isomorphisms. This is what names
> `- ⊗_A^𝐋 N` as a functor on `D(A, d)`.

```lean
theorem tensorFunctorToDerivedCategory_hasLeftDerivedFunctor (N : Bimodule A B) :
    (tensorFunctorToDerivedCategory N).HasLeftDerivedFunctor (quasiIsomorphisms' A)
```

**`DifferentialGraded.Bimodule.derivedTensorFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean#L128). The attribute's comment: “the derived tensor functor”.

> The derived tensor product `- ⊗_A^𝐋 N : D(A, d) ⥤ D(B, d)` of **Stacks Tag 09LS**: the total
> left derived functor of tensoring with `N` followed by localization.

```lean
def derivedTensorFunctor (N : Bimodule A B) : derivedCategory' A ⥤ derivedCategory' B
```

**`DifferentialGraded.Bimodule.derivedTensorFunctor_isLeftDerivedFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean#L149). The attribute's comment: “universal property”.

> The universal property of **Stacks Tag 09LS**: the comparison
> `DifferentialGraded.Bimodule.derivedTensorFunctorCounit` exhibits `- ⊗_A^𝐋 N` as the left derived
> functor of tensoring with `N` followed by localization, with respect to the
> quasi-isomorphisms.

```lean
instance derivedTensorFunctor_isLeftDerivedFunctor (N : Bimodule A B) :
    (derivedTensorFunctor N).IsLeftDerivedFunctor
      (derivedTensorFunctorCounit N) (quasiIsomorphisms' A)
```

## Tag 09S3, a lemma

[Tag 09S3](https://stacks.math.columbia.edu/tag/09S3) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedTensorNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorBimoduleMap.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorBimoduleMap.lean#L299). The attribute's comment: “the natural transformation 1 (x) f”.

> **Stacks 09S3**, the morphism of functors. A homomorphism `f : N ⟶ N'` of differential graded
> `(A, B)`-bimodules induces `1 ⊗ f : - ⊗_A^𝐋 N ⟶ - ⊗_A^𝐋 N'`, a natural transformation of the
> derived tensor functors of Tag 09LS on `D(A, d)`.
>
> It is the descent of `DifferentialGraded.Bimodule.ordinaryTensorNatTrans` along the localization:
> `- ⊗_A^𝐋 N'` is a right Kan extension of ordinary tensoring with `N'`, so the transformation is
> the unique one compatible with the two comparisons of Tag 09LS
> (`DifferentialGraded.Bimodule.derivedTensorNatTrans_counit`).

```lean
def derivedTensorNatTrans {N N' : Bimodule A B} (f : N ⟶ N') :
    derivedTensorFunctor N ⟶ derivedTensorFunctor N'
```

**`DifferentialGraded.Bimodule.isIso_derivedTensorNatTrans_app_shift_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean#L198). The attribute's comment: “the second assertion at the shifts A[k] of the algebra, where the quasi-isomorphism hypothesis enters”.

> **Clause (3) of the dévissage of Stacks 0FQE for `1 ⊗ f`**: for a homomorphism `f : N ⟶ N'` of
> differential graded `(A, B)`-bimodules which is a quasi-isomorphism of right differential graded
> `B`-modules, the transformation `1 ⊗ f : - ⊗_A^𝐋 N ⟶ - ⊗_A^𝐋 N'` is invertible at the class of
> every shift `A[k]` of the regular module.
>
> The shift `A[k]` is orthogonal on the left to the acyclic modules by Tag 09K1, so both comparisons
> of Tag 09LS are invertible there and `1 ⊗ f` becomes the ordinary map `A[k] ⊗_A N ⟶ A[k] ⊗_A N'`,
> which is the quasi-isomorphism `f[k]`.

```lean
theorem isIso_derivedTensorNatTrans_app_shift_regularModule {N N' : Bimodule A B} (f : N ⟶ N')
    (hf : QuasiIso ((forgetToCochainComplex B).map f.rightHom)) (k : ℤ) :
    IsIso ((derivedTensorNatTrans f).app
      (((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj (regularModule A))⟦k⟧))
```

**`DifferentialGraded.Bimodule.isIso_derivedTensorNatTrans_app_sigma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean#L237). The attribute's comment: “the second assertion at a direct sum, from the summands”.

> **Clause (1) of the dévissage of Stacks 0FQE for `1 ⊗ f`**: the transformation
> `1 ⊗ f : - ⊗_A^𝐋 N ⟶ - ⊗_A^𝐋 N'` is invertible at a direct sum of objects of `D(A, d)` at which it
> is invertible.
>
> Both functors are left adjoints by Tag 09LT, hence preserve direct sums, so the component of
> `1 ⊗ f` at `⨁ᵢ Kᵢ` is the comparison of the two colimit cocones induced by its components at the
> `Kᵢ`.

```lean
theorem isIso_derivedTensorNatTrans_app_sigma {N N' : Bimodule A B} (f : N ⟶ N')
    {ι : Type u} (K : ι → derivedCategory' A)
    (h : ∀ i, IsIso ((derivedTensorNatTrans f).app (K i))) :
    IsIso ((derivedTensorNatTrans f).app (∐ K))
```

**`DifferentialGraded.Bimodule.derivedTensorTwoOutOfThree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean#L268). The attribute's comment: “the second assertion along a distinguished triangle, two out of three”.

> **Clause (2) of the dévissage of Stacks 0FQE for the transformations `1 ⊗ f`.** The derived
> tensor functors are exact and `1 ⊗ f` commutes with the translation, so its components form a
> morphism of distinguished triangles, to which the five lemma of Tag 014A applies.

```lean
theorem derivedTensorTwoOutOfThree (A B : DifferentialGradedAlgebra.{u, u} R) :
    DerivedTensorTwoOutOfThree A B
```

**`DifferentialGraded.Bimodule.quasiIsoInvertsDerivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorQuasiIsoDevissage.lean#L299). The attribute's comment: “the second assertion”.

> **The second assertion of Stacks 09S3.** A homomorphism `f : N ⟶ N'` of differential graded
> `(A, B)`-bimodules that is a quasi-isomorphism of right differential graded `B`-modules induces
> an isomorphism `1 ⊗ f : - ⊗_A^𝐋 N ⟶ - ⊗_A^𝐋 N'` of functors `D(A, d) ⥤ D(B, d)`.

```lean
theorem quasiIsoInvertsDerivedTensor (A B : DifferentialGradedAlgebra.{u, u} R) :
    QuasiIsoInvertsDerivedTensor A B
```

## Tag 0GZ2, a lemma

[Tag 0GZ2](https://stacks.math.columbia.edu/tag/0GZ2) in the Stacks Project.

**`DifferentialGraded.Bimodule.LeftPropertyP`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLeftPropertyP.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLeftPropertyP.lean#L104). The attribute's comment: “the hypothesis: property (P) as a left differential graded A-module”.

> The differential graded `(A, B)`-bimodule `N` *has property (P) as a left differential graded
> `A`-module*: the left differential graded `A`-module underlying it, read as a right differential
> graded `A^{opp}`-module through the equivalence of Tag 0FQ0, carries a property-(P) filtration in
> the sense of Tag 09KK.

```lean
def LeftPropertyP (N : Bimodule A B) : Prop
```

**`DifferentialGraded.Bimodule.isIso_derivedTensorFunctorCounit_app_of_leftPropertyP'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLeftPropertyPProof.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLeftPropertyPProof.lean#L156).

> For a differential graded `(A, B)`-bimodule `N` with property (P) as a left differential
> graded `A`-module and every differential graded `A`-module `M`, the comparison
> `M ⊗_A^𝐋 N ⟶ M ⊗_A N` of Tag 09LS is an isomorphism in `D(B, d)`.

```lean
theorem isIso_derivedTensorFunctorCounit_app_of_leftPropertyP' (N : Bimodule A B)
    (hP : LeftPropertyP N) (M : DifferentialGradedModule A) :
    IsIso ((derivedTensorFunctorCounit N).app ((toHomotopyCategory A).obj M))
```

**`DifferentialGraded.Bimodule.derivedTensorIsoOfLeftPropertyP'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLeftPropertyPProof.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorLeftPropertyPProof.lean#L165). The attribute's comment: “as an isomorphism of functors”.

> For a differential graded `(A, B)`-bimodule `N` with property (P) as a left differential
> graded `A`-module, the isomorphism `- ⊗_A^𝐋 N ≅ - ⊗_A N` of functors `D(A, d) ⥤ D(B, d)`.

```lean
def derivedTensorIsoOfLeftPropertyP' (N : Bimodule A B) (hP : LeftPropertyP N) :
    (quasiIsomorphisms' A).Q ⋙ derivedTensorFunctor N ≅ tensorFunctorToDerivedCategory N
```

## Tag 09LT, a lemma

[Tag 09LT](https://stacks.math.columbia.edu/tag/09LT) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedHomFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean#L240). References: SGA 5 IIIB (5.2), “5.2.3”.

> **Stacks 09LT.** The derived tensor product `- ⊗_A^𝐋 N : D(A, d) ⥤ D(B, d)` of Tag 09LS is a
> left adjoint to derived Hom `RHom(N, -) : D(B, d) ⥤ D(A, d)` of Tag 09LI, for a differential
> graded `(A, B)`-bimodule `N`. Nothing is assumed.
>
> This is `DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedHom` with both of its
> hypotheses supplied: Tag 09LN by
> `DifferentialGraded.Bimodule.tensorHomotopyFunctor_adj_homHomotopyCategoryFunctor`, and Tag 09KU
> by `DifferentialGradedModule.exists_propertyI_resolution`, which also pins the derived Hom
> functor to that of `DifferentialGradedModule.derivedHomData`.
>
> *The degree-zero scope of the Tag 09LN input does not limit this.* What is proved of Tag 09LN
> for differential graded modules is the bijection of the morphism groups of the two categories,
> not the isomorphism of Hom *complexes* in all degrees that the source also states there. But
> Tag 09LT asserts an adjunction of functors between the derived categories — a bijection of
> morphism groups, natural in both variables — and it is deduced from an adjunction of functors
> between the homotopy categories, which is again a bijection of morphism groups. The all-degrees
> half of Tag 09LN is neither used nor needed, so this is Tag 09LT in full and the tag is bare.

```lean
def derivedTensorFunctor_adj_derivedHomFunctor (N : Bimodule A B) :
    derivedTensorFunctor N ⊣ (derivedHomData A B N.rightModule N.leftAction).functor
```

**`DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedHomFunctor_homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean#L250). The attribute's comment: “as a bijection of morphism groups”.

> **Stacks 09LT**, as the bifunctorial identification of morphism groups
> `Hom_{D(B,d)}(M ⊗_A^𝐋 N, P) ≃ Hom_{D(A,d)}(M, RHom(N, P))` that Stacks 0BYX, Example 22.33.2
> uses. Nothing is assumed: it is the hom-set bijection of
> `DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedHomFunctor`.

```lean
def derivedTensorFunctor_adj_derivedHomFunctor_homEquiv (N : Bimodule A B)
    (M : derivedCategory' A) (P : derivedCategory' B) :
    ((derivedTensorFunctor N).obj M ⟶ P) ≃
      (M ⟶ (derivedHomData A B N.rightModule N.leftAction).functor.obj P)
```

## Tag 0BYX, an example

[Tag 0BYX](https://stacks.math.columbia.edu/tag/0BYX) in the Stacks Project.

**`DifferentialGraded.Bimodule.tensorRegularRightNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorRegularRight.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorRegularRight.lean#L255). The attribute's comment: “restriction of scalars is tensoring with the regular bimodule, on differential graded modules”.

> **Stacks 0BYX, the tensor half, on differential graded modules.** Restriction of scalars
> along `ψ : C → B` is tensoring with the regular `(B, C)`-bimodule, naturally in the module.
>
> Naturality is an equality of two homomorphisms out of a tensor product, so it is checked on pure
> tensors, where both sides send `x ⊗ b` to `f(x) b`.

```lean
def tensorRegularRightNatIso (ψ : C.Hom B) :
    tensorCompFunctor (regularRight ψ) ≅ restrictScalarsFunctor ψ
```

**`DifferentialGraded.Bimodule.derivedTensorRegularRightIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorRegularRight.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorRegularRight.lean#L300). The attribute's comment: “restriction of scalars is tensoring with the regular bimodule, on derived categories”.

> **Stacks 0BYX, the tensor half, on derived categories.** Derived restriction of scalars
> along `ψ : C → B` is the derived tensor product with the regular `(B, C)`-bimodule.
>
> Tensoring with the regular bimodule already inverts the quasi-isomorphisms, so by the
> construction of the derived tensor product in the proof of Tag 09LS it computes the derived
> tensor product; and it descends to derived restriction of scalars through the localizations.

```lean
def derivedTensorRegularRightIso (ψ : C.Hom B) :
    derivedTensorFunctor (regularRight ψ) ≅ derivedRestriction ψ
```

**`DifferentialGradedModule.regularHomFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean#L242). The attribute's comment: “the factorization of derived Hom out of the regular bimodule”.

> **Stacks 0BYX.** Internal Hom out of the regular differential graded `(A, B)`-bimodule,
> followed by localization of the target, factors through the derived category of `B` as derived
> restriction of scalars along `φ`.
>
> This is the composite of the identification of internal Hom out of the regular bimodule with
> restriction of scalars (`DifferentialGradedModule.homHomotopyFunctorRegularIso`) and the
> defining factorisation of derived restriction
> (`DifferentialGradedModule.derivedRestrictionFactorization`).

```lean
def regularHomFactorization (φ : A.Hom B) :
    (quasiIsomorphisms' B).Q ⋙ derivedRestriction φ ≅
      homToDerivedCategory A B (regularModule B) (regularBimoduleStructure φ)
```

**`DifferentialGradedModule.DerivedHomData.regular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean#L261). The attribute's comment: “derived Hom out of the regular bimodule, as a right derived functor”.

> **Stacks 0BYX, and Stacks 09LI for the regular bimodule.** Derived Hom out of the regular
> differential graded `(A, B)`-bimodule of a homomorphism `φ : A → B`, as a right derived functor
> of internal Hom — unconditionally, with the derived functor being the already-constructed
> `DifferentialGradedModule.derivedRestriction`.
>
> No resolutions are used: the hypothesis of
> `DifferentialGradedModule.DerivedHomData.ofResolutions` — the existence of property (I)
> resolutions, Tag 09KU — does not appear, because internal Hom out of the regular bimodule is
> restriction of scalars, which does not change the underlying complex and therefore already
> inverts the quasi-isomorphisms.

```lean
def regular (φ : A.Hom B) :
    DerivedHomData A B (regularModule B) (regularBimoduleStructure φ)
```

**`DifferentialGradedModule.DerivedHomData.functorIsoDerivedRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedHomFunctor.lean#L273). The attribute's comment: “RHom(B, -) is restriction of scalars, for any derived Hom datum”.

> **Stacks 0BYX, Example 22.33.2.** `RHom(B, -) = (-)_A`: the functor of *any* right derived
> functor of Hom out of the regular differential graded `(A, B)`-bimodule is canonically derived
> restriction of scalars along `φ`.

```lean
def functorIsoDerivedRestriction (φ : A.Hom B)
    (D : DerivedHomData A B (regularModule B) (regularBimoduleStructure φ)) :
    D.functor ≅ derivedRestriction φ
```

**`DifferentialGradedModule.regularBimoduleStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L203). The attribute's comment: “the regular bimodule structure”.

> A homomorphism `φ : A → B` of differential graded algebras makes the regular right differential
> graded `B`-module into a differential graded `(A, B)`-bimodule: `A` acts on the left by
> multiplication through `φ`, and that action is right `B`-linear by associativity.

```lean
def regularBimoduleStructure (φ : A.Hom B) : BimoduleStructure A B (regularModule B)
```

**`DifferentialGradedModule.regularHomogeneousEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L271). The attribute's comment: “evaluation at one, degreewise”.

> **Evaluation at one.** The degree-`n` homogeneous right `B`-linear maps out of the regular
> differential graded `B`-module are the degree-`n` elements of the target, by evaluation at the
> unit. This is the degreewise half of Example 22.33.2.

```lean
def regularHomogeneousEquiv (P : DifferentialGradedModule B) (n : ℤ) :
    P.grading n ≃ₗ[R] HomogeneousMap B (regularModule B) P n
```

**`DifferentialGradedModule.restrictScalarsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L309). The attribute's comment: “restriction of scalars as a functor”. References: EGA II (2.8.6), “more general”.

> Restriction of scalars along `φ`, as a functor between the categories of differential graded
> modules. A homomorphism is unchanged: a `B`-linear map is `A`-linear through `φ`.

```lean
def restrictScalarsFunctor (φ : A.Hom B) :
    DifferentialGradedModule B ⥤ DifferentialGradedModule A
```

**`DifferentialGradedModule.restrictScalarsHomotopyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L369). The attribute's comment: “restriction of scalars on homotopy categories”.

> Restriction of scalars along `φ` on the homotopy categories: it descends through the homotopy
> quotient because it preserves homotopies.

```lean
def restrictScalarsHomotopyFunctor (φ : A.Hom B) : HomotopyCategory B ⥤ HomotopyCategory A
```

**`DifferentialGradedModule.derivedRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L416). The attribute's comment: “restriction of scalars on derived categories”.

> Restriction of scalars along `φ` on the derived categories, obtained by descending restriction
> on the homotopy categories through the localization at the quasi-isomorphisms. This is the functor
> `R Hom(B, -) : D(B, d) ⥤ D(A, d)` of Example 22.33.2, whose identification with derived Hom out of
> the regular bimodule is the content of that example.

```lean
def derivedRestriction (φ : A.Hom B) : derivedCategory' B ⥤ derivedCategory' A
```

**`DifferentialGradedModule.derivedRestrictionFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L423). The attribute's comment: “the factorization of derived restriction”.

> Derived restriction of scalars is restriction of scalars read through the localizations: the
> square of homotopy and derived categories commutes up to this canonical isomorphism.

```lean
def derivedRestrictionFactorization (φ : A.Hom B) :
    (quasiIsomorphisms' B).Q ⋙ derivedRestriction φ ≅
      restrictScalarsHomotopyFunctor φ ⋙ (quasiIsomorphisms' A).Q
```

**`DifferentialGradedModule.regularHomModuleData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L465). The attribute's comment: “restriction of scalars presents the internal hom”. References: EGA III (7.2.2), “more general”.

> Restriction of scalars along `φ` presents the internal hom out of the regular differential
> graded `(A, B)`-bimodule: its degree-`n` part is the degree-`n` homogeneous right `B`-linear maps
> `B → P`, by evaluation at the unit, and the right `A`-action matches precomposition with
> multiplication through `φ`.

```lean
def regularHomModuleData (φ : A.Hom B) (P : DifferentialGradedModule B) :
    HomModuleData A B (regularModule B) P (regularBimoduleStructure φ)
```

**`DifferentialGradedModule.homModuleRegularIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L491). The attribute's comment: “evaluation at one”.

> Evaluation at the unit identifies the internal hom out of the regular differential graded
> `(A, B)`-bimodule with restriction of scalars along `φ`.

```lean
def homModuleRegularIso (φ : A.Hom B) (P : DifferentialGradedModule B) :
    (regularHomFunctor φ).obj P ≅ (restrictScalarsFunctor φ).obj P
```

**`DifferentialGradedModule.homModuleFunctorRegularIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L532). The attribute's comment: “evaluation at one is natural”.

> Evaluation at one is natural: the internal hom functor out of the regular differential graded
> `(A, B)`-bimodule is restriction of scalars along `φ`.

```lean
def homModuleFunctorRegularIso (φ : A.Hom B) :
    regularHomFunctor φ ≅ restrictScalarsFunctor φ
```

**`DifferentialGradedModule.homHomotopyFunctorRegularIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L586). The attribute's comment: “evaluation at one on homotopy categories”.

> Evaluation at one on homotopy categories: the internal hom functor out of the regular
> differential graded `(A, B)`-bimodule is restriction of scalars along `φ`. This is the
> identification `R Hom(B, -) = (-)_A` of Example 22.33.2, before localizing.

```lean
def homHomotopyFunctorRegularIso (φ : A.Hom B) :
    homHomotopyCategoryFunctor A B (regularModule B) (regularBimoduleStructure φ) ≅
      restrictScalarsHomotopyFunctor φ
```

**`DifferentialGradedModule.quasiIsomorphisms_isInvertedBy_homToDerivedCategory_regular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L598). The attribute's comment: “derived Hom out of the regular bimodule needs no resolutions”.

> The functor whose right derived functor is derived Hom out of the regular differential graded
> `(A, B)`-bimodule already inverts the quasi-isomorphisms: it is restriction of scalars followed by
> localization, and restriction does not change the underlying complex.

```lean
theorem quasiIsomorphisms_isInvertedBy_homToDerivedCategory_regular (φ : A.Hom B) :
    (quasiIsomorphisms' B).IsInvertedBy
      (homToDerivedCategory A B (regularModule B) (regularBimoduleStructure φ))
```

**`DifferentialGraded.Bimodule.regular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestriction.lean#L618). The attribute's comment: “the regular bimodule”.

> The regular differential graded `(A, B)`-bimodule of a homomorphism `φ : A → B` of differential
> graded algebras: `B` itself, with `B` acting on the right by multiplication and `A` acting on the
> left through `φ`. Tensoring with it is the extension of scalars `- ⊗_A B : D(A, d) ⥤ D(B, d)` of
> Example 22.33.2.

```lean
def regular (φ : A.Hom B) : Bimodule A B
```

**`DifferentialGradedModule.derivedHom_comparison_eq_evaluationAtOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestrictionEvaluation.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedRestrictionEvaluation.lean#L143). The attribute's comment: “the comparison of derived Hom out of the regular bimodule is evaluation at one”.

> **Stacks 0BYX, Example 22.33.2.** The identification of derived Hom out of the regular
> differential graded `(A, B)`-bimodule with derived restriction of scalars is pinned by evaluation
> at the unit: on the class of a differential graded `B`-module `N`, the canonical comparison of the
> derived functor with internal Hom, followed by the identification with derived restriction and the
> factorisation of derived restriction, is the localisation of the evaluation morphism
> `Hom^•_B(B, N) → N_A, f ↦ f(1)`, transported along the identification
> `DifferentialGradedModule.homHomotopyFunctorRegularIso` of the two source objects.
>
> The transport is not optional: internal Hom out of the regular bimodule is isomorphic to
> restriction of scalars and not equal to it, so the two morphisms have different sources.

```lean
theorem derivedHom_comparison_eq_evaluationAtOne (φ : A.Hom B)
    (D : DerivedHomData A B (regularModule B) (regularBimoduleStructure φ))
    (N : DifferentialGradedModule B) :
    D.comparison.app ((toHomotopyCategory B).obj N) ≫
        (DerivedHomData.functorIsoDerivedRestriction φ D).hom.app
          ((quasiIsomorphisms' B).Q.obj ((toHomotopyCategory B).obj N)) ≫
        (derivedRestrictionFactorization φ).hom.app ((toHomotopyCategory B).obj N) =
      (quasiIsomorphisms' A).Q.map
          ((homHomotopyFunctorRegularIso φ).hom.app ((toHomotopyCategory B).obj N)) ≫
        (quasiIsomorphisms' A).Q.map
          ((toHomotopyCategory A).map ((evaluationAtOne φ).evaluation N))
```

**`DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean#L279). The attribute's comment: “the adjunction Hom\_\{D(A,d)}(M, N\_A) = Hom\_\{D(B,d)}(M ⊗\_A^𝐋 B, N), bifunctorially”. References: SGA 5 IIIB (5.2), “5.2.3 for F = B”.

> **Stacks 0BYX, Example 22.33.2.** For a homomorphism `φ : (A, d) → (B, d)` of differential
> graded algebras, derived extension of scalars `- ⊗_A^𝐋 B : D(A, d) ⥤ D(B, d)` — tensoring with
> the regular bimodule, `DifferentialGraded.Bimodule.regular` — is left adjoint to derived
> restriction of scalars `(-)_A : D(B, d) ⥤ D(A, d)`. Nothing is assumed.
>
> This is the displayed formula of the example,
> `Hom_{D(A,d)}(M, N_A) = Hom_{D(B,d)}(M ⊗_A^𝐋 B, N)`, *bifunctorially in `M` and `N`*: an
> `CategoryTheory.Adjunction` is exactly a bijection of the two morphism groups together with its
> naturality in both variables, so the bifunctoriality the source asserts is carried by this
> statement and needs no separate lemma. The bijection on its own is
> `DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedRestriction_homEquiv`.
>
> The two inputs are the two steps the example takes. The adjunction with derived Hom out of the
> regular bimodule on the right is Tag 09LT,
> `DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedHomFunctor`; and
> `DifferentialGradedModule.DerivedHomData.functorIsoDerivedRestriction` is the example's
> identification `RHom(B, -) = (-)_A`, which comes from `Hom_{Mod^{dg}_B}(B, N) ≅ N_A`, `f ↦ f(1)`,
> naturally in `N`. Transporting the right adjoint along that isomorphism replaces `RHom(B, -)` by
> restriction of scalars, which is the example's conclusion.

```lean
def derivedTensorFunctor_adj_derivedRestriction (φ : A.Hom B) :
    derivedTensorFunctor (Bimodule.regular φ) ⊣ derivedRestriction φ
```

**`DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedRestriction_homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorHomAdjunction.lean#L293). The attribute's comment: “the displayed formula Hom\_\{D(A,d)}(M, N\_A) = Hom\_\{D(B,d)}(M ⊗\_A^𝐋 B, N)”.

> **Stacks 0BYX, Example 22.33.2**, the displayed formula itself:
> `Hom_{D(A,d)}(M, N_A) = Hom_{D(B,d)}(M ⊗_A^𝐋 B, N)`.
>
> It is the hom-set bijection of
> `DifferentialGraded.Bimodule.derivedTensorFunctor_adj_derivedRestriction`, so the
> bifunctoriality in `M` and `N` that the source asserts is the naturality carried by that
> adjunction; it is not restated here.

```lean
def derivedTensorFunctor_adj_derivedRestriction_homEquiv (φ : A.Hom B)
    (M : derivedCategory' A) (N : derivedCategory' B) :
    (M ⟶ (derivedRestriction φ).obj N) ≃
      ((derivedTensorFunctor (Bimodule.regular φ)).obj M ⟶ N)
```

**`DifferentialGradedModule.evaluationAtOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/EvaluationAtOne.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/EvaluationAtOne.lean#L95). The attribute's comment: “evaluation\_at\_one”.

> Evaluation at the unit identifies the graded Hom from `B` with restriction to `A`,
> naturally in the differential graded `B`-module.

```lean
public noncomputable def evaluationAtOne (φ : A.Hom B) :
    EvaluationAtOneData φ
```

**`DifferentialGradedModule.restrictScalars`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Restriction.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Restriction.lean#L60). The attribute's comment: “restriction\_notation”. References: EGA II (2.8.6), “more general”.

> Restrict a right differential graded `B`-module to `A` along a homomorphism of differential
> graded algebras.

```lean
def restrictScalars (φ : A.Hom B) (N : DifferentialGradedModule B) :
    DifferentialGradedModule A
```

**`Dualizing.derivedExtensionToDGA_adj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionExtension.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionExtension.lean#L87). The attribute's comment: “extension of scalars along R -> E is left adjoint to forgetting the action”.

> **Stacks 0BYX for the structure homomorphism of `E`, read on `D(R)`.** Derived extension of
> scalars `- ⊗_R^𝐋 E : D(R) ⥤ D(E, d)` is left adjoint to the forgetful functor
> `D(E, d) ⥤ D(R)`.
>
> The adjunction of Tag 0BYX is between derived extension and derived restriction of scalars along
> `R → E`; transporting its right adjoint along `Dualizing.derivedRestrictBaseForgetIso`, which
> identifies derived restriction read on `D(R)` with the forgetful functor, gives the statement in
> the form Situation 0BZB uses.

```lean
def derivedExtensionToDGA_adj (E : DifferentialGradedAlgebra.{u, u} R) :
    derivedExtensionToDGA E ⊣ derivedForget E
```

**`Dualizing.derivedTensorResolvingBimoduleForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionForget.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionForget.lean#L150). The attribute's comment: “forgetting the action is derived tensoring with the regular (E, R)-bimodule”.

> **The tensor half of Stacks 0BYX for the structure homomorphism of `E`.** Derived tensoring
> with the resolving bimodule `E`, read in the derived category of `R`-modules through the
> degree-zero equivalence, is the forgetful functor `D(E, d) ⥤ D(R)`: forgetting the `E`-action is
> restriction of scalars along `R → E`, which is tensoring with the regular `(E, R)`-bimodule.

```lean
def derivedTensorResolvingBimoduleForgetIso (E : DifferentialGradedAlgebra.{u, u} R) :
    Bimodule.derivedTensorFunctor (resolvingBimodule E) ⋙
        (degreeZeroDerivedEquivalence (R := R) (A := R)).functor ≅ derivedForget E
```

**`Dualizing.DGAResolution.derivedTensorResolvingBimoduleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionForget.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DifferentialGradedResolutionForget.lean#L166). The attribute's comment: “forgetting the action of the resolving algebra is derived tensoring with its regular (E, R)-bimodule”.

> **The tensor half of Stacks 0BYX at the resolving algebra of Situation 0BZB.** Derived
> tensoring with the resolving bimodule of `E`, read in the derived category of `R`-modules, is
> the forgetful functor `D(E, d) ⥤ D(R)`.

```lean
def derivedTensorResolvingBimoduleIso (S : Dualizing.DGAResolution R A) :
    Bimodule.derivedTensorFunctor (Dualizing.resolvingBimodule S.E) ⋙
        (degreeZeroDerivedEquivalence (R := R) (A := R)).functor ≅
      DifferentialGradedModule.derivedForget S.E
```

## Tag 09R9, a lemma

[Tag 09R9](https://stacks.math.columbia.edu/tag/09R9) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedTensorFunctor_fullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFullyFaithful.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFullyFaithful.lean#L431).

> **Stacks 09R9.** Let `(A, d)` and `(B, d)` be differential graded algebras over a commutative
> ring `R` and let `N` be a differential graded `(A, B)`-bimodule. Assume
>
> 1. the class of `N` in `D(B, d)` is a compact object, and
> 2. the canonical map `H^k(A) → Hom_{D(B,d)}(N, N[k])` of
>    `DifferentialGraded.Bimodule.cohomologyEndomorphismComparison` is bijective for every
>    `k : ℤ`.
>
> Then the derived tensor product `- ⊗_A^𝐋 N : D(A, d) ⥤ D(B, d)` of Tag 09LS is fully faithful.
>
> Full faithfulness is data — a chosen inverse to the action on morphism groups — so this is a
> definition. It is Tag 07RB applied to the adjunction of Tag 09LT, whose unit is invertible by
> `DifferentialGraded.Bimodule.isIso_unit_derivedTensorFunctor_adj_derivedHomFunctor`.

```lean
def derivedTensorFunctor_fullyFaithful (N : Bimodule A B)
    [IsCompactObject.{u} ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj N.rightModule)]
    (h2 : ∀ k : ℤ, Function.Bijective (N.cohomologyEndomorphismComparison k)) :
    (derivedTensorFunctor N).FullyFaithful
```

## Tag 0BYZ, a lemma

[Tag 0BYZ](https://stacks.math.columbia.edu/tag/0BYZ) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedBaseChangeFunctor_isLeftDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BaseChange.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BaseChange.lean#L224). The attribute's comment: “part (1) only, with the functor being derived presented as M |-> M (x)\_A A': the identification c\_M with the source's M |-> M (x)\_R R' is baseChangeTensorIso over R' and baseChangeTensorAlgebraIso over A'. Corrected: the source says "right derived functor", but base change is a tensor product and so is LEFT derived, as Tag 09LS has it. Parts (2) and (3) are elsewhere, per the docstrings; nothing of Tag 0BYZ remains uncovered”.

> **Stacks 0BYZ, part (1).** The derived tensor product `- ⊗_A^𝐋 A'` with the base change
> `A' = A ⊗_R R'` is the total left derived functor of base change
> `K(A, d) → K(A', d)`, `M ↦ M ⊗_R R'`, followed by localization.
>
> The functor derived here is `M ↦ M ⊗_A A'`; it is base change `M ↦ M ⊗_R R'` by the canonical map
> `c_M` of the source's proof, which is `DifferentialGraded.Bimodule.baseChangeTensorIso` as an
> isomorphism of differential graded `R'`-modules and
> `DifferentialGraded.Bimodule.baseChangeTensorAlgebraIso` as one of differential graded
> `A'`-modules. Part (3) is
> `DifferentialGraded.Bimodule.isIso_derivedBaseChangeCounit_app_of_kFlat` of
> `StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeRepresents.lean` and part (2) is
> `DifferentialGraded.Bimodule.derivedBaseChangeRestrictionSquare` of
> `StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeRestrictionSquare.lean`.

```lean
theorem derivedBaseChangeFunctor_isLeftDerivedFunctor :
    (derivedBaseChangeFunctor A R').IsLeftDerivedFunctor
      (derivedBaseChangeCounit A R') (quasiIsomorphisms' A)
```

**`DifferentialGraded.Bimodule.baseChangeTensorAlgebraIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeAbsoluteTensor.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeAbsoluteTensor.lean#L552). The attribute's comment: “the A'-linearity of the canonical map c\_M of the PROOF, NOT any of parts (1), (2), (3): M (x)\_A A' is M (x)\_R R' as differential graded A'-modules, the right action on M (x)\_R R' being (m (x) t)(a (x) s) = (m a) (x) (t s). With this nothing of Tag 0BYZ is left unformalized; the module docstring says where the three parts and the R'-only form baseChangeTensorIso are, and how this A'-module restricts to that R'-module”.

> **The `A'`-linearity of the canonical map `c_M` in the proof of Stacks 0BYZ.** Let `R → R'`
> be a map of commutative rings, let `(A, d)` be a differential graded `R`-algebra and let
> `A' = A ⊗_R R'` be its base change. For a differential graded `A`-module `M` the base change
> `M ⊗_A A'` is `M ⊗_R R'` **as a differential graded `A'`-module**, the right action of `a ⊗ s`
> on `M ⊗_R R'` being `(m ⊗ t) · (a ⊗ s) = (m · a) ⊗ (t s)`
> (`DifferentialGradedModule.baseChange_smul_tmul`).
>
> The isomorphism is the source's `c_M`, read in the direction out of the relative tensor product:
> it sends the pure tensor `x ⊗ (a ⊗ s)` to `(x · a) ⊗ s`
> (`DifferentialGraded.Bimodule.baseChangeTensorForward_pure`), and its inverse — the source's
> `c_M` itself — sends `x ⊗ s` to `x ⊗ (1 ⊗ s)`.

```lean
def baseChangeTensorAlgebraIso :
    baseChangeRelativeTensor A R' M ≅ baseChangeAbsoluteTensor M R'
```

**`DifferentialGraded.Bimodule.isIso_derivedBaseChangeCounit_app_of_kFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeRepresents.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeRepresents.lean#L138). The attribute's comment: “part (3): M K-flat as a complex of R-modules implies that the ordinary base change represents M (x)\_A^L A'. The representing object is spelled M (x)\_A A'; it is the source's differential graded A'-module M (x)\_R R' by baseChangeTensorIso over R' and by baseChangeTensorAlgebraIso of BaseChangeAbsoluteTensor.lean over A'. Part (2) is derivedBaseChangeRestrictionSquare of BaseChangeRestrictionSquare.lean”.

> Let `R → R'` be a ring map, `(A, d)` a differential graded `R`-algebra which is K-flat as a
> complex of `R`-modules, and `A' = A ⊗_R R'`. For a differential graded `A`-module `M` which is
> K-flat as a complex of `R`-modules, the comparison from the derived base change `M ⊗_A^𝐋 A'` to
> the ordinary base change `M ⊗_A A'` is an isomorphism at `M`, so `M ⊗_A A'` represents
> `M ⊗_A^𝐋 A'`. Nothing is asked of `R'`.

```lean
theorem isIso_derivedBaseChangeCounit_app_of_kFlat
    (hA : CochainComplex.KFlat.{u, u} (regularModule A).toCochainComplex)
    (M : DifferentialGradedModule.{u, u, u} A)
    (hM : CochainComplex.KFlat.{u, u} M.toCochainComplex) :
    IsIso ((derivedBaseChangeCounit A R').app ((toHomotopyCategory A).obj M))
```

**`DifferentialGraded.Bimodule.derivedBaseChangeRestrictionSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeRestrictionSquare.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeRestrictionSquare.lean#L391). The attribute's comment: “part (2): the square of restriction and derived base change commutes. The left column is restriction along the structure homomorphism R -> A, the right column restriction along r' |-> 1 (x) r', and the bottom edge derived base change of R in degree zero read in D(R', d) through the unitor R (x)\_R R' = R' of degreeZeroBaseChangeUnitor. Parts (1) and (3) are derivedBaseChangeFunctor\_isLeftDerivedFunctor and isIso\_derivedBaseChangeCounit\_app\_of\_kFlat”.

> **Stacks 0BYZ, part (2).** *"Let `R → R'` be a ring map, let `(A, d)` be a differential
> graded `R`-algebra, let `(A', d)` be the base change `A ⊗_R R'`. If `A` is K-flat as a complex of
> `R`-modules, then the diagram*
> ```
> D(A, d) --- - ⊗_A^𝐋 A' ---> D(A', d)
>    |                           |
> restriction                restriction
>    v                           v
>  D(R)  --- - ⊗_R^𝐋 R' --->   D(R')
> ```
> *commutes."*
>
> The two columns are restriction of scalars along the structure homomorphism `R → A` of
> `DifferentialGradedAlgebra.baseHom` and along `r' ↦ 1 ⊗ r'`; the bottom edge is
> derived base change of the base ring in degree zero, read in `D(R', d)` through
> `DifferentialGradedAlgebra.degreeZeroBaseChangeUnitor`, whose derived restriction is the
> equivalence `DifferentialGradedModule.degreeZeroBaseChangeEquivalence`.
>
> Both composites are left derived functors of the same functor `K(A, d) ⥤ D(R', d)`,
> `M ↦ M ⊗_R R'`: the comparison `c_M` of the plain functors is an isomorphism for every `M`
> (`DifferentialGraded.Bimodule.isIso_baseChangeStructureTensorTrans_app`), and the left-hand
> composite's own comparison is invertible at the modules with property (P) — which is where the
> K-flatness of `A` is used, through
> `DifferentialGradedModule.kFlat_toCochainComplex_of_propertyPFiltration` and part (3) in the
> form `DifferentialGraded.Bimodule.isIso_derivedTensorBimoduleCounit_app_of_kFlat`. So the square
> commutes by the uniqueness of a left derived functor.

```lean
def derivedBaseChangeRestrictionSquare
    (hA : CochainComplex.KFlat.{u, u} (regularModule A).toCochainComplex) :
    derivedBaseChangeFunctor A R' ⋙
        derivedRestriction (tensorIncludeRightHom A (degreeZero R R')) ≅
      derivedRestriction (baseHom A) ⋙
        derivedBaseChangeFunctor (degreeZero R R) R' ⋙
          derivedRestriction (tensorIncludeRightHom (degreeZero R R) (degreeZero R R'))
```

**`DifferentialGraded.Bimodule.baseChangeTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorRestrictRight.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorRestrictRight.lean#L232). The attribute's comment: “the canonical map c\_M of the PROOF, over R' — NOT any of parts (1), (2), (3). It is what identifies the functor derived in part (1), derivedBaseChangeFunctor\_isLeftDerivedFunctor of BaseChange.lean, with the source's M |-> M (x)\_R R'. Part (2) is derivedBaseChangeRestrictionSquare, part (3) isIso\_derivedBaseChangeCounit\_app\_of\_kFlat. The A'-linear form of this map, which is what the source states, is baseChangeTensorAlgebraIso”.

> **The canonical map `c_M` in the proof of Stacks 0BYZ, over `R'`.** Let `R → R'` be a ring
> map, let `(A, d)` be a differential graded `R`-algebra and let `A' = A ⊗_R R'` be its base change.
> For a differential graded `A`-module `M` the differential graded `R'`-module underlying the base
> change `M ⊗_A A'` is `M ⊗_R R'`.
>
> The source's `c_M : M ⊗_R R' → M ⊗_A A'` is a map of differential graded `A'`-modules; this is
> that map after restricting the right action from `A'` to `R'`, which is where its content lies:
> restricting the right action does not change the relative tensor product
> (`DifferentialGraded.Bimodule.tensorCompFunctorRestrictRightIso`), and over `R'` the base-change
> bimodule is the one for which `M ⊗_A (A ⊗_R R') = M ⊗_R R'` is already proved
> (`DifferentialGraded.absBalanceIso`). The `A'`-linear statement, which needs `M ⊗_R R'` built as
> a differential graded `A ⊗_R R'`-module and is proved by the universal property rather than by
> this transfer, is `DifferentialGraded.Bimodule.baseChangeTensorAlgebraIso` in
> `StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeAbsoluteTensor.lean`.

```lean
def baseChangeTensorIso (M : DifferentialGradedModule.{u, u, u} A) :
    (restrictScalarsFunctor (tensorIncludeRightHom A (degreeZero R R'))).obj
        ((tensorCompFunctor (baseChange A R')).obj M) ≅
      M.absoluteTensor (degreeZero R R')
```

**`DifferentialGradedModule.kFlat_toCochainComplex_of_propertyPFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/PropertyPKFlat.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/PropertyPKFlat.lean#L95). The attribute's comment: “the K-flatness half of the claim in the PROOF — a differential graded A-module with property (P) is K-flat as a complex of R-modules. Not any of parts (1), (2), (3); part (1) is DifferentialGraded.Bimodule.derivedBaseChangeFunctor\_isLeftDerivedFunctor”.

> **A differential graded module with property (P) over a differential graded algebra which is
> K-flat as a complex of `R`-modules is itself K-flat as a complex of `R`-modules.** This is the
> K-flatness half of the claim in the proof of Stacks 0BYZ.
>
> The induction is `DifferentialGradedModule.propertyPFiltration_induction`; its five obligations
> are, in order, that K-flatness is invariant under isomorphism, that it holds on a direct sum of
> shifts of `A`, that it is stable under countable direct sums, and the two directions of
> two-out-of-three along an admissible short exact sequence. The hypothesis on `A` enters only in
> the second.

```lean
theorem kFlat_toCochainComplex_of_propertyPFiltration
    (hA : CochainComplex.KFlat.{u, u} (regularModule A).toCochainComplex)
    {P : DifferentialGradedModule A} (F : PropertyPFiltration P) :
    CochainComplex.KFlat.{u, u} P.toCochainComplex
```

## Tag 0BZ0, a lemma

[Tag 0BZ0](https://stacks.math.columbia.edu/tag/0BZ0) in the Stacks Project.

**`DifferentialGraded.Bimodule.homDualBimodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomBimodule.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomBimodule.lean#L254). The attribute's comment: “the (B, A)-bimodule structure on S = Hom(T, B)”.

> **Stacks 0BZ0**, first assertion. For a differential graded `(A, B)`-bimodule `T`, the
> internal hom `S = Hom_{Mod^{dg}_{(B, d)}}(T, B)` is a differential graded `(B, A)`-bimodule: the
> right `A`-action is precomposition with the left action of `A` on `T`, and the left `B`-action is
> postcomposition with left multiplication on `B`.

```lean
def homDualBimodule (T : Bimodule A B) : Bimodule B A
```

**`DifferentialGraded.Bimodule.derivedTensorHomDualFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomTensorIso.lean, line 402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/InternalHomTensorIso.lean#L402). The attribute's comment: “the second assertion: the functorial isomorphism N ⊗\_B^L S ≅ RHom(T, N)”.

> **Stacks 0BZ0, second assertion.** Let `R` be a ring, let `(A, d)` and `(B, d)` be
> differential graded `R`-algebras and let `T` be a differential graded `(A, B)`-bimodule. Assume
>
> 1. `T` defines a compact object of `D(B, d)`, and
> 2. `S = Hom_{Mod^{dg}_{(B, d)}}(T, B)` represents `R Hom(T, B)` in `D(A, d)`, that is, the
>    comparison of Tag 09LI is invertible at the regular module.
>
> Then there is an isomorphism `N ⊗_B^𝐋 S ⟶ R Hom(T, N)` functorial in `N` in `D(B, d)`: the
> differential graded `(B, A)`-bimodule structure on `S` is
> `DifferentialGraded.Bimodule.homDualBimodule`, and the functorial isomorphism is an isomorphism
> of the two functors `D(B, d) ⥤ D(A, d)` of Tag 09LS and Tag 09LI.
>
> The map itself is `DifferentialGraded.Bimodule.derivedEvalNatTrans`: the composition pairing of
> Tag 09LC, read on differential graded modules and descended to the derived category, lifted
> along the localization `K(B, d) ⥤ D(B, d)`.

```lean
def derivedTensorHomDualFunctorIso (T : Bimodule A B)
    (h1 : IsCompactObject.{u}
      ((toHomotopyCategory B ⋙ (quasiIsomorphisms' B).Q).obj T.rightModule))
    (h2 : IsIso ((derivedHomData A B T.rightModule T.leftAction).comparison.app
      ((toHomotopyCategory B).obj (regularModule B)))) :
    derivedTensorFunctor (homDualBimodule T) ≅
      (derivedHomData A B T.rightModule T.leftAction).functor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.33, Tag 09LP](https://stacks.math.columbia.edu/tag/09LP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
