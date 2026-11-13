---
declaration: section
origin: cited
lean: closedPointsEquivDual, pointSubmodule, projection, coe_mapDomain_pointSubmodule, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_isFinite_projection_restrict, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_projection_isClosedImmersion_and_etaleAt, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_forall_closedPoint_projection_restrict, AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_inter_projectionCone_eq
statement: formalized
proof: formalized
---

# 43.23 Projections

Section 43.23 of the Stacks Project, [Tag 0B1N](https://stacks.math.columbia.edu/tag/0B1N). 10 tags here are carried by 48 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B1N, the section

[Tag 0B1N](https://stacks.math.columbia.edu/tag/0B1N) in the Stacks Project.

Declarations registered for the tag:

- [`closedPointsEquivDual`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=closedPointsEquivDual#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean#L47) (StacksFrontier): “section tag; the closed points of 𝐏(V) are the one-dimensional quotients V → L\_p of V”.
- [`pointSubmodule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=pointSubmodule#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean#L49) (StacksFrontier): “section tag; W\_p = Ker(V → L\_p), the degree-one forms vanishing at p”.
- [`projection`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=projection#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean#L51) (StacksFrontier): “section tag; the projection r\_p away from p, for the submodule W\_p”.
- [`coe_mapDomain_pointSubmodule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=coe_mapDomain_pointSubmodule#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionsSection.lean#L53) (StacksFrontier): “section tag; the domain of definition of r\_p is 𝐏(V) ∖ \{p}”.

## Tag 0B1P, a lemma

[Tag 0B1P](https://stacks.math.columbia.edu/tag/0B1P) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_isFinite_projection_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/FiniteProjection.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Projective/FiniteProjection.lean#L167).

> **Stacks Project, Tag 0B1P.** Let `V` be a vector space of dimension `n + 1` over an
> algebraically closed field and let `X ⊆ 𝐏(V)` be a closed subscheme with `X ≠ 𝐏(V)`. Then there
> is a nonempty Zariski open `U ⊆ 𝐏(V)` such that for every closed point `p ∈ U` the projection
> `r_p` away from `p` is defined on `X` and the restriction `r_p|_X : X ⟶ 𝐏(W_p)` is a finite
> morphism.
>
> The open is the complement of `X`, which is nonempty because a surjective closed immersion into
> the reduced scheme `𝐏(V)` would be an isomorphism.

```lean
public theorem exists_isOpen_isFinite_projection_restrict [IsAlgClosed k] [FiniteDimensional k V]
    [Nontrivial V] {X : Scheme.{u}} (i : X ⟶ projectiveSpaceOfModule k V)
    [IsClosedImmersion i] (hX : ¬ IsIso i) :
    ∃ U : (projectiveSpaceOfModule k V).Opens,
      (U : Set (projectiveSpaceOfModule k V)).Nonempty ∧
      ∀ p ∈ U, IsClosed ({p} : Set (projectiveSpaceOfModule k V)) →
        ∃ j : X ⟶ (projectionDomain k V (pointSubmodule k V p)).toScheme,
          j ≫ (projectionDomain k V (pointSubmodule k V p)).ι = i ∧
            IsFinite (j ≫ projection k V (pointSubmodule k V p))
```

## Tag 0B1Q, a lemma

[Tag 0B1Q](https://stacks.math.columbia.edu/tag/0B1Q) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_projection_isClosedImmersion_and_etaleAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/GenericProjection.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Projective/GenericProjection.lean#L638). The attribute's comment: “both parts, for a closed subvariety of the projective space of a vector space of dimension n + 1 over an algebraically closed field and a nonsingular point x of it, each part under its own dimension condition exactly as the source states it: (1) for dim X < n - 1 a nonempty Zariski open of centres p for which r\_p|\_X is an isomorphism over a neighbourhood of r\_p(x), spelled as the restriction of r\_p|\_X over that neighbourhood being a closed immersion, which is the same thing since a closed immersion over an open R is an isomorphism onto its scheme-theoretic image r\_p(X) ∩ R; (2) for dim X = n - 1 a nonempty Zariski open of centres p for which r\_p|\_X : X ⟶ 𝐏(W\_p) is étale at x. Both parts also deliver the source's 'r\_p is defined on X' as the lift j of the closed immersion i through the domain of definition of the projection away from p. WithBot ℕ∞ has no subtraction, so the two dimension conditions are written dim X + 1 < n and dim X + 1 = n.”.

> **Stacks Project, Tag 0B1Q.** Let `V` be a vector space of dimension `n + 1` over an
> algebraically closed field, let `X ⊆ 𝐏(V)` be a closed subvariety and let `x` be a nonsingular
> point of `X`. Then
>
> 1. if `dim X < n - 1`, there is a nonempty Zariski open `U ⊆ 𝐏(V)` such that for every closed
>    point `p ∈ U` the projection `r_p` is defined on `X` and `r_p|_X : X → r_p(X)` is an
>    isomorphism over an open neighbourhood of `r_p(x)`;
> 2. if `dim X = n - 1`, there is a nonempty Zariski open `U ⊆ 𝐏(V)` such that for every closed
>    point `p ∈ U` the projection `r_p` is defined on `X` and `r_p|_X : X ⟶ 𝐏(W_p)` is étale
>    at `x`.
>
> Each part keeps its own dimension condition as the hypothesis of its clause, as the source
> states them. That `r_p` is defined on `X` is the morphism `j` lifting the closed immersion `i`
> through the domain of definition of the projection away from `p`. In part (1) the isomorphism
> onto the image over a neighbourhood `R` of `r_p(x)` is spelled as `r_p|_X` restricted over `R`
> being a closed immersion, which is the same thing: a closed immersion over `R` is an
> isomorphism of its source onto its scheme-theoretic image, and that image is `r_p(X) ∩ R`.
> `WithBot ℕ∞` has no subtraction, so `dim X < n - 1` and `dim X = n - 1` are written
> `dim X + 1 < n` and `dim X + 1 = n`.

```lean
public theorem exists_isOpen_projection_isClosedImmersion_and_etaleAt (n : ℕ)
    (hV : Module.finrank k V = n + 1)
    {X : Scheme.{u}} (i : X ⟶ projectiveSpaceOfModule k V) [IsClosedImmersion i]
    [IsVariety k (i ≫ projectiveSpaceOfModuleToSpec k V)]
    (x : X) (hxreg : x ∈ regularLocus X) :
    (topologicalKrullDim X + 1 < (n : WithBot ℕ∞) →
        ∃ U : (projectiveSpaceOfModule k V).Opens,
          (U : Set (projectiveSpaceOfModule k V)).Nonempty ∧
          ∀ p ∈ U, IsClosed ({p} : Set (projectiveSpaceOfModule k V)) →
            ∃ j : X ⟶ (projectionDomain k V (pointSubmodule k V p)).toScheme,
              j ≫ (projectionDomain k V (pointSubmodule k V p)).ι = i ∧
                ∃ R : (projectiveSpaceOfModule k ↥(pointSubmodule k V p)).Opens,
                  (j ≫ projection k V (pointSubmodule k V p)).base x ∈ R ∧
                  IsClosedImmersion ((j ≫ projection k V (pointSubmodule k V p)) ∣_ R)) ∧
      (topologicalKrullDim X + 1 = (n : WithBot ℕ∞) →
        ∃ U : (projectiveSpaceOfModule k V).Opens,
          (U : Set (projectiveSpaceOfModule k V)).Nonempty ∧
          ∀ p ∈ U, IsClosed ({p} : Set (projectiveSpaceOfModule k V)) →
            ∃ j : X ⟶ (projectionDomain k V (pointSubmodule k V p)).toScheme,
              j ≫ (projectionDomain k V (pointSubmodule k V p)).ι = i ∧
                EtaleAt (j ≫ projection k V (pointSubmodule k V p)) x)
```

## Tag 0H8A, a lemma

[Tag 0H8A](https://stacks.math.columbia.edu/tag/0H8A) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_forall_closedPoint_projection_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/GenericProjectionLocalIsomorphism.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Projective/GenericProjectionLocalIsomorphism.lean#L439).

> **Stacks Project, Tag 0H8A.** Let `V` be a finite-dimensional vector space over an
> algebraically closed field `k`, let `Z ⊆ X ⊆ 𝐏(V)` be closed subvarieties with `Z ≠ X` and
> `X ≠ 𝐏(V)`, and let `x` be a point of `Z` which is nonsingular on `X`. Then there is a nonempty
> Zariski open `U ⊆ 𝐏(V)` such that for every closed point `p ∈ U` the projection `r_p` is
> defined on `Z` and the morphism `r_p|_Z : Z → r_p(Z)` is an isomorphism over an open
> neighbourhood of `r_p(x)`.
>
> `X` is a closed subvariety, a closed immersion `iX` whose source is a variety over `k`; `Z` is
> an irreducible closed subscheme of `X`, the closed immersion `e` with `e ≫ iX = iZ` — this
> generalizes the source, which takes `Z` reduced as well. `Z ≠ X` and `X ≠ 𝐏(V)` are `e` and `iX`
> not being isomorphisms. That `r_p` is defined on `Z` is the lift `j` of `iZ` through the domain
> of definition of the projection away from `p`, and the isomorphism of `Z` onto `r_p(Z)` over a
> neighbourhood `N` of `r_p(x)` is spelled as `r_p|_Z` restricted over `N` being a closed
> immersion, which is the same thing: a closed immersion over `N` is an isomorphism of its source
> onto its scheme-theoretic image, and that image is `r_p(Z) ∩ N`.

```lean
public theorem exists_isOpen_forall_closedPoint_projection_restrict {Z X : Scheme.{u}}
    (iZ : Z ⟶ projectiveSpaceOfModule k V) [IsClosedImmersion iZ] [IrreducibleSpace Z]
    (iX : X ⟶ projectiveSpaceOfModule k V) [IsClosedImmersion iX]
    [IsVariety k (iX ≫ projectiveSpaceOfModuleToSpec k V)]
    (e : Z ⟶ X) (he : e ≫ iX = iZ) (hZX : ¬ IsIso e) (hX : ¬ IsIso iX)
    (x : Z) (hreg : e x ∈ regularLocus X) :
    ∃ U : (projectiveSpaceOfModule k V).Opens,
      (U : Set (projectiveSpaceOfModule k V)).Nonempty ∧
      ∀ p ∈ U, IsClosed ({p} : Set (projectiveSpaceOfModule k V)) →
        ∃ j : Z ⟶ (projectionDomain k V (pointSubmodule k V p)).toScheme,
          j ≫ (projectionDomain k V (pointSubmodule k V p)).ι = iZ ∧
          ∃ N : (projectiveSpaceOfModule k ↥(pointSubmodule k V p)).Opens,
            (j ≫ projection k V (pointSubmodule k V p)) x ∈ N ∧
            IsClosedImmersion ((j ≫ projection k V (pointSubmodule k V p)) ∣_ N)
```

## Tag 0B1R, a lemma

[Tag 0B1R](https://stacks.math.columbia.edu/tag/0B1R) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_inter_projectionCone_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/GenericProjectionIntersection.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/GenericProjectionIntersection.lean#L130). The attribute's comment: “the decomposition Y ∩ r\_p^\{-1}(r\_p(Z)) = (Y ∩ Z) ∪ E with E ⊆ Y closed, for every closed point p of a nonempty Zariski open subset of 𝐏(V), and the dimension bound dim E ≤ dim Y + dim Z + 1 - n carrying the hypothesis n ≤ dim Z + 1, that is for Z of codimension at most one, in which range the bound follows from E ⊆ Y; also carrying the hypothesis Y ∪ Z ≠ 𝐏(V), which the source leaves implicit and without which the asserted identity fails, the left-hand side missing p while Y ∩ Z contains it”.

> For closed subsets `Y` and `Z` of `𝐏(V)` whose union is not all of `𝐏(V)`, there is a
> nonempty Zariski open `U` such that for every closed point `p ∈ U` the intersection
> `Y ∩ r_p^{-1}(r_p(Z))` is `(Y ∩ Z) ∪ E` with `E ⊆ Y` closed, and, in the range
> `n ≤ dim Z + 1`, with `dim E ≤ dim Y + dim Z + 1 - n`, where `dim V = n + 1`.
>
> The decomposition and the closedness of `E` are proved for arbitrary closed `Y` and `Z` rather
> than only irreducible ones. The dimension bound is proved in the range `n ≤ dim Z + 1`, that is
> for `Z` of codimension at most one, where it already follows from `E ⊆ Y`; see the implementation
> notes for the incidence-variety argument that gives it in the remaining range, and for the one
> object it needs.

```lean
public theorem exists_isOpen_inter_projectionCone_eq [IsAlgClosed k] [Module.Finite k V]
    {n : ℕ} (hn : Module.finrank k V = n + 1)
    {Y Z : Set (projectiveSpaceOfModule k V)} (hY : IsClosed Y) (hZ : IsClosed Z)
    (hYZ : Y ∪ Z ≠ Set.univ)
    (hdimZ : (n : WithBot ℕ∞) ≤ topologicalKrullDim ↥Z + 1) :
    ∃ U : Set (projectiveSpaceOfModule k V), IsOpen U ∧ U.Nonempty ∧
      ∀ p ∈ U, IsClosed ({p} : Set (projectiveSpaceOfModule k V)) →
        ∃ E : Set (projectiveSpaceOfModule k V), IsClosed E ∧ E ⊆ Y ∧
          topologicalKrullDim ↥E + (n : WithBot ℕ∞) ≤
            topologicalKrullDim ↥Y + topologicalKrullDim ↥Z + 1 ∧
          Y ∩ projectionCone k V p Z = (Y ∩ Z) ∪ E
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_inter_projectionCone_eq_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/GenericProjectionIntersectionBound.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/GenericProjectionIntersectionBound.lean#L137). The attribute's comment: “the decomposition Y ∩ r\_p^\{-1}(r\_p(Z)) = (Y ∩ Z) ∪ E with E ⊆ Y closed and the dimension bound dim E ≤ dim Y + dim Z + 1 - n, for every closed point p of a nonempty Zariski open subset of 𝐏(V); also carrying the hypothesis Y ∪ Z ≠ 𝐏(V), which the source leaves implicit and without which the asserted identity fails, the left-hand side missing p while Y ∩ Z contains it”.

> **Stacks Project, Tag 0B1R.** For closed subsets `Y` and `Z` of `𝐏(V)` whose union is not
> all of `𝐏(V)`, there is a nonempty Zariski open `U` such that for every closed point `p ∈ U` the
> intersection `Y ∩ r_p^{-1}(r_p(Z))` is `(Y ∩ Z) ∪ E` with `E ⊆ Y` closed and
> `dim E ≤ dim Y + dim Z + 1 - n`, where `dim V = n + 1`.
>
> The decomposition, the closedness of `E` and the dimension bound are all proved for arbitrary
> closed `Y` and `Z` rather than only irreducible ones; see the implementation notes for the
> incidence-variety argument behind the bound.

```lean
public theorem exists_isOpen_inter_projectionCone_eq_of_isClosed [IsAlgClosed k] [Module.Finite k V]
    {n : ℕ} (hn : Module.finrank k V = n + 1)
    {Y Z : Set (projectiveSpaceOfModule k V)} (hY : IsClosed Y) (hZ : IsClosed Z)
    (hYZ : Y ∪ Z ≠ Set.univ) :
    ∃ U : Set (projectiveSpaceOfModule k V), IsOpen U ∧ U.Nonempty ∧
      ∀ p ∈ U, IsClosed ({p} : Set (projectiveSpaceOfModule k V)) →
        ∃ E : Set (projectiveSpaceOfModule k V), IsClosed E ∧ E ⊆ Y ∧
          topologicalKrullDim ↥E + (n : WithBot ℕ∞) ≤
            topologicalKrullDim ↥Y + topologicalKrullDim ↥Z + 1 ∧
          Y ∩ projectionCone k V p Z = (Y ∩ Z) ∪ E
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_inter_projectionConeWithVertex_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionConeWithVertex.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectionConeWithVertex.lean#L237). The attribute's comment: “the decomposition Y ∩ r\_p^\{-1}(r\_p(Z)) = (Y ∩ Z) ∪ E with E ⊆ Y closed and dim E ≤ dim Y + dim Z + 1 - n, for every closed point p of a nonempty Zariski open subset of 𝐏(V), with no hypothesis beyond the closedness of Y and Z, reading r\_p^\{-1}(r\_p(Z)) as the cone over Z with vertex p”.

> **Stacks 0B1R.** Let `V` be a vector space of dimension `n + 1` over an algebraically closed
> field and let `Y, Z ⊆ 𝐏(V)` be closed subsets. There is a nonempty Zariski open `U ⊆ 𝐏(V)` such
> that for every closed point `p ∈ U`
>
> `Y ∩ r_p^{-1}(r_p(Z)) = (Y ∩ Z) ∪ E`
>
> with `E ⊆ Y` closed and `dim E ≤ dim Y + dim Z + 1 - n`, where `r_p^{-1}(r_p(Z))` is the cone
> over `Z` with vertex `p`.
>
> No hypothesis beyond the closedness of `Y` and `Z` is needed, and in particular none on `Y ∪ Z`
> or on `dim Z`. The source asks for `Y` and `Z` to be closed subvarieties; the statement is proved
> here for arbitrary closed subsets, which is more general, a subvariety being an irreducible
> reduced closed subscheme.
>
> The open subset produced is `U₀ ∖ Z` for `U₀` the open of the general-fibre bound, when `Z` is
> neither empty nor everything; in those two degenerate cases the cone is respectively empty and
> everything, and `E = ∅` serves over all of `𝐏(V)`. The subset `E` produced in the main case is
> the closure of `(Y ∖ Z) ∩ r_p^{-1}(r_p(Z))`, and its dimension is bounded through the incidence
> variety `T = {(y, z, p) : y ∈ Y ∖ Z, z ∈ Z, p on the line joining y and z}` exactly as in
> `AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_inter_projectionCone_eq_of_union_ne_univ`,
> whose hypothesis `p ∉ Y` is not available here: the vertex `p` may well lie on `Y`, and when it
> does it is itself a point of `(Y ∖ Z) ∩ r_p^{-1}(r_p(Z))` whose membership of the image of the
> fibre is witnessed by the collinear triple `(p, z₀, p)` for any closed point `z₀` of `Z`.
>
> With the punctured reading of `r_p^{-1}(r_p(Z))` carried by
> `AlgebraicGeometry.ProjectiveSpaceOfModule.projectionCone` the statement is false, by
> `AlgebraicGeometry.ProjectiveSpaceOfModule.not_exists_isOpen_inter_projectionCone_univ_eq`, and
> the registrations of this tag on
> `AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_inter_projectionCone_eq` carry the
> hypotheses that reading forces.

```lean
public theorem exists_isOpen_inter_projectionConeWithVertex_eq [IsAlgClosed k] [Module.Finite k V]
    {n : ℕ} (hn : Module.finrank k V = n + 1)
    {Y Z : Set (projectiveSpaceOfModule k V)} (hY : IsClosed Y) (hZ : IsClosed Z) :
    ∃ U : Set (projectiveSpaceOfModule k V), IsOpen U ∧ U.Nonempty ∧
      ∀ p ∈ U, IsClosed ({p} : Set (projectiveSpaceOfModule k V)) →
        ∃ E : Set (projectiveSpaceOfModule k V), IsClosed E ∧ E ⊆ Y ∧
          topologicalKrullDim ↥E + (n : WithBot ℕ∞) ≤
            topologicalKrullDim ↥Y + topologicalKrullDim ↥Z + 1 ∧
          Y ∩ projectionConeWithVertex k V p Z = (Y ∩ Z) ∪ E
```

## Tag 0B2T, a lemma

[Tag 0B2T](https://stacks.math.columbia.edu/tag/0B2T) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_line_disjoint_and_isOpen_sweep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Projective/AvoidingLines.lean, line 591](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Projective/AvoidingLines.lean#L591). The attribute's comment: “the sweeping-out clause is read as the proof reads it: the avoiding lines through `p` cover the closed points of an open subset, their union itself being non-open at `p`”.

> **Stacks 0B2T.** Let `B` be an irreducible closed subset of codimension at least two in the
> projective space of a nonzero finite-dimensional vector space over an algebraically closed field
> and let `p` be a closed point outside `B`. Then some projective line through `p` is disjoint
> from `B`, and the closed points other than `p` lying on such a line are exactly the closed points
> of a nonempty open subset of `𝐏(V)`, namely the complement of the cone over the image of `B`
> under the projection away from `p`. The union of the avoiding lines itself is not open: in a
> projective plane with `B` a point it contains `p` but no neighbourhood of `p`.

```lean
public theorem exists_line_disjoint_and_isOpen_sweep [IsAlgClosed k] [FiniteDimensional k V]
    [Nontrivial V]
    (B : IrreducibleCloseds (projectiveSpaceOfModule k V)) (hcodim : (2 : ℕ∞) ≤ codimension B)
    (p : projectiveSpaceOfModule k V)
    (hp : IsClosed ({p} : Set (projectiveSpaceOfModule k V)))
    (hpB : p ∉ (B : Set (projectiveSpaceOfModule k V))) :
    (∃ W : Submodule k V, Module.finrank k (V ⧸ W) = 2 ∧ p ∈ linearSubspace k V W ∧
        Disjoint (linearSubspace k V W) (B : Set (projectiveSpaceOfModule k V))) ∧
      ∃ U : Set (projectiveSpaceOfModule k V), IsOpen U ∧
        (∃ q ∈ U, IsClosed ({q} : Set (projectiveSpaceOfModule k V))) ∧
        ∀ q, IsClosed ({q} : Set (projectiveSpaceOfModule k V)) → q ≠ p →
          (q ∈ U ↔ ∃ W : Submodule k V, Module.finrank k (V ⧸ W) = 2 ∧
            p ∈ linearSubspace k V W ∧ q ∈ linearSubspace k V W ∧
            Disjoint (linearSubspace k V W) (B : Set (projectiveSpaceOfModule k V)))
```

## Tag 0B2U, a lemma

[Tag 0B2U](https://stacks.math.columbia.edu/tag/0B2U) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.projGenLinGroupEquivInvertibleClasses`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean#L219). The attribute's comment: “identification with the invertible open locus”.

> **`PGL(V)` is the invertible open locus of the projectivized endomorphism space.** The
> quotient presentation of `PGL(V)` sends a projective linear transformation to the projective
> class of any of its linear representatives.

```lean
public noncomputable def projGenLinGroupEquivInvertibleClasses [Nontrivial V] :
    ProjGenLinGroup k V ≃ InvertibleEndomorphismClasses k V
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.projGenLinGroupEquivInvertibleClasses_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean#L226). The attribute's comment: “representative formula for the invertible locus”.

> The equivalence with the invertible locus sends a projective linear transformation to the
> projective class of any of its linear representatives.

```lean
public theorem projGenLinGroupEquivInvertibleClasses_apply [Nontrivial V]
    (g : LinearMap.GeneralLinearGroup k V) (hg : (g : V →ₗ[k] V) ≠ 0) :
    ((projGenLinGroupEquivInvertibleClasses k V) (g : ProjGenLinGroup k V)).val =
      Projectivization.mk k (g : V →ₗ[k] V) hg
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.dualEndClosedPointsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean#L234). The attribute's comment: “closed-point identification for the parameter space”.

> **The closed points of `P((End V)ᵛ)` are the projective classes of endomorphisms.** This is
> the parameter space of a linear projective transformation.

```lean
public noncomputable def dualEndClosedPointsEquiv [IsAlgClosed k] [Module.Finite k V] :
    ClosedPoints k (Module.Dual k (V →ₗ[k] V)) ≃ Projectivization k (V →ₗ[k] V)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.dualEndClosedPointsEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean#L242). The attribute's comment: “annihilator formula for the parameter-space identification”.

> The parameter point corresponding to a class of endomorphisms is cut out by the linear forms
> annihilating that class. This fixes the identification.

```lean
public theorem dualEndClosedPointsEquiv_apply [IsAlgClosed k] [Module.Finite k V]
    (p : ClosedPoints k (Module.Dual k (V →ₗ[k] V))) (φ : Module.Dual k (V →ₗ[k] V)) :
    SymmetricAlgebra.ι k (Module.Dual k (V →ₗ[k] V)) φ ∈ p.val.asHomogeneousIdeal ↔
      φ ((dualEndClosedPointsEquiv k V p).rep) = 0
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.parameterPointToProjGenLinGroup_of_rep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean#L275). The attribute's comment: “parameter point to projective linear transformation”.

> A parameter point represented by `g` names the class of `g` in `PGL(V)`.

```lean
public theorem parameterPointToProjGenLinGroup_of_rep
    [Nontrivial V] [IsAlgClosed k] [Module.Finite k V]
    (p : InvertibleParameterPoints k V) (g : LinearMap.GeneralLinearGroup k V)
    (hg : (g : V →ₗ[k] V) ≠ 0)
    (hpg : (dualEndClosedPointsEquiv k V) p.val = Projectivization.mk k (g : V →ₗ[k] V) hg) :
    parameterPointToProjGenLinGroup k V p = (g : ProjGenLinGroup k V)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.parameterPoint_smul_eq_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean#L290). The attribute's comment: “compatibility of the parameter-point action”.

> On a parameter point represented by `g`, the morphism in the moving family is the action of
> the inverse element of `PGL(V)`; the inversion accounts for the contravariance of `Proj`.

```lean
public theorem parameterPoint_smul_eq_map
    [Nontrivial V] [IsAlgClosed k] [Module.Finite k V]
    (p : InvertibleParameterPoints k V) (g : LinearMap.GeneralLinearGroup k V)
    (hg : (g : V →ₗ[k] V) ≠ 0)
    (hpg : (dualEndClosedPointsEquiv k V) p.val = Projectivization.mk k (g : V →ₗ[k] V) hg)
    (x : projectiveSpaceOfModule k V) :
    (parameterPointToProjGenLinGroup k V p)⁻¹ • x = map k V g x
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.projGenLinGroup_is_two_pretransitive`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjectiveLinearGroup.lean#L316).

> **Stacks Project, Tag 0B2U.** The projective general linear group of a finite-dimensional
> vector space over an algebraically closed field acts doubly transitively on the closed points of
> its projective space.

```lean
public lemma projGenLinGroup_is_two_pretransitive [IsAlgClosed k] [Module.Finite k V] :
    MulAction.IsMultiplyPretransitive (ProjGenLinGroup k V) (ClosedPoints k V) 2
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.mapDomain_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjMapComparison.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjMapComparison.lean#L55). The attribute's comment: “the invertible locus has full projective domain”.

> An invertible linear map has everywhere-defined projective morphism: the domain of
> definition of the induced graded ring homomorphism is all of `P(V)`.

```lean
public theorem mapDomain_eq_top (g : LinearMap.GeneralLinearGroup k V) :
    mapDomain (fun n => SymPow.symmetricPower n k V) (fun n => SymPow.symmetricPower n k V)
      (SymPow.gradedSymAlgMap (g : V →ₗ[k] V)) = ⊤
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.mapDomain_ι_comp_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjMapComparison.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/ProjMapComparison.lean#L63). The attribute's comment: “compatibility with the projective transformation family”.

> On the domain of definition of the induced graded ring homomorphism, the morphism carrying
> the comparison maps on all twists is the action of `g` on `P(V)`.

```lean
public theorem mapDomain_ι_comp_map (g : LinearMap.GeneralLinearGroup k V) :
    (mapDomain (fun n => SymPow.symmetricPower n k V) (fun n => SymPow.symmetricPower n k V)
          (SymPow.gradedSymAlgMap (g : V →ₗ[k] V))).ι ≫ map k V g =
      (projMapData (fun n => SymPow.symmetricPower n k V)
        (fun n => SymPow.symmetricPower n k V)
        (SymPow.gradedSymAlgMap (g : V →ₗ[k] V))).hom
```

## Tag 0B2V, a lemma

[Tag 0B2V](https://stacks.math.columbia.edu/tag/0B2V) in the Stacks Project.

**`MvPolynomial.irreducible_det_genericMatrix`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/Basic.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/Basic.lean#L225).

> **Stacks Project, Tag 0B2V.** The determinant of the generic square matrix of positive
> size over a field is an irreducible multivariate polynomial.

```lean
lemma irreducible_det_genericMatrix (k : Type*) [Field k] (n : ℕ) (hn : 0 < n) :
    Irreducible (Matrix.det (fun i j : Fin n ↦ MvPolynomial.X (i, j) :
      Matrix (Fin n) (Fin n) (MvPolynomial (Fin n × Fin n) k)))
```

## Tag 0B2W, an equation

[Tag 0B2W](https://stacks.math.columbia.edu/tag/0B2W) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endDomain`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L73). The attribute's comment: “the open U(ψ) over the point [g] of the parameter space, i.e. U(g)”.

> The open `U(g)` on which the projective transformation attached to an endomorphism `g` of
> `V` is defined: the domain of definition of the morphism of projective spectra induced by
> `Sym g`.

```lean
public abbrev endDomain (g : V →ₗ[k] V) : (projectiveSpaceOfModule k V).Opens
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L80). The attribute's comment: “the morphism r\_ψ over the point [g] of the parameter space, i.e. r\_g”.

> The projective transformation `r_g : 𝐏(V) ⊇ U(g) → 𝐏(V)` attached to an endomorphism `g`
> of `V`: the morphism of projective spectra induced by `Sym g` on its domain of definition.

```lean
public def endProjection (g : V →ₗ[k] V) :
    (endDomain k V g).toScheme ⟶ projectiveSpaceOfModule k V
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.notMem_endDomain_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L101). The attribute's comment: “the complement of U(g) is the image of the closed immersion 𝐏(Coker g) → 𝐏(V)”.

> A point of `𝐏(V)` lies outside `U(g)` exactly when it lies on the
> linear subspace cut out by the image of `g`, that is on `𝐏(Coker g) ⊆ 𝐏(V)`.

```lean
public theorem notMem_endDomain_iff (g : V →ₗ[k] V) (q : projectiveSpaceOfModule k V) :
    q ∉ endDomain k V g ↔ q ∈ linearSubspace k V (LinearMap.range g)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endProjection_eq_linearFunctionalPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L150). The attribute's comment: “the value of r\_g on a closed point, namely f ↦ f ∘ g”.

> The morphism `r_g` sends the point cut out by a functional `f` on `V` to the point cut out by
> `f ∘ g`.

```lean
public theorem endProjection_eq_linearFunctionalPoint (g : V →ₗ[k] V)
    (y : (endDomain k V g).toScheme) (f : Module.Dual k V) (hf : f ≠ 0) (hfg : f ∘ₗ g ≠ 0)
    (hy : (y.val : projectiveSpaceOfModule k V) = linearFunctionalPoint k V f hf) :
    endProjection k V g y = linearFunctionalPoint k V (f ∘ₗ g) hfg
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.range_endProjection_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L161). The attribute's comment: “the image of r\_g is contained in the image of 𝐏(Im g) → 𝐏(V)”.

> Every point in the image of `r_g` lies on the linear subspace cut out by the kernel of `g`,
> which is the image of `𝐏(Im g) → 𝐏(V)`.

```lean
public theorem range_endProjection_subset (g : V →ₗ[k] V) :
    Set.range (endProjection k V g).base ⊆ linearSubspace k V (LinearMap.ker g)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_endProjection_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L186). The attribute's comment: “the image of r\_g is the image of 𝐏(Im g) → 𝐏(V), on closed points”.

> Over an algebraically closed field
> every closed point of the linear subspace cut out by the kernel of `g` — that is, of the image
> of `𝐏(Im g) → 𝐏(V)` — is the image under `r_g` of a point of `U(g)`.

```lean
public theorem exists_endProjection_eq [IsAlgClosed k] [Module.Finite k V] (g : V →ₗ[k] V)
    (q : projectiveSpaceOfModule k V)
    (hq : IsClosed ({q} : Set (projectiveSpaceOfModule k V)))
    (hmem : q ∈ linearSubspace k V (LinearMap.ker g)) :
    ∃ y : (endDomain k V g).toScheme, endProjection k V g y = q
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endDomain_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L227). The attribute's comment: “U(g) depends only on the point [g] of the parameter space”.

> A unit multiple of `g` has the same domain of definition `U(g)`.

```lean
public theorem endDomain_smul (c : kˣ) (g : V →ₗ[k] V) :
    endDomain k V ((c : k) • g) = endDomain k V g
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endProjection_smul_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/EndomorphismProjection.lean#L235). The attribute's comment: “r\_g depends only on the point [g] of the parameter space, on closed points”.

> A unit multiple of `g` induces the same morphism `r_g` on the points cut out by linear
> functionals.

```lean
public theorem endProjection_smul_apply (c : kˣ) (g : V →ₗ[k] V)
    (y : (endDomain k V ((c : k) • g)).toScheme) (y' : (endDomain k V g).toScheme)
    (f : Module.Dual k V) (hf : f ≠ 0) (hfg : f ∘ₗ g ≠ 0)
    (hy : (y.val : projectiveSpaceOfModule k V) = linearFunctionalPoint k V f hf)
    (hy' : (y'.val : projectiveSpaceOfModule k V) = linearFunctionalPoint k V f hf) :
    endProjection k V ((c : k) • g) y = endProjection k V g y'
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndCoeff`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L237). The attribute's comment: “the canonical map V → V ⊗ Eᵛ = Hom(E, V), v ↦ (g ↦ g v)”.

> **The canonical map `V → (End V)ᵛ ⊗ V = Hom(End V, V)`** of the source, sending `v` to the
> evaluation `g ↦ g v`.

```lean
public def universalEndCoeff : V →ₗ[k] Module.Dual k (V →ₗ[k] V) ⊗[k] V
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEnd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L246). The attribute's comment: “ψ over the affine parameter space Spec Sym(Eᵛ), the cone over 𝐏: the universal endomorphism of V ⊗ 𝒪, in place of the map of sheaves V ⊗ 𝒪\_𝐏 → V ⊗ 𝒪\_𝐏(1) over 𝐏”.

> **The universal endomorphism `ψ` of `V ⊗ 𝒪` over the affine parameter space**: the `A`-linear
> extension of the canonical map `V → (End V)ᵛ ⊗ V ⊆ A ⊗ V`. On the fibre over an endomorphism `g`
> it is `g`.

```lean
public def universalEnd :
    endParamRing k V ⊗[k] V →ₗ[endParamRing k V] endParamRing k V ⊗[k] V
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndDomain`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L260). The attribute's comment: “U(ψ) ⊆ 𝐏(V ⊗ 𝒪\_S) for S = Spec Sym(Eᵛ) the affine parameter space, the cone over 𝐏; the open over 𝐏 itself is AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafDomain, built there from the source's own ψ : V ⊗ 𝒪\_𝐏 → V ⊗ 𝒪\_𝐏(1) and not from this one by descent along 𝔸(E) ∖ \{0} → 𝐏, which is constructed nowhere; what is not identified with 𝐏 × 𝐏(V) is its ambient 𝐏(V ⊗ 𝒪\_𝐏(1))”.

> **The open `U(ψ)` of the universal family**: the domain of definition of the morphism of
> relative projective spaces induced by `Sym ψ` over the affine parameter space.

```lean
public abbrev universalEndDomain :
    (projectiveSpaceOfModule (endParamRing k V) (endParamRing k V ⊗[k] V)).Opens
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L272). The attribute's comment: “r\_ψ : U(ψ) → 𝐏(V ⊗ 𝒪\_S) for S = Spec Sym(Eᵛ) the affine parameter space, the cone over 𝐏; the morphism over 𝐏 itself is AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafProjection, built there from the source's own ψ and not from this one by descent along 𝔸(E) ∖ \{0} → 𝐏, which is constructed nowhere; what is not identified with 𝐏 × 𝐏(V) are its total spaces”.

> **The universal family `r_ψ` of projective transformations**, `𝐏(V ⊗ 𝒪_S) ⊇ U(ψ) → 𝐏(V ⊗ 𝒪_S)`
> over the affine space `S` of endomorphisms of `V`: the morphism of relative projective spaces
> induced by `Sym ψ` on its domain of definition.

```lean
public def universalEndProjection :
    (universalEndDomain k V).toScheme ⟶
      projectiveSpaceOfModule (endParamRing k V) (endParamRing k V ⊗[k] V)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endParamFibre_universalEnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L314). The attribute's comment: “the fibre of ψ over the parameter point of g is g”.

> **The fibre of the universal endomorphism over the parameter point of `g` is `g`.** This is
> what makes `universalEnd` universal: the family it defines has `r_g` as its fibre over `g`.

```lean
public theorem endParamFibre_universalEnd (g : V →ₗ[k] V) (x : endParamRing k V ⊗[k] V) :
    endParamFibre k V g (universalEnd k V x) = g (endParamFibre k V g x)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endParamFibreHom_symAlgMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L380). The attribute's comment: “the fibre of r\_ψ over the parameter point of g is r\_g, on the homogeneous coordinate rings: Sym ψ reduces to Sym g”.

> **`Sym g` is the fibre of `Sym ψ` over the parameter point of `g`.** Reducing the universal
> graded endomorphism of `Sym_A(V ⊗ A)` along the point of the parameter space attached to an
> endomorphism `g` of `V` gives the graded endomorphism `Sym g` of `Sym_k(V)` out of which `U(g)`
> and `r_g` are built.

```lean
public theorem endParamFibreHom_symAlgMap (g : V →ₗ[k] V)
    (x : SymmetricAlgebra (endParamRing k V) (endParamRing k V ⊗[k] V)) :
    endParamFibreHom k V g (SymPow.symAlgMap (universalEnd k V) x) =
      SymPow.symAlgMap g (endParamFibreHom k V g x)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endParamFibreInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L477). The attribute's comment: “the inclusion of the fibre of 𝐏(V ⊗ 𝒪\_S) over the parameter point of g”.

> **The fibre of the universal family over the parameter point of `g`**: the morphism
> `𝐏(V) → 𝐏(V ⊗ 𝒪_S)` induced by the specialization of the homogeneous coordinate ring, defined on
> all of `𝐏(V)` by `endParamFibreInclusionDomain_eq_top`.

```lean
public def endParamFibreInclusion (g : V →ₗ[k] V) :
    (endParamFibreInclusionDomain k V g).toScheme ⟶
      projectiveSpaceOfModule (endParamRing k V) (endParamRing k V ⊗[k] V)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.mem_universalEndDomain_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L486). The attribute's comment: “U(g) is the fibre U(ψ) over the parameter point of g”.

> **`U(g)` is the fibre `U(ψ)` over the parameter point of `g`.** A point of `𝐏(V)`, included
> as a point of the fibre of the relative projective space over the parameter point of `g`, lies in
> the domain of the universal family exactly when it lies in `U(g)`, the domain of `r_g`.

```lean
public theorem mem_universalEndDomain_iff (g : V →ₗ[k] V)
    (y : (endParamFibreInclusionDomain k V g).toScheme) :
    (endParamFibreInclusion k V g).base y ∈ universalEndDomain k V ↔
      (y.val : projectiveSpaceOfModule k V) ∈ endDomain k V g
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.notMem_universalEndDomain_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L535). The attribute's comment: “the complement of U(ψ) is the relative 𝐏(Coker ψ), as the vanishing of the degree-one forms in the image of ψ”.

> **The domain of the universal family.** A point lies outside `U(ψ)` exactly when every
> degree-one form in the image of the universal endomorphism vanishes at it: the relative form of
> the description of the complement of `U(g)` as the image of `𝐏(Coker g) → 𝐏(V)`.

```lean
public theorem notMem_universalEndDomain_iff
    (q : projectiveSpaceOfModule (endParamRing k V) (endParamRing k V ⊗[k] V)) :
    q ∉ universalEndDomain k V ↔
      ∀ x : endParamRing k V ⊗[k] V,
        SymmetricAlgebra.ι (endParamRing k V) (endParamRing k V ⊗[k] V) (universalEnd k V x) ∈
          q.asHomogeneousIdeal
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndProjection_comp_toSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L573). The attribute's comment: “r\_ψ is a morphism over the parameter space S = Spec Sym(Eᵛ), the cone over 𝐏”.

> **The universal family is a family over the parameter space.** The morphism `r_ψ` commutes
> with the two structure morphisms of the relative projective space `𝐏(V ⊗ 𝒪_S)` to
> `S = Spec Sym((End V)ᵛ)`, so it is a family of projective transformations parametrized by `S`
> and its fibres are morphisms of the fibres.

```lean
public theorem universalEndProjection_comp_toSpec :
    universalEndProjection k V ≫
        projectiveSpaceOfModuleToSpec (endParamRing k V) (endParamRing k V ⊗[k] V) =
      (universalEndDomain k V).ι ≫
        projectiveSpaceOfModuleToSpec (endParamRing k V) (endParamRing k V ⊗[k] V)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.endParamFibreInclusion_comp_toSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L598). The attribute's comment: “the fibre inclusion is a morphism over the parameter point of g”.

