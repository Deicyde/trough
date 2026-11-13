---
declaration: section
origin: cited
lean: Stacks.Intersection.CycleFlatPullback.flatPullback_coherentSheafCycleProduct_integerDimension, Stacks.Intersection.CycleFlatPullback.intersectProperly_flatPullback, Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq_integerDimension, Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq
statement: formalized
proof: formalized
---

# 43.21 Flat pullback and intersection products

Section 43.21 of the Stacks Project, [Tag 0B0B](https://stacks.math.columbia.edu/tag/0B0B). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B0Y, a lemma

[Tag 0B0Y](https://stacks.math.columbia.edu/tag/0B0Y) in the Stacks Project.

**`Stacks.Intersection.CycleFlatPullback.flatPullback_coherentSheafCycleProduct_integerDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean#L240). The attribute's comment: “the whole lemma, in every case of the integer expected dimension `r + s - dim Y`, the case `r + s < dim Y` included: both that `[f^*ℱ]_{r+e}` and `[f^*𝒢]_{s+e}` intersect properly and the identity `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`, for a flat morphism of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — under the source's own three dimension bounds on `Supp ℱ`, `Supp 𝒢` and their intersection. `WithBot ℕ∞` has no subtraction, so `dim(Supp ℱ ∩ Supp 𝒢) ≤ r + s - dim Y` is spelled `dim(Supp ℱ ∩ Supp 𝒢) + dim Y ≤ r + s`, as proper intersection is in Tag 0AZQ, and the products are taken in the integer dimensions `(r : ℤ) + s - dim Y` and `(r : ℤ) + s - dim Y + e`. Both products are the Section 43.17 product of cycles `AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct` (Tag 0B08). The proof is the source's: Tag 0B0W downstairs and upstairs, Tag 0AZF on each Tor summand, and the comparison `f^*Torᵢ(ℱ, 𝒢) ≅ Torᵢ(f^*ℱ, f^*𝒢)` from Tag 079U and the exactness of `f^*`, which is `AlgebraicGeometry.TorFormula.pullbackTorSheafIso`, proved in this library, so the statement carries no hypothesis beyond the source's.”.

> **Stacks Project, Tag 0B0Y**, with the expected dimension an integer. Let `f : X ⟶ Y` be a
> flat morphism of nonsingular varieties over an algebraically closed field `K` — the chapter's
> convention, Tag 0AZ8 — and set `e = dim X - dim Y`. Let `ℱ` and `𝒢` be coherent sheaves on `Y`
> with `dim Supp ℱ ≤ r`, `dim Supp 𝒢 ≤ s` and `dim(Supp ℱ ∩ Supp 𝒢) ≤ r + s - dim Y`. Then the
> cycles `[f^*ℱ]_{r+e}` and `[f^*𝒢]_{s+e}` intersect properly and
>
> `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`.
>
> The products are taken in the integer dimensions `r + s - dim Y` downstairs and
> `r + s - dim Y + e` upstairs, every value included, the negative ones too. `WithBot ℕ∞` has no
> subtraction, so the third bound is written `dim(Supp ℱ ∩ Supp 𝒢) + dim Y ≤ r + s`; when
> `r + s < dim Y` it says that the supports are disjoint, and both sides are then `0`
> (`flatPullback_coherentSheafCycleProduct_eq_zero_of_add_lt`).

```lean
theorem flatPullback_coherentSheafCycleProduct_integerDimension (K : Type u) [Field K]
    [IsAlgClosed K] {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K))
    [IsVariety K sX] [IsVariety K sY] (hX : AlgebraicGeometry.IsRegular X)
    (hY : AlgebraicGeometry.IsRegular Y) (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX)
    (F G : Y.Modules) (hFc : _root_.SheafOfModules.IsCoherent F)
    (hGc : _root_.SheafOfModules.IsCoherent G) (r s dY e : ℕ)
    (hdY : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (hFr : topologicalKrullDim (SheafOfModules.supp F : Set Y) ≤ (r : WithBot ℕ∞))
    (hGs : topologicalKrullDim (SheafOfModules.supp G : Set Y) ≤ (s : WithBot ℕ∞))
    (hFG : topologicalKrullDim (SheafOfModules.supp F ∩ SheafOfModules.supp G : Set Y) +
      (dY : WithBot ℕ∞) ≤ (r : WithBot ℕ∞) + (s : WithBot ℕ∞)) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    letI : IsLocallyNoetherian Y := isLocallyNoetherian_of_isRegular hY
    letI : IsLocallyNoetherian X := isLocallyNoetherian_of_isRegular hX
    letI := hFc
    letI := hGc
    letI := isFiniteType_of_isCoherent F
    letI := isFiniteType_of_isCoherent G
    letI := AlgebraicGeometry.isCoherent_pullback f F
    letI := AlgebraicGeometry.isCoherent_pullback f G
    have hFrY := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le K sY F r hFr
    have hGsY := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le K sY G s hGs
    have hFrX := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le K sX
      ((Scheme.Modules.pullback f).obj F) (r + e)
      (topologicalKrullDim_supp_pullback_le K sX sY f hbase e he F r hFr)
    have hGsX := schemeDeltaDimension_reducedSupport_le_of_topologicalKrullDim_le K sX
      ((Scheme.Modules.pullback f).obj G) (s + e)
      (topologicalKrullDim_supp_pullback_le K sX sY f hbase e he G s hGs)
    AlgebraicCycle.IntersectProperly
        (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj F)
          ((r + e : ℕ) : ℤ) hFrX)
        (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj G)
          ((s + e : ℕ) : ℤ) hGsX) ∧
      (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) ((r : ℤ) + s - dY)
          ⟨torFormulaCycleIntersectionProduct (fieldChowSituation K) sY hY ((r : ℤ) + s - dY)
              (coherentSheafCycle (fieldChowSituation K) sY F (r : ℤ) hFrY)
              (coherentSheafCycle (fieldChowSituation K) sY G (s : ℤ) hGsY),
            torFormulaCycleIntersectionProduct_mem_cyclesOfDimension (fieldChowSituation K) sY hY
              ((r : ℤ) + s - dY) _ _⟩).1 =
        torFormulaCycleIntersectionProduct (fieldChowSituation K) sX hX ((r : ℤ) + s - dY + e)
          (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj F)
            ((r + e : ℕ) : ℤ) hFrX)
          (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj G)
            ((s + e : ℕ) : ℤ) hGsX)
