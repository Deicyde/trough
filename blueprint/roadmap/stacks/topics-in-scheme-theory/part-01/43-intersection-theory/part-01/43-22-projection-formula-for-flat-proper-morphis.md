---
declaration: section
origin: cited
lean: Stacks.Intersection.ProjectionFormula.intersectProperly_coherentSheafCycle_pushforward_unconditional, Stacks.Intersection.ProjectionFormula.properPushforward_intersectionProductCycleGroup_unconditional, Stacks.Intersection.ProjectionFormula.properPushforward_torFormulaCycleIntersectionProduct_eq, Stacks.Intersection.intersectionProduct_zeroFibre_eq_properPushforward_zeroSection
statement: formalized
proof: formalized
---

# 43.22 Projection formula for flat proper morphisms

Section 43.22 of the Stacks Project, [Tag 0B0C](https://stacks.math.columbia.edu/tag/0B0C). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B10, a lemma

[Tag 0B10](https://stacks.math.columbia.edu/tag/0B10) in the Stacks Project.

**`Stacks.Intersection.ProjectionFormula.intersectProperly_coherentSheafCycle_pushforward_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/Basic.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/Basic.lean#L385). The attribute's comment: “the properness clause for `α = [ℱ]_r` and `β = [𝒢]_s`”.

> Let `f : X ⟶ Y` be a flat proper morphism of varieties over a field with `dim X = dim Y + e`,
> let `ℱ` be a coherent `𝒪_X`-module whose support has dimension at most `r` and `𝒢` a coherent
> `𝒪_Y`-module whose support has dimension at most `s`, and assume that `Supp(ℱ)` and
> `f^{-1}(Supp(𝒢))` meet in dimension at most `r + (s + e) - dim X`. Then the cycles
> `f_*[ℱ]_r = [f_*ℱ]_r` and `[𝒢]_s` intersect properly.

```lean
theorem intersectProperly_coherentSheafCycle_pushforward_unconditional (K : Type u) [Field K]
    {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K)) [IsVariety K sX]
    [IsVariety K sY] (f : X ⟶ Y) [Flat f] [IsProper f] (hbase : f ≫ sY = sX) (e : ℕ)
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞)) (F : X.Modules)
    [F.IsCoherent] (G : Y.Modules) [G.IsCoherent] (r s : ℕ)
    (hFr : schemeDeltaDimension (fieldChowSituation K)
      ((reducedSupport F).subschemeι ≫ sX) ≤ ((r : ℤ) : EInt))
    (hGs : schemeDeltaDimension (fieldChowSituation K)
      ((reducedSupport G).subschemeι ≫ sY) ≤ ((s : ℤ) : EInt))
    (hFG : topologicalKrullDim
        (SheafOfModules.supp F ∩ f.base ⁻¹' SheafOfModules.supp G : Set X) +
      topologicalKrullDim X ≤ (r : WithBot ℕ∞) + ((s + e : ℕ) : WithBot ℕ∞)) :
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    haveI := AlgebraicGeometry.ProperCoherenceWitness.isCoherent_pushforward f F
    AlgebraicCycle.IntersectProperly
      (coherentSheafCycle (fieldChowSituation K) sY ((Scheme.Modules.pushforward f).obj F)
        (r : ℤ)
        (schemeDeltaDimension_reducedSupport_pushforward_le (fieldChowSituation K) sX sY f hbase
          F hFr))
      (coherentSheafCycle (fieldChowSituation K) sY G (s : ℤ) hGs)
```

**`Stacks.Intersection.ProjectionFormula.properPushforward_intersectionProductCycleGroup_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/Basic.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/Basic.lean#L419). The attribute's comment: “the identity `f_*(α) · β = f_*(α · f^*β)` for `α = [ℱ]_r` and `β = [𝒢]_s`, both products read by the Tor formula `∑ᵢ (-1)ⁱ [Torᵢ]_n` of Stacks 0AZR”.

> Let `f : X ⟶ Y` be a flat proper morphism of nonsingular varieties over a field. For a
> coherent `𝒪_X`-module `ℱ` and a coherent `𝒪_Y`-module `𝒢`, proper pushforward carries the
> intersection product of `ℱ` and `f^*𝒢` to the intersection product of `f_*ℱ` and `𝒢`:
>
> `f_*(∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_X}(ℱ, f^*𝒢)]_n) = ∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_Y}(f_*ℱ, 𝒢)]_n`.
>
> Taking `n = r + s - dim Y`, for supports of dimension at most `r` and `s` and `e = dim X - dim Y`,
> this is `f_*([ℱ]_r · [f^*𝒢]_{s+e}) = [f_*ℱ]_r · [𝒢]_s`, that is `f_*(α · f^*β) = f_*(α) · β`.

```lean
theorem properPushforward_intersectionProductCycleGroup_unconditional (K : Type u) [Field K]
    {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K)) [IsVariety K sX]
    [IsVariety K sY] (hX : AlgebraicGeometry.IsRegular X) (hY : AlgebraicGeometry.IsRegular Y)
    (f : X ⟶ Y) [Flat f] [IsProper f] (hbase : f ≫ sY = sX) (F : X.Modules)
    (hF : _root_.SheafOfModules.IsCoherent F) (G : Y.Modules)
    (hG : _root_.SheafOfModules.IsCoherent G) (n : ℤ)
    (hFn : ∀ i : ℕ,
      haveI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
      haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
      haveI := isCoherent_torSheaf_of_isRegular X hX F ((Scheme.Modules.pullback f).obj G) hF
        (isCoherent_pullback f G) i
      schemeDeltaDimension (fieldChowSituation K)
        ((reducedSupport (torSheaf X F ((Scheme.Modules.pullback f).obj G) i)).subschemeι ≫ sX)
          ≤ (n : EInt)) :
    haveI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    properPushforward (fieldChowSituation K) sX sY f hbase n
        (intersectionProductCycleGroup (fieldChowSituation K) sX hX F
          ((Scheme.Modules.pullback f).obj G) hF (isCoherent_pullback f G) n hFn) =
      intersectionProductCycleGroup (fieldChowSituation K) sY hY
        ((Scheme.Modules.pushforward f).obj F) G
        (@AlgebraicGeometry.ProperCoherenceWitness.isCoherent_pushforward _ _ f _ _ F hF) hG n
        (schemeDeltaDimension_reducedSupport_torSheaf_pushforward_le_of_bound K sX sY hX hY f
          hbase F hF G hG n hFn)
```

**`Stacks.Intersection.ProjectionFormula.properPushforward_torFormulaCycleIntersectionProduct_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/Cycles.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/Cycles.lean#L527). The attribute's comment: “the whole lemma: both that `f_*α` and `β` intersect properly and the identity `f_*(α) · β = f_*(α · f^*β)`, for arbitrary cycles `α ∈ Z_r(X)` and `β ∈ Z_s(Y)` and every `r`, `s`, under the source's assumption that `α` and `f^*β` intersect properly, for a flat proper morphism of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — with `dim X = dim Y + e`. The products are the Section 43.17 product of cycles of Tag 0B08 in dimension `n = r + s - dim Y`, an integer.”.

> **Stacks Project, Tag 0B10.** Let `f : X ⟶ Y` be a flat proper morphism of nonsingular
> varieties over an algebraically closed field `K` — the chapter's convention, Tag 0AZ8 — with
> `dim X = dim Y + e`. Let `α` be an `r`-cycle on `X` and `β` an `s`-cycle on `Y`, and assume that
> `α` and `f^*β` intersect properly. Then `f_*α` and `β` intersect properly and
>
> `f_*(α) · β = f_*(α · f^*β)`.
>
> The products are the intersection product of cycles of Tag 0B08 in dimension
> `n = r + s - dim Y`, an integer: on `X` the same `n` is `r + (s + e) - dim X`. When `n < 0` the
> supports of `f_*α` and `β` are disjoint and both products vanish, as there are no cycles of
> negative dimension.

```lean
theorem properPushforward_torFormulaCycleIntersectionProduct_eq (K : Type u) [Field K]
    [IsAlgClosed K] {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K))
    [IsVariety K sX] [IsVariety K sY] (hX : AlgebraicGeometry.IsRegular X)
    (hY : AlgebraicGeometry.IsRegular Y) (f : X ⟶ Y) [Flat f] [IsProper f]
    (hbase : f ≫ sY = sX) (e dY r s : ℕ) (n : ℤ)
    (hdY : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (hrs : (r : ℤ) + (s : ℤ) = (dY : ℤ) + n)
    (α : CycleGroup (fieldChowSituation K) sX (r : ℤ))
    (β : CycleGroup (fieldChowSituation K) sY (s : ℤ))
    (hαβ : haveI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
      AlgebraicCycle.IntersectProperly α.1
        (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (s : ℤ) β).1) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    AlgebraicCycle.IntersectProperly
        (properPushforward (fieldChowSituation K) sX sY f hbase (r : ℤ) α).1 β.1 ∧
      (properPushforward (fieldChowSituation K) sX sY f hbase n
          ⟨torFormulaCycleIntersectionProduct (fieldChowSituation K) sX hX n α.1
              (flatPullback (fieldChowSituation K) sX sY f hbase e
                (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (s : ℤ) β).1,
            torFormulaCycleIntersectionProduct_mem_cyclesOfDimension (fieldChowSituation K) sX hX
              n _ _⟩).1 =
        torFormulaCycleIntersectionProduct (fieldChowSituation K) sY hY n
          (properPushforward (fieldChowSituation K) sX sY f hbase (r : ℤ) α).1 β.1
```

## Tag 0B1M, a lemma

[Tag 0B1M](https://stacks.math.columbia.edu/tag/0B1M) in the Stacks Project.

**`Stacks.Intersection.intersectionProduct_zeroFibre_eq_properPushforward_zeroSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/ZeroFibreDegeneration/ZeroFibreIntersection.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProjectionFormulaFlat/ZeroFibreDegeneration/ZeroFibreIntersection.lean#L496). The attribute's comment: “the whole lemma, for a closed immersion of nonsingular varieties over an algebraically closed field and a closed subvariety `C'` of `P × 𝐏¹` presented as an integral closed subscheme: clause (1) is the dimension of the scheme-theoretic zero fibre, clause (2) the Tag 0AZQ inequality for `C'` and `X × 𝐏¹`, clause (3) proper intersection of the cycles `[C]_r` and `[X]`. The conclusion states that the two products are pushforwards of cycles `α` on `X` and `β` on `X × 𝐏¹`, that `β` and `X × 0` intersect properly, and that `α = pr_{X,*}(β · X × 0)` for every such `α` and `β`.”.

> **Stacks Project, Tag 0B1M.** Let `X ⟶ P` be a closed immersion of nonsingular varieties over
> an algebraically closed field `K`, of dimensions `d` and `p`, and let `C' ⊆ P × 𝐏¹` be a closed
> subvariety of dimension `r + 1` such that
>
> 1. the zero fibre `C = C'_0` (the scheme-theoretic fibre `zeroFiber sP C'`) has dimension `r`,
> 2. `C'` intersects `X × 𝐏¹` properly,
> 3. `[C]_r` intersects `X` properly.
>
> Then `[C]_r · X`, an `(r + d - p)`-cycle on `P`, is the pushforward of a cycle `α` on `X`, and
> `C' · X × 𝐏¹`, an `(r + d - p + 1)`-cycle on `P × 𝐏¹`, is the pushforward of a cycle `β` on
> `X × 𝐏¹`; and for any such `α` and `β`, the cycle `β` intersects `X × 0` properly and
>
> `α = pr_{X,*}(β · X × 0)`.
>
> The intersection products are those of Tag 0B08, `X × 𝐏¹ ⟶ P × 𝐏¹` is the base change of `ι`,
> `X × 0` is the image of the zero section, and `pr_X` is the first projection.

```lean
theorem intersectionProduct_zeroFibre_eq_properPushforward_zeroSection
    [IsAlgClosed K] {X P : Scheme.{u}} (sP : P ⟶ Spec (.of K)) [IsVariety K sP]
    (ι : X ⟶ P) [IsClosedImmersion ι] [IsVariety K (ι ≫ sP)] (hX : IsRegular X)
    (hP : IsRegular P) (d p r : ℕ) (hd : topologicalKrullDim X = (d : WithBot ℕ∞))
    (hp : topologicalKrullDim P = (p : WithBot ℕ∞))
    (C' : (projectiveLineProduct sP).IdealSheafData) [IsIntegral C'.subscheme]
    (hC' : topologicalKrullDim (C'.support : Set (projectiveLineProduct sP)) =
      ((r + 1 : ℕ) : WithBot ℕ∞))
    (h1 : topologicalKrullDim ((zeroFiber sP C').support : Set P) = (r : WithBot ℕ∞))
    (h2 : topologicalKrullDim ↥((C'.support : Set (projectiveLineProduct sP)) ∩
          Set.range (familyBaseChange sP ι).base) +
        topologicalKrullDim (projectiveLineProduct sP) ≤
      topologicalKrullDim (C'.support : Set (projectiveLineProduct sP)) +
        topologicalKrullDim (Set.range (familyBaseChange sP ι).base))
    (h3 : AlgebraicCycle.IntersectProperly
      (cycleAssociatedToClosedSubscheme (fieldChowSituation K) sP
        (zeroFiber sP C').subschemeι (r : ℤ)).1
      (Function.locallyFinsuppWithin.single (ι.base (genericPoint X)) (1 : ℤ))) :
    letI : IsLocallyNoetherian P := isLocallyNoetherian_of_isRegular hP
    letI : IsLocallyNoetherian (projectiveLineProduct sP) :=
      isLocallyNoetherian_of_isRegular (isRegular_projectiveLineProduct sP hP)
    letI : IsLocallyNoetherian (projectiveLineProduct (ι ≫ sP)) :=
      isLocallyNoetherian_of_isRegular (isRegular_projectiveLineProduct (ι ≫ sP) hX)
    (∃ α : CycleGroup (fieldChowSituation K) (ι ≫ sP) ((r : ℤ) + d - p),
        (properPushforward (fieldChowSituation K) (ι ≫ sP) sP ι rfl _ α).1 =
          torFormulaCycleIntersectionProduct (fieldChowSituation K) sP hP ((r : ℤ) + d - p)
            (cycleAssociatedToClosedSubscheme (fieldChowSituation K) sP
              (zeroFiber sP C').subschemeι (r : ℤ)).1
            (Function.locallyFinsuppWithin.single (ι.base (genericPoint X)) 1)) ∧
      (∃ β : CycleGroup (fieldChowSituation K)
          (pullback.fst (ι ≫ sP) (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫ ι ≫ sP)
          ((r : ℤ) + d - p + 1),
        (properPushforward (fieldChowSituation K) _
            (pullback.fst sP (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫ sP)
            (familyBaseChange sP ι) (familyBaseChange_comp_structure K sP ι) _ β).1 =
          torFormulaCycleIntersectionProduct (fieldChowSituation K)
            (pullback.fst sP (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫ sP)
            (isRegular_projectiveLineProduct sP hP) ((r : ℤ) + d - p + 1)
            (Function.locallyFinsuppWithin.single
              (C'.subschemeι.base (genericPoint C'.subscheme)) 1)
            (Function.locallyFinsuppWithin.single
              ((familyBaseChange sP ι).base (genericPoint (projectiveLineProduct (ι ≫ sP)))) 1))
        ∧
      ∀ (α : CycleGroup (fieldChowSituation K) (ι ≫ sP) ((r : ℤ) + d - p))
        (β : CycleGroup (fieldChowSituation K)
          (pullback.fst (ι ≫ sP) (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫ ι ≫ sP)
          ((r : ℤ) + d - p + 1)),
        (properPushforward (fieldChowSituation K) (ι ≫ sP) sP ι rfl _ α).1 =
          torFormulaCycleIntersectionProduct (fieldChowSituation K) sP hP ((r : ℤ) + d - p)
            (cycleAssociatedToClosedSubscheme (fieldChowSituation K) sP
              (zeroFiber sP C').subschemeι (r : ℤ)).1
            (Function.locallyFinsuppWithin.single (ι.base (genericPoint X)) 1) →
        (properPushforward (fieldChowSituation K) _
            (pullback.fst sP (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫ sP)
            (familyBaseChange sP ι) (familyBaseChange_comp_structure K sP ι) _ β).1 =
          torFormulaCycleIntersectionProduct (fieldChowSituation K)
            (pullback.fst sP (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫ sP)
            (isRegular_projectiveLineProduct sP hP) ((r : ℤ) + d - p + 1)
            (Function.locallyFinsuppWithin.single
              (C'.subschemeι.base (genericPoint C'.subscheme)) 1)
            (Function.locallyFinsuppWithin.single
              ((familyBaseChange sP ι).base (genericPoint (projectiveLineProduct (ι ≫ sP)))) 1) →
        AlgebraicCycle.IntersectProperly β.1
            (Function.locallyFinsuppWithin.single
              ((zeroSection (ι ≫ sP)).base (genericPoint X)) 1) ∧
          α = properPushforward (fieldChowSituation K)
            (pullback.fst (ι ≫ sP) (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫ ι ≫ sP)
            (ι ≫ sP) (pullback.fst (ι ≫ sP) (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)))
            rfl ((r : ℤ) + d - p)
            ⟨torFormulaCycleIntersectionProduct (fieldChowSituation K)
                (pullback.fst (ι ≫ sP) (relativeProjectiveLine (Spec (.of K)) ↘ Spec (.of K)) ≫
                  ι ≫ sP)
                (isRegular_projectiveLineProduct (ι ≫ sP) hX) ((r : ℤ) + d - p) β.1
                (Function.locallyFinsuppWithin.single
                  ((zeroSection (ι ≫ sP)).base (genericPoint X)) 1),
              torFormulaCycleIntersectionProduct_mem_cyclesOfDimension _ _ _ _ _ _⟩
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.22, Tag 0B0C](https://stacks.math.columbia.edu/tag/0B0C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
