---
declaration: section
origin: cited
lean: Stacks.Conormal.conormalAlgebra, Stacks.Conormal.conormalDegreeOneHom_isIso, Stacks.Conormal.conormalDegreeOneIso, Stacks.Conormal.conormalSymmetricHom, Stacks.Conormal.conormalSymmetricHom_unique, Stacks.Conormal.isIso_conormalSymmetricHom_app_one, Stacks.Conormal.isIso_conormalSymmetricHom_app_zero, Stacks.Conormal.epi_conormalSymmetricHom_app
statement: formalized
proof: formalized
---

# 31.20 The normal cone of an immersion

Section 31.20 of the Stacks Project, [Tag 062Z](https://stacks.math.columbia.edu/tag/062Z). 8 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0630, a definition

[Tag 0630](https://stacks.math.columbia.edu/tag/0630) in the Stacks Project.

**`Stacks.Conormal.conormalAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Immersion.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Immersion.lean#L543). The attribute's comment: “the conormal algebra”. References: EGA IV (16.1.2), “Gr\_•(f), immersions”.

> The conormal algebra of an immersion, together with its local associated-graded quotient
> presentations.

```lean
noncomputable def conormalAlgebra {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i] :
    ConormalAlgebraData i
```

## Tag 0631, an equation

[Tag 0631](https://stacks.math.columbia.edu/tag/0631) in the Stacks Project.

**`Stacks.Conormal.conormalAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Immersion.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Immersion.lean#L543). The attribute's comment: “its degree-n piece: i\_* C\_\{Z/X, n} = I^n/I^\{n+1}”. References: EGA IV (16.1.2), “Gr\_•(f), immersions”.

> The conormal algebra of an immersion, together with its local associated-graded quotient
> presentations.

```lean
noncomputable def conormalAlgebra {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i] :
    ConormalAlgebraData i
```

## Tag 0632, an equation

[Tag 0632](https://stacks.math.columbia.edu/tag/0632) in the Stacks Project.

**`Stacks.Conormal.conormalDegreeOneHom_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/DegreeOne.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/DegreeOne.lean#L464). The attribute's comment: “degree one: the conormal algebra in degree one is the conormal sheaf”.

> **[Stacks, Tag 0632]: the conormal algebra in degree one is the conormal sheaf.** The
> canonical morphism `𝒞_{Z/X} ⟶ 𝒞_{Z/X,1}` is an isomorphism.
>
> This is the degree-one assertion of the canonical surjection `Sym^*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}`: the
> identification of the degree-one piece of the conormal algebra with the conormal sheaf, which is
> what makes that surjection an isomorphism in degree one.

```lean
theorem conormalDegreeOneHom_isIso (i : Z ⟶ X) [IsImmersion i] :
    IsIso (conormalDegreeOneHom i)
```

**`Stacks.Conormal.conormalDegreeOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/DegreeOne.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/DegreeOne.lean#L478). The attribute's comment: “degree one: the identification as an isomorphism”.

> **[Stacks, Tag 0632]: the degree-one identification `𝒞_{Z/X} ≅ 𝒞_{Z/X,1}`.**

```lean
noncomputable def conormalDegreeOneIso (i : Z ⟶ X) [IsImmersion i] :
    conormalSheaf i ≅ (conormalAlgebra i).algebra.piece 1
```

**`Stacks.Conormal.conormalSymmetricHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean#L241). The attribute's comment: “the canonical map Sym*(C\_\{Z/X}) → C\_\{Z/X,*} of graded algebras”. References: EGA 0 (19.5.2), “more general”; EGA 0 (22.1.1), “more general”; EGA IV (17.12.1).

> **Stacks Project, Tag 0632.** The canonical map `Sym*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` of graded
> `𝒪_Z`-algebras, the unital homomorphism which is the identity on degree-one generators.

```lean
def conormalSymmetricHom (i : Z ⟶ X) [IsImmersion i] :
    SheafOfModules.GradedAlgebra.UnitalHom (conormalSymmetricAlgebra i)
      (conormalAlgebra i).algebra
```

**`Stacks.Conormal.conormalSymmetricHom_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean#L260). The attribute's comment: “uniqueness of the canonical map Sym*(C\_\{Z/X}) → C\_\{Z/X,*}”.

> **Stacks Project, Tag 0632.** A unital homomorphism which is the identity on degree-one
> generators is the canonical map, so the canonical map is well defined.

```lean
theorem conormalSymmetricHom_unique (i : Z ⟶ X) [IsImmersion i]
    {g : SheafOfModules.GradedAlgebra.UnitalHom (conormalSymmetricAlgebra i)
      (conormalAlgebra i).algebra}
    (hg : Scheme.Modules.symmetricAlgebraGen Z ((conormalAlgebra i).algebra.piece 1) ≫
      g.app 1 = 𝟙 ((conormalAlgebra i).algebra.piece 1)) :
    g = conormalSymmetricHom i
```

**`Stacks.Conormal.isIso_conormalSymmetricHom_app_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean#L276). The attribute's comment: “the canonical map Sym*(C\_\{Z/X}) → C\_\{Z/X,*} is an isomorphism in degree 1”.

> **Stacks Project, Tag 0632.** The canonical map `Sym*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` is an
> isomorphism in degree one. The degree-one generator `𝒞_{Z/X} ⟶ Sym¹(𝒞_{Z/X})` is an isomorphism,
> and the canonical map is the identity on it.

```lean
theorem isIso_conormalSymmetricHom_app_one (i : Z ⟶ X) [IsImmersion i] :
    IsIso ((conormalSymmetricHom i).app 1)
```

**`Stacks.Conormal.isIso_conormalSymmetricHom_app_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean#L408). The attribute's comment: “the canonical map Sym*(C\_\{Z/X}) → C\_\{Z/X,*} is an isomorphism in degree 0”.

> **Stacks Project, Tag 0632.** The canonical map `Sym*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` is an
> isomorphism in degree zero. It is a monomorphism because both degree-zero pieces are generated
> by their graded units, freely on the source and without torsion on the target, and an
> epimorphism because on an affine closed-immersion chart every degree-zero section of the target
> is a multiple of the unit.

```lean
theorem isIso_conormalSymmetricHom_app_zero (i : Z ⟶ X) [IsImmersion i] :
    IsIso ((conormalSymmetricHom i).app 0)
```

**`Stacks.Conormal.epi_conormalSymmetricHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/SymmetricQuotient.lean#L521). The attribute's comment: “the canonical map Sym*(C\_\{Z/X}) → C\_\{Z/X,*} is surjective”.

> **Stacks Project, Tag 0632.** The canonical map `Sym*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` is surjective:
> an epimorphism of sheaves of modules in every degree. In a negative degree the target vanishes,
> and in a nonnegative degree the map is locally surjective, because over an affine
> closed-immersion chart `ℐⁿ/ℐⁿ⁺¹` is generated by products of `n` sections of `ℐ`.

```lean
theorem epi_conormalSymmetricHom_app (i : Z ⟶ X) [IsImmersion i] (n : ℤ) :
    Epi ((conormalSymmetricHom i).app n)
```

## Tag 0633, a lemma

[Tag 0633](https://stacks.math.columbia.edu/tag/0633) in the Stacks Project.

**`Stacks.Conormal.conormalAlgebra_identifications`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ConormalInverseImage.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ConormalInverseImage.lean#L311). The attribute's comment: “part (1)”.

> Let `i : Z ⟶ X` be an immersion and `U ⊆ X` an open
> subscheme such that `i(Z) ⊆ U` is a closed subset of `U`; let `ℐ ⊆ 𝒪_U` be the quasi-coherent
> ideal sheaf of the closed subscheme `i(Z) ⊂ U`.  Then
> `𝒞_{Z/X,*} = i^*(⨁_{n ≥ 0} ℐⁿ) = i^{-1}(⨁_{n ≥ 0} ℐⁿ/ℐⁿ⁺¹)`:
> * the conormal algebra is isomorphic to `i^*(⨁ₙ ℐⁿ)` as sheaves of graded `𝒪_Z`-algebras, the
>   isomorphism carrying the unit to the unit;
> * the topological inverse image `i^{-1}(⨁ₙ ℐⁿ/ℐⁿ⁺¹)`, a sheaf of graded `i^{-1}𝒪_U`-algebras,
>   is isomorphic to the conormal algebra read over `i^{-1}𝒪_U` along the structure map
>   `i^{-1}𝒪_U ⟶ 𝒪_Z`, as sheaves of graded algebras, the isomorphism carrying the unit to the
>   unit.
>
> The isomorphisms are `Stacks.Conormal.conormalIsoReesPullback` and
> `Stacks.Conormal.inverseImageGrIsoConormal`.

```lean
theorem conormalAlgebra_identifications :
    (∃ e : (conormalAlgebra i).algebra ≅ openReesPullback i U hsub, ∀ W : Z.Opens,
      (e.hom.app 0).val.app (op W) ((conormalAlgebra i).algebra.one.eval (op W)) =
        (openReesPullback i U hsub).one.eval (op W)) ∧
    (∃ e : inverseImageGradedAlgebra (openLift i U hsub).base (U.toScheme).sheaf
          (grGradedAlgebra (openIdeal i U hsub)) ≅
        SheafOfModules.GradedAlgebra.scalarRestrict (openStructureMap i U hsub)
          (conormalAlgebra i).algebra, ∀ W : Z.Opens,
      (e.hom.app 0).val.app (op W)
          ((inverseImageGradedAlgebra (openLift i U hsub).base (U.toScheme).sheaf
            (grGradedAlgebra (openIdeal i U hsub))).one.eval (op W)) =
        (conormalAlgebra i).algebra.one.eval (op W))
```

**`AlgebraicGeometry.affineSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ConormalSections.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ConormalSections.lean#L183). The attribute's comment: “conormal\_algebra\_affine\_sections”.

> The homogeneous sections of the conormal algebra on an affine closed-immersion chart are
> canonically the quotients `I^n/I^(n+1)`, compatibly with multiplication, unit, and scalars.

```lean
noncomputable def affineSectionsEquiv {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (U : X.affineOpens)
    (hU : IsClosedImmersion (i.resLE U.1 (i ⁻¹ᵁ U.1) le_rfl)) :
    AffineSectionsEquiv i U hU
```

**`AlgebraicGeometry.conormalAlgebra_on_closed_open`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ConormalSections.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ConormalSections.lean#L543). The attribute's comment: “conormal\_algebra\_on\_closed\_open”.

> Both canonical identifications of the conormal algebra on an open where the immersion is
> closed.

```lean
noncomputable def conormalAlgebra_on_closed_open
    {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (U : X.Opens)
    (hU : IsClosed (Set.range (i.resLE U (i ⁻¹ᵁ U) le_rfl))) :
    ClosedOpenIdentifications i U
```

## Tag 0634, a lemma

[Tag 0634](https://stacks.math.columbia.edu/tag/0634) in the Stacks Project.

**`AlgebraicGeometry.conormalAlgebraHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/Functoriality/ConormalAlgebraHom.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/Functoriality/ConormalAlgebraHom.lean#L603).

> **Stacks Project, Tag 0634.** The unique morphism of conormal graded
> algebras over a commutative square of immersions is induced on every affine
> closed-immersion chart by the ring map on ideal-power quotients.

```lean
noncomputable def conormalAlgebraHom {Z X Z' X' : Scheme.{u}}
    (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z') (g : X ⟶ X')
    [IsImmersion i] [IsImmersion i'] (comm : f ≫ i' = i ≫ g) :
    CanonicalConormalAlgebraHom i i' f g
```

## Tag 0635, a lemma

[Tag 0635](https://stacks.math.columbia.edu/tag/0635) in the Stacks Project.

**`AlgebraicGeometry.conormalAlgebraMap_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/BaseChange.lean, line 834](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/BaseChange.lean#L834). The attribute's comment: “surjectivity”.

> The canonical map on each homogeneous piece of the conormal algebra is
> locally surjective for a cartesian square of immersions.

```lean
theorem conormalAlgebraMap_epi {Z X Z' X' : Scheme.{u}}
    (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z') (g : X ⟶ X')
    [IsImmersion i] [IsImmersion i'] (sq : IsPullback i f g i') (n : ℤ) :
    Epi ((canonicalPullbackHom i i' f g sq.w.symm).hom n)
```

**`AlgebraicGeometry.conormalAlgebraMap_isIso_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/BaseChange.lean, line 1152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/BaseChange.lean#L1152). The attribute's comment: “flat isomorphism”.

> Under flat base change the canonical map on every homogeneous piece is
> an isomorphism.

```lean
theorem conormalAlgebraMap_isIso_of_flat {Z X Z' X' : Scheme.{u}}
    (i : Z ⟶ X) (i' : Z' ⟶ X') (f : Z ⟶ Z') (g : X ⟶ X')
    [IsImmersion i] [IsImmersion i'] [Flat g]
    (sq : IsPullback i f g i') (n : ℤ) :
    IsIso ((canonicalPullbackHom i i' f g sq.w.symm).hom n)
```

## Tag 0636, a definition

[Tag 0636](https://stacks.math.columbia.edu/tag/0636) in the Stacks Project.

**`Stacks.Conormal.normalBundle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean#L112). The attribute's comment: “the normal bundle N\_ZX = Spec\_Z(Sym(C\_\{Z/X}))”.

> **Stacks Project, Tag 0636.** **The normal bundle `N_ZX = Spec_Z(Sym(𝒞_{Z/X}))`** of an
> immersion `i : Z ⟶ X`: the relative spectrum over `Z` of the symmetric algebra on the conormal
> sheaf `𝒞_{Z/X} = 𝒞_{Z/X,1}`, that is, the vector bundle of Tag 01M2 associated to `𝒞_{Z/X}`.

```lean
def normalBundle : Scheme.{u}
```

**`Stacks.Conormal.normalBundleVectorBundle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean#L145). The attribute's comment: “N\_ZX is a vector bundle over Z in the sense of 062M”.

> **Stacks Project, Tag 0636.** **`N_ZX` is a vector bundle over `Z`** in the sense of Tag
> 062M: it is the vector bundle `𝐕(𝒞_{Z/X})` of Tag 01M2 attached to the conormal sheaf, the
> relative spectrum of `Sym(𝒞_{Z/X})` graded by the symmetric powers `Symⁿ(𝒞_{Z/X})`.

```lean
def normalBundleVectorBundle : VectorBundle Z
```

**`Stacks.Conormal.normalConeCone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean#L216). The attribute's comment: “C\_ZX is a cone over Z in the sense of 062R”.

> **Stacks Project, Tag 0636.** **`C_ZX` is a cone over `Z`** in the sense of Tag 062R: it is
> affine over `Z`, and the homogeneous pieces `𝒞_{Z/X,n}` of the conormal algebra decompose the
> direct image of its structure sheaf — uniquely over every open, locally surjectively, and
> multiplicatively — with the degree-zero piece the structure sheaf of `Z`.

```lean
def normalConeCone : AbstractCone Z
```

Declarations registered for the tag:

- [`Stacks.Conormal.normalCone`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalConeInNormalBundle.lean#L220), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalBundle.lean#L253) (StacksFrontier): “the normal cone C\_ZX = Spec\_Z(C\_\{Z/X,*})”.

## Tag 0637, an equation

[Tag 0637](https://stacks.math.columbia.edu/tag/0637) in the Stacks Project.

**`Stacks.Conormal.isClosedImmersion_normalConeToNormalBundle_and_coneHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalConeConeHom.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalConeConeHom.lean#L96). The attribute's comment: “the canonical closed immersion C\_ZX → N\_ZX of cones over Z”.

> **Stacks Project, Tag 0637.** **The canonical surjection `Sym*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` of
> graded algebras defines a canonical closed immersion `C_ZX ⟶ N_ZX` of cones over `Z`.** The
> morphism `Stacks.Conormal.normalConeToNormalBundle`, the relative spectrum of that surjection, is
> a closed immersion, and it is the morphism of total spaces of a morphism of cones over `Z` from
> the normal cone `Stacks.Conormal.normalConeCone` to the normal bundle
> `Stacks.Conormal.normalBundleVectorBundle` whose graded part is the surjection.

```lean
theorem isClosedImmersion_normalConeToNormalBundle_and_coneHom :
    IsClosedImmersion (normalConeToNormalBundle i) ∧
      ∃ φ : AbstractCone.Hom (normalConeCone i) (normalBundleVectorBundle i).toAbstractCone,
        φ.f = normalConeToNormalBundle i ∧ φ.graded = (conormalSymmetricHom i).toHom
```

**`Stacks.Conormal.normalConeToNormalBundle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalConeInNormalBundle.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalConeInNormalBundle.lean#L233). The attribute's comment: “the canonical surjection of graded algebras defines a morphism C\_ZX → N\_ZX”.

> **Stacks Project, Tag 0637.** **The canonical morphism `C_ZX ⟶ N_ZX` from the normal cone to
> the normal bundle of an immersion**, defined by the canonical map
> `Sym*(𝒞_{Z/X}) ⟶ 𝒞_{Z/X,*}` of graded algebras of Tag 0632: it is the morphism of relative
> spectra attached to that map of algebra sheaves, and
> `Stacks.Conormal.ι_normalConeToNormalBundle` is its characterising property.

```lean
def normalConeToNormalBundle :
    normalCone i ⟶ Scheme.Modules.vectorBundle Z (conormalSheafDegreeOne i)
```

**`Stacks.Conormal.normalConeToNormalBundle_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalConeInNormalBundle.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/NormalCone/NormalConeInNormalBundle.lean#L242). The attribute's comment: “the morphism C\_ZX → N\_ZX is a morphism over Z”.

> **Stacks Project, Tag 0637.** The canonical morphism `C_ZX ⟶ N_ZX` is a morphism of schemes
> over `Z`: it carries the projection of the normal bundle to the projection of the normal cone.

```lean
theorem normalConeToNormalBundle_toBase :
    normalConeToNormalBundle i ≫
        Scheme.Modules.vectorBundleToBase Z (conormalSheafDegreeOne i) =
      normalConeToBase i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.20, Tag 062Z](https://stacks.math.columbia.edu/tag/062Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
