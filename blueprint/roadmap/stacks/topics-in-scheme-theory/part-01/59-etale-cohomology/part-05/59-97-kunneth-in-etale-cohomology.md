---
declaration: section
origin: cited
lean: Stacks.Cohomology.KunnethMapOnRingedTopoi.directImageMap, Stacks.Cohomology.KunnethMapOnRingedTopoi.kunnethMapOfCupProduct, Stacks.Cohomology.KunnethMapOnRingedTopoi.kunnethMapOfAdjoint, Stacks.Cohomology.KunnethMapOnRingedTopoi.kunnethMapOfCupProduct_eq_kunnethMapOfAdjoint, Stacks.EtaleCohomology.isIso_etaleKunnethCompositeMap_zmod_of_finiteType, Stacks.EtaleCohomology.isIso_etaleKunnethCompositeMap_of_isGE_of_isProper, AlgebraicGeometry.subsingleton_sheafH_and_epi_counit_of_supportSheaf_subset_closedPoints, AlgebraicGeometry.isZero_iff_forall_isZero_etaleHypercohomology_of_closedPointSupport
statement: formalized
proof: formalized
---

# 59.97 Künneth in étale cohomology

Section 59.97 of the Stacks Project, [Tag 0F13](https://stacks.math.columbia.edu/tag/0F13). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F1E, a remark

[Tag 0F1E](https://stacks.math.columbia.edu/tag/0F1E) in the Stacks Project.

**`Stacks.Cohomology.KunnethMapOnRingedTopoi.directImageMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean#L174). The attribute's comment: “the canonical map Rf_*E ⟶ Rc_*p⁻¹E”.

> **The canonical map `Rf_*E ⟶ Rc_*Lp^*E`** for a factorization `c = f ∘ p`: the adjoint
> transpose, for `Lc^* ⊣ Rc_*`, of `pullbackDirectImageCounit`.

```lean
def directImageMap (hp : f.comp p = c)
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedPushforward f).obj E ⟶
      (derivedPushforward c).obj ((derivedPullback p).obj E)
```

**`Stacks.Cohomology.KunnethMapOnRingedTopoi.kunnethMapOfCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean#L214). The attribute's comment: “the canonical map, via the relative cup product of Remark 0B6C”.

> **The Künneth map, via the relative cup product.**  For morphisms of ringed topoi
> `p : W ⟶ X`, `f : X ⟶ S`, `q : W ⟶ Y`, `g : Y ⟶ S` and `c : W ⟶ S` with `c = f ∘ p = g ∘ q`,
> and for `E ∈ D(𝒪_X)`, `K ∈ D(𝒪_Y)`, the canonical map
>
> `Rf_*E ⊗^L_{𝒪_S} Rg_*K ⟶ Rc_*(Lp^*E ⊗^L_{𝒪_W} Lq^*K)`.
>
> It is the canonical maps `Rf_*E ⟶ Rc_*Lp^*E` and `Rg_*K ⟶ Rc_*Lq^*K` in the two tensor factors,
> followed by the relative cup product of [Stacks, Tag 0B6C] for `c`.

```lean
def kunnethMapOfCupProduct :
    ((derivedTensorProductFunctor S.O).obj ((derivedPushforward f).obj E)).obj
        ((derivedPushforward g).obj K) ⟶
      (derivedPushforward c).obj
        (((derivedTensorProductFunctor W.O).obj ((derivedPullback p).obj E)).obj
          ((derivedPullback q).obj K))
```

**`Stacks.Cohomology.KunnethMapOnRingedTopoi.kunnethMapOfAdjoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean#L236). The attribute's comment: “the canonical map, as the adjoint of the map on inverse images”.

> **The Künneth map, as an adjoint.**  The same canonical map
>
> `Rf_*E ⊗^L_{𝒪_S} Rg_*K ⟶ Rc_*(Lp^*E ⊗^L_{𝒪_W} Lq^*K)`,
>
> written as the adjoint, for `Lc^* ⊣ Rc_*`, of the compatibility of derived pullback with the
> derived tensor product ([Stacks, Tag 07A4]) followed by the maps `Lc^*Rf_*E ⟶ Lp^*E` and
> `Lc^*Rg_*K ⟶ Lq^*K` in the two factors.

```lean
def kunnethMapOfAdjoint :
    ((derivedTensorProductFunctor S.O).obj ((derivedPushforward f).obj E)).obj
        ((derivedPushforward g).obj K) ⟶
      (derivedPushforward c).obj
        (((derivedTensorProductFunctor W.O).obj ((derivedPullback p).obj E)).obj
          ((derivedPullback q).obj K))
```

**`Stacks.Cohomology.KunnethMapOnRingedTopoi.kunnethMapOfCupProduct_eq_kunnethMapOfAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/KunnethMap.lean#L252). The attribute's comment: “the two constructions of the remark agree”.

> **The two constructions of the Künneth map agree**: `kunnethMapOfCupProduct` equals
> `kunnethMapOfAdjoint`.

```lean
theorem kunnethMapOfCupProduct_eq_kunnethMapOfAdjoint :
    kunnethMapOfCupProduct p f c hmosp hmosf hmosc q g hmosq hmosg hp hq E K =
      kunnethMapOfAdjoint p f c hmosp hmosf hmosc q g hmosq hmosg hp hq E K
```

## Tag 0F14, a lemma

[Tag 0F14](https://stacks.math.columbia.edu/tag/0F14) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_etaleKunnethCompositeMap_zmod_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperKunneth/KunnethFiniteType.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperKunneth/KunnethFiniteType.lean#L68). The attribute's comment: “(2); on D((Spec k)_et, ℤ/nℤ), which global sections identify with D(ℤ/nℤ) for k separably closed, so that the direct images to Spec k are the derived global sections”. References: SGA 4½ Th finitude (1.11), “Künneth arrow RΓ(X”.

> **[Stacks, Tag 0F14] (2).** Let `k` be a separably closed field, `f : X ⟶ Spec k` proper,
> `g : Y ⟶ Spec k` of finite type, and `n ≥ 1`. For `E ∈ D(X_étale, ℤ/nℤ)` and
> `K ∈ D(Y_étale, ℤ/nℤ)`, unbounded, the Künneth map
> `RΓ(X, E) ⊗^L_{ℤ/nℤ} RΓ(Y, K) = Rf_*E ⊗^L Rg_*K ⟶ R(pr₂ ≫ g)_*(pr₁⁻¹E ⊗^L pr₂⁻¹K)
> = RΓ(X ×_k Y, pr₁⁻¹E ⊗^L pr₂⁻¹K)` in `D((Spec k)_étale, ℤ/nℤ) = D(ℤ/nℤ)` is an
> isomorphism.

```lean
theorem isIso_etaleKunnethCompositeMap_zmod_of_finiteType (n : ℕ) (hn : 0 < n) (k : Type u)
    [Field k] [IsSepClosed k] {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (g : Y ⟶ Spec (.of k)) [LocallyOfFiniteType g] [QuasiCompact g]
    (E : DerivedCategory (EtaleModules.{u, 0} (ZMod n) X))
    (K : DerivedCategory (EtaleModules.{u, 0} (ZMod n) Y)) :
    IsIso (etaleKunnethCompositeMap.{u, 0} (ZMod n) f g (pullback.fst f g) (pullback.snd f g)
      pullback.condition E K)
```

**`Stacks.EtaleCohomology.isIso_etaleKunnethCompositeMap_of_isGE_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperKunneth/KunnethIntegral.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperKunneth/KunnethIntegral.lean#L69). The attribute's comment: “(1); on D((Spec k)_et, ℤ), which global sections identify with D(ℤ) for k separably closed, so that the direct images to Spec k are the derived global sections”.

> **[Stacks, Tag 0F14] (1).** Let `k` be a separably closed field, `f : X ⟶ Spec k` proper and
> `g : Y ⟶ Spec k` with `Y` quasi-compact and quasi-separated. Let `E ∈ D⁺(X_étale)` have torsion
> cohomology sheaves and `K ∈ D⁺(Y_étale)`. Then the Künneth map
> `RΓ(X, E) ⊗^L_ℤ RΓ(Y, K) = Rf_*E ⊗^L_ℤ Rg_*K ⟶ R(pr₂ ≫ g)_*(pr₁⁻¹E ⊗^L_ℤ pr₂⁻¹K)
> = RΓ(X ×_k Y, pr₁⁻¹E ⊗^L_ℤ pr₂⁻¹K)` in `D((Spec k)_étale, ℤ) = D(ℤ)` is an isomorphism.

```lean
theorem isIso_etaleKunnethCompositeMap_of_isGE_of_isProper (k : Type u) [Field k]
    [IsSepClosed k] {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (g : Y ⟶ Spec (.of k)) [CompactSpace Y] [QuasiSeparatedSpace Y]
    (E : DerivedCategory (EtaleModules.{u, 0} ℤ X)) (a : ℤ) (hE : E.IsGE a)
    (hT : ∀ n, IsTorsionEtaleModule.{u, 0} ℤ X ((DerivedCategory.homologyFunctor _ n).obj E))
    (K : DerivedCategory (EtaleModules.{u, 0} ℤ Y)) (b : ℤ) (hK : K.IsGE b) :
    IsIso (etaleKunnethCompositeMap.{u, 0} ℤ f g (pullback.fst f g) (pullback.snd f g)
      pullback.condition E K)
```

## Tag 0F1F, a lemma

[Tag 0F1F](https://stacks.math.columbia.edu/tag/0F1F) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_sheafH_and_epi_counit_of_supportSheaf_subset_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointSupport/Main.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointSupport/Main.lean#L75).

> Let `K` be a separably closed field, let `X` be a scheme of finite type over `K` and let `F`
> be an abelian sheaf on the small étale site of `X` whose support is contained in the set of
> closed points of `X`. Then `H^q(X, F) = 0` for `q > 0`, and `F` is globally generated: the
> constant sheaf on its group of global sections surjects onto it.

```lean
public theorem subsingleton_sheafH_and_epi_counit_of_supportSheaf_subset_closedPoints
    (B : BigEtaleSite.{u}) (K : Type u) [Field K] [IsSepClosed K] (X : B.Scheme)
    (f : X.obj ⟶ Spec (.of K)) [LocallyOfFiniteType f] [QuasiCompact f]
    (F : SmallEtaleAbelianSheaf B X)
    (hF : supportSheaf B X.obj X.property F ⊆ {x : X.obj | IsClosed ({x} : Set X.obj)}) :
    (∀ q : ℕ, 0 < q → Subsingleton (Sheaf.H.{u + 1, u + 1} F q)) ∧
      Epi ((constantSheafΓAdj (SmallEtale.topology B X.obj X.property)
        AddCommGrpCat.{u + 1}).counit.app F)
```

## Tag 0F1G, a lemma

[Tag 0F1G](https://stacks.math.columbia.edu/tag/0F1G) in the Stacks Project.

**`AlgebraicGeometry.isZero_iff_forall_isZero_etaleHypercohomology_of_closedPointSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointSupportDetection.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointSupportDetection.lean#L587).

> **[Stacks, Tag 0F1G].** Let `K` be a separably closed field, `X` a scheme of finite type over
> `K` and `Q` an object of the unbounded derived category of abelian sheaves on the small étale
> site of `X` whose stalks vanish away from the closed points of `X`. Then `Q` is zero if and only
> if all of its hypercohomology groups vanish.
>
> One direction is formal. For the other, `Q` is zero exactly when every cohomology sheaf `H^q(Q)`
> is zero; the stalk hypothesis says that each `H^q(Q)` is supported at closed points, so
> [Stacks, Tag 0BKZ] identifies `H^q(X, Q)` with `Γ(X, H^q(Q))`
> (`AlgebraicGeometry.nonempty_hypercohomologyAbIsoΓHomology_of_supportSheaf_subset_closedPoints`),
> and [Stacks, Tag 0F1F] makes a sheaf supported at closed points with no global sections zero
> (`AlgebraicGeometry.isZero_of_isZero_Γ_of_supportSheaf_subset_closedPoints`).

```lean
public theorem isZero_iff_forall_isZero_etaleHypercohomology_of_closedPointSupport
    (K : Type u) [Field K] [IsSepClosed K] (f : X ⟶ Spec (.of K))
    [LocallyOfFiniteType f] [QuasiCompact f]
    (Q : DerivedCategory (Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}))
    (hQ : ∀ (p : GeometricPoint X) (q : ℤ), ¬ IsClosed ({p.hom default} : Set X) →
      IsZero (etaleStalk B X hX p
        ((DerivedCategory.homologyFunctor
          (Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}) q).obj Q).obj)) :
    IsZero Q ↔
      ∀ q : ℤ, IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u + 1} q).obj
        ((smallEtaleDerivedGlobalSectionsAb.{u, u + 1} B X hX).obj Q))
```

## Tag 0F1H, a lemma

[Tag 0F1H](https://stacks.math.columbia.edu/tag/0F1H) in the Stacks Project.

**`Stacks.EtaleCohomology.OpenImmersionProductSquare.isIso_baseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/OpenImmersionProductSquareBaseChange.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/OpenImmersionProductSquareBaseChange.lean#L55).

> Let `K` be a field, `j : U ⟶ X` an open immersion of schemes of finite type over `K` and `Y`
> a scheme of finite type over `K`. For every abelian sheaf `𝓕` on `U_étale` whose stalks are
> torsion of orders invertible in `K`, the base change map `q⁻¹Rj_*𝓕 ⟶ Rh_*p⁻¹𝓕` of the square
> ```
> Y ×_K X  ←-h-  Y ×_K U
>    |q              |p
>    X     ←-j-      U
> ```
> is an isomorphism (in `D⁺((Y ×_K X)_étale)`, `𝓕` placed in degree zero).

```lean
theorem isIso_baseChangeMap {K : Type u} [Field K] {X U Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of K)) (sU : U ⟶ Spec (.of K)) (sY : Y ⟶ Spec (.of K))
    (j : U ⟶ X) [IsOpenImmersion j] (hj : j ≫ sX = sU) [LocallyOfFiniteType sX] [QuasiCompact sX]
    [LocallyOfFiniteType sU] [QuasiCompact sU] [LocallyOfFiniteType sY] [QuasiCompact sY]
    (𝓕 : Sheaf (smallEtaleTopology U) Ab.{u + 1})
    (h𝓕 : ∀ (t : GeometricPoint U) (a : (smallEtaleStalkAb t.hom).obj 𝓕),
      ∃ n : ℕ, 0 < n ∧ IsUnit ((n : ℤ) : K) ∧ n • a = 0) :
    IsIso (baseChangeMap sX sU sY j hj 𝓕)
```

## Tag 0F1I, a lemma

[Tag 0F1I](https://stacks.math.columbia.edu/tag/0F1I) in the Stacks Project.

**`Stacks.EtaleCohomology.BaseChangeOverField.isIso_smallEtaleDerivedBaseChangeAb_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/BaseChangeOverFieldTheorem.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/BaseChangeOverFieldTheorem.lean#L248).

> **[Stacks, Tag 0F1I].** Let `K` be a field. For any commutative diagram
>
> ```
> X  ←-p-  X'  ←-h-  Y
> |        |f'       |e
> Spec K ←-s- S' ←-g- T
> ```
>
> of schemes over `K` with `X' = X ×_{Spec K} S'` and `Y = X' ×_{S'} T` and `g` quasi-compact and
> quasi-separated, and every abelian sheaf `𝓕` on `T_étale` whose stalks are torsion of orders
> invertible in `K`, the base change map `(f')⁻¹Rg_*𝓕 ⟶ Rh_*e⁻¹𝓕` is an isomorphism (in
> `D⁺(X'_étale)`, `𝓕` placed in degree zero).
>
> `𝓕` is the filtered colimit of its subsheaves `𝓕[n]`, `n` invertible in `K`
> (`isIso_higherBaseChangeMapAb_of_forall_annihilated`), and for those this is
> `derivedBaseChangeHolds_of_isUnit`.

```lean
theorem isIso_smallEtaleDerivedBaseChangeAb_of_field (K : Type u) [Field K] {X : Scheme.{u}}
    (πX : X ⟶ Spec (.of K)) {S' X' T Y : Scheme.{u}} (s : S' ⟶ Spec (.of K)) (p : X' ⟶ X)
    (f' : X' ⟶ S') (hp : IsPullback p f' πX s) (g : T ⟶ S') (h : Y ⟶ X') (e : Y ⟶ T)
    (sq : IsPullback h e f' g) [QuasiCompact g] [QuasiSeparated g]
    (𝓕 : Sheaf (smallEtaleTopology T) Ab.{u + 1})
    (h𝓕 : ∀ (t : GeometricPoint T) (a : (smallEtaleStalkAb t.hom).obj 𝓕),
      ∃ n : ℕ, 0 < n ∧ IsUnit ((n : ℤ) : K) ∧ n • a = 0) :
    IsIso ((smallEtaleDerivedBaseChangeAb f' g h e sq.w).app
      ((DerivedCategory.Plus.singleFunctor _ 0).obj 𝓕))
```

## Tag 0F1J, a lemma

[Tag 0F1J](https://stacks.math.columbia.edu/tag/0F1J) in the Stacks Project.

**`Stacks.EtaleCohomology.EtaleCoefficients.isIso_tensorBaseChangeMap_of_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/TensorBaseChangeOverField.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/TensorBaseChangeOverField.lean#L84).

> **[Stacks, Tag 0F1J].** Let `K` be a field and `n ≥ 1` an integer invertible in `K`. Consider
> a commutative diagram
> ```
> X <-p-- X' <-h-- Y
> |       |f'      |e
> v       v        v
> Spec K <- S' <-g- T
> ```
> of schemes with `X' = X ×_{Spec K} S'` and `Y = X' ×_{S'} T` and `g` quasi-compact and
> quasi-separated. The canonical map
>
> `p⁻¹E ⊗^L_{ℤ/nℤ} (f')⁻¹Rg_*F ⟶ Rh_*(h⁻¹p⁻¹E ⊗^L_{ℤ/nℤ} e⁻¹F)`
>
> is an isomorphism if `E ∈ D⁺(X_étale, ℤ/nℤ)` has Tor amplitude in `[a, ∞]` for some `a ∈ ℤ` and
> `F ∈ D⁺(T_étale, ℤ/nℤ)`.
>
> This is `isIso_tensorBaseChangeMap_zmod_of_derivedBaseChangeHolds`, with derived base change over
> `X` and over the schemes finite over the affine opens of `X` given by [Stacks, Tag 0F1I]
> (`derivedBaseChangeHolds_of_isUnit`: `X` over `K` is arbitrary there). The lower bound on `E`
> (`_hE`, `E ∈ D⁺`) is part of the source's statement; the proof does not need it.

```lean
theorem isIso_tensorBaseChangeMap_of_isUnit (K : Type u) [Field K] (n : ℕ) [NeZero n]
    (hn : IsUnit (n : K)) {X X' Y S' T : Scheme.{u}} (πX : X ⟶ Spec (.of K))
    (πS : S' ⟶ Spec (.of K)) (p : X' ⟶ X) (f' : X' ⟶ S') (hX' : IsPullback p f' πX πS)
    (g : T ⟶ S') (h : Y ⟶ X') (e : Y ⟶ T) (hY : IsPullback h e f' g) [QuasiCompact g]
    [QuasiSeparated g] (E : DerivedModules (ULift.{u + 1} (ZMod n)) X) (_hE : ∃ b : ℤ, E.IsGE b)
    (a : ℤ) (hEa : HasTorAmplitudeGE (ULift.{u + 1} (ZMod n)) E a)
    (F : DerivedModules (ULift.{u + 1} (ZMod n)) T) (hF : ∃ b : ℤ, F.IsGE b) :
    IsIso (tensorBaseChangeMap (ULift.{u + 1} (ZMod n)) f' g h e hY.w
      ((pullback (ULift.{u + 1} (ZMod n)) p).obj E) F)
```

## Tag 0F1N, a lemma

[Tag 0F1N](https://stacks.math.columbia.edu/tag/0F1N) in the Stacks Project.

**`Stacks.EtaleCohomology.EtaleCoefficients.isIso_tensorBaseChangeMap_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/TensorBaseChangeOverFieldFiniteType.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/TensorBaseChangeOverFieldFiniteType.lean#L82).

> **[Stacks, Tag 0F1N].** Let `K` be a field and `n ≥ 1` an integer invertible in `K`.
> Consider a commutative diagram
> ```
> X <-p-- X' <-h-- Y
> |       |f'      |e
> v       v        v
> Spec K <- S' <-g- T
> ```
> of schemes of finite type over `K` (through `πX`, `πS` and `g ≫ πS`) with `X' = X ×_K S'` and
> `Y = X' ×_{S'} T`. Then the canonical map
>
> `p⁻¹E ⊗^L_{ℤ/nℤ} (f')⁻¹Rg_*F ⟶ Rh_*(h⁻¹p⁻¹E ⊗^L_{ℤ/nℤ} e⁻¹F)`
>
> is an isomorphism for all `E ∈ D(X_étale, ℤ/nℤ)` and `F ∈ D(T_étale, ℤ/nℤ)`.
>
> The reduction to `E ∈ D⁺` of Tor amplitude bounded below and `F ∈ D⁺`, where the functors
> commute with direct sums because `cd(g), cd(h) < ∞` ([Stacks, Tag 0F10]), is
> `isIso_tensorBaseChangeMap_of_finiteType_of_isGE`; the bounded below case is [Stacks, Tag 0F1J]
> (`isIso_tensorBaseChangeMap_of_isUnit`).

```lean
theorem isIso_tensorBaseChangeMap_of_finiteType (K : Type u) [Field K] (n : ℕ) [NeZero n]
    (hn : IsUnit (n : K)) {X X' Y S' T : Scheme.{u}} (πX : X ⟶ Spec (.of K))
    (πS : S' ⟶ Spec (.of K)) (p : X' ⟶ X) (f' : X' ⟶ S') (h : Y ⟶ X') (e : Y ⟶ T)
    (g : T ⟶ S') [LocallyOfFiniteType πX] [QuasiCompact πX] [LocallyOfFiniteType πS]
    [QuasiCompact πS] [LocallyOfFiniteType (g ≫ πS)] [QuasiCompact (g ≫ πS)]
    (hX' : IsPullback p f' πX πS) (hY : IsPullback h e f' g)
    (E : DerivedModules (ULift.{u + 1} (ZMod n)) X)
    (F : DerivedModules (ULift.{u + 1} (ZMod n)) T) :
    IsIso (tensorBaseChangeMap (ULift.{u + 1} (ZMod n)) f' g h e hY.w
      ((pullback (ULift.{u + 1} (ZMod n)) p).obj E) F)
```

## Tag 0F1P, a lemma

[Tag 0F1P](https://stacks.math.columbia.edu/tag/0F1P) in the Stacks Project.

**`Stacks.EtaleCohomology.EtaleCoefficients.isIso_kunnethMap_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/KunnethOverSeparablyClosedFieldFiniteType.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/KunnethOverSeparablyClosedFieldFiniteType.lean#L101). References: SGA 4½ Th finitude (1.11), “special case”.

> **[Stacks, Tag 0F1P], as the Künneth map of [Stacks, Tag 0F1E].** Let `k` be a separably
> closed field, `X` and `Y` schemes of finite type over `k` (through `f` and `g`), and `n ≥ 1` an
> integer invertible in `k`. For `E ∈ D(X_étale, ℤ/nℤ)` and `K ∈ D(Y_étale, ℤ/nℤ)` the Künneth map
>
> `RΓ(X, E) ⊗^L_{ℤ/nℤ} RΓ(Y, K) = Rf_*E ⊗^L Rg_*K ⟶ R(pr₁ ≫ f)_*(pr₁⁻¹E ⊗^L pr₂⁻¹K)
>   = RΓ(X ×_k Y, pr₁⁻¹E ⊗^L pr₂⁻¹K)`
>
> is an isomorphism in `D((Spec k)_étale, ℤ/nℤ) = D(ℤ/nℤ)`.

```lean
theorem isIso_kunnethMap_of_isSepClosed (hn : IsUnit (n : k))
    (E : DerivedModules (ULift.{u + 1} (ZMod n)) X)
    (K : DerivedModules (ULift.{u + 1} (ZMod n)) Y) :
    IsIso (kunnethMap (ULift.{u + 1} (ZMod n)) (Limits.pullback.fst f g) f
      (Limits.pullback.snd f g) g Limits.pullback.condition E K)
```

**`Stacks.EtaleCohomology.EtaleCoefficients.kunnethOverSepClosedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/KunnethOverSeparablyClosedFieldFiniteType.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/KunnethOverSeparablyClosedFieldFiniteType.lean#L120).

> **[Stacks, Tag 0F1P].** Let `k` be a separably closed field, `X` and `Y` schemes of finite
> type over `k` (through `f` and `g`), and `n ≥ 1` an integer invertible in `k`. For
> `E ∈ D(X_étale, ℤ/nℤ)` and `K ∈ D(Y_étale, ℤ/nℤ)`
>
> `RΓ(X ×_k Y, pr₁⁻¹E ⊗^L_{ℤ/nℤ} pr₂⁻¹K) ≅ RΓ(X, E) ⊗^L_{ℤ/nℤ} RΓ(Y, K)`
>
> in `D(ℤ/nℤ)`, where `RΓ(Z, -) = Γ ∘ R(Z ⟶ Spec k)_*` for the global sections equivalence
> `Γ : D((Spec k)_étale, ℤ/nℤ) ≌ D(ℤ/nℤ)` (`derivedModulesEquivOfSepClosed`). It is the inverse of
> `Γ` of the Künneth map of [Stacks, Tag 0F1E] (`isIso_kunnethMap_of_isSepClosed`), followed by the
> compatibility of `Γ` with `⊗^L` (`kunnethOverSepClosedIso_inv`).

```lean
def kunnethOverSepClosedIso [HasDerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (ZMod n)))]
    (hn : IsUnit (n : k))
    (E : DerivedModules (ULift.{u + 1} (ZMod n)) X)
    (K : DerivedModules (ULift.{u + 1} (ZMod n)) Y) :
    (derivedModulesEquivOfSepClosed k (ULift.{u + 1} (ZMod n))).functor.obj
        ((pushforward (ULift.{u + 1} (ZMod n)) (Limits.pullback.fst f g ≫ f)).obj
          (((tensor (ULift.{u + 1} (ZMod n)) (Limits.pullback f g)).obj
            ((pullback (ULift.{u + 1} (ZMod n)) (Limits.pullback.fst f g)).obj E)).obj
              ((pullback (ULift.{u + 1} (ZMod n)) (Limits.pullback.snd f g)).obj K))) ≅
      ((CochainComplex.DerivedTensor.canonicalDerivedTensorProduct
          (ULift.{u + 1} (ZMod n))).tensor.obj
        ((derivedModulesEquivOfSepClosed k (ULift.{u + 1} (ZMod n))).functor.obj
          ((pushforward (ULift.{u + 1} (ZMod n)) f).obj E))).obj
        ((derivedModulesEquivOfSepClosed k (ULift.{u + 1} (ZMod n))).functor.obj
          ((pushforward (ULift.{u + 1} (ZMod n)) g).obj K))
```

**`Stacks.EtaleCohomology.EtaleCoefficients.kunnethOverSepClosedIso_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/KunnethOverSeparablyClosedFieldFiniteType.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Kunneth/KunnethOverSeparablyClosedFieldFiniteType.lean#L143). References: SGA 4½ Th finitude (1.11), “special case”.

> **[Stacks, Tag 0F1P]: the isomorphism is the Künneth map of [Stacks, Tag 0F1E].** The inverse
> of `kunnethOverSepClosedIso` is the compatibility of `Γ` with `⊗^L`,
> `RΓ(X, E) ⊗^L RΓ(Y, K) ≅ Γ(Rf_*E ⊗^L Rg_*K)`, followed by `Γ` of the Künneth map
> `Rf_*E ⊗^L Rg_*K ⟶ R(pr₁ ≫ f)_*(pr₁⁻¹E ⊗^L pr₂⁻¹K)` of Tag 0F1E.

```lean
theorem kunnethOverSepClosedIso_inv
    [HasDerivedCategory (ModuleCat.{u + 1} (ULift.{u + 1} (ZMod n)))] (hn : IsUnit (n : k))
    (E : DerivedModules (ULift.{u + 1} (ZMod n)) X)
    (K : DerivedModules (ULift.{u + 1} (ZMod n)) Y) :
    (kunnethOverSepClosedIso k n f g hn E K).inv =
      (((derivedModulesEquivOfSepClosedTensorIso k (ULift.{u + 1} (ZMod n))).app
          ((pushforward (ULift.{u + 1} (ZMod n)) f).obj E)).app
          ((pushforward (ULift.{u + 1} (ZMod n)) g).obj K)).inv ≫
        (derivedModulesEquivOfSepClosed k (ULift.{u + 1} (ZMod n))).functor.map
          (kunnethMap (ULift.{u + 1} (ZMod n)) (Limits.pullback.fst f g) f
            (Limits.pullback.snd f g) g Limits.pullback.condition E K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.97, Tag 0F13](https://stacks.math.columbia.edu/tag/0F13)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