> **The fibre of the relative projective space over the parameter point of `g` is where `𝐏(V)`
> goes.** The inclusion `ι_g : 𝐏(V) → 𝐏(V ⊗ 𝒪_S)` is a morphism over the point of `S` attached to
> `g`, which is what makes it the inclusion of a fibre rather than merely a morphism.

```lean
public theorem endParamFibreInclusion_comp_toSpec (g : V →ₗ[k] V) :
    endParamFibreInclusion k V g ≫
        projectiveSpaceOfModuleToSpec (endParamRing k V) (endParamRing k V ⊗[k] V) =
      (endParamFibreInclusionDomain k V g).ι ≫ projectiveSpaceOfModuleToSpec k V ≫
        Spec.map (CommRingCat.ofHom (endParamPoint k V g).toRingHom)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.fibreSquareIso_hom_comp_morphismRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 655](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L655). The attribute's comment: “the fibre of r\_ψ over the parameter point of g is r\_g, as scheme morphisms”.

> **`r_g` is the fibre of `r_ψ` over the parameter point of `g`, as a square of scheme
> morphisms.** Including the fibre `𝐏(V)` into the relative projective space and then applying the
> universal family `r_ψ` is the same as applying `r_g` and then including the fibre: the square
>
> `U(g) --r_g--> 𝐏(V) --ι_g--> 𝐏(V ⊗ 𝒪_S)`,  `U(g) --ι_g--> U(ψ) --r_ψ--> 𝐏(V ⊗ 𝒪_S)`
>
> commutes, after the canonical identification `fibreSquareIso` of the two domains.
>
> This is the composition law of Tag 01MZ applied to the two factorizations
> `endParamFibreGradedHom_comp_gradedSymAlgMap` of a single graded ring homomorphism.

```lean
public theorem fibreSquareIso_hom_comp_morphismRestrict (g : V →ₗ[k] V) :
    (fibreSquareIso k V g).hom ≫
        (endParamFibreInclusion k V g ∣_ universalEndDomain k V) ≫ universalEndProjection k V =
      (endProjection k V g ∣_ endParamFibreInclusionDomain k V g) ≫
        endParamFibreInclusion k V g
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.isPullback_universalFamilySpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 674](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L674). The attribute's comment: “the total space of the family is the product 𝔸(E) × 𝐏(V), for 𝔸(E) = Spec Sym(Eᵛ) the cone over 𝐏; the source writes the displayed family on 𝐏 × 𝐏(V)”.

