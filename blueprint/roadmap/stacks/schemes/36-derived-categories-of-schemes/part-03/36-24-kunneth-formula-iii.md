---
declaration: section
origin: cited
lean: Stacks.Cohomology.BoxKunneth.boxProductObj_module, Stacks.Cohomology.BoxKunneth.boxDoubleComplex, Stacks.Cohomology.BoxKunneth.boxDoubleComplex_X_X, Stacks.Cohomology.BoxKunneth.boxDoubleComplex_d_f, Stacks.Cohomology.BoxKunneth.boxDoubleComplex_X_d, Stacks.Cohomology.BoxKunneth.boxDoubleComplex_comm, Stacks.Cohomology.BoxKunneth.boxTotal_eq_total, Stacks.Cohomology.BoxKunneth.isQuasicoherent_boxTotal_X
statement: formalized
proof: formalized
---

# 36.24 Künneth formula, III

Section 36.24 of the Stacks Project, [Tag 0G4A](https://stacks.math.columbia.edu/tag/0G4A). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G4A, the section

[Tag 0G4A](https://stacks.math.columbia.edu/tag/0G4A) in the Stacks Project.

**`Stacks.Cohomology.BoxKunneth.boxProductObj_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L138). The attribute's comment: “the display `F ⊠ G = p^*F ⊗_{O_{X ×_S Y}} q^*G` that opens the section, including that the tensor product is the nonderived one; the bifunctoriality of `⊠` is Tag 0G46, `AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxProductFunctor`”.

> **`𝓕 ⊠ 𝓖 = p^*𝓕 ⊗_{𝒪_{X ×_S Y}} q^*𝓖`**, the definition [Stacks, Section 0G4A] opens with:
> the tensor product, on `X ×_S Y`, of the two pullbacks along the projections.  The tensor product
> is the **nonderived** one, `Stacks.SheafOfModules.TensorStalkRingedSpace.tensorSheaf`; the
> section says explicitly that, contrary to a later section, the nonderived product is meant.

```lean
theorem boxProductObj_module (F : FiniteOrderDifferentialOperatorCategory a)
    (G : FiniteOrderDifferentialOperatorCategory b) :
    (boxProductObj F G).module =
      (((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨(((pullback a b).toRingedSpace)).presheaf, (((pullback a b).toRingedSpace)).IsSheaf⟩).obj
            (((Scheme.Modules.pullback (pullback.fst a b)).obj F.module))).obj
        (((Scheme.Modules.pullback (pullback.snd a b)).obj G.module)))
```

**`Stacks.Cohomology.BoxKunneth.boxDoubleComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L163). The attribute's comment: “the double complex displayed in the section: the bicomplex `(i, j) ↦ F^i ⊠ G^j` of finite-order differential operators on `X ×_S Y / S`. No boundedness is needed for the double complex itself; its total complex, `Stacks.Cohomology.BoxKunneth.boxTotal`, needs both factors strictly bounded below”.

> **The double complex `𝓕^i ⊠ 𝓖^j` of [Stacks, Section 0G4A]**: the bicomplex obtained by
> applying the box product of [Stacks, Tag 0G46] to two `ℤ`-indexed complexes of quasi-coherent
> modules with finite-order differential operators as differentials, by the construction of
> [Stacks, Tag 0A5J].  Its horizontal differential is `d_1 = d_𝓕 ⊠ 1` and its vertical one is
> `d_2 = 1 ⊠ d_𝓖`; both are morphisms of the category of finite-order differential operators on
> `X ×_S Y / S`, which is the section's assertion that the maps of the diagram are differential
> operators of finite order there.

```lean
abbrev boxDoubleComplex :
    HomologicalComplex₂ (FiniteOrderDifferentialOperatorCategory (pullback.fst a b ≫ a))
      (ComplexShape.up ℤ) (ComplexShape.up ℤ)
```

**`Stacks.Cohomology.BoxKunneth.boxDoubleComplex_X_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L171). The attribute's comment: “the entries of the displayed double complex”.

> **The term of the double complex in degree `(i, j)` is `𝓕^i ⊠ 𝓖^j`.**

```lean
theorem boxDoubleComplex_X_X (i j : ℤ) :
    ((boxDoubleComplex a b K L).X i).X j = boxProductObj (K.X i) (L.X j)
```

**`Stacks.Cohomology.BoxKunneth.boxDoubleComplex_d_f`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L181). The attribute's comment: “the display `d_1^{i, j} = d^i_F ⊠ 1`, the horizontal differential of the double complex”.

> **The horizontal differential of the double complex is `d_1^{i, j} = d^i_𝓕 ⊠ 1`**, the first
> of the two formulas written out in [Stacks, Section 0G4A].  There is no sign: the signs of
> [Stacks, Tag 012Z] enter only in the total complex, where
> `Stacks.Cohomology.BoxKunneth.boxTotal_d` records them.

```lean
theorem boxDoubleComplex_d_f (i i' j : ℤ) :
    ((boxDoubleComplex a b K L).d i i').f j = boxHom (K.d i i') (𝟙 (L.X j))
```

**`Stacks.Cohomology.BoxKunneth.boxDoubleComplex_X_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L189). The attribute's comment: “the display `d_2^{i, j} = 1 ⊠ d^j_G`, the vertical differential of the double complex”.

> **The vertical differential of the double complex is `d_2^{i, j} = 1 ⊠ d^j_𝓖`**, the second
> of the two formulas written out in [Stacks, Section 0G4A], again with no sign.

```lean
theorem boxDoubleComplex_X_d (i j j' : ℤ) :
    ((boxDoubleComplex a b K L).X i).d j j' = boxHom (𝟙 (K.X i)) (L.d j j')
```

**`Stacks.Cohomology.BoxKunneth.boxDoubleComplex_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L198). The attribute's comment: “commutativity of the squares of the displayed diagram, i.e. that `(i, j) ↦ F^i ⊠ G^j` with those two differentials really is a double complex”.

> **The squares of the diagram displayed in [Stacks, Section 0G4A] commute**: boxing with the
> identity in one variable is natural in the other, so `(1 ⊠ d_𝓖) ∘ (d_𝓕 ⊠ 1)` and
> `(d_𝓕 ⊠ 1) ∘ (1 ⊠ d_𝓖)` agree as operators `𝓕^i ⊠ 𝓖^j ⟶ 𝓕^{i'} ⊠ 𝓖^{j'}`.

```lean
theorem boxDoubleComplex_comm (i i' j j' : ℤ) :
    boxHom (K.d i i') (𝟙 (L.X j)) ≫ boxHom (𝟙 (K.X i')) (L.d j j') =
      boxHom (𝟙 (K.X i)) (L.d j j') ≫ boxHom (K.d i i') (𝟙 (L.X j'))
```

**`Stacks.Cohomology.BoxKunneth.boxTotal_eq_total`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L214). The attribute's comment: “the sentence fixing the notation `Tot(F^• ⊠ G^•)` as the total complex of the displayed double complex; the sign convention of that total complex is Tag 012Z, recorded by `Stacks.Cohomology.BoxKunneth.boxTotal_d`”.

> **`Tot(𝓕^• ⊠ 𝓖^•)` is the total complex of the double complex `𝓕^i ⊠ 𝓖^j`**, which is what
> the notation means in [Stacks, Section 0G4A].  `Stacks.Cohomology.BoxKunneth.boxTotal` is formed
> as `HomologicalComplex.mapBifunctor`, the total complex of the bicomplex obtained by applying the
> box product; this identifies the two.

```lean
theorem boxTotal_eq_total
    [HomologicalComplex.HasMapBifunctor K L (boxProductCurried a b) (ComplexShape.up ℤ)] :
    boxTotal a b K L n₁ n₂ = (boxDoubleComplex a b K L).total (ComplexShape.up ℤ)
```

**`Stacks.Cohomology.BoxKunneth.isQuasicoherent_boxTotal_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L225). The attribute's comment: “the assertion that `Tot(F^• ⊠ G^•)` has quasi-coherent terms”.

> **The terms of `Tot(𝓕^• ⊠ 𝓖^•)` are quasi-coherent `𝒪_{X ×_S Y}`-modules**, the first of the
> two closing assertions of the paragraph of [Stacks, Section 0G4A] that fixes the notation.  In
> degree `n` the term is a finite biproduct of the `𝓕^i ⊠ 𝓖^j` with `i + j = n`, and the external
> tensor product of two quasi-coherent modules is quasi-coherent
> (`AlgebraicGeometry.isQuasicoherent_externalTensorProduct`).

```lean
theorem isQuasicoherent_boxTotal_X (n : ℤ) :
    ((boxTotal a b K L n₁ n₂).X n).module.IsQuasicoherent
```

**`Stacks.Cohomology.BoxKunneth.exists_isGlobalDiffOpOfOrder_boxTotal_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalSection.lean#L236). The attribute's comment: “the assertion that the differentials of `Tot(F^• ⊠ G^•)` are differential operators of finite order on `X ×_S Y / S`”.

> **The differentials of `Tot(𝓕^• ⊠ 𝓖^•)` are differential operators of finite order on
> `X ×_S Y / S`**, the second of the two closing assertions of the paragraph of
> [Stacks, Section 0G4A] that fixes the notation: for each pair of degrees there is a `k` for which
> the differential is a global differential operator of order `≤ k` relative to the structure map
> of `X ×_S Y / S`.

```lean
theorem exists_isGlobalDiffOpOfOrder_boxTotal_d (n m : ℤ) :
    ∃ k, DiffOp.IsGlobalDiffOpOfOrder (pullback.fst a b ≫ a).relativeStructureSheafMap k
      ((boxTotal a b K L n₁ n₂).d n m).1
```

## Tag 0G4B, an equation

[Tag 0G4B](https://stacks.math.columbia.edu/tag/0G4B) in the Stacks Project.

**`Stacks.Cohomology.BoxKunneth.relativeBoxKunnethMapUnbounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/RelativeKunnethUnbounded.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/RelativeKunnethUnbounded.lean#L446). The attribute's comment: “the map, for arbitrary complexes `F^•`, `G^•` as in the source: the composite of the five maps of the source, steps (1) to (3) being the Künneth map of Tag 0FLP for the inverse-image ringed spaces (the pullbacks `Lp^*`, which computes `p^{-1}` along `(X ×_S Y, f^{-1}𝒪_S) ⟶ (X, a^{-1}𝒪_S)`), steps (4) and (5) being `boxTotalComplexDerivedComparison`; `Tot(F^• ⊠ G^•)` is the direct-sum total complex, formed over `f^{-1}𝒪_S`”.

> **The relative cup product of [Stacks, Tag 0G4B]**
>
> `Ra_*(𝓕^•) ⊗^𝐋_{𝒪_S} Rb_*(𝓖^•) ⟶ Rf_*(Tot(𝓕^• ⊠ 𝓖^•))`
>
> in `D(𝒪_S)`, for `𝓕^•` on `X/S` and `𝓖^•` on `Y/S` arbitrary `ℤ`-indexed complexes of
> quasi-coherent modules whose differentials are differential operators of finite order, with no
> boundedness condition, and `f` the structure morphism of `X ×_S Y`. The total complex is the
> direct-sum totalization of the double complex `𝓕^i ⊠ 𝓖^j`, whose maps are `f^{-1}𝒪_S`-linear, so
> it is formed over `f^{-1}𝒪_S`. The map is the composite of the five maps of the source: the
> Künneth map of [Stacks, Tag 0FLP] for the inverse-image ringed spaces, which is the two pullback
> maps and the relative cup product of [Stacks, Remark 0B68], followed by `Rf_*` of steps (4)
> and (5), `boxTotalComplexDerivedComparison`.

```lean
def relativeBoxKunnethMapUnbounded
    (K : CochainComplex (FiniteOrderDifferentialOperatorCategory a) ℤ)
    (L : CochainComplex (FiniteOrderDifferentialOperatorCategory b) ℤ) :
    ((derivedTensorProductFunctor.{u, u + 1} (SheafedSpace.sheaf S.toRingedSpace)).obj
          ((derivedPushforward.{u, u + 1, u + 1} (inverseImageBaseProjection a)).obj
            (DerivedCategory.Q.obj (leftComplex a K)))).obj
        ((derivedPushforward.{u, u + 1, u + 1} (inverseImageBaseProjection b)).obj
          (DerivedCategory.Q.obj (rightComplex b L))) ⟶
      (derivedPushforward.{u, u + 1, u + 1}
          (inverseImageBaseProjection (pullback.fst a b ≫ a))).obj
        (DerivedCategory.Q.obj (HomologicalComplex.mapBifunctor K L
          (boxProductRelativeCurried a b) (ComplexShape.up ℤ)))
```

## Tag 0FLR, an equation

[Tag 0FLR](https://stacks.math.columbia.edu/tag/0FLR) in the Stacks Project.

**`Stacks.Cohomology.BoxKunneth.globalBoxCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalKunnethMapUnbounded.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalKunnethMapUnbounded.lean#L249). The attribute's comment: “the map, as the composite of the five maps of the source: steps (1) to (3) are the global Künneth map of Tag 0G7V at the global cup product `globalCupProductCanonical` of Section 0FKU, the pullbacks being `Lp^*`, which computes `p^{-1}` along `(X ×_S Y, f^{-1}𝒪_S) ⟶ (X, a^{-1}𝒪_S)`; steps (4) and (5) are `boxTotalComplexDerivedComparison`”.

> **The global cup product of [Stacks, Tag 0FLR]**
>
> `RΓ(X, 𝓕^•) ⊗^𝐋_A RΓ(Y, 𝓖^•) ⟶ RΓ(X ×_S Y, Tot(𝓕^• ⊠ 𝓖^•))`
>
> in `D(A)` for `A = Γ(S, 𝒪_S)`, for `𝓕^•` on `X/S` and `𝓖^•` on `Y/S` arbitrary `ℤ`-indexed
> complexes of quasi-coherent modules whose differentials are differential operators of finite
> order. It is the composite of the two pullback maps on derived global sections, the global cup
> product of [Stacks, Section 0FKU] (together these are the global Künneth map
> `Stacks.Cohomology.GlobalKunneth.kunnethGlobalMapCanonical` of [Stacks, Tag 0G7V] for the
> inverse-image ringed spaces), and derived global sections of steps (4) and (5).

```lean
def globalBoxCupProduct :
    ((tensorBase S.toRingedSpace).obj
          ((sectionsOverBase (inverseImageBaseProjection a)).obj
            (DerivedCategory.Q.obj (leftComplex a K)))).obj
        ((sectionsOverBase (inverseImageBaseProjection b)).obj
          (DerivedCategory.Q.obj (rightComplex b L))) ⟶
      (sectionsOverBase (inverseImageBaseProjection (pullback.fst a b ≫ a))).obj
        (DerivedCategory.Q.obj
          (HomologicalComplex.mapBifunctor K L (boxProductRelativeCurried a b)
            (ComplexShape.up ℤ)))
```

**`Stacks.Cohomology.BoxKunneth.globalBoxCupProduct_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalKunnethMapUnbounded.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalKunnethMapUnbounded.lean#L272). The attribute's comment: “the map is the composite of steps (1) to (3), the global Künneth map of Tag 0G7V at the global cup product of Section 0FKU, with derived global sections of steps (4) and (5)”.

> **The map is the five-step composite**: the global Künneth map of [Stacks, Tag 0G7V] at the
> global cup product of [Stacks, Section 0FKU], followed by derived global sections of steps (4)
> and (5).

```lean
theorem globalBoxCupProduct_eq :
    globalBoxCupProduct a b K L =
      kunnethGlobalMap (inverseImageBaseProjection a) (inverseImageBaseProjection b)
          (fstProjection a b) (sndProjection a b)
          (inverseImageBaseProjection (pullback.fst a b ≫ a))
          (fstProjection_comp a b) (sndProjection_comp a b)
          (globalCupProductCanonical S.toRingedSpace)
          (DerivedCategory.Q.obj (leftComplex a K)) (DerivedCategory.Q.obj (rightComplex b L)) ≫
        (sectionsOverBase (inverseImageBaseProjection (pullback.fst a b ≫ a))).map
          (boxTotalComplexDerivedComparison a b K L)
```

## Tag 0FLT, a lemma

[Tag 0FLT](https://stacks.math.columbia.edu/tag/0FLT) in the Stacks Project.

**`Stacks.Cohomology.BoxKunnethFlat.isIso_globalBoxCupProduct_of_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxKunnethFlat/Isomorphism.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxKunnethFlat/Isomorphism.lean#L131). The attribute's comment: “the whole statement under exactly the source's hypotheses: S affine; X, Y quasi-compact with affine diagonal; F^• bounded (terms vanish outside some [m₁, m₂]); G^• bounded below (terms vanish below some n); every term of F^• and of G^• flat over S. The cup product is the parameter-free map of Tag 0FLR built from the canonical global cup product; nothing the source proves is assumed”.

> **Stacks Project, Tag 0FLT.** Let `a : X ⟶ S` and `b : Y ⟶ S` be morphisms of schemes and
> let `𝓕^•` and `𝓖^•` be complexes of quasi-coherent `𝒪_X`-, respectively `𝒪_Y`-modules whose
> differentials are differential operators of finite order on `X/S` and on `Y/S`. The cup product
> `RΓ(X, 𝓕^•) ⊗^𝐋_A RΓ(Y, 𝓖^•) ⟶ RΓ(X ×_S Y, Tot(𝓕^• ⊠ 𝓖^•))` of [Stacks, Tag 0FLR] is an
> isomorphism in `D(A)` if
>
> 1. `S = Spec(A)` is affine,
> 2. `X` and `Y` are quasi-compact with affine diagonal,
> 3. `𝓕^•` is bounded,
> 4. `𝓖^•` is bounded below,
> 5. every `𝓕^n` is `S`-flat, and
> 6. every `𝓖^m` is `S`-flat.
>
> Here the cup product is `Stacks.Cohomology.BoxKunneth.globalBoxCupProduct`, built from the
> canonical global cup product, with `A` the ring of global sections of `S`.

```lean
theorem isIso_globalBoxCupProduct_of_isFlatOver [IsAffine S] [CompactSpace X] [CompactSpace Y]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    [IsAffineHom (pullback.diagonal (terminal.from Y))]
    (K : CochainComplex (FiniteOrderDifferentialOperatorCategory a) ℤ)
    (L : CochainComplex (FiniteOrderDifferentialOperatorCategory b) ℤ)
    (hK : ∃ m₁ m₂ : ℤ, K.IsStrictlyGE m₁ ∧ K.IsStrictlyLE m₂)
    (hL : ∃ n : ℤ, L.IsStrictlyGE n)
    (hKflat : ∀ n, IsFlatOver a.toLRSHom.toShHom (K.X n).module)
    (hLflat : ∀ n, IsFlatOver b.toLRSHom.toShHom (L.X n).module) :
    IsIso (globalBoxCupProduct a b K L)
```

**`Stacks.Cohomology.BoxKunneth.isIso_globalBoxKunnethMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalKunnethIsomorphism.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/BoxTotalKunnethIsomorphism.lean#L194). The attribute's comment: “the isomorphism; three inputs are carried, so the geometric hypotheses are not consumed: hκ, invertibility of the global cup product on the affine base, which no bare GlobalCupProduct has; hrel, Tag 0FLQ at the two inverse-image complexes; hstep, steps (4) and (5), which the tag's termwise relative S-flatness cannot discharge in this library”.

> **[Stacks, Tag 0FLT].**  Let `a : X ⟶ S` and `b : Y ⟶ S` be morphisms of schemes with `S`
> affine, let `A = Γ(S, 𝒪_S)`, and let `𝓕^•` on `X/S` and `𝓖^•` on `Y/S` be complexes of
> quasi-coherent modules with differentials differential operators of finite order.  If `X` and `Y`
> are quasi-compact with affine diagonal, `𝓕^•` is bounded, `𝓖^•` is bounded below, and every term
> of `𝓕^•` and of `𝓖^•` is flat over `S`, then the cup product of [Stacks, Tag 0FLR]
>
> `RΓ(X, 𝓕^•) ⊗^𝐋_A RΓ(Y, 𝓖^•) ⟶ RΓ(X ×_S Y, Tot(𝓕^• ⊠ 𝓖^•))`
>
> is an isomorphism in `D(A)`.
>
> The three inputs of the proof are carried as the hypotheses `hκ`, `hrel` and `hstep`, and the
> geometric hypotheses are therefore not consumed; the implementation notes of this file say what
> each of the three is and what the source's own dévissage would need in addition.  `hκ` is the
> invertibility of the `A`-linear global cup product on the affine base, `hrel` is
> [Stacks, Tag 0FLQ] at the two inverse-image complexes, and `hstep` is the invertibility of steps
> (4) and (5), in which the source consumes the flatness of the terms.  What is proved here is that
> the three suffice.

```lean
theorem isIso_globalBoxKunnethMap [IsAffine S] [CompactSpace X] [CompactSpace Y]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    [IsAffineHom (pullback.diagonal (terminal.from Y))]
    (_hK : ∀ n, IsFlatOver a.toLRSHom.toShHom (K.X n).module)
    (_hL : ∀ n, IsFlatOver b.toLRSHom.toShHom (L.X n).module)
    (κ : GlobalCupProduct S.toRingedSpace)
    (hκ : IsIso (κ.app
      ((derivedPushforward (inverseImageBaseProjection a)).obj
          (DerivedCategory.Q.obj (leftComplex a K)),
        (derivedPushforward (inverseImageBaseProjection b)).obj
          (DerivedCategory.Q.obj (rightComplex b L)))))
    (hrel : IsIso (Stacks.Cohomology.DerivedKunneth.kunnethMap (inverseImageBaseProjection a)
      (inverseImageBaseProjection b) (fstProjection a b) (sndProjection a b)
      (inverseImageBaseProjection (pullback.fst a b ≫ a)) (fstProjection_comp a b)
      (sndProjection_comp a b) (DerivedCategory.Q.obj (leftComplex a K))
      (DerivedCategory.Q.obj (rightComplex b L))))
    (hstep : IsIso (boxTotalDerivedComparison a b K L n₁ n₂
      (boxTotalComparison a b K L n₁ n₂))) :
    IsIso (globalBoxKunnethMap a b K L n₁ n₂ κ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.24, Tag 0G4A](https://stacks.math.columbia.edu/tag/0G4A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
