---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.BasisGluingData.exists_isPullback_res_comp, AlgebraicGeometry.Scheme.BasisGluingData.existsUnique_isoOver, Stacks.AlgebraicGeometry.RelativeSheafGluing.RelativeSheafGluingData.exists_glued_and_existsUnique_pairIso, Stacks.AlgebraicGeometry.RelativeSheafGluing.existsUnique_glueHom_and_pullbackHom, Stacks.AlgebraicGeometry.RelativeSheafGluing.existsUnique_glueHom_and_pullbackHom_basis
statement: formalized
proof: formalized
---

# 27.2 Relative glueing

Section 27.2 of the Stacks Project, [Tag 01LG](https://stacks.math.columbia.edu/tag/01LG). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01LH, a lemma

[Tag 01LH](https://stacks.math.columbia.edu/tag/01LH) in the Stacks Project.

**`AlgebraicGeometry.Scheme.BasisGluingData.exists_isPullback_res_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean#L359). The attribute's comment: “existence of the glued scheme, with the charts identifying each piece with the part of it lying over the corresponding member of the basis”.

> Let `S` be a scheme and `B` a basis for its topology. Given a scheme `D.obj U` over `U` for
> every `U ∈ B`, together with morphisms `D.res : D.obj V ⟶ D.obj U` for `V ⊆ U` in `B`
> identifying `D.obj V` with the part of `D.obj U` over `V` and satisfying the cocycle condition,
> there is a morphism of schemes `f : X ⟶ S` and charts `i U : D.obj U ⟶ X` identifying `D.obj U`
> with the part of `X` over `U`, compatibly with the restriction morphisms.

```lean
theorem exists_isPullback_res_comp (hB : Opens.IsBasis B) (D : BasisGluingData S B) :
    ∃ (X : Scheme.{u}) (f : X ⟶ S) (i : ∀ U : B, D.obj U ⟶ X),
      (∀ U : B, IsPullback (D.proj U) (i U) U.1.ι f) ∧
        ∀ {V U : B} (h : V.1 ≤ U.1), D.res h ≫ i U = i V
```

**`AlgebraicGeometry.Scheme.BasisGluingData.existsUnique_isoOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean#L370). The attribute's comment: “the glued scheme is unique up to unique isomorphism over the base”.

> The glued scheme of a gluing datum over a basis of the topology of `S` is unique up to unique
> isomorphism over `S`: between any two solutions of the gluing problem there is exactly one
> isomorphism compatible with the charts, and it is a morphism over `S`.

```lean
theorem existsUnique_isoOver (hB : Opens.IsBasis B) (D : BasisGluingData S B)
    {X X' : Scheme.{u}} {f : X ⟶ S} {f' : X' ⟶ S}
    {i : ∀ U : B, D.obj U ⟶ X} {i' : ∀ U : B, D.obj U ⟶ X'}
    (hi : ∀ U : B, IsPullback (D.proj U) (i U) U.1.ι f)
    (hi' : ∀ U : B, IsPullback (D.proj U) (i' U) U.1.ι f')
    (hres : ∀ {V U : B} (h : V.1 ≤ U.1), D.res h ≫ i U = i V)
    (hres' : ∀ {V U : B} (h : V.1 ≤ U.1), D.res h ≫ i' U = i' V) :
    ∃! e : X ≅ X', (∀ U : B, i U ≫ e.hom = i' U) ∧ e.hom ≫ f' = f
```

## Tag 01LI, a lemma

[Tag 01LI](https://stacks.math.columbia.edu/tag/01LI) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeSheafGluing.RelativeSheafGluingData.exists_glued_and_existsUnique_pairIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingPairUniqueness.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingPairUniqueness.lean#L471). The attribute's comment: “both assertions of the tag as one statement: existence of the glued package — the morphism f, the charts i\_U, the quasi-coherent module F, the identifications θ\_U and their two compatibilities — and uniqueness of the pair (X, F) up to unique isomorphism over S”.

> **Stacks Project, Tag 01LI, both of its assertions as one statement.**  Let `𝒰` be a locally
> directed open cover of a scheme `S`, let `d` be a relative gluing datum over it, and let `D` be a
> compatible family of quasi-coherent modules on the schemes of `d`.  Then:
>
> * *existence of the whole package.*  There is a morphism of schemes `f : X ⟶ S`, morphisms
>   `i a : X a ⟶ X` exhibiting each `X a` as the part of `X` lying over the `a`-th member of the
>   cover and compatible with the transition morphisms of `d`, and a quasi-coherent module `F` on
>   `X` together with isomorphisms `θ a : F a ≅ (i a)^* F` under which the prescribed transition
>   isomorphisms of the `F a` are the ones induced by `F`.
> * *uniqueness.*  The pair `(X, F)` is unique up to unique isomorphism over `S`: any two glued
>   pairs are related by exactly one isomorphism of pairs.
>
> The two conjuncts are
> `Stacks.AlgebraicGeometry.RelativeSheafGluing.RelativeSheafGluingData.exists_isPullback_localIso`
> and
> `Stacks.AlgebraicGeometry.RelativeSheafGluing.RelativeSheafGluingData.existsUnique_pairIso`.

```lean
theorem exists_glued_and_existsUnique_pairIso :
    (∃ (X : Scheme.{u}) (f : X ⟶ S) (i : ∀ a, d.functor.obj a ⟶ X)
      (_ : ∀ a, IsPullback (d.natTrans.app a) (i a) (𝒰.f a) f)
      (hi : ∀ {a b : 𝒰.I₀} (hab : a ⟶ b), d.functor.map hab ≫ i b = i a)
      (F : X.Modules), F.IsQuasicoherent ∧
        ∃ θ : ∀ a, D.obj a ≅ (Scheme.Modules.pullback (i a)).obj F,
          ∀ {a b : 𝒰.I₀} (hab : a ⟶ b),
            (D.transitionIso hab).hom ≫ (θ a).hom =
              (Scheme.Modules.pullback (d.functor.map hab)).map (θ b).hom ≫
                (Scheme.Modules.pullbackComp (d.functor.map hab) (i b)).hom.app F ≫
                  (Scheme.Modules.pullbackCongr (hi hab)).hom.app F) ∧
      ∀ (H H' : Gluing d) (R : D.RealizationOn H) (R' : D.RealizationOn H'),
        ∃ p : D.PairIso R R', ∀ q : D.PairIso R R', q = p
```

## Tag 01LK, a remark

[Tag 01LK](https://stacks.math.columbia.edu/tag/01LK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeSheafGluing.existsUnique_glueHom_and_pullbackHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeSheafGluingMorphism.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/RelativeSheafGluingMorphism.lean#L659). The attribute's comment: “both functoriality assertions of the remark: the induced morphism of glued schemes over S restricting to the h\_U (and unique as such), and the unique induced morphism h^*G -> F restricting to the tau\_U, for arbitrary pairs obtained from the data of Tag 01LI”.

> **Stacks Project, Tag 01LK.** *Functoriality of relative gluing, for schemes and for
> quasi-coherent sheaves.* Let `𝒰` be a locally directed open cover of a scheme `S` (for instance the
> cover by the members of a basis of the topology of `S`, see
> `Stacks.AlgebraicGeometry.RelativeSheafGluing.existsUnique_glueHom_and_pullbackHom_basis`), and
> let `(dX, DX)` and `(dY, DY)` be two data as in Tag 01LI: relative gluing data `Xᵢ ⟶ 𝒰ᵢ`,
> `Yᵢ ⟶ 𝒰ᵢ` with restriction morphisms `ρ`, `σ`, carrying compatible families of quasi-coherent
> modules `ℱᵢ`, `𝒢ᵢ` with transition isomorphisms `θ`, `η`. Let `(G, R)` be a pair
> `(f : X ⟶ S, ℱ)` obtained from the first datum and `(G', R')` a pair `(g : Y ⟶ S, 𝒢)` obtained
> from the second. Suppose given morphisms `hᵢ : Xᵢ ⟶ Yᵢ` over `𝒰ᵢ` compatible with the
> restrictions (the natural transformation `hom` with `hover`), and morphisms
> `τᵢ : hᵢ⁎𝒢ᵢ ⟶ ℱᵢ` compatible with `θ` and `η`. Then:
>
> * the morphism of schemes `h = glueHom hom G G' : X ⟶ Y` restricts back to the `hᵢ` on the
>   charts, is a morphism over `S`, and is the only morphism restricting back to the `hᵢ`;
> * there is exactly one morphism `h⁎𝒢 ⟶ ℱ` restricting back to the `τᵢ` on the charts, read
>   through the canonical identifications.

```lean
theorem existsUnique_glueHom_and_pullbackHom (hover : hom ≫ dY.natTrans = dX.natTrans)
    (R : DX.RealizationOn G) (R' : DY.RealizationOn G')
    (τ : ∀ i, (Scheme.Modules.pullback (hom.app i)).obj (DY.obj i) ⟶ DX.obj i)
    (hτ : IsTransitionCompatible hom DX DY τ) :
    (∀ i, G.chart i ≫ glueHom hom G G' = hom.app i ≫ G'.chart i) ∧
      glueHom hom G G' ≫ G'.toBase = G.toBase ∧
      (∀ k : G.pt ⟶ G'.pt, (∀ i, G.chart i ≫ k = hom.app i ≫ G'.chart i) →
        k = glueHom hom G G') ∧
      ∃! ψ : (Scheme.Modules.pullback (glueHom hom G G')).obj R'.sheaf ⟶ R.sheaf, ∀ i,
        (Scheme.Modules.pullback (G.chart i)).map ψ = pullbackChartHomOn hom R R' τ i
```

**`Stacks.AlgebraicGeometry.RelativeSheafGluing.existsUnique_glueHom_and_pullbackHom_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeSheafGluingMorphism.lean, line 718](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/RelativeSheafGluingMorphism.lean#L718). The attribute's comment: “both functoriality assertions of the remark, for data indexed by a basis of the topology as in Tags 01LH and 01LI”.

> **Stacks Project, Tag 01LK, over a basis of the topology.** Let `S` be a scheme and `B` a
> basis for its topology. Let `D`, `D'` be gluing data over `B` as in Tag 01LH (local schemes
> `f_U : X_U ⟶ U`, `g_U : Y_U ⟶ U` with restriction morphisms `ρ^U_V`, `σ^U_V`), and let `DX`, `DY`
> be compatible families of quasi-coherent modules `ℱ_U`, `𝒢_U` on them with transition
> isomorphisms `θ^U_V`, `η^U_V`, as in Tag 01LI. Let `(G, R)` be a pair `(f : X ⟶ S, ℱ)` obtained
> from the first datum and `(G', R')` a pair `(g : Y ⟶ S, 𝒢)` obtained from the second. Suppose
> given morphisms `h_U : X_U ⟶ Y_U` over `U` compatible with the restrictions `ρ^U_V` and
> `σ^U_V`, and morphisms `τ_U : h_U⁎𝒢_U ⟶ ℱ_U` compatible with the maps `θ^U_V` and `η^U_V`.
> Then the induced morphism of schemes `h : X ⟶ Y` restricts back to the `h_U`, is a morphism over
> `S` and is the only morphism restricting back to the `h_U`, and there is exactly one morphism
> `h⁎𝒢 ⟶ ℱ` restricting back to the `τ_U`.
>
> This is `Stacks.AlgebraicGeometry.RelativeSheafGluing.existsUnique_glueHom_and_pullbackHom` for
> the cover of `S` by the members of `B`.

```lean
theorem existsUnique_glueHom_and_pullbackHom_basis (hB : Opens.IsBasis B)
    {D D' : Scheme.BasisGluingData S B} {DX : RelativeSheafGluingData (D.relativeGluingData hB)}
    {DY : RelativeSheafGluingData (D'.relativeGluingData hB)}
    (G : Gluing (D.relativeGluingData hB)) (G' : Gluing (D'.relativeGluingData hB))
    (R : DX.RealizationOn G) (R' : DY.RealizationOn G')
    (h : ∀ U : B, D.obj U ⟶ D'.obj U) (hover : ∀ U : B, h U ≫ D'.proj U = D.proj U)
    (hcompat : ∀ {V U : B} (hVU : V.1 ≤ U.1), D.res hVU ≫ h U = h V ≫ D'.res hVU)
    (τ : ∀ U, (Scheme.Modules.pullback ((basisNatTrans hB D D' h hcompat).app U)).obj
      (DY.obj U) ⟶ DX.obj U)
    (hτ : IsTransitionCompatible (dX := D.relativeGluingData hB) (dY := D'.relativeGluingData hB)
      (basisNatTrans hB D D' h hcompat) DX DY τ) :
    (∀ U, G.chart U ≫ glueHom (basisNatTrans hB D D' h hcompat) G G' =
        (basisNatTrans hB D D' h hcompat).app U ≫ G'.chart U) ∧
      glueHom (basisNatTrans hB D D' h hcompat) G G' ≫ G'.toBase = G.toBase ∧
      (∀ k : G.pt ⟶ G'.pt,
        (∀ U, G.chart U ≫ k = (basisNatTrans hB D D' h hcompat).app U ≫ G'.chart U) →
          k = glueHom (basisNatTrans hB D D' h hcompat) G G') ∧
      ∃! ψ : (Scheme.Modules.pullback
          (glueHom (basisNatTrans hB D D' h hcompat) G G')).obj R'.sheaf ⟶ R.sheaf, ∀ U,
        (Scheme.Modules.pullback (G.chart U)).map ψ =
          pullbackChartHomOn (dX := D.relativeGluingData hB) (dY := D'.relativeGluingData hB)
            (basisNatTrans hB D D' h hcompat) R R' τ U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.2, Tag 01LG](https://stacks.math.columbia.edu/tag/01LG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