> **The relative projective space of the family is a product.** The square formed by the
> projection `𝐏(V ⊗ 𝒪_S) ⟶ 𝐏(V)` and the two structure morphisms is cartesian, so
> `𝐏(V ⊗ 𝒪_S) = S ×_{Spec k} 𝐏(V)` with `S = Spec Sym((End V)ᵛ)` the affine space of
> endomorphisms. This is `Stacks.ProjectiveSpaceBaseChange.isPullback_projectiveSpaceOfModuleToSpec`
> for the base change of `V` along `k → Sym((End V)ᵛ)`.

```lean
public theorem isPullback_universalFamilySpace :
    IsPullback (Stacks.ProjectiveSpaceBaseChange.map k (endParamRing k V) V)
      (projectiveSpaceOfModuleToSpec (endParamRing k V) (endParamRing k V ⊗[k] V))
      (projectiveSpaceOfModuleToSpec k V)
      (Spec.map (CommRingCat.ofHom (algebraMap k (endParamRing k V))))
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalFamilySpaceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean, line 686](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalEndomorphismFamily.lean#L686). The attribute's comment: “the identification 𝐏(V ⊗ 𝒪\_S) = 𝔸(E) × 𝐏(V) over the cone 𝔸(E) = Spec Sym(Eᵛ)”.

> **The total space of the family, as the product `𝔸(E) × 𝐏(V)`.** The identification of
> `𝐏(V ⊗ 𝒪_S)` with the fibre product of `𝐏(V)` and the affine space of endomorphisms over
> `Spec k`, carried by `isPullback_universalFamilySpace`.

```lean
public def universalFamilySpaceIso :
    projectiveSpaceOfModule (endParamRing k V) (endParamRing k V ⊗[k] V) ≅
      Limits.pullback (projectiveSpaceOfModuleToSpec k V)
        (Spec.map (CommRingCat.ofHom (algebraMap k (endParamRing k V))))
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean#L464). The attribute's comment: “ψ : V ⊗ 𝒪\_𝐏 → V ⊗ 𝒪\_𝐏(1) over the projective parameter space 𝐏 = 𝐏(Eᵛ)”.

