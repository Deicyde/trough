---
declaration: section
origin: cited
lean: Stacks.Chow.KeyFormulaSituation, Stacks.Chow.KeyFormulaData.keyFormula_iff_forall_component_coheight_one, Stacks.Chow.KeyFormulaSituation.keyFormula_toKeyFormulaData, Stacks.Chow.pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary, Stacks.Chow.pointwiseMilnorShortComplex, Stacks.Chow.pointwiseMilnorBoundary, AlgebraicGeometry.milnorKTwoTameSymbol, AlgebraicGeometry.sum_localMilnorBoundaryOrder_eq_zero
statement: formalized
proof: formalized
---

# 42.27 The key formula

Section 42.27 of the Stacks Project, [Tag 0AYB](https://stacks.math.columbia.edu/tag/0AYB). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AYB, the section

[Tag 0AYB](https://stacks.math.columbia.edu/tag/0AYB) in the Stacks Project.

**`Stacks.Chow.KeyFormulaSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/Situation.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/Situation.lean#L169). The attribute's comment: “the situation preceding the key formula: two invertible modules with nonzero meromorphic sections, and a family of prime divisors with chosen local generators”.

> **The situation preceding the key formula, Stacks 0AYB.** On an integral, locally Noetherian
> scheme `X`, two invertible `𝒪_X`-modules `L` and `N` with nonzero meromorphic sections `s` and
> `t`, together with a locally finite family `{Z_i}` of prime divisors of `X` large enough that
> `s` generates `L` and `t` generates `N` at the generic point of every prime divisor outside the
> family, and, for each `i`, chosen generators `s_i` of `L_{ξ_i}` and `t_i` of `N_{ξ_i}` at the
> generic point `ξ_i` of `Z_i`.
>
> The ratios `f_i = s / s_i` and `g_i = t / t_i`, the orders of vanishing, the restrictions
> `s_i|_{Z_i}` and `t_i|_{Z_i}` and the tame symbols `∂_{B_i}(f_i, g_i)` are determined by these
> data, and are constructed from them below.
>
> A meromorphic section is given by its value in the generic stalk, and is nonzero exactly when
> that value is; see the module documentation.

```lean
public structure KeyFormulaSituation (L N : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N]
```

## Tag 0AYC, a lemma

[Tag 0AYC](https://stacks.math.columbia.edu/tag/0AYC) in the Stacks Project.

**`Stacks.Chow.KeyFormulaData.keyFormula_iff_forall_component_coheight_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/LocalReduction.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/LocalReduction.lean#L199). The attribute's comment: “the localization step of the source's proof: the equality of the two cycles is equivalent to the equality of their coefficients at the codimension-two points of the family”.

> **The key formula is local at the codimension-one points of the family.** It holds if and
> only if its two coefficients agree at the image of every codimension-one point of every member
> `Z_i`.
>
> This is the step of the source's proof that says "since we are proving the equality of cycles we
> may argue one coefficient at a time", and it is only that step. At such a point `x` the local
> ring `𝒪_{X, x}` has dimension two, only the finitely many members of the family through `x`
> contribute to either side, and the source derives the resulting identity of coefficients from the
> Key Lemma Stacks 0EAX on `𝒪_{X, x}`. That derivation is not carried out here: the identity of
> coefficients stands on the right hand side of the equivalence, so this declaration proves the
> equivalence and not the key formula.
>
> Stacks 0EAX itself is proved, as
> `Stacks.Chow.finsum_fracTameSymbolOrderAt_canonical_eq_zero`. The step from it to the identity of
> coefficients goes through the dictionary between `X` and `A = 𝒪_{X, x}` described in the module
> documentation.

```lean
theorem keyFormula_iff_forall_component_coheight_one [LocallyOfFiniteType p] :
    D.KeyFormula C p ↔ ∀ (i : D.Index) (z : (D.component i).subscheme), Order.coheight z = 1 →
      D.leftCoeff C p ((D.component i).subschemeι.base z) =
        D.tameSymbolCoeff C p ((D.component i).subschemeι.base z)
```

**`Stacks.Chow.KeyFormulaSituation.keyFormula_toKeyFormulaData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/SituationKeyFormula.lean, line 806](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/SituationKeyFormula.lean#L806). The attribute's comment: “the key formula itself, for the sheaf-level situation of Stacks 0AYB: the difference of the two Chern-class cycles equals the sum of the principal divisors of the tame symbols”.

> **Stacks 0AYC for the situation of Stacks 0AYB.** The key formula holds for the cycle-level
> data of the sheaf-level situation: the difference of the two Chern-class cycles is the locally
> finite sum of the principal divisors of the tame symbols `∂_{B_i}(f_i, g_i)` on the members of the
> family.
>
> At a codimension-two point `x` of a member of the family the two coefficients are compared by the
> local reciprocity law Stacks 0EAX on `A = 𝒪_{X, x}`, read at the pair of coordinates of `s` and
> `t` taken from trivializations of `L` and `N` near `x`: that sum vanishes, the members of the
> family carry all of it, and the difference between its summands and the summands of the right
> hand side of the key formula is the change-of-generator correction of Stacks 0EAN and Stacks
> 02SH, which is the left hand side. See the module documentation.

```lean
theorem keyFormula_toKeyFormulaData : (ℱ.toKeyFormulaData C p).KeyFormula C p
```

## Tag 0GU9, a remark

[Tag 0GU9](https://stacks.math.columbia.edu/tag/0GU9) in the Stacks Project.

**`Stacks.Chow.pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean#L161). The attribute's comment: “the complex of the tag: the composite of the tame-symbol differential of the tag with the divisor differential of Stacks 0GU3 is the zero homomorphism, so the three locally finite direct sums of Stacks 0GU2 -- the degree-two, degree-one and degree-zero Milnor K-groups of the residue fields at the points of relative dimension k + 2, k + 1 and k -- form a complex”.

> **Stacks 0GU9.** The three locally finite direct sums of Milnor K-groups of the tag form a
> complex: the tame-symbol differential followed by the divisor differential of Stacks 0GU3 is the
> zero homomorphism.
>
> This is the assertion of the tag. By
> `Stacks.Chow.pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary_of_forall` it suffices to
> check it one point of relative dimension `k + 2` and one point of relative dimension `k` at a
> time, which is `Stacks.Chow.finsum_pointClosureOrdBoundaryTerm_eq_zero`.

```lean
theorem pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary (k : ℤ) :
    (pointwiseDivisorDifferential C p k).comp (pointwiseMilnorBoundary C p k) = 0
```

**`Stacks.Chow.pointwiseMilnorShortComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean#L183). The attribute's comment: “the complex of the tag, assembled as a short complex of abelian groups out of the three locally finite direct sums of Stacks 0GU2 and the two differentials, the vanishing of whose composite is its defining property”.

> **Stacks 0GU9.** The complex of the tag, packaged as a short complex of abelian groups: the
> degree-two Milnor K-chains at the points of relative dimension `k + 2`, the degree-one chains at
> the points of relative dimension `k + 1` and the degree-zero chains at the points of relative
> dimension `k`, with the tame-symbol differential and the divisor differential of Stacks 0GU3.
> Its `zero` field is
> `Stacks.Chow.pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary`.

```lean
def pointwiseMilnorShortComplex (k : ℤ) : ShortComplex AddCommGrpCat.{u}
```

**`Stacks.Chow.pointwiseMilnorBoundary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseMilnorBoundary.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseMilnorBoundary.lean#L433). The attribute's comment: “the first differential of the complex of the tag, as a homomorphism of the locally finite direct sums of Stacks 0GU2: the degree-two Milnor K-chain group at the points of relative dimension k + 2 maps to the degree-one chain group at the points of relative dimension k + 1 by the rule whose coefficient at a point x' is the sum, over the points x of relative dimension k + 2 specializing to x', of the tame-symbol boundary of the class at x along the one-dimensional local ring of the closure of x at x'; both the finiteness of that sum and the local finiteness of the resulting family are proved, so the rule is a well defined additive map”.

> **Stacks 0GU9.** The first differential of the complex of the tag: the homomorphism from the
> locally finite direct sum of the degree-two Milnor K-groups at the points of relative dimension
> `k + 2` to the locally finite direct sum of the degree-one Milnor K-groups at the points of
> relative dimension `k + 1` whose coefficient at `x'` is the sum, over the points `x` of relative
> dimension `k + 2` specializing to `x'`, of the tame-symbol boundaries
> `∂_{𝒪_{closure {x}, x'}}` of the classes of the chain.

```lean
def pointwiseMilnorBoundary (k : ℤ) :
    PointwiseKTwoGroup C p k →+ PointwiseKOneGroup C p k
```

**`AlgebraicGeometry.milnorKTwoTameSymbol`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/MilnorBoundary.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/MilnorBoundary.lean#L161). The attribute's comment: “the construction of the local component of the first differential: the tame symbol of a one-dimensional Noetherian local domain, descended to a homomorphism from the degree-two Milnor K-group of its fraction field to the degree-one Milnor K-group of its residue field”.

> **Stacks Project, Tag 0GU9.** The tame symbol `∂_A` of a one-dimensional Noetherian local
> domain `A` with fraction field `K`, descended along the presentation of Milnor K-theory to a
> homomorphism `K₂ᴹ(K) ⟶ K₁ᴹ(κ(A))`. This is the local component of the first differential of the
> complex of the tag, the one written `∂_{𝒪_{W_x, x'}}` there.

```lean
def milnorKTwoTameSymbol (hdim : ringKrullDim A = 1) :
    MilnorKTheory K 2 →+ MilnorKTheory (IsLocalRing.ResidueField A) 1
```

**`AlgebraicGeometry.sum_localMilnorBoundaryOrder_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/MilnorBoundary.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/MilnorBoundary.lean#L381). The attribute's comment: “the vanishing of the composite of the two differentials in its local algebraic form: for a two-dimensional Noetherian local domain, the orders along the quotients of the tame-symbol boundaries of an arbitrary degree-two Milnor K-class of the fraction field, summed over the height-one primes, give zero -- this is the displayed sum of the tag's proof, with the reduction to a pure symbol discharged; the fraction field is realized as `FractionRing A`, and the geometric indexing of that sum by the intermediate points, the locally finite chain groups and the three-term complex itself are not formalized here”.

> **Stacks Project, Tag 0GU9.** Let `A` be a two-dimensional Noetherian local domain with
> fraction field `K` and let `α` be a class in the degree-two Milnor K-group of `K`. Summing, over
> the height-one primes `𝔮` of `A`, the order along `A / 𝔮` of the tame-symbol boundary of `α` at
> `𝔮` gives zero.
>
> This is the vanishing which the tag's argument reduces the composite of its two differentials to:
> at a point `x''` of `δ`-dimension `k` lying on the integral closed subscheme `W` with generic
> point `x` of `δ`-dimension `k + 2`, the ring `A` is `𝒪_{W, x''}`, its height-one primes are the
> intermediate points `x'` of `δ`-dimension `k + 1`, and the summand at `𝔮` is the coefficient
> `ord_{𝒪_{closure {x'}, x''}}(∂_{𝒪_{W, x'}}(α))`. The source reduces to a pure symbol by
> additivity and linearity before appealing to Stacks 0EAX; here the reduction is carried out, so
> the statement holds for every class of the Milnor K-group and not only for a pure symbol.

```lean
theorem sum_localMilnorBoundaryOrder_eq_zero (hdim : ringKrullDim A = 2)
    (α : MilnorKTheory (FractionRing A) 2) :
    (∑ᶠ q : {q : Ideal A // q.IsPrime ∧ q.height = 1},
      localMilnorBoundaryOrder hdim q α) = 0
```

## Tag 0GUA, a remark

[Tag 0GUA](https://stacks.math.columbia.edu/tag/0GUA) in the Stacks Project.

**`Stacks.Chow.milnorChainComap_pointwiseMilnorBoundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainBoundaryCompatible.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainBoundaryCompatible.lean#L127). The attribute's comment: “the compatibility of the restriction map of the degreewise localization sequence of the tag with the FIRST boundary map of the complex of Stacks 0GU9, the tame-symbol differential: for an open immersion j into a scheme locally of finite type over a Chow situation, restriction of locally finite Milnor K-chains to the open subscheme carries the tame-symbol differential in relative dimensions k + 2 and k + 1 to the tame-symbol differential of the open subscheme. The companion square for the extension-by-zero map from the closed complement is Stacks.Chow.pointwiseMilnorBoundary\_milnorChainExtend. The two squares for the SECOND boundary map, the divisor differential of Stacks 0GU3, are Stacks.Chow.milnorChainComap\_pointwiseDivisorDifferential and Stacks.Chow.pointwiseDivisorDifferential\_milnorChainExtend; the six-term exact sequence the snake lemma yields from all four is Stacks.Chow.milnorChowLocalization\_exact”.

> **Stacks 0GUA for the first differential and the restriction map.** Restriction of locally
> finite Milnor K-chains to an open subscheme commutes with the tame-symbol differential of
> Stacks 0GU9: the square formed by the two differentials and the two restriction maps, in Milnor
> degrees two and one, commutes.

```lean
theorem milnorChainComap_pointwiseMilnorBoundary (k : ℤ) :
    (pointwiseMilnorBoundary C (j ≫ p) k).comp
        (milnorChainComap C p j (injective_base_of_isOpenImmersion j)
          (bijective_residueFieldMap_openImmersion j) (k + 2) 2) =
      (milnorChainComap C p j (injective_base_of_isOpenImmersion j)
          (bijective_residueFieldMap_openImmersion j) (k + 1) 1).comp
        (pointwiseMilnorBoundary C p k)
```

**`Stacks.Chow.pointwiseMilnorBoundary_milnorChainExtend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainBoundaryCompatible.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainBoundaryCompatible.lean#L254). The attribute's comment: “the compatibility of the extension-by-zero map of the degreewise localization sequence of the tag with the FIRST boundary map of the complex of Stacks 0GU9, the tame-symbol differential: for a closed immersion i into a scheme locally of finite type over a Chow situation, extension by zero of locally finite Milnor K-chains from the closed subscheme carries its tame-symbol differential in relative dimensions k + 2 and k + 1 to the tame-symbol differential of the ambient scheme. The companion square for the restriction map to the open complement is Stacks.Chow.milnorChainComap\_pointwiseMilnorBoundary. The two squares for the SECOND boundary map, the divisor differential of Stacks 0GU3, are Stacks.Chow.milnorChainComap\_pointwiseDivisorDifferential and Stacks.Chow.pointwiseDivisorDifferential\_milnorChainExtend; the six-term exact sequence the snake lemma yields from all four is Stacks.Chow.milnorChowLocalization\_exact”.

> **Stacks 0GUA for the first differential and the extension-by-zero map.** Extension by zero
> of locally finite Milnor K-chains from a closed subscheme commutes with the tame-symbol
> differential of Stacks 0GU9.

```lean
theorem pointwiseMilnorBoundary_milnorChainExtend (k : ℤ) :
    (pointwiseMilnorBoundary C p k).comp
        (milnorChainExtend C p i (injective_base_of_isClosedImmersion i)
          (bijective_residueFieldMap_closedImmersion i) inferInstance (k + 2) 2) =
      (milnorChainExtend C p i (injective_base_of_isClosedImmersion i)
          (bijective_residueFieldMap_closedImmersion i) inferInstance (k + 1) 1).comp
        (pointwiseMilnorBoundary C (i ≫ p) k)
```

**`Stacks.Chow.milnorChainComap_pointwiseDivisorDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainDivisorCompatible.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainDivisorCompatible.lean#L67). The attribute's comment: “the compatibility of the restriction map of the degreewise localization sequence of the tag with the SECOND boundary map of the complex of Stacks 0GU9, the divisor differential of Stacks 0GU3: for an open immersion j into a scheme locally of finite type over a Chow situation, restriction of locally finite Milnor K-chains to the open subscheme carries the divisor differential in relative dimensions k + 1 and k to the divisor differential of the open subscheme. The companion square for the extension-by-zero map from the closed complement is Stacks.Chow.pointwiseDivisorDifferential\_milnorChainExtend”.

> **Stacks 0GUA for the second differential and the restriction map.** Restriction of locally
> finite Milnor K-chains to an open subscheme commutes with the divisor differential of
> Stacks 0GU3: the square formed by the two differentials and the two restriction maps, in Milnor
> degrees one and zero, commutes.

```lean
theorem milnorChainComap_pointwiseDivisorDifferential (k : ℤ) :
    (pointwiseDivisorDifferential C (j ≫ p) k).comp
        (milnorChainComap C p j (injective_base_of_isOpenImmersion j)
          (bijective_residueFieldMap_openImmersion j) (k + 1) 1) =
      (milnorChainComap C p j (injective_base_of_isOpenImmersion j)
          (bijective_residueFieldMap_openImmersion j) k 0).comp
        (pointwiseDivisorDifferential C p k)
```

**`Stacks.Chow.pointwiseDivisorDifferential_milnorChainExtend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainDivisorCompatible.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainDivisorCompatible.lean#L147). The attribute's comment: “the compatibility of the extension-by-zero map of the degreewise localization sequence of the tag with the SECOND boundary map of the complex of Stacks 0GU9, the divisor differential of Stacks 0GU3: for a closed immersion i into a scheme locally of finite type over a Chow situation, extension by zero of locally finite Milnor K-chains from the closed subscheme carries its divisor differential in relative dimensions k + 1 and k to the divisor differential of the ambient scheme. The companion square for the restriction map to the open complement is Stacks.Chow.milnorChainComap\_pointwiseDivisorDifferential”.

> **Stacks 0GUA for the second differential and the extension-by-zero map.** Extension by zero
> of locally finite Milnor K-chains from a closed subscheme commutes with the divisor differential
> of Stacks 0GU3.

```lean
theorem pointwiseDivisorDifferential_milnorChainExtend (k : ℤ) :
    (pointwiseDivisorDifferential C p k).comp
        (milnorChainExtend C p i (injective_base_of_isClosedImmersion i)
          (bijective_residueFieldMap_closedImmersion i) inferInstance (k + 1) 1) =
      (milnorChainExtend C p i (injective_base_of_isClosedImmersion i)
          (bijective_residueFieldMap_closedImmersion i) inferInstance k 0).comp
        (pointwiseDivisorDifferential C (i ≫ p) k)
```

**`Stacks.Chow.milnorChainLocalizationComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean#L577). The attribute's comment: “the degreewise localization sequence of the tag, for one relative dimension m and one Milnor degree n: the locally finite direct sums of Stacks 0GU2 for the closed subscheme, the ambient scheme and the complementary open subscheme, together with the extension-by-zero map from the closed subscheme and the restriction map to the open subscheme, as a short complex of abelian groups; its compatibility with the two boundary maps of Stacks 0GU9, and the six-term exact sequence the snake lemma yields from it, are proved not here but in Stacks.Chow.milnorChowLocalization\_exact, Stacks.Chow.milnorChainComap\_pointwiseMilnorBoundary, Stacks.Chow.pointwiseMilnorBoundary\_milnorChainExtend, Stacks.Chow.milnorChainComap\_pointwiseDivisorDifferential and Stacks.Chow.pointwiseDivisorDifferential\_milnorChainExtend”.

> **Stacks 0GUA.** The degreewise localization sequence of locally finite Milnor K-chains: the
> chains on the closed subscheme `Y`, on `X` and on the open subscheme `U`, with extension by zero
> from `Y` and restriction to `U`.

```lean
def milnorChainLocalizationComplex (hcomp : Set.range i.base = (Set.range j.base)ᶜ)
    (m : ℤ) (n : ℕ) : ShortComplex AddCommGrpCat.{u}
```

**`Stacks.Chow.milnorChainLocalizationSplitting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean#L598). The attribute's comment: “the splitting of the degreewise localization sequence of the tag: restriction to the closed subscheme retracts the extension by zero from it, extension by zero from the open subscheme sections the restriction to it, and the two resulting idempotents of the chains on the ambient scheme add up to the identity”.

> **Stacks 0GUA.** The degreewise localization sequence is split: restriction to `Y` is a
> retraction of the extension by zero from `Y`, extension by zero from `U` is a section of the
> restriction to `U`, and the two composites add up to the identity.

```lean
def milnorChainLocalizationSplitting (hcomp : Set.range i.base = (Set.range j.base)ᶜ)
    (m : ℤ) (n : ℕ) :
    (milnorChainLocalizationComplex C p i j hcomp m n).Splitting
```

**`Stacks.Chow.milnorChainLocalization_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean, line 624](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean#L624). The attribute's comment: “the short exactness of the degreewise localization sequence of the tag, in one relative dimension and one Milnor degree: extension by zero from the closed subscheme is injective, restriction to the open subscheme is surjective, and the image of the first is the kernel of the second”.

> **Stacks 0GUA.** The degreewise localization sequence is short exact: it is split, and a
> split short complex is short exact.

```lean
theorem milnorChainLocalization_shortExact
    (hcomp : Set.range i.base = (Set.range j.base)ᶜ) (m : ℤ) (n : ℕ) :
    (milnorChainLocalizationComplex C p i j hcomp m n).ShortExact
```

**`Stacks.Chow.milnorChainLocalization_shortExact_degrees`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean, line 676](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChainLocalization.lean#L676). The attribute's comment: “the three split short exact sequences of the tag, for i = 2, 1 and 0: for an open subscheme and a closed subscheme with complementary underlying set, the sequence of locally finite direct sums of the degree-i Milnor K-groups of the residue fields at the points of relative dimension k + i is short exact and split; the middle terms are exactly the three groups carrying the complex of Stacks 0GU9. Only the sequences themselves are proved here; their compatibility with the two boundary maps of that complex is proved in Stacks.Chow.milnorChainComap\_pointwiseMilnorBoundary, Stacks.Chow.pointwiseMilnorBoundary\_milnorChainExtend, Stacks.Chow.milnorChainComap\_pointwiseDivisorDifferential and Stacks.Chow.pointwiseDivisorDifferential\_milnorChainExtend, and the six-term exact sequence the snake lemma yields from them is Stacks.Chow.milnorChowLocalization\_exact”.

> **Stacks 0GUA.** The three split short exact sequences of the tag, for `i = 2, 1, 0`: the
> locally finite direct sums of degree-`i` Milnor K-groups at the points of relative dimension
> `k + i`, for the closed subscheme, the ambient scheme and the complementary open subscheme. By
> `Stacks.Chow.milnorChainLocalizationComplex_X₂_two`,
> `Stacks.Chow.milnorChainLocalizationComplex_X₂_one` and
> `Stacks.Chow.milnorChainLocalizationComplex_X₂_zero` the middle terms are the three groups that
> carry the complex of Stacks 0GU9.

```lean
theorem milnorChainLocalization_shortExact_degrees
    (hcomp : Set.range i.base = (Set.range j.base)ᶜ) (k : ℤ) :
    (milnorChainLocalizationComplex C p i j hcomp (k + 2) 2).ShortExact ∧
      (milnorChainLocalizationComplex C p i j hcomp (k + 1) 1).ShortExact ∧
      (milnorChainLocalizationComplex C p i j hcomp k 0).ShortExact
```

**`Stacks.Chow.milnorChowGroupOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean#L226). The attribute's comment: “the definition of the tag: the first higher Chow group CH^M\_k(X, 1) is the homology in the middle of the complex of Stacks 0GU9, formed as the degree-one Milnor K-chains killed by the divisor differential of Stacks 0GU3 modulo the image of the tame-symbol differential of Stacks 0GU9, the latter lying in the former because that composite is the zero homomorphism; the localization property of the tag, namely the degreewise split short exact sequences attached to an open subscheme with reduced closed complement together with the six-term exact sequence the snake lemma yields from them, is not proved here but in Stacks.Chow.milnorChainLocalization\_shortExact\_degrees and Stacks.Chow.milnorChowLocalization\_exact”.

> **Stacks 0GUA.** The first higher Chow group `CH^M_k(X, 1)` of the tag: the homology in the
> middle of the complex of Stacks 0GU9, that is, the degree-one Milnor K-chains killed by the
> divisor differential of Stacks 0GU3 modulo those coming from a degree-two Milnor K-chain under
> the tame-symbol differential. The superscript of the tag distinguishes this group from the higher
> Chow groups of the literature.

```lean
def milnorChowGroupOne (k : ℤ) : Type u
```

**`Stacks.Chow.milnorChowLocalization_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowLocalizationSequence.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowLocalizationSequence.lean#L625). The attribute's comment: “the six-term exact sequence of the tag, the main claim of the remark: for an open subscheme V of a scheme X locally of finite type over a Chow situation and a closed immersion i of Y into X whose image is the complement of V, the sequence of the first higher Chow groups of Y, X and V, followed by the Chow groups of Y, X and V and ending in zero, is exact. The first two maps are induced on the first higher Chow groups of Stacks 0GU9 by the extension-by-zero and restriction maps of the degreewise localization sequence of the tag; the third is the connecting map of the snake lemma, formed from the splitting of that sequence; the last two are the proper pushforward along the closed immersion and the restriction to the open subscheme of Stacks 02RX”.

> **Stacks 0GUA.** The six-term exact sequence
>
> `CH^M_k(Y, 1) ⟶ CH^M_k(X, 1) ⟶ CH^M_k(V, 1) ⟶ CH_k(Y) ⟶ CH_k(X) ⟶ CH_k(V) ⟶ 0`
>
> attached to an open subscheme `V` of `X` and a closed immersion `i : Y ⟶ X` with complementary
> image. The first three maps are those induced by the extension-by-zero and restriction maps of
> the degreewise localization sequence of the tag, together with the connecting map
> `Stacks.Chow.milnorChowBoundary`; the last two are the proper pushforward and the restriction to
> an open subscheme of Stacks 02RX, whose exactness and surjectivity are
> `Stacks.Chow.exact_chowPushforward_chowGroupOpensRestrict` and
> `Stacks.Chow.surjective_chowGroupOpensRestrictOfIsOpenImmersion`.

```lean
theorem milnorChowLocalization_exact (k : ℤ) :
    Function.Exact (milnorChowGroupOneExtend C p i k) (milnorChowGroupOneComap C p V k) ∧
      Function.Exact (milnorChowGroupOneComap C p V k) (milnorChowBoundary C p i V hcomp k) ∧
      Function.Exact (milnorChowBoundary C p i V hcomp k)
        (chowPushforwardOfIsClosedImmersion C (i ≫ p) p i rfl k) ∧
      Function.Exact (chowPushforwardOfIsClosedImmersion C (i ≫ p) p i rfl k)
        (chowGroupOpensRestrictOfIsOpenImmersion C p V k) ∧
      Function.Surjective (chowGroupOpensRestrictOfIsOpenImmersion C p V k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.27, Tag 0AYB](https://stacks.math.columbia.edu/tag/0AYB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