```

## Tag 0B0Z, a lemma

[Tag 0B0Z](https://stacks.math.columbia.edu/tag/0B0Z) in the Stacks Project.

**`Stacks.Intersection.CycleFlatPullback.intersectProperly_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackCycles.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackCycles.lean#L125). The attribute's comment: “the first conclusion only, that `f^*α` and `f^*β` intersect properly, proved unconditionally and without assuming nonsingularity; the second conclusion `f^*(α · β) = f^*α · f^*β` is neither proved nor stated, needing the Tor formula of Stacks 0B0W — see the implementation notes”.

> Let `f : X ⟶ Y` be a flat morphism of varieties over a field `K` with `dim X = dim Y + e`,
> let `α` be an `r`-cycle and `β` an `s`-cycle on `Y`, and assume `α` and `β` intersect properly.
> Then the flat pullbacks `f^*α` and `f^*β` intersect properly.

```lean
theorem intersectProperly_flatPullback (K : Type u) [Field K] {X Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K)) [IsVariety K sX] [IsVariety K sY]
    (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX) (e : ℕ)
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞)) (r s : ℕ)
    (α : CycleGroup (fieldChowSituation K) sY (r : ℤ))
    (β : CycleGroup (fieldChowSituation K) sY (s : ℤ))
    (hαβ : AlgebraicCycle.IntersectProperly α.1 β.1) :
    haveI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    AlgebraicCycle.IntersectProperly
      (flatPullback (fieldChowSituation K) sX sY f hbase e
        (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (r : ℤ) α).1
      (flatPullback (fieldChowSituation K) sX sY f hbase e
        (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (s : ℤ) β).1
```

