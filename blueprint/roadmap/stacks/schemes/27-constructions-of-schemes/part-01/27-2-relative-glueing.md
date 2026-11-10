---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.BasisGluingData.exists_isPullback_res_comp, AlgebraicGeometry.Scheme.BasisGluingData.existsUnique_isoOver, Stacks.AlgebraicGeometry.RelativeSheafGluing.RelativeSheafGluingData.exists_glued_and_existsUnique_pairIso, AlgebraicGeometry.CompatibleRelativeGluingData.colimMap_localHom_toBase, AlgebraicGeometry.Scheme.BasisGluingData.existsUnique_hom_of_compatible, Stacks.AlgebraicGeometry.RelativeSheafGluing.exists_pullbackHom_of_transitionCompatible, CategoryTheory.Limits.colimMap, CategoryTheory.Limits.ι_colimMap
statement: formalized
proof: formalized
---

# 27.2 Relative glueing

Section 27.2 of the Stacks Project, [Tag 01LG](https://stacks.math.columbia.edu/tag/01LG). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01LH, a lemma

[Tag 01LH](https://stacks.math.columbia.edu/tag/01LH) in the Stacks Project.

**`AlgebraicGeometry.Scheme.BasisGluingData.exists_isPullback_res_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean#L359). The attribute's comment: “existence of the glued scheme, with the charts identifying each piece with the part of it lying over the corresponding member of the basis”.

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

**`AlgebraicGeometry.Scheme.BasisGluingData.existsUnique_isoOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/RelativeGluingOverBasis.lean#L370). The attribute's comment: “the glued scheme is unique up to unique isomorphism over the base”.

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

**`Stacks.AlgebraicGeometry.RelativeSheafGluing.RelativeSheafGluingData.exists_glued_and_existsUnique_pairIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingPairUniqueness.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingPairUniqueness.lean#L471). The attribute's comment: “both assertions of the tag as one statement: existence of the glued package — the morphism f, the charts i_U, the quasi-coherent module F, the identifications θ_U and their two compatibilities — and uniqueness of the pair (X, F) up to unique isomorphism over S”.

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

**`AlgebraicGeometry.CompatibleRelativeGluingData.colimMap_localHom_toBase`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean#L114). The attribute's comment: “scheme_morphism”.

> The morphism induced on the glued schemes is a morphism over the common base.

```lean
public lemma colimMap_localHom_toBase :
    colimMap D.localHom ≫ D.target.toBase = D.source.toBase
```

**`AlgebraicGeometry.Scheme.BasisGluingData.existsUnique_hom_of_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean#L141). The attribute's comment: “scheme_morphism, for the gluing data over a basis of Tag 01LH”.

> **Stacks Project, Tag 01LK: functoriality for the data of Lemma 01LH.** Let `S` be a scheme
> and `B` a basis for its topology, and let `D` and `D'` be gluing data over `B` as in Tag 01LH,
> with local schemes `D.obj U ⟶ U` and `D'.obj U ⟶ U` and restriction morphisms `D.res` and
> `D'.res`. Let `f : X ⟶ S` be a scheme glued from `D`, with charts `i U`, and `g : Y ⟶ S` one
> glued from `D'`, with charts `j U`. A family of morphisms `h U : D.obj U ⟶ D'.obj U` over `U`
> compatible with the restriction morphisms gives rise to a morphism `k : X ⟶ Y` over `S` which
> restricts back to the `h U`, and `k` is the only such morphism.

```lean
public theorem existsUnique_hom_of_compatible (hB : Opens.IsBasis B) (D D' : BasisGluingData S B)
    {X Y : Scheme.{u}} {f : X ⟶ S} {g : Y ⟶ S}
    {i : ∀ U : B, D.obj U ⟶ X} {j : ∀ U : B, D'.obj U ⟶ Y}
    (hi : ∀ U : B, IsPullback (D.proj U) (i U) U.1.ι f)
    (hj : ∀ U : B, IsPullback (D'.proj U) (j U) U.1.ι g)
    (hires : ∀ {V U : B} (h : V.1 ≤ U.1), D.res h ≫ i U = i V)
    (hjres : ∀ {V U : B} (h : V.1 ≤ U.1), D'.res h ≫ j U = j V)
    (h : ∀ U : B, D.obj U ⟶ D'.obj U)
    (hover : ∀ U : B, h U ≫ D'.proj U = D.proj U)
    (hcompat : ∀ {V U : B} (hVU : V.1 ≤ U.1), D.res hVU ≫ h U = h V ≫ D'.res hVU) :
    ∃! k : X ⟶ Y, (∀ U : B, i U ≫ k = h U ≫ j U) ∧ k ≫ g = f
```

**`Stacks.AlgebraicGeometry.RelativeSheafGluing.exists_pullbackHom_of_transitionCompatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeSheafGluingMorphism.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeSheafGluingMorphism.lean#L347). The attribute's comment: “sheaf_morphism”.

> **Stacks Project, Tag 01LK.** *Functoriality of relative gluing for quasi-coherent sheaves.*
> Let `𝒰` be a locally directed open cover of a scheme `S` and let `dX`, `dY` be relative gluing
> data over it, carrying compatible families of quasi-coherent modules realized by `ℱ` on the glued
> scheme `X` and `𝒢` on the glued scheme `Y`. Given a family of morphisms `hᵢ : Xᵢ ⟶ Yᵢ` commuting
> with the restriction maps — hence the morphism `h = colimMap` of glued schemes — and morphisms
> `τᵢ : hᵢ⁎𝒢ᵢ ⟶ ℱᵢ` compatible with the transition isomorphisms of the two families, there is a
> morphism `h⁎𝒢 ⟶ ℱ` whose inverse image on the `i`-th chart is `τᵢ`, read through the canonical
> identifications.
>
> The companion half of the remark — that `h` is a morphism over `S` restricting to the given `hᵢ`
> — is `CategoryTheory.Limits.ι_colimMap` together with
> `AlgebraicGeometry.CompatibleRelativeGluingData.colimMap_localHom_toBase`.

```lean
theorem exists_pullbackHom_of_transitionCompatible (hom : dX.functor ⟶ dY.functor)
    (A : DX.Realization) (B : DY.Realization)
    (τ : ∀ i, (Scheme.Modules.pullback (hom.app i)).obj (DY.obj i) ⟶ DX.obj i)
    (hτ : IsTransitionCompatible hom DX DY τ) :
    ∃ ψ : (Scheme.Modules.pullback (colimMap hom)).obj B.sheaf ⟶ A.sheaf, ∀ i,
      (Scheme.Modules.pullback (colimit.ι dX.functor i)).map ψ =
        pullbackChartHom hom A B τ i
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.colimMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.colimMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean#L98) (StacksFrontier): “scheme_morphism”.
- [`CategoryTheory.Limits.ι_colimMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.ι_colimMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/RelativeGluingMorphism.lean#L99) (StacksFrontier): “scheme_morphism”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.2, Tag 01LG](https://stacks.math.columbia.edu/tag/01LG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
