---
declaration: section
origin: cited
lean: TopologicalRing.completionOver_isCountablyGenerated_nhds_zero, TopologicalRing.completionOver_isCountablyAdmissible, TopologicalRing.completionOver_isWeaklyAdic, TopologicalRing.completionOver_exists_fg_isAdic, TopologicalRing.completionOver_isNoetherianAdic, TopologicalRing.LocalizationDiagram, TopologicalRing.PropertyIsLocal, AlgebraicGeometry.FormalSpace.hasPropertyAfterTargetCover_of_everyAffineEtaleDiagram
statement: formalized
proof: formalized
---

# 87.21 Morphisms and continuous ring maps

Section 87.21 of the Stacks Project, [Tag 0ANA](https://stacks.math.columbia.edu/tag/0ANA). 18 tags here are carried by 58 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ANB, a lemma

[Tag 0ANB](https://stacks.math.columbia.edu/tag/0ANB) in the Stacks Project.

**`TopologicalRing.completionOver_isCountablyGenerated_nhds_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 545](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L545). The attribute's comment: “completion_in_sub_countable”.

> Completion over a weakly admissible ring with a countable fundamental system of open
> ideals again has a countable fundamental system of open ideals.

```lean
public lemma completionOver_isCountablyGenerated_nhds_zero
    {B A : Type*} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] (f : B →+* A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (hBcount : (nhds (0 : B)).IsCountablyGenerated) :
    (nhds (0 : CompletionOver f)).IsCountablyGenerated
```

**`TopologicalRing.completionOver_isCountablyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L569). The attribute's comment: “completion_in_sub_cic”.

> Completion over a countably admissible ring is again countably admissible.

```lean
public theorem completionOver_isCountablyAdmissible
    {B A : Type*} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] (f : B →+* A)
    (hB : IsCountablyAdmissible B) :
    IsCountablyAdmissible (CompletionOver f)
```

**`TopologicalRing.completionOver_isWeaklyAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L589). The attribute's comment: “completion_in_sub_weakly_adic”.

> Completion relative to a weakly admissible, weakly adic ring is weakly adic.

```lean
public theorem completionOver_isWeaklyAdic
    {B A : Type*} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] (f : B →+* A)
    (hB : TopologicalRing.IsWeaklyAdmissible B) [TopologicalRing.IsWeaklyAdic B] :
    TopologicalRing.IsWeaklyAdic (CompletionOver f)
```

**`TopologicalRing.completionOver_exists_fg_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 609](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L609). The attribute's comment: “completion_in_sub_adic_star”.

> Completion relative to a weakly admissible adic-star ring is again adic-star: its
> topology is defined by a finitely generated ideal.

```lean
public theorem completionOver_exists_fg_isAdic
    {B A : Type*} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A]
    (f : B →+* A) (hB : TopologicalRing.IsWeaklyAdmissible B)
    (hB_adicStar : ∃ I : Ideal B, I.FG ∧ _root_.IsAdic I) :
    ∃ J : Ideal (CompletionOver f), J.FG ∧ _root_.IsAdic J
```

**`TopologicalRing.completionOver_isNoetherianAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOverNoetherian.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOverNoetherian.lean#L69). The attribute's comment: “completion_in_sub_noetherian”.

> **Stacks 0ANB (5).** Let `B` be an adic Noetherian topological ring and let `f : B →+* A` be
> a ring map, `A` carrying no topology.  If `A` is Noetherian then the completion of `A` over `B`,
> the limit of the rings `A ⧸ JA` over the weak ideals of definition `J` of `B`, is again an adic
> Noetherian topological ring.
>
> The topology of the completion is adic by the clause of this lemma for `WAdm^{adic*}`, which
> applies because an ideal of definition of the Noetherian ring `B` is finitely generated.  The
> completion is then the `IA`-adic completion of `A` for `I` an ideal of definition of `B`, hence
> Noetherian by Tag 0316.

```lean
public theorem completionOver_isNoetherianAdic {B : Type u} {A : Type v}
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [CommRing A] (f : B →+* A) (hB : IsNoetherianAdic B) (hA : IsNoetherianRing A) :
    IsNoetherianAdic (CompletionOver f)
```

## Tag 0CBA, a situation

[Tag 0CBA](https://stacks.math.columbia.edu/tag/0CBA) in the Stacks Project.

**`TopologicalRing.LocalizationDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L53). The attribute's comment: “localization diagram”.

> A commutative localization diagram of countably indexed weakly admissible rings, with
> étale horizontal maps and continuous vertical maps.

```lean
public structure LocalizationDiagram
    (A B A' B' : Type u)
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [CommRing A'] [CommRing B']
```

**`TopologicalRing.PropertyIsLocal`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L146). The attribute's comment: “local property”.

> A property of morphisms of countably indexed weakly admissible rings is local if it
> ascends along completed étale localization diagrams, descends along faithfully flat ones,
> and is preserved by finite products of targets. The optional subclass parameter restricts
> all four corners of each diagram and every ring in the finite-product family.

```lean
public structure PropertyIsLocal
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A],
      (B →+* A) → Prop)
    (C : ∀ (R : Type u) [CommRing R] [TopologicalSpace R] [IsTopologicalRing R]
      [IsLinearTopology R R], Prop := IsCountablyWeaklyAdmissible) : Prop
```

## Tag 0ANG, a lemma

[Tag 0ANG](https://stacks.math.columbia.edu/tag/0ANG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyAfterTargetCover_of_everyAffineEtaleDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalProperty.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalProperty.lean#L194). The attribute's comment: “condition (1) implies condition (2), with Stacks 0AJ3 as a hypothesis”.

> **Stacks 0ANG, condition (1) implies condition (2).** If `P` holds on every affine étale
> diagram over `f`, then the atlas of the target and the atlases of the fibre products of its
> members with the source witness condition (2).
>
> The hypothesis `hpb` is the assertion of Stacks 0AJ3 that the fibre product of the chart
> `V ⟶ Y` with `f` is a formal algebraic space; the library does not yet carry Stacks 0AJ3, so it
> is carried here as a hypothesis for the fibre products the statement needs.

```lean
theorem hasPropertyAfterTargetCover_of_everyAffineEtaleDiagram
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hpb : ∀ (V : FppfSheaf B S hS) (v : V ⟶ Y), IsAffineFormalAlgebraicSpace B S hS V →
      IsRepresentableEtale B S hS v → IsFormalAlgebraicSpace B S hS (pullback v f))
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS C P f) :
    HasPropertyAfterTargetCover B S hS C P f
```

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalProperty.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalProperty.lean#L274). The attribute's comment: “condition (3) implies condition (1), with the refinement of the covering (Stacks 0AJ2 and quasi-compactness of an affine formal algebraic space) and the locality axioms of Situation 0CBA read through Stacks 0AN8 and Stacks 0AN9 carried as hypotheses”.

> **Stacks 0ANG, condition (3) implies condition (1).** If `P` holds on an affine étale
> covering of the source of `f`, whose members factor through affine formal algebraic spaces
> representable étale over the target, then `P` holds on every affine étale diagram over `f`.
>
> Given a diagram as in condition (1), the covering is refined against it by `href`; axiom (1)
> of locality carries `P` from the members of the covering to the refined charts, and axioms (2)
> and (3) descend it along the finite covering of the chart `U₀` so obtained.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hasc : ChartPropertyAscendsAlongAffineEtale B S hS C P)
    (hdesc : ChartPropertyDescendsAlongFiniteAffineEtaleCover B S hS C P)
    (href : HasEtaleRefinementOfSourceCover B S hS f)
    (hf : HasPropertyAfterSourceCover B S hS C P f) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS C P f
```

**`AlgebraicGeometry.FormalSpace.hasProperty_tfae_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCountablyIndexed.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCountablyIndexed.lean#L161).

> **Stacks 0ANG.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of locally
> countably indexed formal algebraic spaces over `S`. Let `P` be a local property of morphisms of
> `WAdm^count`, the countably indexed weakly admissible topological rings (Situation 0CBA: `P` is
> invariant under isomorphism of source and target, and satisfies the three axioms 0AND, 0ANE and
> 0ANF of `TopologicalRing.PropertyIsLocal`). The following are equivalent:
>
> 1. for every commutative diagram with `U` and `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to a
>    morphism of `WAdm^count` with property `P`;
> 2. there is a covering `{Vⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Uᵢ ⟶ Vⱼ ×_Y X}` as in Definition 0AIM such that each `Uᵢ ⟶ Vⱼ` corresponds to a morphism of
>    `WAdm^count` with property `P`;
> 3. there are a covering `{Uᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Uᵢ ⟶ Vᵢ ⟶ Y` where `Vᵢ` is an affine formal algebraic space, `Vᵢ ⟶ Y` is representable by
>    algebraic spaces and étale, and `Uᵢ ⟶ Vᵢ` corresponds to a morphism of `WAdm^count` with
>    property `P`.
>
> "Corresponds to a morphism of `WAdm^count` with property `P`" is
> `AlgebraicGeometry.FormalSpace.HasPropertyOnAffineChartMap`: `P` holds on every continuous
> homomorphism presenting the morphism of formal spectra through rings of `WAdm^count`.
>
> This is `AlgebraicGeometry.FormalSpace.hasProperty_tfae_isCountablyWeaklyAdmissible_of_etale` at
> the étale case of Stacks 0AJH,
> `AlgebraicGeometry.FormalSpace.representableEtaleOverAffineIsFormal`.

```lean
theorem hasProperty_tfae_of_isLocallyCountablyIndexed
    (hP : TopologicalRing.PropertyIsLocal P TopologicalRing.IsCountablyWeaklyAdmissible)
    (hsrc : PropertyIsInvariantUnderSourceIso.{u} TopologicalRing.IsCountablyWeaklyAdmissible P)
    (htgt : PropertyIsInvariantUnderTargetIsoOn.{u} TopologicalRing.IsCountablyWeaklyAdmissible P)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y) :
    List.TFAE
      [ HasPropertyOnEveryAffineEtaleDiagram B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible P f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f ]
```

**`AlgebraicGeometry.FormalSpace.hasProperty_tfae_of_isLocallyCountablyIndexed_of_isLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCountablyIndexedIsLocal.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCountablyIndexedIsLocal.lean#L69). The attribute's comment: “the equivalence of conditions (1), (2) and (3) for a morphism of locally countably indexed formal algebraic spaces and a local property of WAdm^count in the sense of Situation 0CBA (invariance under isomorphism of source and target, and the axioms 0AND, 0ANE, 0ANF)”.

