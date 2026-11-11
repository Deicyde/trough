---
declaration: section
origin: cited
lean: Stacks.Intersection.CycleFlatPullback.flatPullback_coherentSheafCycleProduct_integerDimension, Stacks.Intersection.CycleFlatPullback.flatPullback_coherentSheafCycleProduct, Stacks.Intersection.FlatPullback.intersectProperly_coherentSheafCycle_pullback, Stacks.Intersection.FlatPullback.flatPullback_intersectionProductCycleGroup, Stacks.Intersection.FlatPullback.flatPullback_intersectionProductCycleGroup_eq_pullbackSheaves, Stacks.Intersection.CycleFlatPullback.intersectProperly_flatPullback, Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq_integerDimension, Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq
statement: formalized
proof: formalized
---

# 43.21 Flat pullback and intersection products

Section 43.21 of the Stacks Project, [Tag 0B0B](https://stacks.math.columbia.edu/tag/0B0B). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B0Y, a lemma

[Tag 0B0Y](https://stacks.math.columbia.edu/tag/0B0Y) in the Stacks Project.

**`Stacks.Intersection.CycleFlatPullback.flatPullback_coherentSheafCycleProduct_integerDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean#L236). The attribute's comment: “the whole lemma, in every case of the integer expected dimension `r + s - dim Y`, the case `r + s < dim Y` included: both that `[f^*ℱ]_{r+e}` and `[f^*𝒢]_{s+e}` intersect properly and the identity `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`, for a flat morphism of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — under the source's own three dimension bounds on `Supp ℱ`, `Supp 𝒢` and their intersection. `WithBot ℕ∞` has no subtraction, so `dim(Supp ℱ ∩ Supp 𝒢) ≤ r + s - dim Y` is spelled `dim(Supp ℱ ∩ Supp 𝒢) + dim Y ≤ r + s`, as proper intersection is in Tag 0AZQ, and the products are taken in the integer dimensions `(r : ℤ) + s - dim Y` and `(r : ℤ) + s - dim Y + e`. Both products are the Section 43.17 product of cycles `AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct` (Tag 0B08).”.

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

**`Stacks.Intersection.CycleFlatPullback.flatPullback_coherentSheafCycleProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackWhole.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackWhole.lean#L123). The attribute's comment: “the whole lemma in the case `r + s ≥ dim Y`, the expected dimension being a natural number `n`; every case, `r + s < dim Y` included, is `flatPullback_coherentSheafCycleProduct_integerDimension`. Here: both that `[f^*ℱ]_{r+e}` and `[f^*𝒢]_{s+e}` intersect properly and the identity `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`, for a flat morphism of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — under the source's own three dimension bounds on `Supp ℱ`, `Supp 𝒢` and their intersection. `WithBot ℕ∞` has no subtraction, so `n = r + s - dim Y` is the relation `r + s = dim Y + n`. Both products are the Section 43.17 product of cycles `AlgebraicGeometry.TorFormula.torFormulaCycleIntersectionProduct` (Tag 0B08), so this is the source's statement and not merely its Tor-sheaf shadow: the passage between the two is Tag 0B0W, applied downstairs and upstairs. The flat pullback of the alternating sum of Tor cycles, which is the other half of the source's proof, is `Stacks.Intersection.FlatPullback.flatPullback_intersectionProductCycleGroup_eq_pullbackSheaves`.”.

> **Stacks Project, Tag 0B0Y.** Let `f : X ⟶ Y` be a flat morphism of nonsingular varieties
> over an algebraically closed field `K` — the chapter's convention, Tag 0AZ8 — and set
> `e = dim X - dim Y`. Let `ℱ` and `𝒢` be coherent sheaves on `Y` with
> `dim Supp ℱ ≤ r`, `dim Supp 𝒢 ≤ s` and `dim(Supp ℱ ∩ Supp 𝒢) ≤ r + s - dim Y`. Then the cycles
> `[f^*ℱ]_{r+e}` and `[f^*𝒢]_{s+e}` intersect properly and
>
> `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`.
>
> `WithBot ℕ∞` has no subtraction, so `n = r + s - dim Y` is the relation `r + s = dim Y + n`.

```lean
theorem flatPullback_coherentSheafCycleProduct (K : Type u) [Field K] [IsAlgClosed K]
    {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K))
    [IsVariety K sX] [IsVariety K sY] (hX : AlgebraicGeometry.IsRegular X)
    (hY : AlgebraicGeometry.IsRegular Y) (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX)
    (F G : Y.Modules) (hFc : _root_.SheafOfModules.IsCoherent F)
    (hGc : _root_.SheafOfModules.IsCoherent G) (r s n dY e : ℕ)
    (hdY : topologicalKrullDim Y = (dY : WithBot ℕ∞))
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (hrs : r + s = dY + n)
    (hFr : topologicalKrullDim (SheafOfModules.supp F : Set Y) ≤ (r : WithBot ℕ∞))
    (hGs : topologicalKrullDim (SheafOfModules.supp G : Set Y) ≤ (s : WithBot ℕ∞))
    (hFG : topologicalKrullDim (SheafOfModules.supp F ∩ SheafOfModules.supp G : Set Y) ≤
      (n : WithBot ℕ∞)) :
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
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) (n : ℤ)
          ⟨torFormulaCycleIntersectionProduct (fieldChowSituation K) sY hY (n : ℤ)
              (coherentSheafCycle (fieldChowSituation K) sY F (r : ℤ) hFrY)
              (coherentSheafCycle (fieldChowSituation K) sY G (s : ℤ) hGsY),
            torFormulaCycleIntersectionProduct_mem_cyclesOfDimension (fieldChowSituation K) sY hY
              (n : ℤ) _ _⟩).1 =
        torFormulaCycleIntersectionProduct (fieldChowSituation K) sX hX ((n + e : ℕ) : ℤ)
          (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj F)
            ((r + e : ℕ) : ℤ) hFrX)
          (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj G)
            ((s + e : ℕ) : ℤ) hGsX)
```

**`Stacks.Intersection.FlatPullback.intersectProperly_coherentSheafCycle_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FlatPullback.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FlatPullback.lean#L210). The attribute's comment: “the clause that `[f^*ℱ]_{r+e}` and `[f^*𝒢]_{s+e}` intersect properly, proved unconditionally. It is the source's "immediate from the fact that `f` has relative dimension `e`": the supports of the pullbacks are the inverse images of the supports, and the inverse image of a closed subset of dimension `n` has dimension at most `n + e`, which is the topological form of Stacks 02RE part (1) proved above. Nonsingularity is not used, only that `X` and `Y` are varieties over the field”.

> **Stacks Project, Tag 0B0Y.** Let `f : X ⟶ Y` be a flat morphism of varieties over a field
> with `dim X = dim Y + e`, and let `ℱ` and `𝒢` be coherent `𝒪_Y`-modules whose supports have
> dimension at most `r` and `s` and meet in dimension at most `r + s - dim Y`. Then the cycles
> `[f^*ℱ]_{r+e}` and `[f^*𝒢]_{s+e}` intersect properly.

```lean
theorem intersectProperly_coherentSheafCycle_pullback (K : Type u) [Field K] {X Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K)) [IsVariety K sX] [IsVariety K sY]
    (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX) (e : ℕ)
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (F G : Y.Modules) [hF : F.IsCoherent] [hG : G.IsCoherent] (r s : ℕ)
    (hFr : schemeDeltaDimension (fieldChowSituation K)
      ((reducedSupport F).subschemeι ≫ sY) ≤ ((r : ℤ) : EInt))
    (hGs : schemeDeltaDimension (fieldChowSituation K)
      ((reducedSupport G).subschemeι ≫ sY) ≤ ((s : ℤ) : EInt))
    (hFG : topologicalKrullDim (SheafOfModules.supp F ∩ SheafOfModules.supp G : Set Y) +
      topologicalKrullDim Y ≤ (r : WithBot ℕ∞) + (s : WithBot ℕ∞)) :
    haveI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : ((Scheme.Modules.pullback f).obj F).IsCoherent := isCoherent_pullback f F
    haveI : ((Scheme.Modules.pullback f).obj G).IsCoherent := isCoherent_pullback f G
    AlgebraicCycle.IntersectProperly
      (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj F)
        ((r + e : ℕ) : ℤ)
        (schemeDeltaDimension_support_pullback_le (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) F (r : ℤ) hFr))
      (coherentSheafCycle (fieldChowSituation K) sX ((Scheme.Modules.pullback f).obj G)
        ((s + e : ℕ) : ℤ)
        (schemeDeltaDimension_support_pullback_le (fieldChowSituation K) sX sY f hbase e
          (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) G (s : ℤ) hGs))
