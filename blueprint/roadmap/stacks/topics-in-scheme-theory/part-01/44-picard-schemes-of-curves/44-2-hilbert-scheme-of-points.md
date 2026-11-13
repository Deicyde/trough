---
declaration: section
origin: cited
lean: Stacks.Hilbert.hilbertSubobjects, Stacks.Hilbert.hilbertFamilyEquivHilbertSubobjects, Stacks.Hilbert.pullback_mem_hilbertSubobjects, Stacks.Hilbert.hilbertFamilyEquivHilbertSubobjects_map, Stacks.Hilbert.hilbertScheme, Stacks.Hilbert.baseChange, Stacks.Hilbert.hilbertFunctorOfRank, Stacks.Hilbert.HilbertFamily
statement: formalized
proof: formalized
---

# 44.2 Hilbert scheme of points

Section 44.2 of the Stacks Project, [Tag 0B94](https://stacks.math.columbia.edu/tag/0B94). 8 tags here are carried by 24 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B94, the section

[Tag 0B94](https://stacks.math.columbia.edu/tag/0B94) in the Stacks Project.

**`Stacks.Hilbert.hilbertSubobjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean#L72). The attribute's comment: “the set `Hilb^d_{X/S}(T)` of closed subschemes `Z ⊂ X_T` (closed immersions into `X_T` up to isomorphism over `X_T`) with `Z → T` finite locally free of degree `d`”.

> The set `Hilb^d_{X/S}(T)` of closed subschemes `Z ⊂ X_T`, that is subobjects of `X_T = X ×_S T`
> presented by a closed immersion, such that `Z → T` is finite locally free of degree `d`.

```lean
def hilbertSubobjects (X T : Over S) (d : ℕ) :
    Set (Subobject ((Over.pullback T.hom).obj X).left)
```

**`Stacks.Hilbert.hilbertFamilyEquivHilbertSubobjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean#L121). The attribute's comment: “the values of `Stacks.Hilbert.hilbertFunctorOfRank` are the sets `Hilb^d_{X/S}(T)` of closed subschemes of the section: a bijection with `Stacks.Hilbert.hilbertSubobjects`”.

> The degree-`d` Hilbert families in `X` over `T`, which record a closed subscheme of `X_T` by
> its ideal sheaf, are in bijection with the set `Hilb^d_{X/S}(T)` of closed subschemes `Z ⊂ X_T`
> with `Z → T` finite locally free of degree `d`. A family is sent to the closed subscheme it cuts
> out, and a closed subscheme to its ideal sheaf.

```lean
def hilbertFamilyEquivHilbertSubobjects (X T : Over S) (d : ℕ) :
    HilbertFamily X T d ≃ hilbertSubobjects X T d
```

**`Stacks.Hilbert.pullback_mem_hilbertSubobjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean#L160). The attribute's comment: “for `T' ⟶ T` over `S` and `Z ∈ Hilb^d_{X/S}(T)`, the base change `Z_{T'} ⊂ X_{T'}` lies in `Hilb^d_{X/S}(T')`”.

> For a morphism `T' ⟶ T` of schemes over `S` and a `Z ∈ Hilb^d_{X/S}(T)`, the base change
> `Z_{T'} ⊂ X_{T'}`, the pullback of `Z` along `X_{T'} ⟶ X_T`, is an element of
> `Hilb^d_{X/S}(T')`.

```lean
theorem pullback_mem_hilbertSubobjects (X : Over S) {T' T : Over S} {d : ℕ} (g : T' ⟶ T)
    {Z : Subobject ((Over.pullback T.hom).obj X).left} (hZ : Z ∈ hilbertSubobjects X T d) :
    (Subobject.pullback (familyBaseChangeMap X g)).obj Z ∈ hilbertSubobjects X T' d
```

**`Stacks.Hilbert.hilbertFamilyEquivHilbertSubobjects_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean#L173). The attribute's comment: “the functor `Hilb^d_{X/S}` acts on morphisms `T' ⟶ T` by base change of the closed subscheme `Z ⊂ X_T` to `Z_{T'} ⊂ X_{T'}`”.

> The functor `Hilb^d_{X/S} : (Sch/S)ᵒᵖ ⥤ Sets` acts on a morphism `T' ⟶ T` by base change of the
> closed subscheme: under the identification of its values with `Hilb^d_{X/S}(T)`, the image of `Z`
> is the pullback of `Z` along `X_{T'} ⟶ X_T`.

```lean
theorem hilbertFamilyEquivHilbertSubobjects_map (X : Over S) (d : ℕ) {T' T : Over S}
    (g : T' ⟶ T) (Z : (hilbertFunctorOfRank X d).obj (op T)) :
    (hilbertFamilyEquivHilbertSubobjects X T' d ((hilbertFunctorOfRank X d).map g.op Z) :
        Subobject _) =
      (Subobject.pullback (familyBaseChangeMap X g)).obj
        (hilbertFamilyEquivHilbertSubobjects X T d Z)
```

**`Stacks.Hilbert.hilbertScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedSubschemes.lean#L191). The attribute's comment: “the notation `\underline{Hilb}^d_{X/S}` for the representing scheme”.

> The scheme `\underline{Hilb}^d_{X/S}` over `S` representing the degree-`d` Hilbert functor,
> when that functor is representable by a scheme.

```lean
abbrev hilbertScheme (X : Over S) (d : ℕ) [(hilbertFunctorOfRank X d).IsRepresentable] :
    Over S
```

**`Stacks.Hilbert.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheaf.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheaf.lean#L156). The attribute's comment: “base change of families: that for a morphism `T' ⟶ T` over `S` and a `Z` in `Hilb^d_{X/S}(T)` the base change `Z_{T'} ⊂ X_{T'}` lies in `Hilb^d_{X/S}(T')`. This is the part of the section that requires an argument; the set `Hilb^d_{X/S}(T)` is `Stacks.Hilbert.HilbertFamily` and the functor is `Stacks.Hilbert.hilbertFunctorOfRank`”.

> **Stacks Project, Section 0B94.** The base change of a degree-`d` Hilbert family along a
> morphism of `S`-schemes: the closed subscheme cut out by the pullback of its ideal sheaf.
>
> This is the section's assertion that for a morphism `T' ⟶ T` over `S` and a
> `Z ∈ Hilb^d_{X/S}(T)` the base change `Z_{T'} ⊂ X_{T'}` is again an element of
> `Hilb^d_{X/S}(T')` — the type below says exactly that, and it is the one part of the section
> that requires an argument. That the resulting closed subscheme really is `Z_{T'}`, that is that
> its ideal sheaf is the pullback of `Z`'s, is `Stacks.Hilbert.baseChange_ideal`. The set
> `Hilb^d_{X/S}(T)` is `Stacks.Hilbert.HilbertFamily` and the functor is
> `Stacks.Hilbert.hilbertFunctorOfRank`.

```lean
def baseChange {S : Scheme.{u}} (X : Over S) {T' T : Over S} {d : ℕ} (g : T' ⟶ T)
    (Z : HilbertFamily X T d) : HilbertFamily X T' d
```

**`Stacks.Hilbert.hilbertFunctorOfRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheaf.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheaf.lean#L211). The attribute's comment: “the functor `Hilb^d_{X/S} : (Sch/S)ᵒᵖ ⥤ Sets` itself, acting on morphisms by base change of families. Its values, the sets `Hilb^d_{X/S}(T)`, are `Stacks.Hilbert.HilbertFamily`, which carries the other part of this section”.

> **Stacks Project, Section 0B94.** The degree-`d` Hilbert functor of points of `X` over `S`.
> It sends an `S`-scheme `T` to the degree-`d` Hilbert families in `X` over `T` and a morphism to
> the base change of families.
>
> This is the functor `Hilb^d_{X/S} : (Sch/S)ᵒᵖ ⥤ Sets` of the section, for an arbitrary morphism
> `X ⟶ S` of schemes and an arbitrary degree `d`. Its values are
> `Stacks.Hilbert.HilbertFamily`, which carries the other part of the section; that base change
> of a degree-`d` family is again one, which is what makes the assignment a functor, is
> `Stacks.Hilbert.baseChange` together with `Stacks.Hilbert.baseChange_id` and
> `Stacks.Hilbert.baseChange_comp`.

```lean
def hilbertFunctorOfRank {S : Scheme.{u}} (X : Over S) (d : ℕ) : (Over S)ᵒᵖ ⥤ Type u
```

**`Stacks.Hilbert.HilbertFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorOfPoints.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorOfPoints.lean#L94). The attribute's comment: “the set `Hilb^d_{X/S}(T)`: the closed subschemes of `X_T` that are finite locally free of degree `d` over `T`. The functor these sets are the values of is `Stacks.Hilbert.hilbertFunctorOfRank`, which carries the other part of this section”.

> **Stacks Project, Section 0B94.** A degree-`d` Hilbert family in `X` over `T`: an ideal
> sheaf on `X ×_S T` whose associated closed subscheme is finite locally free of rank `d` over
> `T`.
>
> This is the value `Hilb^d_{X/S}(T)` of the degree-`d` Hilbert functor, which the section
> displays as the set of closed subschemes `Z ⊂ X_T` such that `Z → T` is finite locally free of
> degree `d`. The functor itself, with its action by base change, is
> `Stacks.Hilbert.hilbertFunctorOfRank`.

```lean
structure HilbertFamily {S : Scheme.{u}} (X T : Over S) (d : ℕ)
```

## Tag 0B95, a lemma

[Tag 0B95](https://stacks.math.columbia.edu/tag/0B95) in the Stacks Project.

**`Stacks.Hilbert.isSheaf_fpqcTopology_hilbertFunctorOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcGluing.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcGluing.lean#L373).

> **Stacks Project, Tag 0B95.** The degree-`d` Hilbert functor of points of `X` over `S`
> satisfies the sheaf property for the fpqc topology on the schemes over `S`.

```lean
theorem isSheaf_fpqcTopology_hilbertFunctorOfRank {S : Scheme.{u}} (X : Over S) (d : ℕ) :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over S) (hilbertFunctorOfRank X d)
```

**`Stacks.Hilbert.isSeparated_fpqcTopology_hilbertFunctorOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheaf.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheaf.lean#L337). The attribute's comment: “the separatedness clause of the sheaf property”.

> **Stacks Project, Tag 0B95, separatedness.** The degree-`d` Hilbert functor of points of `X`
> over `S` is separated for the fpqc topology on the schemes over `S`: a section has at most one
> amalgamation along any fpqc covering sieve.

```lean
theorem isSeparated_fpqcTopology_hilbertFunctorOfRank {S : Scheme.{u}} (X : Over S) (d : ℕ) :
    Presieve.IsSeparated (Scheme.fpqcTopology.over S) (hilbertFunctorOfRank X d)
```

**`Stacks.Hilbert.existsUnique_hilbertFamily_of_mem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheafProperty.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorFpqcSheafProperty.lean#L70). The attribute's comment: “the sheaf property in the shape of Tag 022G: unique amalgamation for an arbitrary fpqc covering family, with compatibility over the pairwise fibre products”.

> **Stacks Project, Tag 0B95, in the shape of the definition it refers to, Tag 022G.** Let
> `X` be a scheme over `S`, let `d` be a natural number, and let `{g i : Y i ⟶ T}` be a family of
> morphisms of `S`-schemes whose underlying family of morphisms of schemes is an fpqc covering of
> `T`. Then a collection of degree-`d` Hilbert families `Z i` in `X` over `Y i` whose base changes
> to the fibre products `Y i ×_T Y j` agree is the collection of base changes of a unique
> degree-`d` Hilbert family in `X` over `T`.

```lean
theorem existsUnique_hilbertFamily_of_mem_fpqcPrecoverage {S : Scheme.{u}} (X : Over S) (d : ℕ)
    {T : Over S} {ι : Type*} {Y : ι → Over S} (g : ∀ i, Y i ⟶ T)
    (hcov : Presieve.ofArrows (fun i ↦ (Y i).left) (fun i ↦ (g i).left) ∈
      Scheme.fpqcPrecoverage T.left)
    (Z : ∀ i, HilbertFamily X (Y i) d)
    (hZ : ∀ i j, baseChange X (pullback.fst (g i) (g j)) (Z i) =
      baseChange X (pullback.snd (g i) (g j)) (Z j)) :
    ∃! V : HilbertFamily X T d, ∀ i, baseChange X (g i) V = Z i
```

## Tag 0B96, a lemma

[Tag 0B96](https://stacks.math.columbia.edu/tag/0B96) in the Stacks Project.

**`Stacks.Hilbert.isLimitPreserving_hilbertFunctorOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorLimitPreserving.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorLimitPreserving.lean#L404).

> **Stacks Project, Tag 0B96.** If `X ⟶ S` is of finite presentation, then the degree-`d`
> Hilbert functor of points of `X` over `S` is limit preserving: it turns every cofiltered inverse
> limit of affine `S`-schemes into a filtered colimit of sets.

```lean
theorem isLimitPreserving_hilbertFunctorOfRank (X : Over S) (d : ℕ)
    (hX : FinitePresentation X.hom) :
    Scheme.IsLimitPreserving S (hilbertFunctorOfRank X d)
```

## Tag 0B97, a lemma

[Tag 0B97](https://stacks.math.columbia.edu/tag/0B97) in the Stacks Project.

**`Stacks.Hilbert.exists_closedSubschemeRepresentingHilbertFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedImmersion.lean, line 708](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorClosedImmersion.lean#L708). The attribute's comment: “if the degree-d Hilbert functor of Y is representable by a scheme, so is that of X, by a closed subscheme of it, compatibly with the universal families”.

> **Stacks Project, Tag 0B97.** Let `i : X ⟶ Y` be a closed immersion of schemes over `S`.
> If the degree-`d` Hilbert functor of `Y` is represented by a scheme `H_Y` over `S`, then the
> degree-`d` Hilbert functor of `X` is represented by a scheme `H_X` over `S` together with a
> closed immersion `H_X ⟶ H_Y` over which the universal families correspond.

```lean
public theorem exists_closedSubschemeRepresentingHilbertFunctor {S : Scheme.{u}}
    {X Y : Over S} (i : X ⟶ Y) [IsClosedImmersion i.left] (d : ℕ)
    (H_Y : Over S) (hY : RepresentsHilbertFunctorOfRank Y H_Y d) :
    Nonempty (ClosedSubschemeRepresentingHilbertFunctor i d H_Y hY)
```

## Tag 0B98, a lemma

[Tag 0B98](https://stacks.math.columbia.edu/tag/0B98) in the Stacks Project.

**`Stacks.Hilbert.isSeparated_of_representsHilbertFunctorOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorSeparated.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorSeparated.lean#L330).

> **Stacks Project, Tag 0B98.** Let `X ⟶ S` be separated and let `d` be a natural number.  If
> the degree-`d` Hilbert functor of `X` is represented by a scheme `H` over `S`, then `H ⟶ S` is
> separated.
>
> The separatedness of `X ⟶ S` which the source assumes is not used:
> `Stacks.Hilbert.isSeparated_of_representsHilbertFunctorOfRank'` is the same conclusion for an
> arbitrary `X ⟶ S`, and this is that statement specialised to the hypotheses of the source.

```lean
public theorem isSeparated_of_representsHilbertFunctorOfRank {S : Scheme.{u}}
    (X H : Over S) (d : ℕ) [IsSeparated X.hom]
    (hH : RepresentsHilbertFunctorOfRank X H d) :
    IsSeparated H.hom
```

## Tag 0B99, a lemma

[Tag 0B99](https://stacks.math.columbia.edu/tag/0B99) in the Stacks Project.

**`Stacks.Hilbert.exists_representsHilbertFunctorOfRank_of_isAffine_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorAffineRepresentableUnconditional.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorAffineRepresentableUnconditional.lean#L58). The attribute's comment: “the degree-`d` Hilbert functor of an affine scheme over an affine base is representable by a scheme over `S`”.

> Let `X ⟶ S` be a morphism of affine schemes and let `d` be a natural number. Then the
> degree-`d` Hilbert functor of points of `X` over `S` is representable by a scheme over `S`.

```lean
theorem exists_representsHilbertFunctorOfRank_of_isAffine_of_isAffine {S : Scheme.{u}}
    [IsAffine S] (X : Over S) [IsAffine X.left] (d : ℕ) :
    Nonempty (Σ H : Over S, RepresentsHilbertFunctorOfRank X H d)
```

## Tag 0B9A, a proposition

[Tag 0B9A](https://stacks.math.columbia.edu/tag/0B9A) in the Stacks Project.

**`Stacks.Hilbert.nonempty_representsHilbertFunctorOfRank_of_exists_isAffineOpen_forall_mem_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorRepresentableAmbient.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/HilbertFunctorRepresentableAmbient.lean#L327). The attribute's comment: “corrected statement, recorded in `errata.md`: as printed the proposition is false at `d = 1` (`Stacks.Hilbert.not_nonempty_representsHilbertFunctorOfRank_one`), so `X ⟶ S` is assumed separated when `d = 1`; for `d ≠ 1` the hypothesis is the source's”.

> **Stacks Project, Tag 0B9A, corrected at `d = 1`.** Let `X ⟶ S` be a morphism of schemes and
> let `d ≥ 0`. Assume that for every `s ∈ S` and every tuple of points `x₁, …, x_d` of the fibre
> `X_s` there is an affine open `U ⊆ X` with `x₁, …, x_d ∈ U`, and assume moreover that `X ⟶ S` is
> separated if `d = 1`. Then the degree-`d` Hilbert functor of points `Hilb^d_{X/S}` is
> representable by a scheme over `S`.
>
> This is the source's proposition with the correction recorded for Tag 0B9A in `errata.md`: as
> printed, the proposition is false at `d = 1`. There the `d`-tuple hypothesis holds for every
> morphism of schemes (`Stacks.Hilbert.exists_isAffineOpen_forall_mem_of_le_one`), while no scheme
> represents the degree-`1` Hilbert functor of the affine line with the origin doubled over affine
> `1`-space (`Stacks.Hilbert.not_nonempty_representsHilbertFunctorOfRank_one`). For every `d ≠ 1`
> the hypothesis is the source's, point for point, and separatedness is not assumed.
>
> For `d ≠ 1` this is
> `nonempty_representsHilbertFunctorOfRank_of_exists_isAffineOpen_forall_mem_of_ne_one`.
> At `d = 1` the source's proof runs with the first sentence of its footnote: since `X ⟶ S` is
> separated, a degree-`1` family in an open of `X` is closed in `X ×_S T`
> (`Stacks.Hilbert.familiesClosedInAmbient_of_isSeparated`), and the gluing assembly
> `Stacks.Hilbert.nonempty_representsHilbertFunctorOfRank_of_familiesClosedInAmbient` applies.

```lean
theorem nonempty_representsHilbertFunctorOfRank_of_exists_isAffineOpen_forall_mem_of_isSeparated
    (X : Over S) (d : ℕ) (hsep : d = 1 → IsSeparated X.hom)
    (hX : ∀ (s : S) (x : Fin d → X.left), (∀ i, X.hom.base (x i) = s) →
      ∃ U : X.left.Opens, IsAffineOpen U ∧ ∀ i, x i ∈ U) :
    Nonempty (Σ H : Over S, RepresentsHilbertFunctorOfRank X H d)
```

## Tag 0B9B, a remark

[Tag 0B9B](https://stacks.math.columbia.edu/tag/0B9B) in the Stacks Project.

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L141). The attribute's comment: “case (1), the source is quasi-affine”.

> If `X` is quasi-affine then every finite subset of a fibre of any `f : X ⟶ S` lies in an
> affine open of `X`.

```lean
theorem hasAffineFinitePointsInFibres_of_isQuasiAffine [Scheme.IsQuasiAffine X] (f : X ⟶ S) :
    HasAffineFinitePointsInFibres f
```

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_isLocallyProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L149). The attribute's comment: “case (4), the morphism is locally projective”.

> A locally projective morphism satisfies the fibrewise affineness condition.

```lean
theorem hasAffineFinitePointsInFibres_of_isLocallyProjective {f : X ⟶ S}
    (hf : IsLocallyProjective f) : HasAffineFinitePointsInFibres f
```

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L160). The attribute's comment: “case (5), an ample invertible sheaf on the source”.

> If `X` carries an ample invertible sheaf then every finite subset of a fibre of any
> `f : X ⟶ S` lies in an affine open of `X`.

```lean
theorem hasAffineFinitePointsInFibres_of_isAmple (f : X ⟶ S) (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L) :
    HasAffineFinitePointsInFibres f
```

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_modulesIsAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L170). The attribute's comment: “case (5), an ample invertible sheaf on the source, at `Scheme.Modules.IsAmple`”.

> If `X` carries an invertible sheaf that is ample in the sense of
> `AlgebraicGeometry.Scheme.Modules.IsAmple`, then every finite subset of a fibre of any
> `f : X ⟶ S` lies in an affine open of `X`.

```lean
theorem hasAffineFinitePointsInFibres_of_modulesIsAmple (f : X ⟶ S) (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L]
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple X L) :
    HasAffineFinitePointsInFibres f
```

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L182). The attribute's comment: “case (6), an f-ample invertible sheaf, at `Stacks.RelativeAmple.IsRelativelyAmple`”.