> **Stacks 0ANG.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of locally
> countably indexed formal algebraic spaces over `S`. Let `P` be a local property of morphisms of
> `WAdm^count` in the sense of Situation 0CBA: invariant under isomorphism of source and target in
> `WAdm^count`, and satisfying the axioms 0AND, 0ANE and 0ANF; this is
> `TopologicalRing.PropertyIsLocal' P TopologicalRing.IsCountablyWeaklyAdmissible`. The following
> are equivalent:
>
> 1. for every commutative diagram with `U` and `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to a
>    morphism of `WAdm^count` with property `P`;
> 2. there is a covering `{Vⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Uᵢ ⟶ Vⱼ ×_Y X}` as in Definition 0AIM such that each `Uᵢ ⟶ Vⱼ` corresponds to a morphism of
>    `WAdm^count` with property `P`;
> 3. there are a covering `{Uᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Uᵢ ⟶ Vᵢ ⟶ Y` where `Vᵢ` is an affine formal algebraic space, `Vᵢ ⟶ Y` is representable by
>    algebraic spaces and étale, and `Uᵢ ⟶ Vᵢ` corresponds to a morphism of `WAdm^count` with
>    property `P`.
>
> This is `AlgebraicGeometry.FormalSpace.hasProperty_tfae_of_isLocallyCountablyIndexed`, whose
> invariance under isomorphism of sources and of targets is derived from the invariance clause of
> Situation 0CBA.

```lean
theorem hasProperty_tfae_of_isLocallyCountablyIndexed_of_isLocal
    (hP : TopologicalRing.PropertyIsLocal' P TopologicalRing.IsCountablyWeaklyAdmissible)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y) :
    List.TFAE
      [ HasPropertyOnEveryAffineEtaleDiagram B S hS
          TopologicalRing.IsCountablyWeaklyAdmissible P f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f ]
```

**`AlgebraicGeometry.FormalSpace.hasPropertyAfterTargetCover_of_everyAffineEtaleDiagram_of_formal'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableSourceRefined.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableSourceRefined.lean#L52). The attribute's comment: “condition (1) implies condition (2)”.

> **Stacks 0ANG, condition (1) implies condition (2).** If `P` holds on every affine étale
> diagram over a morphism `f : X ⟶ Y` of formal algebraic spaces, then the atlas of the target
> and the atlases of the fibre products of its members with the source witness condition (2).
>
> The fibre products are formal algebraic spaces by **Stacks 0AJ3**, which this library proves
> outright for a base which is a formal algebraic space:
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_pullback_chart_of_isFormalAlgebraicSpace`
> asks only that `X`, `Y` and the chart `V` be formal algebraic spaces, which `hX`, `hY` and the
> atlas of `Y` give. It therefore supplies the hypothesis `hpb` of
> `AlgebraicGeometry.FormalSpace.hasPropertyAfterTargetCover_of_everyAffineEtaleDiagram` with no
> standing hypothesis of its own, and nothing is assumed here beyond the setting of the tag.

```lean
theorem hasPropertyAfterTargetCover_of_everyAffineEtaleDiagram_of_formal'
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS C P f) :
    HasPropertyAfterTargetCover B S hS C P f
```

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SourceCoverImpliesEveryDiagram.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SourceCoverImpliesEveryDiagram.lean#L428). The attribute's comment: “condition (3) implies condition (1), for a morphism of locally countably indexed formal algebraic spaces and a local property of WAdm^count, as the source states it: hP and hPiso together are Situation 0CBA's notion of a local property”.

> **Stacks 0ANG, condition (3) implies condition (1).** Let `f : X ⟶ Y` be a morphism of
> locally countably indexed formal algebraic spaces over `S` and let `P` be a local property of
> morphisms of `WAdmᶜᵒᵘⁿᵗ` (Situation 0CBA: `hP` for the three axioms and `hPiso` for "invariant
> under isomorphism of source and target in this category"). If there are an affine étale covering
> `{Uᵢ ⟶ X}` as in Definition 0AIM and factorizations `Uᵢ ⟶ Vᵢ ⟶ Y` through affine formal
> algebraic spaces representable étale over `Y` with `P` on each `Uᵢ ⟶ Vᵢ`, then for every
> commutative square with affine formal algebraic spaces `U`, `V` and representable étale maps
> `U ⟶ X`, `V ⟶ Y`, the morphism `U ⟶ V` has `P`.
>
> This is `hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover_of_hasChartsPresentedByClass` at
> the class `WAdmᶜᵒᵘⁿᵗ`, whose three closure conditions are theorems: membership of the class is weak
> admissibility with a countable fundamental system of open ideals by definition, closure under
> completion along an étale ring map is two clauses of **Stacks 0ANB**, and closure under isomorphism
> is `TopologicalRing.isCountablyWeaklyAdmissible_of_ringEquiv`. The charts of `X` and `Y` are
> presented by rings of the class because `X` and `Y` are locally countably indexed.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover_of_isLocallyCountablyIndexed
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hP : TopologicalRing.PropertyIsLocal P TopologicalRing.IsCountablyWeaklyAdmissible)
    (hPiso : ∀ {B A B' A' : Type u}
      [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
      [CommRing B'] [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
      [CommRing A'] [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
      (eB : B ≃+* B') (eA : A ≃+* A'), Continuous eB → Continuous eB.symm →
      Continuous eA → Continuous eA.symm → ∀ (f : B →+* A), Continuous f →
      TopologicalRing.IsCountablyWeaklyAdmissible B →
      TopologicalRing.IsCountablyWeaklyAdmissible A →
      TopologicalRing.IsCountablyWeaklyAdmissible B' →
      TopologicalRing.IsCountablyWeaklyAdmissible A' →
      (P f ↔ P ((eA.toRingHom.comp f).comp eB.symm.toRingHom)))
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (hf : HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
      f
```

**`AlgebraicGeometry.FormalSpace.hasPropertyAfterSourceCover_of_afterTargetCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TautMorphismRepresentability.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TautMorphismRepresentability.lean#L131). The attribute's comment: “condition (2) implies condition (3)”.

> **Stacks 0ANG, condition (2) implies condition (3).** A covering of the target together
> with coverings of the fibre products of its members with the source compose to a covering of
> the source whose members factor through the chart of the target they came from, by the map
> condition (2) puts `P` on.

```lean
theorem hasPropertyAfterSourceCover_of_afterTargetCover {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : HasPropertyAfterTargetCover B S hS C P f) :
    HasPropertyAfterSourceCover B S hS C P f
```

## Tag 0ANH, a remark

[Tag 0ANH](https://stacks.math.columbia.edu/tag/0ANH) in the Stacks Project.

**`TopologicalRing.propertyIsLocalAdicStar_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteria.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteria.lean#L142). The attribute's comment: “the first half, the definition of a local property of morphisms of WAdm^{adic*}, with the three axioms of Situation 0CBA quantified over the diagrams and finite families of WAdm^{adic*} exactly as in the source”.

> **The first half of Stacks 0ANH, in the source's words.** A property `P` of morphisms of
> `WAdm^{adic*}` is a local property, `TopologicalRing.PropertyIsLocalAdicStar P`, exactly when the
> three axioms of Situation 0CBA hold for morphisms of `WAdm^{adic*}`:
>
> 1. for every diagram of Situation 0CBA with `A` and `B` in `WAdm^{adic*}`, `P(φ) ⟹ P(φ')`;
> 2. for every such diagram with `A → A'` faithfully flat, `P(φ') ⟹ P(φ)`;
> 3. if `P(B → Aᵢ)` for finitely many `Aᵢ` of `WAdm^{adic*}`, then `P(B → ∏ᵢ Aᵢ)`.
>
> `TopologicalRing.PropertyIsLocal` asks in addition that the two completions `(A')^∧` and
> `(B')^∧` of a diagram be in `WAdm^{adic*}`, and that the rings of axiom (3) be weakly admissible
> with a countable fundamental system of neighbourhoods of zero. Neither is an extra condition:
> the completions are in `WAdm^{adic*}` by Stacks 0ANB (4),
> `AlgebraicGeometry.FormalSpace.classIsStableUnderEtaleCompletion_isAdicStar`, and every ring of
> `WAdm^{adic*}` is weakly admissible and countably indexed. This equivalence records that
> `TopologicalRing.PropertyIsLocalAdicStar` is the source's notion.

```lean
theorem propertyIsLocalAdicStar_iff
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) :
    PropertyIsLocalAdicStar.{u} P ↔
      (∀ {A B A' B' : Type u}
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
        [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
        [CommRing A'] [CommRing B'] (D : LocalizationDiagram A B A' B'),
        IsAdicStar A → IsAdicStar B → P D.map → P D.completedMap) ∧
      (∀ {A B A' B' : Type u}
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
        [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
        [CommRing A'] [CommRing B'] (D : LocalizationDiagram A B A' B'),
        IsAdicStar A → IsAdicStar B → D.toA'.FaithfullyFlat → P D.completedMap → P D.map) ∧
      (∀ {B : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [IsLinearTopology B B] {ι : Type u} [Fintype ι] (A : ι → Type u)
        [∀ i, CommRing (A i)] [∀ i, TopologicalSpace (A i)]
        [∀ i, IsTopologicalRing (A i)] [∀ i, IsLinearTopology (A i) (A i)]
        (f : ∀ i, B →+* A i), (∀ i, Continuous (f i)) → IsAdicStar B →
        (∀ i, IsAdicStar (A i)) → (∀ i, P (f i)) → P (RingHom.pi f))
```

**`AlgebraicGeometry.FormalSpace.hasProperty_tfae_isAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteria.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteria.lean#L297). The attribute's comment: “the second half: the variant of Stacks 0ANG for morphisms between locally adic* formal algebraic spaces over S, at a local property of morphisms of WAdm^{adic*} invariant under isomorphism of source and target (the standing hypothesis of Situation 0CBA)”.

> **The second half of Stacks 0ANH: the variant of Stacks 0ANG for morphisms between locally
> adic\* formal algebraic spaces.** Let `f : X ⟶ Y` be a morphism of locally adic\* formal
> algebraic spaces over `S` and let `P` be a local property of morphisms of `WAdm^{adic*}`
> (`TopologicalRing.PropertyIsLocalAdicStar P`), invariant under isomorphism of source and target
> as Situation 0CBA stipulates. The following are equivalent:
>
> 1. for every commutative diagram with `U`, `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to a
>    morphism of `WAdm^{adic*}` with property `P`;
> 2. there is a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` as in Definition 0AIM such that each `Xⱼᵢ ⟶ Yⱼ` corresponds to a
>    morphism of `WAdm^{adic*}` with property `P`;
> 3. there are a covering `{Xᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Xᵢ ⟶ Yᵢ ⟶ Y` with `Yᵢ` an affine formal algebraic space, `Yᵢ ⟶ Y` representable by
>    algebraic spaces and étale, and `Xᵢ ⟶ Yᵢ` corresponding to a morphism of `WAdm^{adic*}` with
>    property `P`.
>
> This is `AlgebraicGeometry.FormalSpace.hasProperty_tfae_isAdicStar_of_inputs` with the étale
> case of Stacks 0AJH supplied by
> `AlgebraicGeometry.FormalSpace.representableEtaleOverAffineIsFormal`.

```lean
theorem hasProperty_tfae_isAdicStar
    (hP : TopologicalRing.PropertyIsLocalAdicStar.{u} P)
    (hsrc : PropertyIsInvariantUnderSourceIso.{u} TopologicalRing.IsAdicStar P)
    (htgt : PropertyIsInvariantUnderTargetIsoOn.{u} TopologicalRing.IsAdicStar P)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y) :
    List.TFAE
      [ HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar P f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar P f ]
```

**`TopologicalRing.propertyIsLocalAdicStarUpToIso_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteriaUpToIso.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteriaUpToIso.lean#L83). The attribute's comment: “the first half, the definition of a local property of morphisms of WAdm^{adic*}, in the source's words: axioms (1), (2), (3) of Situation 0CBA quantified over the diagrams and finite families of WAdm^{adic*}, the completed corners being any limits”.

> **The first half of Stacks 0ANH, in the source's words.** A property `P` of morphisms of
> `WAdm^{adic*}` is a local property, `TopologicalRing.PropertyIsLocalAdicStarUpToIso P`, exactly
> when the three axioms of Situation 0CBA hold for morphisms of `WAdm^{adic*}`:
>
> 1. for every diagram of Situation 0CBA with `A` and `B` in `WAdm^{adic*}`, and any rings `Â`,
>    `B̂` isomorphic to the limits `lim A'/IA'`, `lim B'/JB'`, `P(φ) ⟹ P(φ')`;
> 2. for every such diagram with `A → A'` faithfully flat, `P(φ') ⟹ P(φ)`;
> 3. if `P(B → Aᵢ)` for finitely many `Aᵢ` of `WAdm^{adic*}`, then `P(B → ∏ᵢ Aᵢ)`.
>
> The definition asks in addition that `Â` and `B̂` be in `WAdm^{adic*}`, and that the rings
> of the third axiom be weakly admissible and countably indexed. Neither is an extra condition. The
> completions are in `WAdm^{adic*}` by Stacks 0ANB (4),
> `AlgebraicGeometry.FormalSpace.classIsStableUnderEtaleCompletion_isAdicStar`, and so are `Â`
> and `B̂`, which are isomorphic to them. Every ring of `WAdm^{adic*}` is weakly admissible and
> countably indexed.

```lean
theorem propertyIsLocalAdicStarUpToIso_iff
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) :
    PropertyIsLocalAdicStarUpToIso.{u} P ↔
      (∀ {A B A' B' Ahat Bhat : Type u}
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
        [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
        [CommRing A'] [CommRing B']
        [CommRing Ahat] [TopologicalSpace Ahat] [IsTopologicalRing Ahat]
        [IsLinearTopology Ahat Ahat]
        [CommRing Bhat] [TopologicalSpace Bhat] [IsTopologicalRing Bhat]
        [IsLinearTopology Bhat Bhat]
        (D : LocalizationDiagram A B A' B')
        (eA : CompletionOver D.toA' ≃+* Ahat) (eB : CompletionOver D.toB' ≃+* Bhat),
        Continuous eA → Continuous eA.symm → Continuous eB → Continuous eB.symm →
        IsAdicStar A → IsAdicStar B → P D.map →
          P ((eA.toRingHom.comp D.completedMap).comp eB.symm.toRingHom)) ∧
      (∀ {A B A' B' Ahat Bhat : Type u}
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
        [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
        [CommRing A'] [CommRing B']
        [CommRing Ahat] [TopologicalSpace Ahat] [IsTopologicalRing Ahat]
        [IsLinearTopology Ahat Ahat]
        [CommRing Bhat] [TopologicalSpace Bhat] [IsTopologicalRing Bhat]
        [IsLinearTopology Bhat Bhat]
        (D : LocalizationDiagram A B A' B')
        (eA : CompletionOver D.toA' ≃+* Ahat) (eB : CompletionOver D.toB' ≃+* Bhat),
        Continuous eA → Continuous eA.symm → Continuous eB → Continuous eB.symm →
        IsAdicStar A → IsAdicStar B → D.toA'.FaithfullyFlat →
          P ((eA.toRingHom.comp D.completedMap).comp eB.symm.toRingHom) → P D.map) ∧
      (∀ {B : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [IsLinearTopology B B] {ι : Type u} [Fintype ι] (A : ι → Type u)
        [∀ i, CommRing (A i)] [∀ i, TopologicalSpace (A i)]
        [∀ i, IsTopologicalRing (A i)] [∀ i, IsLinearTopology (A i) (A i)]
        (f : ∀ i, B →+* A i), (∀ i, Continuous (f i)) → IsAdicStar B →
        (∀ i, IsAdicStar (A i)) → (∀ i, P (f i)) → P (RingHom.pi f))
```

**`AlgebraicGeometry.FormalSpace.hasProperty_tfae_of_propertyIsLocalAdicStarUpToIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteriaUpToIso.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarChartCriteriaUpToIso.lean#L170). The attribute's comment: “the second half: the variant of Stacks 0ANG for morphisms between locally adic* formal algebraic spaces over S, at any local property of morphisms of WAdm^{adic*}”.

> **The second half of Stacks 0ANH: the variant of Stacks 0ANG for morphisms between locally
> adic\* formal algebraic spaces.** Let `f : X ⟶ Y` be a morphism of locally adic\* formal
> algebraic spaces over `S` and let `P` be a local property of morphisms of `WAdm^{adic*}`
> (`TopologicalRing.PropertyIsLocalAdicStarUpToIso P`). The following are equivalent:
>
> 1. for every commutative diagram with `U`, `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to a
>    morphism of `WAdm^{adic*}` with property `P`;
> 2. there is a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` as in Definition 0AIM such that each `Xⱼᵢ ⟶ Yⱼ` corresponds to a
>    morphism of `WAdm^{adic*}` with property `P`;
> 3. there are a covering `{Xᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Xᵢ ⟶ Yᵢ ⟶ Y` with `Yᵢ` an affine formal algebraic space, `Yᵢ ⟶ Y` representable by
>    algebraic spaces and étale, and `Xᵢ ⟶ Yᵢ` corresponding to a morphism of `WAdm^{adic*}` with
>    property `P`.
>
> There is no hypothesis on `P` beyond locality. Its invariance under isomorphism of source and
> target, which the proof of Stacks 0ANG uses, is derived from axiom (1) of Situation 0CBA by
> `propertyIsInvariantUnderSourceIso_of_propertyIsLocalAdicStarUpToIso` and
> `propertyIsInvariantUnderTargetIsoOn_of_propertyIsLocalAdicStarUpToIso`. The equivalence is
> then `AlgebraicGeometry.FormalSpace.hasProperty_tfae_isAdicStar`.

```lean
theorem hasProperty_tfae_of_propertyIsLocalAdicStarUpToIso
    (hP : TopologicalRing.PropertyIsLocalAdicStarUpToIso.{u} P)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y) :
    List.TFAE
      [ HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar P f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar P f ]
```

**`AlgebraicGeometry.FormalSpace.propertyIsInvariantUnderSourceIso_of_propertyIsLocalAdicStarUpToIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyUpToIsoInvariance.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyUpToIsoInvariance.lean#L184). The attribute's comment: “a local property of morphisms of WAdm^{adic*} is invariant under isomorphism of sources, by axiom (1), an isomorphism being etale; used by the variant of 0ANG”.

> A local property of morphisms of `WAdm^{adic*}` is invariant under isomorphism of sources.
> The variant of Stacks 0ANG in Stacks 0ANH uses this, and it follows from axiom (1) of
> Situation 0CBA.

```lean
theorem propertyIsInvariantUnderSourceIso_of_propertyIsLocalAdicStarUpToIso
    (hP : TopologicalRing.PropertyIsLocalAdicStarUpToIso.{u} P) :
    PropertyIsInvariantUnderSourceIso.{u} TopologicalRing.IsAdicStar P
```

**`AlgebraicGeometry.FormalSpace.propertyIsInvariantUnderTargetIsoOn_of_propertyIsLocalAdicStarUpToIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyUpToIsoInvariance.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyUpToIsoInvariance.lean#L195). The attribute's comment: “a local property of morphisms of WAdm^{adic*} is invariant under isomorphism of targets, by axiom (1), an isomorphism being etale; used by the variant of 0ANG”.

> A local property of morphisms of `WAdm^{adic*}` is invariant under isomorphism of targets.
> The variant of Stacks 0ANG in Stacks 0ANH uses this, and it follows from axiom (1) of
> Situation 0CBA.

```lean
theorem propertyIsInvariantUnderTargetIsoOn_of_propertyIsLocalAdicStarUpToIso
    (hP : TopologicalRing.PropertyIsLocalAdicStarUpToIso.{u} P) :
    PropertyIsInvariantUnderTargetIsoOn.{u} TopologicalRing.IsAdicStar P
```

**`TopologicalRing.AdicStarPropertyIsLocal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L178). The attribute's comment: “adic_star_local_property”.