> **The map of sheaves `ψ : V ⊗ 𝒪_𝐏 ⟶ V ⊗ 𝒪_𝐏(1)` over the projective parameter space
> `𝐏 = 𝐏(Eᵛ)`**, attached by the universal property of `V ⊗ 𝒪_𝐏` to the canonical `k`-linear map
> `V → Γ(𝐏, V ⊗ 𝒪_𝐏(1))`.

```lean
def universalEndSheafMap :
    constantModule k (dualEndSpace k V) V ⟶
      twistObj k (dualEndSpace k V) (constantModule k (dualEndSpace k V) V) ((1 : ℕ) : ℤ)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafDomain`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean#L475). The attribute's comment: “U(ψ) ⊆ 𝐏(V ⊗ 𝒪\_𝐏(1)) over the projective parameter space 𝐏 = 𝐏(Eᵛ); its identification with an open subscheme of the displayed 𝐏 × 𝐏(V) is exists\_iso\_universalEndFamily\_selfMap”.

> **The open `U(ψ) ⊆ 𝐏(V ⊗ 𝒪_𝐏(1))`** of the universal family over the projective parameter
> space: Tag 07ZG's open for `Sym ψ`.

```lean
abbrev universalEndSheafDomain :
    (schemeProjectiveBundle
      (twistObj k (dualEndSpace k V) (constantModule k (dualEndSpace k V) V) ((1 : ℕ) : ℤ))
      (isQuasicoherentPieces_of_isQuasicoherent _)).scheme.Opens
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean#L487). The attribute's comment: “r\_ψ : U(ψ) → 𝐏(V ⊗ 𝒪\_𝐏) over the projective parameter space 𝐏 = 𝐏(Eᵛ); read through the identifications of both total spaces with 𝐏 × 𝐏(V) over 𝐏, it is the displayed self-map, exists\_iso\_universalEndFamily\_selfMap”.

> **The universal family of projective transformations over the projective parameter space**,
> `𝐏(V ⊗ 𝒪_𝐏(1)) ⊇ U(ψ) --r_ψ--> 𝐏(V ⊗ 𝒪_𝐏)`: the partially defined morphism of relative
> projective spaces that Tag 07ZG attaches to `Sym ψ`.

```lean
def universalEndSheafProjection :
    (universalEndSheafDomain k V).toScheme ⟶
      (schemeProjectiveBundle (constantModule k (dualEndSpace k V) V)
        (isQuasicoherentPieces_of_isQuasicoherent _)).scheme
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafProjection_comp_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyOverProjectiveSpace.lean#L496). The attribute's comment: “the universal family over 𝐏 = 𝐏(Eᵛ) is a morphism over 𝐏”.