> A morphism admitting a relatively ample invertible sheaf satisfies the fibrewise affineness
> condition.

```lean
theorem hasAffineFinitePointsInFibres_of_isRelativelyAmple {f : X ⟶ S} (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    HasAffineFinitePointsInFibres f
```

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_modulesIsRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L195). The attribute's comment: “case (6), an f-ample invertible sheaf, at `Stacks.RelativeAmple.IsRelativelyAmple`”.

> A morphism admitting a relatively ample sheaf `L`, invertible in the sense of
> `AlgebraicGeometry.SheafOfModules.IsInvertible`, satisfies the fibrewise affineness
> condition.

```lean
theorem hasAffineFinitePointsInFibres_of_modulesIsRelativelyAmple {f : X ⟶ S} (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L]
    (hL : Stacks.RelativeAmple.IsRelativelyAmple f L) :
    HasAffineFinitePointsInFibres f
```

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_isRelativelyVeryAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L207). The attribute's comment: “case (7), an f-very ample invertible sheaf”.

> A morphism admitting an invertible sheaf that is relatively very ample in the sense of
> `Stacks.Tag01VMRelativeVeryAmple.IsRelativelyVeryAmple` satisfies the fibrewise affineness
> condition.

```lean
theorem hasAffineFinitePointsInFibres_of_isRelativelyVeryAmple {f : X ⟶ S} (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.Tag01VMRelativeVeryAmple.IsRelativelyVeryAmple f L) :
    HasAffineFinitePointsInFibres f
```

**`Stacks.HilbertFibreAffineOpen.hasAffineFinitePointsInFibres_of_isRelativelyVeryAmpleTwistOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L220). The attribute's comment: “case (7), an f-very ample invertible sheaf, at the Tag 01VM predicate”.

> A morphism admitting an invertible sheaf that is relatively very ample in the sense of
> `Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple`, with twist `𝒪_{𝐏(E)}(1)`, satisfies the
> fibrewise affineness condition.

```lean
theorem hasAffineFinitePointsInFibres_of_isRelativelyVeryAmpleTwistOne {f : X ⟶ S} (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f L) :
    HasAffineFinitePointsInFibres f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.hasAffineFinitePointsInFibres_of_isQuasiAffineHom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FreeGroupSchemeQuotient.lean#L168), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L67) (StacksFrontier): “case (2), the morphism is quasi-affine”.
- [`AlgebraicGeometry.hasAffineFinitePointsInFibres_of_isQuasiProjective`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FreeGroupSchemeQuotient.lean#L193), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HilbertFibreAffineOpen/Basic.lean#L69) (StacksFrontier): “case (3), the morphism is quasi-projective”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 44.2, Tag 0B94](https://stacks.math.columbia.edu/tag/0B94)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
