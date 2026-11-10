---
declaration: section
origin: cited
lean: Deformation.relativeInfinitesimalAutomorphisms, Deformation.infinitesimalAutomorphisms, Deformation.existsUnique_retraction, Deformation.existsUnique_pushforwardIso, Deformation.existsUnique_infinitesimalAutomorphismsEquiv, Deformation.existsUnique_infinitesimalAutomorphismAction, Deformation.subsingleton_aut_residueField, Deformation.infinitesimalAutomorphisms_eq_top
statement: formalized
proof: formalized
---

# 90.19 Infinitesimal automorphisms

Section 90.19 of the Stacks Project, [Tag 06JN](https://stacks.math.columbia.edu/tag/06JN). 13 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06JP, a definition

[Tag 06JP](https://stacks.math.columbia.edu/tag/06JP) in the Stacks Project.

**`Deformation.relativeInfinitesimalAutomorphisms`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Object.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Object.lean#L162).

> The group of infinitesimal automorphisms of `x'` relative to `x` along
> `f : x' ⟶ x`: the kernel of the canonical homomorphism between the two fibre
> automorphism groups.

```lean
public noncomputable def relativeInfinitesimalAutomorphisms
    (hp : IsCofiberedInGroupoids p) (g : A' ⟶ A) (f : x'.1 ⟶ x.1)
    (hf : p.IsHomLift g f) : Subgroup (Aut x')
```

## Tag 06JQ, a definition

[Tag 06JQ](https://stacks.math.columbia.edu/tag/06JQ) in the Stacks Project.

**`Deformation.infinitesimalAutomorphisms`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Object.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Object.lean#L273). The attribute's comment: “infinitesimal automorphism group”.

> The group of infinitesimal automorphisms at a point, for a chosen pushforward
> along the constant inclusion into the dual numbers.

```lean
public noncomputable abbrev infinitesimalAutomorphisms
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    {A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k}
    {x₀ : p.Fiber A₀} {xε : p.Fiber Aε}
    (hp : IsCofiberedInGroupoids p)
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i) : Subgroup (Aut xε)
```

**`Deformation.existsUnique_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Object.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Object.lean#L346). The attribute's comment: “unique map back”.

> A chosen pushforward along the constant inclusion into the dual numbers has a
> unique retraction, without a restriction on the image of that retraction in the base.

```lean
public theorem existsUnique_retraction
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    {A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k}
    {x₀ : p.Fiber A₀} {xε : p.Fiber Aε}
    (hp : IsCofiberedInGroupoids p)
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i) :
    ∃! r : xε.1 ⟶ x₀.1, i ≫ r = 𝟙 x₀.1
```

## Tag 06JR, a remark

[Tag 06JR](https://stacks.math.columbia.edu/tag/06JR) in the Stacks Project.

**`Deformation.existsUnique_pushforwardIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L26). The attribute's comment: “canonical isomorphism of pushforwards”.

> Pushforwards of isomorphic objects along the same arrow have a unique
> isomorphism commuting with their structure maps.

```lean
public theorem existsUnique_pushforwardIso
    {F : Type u₁} [Category.{v₁} F]
    {C : Type u₂} [Category.{v₂} C] {p : F ⥤ C}
    {A₀ A : C} {x₀ y₀ : p.Fiber A₀} {x y : p.Fiber A}
    (hp : IsCofiberedInGroupoids p)
    (g : A₀ ⟶ A) (h₀ : x₀ ≅ y₀)
    (i : x₀.1 ⟶ x.1) (hi : p.IsHomLift g i)
    (j : y₀.1 ⟶ y.1) (hj : p.IsHomLift g j) :
    ∃! h : x ≅ y, i ≫ h.hom.val = h₀.hom.val ≫ j
```

**`Deformation.existsUnique_infinitesimalAutomorphismsEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L172). The attribute's comment: “invariance under isomorphism of the original object”.

> An isomorphism of the original objects canonically identifies their
> infinitesimal automorphism groups, by conjugation through the unique
> comparison of their pushforwards.

```lean
public theorem existsUnique_infinitesimalAutomorphismsEquiv
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    {A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k}
    {x₀ y₀ : p.Fiber A₀} {xε yε : p.Fiber Aε}
    (hp : IsCofiberedInGroupoids p)
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀)
    (hpair : IsCanonicalDualNumberPair g e)
    (h₀ : x₀ ≅ y₀)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i)
    (j : y₀.1 ⟶ yε.1) (hj : p.IsHomLift g j) :
    ∃! φ : infinitesimalAutomorphisms hp g e hpair i hi ≃*
        infinitesimalAutomorphisms hp g e hpair j hj,
      ∃ h : xε ≅ yε,
        (i ≫ h.hom.val = h₀.hom.val ≫ j) ∧
        (∀ a, (φ a).1 = h.conjAut a.1)