> A property of morphisms of weakly admissible adic-star rings is local when it satisfies
> the three locality axioms of `TopologicalRing.PropertyIsLocal` within that subcategory: the
> rings tested are those whose topology is the `I`-adic topology of a finitely generated ideal
> `I`.

```lean
public abbrev AdicStarPropertyIsLocal (P : ∀ {B A : Type u} [CommRing B]
    [TopologicalSpace B] [IsTopologicalRing B] [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

**`TopologicalRing.PropertyIsLocalAdicStar`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L202). The attribute's comment: “the first half, the definition, at the source's class of rings: the adic topological rings -- hence complete and separated -- possessing a finitely generated ideal of definition”.

> A property of morphisms of `WAdm^{adic*}` is *local* when the three locality axioms of
> `TopologicalRing.PropertyIsLocal` hold for morphisms of that subcategory.
>
> `WAdm^{adic*}` is the full subcategory of `WAdm` whose objects are the adic topological rings
> possessing a finitely generated ideal of definition. Its objects are complete and separated:
> `TopologicalRing.IsAdic` is pre-adicness together with `TopologicalRing.IsComplete`, which is
> completeness for the canonical uniformity together with the Hausdorff condition.
>
> This agrees with `TopologicalRing.AdicStarPropertyIsLocal`, by
> `TopologicalRing.adicStarPropertyIsLocal_iff_propertyIsLocalAdicStar`.

```lean
public abbrev PropertyIsLocalAdicStar (P : ∀ {B A : Type u} [CommRing B]
    [TopologicalSpace B] [IsTopologicalRing B] [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

**`TopologicalRing.PropertyIsLocalAdicStarUpToIso`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesUpToIso.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesUpToIso.lean#L155). The attribute's comment: “the first half, the definition of a local property of morphisms of WAdm^{adic*}: axioms (1), (2), (3) of Situation 0CBA for morphisms of WAdm^{adic*}, the completed corners of the diagram being any limits lim A'/IA', lim B'/JB'”.

> A property `P` of morphisms of `WAdm^{adic*}`, the adic topological rings possessing a
> finitely generated ideal of definition, is local when axioms (1), (2) and (3) of Situation 0CBA
> hold for morphisms of `WAdm^{adic*}`. The completed corners of the diagrams of axioms (1) and (2)
> are any rings isomorphic to the inverse limits.

```lean
public abbrev PropertyIsLocalAdicStarUpToIso (P : ∀ {B A : Type u} [CommRing B]
    [TopologicalSpace B] [IsTopologicalRing B] [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0ANI, a remark

[Tag 0ANI](https://stacks.math.columbia.edu/tag/0ANI) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasProperty_tfae_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianChartCriteria.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianChartCriteria.lean#L190). The attribute's comment: “the variant of Lemma 0ANG for morphisms between locally Noetherian formal algebraic spaces over S: the equivalence of its three conditions, for a local property of morphisms of WAdm^Noeth”.

> **Stacks 0ANI, the variant of Stacks 0ANG for locally Noetherian formal algebraic spaces.**
> Let `S` be a scheme, let `f : X ⟶ Y` be a morphism of locally Noetherian formal algebraic spaces
> over `S`, and let `P` be a local property of morphisms of `WAdm^{Noeth}`: axioms (1), (2) and (3)
> of Situation 0CBA hold for morphisms of `WAdm^{Noeth}`
> (`TopologicalRing.PropertyIsLocalNoetherianUpToIso`). The following are equivalent:
>
> 1. for every commutative diagram with `U` and `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to a
>    morphism of `WAdm^{Noeth}` with property `P`;
> 2. there is a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` as in Definition 0AIM such that each `Xⱼᵢ ⟶ Yⱼ` corresponds to a
>    morphism of `WAdm^{Noeth}` with property `P`;
> 3. there are a covering `{Xᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Xᵢ ⟶ Yᵢ ⟶ Y` with `Yᵢ` an affine formal algebraic space, `Yᵢ ⟶ Y` representable by
>    algebraic spaces and étale, and `Xᵢ ⟶ Yᵢ` corresponding to a morphism of `WAdm^{Noeth}` with
>    property `P`.
>
> "Corresponds to a morphism of `WAdm^{Noeth}` with property `P`" is
> `AlgebraicGeometry.FormalSpace.HasPropertyOnAffineChartMap` at the class
> `TopologicalRing.IsNoetherianAdic`. This is
> `AlgebraicGeometry.FormalSpace.hasProperty_tfae_isNoetherianAdic_of_isInvariantUnderIso`, with the
> invariance of `P` under isomorphism of source and of target derived from axiom (1).

```lean
theorem hasProperty_tfae_of_isLocallyNoetherian
    (hP : TopologicalRing.PropertyIsLocalNoetherianUpToIso.{u} P)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y) :
    List.TFAE
      [ HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsNoetherianAdic P f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsNoetherianAdic P f ]
```

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SourceCoverImpliesEveryDiagramNoetherian.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SourceCoverImpliesEveryDiagramNoetherian.lean#L172). The attribute's comment: “the variant of Lemma 0ANG for morphisms of locally Noetherian formal algebraic spaces, condition (3) implies condition (1); hP and hPiso together are the local property of WAdm^Noeth”.

> **The variant of Stacks 0ANG for locally Noetherian formal algebraic spaces (Remark 0ANI),
> condition (3) implies condition (1).** Let `f : X ⟶ Y` be a morphism of locally Noetherian
> formal algebraic spaces over `S` and let `P` be a local property of morphisms of `WAdmᴺᵒᵉᵗʰ`
> (Remark 0ANI: `hP` for the three axioms of Situation 0CBA on `WAdmᴺᵒᵉᵗʰ` and `hPiso` for
> "invariant under isomorphism of source and target in this category"). If there are an affine
> étale covering `{Uᵢ ⟶ X}` as in Definition 0AIM and factorizations `Uᵢ ⟶ Vᵢ ⟶ Y` through
> affine formal algebraic spaces representable étale over `Y` with `P` on each `Uᵢ ⟶ Vᵢ`, then
> for every commutative square with affine formal algebraic spaces `U`, `V` and representable
> étale maps `U ⟶ X`, `V ⟶ Y`, the morphism `U ⟶ V` has `P`.
>
> This is
> `AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover_of_hasChartsPresentedByClass`
> at the class `WAdmᴺᵒᵉᵗʰ`: its rings are weakly admissible with a countable fundamental system
> of open ideals, being adic; the class is closed under completion along an étale ring map by
> clause (5) of Stacks 0ANB, an étale algebra over a Noetherian ring being Noetherian; and it is
> closed under isomorphism of topological rings. The charts of `X` and `Y` are presented by rings
> of the class by
> `AlgebraicGeometry.FormalSpace.hasChartsPresentedByClass_of_isLocallyNoetherian`.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_of_afterSourceCover_of_isLocallyNoetherian
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hP : TopologicalRing.PropertyIsLocalNoetherian P)
    (hPiso : ∀ {B A B' A' : Type u}
      [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
      [CommRing B'] [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
      [CommRing A'] [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
      (eB : B ≃+* B') (eA : A ≃+* A'), Continuous eB → Continuous eB.symm →
      Continuous eA → Continuous eA.symm → ∀ (f : B →+* A), Continuous f →
      TopologicalRing.IsNoetherianAdic B → TopologicalRing.IsNoetherianAdic A →
      TopologicalRing.IsNoetherianAdic B' → TopologicalRing.IsNoetherianAdic A' →
      (P f ↔ P ((eA.toRingHom.comp f).comp eB.symm.toRingHom)))
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hf : HasPropertyAfterSourceCover B S hS TopologicalRing.IsNoetherianAdic P f) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P f
```

**`TopologicalRing.PropertyIsLocalNoetherian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L219). The attribute's comment: “local_property_noetherian”.

> A morphism property of Noetherian adic topological rings is local if it ascends along
> completed étale localization diagrams, descends along faithfully flat ones, and is preserved
> by finite products of targets.

```lean
public abbrev PropertyIsLocalNoetherian
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A],
      (B →+* A) → Prop) : Prop
