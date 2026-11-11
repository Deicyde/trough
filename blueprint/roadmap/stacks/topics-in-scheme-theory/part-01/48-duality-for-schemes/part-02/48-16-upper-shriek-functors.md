---
declaration: section
origin: cited
lean: Stacks.Duality.upperShriek, AlgebraicGeometry.isSeparatedFiniteType, AlgebraicGeometry.FTS, Stacks.Duality.compactificationUpperShriekIso, Stacks.Duality.exists_coherent_compactificationUpperShriekIso, Stacks.Duality.upperShriekCompIsoAtModel, Stacks.Duality.exists_canonical_upperShriekCompIso, Stacks.Duality.exists_upperShriekPseudofunctor
statement: formalized
proof: formalized
---

# 48.16 Upper shriek functors

Section 48.16 of the Stacks Project, [Tag 0A9Y](https://stacks.math.columbia.edu/tag/0A9Y). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A9Y, the section

[Tag 0A9Y](https://stacks.math.columbia.edu/tag/0A9Y) in the Stacks Project.

**`Stacks.Duality.upperShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/Basic.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/Basic.lean#L192).

> **Stacks Project, Tag 0A9Y.** The upper shriek functor of a compactification. Let `S` be a
> quasi-compact quasi-separated scheme (in the source, a Noetherian one), let `f : X ⟶ Y` be a
> morphism of schemes separated and of finite type over `S` and let `j` be a compactification of
> `X` over `Y`, with open immersion `j.immersion : X ⟶ X̄` and proper structure morphism
> `f̄ = j.toBase : X̄ ⟶ Y`. Let `ā` be the right adjoint of `Rf̄_* : D_QCoh(𝒪_X̄) ⥤ D_QCoh(𝒪_Y)`
> of [Stacks, Tag 0A9E]. Then `f^! K = ā(K)|_X`, that is `f^! = j^* ∘ ā`.

```lean
def upperShriek :
    quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory X.left
```

## Tag 0F42, a situation

[Tag 0F42](https://stacks.math.columbia.edu/tag/0F42) in the Stacks Project.

**`AlgebraicGeometry.isSeparatedFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SeparatedFiniteTypeCategory.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/SeparatedFiniteTypeCategory.lean#L67). The attribute's comment: “the condition on the objects”. References: SGA 4 Vbis (5.3.1); SGA 4 XVII (7.0.1).

> A morphism of schemes is separated and of finite type when it is separated, locally of
> finite type and quasi-compact.

```lean
abbrev isSeparatedFiniteType : MorphismProperty Scheme.{u}
```

**`AlgebraicGeometry.FTS`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SeparatedFiniteTypeCategory.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/SeparatedFiniteTypeCategory.lean#L80). The attribute's comment: “the category”. References: SGA 4 Vbis (5.3.1).

> The category of schemes separated and of finite type over `S`: its objects are the
> schemes over `S` whose structure morphism is separated and of finite type, and its
> morphisms are the morphisms of schemes over `S` between them.

```lean
abbrev FTS (S : Scheme.{u}) : Type (u + 1)
```

## Tag 0AA0, a lemma

[Tag 0AA0](https://stacks.math.columbia.edu/tag/0AA0) in the Stacks Project.

**`Stacks.Duality.compactificationUpperShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekIndependence.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekIndependence.lean#L203). The attribute's comment: “the canonical isomorphism f^!\_j = f^!\_k between the upper shriek functors (Stacks.Duality.compactificationUpperShriek, which is Stacks.Duality.upperShriek of Stacks 0A9Y, read on D^+\_QCoh(O\_Y) as in the source) of any two compactifications j, k of a morphism f : X -> Y of FTS S over a Noetherian S: the source's alpha\_\{g\_1}^\{-1} then alpha\_\{g\_2} for the two projections of the common refinement with dense interior of Stacks 0ATU. Nothing is carried: alpha\_g needs Stacks 0A9K for the square of g, which is Stacks.Duality.isIso\_refinementXi, and Stacks 0A9P (2) for it (G proper, Xbar\_2 Noetherian), which is Stacks.Duality.isIso\_refinementBaseChangePlus, both instances. Its value on the diagonal is the identity (Stacks.Duality.compactificationUpperShriekIso\_refl), it is transitive (Stacks.Duality.compactificationUpperShriekIso\_trans) and it is the source's alpha\_g for an interior-preserving g (Stacks.Duality.compactificationUpperShriekIso\_eq\_iso); Stacks.Duality.exists\_coherent\_compactificationUpperShriekIso collects these. The compactifications are arguments; that one exists is Stacks 0F41”.

> **[Stacks, Tag 0AA0]: the canonical comparison of the upper shriek functors of two
> compactifications.**  It is `α_{g₁}⁻¹ ≫ α_{g₂}` for the two projections of the common refinement
> with dense interior of [Stacks, Tag 0ATU], as an isomorphism of functors out of
> `D⁺_QCoh(𝒪_Y)`.

```lean
def compactificationUpperShriekIso (j k : CompactificationOf (Over.mk f.left)) :
    compactificationUpperShriek f j ≅ compactificationUpperShriek f k
```

**`Stacks.Duality.exists_coherent_compactificationUpperShriekIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekIndependence.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekIndependence.lean#L328). The attribute's comment: “the upper shriek functor of a compactification (Stacks.Duality.compactificationUpperShriek, which is Stacks.Duality.upperShriek of Stacks 0A9Y) on D^+\_QCoh(O\_Y), the source's own domain for it, is independent of the compactification up to canonical isomorphism: a family of isomorphisms between the functors of any two compactifications that is the identity on the diagonal, transitive, and equal to the source's alpha\_g (Stacks.Duality.refinementIso) whenever the two compactifications are joined by an interior-preserving morphism g. Nothing is carried; the family is Stacks.Duality.compactificationUpperShriekIso”.

> **[Stacks, Tag 0AA0]: the upper shriek functor is independent of the compactification, by a
> coherent family of isomorphisms.**  There is a family of isomorphisms `e j k : f^!_j ≅ f^!_k`
> of functors out of `D⁺_QCoh(𝒪_Y)`,
> indexed by pairs of compactifications of `X` over `Y`, which is the identity on the diagonal,
> composes transitively, and **agrees with the source's comparison `α_g` whenever `j` and `k` are
> joined by an interior-preserving morphism `g`**.  So the isomorphism class of `f^!` does not
> depend on the compactification, the identifications of three compactifications are compatible,
> and the family is the source's.
>
> The family is `Stacks.Duality.compactificationUpperShriekIso` itself; reflexivity is
> `Stacks.Duality.compactificationUpperShriekIso_refl`, transitivity is
> `Stacks.Duality.compactificationUpperShriekIso_trans`, and the agreement with `α_g` is
> `Stacks.Duality.compactificationUpperShriekIso_eq_iso`.

```lean
theorem exists_coherent_compactificationUpperShriekIso :
    ∃ e : ∀ j k : CompactificationOf (Over.mk f.left),
        compactificationUpperShriek f j ≅ compactificationUpperShriek f k,
      (∀ j, e j j = Iso.refl _) ∧ (∀ j k l, e j k ≪≫ e k l = e j l) ∧
        ∀ (j k : CompactificationOf (Over.mk f.left)) (g : j ⟶ k)
          (hg : CompactificationOf.PreservesInterior g), e j k = refinementIso f g hg
```

## Tag 0ATX, a lemma

[Tag 0ATX](https://stacks.math.columbia.edu/tag/0ATX) in the Stacks Project.

**`Stacks.Duality.upperShriekCompIsoAtModel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekComposition.lean, line 1073](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekComposition.lean#L1073). The attribute's comment: “the canonical isomorphism (g o f)^! = f^! o g^! of upper shriek functors for composable morphisms f : X -> Y, g : Y -> Z of FTS S over a Noetherian S, at arbitrary compactifications k of g o f, j of f and i of g, as functors out of D^+\_QCoh(O\_Z), with g^! read in D^+\_QCoh(O\_Y) (Stacks 0A9I) and each f^! the functor Stacks.Duality.compactificationUpperShriek of Stacks 0A9Y/0AA0. It is the source's construction for a choice of compactifications through i: (j' o j)^* a b = j^* (j')^* a b -> j^* a' i^* b via the base change map of Stacks 0AA6, invertible by Stacks 0A9P (2), read through the canonical comparisons of Stacks 0AA0. Canonicity is proved, not assumed: Stacks.Duality.upperShriekCompIsoAtModel\_choice says it is the source's isomorphism for every choice (the second half of the source's proof: the chase of squares A..F through Stacks 0ATQ and 0ATR, and a dominating choice from Stacks 0ATU), and Stacks.Duality.upperShriekCompIsoAtModel\_naturality says it is compatible with the comparisons of Stacks 0AA0 in all three compactifications. The compactifications are arguments, as in Stacks 0AA0; that they exist is Stacks 0F41”.

> **[Stacks, Tag 0ATX]: the canonical isomorphism `(g ∘ f)^! ≅ f^! ∘ g^!`**, for any
> compactifications `k` of `g ∘ f`, `j` of `f` and `i` of `g`. It is the source's construction for a
> choice of compactifications whose compactification of `Y` is `i` (that one exists is
> [Stacks, Tag 0A9Z]), read through the canonical comparisons of [Stacks, Tag 0AA0].

```lean
def upperShriekCompIsoAtModel (k : CompactificationOf (Over.mk (f ≫ g).left))
    (j : CompactificationOf (Over.mk f.left)) (i : CompactificationOf (Over.mk g.left)) :
    compactificationUpperShriek (f ≫ g) k ≅
      upperShriekPlusAtModel i ⋙ compactificationUpperShriek f j
```

**`Stacks.Duality.exists_canonical_upperShriekCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekComposition.lean, line 1136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekComposition.lean#L1136). The attribute's comment: “existence and canonicity of the isomorphism (g o f)^! = f^! o g^! for composable morphisms of FTS S over a Noetherian S, the upper shriek functors being those of Stacks 0AA0 on D^+\_QCoh and g^! read in D^+\_QCoh(O\_Y): a family of isomorphisms indexed by compactifications of g o f, f and g that equals the source's construction for every choice of compactifications (Stacks.Duality.CompositionData.compIsoAPI) and is compatible with the comparisons of Stacks 0AA0 in all three compactifications. Nothing is assumed beyond the compactifications themselves, which are arguments as in Stacks 0AA0 (their existence is Stacks 0F41)”.

> **[Stacks, Tag 0ATX]: there is a canonical isomorphism `(g ∘ f)^! → f^! ∘ g^!`.** For
> composable morphisms `f : X ⟶ Y`, `g : Y ⟶ Z` of `AlgebraicGeometry.FTS S` over a Noetherian `S`
> there is a family of isomorphisms `(g ∘ f)^!_k ≅ f^!_j ∘ g^!_i`, indexed by compactifications `k`
> of `g ∘ f`, `j` of `f` and `i` of `g`, which is the source's construction for **every** choice of
> compactifications, and which is compatible with the canonical comparisons of [Stacks, Tag 0AA0] in
> all three compactifications — so it is independent of the choices made. The family is
> `Stacks.Duality.upperShriekCompIsoAtModel`.

```lean
theorem exists_canonical_upperShriekCompIso :
    ∃ e : ∀ (k : CompactificationOf (Over.mk (f ≫ g).left))
        (j : CompactificationOf (Over.mk f.left)) (i : CompactificationOf (Over.mk g.left)),
        compactificationUpperShriek (f ≫ g) k ≅ upperShriekPlusAtModel i ⋙
            compactificationUpperShriek f j,
      (∀ D : CompositionData f g, e D.outer D.inner D.base = D.compIsoAPI) ∧
      ∀ k k' j j' i i', compactificationUpperShriekIso (f ≫ g) k k' ≪≫ e k' j' i' =
        e k j i ≪≫ NatIso.hcomp (basePlusIsoAPI i i') (compactificationUpperShriekIso f j j')
```

## Tag 0ATY, a lemma

[Tag 0ATY](https://stacks.math.columbia.edu/tag/0ATY) in the Stacks Project.

**`Stacks.Duality.exists_upperShriekPseudofunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekPseudofunctor/Pseudofunctor.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Compactification/ShriekPseudofunctor/Pseudofunctor.lean#L222). The attribute's comment: “the full statement: Stacks.Duality.upperShriekPseudofunctor is a pseudofunctor LocallyDiscrete (FTS S)^op -> Cat (Mathlib's Pseudofunctor, i.e. Categories 003N with conditions (a) invertibility, (b), (c) unit laws and (d) cocycle condition as its axioms) over a Noetherian S, with object X |-> D^+\_QCoh(O\_X), morphism f |-> f^! of Stacks 0AA0 (the functor Stacks.Duality.compactificationUpperShriek of a compactification of f, read in D^+\_QCoh, Stacks 0A9I; compactifications exist by Stacks 0F41) and compositor the canonical isomorphism (g o f)^! = f^! o g^! of Stacks 0ATX (Stacks.Duality.upperShriekCompIsoAtModel). The cocycle condition (d) is the source's proof, Stacks.Duality.upperShriekCompIsoAtModel\_cocycle: a choice Zbar over T, Ybar over Zbar, Xbar over Ybar (0F41, 0A9Z), the squares A, B, C, and gamma\_\{A+B} = gamma\_A o gamma\_B (0ATR), gamma\_\{B+C} = gamma\_C o gamma\_B (0ATQ), gamma\_A and gamma\_C commuting by naturality. The unit (1\_X)^! = id, which the source does not specify, is the one determined by the compositor of 1\_X, and (b), (c) follow from (d). Nothing is assumed”.

> **[Stacks, Tag 0ATY]**: in Situation 0F42 the constructions of [Stacks, Tag 0AA0] and
> [Stacks, Tag 0ATX] define a pseudofunctor from `FTS S` into the 2-category of categories: there
> is a pseudofunctor `(FTS S)ᵒᵖ ⥤ᵖ Cat` whose value at `X` is `D⁺_QCoh(𝒪_X)`, whose value at `f`
> is the upper shriek functor `f^!` of [Stacks, Tag 0AA0] (at a compactification of `f`, which
> exists by More on Flatness, Theorem 0F41; by [Stacks, Tag 0AA0] the choice does not matter up to
> canonical isomorphism), and whose compositor at `f`, `g` is the canonical isomorphism
> `(g ∘ f)^! ≅ f^! ∘ g^!` of [Stacks, Tag 0ATX]. It is `Stacks.Duality.upperShriekPseudofunctor`;
> the axioms of a pseudofunctor are the conditions (a)–(d) of Categories, Definition 003N.

```lean
theorem exists_upperShriekPseudofunctor :
    ∃ P : LocallyDiscrete (FTS S)ᵒᵖ ⥤ᵖ Cat.{u, u + 1},
      ∃ hobj : ∀ X : (FTS S)ᵒᵖ,
          P.obj ⟨X⟩ = Cat.of (quasiCoherentDerivedCategoryPlusAtModel X.unop.left),
        (∀ {X Y : (FTS S)ᵒᵖ} (f : X ⟶ Y),
          eqToHom (hobj X).symm ≫ P.map ⟨f⟩ ≫ eqToHom (hobj Y) =
            (upperShriekPlusAtModel (cc f.unop)).toCatHom) ∧
        (∀ {X Y Z : (FTS S)ᵒᵖ} (f : X ⟶ Y) (g : Y ⟶ Z),
          HEq (Cat.Hom.toNatIso (P.mapComp ⟨f⟩ ⟨g⟩))
            (upperShriekCompIsoAtModelPlus (cc (g.unop ≫ f.unop)) (cc g.unop) (cc f.unop)))
```

## Tag 0B6T, a lemma

[Tag 0B6T](https://stacks.math.columbia.edu/tag/0B6T) in the Stacks Project.

**`Stacks.Duality.upperShriekCompareWithPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparison.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparison.lean#L175). The attribute's comment: “the map mu\_\{f,K} of Lemma 48.16.5, at the compactification j from which Stacks.Duality.upperShriek computes f^!”.

> **Stacks Project, Tag 0B6T (Lemma 48.16.5).** Let `f : X ⟶ Y` be a morphism of
> `AlgebraicGeometry.FTS S` and let `j` be a compactification of `X` over `Y`, with ambient scheme
> `X̄`, open immersion `j.immersion` and proper structure morphism `f̄ = j.toBase`. The map
>
>   `μ_{f,K} : Lf^*K ⊗ᴸ_{𝒪_X} f^!𝒪_Y ⟶ f^!K`
>
> is the restriction to `X` of the comparison map `Lf̄^*K ⊗ᴸ_{𝒪_X̄} ā(𝒪_Y) ⟶ ā(K)` of Equation
> 48.8.0.1 ([Stacks, Tag 0A9S]), the source being read through the composition formula
> `Lf^* ≅ Lf̄^* ⋙ Lj^*` and the monoidality of `Lj^*` of [Stacks, Tag 079U].

```lean
public def upperShriekCompareWithPullback (K : quasiCoherentDerivedCategory Y.left) :
    ((quasiCoherentDerivedTensor X.left).obj
        ((quasiCoherentDerivedPullback' f.left).obj K)).obj
        ((upperShriek f j).obj (derivedStructureSheaf Y.left)) ⟶
      (upperShriek f j).obj K
```

**`Stacks.Duality.upperShriekCompareWithPullback_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparison.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparison.lean#L206). The attribute's comment: “functoriality of mu\_\{f,K} in K”.

> **The map `μ_{f,K}` of [Stacks, Tag 0B6T] is functorial in `K`.** Each of its three factors
> is natural: the composition formula for derived pullback, the monoidality of `Lj^*`, and
> Equation 48.8.0.1 by `Stacks.Duality.compareWithPullback_naturality`.

```lean
public theorem upperShriekCompareWithPullback_naturality
    {K K' : quasiCoherentDerivedCategory Y.left} (h : K ⟶ K') :
    ((quasiCoherentDerivedTensor X.left).map
          ((quasiCoherentDerivedPullback' f.left).map h)).app
          ((upperShriek f j).obj (derivedStructureSheaf Y.left)) ≫
        upperShriekCompareWithPullback f j αBar αImm ρ K' =
      upperShriekCompareWithPullback f j αBar αImm ρ K ≫
        (upperShriek f j).map h
```

**`Stacks.Duality.upperShriekCompareWithPullback_comp_upperShriekPlusIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonCanonical.lean, line 670](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonCanonical.lean#L670). The attribute's comment: “independence of the compactification”.

> **[Stacks, Tag 0B6T]: `μ_{f,K}` does not depend on the compactification.** For two
> compactifications `j₁`, `j₂` of `X` over `Y` and `K ∈ D⁺_QCoh(𝒪_Y)`, `μ_{f,K}` for `j₁`, followed
> by the isomorphism `f^!_{j₁} ≅ f^!_{j₂}` of [Stacks, Tag 0AA0] at `K`, is `Lf^*K` tensored with
> that isomorphism at `𝒪_Y`, followed by `μ_{f,K}` for `j₂`.

```lean
theorem upperShriekCompareWithPullback_comp_upperShriekPlusIso
    (j₁ j₂ : CompactificationOf (Over.mk f.left))
    (K : quasiCoherentDerivedCategoryPlusOfModel Y.left) :
    upperShriekCompareWithPullbackCanonical f j₁ K.obj ≫
        ((upperShriekPlusIso f j₁ j₂).hom.app K).hom =
      ((quasiCoherentDerivedTensor X.left).obj
        ((quasiCoherentDerivedPullback' f.left).obj K.obj)).map
          ((upperShriekPlusIso f j₁ j₂).hom.app (derivedStructureSheafPlus Y.left)).hom ≫
        upperShriekCompareWithPullbackCanonical f j₂ K.obj
```

**`Stacks.Duality.upperShriekCompareWithPullbackCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonCanonicalMaps.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonCanonicalMaps.lean#L85). The attribute's comment: “the maps μ\_\{f,K}”.

> **Stacks Project, Tag 0B6T (Lemma 48.16.5).** Let `f : X ⟶ Y` be a morphism of
> `AlgebraicGeometry.FTS S` and let `j` be a compactification of `X` over `Y`, with ambient scheme
> `X̄`, open immersion `j.immersion` and proper structure morphism `f̄ = j.toBase`. The map
>
>   `μ_{f,K} : Lf^*K ⊗ᴸ_{𝒪_X} f^!𝒪_Y ⟶ f^!K`
>
> is the restriction to `X` of the comparison map `Lf̄^*K ⊗ᴸ_{𝒪_X̄} ā(𝒪_Y) ⟶ ā(K)` of Equation
> 48.8.0.1 ([Stacks, Tag 0A9S]), the source being read through the composition formula
> `Lf^* ≅ Lf̄^* ⋙ Lj^*` and the monoidality of `Lj^*` of [Stacks, Tag 079U].

```lean
public def upperShriekCompareWithPullbackCanonical (K : quasiCoherentDerivedCategory Y.left) :
    ((quasiCoherentDerivedTensor X.left).obj
        ((quasiCoherentDerivedPullback' f.left).obj K)).obj
        ((upperShriek f j).obj (derivedStructureSheaf Y.left)) ⟶
      (upperShriek f j).obj K
```

**`Stacks.Duality.upperShriekCompareWithPullbackCanonical_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonCanonicalMaps.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonCanonicalMaps.lean#L108). The attribute's comment: “functoriality of μ\_\{f,K} in K”.

> **The map `μ_{f,K}` of [Stacks, Tag 0B6T] is functorial in `K`.** Each of its three factors
> is natural: the composition formula for derived pullback, the monoidality of `Lj^*`, and
> Equation 48.8.0.1 by `Stacks.Duality.compareWithPullback_naturality`.

```lean
public theorem upperShriekCompareWithPullbackCanonical_naturality
    {K K' : quasiCoherentDerivedCategory Y.left} (h : K ⟶ K') :
    ((quasiCoherentDerivedTensor X.left).map
          ((quasiCoherentDerivedPullback' f.left).map h)).app
          ((upperShriek f j).obj (derivedStructureSheaf Y.left)) ≫
        upperShriekCompareWithPullbackCanonical f j K' =
      upperShriekCompareWithPullbackCanonical f j K ≫
        (upperShriek f j).map h
```

**`Stacks.Duality.upperShriekCompareWithPullback_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonComp.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPullbackComparisonComp.lean#L549). The attribute's comment: “compatibility with composition”.

> **Stacks Project, Tag 0B6T (Lemma 48.16.5), compatibility with composition.** Let
> `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of `AlgebraicGeometry.FTS S` with `S` Noetherian, and
> let `cf`, `cg`, `cfg` be compactifications of `f`, `g` and `g ∘ f`, computing `f^!`, `g^!` and
> `(g ∘ f)^!`. For `K ∈ D⁺_QCoh(𝒪_Z)`, the map `μ_f` at `Lg^*K ⊗ g^!𝒪_Z` followed by `f^!μ_{g,K}`
> equals: the identification
> `Lf^*(Lg^*K ⊗ g^!𝒪_Z) ⊗ f^!𝒪_Y = Lf^*Lg^*K ⊗ (Lf^*g^!𝒪_Z ⊗ f^!𝒪_Y)` (the tensor structure of
> `Lf^*` and the associator), `Lf^*Lg^*K ⊗ μ_f` at `g^!𝒪_Z`, the identifications
> `Lf^*Lg^*K = L(g ∘ f)^*K` and `f^!g^!𝒪_Z = (g ∘ f)^!𝒪_Z` of [Stacks, Tag 0ATX]
> (`Stacks.Duality.upperShriekCompIso`), `μ_{g ∘ f}` at `K`, and `(g ∘ f)^!K = f^!g^!K`. The
> tensor products are `Stacks.Duality.quasiCoherentDerivedTensor`, read through
> `Stacks.Duality.quasiCoherentDerivedTensorIsoCurriedTensor` where the monoidal structure of
> `D_QCoh` is used.

```lean
theorem upperShriekCompareWithPullback_comp (cf : CompactificationOf (Over.mk f.left))
    (cg : CompactificationOf (Over.mk g.left)) (cfg : CompactificationOf (Over.mk (f ≫ g).left))
    (K : quasiCoherentDerivedCategoryPlusOfModel Z.left) :
    upperShriekCompareWithPullbackCanonical f cf
        (((quasiCoherentDerivedTensor Y.left).obj
          ((quasiCoherentDerivedPullback' g.left).obj K.obj)).obj
          ((upperShriek g cg).obj (DerivedPushforward.derivedStructureSheaf Z.left))) ≫
        (upperShriek f cf).map (upperShriekCompareWithPullbackCanonical g cg K.obj) =
      ((quasiCoherentDerivedTensorIsoCurriedTensor X.left).hom.app
          ((quasiCoherentDerivedPullback' f.left).obj
            (((quasiCoherentDerivedTensor Y.left).obj
              ((quasiCoherentDerivedPullback' g.left).obj K.obj)).obj
              ((upperShriek g cg).obj (DerivedPushforward.derivedStructureSheaf Z.left))))).app
          ((upperShriek f cf).obj (DerivedPushforward.derivedStructureSheaf Y.left)) ≫
        (quasiCoherentDerivedPullback' f.left).map
          (((quasiCoherentDerivedTensorIsoCurriedTensor Y.left).hom.app
            ((quasiCoherentDerivedPullback' g.left).obj K.obj)).app
            ((upperShriek g cg).obj (DerivedPushforward.derivedStructureSheaf Z.left))) ▷ _ ≫
        Functor.OplaxMonoidal.δ (quasiCoherentDerivedPullback' f.left)
          ((quasiCoherentDerivedPullback' g.left).obj K.obj)
          ((upperShriek g cg).obj (DerivedPushforward.derivedStructureSheaf Z.left)) ▷ _ ≫
        (α_ _ _ _).hom ≫
        (quasiCoherentDerivedPullback' f.left).obj
            ((quasiCoherentDerivedPullback' g.left).obj K.obj) ◁
          (((quasiCoherentDerivedTensorIsoCurriedTensor X.left).inv.app
            ((quasiCoherentDerivedPullback' f.left).obj
              ((upperShriek g cg).obj (DerivedPushforward.derivedStructureSheaf Z.left)))).app
            ((upperShriek f cf).obj (DerivedPushforward.derivedStructureSheaf Y.left)) ≫
          upperShriekCompareWithPullbackCanonical f cf
            ((upperShriek g cg).obj (DerivedPushforward.derivedStructureSheaf Z.left))) ≫
        ((quasiCoherentDerivedPullbackCompIso f.left g.left).hom.app K.obj ⊗ₘ
          ((upperShriekCompIso f g cf cg cfg).inv.app (derivedStructureSheafPlus Z.left)).hom) ≫
        ((quasiCoherentDerivedTensorIsoCurriedTensor X.left).inv.app
            ((quasiCoherentDerivedPullback' (f ≫ g).left).obj K.obj)).app
          ((upperShriek (f ≫ g) cfg).obj (DerivedPushforward.derivedStructureSheaf Z.left)) ≫
        upperShriekCompareWithPullbackCanonical (f ≫ g) cfg K.obj ≫
        ((upperShriekCompIso f g cf cg cfg).hom.app K).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.16, Tag 0A9Y](https://stacks.math.columbia.edu/tag/0A9Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
