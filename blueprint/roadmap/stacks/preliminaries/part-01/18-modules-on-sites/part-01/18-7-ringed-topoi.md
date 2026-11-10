---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedToposHom, AlgebraicGeometry.RingedToposHom.comp_assoc, AlgebraicGeometry.RingedTopos, AlgebraicGeometry.RingedToposSiteHom, AlgebraicGeometry.RingedToposSiteHom.comp, AlgebraicGeometry.RingedToposHom.comp, AlgebraicGeometry.RingedToposHom.exists_twoSided_isDenseSubsite_morphismOfSites, AlgebraicGeometry.RingedToposHom.exists_oneSided_isDenseSubsite_of_isEquivalence
statement: formalized
proof: formalized
---

# 18.7 Ringed topoi

Section 18.7 of the Stacks Project, [Tag 01D2](https://stacks.math.columbia.edu/tag/01D2). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01D3, a definition

[Tag 01D3](https://stacks.math.columbia.edu/tag/01D3) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposHom.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposHom.lean#L123). The attribute's comment: “part (2): morphisms of ringed topoi”. References: SGA 4 Vbis (1.3.2), “absolute case (D = pt)”; SGA 4 IV (13.1).

> **Stacks 01D3, part (2).** A morphism of ringed topoi: a morphism of the underlying topoi
> together with a map from the structure sheaf of the target to the direct image of the structure
> sheaf of the source.

```lean
structure RingedToposHom (X : RingedTopos.{v, u, w}) (Y : RingedTopos.{v', u', w'})
    [X.J.HasSheafCompose (forget RingCat.{w})]
    [Y.J.HasSheafCompose (forget RingCat.{w'})]
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [Y.J.HasSheafCompose (forget₂ CommRingCat.{w'} RingCat.{w'})]
```

**`AlgebraicGeometry.RingedToposHom.comp_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposHomCompAssoc.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposHomCompAssoc.lean#L62). The attribute's comment: “part (3): composition is associative”.

> **Composition of morphisms of ringed topoi is associative.**

```lean
theorem comp_assoc (f : RingedToposHom X Y) (g : RingedToposHom Y Z) (h : RingedToposHom Z W) :
    h.comp (g.comp f) = (h.comp g).comp f
```

**`AlgebraicGeometry.RingedTopos`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedTopos.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedTopos.lean#L47). The attribute's comment: “part (1): ringed topoi”. References: SGA 4 Vbis (1.3.1), “absolute case (D = pt)”; SGA 4 IV (11.1.1), “ringed topos”.

> A site with a sheaf of commutative rings.

```lean
structure RingedTopos.{v₁, u₁, w₁}
```

**`AlgebraicGeometry.RingedToposSiteHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean#L83). The attribute's comment: “part (2): morphisms of ringed topoi, with the geometric morphism presented by a continuous functor between the underlying sites rather than by an arbitrary adjoint pair; `RingedToposHom.toToposHom` produces the underlying morphism of topoi once that functor is a morphism of sites”.

> **Stacks 01D3, part (2).** A morphism of ringed topoi `X ⟶ Y`: a morphism of topoi
> between the underlying topoi together with a map of sheaves of commutative rings
> `O_Y ⟶ f_* O_X`.
>
> The geometric morphism is presented by a continuous functor `u : Y.C ⥤ X.C` between the
> underlying sites in the opposite direction, as in the source's convention for a morphism of
> sites; `RingedToposSiteHom.toToposHom` produces the morphism of topoi itself as soon as `u` is a
> morphism of sites. This is the generality in which the pullback of sheaves of modules of
> Stacks 03D6 is available.

```lean
structure RingedToposSiteHom (X : RingedTopos.{v, u, w}) (Y : RingedTopos.{v', u', w})
```

**`AlgebraicGeometry.RingedToposSiteHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposHom.lean#L103). The attribute's comment: “part (3): composition of morphisms of ringed topoi”.

> **Stacks 01D3, part (3).** Composition of morphisms of ringed topoi: the underlying
> continuous functors compose, and the structure map is
> `O_Z ⟶ g_* O_Y ⟶ g_* f_* O_X = (g ∘ f)_* O_X`, the last identification being the canonical
> one of `CategoryTheory.Functor.sheafPushforwardContinuousComp`.

```lean
def comp (g : RingedToposSiteHom Y Z) (f : RingedToposSiteHom X Y) : RingedToposSiteHom X Z
```

**`AlgebraicGeometry.RingedToposHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/RingedToposComp.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/RingedToposComp.lean#L295). The attribute's comment: “part (3): composition”.

> The composition of two morphisms of ringed topoi: the underlying morphisms of topoi compose,
> and the structure map of the composite is
> `O_Z ⟶ g_*O_Y ⟶ g_*f_*O_X ≅ (g ∘ f)_*O_X`, the last step being the canonical comparison of
> successive direct images with the direct image of the composite.

```lean
noncomputable def comp (g : RingedToposHom Y Z) (f : RingedToposHom X Y) :
    RingedToposHom X Z
```

## Tag 03CR, a lemma

[Tag 03CR](https://stacks.math.columbia.edu/tag/03CR) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.exists_twoSided_isDenseSubsite_morphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/RingedToposReplacement.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/RingedToposReplacement.lean#L185). The attribute's comment: “Every morphism of ringed topoi fits into a commutative square whose two vertical arrows are the equivalences induced by special cocontinuous functors, with the replacement structure sheaves the direct images of the given ones and the two structure maps the identity, and whose bottom arrow comes from a continuous functor `u : D' ⥤ C'` preserving all finite limits, with both replacement sites having all finite limits and subcanonical topologies and with prescribed families of sheaves becoming representable on them. Conclusions (1)-(7); the addendum on an equivalence is `exists_oneSided_isDenseSubsite_of_isEquivalence`.”.

> **Stacks 03CR.** Let `(f, f♯) : (Sh(C), O_C) → (Sh(D), O_D)` be a morphism of ringed topoi.
> Then there are sites `(C', J')` and `(D', K')`, special cocontinuous functors `v : C ⥤ C'` and
> `w : D ⥤ D'`, and a functor `u : D' ⥤ C'` such that
>
> 1. `v` and `w` exhibit `(C, J)` and `(D, K)` as dense subsites and the morphisms of topoi
>    `g : Sh(C) → Sh(C')` and `e : Sh(D) → Sh(D')` they induce are equivalences (Stacks 03A0);
> 2. the replacement structure sheaves are `O_{C'} = g_*O_C` and `O_{D'} = e_*O_D`, and the structure
>    maps `g♯` and `e♯` are the identity;
> 3. `J'` and `K'` are subcanonical and `C'` and `D'` have all finite limits;
> 4. `u` is continuous, preserves all finite limits, is representably flat and defines a morphism of
>    sites — in other words Stacks 00X6 applies to `u`;
> 5. each `g_*(F i)` is a representable sheaf on `C'` and each `e_*(G j)` is a representable sheaf on
>    `D'`, for prescribed families of sheaves `F` on `C` and `G` on `D`; and
> 6. there is a morphism of ringed topoi `(h, h♯) : (Sh(C'), O_{C'}) → (Sh(D'), O_{D'})` whose
>    underlying morphism of topoi is the one Stacks 00XC attaches to the morphism of sites `u`, and
>    for which the square `(h, h♯) ∘ (g, g♯) ≅ (e, e♯) ∘ (f, f♯)` 2-commutes.
>
> The source's addendum, on the case of an equivalence, is
> `AlgebraicGeometry.RingedToposHom.exists_oneSided_isDenseSubsite_of_isEquivalence`.

```lean
theorem exists_twoSided_isDenseSubsite_morphismOfSites (X Y : RingedTopos.{u, u, u})
    (f : RingedToposHom X Y) {ι : Type u} (F : ι → Sheaf X.J (Type u)) {κ : Type u}
    (G : κ → Sheaf Y.J (Type u)) :
    ∃ (C' : Type u) (_ : SmallCategory C') (J' : GrothendieckTopology C') (D' : Type u)
      (_ : SmallCategory D') (K' : GrothendieckTopology D') (v : X.C ⥤ C') (w : Y.C ⥤ D')
      (u : D' ⥤ C') (_ : v.IsDenseSubsite X.J J') (_ : w.IsDenseSubsite Y.J K')
      (_ : HasFiniteLimits C') (_ : HasFiniteLimits D') (_ : J'.Subcanonical)
      (_ : K'.Subcanonical) (_ : u.IsContinuous K' J')
      (_ : PreservesFiniteLimits u) (_ : RepresentablyFlat u)
      (hu : u.IsMorphismOfSites K' J'),
      let X' : RingedTopos.{u, u, u} :=
        { C := C', J := J',
          O := (Functor.IsDenseSubsite.morphismOfTopoi X.J J' v).pushforwardRing.obj X.O }
      let Y' : RingedTopos.{u, u, u} :=
        { C := D', J := K',
          O := (Functor.IsDenseSubsite.morphismOfTopoi Y.J K' w).pushforwardRing.obj Y.O }
      let g : RingedToposHom X X' :=
        { toToposHom := Functor.IsDenseSubsite.morphismOfTopoi X.J J' v, fSharp := 𝟙 _ }
      let e : RingedToposHom Y Y' :=
        { toToposHom := Functor.IsDenseSubsite.morphismOfTopoi Y.J K' w, fSharp := 𝟙 _ }
      g.toToposHom.pushforward.IsEquivalence ∧ e.toToposHom.pushforward.IsEquivalence ∧
        (∀ i, (g.toToposHom.pushforward.obj (F i)).obj.IsRepresentable) ∧
        (∀ j, (e.toToposHom.pushforward.obj (G j)).obj.IsRepresentable) ∧
        ∃ h : RingedToposHom X' Y',
          h.toToposHom = hu.morphismOfTopoi ∧
            Nonempty (TwoIso (A := X) (B := Y')
              (RingedToposHom.comp (X := X) (Y := X') (Z := Y') h g)
              (RingedToposHom.comp (X := X) (Y := Y) (Z := Y') e f))
```

**`AlgebraicGeometry.RingedToposHom.exists_oneSided_isDenseSubsite_of_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/RingedToposReplacement.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/RingedToposReplacement.lean#L244). The attribute's comment: “the addendum: an equivalence of ringed topoi is factored over a *single* replacement site `C' = D'`, with the middle morphism of ringed topoi the identity — the identity morphism of topoi together with an isomorphism `e_*O_D ≅ g_*O_C` of the two replacement structure sheaves, which is the agreement of the structure sheaves the source asserts. See the module's implementation notes for why that isomorphism cannot be an equality.”.

> **Stacks 03CR, the addendum.** If `(f, f♯) : (Sh(C), O_C) → (Sh(D), O_D)` is an *equivalence*
> of ringed topoi — that is, `f` is an equivalence of topoi and `f♯` is an isomorphism — then the
> factorization of Stacks 03CR may be chosen with the two replacement sites equal, the two
> replacement structure sheaves identified, and `(h, h♯)` the identity. Concretely there are a single
> site `(C', J')` with all finite limits and a subcanonical topology and special cocontinuous
> functors `v : C ⥤ C'` and `w : D ⥤ C'` such that, writing `g` and `e` for the equivalences of
> ringed topoi they induce as in Stacks 03CR,
>
> 1. prescribed families of sheaves `F` on `C` and `G` on `D` become representable on `C'`; and
> 2. the middle morphism `(h, h♯)` is the identity: its underlying morphism of topoi is
>    `MorphismOfTopoi.id`, its structure map `h♯ : e_*O_D ⟶ g_*O_C` is an isomorphism — this is the
>    agreement of the two replacement structure sheaves — and the square
>    `(h, h♯) ∘ (g, g♯) ≅ (e, e♯) ∘ (f, f♯)` 2-commutes.

```lean
theorem exists_oneSided_isDenseSubsite_of_isEquivalence (X Y : RingedTopos.{u, u, u})
    (f : RingedToposHom X Y) [f.toToposHom.pushforward.IsEquivalence] [IsIso f.fSharp]
    {ι : Type u} (F : ι → Sheaf X.J (Type u)) {κ : Type u} (G : κ → Sheaf Y.J (Type u)) :
    ∃ (C' : Type u) (_ : SmallCategory C') (J' : GrothendieckTopology C') (v : X.C ⥤ C')
      (w : Y.C ⥤ C') (_ : v.IsDenseSubsite X.J J') (_ : w.IsDenseSubsite Y.J J')
      (_ : HasFiniteLimits C') (_ : J'.Subcanonical),
      let X' : RingedTopos.{u, u, u} :=
        { C := C', J := J',
          O := (Functor.IsDenseSubsite.morphismOfTopoi X.J J' v).pushforwardRing.obj X.O }
      let Y' : RingedTopos.{u, u, u} :=
        { C := C', J := J',
          O := (Functor.IsDenseSubsite.morphismOfTopoi Y.J J' w).pushforwardRing.obj Y.O }
      let g : RingedToposHom X X' :=
        { toToposHom := Functor.IsDenseSubsite.morphismOfTopoi X.J J' v, fSharp := 𝟙 _ }
      let e : RingedToposHom Y Y' :=
        { toToposHom := Functor.IsDenseSubsite.morphismOfTopoi Y.J J' w, fSharp := 𝟙 _ }
      g.toToposHom.pushforward.IsEquivalence ∧ e.toToposHom.pushforward.IsEquivalence ∧
        (∀ i, (g.toToposHom.pushforward.obj (F i)).obj.IsRepresentable) ∧
        (∀ j, (e.toToposHom.pushforward.obj (G j)).obj.IsRepresentable) ∧
        ∃ h : RingedToposHom X' Y',
          h.toToposHom = MorphismOfTopoi.id (Sheaf J' (Type u)) ∧ IsIso h.fSharp ∧
            Nonempty (TwoIso (A := X) (B := Y')
              (RingedToposHom.comp (X := X) (Y := X') (Z := Y') h g)
              (RingedToposHom.comp (X := X) (Y := Y) (Z := Y') e f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.7, Tag 01D2](https://stacks.math.columbia.edu/tag/01D2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
