---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_formalSpectrumToSpec, AlgebraicGeometry.FormalSpace.bijective_map_into_affine, AlgebraicGeometry.FormalSpace.existsUnique_equiv_specHom_formalSpectrumHom, AlgebraicGeometry.FormalSpace.injective_map_into_algebraicSpace, AlgebraicGeometry.FormalSpace.surjective_map_into_algebraicSpace, AlgebraicGeometry.FormalSpace.bijective_map_into_algebraicSpace, AlgebraicGeometry.FormalSpace.existsUnique_algebraization_of_adic_into_completion, AlgebraicGeometry.FormalSpace.adicCompletionHomEquiv
statement: formalized
proof: formalized
---

# 87.33 Maps out of affine formal schemes

Section 87.33 of the Stacks Project, [Tag 0AQE](https://stacks.math.columbia.edu/tag/0AQE). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AQF, a lemma

[Tag 0AQF](https://stacks.math.columbia.edu/tag/0AQF) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_formalSpectrumToSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAffine.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAffine.lean#L180). The attribute's comment: “canonical map”.

> The canonical formal-to-ordinary-spectrum map exists and restricts to the
> quotient-spectrum map at every stage.

```lean
public theorem exists_formalSpectrumToSpec
    (D : QuotientSystem B S hS A)
    (hAS : B.Contains (Spec (.of A))) (fA : Spec (.of A) ⟶ S)
    (hcompat : ∀ J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ fA = D.overS J) :
    ∃ q : formalSpectrum D ⟶
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
        ((BigAffineFppf.inclusion B S hS).obj (specOver hAS fA)),
      ∀ J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I },
        formalSpectrumInclusion D (OrderDual.toDual J) ≫ q =
          (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map
            ((BigAffineFppf.inclusion B S hS).map
              (stageToSpec D hAS fA J (hcompat J)))
```

**`AlgebraicGeometry.FormalSpace.bijective_map_into_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAffine.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAffine.lean#L495). The attribute's comment: “bijectivity”.

> For an affine target over `S`, restriction to the quotient spectra is a
> bijection on morphisms over `S`. The ordinary spectrum need not belong to the
> chosen big fppf site.

```lean
public theorem bijective_map_into_affine
    [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (D : QuotientSystem B S hS A)
    (fA : Spec (.of A) ⟶ S)
    (hcompat : ∀ J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ fA = D.overS J)
    (X : BigAffineFppf B S hS) :
    Function.Bijective (restrictToFormalSpectrum D fA hcompat
      ((BigAffineFppf.inclusion B S hS).obj X))
```

## Tag 0AQG, a lemma

[Tag 0AQG](https://stacks.math.columbia.edu/tag/0AQG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.existsUnique_equiv_specHom_formalSpectrumHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToScheme.lean, line 610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToScheme.lean#L610). References: SGA 3 XV (1.4).

> The canonical bijection between maps from a spectrum and from its formal
> spectrum to an `S`-scheme, characterized by restriction to every weak quotient.

```lean
public theorem existsUnique_equiv_specHom_formalSpectrumHom
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {A : Type u} [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (D : QuotientSystem B S hS A)
    (p : Spec (.of A) ⟶ S)
    (hp : ∀ J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ p = D.overS J)
    (I : Ideal A) (hI : TopologicalRing.IsWeakIdealOfDefinition I)
    [IsLocalRing (A ⧸ I)]
    (X : Scheme.{u}) (hX : B.Contains X) (xS : X ⟶ S) :
    let Xo : BigFppfOver B S hS :=
      Over.mk (ObjectProperty.homMk xS : B.obj hX ⟶ B.obj hS)
    ∃! e : ((Over.mk p : Over S) ⟶ (Over.mk xS : Over S)) ≃
        (formalSpectrum D ⟶
          (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj Xo),
      ∀ (f : (Over.mk p : Over S) ⟶ (Over.mk xS : Over S))
    (J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I }),
        ∃ g : (BigAffineFppf.inclusion B S hS).obj (D.stage J) ⟶ Xo,
          B.inclusion.map g.left =
              Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ f.left ∧
            formalSpectrumInclusion D (OrderDual.toDual J) ≫ e f =
              (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map g
```

## Tag 0AQH, a lemma

[Tag 0AQH](https://stacks.math.columbia.edu/tag/0AQH) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.injective_map_into_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAlgebraicSpace.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAlgebraicSpace.lean#L288). The attribute's comment: “injectivity”. References: SGA 3 XV (1.4), “injectivity of (*)”; SGA 3 XI (3.3), “injectivity”.

> **The injectivity half of Stacks 0AQH**, in the shape of the bijectivity statement:
> restriction along the canonical map `Spf R ⟶ Spec R` is injective on morphisms to an
> algebraic space over `S`.
>
> Only the second cofinality condition on the weak ideals of definition is used — that every
> power of the maximal ideal contains one — and the Noetherian hypothesis on `R` enters only
> through locality and completeness.

```lean
public theorem injective_map_into_algebraicSpace
    {R : Type u} [CommRing R] [TopologicalSpace R]
    (hR : IsNoetherianCompleteLocalRing R)
    (D : QuotientSystem B S hS R)
    (hD : ∀ n : ℕ, ∃ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      J.1 ≤ (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n)
    (hRS : B.Contains (Spec (.of R))) (p : Spec (.of R) ⟶ S)
    (hp : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ p = D.overS J)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    Function.Injective (fun f :
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
        ((BigAffineFppf.inclusion B S hS).obj (specOver hRS p)) ⟶ upliftedSheaf X hX =>
      formalSpectrumToSpec D hRS p hp ≫ f)
```

**`AlgebraicGeometry.FormalSpace.surjective_map_into_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAlgebraicSpace.lean, line 2885](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAlgebraicSpace.lean#L2885). The attribute's comment: “surjectivity”.

> **The surjectivity half of Stacks 0AQH.** Restriction along the canonical map
> `Spf R ⟶ Spec R` hits every morphism from the formal spectrum of a Noetherian complete local
> `S`-algebra `R` to an algebraic space over `S`.
>
> Both cofinality conditions on the weak ideals of definition are used, so that the formal
> spectrum of the quotient system is the `𝔪`-adic one.

```lean
public theorem surjective_map_into_algebraicSpace
    {R : Type u} [CommRing R] [TopologicalSpace R]
    (hR : IsNoetherianCompleteLocalRing R)
    (D : QuotientSystem B S hS R)
    (hD₁ : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      ∃ n : ℕ, (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n ≤ J.1)
    (hD : ∀ n : ℕ, ∃ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      J.1 ≤ (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n)
    (hRS : B.Contains (Spec (.of R))) (p : Spec (.of R) ⟶ S)
    (hp : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ p = D.overS J)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    Function.Surjective (fun f :
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
        ((BigAffineFppf.inclusion B S hS).obj (specOver hRS p)) ⟶ upliftedSheaf X hX =>
      formalSpectrumToSpec D hRS p hp ≫ f)
```

**`AlgebraicGeometry.FormalSpace.bijective_map_into_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAlgebraicSpace.lean, line 2907](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MapsToAlgebraicSpace.lean#L2907).

> **Stacks 0AQH.** For `R` a Noetherian complete local `S`-algebra and `X` an algebraic
> space over `S`, restriction along `Spf R ⟶ Spec R` is a bijection
> `Mor_S(Spec R, X) ⟶ Mor_S(Spf R, X)`.

```lean
public theorem bijective_map_into_algebraicSpace
    {R : Type u} [CommRing R] [TopologicalSpace R]
    (hR : IsNoetherianCompleteLocalRing R)
    (D : QuotientSystem B S hS R)
    (hD₁ : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      ∃ n : ℕ, (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n ≤ J.1)
    (hD : ∀ n : ℕ, ∃ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      J.1 ≤ (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n)
    (hRS : B.Contains (Spec (.of R))) (p : Spec (.of R) ⟶ S)
    (hp : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ p = D.overS J)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X) :
    Function.Bijective (fun f :
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
        ((BigAffineFppf.inclusion B S hS).obj (specOver hRS p)) ⟶ upliftedSheaf X hX =>
      formalSpectrumToSpec D hRS p hp ≫ f)
```

## Tag 0GBU, a lemma

[Tag 0GBU](https://stacks.math.columbia.edu/tag/0GBU) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.existsUnique_algebraization_of_adic_into_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMapsIntoCompletion.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMapsIntoCompletion.lean#L369). The attribute's comment: “The algebraization, its existence and uniqueness, and both inclusions of its fibre condition g⁻¹(T) = {𝔪}, the second of them by Krull's intersection theorem.”.

> **Stacks 0GBU.** Let `S` be a scheme, `X` an algebraic space over `S` and `T` a closed
> set of points of `X` whose complementary open subspace has quasi-compact inclusion into `X`.
> Let `R` be a Noetherian complete local `S`-algebra whose spectrum lies in the site, equipped
> with a quotient system whose weak ideals of definition are cofinal among the powers of the
> maximal ideal. Then an adic morphism `p : Spf R ⟶ X_{/T}` into the completion of `X` along
> `T` admits a unique algebraization: a unique morphism `g : Spec R ⟶ X` restricting on
> `Spf R` to the composite `Spf R ⟶ X_{/T} ⟶ X` and satisfying `g⁻¹(T) = {𝔪}`.
>
> The existence and uniqueness of the algebraization are the two halves of **Stacks 0AQH**,
> `AlgebraicGeometry.FormalSpace.bijective_map_into_algebraicSpace`. The inclusion
> `{𝔪} ⊆ g⁻¹(T)` of the fibre condition is
> `AlgebraicGeometry.FormalSpace.pointsMap_mem_of_pointsToScheme_eq_closedPoint` and the reverse
> inclusion `g⁻¹(T) ⊆ {𝔪}` is
> `AlgebraicGeometry.FormalSpace.preimageSubsetClosedPoint_of_comp_eq`.

```lean
public theorem existsUnique_algebraization_of_adic_into_completion
    {R : Type u} [CommRing R] [TopologicalSpace R]
    (hR : IsNoetherianCompleteLocalRing R)
    (D : QuotientSystem B S hS R)
    (hD₁ : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      ∃ n : ℕ, (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n ≤ J.1)
    (hD : ∀ n : ℕ, ∃ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      J.1 ≤ (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n)
    (hRS : B.Contains (Spec (.of R))) (q : Spec (.of R) ⟶ S)
    (hq : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ q = D.overS J)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    (_hTqc : letI : TopologicalSpace (Space.points B S hS X) := Space.pointTopology B S hS X
      Space.IsQuasiCompact B S hS
        ((Space.openSubspacesOrderIso B S hS X hX).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι)
    (P : formalSpectrum D ⟶ Space.completionSheaf B S hS X T)
    (hPadic : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS P.hom) :
    ∃! g : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
        ((BigAffineFppf.inclusion B S hS).obj (specOver hRS q)) ⟶ upliftedSheaf X hX,
      formalSpectrumToSpec D hRS q hq ≫ g = P ≫ completionToUpliftedSheaf X hX T ∧
        PreimageEqClosedPoint hR T hRS q
          (Sheaf.sectionEquiv (BigFppfOver.topology B S hS) g).down
```

**`AlgebraicGeometry.FormalSpace.adicCompletionHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMapsIntoCompletionEquiv.lean, line 628](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMapsIntoCompletionEquiv.lean#L628). The attribute's comment: “The bijection between adic morphisms Spf R ⟶ X_{/T} and morphisms g : Spec R ⟶ X with g⁻¹(T) = {𝔪}.”.

> **Stacks 0GBU.** Let `S` be a scheme, `X` an algebraic space over `S` and `T` a closed set of
> points of `X` whose complementary open subspace has quasi-compact inclusion into `X`. Let `R` be
> a Noetherian complete local `S`-algebra whose spectrum lies in the site, equipped with a
> quotient system whose weak ideals of definition are cofinal among the powers of the maximal
> ideal `𝔪`. Then the adic morphisms `p : Spf R ⟶ X_{/T}` correspond bijectively to the morphisms
> `g : Spec R ⟶ X` with `g⁻¹(T) = {𝔪}`.
>
> The bijection sends `p` to the unique `g` restricting on `Spf R` to `p` followed by
> `X_{/T} ⟶ X` (`AlgebraicGeometry.FormalSpace.existsUnique_algebraization_of_adic_into_completion`),
> and its inverse sends `g` to `AlgebraicGeometry.FormalSpace.adicOfAlgebraization`; the
> correspondence is characterised by
> `AlgebraicGeometry.FormalSpace.adicCompletionHomEquiv_apply_eq_iff`.

```lean
def adicCompletionHomEquiv
    {R : Type u} [CommRing R] [TopologicalSpace R]
    (hR : IsNoetherianCompleteLocalRing R)
    (D : QuotientSystem B S hS R)
    (hD₁ : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      ∃ n : ℕ, (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n ≤ J.1)
    (hD : ∀ n : ℕ, ∃ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      J.1 ≤ (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n)
    (hRS : B.Contains (Spec (.of R))) (q : Spec (.of R) ⟶ S)
    (hq : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ q = D.overS J)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    (hTqc : letI : TopologicalSpace (Space.points B S hS X) := Space.pointTopology B S hS X
      Space.IsQuasiCompact B S hS
        ((Space.openSubspacesOrderIso B S hS X hX).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι) :
    { p : formalSpectrum D ⟶ Space.completionSheaf B S hS X T //
        Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS p.hom } ≃
      { g : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
          ((BigAffineFppf.inclusion B S hS).obj (specOver hRS q)) ⟶ upliftedSheaf X hX //
        PreimageEqClosedPoint hR T hRS q
          (Sheaf.sectionEquiv (BigFppfOver.topology B S hS) g).down }
```

**`AlgebraicGeometry.FormalSpace.adicCompletionHomEquiv_apply_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMapsIntoCompletionEquiv.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicMapsIntoCompletionEquiv.lean#L703). The attribute's comment: “The bijection is the correspondence: p ↦ g exactly when g restricts on Spf R to p followed by X_{/T} ⟶ X.”.

> **Stacks 0GBU, the correspondence.** The bijection `adicCompletionHomEquiv` sends an adic
> `p : Spf R ⟶ X_{/T}` to `g : Spec R ⟶ X` with `g⁻¹(T) = {𝔪}` exactly when `g` restricts on
> `Spf R` to `p` followed by `X_{/T} ⟶ X`.

```lean
theorem adicCompletionHomEquiv_apply_eq_iff
    {R : Type u} [CommRing R] [TopologicalSpace R]
    (hR : IsNoetherianCompleteLocalRing R)
    (D : QuotientSystem B S hS R)
    (hD₁ : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      ∃ n : ℕ, (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n ≤ J.1)
    (hD : ∀ n : ℕ, ∃ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      J.1 ≤ (@IsLocalRing.maximalIdeal R _ hR.isLocal) ^ n)
    (hRS : B.Contains (Spec (.of R))) (q : Spec (.of R) ⟶ S)
    (hq : ∀ J : { I : Ideal R // TopologicalRing.IsWeakIdealOfDefinition I },
      Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J.1)) ≫ q = D.overS J)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    (hTqc : letI : TopologicalSpace (Space.points B S hS X) := Space.pointTopology B S hS X
      Space.IsQuasiCompact B S hS
        ((Space.openSubspacesOrderIso B S hS X hX).symm ⟨Tᶜ, hT.isOpen_compl⟩).1.ι)
    (p : { p : formalSpectrum D ⟶ Space.completionSheaf B S hS X T //
        Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS p.hom })
    (g : { g : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
          ((BigAffineFppf.inclusion B S hS).obj (specOver hRS q)) ⟶ upliftedSheaf X hX //
        PreimageEqClosedPoint hR T hRS q
          (Sheaf.sectionEquiv (BigFppfOver.topology B S hS) g).down }) :
    adicCompletionHomEquiv hR D hD₁ hD hRS q hq X hX T hT hTqc p = g ↔
      formalSpectrumToSpec D hRS q hq ≫ g.1 = p.1 ≫ completionToUpliftedSheaf X hX T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.33, Tag 0AQE](https://stacks.math.columbia.edu/tag/0AQE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
