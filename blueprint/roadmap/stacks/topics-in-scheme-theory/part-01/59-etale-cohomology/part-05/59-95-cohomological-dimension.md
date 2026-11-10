---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.etaleCohomologicalDimension, AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_iSup_of_isLimit, AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_iSup_of_isLimit_of_isDirected, AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_one_add, AlgebraicGeometry.Scheme.etaleCohomologicalDimension_spec_le_add_trdeg, AlgebraicGeometry.exists_strictHenselization_map_of_finiteType, AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_add_of_topologicalKrullDim_le, AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_topologicalKrullDim_add
statement: formalized
proof: formalized
---

# 59.95 Cohomological dimension

Section 59.95 of the Stacks Project, [Tag 0F0P](https://stacks.math.columbia.edu/tag/0F0P). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F0Q, a definition

[Tag 0F0Q](https://stacks.math.columbia.edu/tag/0F0Q) in the Stacks Project.

**`AlgebraicGeometry.Scheme.etaleCohomologicalDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension.lean#L103).

> **Stacks Project, Tag 0F0Q.** The least degree above which the étale cohomology
> of every torsion abelian sheaf on a quasi-compact, quasi-separated scheme vanishes.

```lean
public def etaleCohomologicalDimension (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X]
    [HasSheafify X.smallEtaleTopology AddCommGrpCat.{u + 1}]
    [HasExt.{u + 1} (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})] : ℕ∞
```

## Tag 0F0R, a lemma

[Tag 0F0R](https://stacks.math.columbia.edu/tag/0F0R) in the Stacks Project.

**`AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_iSup_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimensionLimits.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimensionLimits.lean#L199). The attribute's comment: “the hypothesis `h09YQ` of this declaration is the transport of vanishing that Tags 0EYN and 09YQ supply: a degree in which the étale cohomology of every direct image `f_{i,*}𝓕` vanishes is a degree in which that of `𝓕` vanishes”.

> **Stacks Project, Tag 0F0R** (Étale Cohomology, Lemma 59.95.2). Let `X = lim X_i` be a
> directed limit of a system of quasi-compact and quasi-separated schemes with affine transition
> morphisms. Then `cd(X) ≤ max cd(X_i)`.
>
> The directed system is the cofiltered diagram `D` with affine maps and quasi-compact,
> quasi-separated values, the limit is the cone `c` with `hc : IsLimit c`, the projections
> `f_i : X ⟶ X_i` are `c.π.app i`, and the maximum over the index set is the supremum in the
> complete lattice `ℕ∞`, which is attained because a cofiltered category is nonempty.
>
> `h09YQ` is the consequence of [Stacks, Tag 0EYN] and [Stacks, Tag 09YQ] that the proof uses:
> since `𝓕 = colim f_i^{-1} f_{i,*}𝓕` and hence
> `H^q_étale(X, 𝓕) = colim H^q_étale(X_i, f_{i,*}𝓕)`, a degree in which the cohomology of every
> `f_{i,*}𝓕` vanishes is a degree in which the cohomology of `𝓕` vanishes.
>
> The proof is then the source's: a degree above `⨆ i, cd(X_i)` is above every `cd(X_i)`, so each
> `H^q_étale(X_i, f_{i,*}𝓕)` vanishes by the defining property of `cd(X_i)` applied to the sheaf
> `f_{i,*}𝓕`, which is torsion by [Stacks, Tag 0DDD] part (1) in degree zero —
> `Stacks.EtaleCohomology.torsionSheafProperty_rightDerived_smallEtaleDirectImageAb` read through
> `CategoryTheory.Functor.rightDerivedZeroIsoSelf`, the projection `f_i` being affine and hence
> quasi-compact and quasi-separated — and `h09YQ` transports the vanishing to `X`.

```lean
public theorem etaleCohomologicalDimension_le_iSup_of_isLimit
    [CompactSpace c.pt] [QuasiSeparatedSpace c.pt]
    [HasSheafify c.pt.smallEtaleTopology AddCommGrpCat.{u + 1}]
    [HasExt.{u + 1} (Sheaf c.pt.smallEtaleTopology AddCommGrpCat.{u + 1})]
    [∀ i : I, HasSheafify (D.obj i).smallEtaleTopology AddCommGrpCat.{u + 1}]
    [∀ i : I, HasExt.{u + 1} (Sheaf (D.obj i).smallEtaleTopology AddCommGrpCat.{u + 1})]
    (hc : IsLimit c)
    (h09YQ : ∀ F : Sheaf c.pt.smallEtaleTopology AddCommGrpCat.{u + 1},
      Stacks.Torsion.torsionSheafProperty c.pt.smallEtaleTopology F →
        ∀ q : ℕ, (∀ i : I, Subsingleton (Sheaf.H.{u + 1, u + 1}
            ((Stacks.EtaleCohomology.smallEtalePushforward
              (c.π.app i) AddCommGrpCat.{u + 1}).obj F) q)) →
          Subsingleton (Sheaf.H.{u + 1, u + 1} F q)) :
    etaleCohomologicalDimension c.pt ≤
      ⨆ i : I, etaleCohomologicalDimension (D.obj i)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_iSup_of_isLimit_of_isDirected`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/DirectedLimit.lean#L110), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimensionDirectedLimits.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimensionDirectedLimits.lean#L29) (StacksFrontier): “cd(lim X_i) ≤ max cd(X_i) for a directed limit of qcqs schemes with affine transition morphisms”.

## Tag 0F0S, a lemma

[Tag 0F0S](https://stacks.math.columbia.edu/tag/0F0S) in the Stacks Project.

**`AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_one_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineCurve.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineCurve.lean#L237). The attribute's comment: “for `X` of dimension at most one, which contains the source's dimension one”. References: SGA 4 X (5.2), “special case”; SGA 4 XIV (3.2), “special case”; SGA 4½ Arcata (4.6.4), “special case”; SGA 5 I (1.5.2), “special case”.

> **Stacks Project, Tag 0F0S.** Let `K` be a field and `X` an affine scheme of finite type over
> `K` of dimension at most one. Then `cd(X) ≤ 1 + cd(K)`.
>
> The source's statement is for `X` of dimension one; dimension at most one is no harder, and
> contains it.
>
> The proof is the source's. Let `𝓕` be a torsion sheaf on `X_étale`. By the Leray spectral
> sequence for `g : X ⟶ Spec K` (`Stacks.EtaleCohomology.LerayVanishing`) it suffices that
> `H^p(Spec K, R^qg_*𝓕) = 0` for `p + q > 1 + cd(K)`. For `q ≤ 1` this is the definition of
> `cd(K)`, `R^qg_*𝓕` being torsion (Stacks 0DDD). For `q ≥ 2` the sheaf `R^qg_*𝓕` vanishes: its
> stalk at a geometric point is the cohomology of the base change of `X` to the strict
> henselization, which is a separable closure `Ω` of `K` (Stacks 03Q9), and `X_Ω` is an affine curve
> over a separably closed field, of cohomological dimension at most one by
> `etaleCohomologicalDimension_le_one_of_isSepClosed`.

```lean
public theorem etaleCohomologicalDimension_le_one_add
    {K : Type u} [Field K] {X : Scheme.{u}} [IsAffine X] (g : X ⟶ Spec (.of K))
    [LocallyOfFiniteType g] (hX : topologicalKrullDim X ≤ 1) :
    etaleCohomologicalDimension X ≤ 1 + etaleCohomologicalDimension (Spec (.of K))
```

## Tag 0F0T, a lemma

[Tag 0F0T](https://stacks.math.columbia.edu/tag/0F0T) in the Stacks Project.

**`AlgebraicGeometry.Scheme.etaleCohomologicalDimension_spec_le_add_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/FieldExtension.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/FieldExtension.lean#L224).

> **Stacks Project, Tag 0F0T** (Étale Cohomology, Lemma 59.95.4). Let `L/K` be a field
> extension. Then `cd(L) ≤ cd(K) + trdeg_K(L)`.
>
> The cohomological dimension of a field is that of its spectrum (Tag 0F0Q: "if `X = Spec(A)` we
> sometimes call this the cohomological dimension of `A`"), `etaleCohomologicalDimension`, valued in
> `ℕ∞`; the transcendence degree is the cardinal `Algebra.trdeg K L` read in `ℕ∞` by
> `Cardinal.toENat`, so that an infinite transcendence degree is `⊤` and the inequality is then
> clear, as in the source.
>
> The proof is the source's: a tower of transcendence degree one steps
> (`etaleCohomologicalDimension_spec_le_add_trdeg_of_le_one_add`, which also treats the algebraic
> case `r = 0`) reduces to `trdeg_K(L) ≤ 1`, which is
> `etaleCohomologicalDimension_spec_le_one_add_of_trdeg_le_one` (Tags 0F0R and 0F0S).

```lean
theorem etaleCohomologicalDimension_spec_le_add_trdeg
    (K L : Type u) [Field K] [Field L] [Algebra K L] :
    etaleCohomologicalDimension (Spec (.of L)) ≤
      etaleCohomologicalDimension (Spec (.of K)) + (Algebra.trdeg K L).toENat
```

## Tag 0F0U, a lemma

[Tag 0F0U](https://stacks.math.columbia.edu/tag/0F0U) in the Stacks Project.

**`AlgebraicGeometry.exists_strictHenselization_map_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/StrictHenselizationOverField.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/StrictHenselizationOverField.lean#L563).

> **Stacks Project, Tag 0F0U.** At a point `x` of a finite-type `K`-scheme, a strict
> henselization of the local ring admits a map from a separable closure of a rational function
> field in `trdeg K κ(x)` variables. The induced residue-field extension is purely inseparable,
> and the strict henselization is a filtered colimit of finite-type algebras of dimension at most
> `dimₓ(X) - trdeg K κ(x)`.

```lean
theorem exists_strictHenselization_map_of_finiteType
    (K : Type u) [Field K] {X : Scheme.{u}} (f : X ⟶ Spec (.of K))
    [LocallyOfFiniteType f] [QuasiCompact f] (x : X) :
    letI := (((Scheme.ΓSpecIso (.of K)).inv ≫ f.appTop ≫
      X.presheaf.germ ⊤ x (by simp)).hom).toAlgebra
    letI := (((Scheme.ΓSpecIso (.of K)).inv ≫
      (Spec (.of K)).presheaf.germ ⊤ (f x) trivial ≫
      (Spec (.of K)).residue (f x) ≫ f.residueFieldMap x).hom).toAlgebra
    ∃ (ι E Rsh L : Type u)
      (_ : Field E) (_ : Algebra K E) (_ : Algebra (MvRatFunc ι K) E)
      (_ : IsScalarTower K (MvRatFunc ι K) E)
      (_ : IsSepClosure (MvRatFunc ι K) E)
      (_ : CommRing Rsh) (_ : IsLocalRing Rsh)
      (_ : Algebra K Rsh) (_ : Algebra (X.presheaf.stalk x) Rsh)
      (_ : IsScalarTower K (X.presheaf.stalk x) Rsh)
      (_ : Field L) (_ : Algebra (ResidueField (X.presheaf.stalk x)) L)
      (_ : IsSepClosure (ResidueField (X.presheaf.stalk x)) L),
      Cardinal.mk ι = Algebra.trdeg K (X.residueField x) ∧
      IsLocalRing.IsHenselization (X.presheaf.stalk x) L Rsh ∧
      ∃ e : E →ₐ[K] Rsh,
        letI := ((residue Rsh).comp e.toRingHom).toAlgebra
        IsPurelyInseparable E (ResidueField Rsh) ∧
          letI := e.toAlgebra
          IsFilteredColimitOfFiniteTypeAlgebrasWithDimensionAddLE E Rsh
            (Cardinal.toENat (Cardinal.mk ι)) (topologicalKrullDimAt X x)
```

## Tag 0F0V, a proposition

[Tag 0F0V](https://stacks.math.columbia.edu/tag/0F0V) in the Stacks Project.

**`AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_add_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineFiniteType.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineFiniteType.lean#L142). The attribute's comment: “for every natural number n ≥ dim X, which also covers the empty scheme; the literal inequality cd(X) ≤ dim(X) + cd(K) for nonempty X is etaleCohomologicalDimension_le_topologicalKrullDim_add”. References: SGA 4 X (5.2), “special case”; SGA 4 XIV (3.2), “more general”.

> **Stacks Project, Tag 0F0V**, for every bound `n` on the dimension. Let `K` be a field and
> let `X` be an affine scheme of finite type over `K` with `dim(X) ≤ n`. Then `cd(X) ≤ n + cd(K)`.
>
> The proof is the source's induction on the dimension: dimension at most one is Stacks 0F0S, and
> in dimension `d ≥ 2` Noether normalization reduces to `𝔸^d_K`, which is the inductive step
> `etaleCohomologicalDimension_spec_polynomial_le`. This form holds for every `X`, the empty one
> included; with `n = dim(X)` it is the source's `cd(X) ≤ dim(X) + cd(K)`.

```lean
theorem etaleCohomologicalDimension_le_add_of_topologicalKrullDim_le
    (K : Type u) [Field K] (X : Scheme.{u}) (f : X ⟶ Spec (.of K)) [LocallyOfFiniteType f]
    [IsAffine X] (n : ℕ) (hX : topologicalKrullDim X ≤ n) :
    etaleCohomologicalDimension X ≤ n + etaleCohomologicalDimension (Spec (.of K))
```

**`AlgebraicGeometry.Scheme.etaleCohomologicalDimension_le_topologicalKrullDim_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineFiniteType.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineFiniteType.lean#L197). The attribute's comment: “verbatim, cd(X) ≤ dim(X) + cd(K) in WithBot ℕ∞, for nonempty X: for X = ∅ the source's inequality reads 0 ≤ −∞ and fails; etaleCohomologicalDimension_le_add_of_topologicalKrullDim_le covers every X”. References: SGA 4 X (5.2), “special case”; SGA 5 VII (7.1.1), “a), special case”.

> **Stacks Project, Tag 0F0V.** Let `K` be a field and let `X` be a nonempty affine scheme of
> finite type over `K`. Then `cd(X) ≤ dim(X) + cd(K)`.
>
> The inequality is read in `WithBot ℕ∞`, where `dim(X)` lives. Nonemptiness is needed: for
> `X = ∅` the dimension is `−∞` and `cd(∅) = 0`, so the inequality fails; the empty case is covered
> by `etaleCohomologicalDimension_le_add_of_topologicalKrullDim_le`.

```lean
theorem etaleCohomologicalDimension_le_topologicalKrullDim_add
    (K : Type u) [Field K] (X : Scheme.{u}) (f : X ⟶ Spec (.of K)) [LocallyOfFiniteType f]
    [IsAffine X] [Nonempty X] :
    (etaleCohomologicalDimension X : WithBot ℕ∞) ≤
      topologicalKrullDim X + (etaleCohomologicalDimension (Spec (.of K)) : WithBot ℕ∞)
```

## Tag 0F0W, a lemma

[Tag 0F0W](https://stacks.math.columbia.edu/tag/0F0W) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_H_of_smallEtaleSupport_subset_trdegLESet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/TrdegSupportVanishingUnconditional.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/TrdegSupportVanishingUnconditional.lean#L52). References: SGA 2 XIV (3.1), “special case”; SGA 4½ Arcata (4.6.4), “more general”.

> **Stacks Project, Tag 0F0W.** Let `K` be a field and `X` an affine scheme of finite type over
> `K`. Let `E_a ⊆ X` be the set of points `x` with `trdeg_K κ(x) ≤ a`, and let `𝓕` be an abelian
> torsion sheaf on `X_ét` whose support is contained in `E_a`. Then `H^b_ét(X, 𝓕) = 0` for
> `b > a + cd(K)`.
>
> The scheme is of finite type over `K` through `f`, the residue fields are `K`-algebras through
> `f`, `E_a` is `AlgebraicGeometry.Scheme.trdegLESet K f a`, the support is
> `Stacks.EtaleCohomology.smallEtaleSupport` (the points over which some geometric stalk is nonzero),
> torsion is `Stacks.Torsion.torsionSheafProperty` (Stacks 0DD7), `cd(K)` is the cohomological
> dimension `AlgebraicGeometry.Scheme.etaleCohomologicalDimension` of `Spec K` (Stacks 0F0Q), and the
> vanishing of `H^b` is `Subsingleton`.

```lean
theorem subsingleton_H_of_smallEtaleSupport_subset_trdegLESet (K : Type u) [Field K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of K)) [IsAffine X] [LocallyOfFiniteType f] (a : ℕ)
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F)
    (hsupp : Stacks.EtaleCohomology.smallEtaleSupport F ⊆ Scheme.trdegLESet K f a)
    (b : ℕ) (hb : (a : ℕ∞) + Scheme.etaleCohomologicalDimension (Spec (.of K)) < b) :
    Subsingleton (Sheaf.H.{u + 1, u + 1} F b)
```

## Tag 0F0X, a lemma

[Tag 0F0X](https://stacks.math.columbia.edu/tag/0F0X) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleSupport_rightDerived_etaleAbelianDirectImage_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineHigherDirectImageSupport.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologicalDimension/AffineHigherDirectImageSupport.lean#L466). References: SGA 4 XIV (3.1), “more general”.

> **Stacks Project, Tag 0F0X.** Let `f : X ⟶ Y` be an affine morphism of schemes locally of
> finite type over a field `K` (the structure morphisms `gX`, `gY`, with `f ≫ gY = gX`), let
> `E_a(X)` be the set of points `x ∈ X` with `trdeg_K κ(x) ≤ a`
> (`AlgebraicGeometry.Scheme.trdegLESet`), and let `𝓕` be an abelian torsion sheaf on `X_ét` whose
> support is contained in `E_a(X)`. Then `R^q f_* 𝓕` has support contained in `E_{a - q}(Y)`: every
> point `y` of its support has `trdeg_K κ(y) + q ≤ a` (so the support is empty when `q > a`).
>
> The proof is the source's: Stacks 03Q9
> (`AlgebraicGeometry.isZero_stalk_rightDerived_iff_subsingleton_sheafH`) computes the stalk at a
> geometric point over `y` as the cohomology of `X ×_Y Spec(𝒪^{sh}_{Y,y})`, which vanishes by
> `AlgebraicGeometry.subsingleton_H_strictHenselizationBaseChange_of_trdeg` (Stacks 0F0U, 0F0W
> over a separable closure of `K(t_1, …, t_b)`, and the vanishing form of Stacks 03Q6).

```lean
theorem smallEtaleSupport_rightDerived_etaleAbelianDirectImage_subset
    (K : Type u) [Field K] {X Y : Scheme.{u}} (gX : X ⟶ Spec (.of K)) (gY : Y ⟶ Spec (.of K))
    [LocallyOfFiniteType gX] [LocallyOfFiniteType gY] (f : X ⟶ Y) [IsAffineHom f]
    (hfg : f ≫ gY = gX) (a : ℕ) (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F)
    (hsupp : smallEtaleSupport F ⊆ Scheme.trdegLESet K gX a) (q : ℕ) :
    smallEtaleSupport (((etaleAbelianDirectImage.{u, u + 1} f).rightDerived q).obj F) ⊆
      {y | letI : Algebra K (Y.residueField y) :=
          ((Scheme.ΓSpecIso (.of K)).inv ≫ gY.appTop ≫ Y.Γevaluation y).hom.toAlgebra
        Algebra.trdeg K (Y.residueField y) + q ≤ a}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.95, Tag 0F0P](https://stacks.math.columbia.edu/tag/0F0P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
