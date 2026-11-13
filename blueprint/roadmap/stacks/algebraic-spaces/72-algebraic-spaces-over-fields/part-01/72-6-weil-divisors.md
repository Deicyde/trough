---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.locallyFinite_irreducibleComponents_of_isClosed, AlgebraicGeometry.Space.PrimeDivisor, AlgebraicGeometry.Space.WeilDivisor, AlgebraicGeometry.Space.PrimeDivisor.neighborhoodTotalFractionRingToGeneric_pullback_eq, AlgebraicGeometry.Space.PrimeDivisor.rationalFunctionsToGenericTotalFractionRing, AlgebraicGeometry.Space.PrimeDivisor.injective_rationalFunctionsToGenericTotalFractionRing, AlgebraicGeometry.Space.genericFractionEmbedding, AlgebraicGeometry.Space.PrimeDivisor.isReduced_and_ringKrullDim_eq_one_and_isNoetherianRing_genericHenselianLocalRing
statement: formalized
proof: formalized
---

# 72.6 Weil divisors

Section 72.6 of the Stacks Project, [Tag 0ENI](https://stacks.math.columbia.edu/tag/0ENI). 11 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EE5, a lemma

[Tag 0EE5](https://stacks.math.columbia.edu/tag/0EE5) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyFinite_irreducibleComponents_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianIrreducibleComponents.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianIrreducibleComponents.lean#L45).

> The irreducible components of a closed subset of the space of points of a locally Noetherian
> algebraic space over `S` form a locally finite collection.

```lean
theorem locallyFinite_irreducibleComponents_of_isClosed (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F)
    (hN : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} ↦ IsLocallyNoetherian X))
    (T : Set (points B S hS F)) (hT : IsClosed T) :
    LocallyFinite fun C : irreducibleComponents T ↦ Subtype.val '' (C : Set T)
```

## Tag 0ENJ, a definition

[Tag 0ENJ](https://stacks.math.columbia.edu/tag/0ENJ) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisor.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisor.lean#L75). The attribute's comment: “part (1): prime divisors”.

> **Stacks 0ENJ, part (1).** A *prime divisor* of `X` is an integral closed subspace of `X`
> whose generic point has codimension one in `X`.

```lean
structure PrimeDivisor
```

**`AlgebraicGeometry.Space.WeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisor.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisor.lean#L121). The attribute's comment: “part (2): Weil divisors”.

> **Stacks 0ENJ, part (2).** The group `Div(X)` of *Weil divisors* of `X`: integer
> coefficient families on prime divisors of `X` whose nonzero part has locally finite support
> in `|X|`.

```lean
def WeilDivisor : AddSubgroup (PrimeDivisor B S hS X → ℤ)
```

## Tag 0ENK, a lemma

[Tag 0ENK](https://stacks.math.columbia.edu/tag/0ENK) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.neighborhoodTotalFractionRingToGeneric_pullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldChartIndependence.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldChartIndependence.lean#L149). The attribute's comment: “independence of the canonical map R(X) → Q(𝒪^h\_\{X, ξ}) of the affine elementary étale neighbourhood used to compute it -- a verification the source omits”.

> **Stacks 0ENK, computed on an arbitrary affine chart.** The canonical map from the function
> field of a decent, locally Noetherian, integral algebraic space into the total ring of fractions
> of the henselian local ring at the generic point of a prime divisor is computed on *any* affine
> elementary étale neighbourhood of that generic point, not only on the chart of Stacks 0BBP which
> defines it.

```lean
theorem PrimeDivisor.neighborhoodTotalFractionRingToGeneric_pullback_eq
    [IsLocalRing ↥(Z.genericHenselianLocalRing B S hS hX hdec)]
    (hInt : IsIntegralSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (U : ElementaryEtaleNeighborhood B S hS X hX (Z.genericPoint B S hS X))
    [IsAffine U.scheme.left.1] [IsReduced U.scheme.left.1]
    [IsLocallyNoetherian U.scheme.left.1]
    (r : rationalFunctions B S hS hX) :
    Z.neighborhoodTotalFractionRingToGeneric B S hS hX hdec U
        (rationalFunctionsToTotalFractionRing B S hS hX U.scheme U.toSpace U.etale_toSpace r) =
      Z.rationalFunctionsToGenericTotalFractionRing B S hS hX hdec hInt hN r
```

**`AlgebraicGeometry.Space.PrimeDivisor.rationalFunctionsToGenericTotalFractionRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldEmbedding.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldEmbedding.lean#L177). The attribute's comment: “the canonical map R(X) → Q(𝒪^h\_\{X, ξ}) from the function field into the total ring of fractions of the henselian local ring at the generic point of a prime divisor”.

> The canonical map from the function field of a decent, locally Noetherian, integral algebraic
> space into the total ring of fractions of the henselian local ring at the generic point of a
> prime divisor: a rational function is pulled back to the spectrum of the total ring of fractions
> of the global sections `A` of the chosen affine elementary étale neighbourhood `(U, u)` of the
> generic point, and then pushed along `A → 𝒪_{U, u} → 𝒪^h_{X, ξ}`.

```lean
def PrimeDivisor.rationalFunctionsToGenericTotalFractionRing :
    rationalFunctions B S hS hX →+* Z.genericTotalFractionRing B S hS hX hdec
```

**`AlgebraicGeometry.Space.PrimeDivisor.injective_rationalFunctionsToGenericTotalFractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldEmbedding.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldEmbedding.lean#L192). The attribute's comment: “injectivity of the canonical map R(X) → Q(𝒪^h\_\{X, ξ}), the function field being a field and the total ring of fractions nontrivial”.

> The canonical map from the function field of a decent, locally Noetherian, integral algebraic
> space into the total ring of fractions of the henselian local ring at the generic point of a
> prime divisor is injective.

```lean
theorem PrimeDivisor.injective_rationalFunctionsToGenericTotalFractionRing :
    Function.Injective
      (Z.rationalFunctionsToGenericTotalFractionRing B S hS hX hdec hInt hN)
```

**`AlgebraicGeometry.Space.genericFractionEmbedding`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldEmbedding.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorFunctionFieldEmbedding.lean#L207). The attribute's comment: “the conclusions of the lemma assembled at every prime divisor, as the data the order of vanishing along a prime divisor is defined from”.

> At every prime divisor of a decent, locally Noetherian, integral algebraic space: the
> henselian local ring at the generic point of the prime divisor is a nontrivial Noetherian local
> ring of dimension at most one, and the function field embeds in its total ring of fractions.

```lean
def genericFractionEmbedding : GenericFractionEmbedding B S hS hX hdec
```

**`AlgebraicGeometry.Space.PrimeDivisor.isReduced_and_ringKrullDim_eq_one_and_isNoetherianRing_genericHenselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorHenselianLocalRing.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrimeDivisorHenselianLocalRing.lean#L55). The attribute's comment: “the henselian local ring at the generic point of a prime divisor is a reduced 1-dimensional Noetherian local ring; the canonical injection of the function field into its total ring of fractions is `AlgebraicGeometry.Space.PrimeDivisor.rationalFunctionsToGenericTotalFractionRing`”.

> The henselian local ring at the generic point of a prime divisor of a decent, locally
> Noetherian, integral algebraic space is reduced, of Krull dimension one, and Noetherian.

```lean
theorem
  PrimeDivisor.isReduced_and_ringKrullDim_eq_one_and_isNoetherianRing_genericHenselianLocalRing
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X)
    (hInt : IsIntegralSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (Z : PrimeDivisor B S hS X) :
    _root_.IsReduced ↥(Z.genericHenselianLocalRing B S hS hX hdec) ∧
      ringKrullDim ↥(Z.genericHenselianLocalRing B S hS hX hdec) = 1 ∧
      IsNoetherianRing ↥(Z.genericHenselianLocalRing B S hS hX hdec)
```

## Tag 0ENL, a definition

[Tag 0ENL](https://stacks.math.columbia.edu/tag/0ENL) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.ord_mk'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishing.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishing.lean#L219). The attribute's comment: “the difference-of-lengths formula, on a unit of the total ring of fractions of the henselian local ring at the generic point”.

> The order of vanishing along a prime divisor of a fraction `a / b` of nonzerodivisors of the
> henselian local ring at its generic point is the difference of the lengths of the quotients by
> the ideals `(a)` and `(b)`.
>
> This is the defining formula of the order of vanishing, computed on the total ring of fractions
> of the henselian local ring.

```lean
theorem PrimeDivisor.ord_mk'
    (a b : nonZeroDivisors ↥(Z.genericHenselianLocalRing B S hS hX hdec))
    (hu : IsUnit (IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hdec)
      (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec)) b)) :
    Z.ord B S hS hX hdec (IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hdec)
        (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec)) b) hu =
      ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
          (a : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ) -
        ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hdec)
          (b : ↥(Z.genericHenselianLocalRing B S hS hX hdec))).toNat : ℤ)
```

**`AlgebraicGeometry.Space.ordRationalFunction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishingRationalFunction.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishingRationalFunction.lean#L88). The attribute's comment: “ord\_Z(f) for an invertible rational function f on a locally Noetherian integral algebraic space, at the hypotheses of the source; the defining difference-of-lengths formula is `AlgebraicGeometry.Space.ordRationalFunction_eq_length_sub_length`”.

> **Stacks 0ENL.** The *order of vanishing of `f` along `Z`*, for `f` an invertible rational
> function on a locally Noetherian integral algebraic space `X` and `Z` a prime divisor of `X`:
> the order of vanishing, along `Z`, of the image of `f` in the total ring of fractions of the
> henselian local ring at the generic point of `Z` under the canonical injection of Stacks 0ENK.
>
> The hypotheses are those of the source and no others — the conclusions of Stacks 0ENK are
> discharged by `AlgebraicGeometry.Space.genericFractionEmbedding`, and decency comes from
> integrality by Stacks 0AD4 — and the defining difference of lengths is
> `AlgebraicGeometry.Space.ordRationalFunction_eq_length_sub_length`.

```lean
abbrev ordRationalFunction (f : (rationalFunctions B S hS hX)ˣ)
    (Z : PrimeDivisor B S hS X) : ℤ
```

**`AlgebraicGeometry.Space.ordRationalFunction_eq_length_sub_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishingRationalFunction.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishingRationalFunction.lean#L102). The attribute's comment: “the difference-of-lengths formula defining ord\_Z(f), on an arbitrary presentation of the image of f in Q(𝒪^h\_\{X, ξ}) as a ratio of nonzerodivisors; hence also the independence of the presentation, which the source cites Algebra, Lemma 02MC for”.

> **Stacks 0ENL, the defining formula.** If the image of `f` in `Q(𝒪^h_{X, ξ})` is the ratio
> `a / b` of nonzerodivisors `a` and `b` of `𝒪^h_{X, ξ}`, then `ord_Z(f)` is the difference of the
> lengths of `𝒪^h_{X, ξ} / a 𝒪^h_{X, ξ}` and `𝒪^h_{X, ξ} / b 𝒪^h_{X, ξ}`.
>
> The hypothesis is placed on an arbitrary such presentation, so this is simultaneously the
> formula the source defines `ord_Z(f)` by and the independence of that formula from the choice
> of `a` and `b`, which the source takes from Algebra, Lemma 02MC.

```lean
theorem ordRationalFunction_eq_length_sub_length (f : (rationalFunctions B S hS hX)ˣ)
    (Z : PrimeDivisor B S hS X)
    (a b : nonZeroDivisors ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace))
    (hab : Z.rationalFunctionsToGenericTotalFractionRing B S hS hX hInt.isDecentSpace hInt hN
        (f : rationalFunctions B S hS hX) =
      IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hInt.isDecentSpace)
        (a : ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace)) b) :
    ordRationalFunction B S hS hX hInt hN f Z =
      ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace)
          (a : ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace))).toNat : ℤ) -
        ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace)
          (b : ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace))).toNat : ℤ)
```

**`AlgebraicGeometry.Space.exists_ordRationalFunction_eq_length_sub_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishingRationalFunction.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OrderOfVanishingRationalFunction.lean#L141). The attribute's comment: “existence of the presentation a/b by nonzerodivisors of the image of f in Q(𝒪^h\_\{X, ξ}), which is what makes the difference of lengths an admissible description of ord\_Z(f)”.

> **Stacks 0ENL, well-definedness.** The image of an invertible rational function `f` in
> `Q(𝒪^h_{X, ξ})` *is* a ratio `a / b` of nonzerodivisors of `𝒪^h_{X, ξ}`, and for one — hence,
> by `AlgebraicGeometry.Space.ordRationalFunction_eq_length_sub_length`, for every — such
> presentation `ord_Z(f)` is the difference of the lengths of `𝒪^h_{X, ξ} / a 𝒪^h_{X, ξ}` and
> `𝒪^h_{X, ξ} / b 𝒪^h_{X, ξ}`.
>
> The source defines `ord_Z(f)` *by* that difference, for `a` and `b` nonzerodivisors such that
> the image of `f` is `a / b`, so the existence of such a pair is what makes the difference of
> lengths an admissible description of `ord_Z(f)`. Invertibility of `f` is what produces it: the
> image of `f` is a unit of the total ring of fractions, and the numerator of any presentation of
> a unit is again a nonzerodivisor.

```lean
theorem exists_ordRationalFunction_eq_length_sub_length (f : (rationalFunctions B S hS hX)ˣ)
    (Z : PrimeDivisor B S hS X) :
    ∃ a b : nonZeroDivisors ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace),
      Z.rationalFunctionsToGenericTotalFractionRing B S hS hX hInt.isDecentSpace hInt hN
            (f : rationalFunctions B S hS hX) =
          IsLocalization.mk' (Z.genericTotalFractionRing B S hS hX hInt.isDecentSpace)
            (a : ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace)) b ∧
        ordRationalFunction B S hS hX hInt hN f Z =
          ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace)
              (a : ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace))).toNat : ℤ) -
            ((Ring.ord ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace)
              (b : ↥(Z.genericHenselianLocalRing B S hS hX hInt.isDecentSpace))).toNat : ℤ)
