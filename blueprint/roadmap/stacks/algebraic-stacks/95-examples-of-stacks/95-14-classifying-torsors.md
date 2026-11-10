---
declaration: section
origin: cited
lean: SheafOfGroups.Torsors, SheafOfGroups.Torsors.Hom, SheafOfGroups.Torsors.instCategory, SheafOfGroups.Torsors.projection, SheafOfGroups.Torsors.isIso_of_isIso_base, SheafOfGroups.Torsors.projection_effectiveDescent, SheafOfGroups.Torsors.projection_isStackInGroupoids, SheafOfGroups.Torsors.projection_isFiberedInGroupoids
statement: formalized
proof: formalized
---

# 95.14 Classifying torsors

Section 95.14 of the Stacks Project, [Tag 036Z](https://stacks.math.columbia.edu/tag/036Z). 9 tags here are carried by 46 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04UJ, a subsection

[Tag 04UJ](https://stacks.math.columbia.edu/tag/04UJ) in the Stacks Project.

**`SheafOfGroups.Torsors`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean#L88). The attribute's comment: “the objects of 𝒢-Torsors”. References: SGA 1 XIII (1.3), “partial”.

> **Stacks 04UJ.** An object of the category `𝒢-Torsors` of torsors under a sheaf of groups
> `𝒢` on a site `(C, J)`: an object `U` of `C` together with a `𝒢|_U`-torsor on the localized
> site `C/U`.

```lean
structure SheafOfGroups.Torsors (𝒢 : SheafOfGroups.{w} (C := C) J)
```

**`SheafOfGroups.Torsors.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean#L134). The attribute's comment: “the morphisms of 𝒢-Torsors”. References: SGA 1 XIII (1.3), “partial”.

> **Stacks 04UJ.** A morphism `(U, F) ⟶ (V, H)` of the category `𝒢-Torsors`: a morphism
> `f : U ⟶ V` of `C` together with an isomorphism `α : f^{-1}H ⟶ F` of `𝒢|_U`-torsors. The
> isomorphism is recorded through its inverse on total spaces: a map of sheaves on `C` over `f`
> which restricts to a bijection from the fibre of `Total F` over each `a : V ⟶ U` to the fibre
> of `Total H` over `a ≫ f`.

```lean
structure Hom (T T' : Torsors.{t} 𝒢)
```

**`SheafOfGroups.Torsors.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean#L198). The attribute's comment: “the category 𝒢-Torsors”. References: SGA 1 XIII (1.3), “partial”.

> **Stacks 04UJ.** The torsors under a sheaf of groups `𝒢` on a site `(C, J)` form a category
> `𝒢-Torsors`: morphisms compose by composing `f` and `α`.

```lean
instance instCategory : Category (Torsors.{t} 𝒢)
```

**`SheafOfGroups.Torsors.projection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean#L209). The attribute's comment: “the functor p to the site”. References: SGA 1 XIII (1.3), “partial”.

> **Stacks 04UJ.** The functor `p : 𝒢-Torsors ⥤ C` sending a pair `(U, F)` to `U`, which is
> how `𝒢-Torsors` is regarded as a category over the site.

```lean
def projection : Torsors.{t} 𝒢 ⥤ C
```

**`SheafOfGroups.Torsors.isIso_of_isIso_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/CategoryOfTorsors.lean#L275). The attribute's comment: “the fibre categories are groupoids”.

> **Stacks 04UJ.** A morphism of `𝒢-Torsors` whose morphism `f` of the site is an isomorphism
> is itself an isomorphism. Every morphism of a fibre category of `p : 𝒢-Torsors ⥤ C` lies over an
> identity, so this says that the fibre category over `U` — the category of `𝒢|_U`-torsors — is a
> groupoid.

```lean
theorem isIso_of_isIso_base : IsIso m
```

## Tag 04UK, a lemma

[Tag 04UK](https://stacks.math.columbia.edu/tag/04UK) in the Stacks Project.

**`SheafOfGroups.Torsors.projection_effectiveDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/EffectiveDescent.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/EffectiveDescent.lean#L590). The attribute's comment: “condition (3): descent data are effective”. References: EGA IV (16.5.15), “more general”.

> **Stacks 04UK**, condition (3) of Stacks 02ZI: every descent datum for
> `p : 𝒢-Torsors ⥤ C` relative to a `J`-covering family with genuine fibre-product overlaps is
> effective.
>
> The object over `U` is glued by hand: the sections of its torsor over `(W, β)` are the matching
> families which assign, to every factorization of `g ≫ β` through a member `f i` of the covering
> family, a section of `D.x i`, compatibly with the restriction maps and with the glueing
> isomorphisms of the descent datum. That this is a sheaf is the sheaf condition for the `D.x i`;
> that `𝒢` acts simply transitively on it is the simple transitivity on the `D.x i` together with
> the sheaf condition for `𝒢`; and that it is locally nonempty follows because each `D.x i` is.
> The morphisms `D.x i ⟶ x` send a section of `D.x i` to the matching family it spreads out to,
> whose compatibility over the double overlaps is exactly the cocycle condition of the descent
> datum, and which recovers the section it came from because of the cocycle condition at
> `(i, i, i)`. Effectivity then follows from
> `SheafOfGroups.Torsors.isEffective_of_glueing`.
>
> A matching family is indexed by the objects and the morphisms of `C` and by the index set of the
> covering family, so it lives in `Type (max u v s t)`: the statement is for torsors whose
> sections lie in `Type (max u v s t)`, which is the same bound `max u v s ≤ t` that the route
> through Stacks 04TP and 04TS imposes.

```lean
theorem projection_effectiveDescent {U : C} {I : Type s} (V : I → C) (f : ∀ i, V i ⟶ U)
    (hf : Sieve.ofArrows V f ∈ J U)
    (Vij : I → I → C) (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j)
    (hVij : ∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j))
    (Vijk : I → I → I → C)
    (s₁₂ : ∀ i j k, Vijk i j k ⟶ Vij i j) (s₂₃ : ∀ i j k, Vijk i j k ⟶ Vij j k)
    (hVijk : ∀ i j k, IsPullback (s₁₂ i j k) (s₂₃ i j k) (pr₂ i j) (pr₁ j k))
    (q₁ : ∀ i j k, Vijk i j k ⟶ V i) (q₂ : ∀ i j k, Vijk i j k ⟶ V j)
    (q₃ : ∀ i j k, Vijk i j k ⟶ V k)
    (hq₁ : ∀ i j k, q₁ i j k = s₁₂ i j k ≫ pr₁ i j)
    (hq₂ : ∀ i j k, q₂ i j k = s₁₂ i j k ≫ pr₂ i j)
    (hq₃ : ∀ i j k, q₃ i j k = s₂₃ i j k ≫ pr₂ j k)
    (D : Functor.DescentDatum (projection : Torsors.{max u v s t} 𝒢 ⥤ C) V f Vij pr₁ pr₂ hVij
      Vijk s₁₂ s₂₃ hVijk q₁ q₂ q₃ hq₁ hq₂ hq₃) :
    D.IsEffective
```

**`SheafOfGroups.Torsors.projection_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/EffectiveDescent.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/EffectiveDescent.lean#L719). References: SGA 3 IV (4.5.13), “special case”.

> **Stacks 04UK.** The functor `p : 𝒢-Torsors ⥤ C` of Stacks 04UJ is a stack in groupoids
> over the site `(C, J)`: it is fibred in groupoids, its `Isom` presheaves are sheaves, and every
> descent datum relative to a covering family is effective.

```lean
theorem projection_isStackInGroupoids :
    Functor.IsStackInGroupoids.{s} (projection : Torsors.{max u v s t} 𝒢 ⥤ C) J
```

**`SheafOfGroups.Torsors.projection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/FiberedInGroupoids.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/FiberedInGroupoids.lean#L188). The attribute's comment: “condition (1): p is fibred in groupoids”. References: SGA 4 XVIII (1.2.1), “partial”.

> **Stacks 04UK**, condition (1) of Stacks 02ZI. The functor `p : 𝒢-Torsors ⥤ C` of
> Stacks 04UJ is fibred in groupoids: a morphism `f : V ⟶ U` of `C` lifts to the morphism
> `(V, f^{-1}F) ⟶ (U, F)` out of the restricted torsor, and a fill-in is unique because the
> recorded map of a morphism of `𝒢-Torsors` is a bijection on the sections over each base
> morphism.

```lean
theorem projection_isFiberedInGroupoids :
    (projection : Torsors.{t} 𝒢 ⥤ C).IsFiberedInGroupoids
```

**`SheafOfGroups.Torsors.projection_isomIsSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/IsomSheaf.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsors/StackOfTorsors/IsomSheaf.lean#L45). The attribute's comment: “condition (2): the Isom presheaves are sheaves”.

> **Stacks 04UK**, condition (2) of Stacks 02ZI: the presheaves `Isom(x, y)` on `C/U` are
> sheaves. For two torsors `x` and `y` over the same object `U` of `C` and a covering family
> `{V i → U}` of `U` whose overlaps are genuine fibre products `V i ×_U V j`, a family of
> isomorphisms `x|_{V i} ⟶ y|_{V i}` of torsors which agree on the overlaps glues to a unique
> isomorphism `x ⟶ y` of `𝒢|_U`-torsors restricting to the given ones.
>
> The glued morphism is produced by the sheaf condition for the torsor `y` on `C/U`: a section of
> `x` over an object of `C/U` is, locally on a covering refining `{V i → U}`, the image of a
> section of a restriction `x|_{V i}` under the cartesian morphism `x|_{V i} ⟶ x`, and applying
> the given isomorphism there prescribes the sought section of `y` locally. The prescriptions
> agree because two local factorizations through `f i` and `f j` factor jointly through the fibre
> product `V i ×_U V j`, where the hypothesis supplies a single common restriction of the two
> isomorphisms. Equivariance for `𝒢` and compatibility with the restriction maps are inherited
> pointwise from the given isomorphisms, and the glued morphism is an isomorphism because a
> morphism of `𝒢-Torsors` lying over an isomorphism of `C` is one (Stacks 04UJ).

```lean
theorem projection_isomIsSheaf {U : C} (x y : Torsors.{t} 𝒢)
    (hx : projection.obj x = U) (hy : projection.obj y = U)
    {I : Type s} (V : I → C) (f : ∀ i, V i ⟶ U) (hf : Sieve.ofArrows V f ∈ J U)
    (Vij : I → I → C) (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j)
    (hVij : ∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j))
    (xr : ∀ i, Functor.Restriction projection (f i) x hx)
    (yr : ∀ i, Functor.Restriction projection (f i) y hy)
    (xrij : ∀ i j, Functor.Restriction projection (pr₁ i j ≫ f i) x hx)
    (yrij : ∀ i j, Functor.Restriction projection (pr₁ i j ≫ f i) y hy) :
    Functor.IsomIsSheafFor projection x y hx hy V f Vij pr₁ pr₂ hVij xr yr xrij yrij
```

## Tag 04UL, a subsection

[Tag 04UL](https://stacks.math.columbia.edu/tag/04UL) in the Stacks Project.

**`AlgebraicGeometry.Space.SheafTorsors`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean#L123). The attribute's comment: “the objects of 𝒢/ℬ-Torsors”.

> **Stacks 04UL.** An object of the category `𝒢/ℬ-Torsors`: an object `U` of the big fppf site
> of `S`, a section `b : U ⟶ ℬ` of `ℬ` over `U`, and a `U ×_{b, ℬ} 𝒢`-torsor `F` over `U`.

```lean
structure SheafTorsors
```

**`AlgebraicGeometry.Space.SheafTorsors.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean#L272). The attribute's comment: “the morphisms of 𝒢/ℬ-Torsors”.

> **Stacks 04UL.** A morphism `(U, b, F) ⟶ (U', b', F')` of `𝒢/ℬ-Torsors`: a morphism
> `f : U ⟶ U'` with `b = b' ∘ f` together with an equivariant identification of `F` with
> `f^{-1}F'`.

```lean
structure Hom (T T' : SheafTorsors G)
```

**`AlgebraicGeometry.Space.SheafTorsors.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean#L323). The attribute's comment: “the category 𝒢/ℬ-Torsors”.

> **Stacks 04UL.** The torsors for a group object `𝒢` over a sheaf `ℬ` form a category
> `𝒢/ℬ-Torsors`: morphisms compose by composing `f` and the identification of the total
> spaces.

```lean
instance instCategory : Category (SheafTorsors G)
```

**`AlgebraicGeometry.Space.SheafTorsors.projection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean#L336). The attribute's comment: “the functor p to the site”.

> **Stacks 04UL.** The functor `p : 𝒢/ℬ-Torsors ⥤ (Sch/S)_fppf` sending `(U, b, F)` to `U`,
> which is how `𝒢/ℬ-Torsors` is regarded as a category over the big fppf site of `S`.

```lean
def projection : SheafTorsors G ⥤ BigFppfOver 𝒞 S hS
```

**`AlgebraicGeometry.Space.SheafTorsors.isIso_of_isIso_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfSheafTorsors.lean#L391). The attribute's comment: “the fibre categories are groupoids”.

> **Stacks 04UL.** A morphism of `𝒢/ℬ-Torsors` whose morphism `f` of the big fppf site is an
> isomorphism is itself an isomorphism. Every morphism of a fibre category of
> `p : 𝒢/ℬ-Torsors ⥤ (Sch/S)_fppf` lies over an identity, so this says that the fibre category
> over `U` — the disjoint union over the sections `b` of `ℬ` over `U` of the categories of
> `U ×_{b, ℬ} 𝒢`-torsors — is a groupoid.

```lean
theorem isIso_of_isIso_base : IsIso φ
```

## Tag 04UM, a lemma

[Tag 04UM](https://stacks.math.columbia.edu/tag/04UM) in the Stacks Project.

**`AlgebraicGeometry.Space.SheafTorsors.projection_effectiveDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/SheafTorsorsEffectiveDescent.lean, line 1392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/SheafTorsorsEffectiveDescent.lean#L1392). The attribute's comment: “condition (3): descent data are effective”.

> **Stacks 04UM.** Condition (3) of Stacks 02ZI for the functor
> `p : 𝒢/ℬ-Torsors ⥤ (Sch/S)_fppf` of Stacks 04UL: every descent datum of `𝒢/ℬ-Torsors`
> relative to a covering family of the big fppf site of `S` is effective.

```lean
theorem projection_effectiveDescent
    (hB : Presheaf.IsSheaf (BigFppfOver.topology 𝒞 S hS) B)
    (hG : Presheaf.IsSheaf (BigFppfOver.topology 𝒞 S hS) G.X.left) :
    ∀ {U : BigFppfOver 𝒞 S hS} {I : Type w} (V : I → BigFppfOver 𝒞 S hS)
      (f : ∀ i, V i ⟶ U), Sieve.ofArrows V f ∈ BigFppfOver.topology 𝒞 S hS U →
      ∀ (Vij : I → I → BigFppfOver 𝒞 S hS)
        (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j)
        (hVij : ∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j))
        (Vijk : I → I → I → BigFppfOver 𝒞 S hS)
        (s₁₂ : ∀ i j k, Vijk i j k ⟶ Vij i j) (s₂₃ : ∀ i j k, Vijk i j k ⟶ Vij j k)
        (hVijk : ∀ i j k, IsPullback (s₁₂ i j k) (s₂₃ i j k) (pr₂ i j) (pr₁ j k))
        (q₁ : ∀ i j k, Vijk i j k ⟶ V i) (q₂ : ∀ i j k, Vijk i j k ⟶ V j)
        (q₃ : ∀ i j k, Vijk i j k ⟶ V k)
        (hq₁ : ∀ i j k, q₁ i j k = s₁₂ i j k ≫ pr₁ i j)
        (hq₂ : ∀ i j k, q₂ i j k = s₁₂ i j k ≫ pr₂ i j)
        (hq₃ : ∀ i j k, q₃ i j k = s₂₃ i j k ≫ pr₂ j k)
        (D : Functor.DescentDatum (projection G) V f Vij pr₁ pr₂ hVij Vijk s₁₂ s₂₃ hVijk
          q₁ q₂ q₃ hq₁ hq₂ hq₃),
        D.IsEffective
```

**`AlgebraicGeometry.Space.SheafTorsors.projection_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/SheafTorsorsEffectiveDescent.lean, line 1789](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/SheafTorsorsEffectiveDescent.lean#L1789).

> **Stacks 04UM.** The functor `p : 𝒢/ℬ-Torsors ⥤ (Sch/S)_fppf` of Stacks 04UL is a stack in
> groupoids over the big fppf site of `S`: the three conditions of Stacks 02ZI, namely
> `AlgebraicGeometry.Space.SheafTorsors.projection_isFiberedInGroupoids`,
> `AlgebraicGeometry.Space.SheafTorsors.projection_isomIsSheaf` and
> `AlgebraicGeometry.Space.SheafTorsors.projection_effectiveDescent`.

```lean
theorem projection_isStackInGroupoids
    (hB : Presheaf.IsSheaf (BigFppfOver.topology 𝒞 S hS) B)
    (hG : Presheaf.IsSheaf (BigFppfOver.topology 𝒞 S hS) G.X.left) :
    Functor.IsStackInGroupoids.{w} (projection G) (BigFppfOver.topology 𝒞 S hS)
```

**`AlgebraicGeometry.Space.SheafTorsors.projection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfSheafTorsors.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfSheafTorsors.lean#L612). The attribute's comment: “condition (1): p is fibred in groupoids”.

> **Stacks 04UM.** Condition (1) of Stacks 02ZI for the functor
> `p : 𝒢/ℬ-Torsors ⥤ (Sch/S)_fppf` of Stacks 04UL: `p` is fibred in groupoids. Every morphism
> `f : V ⟶ U` of the big fppf site of `S` lifts to the restriction `(V, b ∘ f, f^{-1}F)` of an
> object `(U, b, F)` along `f`, and fill-ins exist and are unique.

```lean
theorem projection_isFiberedInGroupoids : (projection G).IsFiberedInGroupoids
```

**`AlgebraicGeometry.Space.SheafTorsors.projection_isomIsSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfSheafTorsors.lean, line 1011](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfSheafTorsors.lean#L1011). The attribute's comment: “condition (2): the Isom presheaves are sheaves”.

> **Stacks 04UM.** Condition (2) of Stacks 02ZI for the functor
> `p : 𝒢/ℬ-Torsors ⥤ (Sch/S)_fppf` of Stacks 04UL: for two objects `(U, b, F)` and `(U, b', F')`
> over the same object of the big fppf site of `S`, the presheaf `Isom(F, F')` is a sheaf. A family
> of isomorphisms of the restrictions along a covering family which agree on the overlaps glues,
> uniquely, to an isomorphism over `U`, because the total spaces are sheaves and the restrictions
> have as total spaces their base changes.

```lean
theorem projection_isomIsSheaf
    (hB : Presheaf.IsSheaf (BigFppfOver.topology 𝒞 S hS) B) :
    ∀ {U : BigFppfOver 𝒞 S hS} (x y : SheafTorsors G)
      (hx : (projection G).obj x = U) (hy : (projection G).obj y = U)
      {I : Type w} (V : I → BigFppfOver 𝒞 S hS) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ BigFppfOver.topology 𝒞 S hS U →
      ∀ (Vij : I → I → BigFppfOver 𝒞 S hS)
        (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j)
        (hVij : ∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j))
        (xr : ∀ i, Functor.Restriction (projection G) (f i) x hx)
        (yr : ∀ i, Functor.Restriction (projection G) (f i) y hy)
        (xrij : ∀ i j, Functor.Restriction (projection G) (pr₁ i j ≫ f i) x hx)
        (yrij : ∀ i j, Functor.Restriction (projection G) (pr₁ i j ≫ f i) y hy),
        Functor.IsomIsSheafFor (projection G) x y hx hy V f Vij pr₁ pr₂ hVij xr yr xrij yrij
```

## Tag 04UN, a subsection

[Tag 04UN](https://stacks.math.columbia.edu/tag/04UN) in the Stacks Project.

**`AlgebraicGeometry.Space.TorsorsFor.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L280). The attribute's comment: “the morphisms of G-Principal, stated for an arbitrary trivializing covering property”.

> A morphism `(U, b, X) ⟶ (U', b', X')` of torsors: a morphism `f : U ⟶ U'` over `B` together
> with an equivariant identification of `X` with `U ×_{f, U'} X'`.

```lean
structure Hom (T T' : TorsorsFor hB G P)
```

**`AlgebraicGeometry.Space.TorsorsFor.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L331). The attribute's comment: “the category G-Principal, whose composition is stated for an arbitrary trivializing covering property”.

> The torsors under a group algebraic space `G` over `B` which are trivialized by a family
> satisfying `P` form a category: morphisms compose by composing `f` and the identification of the
> total spaces.

```lean
instance instCategory : Category (TorsorsFor hB G P)
```

**`AlgebraicGeometry.Space.TorsorsFor.isIso_of_isIso_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L402). The attribute's comment: “the fibre categories of p : G-Principal ⥤ (Sch/S)\_fppf are groupoids, by the assertion for an arbitrary trivializing covering property”.

> A morphism of torsors whose morphism `f` of the big fppf site is an isomorphism is itself an
> isomorphism. Every morphism of a fibre category of the functor `p` to the site lies over an
> identity, so this says that the fibre category over `U` — the disjoint union over the morphisms
> `b : U ⟶ B` of the categories of torsors under `U ×_{b, B} G` trivialized by a family satisfying
> `P` — is a groupoid.

```lean
theorem isIso_of_isIso_base : IsIso φ
```

**`AlgebraicGeometry.Space.PrincipalHomogeneousSpaces`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfPrincipalHomogeneousSpaces.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfPrincipalHomogeneousSpaces.lean#L89). The attribute's comment: “the objects of G-Principal”.

> **Stacks 04UN.** An object of the category `G-Principal`: an object `U` of the big fppf site
> of `S`, a morphism `b : U ⟶ B`, and a principal homogeneous space `X` over `U` under
> `G_U = U ×_{b, B} G`, that is a pseudo-torsor trivialized by an fpqc covering of `U`.

```lean
abbrev PrincipalHomogeneousSpaces
```

**`AlgebraicGeometry.Space.PrincipalHomogeneousSpaces.projection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfPrincipalHomogeneousSpaces.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfPrincipalHomogeneousSpaces.lean#L109). The attribute's comment: “the functor p to the site”.

> **Stacks 04UN.** The functor `p : G-Principal ⥤ (Sch/S)_fppf` sending `(U, b, X)` to `U`,
> which is how `G-Principal` is regarded as a category over the big fppf site of `S`.

```lean
abbrev PrincipalHomogeneousSpaces.projection :
    PrincipalHomogeneousSpaces hB G ⥤ BigFppfOver 𝒞 S hS
```

## Tag 04UP, a remark

[Tag 04UP](https://stacks.math.columbia.edu/tag/04UP) in the Stacks Project.

**`AlgebraicGeometry.Space.PrincipalHomogeneousSpaces.isStackInGroupoids_of_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/PrincipalHomogeneousSpacesStack.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/PrincipalHomogeneousSpacesStack.lean#L742). The attribute's comment: “p : G-Principal ⥤ (Sch/S)\_fppf is a stack in groupoids once principal homogeneous spaces descend along fppf coverings as in (1)-(4)”.

> **Stacks 04UP.** If principal homogeneous spaces satisfy effective descent along the
> coverings of `(Sch/S)_fppf` (items (1)–(4) of the remark,
> `AlgebraicGeometry.Space.PrincipalHomogeneousSpaceDescent`), then
> `p : G-Principal ⥤ (Sch/S)_fppf` is a stack in groupoids over `(Sch/S)_fppf`.
>
> This is the formal content of the remark: Stacks conjectures that `p` is a stack in groupoids and
> says that this would follow from the descent statement (1)–(4), whose proof by the technique of
> Stacks 04U1 stops at a set theoretical question; that descent statement is the antecedent here,
> and the implication is proved in full.
>
> * Condition (1) of Stacks 02ZI, that `p` is fibred in groupoids, is
>   `AlgebraicGeometry.Space.PrincipalHomogeneousSpaces.projection_isFiberedInGroupoids`.
> * Condition (2), that the `Isom` presheaves are sheaves, is
>   `AlgebraicGeometry.Space.TorsorsFor.projection_isomIsSheaf` at the fpqc coverings: isomorphisms
>   of total spaces glue because the total spaces are algebraic spaces, hence sheaves.
> * Condition (3): given a descent datum of `G-Principal` along a covering `{Vᵢ ⟶ U}`, the sections
>   `bᵢ : Vᵢ ⟶ B` glue to `b : U ⟶ B` because `B` is a sheaf
>   (`AlgebraicGeometry.Space.PrincipalHomogeneousSpaces.exists_glued_sec`); with
>   `H = U ×_{b, B} G` the acting groups `Vᵢ ×_{bᵢ, B} G` are identified with `H_{Vᵢ}`
>   (`AlgebraicGeometry.Space.groupCompIso`), which turns the datum into one of the shape (1)–(4)
>   (`AlgebraicGeometry.Space.PrincipalHomogeneousSpaces.descentDatumOfBase`); the antecedent makes
>   it effective, and the descended principal homogeneous `H`-space read back in `G-Principal`
>   makes the original datum effective
>   (`PrincipalHomogeneousSpaces.isEffective_of_isEffective_descentDatumOfBase`).
>
> "Up to a replacement as in Stacks 03ZZ" is not needed: an object of `G-Principal` carries as total
> space an object of the slice over a representable presheaf of the set-sized big fppf site, so
> `G-Principal` is a genuine category and `p` a functor, as for Stacks 04US.

```lean
theorem isStackInGroupoids_of_descent (h : PrincipalHomogeneousSpaceDescent.{w} 𝒞 S hS) :
    Functor.IsStackInGroupoids.{w} (projection hB G) (BigFppfOver.topology 𝒞 S hS)
```

## Tag 04UR, a subsection

[Tag 04UR](https://stacks.math.columbia.edu/tag/04UR) in the Stacks Project.

**`AlgebraicGeometry.Space.FppfTorsors`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L145). The attribute's comment: “the objects of G-Torsors”.

> **Stacks 04UR.** An object of the category `G-Torsors`: an object `U` of the big fppf site
> of `S`, a morphism `b : U ⟶ B`, and an fppf torsor `X` over `U` under `G_U = U ×_{b, B} G`.

```lean
abbrev FppfTorsors
```

**`AlgebraicGeometry.Space.TorsorsFor.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L280). The attribute's comment: “the morphisms of G-Torsors”.

> A morphism `(U, b, X) ⟶ (U', b', X')` of torsors: a morphism `f : U ⟶ U'` over `B` together
> with an equivariant identification of `X` with `U ×_{f, U'} X'`.

```lean
structure Hom (T T' : TorsorsFor hB G P)
```

**`AlgebraicGeometry.Space.TorsorsFor.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L331). The attribute's comment: “the category G-Torsors”.

> The torsors under a group algebraic space `G` over `B` which are trivialized by a family
> satisfying `P` form a category: morphisms compose by composing `f` and the identification of the
> total spaces.

```lean
instance instCategory : Category (TorsorsFor hB G P)
```

**`AlgebraicGeometry.Space.TorsorsFor.isIso_of_isIso_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L402). The attribute's comment: “the fibre categories are groupoids”.

> A morphism of torsors whose morphism `f` of the big fppf site is an isomorphism is itself an
> isomorphism. Every morphism of a fibre category of the functor `p` to the site lies over an
> identity, so this says that the fibre category over `U` — the disjoint union over the morphisms
> `b : U ⟶ B` of the categories of torsors under `U ×_{b, B} G` trivialized by a family satisfying
> `P` — is a groupoid.

```lean
theorem isIso_of_isIso_base : IsIso φ
```

**`AlgebraicGeometry.Space.FppfTorsors.projection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/CategoryOfFppfTorsors.lean#L415). The attribute's comment: “the functor p to the site”.

> **Stacks 04UR.** The functor `p : G-Torsors ⥤ (Sch/S)_fppf` sending `(U, b, X)` to `U`,
> which is how `G-Torsors` is regarded as a category over the big fppf site of `S`.

```lean
abbrev projection : FppfTorsors hB G ⥤ BigFppfOver 𝒞 S hS
```

## Tag 04US, a lemma

[Tag 04US](https://stacks.math.columbia.edu/tag/04US) in the Stacks Project.

**`AlgebraicGeometry.Space.FppfTorsors.projection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfFppfTorsors.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfFppfTorsors.lean#L182). The attribute's comment: “condition (1): p is fibred in groupoids”.

> Condition (1) of Stacks 02ZI for the functor `p : G-Torsors ⥤ (Sch/S)_fppf` of Stacks 04UR:
> `p` is fibred in groupoids.

```lean
theorem projection_isFiberedInGroupoids : (projection hB G).IsFiberedInGroupoids
```

**`AlgebraicGeometry.Space.FppfTorsors.projection_isomIsSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfFppfTorsors.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/StackOfFppfTorsors.lean#L270). The attribute's comment: “condition (2): the Isom presheaves are sheaves”.

> Condition (2) of Stacks 02ZI for the functor `p : G-Torsors ⥤ (Sch/S)_fppf` of Stacks 04UR:
> for two objects `(U, b, X)` and `(U, b', X')` over the same object of the big fppf site of `S`,
> the presheaf `Isom(X, X')` is a sheaf.

```lean
theorem projection_isomIsSheaf
    {U : BigFppfOver 𝒞 S hS} (x y : FppfTorsors hB G)
    (hx : (projection hB G).obj x = U) (hy : (projection hB G).obj y = U)
    {I : Type w} (V : I → BigFppfOver 𝒞 S hS) (f : ∀ i, V i ⟶ U)
    (hf : Sieve.ofArrows V f ∈ BigFppfOver.topology 𝒞 S hS U)
    (Vij : I → I → BigFppfOver 𝒞 S hS)
    (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j)
    (hVij : ∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j))
    (xr : ∀ i, Functor.Restriction (projection hB G) (f i) x hx)
    (yr : ∀ i, Functor.Restriction (projection hB G) (f i) y hy)
    (xrij : ∀ i j, Functor.Restriction (projection hB G) (pr₁ i j ≫ f i) x hx)
    (yrij : ∀ i j, Functor.Restriction (projection hB G) (pr₁ i j ≫ f i) y hy) :
    Functor.IsomIsSheafFor (projection hB G) x y hx hy V f Vij pr₁ pr₂ hVij
      xr yr xrij yrij
```

**`AlgebraicGeometry.Space.FppfTorsors.hasEffectiveDescent_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean#L108). The attribute's comment: “condition (3): effectivity of descent, with nothing carried”.

> **Stacks 04US**, condition (3) of Stacks 026F for `p : G-Torsors ⥤ (Sch/S)_fppf`, with
> nothing carried: every descent datum relative to a covering sieve of the big fppf site of `S` is
> effective.
>
> This is `AlgebraicGeometry.Space.FppfTorsors.hasEffectiveDescent_projection_of_bootstrap` with
> both of its hypotheses discharged: Stacks 04S6 part (3) by
> `AlgebraicGeometry.Space.isBootstrapAlgebraicSpaceAlongFlatSurjection`, and condition (3) of
> Stacks 04UM for `𝒢/ℬ-Torsors` by
> `AlgebraicGeometry.Space.SheafTorsors.projection_hasEffectiveDescent`, whose two sheaf
> hypotheses hold because `B` and `G` are algebraic spaces.

```lean
theorem hasEffectiveDescent_projection (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    letI : (projection hB G).IsFibered :=
      (projection_isFiberedInGroupoids (hB := hB) (G := G)).isFibered
    Functor.HasEffectiveDescent (projection hB G) (BigFppfOver.topology 𝒞 S hS)
```

**`AlgebraicGeometry.Space.FppfTorsors.projection_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean#L126). The attribute's comment: “the three conditions of Stacks 026F together, with nothing carried”.

> **Stacks 04US**, with nothing carried: the projection
> `p : G-Torsors ⥤ (Sch/S)_fppf` of Stacks 04UR is a stack over the big fppf site of `S`, in the
> sense of Stacks 026F.
>
> Condition (1) is `AlgebraicGeometry.Space.FppfTorsors.projection_isFiberedInGroupoids`;
> condition (2) is `AlgebraicGeometry.Space.FppfTorsors.projection_isomIsSheaf`, read through
> `CategoryTheory.Functor.isMorSheaf_of_isomIsSheaf`; condition (3) is
> `AlgebraicGeometry.Space.FppfTorsors.hasEffectiveDescent_projection`.

```lean
theorem projection_isStack (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    Functor.IsStack (projection hB G) (BigFppfOver.topology 𝒞 S hS)
```

**`AlgebraicGeometry.Space.FppfTorsors.projection_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean#L146). The attribute's comment: “the stack in groupoids in the rendering of Stacks 02ZI, with nothing carried”.

> **Stacks 04US**, with nothing carried, in the rendering of Stacks 02ZI: the projection
> `p : G-Torsors ⥤ (Sch/S)_fppf` is a stack in groupoids over the big fppf site of `S`.
>
> This is `AlgebraicGeometry.Space.FppfTorsors.projection_isStack` read through the forward bridge
> of Stacks 02ZJ, `CategoryTheory.Functor.IsStack.isStackInGroupoids`.

```lean
theorem projection_isStackInGroupoids (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    Functor.IsStackInGroupoids.{w} (projection hB G) (BigFppfOver.topology 𝒞 S hS)
```

**`AlgebraicGeometry.Space.torsorProjection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean#L232). The attribute's comment: “condition (1) for the TorsorObj rendering, with nothing carried”.

> **Stacks 04US**, condition (1) of Stacks 02ZI for the second rendering of the category of
> fppf `G`-torsors: `AlgebraicGeometry.Space.torsorProjection` is fibred in groupoids.
>
> This is `AlgebraicGeometry.Space.FppfTorsors.projection_isFiberedInGroupoids` transported along
> `AlgebraicGeometry.Space.torsorObjBasedEquivalence` by Stacks 042G.

```lean
theorem torsorProjection_isFiberedInGroupoids :
    (torsorProjection hB G).IsFiberedInGroupoids
```

**`AlgebraicGeometry.Space.torsorProjection_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorStackUnconditional.lean#L244). The attribute's comment: “the stack property for the TorsorObj rendering, with nothing carried”.

> **Stacks 04US** in full, with nothing carried, for the second rendering of the category of
> fppf `G`-torsors: `AlgebraicGeometry.Space.torsorProjection` is a stack over the big fppf site
> of `S`.
>
> This is `AlgebraicGeometry.Space.FppfTorsors.projection_isStack` transported along
> `AlgebraicGeometry.Space.torsorObjBasedEquivalence` by Stacks 042W.

```lean
theorem torsorProjection_isStack :
    (torsorProjection hB G).IsStack (BigFppfOver.topology 𝒞 S hS)
```

## Tag 04UT, a lemma

[Tag 04UT](https://stacks.math.columbia.edu/tag/04UT) in the Stacks Project.

**`AlgebraicGeometry.Space.FppfTorsors.comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean#L167). The attribute's comment: “the comparison functor”.

> The comparison functor `G-Torsors ⥤ 𝒢/ℬ-Torsors` which associates to a triple `(U, b, X)`
> the triple `(U, b, 𝒳)` where `𝒳` is `X` viewed as a sheaf.

```lean
def comparison (hB : IsAlgebraicSpace 𝒞 S hS B) (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    FppfTorsors hB G ⥤ SheafTorsors G.obj
```

**`AlgebraicGeometry.Space.FppfTorsors.comparison_comp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean#L191). The attribute's comment: “the comparison functor lies over the site”.

> The comparison functor is a 1-morphism of categories over the big fppf site of `S`: it
> sends a triple `(U, b, X)` to a triple with the same base object `U` and a morphism to a
> morphism with the same morphism `f` of the site.

```lean
theorem comparison_comp_projection (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    comparison hB G ⋙ SheafTorsors.projection G.obj = projection hB G
```

**`AlgebraicGeometry.Space.FppfTorsors.instFaithfulComparison`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean#L199). The attribute's comment: “the comparison functor is faithful”.

> The comparison functor is faithful: a morphism of `G-Torsors` is determined by the
> morphism of `𝒢/ℬ-Torsors` it becomes.

```lean
instance instFaithfulComparison : (comparison hB G).Faithful
```

**`AlgebraicGeometry.Space.FppfTorsors.instFullComparison`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparison.lean#L206). The attribute's comment: “the comparison functor is full”.

> The comparison functor is full: a morphism of `𝒢/ℬ-Torsors` between torsors of algebraic
> spaces is already a morphism of `G-Torsors`.

```lean
instance instFullComparison : (comparison hB G).Full
```

**`AlgebraicGeometry.Space.FppfTorsors.isEquivalenceOverComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean#L203). The attribute's comment: “the hypothesis-carrying form, taking hdesc — effectivity of descent for G-Torsors, condition (3) of Stacks 02ZI in Stacks 04US. That hypothesis is PROVED, as `FppfTorsors.hasEffectiveDescent_projection`, and the form carrying nothing is `FppfTorsors.nonempty_isEquivalenceOver_comparison`”.

> If every descent datum of fppf torsors of algebraic spaces along a covering sieve of the big
> fppf site of `S` is effective (`hdesc`, condition (3) of Stacks 02ZI for
> `p : G-Torsors ⥤ (Sch/S)_fppf`), then the comparison functor `G-Torsors ⥤ 𝒢/ℬ-Torsors`, which
> sends a triple `(U, b, X)` to the triple `(U, b, 𝒳)` with `𝒳` the total space seen as a sheaf, is
> an equivalence of stacks in groupoids over the big fppf site of `S`: it has a quasi-inverse which
> is again a functor over the site, with vertical unit and counit.

```lean
noncomputable def isEquivalenceOverComparison (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB)
    (hdesc : letI : (projection hB G).IsFibered :=
        (projection_isFiberedInGroupoids (hB := hB) (G := G)).isFibered
      Functor.HasEffectiveDescent (projection hB G) (BigFppfOver.topology 𝒞 S hS)) :
    Functor.IsEquivalenceOver (projection hB G) (SheafTorsors.projection G.obj)
      (comparison hB G)
```

**`AlgebraicGeometry.Space.FppfTorsors.nonempty_isEquivalenceOver_comparison_of_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean#L220). The attribute's comment: “the hypothesis-carrying form of the criterion Stacks 046N, taking the two stack conditions Stacks 04US and Stacks 04UM as hsource and htarget. BOTH are proved — `FppfTorsors.projection_isStack` and `SheafTorsors.projection_isStackInGroupoids` — and the form carrying nothing is `FppfTorsors.nonempty_isEquivalenceOver_comparison`”.

> If both `p : G-Torsors ⥤ (Sch/S)_fppf` and `p : 𝒢/ℬ-Torsors ⥤ (Sch/S)_fppf` are stacks over
> the big fppf site of `S` (Stacks 04US and Stacks 04UM), then the comparison functor is an
> equivalence over that site.

```lean
theorem nonempty_isEquivalenceOver_comparison_of_isStack (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB)
    (hsource : (projection hB G).IsStack (BigFppfOver.topology 𝒞 S hS))
    (htarget : (SheafTorsors.projection G.obj).IsStack (BigFppfOver.topology 𝒞 S hS)) :
    Nonempty (Functor.IsEquivalenceOver (projection hB G) (SheafTorsors.projection G.obj)
      (comparison hB G))
```

**`AlgebraicGeometry.Space.FppfTorsors.isEquivalenceOverComparisonOfAlgebraic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean#L295). The attribute's comment: “the hypothesis-carrying form, taking halg — algebraicity of the total space of every 𝒢/ℬ-torsor sheaf, which `isAlgebraicSpace_total_of_isEquivalenceOver` shows the tag's conclusion in turn implies, so the two are equivalent. halg is PROVED, via `isBootstrapAlgebraicSpaceAlongFlatSurjection`, and the form carrying nothing is `FppfTorsors.nonempty_isEquivalenceOver_comparison`”.

> The comparison functor `G-Torsors ⥤ 𝒢/ℬ-Torsors` is an equivalence of stacks in groupoids
> over the big fppf site of `S` as soon as every torsor of sheaves has an algebraic space as total
> space.

```lean
noncomputable def isEquivalenceOverComparisonOfAlgebraic
    (hB : IsAlgebraicSpace 𝒞 S hS B) (G : GroupAlgebraicSpace 𝒞 S hS B hB)
    (halg : ∀ T : SheafTorsors G.obj, IsAlgebraicSpace 𝒞 S hS T.total.left) :
    Functor.IsEquivalenceOver (projection hB G) (SheafTorsors.projection G.obj)
      (comparison hB G)
```

**`AlgebraicGeometry.Space.FppfTorsors.nonempty_isEquivalenceOver_comparison_iff_isAlgebraicSpace_total`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonEquivalence.lean#L347). The attribute's comment: “the equivalence holds exactly when every 𝒢/ℬ-torsor sheaf has an algebraic space as total space; the tag asserts the left-hand side, which this does not prove unconditionally”.

> The comparison functor `G-Torsors ⥤ 𝒢/ℬ-Torsors` is an equivalence of stacks in groupoids
> over the big fppf site of `S` if and only if every `𝒢/ℬ`-torsor sheaf has an algebraic space as
> total space.

```lean
theorem nonempty_isEquivalenceOver_comparison_iff_isAlgebraicSpace_total
    (hB : IsAlgebraicSpace 𝒞 S hS B) (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    Nonempty (Functor.IsEquivalenceOver (projection hB G) (SheafTorsors.projection G.obj)
        (comparison hB G)) ↔
      ∀ T : SheafTorsors G.obj, IsAlgebraicSpace 𝒞 S hS T.total.left
```

**`AlgebraicGeometry.Space.FppfTorsors.isFibredOneMorphism_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonFibred.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonFibred.lean#L45). The attribute's comment: “the comparison functor is a 1-morphism of fibred categories”.

> The comparison functor `G-Torsors ⥤ 𝒢/ℬ-Torsors` is a 1-morphism of fibred categories over
> the big fppf site of `S`: it lies over the site and preserves strongly cartesian morphisms.

```lean
theorem isFibredOneMorphism_comparison (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    Functor.IsFibredOneMorphism (projection hB G) (SheafTorsors.projection G.obj)
      (comparison hB G)
```

**`AlgebraicGeometry.Space.FppfTorsors.nonempty_isEquivalenceOver_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonUnconditional.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/TorsorComparisonUnconditional.lean#L67). The attribute's comment: “the equivalence of stacks in groupoids, with nothing carried”.

> **Stacks 04UT**, with nothing carried, and with it the `𝒢/ℬ-Torsors` leg of **Stacks
> 0CQJ**: the comparison functor `G-Torsors ⥤ 𝒢/ℬ-Torsors` is an equivalence of stacks in
> groupoids over the big fppf site of `S`.
>
> The hypothesis every earlier rendering carried is the object half of Stacks 04U1, equivalently
> Stacks 04S6 part (3), which is now the theorem
> `AlgebraicGeometry.Space.isBootstrapAlgebraicSpaceAlongFlatSurjection`.

```lean
theorem nonempty_isEquivalenceOver_comparison (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    Nonempty (Functor.IsEquivalenceOver (projection hB G) (SheafTorsors.projection G.obj)
      (comparison hB G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.14, Tag 036Z](https://stacks.math.columbia.edu/tag/036Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
