---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProjectiveSpaceOfModule.exists_intersectProperly_torFormulaCycleIntersectionProduct_eq, AlgebraicGeometry.ProjectiveSpaceOfModule.endProjectionImage_eq_of_represents_identity, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_movingFamily_of_subvariety_fixed, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_forall_closedPoint_line_moving_of_codimension, AlgebraicGeometry.exists_rationallyEquivalent_forall_intersectProperly, AlgebraicGeometry.exists_rationallyEquivalent_intersectProperly
statement: formalized
proof: formalized
---

# 43.24 Moving Lemma

Section 43.24 of the Stacks Project, [Tag 0B0D](https://stacks.math.columbia.edu/tag/0B0D). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B0E, a lemma

[Tag 0B0E](https://stacks.math.columbia.edu/tag/0B0E) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_intersectProperly_torFormulaCycleIntersectionProduct_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/KeyLemma.lean, line 1024](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/KeyLemma.lean#L1024). The attribute's comment: “the whole lemma. `X ⊂ 𝐏^N` is read as `⊆`, so `dim X = N` is covered: there `X` is the whole of `𝐏(V)` and the conclusion holds with `C = Z` and an empty family of `Z_j`, which is the empty case of the source's chain of projections. The non-strict dimension clause is registered in the disjunctive form `dim (Z_j ∩ T_i) ≤ dim (Z ∩ T_i) ∨ dim (Z_j ∩ T_i) + n ≤ d + d'` — written additively because `WithBot ℕ∞` has no subtraction — which is what condition (4) of the source's proof yields and which implies the source's own first inequality wherever Tag 0AZP makes it true, namely whenever `Z ∩ T_i` is nonempty; in the bottom case `Z ∩ T_i = ∅` the source's first inequality is refuted by a nonsingular quadric surface in 𝐏^3 with Z and T\_1 two distinct lines of one ruling, written out in this module's implementation notes, and the second disjunct is what holds there. The strict clause is as the source has it, and is vacuous exactly on that bottom case”.

> **Stacks Project, Tag 0B0E.** Let `X ⊆ 𝐏(V)` be a nonsingular closed subvariety of dimension
> `n` of the projective space of a vector space of dimension `N + 1` over an algebraically closed
> field; let `Z ⊆ X` be a closed subvariety of dimension `d < n`, and let `T_i ⊆ X` be finitely
> many closed subvarieties of dimension `d' < n`. Then there is a closed subvariety `C ⊆ 𝐏(V)`
> whose prime cycle intersects that of `X` properly, with
>
> `C · X = [Z] + ∑ m_j [Z_j]`
>
> in the Tor-formula intersection product of Section 0B08, where the `Z_j ⊆ X` are irreducible
> closed of dimension `d`, distinct from `Z`, with nonzero multiplicities, and where
>
> * `dim (Z_j ∩ T_i) ≤ dim (Z ∩ T_i)` or `dim (Z_j ∩ T_i) + n ≤ d + d'`, and
> * `dim (Z_j ∩ T_i) < dim (Z ∩ T_i)` whenever `Z` does not intersect `T_i` properly inside `X`.
>
> The first clause is the disjunction that condition (4) of the source's proof yields; its first
> disjunct is the source's own inequality, which Tag 0AZP supplies from the second whenever
> `Z ∩ T_i` is nonempty, and which alone would be false in the bottom case `Z ∩ T_i = ∅` — see the
> quadric-surface counterexample in the implementation notes of this module. The second clause is
> vacuous exactly on that bottom case and needs no guard.

```lean
public theorem exists_intersectProperly_torFormulaCycleIntersectionProduct_eq
    (k V : Type u) [Field k] [IsAlgClosed k] [AddCommGroup V] [Module k V]
    [FiniteDimensional k V] [Nontrivial V] [DecidableEq (projectiveSpaceOfModule k V)]
    {N n d d' : ℕ} (hV : Module.finrank k V = N + 1)
    {X : Scheme.{u}} (iX : X ⟶ projectiveSpaceOfModule k V) [IsClosedImmersion iX]
    [IsVariety k (iX ≫ projectiveSpaceOfModuleToSpec k V)] (hXreg : IsRegular X)
    (hdimX : topologicalKrullDim X = (n : WithBot ℕ∞))
    (hd : d < n) (hd' : d' < n)
    (Z : Set X) (hZcl : IsClosed Z) (hZirr : IsIrreducible Z)
    (hZd : topologicalKrullDim ↥Z = (d : WithBot ℕ∞))
    {ι : Type*} [Finite ι] (T : ι → Set X) (hTcl : ∀ i, IsClosed (T i))
    (hTirr : ∀ i, IsIrreducible (T i))
    (hTd : ∀ i, topologicalKrullDim ↥(T i) = (d' : WithBot ℕ∞))
    (XC ZC : IrreducibleCloseds (projectiveSpaceOfModule k V))
    (TC : ι → IrreducibleCloseds (projectiveSpaceOfModule k V))
    (hXC : (XC : Set (projectiveSpaceOfModule k V)) = Set.range iX.base)
    (hZC : (ZC : Set (projectiveSpaceOfModule k V)) = iX.base '' Z)
    (hTC : ∀ i, (TC i : Set (projectiveSpaceOfModule k V)) = iX.base '' (T i)) :
    ∃ (C : IrreducibleCloseds (projectiveSpaceOfModule k V))
      (S : Finset (IrreducibleCloseds (projectiveSpaceOfModule k V)))
      (m : IrreducibleCloseds (projectiveSpaceOfModule k V) → ℤ),
      AlgebraicCycle.IntersectProperly
          (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
          (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)) ∧
        TorFormula.torFormulaCycleIntersectionProduct (fieldChowSituation k)
            (projectiveSpaceOfModuleToSpec k V) (isRegular_projectiveSpaceOfModule k V) (d : ℤ)
            (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
            (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)) =
          Function.locallyFinsuppWithin.single ZC.isIrreducible.genericPoint (1 : ℤ) +
            ∑ W ∈ S, m W • Function.locallyFinsuppWithin.single
              W.isIrreducible.genericPoint (1 : ℤ) ∧
        ZC ∉ S ∧ (∀ W ∈ S, m W ≠ 0) ∧
        (∀ W ∈ S, (W : Set (projectiveSpaceOfModule k V)) ⊆
          (XC : Set (projectiveSpaceOfModule k V))) ∧
        (∀ W ∈ S, topologicalKrullDim (W : Set (projectiveSpaceOfModule k V)) =
          (d : WithBot ℕ∞)) ∧
        (∀ W ∈ S, ∀ i,
          topologicalKrullDim ↥((W : Set (projectiveSpaceOfModule k V)) ∩
                (TC i : Set (projectiveSpaceOfModule k V))) ≤
              topologicalKrullDim ↥((ZC : Set (projectiveSpaceOfModule k V)) ∩
                (TC i : Set (projectiveSpaceOfModule k V))) ∨
            topologicalKrullDim ↥((W : Set (projectiveSpaceOfModule k V)) ∩
                  (TC i : Set (projectiveSpaceOfModule k V))) + (n : WithBot ℕ∞) ≤
              (d : WithBot ℕ∞) + (d' : WithBot ℕ∞)) ∧
        (∀ W ∈ S, ∀ i,
          ¬ (topologicalKrullDim ↥((ZC : Set (projectiveSpaceOfModule k V)) ∩
                  (TC i : Set (projectiveSpaceOfModule k V))) +
                topologicalKrullDim (XC : Set (projectiveSpaceOfModule k V)) ≤
              topologicalKrullDim (ZC : Set (projectiveSpaceOfModule k V)) +
                topologicalKrullDim (TC i : Set (projectiveSpaceOfModule k V))) →
            topologicalKrullDim ↥((W : Set (projectiveSpaceOfModule k V)) ∩
                (TC i : Set (projectiveSpaceOfModule k V))) <
              topologicalKrullDim ↥((ZC : Set (projectiveSpaceOfModule k V)) ∩
                (TC i : Set (projectiveSpaceOfModule k V))))
```

## Tag 0B1T, a lemma

[Tag 0B1T](https://stacks.math.columbia.edu/tag/0B1T) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endProjectionImage_eq_of_represents_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/MovingLemma.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/Projections/MovingLemma.lean#L183). The attribute's comment: “clause (2), C'\_0 = C, in the fibrewise form of this module: the fibre of the family over 0 = [id\_V] is r\_g(C) for g a representative of [id\_V], and that translate is C itself; the family C' and hence the scheme-theoretic reading of the equality are not constructed, see the implementation notes”.

> **Clause (2) of the Moving Lemma: the fibre over `0` is `C`.** Every endomorphism
> representing the point `[id_V]` of the parameter space is a unit scalar multiple of the
> identity, so the translate it induces is the identity on subsets of `𝐏(V)`.

```lean
public theorem endProjectionImage_eq_of_represents_identity [Nontrivial V]
    {p : ClosedPoints k (ParameterModule k V)}
    (hp : (p : projectiveSpaceOfModule k (ParameterModule k V)) = identityParameterPoint k V)
    {g : V →ₗ[k] V} (hg : RepresentsParameterPoint k V p g)
    (S : Set (projectiveSpaceOfModule k V)) :
    endProjectionImage k V g S = S
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_movingFamily_of_subvariety_fixed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/MovingLemmaFixedPoints.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/Projections/MovingLemmaFixedPoints.lean#L172). The attribute's comment: “the whole lemma, at the source's hypotheses and no others, over the source's fixed 𝐏^1 with its fixed points: C a closed subvariety of 𝐏^N = 𝐏(V) (an irreducible closed subset with its reduced structure), X a subvariety of 𝐏^N (an irreducible locally closed subset, not necessarily closed), T i ⊆ X finitely many closed subvarieties of X (irreducible, closed in X), C and X intersecting properly; for every projective line 𝐏^1 = 𝐏(W), dim\_k W = 2, and every pair of distinct closed points 0, ∞ of it, a closed subvariety C' of 𝐏^1 × 𝐏^N with (1) C' → 𝐏^1 dominant, read as density of the image; (2) C'\_0 = C scheme theoretically: the ideal sheaf of the reduced closed subscheme on C' pulled back along the section of 𝐏^1 × 𝐏^N → 𝐏^N at 0 is the ideal sheaf of the reduced closed subscheme on C; (3) C' and X × 𝐏^1 intersect properly; (4) C'\_∞ intersects each T i properly. Proper intersection is the dimension criterion of Definition 0AZQ read on the subsets”.

> **Stacks Project, Tag 0B1T, over a given projective line with given points `0 ≠ ∞`.** Let `C`
> be a closed subvariety of `𝐏^N = 𝐏(V)`, `X` a subvariety of `𝐏^N` (irreducible and locally
> closed, not necessarily closed), `T i ⊆ X` finitely many closed subvarieties of `X`, and assume
> `C` and `X` intersect properly. Let `𝐏^1 = 𝐏(W)`, `dim_k W = 2`, and let `0 ≠ ∞` be closed points
> of it. Then there is a closed subvariety `C'` of `𝐏^1 × 𝐏^N` such that
>
> 1. `C' → 𝐏^1` is dominant;
> 2. `C'_0 = C` scheme theoretically;
> 3. `C'` and `X × 𝐏^1` intersect properly;
> 4. `C'_∞` properly intersects each `T i`.
>
> Proper intersection is the dimension criterion of Definition 0AZQ read on the subsets. The
> instance `Nontrivial W` is implied by `dim_k W = 2` and is there only because the products and
> sections of `𝐏(W)` are stated under it. The family
> of `AlgebraicGeometry.ProjectiveSpaceOfModule.exists_movingFamily_of_subvariety` is transported
> along an isomorphism of projective lines carrying its points to the given ones.

```lean
public theorem exists_movingFamily_of_subvariety_fixed
    (C : IrreducibleCloseds (projectiveSpaceOfModule k V))
    (X : Set (projectiveSpaceOfModule k V)) (hX : IsLocallyClosed X) (hXirr : IsIrreducible X)
    (hCX : topologicalKrullDim ↥((C : Set (projectiveSpaceOfModule k V)) ∩ X) +
        topologicalKrullDim (projectiveSpaceOfModule k V) ≤
      topologicalKrullDim ↥(C : Set (projectiveSpaceOfModule k V)) + topologicalKrullDim ↥X)
    {ι : Type*} [Finite ι] (T : ι → Set (projectiveSpaceOfModule k V))
    (hTX : ∀ i, T i ⊆ X) (hTc : ∀ i, IsClosed {x : X | x.1 ∈ T i})
    (hTirr : ∀ i, IsIrreducible (T i))
    (W : Type u) [AddCommGroup W] [Module k W] [FiniteDimensional k W] [Nontrivial W]
    (hW : Module.finrank k W = 2) (zero infty : projectiveSpaceOfModule k W)
    (hzero : IsClosed ({zero} : Set (projectiveSpaceOfModule k W)))
    (hinfty : IsClosed ({infty} : Set (projectiveSpaceOfModule k W))) (hne : zero ≠ infty) :
    ∃ Cfam : IrreducibleCloseds (lineProduct k V W),
      closure ((lineProductLine k V W).base '' (Cfam : Set (lineProduct k V W))) = Set.univ ∧
      (Scheme.IdealSheafData.vanishingIdeal
            (⟨Cfam, Cfam.isClosed'⟩ : Closeds (lineProduct k V W))).comap
          (lineProductSection k V W zero hzero) =
        Scheme.IdealSheafData.vanishingIdeal
          (⟨C, C.isClosed'⟩ : Closeds (projectiveSpaceOfModule k V)) ∧
      topologicalKrullDim ↥((Cfam : Set (lineProduct k V W)) ∩ lineProductConstant k V W X) +
          topologicalKrullDim (lineProduct k V W) ≤
        topologicalKrullDim ↥(Cfam : Set (lineProduct k V W)) +
          topologicalKrullDim ↥(lineProductConstant k V W X) ∧
      ∀ i, topologicalKrullDim
            ↥(lineProductFibre k V W infty hinfty (Cfam : Set (lineProduct k V W)) ∩ T i) +
          topologicalKrullDim (projectiveSpaceOfModule k V) ≤
        topologicalKrullDim
            ↥(lineProductFibre k V W infty hinfty (Cfam : Set (lineProduct k V W))) +
          topologicalKrullDim ↥(T i)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_forall_closedPoint_line_moving_of_codimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/MovingLemmaOfCodimension.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/Projections/MovingLemmaOfCodimension.lean#L190). The attribute's comment: “clauses (1), (3) and (4), read on the fibres, in the form that assumes bounds on the two bad loci: 𝐏^1 is the source's own line ℓ ⊆ 𝐏 = 𝐏((End V)ᵛ) through [id\_V] and the fibre C'\_[g] is the translate r\_g(C), so that (1) 'C' → 𝐏^1 is dominant' is read as 'the fibre over every closed point of ℓ is nonempty', (3) as 'r\_g(C) intersects X properly for every representative g of every closed point of ℓ' and (4) as 'r\_g(C) intersects each T i properly for every representative g of the ∞ point of ℓ'; clause (2) is endProjectionImage\_eq\_of\_represents\_identity of this module; 'general' is read as in Tags 0B2T and 0B1S, namely that there is a nonempty Zariski open subset of 𝐏 each of whose closed points is the ∞ point of such a line; proper intersection is the dimension criterion defining Tag 0AZQ read on the image set r\_g(C), as in Tag 0B1S; X is taken closed in this form, Lemma 0B1S being formalized for a pair of closed subvarieties. The two bad-locus bounds are discharged by AlgebraicGeometry.ProjectiveSpaceOfModule .exists\_isOpen\_forall\_closedPoint\_line\_moving\_of\_intersectProperly of StacksFrontier.AlgebraicGeometry.Intersection.Projections.MovingFamilyMain, and the tag is registered for all four clauses about the family C' over 𝐏^1 at the source's own hypotheses on C, X (not necessarily closed) and the T i, clause (2) scheme theoretically, on AlgebraicGeometry.ProjectiveSpaceOfModule.exists\_movingFamily\_of\_subvariety\_fixed of StacksFrontier.AlgebraicGeometry.Intersection.Projections.MovingLemmaFixedPoints; this form keeps its place here, upstream of the incidence-correspondence construction that either discharge needs”.

> **Stacks Project, Tag 0B1T.** Let `C, X` be closed subvarieties of
> `𝐏(V)` which intersect properly, with `C ≠ 𝐏(V)` and `C ∩ X ≠ ∅`, and let `T i ⊆ X` be a finite
> collection of closed subvarieties. Suppose the bad locus of `(C, X)` in the parameter space
> `𝐏 = 𝐏((End V)ᵛ)` is contained in a closed subset `B` which has codimension at least two at each
> of its points and does not contain `[id_V]`, and that for each `i` the bad locus of `(C, T i)` is
> contained in a closed subset `BT i` other than all of `𝐏`. Then for a
> general line `ℓ ⊆ 𝐏` through `[id_V]` — that is, for the line through `[id_V]` and any closed
> point `∞` of a nonempty Zariski open subset of `𝐏` — the four clauses of the source hold of the
> family whose fibre over a point `[g]` of `ℓ` is the translate `r_g(C)`: that family is dominant
> over `ℓ`, because `r_g(C)` is nonempty for every representative `g` of every closed point of
> `ℓ`; its fibre over `0 = [id_V]` is `C`; it meets the constant family `X × ℓ` properly, because
> `r_g(C)` meets `X` properly at every closed point of `ℓ`; and its fibre over `∞` meets each
> `T i` properly.
>
> Both families of hypotheses are carried, this module being upstream of either discharge, which
> is why Tag 0B1T is registered not here but on the form over `𝐏^1`
> `…ProjectiveSpaceOfModule.exists_movingFamily_of_subvariety_fixed` of
> `StacksFrontier.AlgebraicGeometry.Intersection.Projections.MovingLemmaFixedPoints`, which
> states all four clauses about the family itself at the source's hypotheses alone.

```lean
public theorem exists_isOpen_forall_closedPoint_line_moving_of_codimension [Nontrivial V]
    (C X : IrreducibleCloseds (projectiveSpaceOfModule k V)) (hCX : IntersectProperly C X)
    (hCne : (C : Set (projectiveSpaceOfModule k V)) ≠ Set.univ)
    (hCXne : ((C : Set (projectiveSpaceOfModule k V)) ∩
      (X : Set (projectiveSpaceOfModule k V))).Nonempty)
    {ι : Type*} [Finite ι] (T : ι → IrreducibleCloseds (projectiveSpaceOfModule k V))
    (_hTX : ∀ i, (T i : Set (projectiveSpaceOfModule k V)) ⊆
      (X : Set (projectiveSpaceOfModule k V)))
    (B : Set (projectiveSpaceOfModule k (ParameterModule k V))) (hBc : IsClosed B)
    (hB : ∀ p : ClosedPoints k (ParameterModule k V),
      (p : projectiveSpaceOfModule k (ParameterModule k V)) ∈
          badParameterLocus k V (C : Set (projectiveSpaceOfModule k V))
            (X : Set (projectiveSpaceOfModule k V)) →
        (p : projectiveSpaceOfModule k (ParameterModule k V)) ∈ B)
    (hBid : identityParameterPoint k V ∉ B)
    (hcodim : ∀ x ∈ B, (2 : ℕ∞) ≤ codimension (IrreducibleCloseds.closureSingleton x))
    (BT : ι → Set (projectiveSpaceOfModule k (ParameterModule k V)))
    (hBT : ∀ i, IsClosed (BT i)) (hBTne : ∀ i, BT i ≠ Set.univ)
    (hBTbad : ∀ (i) (p : ClosedPoints k (ParameterModule k V)),
      (p : projectiveSpaceOfModule k (ParameterModule k V)) ∈
          badParameterLocus k V (C : Set (projectiveSpaceOfModule k V))
            (T i : Set (projectiveSpaceOfModule k V)) →
        (p : projectiveSpaceOfModule k (ParameterModule k V)) ∈ BT i) :
    ∃ U : Set (projectiveSpaceOfModule k (ParameterModule k V)), IsOpen U ∧ U.Nonempty ∧
      ∀ q ∈ U, IsClosed ({q} : Set (projectiveSpaceOfModule k (ParameterModule k V))) →
        ∃ L : Submodule k (ParameterModule k V),
          Module.finrank k (ParameterModule k V ⧸ L) = 2 ∧
          identityParameterPoint k V ∈ linearSubspace k (ParameterModule k V) L ∧
          q ∈ linearSubspace k (ParameterModule k V) L ∧
          (∀ p : ClosedPoints k (ParameterModule k V),
            (p : projectiveSpaceOfModule k (ParameterModule k V)) ∈
              linearSubspace k (ParameterModule k V) L →
            ∀ g : V →ₗ[k] V, RepresentsParameterPoint k V p g →
              (endProjectionImage k V g (C : Set (projectiveSpaceOfModule k V))).Nonempty ∧
                IsGoodEndomorphism k V (C : Set (projectiveSpaceOfModule k V))
                  (X : Set (projectiveSpaceOfModule k V)) g) ∧
          (∀ p : ClosedPoints k (ParameterModule k V),
            (p : projectiveSpaceOfModule k (ParameterModule k V)) =
              identityParameterPoint k V →
            ∀ g : V →ₗ[k] V, RepresentsParameterPoint k V p g →
              endProjectionImage k V g (C : Set (projectiveSpaceOfModule k V)) =
                (C : Set (projectiveSpaceOfModule k V))) ∧
          ∀ p : ClosedPoints k (ParameterModule k V),
            (p : projectiveSpaceOfModule k (ParameterModule k V)) = q →
            ∀ g : V →ₗ[k] V, RepresentsParameterPoint k V p g → ∀ i,
              IsGoodEndomorphism k V (C : Set (projectiveSpaceOfModule k V))
                (T i : Set (projectiveSpaceOfModule k V)) g
```

## Tag 0B1U, a lemma

[Tag 0B1U](https://stacks.math.columbia.edu/tag/0B1U) in the Stacks Project.

**`AlgebraicGeometry.exists_rationallyEquivalent_forall_intersectProperly`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/MovingCycles.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/MovingCycles.lean#L97). The attribute's comment: “for a finite family of cycles `β i` of arbitrary dimensions `s i` in place of the single `s`-cycle `β`, which is the case of a one-element family; `r` and the `s i` are arbitrary integers. Nonsingular is `IsRegular X`, projective variety is `IsProjectiveVariety`, cycles are the graded cycle groups `Stacks.Chow.CycleGroup` over `Spec k`, rational equivalence is Tag 02RW and proper intersection is Definition 0AZQ. The proof replaces the source's degeneration of the cone `C` in `𝐏^N × 𝐏^1` (Tags 0B1T, 0B1M, 0B07) by the flat pullback along the finite projection `π : X → 𝐏^n` of the proof of Tag 0B0E, which is flat by miracle flatness, together with moving `π(Z)` inside `𝐏^n`”.

> **Stacks Project, Tag 0B1U, for a finite family of cycles.** Let `X` be a nonsingular
> projective variety over an algebraically closed field, let `α` be an `r`-cycle on `X` and let
> `β i` be finitely many cycles on `X`, of dimensions `s i`. Then there is an `r`-cycle `α'` with
> `α' ∼_rat α` which intersects every `β i` properly. This is the case of
> `exists_rationallyEquivalent_forall_intersectProperly_of_isQuasiProjectiveVariety` for a
> projective variety.

```lean
public theorem exists_rationallyEquivalent_forall_intersectProperly (k : Type u) [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k)) [IsProjectiveVariety k sX]
    (hX : IsRegular X) {r : ℤ} (α : CycleGroup (fieldChowSituation k) sX r)
    {ι : Type*} [Finite ι] (s : ι → ℤ) (β : ∀ i, CycleGroup (fieldChowSituation k) sX (s i)) :
    ∃ α' : CycleGroup (fieldChowSituation k) sX r,
      RationallyEquivalent (fieldChowSituation k) sX r α' α ∧
        ∀ i, AlgebraicCycle.IntersectProperly α'.1 (β i).1
```

**`AlgebraicGeometry.exists_rationallyEquivalent_intersectProperly`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/MovingCycles.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/MovingCycles.lean#L115). The attribute's comment: “as stated: nonsingular is `IsRegular X`, projective variety is `IsProjectiveVariety`, cycles are the graded cycle groups `Stacks.Chow.CycleGroup` over `Spec k`, rational equivalence is Tag 02RW and proper intersection is Definition 0AZQ; `r` and `s` are arbitrary integers”.

> **Stacks Project, Tag 0B1U.** Let `X` be a nonsingular projective variety over an
> algebraically closed field, let `α` be an `r`-cycle and `β` an `s`-cycle on `X`. Then there is an
> `r`-cycle `α'` with `α' ∼_rat α` which intersects `β` properly.

```lean
public theorem exists_rationallyEquivalent_intersectProperly (k : Type u) [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k)) [IsProjectiveVariety k sX]
    (hX : IsRegular X) {r s : ℤ} (α : CycleGroup (fieldChowSituation k) sX r)
    (β : CycleGroup (fieldChowSituation k) sX s) :
    ∃ α' : CycleGroup (fieldChowSituation k) sX r,
      RationallyEquivalent (fieldChowSituation k) sX r α' α ∧
        AlgebraicCycle.IntersectProperly α'.1 β.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.24, Tag 0B0D](https://stacks.math.columbia.edu/tag/0B0D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