```

**`TopologicalRing.PropertyIsLocalNoetherianUpToIso`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesUpToIso.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesUpToIso.lean#L168). The attribute's comment: “the definition of a local property of morphisms of WAdm^Noeth: axioms (1), (2), (3) of Situation 0CBA for morphisms of WAdm^Noeth, the completed corners of the diagram being any limits lim A'/IA', lim B'/JB'”.

> A property `P` of morphisms of `WAdm^{Noeth}`, the adic topological rings whose underlying
> ring is Noetherian, is local when axioms (1), (2) and (3) of Situation 0CBA hold for morphisms of
> `WAdm^{Noeth}`. The completed corners of the diagrams of axioms (1) and (2) are any rings
> isomorphic to the inverse limits.

```lean
public abbrev PropertyIsLocalNoetherianUpToIso (P : ∀ {B A : Type u} [CommRing B]
    [TopologicalSpace B] [IsTopologicalRing B] [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBC, a situation

[Tag 0GBC](https://stacks.math.columbia.edu/tag/0GBC) in the Stacks Project.

**`TopologicalRing.IsStableUnderBaseChange`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L237).

> A local property of morphisms of countably indexed weakly admissible rings
> that is preserved by completed tensor-product base change.

```lean
public structure IsStableUnderBaseChange
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBD, a lemma

[Tag 0GBD](https://stacks.math.columbia.edu/tag/0GBD) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasProperty_pullback_snd_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedPullbackLocalProperty.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedPullbackLocalProperty.lean#L117).

> **Stacks 0GBD.** Let `S` be a scheme. Let `P` be a local property of morphisms of
> `WAdm^count` which is stable under base change. Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of
> locally countably indexed formal algebraic spaces over `S`. If `f` satisfies the equivalent
> conditions of Stacks 0ANG, then so does `pr₂ : X ×_Y Z ⟶ Z`.
>
> `P` being local in the sense of Situation 0CBA is `TopologicalRing.PropertyIsLocal P`, which
> `TopologicalRing.IsStableUnderBaseChange P` (Stacks 0GBC) contains, together with the
> invariance under isomorphism of source and target with which Situation 0CBA opens, `hsrc` and
> `htgt`. The conditions of Stacks 0ANG for `f` are equivalent by
> `hasProperty_tfae_of_isLocallyCountablyIndexed`, and `hf` is condition (1). The conclusion is
> that `X ×_Y Z` is locally countably indexed (Stacks 0GBB, clause (1)), so that the conditions
> of Stacks 0ANG are equivalent for `pr₂`, and that `pr₂` satisfies all three of them.

```lean
theorem hasProperty_pullback_snd_of_isLocallyCountablyIndexed
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hP : TopologicalRing.IsStableUnderBaseChange.{u} P)
    (hsrc : PropertyIsInvariantUnderSourceIso.{u}
      TopologicalRing.IsCountablyWeaklyAdmissible P)
    (htgt : PropertyIsInvariantUnderTargetIsoOn.{u}
      TopologicalRing.IsCountablyWeaklyAdmissible P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (hZ : IsLocallyCountablyIndexed B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS
      TopologicalRing.IsCountablyWeaklyAdmissible P f) :
    IsLocallyCountablyIndexed B S hS (pullback f g) ∧
      HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasProperty_pullback_snd_of_isLocalUpToIso_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedPullbackLocalPropertyUpToIso.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedPullbackLocalPropertyUpToIso.lean#L58).

> Let `S` be a scheme. Let `P` be a local property of morphisms of `WAdm^count` which is
> stable under base change. Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally countably
> indexed formal algebraic spaces over `S`. If `f` satisfies the equivalent conditions of Stacks
> 0ANG, then so does `pr₂ : X ×_Y Z ⟶ Z`.
>
> Here `hloc` says that `P` is local in the sense of Situation 0CBA, `hP` that it is stable under
> base change (Situation 0GBC), and `hf` is condition (1) of Stacks 0ANG for `f`. The conclusion is
> that `X ×_Y Z` is locally countably indexed (Stacks 0GBB, clause (1)) and that `pr₂` satisfies
> all three conditions of Stacks 0ANG.

```lean
theorem hasProperty_pullback_snd_of_isLocalUpToIso_of_isLocallyCountablyIndexed
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hloc : TopologicalRing.PropertyIsLocalUpToIso.{u} P)
    (hP : TopologicalRing.IsStableUnderBaseChange.{u} P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (hZ : IsLocallyCountablyIndexed B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS
      TopologicalRing.IsCountablyWeaklyAdmissible P f) :
    IsLocallyCountablyIndexed B S hS (pullback f g) ∧
      HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasProperty_tfae_pullback_snd_of_isLocalUpToIso_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedPullbackLocalPropertyUpToIso.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedPullbackLocalPropertyUpToIso.lean#L89). The attribute's comment: “the conditions of Stacks 0ANG for f taken as any one of them, and the conclusion including their equivalence for pr₂”.

> Let `S` be a scheme. Let `P` be a local property of morphisms of `WAdm^count` which is
> stable under base change. Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally countably
> indexed formal algebraic spaces over `S`. If `f` satisfies one, hence all, of the equivalent
> conditions of Stacks 0ANG, then `X ×_Y Z` is locally countably indexed, the conditions of Stacks
> 0ANG are equivalent for `pr₂ : X ×_Y Z ⟶ Z`, and `pr₂` satisfies all three of them.

```lean
theorem hasProperty_tfae_pullback_snd_of_isLocalUpToIso_of_isLocallyCountablyIndexed
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hloc : TopologicalRing.PropertyIsLocalUpToIso.{u} P)
    (hP : TopologicalRing.IsStableUnderBaseChange.{u} P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (hZ : IsLocallyCountablyIndexed B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS
        TopologicalRing.IsCountablyWeaklyAdmissible P f ∨
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f ∨
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f) :
    IsLocallyCountablyIndexed B S hS (pullback f g) ∧
      List.TFAE
        [ HasPropertyOnEveryAffineEtaleDiagram B S hS
            TopologicalRing.IsCountablyWeaklyAdmissible P (pullback.snd f g),
          HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
            (pullback.snd f g),
          HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
            (pullback.snd f g) ] ∧
      HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P
        (pullback.snd f g)
```

## Tag 0GBE, a remark

[Tag 0GBE](https://stacks.math.columbia.edu/tag/0GBE) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.pullback_snd_hasProperty_of_isLocallyAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarBaseChangeVariant.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarBaseChangeVariant.lean#L134). The attribute's comment: “the second half, the variant of Lemma 0GBD for morphisms between locally adic* formal algebraic spaces: for a local property P of morphisms of WAdm^{adic*} (Remark 0ANH, with the invariance under isomorphism of source and target that Situation 0CBA stipulates) which is stable under base change in the sense of the first half, TopologicalRing.PropertyIsStableUnderBaseChangeAdicStar, and morphisms f : X -> Y, g : Z -> Y of locally adic* formal algebraic spaces, if f satisfies condition (1) of the equivalent conditions of Stacks 0ANG then X x_Y Z is locally adic* and pr2 : X x_Y Z -> Z satisfies all three”.

> **Stacks 0GBE, second half: the variant of Lemma 0GBD for locally adic\* formal algebraic
> spaces.** Let `P` be a local property of morphisms of `WAdm^{adic*}` (Remark 0ANH), invariant
> under isomorphism of source and target as Situation 0CBA stipulates, and stable under base
> change in the sense of the first half of Remark 0GBE. Let `f : X ⟶ Y` and `g : Z ⟶ Y` be
> morphisms of locally adic\* formal algebraic spaces over `S`. If `f` satisfies the equivalent
> conditions of Stacks 0ANG for `P` — here condition (1), that `P` holds on every affine étale
> diagram over `f` — then `X ×_Y Z` is again locally adic\* (Stacks 0GBB (4)), so that the
> conditions of Stacks 0ANG make sense for `pr₂ : X ×_Y Z ⟶ Z`, and `pr₂` satisfies all three of
> them.

```lean
theorem pullback_snd_hasProperty_of_isLocallyAdicStar
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hP : TopologicalRing.PropertyIsStableUnderBaseChangeAdicStar.{u} P)
    (hsrc : PropertyIsInvariantUnderSourceIso.{u} TopologicalRing.IsAdicStar P)
    (htgt : PropertyIsInvariantUnderTargetIsoOn.{u} TopologicalRing.IsAdicStar P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y)
    (hZ : IsLocallyAdicStar B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P f) :
    IsLocallyAdicStar B S hS (pullback f g) ∧
      HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P
        (pullback.snd f g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar P (pullback.snd f g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasProperty_pullback_snd_of_isLocalUpToIso_of_isLocallyAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarPullbackLocalPropertyUpToIso.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarPullbackLocalPropertyUpToIso.lean#L81). The attribute's comment: “the second half, the variant of Lemma 0GBD for morphisms between locally adic* formal algebraic spaces: for a local property P of morphisms of WAdm^{adic*} in the sense of Remark 0ANH (hloc, TopologicalRing.PropertyIsLocalAdicStarUpToIso) which is stable under base change in the sense of the first half (hP, TopologicalRing.PropertyIsStableUnderBaseChangeAdicStar), and morphisms f : X -> Y, g : Z -> Y of locally adic* formal algebraic spaces, if f satisfies the equivalent conditions of the variant of Stacks 0ANG then X x_Y Z is locally adic* and pr2 : X x_Y Z -> Z satisfies all three”.

> **Stacks 0GBE, second half: the variant of Lemma 0GBD for locally adic\* formal algebraic
> spaces.** Let `P` be a local property of morphisms of `WAdm^{adic*}` (Remark 0ANH) which is
> stable under base change in the sense of the first half of Remark 0GBE. Let `f : X ⟶ Y` and
> `g : Z ⟶ Y` be morphisms of locally adic\* formal algebraic spaces over `S`. If `f` satisfies the
> equivalent conditions of the variant of Stacks 0ANG of Remark 0ANH for `P`, then so does
> `pr₂ : X ×_Y Z ⟶ Z`.
>
> `P` being local in the sense of Remark 0ANH is `hloc`, and `P` being stable under base change is
> `hP`. The conditions for `f` are equivalent by
> `AlgebraicGeometry.FormalSpace.hasProperty_tfae_isAdicStar`, and `hf` is condition (1). The
> conclusion is that `X ×_Y Z` is again locally adic\*, so that those conditions are equivalent for
> `pr₂`, and that `pr₂` satisfies all three of them.

```lean
theorem hasProperty_pullback_snd_of_isLocalUpToIso_of_isLocallyAdicStar
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hloc : TopologicalRing.PropertyIsLocalAdicStarUpToIso.{u} P)
    (hP : TopologicalRing.PropertyIsStableUnderBaseChangeAdicStar.{u} P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y)
    (hZ : IsLocallyAdicStar B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P f) :
    IsLocallyAdicStar B S hS (pullback f g) ∧
      HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P
        (pullback.snd f g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar P (pullback.snd f g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar P (pullback.snd f g)
```

**`TopologicalRing.AdicStarPropertyIsStableUnderBaseChange`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L264). The attribute's comment: “adic_star_base_change_stability”.

> A local property of morphisms of weakly admissible adic-star rings that is
> preserved by completed tensor-product base change.

```lean
public structure AdicStarPropertyIsStableUnderBaseChange
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

**`TopologicalRing.PropertyIsStableUnderBaseChangeAdicStar`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L317). The attribute's comment: “the first half, the definition of stability under base change, at the source's class of rings: the morphisms range over WAdm^{adic*}, the adic topological rings -- hence complete and separated -- possessing a finitely generated ideal of definition, and the locality of P is read in the same subcategory by TopologicalRing.PropertyIsLocalAdicStar. The well definedness the remark cites, that the completed tensor product is again an object of WAdm^{adic*} by Lemma 87.4.12, is TopologicalRing.isAdicStar_completedTensorProduct”.

> A local property `P` of morphisms of `WAdm^{adic*}` is *stable under base change* when,
> for every pair of morphisms `B → A` and `B → C` of `WAdm^{adic*}`, `P (B → A)` implies
> `P (C → A ⊗̂_B C)`.
>
> `WAdm^{adic*}` is the full subcategory of `WAdm` whose objects are the adic, hence complete and
> separated, topological rings possessing a finitely generated ideal of definition, and the
> locality of `P` is `TopologicalRing.PropertyIsLocalAdicStar`, read in the same subcategory. That
> `A ⊗̂_B C` lies in `WAdm^{adic*}` is `TopologicalRing.isAdicStar_completedTensorProduct`.
>
> This agrees with `TopologicalRing.AdicStarPropertyIsStableUnderBaseChange`, by
> `TopologicalRing.adicStarPropertyIsStableUnderBaseChange_iff`.

```lean
public structure PropertyIsStableUnderBaseChangeAdicStar
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

Declarations registered for the tag:

- [`TopologicalRing.completedTensorProduct_isWeaklyAdmissible`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L951), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L287) (StacksFrontier): “completed_tensor_adic_star”.
- [`TopologicalRing.completedTensorProduct_isAdic`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L364), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L289) (StacksFrontier): “completed_tensor_adic_star”.
- [`TopologicalRing.exists_fg_ideal_of_definition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L383), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L290) (StacksFrontier): “completed_tensor_adic_star”.
- [`TopologicalRing.completedTensorProduct_isWeaklyAdmissible`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L951), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesRefined.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesRefined.lean#L277) (StacksFrontier): “completed_tensor_adic_star”.
- [`TopologicalRing.completedTensorProduct_isAdic`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L364), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesRefined.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesRefined.lean#L279) (StacksFrontier): “completed_tensor_adic_star”.
- [`TopologicalRing.exists_fg_ideal_of_definition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L383), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesRefined.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalPropertiesRefined.lean#L280) (StacksFrontier): “completed_tensor_adic_star”.