**`Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq_integerDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean, line 563](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean#L563). The attribute's comment: “the whole lemma, in every case of the integer expected dimension `r + s - dim Y`, the case `r + s < dim Y` included: both that `f^*α` and `f^*β` intersect properly and the identity `f^*(α · β) = f^*α · f^*β`, for an `r`-cycle `α` and an `s`-cycle `β` intersecting properly on `Y` and a flat morphism `f : X ⟶ Y` of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — with `dim X = dim Y + e`. The products are the Section 43.17 product of cycles of Tag 0B08, taken in the integer dimensions `(r : ℤ) + s - dim Y` downstairs and `(r : ℤ) + s - dim Y + e` upstairs.”.

> **Stacks Project, Tag 0B0Z**, with the expected dimension an integer. Let `f : X ⟶ Y` be a
> flat morphism of nonsingular varieties over an algebraically closed field `K` — the chapter's
> convention, Tag 0AZ8 — with `dim X = dim Y + e`. Let `α` be an `r`-cycle and `β` an `s`-cycle on
> `Y` which intersect properly. Then `f^*α` and `f^*β` intersect properly and
>
> `f^*(α · β) = f^*α · f^*β`.
>
> The products are taken in the integer dimensions `r + s - dim Y` downstairs and
> `r + s - dim Y + e` upstairs, every value included. When `r + s < dim Y`, proper intersection
> forces every component of `α` to be disjoint from every component of `β`, and both sides are
> then `0` (`flatPullback_torFormulaCycleIntersectionProduct_eq_zero_of_add_lt`).

```lean
theorem flatPullback_torFormulaCycleIntersectionProduct_eq_integerDimension
    (K : Type u) [Field K] [IsAlgClosed K] {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K))
    (sY : Y ⟶ Spec (.of K)) [IsVariety K sX] [IsVariety K sY] (hX : AlgebraicGeometry.IsRegular X)
    (hY : AlgebraicGeometry.IsRegular Y) (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX)
    (e dY r s : ℕ)
    (hdY : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (α : CycleGroup (fieldChowSituation K) sY (r : ℤ))
    (β : CycleGroup (fieldChowSituation K) sY (s : ℤ))
    (hαβ : AlgebraicCycle.IntersectProperly α.1 β.1) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    AlgebraicCycle.IntersectProperly
        (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (r : ℤ) α).1
        (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (s : ℤ) β).1 ∧
      (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) ((r : ℤ) + s - dY)
          ⟨torFormulaCycleIntersectionProduct (fieldChowSituation K) sY hY ((r : ℤ) + s - dY)
              α.1 β.1,
            torFormulaCycleIntersectionProduct_mem_cyclesOfDimension (fieldChowSituation K) sY hY
              ((r : ℤ) + s - dY) α.1 β.1⟩).1 =
        torFormulaCycleIntersectionProduct (fieldChowSituation K) sX hX ((r : ℤ) + s - dY + e)
          (flatPullback (fieldChowSituation K) sX sY f hbase e
            (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (r : ℤ) α).1
          (flatPullback (fieldChowSituation K) sX sY f hbase e
            (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (s : ℤ) β).1
```

**`Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackWhole.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackWhole.lean#L308). The attribute's comment: “the whole lemma in the case `r + s ≥ dim Y`, the product being graded by a natural number `n`; every case, `r + s < dim Y` included, is `flatPullback_torFormulaCycleIntersectionProduct_eq_integerDimension`. Here: both that `f^*α` and `f^*β` intersect properly and the identity `f^*(α · β) = f^*α · f^*β`, for a flat morphism of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — with `dim X = dim Y + e`. The products are the Section 43.17 product of cycles of Tag 0B08, graded so that an `r`-cycle and an `s`-cycle multiply into dimension `n` with `r + s = dim Y + n`, `WithBot ℕ∞` having no subtraction. The source's `[V] = [𝒪_V]_r` is `AlgebraicGeometry.TorFormula.coherentSheafCycle_structureSheafAt` and its `f^*[V] = [f^*𝒪_V]_{r+e}` is Tag 0AZF, so the pulled-back components are cycles of coherent sheaves; bilinearity of the product then reduces the identity to one pair of components, where it is Tag 0B0W upstairs.”.

> **Stacks Project, Tag 0B0Z.** Let `f : X ⟶ Y` be a flat morphism of nonsingular varieties
> over an algebraically closed field `K` — the chapter's convention, Tag 0AZ8 — with
> `dim X = dim Y + e`. Let `α` be an `r`-cycle and `β` an `s`-cycle on `Y` which intersect
> properly. Then `f^*α` and `f^*β` intersect properly and
>
> `f^*(α · β) = f^*α · f^*β`.

```lean
theorem flatPullback_torFormulaCycleIntersectionProduct_eq (K : Type u) [Field K] [IsAlgClosed K]
    {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K))
    [IsVariety K sX] [IsVariety K sY] (hX : AlgebraicGeometry.IsRegular X)
    (hY : AlgebraicGeometry.IsRegular Y) (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX)
    (e dY r s n : ℕ) (hdY : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (hrs : r + s = dY + n)
    (α : CycleGroup (fieldChowSituation K) sY (r : ℤ))
    (β : CycleGroup (fieldChowSituation K) sY (s : ℤ))
    (hαβ : AlgebraicCycle.IntersectProperly α.1 β.1) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    AlgebraicCycle.IntersectProperly
        (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (r : ℤ) α).1
        (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (s : ℤ) β).1 ∧
      (flatPullback (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (n : ℤ)
          ⟨torFormulaCycleIntersectionProduct (fieldChowSituation K) sY hY (n : ℤ) α.1 β.1,
            torFormulaCycleIntersectionProduct_mem_cyclesOfDimension (fieldChowSituation K) sY hY
              (n : ℤ) α.1 β.1⟩).1 =
        torFormulaCycleIntersectionProduct (fieldChowSituation K) sX hX ((n : ℤ) + (e : ℤ))
          (flatPullback (fieldChowSituation K) sX sY f hbase e
            (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (r : ℤ) α).1
          (flatPullback (fieldChowSituation K) sX sY f hbase e
            (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (s : ℤ) β).1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.21, Tag 0B0B](https://stacks.math.columbia.edu/tag/0B0B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
