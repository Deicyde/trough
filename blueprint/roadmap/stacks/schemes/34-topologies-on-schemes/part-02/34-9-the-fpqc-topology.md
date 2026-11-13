---
declaration: section
origin: cited
lean: AlgebraicGeometry.ofArrows_mem_fpqcPrecoverage_iff_isFpqcCoveringFamily, AlgebraicGeometry.ofArrows_mem_fpqcPrecoverage_iff, AlgebraicGeometry.Scheme.fpqcPrecoverage, AlgebraicGeometry.isFpqcCoveringFamily_iff_affine_finite_support, AlgebraicGeometry.isFpqcCoveringFamily_iff_exists_affine_open_cover, AlgebraicGeometry.isFpqcCoveringFamily_iff_pointwise_compact_open_neighborhood, AlgebraicGeometry.DoubledOriginSource.flat_map, AlgebraicGeometry.DoubledOriginSource.surjective_map
statement: formalized
proof: formalized
---

# 34.9 The fpqc topology

Section 34.9 of the Stacks Project, [Tag 022A](https://stacks.math.columbia.edu/tag/022A). 14 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 022B, a definition

[Tag 022B](https://stacks.math.columbia.edu/tag/022B) in the Stacks Project.

**`AlgebraicGeometry.ofArrows_mem_fpqcPrecoverage_iff_isFpqcCoveringFamily`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean#L51). The attribute's comment: “identification with Mathlib's `Scheme.fpqcPrecoverage`”.

> A family lies in Mathlib's `Scheme.fpqcPrecoverage` if and only if it is an fpqc covering
> in the sense of Stacks 022B: every member is flat and every affine open of the target is the
> union of the images of finitely many affine opens of the sources.  Mathlib's quasi-compactness
> condition asks for quasi-compact opens instead of affine ones; a quasi-compact open is a finite
> union of affine opens, and an affine open is quasi-compact.

```lean
public lemma ofArrows_mem_fpqcPrecoverage_iff_isFpqcCoveringFamily :
    Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage T ↔ IsFpqcCoveringFamily X f
```

**`AlgebraicGeometry.ofArrows_mem_fpqcPrecoverage_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StacksDefinition.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StacksDefinition.lean#L44). The attribute's comment: “the fpqc coverings: Scheme.fpqcPrecoverage, with the definition's condition”.

> **The fpqc coverings of a scheme.** A family `{f i : X i ⟶ T}` lies in Mathlib's fpqc
> precoverage `Scheme.fpqcPrecoverage` if and only if it is an fpqc covering in the sense of the
> source: every `f i` is flat, and every affine open `U` of `T` is the union of the images
> `f (a j) '' V j` of finitely many affine opens `V j` of the `X (a j)`, `j : Fin n`.
>
> Mathlib's precoverage also asks for the family to be jointly surjective; the source remarks right
> after the definition that this follows from the covering condition, and the right-hand side here
> does not ask for it.

```lean
public lemma ofArrows_mem_fpqcPrecoverage_iff :
    Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage T ↔
      ((∀ i, Flat (f i)) ∧
        ∀ U : T.Opens, IsAffineOpen U →
          ∃ (n : ℕ) (a : Fin n → I) (V : ∀ j, (X (a j)).Opens),
            (∀ j, IsAffineOpen (V j)) ∧
              ⋃ j, f (a j) '' (V j : Set (X (a j))) = (U : Set T))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.fpqcPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.fpqcPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L41) (StacksFrontier): “fpqc coverings: the families that are flat, jointly surjective and quasi-compact (QuasiCompactCover, which carries Mathlib's own 022B attribution, is the quasi-compactness condition alone)”. References: SGA 3 IV (4.7); SGA 4 VII (4.2); SGA 4 XVII (0.10), “partial”.

## Tag 03L7, a lemma

[Tag 03L7](https://stacks.math.columbia.edu/tag/03L7) in the Stacks Project.

**`AlgebraicGeometry.ofArrows_mem_fpqcPrecoverage_iff_isFpqcCoveringFamily`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean#L51). The attribute's comment: “(1)”.

> A family lies in Mathlib's `Scheme.fpqcPrecoverage` if and only if it is an fpqc covering
> in the sense of Stacks 022B: every member is flat and every affine open of the target is the
> union of the images of finitely many affine opens of the sources.  Mathlib's quasi-compactness
> condition asks for quasi-compact opens instead of affine ones; a quasi-compact open is a finite
> union of affine opens, and an affine open is quasi-compact.

```lean
public lemma ofArrows_mem_fpqcPrecoverage_iff_isFpqcCoveringFamily :
    Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage T ↔ IsFpqcCoveringFamily X f
```

**`AlgebraicGeometry.isFpqcCoveringFamily_iff_affine_finite_support`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean#L70). The attribute's comment: “conditions (1) and (2)”.

> A family is an fpqc covering (Stacks 022B) if and only if every member is flat and every
> affine open of the target is the union of the images of quasi-compact opens in the sources,
> all but finitely many of which are empty.

```lean
public lemma isFpqcCoveringFamily_iff_affine_finite_support :
    IsFpqcCoveringFamily X f ↔
      ((∀ i, Flat (f i)) ∧
        (∀ U : T.Opens, IsAffineOpen U →
            ∃ V : ∀ i, (X i).Opens,
              ((∀ i, IsCompact (V i : Set (X i))) ∧
                ({i | V i ≠ ⊥} : Set I).Finite ∧
                ⋃ i, f i '' (V i : Set (X i)) = (U : Set T))))
```

**`AlgebraicGeometry.isFpqcCoveringFamily_iff_exists_affine_open_cover`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean#L85). The attribute's comment: “conditions (1) and (3)”.

> A family is an fpqc covering (Stacks 022B) if and only if its members are flat and some
> affine open covering of the target is, member by member, the union of images of finitely many
> quasi-compact opens in the sources.

```lean
public lemma isFpqcCoveringFamily_iff_exists_affine_open_cover :
    IsFpqcCoveringFamily X f ↔
      ((∀ i, Flat (f i)) ∧
        ∃ (A : Type u) (U : A → T.Opens),
          ((∀ a, IsAffineOpen (U a)) ∧
            (⋃ a, (U a : Set T)) = Set.univ ∧
            ∀ a, ∃ (n : ℕ) (i : Fin n → I) (V : ∀ j, (X (i j)).Opens),
              ((∀ j, IsCompact (V j : Set (X (i j)))) ∧
                ⋃ j, f (i j) '' (V j : Set (X (i j))) = (U a : Set T))))
```

**`AlgebraicGeometry.isFpqcCoveringFamily_iff_pointwise_compact_open_neighborhood`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/CoveringFamily.lean#L102). The attribute's comment: “conditions (1) and (4)”.

> If the target is quasi-separated, a family is an fpqc covering (Stacks 022B) if and only
> if its members are flat and every point has a neighborhood which is the union of the images of
> finitely many quasi-compact opens in the sources. The neighborhood itself is not required to be
> open.

```lean
public lemma isFpqcCoveringFamily_iff_pointwise_compact_open_neighborhood
    [QuasiSeparatedSpace T] :
    IsFpqcCoveringFamily X f ↔
      ((∀ i, Flat (f i)) ∧
        ∀ t : T, ∃ (n : ℕ) (i : Fin n → I) (V : ∀ j, (X (i j)).Opens),
          ((∀ j, IsCompact (V j : Set (X (i j)))) ∧
            (⋃ j, f (i j) '' (V j : Set (X (i j)))) ∈ nhds t))
```

## Tag 0H7E, an example

[Tag 0H7E](https://stacks.math.columbia.edu/tag/0H7E) in the Stacks Project.

**`AlgebraicGeometry.DoubledOriginSource.flat_map`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/DoubledOriginSource.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/DoubledOriginSource.lean#L115). The attribute's comment: “flatness”.

> The canonical map from the first chart and the local scheme of the second
> chart to the doubled-origin scheme is flat.

```lean
public instance flat_map (S : DoubledOriginSource.{u}) : Flat S.map
```

**`AlgebraicGeometry.DoubledOriginSource.surjective_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/DoubledOriginSource.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/DoubledOriginSource.lean#L223). The attribute's comment: “surjectivity”.

> The canonical map from an affine chart and the local spectrum covers the
> scheme with doubled origin.

```lean
public theorem surjective_map (S : DoubledOriginSource.{u}) :
    Surjective S.map
```

**`AlgebraicGeometry.DoubledOriginSource.map_image_ne_range_secondChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/NotFpqc.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/NotFpqc.lean#L250). The attribute's comment: “no\_quasicompact\_open”.

> No quasi-compact open of the source maps onto the second affine chart of the
> infinite-dimensional doubled-origin scheme.

```lean
public theorem map_image_ne_range_secondChart (S : DoubledOriginSource)
    (W : S.source.Opens) (hW : IsCompact (W : Set S.source)) :
    S.map.base '' (W : Set S.source) ≠ Set.range S.secondChart.base
```

**`AlgebraicGeometry.DoubledOriginSource.exists_isCompact_opens_image_mem_nhds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/NotFpqc.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/NotFpqc.lean#L307). The attribute's comment: “pointwise\_condition”.

> Every point of the doubled-origin scheme has a neighbourhood that is the image of a
> quasi-compact open of the source of the canonical map.

```lean
public theorem exists_isCompact_opens_image_mem_nhds
    (S : DoubledOriginSource.{u}) (x : S.target) :
    ∃ V : S.source.Opens,
      IsCompact (V : Set S.source) ∧ S.map '' (V : Set S.source) ∈ nhds x
```

**`AlgebraicGeometry.DoubledOriginSource.singleton_map_notMem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/NotFpqc.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/FpqcCounterexample/NotFpqc.lean#L319). The attribute's comment: “not\_fpqc”.

> The map from the affine chart and the local scheme at the origin to the infinite-dimensional
> doubled-origin scheme does not form an fpqc covering.

```lean
public theorem singleton_map_notMem_fpqcPrecoverage (S : DoubledOriginSource.{u}) :
    Presieve.singleton S.map ∉ Scheme.fpqcPrecoverage S.target
```

## Tag 040I, a lemma

[Tag 040I](https://stacks.math.columbia.edu/tag/040I) in the Stacks Project.

**`AlgebraicGeometry.ofArrows_mem_fpqcPrecoverage_iff_singleton_sigmaDesc_mem`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/DisjointUnion.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/DisjointUnion.lean#L157).

> A family of morphisms of schemes is an fpqc covering precisely when the induced
> morphism from the disjoint union of the source schemes is an fpqc covering.

```lean
public lemma ofArrows_mem_fpqcPrecoverage_iff_singleton_sigmaDesc_mem
    {ι : Type v} [Small.{u} ι] {T : Scheme.{u}} (T' : ι → Scheme.{u})
    (f : ∀ i, T' i ⟶ T) :
    Presieve.ofArrows T' f ∈ Scheme.fpqcPrecoverage T ↔
      Presieve.singleton (Sigma.desc f) ∈ Scheme.fpqcPrecoverage T
```

## Tag 03L9, a lemma

[Tag 03L9](https://stacks.math.columbia.edu/tag/03L9) in the Stacks Project.

**`AlgebraicGeometry.ofArrows_mem_fpqcPrecoverage_of_fpqc_locally`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Characterization.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Characterization.lean#L446).

> Being an fpqc covering is local on an fpqc covering of the base. If every
> member of a family `f i : X i ⟶ T` is flat and there is an fpqc covering `g j : S j ⟶ T` of the
> target such that for every `j` the base-changed family `S j ×[T] X i ⟶ S j` is an fpqc covering
> of `S j`, then `f` is an fpqc covering of `T`.

```lean
public lemma ofArrows_mem_fpqcPrecoverage_of_fpqc_locally
    {J : Type w} {S : J → Scheme.{u}} (g : ∀ j, S j ⟶ T)
    (hflat : ∀ i, Flat (f i))
    (hg : Presieve.ofArrows S g ∈ Scheme.fpqcPrecoverage T)
    (hbc : ∀ j, Presieve.ofArrows (fun i ↦ pullback (g j) (f i))
      (fun i ↦ pullback.fst (g j) (f i)) ∈ Scheme.fpqcPrecoverage (S j)) :
    Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage T
```

## Tag 022C, a lemma

[Tag 022C](https://stacks.math.columbia.edu/tag/022C) in the Stacks Project.

**`AlgebraicGeometry.Scheme.smoothPrecoverage_le_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean#L53). The attribute's comment: “smooth coverings”.

> **Stacks 022C.** Every smooth covering family is an fpqc covering family.

```lean
public theorem smoothPrecoverage_le_fpqcPrecoverage :
    Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}) ≤
      Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.Scheme.etalePrecoverage_le_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean#L60). The attribute's comment: “étale coverings”.

> **Stacks 022C, 03PH.** Every étale covering family is an fpqc covering family.

```lean
public theorem etalePrecoverage_le_fpqcPrecoverage :
    Scheme.etalePrecoverage ≤ Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.Scheme.syntomicPrecoverage_le_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/FinerTopologies.lean#L84). The attribute's comment: “syntomic coverings”.

> **Stacks 022C.** Every syntomic covering family is an fpqc covering family.

```lean
public theorem syntomicPrecoverage_le_fpqcPrecoverage :
    Scheme.precoverage (@Syntomic : MorphismProperty Scheme.{u}) ≤ Scheme.fpqcPrecoverage
```

Declarations registered for the tag:

- [`Scheme.fppfPrecoverage_le_fpqcPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.fppfPrecoverage_le_fpqcPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean#L49) (StacksFrontier): “fppf coverings”.
- [`Scheme.zariskiPrecoverage_le_fpqcPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Scheme.zariskiPrecoverage_le_fpqcPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Coverings.lean#L66) (StacksFrontier): “Zariski coverings”.

## Tag 022D, a lemma

[Tag 022D](https://stacks.math.columbia.edu/tag/022D) in the Stacks Project.

**`isFpqcCoveringFamily_of_isIso_and_comp_and_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Sites/FpqcCoveringStability.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Sites/FpqcCoveringStability.lean#L109). The attribute's comment: “all three parts, for fpqc coverings in the sense of Definition 022B (`IsFpqcCoveringFamily`: flat members, every affine open of the base covered by the images of finitely many affine opens): (1) an isomorphism is an fpqc covering, (2) composites of fpqc coverings are fpqc coverings, (3) base changes of fpqc coverings are fpqc coverings”.

> **Stacks 022D.** Let `T` be a scheme.
> 1. If `T' ⟶ T` is an isomorphism, then `{ T' ⟶ T }` is an fpqc covering of `T`.
> 2. If `{ T i ⟶ T }` is an fpqc covering and for each `i` the family `{ T i j ⟶ T i }` is an
>    fpqc covering, then `{ T i j ⟶ T }` (indexed by all pairs `(i, j)`) is an fpqc covering.
> 3. If `{ T i ⟶ T }` is an fpqc covering and `T' ⟶ T` is a morphism of schemes, then
>    `{ T' ×_T T i ⟶ T' }` is an fpqc covering.
>
> Here "fpqc covering" is Stacks' own notion `IsFpqcCoveringFamily` (Definition 022B).

```lean
theorem isFpqcCoveringFamily_of_isIso_and_comp_and_pullback :
    (∀ {T T' : Scheme.{u₁}} (f : T' ⟶ T) [IsIso f],
      IsFpqcCoveringFamily (fun _ : Unit => T') (fun _ => f)) ∧
    (∀ {ι : Type w₁} {T : Scheme.{u₁}} {T' : ι → Scheme.{u₁}} {f : ∀ i, T' i ⟶ T}
      {J : ι → Type w₂} {T'' : ∀ i, J i → Scheme.{u₁}} {g : ∀ i j, T'' i j ⟶ T' i},
      IsFpqcCoveringFamily T' f → (∀ i, IsFpqcCoveringFamily (T'' i) (g i)) →
      IsFpqcCoveringFamily (fun p : Σ i, J i => T'' p.1 p.2) (fun p => g p.1 p.2 ≫ f p.1)) ∧
    (∀ {ι : Type w₁} {T : Scheme.{u₁}} {T' : ι → Scheme.{u₁}} {f : ∀ i, T' i ⟶ T}
      {S : Scheme.{u₁}} (g : S ⟶ T), IsFpqcCoveringFamily T' f →
      IsFpqcCoveringFamily (fun i => pullback g (f i)) (fun i => pullback.fst g (f i)))
```

## Tag 022E, a lemma

[Tag 022E](https://stacks.math.columbia.edu/tag/022E) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_affineCover_flat_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardRefinement.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardRefinement.lean#L163).

> An fpqc covering of an affine scheme admits a refinement by a standard fpqc
> covering: a finite jointly surjective family of flat morphisms from affine schemes, again an
> fpqc covering, whose members are affine open subschemes of members of the given covering.

```lean
public theorem exists_finite_affineCover_flat_refinement {T : Scheme.{u}} [IsAffine T]
    (U : PreZeroHypercover.{v} T) (hU : U.presieve₀ ∈ Scheme.fpqcPrecoverage T) :
    ∃ (V : T.AffineCover.{0} (@Flat.{u})) (refinement : V.cover.toPreZeroHypercover.Hom U),
      Finite V.I₀ ∧ V.cover.presieve₀ ∈ Scheme.fpqcPrecoverage T ∧
        ∀ j, IsOpenImmersion (refinement.h₀ j)
```

## Tag 022F, a definition

[Tag 022F](https://stacks.math.columbia.edu/tag/022F) in the Stacks Project.

**`AlgebraicGeometry.IsStandardFpqcCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoverings.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoverings.lean#L69).

> A family `fᵢ : Uᵢ ⟶ T` is a **standard fpqc covering** if it is finite, its target and all
> its sources are affine, every `fᵢ` is flat, and the images of the `fᵢ` cover `T`.

```lean
public structure IsStandardFpqcCovering {T : Scheme.{u}} {I : Type v}
    (U : I → Scheme.{u}) (f : ∀ i, U i ⟶ T) : Prop
```

## Tag 03LA, a lemma

[Tag 03LA](https://stacks.math.columbia.edu/tag/03LA) in the Stacks Project.

**`AlgebraicGeometry.isStandardFpqcCovering_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoveringProperties.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoveringProperties.lean#L116). The attribute's comment: “(1)”.

> **Stacks 03LA (1).** If `T' ⟶ T` is an isomorphism onto an affine scheme, then the one-member
> family `{T' ⟶ T}` is a standard fpqc covering: the source is affine because it is isomorphic to
> the affine target, and an isomorphism is flat and surjective.

```lean
public theorem isStandardFpqcCovering_of_isIso {T T' : Scheme.{u}} [IsAffine T] (f : T' ⟶ T)
    [IsIso f] : IsStandardFpqcCovering (fun _ : PUnit.{v + 1} ↦ T') (fun _ ↦ f)
```

**`AlgebraicGeometry.IsStandardFpqcCovering.bind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoveringProperties.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoveringProperties.lean#L133). The attribute's comment: “(2)”.

> **Stacks 03LA (2).** If `{T_i ⟶ T}_{i ∈ I}` is a standard fpqc covering and
> `{T_ij ⟶ T_i}_{j ∈ J i}` is a standard fpqc covering for every `i`, then the family of composites
> `{T_ij ⟶ T}_{⟨i, j⟩ ∈ Σ i, J i}` is a standard fpqc covering.  Its index is the sigma type of the
> indices, finite because each of its factors is; its members are composites of flat morphisms,
> hence flat; and a point of `T` is hit through some member of the outer family and then through
> some member of the inner family above it.  The inner and the outer index types may lie in
> different universes.

```lean
public theorem IsStandardFpqcCovering.bind {T : Scheme.{u}} {I : Type v} {U : I → Scheme.{u}}
    {f : ∀ i, U i ⟶ T} (hf : IsStandardFpqcCovering U f) {J : I → Type w}
    {V : ∀ i, J i → Scheme.{u}} {g : ∀ i (j : J i), V i j ⟶ U i}
    (hg : ∀ i, IsStandardFpqcCovering (V i) (g i)) :
    IsStandardFpqcCovering (fun ij : Σ i, J i ↦ V ij.1 ij.2)
      (fun ij : Σ i, J i ↦ g ij.1 ij.2 ≫ f ij.1)
```

**`AlgebraicGeometry.IsStandardFpqcCovering.pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoveringProperties.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardCoveringProperties.lean#L161). The attribute's comment: “(3)”.

> **Stacks 03LA (3).** If `{T_i ⟶ T}_{i ∈ I}` is a standard fpqc covering and `T' ⟶ T` is a
> morphism of affine schemes, then the family of first projections `{T' ×_T T_i ⟶ T'}_{i ∈ I}` is a
> standard fpqc covering.  The index is unchanged, flatness is preserved by base change, each fibre
> product is affine because it is a fibre product of affine schemes over an affine base, Stacks
> 01JQ, and a point of `T'` lies under a point of the fibre product over any point of `T_i` with the
> same image in `T`.

```lean
public theorem IsStandardFpqcCovering.pullback {T : Scheme.{u}} {I : Type v} {U : I → Scheme.{u}}
    {f : ∀ i, U i ⟶ T} (hf : IsStandardFpqcCovering U f) {T' : Scheme.{u}} [IsAffine T']
    (g : T' ⟶ T) :
    IsStandardFpqcCovering (fun i ↦ Limits.pullback g (f i))
      (fun i ↦ Limits.pullback.fst g (f i))
```

## Tag 03LB, a lemma

[Tag 03LB](https://stacks.math.columbia.edu/tag/03LB) in the Stacks Project.

**`AlgebraicGeometry.presieve₀_mem_fpqcPrecoverage_of_affine_refinements`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Characterization.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/Characterization.lean#L355). References: SGA 3 IV (6.3.1), “(i) fpqc, sufficiency”.

> A flat family which admits a standard fpqc refinement after every affine base change
> is an fpqc covering.

```lean
public lemma presieve₀_mem_fpqcPrecoverage_of_affine_refinements
    {T : Scheme.{u}} (U : PreZeroHypercover.{v} T)
    (hflat : ∀ i, Flat (U.f i))
    (hrefine : ∀ {Z : Scheme.{u}} [IsAffine Z] (h : Z ⟶ T),
      ∃ (V : Z.AffineCover.{0} @Flat), Finite V.I₀ ∧
        Nonempty (V.cover.toPreZeroHypercover.Hom (U.pullback₂ h))) :
    U.presieve₀ ∈ Scheme.fpqcPrecoverage T
```

## Tag 022G, a definition

[Tag 022G](https://stacks.math.columbia.edu/tag/022G) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Presieve.IsSheafFor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presieve.IsSheafFor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L58) (StacksFrontier): “(1) the sheaf property for a family: more general, for any presieve, here Presieve.ofArrows of the family”. References: EGA 0 (3.1.2), “(F)”; SGA 3 IV (4.3.1), “partial”; SGA 3 IV (4.3.18), “partial”; SGA 4 II (2.1), “partial”; SGA 4½ Arcata (1.2.3); SGA 4½ Arcata (1.6.3), “partial”.
- [`CategoryTheory.Presieve.isSheafFor_arrows_iff_pullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presieve.isSheafFor_arrows_iff_pullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L61) (StacksFrontier): “(1) the same, in the form of the tex: elements agreeing on the U\_i ×\_T U\_j glue uniquely”.
- [`AlgebraicGeometry.Scheme.fpqcTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.fpqcTopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L64) (StacksFrontier): “(2) the fpqc topology on schemes”. References: SGA 3 IV (4.7); SGA 3 IV (6.3); SGA 4 VII (4.2); SGA 4 XVII (0.10), “fpqc topology on Sch”.
- [`CategoryTheory.Presieve.IsSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presieve.IsSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L66) (StacksFrontier): “(2) the sheaf property for a topology: more general, here the fpqc topology”. References: EGA 0 (3.1.2), “Set-valued coefficients”; SGA 3 IV (4.3.1); SGA 3 IV (4.3.18); SGA 4 II (2.1); SGA 4 II (2.7); SGA 4 II (6.1), “special case”; SGA 4½ Arcata (1.2.3); SGA 4½ Arcata (1.6.3).
- [`CategoryTheory.Precoverage.isSheaf_toGrothendieck_iff_of_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Precoverage.isSheaf_toGrothendieck_iff_of_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L68) (StacksFrontier): “(2) the same as the sheaf property for every fpqc covering: more general, for any precoverage stable under base change, here the fpqc precoverage”.

## Tag 022H, a lemma

[Tag 022H](https://stacks.math.columbia.edu/tag/022H) in the Stacks Project.

**`AlgebraicGeometry.isSheaf_fpqcTopology_iff_and_standardCovering_iff_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardSheafCondition.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/StandardSheafCondition.lean#L176). The attribute's comment: “both statements of the lemma: the fpqc sheaf condition is equivalent to (1) ∧ (2), and under (1), (2) is equivalent to (2')”. References: SGA 3 XI (3.4), “special case”.

> **Stacks 022H.** A presheaf of sets `F` on the category of schemes satisfies the sheaf
> property for the fpqc topology if and only if it satisfies
> (1) the sheaf property for every Zariski covering, that is, every jointly surjective family of
> open immersions, and
> (2) the sheaf property for every standard fpqc covering, that is, every finite jointly surjective
> family of flat morphisms with affine sources over an affine base.
> Moreover, in the presence of (1), property (2) is equivalent to
> (2') the sheaf property for `{V ⟶ U}` with `V` and `U` affine and `V ⟶ U` faithfully flat.

```lean
public theorem isSheaf_fpqcTopology_iff_and_standardCovering_iff_faithfullyFlat
    (F : Scheme.{u}ᵒᵖ ⥤ Type v) :
    (Presieve.IsSheaf Scheme.fpqcTopology.{u} F ↔
      (∀ {T : Scheme.{u}} (R : Presieve T), R ∈ Scheme.zariskiPrecoverage T →
          Presieve.IsSheafFor F R) ∧
        ∀ {T : Scheme.{u}} [IsAffine T] (𝒱 : T.AffineCover.{w} (@Flat.{u})), Finite 𝒱.I₀ →
          Presieve.IsSheafFor F 𝒱.cover.presieve₀) ∧
    ((∀ {T : Scheme.{u}} (R : Presieve T), R ∈ Scheme.zariskiPrecoverage T →
        Presieve.IsSheafFor F R) →
      ((∀ {T : Scheme.{u}} [IsAffine T] (𝒱 : T.AffineCover.{w} (@Flat.{u})), Finite 𝒱.I₀ →
          Presieve.IsSheafFor F 𝒱.cover.presieve₀) ↔
        ∀ {V U : Scheme.{u}} [IsAffine V] [IsAffine U] (g : V ⟶ U), Flat g → Surjective g →
          Presieve.IsSheafFor F (Presieve.singleton g)))
```

## Tag 0BBK, a lemma

[Tag 0BBK](https://stacks.math.columbia.edu/tag/0BBK) in the Stacks Project.

**`AlgebraicGeometry.exists_fpqcCover_not_refined_by_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/NoCofinalSet.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fpqc/NoCofinalSet.lean#L170).

> No small family of fpqc coverings of the spectrum of a nonzero ring is cofinal under
> refinement.

```lean
public theorem exists_fpqcCover_not_refined_by_family
    (R : Type u) [CommRing R] [Nontrivial R]
    (A : Type u)
    (U : A → Scheme.fpqcPrecoverage.ZeroHypercover.{u} (Spec (.of R))) :
    ∃ V : Scheme.fpqcPrecoverage.ZeroHypercover.{u} (Spec (.of R)),
      ∀ a : A, ¬ Nonempty ((U a).toPreZeroHypercover.Hom V.toPreZeroHypercover)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.9, Tag 022A](https://stacks.math.columbia.edu/tag/022A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