## Tag 0GBF, a remark

[Tag 0GBF](https://stacks.math.columbia.edu/tag/0GBF) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_pullback_snd_of_stableBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean#L340). The attribute's comment: “the 0GBD variant for locally Noetherian formal algebraic spaces”.

> **Stacks 0GBF**, the variant of Stacks 0GBD for locally Noetherian formal algebraic
> spaces: let `P` be stable under base change for Noetherian adic topological rings in the sense
> of Stacks 0GBF. If `f : X ⟶ Y` satisfies condition (1) of Stacks 0ANG for `P`, then for every
> `g : Z ⟶ Y` the second projection `X ×_Y Z ⟶ Z` satisfies condition (1) for `P`.
>
> Nothing is asked of `g`, exactly as the definition of Stacks 0GBF imposes no condition on the
> morphism being based along: stability under base change is stability under base change by the
> property that holds of every morphism, and that property is local, so the statement is the one
> of Stacks 0GBG with `Q` instantiated there.
>
> The three further hypotheses are those the Stacks 0GBG statements already carry, for the same
> reasons: `hcover` is the geometric input of Stacks 0GBD, `h31` the implication (3) ⟹ (1) of
> Stacks 0ANG, and `hiso` the invariance of `P` under isomorphism of targets.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_pullback_snd_of_stableBaseChange
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hP : TopologicalRing.IsStableUnderBaseChangeNoetherian.{u} P)
    (hiso : PropertyIsInvariantUnderTargetIso.{u} P)
    (h31 : SourceCoverImpliesEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hcover : HasBaseChangeCoverOverPullbackSnd B S hS f g)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P f) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.conditions_pullback_snd_of_isStableUnderBaseChangeNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChangeNoetherian.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChangeNoetherian.lean#L273). The attribute's comment: “the variant of Stacks 0GBD for morphisms between locally Noetherian formal algebraic spaces; the definition of stability under base change is TopologicalRing.IsStableUnderBaseChangeNoetherian”.