```

**`Stacks.Intersection.FlatPullback.flatPullback_intersectionProductCycleGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FlatPullback.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FlatPullback.lean#L338). The attribute's comment: “the intersection-product identity `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`, with the product read as the Tor formula `∑ᵢ (-1)ⁱ [Torᵢ(ℱ, 𝒢)]_{r+s-dim Y}` of Stacks 0AZR, which is how this library defines it. What is discharged here is the half of the source's proof that reduces the identity to the Tor comparison: that flat pullback passes through the alternating sum, and that on each summand it is the cycle identity `f^*[Torᵢ]_k = [f^*Torᵢ]_{k+e}` of Stacks 0AZF. The comparison itself, `f^*Torᵢ^{𝒪_Y}(ℱ, 𝒢) = Torᵢ^{𝒪_X}(f^*ℱ, f^*𝒢)`, is carried as the hypothesis `hTor`: the source gets it from Stacks 079U together with the exactness of `f^*` for flat `f`, and this library has 079U but not the identification `Lf^*ℱ = f^*ℱ` that exactness supplies. It is not an instance of the conclusion below, which is a statement about cycles. The properness clause of the tag is `Stacks.Intersection.FlatPullback.intersectProperly_coherentSheafCycle_pullback`”.

> **Stacks Project, Tag 0B0Y.** Let `f : X ⟶ Y` be a flat morphism of nonsingular varieties
> over a field and let `e = dim X - dim Y`. For coherent `𝒪_Y`-modules `ℱ` and `𝒢` the flat
> pullback of their intersection product is the intersection product of their pullbacks:
>
> `f^*(∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_Y}(ℱ, 𝒢)]_k) = ∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_X}(f^*ℱ, f^*𝒢)]_{k+e}`.
>
> Taking `k = r + s - dim Y`, for supports of dimension at most `r` and `s`, this is
> `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`.