```

## Tag 0ENM, a lemma

[Tag 0ENM](https://stacks.math.columbia.edu/tag/0ENM) in the Stacks Project.

**`AlgebraicGeometry.Space.PrimeDivisor.ord_eq_ord_schematicLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusOrderOfVanishing.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusOrderOfVanishing.lean#L108). The attribute's comment: “the order of vanishing along a prime divisor `Z` meeting the schematic locus is the order of vanishing, in the sense of Divisors 02RJ, of the restriction of `f` to a scheme `X'` representing the schematic locus, at the point of `X'` over the generic point of `Z`”.

> **Stacks 0ENM.** Let `S` be a scheme, let `X` be a locally Noetherian integral algebraic
> space over `S` and let `f ∈ R(X)^*`. Let `Z ⊂ X` be a prime divisor meeting the schematic locus
> of `X`, and let `X'` be a scheme representing the schematic locus, through an isomorphism
> `e : h_{X'} ≅ (schematicLocus X)`, so that `X' ⟶ X` is an open immersion; such an `X'` exists
> by Stacks 03JH,
> `AlgebraicGeometry.Space.isOpenSubspace_and_isRepresentable_schematicLocus_of_isAlgebraicSpace`.
> Then:
>
> * the generic point `ξ` of `Z` is the image of a point `ξ'` of `X'`;
> * for every such `ξ'` (it is unique, `X' ⟶ X` being a monomorphism), the scheme `X'` is integral
>   and locally Noetherian, `ξ'` has codimension one in `X'`, so that it is the generic point of
>   the prime divisor `Z ∩ X'` of `X'`, the restriction `f|_{X'}` of `f` to `X'` exists in the
>   function field of `X'`, and for it `ord_Z(f) = ord_{ξ'}(f|_{X'})`: the order of vanishing of
>   Definition 0ENL agrees with the order of vanishing of Divisors, Definition 02RJ, on the scheme
>   `X'`.
>
> Integrality of `X` includes decency (Stacks 0AD4, `AlgebraicGeometry.Space.IsIntegralSpace`),
> which the henselian local ring of Definition 0ENL is built from; it is taken from `hInt`.
>
> The point `ξ'` exists because the point set of the schematic locus is open in `|X|` and meets
> `|Z|`, so contains its generic point. The comparison is
> `AlgebraicGeometry.Space.PrimeDivisor.ord_eq_scheme_ord_of_isOpenImmersion`: on an affine open of
> `X'` around `ξ'` the henselian local ring `𝒪^h_{X, ξ}` is a henselization of `𝒪_{X', ξ'}`, which
> preserves the lengths both orders of vanishing are differences of.