> The variant of Stacks 0GBD for locally Noetherian formal algebraic spaces. Let `P` be a local
> property of morphisms of `WAdm^{Noeth}` (Remark 0ANI) which is stable under base change: given
> `B → A` and `B → C` in `WAdm^{Noeth}`, `P (B → A)` implies that `A ⊗̂_B C` is adic Noetherian and
> that `P (C → A ⊗̂_B C)` holds (`TopologicalRing.IsStableUnderBaseChangeNoetherian`, the definition
> of the remark). Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally Noetherian formal algebraic
> spaces over `S`. If `f` satisfies the equivalent conditions of Stacks 0ANG, then so does
> `pr₂ : X ×_Y Z ⟶ Z`; all three of them are concluded.
>
> Being local in the sense of Remark 0ANI is `hP.isLocal` together with `hPiso`, the invariance
> of `P` under isomorphism of source and target that Situation 0CBA assumes. Nothing is asked of
> `g`.

```lean
theorem conditions_pullback_snd_of_isStableUnderBaseChangeNoetherian
    (P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hP : TopologicalRing.IsStableUnderBaseChangeNoetherian.{u} P)
    (hPiso : ∀ {B A B' A' : Type u}
      [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
      [CommRing B'] [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
      [CommRing A'] [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
      (eB : B ≃+* B') (eA : A ≃+* A'), Continuous eB → Continuous eB.symm →
      Continuous eA → Continuous eA.symm → ∀ (f : B →+* A), Continuous f →
      TopologicalRing.IsNoetherianAdic B → TopologicalRing.IsNoetherianAdic A →
      TopologicalRing.IsNoetherianAdic B' → TopologicalRing.IsNoetherianAdic A' →
      (P f ↔ P ((eA.toRingHom.comp f).comp eB.symm.toRingHom)))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P f) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P
        (pullback.snd f g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsNoetherianAdic P (pullback.snd f g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsNoetherianAdic P (pullback.snd f g)
```

**`TopologicalRing.IsStableUnderBaseChangeNoetherian`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L352). The attribute's comment: “the definition of stability under base change; not the 0GBD variant for spaces”.

> A local property `P` of morphisms of Noetherian adic topological rings is *stable under
> base change* when, for every pair of continuous homomorphisms `B →+* A` and `B →+* C` of such
> rings, `P (B →+* A)` forces the completed tensor product `A ⊗̂_B C` to be adic Noetherian again
> and `P` to hold for `C →+* A ⊗̂_B C`. No condition is imposed on `B →+* C`.

```lean
public structure IsStableUnderBaseChangeNoetherian
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBG, a remark

[Tag 0GBG](https://stacks.math.columbia.edu/tag/0GBG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyAfterSourceCover_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean#L236). The attribute's comment: “condition (3) for pr₂, with the 0GBD cover and iso-invariance assumed”.

> **Stacks 0GBG**, in the form that the argument of Stacks 0GBD produces: if `P` is stable
> under base change by `Q` and `f : X ⟶ Y`, `g : Z ⟶ Y` satisfy condition (1) of Stacks 0ANG for
> `P` and for `Q`, then the second projection `X ×_Y Z ⟶ Z` satisfies condition (3) of Stacks
> 0ANG for `P`.
>
> The covering of `X ×_Y Z` by fibre products of charts, with the presentation of those fibre
> products by completed tensor products, is the hypothesis `hcover`; it mentions neither `P` nor
> `Q`. The isomorphism invariance of `P` implied by the locality of Stacks 0ANI is `hiso`.

```lean
theorem hasPropertyAfterSourceCover_pullback_snd
    (P Q : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hPQ : TopologicalRing.IsStableUnderBaseChangeBy.{u} P Q)
    (hiso : PropertyIsInvariantUnderTargetIso.{u} P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hcover : HasBaseChangeCoverOverPullbackSnd B S hS f g)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P f)
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) Q g) :
    HasPropertyAfterSourceCover B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean#L263). The attribute's comment: “condition (1) for pr₂, with the 0GBD cover, 0ANG (3) ⟹ (1) and iso-invariance”.