```

**`Deformation.existsUnique_infinitesimalAutomorphismAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L207). The attribute's comment: “action of automorphisms of the original object”.

> The automorphism group of the original object acts on its infinitesimal
> automorphism group by conjugation through pushed-forward automorphisms.

```lean
public theorem existsUnique_infinitesimalAutomorphismAction
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    {A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k}
    {x₀ : p.Fiber A₀} {xε : p.Fiber Aε}
    (hp : IsCofiberedInGroupoids p)
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i) :
    ∃! ρ : Aut x₀ →* MulAut
        (infinitesimalAutomorphisms hp g e hpair i hi),
      ∀ (a : Aut x₀)
        (b : infinitesimalAutomorphisms hp g e hpair i hi),
        ((ρ a) b).1 =
          (pushforwardAutomorphism hp g i hi a).asIso.conjAut b.1
```

## Tag 06JS, a remark

[Tag 06JS](https://stacks.math.columbia.edu/tag/06JS) in the Stacks Project.

**`Deformation.subsingleton_aut_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L274). The attribute's comment: “automorphisms\_at\_a\_point”.

> The automorphism group of an object over the residue field in a predeformation
> category is trivial.

```lean
public theorem subsingleton_aut_residueField
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsPredeformationCategory p)
    (x₀ : p.Fiber (residueFieldObject Λ k)) :
    Subsingleton (Aut x₀)
```

**`Deformation.infinitesimalAutomorphisms_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L285). The attribute's comment: “automorphisms\_at\_a\_point”.

> Every automorphism of a pushforward to the dual numbers is infinitesimal.

```lean
public theorem infinitesimalAutomorphisms_eq_top
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsPredeformationCategory p)
    {Aε : ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (x₀ : p.Fiber (residueFieldObject Λ k)) (xε : p.Fiber Aε)
    (g : residueFieldObject Λ k ⟶ Aε)
    (e : Aε ⟶ residueFieldObject Λ k)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i) :
    infinitesimalAutomorphisms hp.cofibered g e hpair i hi = ⊤
```

**`Deformation.existsUnique_pointIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L312). The attribute's comment: “independence\_of\_point”.

> Any two points over the residue field in a predeformation category have exactly
> one isomorphism between them.

```lean
public theorem existsUnique_pointIso
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsPredeformationCategory p)
    (x₀ y₀ : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    ∃! _ : x₀ ≅ y₀, True
```

**`Deformation.existsUnique_infinitesimalAutomorphismsEquiv_of_isPredeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L328). The attribute's comment: “independence\_of\_point”.

> The unique isomorphism of points induces the canonical group isomorphism on
> infinitesimal automorphisms. Its action is conjugation by any compatible
> isomorphism between chosen pushforwards to the dual numbers.

```lean
public theorem existsUnique_infinitesimalAutomorphismsEquiv_of_isPredeformationCategory
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsPredeformationCategory p)
    {Aε : ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (g : residueFieldObject.{u, v, w} Λ k ⟶ Aε)
    (e : Aε ⟶ residueFieldObject.{u, v, w} Λ k)
    (hpair : IsCanonicalDualNumberPair g e)
    (x₀ y₀ : p.Fiber (residueFieldObject.{u, v, w} Λ k))
    (xε yε : p.Fiber Aε)
    (iₓ : x₀.1 ⟶ xε.1) (hiₓ : p.IsHomLift g iₓ)
    (iᵧ : y₀.1 ⟶ yε.1) (hiᵧ : p.IsHomLift g iᵧ) :
    ∃! φ : ↥(infinitesimalAutomorphisms hp.cofibered g e hpair iₓ hiₓ) ≃*
        ↥(infinitesimalAutomorphisms hp.cofibered g e hpair iᵧ hiᵧ),
      ∀ (f : x₀ ≅ y₀) (j : xε ≅ yε),
        (iₓ ≫ j.hom.val = f.hom.val ≫ iᵧ) →
          ∀ a, (φ a).val.asIso.hom.val = j.inv.val ≫ a.val.asIso.hom.val ≫ j.hom.val
```

**`Deformation.infinitesimalAutomorphismGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L425). The attribute's comment: “infinitesimal\_automorphisms\_of\_predeformation\_category”.

> The infinitesimal automorphism group of a predeformation category, formed using a
> chosen object over the residue field and its pushforward to the dual numbers.

```lean
public noncomputable abbrev infinitesimalAutomorphismGroup
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsPredeformationCategory p)
    {Aε : ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    {x₀ : p.Fiber (residueFieldObject Λ k)} {xε : p.Fiber Aε}
    (g : residueFieldObject Λ k ⟶ Aε)
    (e : Aε ⟶ residueFieldObject Λ k)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i) : Type _
```

**`Deformation.infinitesimalAutomorphismGroup_uniqueEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Independence.lean#L442). The attribute's comment: “infinitesimal\_automorphisms\_of\_predeformation\_category”.

> Changing the chosen object over the residue field, and its pushforward, gives a unique
> identification of infinitesimal automorphism groups. On automorphisms it is conjugation by
> the isomorphism between the pushforwards.

```lean
public theorem infinitesimalAutomorphismGroup_uniqueEquiv
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsPredeformationCategory p)
    {Aε : ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    {x₀ y₀ : p.Fiber (residueFieldObject Λ k)}
    {xε yε : p.Fiber Aε}
    (g : residueFieldObject Λ k ⟶ Aε)
    (e : Aε ⟶ residueFieldObject Λ k)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i)
    (j : y₀.1 ⟶ yε.1) (hj : p.IsHomLift g j) :
    ∃! E : infinitesimalAutomorphismGroup hp g e hpair i hi ≃*
        infinitesimalAutomorphismGroup hp g e hpair j hj,
      ∃ (f₀ : x₀ ≅ y₀) (fε : xε ≅ yε),
        f₀.hom.val ≫ j = i ≫ fε.hom.val ∧
        (∀ a, (E a).val = fε.conjAut a.val)
```

**`Deformation.infinitesimalAutomorphismGroup_objectsOverFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Localization.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Basic/Localization.lean#L225). The attribute's comment: “infinitesimal\_automorphisms\_of\_localization”.

> Infinitesimal automorphisms of objects over `x₀` are the infinitesimal
> automorphisms of `x₀`.

```lean
public theorem infinitesimalAutomorphismGroup_objectsOverFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (hp : IsPredeformationCategory p)
    {Aε : ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    {x₀ : p.Fiber (residueFieldObject Λ k)} {xε : p.Fiber Aε}
    (g : residueFieldObject Λ k ⟶ Aε)
    (e : Aε ⟶ residueFieldObject Λ k)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i)
    {y₀ : (objectsOverFunctor p x₀.1).Fiber
      (residueFieldObject Λ k)}
    {yε : (objectsOverFunctor p x₀.1).Fiber Aε}
    (j : y₀.1 ⟶ yε.1)
    (hj : (objectsOverFunctor p x₀.1).IsHomLift g j)
    (h₀ : y₀.1.left = x₀.1) (hε : yε.1.left = xε.1)
    (h₀hom : y₀.1.hom = eqToHom h₀)
    (hεhom : yε.1.hom = eqToHom hε ≫
      (canonicalRetraction hp.cofibered g e hpair.split i hi).1)
    (hjleft : j.left ≫ eqToHom hε = eqToHom h₀ ≫ i) :
    ∃! E :
      infinitesimalAutomorphismGroup
        (isPredeformationCategory_objectsOverFunctor p hp.cofibered x₀)
        g e hpair j hj ≃* infinitesimalAutomorphismGroup hp g e hpair i hi,
      ∀ a, (E a).val.asIso.hom.val =
        eqToHom hε.symm ≫ a.val.asIso.hom.val.left ≫ eqToHom hε
```

## Tag 06JT, a definition

[Tag 06JT](https://stacks.math.columbia.edu/tag/06JT) in the Stacks Project.

**`Deformation.automorphismFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Functor.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Functor.lean#L338).