```lean
theorem flatPullback_intersectionProductCycleGroup (K : Type u) [Field K] {X Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K)) [IsVariety K sX] [IsVariety K sY]
    (hX : AlgebraicGeometry.IsRegular X) (hY : AlgebraicGeometry.IsRegular Y) (f : X ⟶ Y)
    [Flat f] (hbase : f ≫ sY = sX) (e : ℕ)
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (F G : Y.Modules) (hF : _root_.SheafOfModules.IsCoherent F)
    (hG : _root_.SheafOfModules.IsCoherent G) (k : ℤ)
    (hFk : ∀ i : ℕ,
      haveI := isCoherent_torSheaf_of_isRegular Y hY F G hF hG i
      schemeDeltaDimension (fieldChowSituation K)
        ((reducedSupport (torSheaf Y F G i)).subschemeι ≫ sY) ≤ (k : EInt))
    (hTor : ∀ i : ℕ,
      haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
      (Scheme.Modules.pullback f).obj (torSheaf Y F G i) ≅
        torSheaf X ((Scheme.Modules.pullback f).obj F)
          ((Scheme.Modules.pullback f).obj G) i) :
    haveI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    flatPullback (fieldChowSituation K) sX sY f hbase e
        (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) k
        (intersectionProductCycleGroup (fieldChowSituation K) sY hY F G hF hG k hFk) =
      intersectionProductCycleGroup (fieldChowSituation K) sX hX
        ((Scheme.Modules.pullback f).obj F) ((Scheme.Modules.pullback f).obj G)
        (isCoherent_pullback f F) (isCoherent_pullback f G) (k + (e : ℤ))
        (schemeDeltaDimension_reducedSupport_torSheaf_pullback_le K sX sY hX hY f hbase e he
          F G hF hG k hFk hTor)
```

