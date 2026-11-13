---
declaration: section
origin: cited
lean: Stacks.Intersection.RationalEquivalence.rationallyEquivalent_intersectionProduct_fibreCycle, Stacks.Intersection.RationalEquivalence.rationallyEquivalent_intersectionProduct_fibreCycle_dimension_r, AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct_mem_rationalEquivalences, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_intersectProperly_cycleComap_torFormulaCycleIntersectionProduct_eq, AlgebraicGeometry.exists_rationallyEquivalent_forall_intersectProperly_of_isQuasiProjectiveVariety, AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct_mem_rationalEquivalences_of_isQuasiProjectiveVariety, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_intersectProperly_cycleComap_regularLocus_eq
statement: formalized
proof: formalized
---

# 43.25 Intersection products and rational equivalence

Section 43.25 of the Stacks Project, [Tag 0B0F](https://stacks.math.columbia.edu/tag/0B0F). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B60, a lemma

[Tag 0B60](https://stacks.math.columbia.edu/tag/0B60) in the Stacks Project.

**`Stacks.Intersection.RationalEquivalence.rationallyEquivalent_intersectionProduct_fibreCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/RationalEquivalence/FibreSpecialCase.lean, line 1164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/RationalEquivalence/FibreSpecialCase.lean#L1164). The attribute's comment: “the whole lemma with the fibre cycles in their dimension `s`, as the proof and Tag 0B1V use it, at the source's own data: `X` a nonsingular variety over an algebraically closed field (the chapter's convention, Tag 0AZ8) of dimension `dX`, `W ⊆ X × P^1` an integral closed subscheme of dimension `s + 1` dominating `P^1`, `a`, `b` closed points of `P^1` with fibres `W_a`, `W_b` read in `X` as in Tag 0B07, and `V` the closure of a point of dimension `r` with `dim (V ∩ W_a)` and `dim (V ∩ W_b)` at most `r + s - dX`, the proper intersection of Tag 0AZQ written additively. The conclusion is that `[V] · [W_a]_s` and `[V] · [W_b]_s` are rationally equivalent (Tag 02RW), the products being those of Tag 0B08 in the integer expected dimension `r + s - dX`. The source prints `[W_a]_r`; the fibre has dimension `s`, and the statement as printed is `rationallyEquivalent_intersectionProduct_fibreCycle_dimension_r`.”.

> **Stacks Project, Tag 0B60.** Let `X` be a nonsingular variety over an algebraically closed
> field, of dimension `dX`. Let `W ⊆ X × ℙ¹` be a closed subvariety of dimension `s + 1` dominating
> `ℙ¹`, let `a`, `b` be closed points of `ℙ¹` and let `W_a`, `W_b` be the fibres of `W` over them,
> viewed as closed subschemes of `X`. Let `V ⊆ X` be the closure of a point `v`, of dimension `r`,
> meeting `W_a` and `W_b` properly. Then `[V] · [W_a]_s ∼_rat [V] · [W_b]_s`.

```lean
theorem rationallyEquivalent_intersectionProduct_fibreCycle [DecidableEq X] (hX : IsRegular X)
    (dX r s : ℕ) (hdX : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (W : (projectiveLineProduct f).IdealSheafData) [IsIntegral W.subscheme]
    (hW : topologicalKrullDim (W.support : Set (projectiveLineProduct f)) =
      ((s + 1 : ℕ) : WithBot ℕ∞))
    [IsDominant (W.subschemeι ≫
      pullback.snd f (relativeProjectiveLine (Spec (.of k)) ↘ Spec (.of k)))]
    (a b : relativeProjectiveLine (Spec (.of k))) (ha : IsClosed {a}) (hb : IsClosed {b})
    (v : X) (hv : topologicalKrullDim (closure ({v} : Set X)) = (r : WithBot ℕ∞))
    (hVa : topologicalKrullDim (↥(closure ({v} : Set X) ∩
        Set.range (W.comap (closedPointSection k rfl a ha f)).subschemeι)) +
        (dX : WithBot ℕ∞) ≤ ((r + s : ℕ) : WithBot ℕ∞))
    (hVb : topologicalKrullDim (↥(closure ({v} : Set X) ∩
        Set.range (W.comap (closedPointSection k rfl b hb f)).subschemeι)) +
        (dX : WithBot ℕ∞) ≤ ((r + s : ℕ) : WithBot ℕ∞)) :
    letI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    RationallyEquivalent (fieldChowSituation k) f ((r : ℤ) + s - dX)
      ⟨torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX ((r : ℤ) + s - dX)
          (Function.locallyFinsuppWithin.single v 1)
          (cycleAssociatedToClosedSubscheme (fieldChowSituation k) f
            (W.comap (closedPointSection k rfl a ha f)).subschemeι s).1,
        torFormulaCycleIntersectionProduct_mem_cyclesOfDimension
          (fieldChowSituation k) f hX _ _ _⟩
      ⟨torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX ((r : ℤ) + s - dX)
          (Function.locallyFinsuppWithin.single v 1)
          (cycleAssociatedToClosedSubscheme (fieldChowSituation k) f
            (W.comap (closedPointSection k rfl b hb f)).subschemeι s).1,
        torFormulaCycleIntersectionProduct_mem_cyclesOfDimension
          (fieldChowSituation k) f hX _ _ _⟩
```

**`Stacks.Intersection.RationalEquivalence.rationallyEquivalent_intersectionProduct_fibreCycle_dimension_r`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/RationalEquivalence/FibreSpecialCase.lean, line 1330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/RationalEquivalence/FibreSpecialCase.lean#L1330). The attribute's comment: “as printed, with `[W_a]_r` and `[W_b]_r`, the fibre cycles in the dimension `r` of `V`, the products being those of Tag 0B08 in the integer expected dimension `r + r - dX`; the data are those of `rationallyEquivalent_intersectionProduct_fibreCycle`, the fibres being pure of dimension `s` by Tag 02RK.”.

> **Stacks Project, Tag 0B60, as printed.** The statement with the fibre cycles `[W_a]_r` and
> `[W_b]_r` in the dimension `r` of `V`, as the source writes it. The fibres are pure of dimension
> `s` (Tag 02RK), so for `r ≠ s` both cycles vanish, and for `r = s` this is
> `Stacks.Intersection.RationalEquivalence.rationallyEquivalent_intersectionProduct_fibreCycle`.

```lean
theorem rationallyEquivalent_intersectionProduct_fibreCycle_dimension_r [DecidableEq X]
    (hX : IsRegular X)
    (dX r s : ℕ) (hdX : topologicalKrullDim X = (dX : WithBot ℕ∞))
    (W : (projectiveLineProduct f).IdealSheafData) [IsIntegral W.subscheme]
    (hW : topologicalKrullDim (W.support : Set (projectiveLineProduct f)) =
      ((s + 1 : ℕ) : WithBot ℕ∞))
    [IsDominant (W.subschemeι ≫
      pullback.snd f (relativeProjectiveLine (Spec (.of k)) ↘ Spec (.of k)))]
    (a b : relativeProjectiveLine (Spec (.of k))) (ha : IsClosed {a}) (hb : IsClosed {b})
    (v : X) (hv : topologicalKrullDim (closure ({v} : Set X)) = (r : WithBot ℕ∞))
    (hVa : topologicalKrullDim (↥(closure ({v} : Set X) ∩
        Set.range (W.comap (closedPointSection k rfl a ha f)).subschemeι)) +
        (dX : WithBot ℕ∞) ≤ ((r + s : ℕ) : WithBot ℕ∞))
    (hVb : topologicalKrullDim (↥(closure ({v} : Set X) ∩
        Set.range (W.comap (closedPointSection k rfl b hb f)).subschemeι)) +
        (dX : WithBot ℕ∞) ≤ ((r + s : ℕ) : WithBot ℕ∞)) :
    letI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    RationallyEquivalent (fieldChowSituation k) f ((r : ℤ) + r - dX)
      ⟨torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX ((r : ℤ) + r - dX)
          (Function.locallyFinsuppWithin.single v 1)
          (cycleAssociatedToClosedSubscheme (fieldChowSituation k) f
            (W.comap (closedPointSection k rfl a ha f)).subschemeι r).1,
        torFormulaCycleIntersectionProduct_mem_cyclesOfDimension
          (fieldChowSituation k) f hX _ _ _⟩
      ⟨torFormulaCycleIntersectionProduct (fieldChowSituation k) f hX ((r : ℤ) + r - dX)
          (Function.locallyFinsuppWithin.single v 1)
          (cycleAssociatedToClosedSubscheme (fieldChowSituation k) f
            (W.comap (closedPointSection k rfl b hb f)).subschemeι r).1,
        torFormulaCycleIntersectionProduct_mem_cyclesOfDimension
          (fieldChowSituation k) f hX _ _ _⟩
```

## Tag 0B1V, a theorem

[Tag 0B1V](https://stacks.math.columbia.edu/tag/0B1V) in the Stacks Project.

**`AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct_mem_rationalEquivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/RationalEquivalenceProduct.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/RationalEquivalenceProduct.lean#L160). The attribute's comment: “the whole theorem, for a nonsingular projective variety `X` of dimension `n` over an algebraically closed field: for an `r`-cycle `α` and an `s`-cycle `β` meeting properly (Tag 0AZQ) with `α` rationally equivalent to zero, the Tag 0B08 product `α · β` is a rationally trivial `(r + s - n)`-cycle”.

> **Stacks Project, Tag 0B1V.** Let `X` be a nonsingular projective variety of dimension `n` over
> an algebraically closed field `k`. Let `α` be an `r`-cycle and `β` an `s`-cycle on `X` which
> intersect properly, so that `α · β` is defined, and assume `α ∼_rat 0`. Then `α · β ∼_rat 0`.
>
> The product is the intersection product of Tag 0B08, an `(r + s - n)`-cycle.

```lean
theorem torFormulaCycleIntersectionProduct_mem_rationalEquivalences (k : Type u) [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [IsProjectiveVariety k p]
    (hX : IsRegular X) {n : ℕ} (hn : topologicalKrullDim X = (n : WithBot ℕ∞)) {r s : ℤ}
    (α : CycleGroup (fieldChowSituation k) p r) (β : CycleGroup (fieldChowSituation k) p s)
    (hαβ : AlgebraicCycle.IntersectProperly α.1 β.1)
    (hα : α ∈ rationalEquivalences (fieldChowSituation k) p r) :
    haveI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    (⟨torFormulaCycleIntersectionProduct (fieldChowSituation k) p hX (r + s - n) α.1 β.1,
        torFormulaCycleIntersectionProduct_mem_cyclesOfDimension (fieldChowSituation k) p hX
          (r + s - n) α.1 β.1⟩ :
      CycleGroup (fieldChowSituation k) p (r + s - n)) ∈
      rationalEquivalences (fieldChowSituation k) p (r + s - n)
```

## Tag 0B61, a remark

[Tag 0B61](https://stacks.math.columbia.edu/tag/0B61) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_intersectProperly_cycleComap_torFormulaCycleIntersectionProduct_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/KeyLemma.lean, line 774](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/KeyLemma.lean#L774). The attribute's comment: “the variant of the moving lemma 0B0E stated there, for an arbitrary open subscheme U ⟶ X of the nonsingular locus of a closed subvariety X ⊆ 𝐏(V) (the source's U = X^reg), with the dimensions of the T\_i allowed to vary; (C · X)|\_U is the coefficientwise inverse image of the cycle C · X along U ⟶ X ⟶ 𝐏(V); the non-strict dimension clause is the disjunction dim (Z\_j ∩ T\_i) ≤ dim (Z ∩ T\_i) or dim (Z\_j ∩ T\_i) + n ≤ d + d', as for 0B0E, because the source's inequality fails when Z ∩ T\_i is empty”.

> **Stacks Project, Remark 0B61: the moving lemma on an open subset of the nonsingular locus.**
> Let `X ⊆ 𝐏(V)` be a closed subvariety of dimension `n` of the projective space of a vector space
> of dimension `N + 1` over an algebraically closed field, let `U ⊆ X` be an open subscheme
> contained in the nonsingular locus `X^{reg}`, given as an open immersion `j₀ : U ⟶ X` (written
> `Y ⟶ X` below), let `Z ⊆ U` be a closed subvariety of dimension `d < n`, and
> let `T_i ⊆ U` be finitely many closed subvarieties, `T_i` of dimension `d' i < n`. Then there is
> a closed subvariety `C ⊆ 𝐏(V)` whose prime cycle intersects that of `X` properly, with
>
> `(C · X)|_U = [Z] + ∑ m_j [Z_j]`
>
> in the Tor-formula intersection product of Section 0B08, where `C · X` is supported on `C ∩ X`,
> the `Z_j ⊆ U` are irreducible closed of dimension `d`, distinct from `Z`, with nonzero
> multiplicities, and where, inside `U`,
>
> * `dim (Z_j ∩ T_i) ≤ dim (Z ∩ T_i)` or `dim (Z_j ∩ T_i) + n ≤ d + d' i`, and
> * `dim (Z_j ∩ T_i) < dim (Z ∩ T_i)` whenever `Z` does not intersect `T_i` properly in `U`.
>
> The restriction of `C · X` to `U` is its coefficientwise inverse image `Stacks.Chow.cycleComap`
> along `U ⟶ X ⟶ 𝐏(V)`. `U = X^{reg}` is the statement of Remark 0B61, `U` a quasi-projective
> variety embedded in a closed subvariety `X` of `𝐏(V)` is the form the remark's 0B1U and 0B1V use,
> and `j₀ = 𝟙 X` for a nonsingular `X` is Lemma 0B0E; the dimensions `d' i` may vary with `i`, the
> source's single `d'` being the constant family.
>
> **The first clause departs from the source's text, because the source's clause is false.** The
> source asks for `dim (Z_j ∩ T_i) ≤ dim (Z ∩ T_i)` outright. When `Z ∩ T_i = ∅` this demands
> `Z_j ∩ T_i = ∅` for every `j`, and that fails already for the projective Lemma 0B0E, where
> `U = X = X^{reg}`. Take `X ⊆ 𝐏^3` a nonsingular quadric surface (`n = 2`) and `Z`, `T_1` two
> distinct lines of one ruling (`d = d' = 1`), so that `Z ∩ T_1 = ∅`. A `C` as in the conclusion
> must be a surface: if `dim C ≤ 1` then `C ∩ X` is finite and `Z` does not occur in `C · X`, and
> if `C = 𝐏^3` then `C · X` has no component of dimension `1`. A surface `C` meets the line `T_1`,
> and every component of `C ∩ X` through such a point has dimension exactly `1`, so it occurs in
> `C · X` with a positive multiplicity and meets `T_1`; it is neither `Z` nor any admissible
> `Z_j`. The argument is written out in full in the implementation notes of this module. The
> disjunction is what condition (4) of the source's proof gives, and its first disjunct is the
> source's inequality whenever `Z ∩ T_i` is nonempty, by Tag 0AZP; in the empty case the second
> disjunct `dim (Z_j ∩ T_i) + n ≤ d + d' i` is what holds. The second clause is as the source has
> it, and is vacuous exactly in the empty case. The statement on `X^{reg}` itself, with the source's
> inequality whenever `Z ∩ T_i` is nonempty and proper intersection when it is empty, is
> `exists_intersectProperly_cycleComap_regularLocus_eq`; the erratum is recorded in `errata.md`.

```lean
public theorem exists_intersectProperly_cycleComap_torFormulaCycleIntersectionProduct_eq
    (k V : Type u) [Field k] [IsAlgClosed k] [AddCommGroup V] [Module k V]
    [FiniteDimensional k V] [Nontrivial V] [DecidableEq (projectiveSpaceOfModule k V)]
    {N n d : ℕ} (hV : Module.finrank k V = N + 1)
    {X : Scheme.{u}} (iX : X ⟶ projectiveSpaceOfModule k V) [IsClosedImmersion iX]
    [IsVariety k (iX ≫ projectiveSpaceOfModuleToSpec k V)]
    (hdimX : topologicalKrullDim X = (n : WithBot ℕ∞)) (hd : d < n)
    {Y : Scheme.{u}} (j₀ : Y ⟶ X) [IsOpenImmersion j₀] (hU : Set.range j₀.base ⊆ regularLocus X)
    [DecidableEq Y]
    (Z : IrreducibleCloseds Y)
    (hZd : topologicalKrullDim (Z : Set Y) = (d : WithBot ℕ∞))
    {ι : Type*} [Finite ι] (T : ι → IrreducibleCloseds Y) {d' : ι → ℕ}
    (hd' : ∀ i, d' i < n)
    (hTd : ∀ i, topologicalKrullDim (T i : Set Y) = (d' i : WithBot ℕ∞))
    (XC : IrreducibleCloseds (projectiveSpaceOfModule k V))
    (hXC : (XC : Set (projectiveSpaceOfModule k V)) = Set.range iX.base) :
    ∃ (C : IrreducibleCloseds (projectiveSpaceOfModule k V))
      (S : Finset (IrreducibleCloseds Y)) (m : IrreducibleCloseds Y → ℤ),
      AlgebraicCycle.IntersectProperly
          (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
          (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)) ∧
        cycleComap j₀ j₀.isOpenEmbedding.injective
            (cycleComap iX iX.isClosedEmbedding.injective
              (TorFormula.torFormulaCycleIntersectionProduct (fieldChowSituation k)
                (projectiveSpaceOfModuleToSpec k V) (isRegular_projectiveSpaceOfModule k V)
                (d : ℤ)
                (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
                (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)))) =
          Function.locallyFinsuppWithin.single Z.isIrreducible.genericPoint (1 : ℤ) +
            ∑ W ∈ S, m W • Function.locallyFinsuppWithin.single
              W.isIrreducible.genericPoint (1 : ℤ) ∧
        (∀ p : projectiveSpaceOfModule k V,
          TorFormula.torFormulaCycleIntersectionProduct (fieldChowSituation k)
              (projectiveSpaceOfModuleToSpec k V) (isRegular_projectiveSpaceOfModule k V) (d : ℤ)
              (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
              (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)) p ≠
              0 →
            p ∈ (C : Set (projectiveSpaceOfModule k V)) ∩
              (XC : Set (projectiveSpaceOfModule k V))) ∧
        Z ∉ S ∧ (∀ W ∈ S, m W ≠ 0) ∧
        (∀ W ∈ S, topologicalKrullDim (W : Set Y) = (d : WithBot ℕ∞)) ∧
        (∀ W ∈ S, ∀ i,
          topologicalKrullDim ↥((W : Set Y) ∩ (T i : Set Y)) ≤
              topologicalKrullDim ↥((Z : Set Y) ∩ (T i : Set Y)) ∨
            topologicalKrullDim ↥((W : Set Y) ∩ (T i : Set Y)) +
                (n : WithBot ℕ∞) ≤ (d : WithBot ℕ∞) + (d' i : WithBot ℕ∞)) ∧
        (∀ W ∈ S, ∀ i, ¬ AlgebraicGeometry.IntersectProperly Z (T i) →
          topologicalKrullDim ↥((W : Set Y) ∩ (T i : Set Y)) <
            topologicalKrullDim ↥((Z : Set Y) ∩ (T i : Set Y)))
```

**`AlgebraicGeometry.exists_rationallyEquivalent_forall_intersectProperly_of_isQuasiProjectiveVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/MovingCycles.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/MovingCycles.lean#L64). The attribute's comment: “Lemma 0B1U for a nonsingular quasi-projective variety, which the remark asserts with the same proof; for a finite family of cycles `β i` of arbitrary dimensions `s i` in place of a single `s`-cycle, and with `r` and the `s i` arbitrary integers. Nonsingular is `IsRegular X`, quasi-projective variety is `IsQuasiProjectiveVariety`, cycles are the graded cycle groups `Stacks.Chow.CycleGroup` over `Spec k`, rational equivalence is Tag 02RW and proper intersection is Definition 0AZQ. The moving lemma is run on `X` as an open subset of the nonsingular locus of its closure in projective space, which is the version of Tag 0B0E the remark describes”.

> **Remark 0B61: the moving lemma for a nonsingular quasi-projective variety, for a finite
> family of cycles.** Let `X` be a nonsingular quasi-projective variety over an algebraically closed
> field, let `α` be an `r`-cycle on `X` and let `β i` be finitely many cycles on `X`, of dimensions
> `s i`. Then there is an `r`-cycle `α'` with `α' ∼_rat α` which intersects every `β i` properly.
>
> `X` is an open subscheme of a closed subvariety `X̄ ⊆ 𝐏(k^{N+1})`
> (`exists_isOpenImmersion_projectiveSpaceOfModule_of_isQuasiProjectiveVariety`), contained in the
> nonsingular locus of `X̄` because `X` is nonsingular, and the moving lemma on such an open subset
> is `isMovableOff_of_isOpenImmersion`.

```lean
public theorem exists_rationallyEquivalent_forall_intersectProperly_of_isQuasiProjectiveVariety
    (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k))
    [IsQuasiProjectiveVariety k sX] (hX : IsRegular X) {r : ℤ}
    (α : CycleGroup (fieldChowSituation k) sX r)
    {ι : Type*} [Finite ι] (s : ι → ℤ) (β : ∀ i, CycleGroup (fieldChowSituation k) sX (s i)) :
    ∃ α' : CycleGroup (fieldChowSituation k) sX r,
      RationallyEquivalent (fieldChowSituation k) sX r α' α ∧
        ∀ i, AlgebraicCycle.IntersectProperly α'.1 (β i).1
```

**`AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct_mem_rationalEquivalences_of_isQuasiProjectiveVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/RationalEquivalenceProduct.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/RationalEquivalenceProduct.lean#L196). The attribute's comment: “Theorem 0B1V for a nonsingular quasi-projective variety `X` of dimension `n` over an algebraically closed field, which the remark asserts with the same proof: for an `r`-cycle `α` and an `s`-cycle `β` meeting properly (Tag 0AZQ) with `α` rationally equivalent to zero, the Tag 0B08 product `α · β` is a rationally trivial `(r + s - n)`-cycle. Quasi-projective variety is `IsQuasiProjectiveVariety`; the argument is run on `X` as an open subset of the nonsingular locus of its closure in projective space, the version of Tag 0B0E the remark describes”.

> **Stacks Project, Tag 0B61 for Theorem 0B1V.** Let `X` be a nonsingular quasi-projective
> variety of dimension `n` over an algebraically closed field `k`. Let `α` be an `r`-cycle and `β`
> an `s`-cycle on `X` which intersect properly, and assume `α ∼_rat 0`. Then `α · β ∼_rat 0`.
>
> `X` is an open subscheme of a closed subvariety `X̄ ⊆ 𝐏^N` of the same dimension, inside the
> nonsingular locus of `X̄`, and the proof of Tag 0B1V runs on such an open subscheme.

```lean
theorem torFormulaCycleIntersectionProduct_mem_rationalEquivalences_of_isQuasiProjectiveVariety
    (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}} (p : X ⟶ Spec (.of k))
    [IsQuasiProjectiveVariety k p] (hX : IsRegular X) {n : ℕ}
    (hn : topologicalKrullDim X = (n : WithBot ℕ∞)) {r s : ℤ}
    (α : CycleGroup (fieldChowSituation k) p r) (β : CycleGroup (fieldChowSituation k) p s)
    (hαβ : AlgebraicCycle.IntersectProperly α.1 β.1)
    (hα : α ∈ rationalEquivalences (fieldChowSituation k) p r) :
    haveI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    (⟨torFormulaCycleIntersectionProduct (fieldChowSituation k) p hX (r + s - n) α.1 β.1,
        torFormulaCycleIntersectionProduct_mem_cyclesOfDimension (fieldChowSituation k) p hX
          (r + s - n) α.1 β.1⟩ :
      CycleGroup (fieldChowSituation k) p (r + s - n)) ∈
      rationalEquivalences (fieldChowSituation k) p (r + s - n)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_intersectProperly_cycleComap_regularLocus_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/RegularLocusMoving.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/MovingLemma/RegularLocusMoving.lean#L186). The attribute's comment: “the version of the moving lemma 0B0E that the remark states, on the open subscheme X^reg of nonsingular points of a closed subvariety X ⊆ 𝐏(V) (an open of X whose underlying set is the regular locus, which exists by exists\_opens\_coe\_eq\_regularLocus); (C · X)|\_\{X^reg} is the coefficientwise inverse image of the cycle C · X along X^reg ⟶ X ⟶ 𝐏(V). The inequality dim (Z\_j ∩ T\_i) ≤ dim (Z ∩ T\_i) is proved whenever Z ∩ T\_i is nonempty, and when Z ∩ T\_i is empty Z\_j is proved to meet T\_i properly: the unguarded inequality is false there (dim ∅ = -∞ would force Z\_j ∩ T\_i = ∅, refuted by two lines of one ruling on a nonsingular quadric surface in 𝐏^3, recorded in errata.md). The strict clause is as the source has it. Together with the quasi-projective Lemma 0B1U and Theorem 0B1V registered under this tag, this is the whole remark”.

> **Stacks Project, Remark 0B61: the moving lemma on the nonsingular locus.** Let `X ⊆ 𝐏(V)` be
> a closed subvariety of dimension `n` of the projective space of a vector space of dimension
> `N + 1` over an algebraically closed field, and let `X^{reg} ⊆ X` be the open subset of nonsingular
> points (`Xreg`, an open subscheme of `X` whose underlying set is the regular locus; it exists by
> `exists_opens_coe_eq_regularLocus`). Let `0 ≤ d, d' < n`, let `Z ⊆ X^{reg}` be a closed subvariety
> of dimension `d` and let `T_i ⊆ X^{reg}`, `i ∈ ι`, be finitely many closed subvarieties of
> dimension `d'`. Then there is a closed subvariety `C ⊆ 𝐏(V)` whose prime cycle intersects that of
> `X` properly, with
>
> `(C · X)|_{X^{reg}} = [Z] + ∑ m_j [Z_j]`
>
> in the Tor-formula intersection product of Section 0B08 (restriction to `X^{reg}` being the
> coefficientwise inverse image `Stacks.Chow.cycleComap` along `X^{reg} ⟶ X ⟶ 𝐏(V)`, and `C · X`
> being supported on `C ∩ X`), where the `Z_j ⊆ X^{reg}` are irreducible closed of dimension `d`,
> distinct from `Z`, with nonzero multiplicities, and, inside `X^{reg}`,
>
> * `dim (Z_j ∩ T_i) ≤ dim (Z ∩ T_i)` whenever `Z ∩ T_i` is nonempty;
> * `Z_j` intersects `T_i` properly, `dim (Z_j ∩ T_i) + n ≤ d + d'`, whenever `Z ∩ T_i` is empty;
> * `dim (Z_j ∩ T_i) < dim (Z ∩ T_i)` whenever `Z` does not intersect `T_i` properly.
>
> The source states the first clause without the nonemptiness guard. With `dim ∅ = -∞` (Tag 0055)
> that would force `Z_j ∩ T_i = ∅` whenever `Z ∩ T_i = ∅`, and this is false: for `X ⊆ 𝐏^3` a
> nonsingular quadric surface (so `X^{reg} = X`) and `Z`, `T_1` two distinct lines of one ruling,
> every surface `C` meets `T_1` and some component of `C ∩ X` other than `Z` through such a point
> occurs in `C · X`; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Intersection.MovingLemma.KeyLemma` and `errata.md`. In that empty
> case the second clause is what holds. The strict clause is vacuous exactly when `Z ∩ T_i` is
> empty.
>
> The proof is `exists_intersectProperly_cycleComap_torFormulaCycleIntersectionProduct_eq` on the
> open subscheme `X^{reg}`, whose first clause `dim (Z\_j ∩ T\_i) ≤ dim (Z ∩ T\_i) ∨
> dim (Z\_j ∩ T\_i) + n ≤ d + d'` gives the two guarded clauses: the second disjunct gives the first
> clause by Tag 0AZP on the nonsingular variety `X^{reg}`, which bounds `d + d' ≤ n + dim (Z ∩ T_i)`
> when `Z ∩ T_i` is nonempty, and the first disjunct gives the second clause when `Z ∩ T_i` is
> empty, since then `Z_j ∩ T_i` is empty too.

```lean
public theorem exists_intersectProperly_cycleComap_regularLocus_eq
    (k V : Type u) [Field k] [IsAlgClosed k] [AddCommGroup V] [Module k V]
    [FiniteDimensional k V] [Nontrivial V] [DecidableEq (projectiveSpaceOfModule k V)]
    {N n d d' : ℕ} (hV : Module.finrank k V = N + 1)
    {X : Scheme.{u}} (iX : X ⟶ projectiveSpaceOfModule k V) [IsClosedImmersion iX]
    [IsVariety k (iX ≫ projectiveSpaceOfModuleToSpec k V)]
    (hdimX : topologicalKrullDim X = (n : WithBot ℕ∞)) (hd : d < n) (hd' : d' < n)
    (Xreg : X.Opens) (hXreg : (Xreg : Set X) = regularLocus X) [DecidableEq Xreg.toScheme]
    (Z : IrreducibleCloseds Xreg.toScheme)
    (hZd : topologicalKrullDim (Z : Set Xreg.toScheme) = (d : WithBot ℕ∞))
    {ι : Type*} [Finite ι] (T : ι → IrreducibleCloseds Xreg.toScheme)
    (hTd : ∀ i, topologicalKrullDim (T i : Set Xreg.toScheme) = (d' : WithBot ℕ∞))
    (XC : IrreducibleCloseds (projectiveSpaceOfModule k V))
    (hXC : (XC : Set (projectiveSpaceOfModule k V)) = Set.range iX.base) :
    ∃ (C : IrreducibleCloseds (projectiveSpaceOfModule k V))
      (S : Finset (IrreducibleCloseds Xreg.toScheme)) (m : IrreducibleCloseds Xreg.toScheme → ℤ),
      AlgebraicCycle.IntersectProperly
          (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
          (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)) ∧
        cycleComap Xreg.ι Xreg.ι.isOpenEmbedding.injective
            (cycleComap iX iX.isClosedEmbedding.injective
              (TorFormula.torFormulaCycleIntersectionProduct (fieldChowSituation k)
                (projectiveSpaceOfModuleToSpec k V) (isRegular_projectiveSpaceOfModule k V)
                (d : ℤ)
                (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
                (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)))) =
          Function.locallyFinsuppWithin.single Z.isIrreducible.genericPoint (1 : ℤ) +
            ∑ W ∈ S, m W • Function.locallyFinsuppWithin.single
              W.isIrreducible.genericPoint (1 : ℤ) ∧
        (∀ p : projectiveSpaceOfModule k V,
          TorFormula.torFormulaCycleIntersectionProduct (fieldChowSituation k)
              (projectiveSpaceOfModuleToSpec k V) (isRegular_projectiveSpaceOfModule k V) (d : ℤ)
              (Function.locallyFinsuppWithin.single C.isIrreducible.genericPoint (1 : ℤ))
              (Function.locallyFinsuppWithin.single XC.isIrreducible.genericPoint (1 : ℤ)) p ≠
              0 →
            p ∈ (C : Set (projectiveSpaceOfModule k V)) ∩
              (XC : Set (projectiveSpaceOfModule k V))) ∧
        Z ∉ S ∧ (∀ W ∈ S, m W ≠ 0) ∧
        (∀ W ∈ S, topologicalKrullDim (W : Set Xreg.toScheme) = (d : WithBot ℕ∞)) ∧
        (∀ W ∈ S, ∀ i, ((Z : Set Xreg.toScheme) ∩ (T i : Set Xreg.toScheme)).Nonempty →
          topologicalKrullDim ↥((W : Set Xreg.toScheme) ∩ (T i : Set Xreg.toScheme)) ≤
            topologicalKrullDim ↥((Z : Set Xreg.toScheme) ∩ (T i : Set Xreg.toScheme))) ∧
        (∀ W ∈ S, ∀ i, (Z : Set Xreg.toScheme) ∩ (T i : Set Xreg.toScheme) = ∅ →
          topologicalKrullDim ↥((W : Set Xreg.toScheme) ∩ (T i : Set Xreg.toScheme)) +
              (n : WithBot ℕ∞) ≤ (d : WithBot ℕ∞) + (d' : WithBot ℕ∞)) ∧
        (∀ W ∈ S, ∀ i, ¬ AlgebraicGeometry.IntersectProperly Z (T i) →
          topologicalKrullDim ↥((W : Set Xreg.toScheme) ∩ (T i : Set Xreg.toScheme)) <
            topologicalKrullDim ↥((Z : Set Xreg.toScheme) ∩ (T i : Set Xreg.toScheme)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.25, Tag 0B0F](https://stacks.math.columbia.edu/tag/0B0F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