> **Stacks 0GBG.** Let `P` be stable under base change by `Q` for Noetherian adic
> topological rings. If `f : X ⟶ Y` and `g : Z ⟶ Y` are morphisms of locally Noetherian formal
> algebraic spaces over `S` satisfying condition (1) of Stacks 0ANG for `P` and for `Q`
> respectively, then the second projection `X ×_Y Z ⟶ Z` satisfies condition (1) for `P`.
>
> Condition (3) is what the argument of Stacks 0GBD gives; the passage back to condition (1) is
> the implication (3) ⟹ (1) of Stacks 0ANG, carried as the hypothesis `h31`.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_pullback_snd
    (P Q : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hPQ : TopologicalRing.IsStableUnderBaseChangeBy.{u} P Q)
    (hiso : PropertyIsInvariantUnderTargetIso.{u} P)
    (h31 : SourceCoverImpliesEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hcover : HasBaseChangeCoverOverPullbackSnd B S hS f g)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P f)
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) Q g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.transfersBaseChangeOnAffineEtaleDiagrams`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChange.lean#L288). The attribute's comment: “the transfer for every property pair, on the same three hypotheses”.

> **Stacks 0GBG**, uniformly over all pairs of properties: whenever `P` is stable under base
> change by `Q` for Noetherian adic topological rings, condition (1) of Stacks 0ANG transfers
> from `(f, P)` and `(g, Q)` to `(X ×_Y Z ⟶ Z, P)`.
>
> The three inputs of the single-pair statement are asked of every property local in the sense
> of Stacks 0ANI, which is how the stability bundle of Stacks 0GBG supplies locality, and of
> every pair of morphisms.

```lean
theorem transfersBaseChangeOnAffineEtaleDiagrams
    (hiso : ∀ P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop,
      TopologicalRing.PropertyIsLocalNoetherian.{u} P → PropertyIsInvariantUnderTargetIso.{u} P)
    (h31 : ∀ P : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop,
      TopologicalRing.PropertyIsLocalNoetherian.{u} P →
        SourceCoverImpliesEveryAffineEtaleDiagram B S hS
          (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P)
    (hcover : ∀ {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y),
      HasBaseChangeCoverOverPullbackSnd B S hS f g) :
    ∀ (P Q : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop),
      TopologicalRing.IsStableUnderBaseChangeBy.{u} P Q →
      ∀ {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y),
        HasPropertyOnEveryAffineEtaleDiagram B S hS
            (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P f →
          HasPropertyOnEveryAffineEtaleDiagram B S hS
              (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) Q g →
            HasPropertyOnEveryAffineEtaleDiagram B S hS
              (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R) P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.conditions_pullback_snd_of_isStableUnderBaseChangeBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChangeNoetherian.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyBaseChangeNoetherian.lean#L162). The attribute's comment: “the statement drawn there: the equivalent conditions of Stacks 0ANG pass from f and P and from g and Q to the second projection of X ×_Y Z and P, for locally Noetherian formal algebraic spaces; the notion of stability under base change by Q is TopologicalRing.IsStableUnderBaseChangeBy”.

> Let `P` and `Q` be local properties of morphisms of `WAdm^{Noeth}` (Remark 0ANI), with `P`
> stable under base change by `Q`: given `B → A` and `B → C` in `WAdm^{Noeth}` with `P (B → A)` and
> `Q (B → C)`, the completed tensor product `A ⊗̂_B C` is adic Noetherian and `P (C → A ⊗̂_B C)`
> holds (`TopologicalRing.IsStableUnderBaseChangeBy`). Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms
> of locally Noetherian formal algebraic spaces over `S` such that the equivalent conditions of
> Stacks 0ANG hold for `f` and `P` and for `g` and `Q`. Then the equivalent conditions of Stacks 0ANG
> hold for `pr₂ : X ×_Y Z ⟶ Z` and `P`; all three of them are concluded.
>
> Being local in the sense of Remark 0ANI is `hPQ.isLocalP` together with `hPiso`, the invariance
> of `P` under isomorphism of source and target that Situation 0CBA assumes of a property of
> arrows of the category.

```lean
theorem conditions_pullback_snd_of_isStableUnderBaseChangeBy
    (P Q : ∀ {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
      [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂], (R₁ →+* R₂) → Prop)
    (hPQ : TopologicalRing.IsStableUnderBaseChangeBy.{u} P Q)
    (hPiso : ∀ {B A B' A' : Type u}
      [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
      [CommRing B'] [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
      [CommRing A'] [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
      (eB : B ≃+* B') (eA : A ≃+* A'), Continuous eB → Continuous eB.symm →
      Continuous eA → Continuous eA.symm → ∀ (f : B →+* A), Continuous f →
      TopologicalRing.IsNoetherianAdic B → TopologicalRing.IsNoetherianAdic A →
      TopologicalRing.IsNoetherianAdic B' → TopologicalRing.IsNoetherianAdic A' →
      (P f ↔ P ((eA.toRingHom.comp f).comp eB.symm.toRingHom)))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P f)
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic Q g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P
        (pullback.snd f g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsNoetherianAdic P (pullback.snd f g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsNoetherianAdic P (pullback.snd f g)
```

**`TopologicalRing.IsStableUnderBaseChangeBy`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L379). The attribute's comment: “stable_under_base_change_by_noetherian”.

> A local morphism property of Noetherian adic rings is stable under completed
> tensor-product base change along morphisms satisfying another local property.

```lean
public structure IsStableUnderBaseChangeBy (P Q : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B]
    [IsTopologicalRing B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A],
    (B →+* A) → Prop) : Prop
```

## Tag 0GBH, a situation

[Tag 0GBH](https://stacks.math.columbia.edu/tag/0GBH) in the Stacks Project.

**`TopologicalRing.PropertyIsStableUnderComposition`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L439).

> A local property of morphisms of countably indexed weakly admissible rings is
> stable under composition when two composable morphisms with the property have a
> composite with the property.

```lean
public structure PropertyIsStableUnderComposition
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBI, a lemma

[Tag 0GBI](https://stacks.math.columbia.edu/tag/0GBI) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyComposition.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyComposition.lean#L261). The attribute's comment: “condition (1) for the composite, granting the composition axiom of Situation 0GBH read on charts through Stacks 0AN0 (hchart), the implication (3) ⟹ (1) of Stacks 0ANG (h31) and the fibre products of Stacks 0AJ3 (hpbf, hpbg)”.

> **Stacks 0GBI.** Let `P` be a local property of arrows of the class `C` which is stable
> under composition. If `f : X ⟶ Y` and `g : Y ⟶ Z` are morphisms of formal algebraic spaces over
> `S` satisfying the equivalent conditions of Stacks 0ANG for `P`, then so does `g ∘ f`.
>
> Condition (3) is what the covering of the proof gives; the passage back to condition (1) is the
> implication (3) ⟹ (1) of Stacks 0ANG, carried as the hypothesis `h31`.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_comp
    (hchart : ChartPropertyIsStableUnderComposition B S hS C P)
    (h31 : SourceCoverImpliesEveryAffineEtaleDiagram B S hS C P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hZ : IsFormalAlgebraicSpace B S hS Z)
    (hpbg : HasFormalAlgebraicSpaceChartPullbacks B S hS g)
    (hpbf : HasFormalAlgebraicSpaceChartPullbacks B S hS f)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS C P f)
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS C P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS C P (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_comp_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCompositionPresented.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCompositionPresented.lean#L314).

> **Stacks 0GBI.** Let `P` be a local property of morphisms of `WAdm^{count}` which is stable
> under composition, and let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally countably
> indexed formal algebraic spaces over `S`. If `f` and `g` satisfy the equivalent conditions of
> Stacks 0ANG, then so does `g ∘ f`: the conclusion lists all three of them. Being a local
> property in the sense of Situation 0CBA is `hP.isLocal` together with `hPiso`, the invariance of
> `P` under isomorphism of source and target that the situation assumes.
>
> The covering of the proof is
> `AlgebraicGeometry.FormalSpace.exists_affineEtaleCover_chartFactorization_comp_of_atlas`, built
> on the countably indexed atlas of `Y`; its intermediate charts are countably indexed by clause
> (1) of Stacks 0AKQ, hence presented by rings of `WAdm^{count}` (Stacks 0AN1), and the
> composition axiom applies through Stacks 0AN0. That gives condition (3) for `g ∘ f`; condition
> (1) follows by the implication (3) ⟹ (1) of Stacks 0ANG, from the presented refinement of a
> covering of the source and the locality of `P`, and condition (2) by (1) ⟹ (2).

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_comp_of_isLocallyCountablyIndexed
    (hP : TopologicalRing.PropertyIsStableUnderComposition P)
    (hPiso : ∀ {B A B' A' : Type u}
      [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
      [CommRing B'] [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
      [CommRing A'] [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
      (eB : B ≃+* B') (eA : A ≃+* A'), Continuous eB → Continuous eB.symm →
      Continuous eA → Continuous eA.symm → ∀ (f : B →+* A), Continuous f →
      TopologicalRing.IsCountablyWeaklyAdmissible B →
      TopologicalRing.IsCountablyWeaklyAdmissible A →
      TopologicalRing.IsCountablyWeaklyAdmissible B' →
      TopologicalRing.IsCountablyWeaklyAdmissible A' →
      (P f ↔ P ((eA.toRingHom.comp f).comp eB.symm.toRingHom)))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (hZ : IsLocallyCountablyIndexed B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS
      TopologicalRing.IsCountablyWeaklyAdmissible P f)
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS
      TopologicalRing.IsCountablyWeaklyAdmissible P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS
        TopologicalRing.IsCountablyWeaklyAdmissible P (f ≫ g) ∧
      HasPropertyAfterTargetCover B S hS
        TopologicalRing.IsCountablyWeaklyAdmissible P (f ≫ g) ∧
      HasPropertyAfterSourceCover B S hS
        TopologicalRing.IsCountablyWeaklyAdmissible P (f ≫ g)
```

## Tag 0GBJ, a remark

[Tag 0GBJ](https://stacks.math.columbia.edu/tag/0GBJ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_comp_of_isLocallyAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarCompositionVariant.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarCompositionVariant.lean#L234). The attribute's comment: “the second half, the variant of Lemma 0GBI for morphisms between locally adic* formal algebraic spaces: for a local property P of morphisms of WAdm^{adic*} (Remark 0ANH) which is stable under composition in the sense of the first half, TopologicalRing.PropertyIsStableUnderCompositionAdicStar, and morphisms f : X -> Y, g : Y -> Z of locally adic* formal algebraic spaces satisfying the equivalent conditions of Stacks 0ANG (condition (1)), the composite g o f satisfies all three; the invariance of P under isomorphism of Situation 0CBA is not used”.

> **Stacks 0GBJ, second half: the variant of Lemma 0GBI for locally adic\* formal algebraic
> spaces.** Let `P` be a local property of morphisms of `WAdm^{adic*}` (Remark 0ANH) which is
> stable under composition in the sense of the first half of Remark 0GBJ,
> `TopologicalRing.PropertyIsStableUnderCompositionAdicStar`. Let `f : X ⟶ Y` and `g : Y ⟶ Z` be
> morphisms of locally adic\* formal algebraic spaces over `S`. If `f` and `g` satisfy the
> equivalent conditions of Stacks 0ANG for `P` (in the adic\* reading of Remark 0ANH) — here
> condition (1), that `P` holds on every affine étale diagram, the strongest of the three — then
> so does `g ∘ f`: the conclusion lists all three conditions.
>
> Condition (1) for `g ∘ f` is
> `AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_comp_of_isLocal` at the
> class `WAdm^{adic*}`: every affine formal algebraic space representable étale over `Y` is adic\*
> by the implication (2) ⟹ (1) of Stacks 0AKX, hence presented by a ring of `WAdm^{adic*}`.
> Conditions (2) and (3) follow by the implications (1) ⟹ (2) ⟹ (3) of Stacks 0ANG. The
> invariance of `P` under isomorphism of source and target, which Situation 0CBA stipulates, is
> not needed.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_comp_of_isLocallyAdicStar
    (hP : TopologicalRing.PropertyIsStableUnderCompositionAdicStar.{u} P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y)
    (hZ : IsLocallyAdicStar B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P f)
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P (f ≫ g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar P (f ≫ g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar P (f ≫ g)
```

**`TopologicalRing.AdicStarPropertyIsStableUnderComposition`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L461). The attribute's comment: “stable_under_composition_for_adic_ring_map_properties”.

> A local property of morphisms of weakly admissible adic-star rings is stable
> under composition if it is preserved by composition of continuous maps between
> such rings.

```lean
public structure AdicStarPropertyIsStableUnderComposition
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
      [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

**`TopologicalRing.PropertyIsStableUnderCompositionAdicStar`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L497). The attribute's comment: “the definition of stability under composition, at the source's class of rings: the morphisms range over WAdm^{adic*}, the adic topological rings -- hence complete and separated -- possessing a finitely generated ideal of definition, and the locality of P is read in the same subcategory by TopologicalRing.PropertyIsLocalAdicStar”.

> A local property `P` of morphisms of `WAdm^{adic*}` is *stable under composition* when,
> for morphisms `B → A` and `C → B` of `WAdm^{adic*}`, `P (B → A)` and `P (C → B)` imply
> `P (C → A)`.
>
> `WAdm^{adic*}` is the full subcategory of `WAdm` whose objects are the adic, hence complete and
> separated, topological rings possessing a finitely generated ideal of definition, and the
> locality of `P` is `TopologicalRing.PropertyIsLocalAdicStar`, read in the same subcategory.
>
> This agrees with `TopologicalRing.AdicStarPropertyIsStableUnderComposition`, by
> `TopologicalRing.adicStarPropertyIsStableUnderComposition_iff`.

```lean
public structure PropertyIsStableUnderCompositionAdicStar
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
      [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBK, a remark

[Tag 0GBK](https://stacks.math.columbia.edu/tag/0GBK) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_comp_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCompositionPresented.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCompositionPresented.lean#L378). The attribute's comment: “the variant of Stacks 0GBI for morphisms between locally Noetherian formal algebraic spaces; the definition of stability under composition is TopologicalRing.PropertyIsStableUnderCompositionNoetherian”.

> **Stacks 0GBK.** A local property `P` of morphisms of `WAdm^{Noeth}` is *stable under
> composition* when `P(B → A) ∧ P(C → B) ⟹ P(C → A)` for arrows of `WAdm^{Noeth}`: that is the
> structure `TopologicalRing.PropertyIsStableUnderCompositionNoetherian`, whose `isLocal` field
> together with `hPiso` (invariance under isomorphism of source and target, assumed by Situation
> 0CBA and hence by Remark 0ANI) make `P` local. The variant of Stacks 0GBI then holds for
> morphisms between locally Noetherian formal algebraic spaces: if `f : X ⟶ Y` and `g : Y ⟶ Z`
> satisfy the equivalent conditions of Stacks 0ANG for `P` on `WAdm^{Noeth}`, so does `g ∘ f`, and
> the conclusion lists all three of them.
>
> The covering is
> `AlgebraicGeometry.FormalSpace.exists_presentedSourceCover_comp_of_atlas` built on the
> Noetherian atlases of `X`, `Y` and `Z`: its charts stay Noetherian along representable étale
> maps by clause (5) of Stacks 0AKQ and are then presented by their presenting rings, which are
> Noetherian and adic, so the composition axiom applies through Stacks 0AN0 and gives condition
> (3) on a covering with presented members. The implication (3) ⟹ (1) of Stacks 0ANG on such a
> covering is
> `AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_presentedSourceCover`,
> at the class `WAdm^{Noeth}`, whose closure conditions are clauses of Stacks 0ANB; condition (2)
> follows by (1) ⟹ (2).

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_comp_of_isLocallyNoetherian
    (hP : TopologicalRing.PropertyIsStableUnderCompositionNoetherian P)
    (hPiso : ∀ {B A B' A' : Type u}
      [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
      [CommRing B'] [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
      [CommRing A'] [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
      (eB : B ≃+* B') (eA : A ≃+* A'), Continuous eB → Continuous eB.symm →
      Continuous eA → Continuous eA.symm → ∀ (f : B →+* A), Continuous f →
      TopologicalRing.IsNoetherianAdic B → TopologicalRing.IsNoetherianAdic A →
      TopologicalRing.IsNoetherianAdic B' → TopologicalRing.IsNoetherianAdic A' →
      (P f ↔ P ((eA.toRingHom.comp f).comp eB.symm.toRingHom)))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hf : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P f)
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P (f ≫ g) ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsNoetherianAdic P (f ≫ g) ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsNoetherianAdic P (f ≫ g)
```

**`TopologicalRing.PropertyIsStableUnderCompositionNoetherian`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L525). The attribute's comment: “stable_under_composition_noetherian”.

> A local property of morphisms of Noetherian adic rings is stable under composition
> when it holds for the composite of two continuous morphisms having the property.

```lean
public structure PropertyIsStableUnderCompositionNoetherian
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBL, a situation

[Tag 0GBL](https://stacks.math.columbia.edu/tag/0GBL) in the Stacks Project.

**`TopologicalRing.PropertyIsLocalWithCancellation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L546).

> A local property of morphisms of countably indexed weakly admissible rings with
> the cancellation property for composable morphisms.

```lean
public structure PropertyIsLocalWithCancellation
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBM, a lemma

[Tag 0GBM](https://stacks.math.columbia.edu/tag/0GBM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_comp_of_isLocallyCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCancellation.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCancellation.lean#L182).

> Let `P` be a local property of morphisms of `WAdmᶜᵒᵘⁿᵗ` which has the cancellation
> property, and let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally countably indexed formal
> algebraic spaces over `S`. If `g ∘ f` and `g` satisfy `HasPropertyOnEveryAffineEtaleDiagram`,
> then `f` satisfies `HasPropertyOnEveryAffineEtaleDiagram`, `HasPropertyAfterTargetCover` and
> `HasPropertyAfterSourceCover`.
>
> Here `P` being local with the cancellation property is `hP` (the three axioms and the
> cancellation property) together with `hPiso`, the clause that `P` is "invariant under isomorphism
> of source and target in this category".

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_of_comp_of_isLocallyCountablyIndexed
    (hP : TopologicalRing.PropertyIsLocalWithCancellation P)
    (hPiso : ∀ {B A B' A' : Type u}
      [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
      [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
      [CommRing B'] [TopologicalSpace B'] [IsTopologicalRing B'] [IsLinearTopology B' B']
      [CommRing A'] [TopologicalSpace A'] [IsTopologicalRing A'] [IsLinearTopology A' A']
      (eB : B ≃+* B') (eA : A ≃+* A'), Continuous eB → Continuous eB.symm →
      Continuous eA → Continuous eA.symm → ∀ (f : B →+* A), Continuous f →
      TopologicalRing.IsCountablyWeaklyAdmissible B →
      TopologicalRing.IsCountablyWeaklyAdmissible A →
      TopologicalRing.IsCountablyWeaklyAdmissible B' →
      TopologicalRing.IsCountablyWeaklyAdmissible A' →
      (P f ↔ P ((eA.toRingHom.comp f).comp eB.symm.toRingHom)))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsLocallyCountablyIndexed B S hS Y)
    (hZ : IsLocallyCountablyIndexed B S hS Z)
    (hfg : HasPropertyOnEveryAffineEtaleDiagram B S hS
      TopologicalRing.IsCountablyWeaklyAdmissible P (f ≫ g))
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS
      TopologicalRing.IsCountablyWeaklyAdmissible P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS
        TopologicalRing.IsCountablyWeaklyAdmissible P f ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsCountablyWeaklyAdmissible P f
```

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyComposition.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyComposition.lean#L306). The attribute's comment: “condition (1) for the first factor, granting the cancellation axiom of Situation 0GBL read on charts through Stacks 0AN0 (hchart), the implication (3) ⟹ (1) of Stacks 0ANG (h31) and the fibre products of Stacks 0AJ3 (hpbf, hpbg)”.

> **Stacks 0GBM.** Let `P` be a local property of arrows of the class `C` with the
> cancellation property. If `g ∘ f` and `g : Y ⟶ Z` satisfy the equivalent conditions of Stacks
> 0ANG for `P`, then so does `f : X ⟶ Y`.
>
> Condition (3) is what the covering of the proof gives; the passage back to condition (1) is the
> implication (3) ⟹ (1) of Stacks 0ANG, carried as the hypothesis `h31`.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_of_comp
    (hchart : ChartPropertyHasCancellation B S hS C P)
    (h31 : SourceCoverImpliesEveryAffineEtaleDiagram B S hS C P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hZ : IsFormalAlgebraicSpace B S hS Z)
    (hpbg : HasFormalAlgebraicSpaceChartPullbacks B S hS g)
    (hpbf : HasFormalAlgebraicSpaceChartPullbacks B S hS f)
    (hfg : HasPropertyOnEveryAffineEtaleDiagram B S hS C P (f ≫ g))
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS C P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS C P f
```

## Tag 0GBN, a remark

[Tag 0GBN](https://stacks.math.columbia.edu/tag/0GBN) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_comp_of_isLocallyAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarCancellationVariant.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarCancellationVariant.lean#L102). The attribute's comment: “the second half: the variant of Lemma 0GBM (the remark's Lemma 0GBI is a slip for 0GBM, an erratum to the Stacks Project) for morphisms f : X -> Y, g : Y -> Z between locally adic* formal algebraic spaces over S, for a local property P of WAdm^{adic*} (Remark 0ANH: invariant under isomorphism of source and target and satisfying the three axioms of Situation 0CBA) having the cancellation property TopologicalRing.HasAdicStarCancellationProperty: if g o f and g satisfy the equivalent conditions of Stacks 0ANG then so does f”.

> **Stacks 0GBN, second half: the cancellation variant for locally adic\* formal algebraic
> spaces.** Let `P` be a local property of morphisms of `WAdm^{adic*}` in the sense of Remark
> 0ANH, `hP`: a property of arrows of `WAdm^{adic*}` invariant under isomorphism of source and
> target in that category and satisfying the three axioms of Situation 0CBA there. Suppose `P`
> has the cancellation property of the first half of the remark, `hcancel`: for `B → A` and
> `C → B` in `WAdm^{adic*}`, `P(C → A) ∧ P(C → B) ⟹ P(B → A)`. Let `f : X ⟶ Y` and
> `g : Y ⟶ Z` be morphisms of locally adic\* formal algebraic
> spaces over `S`. If `g ∘ f` and `g` satisfy the equivalent conditions of
> Stacks 0ANG for `P` at `WAdm^{adic*}` — here condition (1), which is equivalent to the other two
> by the second half of Stacks 0ANH — then so does `f`; the conclusion lists all three.
>
> The proof is that of Stacks 0GBM: on the covering `Uᵢ ⟶ Vᵢ ⟶ Wᵢ` of
> `AlgebraicGeometry.FormalSpace.hasPropertyAfterSourceCover_of_comp_of_atlas`, built on adic\*
> atlases of `X`, `Y`, `Z`, the maps `Vᵢ ⟶ Wᵢ` and `Uᵢ ⟶ Wᵢ` correspond to arrows `C → B` and
> `C → A` of `WAdm^{adic*}` with `P`, so `Uᵢ ⟶ Vᵢ`, corresponding to `B → A`, has `P`.

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_of_comp_of_isLocallyAdicStar
    (hP : TopologicalRing.PropertyIsLocal'.{u} P TopologicalRing.IsAdicStar)
    (hcancel : TopologicalRing.HasAdicStarCancellationProperty.{u} P)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsLocallyAdicStar B S hS Y)
    (hZ : IsLocallyAdicStar B S hS Z)
    (hfg : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P (f ≫ g))
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsAdicStar P f ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsAdicStar P f ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsAdicStar P f
```

**`TopologicalRing.HasAdicStarCancellationProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/AdicStarCancellation.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/AdicStarCancellation.lean#L48). The attribute's comment: “the cancellation property”.

> **Cancellation for a morphism property of `WAdm^{adic*}`** (Stacks 0GBN).  Given arrows
> `f : B →+* A` and `g : C →+* B` of `WAdm^{adic*}` — continuous homomorphisms of weakly
> admissible topological rings each carrying the adic topology of a finitely generated ideal —
> the property of the composite `C → A` and the property of `C → B` together imply the property
> of `B → A`.

```lean
public abbrev HasAdicStarCancellationProperty
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
      [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Tag 0GBP, a remark

[Tag 0GBP](https://stacks.math.columbia.edu/tag/0GBP) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_comp_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCancellationPresented.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocalPropertyCancellationPresented.lean#L90). The attribute's comment: “the variant of Stacks 0GBM for morphisms between locally Noetherian formal algebraic spaces; the definition of the cancellation property is TopologicalRing.HasNoetherianCancellationProperty”.

> **Stacks 0GBP.** Let `P` be a local property of morphisms of `WAdm^{Noeth}` in the sense of
> Remark 0ANI: it satisfies the three axioms of Situation 0CBA for morphisms of `WAdm^{Noeth}`,
> which is `hP`, and is invariant under isomorphism of source and target, which Situation 0CBA
> assumes and is `hPiso`. Suppose `P` has the *cancellation property*: for arrows `B → A` and
> `C → B` of `WAdm^{Noeth}`, `P(C → B) ∧ P(C → A) ⟹ P(B → A)`, which is `hcancel`. Then the
> variant of Stacks 0GBM holds for morphisms between locally Noetherian formal algebraic spaces:
> if `f : X ⟶ Y` and `g : Y ⟶ Z` are such that `g ∘ f` and `g` satisfy the equivalent conditions
> of Stacks 0ANG for `P` on `WAdm^{Noeth}`, so does `f`, and the conclusion lists all three of
> them.
>
> The covering is the one of the proof of Stacks 0GBM,
> `AlgebraicGeometry.FormalSpace.exists_presentedSourceCover_of_comp_of_atlas`, built on the
> Noetherian atlases of `X`, `Y` and `Z`: its charts stay Noetherian along representable étale
> maps by clause (5) of Stacks 0AKQ and are presented by their presenting rings, which are
> Noetherian and adic, so the cancellation property applies through Stacks 0AN0 and gives
> condition (3) for `f` on a covering with presented members. The implication (3) ⟹ (1) of
> Stacks 0ANG on such a covering is
> `AlgebraicGeometry.FormalSpace.hasPropertyOnEveryAffineEtaleDiagram_of_presentedSourceCover`,
> at the class `WAdm^{Noeth}`; condition (2) follows by (1) ⟹ (2).

```lean
theorem hasPropertyOnEveryAffineEtaleDiagram_of_comp_of_isLocallyNoetherian
    (hP : TopologicalRing.PropertyIsLocalNoetherian.{u} P)
    (hcancel : TopologicalRing.HasNoetherianCancellationProperty.{u} P)
    (hPiso : TopologicalRing.IsomorphismInvariant.{u} P
      (fun R _ _ _ _ ↦ TopologicalRing.IsNoetherianAdic R))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hfg : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P
      (f ≫ g))
    (hg : HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P g) :
    HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic P f ∧
      HasPropertyAfterTargetCover B S hS TopologicalRing.IsNoetherianAdic P f ∧
      HasPropertyAfterSourceCover B S hS TopologicalRing.IsNoetherianAdic P f
```

**`TopologicalRing.HasNoetherianCancellationProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/LocalProperties.lean#L565). The attribute's comment: “noetherian_cancellation_property”.

> Cancellation for a morphism property on Noetherian adic topological rings.

```lean
public abbrev HasNoetherianCancellationProperty
    (P : ∀ {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A], (B →+* A) → Prop) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.21, Tag 0ANA](https://stacks.math.columbia.edu/tag/0ANA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