```lean
theorem PrimeDivisor.ord_eq_ord_schematicLocus (hInt : IsIntegralSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (Z : PrimeDivisor B S hS X)
    (hmeet : (Z.support B S hS X ∩
      subspacePointSet B S hS X (schematicLocus B S hS X)).Nonempty)
    {W : BigFppfOver B S hS} (e : yoneda.obj W ≅ (schematicLocus B S hS X).toFunctor)
    (f : (rationalFunctions B S hS hX)ˣ) :
    (∃ ξ' : (BigFppfOver.toScheme B S hS).obj W,
      pointsMap B S hS (yoneda.obj W) (e.hom ≫ (schematicLocus B S hS X).ι)
        ((pointsEquivScheme B S hS W).symm ξ') = Z.genericPoint B S hS X) ∧
    ∀ ξ' : (BigFppfOver.toScheme B S hS).obj W,
      pointsMap B S hS (yoneda.obj W) (e.hom ≫ (schematicLocus B S hS X).ι)
        ((pointsEquivScheme B S hS W).symm ξ') = Z.genericPoint B S hS X →
      ∃ (_ : IsIntegral ((BigFppfOver.toScheme B S hS).obj W))
        (_ : IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj W)),
        coheight ξ' = 1 ∧
        (∃ f' : ((BigFppfOver.toScheme B S hS).obj W).functionField,
          IsOpenChartRestriction B S hS hX (e.hom ≫ (schematicLocus B S hS X).ι)
            (isOpenImmersion_hom_comp_schematicLocus_ι B S hS hX e)
            (f : rationalFunctions B S hS hX) f') ∧
        ∀ f' : ((BigFppfOver.toScheme B S hS).obj W).functionField,
          IsOpenChartRestriction B S hS hX (e.hom ≫ (schematicLocus B S hS X).ι)
            (isOpenImmersion_hom_comp_schematicLocus_ι B S hS hX e)
            (f : rationalFunctions B S hS hX) f' →
          (genericFractionEmbedding B S hS hX (hInt.isDecentSpace B S hS X) hInt hN).ord f Z =
            ((BigFppfOver.toScheme B S hS).obj W).ord f' ξ'
```

## Tag 0ENN, a lemma

