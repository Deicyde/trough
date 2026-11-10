---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.exists_schemeQuotient, AlgebraicGeometry.Space.isRepresentable_quotientSheaf_of_isInvariantOpen_isAffineOpen_cover, AlgebraicGeometry.Space.exists_quotientMap_isRepresented_of_isInvariantOpen_isAffineOpen_cover, AlgebraicGeometry.Space.exists_quotientMap_isRepresented_of_affineOrbits, AlgebraicGeometry.Space.nonempty_finiteFlatQuotient_of_affineOrbits_of_bigFppfSite, AlgebraicGeometry.Space.nonempty_finiteFlatQuotient_of_affineOrbits, AlgebraicGeometry.nonempty_finiteFlatQuotient_actionGroupoid_of_geometry, AlgebraicGeometry.isFppfTorsor_quotientMap
statement: formalized
proof: formalized
---

# 66.14 Obtaining a scheme

Section 66.14 of the Stacks Project, [Tag 07S5](https://stacks.math.columbia.edu/tag/07S5). 3 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07S6, a proposition

[Tag 07S6](https://stacks.math.columbia.edu/tag/07S6) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_schemeQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/FppfQuotient.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/FppfQuotient.lean#L363). References: SGA 3 V (4.1), “(iv)”.

> **Stacks 07S6.** Let `(U, R, s, t, c)` be a groupoid scheme over `S` with `s` and `t` finite
> locally free, with `(t, s)` an equivalence relation, and such that every nonempty closed subset
> of `U` contains a point whose `R`-equivalence class lies in an affine open.  Then there is a
> scheme `M` over `S`, no larger than `U`, and a finite locally free surjection `p : U ⟶ M`,
> whose kernel pair is `(t, s)` and which represents the fppf quotient sheaf `U/R`.
>
> The invariant affine opens cover `U` (Stacks 03JE), the quotient of the restriction of the
> groupoid to each of them is affine (Stacks 03BM) and is an open subspace of `U/R`
> (Stacks 02WU), and those open subspaces jointly cover `U/R` because `U` covers it; glueing
> them (Stacks 01JJ) gives `M`.  Finite local freeness, surjectivity and the size bound transfer
> from the charts to `p` because they are local on the target, and the kernel-pair square is the
> identification of `R` with the kernel pair of the projection of `U` onto `U/R`.

```lean
theorem exists_schemeQuotient (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)] (G : GroupoidScheme S)
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source] (hU : B.Contains G.objects.left)
    (h3 : HasAffineOrbitInEveryClosed G) :
    ∃ (M : Over S) (p : G.objects ⟶ M)
      (hp : (groupoidPreRelation G).target ≫ p = (groupoidPreRelation G).source ≫ p)
      (hM : Presheaf.IsSheaf (BigFppfOver.topology B S hS)
        (points (Over.post B.inclusion) M)),
      M.left.size ≤ G.objects.left.size ∧ IsFiniteLocallyFree p.left ∧ Surjective p.left ∧
        IsPullback G.target G.source p p ∧
        IsIso (quotientSheafToPoints (BigFppfOver.topology B S hS) (Over.post B.inclusion)
          (groupoidPreRelation G) p hp hM)
```

**`AlgebraicGeometry.Space.isRepresentable_quotientSheaf_of_isInvariantOpen_isAffineOpen_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean#L229). The attribute's comment: “representability of the quotient sheaf”. References: SGA 3 V (4.1), “(iv), special case”; SGA 3 V (7.1), “(iv), special case”.

> **The fppf quotient sheaf of a finite locally free groupoid covered by invariant affine opens
> is representable.** For a groupoid scheme over `S` with finite locally free source and target whose
> pre-relation is an equivalence relation, and whose object scheme is covered by `R`-invariant affine
> opens indexed by a type below the site's cutoff, the quotient sheaf `U/R` is representable on the
> big fppf site of `S`.

```lean
theorem isRepresentable_quotientSheaf_of_isInvariantOpen_isAffineOpen_cover {S : Scheme.{u}}
    (G : GroupoidScheme S) [IsFiniteLocallyFree G.source.left]
    [IsFiniteLocallyFree G.target.left] [IsEquivalenceRelation G.target G.source]
    (B : BigFppfSite.{u}) (hS : B.Contains S) (hU : B.Contains G.objects.left)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    {ι : Type u} (hι : #ι < B.cutoff) (V : ι → G.objects.left.Opens)
    (hVinv : ∀ i, IsInvariantOpen G (V i)) (hVaff : ∀ i, IsAffineOpen (V i))
    (hcov : ⨆ i, V i = ⊤) :
    let F : BigFppfOver B S hS ⥤ Over S := Over.post B.inclusion
    let J := BigFppfOver.topology B S hS
    (quotientSheaf J F (groupoidPreRelation G)).obj.IsRepresentable
```

**`AlgebraicGeometry.Space.exists_quotientMap_isRepresented_of_isInvariantOpen_isAffineOpen_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean#L346). The attribute's comment: “the quotient scheme and the three conclusion clauses, on a given site”. References: SGA 3 V (4.1), “invariant affine cover”.

> **The quotient scheme and the quotient morphism, on a given big fppf site.** Under the
> hypotheses of
> `AlgebraicGeometry.Space.isRepresentable_quotientSheaf_of_isInvariantOpen_isAffineOpen_cover` there
> are a scheme `M` over `S` belonging to the big fppf site and a morphism `f : U ⟶ M` of `S`-schemes
> which is finite locally free and surjective, whose kernel pair is the given pair `(t, s)` — that is
> `R = U ×_M U` — and under which the restricted functor of points of `M` is a sheaf representing the
> quotient sheaf `U/R` compatibly with `f`.

```lean
theorem exists_quotientMap_isRepresented_of_isInvariantOpen_isAffineOpen_cover
    {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source]
    (B : BigFppfSite.{u}) (hS : B.Contains S) (hU : B.Contains G.objects.left)
    (hR : B.Contains G.arrows.left)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    {ι : Type u} (hι : #ι < B.cutoff) (V : ι → G.objects.left.Opens)
    (hVinv : ∀ i, IsInvariantOpen G (V i)) (hVaff : ∀ i, IsAffineOpen (V i))
    (hcov : ⨆ i, V i = ⊤) :
    let F : BigFppfOver B S hS ⥤ Over S := Over.post B.inclusion
    let J := BigFppfOver.topology B S hS
    ∃ (M : Over S) (f : G.objects ⟶ M), B.Contains M.left ∧
      IsFiniteLocallyFree f.left ∧ Surjective f.left ∧
      IsPullback G.target G.source f f ∧
      ∃ hM : Presheaf.IsSheaf J (Stacks.Groupoids.points F M),
        ∃ q : quotientSheaf J F (groupoidPreRelation G) ⟶
            (⟨Stacks.Groupoids.points F M, hM⟩ : Sheaf J (Type u)),
          IsIso q ∧ toQuotientSheaf J F (groupoidPreRelation G) ≫ q.hom =
            F.op.whiskerLeft (yoneda.map f)
```

**`AlgebraicGeometry.Space.exists_quotientMap_isRepresented_of_affineOrbits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean#L514). The attribute's comment: “the three conclusion clauses from the affine-orbit condition, on a given site”. References: SGA 3 V (4.1), “(iv)”.

> **The quotient scheme and the quotient morphism for a groupoid with affine orbits, on a given
> big fppf site.** The same conclusion as
> `AlgebraicGeometry.Space.exists_quotientMap_isRepresented_of_isInvariantOpen_isAffineOpen_cover`
> with the covering by invariant affine opens replaced by the condition that every nonempty closed
> subset of `U` contains a point whose `R`-equivalence class `t(s⁻¹({u}))` lies in an affine open of
> `U`.

```lean
theorem exists_quotientMap_isRepresented_of_affineOrbits {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source]
    (B : BigFppfSite.{u}) (hS : B.Contains S) (hU : B.Contains G.objects.left)
    (hR : B.Contains G.arrows.left)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (horbit : ∀ Z : Set G.objects.left, IsClosed Z → Z.Nonempty →
      ∃ u ∈ Z, ∃ W : G.objects.left.Opens, IsAffineOpen W ∧
        G.target.left.base '' (G.source.left.base ⁻¹' {u}) ⊆ (W : Set G.objects.left)) :
    let F : BigFppfOver B S hS ⥤ Over S := Over.post B.inclusion
    let J := BigFppfOver.topology B S hS
    ∃ (M : Over S) (f : G.objects ⟶ M), B.Contains M.left ∧
      IsFiniteLocallyFree f.left ∧ Surjective f.left ∧
      IsPullback G.target G.source f f ∧
      ∃ hM : Presheaf.IsSheaf J (Stacks.Groupoids.points F M),
        ∃ q : quotientSheaf J F (groupoidPreRelation G) ⟶
            (⟨Stacks.Groupoids.points F M, hM⟩ : Sheaf J (Type u)),
          IsIso q ∧ toQuotientSheaf J F (groupoidPreRelation G) ≫ q.hom =
            F.op.whiskerLeft (yoneda.map f)
```

**`AlgebraicGeometry.Space.nonempty_finiteFlatQuotient_of_affineOrbits_of_bigFppfSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean#L551). The attribute's comment: “the finite flat quotient, given a big fppf site containing the groupoid”. References: SGA 3 V (4.1), “more general”.

> **A finite flat quotient of a groupoid with affine orbits, given a big fppf site.** Let
> `(U, R, s, t, c)` be a groupoid scheme over `S` with `s` and `t` finite locally free and with
> `(t, s)` an equivalence relation, such that every nonempty closed subset of `U` contains a point
> whose `R`-equivalence class lies in an affine open, and suppose given a big fppf site of `S`
> containing `S`, `U` and `R`. Then the groupoid has a finite flat quotient in the sense of
> `Stacks.Groupoids.FiniteFlatQuotient`.

```lean
theorem nonempty_finiteFlatQuotient_of_affineOrbits_of_bigFppfSite {S : Scheme.{u}}
    (G : GroupoidScheme S)
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source]
    (B : BigFppfSite.{u}) (hS : B.Contains S) (hU : B.Contains G.objects.left)
    (hR : B.Contains G.arrows.left)
    (horbit : ∀ Z : Set G.objects.left, IsClosed Z → Z.Nonempty →
      ∃ u ∈ Z, ∃ W : G.objects.left.Opens, IsAffineOpen W ∧
        G.target.left.base '' (G.source.left.base ⁻¹' {u}) ⊆ (W : Set G.objects.left)) :
    Nonempty (FiniteFlatQuotient G)
```

**`AlgebraicGeometry.Space.nonempty_finiteFlatQuotient_of_affineOrbits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientCharts.lean#L581). References: SGA 3 V (4.1), “more general”; SGA 3 V (7.1), “special case”.

> **Finite flat quotients of groupoids with affine orbits.** Let `(U, R, s, t, c)` be a groupoid
> scheme over a scheme `S` such that
>
> 1. `s, t : R ⟶ U` are finite locally free,
> 2. `j = (t, s)` is an equivalence relation, and
> 3. every nonempty closed subset `Z` of `U` contains a point `u` whose `R`-equivalence class
>    `t(s⁻¹({u}))` is contained in an affine open of `U`.
>
> Then there is a finite locally free morphism `U ⟶ M` of schemes over `S` with `R = U ×_M U` and
> with `M` representing the quotient sheaf `U/R` in the fppf topology — that is, the groupoid has a
> finite flat quotient in the sense of `Stacks.Groupoids.FiniteFlatQuotient`, which also records that
> `U ⟶ M` is surjective.

```lean
theorem nonempty_finiteFlatQuotient_of_affineOrbits {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source]
    (horbit : ∀ Z : Set G.objects.left, IsClosed Z → Z.Nonempty →
      ∃ u ∈ Z, ∃ W : G.objects.left.Opens, IsAffineOpen W ∧
        G.target.left.base '' (G.source.left.base ⁻¹' {u}) ⊆ (W : Set G.objects.left)) :
    Nonempty (FiniteFlatQuotient G)
```

## Tag 07S7, a lemma

[Tag 07S7](https://stacks.math.columbia.edu/tag/07S7) in the Stacks Project.

**`AlgebraicGeometry.nonempty_finiteFlatQuotient_actionGroupoid_of_geometry`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FreeGroupSchemeQuotient.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FreeGroupSchemeQuotient.lean#L399). The attribute's comment: “the quotient sheaf is a scheme; all seven alternatives of condition (3)”. References: SGA 3 IX (2.3), “2.3(a)”; SGA 3 V (4.1), “special case”; SGA 3 V (9.0), “partial”; SGA 3 VIB (9.3), “Case 2° of Remark 9.3 b)”; SGA 3 XVI (1.1), “more general”; SGA 3 XXV (4.2), “special case”.

> Let `S` be a scheme, `G ⟶ S` a group scheme, `X ⟶ S` a
> morphism of schemes and `a : G ×_S X ⟶ X` an action. Assume that `G ⟶ S` is finite locally
> free, that the action is free, and that `X ⟶ S` is affine, or quasi-affine, or projective, or
> quasi-projective, or `X` admits an immersion into an affine scheme, or an immersion into
> `Proj A` for a graded ring `A`, or `G ⟶ S` is radicial. Then the fppf quotient sheaf `X/G` is a
> scheme: the action groupoid has a finite flat quotient, so there is a scheme `M` over `S`
> representing `X/G` on every big fppf site, with `X ⟶ M` surjective and finite locally free and
> with kernel pair `G ×_S X`.

```lean
theorem nonempty_finiteFlatQuotient_actionGroupoid_of_geometry [IsFiniteLocallyFree G.hom]
    (hfree : IsFreeAction G X)
    (hgeom : IsAffineHom X.hom ∨ IsQuasiAffineHom X.hom ∨ IsProjective X.hom ∨
      IsQuasiProjective X.hom ∨ HasImmersionToAffine X.left ∨ HasImmersionToProj X.left ∨
      UniversallyInjective G.hom) :
    Nonempty (FiniteFlatQuotient (actionGroupoid (Over.mk (𝟙 S)) G X))
```

**`AlgebraicGeometry.isFppfTorsor_quotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FreeGroupSchemeQuotient.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FreeGroupSchemeQuotient.lean#L422). The attribute's comment: “the fppf torsor clause: shear isomorphism and fppf-local sections”.

> For a finite flat quotient `M = X/G` of the action groupoid, the morphism
> `G ×_S X ⟶ X ×_M X` sending `(g, x)` to `(g · x, x)` is an isomorphism, and `X ⟶ M` is itself an
> fppf covering of `M` over which `X ⟶ M` has a section, namely the diagonal. These are the two
> conditions for `X ⟶ X/G` to be an fppf `G`-torsor.

```lean
theorem isFppfTorsor_quotientMap [IsFiniteLocallyFree G.hom]
    (Q : FiniteFlatQuotient (actionGroupoid (Over.mk (𝟙 S)) G X)) :
    (∃ e : (G ⊗ X).left ≅ pullback Q.quotientMap.left Q.quotientMap.left,
        e.hom ≫ pullback.fst Q.quotientMap.left Q.quotientMap.left = (γ[G, X]).left ∧
          e.hom ≫ pullback.snd Q.quotientMap.left Q.quotientMap.left = (snd G X).left) ∧
      Presieve.singleton Q.quotientMap.left ∈ Scheme.fppfPrecoverage Q.space.left ∧
      ∃ s : X.left ⟶ pullback Q.quotientMap.left Q.quotientMap.left,
        s ≫ pullback.fst Q.quotientMap.left Q.quotientMap.left = 𝟙 X.left
```

## Tag 0BBM, a lemma

[Tag 0BBM](https://stacks.math.columbia.edu/tag/0BBM) in the Stacks Project.

**`Stacks.Groupoids.FiniteFlatQuotient.quasiSeparated_space_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean#L84). The attribute's comment: “part (1), quasi-separated over the base”.

> If the object scheme of the groupoid is quasi-separated over `S`, then so is the quotient
> scheme.

```lean
theorem quasiSeparated_space_hom (Q : FiniteFlatQuotient G)
    (hU : QuasiSeparated G.objects.hom) : QuasiSeparated Q.space.hom
```

**`Stacks.Groupoids.FiniteFlatQuotient.quasiSeparatedSpace_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean#L91). The attribute's comment: “part (2), quasi-separated”.

> If the object scheme of the groupoid is quasi-separated, then so is the quotient scheme.

```lean
theorem quasiSeparatedSpace_space (Q : FiniteFlatQuotient G)
    (hU : QuasiSeparatedSpace G.objects.left) : QuasiSeparatedSpace Q.space.left
```

**`Stacks.Groupoids.FiniteFlatQuotient.isSeparated_space_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean#L98). The attribute's comment: “part (3), separated over the base”. References: SGA 1 V (1.6), “partial”.

> If the object scheme of the groupoid is separated over `S`, then so is the quotient scheme.

```lean
theorem isSeparated_space_hom (Q : FiniteFlatQuotient G)
    (hU : IsSeparated G.objects.hom) : IsSeparated Q.space.hom
```

**`Stacks.Groupoids.FiniteFlatQuotient.isSeparated_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFlatQuotientSeparated.lean#L105). The attribute's comment: “part (4), separated”. References: SGA 1 V (1.6), “partial”.

> If the object scheme of the groupoid is separated, then so is the quotient scheme.

```lean
theorem isSeparated_space (Q : FiniteFlatQuotient G)
    (hU : Scheme.IsSeparated G.objects.left) : Scheme.IsSeparated Q.space.left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.14, Tag 07S5](https://stacks.math.columbia.edu/tag/07S5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
