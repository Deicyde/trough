---
declaration: section
origin: cited
lean: AlgebraicGeometry.TorFormula.cycleIntersectionProduct, AlgebraicGeometry.TorFormula.cycleIntersectionProduct_eq_sum, AlgebraicGeometry.TorFormula.cycleIntersectionProduct_single_single, AlgebraicGeometry.TorFormula.cycleIntersectionProduct_single_right, AlgebraicGeometry.TorFormula.cycleIntersectionProduct_single_left, AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct, AlgebraicGeometry.TorFormula.torFormulaSubvarietyProductTotal_eq_of_intersectProperly, Stacks.Chow.tag_0B07
statement: formalized
proof: formalized
---

# 43.17 Intersection product using Tor formula

Section 43.17 of the Stacks Project, [Tag 0B08](https://stacks.math.columbia.edu/tag/0B08). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B08, the section

[Tag 0B08](https://stacks.math.columbia.edu/tag/0B08) in the Stacks Project.

**`AlgebraicGeometry.TorFormula.cycleIntersectionProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean#L135). The attribute's comment: “the displayed definition `α · β = ∑ᵢⱼ nᵢ mⱼ Wᵢ · Vⱼ` of the intersection product of an `r`-cycle and an `s`-cycle, with no hypotheses, for the product `Wᵢ · Vⱼ` of two closed subvarieties of Section 43.14 supplied as the parameter `prod`. Closed subvarieties are their generic points, so `prod` is a function of two points and the sum is indexed by `X × X`; the pairs that contribute are the pairs of components of `α` and `β`, and `cycleIntersectionProduct_eq_sum` identifies the value with the finite double sum displayed by the source. The instance of this definition in which `prod` is the Tor-formula product of Section 43.14 is `torFormulaCycleIntersectionProduct`.”.

> **Stacks 0B08: the intersection product of two cycles.** For a rule `prod` assigning a cycle
> to a pair of closed subvarieties of `X`, the bilinear extension `α · β = ∑ᵢⱼ nᵢ mⱼ Wᵢ · Vⱼ` of
> `prod` to cycles `α = ∑ᵢ nᵢ [Wᵢ]` and `β = ∑ⱼ mⱼ [Vⱼ]`.

```lean
def cycleIntersectionProduct (prod : X → X → AlgebraicCycle X ℤ)
    (α β : AlgebraicCycle X ℤ) : AlgebraicCycle X ℤ
```

**`AlgebraicGeometry.TorFormula.cycleIntersectionProduct_eq_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean#L169). The attribute's comment: “the display `α · β = ∑ᵢⱼ nᵢ mⱼ Wᵢ · Vⱼ` as a finite double sum over the components of the two cycles, assuming each has finitely many components — which on a quasi-compact scheme, in particular on a variety, is automatic by `finite_support_of_compactSpace`.”.

> **The display of Stacks 0B08.** For cycles `α = ∑ᵢ nᵢ [Wᵢ]` and `β = ∑ⱼ mⱼ [Vⱼ]` with
> finitely many components, `α · β = ∑ᵢⱼ nᵢ mⱼ Wᵢ · Vⱼ` as a finite double sum.

```lean
theorem cycleIntersectionProduct_eq_sum (prod : X → X → AlgebraicCycle X ℤ)
    {α β : AlgebraicCycle X ℤ} (hα : (Function.support α).Finite)
    (hβ : (Function.support β).Finite) :
    cycleIntersectionProduct prod α β =
      ∑ x ∈ hα.toFinset, ∑ y ∈ hβ.toFinset, (α x * β y) • prod x y
```

**`AlgebraicGeometry.TorFormula.cycleIntersectionProduct_single_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean#L360). The attribute's comment: “the one-term case of the display, with NO hypotheses: on the prime cycles `α = m [W]` and `β = n [V]` the product is `m n (W · V)`, so the bilinear extension really does extend the product of two closed subvarieties of Section 43.14. This is the clause of the section that is carried unrestrictedly; the full display needs each cycle to have finitely many components (`cycleIntersectionProduct_eq_sum`).”.

> On two prime cycles the intersection product is the product of the two closed subvarieties:
> `[W] · [V] = W · V`.

```lean
theorem cycleIntersectionProduct_single_single [DecidableEq X]
    (prod : X → X → AlgebraicCycle X ℤ) (x y : X) (m n : ℤ) :
    cycleIntersectionProduct prod (Function.locallyFinsuppWithin.single x m)
      (Function.locallyFinsuppWithin.single y n) = (m * n) • prod x y
```

**`AlgebraicGeometry.TorFormula.cycleIntersectionProduct_single_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean#L377). The attribute's comment: “the final clause of the section: for `β = [V]` the prime cycle of a closed subvariety `V`, the product `α · β`, there written `α · V`, is `∑ᵢ nᵢ Wᵢ · V`. Assumes `α` has finitely many components.”.

> **The clause `α · V` of Stacks 0B08.** For `β = [V]` the prime cycle of a closed subvariety,
> the intersection product is `α · V = ∑ᵢ nᵢ Wᵢ · V`.

```lean
theorem cycleIntersectionProduct_single_right [DecidableEq X]
    (prod : X → X → AlgebraicCycle X ℤ) {α : AlgebraicCycle X ℤ}
    (hα : (Function.support α).Finite) (y : X) :
    cycleIntersectionProduct prod α (Function.locallyFinsuppWithin.single y 1) =
      ∑ x ∈ hα.toFinset, α x • prod x y
```

**`AlgebraicGeometry.TorFormula.cycleIntersectionProduct_single_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean#L397). The attribute's comment: “the first-variable form of the final clause of the section: for `α = [W]` the prime cycle of a closed subvariety `W`, the product `α · β` is `∑ⱼ mⱼ W · Vⱼ`. Assumes `β` has finitely many components.”.

> **The clause `W · β` of Stacks 0B08.** For `α = [W]` the prime cycle of a closed subvariety,
> the intersection product is `W · β = ∑ⱼ mⱼ W · Vⱼ`.

```lean
theorem cycleIntersectionProduct_single_left [DecidableEq X]
    (prod : X → X → AlgebraicCycle X ℤ) {β : AlgebraicCycle X ℤ}
    (hβ : (Function.support β).Finite) (x : X) :
    cycleIntersectionProduct prod (Function.locallyFinsuppWithin.single x 1) β =
      ∑ y ∈ hβ.toFinset, β y • prod x y
```

**`AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean#L529). The attribute's comment: “the intersection product α · β, total in the Tor-support bound”.

> **Stacks 0B08 for the Tor formula.** The intersection product `α · β = ∑ᵢⱼ nᵢ mⱼ Wᵢ · Vⱼ` of
> two cycles on a regular scheme, with `Wᵢ · Vⱼ` the Tor-formula product of Section 43.14.

```lean
def torFormulaCycleIntersectionProduct (C : Stacks.Chow.ChowSituation.{u}) {X : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f] [IsLocallyNoetherian X] (hX : IsRegular X) (k : ℤ)
    (α β : AlgebraicCycle X ℤ) : AlgebraicCycle X ℤ
```

**`AlgebraicGeometry.TorFormula.torFormulaSubvarietyProductTotal_eq_of_intersectProperly`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/CycleIntersectionProduct.lean#L647). The attribute's comment: “the summand Wᵢ · Vⱼ at a pair of components, by the Tor formula”.

> **Stacks 0B08: the value computed here is the product of the source.** For cycles `α` and `β`
> on a regular scheme over a field which intersect properly, with `dim X = m` and the dimensions of
> the components summing to `m + n`, every summand of `α · β` that contributes is the genuine
> alternating sum `∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_X}(𝒪_{Wᵢ}, 𝒪_{Vⱼ})]_n` of Section 43.14, the
> `intersectionProductCycle` of Tag 0AZR. So the double sum of `torFormulaCycleIntersectionProduct`
> is the `α · β` the source displays.

```lean
theorem torFormulaSubvarietyProductTotal_eq_of_intersectProperly (k : Type u) [Field k]
    {X : Scheme.{u}} (sX : X ⟶ (Stacks.Chow.fieldChowSituation k).S) [LocallyOfFiniteType sX]
    [IsLocallyNoetherian X] (hX : IsRegular X) {m n : ℕ} {α β : AlgebraicCycle X ℤ}
    (hαβ : AlgebraicCycle.IntersectProperly α β)
    (hdimX : topologicalKrullDim X = (m : WithBot ℕ∞))
    (hdim : ∀ x ∈ Function.support α, ∀ y ∈ Function.support β,
      topologicalKrullDim (closure ({x} : Set X)) +
        topologicalKrullDim (closure ({y} : Set X)) = (m : WithBot ℕ∞) + (n : WithBot ℕ∞))
    {q : X × X}
    (hq : q ∈ Function.support (cycleIntersectionProductSummand
      (torFormulaSubvarietyProductTotal (Stacks.Chow.fieldChowSituation k) sX hX (n : ℤ)) α β)) :
    torFormulaSubvarietyProductTotal (Stacks.Chow.fieldChowSituation k) sX hX (n : ℤ) q.1 q.2 =
      intersectionProductCycle (Stacks.Chow.fieldChowSituation k) sX hX
        (structureSheafAt q.1) (structureSheafAt q.2) (isCoherent_structureSheafAt q.1)
        (isCoherent_structureSheafAt q.2) (n : ℤ)
        (torSupportBound_of_mem_support_of_intersectProperly k sX hX hαβ hdimX hdim _ hq)
```

## Tag 0B07, a lemma

[Tag 0B07](https://stacks.math.columbia.edu/tag/0B07) in the Stacks Project.

**`Stacks.Chow.tag_0B07`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FibreCycleClosedPointPair.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FibreCycleClosedPointPair.lean#L99). The attribute's comment: “the whole tag, at an ARBITRARY pair of distinct closed points `a`, `b` of `P^1` over an algebraically closed field: (1)(a) `[W_a]_k = W · X × a` as cycles on `X × P^1`, (1)(b) `[W_a]_k = pr_{X,*}(W · X × a)` as cycles on `X`, (2) `pr_{X,*}(α · X × a - α · X × b)` is rationally equivalent to zero for every `(k + 1)`-cycle `α` meeting the two fibres properly, and (3) the converse, that every `k`-cycle rationally equivalent to zero is of that form. The hypotheses are the source's own and concern `X`, `a`, `b` and `W` (resp. `α`, `β`) alone: `X` is nonsingular (`hX`) and a variety over an algebraically closed field `Kf`, and `a`, `b` are distinct closed points of the projective line (`ha`, `hb`, `hab`); `k` is an arbitrary integer, the source's `k ≥ 0` being unnecessary. `X × a` is the image of the section of the family at `a`, which is `Stacks.Chow.closedPointSection`, built from Mathlib's `AlgebraicGeometry.pointOfClosedPoint`: over an algebraically closed field the residue field at a closed point of a scheme locally of finite type is the field itself, so a closed point of `P^1` is a rational point. The first clause of the conclusion records that the second projection of each of the two sections is constant at its point, so that `X × a` and `X × b` are the fibres of `X × P^1` over `a` and over `b`. That this section is `Stacks.Chow.pointSection` at a global function on the base, or `Stacks.Chow.infinitySection`, is `Stacks.Chow.exists_closedPointSection_eq_pointSection_or_eq_infinitySection`, proved from the chart dichotomy `Stacks.Chow.compl_range_affineChart` together with the classification of the `S`-points of the affine chart, `Stacks.Chow.eq_affineLineSection_of_comp_eq`. The products are the honest Section 43.14 products of Tag 0AZR and the Tag 0B08 products `AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct` assembled from them; `rationally equivalent to zero` is `Stacks.Chow.rationalEquivalences`, the group of Tag 02RW; `of that form` in (3) is `Stacks.Chow.PointCycle.IsSectionPairFibreIntersectionDifference`, which spells out the conclusion of (2) at the two sections. Proper intersection is the delta-dimension idiom of chapter 42 (`hWD`, for `dim (W ∩ X × a) ≤ k`) in (1) and the form Section 43.8 and Tag 02S4 part (2) use in (2) — no component of `α` is contained in the section. Nothing is assumed about the ambient `X × P^1`: its regularity is `Stacks.Chow.isRegular_projectiveLineProduct_of_eq`, derived from nonsingularity of `X`; the pointwise readings of (1)(a) are `Stacks.Chow.localConditions_ker_pointSection` and its infinity twin; the delta-dimension bounds on the supports of the Tor sheaves are `AlgebraicGeometry.TorFormula.schemeDeltaDimension_reducedSupport_torSheaf_le`; and the bound on the Krull dimension of the family that makes the alternating Tor sum finite is `Stacks.Chow.exists_topologicalKrullDim_projectiveLineProduct_le`. Tag 0B2U, the 2-transitivity of the automorphism group of `P^1`, is not invoked: each clause is proved at the pair of points themselves.”.

> **Stacks Project, Tag 0B07.** Let `X` be a nonsingular variety over an algebraically closed
> field, let `a ≠ b` be closed points of `ℙ¹` and let `k` be an integer. Writing `X × a` for the
> image of the section of `X ×_S ℙ¹_S ⟶ X` at `a`:
>
> 0. that section is constant at `a` — its second projection sends every point of `X` to `a` — so
>    `X × a` is the fibre of `X ×_S ℙ¹_S ⟶ ℙ¹_S` over `a`, and likewise at `b`;
> 1. if `W ⊆ X ×_S ℙ¹_S` is a closed subvariety of delta-dimension `k + 1` meeting `X × a`
>    properly, then (a) `[W_a]_k = W · (X × a)` as cycles on `X ×_S ℙ¹_S`, and (b)
>    `[W_a]_k = pr_{X,*}(W · X × a)` as cycles on `X`;
> 2. for every `(k + 1)`-cycle `α` on `X ×_S ℙ¹_S` meeting `X × a` and `X × b` properly,
>    `pr_{X,*}(α · X × a - α · X × b)` is rationally equivalent to zero;
> 3. conversely, every `k`-cycle rationally equivalent to zero is of that form.
>
> The intersection products are the Section 43.14 products of Tag 0AZR, read on cycles by the Tag
> 0B08 product; rational equivalence is `Stacks.Chow.rationalEquivalences`, the group of Tag 02RW;
> and "of that form" is `Stacks.Chow.PointCycle.IsSectionPairFibreIntersectionDifference`, which
> spells out the conclusion of (2). Nothing is assumed about the ambient family `X ×_S ℙ¹_S`.

```lean
theorem tag_0B07 (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] (Kf : Type u) [Field Kf] [IsAlgClosed Kf]
    (hC : C.S = AlgebraicGeometry.Spec (CommRingCat.of Kf))
    [AlgebraicGeometry.IsVariety Kf (p ≫ eqToHom hC)] (hX : IsRegular X) (k : ℤ)
    (a b : relativeProjectiveLine C.S) (ha : IsClosed {a}) (hb : IsClosed {b}) (hab : a ≠ b) :
    haveI : IsLocallyNoetherian (projectiveLineProduct p) :=
      LocallyOfFiniteType.isLocallyNoetherian
        (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
    ((∀ x : X, (closedPointSection Kf hC a ha p ≫
            pullback.snd p (relativeProjectiveLine C.S ↘ C.S)) x = a) ∧
        ∀ x : X, (closedPointSection Kf hC b hb p ≫
          pullback.snd p (relativeProjectiveLine C.S ↘ C.S)) x = b) ∧
      (∀ W : (projectiveLineProduct p).IdealSheafData, IsIntegral W.subscheme →
        (∀ ξ : genericPoints W.subscheme,
          relativeDimension C.dimensionFunction (familyBase p W) ξ.1 = k + 1) →
        ∀ hWD : schemeDeltaDimension C
            ((W ⊔ (closedPointSection Kf hC a ha p).ker).subschemeι ≫
              (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)) ≤ (k : EInt),
          (cycleAssociatedToClosedSubscheme C
              (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
              (W ⊔ (closedPointSection Kf hC a ha p).ker).subschemeι k).1 =
            intersectionProductCycle C (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
              (isRegular_projectiveLineProduct_of_eq p hC hX)
              (subschemeStructureSheaf W)
              (subschemeStructureSheaf (closedPointSection Kf hC a ha p).ker)
              (isCoherent_subschemeStructureSheaf W)
              (isCoherent_subschemeStructureSheaf (closedPointSection Kf hC a ha p).ker) k
              (schemeDeltaDimension_reducedSupport_torSheaf_le C
                (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
                (isRegular_projectiveLineProduct_of_eq p hC hX) W
                (closedPointSection Kf hC a ha p).ker k hWD) ∧
          properPushforward C (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p) p
              (pullback.fst p (relativeProjectiveLine C.S ↘ C.S)) rfl k
              ⟨intersectionProductCycle C
                  (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
                  (isRegular_projectiveLineProduct_of_eq p hC hX)
                  (subschemeStructureSheaf W)
                  (subschemeStructureSheaf (closedPointSection Kf hC a ha p).ker)
                  (isCoherent_subschemeStructureSheaf W)
                  (isCoherent_subschemeStructureSheaf (closedPointSection Kf hC a ha p).ker) k
                  (schemeDeltaDimension_reducedSupport_torSheaf_le C
                    (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
                    (isRegular_projectiveLineProduct_of_eq p hC hX) W
                    (closedPointSection Kf hC a ha p).ker k hWD),
                intersectionProductCycle_mem_cyclesOfDimension C
                  (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
                  (isRegular_projectiveLineProduct_of_eq p hC hX) W
                  (closedPointSection Kf hC a ha p).ker k hWD⟩ =
            cycleAssociatedToClosedSubscheme C p
              (W.comap (closedPointSection Kf hC a ha p)).subschemeι k) ∧
      (∀ α : CycleGroup C (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p) (k + 1),
          ∀ hT₁ : ∀ x ∈ Function.support α.1, ¬ Set.range (integralComponentAt x).subschemeι ⊆
            Set.range (closedPointSection Kf hC a ha p),
          ∀ hT₂ : ∀ x ∈ Function.support α.1, ¬ Set.range (integralComponentAt x).subschemeι ⊆
            Set.range (closedPointSection Kf hC b hb p),
            properPushforward C (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p) p
                (pullback.fst p (relativeProjectiveLine C.S ↘ C.S)) rfl k
                ⟨torFormulaCycleIntersectionProduct C
                    (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
                    (isRegular_projectiveLineProduct_of_eq p hC hX) k α.1
                    (@Function.locallyFinsuppWithin.single (projectiveLineProduct p) _ ℤ
                      (Classical.decEq _) _
                      ((closedPointSection Kf hC a ha p) (genericPoint X)) (1 : ℤ)),
                  torFormulaCycleIntersectionProduct_section_mem_cyclesOfDimension C p Kf hC
                    (isRegular_projectiveLineProduct_of_eq p hC hX) k
                    (exists_closedPointSection_eq_pointSection_or_eq_infinitySection Kf hC a ha p)
                    α hT₁⟩ -
              properPushforward C (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p) p
                (pullback.fst p (relativeProjectiveLine C.S ↘ C.S)) rfl k
                ⟨torFormulaCycleIntersectionProduct C
                    (pullback.fst p (relativeProjectiveLine C.S ↘ C.S) ≫ p)
                    (isRegular_projectiveLineProduct_of_eq p hC hX) k α.1
                    (@Function.locallyFinsuppWithin.single (projectiveLineProduct p) _ ℤ
                      (Classical.decEq _) _
                      ((closedPointSection Kf hC b hb p) (genericPoint X)) (1 : ℤ)),
                  torFormulaCycleIntersectionProduct_section_mem_cyclesOfDimension C p Kf hC
                    (isRegular_projectiveLineProduct_of_eq p hC hX) k
                    (exists_closedPointSection_eq_pointSection_or_eq_infinitySection Kf hC b hb p)
                    α hT₂⟩ ∈
            rationalEquivalences C p k) ∧
      (∀ β : CycleGroup C p k, β ∈ rationalEquivalences C p k →
        PointCycle.IsSectionPairFibreIntersectionDifference C p
          (isRegular_projectiveLineProduct_of_eq p hC hX) k
          (closedPointSection Kf hC a ha p) (closedPointSection Kf hC b hb p) β)
```

## Tag 0B1J, a lemma

[Tag 0B1J](https://stacks.math.columbia.edu/tag/0B1J) in the Stacks Project.

**`AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct_cycleAssociatedToClosedSubscheme_apply_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/TransversalSubschemeCycles.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormulaMultiplicities/TransversalSubschemeCycles.lean#L294).

> Let `X` be a nonsingular variety over a field `k` of dimension `d`, let `r, s ≥ 0` and let `Y`,
> `Z` be the closed subschemes cut out by `IY`, `IZ`, with `dim Y ≤ r` and `dim Z ≤ s`, whose cycles
> `[Y]_r = ∑ nᵢ [Yᵢ]` and `[Z]_s = ∑ mⱼ [Zⱼ]` intersect properly. Let `Y_{i₀}` and `Z_{j₀}` be
> components of the two cycles, with generic points `y₀` and `z₀`, and let `T` be the closure of a
> point `t` of `Y_{i₀} ∩ Z_{j₀}` (for instance the generic point of an irreducible component of it)
> along which the multiplicity of `Y ∩ Z`, `length_{𝒪_{X, t}} 𝒪_{X, t} ⧸ (𝓘_Y + 𝓘_Z)_t`, is `1`. Then
>
> 1. the coefficient of `T` in `[Y]_r · [Z]_s` is `1`,
> 2. `Y` and `Z` are nonsingular at `t`,
> 3. `n_{i₀} = 1` and `m_{j₀} = 1`, and
> 4. `T` is contained in no other component of `[Y]_r` and in no other component of `[Z]_s`.

```lean
theorem torFormulaCycleIntersectionProduct_cycleAssociatedToClosedSubscheme_apply_eq_one
    (k : Type u) [Field k] {X : Scheme.{u}} (sX : X ⟶ (fieldChowSituation k).S)
    [IsVariety k sX] (hX : IsRegular X) {d : ℕ} (hd : topologicalKrullDim X = d) (r s : ℕ)
    (IY IZ : X.IdealSheafData) (hY : topologicalKrullDim IY.subscheme ≤ r)
    (hZ : topologicalKrullDim IZ.subscheme ≤ s)
    (hprop : AlgebraicCycle.IntersectProperly
      (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
        IY.subschemeι r).1
      (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
        IZ.subschemeι s).1)
    {y₀ z₀ t : X}
    (hy₀ : (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
      IY.subschemeι r).1 y₀ ≠ 0)
    (hz₀ : (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
      IZ.subschemeι s).1 z₀ ≠ 0)
    (ht : t ∈ closure ({y₀} : Set X) ∩ closure ({z₀} : Set X))
    (hmult : Module.length (X.presheaf.stalk t)
      (X.presheaf.stalk t ⧸ IdealSheafData.stalk (IY ⊔ IZ) t) = 1) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    torFormulaCycleIntersectionProduct (fieldChowSituation k) sX hX ((r + s : ℤ) - d)
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
          IY.subschemeι r).1
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
          IZ.subschemeι s).1 t = 1 ∧
      (∀ ζ : IY.subscheme, IY.subschemeι ζ = t →
        IsRegularLocalRing (IY.subscheme.presheaf.stalk ζ)) ∧
      (∀ ζ : IZ.subscheme, IZ.subschemeι ζ = t →
        IsRegularLocalRing (IZ.subscheme.presheaf.stalk ζ)) ∧
      (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
        IY.subschemeι r).1 y₀ = 1 ∧
      (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
        IZ.subschemeι s).1 z₀ = 1 ∧
      (∀ y, (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
        IY.subschemeι r).1 y ≠ 0 → t ∈ closure ({y} : Set X) → y = y₀) ∧
      (∀ z, (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sX
        IZ.subschemeι s).1 z ≠ 0 → t ∈ closure ({z} : Set X) → z = z₀)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.17, Tag 0B08](https://stacks.math.columbia.edu/tag/0B08)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