[Tag 0ENN](https://stacks.math.columbia.edu/tag/0ENN) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyFinite_principalDivisorCoefficients_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L288). The attribute's comment: “the second set: the prime divisors with ord\_Z(f) ≠ 0 are locally finite. The first set, the prime divisors at whose generic point f is not regular, is locallyFinite\_primeDivisor\_not\_isDefinedAt”.

> **Stacks 0ENN, the second set.** The prime divisors of `X` along which a rational function
> `f` has nonzero order of vanishing are locally finite in `|X|`, given a nonempty open subset of
> `|X|` over which `f` is invertible.
>
> This is the source's argument. Such a prime divisor has its generic point outside the open set,
> by `AlgebraicGeometry.Space.genericPoint_notMem_of_principalDivisorCoefficients_ne_zero`, so its
> point set is an irreducible component of the closed complement — codimension one leaves no room
> for a larger irreducible closed subset of that complement — and the irreducible components of a
> closed set are locally finite by Stacks 0EE5. Both steps are
> `AlgebraicGeometry.Space.locallyFinite_primeDivisor_of_genericPoint_notMem`, already in the
> library in exactly this generality; it is also the Stacks 0EE5 step in the proof of Stacks
> 0EPS.

```lean
theorem locallyFinite_principalDivisorCoefficients_ne_zero
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (hirr : IrreducibleSpace (points B S hS X))
    (emb : ∀ W : PrimeDivisor B S hS X, rationalFunctions B S hS hX →+*
      W.genericTotalFractionRing B S hS hX hdec)
    (f : rationalFunctions B S hS hX)
    (hf : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W f))
    (U : Set (points B S hS X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hreg : ∀ W : PrimeDivisor B S hS X, W.genericPoint B S hS X ∈ U →
      ∃ r : ↥(W.genericHenselianLocalRing B S hS hX hdec), IsUnit r ∧
        emb W f = algebraMap _ (W.genericTotalFractionRing B S hS hX hdec) r) :
    LocallyFinite fun W : PrimeDivisor B S hS X =>
      if principalDivisorCoefficients B S hS hX hdec emb f hf W = 0 then ∅
      else W.support B S hS X
```

**`AlgebraicGeometry.Space.locallyFinite_primeDivisor_not_isDefinedAt_and_ordRationalFunction_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvertibleRationalFunctionUnitLocus.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InvertibleRationalFunctionUnitLocus.lean#L296). The attribute's comment: “both collections, with the source's hypotheses only: the prime divisors at whose generic point f is not defined (f ∉ 𝒪\_\{X,ξ}) and those with ord\_Z(f) ≠ 0 are locally finite”.

> **Stacks 0ENN.** Let `X` be a locally Noetherian integral algebraic space over `S` and let
> `f ∈ R(X)^*`. Then the prime divisors `Z` of `X` whose generic point `ξ` has `f ∉ 𝒪_{X, ξ}` —
> `f` not defined at `ξ` in the sense of Stacks 0EMQ — and the prime divisors `Z` with
> `ord_Z(f) ≠ 0`, for the order of vanishing of Stacks 0ENL, are both locally finite collections
> in `|X|`.
>
> As in the source, both follow from Stacks 0EE5 once the generic points of the prime divisors in
> question avoid a nonempty open. For the first collection that open is the domain of a
> representative of `f`, which is
> `AlgebraicGeometry.Space.locallyFinite_primeDivisor_not_isDefinedAt`; for the second it is the
> open on which `f` is a unit section, which is
> `AlgebraicGeometry.Space.ordRationalFunction_mem_weilDivisor`.

```lean
theorem locallyFinite_primeDivisor_not_isDefinedAt_and_ordRationalFunction_ne_zero
    (f : (rationalFunctions B S hS hX)ˣ) :
    LocallyFinite (fun Z : {Z : PrimeDivisor B S hS X //
        ¬ RationalMap.IsDefinedAt B S hS (f : rationalFunctions B S hS hX)
          (Z.genericPoint B S hS X)} ↦ Z.1.support B S hS X) ∧
    LocallyFinite (fun Z : {Z : PrimeDivisor B S hS X //
        ordRationalFunction B S hS hX hInt hN f Z ≠ 0} ↦ Z.1.support B S hS X)
```

## Tag 0ENP, a definition

[Tag 0ENP](https://stacks.math.columbia.edu/tag/0ENP) in the Stacks Project.

**`AlgebraicGeometry.Space.principalDivisorCoefficients`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L219). The attribute's comment: “the coefficients ord\_Z(f) of div(f); the embeddings R(X) → Q(O^h\_\{X,ξ}) of Stacks 0ENK are the parameter emb, as they are for Stacks 0EPT”.

> **Stacks 0ENP, the coefficients.** The coefficients `ord_Z(f)` of the principal divisor
> `div(f) = ∑_Z ord_Z(f) [Z]` of a rational function `f` on `X`, indexed by the prime divisors of
> `X`: the coefficient at `Z` is the order of vanishing along `Z` of the image of `f` in the total
> ring of fractions of `𝒪^h_{X,ξ}`.
>
> The embeddings `R(X) → Q(𝒪^h_{X,ξ})` of Stacks 0ENK are the parameter `emb`, as in Stacks 0EPT;
> regularity of `f` is the hypothesis `hf` that each image is a unit.

```lean
def principalDivisorCoefficients
    (emb : ∀ W : PrimeDivisor B S hS X, rationalFunctions B S hS hX →+*
      W.genericTotalFractionRing B S hS hX hdec)
    (f : rationalFunctions B S hS hX)
    (hf : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W f)) :
    PrimeDivisor B S hS X → ℤ
```

**`AlgebraicGeometry.Space.principalWeilDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L320). The attribute's comment: “div(f) = ∑ ord\_Z(f) [Z] as an element of Div(X); local finiteness is Stacks 0ENN, the argument hfin, discharged by locallyFinite\_principalDivisorCoefficients\_ne\_zero in principalWeilDivisorOfRegularLocus; the embeddings of Stacks 0ENK are the parameter emb”.

> **Stacks 0ENP.** The *principal divisor associated to `f ∈ R(X)^*`*, that is
> `div(f) = ∑_Z ord_Z(f) [Z]`, as an element of `Div(X)`.
>
> That the sum makes sense is Stacks 0ENN, the argument `hfin`, which
> `AlgebraicGeometry.Space.locallyFinite_principalDivisorCoefficients_ne_zero` proves and
> `AlgebraicGeometry.Space.principalWeilDivisorOfRegularLocus` discharges from a nonempty open
> subset of `|X|` over which `f` is invertible.

```lean
def principalWeilDivisor
    (emb : ∀ W : PrimeDivisor B S hS X, rationalFunctions B S hS hX →+*
      W.genericTotalFractionRing B S hS hX hdec)
    (f : rationalFunctions B S hS hX)
    (hf : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W f))
    (hfin : LocallyFinite fun W : PrimeDivisor B S hS X =>
      if principalDivisorCoefficients B S hS hX hdec emb f hf W = 0 then ∅
      else W.support B S hS X) :
    WeilDivisor B S hS X
```

