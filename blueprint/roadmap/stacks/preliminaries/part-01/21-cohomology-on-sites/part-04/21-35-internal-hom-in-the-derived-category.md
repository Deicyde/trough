---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.derivedCurrySectionsEquiv, AlgebraicGeometry.RingedSite.derivedCurrySectionsEquiv_restriction, AlgebraicGeometry.RingedSite.derivedCurrySectionsEquiv_naturality_source, AlgebraicGeometry.RingedSite.derivedCurryHomEquiv, AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_apply, AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_naturality, AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_dinaturality, AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_naturality_source
statement: formalized
proof: formalized
---

# 21.35 Internal hom in the derived category

Section 21.35 of the Stacks Project, [Tag 08J7](https://stacks.math.columbia.edu/tag/08J7). 13 tags here are carried by 57 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08J8, an equation

[Tag 08J8](https://stacks.math.columbia.edu/tag/08J8) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedCurrySectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/TensorHomSectionsCurrying.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/TensorHomSectionsCurrying.lean#L142). The attribute's comment: “the bijection of morphism groups over an object of the site”.

> **The tensor–internal-Hom bijection of [Stacks, Tag 08J8] over an object `U` of the site.**
> Morphisms `K|_U ⟶ RSheafHom(B, Z)|_U` are morphisms `(K ⊗^L_O B)|_U ⟶ Z|_U`.
>
> It is the derived currying isomorphism of [Stacks, Tag 08J9] read on degree-zero hypercohomology
> over `U`, with both sides identified with groups of morphisms between restrictions by
> [Stacks, Tag 08JA].  The tensor product is the one taken on `C`.

```lean
def derivedCurrySectionsEquiv
    (K B Z : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        U).mapDerivedCategory.obj K ⟶
        (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
            U).mapDerivedCategory.obj
          (((derivedSheafHomBifunctor X).obj (op B)).obj Z)) ≃+
      ((SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
          U).mapDerivedCategory.obj
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj B) ⟶
        (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
            U).mapDerivedCategory.obj Z)
```

**`AlgebraicGeometry.RingedSite.derivedCurrySectionsEquiv_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/TensorHomSectionsCurrying.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/TensorHomSectionsCurrying.lean#L222). The attribute's comment: “the bijection over an object of the site restricts the global one”.

> **The bijection of [Stacks, Tag 08J8] over `U` is the restriction of the bijection over
> `C`.**  For `g : K ⟶ RSheafHom(B, Z)` the morphism `(K ⊗^L_O B)|_U ⟶ Z|_U` matched with `g|_U`
> over `U` is the restriction of the morphism `K ⊗^L_O B ⟶ Z` matched with `g` over `C`.
>
> This is the compatibility of [Stacks, Tag 08JA] globally and over `U` under restriction of
> hypercohomology, applied at the two ends of the bijection, with the naturality of that
> restriction at the derived currying isomorphism in between.

```lean
theorem derivedCurrySectionsEquiv_restriction
    (K B Z : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (g : K ⟶ ((derivedSheafHomBifunctor X).obj (op B)).obj Z) :
    derivedCurrySectionsEquiv X U K B Z
        ((SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
            U).mapDerivedCategory.map g) =
      (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
          U).mapDerivedCategory.map
        (derivedCurryHomEquiv X K B Z g)
```

**`AlgebraicGeometry.RingedSite.derivedCurrySectionsEquiv_naturality_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/TensorHomSectionsCurrying.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/OpenLift/TensorHomSectionsCurrying.lean#L343). The attribute's comment: “functoriality in the source, over an object of the site”.

> **The bijection of [Stacks, Tag 08J8] over `U` is natural in its source variable.**  For a
> morphism `u : K' ⟶ K` of `D(O)`, precomposing a morphism `K|_U ⟶ RSheafHom(B, Z)|_U` with `u|_U`
> corresponds to precomposing the matched morphism `(K ⊗^L_O B)|_U ⟶ Z|_U` with the restriction of
> `u ⊗ 1`.

```lean
theorem derivedCurrySectionsEquiv_naturality_source
    (K K' B Z : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (u : K' ⟶ K)
    (h : (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        U).mapDerivedCategory.obj K ⟶
      (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
          U).mapDerivedCategory.obj
        (((derivedSheafHomBifunctor X).obj (op B)).obj Z)) :
    derivedCurrySectionsEquiv X U K' B Z
        ((SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
            U).mapDerivedCategory.map u ≫ h) =
      (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
          U).mapDerivedCategory.map
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).map u).app B) ≫
        derivedCurrySectionsEquiv X U K B Z h
```

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrying.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrying.lean#L221). The attribute's comment: “the tensor-internal-Hom bijection of morphism groups”.

> **The tensor–internal-Hom isomorphism of morphism groups**, Stacks 08J8 as 08J9 gives it:
> morphisms `K ⟶ RSheafHom(L, M)` in `D(O)` are morphisms `K ⊗^L_O L ⟶ M`.
>
> It is the derived currying isomorphism read on degree-zero global hypercohomology, with both
> sides identified with groups of morphisms by Stacks 08JA.

```lean
def derivedCurryHomEquiv :
    (K ⟶ ((derivedSheafHomBifunctor X).obj (op L)).obj M) ≃+
      (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L ⟶ M)
```

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingCounitFormula.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingCounitFormula.lean#L83). The attribute's comment: “the bijection is tensoring with the identity followed by the evaluation morphism”.

> **The tensor–internal-Hom bijection is tensoring and then evaluating.** For objects `K`, `A`,
> `B` of `D(O)` it carries `g : K ⟶ RSheafHom(A, B)` to
>
> `(g ⊗^𝐋_O 1_A) ≫ e`,
>
> with `e : RSheafHom(A, B) ⊗^𝐋_O A ⟶ B` the evaluation morphism
> `AlgebraicGeometry.RingedSite.derivedSheafHomCounit`.

```lean
theorem derivedCurryHomEquiv_apply
    (K A B : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (g : K ⟶ ((derivedSheafHomBifunctor Y).obj (op A)).obj B) :
    derivedCurryHomEquiv Y K A B g =
      ((Stacks.SheafOfModules.derivedTensorProductFunctor Y).map g).app A ≫
        derivedSheafHomCounit Y A B
```

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingHomEquivNaturality.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingHomEquivNaturality.lean#L73). The attribute's comment: “naturality of the tensor-internal-Hom bijection in all three objects”.

> **The tensor–internal-Hom bijection of Stacks 08J8 is natural in all three objects.** For
> morphisms `k : K' ⟶ K`, `l : L' ⟶ L` and `m : M ⟶ M'` of `D(O)`, the bijection carries a
> morphism `θ : K ⟶ RSheafHom(L, M)` precomposed with `k` and postcomposed with
> `RSheafHom(l, m)` to its transpose precomposed with the derived tensor product of `k` and `l`
> and postcomposed with `m`.

```lean
theorem derivedCurryHomEquiv_naturality
    {K K' L L' M M' :
      DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (k : K' ⟶ K) (l : L' ⟶ L) (m : M ⟶ M')
    (θ : K ⟶ ((derivedSheafHomBifunctor X).obj (op L)).obj M) :
    derivedCurryHomEquiv X K' L' M'
        (k ≫ θ ≫ (((derivedSheafHomBifunctor X).map l.op).app M ≫
          ((derivedSheafHomBifunctor X).obj (op L')).map m)) =
      (((Stacks.SheafOfModules.derivedTensorProductFunctor X).map k).app L' ≫
          ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).map l) ≫
        derivedCurryHomEquiv X K L M θ ≫ m
```

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_dinaturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingInternalHomNaturality.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingInternalHomNaturality.lean#L136). The attribute's comment: “dinaturality of the bijection of morphism groups in the internal-Hom variable”.

> **Stacks 08J8, dinaturality in the internal-Hom variable.** Postcomposing a morphism
> `h : A ⟶ RSheafHom(B, Z)` with the map `RSheafHom(B, Z) ⟶ RSheafHom(B', Z)` induced by
> `v : B' ⟶ B` corresponds, under the tensor–internal-Hom bijection, to precomposing the morphism
> `A ⊗^L_O B ⟶ Z` matched with `h` with `1 ⊗ v`.
>
> The variable `B` is contravariant on the left of the bijection and covariant on the right, so
> this is a dinaturality identity and not a naturality square.

```lean
theorem derivedCurryHomEquiv_dinaturality
    {B B' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (A Z : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (v : B' ⟶ B)
    (h : A ⟶ ((derivedSheafHomBifunctor X).obj (op B)).obj Z) :
    derivedCurryHomEquiv X A B' Z
        (h ≫ ((derivedSheafHomBifunctor X).map v.op).app Z) =
      ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj A).map v ≫
        derivedCurryHomEquiv X A B Z h
```

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_naturality_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrySourceNaturality.lean, line 537](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrySourceNaturality.lean#L537). The attribute's comment: “the tensor-internal-Hom bijection is natural in the source variable”.

> **Stacks 08J8 is natural in its source variable.** Precomposing a morphism
> `h : A ⟶ RSheafHom(B, Z)` with `u : A' ⟶ A` corresponds, under the tensor-internal-Hom
> bijection `derivedCurryHomEquiv`, to precomposing the morphism `A ⊗^L_O B ⟶ Z` matched with
> `h` by `u ⊗ 1`.
>
> The bijection is the derived currying isomorphism of Stacks 08J9 read on degree-zero global
> hypercohomology with both sides identified with morphism groups by Stacks 08JA, so this is the
> object-level naturality `derivedCurryIso_natural` together with the naturality of Stacks 08JA
> in its source variable,
> `derivedSheafHomGlobalSectionsEquiv_naturality_source`.

```lean
theorem derivedCurryHomEquiv_naturality_source
    {A A' B Z : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (u : A' ⟶ A)
    (h : A ⟶ ((derivedSheafHomBifunctor X).obj (op B)).obj Z) :
    derivedCurryHomEquiv X A' B Z (u ≫ h) =
      ((Stacks.SheafOfModules.derivedTensorProductFunctor X).map u).app B ≫
        derivedCurryHomEquiv X A B Z h
```

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_naturality_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryTargetNaturality.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryTargetNaturality.lean#L275). The attribute's comment: “the tensor-internal-Hom bijection is natural in the target variable”.

> **Stacks 08J8 is natural in its target variable.** Postcomposing a morphism
> `h : A ⟶ RSheafHom(B, Z)` with `RSheafHom(B, w)`, for `w : Z ⟶ Z'`, corresponds under the
> tensor–internal-Hom bijection `derivedCurryHomEquiv` to postcomposing the morphism
> `A ⊗^L_O B ⟶ Z` matched with `h` by `w`.
>
> The bijection is the derived currying isomorphism of Stacks 08J9 read on degree-zero global
> hypercohomology with both sides identified with morphism groups by Stacks 08JA, so this is the
> object-level naturality `derivedCurryIso_natural` together with the naturality of Stacks 08JA
> in its target variable, `derivedSheafHomGlobalSectionsEquiv_naturality_target_globalMap`.

```lean
theorem derivedCurryHomEquiv_naturality_target
    {A B Z Z' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (w : Z ⟶ Z')
    (h : A ⟶ ((derivedSheafHomBifunctor X).obj (op B)).obj Z) :
    derivedCurryHomEquiv X A B Z'
        (h ≫ ((derivedSheafHomBifunctor X).obj (op B)).map w) =
      derivedCurryHomEquiv X A B Z h ≫ w
```

**`AlgebraicGeometry.RingedSite.derivedTensorSheafHomAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryTargetNaturality.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryTargetNaturality.lean#L314). The attribute's comment: “the tensor-internal-Hom bijection as an adjunction, at a fixed middle object”.

> **Stacks 08J8 as an adjunction.** For an object `B` of `D(O)`, the derived tensor product
> with `B` is left adjoint to the derived internal Hom out of `B`:
>
> `Hom_{D(O)}(A ⊗^L_O B, Z) ≅ Hom_{D(O)}(A, RSheafHom(B, Z))`,
>
> naturally in `A` and `Z`. The bijection is `derivedCurryHomEquiv`, its naturality in `A` is
> `derivedCurryHomEquiv_naturality_source` and its naturality in `Z` is
> `derivedCurryHomEquiv_naturality_target`.

```lean
def derivedTensorSheafHomAdjunction
    (B : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (Stacks.SheafOfModules.derivedTensorProductFunctor X).flip.obj B ⊣
      (derivedSheafHomBifunctor X).obj (op B)
```

**`Stacks.Cohomology.DerivedInternalHomPullback.tensorHomEquivDinatural_ringedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackDinaturality.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackDinaturality.lean#L284). The attribute's comment: “dinaturality of the bijection of morphism groups of Tag 08DI in its internal-hom variable, read on a ringed space at the uncurried spelling of the derived tensor product; the companion clause in the source variable is tensorHomEquivNaturalLeft\_ringedSpace”.

> **The bijection of Tag 08DI on a ringed space is dinatural in its internal-hom variable.**
> This is `Transpose.TensorHomEquivDinatural` for the bijection of Tag 08DI, the companion of
> `tensorHomEquivNaturalLeft_ringedSpace`, and it is the clause the assembly of
> `Stacks.Cohomology.DerivedInternalHomStalk.InternalHomComparison` and the dévissage of Tag 0GM7
> in the perfect variable both ask for.
>
> The bijection is presented as the site-level `RingedSite.derivedCurryHomEquiv` of
> `Stacks.SheafOfModules.ringedSite Z.sheaf` rather than as
> `Stacks.SheafOfModules.derivedSheafHomTensorEquiv Z.sheaf`, which is the same family of additive
> equivalences; see the implementation notes of this file.  `convert … using 1` rather than `exact`
> for the reason recorded on `tensorHomEquivNaturalLeft_ringedSpace`: what is left to settle lives
> inside the `FunLike` instance of the coercion, where the two spellings of the derived tensor
> product and of the derived internal hom appear as instance arguments, and the congruence `convert`
> builds settles those argument by argument.

```lean
theorem tensorHomEquivDinatural_ringedSpace :
    Transpose.TensorHomEquivDinatural (Stacks.SheafOfModules.derivedSheafHom Z.sheaf)
      (internalHomTensorUncurried Z)
      (fun A B C => (RingedSite.derivedCurryHomEquiv
        (Stacks.SheafOfModules.ringedSite Z.sheaf) A B C).toEquiv)
```

## Tag 08JA, a lemma

[Tag 08JA](https://stacks.math.columbia.edu/tag/08JA) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedSheafHomGlobalSectionsEquiv_naturality_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrySourceNaturality.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrySourceNaturality.lean#L446). The attribute's comment: “global sections, naturality in the source variable”.

> **Stacks 08JA globally is natural in the source variable, for an arbitrary morphism of
> `D(O)`**: the identification of the degree-zero global hypercohomology of `RSheafHom(L, M)`
> with `Hom_{D(O)}(L, M)` carries the map induced by `u : L' ⟶ L` to precomposition with `u`.
>
> This is the global half of the naturality of Stacks 0A94 read at arbitrary objects of `D(O)`:
> the two sides are compared at the chosen K-flat representative of the source and the chosen
> K-injective representative of the target, where it is
> `derivedSheafHomGlobalSectionsEquivOfKFlat_naturality_derived`.

```lean
theorem derivedSheafHomGlobalSectionsEquiv_naturality_source
    {A A' W : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (u : A' ⟶ A)
    (x : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        (((derivedSheafHomBifunctor X).obj (op A)).obj W)) : Type u)) :
    derivedSheafHomGlobalSectionsEquiv X A' W (derivedHomGlobalMap X u (𝟙 W) x) =
      u ≫ derivedSheafHomGlobalSectionsEquiv X A W x
```

**`AlgebraicGeometry.RingedSite.derivedSheafHomGlobalSectionsEquiv_naturality_target_globalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryTargetNaturality.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryTargetNaturality.lean#L168). The attribute's comment: “global sections, naturality in the target variable”.

> **Stacks 08JA globally is natural in the target variable, for an arbitrary morphism of
> `D(O)`**: the identification of the degree-zero global hypercohomology of `RSheafHom(A, W)`
> with `Hom_{D(O)}(A, W)` carries the map induced by `v : W ⟶ W'` to postcomposition with `v`.
>
> This is the target half of the naturality of Stacks 0A94 read at arbitrary objects of `D(O)`:
> the two sides are compared at the chosen K-flat representative of the source and the chosen
> K-injective representatives of the two targets, where it is
> `derivedSheafHomGlobalSectionsEquivOfKFlat_naturality_derived_snd`.

```lean
theorem derivedSheafHomGlobalSectionsEquiv_naturality_target_globalMap
    {A W W' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (v : W ⟶ W')
    (x : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        (((derivedSheafHomBifunctor X).obj (op A)).obj W)) : Type u)) :
    derivedSheafHomGlobalSectionsEquiv X A W' (derivedHomGlobalMap X (𝟙 A) v x) =
      derivedSheafHomGlobalSectionsEquiv X A W x ≫ v
```

**`AlgebraicGeometry.RingedSite.derivedSheafHomGlobalSectionsEquiv_naturality_bifunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsNaturality.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsNaturality.lean#L239). The attribute's comment: “global sections, naturality in both variables”.

> **Stacks 08JA globally is natural in both variables.** For arbitrary morphisms `f : L' ⟶ L`
> and `g : M ⟶ M'` of `D(O)`, the identification of the degree-zero global hypercohomology of
> `RSheafHom(L, M)` with `Hom_{D(O)}(L, M)` carries the derived internal Hom of `f` and `g` to
> precomposition with `f` and postcomposition with `g`.

```lean
theorem derivedSheafHomGlobalSectionsEquiv_naturality_bifunctor
    {L L' M M' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (f : L' ⟶ L) (g : M ⟶ M')
    (z : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        (((derivedSheafHomBifunctor X).obj (op L)).obj M)) : Type u)) :
    derivedSheafHomGlobalSectionsEquiv X L' M'
        ((derivedSheafHomGlobalSectionsFunctor X).map
          ((f.op, g) : ((op L, M) :
            (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))ᵒᵖ ×
              DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) ⟶
            (op L', M')) z) =
      f ≫ derivedSheafHomGlobalSectionsEquiv X L M z ≫ g
```

**`AlgebraicGeometry.RingedSite.derivedSheafHomGlobalSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsOnDerivedObjects.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsOnDerivedObjects.lean#L227). The attribute's comment: “global sections”. References: SGA 6 I (8.1), “partial”.

> **Stacks 08JA globally.** For arbitrary objects `L`, `M` of `D(O)` the degree-zero global
> hypercohomology of the derived internal Hom `RSheafHom(L, M)` is the group of morphisms
> `L ⟶ M` in the derived category of `O`-modules.
>
> A K-injective complex representing `M` and a K-flat complex representing `L` are chosen; the
> internal Hom complex between them is K-injective by Stacks 0A96, so global sections compute
> derived global sections and the degree-zero cohomology is the group of derived-category
> morphisms, by Stacks 0A94.

```lean
def derivedSheafHomGlobalSectionsEquiv
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((derivedModuleGlobalSections X).obj
          (((derivedSheafHomBifunctor X).obj (op L)).obj M)) : Type u) ≃+ (L ⟶ M)
```

**`AlgebraicGeometry.RingedSite.derivedSheafHomSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsOnDerivedObjects.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsOnDerivedObjects.lean#L269). The attribute's comment: “sections over an object”.

> **Stacks 08JA over an object of the site.** For arbitrary objects `L`, `M` of `D(O)` the
> degree-zero hypercohomology over `U` of the derived internal Hom `RSheafHom(L, M)` is the
> group of morphisms `L|_U ⟶ M|_U` in the derived category of `O|_U`-modules.
>
> A K-injective complex representing `M` and a K-flat complex representing `L` are chosen; the
> internal Hom complex between them is K-injective by Stacks 0A96, so sections compute derived
> sections and the degree-zero cohomology is the group of derived-category morphisms between
> the restrictions, by Stacks 0A94.

```lean
def derivedSheafHomSectionsEquiv
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((Stacks.Cohomology.Localization.derivedSectionsOverObject X U).obj
          (((derivedSheafHomBifunctor X).obj (op L)).obj M)) : Type u) ≃+
      ((SheafOfModules.overFunctor.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U).mapDerivedCategory.obj L ⟶
        (SheafOfModules.overFunctor.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U).mapDerivedCategory.obj M)
```

**`AlgebraicGeometry.RingedSite.derivedSheafHomSectionsEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsOverAnObjectNaturality.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsOverAnObjectNaturality.lean#L475). The attribute's comment: “sections over an object, naturality in both variables”.

> **Stacks 08JA over an object of the site is natural in both variables.** For arbitrary
> morphisms `f : L' ⟶ L` and `g : M ⟶ M'` of `D(O)`, the identification of the degree-zero
> hypercohomology over `U` of `RSheafHom(L, M)` with `Hom_{D(O|_U)}(L|_U, M|_U)` carries the
> derived internal Hom of `f` and `g` to precomposition with `f|_U` and postcomposition with
> `g|_U`.

```lean
theorem derivedSheafHomSectionsEquiv_naturality
    {L L' M M' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (f : L' ⟶ L) (g : M ⟶ M')
    (z : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((Stacks.Cohomology.Localization.derivedSectionsOverObject X U).obj
        (((derivedSheafHomBifunctor X).obj (op L)).obj M)) : Type u)) :
    derivedSheafHomSectionsEquiv X U L' M'
        ((derivedSheafHomSectionsFunctor X U).map
          ((f.op, g) : ((op L, M) :
              (DerivedCategory
                (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))ᵒᵖ ×
              DerivedCategory (SheafOfModules.{u}
                (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) ⟶
              (op L', M')) z) =
      (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        U).mapDerivedCategory.map f ≫
        derivedSheafHomSectionsEquiv X U L M z ≫
          (SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
            U).mapDerivedCategory.map g
```

**`AlgebraicGeometry.RingedSite.derivedSheafHomGlobalSectionsEquiv_naturality_source_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsSourceNaturality.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsSourceNaturality.lean#L414). The attribute's comment: “global sections, naturality in the source”.

> **Stacks 08JA, naturality in the source variable.** For objects `L'`, `L`, `M` of `D(O)` and
> an arbitrary morphism `u : L' ⟶ L`, the identification of the degree-zero global
> hypercohomology of `RSheafHom(L, M)` with `Hom_{D(O)}(L, M)` carries the contravariant
> functoriality of the derived internal Hom to precomposition with `u`.

```lean
theorem derivedSheafHomGlobalSectionsEquiv_naturality_source_homologyMap
    {L L' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (u : L' ⟶ L)
    (x : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        (((derivedSheafHomBifunctor X).obj (op L)).obj M)) : Type u)) :
    derivedSheafHomGlobalSectionsEquiv X L' M
        ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
          ((derivedModuleGlobalSections X).map
            (((derivedSheafHomBifunctor X).map u.op).app M)) x) =
      u ≫ derivedSheafHomGlobalSectionsEquiv X L M x
```

**`AlgebraicGeometry.RingedSite.derivedSheafHomGlobalSectionsEquiv_naturality_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsTargetNaturality.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsTargetNaturality.lean#L338). The attribute's comment: “global sections, naturality in the target”.

> **Stacks 08JA, naturality in the target variable.** For objects `L`, `M`, `M'` of `D(O)` and
> an arbitrary morphism `φ : M ⟶ M'`, the identification of the degree-zero global
> hypercohomology of `RSheafHom(L, M)` with `Hom_{D(O)}(L, M)` carries the covariant
> functoriality of the derived internal Hom to postcomposition with `φ`.

```lean
theorem derivedSheafHomGlobalSectionsEquiv_naturality_target
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {M M' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (φ : M ⟶ M')
    (x : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        (((derivedSheafHomBifunctor X).obj (op L)).obj M)) : Type u)) :
    derivedSheafHomGlobalSectionsEquiv X L M'
        ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
          ((derivedModuleGlobalSections X).map
            (((derivedSheafHomBifunctor X).obj (op L)).map φ)) x) =
      derivedSheafHomGlobalSectionsEquiv X L M x ≫ φ
```

**`AlgebraicGeometry.RingedSite.globalDerivedHomDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHomShift.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalDerivedHomShift.lean#L186). The attribute's comment: “global sections in every degree, via the translation in the covariant variable”.

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

**`AlgebraicGeometry.RingedSite.derivedStructureSheafGlobalSectionsDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/StructureSheafHypercohomology.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/StructureSheafHypercohomology.lean#L72). The attribute's comment: “hypercohomology out of the structure sheaf in every degree”.

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

**`Stacks.SheafOfModules.derivedStructureSheafGlobalSectionsDegreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StructureSheafHypercohomologyOnASpace.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/StructureSheafHypercohomologyOnASpace.lean#L57). The attribute's comment: “hypercohomology of a ringed space out of the structure sheaf in every degree”.

> **Hypercohomology of a ringed space in every degree is morphisms out of the structure
> sheaf.** For an object `Z` of `D(O_X)` the hypercohomology group `H^n(X, Z)`, the degree-`n`
> homology of unbounded derived global sections, is `Hom_{D(O_X)}(O_X[0], Z[n])`.
>
> This is `AlgebraicGeometry.RingedSite.derivedStructureSheafGlobalSectionsDegreeEquiv` read at the
> site of opens of `X`.

```lean
def derivedStructureSheafGlobalSectionsDegreeEquiv
    (Z : DerivedCategory (StructureSheafModules Rc)) (n : ℤ) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} n).obj
        ((derivedModuleGlobalSections (ringedSite Rc)).obj Z) : Type u) ≃+
      (RingedSite.derivedStructureSheaf (ringedSite Rc) ⟶ Z⟦n⟧)
```

## Tag 08J9, a lemma

[Tag 08J9](https://stacks.math.columbia.edu/tag/08J9) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrying.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrying.lean#L235). The attribute's comment: “recovers the morphism-group bijection on H^0”.

> **The isomorphism of morphism groups is the derived currying isomorphism on global
> hypercohomology.** This is the last assertion of Stacks 08J9: taking degree-zero global
> hypercohomology of `derivedCurryIso` and identifying both sides with morphism groups by
> Stacks 08JA gives `derivedCurryHomEquiv`, the bijection (21.35.0.1) of Stacks 08J8.

```lean
theorem derivedCurryHomEquiv_globalSections
    (x : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        (((derivedSheafHomBifunctor X).obj (op K)).obj
          (((derivedSheafHomBifunctor X).obj (op L)).obj M))) : Type u)) :
    derivedCurryHomEquiv X K L M
        (derivedSheafHomGlobalSectionsEquiv X K
          (((derivedSheafHomBifunctor X).obj (op L)).obj M) x) =
      derivedSheafHomGlobalSectionsEquiv X
        (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L) M
        (derivedCurryGlobalEquiv X K L M x)
```

**`AlgebraicGeometry.RingedSite.derivedCurryHomEquiv_globalSections_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrying.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurrying.lean#L252). The attribute's comment: “recovers the morphism-group bijection on H^0”.

> `derivedCurryHomEquiv_globalSections` with the additive equivalence
> `derivedCurryGlobalEquiv` spelled out as the map induced by `derivedCurryIso`.

```lean
theorem derivedCurryHomEquiv_globalSections_homologyMap
    (x : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        (((derivedSheafHomBifunctor X).obj (op K)).obj
          (((derivedSheafHomBifunctor X).obj (op L)).obj M))) : Type u)) :
    derivedCurryHomEquiv X K L M
        (derivedSheafHomGlobalSectionsEquiv X K
          (((derivedSheafHomBifunctor X).obj (op L)).obj M) x) =
      derivedSheafHomGlobalSectionsEquiv X
        (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L) M
        ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
          ((derivedModuleGlobalSections X).map (derivedCurryIso X K L M).hom) x)
```

**`AlgebraicGeometry.RingedSite.derivedCurryNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingNaturality.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingNaturality.lean#L514). The attribute's comment: “functoriality in all three objects”. References: SGA 6 I (7.4), “first isomorphism”.

> **Stacks 08J9: the derived currying isomorphism is a natural isomorphism.** The canonical
> isomorphism
>
> `RSheafHom(K, RSheafHom(L, M)) ≅ RSheafHom(K ⊗^L_O L, M)`
>
> of `AlgebraicGeometry.RingedSite.derivedCurryIso`, bundled as an isomorphism between the
> trifunctor `(K, L, M) ↦ RSheafHom(K, RSheafHom(L, M))` and the trifunctor
> `(K, L, M) ↦ RSheafHom(K ⊗^L_O L, M)` on `D(O)ᵒᵖ × D(O)ᵒᵖ × D(O)`. It is obtained by extending
> the comparison on models.

```lean
def derivedCurryNatIso : iteratedHomFunctor X ≅ tensorHomFunctor X
```

**`AlgebraicGeometry.RingedSite.derivedCurryIso_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingNaturality.lean, line 559](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingNaturality.lean#L559). The attribute's comment: “functoriality in all three objects”. References: SGA 6 I (7.4), “functoriality, 1st iso”.

> **Functoriality of the derived currying isomorphism in all three objects.** For morphisms
> `k : K' ⟶ K`, `l : L' ⟶ L` and `m : M ⟶ M'` of `D(O)` the square formed by `derivedCurryIso`
> at `(K, L, M)` and at `(K', L', M')` commutes: the derived currying isomorphism is natural
> contravariantly in the source and in the middle object and covariantly in the target.

```lean
theorem derivedCurryIso_natural
    {K K' L L' M M' :
      DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (k : K' ⟶ K) (l : L' ⟶ L) (m : M ⟶ M') :
    ((derivedSheafHomBifunctor X).map k.op).app
          (((derivedSheafHomBifunctor X).obj (op L)).obj M) ≫
        ((derivedSheafHomBifunctor X).obj (op K')).map
          (((derivedSheafHomBifunctor X).map l.op).app M ≫
            ((derivedSheafHomBifunctor X).obj (op L')).map m) ≫
        (derivedCurryIso X K' L' M').hom =
      (derivedCurryIso X K L M).hom ≫
        ((derivedSheafHomBifunctor X).map
            ((((Stacks.SheafOfModules.derivedTensorProductFunctor X).map k).app L' ≫
              ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).map l).op)).app M ≫
          ((derivedSheafHomBifunctor X).obj
            (op (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K').obj L'))).map
              m
```

**`AlgebraicGeometry.RingedSite.derivedCurryIso_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingNaturality.lean, line 604](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCurryingNaturality.lean#L604). The attribute's comment: “comparison with currying of complexes”.

> **The comparison of Stacks 08J9 with the currying isomorphism of complexes of Stacks
> 0A90.** For complexes `A`, `B`, `I` with `B` K-flat and `I` K-injective, `derivedCurryIso` on
> the classes of `A`, `B`, `I` is, after the two identifications
>
> `RSheafHom(QA, RSheafHom(QB, QI)) ≅ Q SheafHom(A, SheafHom(B, I))` and
> `RSheafHom(QA ⊗^L_O QB, QI) ≅ Q SheafHom(Tot(A ⊗_O B), I)`,
>
> the class of the complex-level currying isomorphism `SheafHom(A, SheafHom(B, I)) ≅
> SheafHom(Tot(A ⊗\_O B), I)`.

```lean
theorem derivedCurryIso_comparison
    (A B I : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (hB : Stacks.SheafOfModules.IsKFlat X.O B) [I.IsKInjective] :
    (derivedCurryIso X (DerivedCategory.Q.obj A) (DerivedCategory.Q.obj B)
            (DerivedCategory.Q.obj I)).hom ≫
        (tensorHomRepresentativeIso X A B I hB).hom =
      (iteratedHomRepresentativeIso X A B I hB).hom ≫
        DerivedCategory.Q.map (sheafHomTensorCurryIso X A B I).hom
```

## Tag 08JB, a lemma

[Tag 08JB](https://stacks.math.columbia.edu/tag/08JB) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.DerivedHomRestriction.complexMap_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean, line 727](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean#L727). The attribute's comment: “restriction on local homogeneous cochains”.

> The component of the complex map restricts each local homogeneous map
> along the iterated slice, as in the canonical comparison of Tag 0E8H.

```lean
theorem DerivedHomRestriction.complexMap_apply
    (r : DerivedHomRestriction X U)
    (A B : CochainComplex (SheafOfModules.{u} (ringSheaf X.O)) ℤ)
    (V : (Over U)ᵒᵖ) (W : (Over V.unop)ᵒᵖ)
    (n p q : ℤ) (hpq : p + n = q)
    (s : ((sheafHomComplex X A B).obj.X n).val.obj (op V.unop.left))
    (x : ((restrictComplex (X.over U)
      (restrictComplex X A U) V.unop).X p).val.obj W) :
    (((AddCommGrpCat.Hom.hom
      (((sheafHomComplex (X.over U)
        (restrictComplex X A U) (restrictComplex X B U)).sectionsIso V.unop).hom.f n)
      (((r.complexMap A B).f n).val.app V s)).v p q hpq).val.app W x) =
      (((AddCommGrpCat.Hom.hom
        (((sheafHomComplex X A B).sectionsIso V.unop.left).hom.f n) s).v p q hpq).val.app
          (op (Over.mk W.unop.hom.left)) x)
```

**`AlgebraicGeometry.RingedSite.derivedHom_restriction_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean, line 809](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean#L809).

> Derived internal Hom commutes, naturally in both arguments, with
> restriction to the slice site over any object.

```lean
theorem derivedHom_restriction_exists :
    Nonempty (DerivedHomRestriction X U)
```

**`AlgebraicGeometry.RingedSite.derivedHomRestriction_complexMap_isRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean, line 864](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean#L864). The attribute's comment: “restriction of internal-Hom complexes”.

> Restriction of internal-Hom complexes is induced on every homogeneous
> component by the canonical internal-Hom restriction isomorphism of Tag 0E8H.

```lean
theorem derivedHomRestriction_complexMap_isRestriction
    (A B : CochainComplex (SheafOfModules.{u} (ringSheaf X.O)) ℤ) :
    IsInternalHomRestrictionMap X U A B
      ((derivedHomRestriction X U).complexMap A B)
```

**`AlgebraicGeometry.RingedSite.derivedHomRestriction_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean, line 874](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomRestriction.lean#L874). The attribute's comment: “canonical model characterization”.

> Under the fixed K-injective and exact-restriction comparisons, the full
> derived comparison is the localization of the restriction map of internal-Hom
> complexes induced by `Stacks.SheafOfModules.InternalHom.internalHomOverIso`.

```lean
theorem derivedHomRestriction_model
    (A B : CochainComplex (SheafOfModules.{u} (ringSheaf X.O)) ℤ) [B.IsKInjective] :
    ((derivedHomRestriction X U).iso
      (DerivedCategory.Q.obj A) (DerivedCategory.Q.obj B)).hom ≫
        (restrictionTargetComparison X U A B).hom =
      (restrictionSourceComparison X U A B).hom ≫
        DerivedCategory.Q.map ((derivedHomRestriction X U).complexMap A B)
```

## Tag 08JC, a lemma

[Tag 08JC](https://stacks.math.columbia.edu/tag/08JC) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_distinguished_derivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomTriangulated.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomTriangulated.lean#L174). The attribute's comment: “contravariant variable”.

> **Stacks 08JC, contravariant variable.**  The derived internal Hom into a fixed object carries
> a distinguished triangle of `D(O)` to a distinguished triangle: for any distinguished `T` and any
> `E`, the two morphisms `RSheafHom(T.obj₃, E) ⟶ RSheafHom(T.obj₂, E) ⟶ RSheafHom(T.obj₁, E)`
> induced by `T.mor₂` and `T.mor₁` extend by a connecting morphism to a distinguished triangle.
>
> Every distinguished triangle is presented by a termwise split short exact sequence of complexes,
> so this follows from
> `AlgebraicGeometry.RingedSite.exists_distinguished_derivedSheafHom_of_ses_obj`.

```lean
theorem exists_distinguished_derivedSheafHom
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (T : Triangle
      (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distTriang
      (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    ∃ δ : ((derivedSheafHomBifunctor X).flip.obj E).obj (op T.obj₁) ⟶
        (((derivedSheafHomBifunctor X).flip.obj E).obj (op T.obj₃))⟦(1 : ℤ)⟧,
      Triangle.mk
        (((derivedSheafHomBifunctor X).flip.obj E).map T.mor₂.op)
        (((derivedSheafHomBifunctor X).flip.obj E).map T.mor₁.op)
        δ ∈ distTriang
          (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
```

**`AlgebraicGeometry.RingedSite.exists_distinguished_derivedSheafHom_second`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/Exactness.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/Exactness.lean#L176). The attribute's comment: “covariant variable”.

> The derived internal Hom out of a fixed object carries a distinguished triangle of `D(O)` to
> a distinguished triangle: for any distinguished `T` and any `E`, the two morphisms
> `RSheafHom(E, T.obj₁) ⟶ RSheafHom(E, T.obj₂) ⟶ RSheafHom(E, T.obj₃)` induced by `T.mor₁` and
> `T.mor₂` extend by a connecting morphism to a distinguished triangle.

```lean
theorem exists_distinguished_derivedSheafHom_second
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (T : Triangle
      (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hT : T ∈ distTriang
      (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    ∃ δ : ((derivedSheafHomBifunctor X).obj (op E)).obj T.obj₃ ⟶
        (((derivedSheafHomBifunctor X).obj (op E)).obj T.obj₁)⟦(1 : ℤ)⟧,
      Triangle.mk
        (((derivedSheafHomBifunctor X).obj (op E)).map T.mor₁)
        (((derivedSheafHomBifunctor X).obj (op E)).map T.mor₂)
        δ ∈ distTriang
          (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
```

## Tag 0A97, a lemma

[Tag 0A97](https://stacks.math.columbia.edu/tag/0A97) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedEvaluation.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedEvaluation.lean#L505). The attribute's comment: “the canonical evaluation morphism”.

> **Stacks 0A97: the canonical evaluation morphism of derived internal Homs.** For arbitrary
> objects `K`, `L`, `M` of `D(Mod(O))` there is a canonical morphism
>
> `RSheafHom(L, M) ⊗^L_O K ⟶ RSheafHom(RSheafHom(K, L), M)`.

```lean
def derivedEvaluation
    (K L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor.{u, u, d} X).obj
        (((derivedInternalHomFunctor.{u, d} X).obj (op L)).obj M)).obj K ⟶
      ((derivedInternalHomFunctor.{u, d} X).obj
        (op (((derivedInternalHomFunctor.{u, d} X).obj (op K)).obj L))).obj M
```

**`AlgebraicGeometry.RingedSite.derivedEvaluation_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedEvaluation.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedEvaluation.lean#L517). The attribute's comment: “comparison with evaluation of complexes”.

> **Stacks 0A97.** On a K-flat source and K-injective targets, the canonical evaluation
> morphism is the class of the evaluation morphism of internal Hom complexes of Stacks 0A92.

```lean
theorem derivedEvaluation_model
    (A B C : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (hA : Stacks.SheafOfModules.IsKFlat X.O A) [B.IsKInjective] [C.IsKInjective] :
    derivedEvaluation X (DerivedCategory.Q.obj A) (DerivedCategory.Q.obj B)
          (DerivedCategory.Q.obj C) ≫
        (derivedEvaluationTargetComparison X (canonicalDerivedInternalHom.{u, d} X)
          A B C).hom =
      (derivedEvaluationSourceComparison X
          (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u, u, d} X)
          (canonicalDerivedInternalHom.{u, d} X) A B C hA).hom ≫
        DerivedCategory.Q.map (evaluationMap X A B C)
```

**`AlgebraicGeometry.RingedSite.derivedEvaluation_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedEvaluation.lean, line 533](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedEvaluation.lean#L533). The attribute's comment: “functoriality in all three objects”.

> **Stacks 0A97.** The canonical evaluation morphism is natural in the source object and in
> the target object, and contranatural in the intermediate object.

```lean
theorem derivedEvaluation_natural
    {K K' L L' M M' :
      DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (f : K ⟶ K') (g : L' ⟶ L) (h : M ⟶ M') :
    derivedEvaluation X K L M ≫
        ((derivedInternalHomFunctor.{u, d} X).map
          ((((derivedInternalHomFunctor.{u, d} X).obj (op K')).map g ≫
            ((derivedInternalHomFunctor.{u, d} X).map f.op).app L).op)).app M ≫
        ((derivedInternalHomFunctor.{u, d} X).obj
          (op (((derivedInternalHomFunctor.{u, d} X).obj (op K')).obj L'))).map h =
      ((Stacks.SheafOfModules.derivedTensorProductFunctor.{u, u, d} X).map
          (((derivedInternalHomFunctor.{u, d} X).map g.op).app M ≫
            ((derivedInternalHomFunctor.{u, d} X).obj (op L')).map h)).app K ≫
        ((Stacks.SheafOfModules.derivedTensorProductFunctor.{u, u, d} X).obj
          (((derivedInternalHomFunctor.{u, d} X).obj (op L')).obj M')).map f ≫
        derivedEvaluation X K' L' M'
```

## Tag 0A98, a lemma

[Tag 0A98](https://stacks.math.columbia.edu/tag/0A98) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedSheafHomCompositionConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCompositionConstruction.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedCompositionConstruction.lean#L263).

> **Stacks 0A98: the composition morphism of derived internal Homs.** For arbitrary objects
> `K`, `L`, `M` of `D(Mod(O))` there is a canonical morphism
>
> `RSheafHom(L, M) ⊗^L_O RSheafHom(K, L) ⟶ RSheafHom(K, M)`,
>
> which on a K-flat model of the second internal Hom complex is the composition morphism of
> internal Hom complexes of Stacks 0A91, and which is contravariant in the source, covariant in
> the target and dinatural in the intermediate object.

```lean
def derivedSheafHomCompositionConstruction : DerivedSheafHomComposition X T Hd
```

## Tag 0BYU, a lemma

[Tag 0BYU](https://stacks.math.columbia.edu/tag/0BYU) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedTensorHomInterchange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorHomInterchange.lean, line 568](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorHomInterchange.lean#L568). The attribute's comment: “the canonical morphism”.

> **Stacks 0BYU.** For objects `K`, `L`, `M` of `D(O)` there is a canonical morphism
>
> `K ⊗^L_O RSheafHom(M, L) ⟶ RSheafHom(M, K ⊗^L_O L)`
>
> in `D(O)`: on a K-flat representative `A` of `K`, a K-injective representative `I` of `L` and
> an arbitrary representative `C` of `M` it is the interchange morphism of complexes of Stacks
> 0BYT, followed by the augmentation of `Tot(A ⊗_O I)` into a K-injective resolution.

```lean
def derivedTensorHomInterchange
    (K L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj
        (((derivedSheafHomBifunctor X).obj (op M)).obj L) ⟶
      ((derivedSheafHomBifunctor X).obj (op M)).obj
        (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L)
```

**`AlgebraicGeometry.RingedSite.derivedTensorHomInterchange_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorHomInterchange.lean, line 597](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorHomInterchange.lean#L597). The attribute's comment: “comparison with the interchange morphism of complexes”.

> **The comparison of Stacks 0BYU with the interchange morphism of complexes of Stacks
> 0BYT.** For complexes `A`, `I`, `C` with `A` K-flat and `I` K-injective, the canonical morphism
> on their classes is, after the two identifications
>
> `QA ⊗^L_O RSheafHom(QC, QI) ≅ Q Tot(A ⊗_O SheafHom(C, I))` and
> `RSheafHom(QC, QA ⊗^L_O QI) ≅ Q SheafHom(C, J)` with `J` the chosen K-injective resolution of
> `Tot(A ⊗_O I)`,
>
> the class of the interchange morphism of complexes `Tot(A ⊗\_O SheafHom(C, I)) ⟶
> SheafHom(C, Tot(A ⊗\_O I))` followed by the resolution augmentation.

```lean
theorem derivedTensorHomInterchange_comparison
    (A I C : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (hA : Stacks.SheafOfModules.IsKFlat X.O A) [I.IsKInjective] :
    derivedTensorHomInterchange X (DerivedCategory.Q.obj A) (DerivedCategory.Q.obj I)
          (DerivedCategory.Q.obj C) ≫
        (interchangeTargetIso X A I C hA).hom =
      (interchangeSourceIso X A I C hA).hom ≫
        DerivedCategory.Q.map (tensorHomInterchange X A I C ≫
          homMap X (𝟙 C) ((kInjectiveAugmentation X).app (tensorTotal X A I)))
```

**`AlgebraicGeometry.RingedSite.derivedTensorHomInterchange_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorHomInterchange.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorHomInterchange.lean#L615). The attribute's comment: “functoriality in all three objects”.

> **Functoriality of the interchange morphism of Stacks 0BYU in all three objects.** For
> morphisms `k : K ⟶ K'`, `l : L ⟶ L'` and `m : M' ⟶ M` of `D(O)` the square formed by the
> canonical morphism at `(K, L, M)` and at `(K', L', M')` commutes: the interchange morphism is
> natural covariantly in the tensor factor and in the target of the internal Hom and
> contravariantly in its source.

```lean
theorem derivedTensorHomInterchange_natural
    {K K' L L' M M' :
      DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (k : K ⟶ K') (l : L ⟶ L') (m : M' ⟶ M) :
    ((Stacks.SheafOfModules.derivedTensorProductFunctor X).map k).app
          (((derivedSheafHomBifunctor X).obj (op M)).obj L) ≫
        ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K').map
          (((derivedSheafHomBifunctor X).map m.op).app L ≫
            ((derivedSheafHomBifunctor X).obj (op M')).map l) ≫
        derivedTensorHomInterchange X K' L' M' =
      derivedTensorHomInterchange X K L M ≫
        ((derivedSheafHomBifunctor X).map m.op).app
            (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L) ≫
          ((derivedSheafHomBifunctor X).obj (op M')).map
            (((Stacks.SheafOfModules.derivedTensorProductFunctor X).map k).app L ≫
              ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K').map l)
```

## Tag 0A99, a lemma

[Tag 0A99](https://stacks.math.columbia.edu/tag/0A99) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.canonicalDerivedDiagonal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean#L336). The attribute's comment: “the canonical morphism”.

> **Stacks 0A99.** For objects `K`, `L` of `D(O)` the canonical morphism
>
> `K ⟶ RSheafHom(L, K ⊗_O^L L)`
>
> in `D(O)`: on the chosen K-flat representative `A` of `K` and the chosen K-injective
> representative `B` of `L` it is the diagonal morphism of complexes of Stacks 0A93, followed by
> the augmentation of `Tot(A ⊗_O B)` into its chosen K-injective resolution.

```lean
def canonicalDerivedDiagonal
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    K ⟶ ((derivedSheafHomBifunctor X).obj (op L)).obj
      (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L)
```

**`AlgebraicGeometry.RingedSite.canonicalDerivedDiagonal_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean#L348). The attribute's comment: “the characterisation on representatives”.

> **The canonical morphism of Stacks 0A99 is the class of the resolved diagonal of complexes**,
> read through the comparisons of its source and target with classes of complexes.  In particular
> it is not an arbitrary morphism between the two objects.

```lean
theorem canonicalDerivedDiagonal_eq
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (kFlatModelIso X K).hom ≫ canonicalDerivedDiagonal X K L ≫
        (diagonalTargetIso X K L L).hom =
      DerivedCategory.Q.map (diagonalComplexMap X (kFlatModel X K) (kInjectiveModel X L))
```

**`AlgebraicGeometry.RingedSite.canonicalDerivedDiagonal_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean#L530). The attribute's comment: “functoriality in L”.

> **Stacks 0A99: the canonical morphism is functorial in `L`.** For a morphism `l : L' ⟶ L` of
> `D(O)` the square
>
> `u_{K,L} ≫ RSheafHom(l, 𝟙) = u_{K,L'} ≫ RSheafHom(𝟙, 𝟙_K ⊗ l)`
>
> commutes in `D(O)`: the second variable of the diagonal acts contravariantly in the source of
> the internal Hom and covariantly inside the derived tensor product, which is the dinaturality
> that the statement of the tag asserts.
>
> The chosen representative of `L` is K-injective, so `l` is the class of a morphism of the chosen
> representatives and the square is the dinaturality of Stacks 0A93 at the level of complexes,
> conjugated by the target comparisons.

```lean
theorem canonicalDerivedDiagonal_natural_right
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {L L' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (l : L' ⟶ L) :
    canonicalDerivedDiagonal X K L ≫
        ((derivedSheafHomBifunctor X).map l.op).app
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj L) =
      canonicalDerivedDiagonal X K L' ≫
        ((derivedSheafHomBifunctor X).obj (op L')).map
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).map l)
```

**`AlgebraicGeometry.RingedSite.canonicalDerivedDiagonal_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean, line 774](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedDiagonal.lean#L774). The attribute's comment: “functoriality in K”.

> **Stacks 0A99: the canonical morphism is functorial in `K`.** For a morphism `f : K ⟶ K'` of
> `D(O)` the square
>
> `f ≫ u_{K',L} = u_{K,L} ≫ RSheafHom(𝟙_L, f ⊗ 𝟙_L)`
>
> commutes in `D(O)`: the first variable of the diagonal acts covariantly.
>
> A morphism of `D(O)` does not lift to the chosen K-flat representatives, which are not
> K-injective.  It is instead written as a right fraction `inv (Q s₀) ≫ Q g₀`
> (`DerivedCategory.right_fac`) and the apex of that roof is replaced by a K-flat resolution of it
> (Stacks 06YS), giving a roof `A ⟵ P ⟶ A'` with all three complexes K-flat and the left leg
> invertible in `D(O)`.  The one-sided K-flat comparison of Stacks 06YU is then available at all
> three vertices, which makes the tensored left leg invertible with no K-flatness of the other
> factor, and the square closes from the complex-level functoriality of Stacks 0A93.

```lean
theorem canonicalDerivedDiagonal_natural_left
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {K K' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (f : K ⟶ K') :
    f ≫ canonicalDerivedDiagonal X K' L =
      canonicalDerivedDiagonal X K L ≫
        ((derivedSheafHomBifunctor X).obj (op L)).map
          (((Stacks.SheafOfModules.derivedTensorProductFunctor X).map f).app L)
```

## Tag 08JD, a lemma

[Tag 08JD](https://stacks.math.columbia.edu/tag/08JD) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedTensorDualGlobalSectionsMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsTargetNaturality.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedSectionsTargetNaturality.lean#L424). The attribute's comment: “functoriality in M of the map on degree-zero derived global sections”.

> **The map of Stacks 08JD on degree-zero global hypercohomology is natural in `M`.** For
> `m : M ⟶ M'` the map `H⁰(C, M ⊗^L_O L^∨) ⟶ Hom_{D(O)}(L, M)` of
> `AlgebraicGeometry.RingedSite.derivedTensorDualGlobalSectionsMap` carries the map induced by `m`
> on the left to postcomposition with `m` on the right.
>
> That map is the degree-zero global hypercohomology of the canonical map
> `M ⊗^L_O L^∨ ⟶ RSheafHom(L, M)` followed by Stacks 08JA, so this is the naturality in `M` of
> those two pieces: `derivedTensorDualSectionsMap_naturality` for the first, and
> `derivedSheafHomGlobalSectionsEquiv_naturality_target` above for the second. No bijectivity of the
> map, hence no perfectness of `L`, is involved: this is functoriality of the comparison of Stacks
> 08JD, not Stacks 08DQ.

```lean
theorem derivedTensorDualGlobalSectionsMap_naturality
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {M M' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (m : M ⟶ M')
    (z : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections X).obj
        ((T.tensor.obj M).obj (derivedDual X L))) : Type u)) :
    derivedTensorDualGlobalSectionsMap X T L M'
        ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
          ((derivedModuleGlobalSections X).map
            ((T.tensor.map m).app (derivedDual X L))) z) =
      derivedTensorDualGlobalSectionsMap X T L M z ≫ m
```

**`AlgebraicGeometry.RingedSite.derivedTensorDualToSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorDual.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorDual.lean#L169). The attribute's comment: “the canonical map”.

> **Stacks 08JD: the canonical map `M ⊗^L_O L^∨ ⟶ RSheafHom(L, M)`.** It is the composition
> morphism of derived internal Homs of Stacks 0A98, taken at intermediate object the structure
> sheaf, after the left tensor factor `M` has been identified with `RSheafHom(O, M)`.

```lean
def derivedTensorDualToSheafHom
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (T.tensor.obj M).obj (derivedDual X L) ⟶
      ((derivedSheafHomBifunctor X).obj (op L)).obj M
```

**`AlgebraicGeometry.RingedSite.derivedTensorDualGlobalSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorDual.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedTensorDual.lean#L303). The attribute's comment: “map on degree-zero derived global sections”.

> **Stacks 08JD: the canonical map on degree-zero global hypercohomology.** The canonical map
> `M ⊗^L_O L^∨ ⟶ RSheafHom(L, M)` induces a map of abelian groups
>
> `H⁰(C, M ⊗^L_O L^∨) ⟶ Hom_{D(O)}(L, M)`,
>
> namely its degree-zero global hypercohomology followed by the identification
> `H⁰(C, RSheafHom(L, M)) ≅ Hom_{D(O)}(L, M)` of Stacks 08JA.

```lean
def derivedTensorDualGlobalSectionsMap
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
        ((derivedModuleGlobalSections X).obj
          ((T.tensor.obj M).obj (derivedDual X L))) : Type u) →+ (L ⟶ M)
```

## Tag 0B6D, a remark

[Tag 0B6D](https://stacks.math.columbia.edu/tag/0B6D) in the Stacks Project.

**`Stacks.Cohomology.ProjectionFormulaInternalHomOnRingedTopoi.derivedPushforwardSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/ProjectionFormulaInternalHom.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/ProjectionFormulaInternalHom.lean#L403). The attribute's comment: “the canonical map, variant: the special case of a morphism of ringed topoi presented by a morphism of sites; the tag for an arbitrary morphism of ringed topoi is Stacks.Cohomology.PushforwardInternalHomOfToposHom.derivedPushforwardSheafHomMap”.

> The canonical map of [Stacks, Tag 0B6D] when the morphism of ringed topoi
> `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` comes from a morphism of sites: for objects `L`, `M` of
> `D(O_C)`, the map
>
> `Rf_*RHom_{O_C}(L, M) ⟶ RHom_{O_D}(Rf_*L, Rf_*M)`.
>
> It is the morphism which the tensor–internal-Hom bijection of [Stacks, Tag 08J8] on `D(O_D)`
> sends to the relative cup product of [Stacks, Tag 0B6C] followed by `Rf_*` of the evaluation
> morphism `RHom_{O_C}(L, M) ⊗^L_{O_C} L ⟶ M`.

```lean
def derivedPushforwardSheafHomMap
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedPushforward f).obj
        (((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite X)).obj (op L)).obj M) ⟶
      ((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite Y)).obj
        (op ((derivedPushforward f).obj L))).obj ((derivedPushforward f).obj M)
```

**`Stacks.Cohomology.ProjectionFormulaInternalHomOnRingedTopoi.derivedPushforwardSheafHomMap_homEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/ProjectionFormulaInternalHom.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/ProjectionFormulaInternalHom.lean#L435). The attribute's comment: “the defining adjunction property, variant: the special case of a morphism of ringed topoi presented by a morphism of sites; the tag for an arbitrary morphism of ringed topoi is Stacks.Cohomology.PushforwardInternalHomOfToposHom.derivedPushforwardSheafHomMap\_homEquiv”.

> **The defining property of the canonical map of [Stacks, Tag 0B6D]**: its adjunct under the
> tensor–internal-Hom bijection of [Stacks, Tag 08J8] on `D(O_D)` is the relative cup product of
> [Stacks, Tag 0B6C] followed by `Rf_*` of the evaluation morphism
> `RHom_{O_C}(L, M) ⊗^L_{O_C} L ⟶ M`.

```lean
theorem derivedPushforwardSheafHomMap_homEquiv
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedTensorHomBijection (RingedTopos.toRingedSite Y)).homEquiv
        ((derivedPushforward f).obj
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite X)).obj (op L)).obj M))
        ((derivedPushforward f).obj L) ((derivedPushforward f).obj M)
        (derivedPushforwardSheafHomMap f hmos L M) =
      relativeCupProduct f hmos
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite X)).obj (op L)).obj M) L ≫
        (derivedPushforward f).map
          ((derivedTensorHomBijection (RingedTopos.toRingedSite X)).evaluation L M)
```

**`Stacks.Cohomology.PushforwardInternalHomOfToposHom.derivedPushforwardSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/PushforwardInternalHomOfToposHom.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/PushforwardInternalHomOfToposHom.lean#L210). The attribute's comment: “the canonical map, for an arbitrary morphism of ringed topoi (no morphism-of-sites hypothesis); its defining property is `derivedPushforwardSheafHomMap_homEquiv`”.

> **[Stacks, Tag 0B6D].**  For a morphism of ringed topoi
> `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and objects `L`, `M` of `D(O_C)`, the canonical map
>
> `Rf_*RHom_{O_C}(L, M) ⟶ RHom_{O_D}(Rf_*L, Rf_*M)`.
>
> It is the morphism which the tensor–internal-Hom bijection of [Stacks, Tag 08J8] on `D(O_D)`
> sends to the relative cup product
> `Rf_*RHom(L, M) ⊗^L_{O_D} Rf_*L ⟶ Rf_*(RHom(L, M) ⊗^L_{O_C} L)` of [Stacks, Tag 0B6C] followed
> by `Rf_*` of the evaluation morphism `RHom_{O_C}(L, M) ⊗^L_{O_C} L ⟶ M`.

```lean
def derivedPushforwardSheafHomMap
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedPushforward f).obj
        (((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite X)).obj (op L)).obj M) ⟶
      ((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite Y)).obj
        (op ((derivedPushforward f).obj L))).obj ((derivedPushforward f).obj M)
```

**`Stacks.Cohomology.PushforwardInternalHomOfToposHom.derivedPushforwardSheafHomMap_homEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/PushforwardInternalHomOfToposHom.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/PushforwardInternalHomOfToposHom.lean#L240). The attribute's comment: “the defining property: the 08J8 adjunct of the canonical map is the relative cup product of 0B6C followed by Rf\_* of evaluation, for an arbitrary morphism of ringed topoi”.

> **The defining property of the canonical map of [Stacks, Tag 0B6D]**: its adjunct under the
> tensor–internal-Hom bijection of [Stacks, Tag 08J8] on `D(O_D)` is the relative cup product of
> [Stacks, Tag 0B6C] followed by `Rf_*` of the evaluation morphism
> `RHom_{O_C}(L, M) ⊗^L_{O_C} L ⟶ M`.

```lean
theorem derivedPushforwardSheafHomMap_homEquiv
    (L M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedTensorHomBijection (RingedTopos.toRingedSite Y)).homEquiv
        ((derivedPushforward f).obj
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite X)).obj (op L)).obj M))
        ((derivedPushforward f).obj L) ((derivedPushforward f).obj M)
        (derivedPushforwardSheafHomMap f L M) =
      relativeCupProduct f
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite X)).obj (op L)).obj M) L ≫
        (derivedPushforward f).map
          ((derivedTensorHomBijection (RingedTopos.toRingedSite X)).evaluation L M)
