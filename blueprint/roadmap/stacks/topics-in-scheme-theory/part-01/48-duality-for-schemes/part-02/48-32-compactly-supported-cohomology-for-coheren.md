---
declaration: section
origin: cited
lean: AlgebraicGeometry.lowerShriekIso, CategoryTheory.Compactification.shriekImageIso, CategoryTheory.CompactificationData.shriekImageIso, AlgebraicGeometry.lowerShriekHomIso, AlgebraicGeometry.exists_shriekImage_distTriang_system, CategoryTheory.Pro.exists_diagonalRepresentation, CategoryTheory.Pro.diagonalRepresentation_uniqueUpToIso, CategoryTheory.Pro.exists_compositionRepresentation
statement: formalized
proof: formalized
---

# 48.32 Compactly supported cohomology for coherent modules

Section 48.32 of the Stacks Project, [Tag 0G4Z](https://stacks.math.columbia.edu/tag/0G4Z). 9 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G50, a lemma

[Tag 0G50](https://stacks.math.columbia.edu/tag/0G50) in the Stacks Project.

**`AlgebraicGeometry.lowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompactificationShriek.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompactificationShriek.lean#L388).

> **Stacks Project, Tag 0G50.** In Situation [Stacks, Tag 0F42] let `f : X ⟶ Y` be a morphism
> of `FTS_S`. The functor `Rf_! = Rf̄_* ∘ Rj_!` of [Stacks, Section 0G4Z]
> (`AlgebraicGeometry.lowerShriek`) is, up to isomorphism, independent of the choice of the
> compactification `j : X ⟶ X̄` of `X` over `Y`.
>
> The proof is the source's. Two compactifications `X̄₁`, `X̄₂` are dominated by a third, the
> scheme-theoretic closure `X̄₃` of `X` in `X̄₁ ×_Y X̄₂`
> (the closure of `AlgebraicGeometry.compactificationPairMap`; that `X ⟶ X̄₃` is an open immersion is
> because `X ⟶ X̄₁ ×_Y X̄₂` is a quasi-compact immersion), which is cofilteredness of the category of
> compactifications for these two objects; and a morphism `g : X̄₃ ⟶ X̄ᵢ` of compactifications gives
> `Rf̄ᵢ_* ∘ Rjᵢ_! ≅ Rf̄ᵢ_* ∘ Rg_* ∘ Rj₃_! ≅ Rf̄₃_* ∘ Rj₃_!` by [Stacks, Tag 0G4X]
> (`AlgebraicGeometry.lowerShriekIsoOfFactor`).

```lean
public def lowerShriekIso : lowerShriek f c₁ ≅ lowerShriek f c₂
```

**`CategoryTheory.Compactification.shriekImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Independence.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Independence.lean#L120). The attribute's comment: “the per-compactification data, the cofilteredness of the category of compactifications, and the isomorphisms attached to its morphisms by Tag 0G4X, supplied as data”.

> **Stacks Project, Tag 0G50.** The functor `Rf_!` is, up to isomorphism, independent of the
> choice of the compactification.
>
> The compactifications of `X` over `Y` are the objects of a cofiltered category `𝒦`, each carrying
> the data of a `CategoryTheory.Compactification`, and each morphism of `𝒦` induces an isomorphism
> of the attached functors `Rf_!` — the isomorphism of [Stacks, Tag 0G4X], produced by
> `CategoryTheory.Compactification.shriekImageIsoOfMorphism`. Any two compactifications are then
> dominated by a third, and the two isomorphisms to it compose to one between them.

```lean
public def shriekImageIso {𝒦 : Type w₁} [Category.{w₂} 𝒦] [IsCofiltered 𝒦] {ℳ : 𝒦 → Type u₃}
    [∀ c, Category.{v} (ℳ c)] (C : ∀ c, Compactification 𝒞 𝒟 (ℳ c))
    (e : ∀ {c c' : 𝒦}, (c ⟶ c') → ((C c').shriekImage ≅ (C c).shriekImage)) (c c' : 𝒦) :
    (C c).shriekImage ≅ (C c').shriekImage
```

**`CategoryTheory.CompactificationData.shriekImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/IndependenceLan.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/IndependenceLan.lean#L51). The attribute's comment: “the per-compactification data, the cofilteredness of the category of compactifications, and the isomorphisms attached to its morphisms by Tag 0G4X, supplied as data”.

> The functor `Rf_!` is, up to isomorphism, independent of the choice of the compactification.
>
> The compactifications of `X` over `Y` are the objects of a cofiltered category `𝒦`, each carrying
> the data of a `CategoryTheory.CompactificationData`, and each morphism of `𝒦` induces an
> isomorphism of the attached functors `Rf_!`, that of Stacks, Tag 0G4X. The isomorphism between the
> functors of `c` and `c'` is the composite of the isomorphisms to the functor of a compactification
> dominating both.

```lean
public def shriekImageIso {𝒦 : Type w₁} [Category.{w₂} 𝒦] [IsCofiltered 𝒦] {ℳ : 𝒦 → Type u₃}
    [∀ c, Category.{v} (ℳ c)] (C : ∀ c, CompactificationData 𝒞 𝒟 (ℳ c))
    [∀ c (A : ℳ c ⥤ Type v), (C c).direct.HasLeftKanExtension A]
    (e : ∀ {c c' : 𝒦}, (c ⟶ c') → ((C c').shriekImage ≅ (C c).shriekImage)) (c c' : 𝒦) :
    (C c).shriekImage ≅ (C c').shriekImage
```

## Tag 0G51, a proposition

[Tag 0G51](https://stacks.math.columbia.edu/tag/0G51) in the Stacks Project.

**`AlgebraicGeometry.lowerShriekHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekAdjunction.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekAdjunction.lean#L443).

> In Situation [Stacks, Tag 0F42] let `f : X ⟶ Y` be a morphism of `FTS_S`. Then `Rf_!` and
> `f^!` are adjoint in the following sense: for `K` in `D^b_{Coh}(𝒪_X)` and `L` in
> `D^+_{Coh}(𝒪_Y)`
>
> `Hom_X(K, f^! L) = Hom_{Pro-D^+_{Coh}(𝒪_Y)}(Rf_! K, L)`,
>
> bifunctorially in `K` and `L`: an isomorphism of functors
> `D^b_{Coh}(𝒪_X)ᵒᵖ ⥤ D^+_{Coh}(𝒪_Y) ⥤ Type`, with components
> `AlgebraicGeometry.lowerShriekHomEquiv`. Here `Rf_!` and `f^!` are computed at an arbitrary
> compactification `c` of `X` over `Y`, `Rf_! K` is viewed in `Pro-D^+_{Coh}(𝒪_Y)` through
> `D^b_{Coh} ⊆ D^+_{Coh}`, and `f^! L` is read at the standard model of `D(𝒪_X)`
> (`Stacks.Duality.UpperShriekDuality.upperShriekStd`).

```lean
def lowerShriekHomIso :
    (lowerShriek f c ⋙ ProSeq.map (boundedCoherentToPlusCoh Y₁.left)).op ⋙ coyoneda ⋙
        (Functor.whiskeringLeft _ _ _).obj ProSeq.const ≅
      (boundedCoherentDerived X₁.left).ι.op ⋙ coyoneda ⋙
        (Functor.whiskeringLeft _ _ _).obj (upperShriekStd f c)
```

## Tag 0G52, a lemma

[Tag 0G52](https://stacks.math.columbia.edu/tag/0G52) in the Stacks Project.

**`AlgebraicGeometry.exists_shriekImage_distTriang_system`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/ShriekTrianglesData.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/ShriekTrianglesData.lean#L390).

> In Situation [Stacks, Tag 0F42] let `f : X ⟶ Y` be a morphism of `FTS_S` and let
>
> `K ⟶ L ⟶ M ⟶ K[1]`
>
> be a distinguished triangle of `D^b_{Coh}(𝒪_X)`. Then there is an inverse system of distinguished
> triangles
>
> `K_n ⟶ L_n ⟶ M_n ⟶ K_n[1]`
>
> of `D^b_{Coh}(𝒪_Y)` such that the pro-systems `(K_n)`, `(L_n)` and `(M_n)` give `Rf_! K`,
> `Rf_! L` and `Rf_! M`.
>
> Here `Rf_! = Rf̄_* ∘ Rj_!` is `AlgebraicGeometry.lowerShriek f c`, the functor of
> [Stacks, Section 0G4Z] attached to a compactification `c`, `j : X ⟶ X̄`, of `X` over `Y` with
> structure morphism `f̄ : X̄ ⟶ Y`: `Rj_!` is the extension by zero of [Stacks, Tag 0G4N] and `Rf̄_*`
> is the derived direct image `D^b_{Coh}(𝒪_{X̄}) ⥤ D^b_{Coh}(𝒪_Y)`, applied termwise to
> pro-objects. The statement holds for every compactification; by [Stacks, Tag 0G50] the functor
> does not depend on it.
>
> The proof is the source's. [Stacks, Tag 0G4M] for `j`
> (`AlgebraicGeometry.DeligneTriangle.exists_extensionByZero_distTriang`) gives an inverse system of
> distinguished triangles `K̄_n ⟶ L̄_n ⟶ M̄_n ⟶ K̄_n[1]` of `D^b_{Coh}(𝒪_{X̄})` whose vertex systems
> give `Rj_! K`, `Rj_! L` and `Rj_! M`; the system `K_n = Rf̄_* K̄_n`, and likewise for `L_n` and
> `M_n`, works by the very definition of `Rf_!`
> (`CategoryTheory.CompactificationData.exists_shriekImage_distTriang_system`).

```lean
public theorem exists_shriekImage_distTriang_system (f : X₁ ⟶ Y₁)
    (c : CompactificationOf (Over.mk f.left)) (T : Triangle (BoundedCoherentDerived X₁.left))
    (hT : T ∈ distTriang (BoundedCoherentDerived X₁.left)) :
    ∃ TY : ℕᵒᵖ ⥤ Triangle (BoundedCoherentDerived Y₁.left),
      (∀ n, TY.obj n ∈ distTriang (BoundedCoherentDerived Y₁.left)) ∧
      Nonempty (ProSeq.of (TY ⋙ Triangle.π₁) ≅ (lowerShriek f c).obj T.obj₁) ∧
      Nonempty (ProSeq.of (TY ⋙ Triangle.π₂) ≅ (lowerShriek f c).obj T.obj₂) ∧
      Nonempty (ProSeq.of (TY ⋙ Triangle.π₃) ≅ (lowerShriek f c).obj T.obj₃)
```

## Tag 0G53, a remark

[Tag 0G53](https://stacks.math.columbia.edu/tag/0G53) in the Stacks Project.

**`CategoryTheory.Pro.exists_diagonalRepresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/DiagonalRepresentation.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/DiagonalRepresentation.lean#L494). The attribute's comment: “diagonal\_representation”.

> **Stacks Project, Tag 0G53 (diagonal representation).** A countable inverse
> system of pro-objects, each represented by an inverse sequence, has a diagonal
> inverse-sequence representation.  Equivalently, naturally in `N`,
> `colim_i colim_n Hom(M_{i,n}, N)` is `colim_k Hom(D_k, N)`.

```lean
public theorem exists_diagonalRepresentation {C : Type u} [Category.{v} C]
    (P : Functor ℕ (Functor C (Type v))) (M : ℕ → Functor ℕᵒᵖ C)
    (e : ∀ i, P.obj i ≅ Pro.coyonedaColim (liftedInverseSequence (M i))) :
    Nonempty (DiagonalRepresentation P M e)
```

**`CategoryTheory.Pro.diagonalRepresentation_uniqueUpToIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/DiagonalUniqueness.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/DiagonalUniqueness.lean#L39). The attribute's comment: “diagonal\_uniqueness”.

> The diagonal inverse sequence is uniquely pro-isomorphic to any other representation `G` of
> the same functor of points: there is a unique pro-morphism to `G` compatible with the comparison
> isomorphisms, and it has a two-sided inverse.

```lean
public theorem diagonalRepresentation_uniqueUpToIso {C : Type u} [Category.{v} C]
    (P : Functor ℕ (Functor C (Type v))) (M : ℕ → Functor ℕᵒᵖ C)
    (e : ∀ i, P.obj i ≅ Pro.coyonedaColim (liftedInverseSequence (M i)))
    (r : DiagonalRepresentation P M e) {I : Type v} [Category.{v} I]
    (G : Functor I C) (eG : colimit P ≅ Pro.coyonedaColim G) :
    ∃! φ : Pro.Hom (liftedInverseSequence r.system) G,
      (∃ ψ : Pro.Hom G (liftedInverseSequence r.system),
        (Pro.homEquiv G (liftedInverseSequence r.system)).symm ψ ≫
            (Pro.homEquiv (liftedInverseSequence r.system) G).symm φ =
          𝟙 (Pro.coyonedaColim (liftedInverseSequence r.system)) ∧
        (Pro.homEquiv (liftedInverseSequence r.system) G).symm φ ≫
            (Pro.homEquiv G (liftedInverseSequence r.system)).symm ψ =
          𝟙 (Pro.coyonedaColim G)) ∧
      eG.hom ≫ (Pro.homEquiv (liftedInverseSequence r.system) G).symm φ =
        r.comparison.hom
```

## Tag 0G54, a remark

[Tag 0G54](https://stacks.math.columbia.edu/tag/0G54) in the Stacks Project.

**`CategoryTheory.Pro.exists_compositionRepresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Composition.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Composition.lean#L66). The attribute's comment: “the composition, for pro-object-valued functors with countable-index representations supplied as data”.

> The composition of two compactly supported direct images: the termwise image under `G` of an
> inverse sequence `M` is represented by an inverse sequence in the target category.

```lean
public theorem exists_compositionRepresentation {C : Type u'} [Category.{v'} C] {D : Type u}
    [Category.{v} D] (G : Cᵒᵖ ⥤ D ⥤ Type v) (S : C → ℕᵒᵖ ⥤ D)
    (e : ∀ L : C, G.obj (op L) ≅ Pro.coyonedaColim (liftedInverseSequence (S L)))
    (M : ℕᵒᵖ ⥤ C) : Nonempty (CompositionRepresentation G M)
```

**`CategoryTheory.Pro.CompositionRepresentation.homColimitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Composition.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Composition.lean#L78). The attribute's comment: “the Hom-colimit formula, for pro-object-valued functors with countable-index representations supplied as data”.

> **Stacks Project, Tag 0G54**, the displayed formula: for every object `L`, the colimit over
> `n` of `Hom(G (M n), L)` is the colimit over `k` of `Hom(system_k, L)`.

```lean
public noncomputable def CompositionRepresentation.homColimitIso {C : Type u'} [Category.{v'} C]
    {D : Type u} [Category.{v} D] {G : Cᵒᵖ ⥤ D ⥤ Type v} {M : ℕᵒᵖ ⥤ C}
    (r : CompositionRepresentation G M) (L : D) :
    colimit ((M.rightOp ⋙ G) ⋙ (evaluation D (Type v)).obj L) ≅
      colimit ((liftedInverseSequence r.system).op ⋙ coyoneda ⋙
        (evaluation D (Type v)).obj L)
```

**`CategoryTheory.Pro.compositionRepresentation_uniqueUpToIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Composition.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/Composition.lean#L92). The attribute's comment: “uniqueness up to pro-isomorphism, for pro-object-valued functors with countable-index representations supplied as data”.

> **Stacks Project, Tag 0G54**, uniqueness: two inverse sequences representing the termwise
> image of `M` under `G` are uniquely pro-isomorphic over their comparison isomorphisms. The
> pro-morphism and its inverse are expressed through Stacks 0G2X.

```lean
public theorem compositionRepresentation_uniqueUpToIso {C : Type u'} [Category.{v'} C]
    {D : Type u} [Category.{v} D] (G : Cᵒᵖ ⥤ D ⥤ Type v) (M : ℕᵒᵖ ⥤ C)
    (r r' : CompositionRepresentation G M) :
    ∃! φ : Pro.Hom (liftedInverseSequence r.system) (liftedInverseSequence r'.system),
      (∃ ψ : Pro.Hom (liftedInverseSequence r'.system) (liftedInverseSequence r.system),
        (Pro.homEquiv (liftedInverseSequence r'.system)
              (liftedInverseSequence r.system)).symm ψ ≫
            (Pro.homEquiv (liftedInverseSequence r.system)
              (liftedInverseSequence r'.system)).symm φ =
          𝟙 (Pro.coyonedaColim (liftedInverseSequence r.system)) ∧
        (Pro.homEquiv (liftedInverseSequence r.system)
              (liftedInverseSequence r'.system)).symm φ ≫
            (Pro.homEquiv (liftedInverseSequence r'.system)
              (liftedInverseSequence r.system)).symm ψ =
          𝟙 (Pro.coyonedaColim (liftedInverseSequence r'.system))) ∧
      r'.comparison.hom ≫ (Pro.homEquiv (liftedInverseSequence r.system)
          (liftedInverseSequence r'.system)).symm φ = r.comparison.hom
```

**`AlgebraicGeometry.lowerShriekComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean#L216). The attribute's comment: “the definition of Rg\_! Rf\_! K”.

> **Stacks Project, Tag 0G54**, the definition. In Situation [Stacks, Tag 0F42] let
> `f : X ⟶ Y` and `g : Y ⟶ Z` be composable morphisms of `FTS_S`, with compactifications `cf` of `X`
> over `Y` and `cg` of `Y` over `Z` defining `Rf_!` and `Rg_!` ([Stacks, Section 0G4Z],
> `AlgebraicGeometry.lowerShriek`). For `K` in `D^b_{Coh}(𝒪_X)`, `Rf_! K` is given by an inverse
> system `(M_n)` of `D^b_{Coh}(𝒪_Y)` (`AlgebraicGeometry.lowerShriekObjIso`), `(Rg_! M_n)` is an
> inverse system of `Pro-D^b_{Coh}(𝒪_Z)`, and `Rg_! Rf_! K` is the pro-object of `D^b_{Coh}(𝒪_Z)`
> given by [Stacks, Tag 0G53] with
>
> `Hom(Rg_! Rf_! K, L) = colim_n Hom(Rg_! M_n, L)`
>
> for every `L` (`AlgebraicGeometry.lowerShriekCompPointsIso`); it is unique up to pro-isomorphism
> (`AlgebraicGeometry.nonempty_iso_lowerShriekComp_iff`) and does not depend on the inverse system
> `(M_n)` chosen. Functoriality in `K` is omitted, as in the source.

```lean
public noncomputable def lowerShriekComp (f : X ⟶ Y) (g : Y ⟶ Z)
    (cf : CompactificationOf (Over.mk f.left)) (cg : CompactificationOf (Over.mk g.left))
    (K : BoundedCoherentDerived X.left) : ProSeq (BoundedCoherentDerived Z.left)
```

**`AlgebraicGeometry.lowerShriekCompPointsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean#L229). The attribute's comment: “Hom(Rg\_! Rf\_! K, L) = colim\_n Hom(Rg\_! M\_n, L) for every inverse system (M\_n) giving Rf\_! K”.

> **Stacks Project, Tag 0G54**, the defining property: for every inverse system `(M_n)` of
> `D^b_{Coh}(𝒪_Y)` giving `Rf_! K`,
>
> `Hom(Rg_! Rf_! K, L) = colim_n Hom(Rg_! M_n, L)`
>
> naturally in `L` in `D^b_{Coh}(𝒪_Z)`.

```lean
public noncomputable def lowerShriekCompPointsIso (f : X ⟶ Y) (g : Y ⟶ Z)
    (cf : CompactificationOf (Over.mk f.left)) (cg : CompactificationOf (Over.mk g.left))
    (K : BoundedCoherentDerived X.left) {M : ℕᵒᵖ ⥤ BoundedCoherentDerived Y.left}
    (e : ProSeq.of M ≅ (lowerShriek f cf).obj K) :
    (lowerShriekComp f g cf cg K).points ≅
      colimit (M.rightOp ⋙ ProSeq.pointsFunctor (lowerShriek g cg))
```

**`AlgebraicGeometry.lowerShriekCompHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean#L242). The attribute's comment: “Hom\_Pro(Rg\_! Rf\_! K, L) = colim\_n Hom\_Pro(Rg\_! M\_n, L)”.

> **Stacks Project, Tag 0G54**, the displayed formula with `Hom`-sets of pro-objects: for every
> inverse system `(M_n)` giving `Rf_! K` and every `L` in `D^b_{Coh}(𝒪_Z)`,
>
> `Hom_{Pro}(Rg_! Rf_! K, L) = colim_n Hom_{Pro}(Rg_! M_n, L)`.

```lean
public noncomputable def lowerShriekCompHomEquiv (f : X ⟶ Y) (g : Y ⟶ Z)
    (cf : CompactificationOf (Over.mk f.left)) (cg : CompactificationOf (Over.mk g.left))
    (K : BoundedCoherentDerived X.left) {M : ℕᵒᵖ ⥤ BoundedCoherentDerived Y.left}
    (e : ProSeq.of M ≅ (lowerShriek f cf).obj K) (L : BoundedCoherentDerived Z.left) :
    (lowerShriekComp f g cf cg K ⟶ ProSeq.const.obj L) ≃
      colimit (M.rightOp ⋙ (lowerShriek g cg).op ⋙ yoneda.obj (ProSeq.const.obj L))
```

**`AlgebraicGeometry.nonempty_iso_lowerShriekComp_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/CompositionLowerShriek.lean#L268). The attribute's comment: “uniqueness up to pro-isomorphism”.

> **Stacks Project, Tag 0G54**, uniqueness: for an inverse system `(M_n)` giving `Rf_! K`, an
> inverse system `(N_k)` of `D^b_{Coh}(𝒪_Z)` satisfies `Hom((N_k), L) = colim_n Hom(Rg_! M_n, L)`
> naturally in `L` if and only if it gives `Rg_! Rf_! K`; so `Rg_! Rf_! K` is the unique
> pro-isomorphism class with that property.

```lean
public theorem nonempty_iso_lowerShriekComp_iff (f : X ⟶ Y) (g : Y ⟶ Z)
    (cf : CompactificationOf (Over.mk f.left)) (cg : CompactificationOf (Over.mk g.left))
    (K : BoundedCoherentDerived X.left) {M : ℕᵒᵖ ⥤ BoundedCoherentDerived Y.left}
    (e : ProSeq.of M ≅ (lowerShriek f cf).obj K) (N : ℕᵒᵖ ⥤ BoundedCoherentDerived Z.left) :
    Nonempty ((ProSeq.of N).points ≅
        colimit (M.rightOp ⋙ ProSeq.pointsFunctor (lowerShriek g cg))) ↔
      Nonempty (ProSeq.of N ≅ lowerShriekComp f g cf cg K)
```

## Tag 0G55, a lemma

[Tag 0G55](https://stacks.math.columbia.edu/tag/0G55) in the Stacks Project.

**`AlgebraicGeometry.lowerShriekCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekComposition.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekComposition.lean#L260).

> **Stacks Project, Tag 0G55.** In Situation [Stacks, Tag 0F42] let `f : X ⟶ Y` and
> `g : Y ⟶ Z` be composable morphisms of `FTS_S`. With notation as in [Stacks, Tag 0G54] we have
> `Rg_! ∘ Rf_! = R(g ∘ f)_!`: for `K` in `D^b_{Coh}(𝒪_X)` the composition `Rg_! Rf_! K`
> (`AlgebraicGeometry.lowerShriekComp`) is isomorphic to `R(g ∘ f)_! K`, for arbitrary
> compactifications `cf`, `cg` and `cfg` computing `Rf_!`, `Rg_!` and `R(g ∘ f)_!`.
>
> The proof is the source's: both pro-objects have the functor of points
> `L ↦ Hom_X(K, (g ∘ f)^! L)` on `D^b_{Coh}(𝒪_Z)`, by [Stacks, Tag 0G51] for `g`, `f` and `g ∘ f`
> and `f^! ∘ g^! = (g ∘ f)^!` ([Stacks, Tag 0ATX]); a pro-object is determined by its functor of
> points ([Stacks, Tag 0G2X]).

```lean
def lowerShriekCompIso (f : X ⟶ Y) (g : Y ⟶ Z)
    (cf : CompactificationOf (Over.mk f.left)) (cg : CompactificationOf (Over.mk g.left))
    (cfg : CompactificationOf (Over.mk (f ≫ g).left)) (K : BoundedCoherentDerived X.left) :
    lowerShriekComp f g cf cg K ≅ (lowerShriek (f ≫ g) cfg).obj K
```

## Tag 0G56, a remark

[Tag 0G56](https://stacks.math.columbia.edu/tag/0G56) in the Stacks Project.

**`AlgebraicGeometry.lowerShriekOpenImmersionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovariance.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovariance.lean#L236).

> **Stacks Project, Tag 0G56.** In Situation [Stacks, Tag 0F42] let `f : X ⟶ Y` be a morphism
> of `FTS_S`, let `j : U ⟶ X` be an open immersion and `g = f ∘ j = f|_U`. Then there is a
> canonical morphism
>
> `Rg_!(K|_U) ⟶ Rf_! K`,
>
> functorial in `K` in `D^b_{Coh}(𝒪_X)`. This is the third construction of the source: for `L` in
> `D^b_{Coh}(𝒪_Y)`,
>
> `Hom(Rf\_! K, L) = Hom\_X(K, f^! L) ⟶ Hom\_U(K|\_U, (f^! L)|\_U) = Hom\_U(K|\_U, g^! L)
>   = Hom(Rg\_!(K|\_U), L)`,
>
> by [Stacks, Tag 0G51] twice and `g^! = j^* ∘ f^!` (the construction of the upper shriek
> functors, `Stacks.Duality.UpperShriekDuality.upperShriekStdPrecompOpenIso`), and the
> functoriality in `L` gives the morphism of pro-objects by [Stacks, Tag 0G2X]
> (`AlgebraicGeometry.lowerShriekMapOfHom`). `Rf_!` and `Rg_!` are computed at arbitrary
> compactifications `c` and `cU`.

```lean
def lowerShriekOpenImmersionMap (f : X ⟶ Y) (c : CompactificationOf (Over.mk f.left))
    (j : U ⟶ X) [IsOpenImmersion j.left] (cU : CompactificationOf (Over.mk (j ≫ f).left)) :
    restrictBoundedCoherentLift j.left ⋙ lowerShriek (j ≫ f) cU ⟶ lowerShriek f c
```

**`AlgebraicGeometry.lowerShriekOpenImmersionMapOfCompactification_eq_lowerShriekOpenImmersionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceAgreement.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceAgreement.lean#L430). The attribute's comment: “constructions (2) and (3) give the same arrow”.

> The agreement of constructions (2) and (3). In Situation [Stacks, Tag 0F42] let `f : X ⟶ Y`
> be a morphism of `FTS_S`, `i : U ⟶ X` an open immersion, `g = f ∘ i`, and `j : X ⟶ X̄` a
> compactification of `X` over `Y` with `f̄ : X̄ ⟶ Y`. The canonical map `Rg_!(K|_U) ⟶ Rf_! K` given
> by `Rf̄_*` applied to the map `Rj'_!(K|_U) ⟶ Rj_! K` of [Stacks, Tag 0G4Y], `j' = j ∘ i`
> (construction (2), `AlgebraicGeometry.lowerShriekOpenImmersionMapOfCompactification`), is the map
> induced by `Hom(Rf_! K, L) = Hom_X(K, f^! L) ⟶ Hom_U(K|_U, f^! L|_U)`
> `= Hom_U(K|_U, g^! L) = Hom(Rg_!(K|_U), L)` (construction (3),
> `AlgebraicGeometry.lowerShriekOpenImmersionMap`), with `Rg_!` computed at the compactification
> `j'`.

```lean
theorem lowerShriekOpenImmersionMapOfCompactification_eq_lowerShriekOpenImmersionMap (f : X ⟶ Y)
    (c : CompactificationOf (Over.mk f.left)) (i : U ⟶ X) [IsOpenImmersion i.left] :
    lowerShriekOpenImmersionMapOfCompactification f c i =
      lowerShriekOpenImmersionMap f c i (c.precompOpen i.left)
```

**`AlgebraicGeometry.lowerShriekOpenImmersionMapOfCompactification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceCompactification.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceCompactification.lean#L45). The attribute's comment: “construction (2): Rf̄\_* applied to the map Rj'\_!(K|\_U) ⟶ Rj\_! K of Tag 0G4Y”.

> **[Stacks, Tag 0G56], construction (2).** Let `f : X ⟶ Y` be a morphism of `FTS_S`,
> `i : U ⟶ X` an open immersion, `c` a compactification `j : X ⟶ X̄` of `X` over `Y` with structure
> morphism `f̄ : X̄ ⟶ Y`, and `j' = j ∘ i` the induced compactification of `U` over `Y`. With
> `Rf_! = Rf̄_* ∘ Rj_!` and `Rg_! = Rf̄_* ∘ Rj'_!` for `g = f ∘ i`, the canonical map
> `Rg_!(K|_U) ⟶ Rf_! K`, functorial in `K` in `D^b_{Coh}(𝒪_X)`, is `Rf̄_*` applied to the map
> `Rj'_!(K|_U) ⟶ Rj_! K` of [Stacks, Tag 0G4Y].

```lean
def lowerShriekOpenImmersionMapOfCompactification (f : X ⟶ Y)
    (c : CompactificationOf (Over.mk f.left)) (i : U ⟶ X) [IsOpenImmersion i.left] :
    restrictBoundedCoherentLift i.left ⋙ lowerShriek (i ≫ f) (c.precompOpen i.left) ⟶
      lowerShriek f c
```

**`AlgebraicGeometry.lowerShriekOpenImmersionMapOfComposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceComposition.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceComposition.lean#L407). The attribute's comment: “construction (1): Rf\_! applied to the map Ri\_!(K|\_U) ⟶ K of Tag 0G4Y, through Rg\_! = Rf\_! ∘ Ri\_! of Tag 0G55, functorial in K”.

> In Situation [Stacks, Tag 0F42] let `f : X ⟶ Y` be a morphism of `FTS_S`, `i : U ⟶ X` an
> open immersion and `g = f ∘ i`. The canonical map `Rg_!(K|_U) ⟶ Rf_! K`, functorial in `K` in
> `D^b_{Coh}(𝒪_X)`, obtained from `Rg_! = Rf_! ∘ Ri_!` ([Stacks, Tag 0G55]) and `Rf_!` applied to the
> map `Ri_!(K|_U) ⟶ K` of [Stacks, Tag 0G4Y] (`AlgebraicGeometry.lowerShriekOpenImmersionCompMap`),
> with `Ri_!` computed at the compactification `X` of `U` over `X` and `Rg_!` at the
> compactification restricted from the compactification `c` of `f`.

```lean
def lowerShriekOpenImmersionMapOfComposition (f : X ⟶ Y) (c : CompactificationOf (Over.mk f.left))
    (i : U ⟶ X) [IsOpenImmersion i.left] :
    restrictBoundedCoherentLift i.left ⋙ lowerShriek (i ≫ f) (c.precompOpen i.left) ⟶
      lowerShriek f c
```

**`AlgebraicGeometry.lowerShriekOpenImmersionMapOfComposition_eq_lowerShriekOpenImmersionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceComposition.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceComposition.lean#L421). The attribute's comment: “constructions (1) and (3) give the same arrow”.

> `Rf_!` applied to the map `Ri_!(K|_U) ⟶ K` of [Stacks, Tag 0G4Y] through `Rg_! = Rf_! ∘ Ri_!`
> is the map induced by
> `Hom(Rf_! K, L) = Hom_X(K, f^! L) ⟶ Hom_U(K|_U, g^! L) = Hom(Rg_!(K|_U), L)`.

```lean
theorem lowerShriekOpenImmersionMapOfComposition_eq_lowerShriekOpenImmersionMap (f : X ⟶ Y)
    (c : CompactificationOf (Over.mk f.left)) (i : U ⟶ X) [IsOpenImmersion i.left] :
    lowerShriekOpenImmersionMapOfComposition f c i =
      lowerShriekOpenImmersionMap f c i (c.precompOpen i.left)
```

**`AlgebraicGeometry.lowerShriekOpenImmersionMapOfComposition_eq_lowerShriekOpenImmersionMapOfCompactification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceComposition.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovarianceComposition.lean#L432). The attribute's comment: “constructions (1) and (2) give the same arrow”.

> `Rf_!` applied to the map `Ri_!(K|_U) ⟶ K` of [Stacks, Tag 0G4Y] through `Rg_! = Rf_! ∘ Ri_!`
> is `Rf̄_*` applied to the map `Rj'_!(K|_U) ⟶ Rj_! K` of [Stacks, Tag 0G4Y], for the
> compactification `j : X ⟶ X̄`.

```lean
theorem lowerShriekOpenImmersionMapOfComposition_eq_lowerShriekOpenImmersionMapOfCompactification
    (f : X ⟶ Y) (c : CompactificationOf (Over.mk f.left)) (i : U ⟶ X) [IsOpenImmersion i.left] :
    lowerShriekOpenImmersionMapOfComposition f c i =
      lowerShriekOpenImmersionMapOfCompactification f c i
```

## Tag 0G57, a remark

[Tag 0G57](https://stacks.math.columbia.edu/tag/0G57) in the Stacks Project.

**`AlgebraicGeometry.lowerShriekEtaleMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovariance.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekCovariance.lean#L307).

> **Stacks Project, Tag 0G57.** In Situation [Stacks, Tag 0F42] let
>
> `U --h--> X --f--> Y`,  `g = f ∘ h`
>
> be a commutative diagram of `FTS_S` with `h` étale. Then there is a canonical morphism
>
> `Rg_!(h^* K) ⟶ Rf_! K`,
>
> functorial in `K` in `D^b_{Coh}(𝒪_X)`, defined by the sequence of maps
>
> `Hom(Rf\_! K, L) = Hom\_X(K, f^! L) ⟶ Hom\_U(h^* K, h^*(f^! L)) = Hom\_U(h^* K, h^! f^! L)
>   = Hom\_U(h^* K, g^! L) = Hom(Rg\_!(h^* K), L)`
>
> for `L` in `D^b_{Coh}(𝒪_Y)`: [Stacks, Tag 0G51] twice, `h^* = h^!` ([Stacks, Tag 0FWI]) and
> `h^! ∘ f^! = g^!` ([Stacks, Tag 0ATX]); the functoriality in `L` gives the morphism of
> pro-objects by [Stacks, Tag 0G2X] (`AlgebraicGeometry.lowerShriekMapOfHom`). `Rf_!` and `Rg_!` are
> computed at arbitrary compactifications `c` and `cU`, and `h^!` at the compactification of `h`
> obtained from them (`Stacks.Duality.CompCompactification.restrictCompactification`).

```lean
def lowerShriekEtaleMap (f : X ⟶ Y) (c : CompactificationOf (Over.mk f.left)) (h : U ⟶ X)
    [Etale h.left] (g : U ⟶ Y) (w : h ≫ f = g) (cU : CompactificationOf (Over.mk g.left)) :
    boundedCoherentPullback h.left ⋙ lowerShriek g cU ⟶ lowerShriek f c
```

## Tag 0G58, a remark

[Tag 0G58](https://stacks.math.columbia.edu/tag/0G58) in the Stacks Project.

**`AlgebraicGeometry.lowerShriekFlatQuasiFiniteMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekFlatQuasiFinite.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CompactlySupportedCohomology/LowerShriekFlatQuasiFinite.lean#L243).

> **Stacks Project, Tag 0G58.** In Situation [Stacks, Tag 0F42] let
>
> `U --h--> X --f--> Y`,  `g = f ∘ h`
>
> be a commutative diagram of `FTS_S` with `h` flat and quasi-finite. Then there is a canonical
> transformation
>
> `Rg_! ∘ h^* ⟶ Rf_!`
>
> of functors on `D^b_{Coh}(𝒪_X)`, constructed as in [Stacks, Tag 0G57] from the transformation
> `h^* ⟶ h^!` on `D^+_{Coh}(𝒪_X)` (`Stacks.Duality.pullbackToUpperShriekOfFlatQuasiFinite`) given by
> `h^! K = h^* K ⊗ ω_{U/X}`, `ω_{U/X} = h^! 𝒪_X` the relative dualizing module of `h`
> ([Stacks, Tag 0B6U], [Stacks, Tag 0BV7], [Stacks, Tag 0BVG], [Stacks, Tag 0BUL]), and the trace
> element `τ_{U/X} : 𝒪_U ⟶ ω_{U/X}` ([Stacks, Tag 0BVJ]): for `L` in `D^b_{Coh}(𝒪_Y)`,
>
> `Hom(Rf\_! K, L) = Hom\_X(K, f^! L) ⟶ Hom\_U(h^* K, h^* f^! L) ⟶ Hom\_U(h^* K, h^! f^! L)
>   = Hom\_U(h^* K, g^! L) = Hom(Rg\_!(h^* K), L)`,
>
> by [Stacks, Tag 0G51] twice and `h^! ∘ f^! = g^!` ([Stacks, Tag 0ATX]); the functoriality in `L`
> gives the morphism of pro-objects by [Stacks, Tag 0G2X] (`AlgebraicGeometry.lowerShriekMapOfHom`).
> Quasi-finiteness is `LocallyQuasiFinite`, morphisms of `FTS_S` being quasi-compact. `Rf_!` and
> `Rg_!` are computed at arbitrary compactifications `c` and `cU`, and `h^!` at the
> compactification of `h` obtained from them
> (`Stacks.Duality.CompCompactification.restrictCompactification`).

```lean
def lowerShriekFlatQuasiFiniteMap (f : X ⟶ Y) (c : CompactificationOf (Over.mk f.left))
    (h : U ⟶ X) [Flat h.left] [LocallyQuasiFinite h.left] (g : U ⟶ Y) (w : h ≫ f = g)
    (cU : CompactificationOf (Over.mk g.left)) :
    boundedCoherentPullback h.left ⋙ lowerShriek g cU ⟶ lowerShriek f c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.32, Tag 0G4Z](https://stacks.math.columbia.edu/tag/0G4Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
