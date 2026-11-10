---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.conormalModuleOfImmersion, AlgebraicGeometry.Space.conormalModule, AlgebraicGeometry.Space.conormalIdealQuotientIso, AlgebraicGeometry.Space.isQuasicoherentOnSite_conormalModuleOfImmersion, AlgebraicGeometry.Space.isQuasicoherentOnSite_and_nonempty_conormalIdealQuotientIso, AlgebraicGeometry.Space.conormalModuleEtaleRestrictionIso, AlgebraicGeometry.Space.conormalModuleEtaleRestrictionCanonicalIso, AlgebraicGeometry.Space.conormalModuleEtaleRestrictionCanonicalIso_comp
statement: formalized
proof: formalized
---

# 76.5 Conormal sheaf of an immersion

Section 76.5 of the Stacks Project, [Tag 04CM](https://stacks.math.columbia.edu/tag/04CM). 6 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04CN, a definition

[Tag 04CN](https://stacks.math.columbia.edu/tag/04CN) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalModuleOfImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebra.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalAlgebra.lean#L410). The attribute's comment: “construction as the pullback of the ideal sheaf, via the closed factorisation”.

> **Stacks 04CN for an immersion.**  The conormal module `𝒞_{Z/X}` of an immersion
> `i : Z ⟶ X` of algebraic spaces: the inverse image along the closed factorisation
> `Z ⟶ X ∖ ∂Z` of the defining ideal sheaf of the image of that factorisation.
>
> Stacks 76.5 defines the conormal sheaf of an immersion to be the conormal sheaf of the closed
> immersion `i : Z ⟶ X ∖ ∂Z` of Stacks 04CE, which is what this is.  Unlike
> `AlgebraicGeometry.Space.conormalModule`, which returns a module on the closed subspace's own
> functor, this is a module on `Z` itself, as the source asks; the two are related by
> `AlgebraicGeometry.Space.conormalModuleOfImmersion_eq_conormalAlgebraOfImmersion_piece_one`
> below, which identifies this module with the degree-one piece of the conormal algebra
> `AlgebraicGeometry.Space.conormalAlgebraOfImmersion`.
>
> The source describes the module as `𝓘/𝓘²`, which is `i_*i^*𝓘`; the module documentation of
> `StacksFrontier.AlgebraicGeometry.Spaces.ConormalModule` records why `i^*𝓘` is that module
> and that the identification is not formalized, and the "What is not proved" section of this
> file records that quasi-coherence is not established either.

```lean
noncomputable def conormalModuleOfImmersion (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    Modules.{u, u} B S hS Z₀ hZ
```

**`AlgebraicGeometry.Space.conormalModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModule.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModule.lean#L192). The attribute's comment: “construction as the pullback of the ideal sheaf, closed immersion”. References: SGA 6 0 (2.1), “more general”.

> **Stacks 04CN for a closed immersion.**  The conormal module `𝒞_{Z/X}` of a closed subspace
> `Z` of an algebraic space `X`: the inverse image along the inclusion `i : Z ⟶ X` of the defining
> ideal sheaf `𝓘_Z ⊆ 𝒪_X` of Stacks 03MB.
>
> Stacks 76.5 describes this `𝒪_Z`-module as `𝓘/𝓘²`, which is `i_*i^*𝓘`; the implementation notes
> of this file record why `i^*𝓘` is that module and that the identification is not formalized
> here, and that this is the convention of the scheme-level `Stacks.Conormal.conormalSheaf`.

```lean
noncomputable def conormalModule (X : AlgebraicSpaces B S hS)
    (Z : ClosedSubspaces B S hS X.1) :
    Modules.{u, u} B S hS Z.1.toFunctor Z.2.1
```

**`AlgebraicGeometry.Space.conormalIdealQuotientIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersion.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersion.lean#L518). The attribute's comment: “the identification of the conormal module with 𝓘/𝓘², for a closed immersion”.

> **Stacks 04CN, the identification with `𝓘/𝓘²`.**  For a closed immersion `i : Z ⟶ X` of
> algebraic spaces the canonical map induced by the unit of `i^* ⊣ i_*` is an isomorphism
>
> `𝓘/𝓘² ≅ i_*𝒞_{Z/X}`,
>
> so the `𝒪_Z`-module `𝒞_{Z/X} = i^*𝓘` of `AlgebraicGeometry.Space.conormalModuleOfHom` is the one
> Stacks 76.5 describes as `𝓘/𝓘²`.  The characterising property is
> `AlgebraicGeometry.Space.conormalIdealQuotientπ_comp_toPushforward`: composed with the
> projection `𝓘 ⟶ 𝓘/𝓘²` it is the unit.

```lean
def conormalIdealQuotientIso (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom) :
    conormalIdealQuotient B S hS i ≅
      (modulePushforward B S hS i).obj (conormalModuleOfHom B S hS i)
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_conormalModuleOfImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersion.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersion.lean#L569). The attribute's comment: “the conormal sheaf is a quasi-coherent module”.

> **The quasi-coherence clause of Stacks 04CN for an arbitrary immersion**, unconditionally:
> the closed factorisation of Stacks 04CE is a closed immersion, where
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_conormalModuleOfHom` applies.
>
> The definition of the source calls `𝒞_{Z/X}` *the quasi-coherent `𝒪_Z`-module* `𝓘/𝓘²`; this is
> that clause of the definition, which `AlgebraicGeometry.Space.conormalModuleOfImmersion` — being
> a definition — cannot itself state.

```lean
theorem isQuasicoherentOnSite_conormalModuleOfImmersion (hX : IsAlgebraicSpace B S hS X₀)
    (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀) (hi : IsImmersion B S hS i) :
    (conormalModuleOfImmersion B S hS hX hZ i hi).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_and_nonempty_conormalIdealQuotientIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersion.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersion.lean#L599).

> **Stacks Project, Tag 04CN.**  The *conormal sheaf* `𝒞_{Z/X}` of an immersion
> `i : Z ⟶ X` of algebraic spaces over `S`, constructed as
> `AlgebraicGeometry.Space.conormalModuleOfImmersion` through the closed immersion of `Z` into the
> complement `X ∖ ∂Z` of the boundary of its image (Stacks 04CE), is the quasi-coherent
> `𝒪_Z`-module `𝓘/𝓘²` of the source: it is quasi-coherent, and for `𝓘` the ideal sheaf of `Z` in
> `X ∖ ∂Z` its direct image along that closed immersion is `𝓘/𝓘²`.

```lean
theorem isQuasicoherentOnSite_and_nonempty_conormalIdealQuotientIso
    (hX : IsAlgebraicSpace B S hS X₀) (hZ : IsAlgebraicSpace B S hS Z₀) (i : Z₀ ⟶ X₀)
    (hi : IsImmersion B S hS i) :
    (conormalModuleOfImmersion B S hS hX hZ i hi).IsQuasicoherentOnSite ∧
      Nonempty (conormalIdealQuotient B S hS (immersionClosedFactorization B S hS hX hZ i hi) ≅
        (modulePushforward B S hS (immersionClosedFactorization B S hS hX hZ i hi)).obj
          (conormalModuleOfImmersion B S hS hX hZ i hi))
```

## Tag 04CO, a lemma

[Tag 04CO](https://stacks.math.columbia.edu/tag/04CO) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalModuleEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleEtaleRestriction.lean, line 954](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleEtaleRestriction.lean#L954). The attribute's comment: “the conormal module commutes with etale base change”. References: SGA 3 I (6.8.5), “étale base change”.

> **Stacks 04CO for the conormal module.**  Let `φ : U ⟶ X` be an étale morphism of algebraic
> spaces and `Z ⊆ X` a closed subspace, with inverse image `Z_U = U ×_X Z` and projection
> `p : Z_U ⟶ Z`.  Then the inverse image along `p` of the conormal module of `Z` in `X` is the
> conormal module of `Z_U` in `U`:
>
> `𝒞_{Z/X}|_{Z_U} = p^*𝒞_{Z/X} ≅ 𝒞_{Z_U/U}`.
>
> The isomorphism is the square comparison `p^*i^* ≅ i_U^*φ^*` of
> `AlgebraicGeometry.Space.conormalPullbackCompIso`, then the inverse image along `i_U` of the
> identification of `φ^*` with étale restriction of [Stacks Project, Tag 03LW], then the equality
> `𝓘_Z|_U = 𝓘_{Z_U}` of defining ideal sheaves.

```lean
noncomputable def conormalModuleEtaleRestrictionIso (φ : U ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (Z : ClosedSubspaces B S hS X.1) :
    (modulePullback B S hS
          (ObjectProperty.homMk (Z.1.fromPreimage φ.hom) :
            (⟨(Z.1.preimage φ.hom).toFunctor,
                (isClosedSubspace_preimage B S hS φ.hom Z.1 X.2 U.2 Z.2).1⟩ :
              AlgebraicSpaces B S hS) ⟶
            (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS))).obj
        (conormalModule B S hS X Z) ≅
      conormalModule B S hS U (⟨Z.1.preimage φ.hom,
        isClosedSubspace_preimage B S hS φ.hom Z.1 X.2 U.2 Z.2⟩ :
        ClosedSubspaces B S hS U.1)
```

**`AlgebraicGeometry.Space.conormalModuleEtaleRestrictionCanonicalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleEtaleRestrictionCanonical.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleEtaleRestrictionCanonical.lean#L189). The attribute's comment: “the identification, as the canonical map of 04CP, for an etale source”.

> **Stacks 04CO.**  Let `Z ⊆ X` be a closed subspace of an algebraic space over `S`, let
> `g : X' ⟶ X` be étale — written `φ : U ⟶ X` in the source — and let
>
> ```
> Z_U --f--> Z
> |          |
> U  --g-->  X
> ```
>
> be a cartesian square, so that `Z_U = U ×_X Z` is the inverse image of `Z`.  Then the inverse
> image along `f` of the conormal module of `Z` in `X` is the conormal module of `Z_U` in `U`:
>
> `𝒞_{Z/X}|_{Z_U} = f^*𝒞_{Z/X} ≅ 𝒞_{Z_U/U}`.
>
> The identification is the canonical map of Stacks 04CP itself, which is invertible by
> `AlgebraicGeometry.Space.isIso_conormalMap_of_isPullback_of_isEtale`; it is therefore canonical by
> construction, and functorial in the étale source by
> `AlgebraicGeometry.Space.conormalModuleEtaleRestrictionCanonicalIso_comp`.

```lean
noncomputable def conormalModuleEtaleRestrictionCanonicalIso
    (Z : ClosedSubspaces B S hS X.1) (Z' : ClosedSubspaces B S hS X'.1) (g : X ⟶ X')
    (f : (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS) ⟶
      (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (hsq : subspaceInclusion B S hS X Z ≫ g = f ≫ subspaceInclusion B S hS X' Z')
    (hcart : IsPullback Z.1.ι f.hom g.hom Z'.1.ι)
    (hg : IsEtale B S hS g.hom) :
    (modulePullback B S hS f).obj (conormalModule B S hS X' Z') ≅
      conormalModule B S hS X Z
```

**`AlgebraicGeometry.Space.conormalModuleEtaleRestrictionCanonicalIso_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleEtaleRestrictionCanonical.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleEtaleRestrictionCanonical.lean#L239). The attribute's comment: “functoriality in the etale source U”.

> **Stacks 04CO, the functoriality in the étale source `U`.**  Let `Z ⊆ X` be a closed
> subspace, let `g' : X' ⟶ X''` and `g : X ⟶ X'` be étale — written `φ : U ⟶ X` and `ψ : V ⟶ U` in
> the source — and let the two squares
>
> ```
> Z   --f--> Z'  --f'--> Z''
> |          |           |
> X   --g--> X'  --g'--> X''
> ```
>
> both be cartesian.  Then the identification of Stacks 04CO for the composite `g ≫ g'` is the
> composition comparison of Stacks 03LU for `f` and `f'`, followed by the inverse image along `f`
> of the identification for `g'`, followed by the identification for `g`.
>
> The étaleness of the composite and the cartesianness of the outer rectangle are derived from the
> hypotheses, so what is assumed is exactly what the tag assumes.  The proof is the composition law
> for the canonical map, part (3) of Stacks 04G2
> (`AlgebraicGeometry.Space.conormalMap_comp`), together with
> `AlgebraicGeometry.Space.conormalModuleEtaleRestrictionCanonicalIso_hom`: because the
> identification *is* the canonical map, its functoriality is that law and needs nothing further.
> In particular the composition law for the identification of Stacks 03LW is not needed, which is
> what blocks the functoriality of the separately built isomorphism of
> `StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleEtaleRestriction.lean`.

```lean
theorem conormalModuleEtaleRestrictionCanonicalIso_comp
    (Z : ClosedSubspaces B S hS X.1) (Z' : ClosedSubspaces B S hS X'.1)
    (Z'' : ClosedSubspaces B S hS X''.1) (g : X ⟶ X') (g' : X' ⟶ X'')
    (f : (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS) ⟶
      (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (f' : (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS) ⟶
      (⟨Z''.1.toFunctor, Z''.2.1⟩ : AlgebraicSpaces B S hS))
    (hsq : subspaceInclusion B S hS X Z ≫ g = f ≫ subspaceInclusion B S hS X' Z')
    (hsq' : subspaceInclusion B S hS X' Z' ≫ g' = f' ≫ subspaceInclusion B S hS X'' Z'')
    (hcart : IsPullback Z.1.ι f.hom g.hom Z'.1.ι)
    (hcart' : IsPullback Z'.1.ι f'.hom g'.hom Z''.1.ι)
    (hg : IsEtale B S hS g.hom) (hg' : IsEtale B S hS g'.hom) :
    (conormalModuleEtaleRestrictionCanonicalIso B S hS Z Z'' (g ≫ g') (f ≫ f')
          (by rw [← Category.assoc, hsq, Category.assoc, hsq', Category.assoc])
          ((hcart.flip.paste_horiz hcart'.flip).flip)
          (isEtale_comp B S hS hg hg')).hom =
      (modulePullbackCompIso B S hS f f').inv.app (conormalModule B S hS X'' Z'') ≫
        (modulePullback B S hS f).map
            (conormalModuleEtaleRestrictionCanonicalIso B S hS Z' Z'' g' f' hsq' hcart' hg').hom ≫
          (conormalModuleEtaleRestrictionCanonicalIso B S hS Z Z' g f hsq hcart hg).hom
```

**`AlgebraicGeometry.Space.isLocallyClosedSubspace_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionEtaleRestriction.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionEtaleRestriction.lean#L168). The attribute's comment: “Z_U = U ×_X Z is a locally closed subspace of U”.

> **Stacks 04CO, the locally closed clause.**  The inverse image of a locally closed subspace
> of an algebraic space along a morphism of algebraic spaces over `S` is a locally closed subspace
> of the source.
>
> For an étale `f` this is the clause of Stacks 04CO that `Z_U = U ×_X Z` is a locally closed
> subspace of `U`; no étaleness is needed, the inverse image being the fibre product by
> Stacks 083Q and immersions being stable under base change by Stacks 02YW.

```lean
theorem isLocallyClosedSubspace_preimage
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : Y ⟶ X) (Z : Subfunctor X)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsLocallyClosedSubspace B S hS Z) :
    IsLocallyClosedSubspace B S hS (Z.preimage f)
```

**`AlgebraicGeometry.Space.conormalModuleOfImmersionEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionEtaleRestriction.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionEtaleRestriction.lean#L295). The attribute's comment: “the conormal module of an immersion commutes with etale localisation”.

> **Stacks 04CO.**  Let `i : Z ⟶ X` be an immersion of algebraic spaces over `S`, let
> `φ : U ⟶ X` be étale and let `Z_U = U ×_X Z` with projections `p : Z_U ⟶ Z` and `i_U : Z_U ⟶ U`.
> Then the inverse image along `p` of the conormal module of `Z` in `X` is the conormal module of
> `Z_U` in `U`:
>
> `𝒞_{Z/X}|_{Z_U} = p^*𝒞_{Z/X} ≅ 𝒞_{Z_U/U}`.
>
> Both conormal modules are taken through the closed factorisation of Stacks 04CE, as
> `AlgebraicGeometry.Space.immersionConormalModule`; `i_U` is an immersion because immersions are
> stable under base change.  The isomorphism is the degree-one instance of the conormal-algebra
> isomorphism of Stacks 09RR, conjugated by the bridge
> `AlgebraicGeometry.Space.conormalAlgebraOfImmersionPieceIso` at `i` and at `i_U`.

```lean
noncomputable def conormalModuleOfImmersionEtaleRestrictionIso (p : ZU ⟶ Z) (iU : ZU ⟶ U)
    (i : Z ⟶ X) (φ : U ⟶ X) (sq : IsPullback p iU i φ) (hi : IsImmersion B S hS i.hom)
    (hφ : IsEtale B S hS φ.hom) :
    (modulePullback B S hS p).obj (immersionConormalModule B S hS i hi) ≅
      immersionConormalModule B S hS iU (isImmersion_of_isPullback B S hS sq hi)
```

**`AlgebraicGeometry.Space.conormalModuleSubspaceEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionEtaleRestriction.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionEtaleRestriction.lean#L334). The attribute's comment: “the conormal module of a locally closed subspace commutes with etale localisation”.

> **Stacks 04CO in the shape the source states it.**  Let `Z` be a locally closed subspace of
> an algebraic space `X` over `S`, let `φ : U ⟶ X` be étale and let `Z_U = U ×_X Z` be the inverse
> image of `Z`, a locally closed subspace of `U` by
> `AlgebraicGeometry.Space.isLocallyClosedSubspace_preimage`.  Then the inverse image along the
> projection `p : Z_U ⟶ Z` of the conormal module of `Z` in `X` is the conormal module of `Z_U` in
> `U`.
>
> This is `AlgebraicGeometry.Space.conormalModuleOfImmersionEtaleRestrictionIso` at the cartesian
> square of Stacks 083Q, the inverse image being the fibre product by
> `CategoryTheory.Subfunctor.isPullback_preimage`.

```lean
noncomputable def conormalModuleSubspaceEtaleRestrictionIso (φ : U ⟶ X)
    (hφ : IsEtale B S hS φ.hom) (Z : Subfunctor X.1)
    (hZ : IsLocallyClosedSubspace B S hS Z) :
    (modulePullback B S hS (ObjectProperty.homMk (Z.fromPreimage φ.hom) :
          (⟨(Z.preimage φ.hom).toFunctor,
              (isLocallyClosedSubspace_preimage B S hS φ.hom Z X.2 U.2 hZ).1⟩ :
            AlgebraicSpaces B S hS) ⟶
          (⟨Z.toFunctor, hZ.1⟩ : AlgebraicSpaces B S hS))).obj
        (immersionConormalModule B S hS
          (ObjectProperty.homMk Z.ι : (⟨Z.toFunctor, hZ.1⟩ : AlgebraicSpaces B S hS) ⟶ X)
          hZ.2) ≅
      immersionConormalModule B S hS
        (ObjectProperty.homMk (Z.preimage φ.hom).ι :
          (⟨(Z.preimage φ.hom).toFunctor,
              (isLocallyClosedSubspace_preimage B S hS φ.hom Z X.2 U.2 hZ).1⟩ :
            AlgebraicSpaces B S hS) ⟶ U)
        (isLocallyClosedSubspace_preimage B S hS φ.hom Z X.2 U.2 hZ).2
```

**`AlgebraicGeometry.Space.conormalModuleSchemeEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleSchemeEtaleRestriction.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleSchemeEtaleRestriction.lean#L208).

> **Stacks 04CO.**  Let `i : Z ⟶ X` be an immersion of algebraic spaces over `S`, let `U` be a
> scheme of the site and `φ : U ⟶ X` étale.  Then
>
> * the fibre product `Z_U = U ×_X Z` is a scheme `R` of the site, and for every presentation of
>   it by a cartesian square with `j : R ⟶ U` and `p : Z_U ⟶ Z`:
> * `j` is an immersion of schemes, so `Z_U` is a locally closed subscheme of `U`;
> * the canonical map `𝒞_{Z/X}|_{Z_U} = p^*𝒞_{Z/X} ⟶ 𝒞_{Z_U/U}` — the canonical map of
>   [Stacks Project, Tag 04CP] of the square followed by part (1) of [Stacks Project, Tag 04G2],
>   whose target is the conormal sheaf `Stacks.Conormal.conormalSheaf` of the immersion of schemes
>   `j` of Morphisms, Definition [Stacks Project, Tag 01R2] read on the small étale site — is an
>   isomorphism;
> * this identification is functorial in `U`: for a morphism `ψ : U' ⟶ U` of schemes over `X`
>   with induced `b : Z_{U'} ⟶ Z_U`, the identification for `U'` is the restriction along `b` of
>   the identification for `U` followed by the canonical map of Morphisms, Lemma
>   [Stacks Project, Tag 01R4] of the schemes.

```lean
theorem conormalModuleSchemeEtaleRestriction (i : Z ⟶ X) (hi : IsImmersion B S hS i.hom)
    (φ : (⟨yoneda.obj V, isAlgebraicSpace_yoneda B S hS V⟩ : AlgebraicSpaces B S hS) ⟶ X)
    (hφ : IsEtale B S hS φ.hom) :
    (∃ (R : BigFppfOver B S hS) (j : R ⟶ V)
      (p : (⟨yoneda.obj R, isAlgebraicSpace_yoneda B S hS R⟩ : AlgebraicSpaces B S hS) ⟶ Z),
      IsPullback p (representedSpaceMap B S hS j) i φ) ∧
    ∀ {R : BigFppfOver B S hS} (j : R ⟶ V)
      (p : (⟨yoneda.obj R, isAlgebraicSpace_yoneda B S hS R⟩ : AlgebraicSpaces B S hS) ⟶ Z)
      (sq : IsPullback p (representedSpaceMap B S hS j) i φ),
      AlgebraicGeometry.IsImmersion ((BigFppfOver.toScheme B S hS).map j) ∧
      (haveI := isImmersion_toScheme_of_isPullback B S hS sq hi
      IsIso (conormalMapOfImmersions B S hS (representedSpaceMap B S hS j) i
        p φ
        (isImmersion_representedSpaceMap B S hS j) hi sq.w.symm ≫
        (conormalModuleOfImmersionRepresentedIso B S hS j).hom)) ∧
      ∀ {R' V' : BigFppfOver B S hS} (ψ : V' ⟶ V) (j' : R' ⟶ V') (b : R' ⟶ R)
        (hb : j' ≫ ψ = b ≫ j)
        (sq' : IsPullback (representedSpaceMap B S hS b ≫ p) (representedSpaceMap B S hS j') i
          (representedSpaceMap B S hS ψ ≫ φ)),
        haveI := isImmersion_toScheme_of_isPullback B S hS sq hi
        haveI := isImmersion_toScheme_of_isPullback B S hS sq' hi
        conormalMapOfImmersions B S hS (representedSpaceMap B S hS j') i
            (representedSpaceMap B S hS b ≫ p) (representedSpaceMap B S hS ψ ≫ φ)
            (isImmersion_representedSpaceMap B S hS j') hi sq'.w.symm ≫
          (conormalModuleOfImmersionRepresentedIso B S hS j').hom =
          (modulePullbackCompIso B S hS (representedSpaceMap B S hS b) p).inv.app
              (immersionConormalModule B S hS i hi) ≫
            (modulePullback B S hS (representedSpaceMap B S hS b)).map
              (conormalMapOfImmersions B S hS (representedSpaceMap B S hS j) i
            p φ
            (isImmersion_representedSpaceMap B S hS j) hi sq.w.symm ≫
                (conormalModuleOfImmersionRepresentedIso B S hS j).hom) ≫
            (representedAssociatedModulePullbackIso B S hS b
                (relativelyRepresentable_yoneda_map B S hS b)
                (Stacks.Conormal.conormalSheaf ((BigFppfOver.toScheme B S hS).map j))).hom ≫
            (representedSmallEtaleModuleEquivalence B S hS R').functor.map
              ((_root_.AlgebraicGeometry.SmallEtale.associatedModule (associatedBigEtaleSite B)
                  ((BigFppfOver.toScheme B S hS).obj R') R'.left.property).map
                (Stacks.Immersion.immersionConormalSheafMap
                  ((BigFppfOver.toScheme B S hS).map j')
                  ((BigFppfOver.toScheme B S hS).map j)
                  ((BigFppfOver.toScheme B S hS).map b)
                  ((BigFppfOver.toScheme B S hS).map ψ)
                  (toShHom_square_of_comp_eq B S hS j' j b ψ hb)))
```

**`AlgebraicGeometry.Space.etaleIdealSheafRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleIdealSheafRestriction.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleIdealSheafRestriction.lean#L196). The attribute's comment: “the ideal sheaf of the inverse image is the restriction of the ideal sheaf”.

> **Stacks 04CO.** The étale restriction of the defining ideal sheaf of a closed subspace
> `Z ⊆ X` along an étale `φ : U ⟶ X` is the defining ideal sheaf of the inverse image `φ⁻¹(Z)`.
>
> Over every étale chart of `U` the two sheaves have the same sections, by
> `AlgebraicGeometry.Space.definingIdealAt_preimage_eq_definingIdealAt_postcomp`, and this
> isomorphism is the identity on the underlying regular functions there.

```lean
noncomputable def etaleIdealSheafRestrictionIso (φ : U ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (Z : ClosedSubspaces B S hS X.1) :
    (etaleModulePullback.{u, u} B S hS φ hφ).obj
        (definingIdealSheaf B S hS X Z).toSheafOfModules ≅
      (definingIdealSheaf B S hS U (⟨Z.1.preimage φ.hom,
        isClosedSubspace_preimage B S hS φ.hom Z.1 X.2 U.2 Z.2⟩ :
        ClosedSubspaces B S hS U.1)).toSheafOfModules
```

**`AlgebraicGeometry.Space.conormalModuleEtaleRestrictionIso_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsConormalAction.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SectionsConormalAction.lean#L294). The attribute's comment: “functoriality in the étale source”.

> **The functoriality of Stacks 04CO in the étale source.**  For étale morphisms
> `ψ : V ⟶ U` and `φ : U ⟶ X` of algebraic spaces with étale composite and a closed subspace
> `Z ⊆ X`, the identification `p^*𝒞_{Z/X} ≅ 𝒞_{Z_V/V}` of [Stacks Project, Tag 04CO] taken in two
> steps — the comparison of the inverse images along the two projections of [Stacks Project,
> Tag 03LU], then the inverse image along `q : ψ⁻¹(φ⁻¹Z) ⟶ φ⁻¹Z` of the identification for `φ`,
> then the identification for `ψ` over `φ⁻¹(Z)` — is the identification for `ψ ≫ φ` taken in one
> step.  This is the "functorially in `U`" of the source.
>
> The route is the one of [Stacks Project, Tag 04CP]: both sides are read through
> `AlgebraicGeometry.Space.conormalMap_eq_conormalModuleEtaleRestrictionIso_hom`, which identifies
> the canonical map of that tag at an étale restriction square with the forward map constructed by
> [Stacks Project, Tag 04CO], and the clause becomes part (3) of [Stacks Project, Tag 04G2] at the
> two stacked étale restriction squares, in the form
> `AlgebraicGeometry.Space.conormalMap_comp_of_spaces`.  The one-step identification for `ψ ≫ φ` is
> read at the *iterated* spelling `ψ⁻¹(φ⁻¹Z)` of the upper closed subspace and with the projection
> written as the composite `q ≫ p`, which costs nothing: an iota-crossing in a first-order argument
> position of `AlgebraicGeometry.Space.conormalMap` is free, so neither
> `AlgebraicGeometry.Space.closedSubspacePreimage_comp` nor
> `AlgebraicGeometry.Space.subspaceProjection_comp` has to be rewritten.
>
> The two-step composite is written out here rather than quoted as
> `AlgebraicGeometry.Space.conormalEtaleRestrictionTwoStep`; the implementation notes of this file
> record why, and that the difference is one of spelling and not of content.

```lean
theorem conormalModuleEtaleRestrictionIso_hom_comp (ψ : V ⟶ U) (φ : U ⟶ X)
    (hψ : IsEtale C S hS ψ.hom) (hφ : IsEtale C S hS φ.hom)
    (hψφ : IsEtale C S hS (ψ ≫ φ).hom) (Z : ClosedSubspaces C S hS X.1) :
    (modulePullbackCompIso C S hS
          (ObjectProperty.homMk ((Z.1.preimage φ.hom).fromPreimage ψ.hom) :
        (⟨((Z.1.preimage φ.hom).preimage ψ.hom).toFunctor,
          (isClosedSubspace_preimage C S hS ψ.hom (Z.1.preimage φ.hom) U.2 V.2
            (isClosedSubspace_preimage C S hS φ.hom Z.1 X.2 U.2 Z.2)).1⟩ :
        AlgebraicSpaces C S hS) ⟶
        (⟨(Z.1.preimage φ.hom).toFunctor,
          (isClosedSubspace_preimage C S hS φ.hom Z.1 X.2 U.2 Z.2).1⟩ :
        AlgebraicSpaces C S hS))
          (ObjectProperty.homMk (Z.1.fromPreimage φ.hom) :
        (⟨(Z.1.preimage φ.hom).toFunctor,
          (isClosedSubspace_preimage C S hS φ.hom Z.1 X.2 U.2 Z.2).1⟩ :
        AlgebraicSpaces C S hS) ⟶
        (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces C S hS))).inv.app (conormalModule C S hS X Z) ≫
        (modulePullback C S hS
            (ObjectProperty.homMk ((Z.1.preimage φ.hom).fromPreimage ψ.hom) :
        (⟨((Z.1.preimage φ.hom).preimage ψ.hom).toFunctor,
          (isClosedSubspace_preimage C S hS ψ.hom (Z.1.preimage φ.hom) U.2 V.2
            (isClosedSubspace_preimage C S hS φ.hom Z.1 X.2 U.2 Z.2)).1⟩ :
        AlgebraicSpaces C S hS) ⟶
        (⟨(Z.1.preimage φ.hom).toFunctor,
          (isClosedSubspace_preimage C S hS φ.hom Z.1 X.2 U.2 Z.2).1⟩ :
        AlgebraicSpaces C S hS))).map
          (conormalModuleEtaleRestrictionIso C S hS φ hφ Z).hom ≫
          (conormalModuleEtaleRestrictionIso C S hS ψ hψ
            (⟨Z.1.preimage φ.hom,
          isClosedSubspace_preimage C S hS φ.hom Z.1 X.2 U.2 Z.2⟩ :
          ClosedSubspaces C S hS U.1)).hom =
      (conormalModuleEtaleRestrictionIso C S hS (ψ ≫ φ) hψφ Z).hom
```

## Tag 04CP, a lemma

[Tag 04CP](https://stacks.math.columbia.edu/tag/04CP) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFunctorial.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFunctorial.lean#L283). The attribute's comment: “the canonical map, for closed immersions”.

> **Stacks 04CP for closed immersions.**  The canonical map of `𝒪_Z`-modules
> `f^*𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` attached to a commutative square of algebraic spaces in which `Z` is a
> closed subspace of `X` and `Z'` a closed subspace of `X'`: the inverse image along the inclusion
> of `Z` of `AlgebraicGeometry.Space.idealSheafMap`, read through the identification
> `f^*(i')^* ≅ i^*g^*` of `AlgebraicGeometry.Space.conormalPullbackCompIso`.
>
> The source states the lemma for immersions and reduces it to closed immersions at the start of
> its proof; the lemma for arbitrary immersions is
> `AlgebraicGeometry.Space.conormalMapOfImmersions`, and the implementation notes of this file say
> why the closed case is the one carried here.

```lean
noncomputable def conormalMap
    (hsq : subspaceInclusion B S hS X Z ≫ g = f ≫ subspaceInclusion B S hS X' Z') :
    (modulePullback B S hS f).obj (conormalModule B S hS X' Z') ⟶
      conormalModule B S hS X Z
```

**`AlgebraicGeometry.Space.conormalMapOfImmersions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionFunctorial.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleImmersionFunctorial.lean#L601). The attribute's comment: “the canonical map, for arbitrary immersions”.

> **Stacks 04CP.**  Let
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
> be a commutative square of algebraic spaces over `S` in which `i` and `i'` are immersions.  Then
> there is a canonical map of `𝒪_Z`-modules
>
> `f^*𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}`
>
> between the conormal modules of the two immersions.
>
> The conormal modules are `AlgebraicGeometry.Space.immersionConormalModule`, the conormal
> modules taken through the canonical closed factorisation of Stacks 04CE, which is how the
> source's reduction of an immersion to a closed immersion into an open subspace is carried.  The
> map is the degree-one canonical map `AlgebraicGeometry.Space.conormalAlgebraSquarePieceMap` of
> the square, conjugated by the bridge `AlgebraicGeometry.Space.conormalAlgebraOfImmersionPieceIso`
> at `i'` and at `i`; the module documentation of this file explains why that construction needs no
> choice of ambient open subspaces and no hypothesis beyond the commutativity of the square.

```lean
noncomputable def conormalMapOfImmersions (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z') (g : X ⟶ X')
    (hi : IsImmersion B S hS i.hom) (hi' : IsImmersion B S hS i'.hom)
    (hsq : i ≫ g = f ≫ i') :
    (modulePullback B S hS f).obj (immersionConormalModule B S hS i' hi') ⟶
      immersionConormalModule B S hS i hi
```

## Tag 04G2, a lemma

[Tag 04G2](https://stacks.math.columbia.edu/tag/04G2) in the Stacks Project.

**`Stacks.Immersion.immersionConormalSheafMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean#L454). The attribute's comment: “part (3) for schemes”.

> **[Stacks Project, Tag 01R4] is functorial for stacked squares.** For two commutative squares
> of immersions stacked vertically, the induced map of conormal sheaves of the composite square is
> the composite of the two induced maps, read through the pullback composition isomorphism
> `RingedSpaceModuleAdjunction.modulePullbackComp`.
>
> The source states no such law; it is what makes the map of the tag a map of *pseudofunctors*, and
> it is what transports the map along a restriction of the ambient scheme.
>
> The proof is `Stacks.Immersion.immersionConormalSheafMap_unique`: the composite is shown to
> satisfy the affine characterisation of the composite square. A pair of affine opens `U ⊆ X₁` and
> `P ⊆ X₃` need not factor through an affine open of `X₂`, so the characterisation is verified after
> restricting to the affine opens `U₀ ⊆ U` that do, by
> `Stacks.Immersion.transpose_comp_eq_of_affineModel` and
> `Stacks.Tag01R3PartTwo.affineConormalIsoCotangent_restrict`; those cover `i₁⁻¹U`, since the
> square carries a point of it into the coborder of the range of `i₂`.

```lean
theorem immersionConormalSheafMap_comp {Z₁ Z₂ Z₃ X₁ X₂ X₃ : Scheme.{u}}
    (i₁ : Z₁ ⟶ X₁) (i₂ : Z₂ ⟶ X₂) (i₃ : Z₃ ⟶ X₃)
    [IsImmersion i₁] [IsImmersion i₂] [IsImmersion i₃]
    (f₁ : Z₁ ⟶ Z₂) (g₁ : X₁ ⟶ X₂) (comm₁ : i₁ ≫ g₁ = f₁ ≫ i₂)
    (f₂ : Z₂ ⟶ Z₃) (g₂ : X₂ ⟶ X₃) (comm₂ : i₂ ≫ g₂ = f₂ ≫ i₃) :
    immersionConormalSheafMap i₁ i₃ (f₁ ≫ f₂) (g₁ ≫ g₂)
        (toShHom_square (square_comp comm₁ comm₂)) =
      (modulePullbackComp f₁.toLRSHom.toShHom f₂.toLRSHom.toShHom).hom.app
          (conormalSheaf i₃.liftCoborder.toLRSHom.toShHom) ≫
        (modulePullback f₁.toLRSHom.toShHom).map
          (immersionConormalSheafMap i₂ i₃ f₂ g₂ (toShHom_square comm₂)) ≫
        immersionConormalSheafMap i₁ i₂ f₁ g₁ (toShHom_square comm₁)
```

**`AlgebraicGeometry.Space.conormalModuleOfImmersionRepresentedIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalLeadingIdentityStack.lean, line 657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalLeadingIdentityStack.lean#L657). The attribute's comment: “part (2): for a commutative square of the big fppf site whose two horizontal morphisms are immersions of schemes, the comparison of part (1) carries the canonical map of conormal modules of 04CP to the associated module of the canonical map of Morphisms, Lemma 01R4”.

> **Part (2) of [Stacks Project, Tag 04G2] at immersion generality.**
>
> For a commutative square of the big fppf category over `S` whose horizontal morphisms are
> immersions of schemes — the generality at which [Stacks Project, Tag 04CP] states its hypothesis,
> and so the generality of the clause — the comparison of part (1)
> (`AlgebraicGeometry.Space.conormalModuleOfImmersionRepresentedIso`) carries the canonical map of
> conormal modules of [Stacks Project, Tag 04CP] to the associated module of
> `Stacks.Immersion.immersionConormalSheafMap`, the canonical map of Morphisms, Lemma
> [Stacks Project, Tag 01R4].
>
> `AlgebraicGeometry.Space.conormalMapOfImmersions_conormalModuleOfImmersionRepresentedIso` with its
> hypothesis `hnat` supplied by
> `AlgebraicGeometry.Space.conormalMapOfImmersions_naturality_of_immersions`.

```lean
theorem conormalModuleOfImmersionRepresentedIso_naturality (hsq : j ≫ a = b ≫ j') :
    conormalMapOfImmersions B S hS (representedSpaceMap B S hS j)
          (representedSpaceMap B S hS j') (representedSpaceMap B S hS b)
          (representedSpaceMap B S hS a) (isImmersion_representedSpaceMap B S hS j)
          (isImmersion_representedSpaceMap B S hS j')
          (representedSpaceMap_square_of_comp_eq B S hS j j' b a hsq) ≫
        (conormalModuleOfImmersionRepresentedIso B S hS j).hom =
      (modulePullback B S hS (representedSpaceMap B S hS b)).map
          (conormalModuleOfImmersionRepresentedIso B S hS j').hom ≫
        (representedAssociatedModulePullbackIso B S hS b
              (relativelyRepresentable_yoneda_map B S hS b)
              (Stacks.Conormal.conormalSheaf
                ((BigFppfOver.toScheme B S hS).map j'))).hom ≫
          (representedSmallEtaleModuleEquivalence B S hS R).functor.map
            ((_root_.AlgebraicGeometry.SmallEtale.associatedModule (associatedBigEtaleSite B)
                ((BigFppfOver.toScheme B S hS).obj R) R.left.property).map
              (Stacks.Immersion.immersionConormalSheafMap
                ((BigFppfOver.toScheme B S hS).map j)
                ((BigFppfOver.toScheme B S hS).map j')
                ((BigFppfOver.toScheme B S hS).map b)
                ((BigFppfOver.toScheme B S hS).map a)
                (toShHom_square_of_comp_eq B S hS j j' b a hsq)))
```

**`AlgebraicGeometry.Space.isIso_comp_conormalMap_of_isIso_conormalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleComposition.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleComposition.lean#L574). The attribute's comment: “invertibility of the conormal map of a composite, on the small étale site of an algebraic space”.

> **Invertibility of the conormal map of a composite descends to the two factors**, part (3)
> of [Stacks Project, Tag 04G2] in the form invertibility consumes.  If the conormal map of the
> outer rectangle is an isomorphism then so is the inverse image along `f` of the conormal map of
> the lower square followed by the conormal map of the upper square.
>
> Both composites have the inverse image along the inclusion of `Z` of the two maps of defining
> ideal sheaves of [Stacks Project, Tag 04CP] as a right factor, and in both the left factor is a
> composite of comparison isomorphisms; so the hypothesis makes that common right factor
> invertible, and with it the second composite.

```lean
theorem isIso_comp_conormalMap_of_isIso_conormalMap
    (hiso : IsIso (conormalMap B S hS Z Z'' (g ≫ g') (f ≫ f') hsq'')) :
    IsIso ((modulePullback B S hS f).map (conormalMap B S hS Z' Z'' g' f' hsq') ≫
      conormalMap B S hS Z Z' g f hsq)
```

**`AlgebraicGeometry.Space.conormalMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleComposition.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleComposition.lean#L641). The attribute's comment: “part (3), for closed subspaces of algebraic spaces”.

> **The composition formula for conormal maps**, part (3) of [Stacks Project, Tag 04G2], for
> closed subspaces of algebraic spaces.  For two vertically composable commutative squares of
> closed subspaces, the conormal map `(f ≫ f')^*𝒞_{Z''/X''} ⟶ 𝒞_{Z/X}` of the outer rectangle is
> the inverse image along `f` of the conormal map of the lower square followed by the conormal map
> of the upper square, read through the composition comparison
> `AlgebraicGeometry.Space.modulePullbackCompIso` of [Stacks Project, Tag 03LU].
>
> Both sides have the inverse image along the inclusion of `Z` of the two maps of defining ideal
> sheaves as a right factor, by `AlgebraicGeometry.Space.idealSheafMap_comp`; the two left factors
> agree by the pasting `AlgebraicGeometry.Space.conormalPullbackCompIso_paste_app` of the
> comparisons of the two squares.

```lean
theorem conormalMap_comp :
    conormalMap B S hS Z Z'' (g ≫ g') (f ≫ f') hsq'' =
      (modulePullbackCompIso B S hS f f').inv.app (conormalModule B S hS X'' Z'') ≫
        (modulePullback B S hS f).map (conormalMap B S hS Z' Z'' g' f' hsq') ≫
          conormalMap B S hS Z Z' g f hsq
```

**`AlgebraicGeometry.Space.conormalMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleComposition.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleComposition.lean#L641). The attribute's comment: “part (3): the composition law for the conormal map, on the small étale site of an algebraic space”.

> **The composition formula for conormal maps**, part (3) of [Stacks Project, Tag 04G2], for
> closed subspaces of algebraic spaces.  For two vertically composable commutative squares of
> closed subspaces, the conormal map `(f ≫ f')^*𝒞_{Z''/X''} ⟶ 𝒞_{Z/X}` of the outer rectangle is
> the inverse image along `f` of the conormal map of the lower square followed by the conormal map
> of the upper square, read through the composition comparison
> `AlgebraicGeometry.Space.modulePullbackCompIso` of [Stacks Project, Tag 03LU].
>
> Both sides have the inverse image along the inclusion of `Z` of the two maps of defining ideal
> sheaves as a right factor, by `AlgebraicGeometry.Space.idealSheafMap_comp`; the two left factors
> agree by the pasting `AlgebraicGeometry.Space.conormalPullbackCompIso_paste_app` of the
> comparisons of the two squares.

```lean
theorem conormalMap_comp :
    conormalMap B S hS Z Z'' (g ≫ g') (f ≫ f') hsq'' =
      (modulePullbackCompIso B S hS f f').inv.app (conormalModule B S hS X'' Z'') ≫
        (modulePullback B S hS f).map (conormalMap B S hS Z' Z'' g' f' hsq') ≫
          conormalMap B S hS Z Z' g f hsq
```

**`AlgebraicGeometry.Space.conormalModuleClosedSubspaceRangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleSchemeAgreement.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleSchemeAgreement.lean#L427). The attribute's comment: “part (1): the conormal sheaf of a closed immersion of schemes of the site is the associated module of the conormal sheaf of Morphisms, Definition 01R2”.

> **Stacks 04G2, part (1).**  For a morphism `j` of the big fppf category over `S` whose
> underlying morphism of schemes is a closed immersion, the conormal module of [Stacks Project,
> Tag 04CN] of the closed subspace which `j` cuts out of `yoneda.obj V` — read on `yoneda.obj R`
> along the identification `AlgebraicGeometry.Space.rangeSpaceIso` of that subspace with it — is
> the module which the conormal sheaf of [Stacks Project, Tag 01R2] of the underlying morphism of
> schemes becomes on the small étale site.
>
> This is the closed case.  The clause at the immersion generality the source states it at is
> `AlgebraicGeometry.Space.conormalModuleOfImmersionRepresentedIso`, which is this comparison
> applied to the factorisation of the immersion through its ambient open.

```lean
noncomputable def conormalModuleClosedSubspaceRangeIso :
    (modulePullback B S hS (rangeSpaceIso B S hS j hj).hom).obj
        (conormalModule B S hS ⟨yoneda.obj V, isAlgebraicSpace_yoneda B S hS V⟩
          (closedSubspaceRange B S hS j hj)) ≅
      (representedSmallEtaleModuleEquivalence B S hS R).functor.obj
        ((_root_.AlgebraicGeometry.SmallEtale.associatedModule (associatedBigEtaleSite B)
            ((BigFppfOver.toScheme B S hS).obj R) R.left.property).obj
          (Stacks.Conormal.conormalSheaf ((BigFppfOver.toScheme B S hS).map j)))
```

**`AlgebraicGeometry.Space.conormalModuleOfImmersionRepresentedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleSchemeAgreementImmersion.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleSchemeAgreementImmersion.lean#L196). The attribute's comment: “part (1): for an immersion of schemes of the site, the conormal sheaf of 04CN of the represented morphism is the associated module of the conormal sheaf of Morphisms, Definition 01R2”.

> **Stacks 04G2, part (1).**  For a morphism `j : R ⟶ V` of the big fppf category over `S`
> whose underlying morphism of schemes is an **immersion**, the conormal module of [Stacks Project,
> Tag 04CN] of the morphism of algebraic spaces `yoneda.obj R ⟶ yoneda.obj V` which `j` represents
> is the module which the conormal sheaf of Morphisms, Definition [Stacks Project, Tag 01R2] of the
> underlying morphism of schemes becomes on the small étale site of `yoneda.obj R`.
>
> No hypothesis beyond the immersion of the source is carried: the closed case is
> `AlgebraicGeometry.Space.conormalModuleClosedSubspaceRangeIso`, and this is that comparison
> applied over the ambient open of [Stacks Project, Tag 04CE], transported back to `j` by
> [Stacks Project, Tag 04CO].

```lean
def conormalModuleOfImmersionRepresentedIso (j : R ⟶ V)
    [AlgebraicGeometry.IsImmersion ((BigFppfOver.toScheme B S hS).map j)] :
    immersionConormalModule B S hS (representedSpaceMap B S hS j)
        (isImmersion_representedSpaceMap B S hS j) ≅
      (representedSmallEtaleModuleEquivalence B S hS R).functor.obj
        ((_root_.AlgebraicGeometry.SmallEtale.associatedModule (associatedBigEtaleSite B)
            ((BigFppfOver.toScheme B S hS).obj R) R.left.property).obj
          (Stacks.Conormal.conormalSheaf ((BigFppfOver.toScheme B S hS).map j)))
```

**`AlgebraicGeometry.Space.conormalMapOfImmersions_comp_of_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSquarePieceMapCompositionLaw.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSquarePieceMapCompositionLaw.lean#L359). The attribute's comment: “part (3): the composition law for the canonical map of 04CP, for arbitrary immersions of algebraic spaces”.

> **Stacks 04G2, part (3), at the generality the source states it.**  Let
> ```
> Z₁ --i₁--→ X₁
> |          |
> f₁         g₁
> ↓          ↓
> Z₂ --i₂--→ X₂
> |          |
> f₂         g₂
> ↓          ↓
> Z₃ --i₃--→ X₃
> ```
> be two commutative squares of algebraic spaces over `S` whose horizontal arrows are
> **immersions**, stacked vertically.  Then the canonical map
> `(f₁ ≫ f₂)^*𝒞_{Z₃/X₃} ⟶ 𝒞_{Z₁/X₁}` of [Stacks Project, Tag 04CP] attached to the outer rectangle
> is the composition comparison of [Stacks Project, Tag 03LU] for `f₁` and `f₂`, followed by the
> inverse image along `f₁` of the map `f₂^*𝒞_{Z₃/X₃} ⟶ 𝒞_{Z₂/X₂}` of the lower square, followed by
> the map `f₁^*𝒞_{Z₂/X₂} ⟶ 𝒞_{Z₁/X₁}` of the upper square.
>
> The hypotheses are exactly the source's: the three immersions and the two commutativities, the
> commutativity of the outer rectangle being derived by
> `AlgebraicGeometry.Space.stackedSquare_comm`.  Nothing is assumed about closedness,
> quasi-compactness or quasi-coherence.

```lean
theorem conormalMapOfImmersions_comp_of_comm :
    conormalMapOfImmersions B S hS i₁ i₃ (f₁ ≫ f₂) (g₁ ≫ g₂) hi₁ hi₃
        (stackedSquare_comm B S hS i₁ i₂ i₃ f₁ g₁ f₂ g₂ hsq₁ hsq₂) =
      (modulePullbackCompIso B S hS f₁ f₂).inv.app
          (immersionConormalModule B S hS i₃ hi₃) ≫
        (modulePullback B S hS f₁).map
            (conormalMapOfImmersions B S hS i₂ i₃ f₂ g₂ hi₂ hi₃ hsq₂) ≫
          conormalMapOfImmersions B S hS i₁ i₂ f₁ g₁ hi₁ hi₂ hsq₁
```

## Tag 04CQ, a lemma

[Tag 04CQ](https://stacks.math.columbia.edu/tag/04CQ) in the Stacks Project.

**`AlgebraicGeometry.Space.epi_conormalMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeCartesian.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeCartesian.lean#L269). The attribute's comment: “surjectivity, at an arbitrary fibre product square”.

> **The surjectivity clause of [Stacks Project, Tag 04CQ].**  Let
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
> be a fibre product square of algebraic spaces over `S` in which `Z ⊆ X` and `Z' ⊆ X'` are closed
> subspaces and `i`, `i'` are their inclusions.  Then the canonical map of conormal modules
> `f^*𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` of [Stacks Project, Tag 04CP] is an epimorphism of `𝒪_Z`-modules.
>
> This is `AlgebraicGeometry.Space.epi_conormalMap` released from the canonical inverse-image
> square: by `AlgebraicGeometry.Space.closedSubspaces_eq_preimageSubspace_of_isPullback` the
> cartesian hypothesis makes `Z` the inverse image `g⁻¹(Z')` and by
> `AlgebraicGeometry.Space.vertical_eq_preimageProjection_of_isPullback` it makes `f` the
> projection, after which the square's commutativity proof and the canonical one are proofs of the
> same proposition.
>
> The horizontal arrows are closed immersions, where the source takes immersions; the
> implementation notes of this file record what the passage to the immersion case still needs.

```lean
theorem epi_conormalMap_of_isPullback
    (Z : ClosedSubspaces B S hS X.1) (Z' : ClosedSubspaces B S hS X'.1) (g : X ⟶ X')
    (f : (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS) ⟶
      (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (hsq : subspaceInclusion B S hS X Z ≫ g = f ≫ subspaceInclusion B S hS X' Z')
    (hcart : IsPullback Z.1.ι f.hom g.hom Z'.1.ι) :
    Epi (conormalMap B S hS Z Z' g f hsq)
```

**`AlgebraicGeometry.Space.isIso_conormalMap_of_isPullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeCartesian.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeCartesian.lean#L289). The attribute's comment: “flat isomorphism, at an arbitrary fibre product square”.

> **The flat clause of [Stacks Project, Tag 04CQ].**  For a fibre product square as in
> `AgebraicGeometry.Space.epi_conormalMap_of_isPullback`, if `g` is flat — that is, if the
> morphism of small étale ringed topoi it induces is flat in the sense of
> [Stacks Project, Tag 04JB] — then the canonical map of conormal modules
> `f^*𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` of [Stacks Project, Tag 04CP] is an isomorphism.
>
> This is `AlgebraicGeometry.Space.isIso_conormalMap_of_isFlat` released from the canonical
> inverse-image square, by the same two identifications.

```lean
theorem isIso_conormalMap_of_isPullback_of_isFlat
    (Z : ClosedSubspaces B S hS X.1) (Z' : ClosedSubspaces B S hS X'.1) (g : X ⟶ X')
    (f : (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS) ⟶
      (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (hsq : subspaceInclusion B S hS X Z ≫ g = f ≫ subspaceInclusion B S hS X' Z')
    (hcart : IsPullback Z.1.ι f.hom g.hom Z'.1.ι)
    (hg : (smallEtaleRingedToposHom B S hS g).IsFlat) :
    IsIso (conormalMap B S hS Z Z' g f hsq)
```

**`AlgebraicGeometry.Space.epi_conormalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeEpi.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeEpi.lean#L230). The attribute's comment: “surjectivity”.

> **The surjectivity clause of [Stacks Project, Tag 04CQ], for closed immersions.**  Let `Z'`
> be a closed subspace of an algebraic space `X'` and let `g : X ⟶ X'` be a morphism of algebraic
> spaces.  For the fibre product square — the one whose upper closed subspace is the inverse image
> `g⁻¹(Z') ⊆ X` of [Stacks Project, Tag 083Q] and whose vertical morphism is the projection
> `g⁻¹(Z') ⟶ Z'` — the canonical map of conormal modules
> `f^*𝒞_{Z'/X'} ⟶ 𝒞_{g⁻¹(Z')/X}` of [Stacks Project, Tag 04CP] is an epimorphism of
> `𝒪_{g⁻¹(Z')}`-modules.
>
> The source states the lemma for immersions and reduces it to closed immersions at the start of
> the proof of [Stacks Project, Tag 04CP]; the closed case is the one this development carries,
> for the reasons recorded in the implementation notes of
> `StacksFrontier/AlgebraicGeometry/Spaces/ConormalModule.lean`.  The flat clause of the tag is not
> proved; see the "What is not proved" section of this file.
>
> Surjectivity of a map of modules on the small étale site means that the map is an epimorphism,
> which by [Stacks Project, Tag 01AH] is local surjectivity; the chartwise statement behind it is
> `AlgebraicGeometry.Space.surjective_idealSheafMap_val_app`.

```lean
theorem epi_conormalMap (g : X ⟶ X') (Z' : ClosedSubspaces B S hS X'.1) :
    Epi (conormalMap B S hS (preimageSubspace B S hS g Z') Z' g
      (preimageProjection B S hS g Z')
      (conormalEtaleRestrictionSquare B S hS g Z'))
```

**`AlgebraicGeometry.Space.isIso_conormalMap_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeFlat.lean, line 783](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeFlat.lean#L783). The attribute's comment: “isomorphism when the morphism of small etale ringed topoi is flat”.

> **The flat clause of [Stacks Project, Tag 04CQ], for closed immersions.**  If `g` is flat —
> that is, if the morphism of small étale ringed topoi it induces is flat in the sense of
> [Stacks Project, Tag 04JB] — then the canonical map of conormal modules
> `f^*𝒞_{Z'/X'} ⟶ 𝒞_{g⁻¹(Z')/X}` of [Stacks Project, Tag 04CP] attached to the fibre product
> square is an isomorphism.

```lean
theorem isIso_conormalMap_of_isFlat (g : X ⟶ X') (Z' : ClosedSubspaces B S hS X'.1)
    (hg : (smallEtaleRingedToposHom B S hS g).IsFlat) :
    IsIso (conormalMap B S hS (preimageSubspace B S hS g Z') Z' g
      (preimageProjection B S hS g Z')
      (conormalEtaleRestrictionSquare B S hS g Z'))
```

**`AlgebraicGeometry.Space.epi_conormalMap_of_epi_idealSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFlatBaseChange.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFlatBaseChange.lean#L111). The attribute's comment: “surjectivity, reduced to surjectivity of the map of defining ideal sheaves”.

> **The surjectivity clause of Stacks 04CQ, reduced to the map of defining ideal sheaves.**
> If the map `g^*𝓘' ⟶ 𝓘` of `AlgebraicGeometry.Space.idealSheafMap` attached to a commutative
> square of closed subspaces is surjective, then so is the map `f^*𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` of
> conormal modules of [Stacks Project, Tag 04CP].
>
> `AlgebraicGeometry.Space.conormalMap` is the isomorphism
> `AlgebraicGeometry.Space.conormalPullbackComparison` followed by the inverse image along the
> inclusion of `Z` of the map of defining ideal sheaves.  The inverse image of modules is a left
> adjoint, by the adjunction of [Stacks Project, Tag 03LU], and a left adjoint preserves
> epimorphisms.
>
> Surjectivity of `g^*𝓘' ⟶ 𝓘` is what [Stacks Project, Tag 04CQ] obtains from cartesianness of the
> square, by reduction to the scheme-level [Stacks Project, Tag 0473]; that reduction is not
> carried in this development, so the hypothesis is assumed.  The invertibility clause reduces the
> same way, by `AlgebraicGeometry.Space.isIso_conormalMap_of_isIso_idealSheafMap`.

```lean
theorem epi_conormalMap_of_epi_idealSheafMap
    (hsq : subspaceInclusion B S hS X Z ≫ g = f ≫ subspaceInclusion B S hS X' Z')
    (h : Epi (idealSheafMap B S hS Z Z' g f hsq)) :
    Epi (conormalMap B S hS Z Z' g f hsq)
```

**`AlgebraicGeometry.Space.epi_conormalMapOfImmersions_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfImmersionBaseChange.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfImmersionBaseChange.lean#L577). The attribute's comment: “surjectivity, for a fibre product square of immersions”.

> **The surjectivity clause of [Stacks Project, Tag 04CQ].**  Let
> ```
> Z --i--→ X
> |        |
> f        g
> ↓        ↓
> Z' -i'-→ X'
> ```
> be a fibre product square of algebraic spaces over `S` in which `i` and `i'` are immersions.  Then
> the canonical map `f^*𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` of [Stacks Project, Tag 04CP] between the conormal
> modules of the two immersions is an epimorphism of `𝒪_Z`-modules.

```lean
theorem epi_conormalMapOfImmersions_of_isPullback
    (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z') (g : X ⟶ X')
    (hi : IsImmersion B S hS i.hom) (hi' : IsImmersion B S hS i'.hom)
    (hcart : IsPullback i f g i') :
    Epi (conormalMapOfImmersions B S hS i i' f g hi hi' hcart.w)
```

**`AlgebraicGeometry.Space.isIso_conormalMapOfImmersions_of_isPullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfImmersionBaseChange.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfImmersionBaseChange.lean#L606). The attribute's comment: “isomorphism when g is flat, for a fibre product square of immersions”.

> **The flat clause of [Stacks Project, Tag 04CQ].**  For a fibre product square as in
> `AlgebraicGeometry.Space.epi_conormalMapOfImmersions_of_isPullback`, if `g` is flat as a
> morphism of algebraic spaces (Stacks 03ML), then the canonical map `f^*𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` of
> [Stacks Project, Tag 04CP] is an isomorphism.

```lean
theorem isIso_conormalMapOfImmersions_of_isPullback_of_isFlat
    (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z') (g : X ⟶ X')
    (hi : IsImmersion B S hS i.hom) (hi' : IsImmersion B S hS i'.hom)
    (hcart : IsPullback i f g i') (hg : IsFlat B S hS g.hom) :
    IsIso (conormalMapOfImmersions B S hS i i' f g hi hi' hcart.w)
```

## Tag 06BD, a lemma

[Tag 06BD](https://stacks.math.columbia.edu/tag/06BD) in the Stacks Project.

**`AlgebraicGeometry.Space.epi_conormalMap_closedSubspaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeEpi.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeEpi.lean#L255). The attribute's comment: “exactness at the right term”.

> **Exactness at the right term of [Stacks Project, Tag 06BD].**  Let `Y` and `Z` be closed
> subspaces of an algebraic space `X` with `Z ⊆ Y`.  The canonical map `𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` of
> [Stacks Project, Tag 04CP], the right-hand map of the conormal sequence of the pair, is an
> epimorphism.
>
> This is the surjectivity clause of [Stacks Project, Tag 04CQ] at the fibre product square whose
> morphism of ambient spaces is the inclusion `j : Y ⟶ X`: the inverse image `j⁻¹(Z)` is `Z` read
> as a closed subspace of `Y`, and `𝒞_{Z/Y}` is its conormal module there.  The subspace of `Y` is
> taken as that inverse image rather than as `Z` itself because this development has no
> composition of closed subspaces, so no closed subspace of `Y` is attached to `Z` by any other
> route.  The hypothesis `Z ⊆ Y` is what makes that inverse image the subspace the source calls
> `Z`, and it is carried for that reason alone: the proof is the instance of Stacks 04CQ, which
> holds for any pair, so the hypothesis is not used and its name is prefixed accordingly.
>
> The exactness in the middle is not proved; see the "What is not proved" section of this file,
> which also names the composite-is-zero clause.

```lean
theorem epi_conormalMap_closedSubspaces (Y Z : ClosedSubspaces B S hS X.1)
    (_hZY : Z.1 ≤ Y.1) :
    Epi (conormalMap B S hS
      (preimageSubspace B S hS (subspaceInclusion B S hS X Y) Z) Z
      (subspaceInclusion B S hS X Y)
      (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)
      (conormalEtaleRestrictionSquare B S hS (subspaceInclusion B S hS X Y) Z))
```

**`AlgebraicGeometry.Space.conormalMap_comp_conormalMap_closedSubspaces_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleClosedSubspacesComplex.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleClosedSubspacesComplex.lean#L106). The attribute's comment: “the sequence is a complex: the composite of i^*𝒞_{Y/X} ⟶ 𝒞_{Z/X} and 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} is zero”.

> **The composite-is-zero clause of [Stacks Project, Tag 06BD].**  Let `Y` and `Z` be closed
> subspaces of an algebraic space `X` with `Z` contained in `Y` through `f : Z ⟶ Y`.  The composite
> of the two maps `i^*𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` of the conormal sequence of the pair is zero,
> so that the sequence is a complex; together with
> `AlgebraicGeometry.Space.epi_conormalMap_closedSubspaces` this makes it a complex, exact at its
> right term.
>
> Both maps are maps of [Stacks Project, Tag 04CP], the left one at the square of
> `AlgebraicGeometry.Space.closedSubspacesConormal_square` and the right one at the fibre product
> square of the inclusion `j : Y ⟶ X`.  By part (3) of [Stacks Project, Tag 04G2] their composite
> is the conormal map of the outer rectangle, whose morphism of ambient spaces is `j ≫ 𝟙 X = j`;
> that factors through the inclusion of `Y`, so
> `AlgebraicGeometry.Space.comp_conormalMap_eq_zero_of_factors` applies.
>
> Exactness in the middle is not proved; see the "What is not proved" section of
> `StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeEpi.lean`.

```lean
theorem conormalMap_comp_conormalMap_closedSubspaces_eq_zero
    (hf : f ≫ subspaceInclusion B S hS X Y = subspaceInclusion B S hS X Z) :
    (modulePullback B S hS
          (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)).map
        (conormalMap B S hS Z Y (𝟙 X : X ⟶ X) f
          (closedSubspacesConormal_square B S hS Y Z f hf)) ≫
      conormalMap B S hS
        (preimageSubspace B S hS (subspaceInclusion B S hS X Y) Z) Z
        (subspaceInclusion B S hS X Y)
        (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)
        (conormalEtaleRestrictionSquare B S hS (subspaceInclusion B S hS X Y) Z) = 0
```

**`AlgebraicGeometry.Space.conormalSequenceImmersion_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersion.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersion.lean#L263). The attribute's comment: “the canonical exact sequence i^*C_{Y/X} → C_{Z/X} → C_{Z/Y} → 0 for immersions Z → Y → X of algebraic spaces, with the maps of Tag 04CP: the composite is zero, the sequence is exact at C_{Z/X}, and C_{Z/X} → C_{Z/Y} is an epimorphism”.

> **[Stacks Project, Tag 06BD].**  Let `i : Z ⟶ Y` and `j : Y ⟶ X` be immersions of algebraic
> spaces over `S`.  The canonical sequence of `𝒪_Z`-modules
>
> `i^*𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0`
>
> of the conormal modules of Stacks 04CN, with the maps of Stacks 04CP
> (`AlgebraicGeometry.Space.conormalSequenceImmersionFirstMap` and
> `AlgebraicGeometry.Space.conormalSequenceImmersionSecondMap`), is exact: the two maps compose to
> zero, the resulting short complex is exact, and the second map is an epimorphism.
>
> It is isomorphic to the sequence `i^*c^*Ker(c^♯) ⟶ (i ≫ c)^*Ker((i ≫ c)^♯) ⟶ i^*Ker(i^♯) ⟶ 0` of
> the closed factorisation `c : Y ⟶ X ∖ ∂Y` of `j`, which is exact by
> `AlgebraicGeometry.Space.kernelConormalSequenceShortComplex_exact`.

```lean
theorem conormalSequenceImmersion_exact :
    ∃ h : conormalSequenceImmersionFirstMap B S hS hX hY hZ i j hi hj ≫
        conormalSequenceImmersionSecondMap B S hS hX hY hZ i j hi hj = 0,
      (ShortComplex.mk _ _ h).Exact ∧
        Epi (conormalSequenceImmersionSecondMap B S hS hX hY hZ i j hi hj)
```

**`AlgebraicGeometry.Space.conormalMap_comp_conormalMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealSheafMapVanishing.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IdealSheafMapVanishing.lean#L214). The attribute's comment: “the vanishing of the composite of the two maps of the sequence”.

> **The vanishing of the composite in Stacks 06BD.**  Let `Y` and `Z` be closed subspaces of
> an algebraic space `X` with `Z ⊆ Y`, let `j : Y ⟶ X` be the inclusion and let `p : j⁻¹(Z) ⟶ Z`
> be the projection.  The two arrows of the conormal sequence of the pair,
>
> `p^*(i^*𝒞_{Y/X}) ⟶ p^*𝒞_{Z/X} ⟶ 𝒞_{j⁻¹(Z)/Y}`,
>
> compose to zero.  The first is the inverse image along `p` of the map of [Stacks Project,
> Tag 04CP] at the square of `AlgebraicGeometry.Space.subspaceInclusion_homOfLe_square`, the
> second is the map of [Stacks Project, Tag 04CP] at the inverse-image square, whose surjectivity
> is `AlgebraicGeometry.Space.epi_conormalMap_closedSubspaces`.
>
> By the composition law of part (3) of [Stacks Project, Tag 04G2],
> `AlgebraicGeometry.Space.conormalMap_comp`, the composite is the map of [Stacks Project,
> Tag 04CP] attached to the outer rectangle, read through the composition comparison of
> [Stacks Project, Tag 03LU], which is an isomorphism.  The lower edge of that rectangle is
> `j ≫ 𝟙 X = j`, which factors through `Y` by the identity of `Y`, so the map of the outer
> rectangle vanishes by
> `AlgebraicGeometry.Space.conormalMap_eq_zero_of_factorization`.

```lean
theorem conormalMap_comp_conormalMap_eq_zero {X : AlgebraicSpaces B S hS}
    (Y Z : ClosedSubspaces B S hS X.1) (hZY : Z.1 ≤ Y.1) :
    (modulePullback B S hS
          (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)).map
        (conormalMap B S hS Z Y (𝟙 X)
          (ObjectProperty.homMk (Subfunctor.homOfLe hZY))
          (subspaceInclusion_homOfLe_square B S hS Y Z hZY)) ≫
      conormalMap B S hS (preimageSubspace B S hS (subspaceInclusion B S hS X Y) Z) Z
        (subspaceInclusion B S hS X Y)
        (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)
        (conormalEtaleRestrictionSquare B S hS (subspaceInclusion B S hS X Y) Z) = 0
```

**`AlgebraicGeometry.Space.exact_conormalShortComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealSheafSequenceExact.lean, line 676](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IdealSheafSequenceExact.lean#L676). The attribute's comment: “exactness at the middle term”. References: SGA 6 VIII (2.2), “partial”.

> **Exactness in the middle of [Stacks Project, Tag 06BD].**  Let `Y` and `Z` be closed
> subspaces of an algebraic space `X` with `Z ⊆ Y`, let `j : Y ⟶ X` be the inclusion and let
> `p : j⁻¹(Z) ⟶ Z` be the projection.  The conormal sequence of the pair,
>
> `p^*(i^*𝒞_{Y/X}) ⟶ p^*𝒞_{Z/X} ⟶ 𝒞_{j⁻¹(Z)/Y}`,
>
> is exact in the middle.
>
> The sequence is the inverse image along `j`, and then along the inclusion of `j⁻¹(Z)`, of the
> sequence of defining ideal sheaves `(𝟙 X)^*𝓘_Y ⟶ 𝓘_Z ⟶ j_*𝓘_{j⁻¹(Z)}`, which is exact in the
> middle and whose second map is an epimorphism, so exactness in the middle survives both inverse
> images (`AlgebraicGeometry.Space.exact_map_idealSheafSequence`, written out as
> `AlgebraicGeometry.Space.exact_mk_map_idealSheafSequence`).  The identification of the two
> sequences is the pair of squares
> `AlgebraicGeometry.Space.conormalSequence_comparison_square₁₂` and
> `AlgebraicGeometry.Space.conormalSequence_comparison_square₂₃`, whose vertical maps are
> isomorphisms — the inverse image along `p` of
> `AlgebraicGeometry.Space.conormalPullbackComparison` followed by a component of
> `AlgebraicGeometry.Space.conormalPullbackCompIso`, that component at the defining ideal sheaf of
> `Z`, and the identity — and the transport along them is
> `CategoryTheory.Limits.exact_mk_of_squares`.
>
> The companion clauses of the tag are
> `AlgebraicGeometry.Space.conormalMap_comp_conormalMap_eq_zero`, which says that the two arrows
> compose to zero, and `AlgebraicGeometry.Space.epi_conormalMap_closedSubspaces`, which says the
> second is an epimorphism; with this clause the tag carries all three.
>
> The source and target of the inverse-image functor along `p` are supplied explicitly, as the
> projections of the two subspaces, and the vanishing is taken from
> `AlgebraicGeometry.Space.conormalMap_comp_conormalMap_eq_zero_chain` rather than from the
> clause-one instance; the implementation notes record why.

```lean
theorem exact_conormalShortComplex :
    (ShortComplex.mk
      ((@modulePullback B S hS
          (⟨(preimageSubspace B S hS (subspaceInclusion B S hS X Y) Z).1.toFunctor,
              (preimageSubspace B S hS (subspaceInclusion B S hS X Y) Z).2.1⟩ :
            AlgebraicSpaces B S hS)
          (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS)
          (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)).map
        (conormalMap B S hS Z Y (𝟙 X) (ObjectProperty.homMk (Subfunctor.homOfLe hZY))
          (subspaceInclusion_homOfLe_square B S hS Y Z hZY)))
      (conormalMap B S hS (preimageSubspace B S hS (subspaceInclusion B S hS X Y) Z) Z
        (subspaceInclusion B S hS X Y)
        (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)
        (conormalEtaleRestrictionSquare B S hS (subspaceInclusion B S hS X Y) Z))
      (conormalMap_comp_conormalMap_eq_zero_chain B S hS Y Z hZY
        (preimageSubspace B S hS (subspaceInclusion B S hS X Y) Z)
        (preimageProjection B S hS (subspaceInclusion B S hS X Y) Z)
        (conormalEtaleRestrictionSquare B S hS (subspaceInclusion B S hS X Y) Z))).Exact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.5, Tag 04CM](https://stacks.math.columbia.edu/tag/04CM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
