---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsAdmissibleBlowup, AlgebraicGeometry.Space.isAdmissibleBlowup_comp_of_isQuasiCompactSpace, AlgebraicGeometry.Space.IsBlowupAlong.exists_restrictionToOpen, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_isPullback', AlgebraicGeometry.Space.exists_isAdmissibleBlowup_factoring, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_factoring_isAdmissibleBlowup, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_disjoint_openSubspace_decomposition'
statement: formalized
proof: formalized
---

# 71.19 Admissible blowups

Section 71.19 of the Stacks Project, [Tag 086A](https://stacks.math.columbia.edu/tag/086A). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 086B, a definition

[Tag 086B](https://stacks.math.columbia.edu/tag/086B) in the Stacks Project.

**`AlgebraicGeometry.Space.IsAdmissibleBlowup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowup.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowup.lean#L229).

> **Stacks 086B.** A morphism `f : X' ⟶ X` of algebraic spaces over `S` is a
> **`U`-admissible blowup**, for an open subspace `U ⊆ X`, when there is a closed subspace
> `Z ⊆ X` whose closed immersion into `X` is of finite presentation and whose points are disjoint
> from those of `U`, such that `f` exhibits `X'` as the blowup of `X` in `Z`.
>
> Being the blowup of `X` in `Z` is `AlgebraicGeometry.Space.IsBlowupAlong`, the universal
> property of Tag 085U: `f` is a terminal object of the category of algebraic spaces over `X` on
> which the inverse image of `Z` is an effective Cartier divisor.  Since terminal objects are
> unique up to unique isomorphism and the blowup of `X` in `Z` is such a terminal object, this is
> the source's "`X'` is isomorphic to the blowup of `X` in `Z`"; see the module documentation, and
> `AlgebraicGeometry.Space.IsAdmissibleBlowup.exists_iso_blowup` for that reading as a
> theorem.

```lean
abbrev IsAdmissibleBlowup (U : OpenSubspaces B S hS X.1) (f : X' ⟶ X) : Prop
```

## Tag 086C, a lemma

[Tag 086C](https://stacks.math.columbia.edu/tag/086C) in the Stacks Project.

**`AlgebraicGeometry.Space.isAdmissibleBlowup_comp_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupComposition.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupComposition.lean#L47).

> Let `S` be a scheme, let `X` be a quasi-compact and quasi-separated algebraic space over `S`
> and let `U ⊆ X` be an open subspace.  Let `b : X' ⟶ X` be a `U`-admissible blowup and let
> `c : X'' ⟶ X'` be a `U`-admissible blowup.  Then the composition `c ≫ b : X'' ⟶ X` is a
> `U`-admissible blowup.
>
> Since `b` is an isomorphism over `U`, the source regards `U` as an open subspace of `X'` as well;
> as a subspace of `X'` it is the inverse image `b⁻¹(U)`, which is how the admissibility of `c`
> is stated.  Quasi-separatedness of `X` is absolute quasi-separatedness, which needs the terminal
> scheme in the site (`hZ`).  The source also takes `U` quasi-compact; that hypothesis is not
> needed and is omitted.

```lean
theorem isAdmissibleBlowup_comp_of_isQuasiCompactSpace
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (hZ : B.Contains (⊤_ Scheme.{u})) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (U : OpenSubspaces B S hS X.1) {b : X' ⟶ X} {c : X'' ⟶ X'}
    (hb : IsAdmissibleBlowup B S hS U b)
    (hc : IsAdmissibleBlowup B S hS
      ⟨U.1.preimage b.hom, isOpenSubspace_preimage B S hS b.hom U.1 X.2 X'.2 U.2⟩ c) :
    IsAdmissibleBlowup B S hS U (c ≫ b)
```

## Tag 086D, a lemma

[Tag 086D](https://stacks.math.columbia.edu/tag/086D) in the Stacks Project.

**`AlgebraicGeometry.Space.IsBlowupAlong.exists_restrictionToOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupExtension.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupExtension.lean#L201). The attribute's comment: “unconditional: the restriction over an open subspace `V` of the blowup of `X` in `Z` is the blowup of `V` in `Z ∩ V`”.

> **The blowup of `X` in a closed subspace `Z` restricts, over an open subspace `V ⊆ X`, to
> the blowup of `V` in `Z ∩ V`.**  This is the clause "whose restriction to `V` is `V'`" of Tag
> 086D, and the one step of its proof that the universal property of Tag 085U supplies on its own.
>
> The inverse image `f⁻¹(V)` is an open subspace of `X'` and exhibits a cartesian square over
> `V ⊆ X` by Tag 083Q; the inclusion of an open subspace is étale, hence flat, so
> `AlgebraicGeometry.Space.IsBlowupAlong.of_isPullback_of_isFlat` applies.

```lean
theorem IsBlowupAlong.exists_restrictionToOpen {X X' : AlgebraicSpaces B S hS} {f : X' ⟶ X}
    (V : OpenSubspaces B S hS X.1) (Z : ClosedSubspaces B S hS X.1)
    (hf : IsBlowupAlong B S hS Z f) :
    ∃ (P : AlgebraicSpaces B S hS) (p : P ⟶ openSubspace B S hS X V) (q : P ⟶ X'),
      IsPullback p q (openSubspaceι B S hS X V) f ∧
        IsBlowupAlong B S hS (closedSubspaceRestrict B S hS X V Z) p
```

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupExtensionFromOpen.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupExtensionFromOpen.lean#L64).

> **Stacks 086D.**  Let `X` be a quasi-compact and quasi-separated algebraic space over `S`,
> let `U, V ⊆ X` be quasi-compact open subspaces and let `b : V' ⟶ V` be a `U ∩ V`-admissible
> blowup.  Then there is a `U`-admissible blowup `f : X' ⟶ X` whose restriction to `V` is `V'`,
> the restriction being recorded as a cartesian square.
>
> The extension of the centre is
> `AlgebraicGeometry.Space.exists_closedSubspace_extension_disjoint`: the centre `W ⊆ V` of `b`,
> together with the empty closed subspace on `U`, extends to a finitely presented `Z ⊆ X` whose
> points avoid those of `U` and with `Z ∩ V = W`, by the induction principle of Stacks 08GP.  The
> blowup of `X` in `Z` exists by
> `AlgebraicGeometry.Space.exists_isBlowupAlong_of_isFinitePresentation`, it is `U`-admissible,
> and by `AlgebraicGeometry.Space.IsBlowupAlong.exists_restrictionToOpen` its restriction to `V`
> is the blowup of `V` in `Z ∩ V = W`, hence isomorphic over `V` to `V'`.

```lean
theorem exists_isAdmissibleBlowup_isPullback'
    (hZ : B.Contains (⊤_ Scheme.{u})) {X V' : AlgebraicSpaces B S hS}
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (U V : OpenSubspaces B S hS X.1)
    (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    (hVqc : IsQuasiCompactSpace B S hS V.1.toFunctor)
    (b : V' ⟶ openSubspace B S hS X V)
    (hb : IsAdmissibleBlowup B S hS (openSubspaceRestrict B S hS X V U) b) :
    ∃ (X' : AlgebraicSpaces B S hS) (f : X' ⟶ X), IsAdmissibleBlowup B S hS U f ∧
      ∃ e : V' ⟶ X', IsPullback b e (openSubspaceι B S hS X V) f
```

## Tag 086E, a lemma

[Tag 086E](https://stacks.math.columbia.edu/tag/086E) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_factoring`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupDominating.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupDominating.lean#L425). The attribute's comment: “clause (a): a U-admissible blowup factoring through each member of a finite family of U-admissible blowups, with no assumed inputs beyond the Stacks 085Q construction data for X -- a presentation P, the HasSheafify universe choice, and the three B.Contains side conditions on the relative Projs, asked for EVERY closed subspace of X because the centre is the sum of the given centres and is built inside the proof, so it cannot be named in advance -- none of which occurs in the conclusion”.

> **Stacks 086E, clause (a).**  Let `S` be a scheme, let `X` be a quasi-compact and
> quasi-separated algebraic space over `S`, let `U ⊆ X` be a quasi-compact open subspace and let
> `b i : X i ⟶ X`, `i : ι` with `ι` finite, be `U`-admissible blowups.  There is a `U`-admissible
> blowup `c : X' ⟶ X` which factors as `X' ⟶ X i ⟶ X` for every `i`.
>
> Take for `X'` the blowup of `X` in the sum `Z i₀ + Z i₁ + ⋯` of the centres of the given
> blowups, Stacks 083U; the sum of finitely many finitely presented centres disjoint from `U` is
> again finitely presented (`AlgebraicGeometry.Space.isFinitePresentation_ι_sumClosedSubspaces`)
> and disjoint from `U` (`AlgebraicGeometry.Space.subspacePointSet_sumClosedSubspaces`), so `c` is
> `U`-admissible.  The inverse image of the sum along `c` is an effective Cartier divisor, hence so
> is the inverse image of each summand `Z i` by Stacks 083W, and the universal property of `b i`,
> Stacks 085U, then produces the factorisation through `b i`.  For the empty family the identity of
> `X` is a `U`-admissible blowup, being the blowup in the empty closed subspace.
>
> The hypotheses beyond the source's are the construction data of Stacks 085Q for the blowup of
> `X`: an étale presentation `P` of `X`, the universe choice `HasSheafify` for the quotient
> presheaf, and the three `B.Contains` smallness side conditions on the relative `Proj`s, asked for
> every closed subspace of `X` since the centre is built inside the proof.  None of these says
> anything about blowups; they are exactly what
> `AlgebraicGeometry.Space.isBlowupAlong_blowUpAlongHom'` takes.

```lean
theorem exists_isAdmissibleBlowup_factoring
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (hZtop : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (_hXqc : IsQuasiCompactSpace B S hS X.1)
    (_hXqs : IsAbsolutelyQuasiSeparated B S hS hZtop X.1)
    (U : OpenSubspaces B S hS X.1)
    (_hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    {ι : Type v} [Finite ι] (Xi : ι → AlgebraicSpaces B S hS) (b : ∀ i, Xi i ⟶ X)
    (hb : ∀ i, IsAdmissibleBlowup B S hS U (b i))
    (P : Presentation B S hS X.obj X.property)
    (hc : ∀ K : ClosedSubspaces B S hS X.obj,
      B.Contains (reesChartSituation (centreIdeal K)
          (isCartesianOnAffineCharts_centreIdeal K) P).relativeProj ∧
        B.Contains (reesRelationSituation (centreIdeal K)
          (isCartesianOnAffineCharts_centreIdeal K) P).relativeProj ∧
          B.Contains (reesDoubleSituation (centreIdeal K)
            (isCartesianOnAffineCharts_centreIdeal K) P).relativeProj) :
    ∃ (X' : AlgebraicSpaces B S hS) (c : X' ⟶ X), IsAdmissibleBlowup B S hS U c ∧
      ∃ g : ∀ i, X' ⟶ Xi i, ∀ i, g i ≫ b i = c
```

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_factoring_isAdmissibleBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupDominating.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupDominating.lean#L497). The attribute's comment: “clause (b): the factor morphisms of the dominating blowup are themselves admissible blowups, with no assumed inputs beyond the Stacks 085Q construction data for X and for the X i -- presentations P and Pi, the HasSheafify universe choice, and the B.Contains side conditions on the relative Projs, asked for EVERY closed subspace of X and of each X i because the centres are built inside the proof and cannot be named in advance -- none of which occurs in the conclusion”.

> **Stacks 086E, clause (b).**  In the situation of clause (a) the dominating `U`-admissible
> blowup `c : X' ⟶ X` can be chosen so that, in addition, each factor morphism `g i : X' ⟶ X i` is
> itself a `b i⁻¹(U)`-admissible blowup.
>
> Writing the centre of `c` as `Z i + J i` — every member of the family is a summand of the sum,
> `AlgebraicGeometry.Space.exists_eq_sumClosedSubspaces_of_mem` — the blowup `c i` of `X i` in the
> inverse image of `J i` exists by Stacks 085Q and 085U, and Stacks 085Y identifies the composite
> `c i ≫ b i` with the blowup of `X` in `Z i + J i`, the input it needs being Stacks 085X for `c i`
> and the exceptional divisor of `b i`
> (`AlgebraicGeometry.Space.isPullbackDefined_of_isBlowupAlong`).  Blowups in a fixed centre are
> isomorphic over the base, so `X'` is isomorphic over `X` to the source of `c i ≫ b i`, and the
> factor morphism transported along that isomorphism is again the blowup of `X i` in the inverse
> image of `J i`.  That centre is finitely presented (a base change of `J i`) and disjoint from
> `b i⁻¹(U)` (the inverse image of a disjointness), so the factor morphism is
> `b i⁻¹(U)`-admissible.  For the empty family the identity of `X` is the blowup in the empty
> closed subspace and there is nothing to factor.
>
> The hypotheses beyond the source's are the construction data of Stacks 085Q, now also for each
> `X i` because the second blowup of the tower is formed there: étale presentations `P` of `X` and
> `Pi i` of `X i`, the universe choice `HasSheafify`, and the `B.Contains` smallness side
> conditions on the relative `Proj`s.  None of them occurs in the conclusion, and none says
> anything about blowups.

```lean
theorem exists_isAdmissibleBlowup_factoring_isAdmissibleBlowup
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (hZtop : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (_hXqc : IsQuasiCompactSpace B S hS X.1)
    (_hXqs : IsAbsolutelyQuasiSeparated B S hS hZtop X.1)
    (U : OpenSubspaces B S hS X.1)
    (_hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    {ι : Type v} [Finite ι] (Xi : ι → AlgebraicSpaces B S hS) (b : ∀ i, Xi i ⟶ X)
    (hb : ∀ i, IsAdmissibleBlowup B S hS U (b i))
    (P : Presentation B S hS X.obj X.property)
    (hc : ∀ K : ClosedSubspaces B S hS X.obj,
      B.Contains (reesChartSituation (centreIdeal K)
          (isCartesianOnAffineCharts_centreIdeal K) P).relativeProj ∧
        B.Contains (reesRelationSituation (centreIdeal K)
          (isCartesianOnAffineCharts_centreIdeal K) P).relativeProj ∧
          B.Contains (reesDoubleSituation (centreIdeal K)
            (isCartesianOnAffineCharts_centreIdeal K) P).relativeProj)
    (Pi : ∀ i, Presentation B S hS (Xi i).obj (Xi i).property)
    (hci : ∀ (i : ι) (K : ClosedSubspaces B S hS (Xi i).obj),
      B.Contains (reesChartSituation (centreIdeal K)
          (isCartesianOnAffineCharts_centreIdeal K) (Pi i)).relativeProj ∧
        B.Contains (reesRelationSituation (centreIdeal K)
          (isCartesianOnAffineCharts_centreIdeal K) (Pi i)).relativeProj ∧
          B.Contains (reesDoubleSituation (centreIdeal K)
            (isCartesianOnAffineCharts_centreIdeal K) (Pi i)).relativeProj) :
    ∃ (X' : AlgebraicSpaces B S hS) (c : X' ⟶ X), IsAdmissibleBlowup B S hS U c ∧
      ∃ g : ∀ i, X' ⟶ Xi i, (∀ i, g i ≫ b i = c) ∧
        ∀ i, IsAdmissibleBlowup B S hS
          ⟨U.1.preimage (b i).hom,
            isOpenSubspace_preimage B S hS (b i).hom U.1 X.2 (Xi i).2 U.2⟩ (g i)
```

## Tag 086F, a lemma

[Tag 086F](https://stacks.math.columbia.edu/tag/086F) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_disjoint_openSubspace_decomposition'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupSeparationQuasiCompact.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdmissibleBlowupSeparationQuasiCompact.lean#L117).

> **Stacks 086F.**  Let `S` be a scheme, let `X` be a quasi-compact and quasi-separated
> algebraic space over `S` and let `U, V ⊆ X` be quasi-compact open subspaces with disjoint sets
> of points.  Then there is a `U ∪ V`-admissible blowup `b : X' ⟶ X` such that `X'` is the
> disjoint union of two open subspaces `X' = X'₁ ⊔ X'₂` with `b⁻¹(U) ⊆ X'₁` and
> `b⁻¹(V) ⊆ X'₂`.
>
> "`X'` is the disjoint union of `X'₁` and `X'₂`" is recorded as follows: the two
> are open and closed subspaces with complementary sets of points, whose join sheafifies to `X'`
> and whose meet is the sheafification of the bottom subfunctor.
>
> Two finitely presented closed subspaces `Z₁, Z₂` with `|Z₁| ∩ |U| = ∅`, `|Z₂| ∩ |V| = ∅` and
> `|Z₁| ∪ |Z₂| = |X|` are produced by two applications of
> `AlgebraicGeometry.Space.exists_closedSubspace_disjoint_superset`, the second to `V` and the
> quasi-compact open complement of `Z₁`; the blowup in `Z₁ ∩ Z₂` is then the one sought, by
> `exists_isAdmissibleBlowup_disjoint_openSubspace_decomposition_of_closedSubspaces`.

```lean
theorem exists_isAdmissibleBlowup_disjoint_openSubspace_decomposition'
    (hZ : B.Contains (⊤_ Scheme.{u})) {X : AlgebraicSpaces B S hS}
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (U V : OpenSubspaces B S hS X.1)
    (hUqc : IsQuasiCompactSpace B S hS U.1.toFunctor)
    (hVqc : IsQuasiCompactSpace B S hS V.1.toFunctor)
    (hUV : Disjoint (subspacePointSet B S hS X.1 U.1) (subspacePointSet B S hS X.1 V.1)) :
    ∃ (X' : AlgebraicSpaces B S hS) (b : X' ⟶ X) (X'₁ X'₂ : OpenSubspaces B S hS X'.1),
      IsAdmissibleBlowup B S hS (openSubspaceUnion B S hS X U V) b ∧
        IsClosedSubspace B S hS X'₁.1 ∧ IsClosedSubspace B S hS X'₂.1 ∧
          Disjoint (subspacePointSet B S hS X'.1 X'₁.1)
            (subspacePointSet B S hS X'.1 X'₂.1) ∧
            subspacePointSet B S hS X'.1 X'₁.1 ∪ subspacePointSet B S hS X'.1 X'₂.1
                = Set.univ ∧
              (X'₁.1 ⊔ X'₂.1).sheafify (BigFppfOver.topology B S hS) = ⊤ ∧
                X'₁.1 ⊓ X'₂.1
                    = (⊥ : Subfunctor X'.1).sheafify (BigFppfOver.topology B S hS) ∧
                  U.1.preimage b.hom ≤ X'₁.1 ∧ V.1.preimage b.hom ≤ X'₂.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.19, Tag 086A](https://stacks.math.columbia.edu/tag/086A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