**`Stacks.Intersection.FlatPullback.flatPullback_intersectionProductCycleGroup_eq_pullbackSheaves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FlatPullbackTorComparison.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/TorFormula/FlatPullbackTorComparison.lean#L94). The attribute's comment: “the intersection-product identity `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`, with the product read as the Tor formula `∑ᵢ (-1)ⁱ [Torᵢ(ℱ, 𝒢)]_{r+s-dim Y}` of Stacks 0AZR, which is how this library defines it. As in the source, flat pullback passes through the alternating sum, on each summand it is the cycle identity `f^*[Torᵢ]_k = [f^*Torᵢ]_{k+e}` of Stacks 0AZF, and the Tor comparison `f^*Torᵢ^{𝒪_Y}(ℱ, 𝒢) = Torᵢ^{𝒪_X}(f^*ℱ, f^*𝒢)` is `AlgebraicGeometry.TorFormula.pullbackTorSheafIso`, which runs the source's argument from Stacks 079U on K-flat representatives. The properness clause of the tag is `Stacks.Intersection.FlatPullback.intersectProperly_coherentSheafCycle_pullback`”.

> **Stacks Project, Tag 0B0Y.** Let `f : X ⟶ Y` be a flat morphism of nonsingular varieties
> over a field and let `e = dim X - dim Y`. For coherent `𝒪_Y`-modules `ℱ` and `𝒢` the flat
> pullback of their intersection product is the intersection product of their pullbacks:
>
> `f^*(∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_Y}(ℱ, 𝒢)]_k) = ∑ᵢ (-1)ⁱ [Torᵢ^{𝒪_X}(f^*ℱ, f^*𝒢)]_{k+e}`.
>
> Taking `k = r + s - dim Y`, for supports of dimension at most `r` and `s`, this is
> `f^*([ℱ]_r · [𝒢]_s) = [f^*ℱ]_{r+e} · [f^*𝒢]_{s+e}`.
>
> This is `Stacks.Intersection.FlatPullback.flatPullback_intersectionProductCycleGroup` with the
> comparison `f^*Torᵢ^{𝒪_Y}(ℱ, 𝒢) ≅ Torᵢ^{𝒪_X}(f^*ℱ, f^*𝒢)` supplied by
> `AlgebraicGeometry.TorFormula.pullbackTorSheafIso`.

```lean
theorem flatPullback_intersectionProductCycleGroup_eq_pullbackSheaves (K : Type u) [Field K]
    {X Y : Scheme.{u}} (sX : X ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K)) [IsVariety K sX]
    [IsVariety K sY] (hX : AlgebraicGeometry.IsRegular X) (hY : AlgebraicGeometry.IsRegular Y)
    (f : X ⟶ Y) [Flat f] (hbase : f ≫ sY = sX) (e : ℕ)
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞))
    (F G : Y.Modules) (hF : _root_.SheafOfModules.IsCoherent F)
    (hG : _root_.SheafOfModules.IsCoherent G) (k : ℤ)
    (hFk : ∀ i : ℕ,
      haveI := isCoherent_torSheaf_of_isRegular Y hY F G hF hG i
      schemeDeltaDimension (fieldChowSituation K)
        ((reducedSupport (torSheaf Y F G i)).subschemeι ≫ sY) ≤ (k : EInt)) :
    haveI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hbase
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    flatPullback (fieldChowSituation K) sX sY f hbase e
        (relativeDimension_of_flat_of_isVariety K sX sY f hbase e he) k
        (intersectionProductCycleGroup (fieldChowSituation K) sY hY F G hF hG k hFk) =
      intersectionProductCycleGroup (fieldChowSituation K) sX hX
        ((Scheme.Modules.pullback f).obj F) ((Scheme.Modules.pullback f).obj G)
        (isCoherent_pullback f F) (isCoherent_pullback f G) (k + (e : ℤ))
        (schemeDeltaDimension_torSheaf_flatPullback_le K sX sY hX hY f hbase e he
          F G hF hG k hFk)
```

## Tag 0B0Z, a lemma

[Tag 0B0Z](https://stacks.math.columbia.edu/tag/0B0Z) in the Stacks Project.

**`Stacks.Intersection.CycleFlatPullback.intersectProperly_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackCycles.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackCycles.lean#L125). The attribute's comment: “the first conclusion only, that `f^*α` and `f^*β` intersect properly, proved unconditionally and without assuming nonsingularity; the second conclusion `f^*(α · β) = f^*α · f^*β` is neither proved nor stated, needing the Tor formula of Stacks 0B0W — see the implementation notes”.

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

**`Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq_integerDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackIntegerDimension.lean#L559). The attribute's comment: “the whole lemma, in every case of the integer expected dimension `r + s - dim Y`, the case `r + s < dim Y` included: both that `f^*α` and `f^*β` intersect properly and the identity `f^*(α · β) = f^*α · f^*β`, for an `r`-cycle `α` and an `s`-cycle `β` intersecting properly on `Y` and a flat morphism `f : X ⟶ Y` of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — with `dim X = dim Y + e`. The products are the Section 43.17 product of cycles of Tag 0B08, taken in the integer dimensions `(r : ℤ) + s - dim Y` downstairs and `(r : ℤ) + s - dim Y + e` upstairs.”.

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

**`Stacks.Intersection.CycleFlatPullback.flatPullback_torFormulaCycleIntersectionProduct_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackWhole.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ProperIntersections/FlatPullbackWhole.lean#L320). The attribute's comment: “the whole lemma in the case `r + s ≥ dim Y`, the product being graded by a natural number `n`; every case, `r + s < dim Y` included, is `flatPullback_torFormulaCycleIntersectionProduct_eq_integerDimension`. Here: both that `f^*α` and `f^*β` intersect properly and the identity `f^*(α · β) = f^*α · f^*β`, for a flat morphism of nonsingular varieties over an algebraically closed field — the chapter's own convention, Tag 0AZ8 — with `dim X = dim Y + e`. The products are the Section 43.17 product of cycles of Tag 0B08, graded so that an `r`-cycle and an `s`-cycle multiply into dimension `n` with `r + s = dim Y + n`, `WithBot ℕ∞` having no subtraction. The source's `[V] = [𝒪_V]_r` is `AlgebraicGeometry.TorFormula.coherentSheafCycle_structureSheafAt` and its `f^*[V] = [f^*𝒪_V]_{r+e}` is Tag 0AZF, so the pulled-back components are cycles of coherent sheaves; bilinearity of the product then reduces the identity to one pair of components, where it is Tag 0B0W upstairs.”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
