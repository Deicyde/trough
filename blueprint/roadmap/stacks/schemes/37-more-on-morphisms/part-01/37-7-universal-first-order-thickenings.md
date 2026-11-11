---
declaration: section
origin: cited
lean: Stacks.Thickenings.nonempty_universalFirstOrderThickening, Stacks.Thickenings.universalFirstOrderThickening, Stacks.Thickenings.universalConormalSheaf, Stacks.Thickenings.universalThickeningIsoFirstOrderNeighbourhood, Stacks.Thickenings.immersionConormalSheafIsoUniversalConormalSheaf, Stacks.Thickenings.formallyUnramified_of_isImmersion, Stacks.Thickenings.isUniversalFirstOrderThickening_nthOrderInclusion_one, Stacks.Thickenings.UniversalFirstOrderThickening.formallyUnramified_toBase
statement: formalized
proof: formalized
---

# 37.7 Universal first order thickenings

Section 37.7 of the Stacks Project, [Tag 04F2](https://stacks.math.columbia.edu/tag/04F2). 12 tags here are carried by 44 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04F3, a lemma

[Tag 04F3](https://stacks.math.columbia.edu/tag/04F3) in the Stacks Project.

**`Stacks.Thickenings.nonempty_universalFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Existence/Gluing.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Existence/Gluing.lean#L494).

> **Stacks Project, Tag 04F3.** A formally unramified morphism of schemes admits a universal
> first-order thickening. It is constructed by gluing the thickenings of the charts of an affine
> open cover of `Z` subordinate to an affine open cover of `X`; the affine charts come from the
> algebraic universal first-order thickening
> (`Algebra.FormallyUnramified.universalFirstOrderThickening`, Tag 04EB).

```lean
theorem nonempty_universalFirstOrderThickening {Z X : Scheme.{u}} (h : Z ⟶ X)
    [FormallyUnramified h] : Nonempty (UniversalFirstOrderThickening h)
```

**`Stacks.Thickenings.universalFirstOrderThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Existence/Gluing.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Existence/Gluing.lean#L542).

> **Stacks Project, Tag 04F3.** *The* universal first-order thickening of a formally
> unramified morphism `h : Z ⟶ X`, chosen by
> `Stacks.Thickenings.nonempty_universalFirstOrderThickening`.
>
> The universal property is part of the data, as the field
> `Stacks.Thickenings.UniversalFirstOrderThickening.isUniversal`; it is spelled out in
> `Stacks.Thickenings.universalFirstOrderThickening_isUniversal` and its consequences below.
> Nothing beyond that property should be used: by
> `Stacks.Thickenings.UniversalFirstOrderThickening.canonicalIso` the choice is unique up to
> unique isomorphism, which is why the ambient scheme is left opaque here rather than exposed as
> the glued scheme.

```lean
noncomputable def universalFirstOrderThickening {Z X : Scheme.{u}} (h : Z ⟶ X)
    [FormallyUnramified h] : UniversalFirstOrderThickening h
```

## Tag 04F4, a definition

[Tag 04F4](https://stacks.math.columbia.edu/tag/04F4) in the Stacks Project.

**`Stacks.Thickenings.universalConormalSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean#L144). The attribute's comment: “part (2): conormal sheaf”.

> **Stacks Project, Tag 04F4, part (2).** The conormal sheaf `𝒞_{Z/X}` of a formally
> unramified morphism `h : Z ⟶ X`: the conormal sheaf, in the sense of
> `Stacks.Thickenings.immersionConormalSheaf` ([Stacks Project, Tag 01R2]), of the inclusion of
> `Z` into the universal first-order thickening of `Z` over `X` chosen by
> `Stacks.Thickenings.universalFirstOrderThickening`.
>
> The inclusion is a closed immersion, hence an immersion, by
> `Stacks.Thickenings.UniversalFirstOrderThickening.isClosedImmersion_inclusion`.

```lean
noncomputable abbrev universalConormalSheaf {Z X : Scheme.{u}} (h : Z ⟶ X)
    [FormallyUnramified h] :
    SheafOfModules.{u} (structureSheafRing Z.toLocallyRingedSpace.toRingedSpace)
```

Declarations registered for the tag:

- [`Stacks.Thickenings.universalFirstOrderThickening`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Existence/Gluing.lean#L542), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean#L132) (StacksFrontier): “part (1): universal first-order thickening”.

## Tag 04F5, a lemma

[Tag 04F5](https://stacks.math.columbia.edu/tag/04F5) in the Stacks Project.

**`Stacks.Thickenings.universalThickeningIsoFirstOrderNeighbourhood`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean#L119). The attribute's comment: “part (2): the chosen universal first-order thickening is the first-order infinitesimal neighbourhood”.

> The ambient scheme of the universal first-order thickening of an immersion `i : Z ⟶ X` chosen
> by `Stacks.Thickenings.universalFirstOrderThickening` is isomorphic to the first-order
> infinitesimal neighbourhood of `Z` in `X` of [Stacks Project, Tag 04EY].
>
> The isomorphism is the canonical one between two universal first-order thickenings of the same
> morphism, `Stacks.Thickenings.UniversalFirstOrderThickening.canonicalIso`. It is the unique
> isomorphism of thickenings of `Z` over `X`, by
> `Stacks.Thickenings.UniversalFirstOrderThickening.existsUnique_canonicalMap`.

```lean
def universalThickeningIsoFirstOrderNeighbourhood :
    (universalFirstOrderThickening i).ambient ≅ firstOrderInfinitesimalNeighbourhood i
```

**`Stacks.Thickenings.immersionConormalSheafIsoUniversalConormalSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean#L201). The attribute's comment: “part (3): the two conormal sheaves agree”.

> For an immersion `i : Z ⟶ X`, the conormal sheaf of `i` in the sense of
> [Stacks Project, Tag 01R2], `Stacks.Thickenings.immersionConormalSheaf i`, agrees with the
> conormal sheaf of `i` in the sense of [Stacks Project, Tag 04F4],
> `Stacks.Thickenings.universalConormalSheaf i`, built from the universal first-order thickening
> chosen by `Stacks.Thickenings.universalFirstOrderThickening`.
>
> It is the composite of the comparison `Stacks.Thickenings.infinitesimalConormalTransitivityMap`
> of [Stacks Project, Tag 04F0], `Stacks.Immersion.conormalSheafSelfIso` for the inclusion
> `Z ⟶ Z₁`, and `Stacks.Thickenings.universalConormalSheafIsoFirstOrderNeighbourhood`.

```lean
def immersionConormalSheafIsoUniversalConormalSheaf :
    immersionConormalSheaf i ≅ universalConormalSheaf i
```

Declarations registered for the tag:

- [`Stacks.Thickenings.formallyUnramified_of_isImmersion`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/InfinitesimalUniversal.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean#L98) (StacksFrontier): “part (1): an immersion of schemes is formally unramified”.
- [`Stacks.Thickenings.isUniversalFirstOrderThickening_nthOrderInclusion_one`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/InfinitesimalUniversal.lean#L59), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/ImmersionConormalIdentification.lean#L103) (StacksFrontier): “part (2): the first-order infinitesimal neighbourhood has the universal property of a first-order thickening over the base”.

## Tag 04F6, a lemma

[Tag 04F6](https://stacks.math.columbia.edu/tag/04F6) in the Stacks Project.

**`Stacks.Thickenings.UniversalFirstOrderThickening.formallyUnramified_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean#L160).

> **Stacks Project, Tag 04F6.** The ambient scheme of a universal first-order thickening of a
> formally unramified morphism `h : Z ⟶ X` is formally unramified over `X`.
>
> The thickening produced by the gluing construction of [Stacks Project, Tag 04F3] has this
> property, by
> `Stacks.Thickenings.exists_universalFirstOrderThickening_formallyUnramified_toBase`, and any
> other universal first-order thickening of `h` is isomorphic to it over `X` by
> `Stacks.Thickenings.UniversalFirstOrderThickening.canonicalIso`.

```lean
theorem UniversalFirstOrderThickening.formallyUnramified_toBase {Z X : Scheme.{u}} {h : Z ⟶ X}
    [FormallyUnramified h] (t : UniversalFirstOrderThickening h) :
    FormallyUnramified t.toBase
```

## Tag 04F7, a lemma

[Tag 04F7](https://stacks.math.columbia.edu/tag/04F7) in the Stacks Project.

**`Stacks.Thickenings.universalConormalSheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/ConormalSheaf.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/ConormalSheaf.lean#L291). The attribute's comment: “the induced morphism of conormal sheaves”.

> **Stacks 04F7, the conormal half.** Let `h : Z ⟶ X` and `h' : W ⟶ Y` be formally unramified,
> let `Z ⊂ Z'` and `W ⊂ W'` be universal first-order thickenings of `h` and of `h'`, and let
> `h ≫ g = f ≫ h'` be a commutative square. The canonical morphism `(f, f')` of thickenings of
> `Stacks.Thickenings.universalFirstOrderThickeningMap` induces a morphism of conormal sheaves
>
> `f^* 𝒞_{W/Y} ⟶ 𝒞_{Z/X}`.
>
> It is the map of [Stacks Project, Tag 01R4] applied to the square
> `(Z ⊂ Z') → (W ⊂ W')`, namely `Stacks.ClosedImmersion.conormalSheafMap`, which for the
> inclusions of thickenings needs no reduction of immersions to closed immersions and no quotient
> by the square of the defining ideal. Its characterising property is
> `Stacks.ClosedImmersion.conormalSheafMap_comp_pullback_ι`.

```lean
noncomputable def universalConormalSheafMap
    (tZ : UniversalFirstOrderThickening h) (tW : UniversalFirstOrderThickening h')
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h') :
    (modulePullback f.toLRSHom.toShHom).obj (schemeConormalSheaf tW.inclusion) ⟶
      schemeConormalSheaf tZ.inclusion
```

**`Stacks.Thickenings.UniversalFirstOrderThickening.existsUnique_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean#L152). The attribute's comment: “unique existence of the canonical morphism of thickenings”.

> There is a unique morphism between the ambient schemes of two universal first-order
> thickenings which restricts to `f` on the closed subschemes and is compatible with the
> structure morphisms over `g`. This is the unique-existence statement behind the canonical
> morphism of Tag 04F7, obtained by applying the universal property of `tW` to the first-order
> thickening `tZ.inclusion`.

```lean
theorem existsUnique_map (tZ : UniversalFirstOrderThickening h)
    (tW : UniversalFirstOrderThickening h')
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h') :
    ∃! k : tZ.ambient ⟶ tW.ambient,
      (tZ.inclusion ≫ k = f ≫ tW.inclusion) ∧ (k ≫ tW.toBase = tZ.toBase ≫ g)
```

**`Stacks.Thickenings.universalFirstOrderThickeningMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean#L169). The attribute's comment: “the canonical morphism of thickenings”.

> The canonical morphism between the ambient schemes of two universal first-order thickenings
> associated to a commutative square. It is selected by the unique lifting property of the target
> thickening.

```lean
noncomputable def universalFirstOrderThickeningMap
    (tZ : UniversalFirstOrderThickening h) (tW : UniversalFirstOrderThickening h')
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h') :
    tZ.ambient ⟶ tW.ambient
```

**`Stacks.Thickenings.universalFirstOrderThickeningMap_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean#L177). The attribute's comment: “compatibility with the inclusions”.

> The canonical morphism restricts to `f` on the closed subscheme.

```lean
theorem universalFirstOrderThickeningMap_inclusion
    (tZ : UniversalFirstOrderThickening h) (tW : UniversalFirstOrderThickening h')
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h') :
    tZ.inclusion ≫ universalFirstOrderThickeningMap tZ tW f g comm = f ≫ tW.inclusion
```

**`Stacks.Thickenings.universalFirstOrderThickeningMap_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean#L185). The attribute's comment: “compatibility with the base”.

> The canonical morphism is a morphism over `Y`.

```lean
theorem universalFirstOrderThickeningMap_toBase
    (tZ : UniversalFirstOrderThickening h) (tW : UniversalFirstOrderThickening h')
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h') :
    universalFirstOrderThickeningMap tZ tW f g comm ≫ tW.toBase = tZ.toBase ≫ g
```

**`Stacks.Thickenings.universalFirstOrderThickeningMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Universal.lean#L194). The attribute's comment: “uniqueness of the canonical morphism”.

> The canonical morphism is the unique extension of `f` over `Y`: any morphism of the ambient
> schemes restricting to `f` and compatible with the structure morphisms over `g` equals it.

```lean
theorem universalFirstOrderThickeningMap_unique
    (tZ : UniversalFirstOrderThickening h) (tW : UniversalFirstOrderThickening h')
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h')
    (k : tZ.ambient ⟶ tW.ambient)
    (hk₁ : tZ.inclusion ≫ k = f ≫ tW.inclusion)
    (hk₂ : k ≫ tW.toBase = tZ.toBase ≫ g) :
    k = universalFirstOrderThickeningMap tZ tW f g comm
```

**`Stacks.Thickenings.universalConormalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormal.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormal.lean#L208). The attribute's comment: “the induced morphism of conormal modules, on affine ambient thickenings”.

> **The map of conormal modules induced by the canonical morphism of universal first-order
> thickenings.** For universal first-order thickenings `tZ` of `h : Z ⟶ X` and `tW` of
> `h' : W ⟶ Y` with affine ambient schemes, and a commutative square `h ≫ g = f ≫ h'`, the
> canonical morphism `tZ.ambient ⟶ tW.ambient` of
> `Stacks.Thickenings.universalFirstOrderThickeningMap` carries the conormal module of `tW` into
> the conormal module of `tZ`, linearly over `Γ(W, ⊤)` acting through `f`.
>
> This is the affine, module-level avatar of the morphism of conormal sheaves
> `f^*𝒞_{W/Y} → 𝒞_{Z/X}` asserted by [Stacks Project, Tag 04F7]; it is not that morphism, which
> lives on all of `Z`.

```lean
noncomputable def universalConormalMap (tZ : UniversalFirstOrderThickening h)
    (tW : UniversalFirstOrderThickening h') [IsAffine tZ.ambient] [IsAffine tW.ambient]
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h') :
    letI := Smooth.thickeningKerModule tW.isUniversal.isFirstOrderThickening
    letI := conormalModuleAlong tZ.isUniversal.isFirstOrderThickening f
    RingHom.ker tW.inclusion.appTop.hom →ₗ[Γ(W, (⊤ : W.Opens))]
      RingHom.ker tZ.inclusion.appTop.hom
```

**`Stacks.Thickenings.universalConormalMap_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormal.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormal.lean#L227). The attribute's comment: “affine characterization of the induced morphism of conormal modules”.

> **The affine characterization of the induced map of conormal modules.** On underlying sections
> the map of `Stacks.Thickenings.universalConormalMap` is the ring map of the canonical morphism
> `tZ.ambient ⟶ tW.ambient` of universal first-order thickenings.
>
> This is the characterizing property of [Stacks Project, Tag 01R4] for the square
> `(Z ⊂ Z') → (W ⊂ W')`: a section of the defining ideal of `W` in `W'` goes to its image under
> the ambient ring map. For a first-order thickening the defining ideal is already its own conormal
> module, so there is no quotient by the square of the ideal.

```lean
theorem universalConormalMap_apply (tZ : UniversalFirstOrderThickening h)
    (tW : UniversalFirstOrderThickening h') [IsAffine tZ.ambient] [IsAffine tW.ambient]
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h')
    (x : RingHom.ker tW.inclusion.appTop.hom) :
    ((universalConormalMap tZ tW f g comm x : RingHom.ker tZ.inclusion.appTop.hom) :
        Γ(tZ.ambient, (⊤ : tZ.ambient.Opens)))
      = (universalFirstOrderThickeningMap tZ tW f g comm).appTop.hom
          (x : Γ(tW.ambient, (⊤ : tW.ambient.Opens)))
```

**`Stacks.Thickenings.isInducedConormalSheafMap_universalImmersionConormalSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalGenerators.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalGenerators.lean#L446). The attribute's comment: “affine characterization of the induced conormal-sheaf morphism”.

> **The affine characterization of the induced morphism of conormal sheaves.** Let
> `h : Z ⟶ X` and `h' : W ⟶ Y` be formally unramified, let `Z ⊂ Z'` and `W ⊂ W'` be universal
> first-order thickenings of `h` and of `h'`, and let `h ≫ g = f ≫ h'` be a commutative square. The
> morphism of conormal sheaves `f^* 𝒞_{W/Y} ⟶ 𝒞_{Z/X}` induced by the canonical morphism `(f, f')`
> of thickenings is *the* map of [Stacks Project, Tag 01R4] for the square `(Z ⊂ Z') → (W ⊂ W')`:
> on a compatible pair of affine opens `V ⊆ W'` and `U ⊆ Z'` cut out by ideals `J` and `I`, it
> carries the class of `a : J` in `J/J²` to the class in `I/I²` of the image of `a` under the ring
> map of `f'`.

```lean
theorem isInducedConormalSheafMap_universalImmersionConormalSheafMap
    (tZ : UniversalFirstOrderThickening h) (tW : UniversalFirstOrderThickening h')
    (f : Z ⟶ W) (g : X ⟶ Y) (comm : h ≫ g = f ≫ h') :
    IsInducedConormalSheafMap tZ.inclusion tW.inclusion f
      (universalFirstOrderThickeningMap tZ tW f g comm)
      (universalFirstOrderThickeningMap_inclusion tZ tW f g comm)
      (universalImmersionConormalSheafMap tZ tW f g comm)
```

## Tag 04F8, a lemma

[Tag 04F8](https://stacks.math.columbia.edu/tag/04F8) in the Stacks Project.

**`Stacks.Thickenings.formallyUnramified_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean#L116). The attribute's comment: “part (1): the base change of a formally unramified morphism”.

> In a cartesian square of schemes, the base change of a formally unramified morphism is
> formally unramified.

```lean
theorem formallyUnramified_of_isPullback (sq : IsPullback h f g h')
    [FormallyUnramified h'] : FormallyUnramified h
```

**`Stacks.Thickenings.isUniversal_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean#L180). The attribute's comment: “part (2): X ×\_Y W' is the universal first-order thickening of Z over X”.

> **The fibre product `X ×_Y W'` is a universal first-order thickening of `Z = X ×_Y W` over
> `X`.**

```lean
theorem isUniversal_baseChange (sq : IsPullback h f g h')
    (t : UniversalFirstOrderThickening h') :
    IsUniversalFirstOrderThickening h (baseChangeInclusion sq t) (baseChangeToBase g t)
```

**`Stacks.Thickenings.epi_immersionConormalSheafMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean#L308). The attribute's comment: “part (3): the canonical map f^* 𝒞\_\{W/Y} ⟶ 𝒞\_\{Z/X} is surjective”. References: EGA IV (17.13.1), “more general”.

> For a cartesian square of schemes, with no flatness hypothesis on `g`, the canonical map of
> conormal sheaves `f^* 𝒞_{W/Y} ⟶ 𝒞_{Z/X}` of [Stacks Project, Tag 01R4] between the inclusions of
> universal first-order thickenings is surjective.

```lean
theorem epi_immersionConormalSheafMap_of_isPullback (sq : IsPullback h f g h')
    (t : UniversalFirstOrderThickening h') :
    Epi (Stacks.Immersion.immersionConormalSheafMap tZ.inclusion t.inclusion f
      (universalFirstOrderThickeningMap tZ t f g sq.w)
      (Stacks.Immersion.toShHom_square
        (universalFirstOrderThickeningMap_inclusion tZ t f g sq.w)))
```

**`Stacks.Thickenings.epi_universalConormalSheafMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean#L321). The attribute's comment: “part (3): the canonical map of conormal sheaves of Tag 04F7 is surjective”.

> For a cartesian square of schemes, the morphism of conormal sheaves
> `Stacks.Thickenings.universalConormalSheafMap` of [Stacks Project, Tag 04F7], induced by the
> canonical morphism of universal first-order thickenings, is surjective.

```lean
theorem epi_universalConormalSheafMap_of_isPullback (sq : IsPullback h f g h')
    (t : UniversalFirstOrderThickening h') :
    Epi (universalConormalSheafMap tZ t f g sq.w)
```

## Tag 04F9, a lemma

[Tag 04F9](https://stacks.math.columbia.edu/tag/04F9) in the Stacks Project.

**`Stacks.Thickenings.flat_universalFirstOrderThickeningMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean#L277). The attribute's comment: “the morphism Z' ⟶ W' of universal first-order thickenings is flat”.

> Let
> ```
> Z --h--→ X
> |        |
> f        g
> ↓        ↓
> W --h'-→ Y
> ```
> be a cartesian square of schemes with `g` flat, let `Z ⊂ Z'` be a universal first-order
> thickening of `h` over `X` and `W ⊂ W'` one of `h'` over `Y`. Then the canonical morphism
> `Z' ⟶ W'` of [Stacks Project, Tag 04F7] is flat.

```lean
theorem flat_universalFirstOrderThickeningMap (sq : IsPullback h f g h')
    (t : UniversalFirstOrderThickening h') [Flat g] :
    Flat (universalFirstOrderThickeningMap tZ t f g sq.w)
```

**`Stacks.Thickenings.isIso_immersionConormalSheafMap_of_isPullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean#L336). The attribute's comment: “the induced map f^* 𝒞\_\{W/Y} ⟶ 𝒞\_\{Z/X} of conormal sheaves is an isomorphism”.

> For a cartesian square of schemes with `g` flat, the canonical map of conormal sheaves
> `f^* 𝒞_{W/Y} ⟶ 𝒞_{Z/X}` of [Stacks Project, Tag 01R4] between the inclusions of the two
> universal first-order thickenings is an isomorphism.

```lean
theorem isIso_immersionConormalSheafMap_of_isPullback_of_flat (sq : IsPullback h f g h')
    (t : UniversalFirstOrderThickening h') [Flat g] :
    IsIso (Stacks.Immersion.immersionConormalSheafMap tZ.inclusion t.inclusion f
      (universalFirstOrderThickeningMap tZ t f g sq.w)
      (Stacks.Immersion.toShHom_square
        (universalFirstOrderThickeningMap_inclusion tZ t f g sq.w)))
```

**`Stacks.Thickenings.isIso_universalConormalSheafMap_of_isPullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/FlatBaseChange.lean#L350). The attribute's comment: “the induced map of conormal sheaves of Tag 04F7 is an isomorphism”.

> For a cartesian square of schemes with `g` flat, the morphism of conormal sheaves
> `Stacks.Thickenings.universalConormalSheafMap` of [Stacks Project, Tag 04F7], induced by the
> canonical morphism of universal first-order thickenings, is an isomorphism.

```lean
theorem isIso_universalConormalSheafMap_of_isPullback_of_flat (sq : IsPullback h f g h')
    (t : UniversalFirstOrderThickening h') [Flat g] :
    IsIso (universalConormalSheafMap tZ t f g sq.w)
```

## Tag 04FA, a lemma

[Tag 04FA](https://stacks.math.columbia.edu/tag/04FA) in the Stacks Project.

**`AlgebraicGeometry.universalConormalSheafRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/LocalCompleteIntersection/UnramifiedConormal.lean#L112). The attribute's comment: “restriction of the conormal sheaf to an open, as an isomorphism of sheaves of modules on that open”.

> **Stacks 04FA, the restriction of the conormal sheaf, as an isomorphism.** For opens `U` of
> the source and `V` of the target of a formally unramified morphism `f : X ⟶ S` with
> `f (U) ⊆ V`, the restriction to `U` of the conormal sheaf of `f` is the conormal sheaf of the
> restriction of `f` to a morphism `U ⟶ V`.

```lean
noncomputable def universalConormalSheafRestrictIso {X S : Scheme.{u}} (f : X ⟶ S)
    [FormallyUnramified f] {V : S.Opens} {U : X.Opens} (hUV : U ≤ f ⁻¹ᵁ V)
    [FormallyUnramified (f.resLE V U hUV)] :
    (Scheme.Modules.restrictFunctor U.ι).obj (universalConormalSheaf f) ≅
      universalConormalSheaf (f.resLE V U hUV)
```

**`Stacks.Thickenings.isUniversalFirstOrderThickening_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Existence/Affine.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Existence/Affine.lean#L581). The attribute's comment: “the universal first-order thickening of an open is the corresponding open”.

> **Stacks Project, Tag 04FA, the second assertion.** Let `i : Z ⟶ Z'` with structure morphism
> `p : Z' ⟶ X` be a universal first-order thickening of `h : Z ⟶ X` over `X`. Let `U ⊆ X` and
> `V ⊆ Z` be opens with `h(V) ⊆ U`, and let `W ⊆ Z'` be an open with `Z ∩ W = V` and `p(W) ⊆ U`.
> Then the restrictions `i.resLE W V : V ⟶ W` and `p.resLE U W : W ⟶ U` are a universal
> first-order thickening of `h|_V : V ⟶ U` over `U`.
>
> That `V ⟶ W` is a first-order thickening is the statement that the restriction of a first-order
> thickening to an open subscheme of the ambient scheme is again one. The lifting property is the
> lifting property of `Z'` followed by the observation that the resulting lift `T' ⟶ Z'` factors
> through the open `W`: the points of `T'` are the points of `T`, which land in `V`, hence in
> `W`.

```lean
theorem isUniversalFirstOrderThickening_resLE {Z' : Scheme.{u}} {i : Z ⟶ Z'} {p : Z' ⟶ X}
    (hi : IsUniversalFirstOrderThickening h i p) {U : X.Opens} {V : Z.Opens} {W : Z'.Opens}
    (hWV : i ⁻¹ᵁ W = V) (hWU : W ≤ p ⁻¹ᵁ U) (hVU : V ≤ h ⁻¹ᵁ U) :
    IsUniversalFirstOrderThickening (h.resLE U V hVU) (i.resLE W V hWV.ge) (p.resLE U W hWU)
```

**`Stacks.Thickenings.formallyUnramified_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/OpenRestriction.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/OpenRestriction.lean#L94). The attribute's comment: “formal unramifiedness of the restriction”.

> **Formal unramifiedness restricts to opens.** If `h : Z ⟶ X` is formally unramified and
> `V ⊆ Z`, `U ⊆ X` are opens with `h(V) ⊆ U`, then `h|_V : V ⟶ U` is formally unramified.

```lean
theorem formallyUnramified_resLE (h : Z ⟶ X) [FormallyUnramified h] {U : X.Opens} {V : Z.Opens}
    (hVU : V ≤ h ⁻¹ᵁ U) : FormallyUnramified (h.resLE U V hVU)
```

**`Stacks.Thickenings.isIso_universalImmersionConormalSheafMap_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/OpenRestriction.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/OpenRestriction.lean#L240). The attribute's comment: “restriction of the conormal sheaf”.

> **`𝒞_{Z/X}|_V = 𝒞_{V/U}`.** For universal first-order thickenings `Z ⊂ Z'` of `h : Z ⟶ X`
> and `V ⊂ V''` of `h|_V : V ⟶ U`, the canonical morphism of conormal sheaves
> `(ι_V)^* 𝒞_{Z/X} ⟶ 𝒞_{V/U}` of [Stacks Project, Tag 04F7] is an isomorphism.

```lean
theorem isIso_universalImmersionConormalSheafMap_resLE
    (t : UniversalFirstOrderThickening h) {U : X.Opens} {V : Z.Opens} (hVU : V ≤ h ⁻¹ᵁ U)
    (tV : UniversalFirstOrderThickening (h.resLE U V hVU)) :
    IsIso (universalImmersionConormalSheafMap tV t V.ι U.ι (Scheme.Hom.resLE_comp_ι h hVU))
```

**`Stacks.Thickenings.isIso_universalConormalSheafMap_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/OpenRestriction.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/OpenRestriction.lean#L255). The attribute's comment: “restriction of the conormal sheaf, at the chosen thickenings”.

> **`𝒞_{Z/X}|_V = 𝒞_{V/U}` at the chosen thickenings.** For a formally unramified
> `h : Z ⟶ X` and opens `V ⊆ Z`, `U ⊆ X` with `h(V) ⊆ U`, the canonical morphism
> `(ι_V)^* 𝒞_{Z/X} ⟶ 𝒞_{V/U}` between the conormal sheaves
> `Stacks.Thickenings.universalConormalSheaf h` and
> `Stacks.Thickenings.universalConormalSheaf (h|_V)` is an isomorphism.

```lean
theorem isIso_universalConormalSheafMap_resLE (h : Z ⟶ X) [FormallyUnramified h] {U : X.Opens}
    {V : Z.Opens} (hVU : V ≤ h ⁻¹ᵁ U) :
    letI : FormallyUnramified (h.resLE U V hVU) := formallyUnramified_resLE h hVU
    IsIso (universalImmersionConormalSheafMap
      (universalFirstOrderThickening (h.resLE U V hVU)) (universalFirstOrderThickening h)
      V.ι U.ι (Scheme.Hom.resLE_comp_ι h hVU))
```

## Tag 04FB, a lemma

[Tag 04FB](https://stacks.math.columbia.edu/tag/04FB) in the Stacks Project.

**`Stacks.Thickenings.isIso_thickeningRelativeDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalDifferentials.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalDifferentials.lean#L573). The attribute's comment: “the restriction along the inclusion of a universal first-order thickening of the canonical map on relative differentials is an isomorphism; formal unramifiedness of `h` is not assumed, a universal first-order thickening being given”.

> Let `h : Z ⟶ X` be a morphism of schemes over `S` and let `i : Z ⟶ Z'` with structure
> morphism `h' : Z' ⟶ X` be a universal first-order thickening of `Z` over `X`. The canonical map
> `c_{h'} : (h')^* Ω_{X/S} ⟶ Ω_{Z'/S}` induces an isomorphism `h^* Ω_{X/S} ⟶ Ω_{Z'/S} ⊗ 𝒪_Z`,
> namely its restriction along `i`.
>
> Formal unramifiedness of `h`, a hypothesis of the source, is not needed here: it is what makes a
> universal first-order thickening exist, and one is given.

```lean
public theorem isIso_thickeningRelativeDifferentialsMap {Z X Z' S : Scheme.{u}} {h : Z ⟶ X}
    {i : Z ⟶ Z'} {h' : Z' ⟶ X} (hi : IsUniversalFirstOrderThickening h i h') (p : X ⟶ S) :
    IsIso (Scheme.Hom.thickeningRelativeDifferentialsMap i h' p)
```

## Tag 04FC, a lemma

[Tag 04FC](https://stacks.math.columbia.edu/tag/04FC) in the Stacks Project.

**`Stacks.ConormalSequenceRight.epi_relativeDifferentialsMap_of_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramified.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramified.lean#L120). The attribute's comment: “exactness at the right term”.

> **[Stacks, Tag 04FC], exactness at the right term.** For a formally unramified morphism
> `h : Z ⟶ X` of schemes over `S`, the canonical map `h^*Ω_{X/S} ⟶ Ω_{Z/S}` of
> [Stacks, Tag 01UV] is an epimorphism, so the differential sequence of `h` ends in zero.
>
> A formally unramified morphism has `Ω_{Z/X} = 0` by [Stacks, Tag 02G4], so this is
> `epi_relativeDifferentialsMap_of_isZero_relativeDifferentials`.

```lean
theorem epi_relativeDifferentialsMap_of_formallyUnramified (h : Z ⟶ X) [FormallyUnramified h]
    (p : X ⟶ S) :
    Epi (Scheme.Hom.relativeDifferentialsMap h p (h ≫ p) (𝟙 S) (by simp))
```

**`Stacks.ConormalSequenceRight.universalConormalDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramifiedConormal.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramifiedConormal.lean#L232). The attribute's comment: “the first arrow induced by the universal derivation”.

> **[Stacks, Tag 04FC], the first arrow.** For a formally unramified morphism `h : Z ⟶ X` of
> schemes over `S`, the canonical morphism `𝒞_{Z/X} ⟶ h^*Ω_{X/S}` induced by the universal
> derivation `d_{Z'/S}` on the ambient scheme of the universal first-order thickening of `Z` over
> `X`.
>
> It is the first arrow of [Stacks, Tag 01UZ] for the closed immersion `ι : Z ⟶ Z'` over
> `h' ≫ p`, whose source is the conormal sheaf of `ι`, that is `𝒞_{Z/X}` by the definition
> [Stacks, Tag 04F4] makes, and whose target is moved onto `h^*Ω_{X/S}` by [Stacks, Tag 04FB].

```lean
noncomputable def universalConormalDifferential :
    Stacks.ConormalSequenceUnramifiedPair.conormalSheafModules h ⟶
      (Scheme.Modules.pullback h).obj (Scheme.Hom.relativeDifferentials p)
```

**`Stacks.ConormalSequenceRight.universalConormalShortComplex_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramifiedConormal.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramifiedConormal.lean#L284). The attribute's comment: “exactness at the middle term”. References: SGA 7 XI (1.3), “partial”.

> **[Stacks, Tag 04FC], exactness at the middle term.** For a formally unramified morphism
> `h : Z ⟶ X` of schemes over `S` the sequence `𝒞_{Z/X} ⟶ h^*Ω_{X/S} ⟶ Ω_{Z/S}` is exact at
> `h^*Ω_{X/S}`.
>
> This is [Stacks, Tag 01UZ] for the closed immersion of `Z` into the ambient scheme of its
> universal first-order thickening over `X`, transported along the identifications of
> `Stacks.ConormalSequenceRight.universalConormalShortComplexIso`.

```lean
theorem universalConormalShortComplex_exact :
    (universalConormalShortComplex h p).Exact
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.relativeDifferentialsMap`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Functoriality.lean#L122), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramified.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/FormallyUnramified.lean#L134) (StacksFrontier): “the second arrow”.

## Tag 067V, a lemma

[Tag 067V](https://stacks.math.columbia.edu/tag/067V) in the Stacks Project.

**`Stacks.ConormalSequenceUnramifiedPair.universalConormalTransitivityMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairConormalSequence.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairConormalSequence.lean#L153). The attribute's comment: “the first arrow”.

> **[Stacks, Tag 067V], the first arrow.** For formally unramified `i : Z ⟶ X` and
> `j : Z ⟶ Y` in a commutative triangle `i ≫ p = j`, the canonical map `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}` of
> conormal sheaves in the sense of [Stacks, Tag 04F4] part (2).
>
> It is the morphism of conormal sheaves of [Stacks, Tag 04F7] for the square whose top morphism
> is `𝟙 Z` and whose bottom morphism is `p`, transported along the identification of pullback
> along an identity with the identity functor and along the identifications of the conormal
> sheaves of the two inclusions with those of their closed-immersion factorizations.

```lean
def universalConormalTransitivityMap (h : i ≫ p = j) :
    universalConormalSheaf j ⟶ universalConormalSheaf i
```

**`Stacks.ConormalSequenceUnramifiedPair.conormalSequenceSecondArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L448). The attribute's comment: “the second arrow 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/Y}, built as the conormal differential of Tag 01UZ for Z ⟶ Z' over Z'' and moved along the identification thirdTermIso of the third term”.

> **The second arrow `𝒞_{Z/X} ⟶ i^*Ω_{X/Y}` of [Stacks, Tag 067V].** It is the conormal
> differential of [Stacks, Tag 01UZ] for the closed immersion `Z ⟶ Z'` of `Z` into the ambient
> scheme of its universal first-order thickening over `X`, taken over the ambient scheme `Z''` of
> the universal first-order thickening over `Y` — that is, the second arrow of the sequence of
> [Stacks, Tag 067L] that the proof of [Stacks, Tag 067V] reduces to — with its target moved onto
> `i^*Ω_{X/Y}` by `Stacks.ConormalSequenceUnramifiedPair.thirdTermIso` and its source read through
> `Stacks.ConormalSequenceUnramifiedPair.conormalSheafComparisonIso`.

```lean
def conormalSequenceSecondArrow (h : i ≫ p = j) :
    conormalSheafModules i ⟶
      (Scheme.Modules.pullback i).obj (Scheme.Hom.relativeDifferentials p)
```

**`Stacks.ConormalSequenceUnramifiedPair.conormalSequenceComp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L1081). The attribute's comment: “the composite of the two arrows 𝒞\_\{Z/Y} ⟶ 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/Y} vanishes, so the two arrows form a complex”.

> **[Stacks, Tag 067V]: the two arrows form a complex.** The composite
> `𝒞_{Z/Y} ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/Y}` vanishes.

```lean
theorem conormalSequenceComp_eq_zero (h : i ≫ p = j) :
    conormalSequenceFirstArrow i j p h ≫ conormalSequenceSecondArrow i j p h = 0
```

**`Stacks.ConormalSequenceUnramifiedPair.epi_conormalSequenceSecondArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 1093](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L1093). The attribute's comment: “surjectivity of the second arrow 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/Y}, which is the ⟶ 0 at the right-hand end of the sequence”.

> **[Stacks, Tag 067V]: the second arrow is an epimorphism.** This is the `⟶ 0` at the
> right-hand end of the sequence.

```lean
theorem epi_conormalSequenceSecondArrow (h : i ≫ p = j) :
    Epi (conormalSequenceSecondArrow i j p h)
```

**`Stacks.ConormalSequenceUnramifiedPair.conormalSequenceShortComplex_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 1110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L1110). The attribute's comment: “exactness at the middle term 𝒞\_\{Z/X}: the kernel of the second arrow is the image of the first”.

> **[Stacks, Tag 067V]: the sequence is exact at `𝒞_{Z/X}`.** The kernel of the second arrow is
> the image of the first.

```lean
theorem conormalSequenceShortComplex_exact (h : i ≫ p = j) :
    (ShortComplex.mk _ _ (conormalSequenceComp_eq_zero i j p h)).Exact
```

## Tag 06AE, a lemma

[Tag 06AE](https://stacks.math.columbia.edu/tag/06AE) in the Stacks Project.

**`Stacks.Thickenings.transitivityMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Transitivity.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Transitivity.lean#L81). The attribute's comment: “part (1): the morphism Z' ⟶ Y'”.

> **The morphism `Z' ⟶ Y'` of part (1) of [Stacks Project, Tag 06AE].** For a universal
> first-order thickening `Z ⊂ Z'` of `Z` over `X` and one `Y ⊂ Y'` of `Y` over `X`, this is the
> canonical morphism of [Stacks Project, Tag 04F7] for the square over `X` with vertical maps `i`
> and `𝟙 X`.

```lean
noncomputable def transitivityMap (tZ : UniversalFirstOrderThickening (i ≫ p))
    (tY : UniversalFirstOrderThickening p) : tZ.ambient ⟶ tY.ambient
```

**`Stacks.Thickenings.isUniversal_relative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Transitivity.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/Transitivity.lean#L149). The attribute's comment: “part (1): Y ×\_\{Y'} Z' is the universal first-order thickening of Z over Y”.

> **Part (1) of [Stacks Project, Tag 06AE].** Let `Z --i--→ Y --p--→ X` be morphisms of
> schemes, let `Z ⊂ Z'` be a universal first-order thickening of `Z` over `X` and `Y ⊂ Y'` one of
> `Y` over `X`. Then the fibre product `Y ×_{Y'} Z'` along the morphism
> `Stacks.Thickenings.transitivityMap` is a universal first-order thickening of `Z` over `Y`.

```lean
theorem isUniversal_relative :
    IsUniversalFirstOrderThickening i (relativeInclusion i p tZ tY)
      (relativeToBase i p tZ tY)
```

**`Stacks.Thickenings.transitivityConormalLeftMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean#L94). The attribute's comment: “part (2): the first arrow i^* 𝒞\_\{Y/X} ⟶ 𝒞\_\{Z/X}”.

> **The first arrow `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X}` of the conormal sequence of part (2) of
> [Stacks Project, Tag 06AE].** It is the canonical map of [Stacks Project, Tag 01R4] for the
> square of inclusions with vertical maps `i` and the morphism `Z' ⟶ Y'` of
> `Stacks.Thickenings.transitivityMap`.

```lean
def transitivityConormalLeftMap :
    (modulePullback i.toLRSHom.toShHom).obj
        (conormalSheaf tY.inclusion.liftCoborder.toLRSHom.toShHom) ⟶
      conormalSheaf tZ.inclusion.liftCoborder.toLRSHom.toShHom
```

**`Stacks.Thickenings.transitivityConormalRightMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean#L116). The attribute's comment: “part (2): the second arrow 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y}”.

> **The second arrow `𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` of the conormal sequence of part (2) of
> [Stacks Project, Tag 06AE].** It is the canonical map of [Stacks Project, Tag 01R4] for the
> square of inclusions with vertical maps `𝟙 Z` and the projection `Y ×_{Y'} Z' ⟶ Z'`, read
> through the identification of pullback along the identity with the identity functor.

```lean
def transitivityConormalRightMap :
    conormalSheaf tZ.inclusion.liftCoborder.toLRSHom.toShHom ⟶
      conormalSheaf (relativeInclusion i p tZ tY).liftCoborder.toLRSHom.toShHom
```

**`Stacks.Thickenings.epi_transitivityConormalRightMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean#L129). The attribute's comment: “part (2): exactness at the right term”. References: SGA 6 VIII (2.6), “right exactness”.

> **Part (2) of [Stacks Project, Tag 06AE], exactness at `𝒞_{Z/Y}`.** The second arrow
> `𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` of the conormal sequence is an epimorphism, which is the `⟶ 0` at the
> right-hand end of the canonical sequence `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0`.

```lean
theorem epi_transitivityConormalRightMap :
    Epi (transitivityConormalRightMap i p tZ tY)
```

**`Stacks.Thickenings.transitivityConormalLeftMap_comp_rightMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean#L276). The attribute's comment: “part (2): the two arrows of the sequence compose to zero”.

> **The two arrows of the conormal sequence of part (2) of [Stacks Project, Tag 06AE] compose
> to zero.**

```lean
theorem transitivityConormalLeftMap_comp_rightMap :
    transitivityConormalLeftMap i p tZ tY ≫ transitivityConormalRightMap i p tZ tY = 0
```

**`Stacks.Thickenings.transitivityConormalShortComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean#L288). The attribute's comment: “part (2): the sequence as a short complex”.

> **The conormal sequence of part (2) of [Stacks Project, Tag 06AE]** as a two-term complex of
> `𝒪_Z`-modules, `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}`.

```lean
def transitivityConormalShortComplex :
    ShortComplex (SheafOfModules.{u} (structureSheafRing Z.toLocallyRingedSpace.toRingedSpace))
```

**`Stacks.Thickenings.transitivityConormalShortComplex_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/TransitivityConormal.lean#L614). The attribute's comment: “part (2): exactness at the middle term”. References: SGA 6 VIII (2.2), “partial”; SGA 6 VIII (2.6), “partial”.

> **Part (2) of [Stacks Project, Tag 06AE], exactness at `𝒞_{Z/X}`.** The conormal sequence
> `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` is exact at its middle term; with
> `Stacks.Thickenings.epi_transitivityConormalRightMap` this makes
> `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0` exact.

```lean
theorem transitivityConormalShortComplex_exact :
    (transitivityConormalShortComplex i p tZ tY).Exact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.7, Tag 04F2](https://stacks.math.columbia.edu/tag/04F2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
