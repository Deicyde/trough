---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_discreteValuationRing_of_mem_closure_range_pointsMap, AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_discreteUniqueness, AlgebraicGeometry.Stack.AlgebraicStacks.isProper_of_discreteExistenceAlong, AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_denseTestUniqueness, AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_discreteUniquenessAlong_of_dense, AlgebraicGeometry.Stack.ValuativeCriterion.DiscreteExistence, AlgebraicGeometry.Stack.discreteExistence_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_of_discreteExistence
statement: formalized
proof: formalized
---

# 106.11 Noetherian valuative criterion

Section 106.11 of the Stacks Project, [Tag 0CQL](https://stacks.math.columbia.edu/tag/0CQL). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H2B, a lemma

[Tag 0H2B](https://stacks.math.columbia.edu/tag/0H2B) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_discreteValuationRing_of_mem_closure_range_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ClosureImageDiscreteValuationPoint.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ClosureImageDiscreteValuationPoint.lean#L227).

> **Stacks 0H2B.** A point in the closure of the image of a finite-type 1-morphism of algebraic
> stacks whose target is locally Noetherian is reached by the closed point of a valuative square
> whose valuation ring is a discrete valuation ring.

```lean
theorem exists_discreteValuationRing_of_mem_closure_range_pointsMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicStacks.IsFiniteType B S hS f)
    (h𝒴 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (y : points B S hS 𝒴.val.val (Classical.choose 𝒴.property))
    (hy : y ∈ @closure _
      (pointTopology B S hS 𝒴.val)
      (Set.range
        (pointsMap B S hS 𝒳.val.val (Classical.choose 𝒳.property)
          (Classical.choose 𝒴.property) f.hom.hom))) :
    ∃ (q : ValuativeSquare B S hS f) (_ : IsDiscreteValuationRing q.R)
      (hz : B.Contains
        (Spec (.of ((Spec (.of q.R)).residueField (IsLocalRing.closedPoint q.R))))),
      pointClass B S hS 𝒴.val.val
        (Classical.choose 𝒴.property)
        (fieldValuedPointMap B S hS
          (schemeFibredCategory B S hS
            (siteObject B S hS q.ring_mem q.base)).val
          q.y.hom
          (closedPointFieldValuedPoint B S hS
            (siteObject B S hS q.ring_mem q.base)
            (IsLocalRing.closedPoint q.R) hz)) = y
```

## Tag 0E80, a lemma

[Tag 0E80](https://stacks.math.columbia.edu/tag/0E80) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_discreteUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionSeparated.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionSeparated.lean#L324). The attribute's comment: “a quasi-separated 1-morphism of algebraic stacks, locally of finite type over a locally Noetherian target, is separated as soon as the uniqueness part of the valuative criterion holds at every discrete valuation ring”.

> **Stacks 0E80, the Noetherian valuative criterion for separatedness.** Let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks over `S` with `𝒴` locally Noetherian and `f` locally of finite type
> and quasi-separated. If, for every valuative diagram for `f` whose valuation ring is a *discrete*
> valuation ring, the category of dotted arrows is either empty or a setoid with exactly one
> isomorphism class, then `f` is separated.
>
> Separatedness is properness of `Δ_f` in the relative sense of Stacks 04XB, and
> `AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_discreteLift` reduces it, along a locally
> Noetherian scheme chart of `𝒳 ×_𝒴 𝒳`, to the full valuative criterion at discrete valuation rings
> for the algebraic spaces representing the base changes of `Δ_f`. Both halves of that criterion
> come from the hypothesis through the two transfers of Stacks 0CLN and Stacks 0CLJ, each of which
> carries a restriction on the valuation ring through unchanged:
>
> * a lift exists by `AlgebraicGeometry.Stack.nonempty_lift_baseChange_point`, whose input is a
>   dotted arrow for a valuative *square* for `Δ_f` over the same valuation ring; reading that
>   square as a valuative diagram, Stacks 0E8L builds it from the hypothesis through
>   `AlgebraicGeometry.Stack.nonempty_dottedArrow_relativeDiagonal_of_pred`;
> * it is unique by `AlgebraicGeometry.Stack.subsingleton_lift_baseChange_point`, whose input is the
>   isomorphism of any two dotted arrows of a valuative diagram for `Δ_f`, which is
>   `AlgebraicGeometry.Stack.nonempty_iso_dottedArrow_relativeDiagonal_of_pred`.
>
> The valuation ring never changes along the way — no extension of the fraction field and no passage
> to a dominating valuation ring — so "discrete" survives every step, which is the whole point of
> the Noetherian form of the criterion.

```lean
theorem isSeparated_of_discreteUniqueness (f : 𝒳 ⟶ 𝒴)
    (hY : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hqs : IsQuasiSeparated B S hS f)
    (H : ValuativeCriterion.DiscreteUniqueness B S hS f) :
    IsSeparated B S hS f
```

## Tag 0CQM, a lemma

[Tag 0CQM](https://stacks.math.columbia.edu/tag/0CQM) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_of_discreteExistenceAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RefinedValuativeCriterionProper.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RefinedValuativeCriterionProper.lean#L405).

> **Stacks 0CQM.** Let `f : 𝒳 ⟶ 𝒴` and `h : 𝒰 ⟶ 𝒳` be 1-morphisms of algebraic stacks over
> `S`. Assume that `𝒴` is locally Noetherian, that `f` and `h` are of finite type, that `f` is
> separated, and that the image of `|h| : |𝒰| → |𝒳|` is dense in `|𝒳|`. If for every
> 2-commutative diagram `Spec K ⟶ 𝒰 ⟶ 𝒳 ⟶ 𝒴`, `Spec A ⟶ 𝒴`, with `A` a discrete valuation ring
> with field of fractions `K` and a 2-arrow `γ : y ∘ j → f ∘ h ∘ u`, there are an extension
> `K'/K` of fields and a valuation ring `A' ⊂ K'` dominating `A` such that the category of dotted
> arrows of the induced diagram for `f` is nonempty, then `f` is proper.
>
> `𝒴` locally Noetherian is the existence of a smooth surjective atlas by a locally Noetherian
> scheme (`HasPropertyOnSomeSchemeAtlas`). The valuative hypothesis is
> `ValuativeCriterion.DiscreteExistenceAlong B S hS h f`: a diagram of the statement is a valuative
> square for `f` (Stacks 0CLK) over a discrete valuation ring whose generic point `x` is `u ≫ h`,
> its 2-arrow being the square's `γ`; the induced diagram over `A'` with its 2-arrow `γ'` is the
> square's restriction along the dominating extension (`e.inducedGamma`), and its category of
> dotted arrows is that of Stacks 0CLA (`CategoryTheory.DottedArrow`).
>
> The proof is the source's: the reduction to an affine locally Noetherian base and an affine
> source (`isProper_of_discreteExistenceAlong_of_affineCore`), and the affine case
> (`universallyClosed_of_discreteExistenceAlong_affineCore`), which uses
> Chow's lemma for algebraic stacks over a Noetherian base.

```lean
theorem isProper_of_discreteExistenceAlong
    {𝒰 𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (h : 𝒰 ⟶ 𝒳) (f : 𝒳 ⟶ 𝒴)
    (h𝒴 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hf : IsFiniteType B S hS f) (hh : IsFiniteType B S hS h) (hsep : IsSeparated B S hS f)
    (hdense : @Dense _ (pointTopology B S hS 𝒳.val) (Set.range (pointsMap B S hS h)))
    (hlift : ValuativeCriterion.DiscreteExistenceAlong B S hS h f) :
    IsProper B S hS f
```

## Tag 0E95, a lemma

[Tag 0E95](https://stacks.math.columbia.edu/tag/0E95) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_denseTestUniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DenseTestValuativeSeparated.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DenseTestValuativeSeparated.lean#L288).

> **Stacks 0E95.** Let
> `f : 𝒳 ⟶ 𝒴` and `h : 𝒰 ⟶ 𝒳` be 1-morphisms of algebraic stacks over `S`, with `𝒴` locally
> Noetherian, `f` locally of finite type and quasi-separated, `h` of finite type and the image of
> `|h|` dense in `|𝒳|`. If every discrete valuative square for `f` through `h` has a category of
> dotted arrows which is either empty or a setoid with exactly one isomorphism class, then `f` is
> separated.
>
> `Δ_f` is separated by the first case applied to `Δ_f` and `h`: the relative diagonal of `Δ_f` is
> separated because `Δ_f` is representable by algebraic spaces (Stacks 04YQ part (4), read in the
> sense of Stacks 04YW by Stacks 04YS), `Δ_{Δ_f}` is quasi-compact because `Δ_f` is
> quasi-separated (Stacks 04YZ part (2) and Stacks 050T), and the hypothesis passes from `f` to
> `Δ_f` by Stacks 0E8L. Then the first case applies to `f` and `h`.

```lean
theorem isSeparated_of_denseTestUniqueness
    (f : 𝒳 ⟶ 𝒴) (h : 𝒰 ⟶ 𝒳)
    (hY : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hqs : IsQuasiSeparated B S hS f)
    (hh : IsFiniteType B S hS h)
    (hdense : letI := Stack.pointTopology B S hS 𝒳.val;
      Dense (Set.range (Stack.pointsMap B S hS 𝒰.val.val 𝒰.val.property 𝒳.val.property
        h.hom.hom)))
    (hu : ValuativeCriterion.DenseTestUniqueness B S hS h f) :
    IsSeparated B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_discreteUniquenessAlong_of_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RefinedValuativeCriterionSeparationUnconditional.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RefinedValuativeCriterionSeparationUnconditional.lean#L540).

> **Stacks 0E95.** Let `f : 𝒳 ⟶ 𝒴` and `h : 𝒰 ⟶ 𝒳` be 1-morphisms of algebraic stacks over
> `S`. Assume that `𝒴` is locally Noetherian, that `f` is locally of finite type and
> quasi-separated, that `h` is of finite type, and that the image of `|h| : |𝒰| ⟶ |𝒳|` is dense in
> `|𝒳|`. If for every 2-commutative diagram for `f` over a discrete valuation ring `A` with fraction
> field `K` whose generic point is `h ∘ u` for some `u : Spec K ⟶ 𝒰`, the category of dotted arrows
> is either empty or a setoid with exactly one isomorphism class, then `f` is separated.
>
> The hypothesis on dotted arrows is
> `AlgebraicGeometry.Stack.ValuativeCriterion.DiscreteUniquenessAlong`. The proof is the source's:
> the first case (`isSeparated_of_isSeparated_relativeDiagonal_of_discreteUniquenessAlong`) applied
> to `Δ_f` in place of `f` shows that `Δ_f` is separated, and the first case applied to `f`
> concludes. For the first application, `Δ_f` is representable by algebraic spaces, so every
> category of dotted arrows of a diagram for `Δ_f` is a setoid (Stacks 0E8L, Stacks 0CLC), whence
> `Δ_{Δ_f}` is separated; uniqueness along `h` passes from `f` to `Δ_f` by Stacks 0E8L; `Δ_f` is
> quasi-separated because `f` is; and `𝒳 ×_𝒴 𝒳` is locally Noetherian (Stacks 06R6).

```lean
theorem isSeparated_of_discreteUniquenessAlong_of_dense
    {𝒰 𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (h : 𝒰 ⟶ 𝒳) (f : 𝒳 ⟶ 𝒴)
    (h𝒴 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hf : IsLocallyOfFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f)
    (hh : IsFiniteType B S hS h)
    (hdense : @Dense _ (pointTopology B S hS 𝒳.val) (Set.range (pointsMap B S hS h)))
    (huniq : ValuativeCriterion.DiscreteUniquenessAlong B S hS h f) :
    IsSeparated B S hS f
```

## Tag 0H2C, a lemma

[Tag 0H2C](https://stacks.math.columbia.edu/tag/0H2C) in the Stacks Project.

**`AlgebraicGeometry.Stack.ValuativeCriterion.DiscreteExistence`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean#L107). The attribute's comment: “the hypothesis of the lemma: the existence part of the valuative criterion, restricted to discrete valuation rings”.

> **The hypothesis of Stacks 0H2C.** A 1-morphism of algebraic stacks over `S` satisfies the
> *discrete* existence part of the valuative criterion when every valuative square for it whose
> valuation ring is a discrete valuation ring admits a dotted arrow after an extension of the
> fraction field and passage to a dominating valuation ring.
>
> This is `AlgebraicGeometry.Stack.ValuativeCriterion.Existence` of **Stacks 0CLK** with the extra
> clause `IsDiscreteValuationRing q.R`; the dominating valuation ring is not asked to be
> discrete.

```lean
abbrev DiscreteExistence (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.discreteExistence_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean#L122). The attribute's comment: “step 1 of the proof: the hypothesis is stable under base change, via Tag 0CLE”.

> **The hypothesis of Stacks 0H2C is stable under base change.** A base change of a
> 1-morphism of algebraic stacks satisfying the discrete existence part of the valuative criterion
> satisfies it as well.
>
> The valuative square for `f` obtained by pasting the given square with the base-change square
> has the same valuation ring, so discreteness transports, and the dotted arrow comes back along
> the equivalence of **Stacks 0CLE**.

```lean
theorem discreteExistence_baseChange
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hf : ValuativeCriterion.DiscreteExistence B S hS f) :
    ValuativeCriterion.DiscreteExistence B S hS P.fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_of_discreteExistence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean#L180). The attribute's comment: “steps 3 and 4 of the proof: closedness on points”.

> **Closedness on points from the hypothesis of Stacks 0H2C.** Let `f : 𝒳 ⟶ 𝒴` be a
> finite-type 1-morphism of algebraic stacks over `S` with `𝒴` locally Noetherian which satisfies
> the discrete existence part of the valuative criterion. Then `f` is closed on points.
>
> A closed subset of `|𝒳|` is the set of points of a closed substack `i : 𝒵 ⟶ 𝒳` by the existence
> half of **Stacks 0509**, so its image is
> the image of `|𝒵| → |𝒴|`. A point in the closure of that image is reached by a discrete
> valuative square for `i ≫ f` (**Stacks 0H2B**); read as a square for `f` it yields a lift to `𝒳`
> over a dominating valuation ring, and the full existence criterion, available for the closed
> immersion `i` by **Stacks 0CLP**, lifts that further to `𝒵`.

```lean
theorem isClosed_of_discreteExistence (f : 𝒳 ⟶ 𝒴)
    (hf : IsFiniteType B S hS f)
    (h𝒴 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hlift : ValuativeCriterion.DiscreteExistence B S hS f) :
    IsClosed B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_discreteExistence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean#L257). The attribute's comment: “clause (2) of Tag 0H2A for `f`”.

> **Stacks 0H2A, item (2), from the hypothesis of Stacks 0H2C.** Let `f : 𝒳 ⟶ 𝒴` be a
> finite-type 1-morphism of algebraic stacks over `S` with `𝒴` locally Noetherian which satisfies
> the discrete existence part of the valuative criterion. Then for every object `Z` of the site
> whose scheme is affine and every 1-morphism `Stack.schemeStack Z ⟶ 𝒴` locally of finite
> presentation, the map `|𝒳 ×_𝒴 Z| → |Z|` is closed.
>
> The base change is again of finite type (**Stacks 06Q7**), its target is again locally
> Noetherian (**Stacks 06R6**), and it again satisfies the hypothesis by
> `AlgebraicGeometry.Stack.discreteExistence_baseChange`. Affineness of `Z` is not used.

```lean
theorem isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_discreteExistence
    (f : 𝒳 ⟶ 𝒴) (hf : IsFiniteType B S hS f)
    (h𝒴 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hlift : ValuativeCriterion.DiscreteExistence B S hS f) :
    ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
      ∀ (g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴),
        IsLocallyOfFinitePresentation B S hS g →
          IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_discreteExistence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosed.lean#L285). The attribute's comment: “the lemma”.

> **Stacks 0H2C.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` with `𝒴`
> locally Noetherian and `f` of finite type. If every valuative square for `f` whose valuation ring
> is a discrete valuation ring admits a dotted arrow after an extension of the fraction field and
> passage to a dominating valuation ring, then `f` is universally closed.
>
> Clause (2) of **Stacks 0H2A** holds for `f` by
> `AlgebraicGeometry.Stack.AlgebraicStacks`
> `.isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_discreteExistence`, and `f` is of
> finite type, hence quasi-compact, so (2) implies (1) of **Stacks 0H2A**.

```lean
theorem universallyClosed_of_discreteExistence
    (f : 𝒳 ⟶ 𝒴) (hf : IsFiniteType B S hS f)
    (h𝒴 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hlift : ValuativeCriterion.DiscreteExistence B S hS f) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_of_discreteExistence'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosedUnconditional.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosedUnconditional.lean#L50). The attribute's comment: “steps 3 and 4 of the proof: closedness on points”.

> **Stacks 0H2C, steps 3 and 4: closedness on points, with nothing assumed.** Let `f : 𝒳 ⟶ 𝒴`
> be a finite-type 1-morphism of algebraic stacks over `S` with `𝒴` locally Noetherian which
> satisfies the discrete existence part of the valuative criterion. Then `f` is closed on points.
>
> This is `AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_of_discreteExistence`.

```lean
alias isClosed_of_discreteExistence'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_discreteExistence'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosedUnconditional.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosedUnconditional.lean#L60). The attribute's comment: “clause (2) of Tag 0H2A for `f`”.

> **Stacks 0H2A, item (2), from the hypothesis of Stacks 0H2C, with nothing assumed.** For
> every object `Z` of the site whose scheme is affine and every 1-morphism
> `Stack.schemeStack Z ⟶ 𝒴` locally of finite presentation, the map `|𝒳 ×_𝒴 Z| → |Z|` is closed.
>
> This is
> `AlgebraicGeometry.Stack.AlgebraicStacks`
> `.isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_discreteExistence`.

```lean
alias isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_discreteExistence'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_discreteExistence'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosedUnconditional.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianValuativeCriterionUniversallyClosedUnconditional.lean#L70). The attribute's comment: “the lemma”.

> **Stacks 0H2C.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` with `𝒴`
> locally Noetherian and `f` of finite type. If every valuative square for `f` whose valuation ring
> is a discrete valuation ring admits a dotted arrow after an extension of the fraction field and
> passage to a dominating valuation ring, then `f` is universally closed.
>
> This is `AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_discreteExistence`.

```lean
alias universallyClosed_of_discreteExistence'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.11, Tag 0CQL](https://stacks.math.columbia.edu/tag/0CQL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
