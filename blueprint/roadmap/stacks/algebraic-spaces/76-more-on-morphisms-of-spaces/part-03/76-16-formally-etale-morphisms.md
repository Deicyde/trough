---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FormallyEtale, AlgebraicGeometry.Space.formallyEtale_iff_etaleCharts, AlgebraicGeometry.Space.formallyEtale_iff_surjectiveEtaleChart, AlgebraicGeometry.Space.FormallyEtale.existsUnique_lift_of_firstOrderThickening, AlgebraicGeometry.Space.formallyEtale_comp, AlgebraicGeometry.Space.formallyEtale_of_isPullback, AlgebraicGeometry.Space.formallyEtale_baseChange, AlgebraicGeometry.Space.formallyEtale_iff_sub_eq_top
statement: formalized
proof: formalized
---

# 76.16 Formally étale morphisms

Section 76.16 of the Stacks Project, [Tag 04GB](https://stacks.math.columbia.edu/tag/04GB). 8 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04GC, a definition

[Tag 04GC](https://stacks.math.columbia.edu/tag/04GC) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallyEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean#L79). The attribute's comment: “formally étale for a morphism of algebraic spaces”. References: SGA 3 XI (1.6), “formally étale”.

> **Stacks 049S, part (2).** Every commutative affine square against a
> square-zero closed immersion admits exactly one lift.

```lean
public abbrev FormallyEtale {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v} (a : F ⟶ G) : Prop
```

## Tag 04GD, a lemma

[Tag 04GD](https://stacks.math.columbia.edu/tag/04GD) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyEtale_iff_etaleCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean#L130). The attribute's comment: “condition (2)”.

> **Stacks 04GD, the equivalence of (1) and (2).** A morphism of algebraic spaces over `S` is
> formally étale exactly when the morphism of schemes underlying every commuting square of étale
> scheme charts is formally étale.

```lean
theorem formallyEtale_iff_etaleCharts
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    FormallyEtale f ↔
      HoldsOnEveryEtaleChart B S hS
        (@_root_.AlgebraicGeometry.FormallyEtale.{u} : MorphismProperty Scheme.{u}) f
```

**`AlgebraicGeometry.Space.formallyEtale_iff_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean#L147). The attribute's comment: “condition (3)”.

> **Stacks 04GD, the equivalence of (1) and (3).** A morphism of algebraic spaces over `S` is
> formally étale exactly when there is one commuting square of étale scheme charts, both chart
> maps surjective, whose underlying morphism of schemes is formally étale.

```lean
theorem formallyEtale_iff_surjectiveEtaleChart
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    FormallyEtale f ↔
      ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (ψ : U ⟶ V),
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Etale.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Etale.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf b ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf b ∧
        yoneda.map ψ ≫ b = a ≫ f ∧
        _root_.AlgebraicGeometry.FormallyEtale
          ((BigFppfOver.toScheme B S hS).map ψ)
```

## Tag 0611, a lemma

[Tag 0611](https://stacks.math.columbia.edu/tag/0611) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallyEtale.existsUnique_lift_of_firstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FormallyEtale.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FormallyEtale.lean#L312).

> **Stacks 0611.** A formally étale morphism `f : X ⟶ Y` of algebraic spaces over `S` admits
> exactly one dotted arrow in a solid square over a first-order thickening `T ⊂ T'` of algebraic
> spaces over `S`. No affineness is assumed of either space of the thickening: the affineness of
> the test objects in the definition of formal étaleness, Stacks 049S part (2), may be dropped.

```lean
theorem FormallyEtale.existsUnique_lift_of_firstOrderThickening
    {X Y T' : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : FormallyEtale f.hom)
    (T : Subfunctor T'.obj) (hT : IsFirstOrderThickening B S hS T' T)
    (a : T.toFunctor ⟶ X.obj) (b : T'.obj ⟶ Y.obj) (hsq : a ≫ f.hom = T.ι ≫ b) :
    ∃! c : T'.obj ⟶ X.obj, T.ι ≫ c = a ∧ c ≫ f.hom = b
```

## Tag 0612, a lemma

[Tag 0612](https://stacks.math.columbia.edu/tag/0612) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.formallyEtale_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean#L66) (StacksFrontier).

## Tag 0613, a lemma

[Tag 0613](https://stacks.math.columbia.edu/tag/0613) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyEtale_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean#L111).

> **Stacks 0613.** A base change of a formally étale morphism of algebraic spaces over `S` is
> formally étale: if `fst, snd, f, g` is a cartesian square of algebraic spaces over `S` and `f`
> is formally étale, then so is `snd`.

```lean
public theorem formallyEtale_of_isPullback (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y Z W : AlgebraicSpaces B S hS} {f : X ⟶ Z} {g : Y ⟶ Z}
    {fst : W ⟶ X} {snd : W ⟶ Y} (sq : IsPullback fst snd f g)
    (hf : FormallyEtale f.hom) : FormallyEtale snd.hom
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.formallyEtale_baseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean#L240), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean#L70) (StacksFrontier).

## Tag 0614, a lemma

[Tag 0614](https://stacks.math.columbia.edu/tag/0614) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyEtale_iff_sub_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean#L335). The attribute's comment: “the equivalence of (1) and (2)”.

> **Stacks 0614, the equivalence of (1) and (2).**  A morphism `f : X ⟶ Y` of algebraic spaces
> over `S` admitting a universal first order thickening `X ⊂ X'` over `Y` is formally étale exactly
> when that thickening is trivial, that is when the smaller space is the whole of `X'`.
>
> The formal unramifiedness of `f` which clause (2) of the source states alongside the triviality
> of the thickening is part of the datum of Stacks 0607 and so does not appear; see the
> implementation notes.

```lean
theorem formallyEtale_iff_sub_eq_top (t : UniversalFirstOrderThickening B S hS f) :
    FormallyEtale f.hom ↔ t.sub = ⊤
```

**`AlgebraicGeometry.Space.isZero_conormalSheaf_of_sub_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean#L358). The attribute's comment: “(2) implies (3)”.

> **Stacks 0614, (2) implies (3).**  If the smaller space of a universal first order
> thickening of `X` over `Y` is the whole ambient space, then the conormal sheaf `𝒞_{X/Y}` of
> Stacks 0607 vanishes.
>
> The inclusion of the smaller space is then invertible, so it is retracted by its inverse and the
> defining ideal of the smaller space vanishes on every étale chart.  The conormal sheaf is an
> inverse image of that ideal sheaf along two morphisms of algebraic spaces, and an inverse image
> of modules preserves zero objects, being a left adjoint.

```lean
theorem isZero_conormalSheaf_of_sub_eq_top (t : UniversalFirstOrderThickening B S hS f)
    (hsub : t.sub = ⊤) : IsZero (conormalSheaf B S hS t)
```

**`AlgebraicGeometry.Space.sub_eq_top_of_isZero_conormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean#L410). The attribute's comment: “(3) implies (2)”.

> **Stacks 0614, (3) implies (2).**  If the conormal sheaf `𝒞_{X/Y}` of Stacks 0607 vanishes
> then the smaller space of the universal first order thickening is the whole ambient space.
>
> This is where Stacks 04CN, part (3) is spent, in the only form the argument needs: for a
> *first-order* thickening the unit `𝓘 ⟶ i_*i^*𝓘` of `i^* ⊣ i_*` is an isomorphism — the
> identification `𝓘/𝓘² = 𝓘` of the source, which
> `AlgebraicGeometry.Space.firstOrderConormalModuleIso` supplies from the essential-image clause
> of Stacks 04CJ — so the vanishing of the conormal module forces the defining ideal of `X` in
> `X'` to vanish on every étale chart.  The injectivity clause of Stacks 03MB
> (`AlgebraicGeometry.Space.le_of_definingIdealSheaf_le`) then returns `t.sub = ⊤`.
>
> It is the converse of `AlgebraicGeometry.Space.isZero_conormalSheaf_of_sub_eq_top`, and the two
> are the content of the equivalence of clauses (2) and (3) of Stacks 0614.  Composed with
> `AlgebraicGeometry.Space.formallyEtale_iff_sub_eq_top` it derives clause (1) from clause (3) as
> well, which is what closes the equivalence of (3) with the other clauses.  The formal
> unramifiedness that clause (3) states alongside the vanishing of the conormal sheaf is part of
> the datum of Stacks 0607 and so does not appear; see the implementation notes.

```lean
theorem sub_eq_top_of_isZero_conormalSheaf (t : UniversalFirstOrderThickening B S hS f)
    (h : IsZero (conormalSheaf B S hS t)) : t.sub = ⊤
```

**`AlgebraicGeometry.Space.formallyEtale_of_isZero_sheafOfDifferentials_of_isZero_conormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean#L571). The attribute's comment: “(4) implies (1), for the datum of Stacks 0607”.

> **Stacks 0614, (4) implies (1), for the datum of Stacks 0607.**  If the sheaf of
> differentials `Ω_{X/Y}` of Stacks 04CT and the conormal sheaf `𝒞_{X/Y}` of Stacks 0607 both
> vanish, then `f : X ⟶ Y` is formally étale.
>
> The `formallyUnramified` field of the datum `t` is **not** an extra hypothesis: it is a
> consequence of the universal property that the rest of `t` carries, by
> `AlgebraicGeometry.Space.formallyUnramified_of_isUniversal`.  The form of this implication in
> which that field never appears is
> `AlgebraicGeometry.Space.formallyEtale_of_isZero_conormalSheaf_of_isUniversal`, and this
> statement follows from it; it is kept because `t` is the shape every other clause of the tag is
> stated in.
>
> The `Ω_{X/Y} = 0` conjunct is again not consumed, for the reason recorded there: the datum
> already forces it.

```lean
theorem formallyEtale_of_isZero_sheafOfDifferentials_of_isZero_conormalSheaf
    (t : UniversalFirstOrderThickening B S hS f)
    (h : IsZero (sheafOfDifferentials B S hS f) ∧ IsZero (conormalSheaf B S hS t)) :
    FormallyEtale f.hom
```

**`AlgebraicGeometry.Space.isZero_sheafOfDifferentials_and_isZero_conormalSheaf_of_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean#L592). The attribute's comment: “(3) implies (4), hence also (1) implies (4) and (2) implies (4) through the proved equivalence of (1), (2) and (3)”.

> **Stacks 0614, (3) implies (4).**  If `f : X ⟶ Y` is formally unramified and the conormal
> sheaf `𝒞_{X/Y}` of Stacks 0607 vanishes, then the sheaf of differentials `Ω_{X/Y}` of
> Stacks 04CT vanishes too and so does `𝒞_{X/Y}`.
>
> Since clauses (1), (2) and (3) are mutually equivalent outright — by
> `AlgebraicGeometry.Space.formallyEtale_iff_sub_eq_top`,
> `AlgebraicGeometry.Space.isZero_conormalSheaf_of_sub_eq_top` and
> `AlgebraicGeometry.Space.sub_eq_top_of_isZero_conormalSheaf` — this is at the same time the
> implication from clause (1) and the implication from clause (2).
>
> The content is the forward direction of Stacks 04G9, which is available with no assumed
> input as `AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_formallyUnramified`; the second
> conjunct is carried through unchanged.

```lean
theorem isZero_sheafOfDifferentials_and_isZero_conormalSheaf_of_formallyUnramified
    (t : UniversalFirstOrderThickening B S hS f)
    (h : FormallyUnramified f.hom ∧ IsZero (conormalSheaf B S hS t)) :
    IsZero (sheafOfDifferentials B S hS f) ∧ IsZero (conormalSheaf B S hS t)
```

**`AlgebraicGeometry.Space.formallyEtale_tfae_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean#L750). The attribute's comment: “the equivalence of the four conditions, with no hypotheses: Stacks 0606 supplies the universal first order thickening”.

> **Stacks 0614, with no hypotheses at all.**  Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S`.  Then the four conditions
>
> 1. `f` is formally étale,
> 2. `f` is formally unramified and the universal first order thickening of `X` over `Y` is `X`,
> 3. `f` is formally unramified and `𝒞_{X/Y} = 0`,
> 4. `Ω_{X/Y} = 0` and `𝒞_{X/Y} = 0`
>
> are equivalent.  Nothing is assumed about `f`: no universal first order thickening is a
> parameter, and no formal unramifiedness is a hypothesis.
>
> **How the thickening leaves the hypotheses.**  Stacks 0607 defines `𝒞_{X/Y}` relative to a
> universal first order thickening, so `𝒞_{X/Y} = 0` is a statement quantified over those
> thickenings; `AlgebraicGeometry.Space.forall_isZero_conormalSheaf_iff_exists` shows the two
> quantifiers agree for a formally unramified `f`, which is the source's definite article.  The
> quantifier written in each clause is the one the source's own reading of that clause supplies:
> clauses (2) and (3) state formal unramifiedness, from which Stacks 0606 produces the thickening,
> so they are read with `∀`; clause (4) does not, and the source's remark that it "only makes
> sense because `Ω_{X/Y} = 0` implies that `𝒞_{X/Y}` is defined" is exactly the assertion that a
> thickening exists, so it is read with `∃`.
>
> **Where Stacks 0606 is spent.**  In the step from (3) to (4), to produce the thickening whose
> conormal sheaf the existential of clause (4) names:
> `AlgebraicGeometry.Space.nonempty_universalFirstOrderThickening` of
> `StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalExistence.lean`.  This is what the
> earlier statements of this file carried as a parameter.
>
> **The backward direction of Stacks 04G9 is still not used, and is not needed.**  The source gets
> formal unramifiedness out of clause (4) through it.  Here clause (4) carries a thickening in its
> existential instead, and a thickening forces formal unramifiedness by
> `AlgebraicGeometry.Space.formallyUnramified_of_isUniversal` — which is also why the step from (4)
> to (1) needs nothing beyond the equivalence of (1) and (3).

```lean
theorem formallyEtale_tfae_unconditional :
    List.TFAE
      [FormallyEtale f.hom,
        FormallyUnramified f.hom ∧
          ∀ t : UniversalFirstOrderThickening B S hS f, t.sub = ⊤,
        FormallyUnramified f.hom ∧
          ∀ t : UniversalFirstOrderThickening B S hS f, IsZero (conormalSheaf B S hS t),
        IsZero (sheafOfDifferentials B S hS f) ∧
          ∃ t : UniversalFirstOrderThickening B S hS f, IsZero (conormalSheaf B S hS t)]
```

**`AlgebraicGeometry.Space.formallyEtale_iff_isZero_sheafOfDifferentials_and_exists_isZero_conormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean, line 781](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFormallyEtale.lean#L781). The attribute's comment: “the equivalence of (1) and (4), with no hypotheses”.

> **Stacks 0614, the equivalence of (1) and (4), with no hypotheses.**  A morphism
> `f : X ⟶ Y` of algebraic spaces over `S` is formally étale exactly when the sheaf of
> differentials `Ω_{X/Y}` of Stacks 04CT vanishes and `X` admits a universal first order thickening
> over `Y` whose conormal sheaf `𝒞_{X/Y}` of Stacks 0607 vanishes.
>
> The existential is the source's reading of clause (4), whose remark on that clause is that
> `𝒞_{X/Y}` has to be defined before the clause says anything; see
> `AlgebraicGeometry.Space.formallyEtale_tfae_unconditional`, of which this is the
> instance at indices 1 and 4.

```lean
theorem formallyEtale_iff_isZero_sheafOfDifferentials_and_exists_isZero_conormalSheaf :
    FormallyEtale f.hom ↔
      IsZero (sheafOfDifferentials B S hS f) ∧
        ∃ t : UniversalFirstOrderThickening B S hS f, IsZero (conormalSheaf B S hS t)
```

## Tag 0615, a lemma

[Tag 0615](https://stacks.math.columbia.edu/tag/0615) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyEtale_of_isUnramified_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean#L177).

> **Stacks 0615.** A flat unramified morphism of algebraic spaces over `S` is formally étale.
>
> Unramifiedness and flatness are conditions on the étale charts of the morphism, and on each
> chart Tag 04FF makes the morphism of schemes formally étale; Tag 04GD assembles those into
> formal étaleness of the morphism of algebraic spaces.

```lean
theorem formallyEtale_of_isUnramified_of_isFlat
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hu : IsUnramified B S hS f) (hflat : IsFlat B S hS f) :
    FormallyEtale f
```

## Tag 0616, a lemma

[Tag 0616](https://stacks.math.columbia.edu/tag/0616) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_iff_isLocallyOfFinitePresentation_and_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleChartCriterion.lean#L195). References: EGA IV (17.6.1), “a) <=> d)”.

> **Stacks 0616.** A morphism of algebraic spaces over `S` is étale if and only if it is
> locally of finite presentation and formally étale.
>
> All three conditions are conditions on the same squares of étale scheme charts — étaleness by
> Tag 03XT, local finite presentation by Tag 03XP and formal étaleness by Tag 04GD — so the
> statement is the scheme-level equivalence of Tag 02HM quantified over the charts, together
> with the distribution of a universal quantifier over a conjunction.

```lean
theorem isEtale_iff_isLocallyOfFinitePresentation_and_formallyEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsEtale B S hS f ↔ (IsLocallyOfFinitePresentation B S hS f ∧ FormallyEtale f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.16, Tag 04GB](https://stacks.math.columbia.edu/tag/04GB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
