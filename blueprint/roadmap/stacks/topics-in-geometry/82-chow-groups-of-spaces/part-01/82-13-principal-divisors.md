---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.principalDivisorCycle, AlgebraicGeometry.Space.principalDivisorCycleOfRegularLocus, AlgebraicGeometry.Space.rationalFunctionPrincipalDivisorCycle, AlgebraicGeometry.Space.etalePullback_principalDivisorCycle_eq_sum_components_iff, AlgebraicGeometry.Space.etalePullback_principalDivisorCycle_eq_sum_components_iff_eq_ord_closureImage, AlgebraicGeometry.Space.etalePullbackPrincipalDivisorCycle_apply_eq_componentPushforwardCoeff
statement: formalized
proof: formalized
---

# 82.13 Principal divisors

Section 82.13 of the Stacks Project, [Tag 0EQ0](https://stacks.math.columbia.edu/tag/0EQ0). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EQ1, a definition

[Tag 0EQ1](https://stacks.math.columbia.edu/tag/0EQ1) in the Stacks Project.

**`AlgebraicGeometry.Space.principalDivisorCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 649](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L649). The attribute's comment: “div(f) = ∑ ord\_Z(f) [Z] as an element of Z\_\{n-1}(X); the δ-dimension of a prime divisor is n-1 by Stacks 0EPZ, whose dimension-function hypotheses d and hd are Stacks 0EDN, carried; local finiteness is Stacks 0ENN, the argument hfin, discharged by locallyFinite\_principalDivisorCoefficients\_ne\_zero in principalDivisorCycleOfRegularLocus”.

> **Stacks 0EQ1.** The *principal divisor associated to `f ∈ R(X)^*`*, that is
> `div(f) = ∑_Z ord_Z(f) [Z]`, as an element of `Z_{n-1}(X)` for `X/B` good and integral with
> `dim_δ(X) = n`.
>
> This is the principal divisor of Stacks 0ENP read as a cycle: the formal sum is the same, and it
> is an `(n-1)`-cycle because a prime divisor of such an `X` has δ-dimension `n - 1` by
> Stacks 0EPZ. Local finiteness is Stacks 0ENN, the argument `hfin`, which
> `AlgebraicGeometry.Space.principalDivisorCycleOfRegularLocus` discharges.

```lean
def principalDivisorCycle
    (hfin : LocallyFinite fun W : PrimeDivisor D.site D.base D.base_mem X =>
      if principalDivisorCoefficients D.site D.base D.base_mem hX.1 hdec emb f hf W = 0 then ∅
      else W.support D.site D.base D.base_mem X)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) :
    CycleGroup D sX (n - 1)
```

**`AlgebraicGeometry.Space.principalDivisorCycleOfRegularLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean, line 683](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisor.lean#L683). The attribute's comment: “div(f) in Z\_\{n-1}(X), with local finiteness (Stacks 0ENN) proved from a nonempty open U over which f is invertible, the datum (U, hUopen, hUne, hreg) of the first sentence of the source's own proof of that lemma; the dimension-function hypotheses d and hd are Stacks 0EDN, carried”.

> **Stacks 0EQ1.** The principal divisor `div(f) = ∑_Z ord_Z(f) [Z]` of a rational function
> `f ∈ R(X)^*` as an element of `Z_{n-1}(X)`, with the local finiteness of Stacks 0ENN proved from
> a nonempty open subset of `|X|` over which `f` is invertible.

```lean
def principalDivisorCycleOfRegularLocus
    (hN : HasEtaleLocalProperty D.site D.base D.base_mem X
      (fun Y : Scheme.{u} => IsLocallyNoetherian Y))
    (U : Set (points D.site D.base D.base_mem X)) (hUopen : IsOpen U) (hUne : U.Nonempty)
    (hreg : ∀ W : PrimeDivisor D.site D.base D.base_mem X,
      W.genericPoint D.site D.base D.base_mem X ∈ U →
        ∃ r : ↥(W.genericHenselianLocalRing D.site D.base D.base_mem hX.1 hdec), IsUnit r ∧
          emb W f =
            algebraMap _ (W.genericTotalFractionRing D.site D.base D.base_mem hX.1 hdec) r)
    (hint : IsIntegralSpace D.site D.base D.base_mem X)
    (d : DimensionFunction (points D.site D.base D.base_mem X))
    (hd : ∀ x, d x = D.deltaValue sX x) {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt)) :
    CycleGroup D sX (n - 1)
```

**`AlgebraicGeometry.Space.rationalFunctionPrincipalDivisorCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisorCanonical.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrincipalDivisorCanonical.lean#L73). The attribute's comment: “div(f) = ∑ ord\_Z(f) [Z] in Z\_\{n-1}(X) for X/B good and integral with dim\_δ(X) = n and f ∈ R(X)^*; ord\_Z(f) is read through the canonical embedding of Stacks 0ENK, local finiteness is Stacks 0ENN proved, the δ-dimension n - 1 of a prime divisor is Stacks 0EPZ with the dimension function of Stacks 0EDN proved; nothing carried”.

> The *principal divisor associated to `f ∈ R(X)^*`*, `div(f) = div_X(f) = ∑_Z ord_Z(f) [Z]`, as
> an element of `Z_{n-1}(X)`, for `X/B` good and integral with `dim_δ(X) = n`.

```lean
def rationalFunctionPrincipalDivisorCycle {n : ℤ}
    (hn : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (f : (rationalFunctions D.site D.base D.base_mem hX.1)ˣ) :
    CycleGroup D sX (n - 1)
```

## Tag 0EQ2, a lemma

[Tag 0EQ2](https://stacks.math.columbia.edu/tag/0EQ2) in the Stacks Project.

**`AlgebraicGeometry.Space.etalePullback_principalDivisorCycle_eq_sum_components_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackPrincipalDivisor.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackPrincipalDivisor.lean#L359). The attribute's comment: “REDUCED, not proved: the displayed equality of cycles on X — coefficientwise at every integral closed subspace, with the sum over the irreducible components of X — HOLDS IF AND ONLY IF it holds at the integral closed subspaces of δ-dimension n-1. Proved away from them, where both sides vanish, both being (n-1)-cycles. The coefficient identity at those subspaces is NOT proved and NOT assumed: it is the source's steps three to six, namely the square of henselian local rings of Remark 0EPL, the multiplicity one of Lemma 0EPY, the length equality along a flat unramified map of Lemma 02M1 and the length decomposition of Lemma 02QG. Hypotheses: hrel, the relative dimension 0 of the étale morphism, flatness itself being supplied from Stacks 0467; and, on each irreducible component, the fields of EtaleComponentDivisorData — goodness over the base, the three hypotheses of Stacks 0ENK with the embeddings they go with, the dominance of f restricted to the component (the source's first step, which makes g ∘ f|\_\{X'} defined), that g ∘ f|\_\{X'} is in R(X')^*, local finiteness of its divisor (Stacks 0ENN) and the dimension function of Stacks 0EDN. That dim\_δ(X') = n for every component, the source's second paragraph, is proved”.

> In Situation 0EDT let `f : X ⟶ Y` be an étale morphism of good algebraic spaces over `B`, let
> `Y` be integral with `dim_δ(Y) = n` and let `g ∈ R(Y)^*`. Then the identity of cycles on `X`
>
> `f^*(div_Y(g)) = ∑_{X'} (X' → X)_* div_{X'}(g ∘ f|_{X'})`,
>
> the sum being over the irreducible components `X'` of `X` (Remark 0EE8), holds at every integral
> closed subspace `Z ⊆ X`, coefficientwise, if and only if it holds at those of δ-dimension
> `n - 1`.

```lean
theorem etalePullback_principalDivisorCycle_eq_sum_components_iff
    (data : EtaleComponentDivisorData D sX hX sY hY f hbase hetale hintY n hnY g) :
    (∀ Z : IntegralClosedSubspace D.site D.base D.base_mem X,
        (etalePullbackPrincipalDivisorCycle D sX hX sY hY hbase hetale hrel hintY embY g hg
            hfinY dY hdY hnY).1 Z =
          data.componentPushforwardCoeff Z) ↔
      ∀ Z : IntegralClosedSubspace D.site D.base D.base_mem X,
        deltaDimension D sX Z = n - 1 →
          (etalePullbackPrincipalDivisorCycle D sX hX sY hY hbase hetale hrel hintY embY g hg
              hfinY dY hdY hnY).1 Z =
            data.componentPushforwardCoeff Z
```

**`AlgebraicGeometry.Space.etalePullback_principalDivisorCycle_eq_sum_components_iff_eq_ord_closureImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackPrincipalDivisorComponents.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackPrincipalDivisorComponents.lean#L721). The attribute's comment: “REDUCED to ONE identity of integers, with NOTHING about the components assumed. The displayed equality of cycles on X — coefficientwise, the sum over the irreducible components of X — HOLDS IF AND ONLY IF at every integral closed subspace Z of X of δ-dimension n-1 the sum over the components X' of ord\_Z(g ∘ f|\_\{X'}), computed on X', equals ord\_\{Z'}(g) for Z' the image of Z in Y. This is that equivalence. Proved here, in both halves: away from δ-dimension n-1 both sides vanish, both being (n-1)-cycles, which on the right uses dim\_δ(X') = n for every component (the source's second paragraph, PROVED in deltaDimensionClosed\_univ\_irreducibleComponentSubspace); and at δ-dimension n-1 the coefficient of the left side is ord\_\{Z'}(g) by Lemma 0EPY, for an ARBITRARY X, which is etalePullbackPrincipalDivisorCycle\_apply\_eq\_apply\_closureImage together with IntegralClosedSubspace.exists\_eq\_preimageComponent. The right side is formed through etaleComponentDivisorData, so the dominance of f restricted to a component — the source's first step, what makes g ∘ f|\_\{X'} defined, and formerly a field of EtaleComponentDivisorDataOfGood — is PROVED, in pointsMap\_genericPoint\_eq\_genericPoint\_irreducibleComponentSubspace: an étale morphism is flat, so generizations lift along |X| → |Y|, and a continuous generalizing map into a quasi-sober space carries the generic point of an irreducible component to the generic point of one, which for the irreducible |Y| is its generic point. The source's own route, openness of |f| plus local finiteness of the components, is not needed. The only input beyond the source's hypotheses is ComponentDivisorLocallyFinite, which is Stacks 0ENN on each component and is what makes div\_\{X'}(g ∘ f|\_\{X'}) a cycle at all; Stacks 0EQ1 takes it in the same shape on Y (TargetDivisorLocallyFinite) and this repository proves it from a nonempty open subset over which the function is invertible (locallyFinite\_principalDivisorCoefficients\_ne\_zero). For X INTEGRAL the remaining identity of integers is PROVED and with it the whole of the source's displayed identity, which then reads f^* div\_Y(g) = div\_X(g ∘ f) in Z\_\{n-1}(X): etalePullbackPrincipalDivisorCycle\_eq\_principalDivisorCycle\_of\_isIntegralSpace, coefficientwise etalePullbackPrincipalDivisorCycle\_apply\_of\_isIntegralSpace, through ord\_rationalFunctionMap\_eq\_ord\_of\_isEtale. WHAT IS STILL MISSING, for an X with several components, is exactly the right-hand side of this equivalence, and it is the source's grouping of the branches at the generic point of Z over the components through it: ord\_Z(g ∘ f|\_\{X'}) has to be identified with the sum of Ring.minimalPrimeOrd over the minimal primes 𝔭 of the local ring of an affine étale chart W of X at a point over the generic point of Z with componentOfBranch 𝔭 = X'. The partition itself is available (finsum\_flatBranch\_eq\_finsum\_component\_finsum\_flatBranch), the chart reading of g ∘ f|\_\{X'} is available with no flatness of f|\_\{X'} (rationalFunctionsToTotalFractionRing\_rationalFunctionMap\_componentChart, nonZeroDivisors\_le\_comap\_chartGlobalSectionsRestrict), and the components of W ×\_X X' are components of W (mem\_irreducibleComponents\_image\_closedSubspaceBaseChangeChartProj), in the stalk-level form comap\_stalkMap\_closedSubspaceBaseChangeChartProj\_mem\_minimalPrimes; and the transport of Ring.minimalPrimeOrd along the surjection of local rings 𝒪\_\{W,w} → 𝒪\_\{W ×\_X X', w'} is Ring.minimalPrimeOrd\_map\_of\_surjective. So the grouping of the branches over the components is now proved, as finsum\_minimalPrimeOrd\_stalkMap\_eq\_finsum\_branch\_on\_component, and so is the recognition of its left-hand side as ord\_Z(g ∘ f|\_\{X'}): ord\_rationalFunctionMap\_eq\_finsum\_branch\_on\_component, through the stalk-level chart reading chartPointRationalFunctionMap\_rationalFunctionMap\_componentChart, which composes the two halves, rationalFunctionsToTotalFractionRing\_rationalFunctionMap\_componentChart on global sections and Scheme.totalFractionRingToStalkFractionRing\_map\_appTop from global sections to the local ring. The sum over ALL the branches of 𝒪\_\{W,w} is ord\_\{Z'}(g) on Y, with the same element of Q(𝒪\_\{W,w}): PrimeDivisor.ord\_eq\_finsum\_minimalPrimeOrd\_etaleChartComp. So the whole grouping of the branches, the content of the source's third to sixth paragraphs, is proved. The coefficient of the pushforward along the inclusion of a component is proved too, in componentDivisorPushforward\_apply\_pushforward and \_apply\_of\_forall\_ne, through properCyclePushforward\_ι\_eq\_integralClosedSubspacePushforward: the inclusion of an irreducible component is the inclusion of an integral closed subspace, so the pushforward of Stacks 0EP1 along it is integralClosedSubspacePushforward, whose coefficients are the extension by zero of the coefficients on the component. WHAT NO DECLARATION PROVIDES is the CONVERSE presentation — that an integral closed subspace Z of X whose points lie in |X'| is the image of an integral closed subspace of X', of δ-dimension making it a prime divisor of X' — which is what cuts componentPushforwardCoeff Z, a sum over ALL the components, down to the components through the generic point of Z and matches each term with ord\_\{Z ∩ X'}(g ∘ f|\_\{X'}); nor is the partition of the minimal primes of 𝒪\_\{W,w} over those components (finsum\_flatBranch\_eq\_finsum\_component\_finsum\_flatBranch) joined to the two sums above”.

> **Stacks 0EQ2, reduced to one identity of orders of vanishing, and with no data on the
> components assumed.** In Situation 0EDT let `f : X ⟶ Y` be an étale morphism of good algebraic
> spaces over `B`, let `Y` be integral with `dim_δ(Y) = n` and let `g ∈ R(Y)^*`. Then the identity
> of cycles on `X`
>
> `f^*(div_Y(g)) = ∑_{X'} (X' → X)_* div_{X'}(g ∘ f|_{X'})`,
>
> read coefficientwise over the irreducible components `X'` of `X` (Remark 0EE8), holds **if and
> only if** at every integral closed subspace `Z ⊆ X` of δ-dimension `n - 1`
>
> `∑_{X'} ord_Z(g ∘ f|_{X'}) = ord_{Z'}(g)`,
>
> `Z'` being the image of `Z` in `Y`. That one identity of integers — the last step of the source's
> third to sixth paragraphs — is the whole of what is left.
>
> Nothing about the components is assumed: the right-hand side is formed through
> `AlgebraicGeometry.Space.etaleComponentDivisorData`, whose only input is the local finiteness of
> Stacks 0ENN on each component, which is what makes `div_{X'}(g ∘ f|_{X'})` a cycle at all and
> which Stacks 0EQ1 takes in the same form on `Y`. In particular the dominance of `f|_{X'}` is
> proved, not assumed
> (`AlgebraicGeometry.Space.pointsMap_genericPoint_eq_genericPoint_irreducibleComponentSubspace`).
>
> Two reductions are combined. Away from δ-dimension `n - 1` both sides vanish, both being
> `(n-1)`-cycles — on the right because every component has `dim_δ(X') = n`, the source's second
> paragraph, which is proved — the reduction of
> `AlgebraicGeometry.Space.etalePullback_principalDivisorCycle_eq_sum_components_iff`, taken here
> at the canonical embeddings and hence re-run rather than cited. At
> δ-dimension `n - 1` the left-hand side is `ord_{Z'}(g)`, which is Lemma 0EPY in the form
> `AlgebraicGeometry.Space.etalePullbackPrincipalDivisorCycle_apply_eq_apply_closureImage`,
> and that holds for an arbitrary `X`, not only an integral one.

```lean
theorem etalePullback_principalDivisorCycle_eq_sum_components_iff_eq_ord_closureImage
    (hfin : ComponentDivisorLocallyFinite D sX hX sY hY hetale hintY g hg) :
    (∀ Z : IntegralClosedSubspace D.site D.base D.base_mem X,
        (etalePullbackPrincipalDivisorCycleOfGood D sX hX sY hY hbase hetale hintY g hg
            hfinY hnY).1 Z =
          (etaleComponentDivisorData D sX hX sY hY f hbase hetale hintY n hnY g hg
            hfin).toEtaleComponentDivisorData.componentPushforwardCoeff Z) ↔
      ∀ Z : IntegralClosedSubspace D.site D.base D.base_mem X,
        deltaDimension D sX Z = n - 1 →
          (etaleComponentDivisorData D sX hX sY hY f hbase hetale hintY n hnY g hg
              hfin).toEtaleComponentDivisorData.componentPushforwardCoeff Z =
            (targetPrincipalDivisorCycle D sY hY hintY g hg hfinY hnY).1
              (Z.closureImage D.site D.base D.base_mem hY.1
                (D.isDecentSpace_of_isGood sY hY) f)
```

**`AlgebraicGeometry.Space.etalePullbackPrincipalDivisorCycle_apply_eq_componentPushforwardCoeff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackPrincipalDivisorIdentity.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackPrincipalDivisorIdentity.lean#L353). The attribute's comment: “the displayed equality of cycles on X, read coefficientwise at every integral closed subspace, the sum being over the irreducible components of X (Remark 0EE8); it is read coefficientwise because that family is only locally finite, so the right-hand side is not a sum in Z\_\{n-1}(X). Both sides are formed at the canonical Stacks 0ENK embeddings of genericFractionEmbedding, on Y and on each component, so the two orders of vanishing are taken at the same data and are tied through rationalFunctionMap. UNCONDITIONAL: nothing beyond the source's own hypotheses goes in. The left-hand side is the flat pullback of Stacks 0EP8 at relative dimension 0 (etalePullbackCycleMap), an etale morphism being flat by Stacks 0467 and of relative dimension 0; the right-hand side is the sum of the pushforwards of Stacks 0EP1 of the principal divisors of Stacks 0EQ1 on the components. The source's first step, dominance of f restricted to a component, is PROVED (pointsMap\_genericPoint\_eq\_genericPoint\_irreducibleComponentSubspace); its second paragraph, dim\_delta(X') = n for every component, is PROVED (deltaDimensionClosed\_univ\_irreducibleComponentSubspace); the local finiteness of Stacks 0ENN on Y and on each component, which makes the principal divisors cycles at all, is PROVED (targetDivisorLocallyFinite\_of\_isGood, componentDivisorLocallyFinite\_of\_isGood, out of ordRationalFunction\_mem\_weilDivisor, the repository's Stacks 0ENN); and the source's third to sixth paragraphs are componentPushforwardCoeff\_eq\_ord\_of\_chart, which computes both sides on one affine etale chart of X through the generic point of Z -- also a chart of Y because f is etale -- as sums of Ring.minimalPrimeOrd over the branches at the chart point: the coefficient of the left side is ord\_\{Z'}(g) by Lemma 0EPY (etalePullbackPrincipalDivisorCycle\_apply\_eq\_apply\_closureImage) and is the sum over ALL the branches (PrimeDivisor.ord\_eq\_finsum\_minimalPrimeOrd\_etaleChartComp, Stacks 0ENM), each term of the right side is the subsum over the branches lying on its component (ord\_rationalFunctionMap\_eq\_finsum\_branch\_on\_component), and the branches are partitioned over the components through the generic point of Z (finsum\_minimalPrimes\_eq\_finsum\_componentSubspace), which is the source's last step that \{1,...,t} is the disjoint union of the J(X'); that replaces the square of Remark 0EPL, Lemma 02M1 and Lemma 02QG”.

> **Stacks 0EQ2.** In Situation 0EDT let `f : X ⟶ Y` be an étale morphism of good algebraic
> spaces over `B`, let `Y` be integral with `dim_δ(Y) = n` and let `g ∈ R(Y)^*`. Then, as cycles on
> `X`,
>
> `f^*(div_Y(g)) = ∑_{X'} (X' → X)_* div_{X'}(g ∘ f|_{X'})`,
>
> the sum being over the irreducible components `X'` of `X` (Remark 0EE8). The identity is read
> coefficientwise, at every integral closed subspace of `X`, because the family of irreducible
> components is only locally finite and the right-hand side is therefore not a sum in `Z_{n-1}(X)`.
>
> Both sides are formed at the canonical embeddings of Stacks 0ENK, on `Y` for `g` and on each
> component `X'` for `g ∘ f|_{X'}`, so that the two orders of vanishing are read at the same data
> and are tied to one another through `AlgebraicGeometry.Space.rationalFunctionMap`.
>
> Nothing beyond the source's own hypotheses goes in. The dominance of `f|_{X'}`, the source's
> first step, is
> `AlgebraicGeometry.Space.pointsMap_genericPoint_eq_genericPoint_irreducibleComponentSubspace`;
> `dim_δ(X') = n`, the source's second paragraph, is
> `AlgebraicGeometry.Space.deltaDimensionClosed_univ_irreducibleComponentSubspace`; and the local
> finiteness of Stacks 0ENN, on `Y` and on each component, which is what makes each principal
> divisor a cycle at all, is discharged by
> `AlgebraicGeometry.Space.targetDivisorLocallyFinite_of_isGood` and
> `AlgebraicGeometry.Space.componentDivisorLocallyFinite_of_isGood`.

```lean
theorem etalePullbackPrincipalDivisorCycle_apply_eq_componentPushforwardCoeff
    (D : BaseSpaceDimensionSituation.{u})
    {X Y : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u}
    (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY)
    {f : X ⟶ Y} (hbase : f ≫ sY = sX) (hetale : IsEtale D.site D.base D.base_mem f)
    (hintY : IsIntegralSpace D.site D.base D.base_mem Y)
    (g : rationalFunctions D.site D.base D.base_mem hY.1) (hg : IsUnit g) {n : ℤ}
    (hnY : deltaDimensionClosed D sY hY Set.univ isClosed_univ = (n : EInt))
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) :
    (etalePullbackPrincipalDivisorCycleOfGood D sX hX sY hY hbase hetale hintY g hg
        (targetDivisorLocallyFinite_of_isGood D sY hY hintY g hg) hnY).1 Z =
      (etaleComponentDivisorData D sX hX sY hY f hbase hetale hintY n hnY g hg
        (componentDivisorLocallyFinite_of_isGood D sX hX sY hY hetale hintY g
          hg)).toEtaleComponentDivisorData.componentPushforwardCoeff Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.13, Tag 0EQ0](https://stacks.math.columbia.edu/tag/0EQ0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