**`AlgebraicGeometry.Space.principalWeilDivisorOfRegularLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L352). The attribute's comment: “div(f) in Div(X), with local finiteness (Stacks 0ENN) discharged here: it is proved from a nonempty open U over which f is invertible, the datum (U, hUopen, hUne, hreg) that is the first sentence of the source's own proof of Stacks 0ENN”.

> **Stacks 0ENP.** The principal divisor `div(f) = ∑_Z ord_Z(f) [Z]` of a rational function
> `f ∈ R(X)^*` as an element of `Div(X)`, with the local finiteness of Stacks 0ENN supplied from a
> nonempty open subset of `|X|` over which `f` is invertible.

```lean
def principalWeilDivisorOfRegularLocus
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (hirr : IrreducibleSpace (points B S hS X))
    (emb : ∀ W : PrimeDivisor B S hS X, rationalFunctions B S hS hX →+*
      W.genericTotalFractionRing B S hS hX hdec)
    (f : rationalFunctions B S hS hX)
    (hf : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W f))
    (U : Set (points B S hS X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hreg : ∀ W : PrimeDivisor B S hS X, W.genericPoint B S hS X ∈ U →
      ∃ r : ↥(W.genericHenselianLocalRing B S hS hX hdec), IsUnit r ∧
        emb W f = algebraMap _ (W.genericTotalFractionRing B S hS hX hdec) r) :
    WeilDivisor B S hS X
```

**`AlgebraicGeometry.Space.principalWeilDivisorOfUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrincipalWeilDivisorOfUnit.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PrincipalWeilDivisorOfUnit.lean#L144). The attribute's comment: “div(f) = ∑ ord\_Z(f) [Z] as an element of Div(X), for X a locally Noetherian integral algebraic space over S and f ∈ R(X)^*: the order of vanishing of Stacks 0ENL along the canonical embedding R(X) → Q(O^h\_\{X,ξ}) of Stacks 0ENK, whose ring-theoretic properties are proved; the local finiteness of Stacks 0ENN is proved, nothing is carried”.

> The *principal Weil divisor associated to `f ∈ R(X)^*`*,
> `div(f) = div_X(f) = ∑_Z ord_Z(f) [Z]`, as an element of `Div(X)`, for `X` a locally Noetherian
> integral algebraic space over `S`.
>
> The sum is over the prime divisors of `X`, and `ord_Z(f)` is the order of vanishing of Stacks
> 0ENL, taken along the canonical embedding `R(X) → Q(𝒪^h_{X, ξ})` of Stacks 0ENK
> (`AlgebraicGeometry.Space.genericFractionEmbedding`).

```lean
def principalWeilDivisorOfUnit (f : (rationalFunctions B S hS hX)ˣ) :
    ↥(WeilDivisor B S hS X)
```

**`AlgebraicGeometry.Space.divRationalFunction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrincipalWeilDivisorRationalFunction.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PrincipalWeilDivisorRationalFunction.lean#L70). The attribute's comment: “div\_X(f) = ∑ ord\_Z(f) [Z] as a Weil divisor, at the hypotheses of the source: the order of vanishing is the canonical one of Stacks 0ENL and the local finiteness is Stacks 0ENN, both proved”.

> **Stacks 0ENP.** The *principal Weil divisor* `div_X(f) = ∑ ord_Z(f) [Z]` of an invertible
> rational function `f` on a locally Noetherian integral algebraic space `X`, the sum running over
> the prime divisors `Z` of `X` and `ord_Z(f)` being the order of vanishing of Stacks 0ENL. It is
> a Weil divisor by Stacks 0ENN, which is
> `AlgebraicGeometry.Space.ordRationalFunction_mem_weilDivisor`.

```lean
abbrev divRationalFunction (f : (rationalFunctions B S hS hX)ˣ) : ↥(WeilDivisor B S hS X)
```

## Tag 0ENQ, a lemma

[Tag 0ENQ](https://stacks.math.columbia.edu/tag/0ENQ) in the Stacks Project.

**`AlgebraicGeometry.Space.principalWeilDivisor_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L422). The attribute's comment: “div(fg) = div(f) + div(g) in Div(X)”.

> **Stacks 0ENQ.** The principal divisor of a product of rational functions is the sum of
> their principal divisors, `div(fg) = div(f) + div(g)` in `Div(X)`.
>
> Local finiteness for `fg` is not assumed: it is deduced from local finiteness for `f` and for
> `g`, which is what makes `div(f)` and `div(g)` elements of `Div(X)` in the first place.

```lean
theorem principalWeilDivisor_mul
    (emb : ∀ W : PrimeDivisor B S hS X, rationalFunctions B S hS hX →+*
      W.genericTotalFractionRing B S hS hX hdec)
    (f g : rationalFunctions B S hS hX)
    (hf : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W f))
    (hg : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W g))
    (hfg : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W (f * g)))
    (hfinf : LocallyFinite fun W : PrimeDivisor B S hS X =>
      if principalDivisorCoefficients B S hS hX hdec emb f hf W = 0 then ∅
      else W.support B S hS X)
    (hfing : LocallyFinite fun W : PrimeDivisor B S hS X =>
      if principalDivisorCoefficients B S hS hX hdec emb g hg W = 0 then ∅
      else W.support B S hS X) :
    principalWeilDivisor B S hS hX hdec emb (f * g) hfg
        (locallyFinite_principalDivisorCoefficients_mul B S hS hX hdec emb f g hf hg hfg hfinf
          hfing) =
      principalWeilDivisor B S hS hX hdec emb f hf hfinf +
        principalWeilDivisor B S hS hX hdec emb g hg hfing
```

