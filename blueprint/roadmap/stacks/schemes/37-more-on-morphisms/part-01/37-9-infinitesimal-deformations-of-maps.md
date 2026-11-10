---
declaration: section
origin: cited
lean: Stacks.Thickenings.mapDifferenceDerivation, Stacks.Thickenings.mapDifferenceDerivation_appTop, Stacks.Thickenings.mapDifferenceSheaf, Stacks.Thickenings.mapDifferenceSheaf_app, Stacks.Thickenings.app_mapDifferenceSheaf, Stacks.Thickenings.mapDifferenceSheaf_map, Stacks.Thickenings.mapDifferenceSheaf_add, Stacks.Thickenings.mapDifferenceSheaf_appLE_base
statement: formalized
proof: formalized
---

# 37.9 Infinitesimal deformations of maps

Section 37.9 of the Stacks Project, [Tag 04BU](https://stacks.math.columbia.edu/tag/04BU). 13 tags here are carried by 44 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04FG, a lemma

[Tag 04FG](https://stacks.math.columbia.edu/tag/04FG) in the Stacks Project.

**`Stacks.Thickenings.mapDifferenceDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivation.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivation.lean#L307). The attribute's comment: “affine case”.

> **The difference of two infinitesimal deformations of a map is a derivation**, affine case of
> [Stacks Project, Tag 04FG]. Let `i : X ⟶ X'` and `j : Y ⟶ Y'` be first-order thickenings with
> `X'` and `Y'` affine, let `p : X' ⟶ S` and `q : Y' ⟶ S` make them thickenings over `S`, and let
> `(a, a')` and `(a, b')` be two morphisms of thickenings over `S` with the same reduction `a` —
> hypothesis (1) of the source. Assume the two induced maps of conormal modules agree — hypothesis
> (2). Then the difference of the two comorphisms descends to a `Γ(S, ⊤)`-derivation of `Γ(Y, ⊤)`
> with values in the conormal module of `i`.
>
> The conormal module carries two module structures here: over `Γ(Y, ⊤)` along `a`, and over
> `Γ(S, ⊤)` along the structure morphism `i ≫ p` of `X` over `S`.

```lean
noncomputable def mapDifferenceDerivation [IsAffine X'] [IsAffine Y']
    (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j)
    (ha' : a' ≫ q = p) (hb' : b' ≫ q = p)
    (hC : conormalMap hi hj comm_a = conormalMap hi hj comm_b) :
    letI := appTopAlgebra (j ≫ q)
    letI := conormalModuleAlong hi a
    letI := conormalModuleAlong hi (i ≫ p)
    Derivation Γ(S, (⊤ : S.Opens)) Γ(Y, (⊤ : Y.Opens)) (RingHom.ker i.appTop.hom)
```

**`Stacks.Thickenings.mapDifferenceDerivation_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivation.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivation.lean#L351). The attribute's comment: “affine case”.

> **The factorization of [Stacks Project, Tag 04FG], affine case.** The difference of the two
> comorphisms `a'.appTop` and `b'.appTop` on `Γ(Y', ⊤)` is the composite
> ```
> Γ(Y', ⊤) --j.appTop--> Γ(Y, ⊤) --D--> RingHom.ker i.appTop.hom ⊆ Γ(X', ⊤)
> ```
> where `D` is the `Γ(S, ⊤)`-derivation `Stacks.Thickenings.mapDifferenceDerivation`.

```lean
theorem mapDifferenceDerivation_appTop [IsAffine X'] [IsAffine Y']
    (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j)
    (ha' : a' ≫ q = p) (hb' : b' ≫ q = p)
    (hC : conormalMap hi hj comm_a = conormalMap hi hj comm_b)
    (x : Γ(Y', (⊤ : Y'.Opens))) :
    letI := appTopAlgebra (j ≫ q)
    letI := conormalModuleAlong hi a
    letI := conormalModuleAlong hi (i ≫ p)
    ((mapDifferenceDerivation hi hj comm_a comm_b ha' hb' hC (j.appTop.hom x) :
        RingHom.ker i.appTop.hom) : Γ(X', (⊤ : X'.Opens)))
      = a'.appTop.hom x - b'.appTop.hom x
```

**`Stacks.Thickenings.mapDifferenceSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean#L474). The attribute's comment: “the derivation D”.

> **The derivation `D` of [Stacks Project, Tag 04FG].** For an open `V` of `Y'` this is the map
> `Γ(Y, j ⁻¹ᵁ V) → Γ(X', a' ⁻¹ᵁ V)`, that is `𝒪_Y ⟶ a_*𝒞_{X/X'}` on sections over `V`, through
> which `(a')^♯ - (b')^♯` factors. It is characterised by
> `Stacks.Thickenings.mapDifferenceSheaf_spec`.

```lean
noncomputable def mapDifferenceSheaf (hi : IsFirstOrderThickening i)
    (hj : IsFirstOrderThickening j) (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j)
    (hC : AgreeOnIdeal j a' b') (V : Y'.Opens) (s : Γ(Y, j ⁻¹ᵁ V)) : Γ(X', a' ⁻¹ᵁ V)
```

**`Stacks.Thickenings.mapDifferenceSheaf_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean#L520). The attribute's comment: “the factorization”.

> **The factorization of [Stacks Project, Tag 04FG].** The difference of the two comorphisms on
> `Γ(Y', V)` is the composite of `j^♯ : 𝒪_{Y'} ⟶ 𝒪_Y` with the derivation `D`.

```lean
theorem mapDifferenceSheaf_app (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j) (hC : AgreeOnIdeal j a' b')
    (V : Y'.Opens) (x : Γ(Y', V)) :
    mapDifferenceSheaf hi hj comm_a comm_b hC V ((j.app V).hom x)
      = mapDifferenceLE (le_refl (a' ⁻¹ᵁ V)) (preimage_le_preimage hi comm_a comm_b V) x
```

**`Stacks.Thickenings.app_mapDifferenceSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean#L535). The attribute's comment: “the factorization passes through the conormal sheaf”.

> **The derivation takes values in the conormal sheaf.** The value of `D` is killed by the
> comorphism of `i`, i.e. it is a section of the defining ideal of `X ⊂ X'`, which for a first-order
> thickening is `𝒞_{X/X'}`. This is what makes the factorization of
> `Stacks.Thickenings.mapDifferenceSheaf_app` pass through `a_*𝒞_{X/X'}` and not merely through
> `a_*𝒪_{X'}`.

```lean
theorem app_mapDifferenceSheaf (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j) (hC : AgreeOnIdeal j a' b')
    (V : Y'.Opens) (s : Γ(Y, j ⁻¹ᵁ V)) :
    (i.app (a' ⁻¹ᵁ V)).hom (mapDifferenceSheaf hi hj comm_a comm_b hC V s) = 0
```

**`Stacks.Thickenings.mapDifferenceSheaf_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean#L554). The attribute's comment: “D is a map of sheaves”.

> **`D` is a map of sheaves**: it commutes with restriction.

```lean
theorem mapDifferenceSheaf_map (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j) (hC : AgreeOnIdeal j a' b')
    {V V' : Y'.Opens} (hV : V' ≤ V) (s : Γ(Y, j ⁻¹ᵁ V)) :
    resOpen (a'.preimage_mono hV) (mapDifferenceSheaf hi hj comm_a comm_b hC V s)
      = mapDifferenceSheaf hi hj comm_a comm_b hC V' (resOpen (j.preimage_mono hV) s)
```

**`Stacks.Thickenings.mapDifferenceSheaf_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean#L566). The attribute's comment: “D is additive”.

> **`D` is additive.**

```lean
theorem mapDifferenceSheaf_add (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j) (hC : AgreeOnIdeal j a' b')
    (V : Y'.Opens) (s t : Γ(Y, j ⁻¹ᵁ V)) :
    mapDifferenceSheaf hi hj comm_a comm_b hC V (s + t)
      = mapDifferenceSheaf hi hj comm_a comm_b hC V s
        + mapDifferenceSheaf hi hj comm_a comm_b hC V t
```

**`Stacks.Thickenings.mapDifferenceSheaf_appLE_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean#L587). The attribute's comment: “D is 𝒪\_S-linear”.

> **`D` kills the sections pulled back from the base.** This is `𝒪_S`-linearity: a section of
> `𝒪_S` over an open `Z` of `S` pulls back to a section of `𝒪_Y` over `j ⁻¹ᵁ V` for `V ≤ q ⁻¹ᵁ Z`,
> and `D` vanishes on it, because the two lifts `a'` and `b'` are morphisms over `S` and therefore
> agree on sections coming from `S`.

```lean
theorem mapDifferenceSheaf_appLE_base (hi : IsFirstOrderThickening i)
    (hj : IsFirstOrderThickening j) (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j)
    (hC : AgreeOnIdeal j a' b') (ha' : a' ≫ q = p) (hb' : b' ≫ q = p) {Z : S.Opens}
    {V : Y'.Opens} (hV : V ≤ q ⁻¹ᵁ Z) (hjV : j ⁻¹ᵁ V ≤ (j ≫ q) ⁻¹ᵁ Z) (r : Γ(S, Z)) :
    mapDifferenceSheaf hi hj comm_a comm_b hC V
        (((j ≫ q).appLE Z (j ⁻¹ᵁ V) hjV).hom r) = 0
```

**`Stacks.Thickenings.mapDifferenceSheaf_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationGlobal.lean#L688). The attribute's comment: “the Leibniz rule for D”.

> **The Leibniz rule for `D`.** This is the last clause of [Stacks Project, Tag 04FG]: together
> with `Stacks.Thickenings.mapDifferenceSheaf_add` and
> `Stacks.Thickenings.mapDifferenceSheaf_appLE_base` it says that `D` is an `𝒪_S`-derivation of
> `𝒪_Y` with values in `a_*𝒞_{X/X'}`.
>
> The proof is the computation of the affine case, read on an affine open of `Y'` after lifting the
> two sections: the difference of the two comorphisms on a product is
> `Δ(u)·(a')^♯ v + (b')^♯ u·Δ(v)`, and this agrees with `(a')^♯ u·Δ(v) + (a')^♯ v·Δ(u)` because the
> two differences lie in the defining ideal of `i`, whose square vanishes.

```lean
theorem mapDifferenceSheaf_mul (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (comm_a : i ≫ a' = a ≫ j) (comm_b : i ≫ b' = a ≫ j) (hC : AgreeOnIdeal j a' b')
    (V : Y'.Opens) (s t : Γ(Y, j ⁻¹ᵁ V)) :
    mapDifferenceSheaf hi hj comm_a comm_b hC V (s * t)
      = conormalSmul hi hj comm_a V (mapDifferenceSheaf hi hj comm_a comm_b hC V t)
            (app_mapDifferenceSheaf hi hj comm_a comm_b hC V t) s
        + conormalSmul hi hj comm_a V (mapDifferenceSheaf hi hj comm_a comm_b hC V s)
            (app_mapDifferenceSheaf hi hj comm_a comm_b hC V s) t
```

**`Stacks.Thickenings.differenceDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationSheaf.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationSheaf.lean#L739). The attribute's comment: “the derivation D, for arbitrary X' and Y'”.

> **The `𝒪_S`-derivation `D : 𝒪_Y ⟶ a_*𝒞_{X/X'}` of [Stacks Project, Tag 04FG], at sheaf
> level.** Let `i : X ⟶ X'` be a first-order thickening, let `j : Y ⟶ Y'` be an immersion with
> structure morphism `q : Y' ⟶ S`, and let `(a, a')` and `(a, b')` be two morphisms of thickenings
> over `S` with the same reduction `a` — hypothesis (1) of the source — whose two induced maps
> `a^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` of [Stacks Project, Tag 01R4] agree — hypothesis (2). Then the
> difference `(a')^♯ - (b')^♯` factors through this derivation; the factorization is
> `Stacks.Thickenings.firstOrderImmersionConormalSheafι_differenceDerivation_d`.
>
> It is `Stacks.Thickenings.differenceDerivationHom` composed with the universal relative
> derivation of `Y` over `S`, so that it is an `𝒪_S`-derivation by construction.

```lean
def differenceDerivation (hi : i.ker ^ 2 = ⊥) (hq : b' ≫ q = a' ≫ q) (ca : i ≫ a' = a ≫ j)
    (cb : i ≫ b' = a ≫ j)
    (hC : Stacks.Immersion.immersionConormalSheafMap i j a a'
        (Stacks.Immersion.toShHom_square ca) =
      Stacks.Immersion.immersionConormalSheafMap i j a b'
        (Stacks.Immersion.toShHom_square cb)) :
    SheafOfModules.SheafDerivation (inverseImageStructureMap (j ≫ q))
      ((Scheme.Modules.pushforward a).obj (Stacks.Conormal.conormalSheaf i))
```

**`Stacks.Thickenings.firstOrderImmersionConormalSheafι_differenceDerivation_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationSheaf.lean, line 794](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDerivationSheaf.lean#L794). The attribute's comment: “the factorization, for arbitrary X' and Y'”.

> **The factorization of [Stacks Project, Tag 04FG], at sheaf level.** The difference
> `(a')^♯ s - (b')^♯ s` of the two comorphisms, on a section `s` of `𝒪_{Y'}` over `V` and read over
> the open `(b')⁻¹V ⊓ (a')⁻¹V` of `X'` where both are defined, is the image of
> `D (j^♯ s)` under the inclusion `𝒞_{X/X'} ⟶ 𝒪_{X'}` of the conormal sheaf of the first-order
> thickening `i`.
>
> That is the composite `𝒪_{Y'} ⟶ 𝒪_Y --D--> a_*𝒞_{X/X'} ⟶ a_*𝒪_{X'}` of the source.

```lean
theorem firstOrderImmersionConormalSheafι_differenceDerivation_d (hi : i.ker ^ 2 = ⊥)
    (hq : b' ≫ q = a' ≫ q) (ca : i ≫ a' = a ≫ j) (cb : i ≫ b' = a ≫ j)
    (hC : Stacks.Immersion.immersionConormalSheafMap i j a a'
        (Stacks.Immersion.toShHom_square ca) =
      Stacks.Immersion.immersionConormalSheafMap i j a b'
        (Stacks.Immersion.toShHom_square cb))
    (V : Y'.Opens) (s : Γ(Y', V)) :
    (Stacks.Thickenings.firstOrderImmersionConormalSheafι i hi).val.app
        (op (liftPairOpen a' b' V))
        ((Stacks.Conormal.conormalSheaf i).val.map
          (homOfLE (preimage_liftPairOpen ca cb V).le).op
          ((differenceDerivation q hi hq ca cb hC).d (X := op (j ⁻¹ᵁ V))
            ((j.app V).hom s))) =
      (a'.appLE V (liftPairOpen a' b' V) inf_le_right).hom s -
        (b'.appLE V (liftPairOpen a' b' V) inf_le_left).hom s
```

## Tag 04BV, an equation

[Tag 04BV](https://stacks.math.columbia.edu/tag/04BV) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.derivationDirectImageEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DerivationsIntoDirectImage.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DerivationsIntoDirectImage.lean#L73). The attribute's comment: “the bijection `θ ↔ D = d_{Y/S} ∘ θ` at scheme level on the Zariski site, stated at a general target module”.

> **Equation (04BV).**  For `a : X ⟶ Y`, `b : Y ⟶ Z` morphisms of schemes and an
> `𝒪_X`-module `C`, the `𝒪_X`-linear maps `θ : a^*Ω_{Y/Z} ⟶ C` correspond bijectively to the
> `Z`-derivations `D : 𝒪_Y ⟶ a_*C`, by `D = d_{Y/Z} ∘ θ` with `θ` transposed along the
> adjunction `a^* ⊣ a_*`.

```lean
def derivationDirectImageEquiv (a : X ⟶ Y) (b : Y ⟶ Z) (C : X.Modules) :
    ((Scheme.Modules.pullback a).obj (relativeDifferentials b) ⟶ C) ≃
      SheafOfModules.SheafDerivation (inverseImageStructureMap b)
        ((Scheme.Modules.pushforward a).obj C)
```

**`AlgebraicGeometry.Scheme.Hom.derivationDirectImageEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DerivationsIntoDirectImage.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DerivationsIntoDirectImage.lean#L84). The attribute's comment: “the equation `D = d_{Y/S} ∘ θ` at scheme level on the Zariski site”.

> **Equation (04BV) itself.**  The derivation attached to `θ : a^*Ω_{Y/Z} ⟶ C` is the
> universal derivation `d_{Y/Z}` followed by the transpose of `θ` along `a^* ⊣ a_*`.

```lean
theorem derivationDirectImageEquiv_apply (a : X ⟶ Y) (b : Y ⟶ Z) (C : X.Modules)
    (θ : (Scheme.Modules.pullback a).obj (relativeDifferentials b) ⟶ C) :
    derivationDirectImageEquiv a b C θ =
      (universalRelativeDerivation b).postcomp
        (((Scheme.Modules.pullbackPushforwardAdjunction a).homEquiv
          (relativeDifferentials b) C) θ).val
```

**`AlgebraicGeometry.SheafOfModules.universalDerivation_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials.lean#L130). The attribute's comment: “the factorization D = d o theta of a derivation through the universal derivation”. References: EGA IV (16.5.3), “(ii)”.

> **Stacks Project, Tag 08RM.** Postcomposition with the universal
> derivation gives the unique morphism from the module of relative
> differentials to any coefficient sheaf.

```lean
theorem universalDerivation_isUniversal {X : TopCat.{u}}
    {O₁ O₂ : TopCat.Sheaf CommRingCat.{max u v} X} (φ : O₁ ⟶ O₂) :
    IsUniversal.{u, v, u_1} (universalDerivation.{u, v, u_1} φ)
```

## Tag 02H5, a lemma

[Tag 02H5](https://stacks.math.columbia.edu/tag/02H5) in the Stacks Project.

**`Stacks.Thickenings.existsUnique_derivationActionGlobal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDerivationActionGlobal.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDerivationActionGlobal.lean#L714). References: SGA 3 III (4.9), “Perturbation clause”.

> **A derivation acts in exactly one way on a lift of a map**, [Stacks Project, Tag 02H5].
> Let `S` be a scheme, let `i : X ⟶ X'` and `j : Y ⟶ Y'` be first-order thickenings, let
> `p : X' ⟶ S` and `q : Y' ⟶ S` be the structure morphisms, and let `(a, a')` be a morphism of
> thickenings `(X ⊂ X') ⟶ (Y ⊂ Y')` over `S`. Then for every `𝒪_X`-linear map
> `θ : a^*Ω_{Y/S} ⟶ 𝒞_{X/X'}` there is exactly one morphism `b' : X' ⟶ Y'` such that `(a, b')` is
> again a morphism of thickenings over `S` — conditions (1) and (2) of
> [Stacks Project, Tag 04FG] for the pair `(a', b')` — and the derivation `D` of
> [Stacks Project, Tag 04FG] attached to the pair is related to `θ` by Equation
> [Stacks Project, Tag 04BV], `D = θ ∘ d_{Y/S}`.
>
> Nothing is affine, and the datum is the one of the source: a morphism of sheaves of
> `𝒪_X`-modules out of the pulled-back sheaf of relative differentials.
>
> Tag 04FG numbers two conditions; with Equation 04BV they make the three requirements written out
> on sections below. Condition (1), that the two reductions agree,
> is `comm_b : i ≫ b' = a ≫ j`, the same `a` as for `a'`; that `b'` is a morphism over `S` is
> `b' ≫ q = p`. Condition (2), that the two induced maps `a^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` of
> [Stacks Project, Tag 01R4] agree, is the first conjunct: for a first-order thickening `j` the
> conormal sheaf `𝒞_{Y/Y'}` *is* the defining ideal of `j` and the induced map is the comorphism,
> so the condition says that `(a')^♯` and `(b')^♯` agree on the sections killed by `j^♯`. Equation
> [Stacks Project, Tag 04BV] is the second conjunct: the difference `(b')^♯ - (a')^♯`, which is the
> derivation `D` of [Stacks Project, Tag 04FG] read through the inclusion `𝒞_{X/X'} ⟶ 𝒪_{X'}` of
> `Stacks.Thickenings.firstOrderImmersionConormalSheafι`, is `θ` applied to the pulled-back
> universal differential `Stacks.Smooth.pullbackD`.
>
> Because `d_{Y/S}` kills `j^♯` of a section of the defining ideal of `j`, the second conjunct
> implies the first, so the morphism characterised here is the same whether condition (2) is read
> as above or as the equality of the two maps of conormal sheaves. For the same reason `j` need
> only be a morphism of schemes: the source asks it to be a first-order thickening, and at that
> hypothesis the first conjunct is exactly its condition (2), since `𝒞_{Y/Y'}` is then the
> defining ideal of `j` and the map of [Stacks Project, Tag 01R4] is the comorphism.

```lean
theorem existsUnique_derivationActionGlobal (ha' : a' ≫ q = p) :
    ∃! b' : X' ⟶ Y', ∃ (comm_b : i ≫ b' = a ≫ j) (_ : b' ≫ q = p),
      (∀ (W : Y'.Opens) (V : X'.Opens) (hA : V ≤ a' ⁻¹ᵁ W) (g : Γ(Y', W)),
          (j.app W).hom g = 0 →
            (b'.appLE W V (le_preimage_of_comm hsq comm_a comm_b hA)).hom g
              = (a'.appLE W V hA).hom g)
        ∧ ∀ (W : Y'.Opens) (V : X'.Opens) (hA : V ≤ a' ⁻¹ᵁ W) (g : Γ(Y', W)),
            (b'.appLE W V (le_preimage_of_comm hsq comm_a comm_b hA)).hom g
              = (a'.appLE W V hA).hom g
                + derivationSection hsq θ W V (preimage_le_of_comm comm_a hA) g
```

## Tag 0CK1, a remark

[Tag 0CK1](https://stacks.math.columbia.edu/tag/0CK1) in the Stacks Project.

**`Stacks.Thickenings.differenceDerivation_derivationActionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDerivationActionDifference.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDerivationActionDifference.lean#L413).

> **[Stacks Project, Tag 0CK1], for arbitrary schemes.** Let `S` be a scheme, let
> `i : X ⟶ X'` be a first-order thickening, let `j : Y ⟶ Y'` be an immersion with structure
> morphism `q : Y' ⟶ S`, let `(a, a')` be a morphism of thickenings `(X ⊂ X') ⟶ (Y ⊂ Y')` over
> `S`, and let `θ : a^*Ω_{Y/S} ⟶ 𝒞_{X/X'}` be an `𝒪_X`-linear map. The source writes `θ ⬝ a'` for
> the lift [Stacks Project, Tag 02H5] attaches to `θ`, which is
> `Stacks.Thickenings.derivationActionSheaf`, and says that this notation *means nothing else than*
> the following two things.
>
> * The derivation `D` of [Stacks Project, Tag 04FG] attached to the pair `(a', θ ⬝ a')` — the
>   `𝒪_S`-derivation `𝒪_Y ⟶ a_*𝒞_{X/X'}` of
>   `Stacks.Thickenings.derivationActionDifferenceDerivation` — is related to `θ` by Equation
>   [Stacks Project, Tag 04BV]: it is `d_{Y/S}` followed by `θ`, read through the transpose of `θ`
>   along `a^* ⊣ a_*`. That is the first conjunct.
> * The comorphisms `(a')^♯` and `(θ ⬝ a')^♯` differ by `D`: on a section `s` of `𝒪_{Y'}` over an
>   open `V`, `(θ ⬝ a')^♯ s = (a')^♯ s + D (j^♯ s)`, the value of `D` being read inside `𝒪_{X'}`
>   through the inclusion `𝒞_{X/X'} ⟶ 𝒪_{X'}` by `Stacks.Thickenings.conormalSectionι`. That is
>   the second conjunct.
>
> Nothing is affine, and the datum is the one of the source: a morphism of sheaves of `𝒪_X`-modules
> out of the pulled-back sheaf of relative differentials. The derivation is the one
> [Stacks Project, Tag 04FG] attaches to the pair, with all three of that tag's hypotheses
> discharged for it — in particular condition (2), which is
> `Stacks.Thickenings.immersionConormalSheafMap_derivationActionSheaf`.

```lean
theorem differenceDerivation_derivationActionSheaf :
    derivationActionDifferenceDerivation hi q ca θ =
        (Scheme.Hom.universalRelativeDerivation (j ≫ q)).postcomp
          ((Scheme.Modules.pullbackPushforwardAdjunction a).homEquiv
            (Scheme.Hom.relativeDifferentials (j ≫ q))
            (Stacks.Conormal.conormalSheaf i) θ).val ∧
      ∀ (V : Y'.Opens) (s : Γ(Y', V)),
        ((derivationActionSheaf hi q ca θ).app V).hom s =
          (a'.app V).hom s +
            conormalSectionι hi ca V
              ((derivationActionDifferenceDerivation hi q ca θ).d (X := op (j ⁻¹ᵁ V))
                ((j.app V).hom s))
```

## Tag 04FH, a lemma

[Tag 04FH](https://stacks.math.columbia.edu/tag/04FH) in the Stacks Project.

**`Stacks.Thickenings.isSheaf_compatibleLiftsPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationGluing.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationGluing.lean#L320).

> **[Stacks Project, Tag 04FH].** For a scheme `S`, immersions `i : X ⟶ X'` and `j : Y ⟶ Y'`, a
> morphism `a : X ⟶ Y` and a map `A : a^* 𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}`, the rule assigning to an open `V`
> of `X'` the set of morphisms `V ⟶ Y'` over `S` restricting to `a` on `i⁻¹V` and inducing the
> restriction of `A` there is a **sheaf of sets** on `X'`.
>
> The proof is the unique-gluing form of the sheaf condition. A compatible family of lifts glues to
> a morphism by `Stacks.Thickenings.glueCompatibleLifts`, that morphism is again a compatible lift
> by `Stacks.Thickenings.isCompatibleLift_glueCompatibleLifts`, and a lift over the union is
> determined by its restrictions to the cover.

```lean
theorem isSheaf_compatibleLiftsPresheaf (pX' : X' ⟶ S) (pY' : Y' ⟶ S) (a : X ⟶ Y)
    (A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i) :
    (compatibleLiftsPresheaf pX' pY' a A).IsSheaf
```

**`Stacks.Thickenings.IsCompatibleLift.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheaf.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheaf.lean#L232). The attribute's comment: “the restriction maps”.

> **The three conditions of [Stacks Project, Tag 04FI] are stable under restriction.** A lift of
> `a` over an open `V` of `X'` compatible with `A` restricts to a compatible lift over any smaller
> open `V'`.

```lean
theorem IsCompatibleLift.restrict (hb : IsCompatibleLift pX' pY' a A V b)
    {V' : X'.Opens} (hV : V' ≤ V) :
    IsCompatibleLift pX' pY' a A V' (X'.homOfLE hV ≫ b)
```

**`Stacks.Thickenings.compatibleLiftsPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheaf.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheaf.lean#L258). The attribute's comment: “the restriction maps”.

> **The presheaf of compatible lifts.** The rule assigning to an open `V` of `X'` the set of
> morphisms `V ⟶ Y'` over `S` restricting to `a` on `i⁻¹V` and inducing the restriction of `A`
> there, with the restriction maps of `Stacks.Thickenings.compatibleLiftsRestrict`.

```lean
def compatibleLiftsPresheaf (pX' : X' ⟶ S) (pY' : Y' ⟶ S) (a : X ⟶ Y)
    (A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i) :
    TopCat.Presheaf (Type u) X'.carrier
```

## Tag 04FI, an equation

[Tag 04FI](https://stacks.math.columbia.edu/tag/04FI) in the Stacks Project.

**`Stacks.Thickenings.firstOrderCompatibleLifts`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationMaps.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationMaps.lean#L129).

> **The set of compatible lifts for first-order thickenings.** The set
> `Stacks.Thickenings.compatibleLifts` when `i` and `j` are first-order thickenings in the sense of
> [Stacks Project, Tag 04EX].

```lean
abbrev firstOrderCompatibleLifts (hi : IsFirstOrderThickening i)
    (hj : IsFirstOrderThickening j) (pX' : X' ⟶ S) (pY' : Y' ⟶ S) (a : X ⟶ Y)
    (A : letI := hi.1; letI := hj.1;
      (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
        immersionConormalSheaf i)
    (V : X'.Opens) : Type u
```

## Tag 04FJ, a lemma

[Tag 04FJ](https://stacks.math.columbia.edu/tag/04FJ) in the Stacks Project.

**`Stacks.Thickenings.exists_addAction_compatibleLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheafHomAction.lean, line 856](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheafHomAction.lean#L856). The attribute's comment: “the action of SheafHom(a^*Ω, 𝒞) on the sheaf of Tag 04FI, for arbitrary schemes”.

> **The sheaf `SheafHom_{𝒪_X}(a^*Ω_{Y/S}, 𝒞_{X/X'})` acts on the sheaf of
> [Stacks Project, Tag 04FI]**, [Stacks Project, Tag 04FJ] for arbitrary schemes.
>
> Let `S` be a scheme, let `i : X ⟶ X'` be a first-order thickening, let `j : Y ⟶ Y'` be an
> immersion, let `p : X' ⟶ S` and `q : Y' ⟶ S` be the structure morphisms, let `a : X ⟶ Y` and let
> `A : a^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` be a map of `𝒪_X`-modules. For every open `V` of `X'` the additive
> group of sections of `SheafHom_{𝒪_X}(a^*Ω_{Y/S}, 𝒞_{X/X'})` over the part `i⁻¹V` of `X` cut out
> by `V` acts on the set `Stacks.Thickenings.compatibleLifts` of [Stacks Project, Tag 04FI] of
> lifts of `a` over `V` inducing `A`, and the action commutes with the restriction maps of the
> sheaf `Stacks.Thickenings.compatibleLiftsPresheaf` of [Stacks Project, Tag 04FH]: it is an action
> of sheaves.
>
> Nothing is affine, the datum is the one of the source — a morphism of sheaves of `𝒪_X`-modules
> out of the pulled-back sheaf of relative differentials, read over an open — and the third
> condition of [Stacks Project, Tag 04FI] is the equality of maps of conormal **sheaves**.
>
> The action is `Stacks.Thickenings.compatibleLiftsVAdd`, the group laws are
> `Stacks.Thickenings.homSectionAct_zero` and `Stacks.Thickenings.homSectionAct_add`, and the
> compatibility with restriction is
> `Stacks.Thickenings.compatibleLiftsRestrict_compatibleLiftsVAdd`.

```lean
theorem exists_addAction_compatibleLifts (hsq : i.ker ^ 2 = ⊥) (pX' : X' ⟶ S) (pY' : Y' ⟶ S)
    (a : X ⟶ Y)
    (A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i) :
    ∃ act : ∀ V : X'.Opens, deformationHomSections i a (j ≫ pY') V →
        compatibleLifts pX' pY' a A V → compatibleLifts pX' pY' a A V,
      (∀ (V : X'.Opens) (c : compatibleLifts pX' pY' a A V), act V 0 c = c) ∧
        (∀ (V : X'.Opens) (θ η : deformationHomSections i a (j ≫ pY') V)
          (c : compatibleLifts pX' pY' a A V), act V (θ + η) c = act V θ (act V η c)) ∧
        ∀ (V V' : X'.Opens) (hV : V' ≤ V) (θ : deformationHomSections i a (j ≫ pY') V)
          (c : compatibleLifts pX' pY' a A V),
          compatibleLiftsRestrict pX' pY' a A hV (act V θ c)
            = act V' (moduleHomSections.restrict (i.preimage_mono hV) θ)
                (compatibleLiftsRestrict pX' pY' a A hV c)
```

**`Stacks.Thickenings.existsUnique_compatibleLiftsVAdd_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheafHomTransitivity.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheafHomTransitivity.lean#L636). The attribute's comment: “simple transitivity over an open carrying a lift, for arbitrary schemes”. References: EGA IV (16.5.14), “more general”.

> **[Stacks Project, Tag 04FJ], the transitivity clause, for arbitrary schemes.** Let `S` be a
> scheme, let `i : X ⟶ X'` be a first-order thickening, let `j : Y ⟶ Y'` be an immersion, let
> `a : X ⟶ Y` be a morphism and let `A : a^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` be a map of `𝒪_X`-modules. Over an
> open `V` of `X'` **carrying a lift**, the action of
> `SheafHom_{𝒪_X}(a^*Ω_{Y/S}, 𝒞_{X/X'})` of `Stacks.Thickenings.compatibleLiftsVAdd` on the lifts of
> [Stacks Project, Tag 04FI] is **simply transitive**: for any two lifts `b₀`, `c₀` over `V` there
> is exactly one section carrying `b₀` to `c₀`.
>
> No affineness is assumed, of `S`, `X'`, `Y'` or `V`.
>
> Existence is the unrestricted [Stacks Project, Tag 04FG] read for the restricted thickening
> `i ∣_ V` and transported to the deformation sheaf's conormal track
> (`Stacks.Thickenings.exists_isDerivationAction_over`), followed by the uniqueness half of
> [Stacks Project, Tag 02H5] (`Stacks.Thickenings.eq_of_isDerivationAction`) identifying the lift it
> produces with `θ ⬝ b₀` (`Stacks.Thickenings.homSectionAct_eq_derivationActionSheaf`). Uniqueness of
> the section is `Stacks.Thickenings.deformationHomSections_ext`.

```lean
theorem existsUnique_compatibleLiftsVAdd_eq (hsq : i.ker ^ 2 = ⊥) (pX' : X' ⟶ S) (pY' : Y' ⟶ S)
    (a : X ⟶ Y)
    (A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i) (V : X'.Opens) (b₀ c₀ : compatibleLifts pX' pY' a A V) :
    ∃! θ : deformationHomSections i a (j ≫ pY') V,
      compatibleLiftsVAdd hsq pX' pY' a A V θ b₀ = c₀
```

**`Stacks.Thickenings.deformationAddAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDerivationAction.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDerivationAction.lean#L719). The attribute's comment: “the action on the deformations with a fixed conormal map, over affine schemes”.

> **The action of [Stacks Project, Tag 04FJ], affine case.** The additive group of
> `Γ(Y, ⊤)`-linear maps `Ω[Γ(Y, ⊤)⁄Γ(S, ⊤)] ⟶ 𝒞_{X/X'}` — the sections over the affine `X'` of
> `SheafHom_{𝒪_X}(a^*Ω_{Y/S}, 𝒞_{X/X'})` — acts on the deformations of `a` with conormal map `A`,
> by `Stacks.Thickenings.Deformation.act`.

```lean
noncomputable def deformationAddAction [IsAffine S] [IsAffine X'] [IsAffine Y']
    (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j) (p : X' ⟶ S) (q : Y' ⟶ S)
    (a : X ⟶ Y)
    (A : letI := Smooth.thickeningKerModule hj
      letI := conormalModuleAlong hi a
      RingHom.ker j.appTop.hom →ₗ[Γ(Y, (⊤ : Y.Opens))] RingHom.ker i.appTop.hom) :
    letI := appTopAlgebra (j ≫ q)
    letI := conormalModuleAlong hi a
    AddAction (Ω[Γ(Y, (⊤ : Y.Opens))⁄Γ(S, (⊤ : S.Opens))] →ₗ[Γ(Y, (⊤ : Y.Opens))]
        RingHom.ker i.appTop.hom) (Deformation hi hj p q a A)
```

## Tag 04FK, a remark

[Tag 04FK](https://stacks.math.columbia.edu/tag/04FK) in the Stacks Project.

**`Stacks.Thickenings.eq_zero_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationUnthickenedTarget.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationUnthickenedTarget.lean#L108). The attribute's comment: “the vanishing of the conormal datum A”.

> **The map `A` of [Stacks Project, Tag 04FH] is zero when `Y = Y'`.** This is the first
> assertion of [Stacks Project, Tag 04FK]: in the case `Y = Y'` the conormal datum "is always
> zero".

```lean
theorem eq_zero_of_isIso [IsIso j] (a : X ⟶ Y)
    (A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i) : A = 0
```

**`Stacks.Thickenings.compatibleLiftsPresheafIsoLiftsOverBasePresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationUnthickenedTarget.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationUnthickenedTarget.lean#L185). The attribute's comment: “the elementary description of the lifting sheaf”.

> **The sheaf of [Stacks Project, Tag 04FH] is the elementary rule when `Y = Y'`.** The
> presheaf of compatible lifts for a datum `A` is isomorphic to the presheaf of lifts over `S`
> extending `a`, by the isomorphism which is the identity on underlying morphisms.
>
> This is the description of the sheaf asserted by [Stacks Project, Tag 04FK]. The simply
> transitive action of `Hom_{𝒪_X}(a^*Ω_{Y/S}, 𝒞_{X/X'})` on the elementary rule — the last
> assertion of that remark — is
> `Stacks.Thickenings.exists_simplyTransitive_addAction_liftsOverBase` in
> `StacksFrontier.AlgebraicGeometry.MoreMorphisms.InfinitesimalDeformationUnthickenedTargetAction`,
> obtained by transporting the unrestricted [Stacks Project, Tag 04FJ] along this very
> isomorphism.

```lean
def compatibleLiftsPresheafIsoLiftsOverBasePresheaf [IsIso j]
    (A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i) :
    compatibleLiftsPresheaf pX' pY' a A ≅ liftsOverBasePresheaf i j pX' pY' a
```

**`Stacks.Thickenings.exists_simplyTransitive_addAction_liftsOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationUnthickenedTargetAction.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationUnthickenedTargetAction.lean#L166). The attribute's comment: “the action of Hom(a^*Ω\_\{Y/S}, 𝒞\_\{X/X'}) on the elementary lifting rule, with the group laws, the compatibility with restriction, and simple transitivity over an open carrying a lift”. References: SGA 3 XII (9.4), “partial”.

> **The action clause of [Stacks Project, Tag 04FK].** Let `S` be a scheme, let `i : X ⟶ X'`
> be a first order thickening, let `j : Y ⟶ Y'` be an isomorphism — the case `Y = Y'` of the
> remark — let `p : X' ⟶ S` and `q : Y' ⟶ S` be the structure morphisms and let `a : X ⟶ Y`. The
> sheaf `Hom_{𝒪_X}(a^*Ω_{Y/S}, 𝒞_{X/X'})` acts on the elementary rule
> `Stacks.Thickenings.liftsOverBasePresheaf` of the remark: over every open `V` of `X'` the
> additive group of sections of `SheafHom_{𝒪_X}(a^*Ω_{Y/S}, 𝒞_{X/X'})` over `i⁻¹V` acts on the
> morphisms `V ⟶ Y'` over `S` restricting to `a` on `i⁻¹V`, the action commutes with the
> restriction maps of that rule, and over an open carrying a lift it is **simply transitive**.
>
> No affineness is assumed, of `S`, `X'`, `Y'` or `V`, and no condition on conormal sheaves
> appears anywhere: this is the action on the elementary rule itself, which is what the remark
> asserts.
>
> The action is `Stacks.Thickenings.liftsOverBaseVAdd`; everything about it is the unrestricted
> [Stacks Project, Tag 04FJ] transported along
> `Stacks.Thickenings.compatibleLiftsEquivLiftsOverBase`.

```lean
theorem exists_simplyTransitive_addAction_liftsOverBase (hsq : i.ker ^ 2 = ⊥) (pX' : X' ⟶ S)
    (pY' : Y' ⟶ S) (a : X ⟶ Y) :
    ∃ act : ∀ V : X'.Opens, deformationHomSections i a (j ≫ pY') V →
        liftsOverBase i j pX' pY' a V → liftsOverBase i j pX' pY' a V,
      (∀ (V : X'.Opens) (c : liftsOverBase i j pX' pY' a V), act V 0 c = c) ∧
        (∀ (V : X'.Opens) (θ η : deformationHomSections i a (j ≫ pY') V)
          (c : liftsOverBase i j pX' pY' a V), act V (θ + η) c = act V θ (act V η c)) ∧
        (∀ (V V' : X'.Opens) (hV : V' ≤ V) (θ : deformationHomSections i a (j ≫ pY') V)
          (c : liftsOverBase i j pX' pY' a V),
          liftsOverBaseRestrict i j pX' pY' a hV (act V θ c)
            = act V' (moduleHomSections.restrict (i.preimage_mono hV) θ)
                (liftsOverBaseRestrict i j pX' pY' a hV c)) ∧
        ∀ (V : X'.Opens) (b₀ c₀ : liftsOverBase i j pX' pY' a V),
          ∃! θ : deformationHomSections i a (j ≫ pY') V, act V θ b₀ = c₀
```

## Tag 0CK2, a remark

[Tag 0CK2](https://stacks.math.columbia.edu/tag/0CK2) in the Stacks Project.

**`Stacks.Thickenings.epi_modulePullback_immersionConormalSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean#L143). The attribute's comment: “surjectivity of the conormal map coming from the base, after pullback”.

> **The canonical map of conormal sheaves coming from the base stays surjective after
> pullback.** For `Y = Z ×_{Z'} Y'` the canonical map `h^* 𝒞_{Z/Z'} ⟶ 𝒞_{Y/Y'}` of
> [Stacks Project, Tag 01R4] is an epimorphism by [Stacks Project, Tag 0473], and the module
> pullback along any morphism `c : W ⟶ Y` preserves epimorphisms, being a left adjoint.
>
> Taken at `c = a` this is the surjectivity of `g^* 𝒞_{Z/Z'} ⟶ a^* 𝒞_{Y/Y'}` used in
> [Stacks Project, Tag 0CK2]; taken at `c = ι_{i⁻¹V} ≫ a` it is the same statement over an open
> of `X'`.

```lean
theorem epi_modulePullback_immersionConormalSheafMap [IsImmersion j] [IsImmersion k]
    {W : Scheme.{u}} {h : Y ⟶ Z} {h' : Y' ⟶ Z'} (sq : IsPullback j h h' k) (c : W ⟶ Y) :
    Epi ((modulePullback c.toLRSHom.toShHom).map
      (immersionConormalSheafMap j k h h' (toShHom_square sq.w)))
```

**`Stacks.Thickenings.eq_of_isBaseCompatibleConormalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean#L191). The attribute's comment: “the conormal datum is determined by the map on the closed subschemes”.

> **The conormal datum of [Stacks Project, Tag 04FH] is determined by `a` over a thickened
> base.** If two maps `A, B : a^* 𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` are both compatible with the base, they are
> equal: the map they are precomposed with is an epimorphism by
> `Stacks.Thickenings.epi_modulePullback_immersionConormalSheafMap`.

```lean
theorem eq_of_isBaseCompatibleConormalMap (sq : IsPullback j h h' k)
    (ci : i ≫ g' = (a ≫ h) ≫ k)
    {A B : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i}
    (hA : IsBaseCompatibleConormalMap i j k h h' g' a sq.w ci A)
    (hB : IsBaseCompatibleConormalMap i j k h h' g' a sq.w ci B) : A = B
```

**`Stacks.Thickenings.isBaseCompatibleConormalMap_of_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean#L284). The attribute's comment: “the composition g^*𝒞\_\{Z/Z'} ⟶ a^*𝒞\_\{Y/Y'} ⟶ 𝒞\_\{X/X'} is the canonical map induced by g', for the datum of a lift”.

> **The conormal datum of a lift over the base is compatible with the base.** For a morphism
> `b : V ⟶ Y'` over `Z'` restricting to `a` on `i⁻¹V`, the canonical map of conormal sheaves of the
> square it forms is compatible with the base: stacking that square on the cartesian square gives
> the square `(i ∣_ V) ≫ (V.ι ≫ g') = (ι_{i⁻¹V} ≫ a ≫ h) ≫ k`, whose canonical map does not
> involve `b`.
>
> This is the assertion of [Stacks Project, Tag 0CK2] that the composition
> `g^*𝒞_{Z/Z'} ⟶ a^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` "has to be the canonical map induced by `g'`", read for
> the datum attached to an actual lift.

```lean
theorem isBaseCompatibleConormalMap_of_lift (sq : IsPullback j h h' k)
    (ci : i ≫ g' = (a ≫ h) ≫ k) {V : X'.Opens} {b : V.toScheme ⟶ Y'}
    (hb₁ : b ≫ h' = V.ι ≫ g') (hb₂ : i ∣_ V ≫ b = ((i ⁻¹ᵁ V).ι ≫ a) ≫ j) :
    IsBaseCompatibleConormalMap (i ∣_ V) j k h h' (V.ι ≫ g') ((i ⁻¹ᵁ V).ι ≫ a) sq.w
      (comm_restrict_base i k h g' a ci V)
      (immersionConormalSheafMap (i ∣_ V) j ((i ⁻¹ᵁ V).ι ≫ a) b (toShHom_square hb₂))
```

**`Stacks.Thickenings.isBaseCompatibleConormalMap_of_isCompatibleLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean#L313). The attribute's comment: “the composition g^*𝒞\_\{Z/Z'} ⟶ a^*𝒞\_\{Y/Y'} ⟶ 𝒞\_\{X/X'} has to be the canonical map induced by g', for the given datum: a datum with a compatible lift over an open is base compatible there”.

> **A conormal datum that admits a compatible lift is compatible with the base.** If some
> morphism `b : V ⟶ Y'` out of an open `V` of `X'` is a compatible lift of `a` for the datum `A`,
> then the restriction of `A` to `V` is compatible with the base: condition (3) of
> [Stacks Project, Tag 04FI] identifies that restriction with the canonical map of the square `b`
> forms, which is compatible with the base by
> `Stacks.Thickenings.isBaseCompatibleConormalMap_of_lift`.
>
> This is the assertion of [Stacks Project, Tag 0CK2] that the composition
> `g^*𝒞_{Z/Z'} ⟶ a^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` *has to be* the canonical map induced by `g'`, read for
> the given datum: wherever the sheaf of [Stacks Project, Tag 04FH] has a section, `A` is forced
> to be base compatible, and by `Stacks.Thickenings.eq_of_isBaseCompatibleConormalMap` that pins
> it down. So base compatibility is not a restriction on the data the source considers; it is the
> source's determination of `A` by `a`.

```lean
theorem isBaseCompatibleConormalMap_of_isCompatibleLift (sq : IsPullback j h h' k)
    (ci : i ≫ g' = (a ≫ h) ≫ k)
    {A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i} {V : X'.Opens} {b : V.toScheme ⟶ Y'}
    (hb : IsCompatibleLift g' h' a A V b) :
    IsBaseCompatibleConormalMap (i ∣_ V) j k h h' (V.ι ≫ g') ((i ⁻¹ᵁ V).ι ≫ a) sq.w
      (comm_restrict_base i k h g' a ci V) (restrictConormalSheafMap a A V)
```

**`Stacks.Thickenings.isCompatibleLift_iff_of_isBaseCompatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean#L327). The attribute's comment: “the conormal condition on a lift is automatic”.

> **The third condition of [Stacks Project, Tag 04FI] is automatic over a thickened base.** For
> `A` compatible with the base, a morphism `b : V ⟶ Y'` out of an open `V` of `X'` is a compatible
> lift of `a` exactly when it is a morphism over `Z'` restricting to `a` on `i⁻¹V`.

```lean
theorem isCompatibleLift_iff_of_isBaseCompatible (sq : IsPullback j h h' k)
    (ci : i ≫ g' = (a ≫ h) ≫ k)
    {A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i}
    (hA : IsBaseCompatibleConormalMap i j k h h' g' a sq.w ci A) (V : X'.Opens)
    (b : V.toScheme ⟶ Y') :
    IsCompatibleLift g' h' a A V b ↔
      b ≫ h' = V.ι ≫ g' ∧ i ∣_ V ≫ b = ((i ⁻¹ᵁ V).ι ≫ a) ≫ j
```

**`Stacks.Thickenings.compatibleLiftsPresheafIsoLiftsOverBasePresheafOfBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBase.lean#L354). The attribute's comment: “the elementary description of the lifting sheaf”.

> **The sheaf of [Stacks Project, Tag 04FH] is the elementary rule over a thickened base.** For
> `A` compatible with the base, the presheaf of compatible lifts of `a` is isomorphic to the
> presheaf `Stacks.Thickenings.liftsOverBasePresheaf` of morphisms `V ⟶ Y'` over `Z'` restricting
> to `a` on `i⁻¹V`, by the isomorphism which is the identity on underlying morphisms.
>
> This is the description of the sheaf asserted by [Stacks Project, Tag 0CK2]. The simply
> transitive action of `Hom_{𝒪_X}(a^*Ω_{Y/Z}, 𝒞_{X/X'})` on the elementary rule — the last
> assertion of that remark — is
> `Stacks.Thickenings.exists_simplyTransitive_addAction_liftsOverBaseOfBase` in
> `StacksFrontier.AlgebraicGeometry.MoreMorphisms.InfinitesimalDeformationThickenedBaseAction`,
> obtained by transporting the unrestricted [Stacks Project, Tag 04FJ] for the base `Z'` along
> this isomorphism and along the identification `Ω_{Y/Z'} ≅ Ω_{Y/Z}` that holds because `k` is an
> immersion.

```lean
def compatibleLiftsPresheafIsoLiftsOverBasePresheafOfBase (sq : IsPullback j h h' k)
    (ci : i ≫ g' = (a ≫ h) ≫ k)
    {A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i}
    (hA : IsBaseCompatibleConormalMap i j k h h' g' a sq.w ci A) :
    compatibleLiftsPresheaf g' h' a A ≅ liftsOverBasePresheaf i j g' h' a
```

**`Stacks.Thickenings.exists_simplyTransitive_addAction_liftsOverBaseOfBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseAction.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseAction.lean#L265). The attribute's comment: “the action of Hom(a^*Ω\_\{Y/Z}, 𝒞\_\{X/X'}) on the elementary lifting rule, with the group laws, the compatibility with restriction, and simple transitivity over an open carrying a lift”. References: SGA 3 XII (9.4), “partial”.

> **The action clause of [Stacks Project, Tag 0CK2].** Let `k : Z ⟶ Z'` be an immersion, let
> `i : X ⟶ X'` be a first order thickening and `j : Y ⟶ Y'` an immersion, both over `Z'` by
> `g' : X' ⟶ Z'` and `h' : Y' ⟶ Z'`, assume `Y = Z ×_{Z'} Y'`, let `a : X ⟶ Y` and let `A` be a
> conormal datum compatible with the base. Then the sheaf `Hom_{𝒪_X}(a^*Ω_{Y/Z}, 𝒞_{X/X'})` —
> differentials relative to `Z`, as the source writes them — **acts** on the elementary rule
> `Stacks.Thickenings.liftsOverBasePresheaf` of the remark: over every open `V` of `X'` the
> additive group of its sections over `i⁻¹V` acts on the morphisms `V ⟶ Y'` over `Z'` restricting
> to `a` on `i⁻¹V`, the action commutes with the restriction maps of that rule, and over an open
> carrying a lift it is **simply transitive**.
>
> No affineness is assumed, of `Z'`, `X'`, `Y'` or `V`, and no condition on conormal sheaves
> appears in the conclusion: this is the action on the elementary rule itself, which is what the
> remark asserts.
>
> The action is `Stacks.Thickenings.liftsOverBaseVAddOfBase`: the unrestricted
> [Stacks Project, Tag 04FJ] for the base `Z'`, carried over by the identification
> `Ω_{Y/Z'} ≅ Ω_{Y/Z}` of `Stacks.Thickenings.pullbackCotangentSheafIsoOfBase` and by the
> identification of the two notions of lift.

```lean
theorem exists_simplyTransitive_addAction_liftsOverBaseOfBase (hsq : i.ker ^ 2 = ⊥)
    (sq : IsPullback j h h' k) (ci : i ≫ g' = (a ≫ h) ≫ k)
    {A : (modulePullback a.toLRSHom.toShHom).obj (immersionConormalSheaf j) ⟶
      immersionConormalSheaf i}
    (hA : IsBaseCompatibleConormalMap i j k h h' g' a sq.w ci A) :
    ∃ act : ∀ V : X'.Opens, deformationHomSections i a h V →
        liftsOverBase i j g' h' a V → liftsOverBase i j g' h' a V,
      (∀ (V : X'.Opens) (c : liftsOverBase i j g' h' a V), act V 0 c = c) ∧
        (∀ (V : X'.Opens) (θ η : deformationHomSections i a h V)
          (c : liftsOverBase i j g' h' a V), act V (θ + η) c = act V θ (act V η c)) ∧
        (∀ (V V' : X'.Opens) (hV : V' ≤ V) (θ : deformationHomSections i a h V)
          (c : liftsOverBase i j g' h' a V),
          liftsOverBaseRestrict i j g' h' a hV (act V θ c)
            = act V' (moduleHomSections.restrict (i.preimage_mono hV) θ)
                (liftsOverBaseRestrict i j g' h' a hV c)) ∧
        ∀ (V : X'.Opens) (b₀ c₀ : liftsOverBase i j g' h' a V),
          ∃! θ : deformationHomSections i a h V, act V θ b₀ = c₀
```

**`Stacks.Thickenings.liftsOverBaseVAddOfBase_comp_of_homSectionValue_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseActionNaturality.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseActionNaturality.lean#L200). The attribute's comment: “the action of Hom(a^*Ω\_\{Y/Z}, 𝒞\_\{X/X'}) on the elementary lifting rule is natural in the thickening: for two situations of the tag with vertical maps, acting and pushing a lift forward commute, given the commuting square of Tag 04BZ for the two acting sections. This is naturality of the action, not a new construction of it”.

> **The action of [Stacks Project, Tag 0CK2] on the elementary lifting rule is natural in the
> thickening.** This is the input a statement about a *sum* of first-order deformations needs: the
> sum is realized over the doubled coordinate module `M × M`
> (`Deformation.exists_linearFunctorLift_sum`), so the action has to be run once over `k[M × M]`
> and pushed forward along the two projections `k[M × M] ⟶ k[M]` and their sum, and this is the
> compatibility of the action with those pushforwards.
>
> Let two situations of [Stacks Project, Tag 0CK2] be given, with vertical maps `(wX, w)` of the
> thickenings and `(vY, v)` of the targets. Let `c` be an elementary lift over an open `V₁` of
> `X₁'`, let `d` be one over an open `V₂` of `X₂'` with `d ≫ v = w ≫ c` on underlying morphisms,
> and let `θ₁` and `θ₂` be sections of the two acting sheaves whose perturbations correspond under
> `w^♯` and `v^♯`. Then acting and pushing forward commute:
>
> `(θ₂ ⬝ d) ≫ v = w ≫ (θ₁ ⬝ c)`
>
> on underlying morphisms. The hypothesis `hθ` is the commuting square of
> [Stacks Project, Tag 04BZ] read on the conormal sections the two sections produce, and it is
> transported to the acting sheaf of the source — the differentials relative to `Z₁` and to `Z₂` —
> by `Stacks.Thickenings.baseDeformationHomSectionsEquiv`, which is the identification the action
> is defined through.

```lean
theorem liftsOverBaseVAddOfBase_comp_of_homSectionValue_comm
    (hsq₁ : i₁.ker ^ 2 = ⊥) (hsq₂ : i₂.ker ^ 2 = ⊥)
    (sq₁ : IsPullback j₁ h₁ h₁' k₁) (sq₂ : IsPullback j₂ h₂ h₂' k₂)
    (ci₁ : i₁ ≫ g₁' = (a₁ ≫ h₁) ≫ k₁) (ci₂ : i₂ ≫ g₂' = (a₂ ≫ h₂) ≫ k₂)
    {A₁ : (modulePullback a₁.toLRSHom.toShHom).obj (immersionConormalSheaf j₁) ⟶
      immersionConormalSheaf i₁}
    {A₂ : (modulePullback a₂.toLRSHom.toShHom).obj (immersionConormalSheaf j₂) ⟶
      immersionConormalSheaf i₂}
    (hA₁ : IsBaseCompatibleConormalMap i₁ j₁ k₁ h₁ h₁' g₁' a₁ sq₁.w ci₁ A₁)
    (hA₂ : IsBaseCompatibleConormalMap i₂ j₂ k₂ h₂ h₂' g₂' a₂ sq₂.w ci₂ A₂)
    (V₁ : X₁'.Opens) (V₂ : X₂'.Opens)
    (θ₁ : deformationHomSections i₁ a₁ h₁ V₁) (θ₂ : deformationHomSections i₂ a₂ h₂ V₂)
    (c : liftsOverBase i₁ j₁ g₁' h₁' a₁ V₁) (d : liftsOverBase i₂ j₂ g₂' h₂' a₂ V₂)
    {wX : (i₂ ⁻¹ᵁ V₂).toScheme ⟶ (i₁ ⁻¹ᵁ V₁).toScheme} {w : V₂.toScheme ⟶ V₁.toScheme}
    {vY : Y₂ ⟶ Y₁} {v : Y₂' ⟶ Y₁'}
    (cT : i₂ ∣_ V₂ ≫ w = wX ≫ i₁ ∣_ V₁) (cj : j₂ ≫ v = vY ≫ j₁)
    (cX : ((i₂ ⁻¹ᵁ V₂).ι ≫ a₂) ≫ vY = wX ≫ ((i₁ ⁻¹ᵁ V₁).ι ≫ a₁))
    (cA : d.1 ≫ v = w ≫ c.1)
    (hθ : ∀ (W : Y₁'.Opens) (s : Γ(Y₁', W)),
      (V₂.toScheme.presheaf.map (eqToHom (preimage_comp_eq cA W)).op).hom
          ((w.app (c.1 ⁻¹ᵁ W)).hom
            (homSectionValue hsq₁ h₁' c.2.2
              (baseDeformationHomSectionsEquiv sq₁ a₁ V₁ θ₁) W s))
        = homSectionValue hsq₂ h₂' d.2.2
            (baseDeformationHomSectionsEquiv sq₂ a₂ V₂ θ₂) (v ⁻¹ᵁ W) ((v.app W).hom s)) :
    (liftsOverBaseVAddOfBase hsq₂ sq₂ ci₂ hA₂ V₂ θ₂ d).1 ≫ v =
      w ≫ (liftsOverBaseVAddOfBase hsq₁ sq₁ ci₁ hA₁ V₁ θ₁ c).1
```

**`Stacks.Thickenings.isBaseCompatibleConormalMap_of_globalLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseGlobalLift.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseGlobalLift.lean#L83). The attribute's comment: “the composition g^*C\_\{Z/Z'} -> a^*C\_\{Y/Y'} -> C\_\{X/X'} is the canonical map induced by g', for the datum of a lift defined on all of X'”.

> **The conormal datum of a lift defined on all of `X'` is compatible with the base.** For a
> morphism `b : X' ⟶ Y'` over `Z'` whose restriction along `i` is `a`, the square it forms with
> `i` and `j` has a canonical map of conormal sheaves; stacking that square on the cartesian
> square of the base gives the square `i ≫ g' = (a ≫ h) ≫ k`, whose canonical map does not
> mention `b`. This is the assertion of [Stacks Project, Tag 0CK2] that the composite
> `g^*𝒞_{Z/Z'} ⟶ a^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` "has to be the canonical map induced by `g'`", read for
> a lift over the whole space.
>
> `Stacks.Thickenings.isBaseCompatibleConormalMap_of_lift` is the same statement for a lift
> defined on an open `V` of `X'`, where the thickening is `i ∣_ V`.

```lean
theorem isBaseCompatibleConormalMap_of_globalLift (sq : IsPullback j h h' k)
    (ci : i ≫ g' = (a ≫ h) ≫ k) {b : X' ⟶ Y'} (hb₁ : b ≫ h' = g') (hb₂ : i ≫ b = a ≫ j) :
    IsBaseCompatibleConormalMap i j k h h' g' a sq.w ci
      (immersionConormalSheafMap i j a b (toShHom_square hb₂))
```

**`Stacks.Thickenings.exists_simplyTransitive_addAction_liftsOverBaseOfGlobalLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseGlobalLift.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationThickenedBaseGlobalLift.lean#L110). The attribute's comment: “the simply transitive action of Hom(a^*Omega\_\{Y/Z}, C\_\{X/X'}) on the lifts of a over the whole space, with the conormal datum discharged by an actual lift”. References: SGA 3 XII (9.4), “partial”.

> **The action clause of [Stacks Project, Tag 0CK2] over the whole space, from a lift.** Let
> `k : Z ⟶ Z'` be an immersion, let `i : X ⟶ X'` be a first order thickening and `j : Y ⟶ Y'` an
> immersion, both over `Z'` by `g'` and `h'`, assume `Y = Z ×_{Z'} Y'`, and let `a : X ⟶ Y` admit
> a lift `b : X' ⟶ Y'`, that is, a morphism over `Z'` whose restriction along `i` is `a`. Then the
> additive group of sections over `X` of `SheafHom_{𝒪_X}(a^*Ω_{Y/Z}, 𝒞_{X/X'})` — differentials
> relative to `Z`, as the source writes them — **acts simply transitively** on the morphisms
> `X' ⟶ Y'` over `Z'` restricting to `a` along `i`.
>
> No conormal datum appears: the lift produces one, by
> `Stacks.Thickenings.isBaseCompatibleConormalMap_of_globalLift`, and it is the only one
> compatible with the base by `Stacks.Thickenings.eq_of_isBaseCompatibleConormalMap`. No
> affineness is assumed, of `Z'`, `X'` or `Y'`, and the hypothesis that the open carries a lift —
> which is what makes the action of that tag simply transitive — is discharged by `b`.

```lean
theorem exists_simplyTransitive_addAction_liftsOverBaseOfGlobalLift [IsClosedImmersion i]
    (hsq : i.ker ^ 2 = ⊥) (sq : IsPullback j h h' k) (ci : i ≫ g' = (a ≫ h) ≫ k)
    {b : X' ⟶ Y'} (hb₁ : b ≫ h' = g') (hb₂ : i ≫ b = a ≫ j) :
    ∃ act : deformationHomSections i a h ⊤ →
        liftsOverBase i j g' h' a ⊤ → liftsOverBase i j g' h' a ⊤,
      (∀ c : liftsOverBase i j g' h' a ⊤, act 0 c = c) ∧
        (∀ (θ η : deformationHomSections i a h ⊤) (c : liftsOverBase i j g' h' a ⊤),
          act (θ + η) c = act θ (act η c)) ∧
          ∀ c₀ c₁ : liftsOverBase i j g' h' a ⊤, ∃! θ : deformationHomSections i a h ⊤,
            act θ c₀ = c₁
```

**`Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean#L225). The attribute's comment: “the conormal map of an arrow of deformations is a conormal datum compatible with the base: its composite with the flat base change of the source deformation is the canonical map of Tag 01R4 for the square carrying the special fibre of the target over the closed point of the source's base. This is the factorisation through the total space of the source, not an identification of the map on the base with the map of maximal ideals”.

> **The conormal map of an arrow of deformations is compatible with the base.** The
> special-fibre immersion of `Q` sits over the closed point of `Spec A` through
> `Q.toBase ≫ Spec φ.base`, and that square factors through `P.scheme`: the arrow's square followed
> by the special-fibre square of `P`. Reading the canonical map of [Stacks Project, Tag 01R4] along
> that factorisation is exactly the compatibility of [Stacks Project, Tag 0CK2] for the conormal
> map of the arrow, with the flat-base-change map of `P` as the datum coming from the base.
>
> This is `Stacks.Immersion.immersionConormalSheafMap_comp` and nothing else; the content is that
> the two squares of a deformation and of an arrow of deformations stack to the square the
> flat-base-change map of the target is read on.

```lean
theorem isBaseCompatibleConormalMap_deformationConormalMap (φ : P ⟶ Q) :
    IsBaseCompatibleConormalMap Q.specialMap P.specialMap (residueSpecMap P.base)
      X.hom P.toBase (φ.map ≫ P.toBase) (𝟙 X.left)
      P.specialCartesian.w (square_comp (specialMap_comp_map φ) P.specialCartesian.w)
      (immersionConormalSheafMap Q.specialMap P.specialMap (𝟙 X.left) φ.map
        (toShHom_square (specialMap_comp_map φ)))
```

**`Deformation.Examples.eq_of_isBaseCompatibleConormalMap_deformationConormalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean#L275). The attribute's comment: “the conormal map of an arrow of deformations is the UNIQUE conormal datum compatible with the base, the special-fibre square of the source being cartesian. This pins the map by the base object; it does not compute it on sections”.

> **The conormal map of an arrow of deformations is the unique conormal datum compatible with
> the base.** The special-fibre square of `P` is cartesian, so
> `Stacks.Thickenings.eq_of_isBaseCompatibleConormalMap` applies: any map
> `𝟙_X^* 𝒞_{X/P.scheme} ⟶ 𝒞_{X/Q.scheme}` whose composite with the flat base change of `P` is the
> canonical map of the composite square is the conormal map of `φ`.
>
> This is the sense in which the conormal map of an arrow of deformations "is" the map of the base
> objects: it is determined by the square over `Spec A`, and
> `Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalBaseChangeIso` exhibits that
> square as the one the flat base change of `Q` and the conormal map of `φ.base` are read on.

```lean
theorem eq_of_isBaseCompatibleConormalMap_deformationConormalMap (φ : P ⟶ Q)
    {A : (modulePullback (Scheme.Hom.toLRSHom (𝟙 X.left)).toShHom).obj
        (immersionConormalSheaf P.specialMap) ⟶ immersionConormalSheaf Q.specialMap}
    (hA : IsBaseCompatibleConormalMap Q.specialMap P.specialMap (residueSpecMap P.base)
      X.hom P.toBase (φ.map ≫ P.toBase) (𝟙 X.left)
      P.specialCartesian.w (square_comp (specialMap_comp_map φ) P.specialCartesian.w) A) :
    A = immersionConormalSheafMap Q.specialMap P.specialMap (𝟙 X.left) φ.map
      (toShHom_square (specialMap_comp_map φ))
```

**`Deformation.Examples.isBaseCompatibleConormalMap_baseChangeDeformationHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean#L378). The attribute's comment: “at the base change of a deformation: the conormal map of the arrow of a deformation onto its base change along a morphism of C\_Lambda is a conormal datum compatible with the base. This is the general statement for an arrow of deformations instantiated at baseChangeDeformationHom, not a separate computation”.

> **The conormal map of the arrow of a deformation onto its base change is compatible with the
> base.** This is `Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalMap` at
> `Deformation.Examples.baseChangeDeformationHom`, the arrow the cofibered structure of the
> deformation category produces, whose morphism of total spaces is the first projection of the
> fibre product and whose base component is `g`.
>
> Taken together with
> `Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalBaseChangeIso` and the
> uniqueness `Deformation.Examples.eq_of_isBaseCompatibleConormalMap_deformationConormalMap`, this
> says that the conormal map `𝒞_{X/P.scheme} ⟶ 𝒞_{X/(P ×_A B).scheme}` of the base change is
> determined by `g` through the conormal map
> `Deformation.Examples.residueConormalMap` of the base objects.

```lean
theorem isBaseCompatibleConormalMap_baseChangeDeformationHom :
    IsBaseCompatibleConormalMap (baseChangeDeformation P g).specialMap P.specialMap
      (residueSpecMap P.base) X.hom P.toBase
      ((baseChangeDeformationHom P g).map ≫ P.toBase) (𝟙 X.left)
      P.specialCartesian.w
      (square_comp (specialMap_comp_map (baseChangeDeformationHom P g)) P.specialCartesian.w)
      (immersionConormalSheafMap (baseChangeDeformation P g).specialMap P.specialMap
        (𝟙 X.left) (baseChangeDeformationHom P g).map
        (toShHom_square (specialMap_comp_map (baseChangeDeformationHom P g))))
```

## Tag 04FL, a lemma

[Tag 04FL](https://stacks.math.columbia.edu/tag/04FL) in the Stacks Project.

**`Stacks.Thickenings.homEquiv_diagonalConormalSheafMap_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDiagonalSheaf.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/MapDifferenceDiagonalSheaf.lean#L592).

> **The difference of two maps to a fixed scheme, through the diagonal**,
> [Stacks, Tag 04FL].

```lean
theorem homEquiv_diagonalConormalSheafMap_d [IsImmersion i] (hq : b' ≫ q = a' ≫ q)
    (comm_a : i ≫ a' = a) (comm_b : i ≫ b' = a) (V : Y.Opens) (s : Γ(Y, V)) :
    (((modulePullbackPushforwardAdjunction a.toLRSHom.toShHom).homEquiv _ _
          (diagonalConormalSheafMap hq comm_a comm_b)).val.app (op V))
        (q.universalRelativeDerivation.d s) =
      conormalClass i (liftPairOpen a' b' V) (le_preimage_liftPairOpen comm_a comm_b V)
        (liftDiffSection a' b' V s) (app_liftDiffSection comm_a comm_b V s)
```

## Tag 04BX, a lemma

[Tag 04BX](https://stacks.math.columbia.edu/tag/04BX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isIso_relativeDifferentialsMap_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Etale.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Etale.lean#L111).

> **Stacks Project, Tag 04BX.** In a commutative square of schemes whose two horizontal
> arrows `f : X₂ ⟶ X₁` and `g : S₂ ⟶ S₁` are étale, the canonical map
> `f^* Ω_{X₁/S₁} ⟶ Ω_{X₂/S₂}` is an isomorphism.

```lean
theorem isIso_relativeDifferentialsMap_of_etale {X₁ X₂ S₁ S₂ : Scheme.{u}} (f : X₂ ⟶ X₁)
    (p₁ : X₁ ⟶ S₁) (p₂ : X₂ ⟶ S₂) (g : S₂ ⟶ S₁) (hcomm : f ≫ p₁ = p₂ ≫ g)
    [Etale f] [Etale g] :
    IsIso (relativeDifferentialsMap f p₁ p₂ g hcomm)
```

## Tag 04BY, a lemma

[Tag 04BY](https://stacks.math.columbia.edu/tag/04BY) in the Stacks Project.

**`Stacks.Thickenings.derivationActionSheaf_comp_etaleLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationEtaleLocalizationSheaf.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationEtaleLocalizationSheaf.lean#L481).

> **Acting by a derivation commutes with an étale localization.** Let
> `(h, h') : (T₂ ⊂ T₂') ⟶ (T₁ ⊂ T₁')` be a morphism of first-order thickenings, let
> `(f, f') : (X₂ ⟶ X₂') ⟶ (X₁ ⟶ X₁')` be a morphism of the right-hand pairs, let `(a₁, a₁')` and
> `(a₂, a₂')` be morphisms of thickenings compatible with them, and let `p₁ : X₁' ⟶ S₁`,
> `p₂ : X₂' ⟶ S₂` and `k : S₂ ⟶ S₁` form a commutative square with `f`. Assume `f` and `k` are étale.
> Then for every `𝒪_{T₁}`-linear `θ₁ : a₁^*Ω_{X₁/S₁} ⟶ 𝒞_{T₁/T₁'}`, the lifts `θ₁ ⬝ a₁'` and
> `θ₂ ⬝ a₂'` of [Stacks Project, Tag 0CK1] — for `θ₂` the transported datum
> `Stacks.Thickenings.localizedDerivationSheaf` — give a commutative square:
> ```
> (θ₂ ⬝ a₂') ≫ f' = h' ≫ (θ₁ ⬝ a₁').
> ```
>
> Nothing is assumed affine, and both actions are the ones constructed by
> `Stacks.Thickenings.derivationActionSheaf`, not morphisms assumed to satisfy a relation.
>
> `j₁` and `j₂` are not assumed to be first-order thickenings, and the commutativity of the square
> of bases is assumed only as the square `f ≫ (j₁ ≫ p₁) = (j₂ ≫ p₂) ≫ k` of the closed subschemes,
> which the ambient square `f' ≫ p₁ = p₂ ≫ k` implies.

```lean
theorem derivationActionSheaf_comp_etaleLocalization
    (hi₁ : i₁.ker ^ 2 = ⊥) (hi₂ : i₂.ker ^ 2 = ⊥)
    (ca₁ : i₁ ≫ a₁' = a₁ ≫ j₁) (ca₂ : i₂ ≫ a₂' = a₂ ≫ j₂)
    (cT : i₂ ≫ h' = h ≫ i₁) (cj : j₂ ≫ f' = f ≫ j₁) (cX : a₂ ≫ f = h ≫ a₁)
    (cA : a₂' ≫ f' = h' ≫ a₁') (cS : f ≫ (j₁ ≫ p₁) = (j₂ ≫ p₂) ≫ k)
    [AlgebraicGeometry.Etale f] [AlgebraicGeometry.Etale k]
    (θ₁ : (Scheme.Modules.pullback a₁).obj (Scheme.Hom.relativeDifferentials (j₁ ≫ p₁)) ⟶
      Stacks.Conormal.conormalSheaf i₁) :
    derivationActionSheaf hi₂ p₂ ca₂ (localizedDerivationSheaf cT cX cS θ₁) ≫ f' =
      h' ≫ derivationActionSheaf hi₁ p₁ ca₁ θ₁
```

## Tag 04BZ, a remark

[Tag 04BZ](https://stacks.math.columbia.edu/tag/04BZ) in the Stacks Project.

**`Stacks.Thickenings.derivationAction_comp_of_derivation_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationGivenDerivation.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationGivenDerivation.lean#L130). The attribute's comment: “affine case, with the two actions of Tag 0CK1 constructed by Stacks.Thickenings.derivationAction; the remark for arbitrary schemes is Stacks.Thickenings.derivationActionSheaf\_comp\_of\_derivationSection\_comm”.

> **Acting by compatible derivation data commutes with the vertical maps**, the affine case of
> [Stacks Project, Tag 04BZ]. Let `(h, h')` and `(f, f')` be the vertical maps of a diagram of
> first-order thickenings with affine ambient schemes as in [Stacks Project, Tag 04BY], let
> `(a₁, a₁')` and `(a₂, a₂')` be morphisms of thickenings compatible with them, and let
> `p₁ : X₁' ⟶ S₁` and `p₂ : X₂' ⟶ S₂` be the structure morphisms. Nothing is assumed étale.
> Given `Γ(X₁, ⊤)`-linear `θ₁ : Ω[Γ(X₁, ⊤)⁄Γ(S₁, ⊤)] ⟶ 𝒞_{T₁/T₁'}` and `Γ(X₂, ⊤)`-linear
> `θ₂ : Ω[Γ(X₂, ⊤)⁄Γ(S₂, ⊤)] ⟶ 𝒞_{T₂/T₂'}` whose derivations `D_n = θ_n ∘ d_{X_n/S_n}` of
> Equation [Stacks Project, Tag 04BV] satisfy `D₂ (f^♯ y) = (h')^♯ (D₁ y)` — the commuting square
> of the source — acting by `θ₁` on `a₁'` and by `θ₂` on `a₂'` gives a commutative square:
> ```
> (θ₂ ⬝ a₂') ≫ f' = h' ≫ (θ₁ ⬝ a₁').
> ```
>
> In [Stacks Project, Tag 04BY] the second datum is built from the first out of the étale
> hypotheses, and the hypothesis `hθ` here is then its defining property
> `Stacks.Thickenings.localizedDerivation_apply`; see
> `Stacks.Thickenings.derivationAction_comp_localizedDerivation`.

```lean
theorem derivationAction_comp_of_derivation_comm [IsAffine T₁'] [IsAffine T₂'] [IsAffine X₁']
    [IsAffine X₂'] (hi₁ : IsFirstOrderThickening i₁) (hi₂ : IsFirstOrderThickening i₂)
    (ca₁ : i₁ ≫ a₁' = a₁ ≫ j₁) (ca₂ : i₂ ≫ a₂' = a₂ ≫ j₂) (cj : j₂ ≫ f' = f ≫ j₁)
    (cA : a₂' ≫ f' = h' ≫ a₁') :
    letI := appTopAlgebra (j₁ ≫ p₁)
    letI := conormalModuleAlong hi₁ a₁
    letI := appTopAlgebra (j₂ ≫ p₂)
    letI := conormalModuleAlong hi₂ a₂
    ∀ (θ₁ : Ω[Γ(X₁, (⊤ : X₁.Opens))⁄Γ(S₁, (⊤ : S₁.Opens))] →ₗ[Γ(X₁, (⊤ : X₁.Opens))]
        RingHom.ker i₁.appTop.hom)
      (θ₂ : Ω[Γ(X₂, (⊤ : X₂.Opens))⁄Γ(S₂, (⊤ : S₂.Opens))] →ₗ[Γ(X₂, (⊤ : X₂.Opens))]
        RingHom.ker i₂.appTop.hom),
      (∀ y : Γ(X₁, (⊤ : X₁.Opens)),
          ((θ₂ (KaehlerDifferential.D _ _ (f.appTop.hom y)) : RingHom.ker i₂.appTop.hom) :
              Γ(T₂', (⊤ : T₂'.Opens)))
            = h'.appTop.hom ((θ₁ (KaehlerDifferential.D _ _ y) : RingHom.ker i₁.appTop.hom) :
              Γ(T₁', (⊤ : T₁'.Opens)))) →
        derivationAction hi₂ ca₂ p₂ θ₂ ≫ f' = h' ≫ derivationAction hi₁ ca₁ p₁ θ₁
```

**`Stacks.Thickenings.derivationActionSheaf_comp_of_derivationSection_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheafAction.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/InfinitesimalDeformationSheafAction.lean#L282). The attribute's comment: “the two actions of Tag 0CK1 constructed by Stacks.Thickenings.derivationActionSheaf”.

> **Acting by compatible derivation data commutes with the vertical maps**,
> [Stacks Project, Tag 04BZ] for arbitrary schemes, with both actions *constructed*. Let `(h, h')`
> and `(f, f')` be the vertical maps of a diagram of first-order thickenings as in
> [Stacks Project, Tag 04BY], let `(a₁, a₁')` and `(a₂, a₂')` be morphisms of thickenings
> compatible with them, and let `p₁ : X₁' ⟶ S₁` and `p₂ : X₂' ⟶ S₂` be the structure morphisms.
> Nothing is assumed étale and nothing is assumed affine. Given
> `θ₁ : a₁^*Ω_{X₁/S₁} ⟶ 𝒞_{T₁/T₁'}` and `θ₂ : a₂^*Ω_{X₂/S₂} ⟶ 𝒞_{T₂/T₂'}` whose derivations
> `D_n = θ_n ∘ d_{X_n/S_n}` of Equation [Stacks Project, Tag 04BV] satisfy
> `D₂ (f^♯ y) = (h')^♯ (D₁ y)` — the commuting square of the source, read inside the ambient
> structure sheaves — the lifts `θ₁ ⬝ a₁'` and `θ₂ ⬝ a₂'` of [Stacks Project, Tag 0CK1] give a
> commutative square:
> ```
> (θ₂ ⬝ a₂') ≫ f' = h' ≫ (θ₁ ⬝ a₁').
> ```
>
> This is `Stacks.Thickenings.derivationAction_comp_of_derivationSection_comm` with its two
> hypotheses `Stacks.Thickenings.IsDerivationAction` discharged by
> `Stacks.Thickenings.isDerivationAction_derivationActionSheaf`: the lifts are the morphisms
> constructed by `Stacks.Thickenings.derivationActionSheaf`, not morphisms assumed to satisfy a
> relation.

```lean
theorem derivationActionSheaf_comp_of_derivationSection_comm
    (hi₁ : i₁.ker ^ 2 = ⊥) (hi₂ : i₂.ker ^ 2 = ⊥)
    (p₁ : X₁' ⟶ S₁) (p₂ : X₂' ⟶ S₂)
    (ca₁ : i₁ ≫ a₁' = a₁ ≫ j₁) (ca₂ : i₂ ≫ a₂' = a₂ ≫ j₂)
    (cT : i₂ ≫ h' = h ≫ i₁) (cj : j₂ ≫ f' = f ≫ j₁) (cX : a₂ ≫ f = h ≫ a₁)
    (cA : a₂' ≫ f' = h' ≫ a₁')
    {θ₁ : (Scheme.Modules.pullback a₁).obj (Scheme.Hom.relativeDifferentials (j₁ ≫ p₁)) ⟶
      Stacks.Conormal.conormalSheaf i₁}
    {θ₂ : (Scheme.Modules.pullback a₂).obj (Scheme.Hom.relativeDifferentials (j₂ ≫ p₂)) ⟶
      Stacks.Conormal.conormalSheaf i₂}
    (hθ : ∀ (V : X₁'.Opens) (s : Γ(X₁', V)),
      (T₂'.presheaf.map (eqToHom (preimage_comp_eq cA V)).op).hom
          ((h'.app (a₁' ⁻¹ᵁ V)).hom (derivationSectionι hi₁ p₁ ca₁ θ₁ V ((j₁.app V).hom s)))
        = derivationSectionι hi₂ p₂ ca₂ θ₂ (f' ⁻¹ᵁ V)
            ((j₂.app (f' ⁻¹ᵁ V)).hom ((f'.app V).hom s))) :
    derivationActionSheaf hi₂ p₂ ca₂ θ₂ ≫ f' = h' ≫ derivationActionSheaf hi₁ p₁ ca₁ θ₁
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.9, Tag 04BU](https://stacks.math.columbia.edu/tag/04BU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