> The automorphism functor of `x`: at `f : p.obj x ⟶ V` it is the type
> of automorphisms over `V` of the chosen pushforward `f_* x`.

```lean
public noncomputable def automorphismFunctor
    {F : Type u₁} [Category.{v₁} F] {C : Type u₂} [Category.{v₂} C]
    {p : F ⥤ C} {x : F} (P : ChosenPushforwardsAt p x) : Under (p.obj x) ⥤ Type v₁
```

## Tag 06JU, a lemma

[Tag 06JU](https://stacks.math.columbia.edu/tag/06JU) in the Stacks Project.

**`Deformation.automorphismFunctor_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/AutomorphismFunctorRS.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/LiftsOfObjects/AutomorphismFunctorRS.lean#L69).

> The automorphism functor of an object in a category cofibered in groupoids
> satisfying (RS) itself satisfies (RS).

```lean
public theorem automorphismFunctor_satisfiesRS
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : SatisfiesRS p) (x : F)
    (P : ChosenPushforwardsAt p x) :
    SatisfiesRSUnder (p.obj x) (automorphismFunctor P)
```

## Tag 06JV, a lemma

[Tag 06JV](https://stacks.math.columbia.edu/tag/06JV) in the Stacks Project.

**`Deformation.exists_naturalLocalizedAutomorphismTangentVectorSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentVectorSpace.lean, line 879](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentVectorSpace.lean#L879). The attribute's comment: “part (1)”. References: SGA 7 VI (2.6(c)), “Aut(1\_ε) k-structure”.

> **Stacks Project, Tag 06JV (1).** On the tangent space at the identity of the
> automorphism functor of `x`, addition is composition of automorphisms and scalar
> multiplication is induced by the canonical scaling of the dual-number coordinate; in
> particular composition there is commutative.

```lean
public theorem exists_naturalLocalizedAutomorphismTangentVectorSpace
    (hp : SatisfiesRS p) :
    ∃ V : AddCommGroup (localizedAutomorphismFunctorTangent P),
      letI := V
      ∃ M : Module k (localizedAutomorphismFunctorTangent P),
        letI := M
        (∀ a b, localizedTangentEquivKernel P (a + b) =
          localizedTangentEquivKernel P a * localizedTangentEquivKernel P b) ∧
        (∀ (c : k) a, (localizedTangentEquivKernel P (c • a)).1 =
          P.transportAutHom (tangentScaling c) (localizedTangentEquivKernel P a).1)
```

**`Deformation.existsUnique_localizedTangentAutomorphismLinearEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentVectorSpace.lean, line 1020](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentVectorSpace.lean#L1020). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 06JV (2).** Pushforward to the special fibre canonically
> identifies the tangent spaces at the identity of the two automorphism functors. The
> comparison is conjugation by the unique isomorphism of dual-number pushforwards lying over
> the identity of the dual-number ring.

```lean
public theorem existsUnique_localizedTangentAutomorphismLinearEquiv
    (_hbase : p.obj x₀ = residueFieldObject.{u, v, w} Λ k)
    (P : ChosenPushforwardsAt p x)
    (Q : ChosenPushforwardsAt p x₀) :
    letI := naturalLocalizedTangentAddCommGroup P hp
    letI := naturalLocalizedTangentModule P hp
    letI := naturalLocalizedTangentAddCommGroup Q hp
    letI := naturalLocalizedTangentModule Q hp
    let U₀ := specialFibreUnder (p := p) (x := x)
    let Uε := dualNumbersUnder (p := p) (x := x)
    let V₀ := specialFibreUnder (p := p) (x := x₀)
    let Vε := dualNumbersUnder (p := p) (x := x₀)
    ∃! E : localizedAutomorphismFunctorTangent P ≃ₗ[k]
        localizedAutomorphismFunctorTangent Q,
      ∃ (H₀ : (P.obj U₀).1 ≅ (Q.obj V₀).1)
          (Hε : (P.obj Uε).1 ≅ (Q.obj Vε).1),
        (P.inclusion U₀ ≫ H₀.hom = j ≫ Q.inclusion V₀) ∧
        (P.inclusion Uε ≫ Hε.hom = j ≫ Q.inclusion Vε) ∧
        (∀ t : Uε.right,
          (eqToHom (P.obj Uε).2.symm ≫ p.map Hε.hom ≫
            eqToHom (Q.obj Vε).2).hom t = t) ∧
        (∀ a, (localizedTangentEquivKernel P a).1.asIso.hom.val ≫ Hε.hom =
          Hε.hom ≫ (localizedTangentEquivKernel Q (E a)).1.asIso.hom.val)
```

## Tag 06JW, a remark

[Tag 06JW](https://stacks.math.columbia.edu/tag/06JW) in the Stacks Project.

**`Deformation.relativeInfinitesimalAutomorphismsEquivIdentityLifts`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean#L92). The attribute's comment: “relative identity lifts”.

> Relative infinitesimal automorphisms are precisely lifts of the identity
> automorphism along the given morphism.

```lean
public noncomputable def relativeInfinitesimalAutomorphismsEquivIdentityLifts
    {F : Type u₁} [Category.{v₁} F] {C : Type u} [Category.{v} C]
    {p : F ⥤ C} {A' A : C} {x' : p.Fiber A'} {x : p.Fiber A}
    (hp : IsCofiberedInGroupoids p)
    (g : A' ⟶ A) (f : x'.1 ⟶ x.1) (hf : p.IsHomLift g f) :
    relativeInfinitesimalAutomorphisms hp g f hf ≃
      identityAutomorphismLifts hp g f hf
```

**`Deformation.infinitesimalAutomorphismsEquivIdentityLifts`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean#L122). The attribute's comment: “dual-number identity lifts”.

> Infinitesimal automorphisms at a residue-field object are lifts of its
> identity automorphism to the dual numbers.

```lean
public noncomputable def infinitesimalAutomorphismsEquivIdentityLifts
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    {A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k}
    {x₀ : p.Fiber A₀} {xε : p.Fiber Aε}
    (hp : IsCofiberedInGroupoids p)
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i) :
    let r := canonicalRetraction hp g e hpair.split i hi
    infinitesimalAutomorphisms hp g e hpair i hi ≃
      identityAutomorphismLifts hp e r.1 r.2.1
```

**`Deformation.infinitesimalAutomorphisms_eq_tangentFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean#L141). The attribute's comment: “tangent fibre at the identity”.

> At a point over the residue field, infinitesimal automorphisms are the
> fibre over the identity of the automorphism functor at the dual numbers.

```lean
public theorem infinitesimalAutomorphisms_eq_tangentFiber
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    {x : F} (hp : IsCofiberedInGroupoids p)
    (P : ChosenPushforwardsAt p x)
    {A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k}
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀)
    (hpair : IsCanonicalDualNumberPair g e)
    (hbase : p.obj x = A₀) :
    let U₀ : Under (p.obj x) := Under.mk (eqToHom hbase)
    let Uε : Under (p.obj x) := Under.mk (eqToHom hbase ≫ g)
    let j : U₀ ⟶ Uε := Under.homMk g (by simp [U₀, Uε])
    let r : Uε ⟶ U₀ := Under.homMk e (by simp [U₀, Uε, hpair.split])
    infinitesimalAutomorphisms hp g e hpair (P.map j)
      (P.map_isHomLift j) = MonoidHom.ker (P.transportAutHom r)
```

**`Deformation.infinitesimalAutomorphismsEquivTangentSpaceAtIdentity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/LiftsOfObjects/IdentityLifts.lean#L724). The attribute's comment: “tangent space at the identity”.

> Infinitesimal automorphisms at a residue-field object are the tangent
> space at the identity of its automorphism functor.

```lean
public noncomputable def infinitesimalAutomorphismsEquivTangentSpaceAtIdentity
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    {x : F}
    (hp : IsCofiberedInGroupoids p)
    (P : ChosenPushforwardsAt p x)
    (hbase : p.obj x = residueFieldObject.{u, v, w} Λ k)
    (Aε : ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (g : residueFieldObject.{u, v, w} Λ k ⟶ Aε)
    (e : Aε ⟶ residueFieldObject.{u, v, w} Λ k)
    (hpair : IsCanonicalDualNumberPair g e) :
    let U₀ : Under (p.obj x) := Under.mk (eqToHom hbase)
    let Uε : Under (p.obj x) := Under.mk (eqToHom hbase ≫ g)
    let j : U₀ ⟶ Uε := Under.homMk g (by simp [U₀, Uε])
    let baseChange := residueAlgebrasToUnder.{u, v, w} Λ k ⋙
      Under.map (eqToHom hbase)
    let AutFunctor := baseChange ⋙ automorphismFunctor P
    let q := CategoryOfElements.π AutFunctor
    let k₀ := residueFieldObject.{w, v, w} k k
    let identityPoint : q.Fiber k₀ :=
      ⟨AutFunctor.elementsMk k₀ (1 : Aut (P.obj (baseChange.obj k₀))), rfl⟩
    (infinitesimalAutomorphisms hp g e hpair (P.map j)
      (P.map_isHomLift j)) ≃
    tangentSpaceAtPoint q
        (automorphismFunctorCategory_isCofiberedInGroupoids P baseChange)
        identityPoint
```

## Tag 06JX, a lemma

[Tag 06JX](https://stacks.math.columbia.edu/tag/06JX) in the Stacks Project.

**`Deformation.exists_naturalLocalizedAutomorphismTangentVectorSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentVectorSpace.lean, line 879](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentVectorSpace.lean#L879). The attribute's comment: “Inf\_\{x\_0}(F) as the tangent space, with addition composition”. References: SGA 7 VI (2.6(c)), “Aut(1\_ε) k-structure”.

> **Stacks Project, Tag 06JV (1).** On the tangent space at the identity of the
> automorphism functor of `x`, addition is composition of automorphisms and scalar
> multiplication is induced by the canonical scaling of the dual-number coordinate; in
> particular composition there is commutative.

```lean
public theorem exists_naturalLocalizedAutomorphismTangentVectorSpace
    (hp : SatisfiesRS p) :
    ∃ V : AddCommGroup (localizedAutomorphismFunctorTangent P),
      letI := V
      ∃ M : Module k (localizedAutomorphismFunctorTangent P),
        letI := M
        (∀ a b, localizedTangentEquivKernel P (a + b) =
          localizedTangentEquivKernel P a * localizedTangentEquivKernel P b) ∧
        (∀ (c : k) a, (localizedTangentEquivKernel P (c • a)).1 =
          P.transportAutHom (tangentScaling c) (localizedTangentEquivKernel P a).1)
```

## Tag 07W6, a lemma

[Tag 07W6](https://stacks.math.columbia.edu/tag/07W6) in the Stacks Project.

**`Deformation.inducedInfinitesimalLinearMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Morphism.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Morphism.lean#L542). The attribute's comment: “the induced k-linear map, as a construction”.

> **Stacks Project, Tag 07W6.** A morphism of categories cofibered in groupoids over `𝒞_Λ`
> satisfying (RS) induces a `k`-linear map on infinitesimal automorphisms at a point.

```lean
public noncomputable def inducedInfinitesimalLinearMap (hp : SatisfiesRS (Φ ⋙ q))
    (hq : SatisfiesRS q) :
    letI := naturalLocalizedTangentAddCommGroup P hp
    letI := naturalLocalizedTangentModule P hp
    letI := naturalLocalizedTangentAddCommGroup Q hq
    letI := naturalLocalizedTangentModule Q hq
    localizedAutomorphismFunctorTangent P →ₗ[k] localizedAutomorphismFunctorTangent Q
```

**`Deformation.exists_inducedInfinitesimalLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Morphism.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Morphism.lean#L606). The attribute's comment: “the morphism presented as a functor commuting with the two projections, with the map pinned by the dual-number comparison”.

> **Stacks Project, Tag 07W6.** Presented with a morphism as a functor commuting with the
> two projections: it induces a `k`-linear map on infinitesimal automorphisms, pinned by the
> comparison of dual-number pushforwards.

```lean
public theorem exists_inducedInfinitesimalLinearMap
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k} (hw : Φ ⋙ q = p) (hp : SatisfiesRS p)
    (hq : SatisfiesRS q) (P : ChosenPushforwardsAt p x₀)
    (Q : ChosenPushforwardsAt q (Φ.obj x₀)) :
    letI := naturalLocalizedTangentAddCommGroup P hp
    letI := naturalLocalizedTangentModule P hp
    letI := naturalLocalizedTangentAddCommGroup Q hq
    letI := naturalLocalizedTangentModule Q hq
    ∃ T : localizedAutomorphismFunctorTangent P →ₗ[k] localizedAutomorphismFunctorTangent Q,
      ∃ H : (Q.obj (dualNumbersUnder (p := q) (x := Φ.obj x₀))).1 ⟶
          Φ.obj (P.obj (dualNumbersUnder (p := p) (x := x₀))).1,
        q.IsHomLift (𝟙 (dualNumbersUnder (p := q) (x := Φ.obj x₀)).right) H ∧
          Q.inclusion (dualNumbersUnder (p := q) (x := Φ.obj x₀)) ≫ H =
            Φ.map (P.inclusion (dualNumbersUnder (p := p) (x := x₀))) ∧
          ∀ a, (localizedTangentEquivKernel Q (T a)).1.asIso.hom.val ≫ H =
            H ≫ Φ.map (localizedTangentEquivKernel P a).1.asIso.hom.val
```

## Tag 06JY, a lemma

[Tag 06JY](https://stacks.math.columbia.edu/tag/06JY) in the Stacks Project.

**`Deformation.exists_localizedTangentEquiv_infinitesimalAutomorphismKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentTensorAction.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentTensorAction.lean#L76). The attribute's comment: “the two descriptions of the acting group”.

> **Stacks Project, Tag 06JY.** The two descriptions of the acting group agree: for a
> morphism `j : y ⟶ y₀` of a category cofibered in groupoids over `𝒞_Λ` satisfying (RS) whose
> target lies over the residue field, the `k`-vector space `T_{id_{y₀}} Aut(y)` is linearly
> isomorphic to `T_{id_{y₀}} Aut(y₀)`, and the latter is the group `Inf_{y₀}(𝓕)` of
> infinitesimal automorphisms of the dual-number pushforward of `y₀` by an equivalence taking
> addition to composition. Tensoring with the kernel therefore gives the same space either
> way.

```lean
public theorem exists_localizedTangentEquiv_infinitesimalAutomorphismKernel
    (hrs : SatisfiesRS p) {y y₀ : F} (j : y ⟶ y₀)
    (hbase : p.obj y₀ = residueFieldObject.{u, w, w} Λ k)
    (P : ChosenPushforwardsAt p y) (Q : ChosenPushforwardsAt p y₀) :
    letI := naturalLocalizedTangentAddCommGroup P hrs
    letI := naturalLocalizedTangentModule P hrs
    letI := naturalLocalizedTangentAddCommGroup Q hrs
    letI := naturalLocalizedTangentModule Q hrs
    ∃ (_ : localizedAutomorphismFunctorTangent P ≃ₗ[k]
        localizedAutomorphismFunctorTangent Q)
      (G : localizedAutomorphismFunctorTangent Q ≃
        infinitesimalAutomorphismKernel Q (tangentReduction (p := p) (x := y₀))),
      ∀ a b, G (a + b) = G a * G b
```

**`Deformation.exists_freeTransitiveAction_tangentTensor_relativeInfinitesimalAutomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentTensorSplit.lean, line 777](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/TangentTensorSplit.lean#L777). The attribute's comment: “the free and transitive action”.

> For a category cofibered in groupoids over `𝒞_Λ` satisfying (RS) and a morphism
> `φ : x' ⟶ x` lying over a surjection `g : A' → A` whose kernel `I` is annihilated by the maximal
> ideal of `A'`, the group `Inf(x'/x)` of infinitesimal automorphisms of `x'` over `x` carries a
> free and transitive action by `T_{id_{x₀}} Aut(x') ⊗_k I`.

```lean
public theorem exists_freeTransitiveAction_tangentTensor_relativeInfinitesimalAutomorphisms
    (hrs : SatisfiesRS p) {A' A : ArtinianLocalAlgCat.{u, w, w} Λ k}
    {x' : p.Fiber A'} {x : p.Fiber A}
    (g : A' ⟶ A) (φ : x'.1 ⟶ x.1) (hφ : p.IsHomLift g φ)
    (hg : Function.Surjective g.hom)
    (hann : ∀ a : A', a ∈ maximalIdeal A' →
      ∀ i : RingHom.ker g.hom.toRingHom, a * (i : A') = 0)
    {x₀ : p.Fiber (residueFieldObject.{u, w, w} Λ k)}
    (ψ₀ : x.1 ⟶ x₀.1) (hψ₀ : p.IsHomLift (residueMorphism A) ψ₀)
    (P : ChosenPushforwardsAt p x'.1) :
    letI : Module k (RingHom.ker g.hom.toRingHom) := kernelModule g hann
    letI := naturalLocalizedTangentAddCommGroup P hrs
    letI := naturalLocalizedTangentModule P hrs
    ∃ act : TensorProduct k (localizedAutomorphismFunctorTangent P)
          (RingHom.ker g.hom.toRingHom) →
        ↥(relativeInfinitesimalAutomorphisms hrs.1 g φ hφ) →
        ↥(relativeInfinitesimalAutomorphisms hrs.1 g φ hφ),
      (∀ s, act 0 s = s) ∧
      (∀ t u s, act (t + u) s = act t (act u s)) ∧
      (∀ s t, act t s = s → t = 0) ∧
      (∀ s s', ∃ t, act t s = s') ∧
      (∀ s, Function.Bijective fun t => act t s)
```

## Tag 06JZ, a lemma

[Tag 06JZ](https://stacks.math.columbia.edu/tag/06JZ) in the Stacks Project.

**`Deformation.relativeInfinitesimalAutomorphisms_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/Vanishing.lean, line 884](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/Vanishing.lean#L884).

> Let `𝓕` be a category cofibered in groupoids over `𝒞_Λ` satisfying (RS), let `x' ⟶ x` be a
> morphism of `𝓕` lying over a surjection, and let `x₀` be a pushforward of `x` to the special
> fibre. If the infinitesimal automorphisms of `x₀` vanish, then so do the infinitesimal
> automorphisms of `x'` over `x`.

```lean
theorem relativeInfinitesimalAutomorphisms_eq_bot
    (hrs : SatisfiesRS p)
    {B A A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k}
    {x' : p.Fiber B} {x : p.Fiber A} {x₀ : p.Fiber A₀} {xε : p.Fiber Aε}
    (g : B ⟶ A) (f : x'.1 ⟶ x.1) (hf : p.IsHomLift g f)
    (hg : Function.Surjective g.hom)
    (g₀ : A ⟶ A₀) (f₀ : x.1 ⟶ x₀.1) (hf₀ : p.IsHomLift g₀ f₀)
    (i : A₀ ⟶ Aε) (e : Aε ⟶ A₀)
    (hpair : IsCanonicalDualNumberPair i e)
    (fi : x₀.1 ⟶ xε.1) (hfi : p.IsHomLift i fi)
    (htriv : infinitesimalAutomorphisms hrs.1 i e hpair fi hfi = ⊥) :
    relativeInfinitesimalAutomorphisms hrs.1 g f hf = ⊥
```

## Tag 06K0, a lemma

[Tag 06K0](https://stacks.math.columbia.edu/tag/06K0) in the Stacks Project.

**`Deformation.infinitesimalAutomorphisms_eq_bot_iff_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/InfinitesimalAutomorphism/EquivalenceCriterion.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/InfinitesimalAutomorphism/EquivalenceCriterion.lean#L208).

> **Stacks 06K0.** For a category cofibered in groupoids over `𝒞_Λ` satisfying (RS) and an
> object `x₀` of the fibre over the residue field, the infinitesimal automorphisms of `x₀`
> vanish exactly when the canonical morphism `ℱ_{x₀} ⟶ ℱ̄_{x₀}` to the functor of fibrewise
> isomorphism classes is an equivalence.

```lean
theorem infinitesimalAutomorphisms_eq_bot_iff_isEquivalence (hrs : SatisfiesRS p)
    {A₀ Aε : ArtinianLocalAlgCat.{u, v, w} Λ k} {x₀ : p.Fiber A₀} {xε : p.Fiber Aε}
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1) (hi : p.IsHomLift g i) :
    infinitesimalAutomorphisms hrs.1 g e hpair i hi = ⊥ ↔
      (toIsomorphismClasses (pointLocalization p x₀.1)
        (isCofiberedInGroupoids_objectsOverFunctor hrs.1
          (maximalIdeal_eq_bot_of_isCanonicalDualNumberPair hpair)
            x₀)).toFunctor.IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.19, Tag 06JN](https://stacks.math.columbia.edu/tag/06JN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
