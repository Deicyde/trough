---
declaration: section
origin: cited
lean: AlgebraicGeometry.DeligneSystem.isIso_restrictionNatTrans, AlgebraicGeometry.DeligneSystem.nonempty_isColimit_restrictionHomCocone, AlgebraicGeometry.DeligneSystem.exists_restrictIso, AlgebraicGeometry.DeligneSystem.Value.proHomEquiv, AlgebraicGeometry.DeligneSystem.existsUnique_proHom_restrict, AlgebraicGeometry.DeligneSystem.existsUnique_proIso_restrict, AlgebraicGeometry.DeligneTriangle.exists_deligneSystem_distTriang_boundedCoherent, CategoryTheory.extensionByZero
statement: formalized
proof: formalized
---

# 48.30 Extension by zero for coherent modules

Section 48.30 of the Stacks Project, [Tag 0G2G](https://stacks.math.columbia.edu/tag/0G2G). 10 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G2H, a lemma

[Tag 0G2H](https://stacks.math.columbia.edu/tag/0G2H) in the Stacks Project.

**`AlgebraicGeometry.DeligneSystem.isIso_restrictionNatTrans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemCoreCoherent.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemCoreCoherent.lean#L124).

> **Stacks Project, Tag 0G2H.** Let `j : U ⟶ X` be an open immersion of Noetherian schemes and
> let `(K_n)` be a Deligne system with value `K` on `U`. Then the canonical restriction
> transformation
>
> `colim_n Mor_X(K_n, -) ⟶ Mor_U(K, (-)|_U)`
>
> is an isomorphism: `colim_n Hom_X(K_n, L) = Hom_U(K, L|_U)` for every `L` in
> `D^b_{Coh}(𝒪_X)`.
>
> This is `AlgebraicGeometry.DeligneSystem.isIso_restrictionNatTrans_of_core` with its hypothesis
> `hcore` supplied by `AlgebraicGeometry.DeligneSystem.restrictionLifting_truncGELE`.

```lean
public theorem isIso_restrictionNatTrans (K : BoundedCoherentDerived U)
    (e : D.system ⋙ restrictBoundedCoherent j ≅
      (Functor.const ℕᵒᵖ).obj ((boundedCoherentDerived U).ι.obj K)) :
    IsIso (D.restrictionNatTrans K e)
```

## Tag 0G4K, a lemma

[Tag 0G4K](https://stacks.math.columbia.edu/tag/0G4K) in the Stacks Project.

**`AlgebraicGeometry.DeligneSystem.nonempty_isColimit_restrictionHomCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemRestrictionLifting.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemRestrictionLifting.lean#L257).

> **Stacks Project, Tag 0G4K.** The result of [Stacks, Tag 0G2H] holds even for `L` in
> `D^+_{Coh}(𝒪_X)`. Let `j : U ⟶ X` be an open immersion of Noetherian schemes, let `(K_n)` be a
> Deligne system, identified on `U` by `e` with the constant system at `K`, and let `L` be an object
> of `D(𝒪_X)` that is cohomologically bounded below with coherent cohomology sheaves. Then
>
> `colim_n Hom_X(K_n, L) = Hom_U(K, L|_U)`,
>
> the map being the canonical one: the cocone of `CategoryTheory.restrictionHomCocone`, which sends
> `g : K_n ⟶ L` to `K ≅ K_n|_U ⟶ L|_U`, is a colimit cocone.
>
> This is `AlgebraicGeometry.DeligneSystem.restrictionLifting_of_derivedCategoryBPlus` read through
> `CategoryTheory.RestrictionLifting.isColimitRestrictionHomCocone`. Nothing is assumed.

```lean
public theorem nonempty_isColimit_restrictionHomCocone (K : BoundedCoherentDerived U)
    (e : D.system ⋙ restrictBoundedCoherent j ≅
      (Functor.const ℕᵒᵖ).obj ((boundedCoherentDerived U).ι.obj K))
    (L : DerivedCategory X.Modules)
    (hL : DerivedCategoryB.derivedCategoryBPlus (fun M : X.Modules => M.IsCoherent) L) :
    Nonempty (IsColimit (restrictionHomCocone (D.system ⋙ (boundedCoherentDerived X).ι)
      (Scheme.Modules.restrictFunctor j).mapDerivedCategory L
      ((boundedCoherentDerived U).ι.obj K) e))
```

## Tag 0G4L, a lemma

[Tag 0G4L](https://stacks.math.columbia.edu/tag/0G4L) in the Stacks Project.

**`AlgebraicGeometry.DeligneSystem.exists_restrictIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemExistence.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemExistence.lean#L88). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0G4L (2).** Let `j : U ⟶ X` be an open immersion of Noetherian schemes.
> Given `K` in `D^b_{Coh}(𝒪_U)`, there exists a Deligne system `(K_n)` such that `(K_n|_U)` is
> constant with value `K`.
>
> As in the source, `K` is the restriction of a bounded complex `𝓕^•` of coherent `𝒪_X`-modules
> (`AlgebraicGeometry.exists_bounded_isCoherent_complex_restrict_Q_iso`, which rests on Stacks 0G48
> and Stacks 0FDB), the ideal sheaf is that of the reduced closed complement of `U`, and the Deligne
> system is `(𝓘^n𝓕^•)`, `AlgebraicGeometry.DeligneTriangle.deligneSystemOfComplex`.

```lean
public theorem exists_restrictIso (j : U ⟶ X) [IsOpenImmersion j] [IsNoetherian X]
    (K : BoundedCoherentDerived U) :
    ∃ D : DeligneSystem j, Nonempty (D.system ⋙ restrictBoundedCoherent j ≅
      (Functor.const ℕᵒᵖ).obj ((boundedCoherentDerived U).ι.obj K))
```

**`AlgebraicGeometry.DeligneSystem.Value.proHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemHom.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemHom.lean#L394). The attribute's comment: “lift\_morphisms; the identification of 0G2H supplied as data”.

> **Stacks Project, Tag 0G4L(1)**. Let `j : U ⟶ X` be an open immersion of Noetherian
> schemes, let `(K_n)` and `(L_m)` be Deligne systems and let `K` and `L` be the values of the
> constant systems `(K_n|_U)` and `(L_m|_U)`. Then every morphism `α : K ⟶ L` on `U` is the
> restriction of a unique morphism of pro-systems `(K_n) ⟶ (L_m)` in `D^b_{Coh}(𝒪_X)`.
>
> This is the argument of the source: morphisms of pro-systems are the morphisms of the
> pro-objects they determine (Stacks 0G2X, which is `CategoryTheory.ProSeq.ofHomEquiv`), that is
> `lim_m colim_n Hom_X(K_n, L_m)`; by Stacks 0G2H each term of the limit is `Hom_U(K, L_m|_U)`,
> and `(L_m|_U)` is the constant system at `L`, so the limit is over a constant diagram on a
> connected index category and equals `Hom_U(K, L)`.

```lean
public def proHomEquiv :
    (D.proObject ⟶ E.proObject) ≃
      ((boundedCoherentDerived U).ι.obj V.obj ⟶
        (boundedCoherentDerived U).ι.obj W.obj)
```

**`AlgebraicGeometry.DeligneSystem.existsUnique_proHom_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemProMorphisms.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemProMorphisms.lean#L252). The attribute's comment: “(1)”.

> **Stacks Project, Tag 0G4L (1).** Let `j : U ⟶ X` be an open immersion of Noetherian schemes,
> let `(K_n)` and `(L_m)` be Deligne systems and let `K` and `L` be the values of the constant
> systems `(K_n|_U)` and `(L_m|_U)`, through the identifications `eD` and `eE`. Given a morphism
> `α : K ⟶ L` of `D(𝒪_U)`, there is a unique morphism of pro-systems `ξ : (K_n) ⟶ (L_m)` of
> `D^b_{Coh}(𝒪_X)` whose restriction to `U` is `α`: for every `m`, and every representative
> `g : K_n ⟶ L_m` of the `m`-th component of `ξ` in `colim_n Hom_X(K_n, L_m)`, the restriction
> `K ≅ K_n|_U ⟶ L_m|_U` of `g` is `K ⟶ L ≅ L_m|_U`.
>
> Morphisms of pro-systems are transformations of the functors they corepresent (Stacks 0G2X),
> which by Stacks 0G2H are `Hom_U(L, (-)|_U)` and `Hom_U(K, (-)|_U)`.

```lean
public theorem existsUnique_proHom_restrict (α : K ⟶ L) :
    ∃! ξ : D.proObject ⟶ E.proObject,
      ∀ (m n : ℕ) (g : D.system.obj (op n) ⟶ E.system.obj (op m)),
        proHomComponent ξ m = Pro.seqStage D.system g →
          eD.inv.app (op n) ≫ (restrictBoundedCoherent j).map g = α ≫ eE.inv.app (op m)
```

**`AlgebraicGeometry.DeligneSystem.existsUnique_proIso_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemProMorphisms.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemProMorphisms.lean#L303). The attribute's comment: “(3)”.

> **Stacks Project, Tag 0G4L (3).** Let `j : U ⟶ X` be an open immersion of Noetherian schemes.
> The pro-object of a Deligne system with value `K` (part (2)) is unique up to unique isomorphism
> as a pro-object: for Deligne systems `(K_n)` and `(K'_n)` whose restrictions to `U` are
> identified, by `eD` and `eE`, with the constant system at `K`, there is a unique isomorphism of
> pro-objects `(K_n) ≅ (K'_n)` whose restriction to `U` is the identity of `K`: for every `m`, and
> every representative `g : K_n ⟶ K'_m` of the `m`-th component of its forward morphism, the
> restriction `K ≅ K_n|_U ⟶ K'_m|_U` of `g` is `K ≅ K'_m|_U`.
>
> This follows from part (1): the morphisms restricting to the identity in the two
> directions compose to morphisms restricting to the identity, which are the identities.

```lean
public theorem existsUnique_proIso_restrict
    (eD : D.system ⋙ restrictBoundedCoherent j ≅ (Functor.const ℕᵒᵖ).obj K)
    (eE : E.system ⋙ restrictBoundedCoherent j ≅ (Functor.const ℕᵒᵖ).obj K) :
    ∃! i : D.proObject ≅ E.proObject,
      ∀ (m n : ℕ) (g : D.system.obj (op n) ⟶ E.system.obj (op m)),
        proHomComponent i.hom m = Pro.seqStage D.system g →
          eD.inv.app (op n) ≫ (restrictBoundedCoherent j).map g = eE.inv.app (op m)
```

## Tag 0G4M, a lemma

[Tag 0G4M](https://stacks.math.columbia.edu/tag/0G4M) in the Stacks Project.

**`AlgebraicGeometry.DeligneTriangle.exists_deligneSystem_distTriang_boundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTriangleExtensionCoherent.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTriangleExtensionCoherent.lean#L475).

> **Stacks Project, Tag 0G4M.** Let `j : U ⟶ X` be an open immersion of Noetherian schemes and
> let
>
> `K ⟶ L ⟶ M ⟶ K[1]`
>
> be a distinguished triangle of `D^b_{Coh}(𝒪_U)`. Then there is an inverse system of
> distinguished triangles
>
> `K_n ⟶ L_n ⟶ M_n ⟶ K_n[1]`
>
> in `D^b_{Coh}(𝒪_X)` such that `(K_n)`, `(L_n)` and `(M_n)` are Deligne systems and such that the
> restriction of these distinguished triangles to `U` is isomorphic to the distinguished triangle
> one started with.
>
> The system is the one of
> `AlgebraicGeometry.DeligneTriangle.exists_deligneSystem_distTriang_derived`, the cone triangles
> of a coherent complex model of `K ⟶ L`, lifted to `D^b_{Coh}(𝒪_X)` by
> `AlgebraicGeometry.DeligneTriangle.exists_triangleFunctor_lift`; the identifications of its
> vertex systems and of its restriction to `U` are transported back along the fully faithful
> inclusions of `D^b_{Coh}`.

```lean
public theorem exists_deligneSystem_distTriang_boundedCoherent (j : U ⟶ X) [IsOpenImmersion j]
    [IsNoetherian X]
    (T : Triangle (BoundedCoherentDerived U)) (hT : T ∈ distTriang (BoundedCoherentDerived U)) :
    ∃ (DK DL DM : DeligneSystem j) (TX : ℕᵒᵖ ⥤ Triangle (BoundedCoherentDerived X)),
      (∀ n : ℕᵒᵖ, TX.obj n ∈ distTriang (BoundedCoherentDerived X)) ∧
      Nonempty (TX ⋙ Triangle.π₁ ≅ DK.system) ∧
      Nonempty (TX ⋙ Triangle.π₂ ≅ DL.system) ∧
      Nonempty (TX ⋙ Triangle.π₃ ≅ DM.system) ∧
      Nonempty (TX ⋙ (restrictBoundedCoherentLift j).mapTriangle ≅
        (Functor.const ℕᵒᵖ).obj T)
```

## Tag 0G4N, a remark

[Tag 0G4N](https://stacks.math.columbia.edu/tag/0G4N) in the Stacks Project.

**`CategoryTheory.extensionByZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroFunctor.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroFunctor.lean#L80). The attribute's comment: “the functor Rj\_!, for a Deligne-system assignment supplied as data”.

> **Stacks Project, Tag 0G4N.** Sending an object `K` of `𝒞` to the pro-object of the inverse
> sequence assigned to it determines a functor `Rj_! : 𝒞 ⥤ Pro-𝒟`. Its functor of points at `K` is
> `L ↦ Mor_𝒞(K, j^* L)`.

```lean
public def extensionByZero : 𝒞 ⥤ ProSeq 𝒟
```

**`CategoryTheory.extensionByZeroHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroFunctor.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroFunctor.lean#L99). The attribute's comment: “the left adjointness of Rj\_! to j^*”.

> **Stacks Project, Tag 0G4N**, the left adjointness of `Rj_!` to `j^*`: morphisms of
> pro-objects from `Rj_! K` to the constant pro-object at `L` are the morphisms `K ⟶ j^* L`.

```lean
public def extensionByZeroHomEquiv (K : 𝒞) (L : 𝒟) :
    ((extensionByZero jstar A).obj K ⟶ ProSeq.const.obj L) ≃ (K ⟶ jstar.obj L)
```

**`AlgebraicGeometry.extensionByZeroOpenImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean#L275). The attribute's comment: “the functor Rj\_!”.

> **The extension by zero `Rj_! : D^b_{Coh}(𝒪_U) ⥤ Pro-D^b_{Coh}(𝒪_X)`** along an open immersion
> `j` of Noetherian schemes, [Stacks, Tag 0G4N]: it sends `K` to the pro-object of a Deligne system
> with value `K`, the one of the assignment `AlgebraicGeometry.DeligneSystem.values`. Its functor of
> points at `K` is `L ↦ Hom_U(K, L|_U)`. The value at `K` is the pro-object of any Deligne system
> with value `K`, by `AlgebraicGeometry.DeligneSystem.Value.extensionByZeroIso`, and on morphisms
> it is computed on any morphism of inverse systems restricting to the given one, by
> `CategoryTheory.extensionByZero_map_comp_comparison`.

```lean
public def extensionByZeroOpenImmersion :
    BoundedCoherentDerived U ⥤ ProSeq (BoundedCoherentDerived X)
```

**`AlgebraicGeometry.DeligneSystem.Value.extensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean#L389). The attribute's comment: “Rj\_! K is the pro-object of any Deligne system with value K”.

> **`Rj_! K` is the pro-object of any Deligne system with value `K`.** Both have the functor of
> points `L ↦ Hom_U(K, L|_U)`, by [Stacks, Tag 0G2H]; the identification is the restriction map.

```lean
public def extensionByZeroIso : D.proObject ≅ (extensionByZeroOpenImmersion j).obj V.obj
```

**`AlgebraicGeometry.extensionByZeroOpenImmersionHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean#L425). The attribute's comment: “Rj\_! is left adjoint to j^*”.

> **Stacks Project, Tag 0G4N**, adjointness. `Rj_!` is "left adjoint" to
> `j^* : D^b_{Coh}(𝒪_X) ⥤ D^b_{Coh}(𝒪_U)`: morphisms of pro-objects from `Rj_! K` to the constant
> pro-object at `L` are the morphisms `K ⟶ L|_U`,
>
> `Hom_{Pro}(Rj_! K, L) = Hom_U(K, L|_U)`,
>
> naturally in `K` and in `L`. Both sides are the functor of points of `Rj_! K` at `L`, which is
> `colim_n Hom_X(K_n, L)` for a Deligne system `(K_n)` with restriction `K`, and the identification
> with `Hom_U(K, L|_U)` is Stacks 0G2H.

```lean
public def extensionByZeroOpenImmersionHomIso :
    (extensionByZeroOpenImmersion j).op ⋙ coyoneda ⋙
        (Functor.whiskeringLeft _ _ _).obj ProSeq.const ≅
      coyoneda ⋙ (Functor.whiskeringLeft _ _ _).obj (restrictBoundedCoherentLift j)
```

**`AlgebraicGeometry.extensionByZeroOpenImmersion_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/ExtensionByZeroOpenImmersion.lean#L463). The attribute's comment: “Rj\_! is exact”.

> **Stacks Project, Tag 0G4N**, exactness. Let `K ⟶ L ⟶ M ⟶ K[1]` be a distinguished triangle
> `T` of `D^b_{Coh}(𝒪_U)`. Then there is an inverse system of distinguished triangles
> `K_n ⟶ L_n ⟶ M_n ⟶ K_n[1]` of `D^b_{Coh}(𝒪_X)`, with an identification `e` of its restriction to
> `U` with the constant system at `T`, whose vertex systems `(K_n)`, `(L_n)`, `(M_n)` are Deligne
> systems, and such that `Rj_!` sends `T` to its pro-system: the comparison maps
>
> `Rj_! K ⟶ (K_n)`, `Rj_! L ⟶ (L_n)`, `Rj_! M ⟶ (M_n)`, `Rj_!(K[1]) ⟶ (K_n[1])`
>
> induced by `e` are isomorphisms of pro-objects, and they carry `Rj_!` of the three maps of `T` to
> the morphisms of pro-systems induced by the three maps of the triangles.
>
> The system is the one of Stacks 0G4M; the comparison maps are isomorphisms by Stacks 0G2H, which
> holds for the vertex systems because they are Deligne systems, and for `(K_n[1])` because it holds
> for `(K_n)`.

```lean
public theorem extensionByZeroOpenImmersion_exact (T : Triangle (BoundedCoherentDerived U))
    (hT : T ∈ distTriang (BoundedCoherentDerived U)) :
    ∃ (TX : ℕᵒᵖ ⥤ Triangle (BoundedCoherentDerived X))
      (e : TX ⋙ (restrictBoundedCoherentLift j).mapTriangle ≅ (Functor.const ℕᵒᵖ).obj T),
      (∀ n, TX.obj n ∈ distTriang (BoundedCoherentDerived X)) ∧
      (∃ D : DeligneSystem j, Nonempty (TX ⋙ Triangle.π₁ ≅ D.system)) ∧
      (∃ D : DeligneSystem j, Nonempty (TX ⋙ Triangle.π₂ ≅ D.system)) ∧
      (∃ D : DeligneSystem j, Nonempty (TX ⋙ Triangle.π₃ ≅ D.system)) ∧
      IsIso (extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
        (mapTriangleConstIsoπ₁ _ e)) ∧
      IsIso (extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
        (mapTriangleConstIsoπ₂ _ e)) ∧
      IsIso (extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
        (mapTriangleConstIsoπ₃ _ e)) ∧
      IsIso (extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
        (mapTriangleConstIsoShiftπ₁ _ e)) ∧
      (extensionByZeroOpenImmersion j).map T.mor₁ ≫
          extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
            (mapTriangleConstIsoπ₂ _ e) =
        extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
            (mapTriangleConstIsoπ₁ _ e) ≫
          ProSeq.ofMap (Functor.whiskerLeft TX Triangle.π₁Toπ₂) ∧
      (extensionByZeroOpenImmersion j).map T.mor₂ ≫
          extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
            (mapTriangleConstIsoπ₃ _ e) =
        extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
            (mapTriangleConstIsoπ₂ _ e) ≫
          ProSeq.ofMap (Functor.whiskerLeft TX Triangle.π₂Toπ₃) ∧
      (extensionByZeroOpenImmersion j).map T.mor₃ ≫
          extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
            (mapTriangleConstIsoShiftπ₁ _ e) =
        extensionByZeroComparison _ (DeligneSystem.values j).toAssignment
            (mapTriangleConstIsoπ₃ _ e) ≫
          ProSeq.ofMap (Functor.whiskerLeft TX Triangle.π₃Toπ₁)
```

## Tag 0G4Q, a lemma

[Tag 0G4Q](https://stacks.math.columbia.edu/tag/0G4Q) in the Stacks Project.

**`CategoryTheory.DeligneSystemValues.proIsoDeligne_π₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTriangles.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTriangles.lean#L583). The attribute's comment: “for a Deligne-system assignment supplied as data, including the colimit identification of Stacks 0G2H as its isColimit field”.

> Let `j^* : 𝒟 ⥤ 𝒞` be a triangulated functor with a Deligne system assignment, and let
> `K_n ⟶ L_n ⟶ M_n ⟶ K_n[1]` be an inverse system of distinguished triangles in `𝒟`. If `(K_n)`
> and `(M_n)` are pro-isomorphic to Deligne systems, then so is `(L_n)`.

```lean
public theorem DeligneSystemValues.proIsoDeligne_π₂ {jstar : 𝒟 ⥤ 𝒞} [jstar.Additive]
    [jstar.CommShift ℤ] [jstar.IsTriangulated] (A : DeligneSystemValues jstar)
    (T : ℕᵒᵖ ⥤ Triangle 𝒟) (hT : ∀ n, T.obj n ∈ distTriang 𝒟)
    (hK : A.ProIsoDeligne (T ⋙ Triangle.π₁)) (hM : A.ProIsoDeligne (T ⋙ Triangle.π₃)) :
    A.ProIsoDeligne (T ⋙ Triangle.π₂)
```

**`AlgebraicGeometry.DeligneSystem.proIsoDeligneSystem_π₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTrianglesCoherent.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTrianglesCoherent.lean#L45).

> Let `j : U ⟶ X` be an open immersion of Noetherian schemes and let
> `K_n ⟶ L_n ⟶ M_n ⟶ K_n[1]` be an inverse system of distinguished triangles in `D^b_{Coh}(𝒪_X)`. If
> `(K_n)` and `(M_n)` are pro-isomorphic to Deligne systems, then so is `(L_n)`.

```lean
public theorem proIsoDeligneSystem_π₂ (T : ℕᵒᵖ ⥤ Triangle (BoundedCoherentDerived X))
    (hT : ∀ n, T.obj n ∈ distTriang (BoundedCoherentDerived X))
    (hK : ProIsoDeligneSystem j (T ⋙ Triangle.π₁))
    (hM : ProIsoDeligneSystem j (T ⋙ Triangle.π₃)) :
    ProIsoDeligneSystem j (T ⋙ Triangle.π₂)
```

## Tag 0G4R, a lemma

[Tag 0G4R](https://stacks.math.columbia.edu/tag/0G4R) in the Stacks Project.

**`AlgebraicGeometry.idealPowerComplexSystem`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplex.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/IdealPowerComplex.lean#L146). The attribute's comment: “transition maps only. This supplies the canonical maps `… → H^p(I³F) → H^p(I²F) → H^p(IF) → H^p(F)` of the statement, for an arbitrary scheme and an arbitrary complex of module sheaves. The Artin-Rees part of the tag — the constant `c > 0`, the inclusion of the image of `H^p(I^nF) → H^p(F)` in `I^(n-c)H^p(F)`, the maps back, and the resulting pro-isomorphism — is not proved here and needs Noetherianness and coherence.”.

> **Stacks Project, Tag 0G4R (transition maps).** The ideal-power
> subcomplexes `I^n F` exist and carry their canonical compatible inclusions.
> Taking cohomology in any degree gives the maps
> `⋯ → H^p(I³F) → H^p(I²F) → H^p(IF) → H^p(F)`.

```lean
public noncomputable def idealPowerComplexSystem {X : Scheme.{u}}
    (I : X.IdealSheafData) (F : CochainComplex X.Modules ℤ) :
    IdealPowerComplexSystem I F
```

**`Stacks.Duality.cohomologyIdealPowersProIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/IdealPowerCohomologyProIso.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/IdealPowerCohomologyProIso.lean#L166). The attribute's comment: “the pro-isomorphism, packaged as a `ProIso` of the two inverse sequences `n ↦ H^p(I^n F^•)` and `n ↦ I^n H^p(F^•)`; the underlying data and its equations are `Stacks.Duality.cohomologyIdealPowers_proIsomorphic`.”.

> **[Stacks, Tag 0G4R] as a `ProIso`.** Let `X` be a Noetherian scheme, `𝓘 ⊆ 𝒪_X` a
> quasi-coherent sheaf of ideals and `𝓕^•` a complex of coherent `𝒪_X`-modules. The inverse
> sequence `n ↦ H^p(𝓘^n𝓕^•)` and the inverse sequence `n ↦ 𝓘^n H^p(𝓕^•)` are pro-isomorphic, in
> the explicit "up to refinement" form `ProIso`: with `c` the Artin-Rees constant of
> `Stacks.Duality.cohomologyIdealPowers_proIsomorphic`, both reindexings are `m ↦ m + c`, the
> forward maps are the factorizations `H^p(𝓘^{m+c}𝓕^•) ⟶ 𝓘^m H^p(𝓕^•)` and the backward maps are
> the comparisons `𝓘^{m+c} H^p(𝓕^•) ⟶ H^p(𝓘^m𝓕^•)`.
>
> This is the form a pro-isomorphism is consumed in by
> `CategoryTheory.RestrictionLifting.of_proIso`, which is how the core case of
> [Stacks, Tag 0G2H] is transported from the ideal powers of the cohomology to the cohomology of
> the ideal powers.

```lean
theorem cohomologyIdealPowersProIso [IsNoetherian X] (hF : TermsCoherent F)
    (S : IdealPowerComplexSystem I F) :
    Nonempty (ProIso (cohomologySystem S p) (idealPowerSystem I (F.homology p)))
```

**`Stacks.Duality.cohomologyIdealPowers_proIsomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/IdealPowerCohomologyProIsomorphism.lean, line 844](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/IdealPowerCohomologyProIsomorphism.lean#L844). The attribute's comment: “the pro-isomorphism half, for schemes, with no boundedness assumed on the complex: the constant `c > 0`, the factorization of `H^p(𝓘^n𝓕^•) → H^p(𝓕^•)` through `𝓘^(n-c)H^p(𝓕^•)` (the image containment), the canonical map `𝓘^nH^p(𝓕^•) → H^p(𝓘^(n-c)𝓕^•)`, the two composites, and the resulting explicit isomorphism of pro-objects via the shift `n ↦ n + c`. The canonical maps `… → H^p(𝓘^2𝓕^•) → H^p(𝓘𝓕^•) → H^p(𝓕^•)` that the tag asserts first are the ones carried by `AlgebraicGeometry.IdealPowerComplexSystem`, constructed unconditionally by `AlgebraicGeometry.idealPowerComplexSystem`.”.

> **Stacks 0G4R, pro-isomorphism half.** Let `X` be a Noetherian scheme, `𝓘 ⊆ 𝒪_X` a
> quasi-coherent sheaf of ideals and `𝓕^•` a complex of coherent `𝒪_X`-modules. Write
> `𝓗 = H^p(𝓕^•)` and `𝓗_n = H^p(𝓘^n𝓕^•)`. There is a `c > 0` such that for `n ≥ c` the map
> `𝓗_n → 𝓗` factors through `𝓘^(n-c)𝓗`, there is a canonical `𝓘^n𝓗 → 𝓗_(n-c)`, and the two
> composites are the canonical maps; consequently `(𝓗_n)` and `(𝓘^n𝓗)` are isomorphic as
> pro-objects, by the explicit cofinal shift `n ↦ n + c`.

```lean
theorem cohomologyIdealPowers_proIsomorphic [IsNoetherian X]
    (hF : ∀ i : ℤ, _root_.SheafOfModules.IsCoherent (F.X i))
    (S : IdealPowerComplexSystem I F) :
    ∃ (τ : ∀ m n : ℕ, n ≤ m → (S.cohomology m p ⟶ S.cohomology n p)),
      (∀ n : ℕ, τ n n le_rfl = 𝟙 (S.cohomology n p)) ∧
      (∀ (k m n : ℕ) (hkm : m ≤ k) (hmn : n ≤ m),
        τ k m hkm ≫ τ m n hmn = τ k n (hmn.trans hkm)) ∧
      (∀ n : ℕ, τ (n + 1) n (Nat.le_succ n) = S.cohomologyTransition n p) ∧
      (∀ (m n : ℕ) (hmn : n ≤ m),
        τ m n hmn ≫ S.cohomologyToOriginal n p = S.cohomologyToOriginal m p) ∧
      ∃ c : ℕ, 0 < c ∧
        ∃ (ρ : ∀ n : ℕ, c ≤ n → (S.cohomology n p ⟶
                ((Stacks.Algebraization.idealPowerMultiple I (n - c)
                  (F.homology p)).toSheafOfModules : X.Modules)))
          (ψ : ∀ n : ℕ, c ≤ n →
                (((Stacks.Algebraization.idealPowerMultiple I n
                  (F.homology p)).toSheafOfModules : X.Modules) ⟶ S.cohomology (n - c) p)),
          (∀ (n : ℕ) (hn : c ≤ n), ρ n hn ≫
              subι (Stacks.Algebraization.idealPowerMultiple I (n - c) (F.homology p)) =
            S.cohomologyToOriginal n p) ∧
          (∀ (n : ℕ) (hn : c ≤ n), ψ n hn ≫ S.cohomologyToOriginal (n - c) p =
            subι (Stacks.Algebraization.idealPowerMultiple I n (F.homology p))) ∧
          (∀ (m n : ℕ) (hmn : n ≤ m) (hm : c ≤ m) (hn : c ≤ n),
            τ m n hmn ≫ ρ n hn = ρ m hm ≫
              subHom (idealPowerMultiple_antitone I (F.homology p)
                (Nat.sub_le_sub_right hmn c))) ∧
          (∀ (m n : ℕ) (hmn : n ≤ m) (hm : c ≤ m) (hn : c ≤ n),
            subHom (idealPowerMultiple_antitone I (F.homology p) hmn) ≫ ψ n hn =
              ψ m hm ≫ τ (m - c) (n - c) (Nat.sub_le_sub_right hmn c)) ∧
          (∀ (n : ℕ) (hn : 2 * c ≤ n),
            ρ n (by omega) ≫ ψ (n - c) (by omega) = τ n (n - c - c) (by omega)) ∧
          (∀ (n : ℕ) (hn : 2 * c ≤ n),
            ψ n (by omega) ≫ ρ (n - c) (by omega) =
              subHom (idealPowerMultiple_antitone I (F.homology p)
                (show n - c - c ≤ n by omega))) ∧
          ∃ (forward : ∀ m : ℕ, (S.cohomology (m + c) p ⟶
                  ((Stacks.Algebraization.idealPowerMultiple I m
                    (F.homology p)).toSheafOfModules : X.Modules)))
            (backward : ∀ m : ℕ,
                  (((Stacks.Algebraization.idealPowerMultiple I (m + c)
                    (F.homology p)).toSheafOfModules : X.Modules) ⟶ S.cohomology m p)),
            (∀ m : ℕ, forward m ≫
                subι (Stacks.Algebraization.idealPowerMultiple I m (F.homology p)) =
              S.cohomologyToOriginal (m + c) p) ∧
            (∀ m : ℕ, backward m ≫ S.cohomologyToOriginal m p =
              subι (Stacks.Algebraization.idealPowerMultiple I (m + c) (F.homology p))) ∧
            (∀ (m m' : ℕ) (h : m ≤ m'),
              τ (m' + c) (m + c) (Nat.add_le_add_right h c) ≫ forward m =
                forward m' ≫ subHom (idealPowerMultiple_antitone I (F.homology p) h)) ∧
            (∀ (m m' : ℕ) (h : m ≤ m'),
              subHom (idealPowerMultiple_antitone I (F.homology p)
                  (Nat.add_le_add_right h c)) ≫ backward m = backward m' ≫ τ m' m h) ∧
            (∀ m : ℕ, forward (m + c) ≫ backward m =
              τ (m + c + c) m (by omega)) ∧
            (∀ m : ℕ, backward (m + c) ≫ forward m =
              subHom (idealPowerMultiple_antitone I (F.homology p)
                (show m ≤ m + c + c by omega)))
```

## Tag 0G4S, a lemma

[Tag 0G4S](https://stacks.math.columbia.edu/tag/0G4S) in the Stacks Project.

**`AlgebraicGeometry.DeligneSystem.proIsoDeligneSystem_iff_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemCohomology.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemCohomology.lean#L203).

> **Stacks Project, Tag 0G4S.** Let `j : U ⟶ X` be an open immersion of Noetherian schemes and
> `𝓘 ⊆ 𝒪_X` a quasi-coherent sheaf of ideals with `V(𝓘) = X ∖ U`. Let `a ≤ b` be integers and
> `(K_n)` an inverse system of `D^b_{Coh}(𝒪_X)` such that `H^i(K_n) = 0` for `i ∉ [a, b]`. The
> following are equivalent:
>
> 1. `(K_n)` is pro-isomorphic to a Deligne system;
> 2. for every `p ∈ ℤ` there exists a coherent `𝒪_X`-module `𝓕` such that the pro-systems
>    `(H^p(K_n))` and `(𝓘^n𝓕)` are pro-isomorphic.
>
> (1) ⇒ (2) is `AlgebraicGeometry.DeligneSystem.exists_proIso_homology_of_proIso`, from
> [Stacks, Tag 0G4R]; (2) ⇒ (1) is `AlgebraicGeometry.DeligneSystem.proIsoDeligneSystem_of_homology`,
> from [Stacks, Tag 0G4Q]. The ideal `𝓘` of (2) is any one cutting out `X ∖ U`.

```lean
public theorem proIsoDeligneSystem_iff_homology (I : X.IdealSheafData)
    (hI : (I.support : Set X) = (Set.range j.base)ᶜ) {a b : ℤ}
    (hab : a ≤ b) (K : ℕᵒᵖ ⥤ BoundedCoherentDerived X)
    (hK : ∀ (n : ℕ) (i : ℤ), i < a ∨ b < i →
      IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj
        ((boundedCoherentDerived X).ι.obj (K.obj (op n))))) :
    ProIsoDeligneSystem j K ↔
      ∀ p : ℤ, ∃ F : X.Modules, F.IsCoherent ∧
        Nonempty (ProSeq.of ((K ⋙ (boundedCoherentDerived X).ι) ⋙
          DerivedCategory.homologyFunctor X.Modules p) ≅
            ProSeq.of (Stacks.Duality.idealPowerSystem I F))
```

**`CategoryTheory.DeligneSystemValues.proIsoDeligne_of_truncGELE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTruncation.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemTruncation.lean#L201). The attribute's comment: “(2) implies (1) only, and with (2) in the equivalent form that each one-degree truncation system (τ^\{≥p}τ^\{≤p}K\_n) is pro-isomorphic to a Deligne system, for a Deligne-system assignment and a t-structure supplied as data. (1) implies (2) is not proved: it is Stacks 0G4R, whose Artin-Rees content the library does not have.”.

> **Stacks Project, Tag 0G4S**, the implication (2) ⇒ (1). Let `j^* : 𝒟 ⥤ 𝒞` be a triangulated
> functor with a Deligne system assignment, `t` a `t`-structure on `𝒟`, and `(K_n)` an inverse
> sequence of `𝒟` whose terms lie in the degree range `[a, b]`. If each one-degree truncation
> `τ^{≥p}τ^{≤p}K_n`, for `a ≤ p ≤ b`, is pro-isomorphic to a Deligne system, then `(K_n)` is.

```lean
public theorem DeligneSystemValues.proIsoDeligne_of_truncGELE {jstar : 𝒟 ⥤ 𝒞} [jstar.Additive]
    [jstar.CommShift ℤ] [jstar.IsTriangulated] (A : DeligneSystemValues jstar)
    (t : TStructure 𝒟) {a b : ℤ} (hab : a ≤ b) (K : ℕᵒᵖ ⥤ 𝒟)
    (hGE : ∀ n, t.IsGE (K.obj n) a) (hLE : ∀ n, t.IsLE (K.obj n) b)
    (H : ∀ p : ℤ, a ≤ p → p ≤ b → A.ProIsoDeligne (K ⋙ t.truncGELE p p)) :
    A.ProIsoDeligne K
```

## Tag 0G4T, a lemma

[Tag 0G4T](https://stacks.math.columbia.edu/tag/0G4T) in the Stacks Project.

**`AlgebraicGeometry.proIsoDeligneSystem_iff_forall_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemCovering.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DeligneSystemCovering.lean#L271).

> **Stacks Project, Tag 0G4T.** Let `j : U → X` be an open immersion of Noetherian schemes, let
> `(K_n)` be an inverse system in `D^b_{Coh}(𝒪_X)` and let `X = W_1 ∪ … ∪ W_r` be a finite open
> covering. Then `(K_n)` is pro-isomorphic to a Deligne system if and only if, for each `i`, the
> restriction `(K_n|_{W_i})` is pro-isomorphic to a Deligne system with respect to the open
> immersion `U ∩ W_i → W_i`.
>
> The covering is any family `W : ι → X.Opens` indexed by a finite type, with `⨆ i, W i = ⊤`; the
> open immersion `U ∩ W_i → W_i` is the restriction `j ∣_ W i` of `j`.

```lean
public theorem proIsoDeligneSystem_iff_forall_restrict (j : U ⟶ X) [IsOpenImmersion j]
    [IsNoetherian X] (F : ℕᵒᵖ ⥤ BoundedCoherentDerived X) {ι : Type*} [Finite ι]
    (W : ι → X.Opens) (hW : ⨆ i, W i = ⊤) :
    ProIsoDeligneSystem j F ↔
      ∀ i, ProIsoDeligneSystem (j ∣_ W i) (F ⋙ restrictBoundedCoherentLift (W i).ι)
```

## Tag 0G4U, a lemma

[Tag 0G4U](https://stacks.math.columbia.edu/tag/0G4U) in the Stacks Project.

**`AlgebraicGeometry.exists_deligneSystem_proIso_derivedTensorIdealPowerSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DerivedTensorIdealPowerDeligne.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ExtensionZeroCoherent/DerivedTensorIdealPowerDeligne.lean#L159).

> **Stacks Project, Tag 0G4U.** Let `j : U ⟶ X` be an open immersion of Noetherian schemes, let
> `𝓘 ⊆ 𝒪_X` be a quasi-coherent sheaf of ideals with `V(𝓘) = X ∖ U`, and let `K` be in
> `D^b_{Coh}(𝒪_X)`. Then the inverse system `(K ⊗^L_{𝒪_X} 𝓘^n)_n` is pro-isomorphic to a Deligne
> system whose restriction to `U` is constant with value `K|_U`.
>
> The derived tensor product is that of [Stacks, Tag 06YU]
> (`AlgebraicGeometry.derivedTensorIdealPowerSystem`), and the pro-isomorphism is one of pro-objects
> of `D(𝒪_X)`: the terms `K ⊗^L 𝓘^n` are not in `D^b_{Coh}(𝒪_X)` in general. The Deligne system
> produced is `(𝓘^n 𝓕^•)` for a bounded complex `𝓕^•` of coherent modules representing `K`, with the
> given ideal sheaf `𝓘`.

```lean
public theorem exists_deligneSystem_proIso_derivedTensorIdealPowerSystem (j : U ⟶ X)
    [IsOpenImmersion j] [IsNoetherian X] (I : X.IdealSheafData)
    (hI : (I.support : Set X) = (Set.range j.base)ᶜ) (K : BoundedCoherentDerived X) :
    ∃ D : DeligneSystem j,
      Nonempty (D.system ⋙ restrictBoundedCoherent j ≅
        (Functor.const ℕᵒᵖ).obj ((restrictBoundedCoherent j).obj K)) ∧
      Nonempty (ProSeq.of (derivedTensorIdealPowerSystem I K.obj) ≅
        ProSeq.of (D.system ⋙ (boundedCoherentDerived X).ι))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.30, Tag 0G2G](https://stacks.math.columbia.edu/tag/0G2G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
