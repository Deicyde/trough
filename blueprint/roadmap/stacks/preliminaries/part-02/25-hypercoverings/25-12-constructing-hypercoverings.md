---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.split_iff_components_of_epi, Stacks.CategoryTheory.Hypercovering.components_of_epi_iff_components_of_degeneracy, Stacks.CategoryTheory.Hypercovering.truncated_split_iff_components_of_epi, Stacks.CategoryTheory.Hypercovering.truncated_components_of_epi_iff_components_of_degeneracy, Stacks.CategoryTheory.Hypercovering.exists_hypercovering_with_objects_in, Stacks.CategoryTheory.Hypercovering.exists_hypercoveringOfTerminal_with_objects_in, Stacks.CategoryTheory.Hypercovering.exists_hypercovering_of_map, Stacks.Topology.LocallyQuasiCompactQcSite.isHypercovering_map_smallSite
statement: formalized
proof: formalized
---

# 25.12 Constructing hypercoverings

Section 25.12 of the Stacks Project, [Tag 094J](https://stacks.math.columbia.edu/tag/094J). 9 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DAU, a lemma

[Tag 0DAU](https://stacks.math.columbia.edu/tag/0DAU) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.split_iff_components_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean, line 850](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean#L850). The attribute's comment: “simplicial: (1) iff (2)”.

> **Stacks Project, Tag 0DAU, parts (1) and (2).** A simplicial formal
> coproduct is split iff each component map over a surjective simplicial
> operator is an isomorphism.

```lean
theorem split_iff_components_of_epi
    (K : SimplicialObject (FormalCoproduct.{w} C)) :
    Nonempty K.Splitting ↔
      ∀ {m n : SimplexCategory} (φ : m ⟶ n) [Epi φ]
        (i : (K.obj (op n)).I),
        IsIso ((K.map φ.op).φ i)
```

**`Stacks.CategoryTheory.Hypercovering.components_of_epi_iff_components_of_degeneracy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean, line 864](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean#L864). The attribute's comment: “simplicial: (2) iff (3)”.

> **Stacks Project, Tag 0DAU, parts (2) and (3).** It suffices to test the
> elementary degeneracies of a simplicial formal coproduct.

```lean
theorem components_of_epi_iff_components_of_degeneracy
    (K : SimplicialObject (FormalCoproduct.{w} C)) :
    (∀ {m n : SimplexCategory} (φ : m ⟶ n) [Epi φ]
      (i : (K.obj (op n)).I), IsIso ((K.map φ.op).φ i)) ↔
    (∀ (n : ℕ) (j : Fin (n + 1))
      (i : (K.obj (op (SimplexCategory.mk n))).I),
      IsIso ((K.map (SimplexCategory.σ j).op).φ i))
```

**`Stacks.CategoryTheory.Hypercovering.truncated_split_iff_components_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean, line 895](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean#L895). The attribute's comment: “truncated: (1) iff (2)”.

> **Stacks Project, Tag 0DAU, truncated parts (1) and (2).**

```lean
theorem truncated_split_iff_components_of_epi (r : ℕ)
    (K : SimplicialObject.Truncated (FormalCoproduct.{w} C) r) :
    IsTruncatedSplit r K ↔
      ∀ {m n : SimplexCategory.Truncated r} (φ : m ⟶ n) [Epi φ]
        (i : (K.obj (op n)).I),
        IsIso ((K.map φ.op).φ i)
```

**`Stacks.CategoryTheory.Hypercovering.truncated_components_of_epi_iff_components_of_degeneracy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean, line 918](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Split.lean#L918). The attribute's comment: “truncated: (2) iff (3)”.

> **Stacks Project, Tag 0DAU, truncated parts (2) and (3).**

```lean
theorem truncated_components_of_epi_iff_components_of_degeneracy (r : ℕ)
    (K : SimplicialObject.Truncated (FormalCoproduct.{w} C) r) :
    (∀ {m n : SimplexCategory.Truncated r} (φ : m ⟶ n) [Epi φ]
      (i : (K.obj (op n)).I), IsIso ((K.map φ.op).φ i)) ↔
    (∀ (n : ℕ) (hn : n + 1 ≤ r) (j : Fin (n + 1))
      (i : (K.obj (op (⟨SimplexCategory.mk n, Nat.le_of_succ_le hn⟩ :
        SimplexCategory.Truncated r))).I),
      IsIso ((K.map (ObjectProperty.homMk (SimplexCategory.σ j) :
        (⟨SimplexCategory.mk (n + 1), hn⟩ : SimplexCategory.Truncated r) ⟶
        (⟨SimplexCategory.mk n, Nat.le_of_succ_le hn⟩ :
          SimplexCategory.Truncated r)).op).φ i))
```

## Tag 0DAV, a lemma

[Tag 0DAV](https://stacks.math.columbia.edu/tag/0DAV) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercovering_with_objects_in`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/ObjectsInCollection.lean, line 1156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/ObjectsInCollection.lean#L1156).

> **Stacks Project, Tag 0DAV.** If the objects in `B` cover every object of a site and adjoining
> one more morphism whose source lies in `B` preserves such a covering, then every object has a
> hypercovering all of whose constituent objects lie in `B`.

```lean
theorem exists_hypercovering_with_objects_in
    (J : Pretopology C) (B : Set C)
    (hcover : ∀ U : C, ∃ (ι : Type w) (V : ι → C) (f : ∀ i, V i ⟶ U),
      (∀ i, V i ∈ B) ∧ Presieve.ofArrows V f ∈ J U)
    (hadjoin : ∀ {ι : Type w} (V : ι → C) {U : C} (f : ∀ i, V i ⟶ U),
      (∀ i, V i ∈ B) → Presieve.ofArrows V f ∈ J U →
      ∀ {U' : C}, U' ∈ B → ∀ g : U' ⟶ U,
        (fun {_} h ↦ Presieve.ofArrows V f h ∨ Presieve.singleton g h) ∈ J U)
    (X : C) :
    ∃ K : SimplicialObject (FormalCoproduct.{w} (Over X)),
      IsHypercovering J K ∧
        ∀ (n : ℕ) (i : (K.obj (op (SimplexCategory.mk n))).I),
          ((K.obj (op (SimplexCategory.mk n))).obj i).left ∈ B
```

## Tag 0DAX, a lemma

[Tag 0DAX](https://stacks.math.columbia.edu/tag/0DAX) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercoveringOfTerminal_with_objects_in`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/PresheafObjects/Existence.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/PresheafObjects/Existence.lean#L29).

> **Stacks Project, Tag 0DAX.** A covering collection of objects supplies a hypercovering of
> the final presheaf all of whose terms are coproducts of objects in that collection.

```lean
theorem exists_hypercoveringOfTerminal_with_objects_in
    (J : Pretopology C) (B : Set C)
    (hcover : ∀ U : C, ∃ (ι : Type (max w u v)) (V : ι → C) (f : ∀ i, V i ⟶ U),
      (∀ i, V i ∈ B) ∧ Presieve.ofArrows V f ∈ J U) :
    ∃ K : HypercoveringOfTerminal.{max w u v} J,
      ∀ (n : ℕ) (i : (K.toSimplicialObject.obj (op (SimplexCategory.mk n))).I),
        (K.toSimplicialObject.obj (op (SimplexCategory.mk n))).obj i ∈ B
```

## Tag 0DAY, a lemma

[Tag 0DAY](https://stacks.math.columbia.edu/tag/0DAY) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercovering_of_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismOfSites.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/MorphismOfSites.lean#L585).

> The underlying functor of a morphism of sites which preserves equalizers and pullbacks
> carries a hypercovering to a hypercovering.

```lean
lemma exists_hypercovering_of_map
    [HasEqualizers C] [HasPullbacks C] [HasEqualizers D] [HasPullbacks D]
    (J : Pretopology C) (K : Pretopology D) (u : D ⥤ C)
    [IsMorphismOfSites.{max w vC vD uC uD} u K.toGrothendieck J.toGrothendieck]
    [PreservesLimitsOfShape WalkingParallelPair u]
    [PreservesLimitsOfShape WalkingCospan u]
    (X : HypercoveringOfTerminal.{w} K) :
    ∃ Y : HypercoveringOfTerminal.{w} J,
      Y.toSimplicialObject = X.toSimplicialObject ⋙ mapFormalCoproduct u
```

## Tag 0DAZ, a lemma

[Tag 0DAZ](https://stacks.math.columbia.edu/tag/0DAZ) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactQcSite.isHypercovering_map_smallSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean#L265). The attribute's comment: “a hypercovering of LC\_qc transported to a small model of it”.

> **Stacks 0DAZ at the comparison with the small model.** A hypercovering of an object of
> `LC_qc`, carried degreewise to the small model, is a hypercovering of the image object there.
>
> This is the transport the simplicial-hypercovering apparatus needs: that apparatus consumes a
> hypercovering of a *small* site --- `isLocallyFull_totalForget_over` and
> `essImage_of_isCartesianSheaf` take an `IsHypercovering` --- and `LC_qc` is not one. The
> comparison functor preserves fibre products, being an equivalence, and takes coverings to
> coverings by `mapsCoveringsToCoverings_smallEquivalence`, which are exactly the two hypotheses
> of Stacks 0DAZ.

```lean
theorem isHypercovering_map_smallSite {Y : S.category}
    (K : SimplicialObject (FormalCoproduct.{t₁} (Over Y)))
    (hK : IsHypercovering S.pretopology K) :
    IsHypercovering S.smallPretopology
      (K ⋙ mapFormalCoproduct.{t₁} (Over.post S.smallEquivalence.functor))
```

**`Stacks.CategoryTheory.Hypercovering.IsHypercovering.map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Map.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Map.lean#L467). The attribute's comment: “the hypothesis that `u` be continuous is used only through its covering clause `MapsCoveringsToCoverings`, which is Tag 00WV(1) verbatim — the same index type and the same image family — together with the preservation of fibre products that is Tag 00WV(2); the conclusion is the full statement, both the degree-zero clause and the clause in degree n + 1”.

> **Stacks Project, Tag 0DAZ.** Let `u : D ⥤ C` be a functor between sites given by
> pretopologies which takes covering families to covering families and preserves fibre products.
> Then the degreewise image under `u` of a hypercovering of `Y : D` is a hypercovering of `u Y`.

```lean
theorem IsHypercovering.map (JD : Pretopology D) (JC : Pretopology C) (u : D ⥤ C)
    (hu : MapsCoveringsToCoverings.{w} u JD JC) [PreservesLimitsOfShape WalkingCospan u] {Y : D}
    (K : SimplicialObject (FormalCoproduct.{w} (Over Y)))
    (hK : IsHypercovering JD K) :
    IsHypercovering JC (K ⋙ mapFormalCoproduct.{w} (Over.post u))
```

## Tag 094K, a lemma

[Tag 094K](https://stacks.math.columbia.edu/tag/094K) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_finite_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/FiniteConstruction.lean, line 890](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/FiniteConstruction.lean#L890).

> **Stacks Project, Tag 094K.** If a class `B` supplies finite coverings and every such
> covering remains covering after adjoining one further arrow from an object of `B`, then every
> object has a hypercovering whose family in every degree is finite and consists of objects of
> `B`.

```lean
theorem exists_finite_hypercovering
    {C : Type u} [Category.{v} C] [HasPullbacks C] (J : Pretopology C) (B : Set C)
    (exists_finite_cover : ∀ X : C,
      ∃ (I : Type w) (U : I → C) (f : ∀ i, U i ⟶ X),
        Finite I ∧ (∀ i, B (U i)) ∧ Presieve.ofArrows U f ∈ J X)
    (cover_of_adjoin : ∀ {X : C} {I : Type w} (U : I → C) (f : ∀ i, U i ⟶ X),
      Finite I → (∀ i, B (U i)) → Presieve.ofArrows U f ∈ J X →
      ∀ (V : C) (g : V ⟶ X), B V →
        Presieve.ofArrows
          (fun i : Sum I PUnit ↦ match i with | Sum.inl i => U i | Sum.inr _ => V)
          (fun i : Sum I PUnit ↦ match i with | Sum.inl i => f i | Sum.inr _ => g) ∈ J X) :
    ∀ X : C, ∃ K : SimplicialObject (FormalCoproduct.{w} (Over X)),
      IsHypercovering J K ∧
        ∀ n : ℕ, Finite (K.obj (Opposite.op ⦋n⦌)).I ∧
          ∀ i, B ((K.obj (Opposite.op ⦋n⦌)).obj i).left
```

## Tag 0DB0, a remark

[Tag 0DB0](https://stacks.math.columbia.edu/tag/0DB0) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.Sigma.map'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.Sigma.map'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch25.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch25.lean#L22) (StacksFrontier): “the induced map ∐ U\_i ⟶ ∐ V\_j from α : I → J and f\_i : U\_i ⟶ V\_\{α i}”.
- [`CategoryTheory.Limits.Sigma.ι_comp_map'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.Sigma.ι_comp_map'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch25.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch25.lean#L24) (StacksFrontier): “it sends the summand U\_i into V\_\{α i} via f\_i”.

## Tag 0DB1, a remark

[Tag 0DB1](https://stacks.math.columbia.edu/tag/0DB1) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.degreewiseUnions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DegreewiseUnions.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DegreewiseUnions.lean#L311). The attribute's comment: “the simplicial object of degreewise disjoint unions”.

> Take disjoint unions in each degree of a simplicial semi-representable object.  Only the
> coproducts of the objects actually occurring are required to exist.

```lean
noncomputable def degreewiseUnions (K : SimplicialObject (FormalCoproduct.{w} C))
    (hsum : ∀ n, HasCoproduct (K.obj n).obj) : SimplicialObject (FormalCoproduct.{w} C)
```

**`Stacks.CategoryTheory.Hypercovering.hypercoveringDegreewiseUnions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DegreewiseUnions.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DegreewiseUnions.lean#L443). The attribute's comment: “the degreewise disjoint unions again form a hypercovering”.

> **Stacks Project, Tag 0DB1.** Let `K` be a hypercovering on a site with fibre products and
> equalizers.  If the coproduct of the objects in each degree of `K` exists and the map from the
> coproduct of their representable presheaves to the presheaf represented by that coproduct
> becomes an isomorphism after sheafification, then the degreewise disjoint unions again form a
> hypercovering.

```lean
noncomputable def hypercoveringDegreewiseUnions (K : HypercoveringOfTerminal.{w} J)
    (hsum : ∀ n, HasCoproduct (K.toSimplicialObject.obj n).obj)
    (hinj : ∀ n, Presheaf.IsLocallyInjective J.toGrothendieck
      ((associatedPresheafFunctor.{v}).map
        ((toDegreewiseUnions K.toSimplicialObject hsum).app n)))
    (hsurj : ∀ n, Presheaf.IsLocallySurjective J.toGrothendieck
      ((associatedPresheafFunctor.{v}).map
        ((toDegreewiseUnions K.toSimplicialObject hsum).app n))) :
    HypercoveringOfTerminal.{w} J
```

## Tag 0DB2, a remark

[Tag 0DB2](https://stacks.math.columbia.edu/tag/0DB2) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.takeUnionsSimplicial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DisjointUnions.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DisjointUnions.lean#L95). The attribute's comment: “the degreewise construction”.

> Take the disjoint unions in each degree of a simplicial formal coproduct over `X`.
> Only the coproducts of its actual terms are required to exist.

```lean
noncomputable def takeUnionsSimplicial
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hsum : ∀ n, HasCoproduct (K.obj n).obj) :
    SimplicialObject (FormalCoproduct.{w} (Over X))
```

**`Stacks.CategoryTheory.Hypercovering.isHypercovering_takeUnionsSimplicial`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DisjointUnions.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/DisjointUnions.lean#L226). The attribute's comment: “preservation of hypercoverings”.

> If summable semi-representable objects over `X` are closed
> under finite limits, taking their coproducts commutes with those limits, and it sends coverings
> to coverings, then applying it degreewise to a hypercovering again gives a hypercovering.

```lean
lemma isHypercovering_takeUnionsSimplicial
    [ObjectProperty.IsClosedUnderFiniteLimits
      (fun U : FormalCoproduct.{w} (Over X) ↦ HasCoproduct U.obj)]
    [PreservesFiniteLimits (takeUnions.{w, v, max u v} (C := Over X))]
    (hcover : ∀ ⦃U V : SummableFormalCoproduct.{w} (Over X)⦄ (f : U ⟶ V),
      IsCoveringOver J ((summableInclusion (C := Over X)).map f) →
        IsCoveringOver J ((takeUnions (C := Over X)).map f))
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hsum : ∀ n, HasCoproduct (K.obj n).obj)
    (hK : IsHypercovering J K) :
    IsHypercovering J (takeUnionsSimplicial K hsum)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.12, Tag 094J](https://stacks.math.columbia.edu/tag/094J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
