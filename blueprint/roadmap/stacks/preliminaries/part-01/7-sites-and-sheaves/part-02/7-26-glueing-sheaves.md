---
declaration: section
origin: cited
lean: Stacks.SheafMapGluing.maps_of_sheaves_glue, CategoryTheory.SheafHomAdj.prodHomEquivSheafHom, CategoryTheory.SheafHomAdj.prodHomEquivSheafHom_natural, CategoryTheory.OverShriek.sheafHomYonedaSheafifyNatIso, CategoryTheory.GrothendieckTopology.essSurj_toDescentData_pseudofunctorOver, CategoryTheory.GrothendieckTopology.isEquivalence_toDescentData_pseudofunctorOver, CategoryTheory.SiteGlueing.canonicalEquivalence
statement: formalized
proof: formalized
---

# 7.26 Glueing sheaves

Section 7.26 of the Stacks Project, [Tag 04TP](https://stacks.math.columbia.edu/tag/04TP). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04TQ, a lemma

[Tag 04TQ](https://stacks.math.columbia.edu/tag/04TQ) in the Stacks Project.

**`Stacks.SheafMapGluing.maps_of_sheaves_glue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Glueing/MapsOfSheavesGlue.lean, line 513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Glueing/MapsOfSheavesGlue.lean#L513).

> **Stacks 04TQ — Maps of sheaves glue (existence and uniqueness).**
>
> Let `(C, J)` be a site with fiber products, `A` the target category of sheaf values,
> `F, G : Sheaf J A`, and let `{ f i : U i → U }` be a covering of `U` in `J`.  Then any
> family of maps of restricted sheaves `φ i : F|_{C/U i} ⟶ G|_{C/U i}` that is compatible
> on the overlaps `C/(U i ×_U U j)` glues to a unique map `φ : F|_{C/U} ⟶ G|_{C/U}` whose
> restriction to each `C/U i` is `φ i`.

```lean
theorem maps_of_sheaves_glue
    (hcov : Sieve.generate (Presieve.ofArrows Ui f) ∈ J U)
    (φ : ∀ i, RestrictedHom J F G (Ui i))
    (hφ : CompatibleOnOverlaps J F G U Ui f φ) :
    ∃! ψ : RestrictedHom J F G U, ∀ i, restrictHomAlong J (f i) F G ψ = φ i
```

## Tag 0BWQ, a lemma

[Tag 0BWQ](https://stacks.math.columbia.edu/tag/0BWQ) in the Stacks Project.

**`CategoryTheory.SheafHomAdj.prodHomEquivSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Glueing/SheafHomProdEquiv.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Glueing/SheafHomProdEquiv.lean#L69).

> **Stacks 0BWQ, the bijection.** For sheaves of sets `F`, `G`, `H` on a site, maps
> `F × G ⟶ H` are in canonical bijection with maps `F ⟶ SheafHom(G, H)`, where `SheafHom(G, H)` is
> Mathlib's `sheafHom G H`, the sheaf `U ↦ Mor_{Sh(C/U)}(G|_{C/U}, H|_{C/U})`. It is the
> hom-equivalence of the adjunction `- × G ⊣ SheafHom(G, -)`; the inverse is the source's formula
> `(s, t) ↦ ψ(s)(t)` (`prodHomEquivSheafHom_symm_hom_app`), and the bijection is natural in all
> three entries (`prodHomEquivSheafHom_natural`).

```lean
def prodHomEquivSheafHom (F G H : Sheaf J (Type u)) :
    (F ⨯ G ⟶ H) ≃ (F ⟶ sheafHom G H)
```

**`CategoryTheory.SheafHomAdj.prodHomEquivSheafHom_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Glueing/SheafHomProdEquiv.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Glueing/SheafHomProdEquiv.lean#L132).

> **Stacks 0BWQ, functoriality.** The bijection `prodHomEquivSheafHom` is functorial in all
> three entries: in `F` (precomposition with `f × G`), in `G` (precomposition with `F × g` on the
> left, `SheafHom(g, H)` on the right) and in `H` (postcomposition, `SheafHom(G, h)` on the
> right).

```lean
theorem prodHomEquivSheafHom_natural :
    (∀ {F' F G H : Sheaf J (Type u)} (f : F' ⟶ F) (φ : F ⨯ G ⟶ H),
      prodHomEquivSheafHom F' G H (prod.map f (𝟙 G) ≫ φ) = f ≫ prodHomEquivSheafHom F G H φ) ∧
    (∀ {F G' G H : Sheaf J (Type u)} (g : G' ⟶ G) (φ : F ⨯ G ⟶ H),
      prodHomEquivSheafHom F G' H (prod.map (𝟙 F) g ≫ φ)
        = prodHomEquivSheafHom F G H φ ≫ sheafHomPrecomp g H) ∧
    (∀ {F G H H' : Sheaf J (Type u)} (h : H ⟶ H') (φ : F ⨯ G ⟶ H),
      prodHomEquivSheafHom F G H' (φ ≫ h) = prodHomEquivSheafHom F G H φ ≫ sheafHomMap G h)
```

## Tag 0D7X, a lemma

[Tag 0D7X](https://stacks.math.columbia.edu/tag/0D7X) in the Stacks Project.

**`CategoryTheory.OverShriek.sheafHomYonedaSheafifyNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Glueing/HomSheafLocalization.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Glueing/HomSheafLocalization.lean#L66).

> **Stacks 0D7X.** For an object `U` of a small site `(C, J)`, the internal hom sheaf
> `SheafHom(h_U^\#, -)` out of the sheafification of the representable presheaf `h_U` is the
> composite `j_{U*} \circ j_U^{-1}`: that is,
> `SheafHom(h_U^\#, \mathcal{F}) = j_{U*}(\mathcal{F}|_{\mathcal{C}/U})`, naturally in the sheaf
> `\mathcal{F}`.
>
> Both functors are right adjoint to `\mathcal{G} \mapsto h_U^\# \times \mathcal{G}`, the first by
> Stacks 0BWQ and the second by the localization adjunctions together with Stacks 03EE, so they agree
> by uniqueness of right adjoints. This is the source's argument, whose last step is the Yoneda
> lemma.

```lean
noncomputable def sheafHomYonedaSheafifyNatIso :
    SheafHomAdj.sheafHomFunctor ((presheafToSheaf J (Type u)).obj (yoneda.obj U)) ≅
      localizationPullback U J ⋙ localizationPushforward U J
```

## Tag 04TR, a lemma

[Tag 04TR](https://stacks.math.columbia.edu/tag/04TR) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.essSurj_toDescentData_pseudofunctorOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Glueing/GlueingSheaves.lean, line 839](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Glueing/GlueingSheaves.lean#L839).

> **Glueing sheaves.** Let `(C, J)` be a site, let `{f i : X i ⟶ S}` be a covering of an object
> `S` of `C`, and let `A` be a category with limits of the relevant size. Then every glueing datum
> for `A`-valued sheaves with respect to `{f i : X i ⟶ S}` — a sheaf `F i` on each slice site
> `C/X i` together with isomorphisms between the restrictions of `F i` and of `F j` over the
> overlaps, satisfying the cocycle condition over the triple overlaps — is isomorphic to the
> canonical glueing datum of a sheaf `F` on the slice site `C/S`, i.e. there exists such an `F`
> together with isomorphisms `F|_{C/X i} ≅ F i` compatible with the given ones over the overlaps.

```lean
public theorem essSurj_toDescentData_pseudofunctorOver {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) (A : Type u') [Category.{v'} A]
    [HasLimitsOfSize.{max t u v, max t u v} A] {ι : Type t} {S : C} {X : ι → C} (f : ∀ i, X i ⟶ S)
    (hf : Sieve.ofArrows X f ∈ J S) : ((J.pseudofunctorOver A).toDescentData f).EssSurj
```

## Tag 04TS, a lemma

[Tag 04TS](https://stacks.math.columbia.edu/tag/04TS) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.isEquivalence_toDescentData_pseudofunctorOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Glueing/GlueingSheaves.lean, line 1041](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Glueing/GlueingSheaves.lean#L1041).

> **Sheaves on a slice site are glueing data.** Let `(C, J)` be a site, let `{f i : X i ⟶ S}` be
> a covering of an object `S` of `C`, and let `A` be a category with limits of the relevant size.
> Then the category of `A`-valued sheaves on the slice site `C/S` is equivalent to the category of
> glueing data for `A`-valued sheaves with respect to `{f i : X i ⟶ S}` — a sheaf `F i` on each
> slice site `C/X i` together with isomorphisms between the restrictions of `F i` and of `F j` over
> the overlaps, satisfying the cocycle condition over the triple overlaps — via the functor sending
> a sheaf `F` on `C/S` to its canonical glueing datum `(F|_{C/X i})`.

```lean
public theorem isEquivalence_toDescentData_pseudofunctorOver {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) (A : Type u') [Category.{v'} A]
    [HasLimitsOfSize.{max u v, max u v} A] {ι : Type t} {S : C} {X : ι → C} (f : ∀ i, X i ⟶ S)
    (hf : Sieve.ofArrows X f ∈ J S) : ((J.pseudofunctorOver A).toDescentData f).IsEquivalence
```

## Tag 0GWK, a lemma

[Tag 0GWK](https://stacks.math.columbia.edu/tag/0GWK) in the Stacks Project.

**`CategoryTheory.SiteGlueing.canonicalEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Glueing/AbsoluteGlueingAnySite.lean, line 620](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Glueing/AbsoluteGlueingAnySite.lean#L620).

> **Stacks 0GWK.** For a site `C`, with no smallness hypothesis and with sheaves of sets
> valued in an arbitrary universe, the category of sheaves on `C` is equivalent to the category of
> absolute glueing data, via the functor sending a sheaf to its canonical absolute glueing data.

```lean
noncomputable def canonicalEquivalence : Sheaf J (Type w) ≌ GlueingData.{w} J
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.26, Tag 04TP](https://stacks.math.columbia.edu/tag/04TP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