**`AlgebraicGeometry.Space.principalWeilDivisorOfRegularLocus_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L504). The attribute's comment: “div(fg) = div(f) + div(g) in Div(X), local finiteness proved throughout”.

> **Stacks 0ENQ.** The principal divisor of a product of rational functions is the sum of
> their principal divisors, `div(fg) = div(f) + div(g)` in `Div(X)`, with the local finiteness of
> Stacks 0ENN proved for all three divisors from a nonempty open subset of `|X|` over which both
> `f` and `g` are invertible.

```lean
theorem principalWeilDivisorOfRegularLocus_mul
    (hN : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (hirr : IrreducibleSpace (points B S hS X))
    (emb : ∀ W : PrimeDivisor B S hS X, rationalFunctions B S hS hX →+*
      W.genericTotalFractionRing B S hS hX hdec)
    (f g : rationalFunctions B S hS hX)
    (hf : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W f))
    (hg : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W g))
    (hfg : ∀ W : PrimeDivisor B S hS X, IsUnit (emb W (f * g)))
    (U : Set (points B S hS X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hregf : ∀ W : PrimeDivisor B S hS X, W.genericPoint B S hS X ∈ U →
      ∃ r : ↥(W.genericHenselianLocalRing B S hS hX hdec), IsUnit r ∧
        emb W f = algebraMap _ (W.genericTotalFractionRing B S hS hX hdec) r)
    (hregg : ∀ W : PrimeDivisor B S hS X, W.genericPoint B S hS X ∈ U →
      ∃ r : ↥(W.genericHenselianLocalRing B S hS hX hdec), IsUnit r ∧
        emb W g = algebraMap _ (W.genericTotalFractionRing B S hS hX hdec) r) :
    principalWeilDivisorOfRegularLocus B S hS hX hdec hN hirr emb (f * g) hfg U hUopen hUne
        (exists_isUnit_emb_mul_eq_algebraMap B S hS hX hdec emb f g U hregf hregg) =
      principalWeilDivisorOfRegularLocus B S hS hX hdec hN hirr emb f hf U hUopen hUne hregf +
        principalWeilDivisorOfRegularLocus B S hS hX hdec hN hirr emb g hg U hUopen hUne hregg
```

**`AlgebraicGeometry.Space.divRationalFunction_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrincipalWeilDivisorRationalFunction.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PrincipalWeilDivisorRationalFunction.lean#L96). The attribute's comment: “div\_X(fg) = div\_X(f) + div\_X(g) as Weil divisors on X, at the hypotheses of the source only”.

> **Stacks 0ENQ.** Let `X` be a locally Noetherian integral algebraic space over `S` and let
> `f, g ∈ R(X)^*`. Then `div_X(fg) = div_X(f) + div_X(g)` as Weil divisors on `X`.
>
> As in the source this is the additivity of the order of vanishing,
> `AlgebraicGeometry.Space.GenericFractionEmbedding.ord_mul_apply`, at every prime divisor.

```lean
theorem divRationalFunction_mul (f g : (rationalFunctions B S hS hX)ˣ) :
    divRationalFunction B S hS hX hInt hN (f * g) =
      divRationalFunction B S hS hX hInt hN f + divRationalFunction B S hS hX hInt hN g
```

**`AlgebraicGeometry.Space.GenericFractionEmbedding.ord_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroup.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroup.lean#L146). The attribute's comment: “additivity of the principal Weil divisor, read on the coefficient families over the prime divisors; this form needs no hypothesis beyond the embedding of Stacks 0ENK”.

> **Stacks 0ENQ.** The order of vanishing of a product of invertible rational functions is
> the sum of the orders of vanishing, as coefficient families on the prime divisors of `X`.
>
> This is the equation `div(fg) = div(f) + div(g)` of the source, read on the coefficient families
> of which the two sides of that equation are the Weil divisors.

```lean
theorem ord_mul (f g : (rationalFunctions B S hS hX)ˣ) :
    E.ord (f * g) = E.ord f + E.ord g
```

## Tag 0ENR, a definition

[Tag 0ENR](https://stacks.math.columbia.edu/tag/0ENR) in the Stacks Project.

**`AlgebraicGeometry.Space.GenericFractionEmbedding.principalWeilDivisors`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroup.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroup.lean#L190). The attribute's comment: “the subgroup of principal Weil divisors, by which the class group is formed”.

> **Stacks 0ENR.** The subgroup of `Div(X)` of principal Weil divisors: they contain zero and
> are closed under addition and negation by the additivity of the order of vanishing, which is
> Stacks 0ENQ.

```lean
def principalWeilDivisors : AddSubgroup ↥(WeilDivisor B S hS X)
```

**`AlgebraicGeometry.Space.GenericFractionEmbedding.weilDivisorClassGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroup.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroup.lean#L213). The attribute's comment: “the Weil divisor class group as the quotient of the Weil divisors by the principal Weil divisors”.

> **Stacks 0ENR.** The *Weil divisor class group* `Cl(X)` of `X`: the group of Weil divisors
> on `X` modulo the subgroup of principal Weil divisors.

```lean
abbrev weilDivisorClassGroup : Type (u + 1)
```

**`AlgebraicGeometry.Space.weilDivisorClassGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroupCanonical.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/WeilDivisorClassGroupCanonical.lean#L97). The attribute's comment: “Cl(X) = Div(X) / \{div(f) : f ∈ R(X)^*}, at the source's hypotheses only: the principal divisors are the range of the homomorphism div of Stacks 0ENP and 0ENQ, built from the canonical order of vanishing”.

> **Stacks 0ENR.** The *Weil divisor class group* `Cl(X)` of a locally Noetherian integral
> algebraic space `X` over `S`: the quotient of the group `Div(X)` of Weil divisors by the
> subgroup of principal Weil divisors `div(f)`, `f ∈ R(X)^*`.

```lean
abbrev weilDivisorClassGroup : Type (u + 1)
```

## Tag 0ENT, an example

[Tag 0ENT](https://stacks.math.columbia.edu/tag/0ENT) in the Stacks Project.

**`AlgebraicGeometry.AffineLineInvolution.involutionQuotient_classGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionClassGroup.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionClassGroup.lean#L300).

> **Stacks 0ENT.** Let `k` be a field of characteristic different from two and let
> `X = 𝔸¹_k/\{t ∼ -t ∣ t ≠ 0\}` be the algebraic space of Stacks 02Z1, the quotient of the affine
> line by the punctured graph of negation. Then:
>
> 1. `X` is an algebraic space, smooth over `k`;
> 2. the morphism `X → 𝔸¹_k = Spec k[t]` descended from squaring the coordinate is a universal
>    homeomorphism which is an isomorphism over `𝔸¹_k ∖ {0}`;
> 3. `X` is Noetherian and integral, and `|X|` has dimension one;
> 4. the prime divisors of `X` are the closed points of `X`, a prime divisor corresponding to its
>    generic point;
> 5. the prime divisor `x` of `X` over the origin is a closed point, and the unique point of `X`
>    over `0 ∈ 𝔸¹_k`;
> 6. the classes in `Cl(X)` of the prime divisors other than `x` are zero;
> 7. the divisor of `t` on `X` is `2 [x]`;
> 8. `Cl(X) ≅ ℤ/2ℤ`, by an isomorphism sending `[x]` to `1`.
>
> Here `Cl(X)` is the Weil divisor class group of Stacks 0ENR, and `t` is the coordinate of the
> affine line, pulled back to a rational function on `X`.
>
> The characteristic hypothesis is that of Stacks 02Z1, where `X` is constructed, which Stacks 05Z6
> and Stacks 0ENT continue: in characteristic two the graph of negation is the diagonal, so the
> relation `Δ ⨿ Γ ⟶ 𝔸¹_k ×_k 𝔸¹_k` is not a monomorphism and the construction does not produce an
> equivalence relation at all. The hypothesis `hZ` that the big fppf site contains the final scheme
> is the one under which `AlgebraicGeometry.Space.IsNoetherian` is formulated.

```lean
theorem involutionQuotient_classGroup (hchar : (2 : k) ≠ 0) (hZ : B.Contains (⊤_ Scheme.{u})) :
    IsAlgebraicSpace B (Spec (.of k)) hk (involutionQuotient k B hk).obj ∧
      Space.IsSmooth B (Spec (.of k)) hk (terminal.from (involutionQuotient k B hk).obj) ∧
      Space.UniversalHomeomorphism B (Spec (.of k)) hk (squaringMap k B hk) ∧
      IsIso (pullback.snd (squaringMap k B hk) (Space.puncturedLineInclusion k B hk)) ∧
      Space.IsNoetherian B (Spec (.of k)) hk hZ (involutionQuotient k B hk).obj ∧
      Space.IsIntegralSpace B (Spec (.of k)) hk (involutionQuotient k B hk).obj ∧
      topologicalKrullDim (Space.points B (Spec (.of k)) hk (involutionQuotient k B hk).obj) = 1 ∧
      (∃ e : Space.PrimeDivisor B (Spec (.of k)) hk (involutionQuotient k B hk).obj ≃
          {ξ : Space.points B (Spec (.of k)) hk (involutionQuotient k B hk).obj //
            IsClosed ({ξ} : Set _)},
        ∀ Z, (e Z : Space.points B (Spec (.of k)) hk _) = Z.genericPoint B (Spec (.of k)) hk _) ∧
      IsClosed ({(originDivisor k B hk hchar hZ).genericPoint B (Spec (.of k)) hk _} :
        Set (Space.points B (Spec (.of k)) hk (involutionQuotient k B hk).obj)) ∧
      (∀ ξ : Space.points B (Spec (.of k)) hk (involutionQuotient k B hk).obj,
        Space.pointsHomeomorphAffineLine (squaringMap k B hk)
            (universalHomeomorphism_squaringMap k B hk hchar) ξ = origin k ↔
          ξ = (originDivisor k B hk hchar hZ).genericPoint B (Spec (.of k)) hk _) ∧
      (∀ Z : Space.PrimeDivisor B (Spec (.of k)) hk (involutionQuotient k B hk).obj,
        Z ≠ originDivisor k B hk hchar hZ →
          (Space.primeDivisorClass Z : Space.weilDivisorClassGroup B (Spec (.of k)) hk
            (isAlgebraicSpace_involutionQuotient k hchar B hk)
            (isIntegralSpace_involutionQuotient k B hk hchar hZ)
            (hasEtaleLocalProperty_isLocallyNoetherian k B hk hchar)) = 0) ∧
      Space.divRationalFunction B (Spec (.of k)) hk
          (isAlgebraicSpace_involutionQuotient k hchar B hk)
          (isIntegralSpace_involutionQuotient k B hk hchar hZ)
          (hasEtaleLocalProperty_isLocallyNoetherian k B hk hchar)
          (Space.coordinatePullbackUnit (squaringMap k B hk)
            (isAlgebraicSpace_involutionQuotient k hchar B hk)
            (isIntegralSpace_involutionQuotient k B hk hchar hZ)
            (isIso_squaringMap_pullback_puncturedAffineLine k hchar B hk)) =
        2 • Space.primeDivisorClass (originDivisor k B hk hchar hZ) ∧
      ∃ e : Space.weilDivisorClassGroup B (Spec (.of k)) hk
          (isAlgebraicSpace_involutionQuotient k hchar B hk)
          (isIntegralSpace_involutionQuotient k B hk hchar hZ)
          (hasEtaleLocalProperty_isLocallyNoetherian k B hk hchar) ≃+ ZMod 2,
        e (Space.primeDivisorClass (originDivisor k B hk hchar hZ)) = 1
```

**`AlgebraicGeometry.AffineLineInvolution.isNoetherian_involutionQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionNoetherian.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionNoetherian.lean#L69). The attribute's comment: “the Noetherian property”.

> Away from characteristic two, the quotient of the affine line by the punctured graph of
> negation is a Noetherian algebraic space over the ground field: it is quasi-compact,
> quasi-separated and locally Noetherian.

```lean
theorem isNoetherian_involutionQuotient (hchar : (2 : k) ≠ 0) (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of k))) (hZ : B.Contains (⊤_ Scheme.{u}))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    Space.IsNoetherian B (Spec (.of k)) hS hZ (involutionQuotient k B hS).obj
```

**`AlgebraicGeometry.AffineLineInvolution.isSmooth_involutionQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuotient.lean, line 583](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuotient.lean#L583). The attribute's comment: “smoothness”.

> **Stacks 0ENT.** Away from characteristic two, the quotient of the affine line by the
> punctured graph of negation is smooth over the ground field.
>
> Smoothness is tested on the quotient chart, which is a surjective étale chart of the
> quotient by Stacks 0265, and on the affine line itself, which is smooth over the base.

```lean
theorem isSmooth_involutionQuotient (hchar : (2 : k) ≠ 0) (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    Space.IsSmooth B (Spec (.of k)) hS
      (terminal.from (involutionQuotient k B hS).obj)
```

## Tag 0ENU, an example

[Tag 0ENU](https://stacks.math.columbia.edu/tag/0ENU) in the Stacks Project.

**`AlgebraicGeometry.CoordinateAxesQuotient.coordinateAxesQuotient_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoordinateAxesQuotientClassGroup.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoordinateAxesQuotientClassGroup.lean#L271).

> **Stacks 0ENU.** Let `k` be a field, `U = Spec (k[x, y]/(xy))` the union of the coordinate
> axes, `σ` the automorphism exchanging them, and `R = Δ(U) ⨿ Δ'(U ∖ {0_U})` where `Δ'` is the graph
> `u ↦ (u, σ(u))`. Then:
> 1. `R` is an étale equivalence relation on `U`, and `X = U/R` is an algebraic space;
> 2. the morphism `U → 𝔸¹_k`, `(x, y) ↦ x + y`, is `R`-invariant and defines `π : X → 𝔸¹_k`;
> 3. `π` is a universal homeomorphism and an isomorphism over `𝔸¹_k ∖ {0}`;
> 4. `X` is integral and Noetherian;
> 5. as in Stacks 0ENT, the prime divisors of `X` are its closed points, the point `x` of `X` over
>    `0 ∈ 𝔸¹_k` is closed and is the only point over `0`, the divisor of `t` is `2 [x]`, the class of
>    every other prime divisor is zero, and `Cl(X) ≅ ℤ/2ℤ` by an isomorphism sending `[x]` to `1`;
> 6. the henselian local ring of `X` at `x` is a henselization of `𝒪_{U, 0_U}`, and it is not a
>    domain.
> No hypothesis is put on the field. The hypothesis `hZ` that the big fppf site contains the
> final scheme is the one under which `AlgebraicGeometry.Space.IsNoetherian` is formulated; the
> integrality, the class group and the henselian local ring, which is defined for decent spaces,
> use it through the decency of a Noetherian space.

```lean
theorem coordinateAxesQuotient_properties (hZ : B.Contains (⊤_ Scheme.{u})) :
    Stacks.Groupoids.IsEtaleEquivalenceRelation (relationPreRelation S) ∧
      IsAlgebraicSpace B (Spec (.of S.k)) hS (quotientSpace S B hS).obj ∧
      quotientMap S B hS ≫ sumMap S B hS =
        (Over.post (X := B.obj hS) B.inclusion).op.whiskerLeft
          (yoneda.map (coordinateSumMap S)) ∧
      Space.UniversalHomeomorphism B (Spec (.of S.k)) hS (sumMap S B hS) ∧
      IsIso (pullback.snd (sumMap S B hS) (Space.puncturedLineInclusion S.k B hS)) ∧
      Space.IsIntegralSpace B (Spec (.of S.k)) hS (quotientSpace S B hS).obj ∧
      Space.IsNoetherian B (Spec (.of S.k)) hS hZ (quotientSpace S B hS).obj ∧
      (∀ ξ : Space.points B (Spec (.of S.k)) hS (quotientSpace S B hS).obj,
        (∃ Z : Space.PrimeDivisor B (Spec (.of S.k)) hS (quotientSpace S B hS).obj,
          Z.genericPoint B (Spec (.of S.k)) hS _ = ξ) ↔ IsClosed {ξ}) ∧
      (originDivisor S B hS hZ).genericPoint B (Spec (.of S.k)) hS _ = originPoint S B hS ∧
      IsClosed {originPoint S B hS} ∧
      (∀ ξ : Space.points B (Spec (.of S.k)) hS (quotientSpace S B hS).obj,
        Space.pointsHomeomorphAffineLine (sumMap S B hS) (universalHomeomorphism_sumMap B S hS) ξ =
            AffineLineInvolution.origin S.k ↔ ξ = originPoint S B hS) ∧
      Space.divRationalFunction B (Spec (.of S.k)) hS (isAlgebraicSpace_quotientSpace S B hS)
          (isIntegralSpace_quotientSpace S B hS hZ)
          (hasEtaleLocalProperty_isLocallyNoetherian S B hS)
          (Space.coordinatePullbackUnit (sumMap S B hS) (isAlgebraicSpace_quotientSpace S B hS)
            (isIntegralSpace_quotientSpace S B hS hZ)
            (isIso_sumMap_pullback_puncturedAffineLine B S hS)) =
        2 • Space.primeDivisorClass (originDivisor S B hS hZ) ∧
      (∀ Z : Space.PrimeDivisor B (Spec (.of S.k)) hS (quotientSpace S B hS).obj,
        Z ≠ originDivisor S B hS hZ →
        (Space.primeDivisorClass Z : Space.weilDivisorClassGroup B (Spec (.of S.k)) hS
            (isAlgebraicSpace_quotientSpace S B hS)
            (isIntegralSpace_quotientSpace S B hS hZ)
            (hasEtaleLocalProperty_isLocallyNoetherian S B hS)) = 0) ∧
      (∃ e : Space.weilDivisorClassGroup B (Spec (.of S.k)) hS
            (isAlgebraicSpace_quotientSpace S B hS)
            (isIntegralSpace_quotientSpace S B hS hZ)
            (hasEtaleLocalProperty_isLocallyNoetherian S B hS) ≃+ ZMod 2,
        e (Space.primeDivisorClass (originDivisor S B hS hZ)) = 1) ∧
      (letI := Space.henselianLocalRing_isLocalRing B (Spec (.of S.k)) hS (quotientSpace S B hS).obj
          (isAlgebraicSpace_quotientSpace S B hS) (originPoint S B hS)
            (isIntegralSpace_quotientSpace S B hS hZ).isDecentSpace;
        letI := Space.stalkAlgebra B (Spec (.of S.k)) hS (quotientSpace S B hS).obj
          (isAlgebraicSpace_quotientSpace S B hS) (originPoint S B hS)
            (isIntegralSpace_quotientSpace S B hS hZ).isDecentSpace
          (originNeighborhood S B hS _ rfl);
        IsLocalRing.IsHenselization
          ((originNeighborhood S B hS _ rfl).scheme.left.1.presheaf.stalk
            (originNeighborhood S B hS _ rfl).point)
          (ResidueField ((originNeighborhood S B hS _ rfl).scheme.left.1.presheaf.stalk
            (originNeighborhood S B hS _ rfl).point))
          (Space.henselianLocalRing B (Spec (.of S.k)) hS (quotientSpace S B hS).obj
            (isAlgebraicSpace_quotientSpace S B hS) (originPoint S B hS)
              (isIntegralSpace_quotientSpace S B hS hZ).isDecentSpace : Type (u + 1))) ∧
      ¬ IsDomain (Space.henselianLocalRing B (Spec (.of S.k)) hS (quotientSpace S B hS).obj
        (isAlgebraicSpace_quotientSpace S B hS) (originPoint S B hS)
          (isIntegralSpace_quotientSpace S B hS hZ).isDecentSpace)
```

**`AlgebraicGeometry.Space.EtaleRelation.isEtaleEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/CoordinateAxesEtaleRelation.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/CoordinateAxesEtaleRelation.lean#L497). The attribute's comment: “etale\_relation”.

> The specified relation is an étale equivalence relation on the coordinate axes.

```lean
theorem isEtaleEquivalenceRelation (S : CoordinateAxesQuotientSetup.{u}) :
    Stacks.Groupoids.IsEtaleEquivalenceRelation (relationPreRelation S)
```

**`AlgebraicGeometry.CoordinateAxesQuotient.coordinateSumMap_invariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FunctionFieldEmbedding.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FunctionFieldEmbedding.lean#L315). The attribute's comment: “quotient\_map\_exists”.

> The coordinate-sum map is invariant under the relation: it has the same composite with the
> source and the target of `relationPreRelation`.

```lean
theorem coordinateSumMap_invariant (S : Setup.{u}) :
    (relationPreRelation S).target ≫ coordinateSumMap S =
      (relationPreRelation S).source ≫ coordinateSumMap S
```

**`AlgebraicGeometry.CoordinateAxesQuotient.quotientSumMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FunctionFieldEmbedding.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FunctionFieldEmbedding.lean#L364). The attribute's comment: “quotient\_map\_exists”.

> The morphism from the quotient sheaf to the affine line through which the coordinate-sum map
> factors, together with the equation expressing that factorisation.

```lean
noncomputable def quotientSumMap
    [HasSheafify (BigFppfOver.topology B (Spec (.of S.k)) hS) (Type u)] :
    { f : (Stacks.Groupoids.quotientSheaf
          (BigFppfOver.topology B (Spec (.of S.k)) hS)
          (Over.post (X := B.obj hS) B.inclusion)
          (relationPreRelation S)).obj ⟶
        Stacks.Groupoids.points (Over.post (X := B.obj hS) B.inclusion)
          (AffineLineInvolution.affineLine S.k) //
      Stacks.Groupoids.toQuotientSheaf
          (BigFppfOver.topology B (Spec (.of S.k)) hS)
          (Over.post (X := B.obj hS) B.inclusion)
          (relationPreRelation S) ≫ f =
        (Over.post (X := B.obj hS) B.inclusion).op.whiskerLeft
          (yoneda.map (coordinateSumMap S)) }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.6, Tag 0ENI](https://stacks.math.columbia.edu/tag/0ENI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