```

## Tag 08JF, a remark

[Tag 08JF](https://stacks.math.columbia.edu/tag/08JF) in the Stacks Project.

**`AlgebraicGeometry.RingedToposSiteHom.derivedPullbackSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedPullbackOfInternalHom.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedPullbackOfInternalHom.lean#L176).

> **Stacks 08JF: the canonical map `Lh^* RSheafHom(K, L) ⟶ RSheafHom(Lh^* K, Lh^* L)`** in
> `D(O)`, for a morphism of ringed topoi `h : (Sh(C), O) ⟶ (Sh(C'), O')` and objects `K`, `L` of
> `D(O')`. It is the arrow corresponding to `derivedPullbackSheafHomPairing` under the
> tensor–internal-Hom bijection of Stacks 08J8 on the source topos.

```lean
def derivedPullbackSheafHomMap :
    (derivedPullback h).obj
        (((RingedSite.derivedSheafHomBifunctor
          (RingedTopos.toRingedSite Y)).obj (op K)).obj L) ⟶
      ((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite X)).obj
        (op ((derivedPullback h).obj K))).obj ((derivedPullback h).obj L)
```

**`AlgebraicGeometry.RingedToposHom.derivedPullbackSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedPullbackOfInternalHomOfToposHom.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedPullbackOfInternalHomOfToposHom.lean#L110). The attribute's comment: “for a morphism of ringed topoi in the sense of Tag 01D3, part (2) -- a morphism of the underlying topoi together with the map of structure sheaves, with no functor between the underlying sites”.

> **Stacks 08JF: the canonical map `Lh^* RSheafHom(K, L) ⟶ RSheafHom(Lh^* K, Lh^* L)`** in
> `D(O)`, for a morphism of ringed topoi `h : (Sh(C), O) ⟶ (Sh(C'), O')` in the sense of
> Stacks 01D3, part (2), and objects `K`, `L` of `D(O')`. It is the arrow corresponding to
> `derivedPullbackSheafHomPairing` under the tensor–internal-Hom bijection of Stacks 08J8.

```lean
def derivedPullbackSheafHomMap :
    (derivedPullback h).obj
        (((RingedSite.derivedSheafHomBifunctor
          (RingedTopos.toRingedSite Y)).obj (op K)).obj L) ⟶
      ((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite X)).obj
        (op ((derivedPullback h).obj K))).obj ((derivedPullback h).obj L)
```

## Tag 08JG, a remark

[Tag 08JG](https://stacks.math.columbia.edu/tag/08JG) in the Stacks Project.

**`Stacks.Cohomology.DerivedInternalHomBaseChangeOnTopoi.derivedBaseChangeSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHom.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHom.lean#L175). The attribute's comment: “derived\_base\_change\_sheaf\_hom\_map, variant: the special case of a square of morphisms of ringed topoi presented by morphisms of sites; the tag for an arbitrary commutative square of morphisms of ringed topoi is Stacks.Cohomology.DerivedInternalHomBaseChangeOfToposHom.derivedBaseChangeSheafHomMap”.

> The base change map for the internal hom in the derived category (Stacks 08JG), for a square
> of morphisms of sites.  For a
> commutative square of ringed topoi with `h : (Sh(C'), O_{C'}) ⟶ (Sh(C), O_C)` over
> `g : (Sh(D'), O_{D'}) ⟶ (Sh(D), O_D)` and objects `K`, `L` of `D(O_C)`, the canonical map
>
> `Lg^* Rf_* RSheafHom(K, L) ⟶ R(f')_* RSheafHom(Lh^* K, Lh^* L)`
>
> in `D(O_{D'})`.  It is the derived base change map of Stacks 07A7 at `RSheafHom(K, L)` followed
> by `R(f')_*` of the canonical map of Stacks 08JF, which is the adjoint of the three-step
> composition the source describes.

```lean
def derivedBaseChangeSheafHomMap :
    (derivedPullback g).obj
        ((derivedPushforward f).obj
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ⟶
      (derivedPushforward f').obj
        (((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite C')).obj
            (op ((derivedPullback h).obj K))).obj ((derivedPullback h).obj L))
```

**`Stacks.Cohomology.DerivedInternalHomBaseChangeOnTopoi.derivedBaseChangeSheafHomMap_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHom.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHom.lean#L201). The attribute's comment: “derived\_base\_change\_sheaf\_hom\_map: adjoint characterization, variant: the special case of a square of morphisms of ringed topoi presented by morphisms of sites; the tag for an arbitrary commutative square of morphisms of ringed topoi is Stacks.Cohomology.DerivedInternalHomBaseChangeOfToposHom.derivedBaseChangeSheafHomMap\_adjoint”.

> The adjoint characterization of the base change map (Stacks 08JG), for a square of morphisms
> of sites.  Under the derived adjunction
> `L(f')^* ⊣ R(f')_*` of Stacks 07A6, the base change map for the internal hom is the three-step
> composition the source prescribes: the two identifications of the iterated derived pullbacks
> around the square with the derived pullback along its common composite, then the derived
> pullback along `h` of the derived counit `Lf^* Rf_* ⟶ id` at `RSheafHom(K, L)`, then the
> canonical map of Stacks 08JF.
>
> Since transposition is a bijection this determines the map.

```lean
theorem derivedBaseChangeSheafHomMap_adjoint :
    ((derivedAdjunction f' hmosf').homEquiv
        ((derivedPullback g).obj ((derivedPushforward f).obj
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite C)).obj (op K)).obj L)))
        (((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite C')).obj
            (op ((derivedPullback h).obj K))).obj ((derivedPullback h).obj L))).symm
        (derivedBaseChangeSheafHomMap f h f' g hmosf hmosh hmosf' hmosg sq K L) =
      (derivedPullbackCompIsoLeft f' g hmosf' hmosg).hom.app
          ((derivedPushforward f).obj
            (((RingedSite.derivedSheafHomBifunctor
              (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ≫
        (derivedPullbackCompIsoRight f h f' g hmosf hmosh sq).inv.app
          ((derivedPushforward f).obj
            (((RingedSite.derivedSheafHomBifunctor
              (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ≫
        (derivedPullback h).map ((derivedAdjunction f hmosf).counit.app
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ≫
        RingedToposSiteHom.derivedPullbackSheafHomMap h hmosh K L
```

**`Stacks.Cohomology.DerivedInternalHomBaseChangeOfToposHom.derivedBaseChangeSheafHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHomOfToposHom.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHomOfToposHom.lean#L117). The attribute's comment: “for a commutative square of morphisms of ringed topoi in the sense of Tag 01D3, part (2), with no hypothesis beyond commutativity”.

> **Stacks 08JG: the base change map for the internal hom in the derived category.**  For a
> commutative square of morphisms of ringed topoi, with `h : (Sh(C'), O_{C'}) ⟶ (Sh(C), O_C)`
> over `g : (Sh(D'), O_{D'}) ⟶ (Sh(D), O_D)`, and objects `K`, `L` of `D(O_C)`, the canonical map
>
> `Lg^* Rf_* RSheafHom(K, L) ⟶ R(f')_* RSheafHom(Lh^* K, Lh^* L)`
>
> in `D(O_{D'})`: the derived base change map of Stacks 07A7 at `RSheafHom(K, L)` followed by
> `R(f')_*` of the canonical map of Stacks 08JF.  Its transpose is the three-step composition of
> the source, `derivedBaseChangeSheafHomMap_adjoint`.

```lean
def derivedBaseChangeSheafHomMap :
    (derivedPullback g).obj
        ((derivedPushforward f).obj
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ⟶
      (derivedPushforward f').obj
        (((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite C')).obj
            (op ((derivedPullback h).obj K))).obj ((derivedPullback h).obj L))
```

**`Stacks.Cohomology.DerivedInternalHomBaseChangeOfToposHom.derivedBaseChangeSheafHomMap_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHomOfToposHom.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedBaseChangeOfInternalHomOfToposHom.lean#L137). The attribute's comment: “adjoint characterization, for a commutative square of morphisms of ringed topoi in the sense of Tag 01D3, part (2)”.

> **Stacks 08JG, the adjoint characterization.**  Under the derived adjunction
> `L(f')^* ⊣ R(f')_*` of Stacks 07A6, the base change map for the internal hom is the composition
> the source prescribes: the identification `L(f')^* Lg^* = Lh^* Lf^*` of the iterated derived
> pullbacks around the square (through the derived pullback along its common composite), then
> `Lh^*` of the derived counit `Lf^* Rf_* ⟶ id` at `RSheafHom(K, L)`, then the canonical map of
> Stacks 08JF.  Since transposition is a bijection this determines the map.

```lean
theorem derivedBaseChangeSheafHomMap_adjoint :
    ((derivedAdjunction f').homEquiv
        ((derivedPullback g).obj ((derivedPushforward f).obj
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite C)).obj (op K)).obj L)))
        (((RingedSite.derivedSheafHomBifunctor (RingedTopos.toRingedSite C')).obj
            (op ((derivedPullback h).obj K))).obj ((derivedPullback h).obj L))).symm
        (derivedBaseChangeSheafHomMap f h f' g sq K L) =
      (derivedPullbackCompIsoLeft f' g).hom.app
          ((derivedPushforward f).obj
            (((RingedSite.derivedSheafHomBifunctor
              (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ≫
        (derivedPullbackCompIsoRight f h f' g sq).inv.app
          ((derivedPushforward f).obj
            (((RingedSite.derivedSheafHomBifunctor
              (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ≫
        (derivedPullback h).map ((derivedAdjunction f).counit.app
          (((RingedSite.derivedSheafHomBifunctor
            (RingedTopos.toRingedSite C)).obj (op K)).obj L)) ≫
        RingedToposHom.derivedPullbackSheafHomMap h K L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.35, Tag 08J7](https://stacks.math.columbia.edu/tag/08J7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