> **The universal family is a family over the parameter space `𝐏`**: `r_ψ` is a morphism over
> `𝐏`, so it is a family of maps of the fibres and not merely a morphism of schemes.

```lean
theorem universalEndSheafProjection_comp_toBase :
    universalEndSheafProjection k V ≫
        schemeProjectiveBundleToBase (constantModule k (dualEndSpace k V) V)
          (isQuasicoherentPieces_of_isQuasicoherent _) =
      (universalEndSheafDomain k V).ι ≫
        schemeProjectiveBundleToBase
          (twistObj k (dualEndSpace k V)
            (constantModule k (dualEndSpace k V) V) ((1 : ℕ) : ℤ))
          (isQuasicoherentPieces_of_isQuasicoherent _)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_iso_pullback_universalEndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyProductSpace.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyProductSpace.lean#L176). The attribute's comment: “the identification 𝐏(V ⊗ 𝒪\_𝐏) = 𝐏 × 𝐏(V) over the projective parameter space 𝐏 = 𝐏(Eᵛ), the target of r\_ψ; the second factor is the projective bundle of Ṽ over Spec k”.

> **The target of Tag 0B2W's universal family is the product `𝐏 × 𝐏(V)`.** The relative
> projective space `𝐏(V ⊗ 𝒪_𝐏)` over the projective parameter space `𝐏 = 𝐏(Eᵛ)` is the fibre
> product of `𝐏` with the projective space of `V` over `Spec k`, by an isomorphism over `𝐏`.
>
> This is the first of the two identifications Tag 0B2W's display uses, and it is the base change
> of a relative homogeneous spectrum (Tag 01O3) along the structure morphism of `𝐏`, which is not
> an affine morphism and over which nothing is assumed.

```lean
public theorem exists_iso_pullback_universalEndTarget :
    ∃ e : (Stacks.SymGraded.schemeProjectiveBundle
          (constantModule k (dualEndSpace k V) V)
          (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).scheme ≅
        pullback (projectiveSpaceOfModuleToSpec k (dualEndSpace k V))
          (Stacks.SymGraded.schemeProjectiveBundle
            (AlgebraicGeometry.tilde (ModuleCat.of (CommRingCat.of k) V))
            (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).toBase,
      e.hom ≫ pullback.fst (projectiveSpaceOfModuleToSpec k (dualEndSpace k V))
          (Stacks.SymGraded.schemeProjectiveBundle
            (AlgebraicGeometry.tilde (ModuleCat.of (CommRingCat.of k) V))
            (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).toBase =
        (Stacks.SymGraded.schemeProjectiveBundle
          (constantModule k (dualEndSpace k V) V)
          (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).toBase
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isPullback_universalEndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyProductSpace.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyProductSpace.lean#L204). The attribute's comment: “the identification 𝐏(V ⊗ 𝒪\_𝐏) = 𝐏 × 𝐏(V) as a cartesian square over Spec k, the affine-cone product identification carried over to the projective parameter space 𝐏 = 𝐏(Eᵛ)”.

> **The target of Tag 0B2W's universal family is the product `𝐏 × 𝐏(V)`, as a cartesian
> square.** The projection of `𝐏(V ⊗ 𝒪_𝐏)` to `𝐏`, the comparison with the projective space of `V`
> over `Spec k` and the two structure morphisms form a cartesian square.
>
> This is the statement `AlgebraicGeometry.ProjectiveSpaceOfModule.isPullback_universalFamilySpace`
> over the projective parameter space `𝐏` instead of over the affine cone `𝔸(E)`.

```lean
public theorem exists_isPullback_universalEndTarget :
    ∃ q : (Stacks.SymGraded.schemeProjectiveBundle
          (constantModule k (dualEndSpace k V) V)
          (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).scheme ⟶
        (Stacks.SymGraded.schemeProjectiveBundle
          (AlgebraicGeometry.tilde (ModuleCat.of (CommRingCat.of k) V))
          (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).scheme,
      IsPullback (Stacks.SymGraded.schemeProjectiveBundle
          (constantModule k (dualEndSpace k V) V)
          (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).toBase q
        (projectiveSpaceOfModuleToSpec k (dualEndSpace k V))
        (Stacks.SymGraded.schemeProjectiveBundle
          (AlgebraicGeometry.tilde (ModuleCat.of (CommRingCat.of k) V))
          (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).toBase
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_iso_pullback_universalEndTarget_comp_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyProductSpace.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilyProductSpace.lean#L228). The attribute's comment: “r\_ψ followed by the identification of its target with 𝐏 × 𝐏(V) is a morphism over 𝐏, the first projection of the product”.

> **The universal family is a family over `𝐏` read on the product.** Composing
> `AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafProjection_comp_toBase` with the
> identification of the target with `𝐏 × 𝐏(V)`: the first projection of the product, pulled back
> along `r_ψ` and the identification, is the projection of `U(ψ)` to `𝐏`.

```lean
public theorem exists_iso_pullback_universalEndTarget_comp_toBase :
    ∃ e : (Stacks.SymGraded.schemeProjectiveBundle
          (constantModule k (dualEndSpace k V) V)
          (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).scheme ≅
        pullback (projectiveSpaceOfModuleToSpec k (dualEndSpace k V))
          (Stacks.SymGraded.schemeProjectiveBundle
            (AlgebraicGeometry.tilde (ModuleCat.of (CommRingCat.of k) V))
            (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).toBase,
      (universalEndSheafProjection k V ≫ e.hom) ≫
          pullback.fst (projectiveSpaceOfModuleToSpec k (dualEndSpace k V))
            (Stacks.SymGraded.schemeProjectiveBundle
              (AlgebraicGeometry.tilde (ModuleCat.of (CommRingCat.of k) V))
              (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)).toBase =
        (universalEndSheafDomain k V).ι ≫
          Stacks.SymGraded.schemeProjectiveBundleToBase
            (twistObj k (dualEndSpace k V)
              (constantModule k (dualEndSpace k V) V) ((1 : ℕ) : ℤ))
            (Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent _)
```

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_iso_universalEndFamily_selfMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilySelfMap.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/UniversalFamilySelfMap.lean#L145). The attribute's comment: “the universal family of projective transformations as the displayed partially defined self-map of 𝐏 × 𝐏(V): both total spaces identified with the product over 𝐏, U(ψ) as an open subscheme of the product, and r\_ψ as a morphism of the product over 𝐏”.

> **[Stacks, Tag 0B2W].** The universal family of projective transformations of a
> finite-dimensional vector space `V` over a field `k`, read as the partially defined self-map
>
> `𝐏 × 𝐏(V) ⊇ U(ψ) --r_ψ--> 𝐏 × 𝐏(V)`
>
> of the product of the parameter space `𝐏 = 𝐏(Eᵛ)`, `E = End(V)`, with the projective space of
> `V`, as the source displays it.
>
> Both total spaces of the family built in
> `AlgebraicGeometry.ProjectiveSpaceOfModule.universalEndSheafProjection` — the twisted
> `𝐏(V ⊗ 𝒪_𝐏(1))` and the untwisted `𝐏(V ⊗ 𝒪_𝐏)` — are isomorphic to `𝐏 × 𝐏(V)` by isomorphisms
> over `𝐏`; under the first of them the domain of definition `U(ψ)` becomes an open subscheme of
> `𝐏 × 𝐏(V)`, and `r_ψ`, read through the second, is a morphism from that open subscheme to
> `𝐏 × 𝐏(V)` over `𝐏`, hence a family of partially defined self-maps of `𝐏(V)` indexed by `𝐏`.

```lean
theorem exists_iso_universalEndFamily_selfMap :
    ∃ (α : (schemeProjectiveBundle (twistObj k (dualEndSpace k V)
          (constantModule k (dualEndSpace k V) V) ((1 : ℕ) : ℤ))
          (isQuasicoherentPieces_of_isQuasicoherent _)).scheme ≅ universalProductSpace k V)
      (β : (schemeProjectiveBundle (constantModule k (dualEndSpace k V) V)
          (isQuasicoherentPieces_of_isQuasicoherent _)).scheme ≅ universalProductSpace k V),
      α.hom ≫ universalProductToParam k V =
          schemeProjectiveBundleToBase (twistObj k (dualEndSpace k V)
            (constantModule k (dualEndSpace k V) V) ((1 : ℕ) : ℤ))
            (isQuasicoherentPieces_of_isQuasicoherent _) ∧
        β.hom ≫ universalProductToParam k V =
          schemeProjectiveBundleToBase (constantModule k (dualEndSpace k V) V)
            (isQuasicoherentPieces_of_isQuasicoherent _) ∧
        IsOpenImmersion ((universalEndSheafDomain k V).ι ≫ α.hom) ∧
        (universalEndSheafProjection k V ≫ β.hom) ≫ universalProductToParam k V =
          ((universalEndSheafDomain k V).ι ≫ α.hom) ≫ universalProductToParam k V
```

## Tag 0B1S, a lemma

[Tag 0B1S](https://stacks.math.columbia.edu/tag/0B1S) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpaceOfModule.exists_isOpen_forall_closedPoint_line_subset_endDomain_intersectProperly`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/Projections/GeneralLineIntersectProperly.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/Projections/GeneralLineIntersectProperly.lean#L74). The attribute's comment: “both clauses (1) X ⊆ U(g) and (2) g(X) intersects Y properly, for every [g] on a general line through [id\_V], at the source's hypotheses; 'general' means: there is a nonempty Zariski open subset of 𝐏 = 𝐏((End V)ᵛ) each of whose closed points lies with [id\_V] on such a line (as in Tag 0B2T); clause (2) is IntersectProperly (Tag 0AZQ) of the closed subvariety r\_g(X) with Y”.

> **Stacks Project, Tag 0B1S.** Let `X, Y` be closed subvarieties of `𝐏(V)` which intersect
> properly, with `X ≠ 𝐏(V)` and `X ∩ Y ≠ ∅`. Then for a general line `ℓ ⊆ 𝐏 = 𝐏((End V)ᵛ)` with
> `[id_V] ∈ ℓ` — that is, for the line through `[id_V]` and any closed point of a nonempty Zariski
> open subset of `𝐏` — every representative `g` of every closed point `[g]` of `ℓ` satisfies
>
> 1. `X ⊆ U(g)`, and
> 2. `g(X) = r_g(X)` is a closed subvariety `W` of `𝐏(V)` which intersects `Y` properly.

```lean
public theorem exists_isOpen_forall_closedPoint_line_subset_endDomain_intersectProperly
    (X Y : IrreducibleCloseds (projectiveSpaceOfModule k V)) (hXY : IntersectProperly X Y)
    (hXne : (X : Set (projectiveSpaceOfModule k V)) ≠ Set.univ)
    (hXYne : ((X : Set (projectiveSpaceOfModule k V)) ∩
      (Y : Set (projectiveSpaceOfModule k V))).Nonempty) :
    ∃ U : Set (projectiveSpaceOfModule k (ParameterModule k V)), IsOpen U ∧ U.Nonempty ∧
      ∀ q ∈ U, IsClosed ({q} : Set (projectiveSpaceOfModule k (ParameterModule k V))) →
        ∃ L : Submodule k (ParameterModule k V),
          Module.finrank k (ParameterModule k V ⧸ L) = 2 ∧
          identityParameterPoint k V ∈ linearSubspace k (ParameterModule k V) L ∧
          q ∈ linearSubspace k (ParameterModule k V) L ∧
          ∀ p : ClosedPoints k (ParameterModule k V),
            (p : projectiveSpaceOfModule k (ParameterModule k V)) ∈
              linearSubspace k (ParameterModule k V) L →
            ∀ g : V →ₗ[k] V, RepresentsParameterPoint k V p g →
              (X : Set (projectiveSpaceOfModule k V)) ⊆
                  (endDomain k V g : Set (projectiveSpaceOfModule k V)) ∧
                ∃ W : IrreducibleCloseds (projectiveSpaceOfModule k V),
                  (W : Set (projectiveSpaceOfModule k V)) =
                      endProjectionImage k V g (X : Set (projectiveSpaceOfModule k V)) ∧
                    IntersectProperly W Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.23, Tag 0B1N](https://stacks.math.columbia.edu/tag/0B1N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
