---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_etaleLocalFactorization, Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_etaleLocalFactorizationCover, Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_flat_geometricallyReduced, Stacks.EtaleCohomology.isIso_smallEtaleBaseChangeAb_of_flat_geometricallyReduced, Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isSepClosed, Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isSepClosed_of_quasiCompact, Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isSepClosed_locallyOfFiniteType, Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isOpenMap_connectedFibreOpens
statement: formalized
proof: formalized
---

# 59.87 Base change for pushforward

Section 59.87 of the Stacks Project, [Tag 0EZW](https://stacks.math.columbia.edu/tag/0EZW). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EZX, a lemma

[Tag 0EZX](https://stacks.math.columbia.edu/tag/0EZX) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_etaleLocalFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChange.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChange.lean#L382). The attribute's comment: “The chain of four identifications of the source's first paragraph -- that the sections of `f⁻¹ g_* F` and of `h_* e⁻¹ F` over an object with such a factorization are both the sections of `F` over `V ×_S T`, compatibly with the base change map -- rests on Tag 0A3H (used twice, once for `f` and once for `e`) read through Tag 03EF, and is carried as the declared hypothesis `hlocal`. What is supplied here is the source's second paragraph: the covering condition gives enough objects with a flat such factorization, flatness coming from `f` by `hasFlatConnectedFactorization_of_quasiCompact`, and a map of sheaves bijective on sections over a family of objects covering every object is an isomorphism.”.

> **Stacks Project, Tag 0EZX.** In a cartesian square of schemes with `f : X ⟶ S` flat, if
> every object of the small étale site of `X` has an étale covering whose members factor through
> an étale `S`-scheme by a quasi-compact morphism with geometrically connected fibres, then the
> canonical base change map `f⁻¹ g_* F ⟶ h_* e⁻¹ F` is an isomorphism for every sheaf of sets
> `F` on the small étale site of `T`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_etaleLocalFactorization (f : X ⟶ S) (h : Y ⟶ X)
    (e : Y ⟶ T) (g : T ⟶ S) (sq : IsPullback h e f g) [Flat f]
    (F : Sheaf (smallEtaleTopology T) (Type (max (u + 1) v)))
    (hcover : ∀ U : X.Etale,
      ∃ (ι : Type (u + 1)) (U' : ι → X.Etale) (a : ∀ i, U' i ⟶ U)
        (V : ι → S.Etale) (k : ∀ i, (U' i).left ⟶ (V i).left),
        Sieve.ofArrows U' a ∈ smallEtaleTopology X U ∧
          ∀ i, k i ≫ (V i).hom = (U' i).hom ≫ f ∧
            QuasiCompact (k i) ∧ GeometricallyConnected (k i))
    (hlocal : ∀ ⦃U : X.Etale⦄, HasFlatConnectedFactorization f U →
      Function.Bijective
        (((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F).hom.app (op U))) :
    IsIso ((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F)
```

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_etaleLocalFactorizationCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean, line 850](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean#L850). The attribute's comment: “no residual hypothesis. Both paragraphs of the source's proof are supplied. The first is the chain of four identifications -- that the sections of `f⁻¹ g_* F` and of `h_* e⁻¹ F` over an object with such a factorization are both the sections of `F` over `V ×_S T`, compatibly with the base change map -- and it is `local_baseChange_compatible`: Tag 0A3H in the localized form of the source's own argument, used twice, once at `f` and once at `e`, is `smallEtaleInverseImageSectionsIso` and is unconditional, the factorization upstairs is `etaleBaseChangeFactor`, and their compatibility with the base change map is the Beck-Chevalley identity for the mate defining `smallEtaleSetBaseChange`. The second paragraph is that the covering condition gives enough objects with a flat such factorization, flatness coming from `f` by `hasFlatConnectedFactorization_of_quasiCompact`, and that a map of sheaves bijective on sections over a family of objects covering every object is an isomorphism.”.

> In a cartesian square of schemes with `f : X ⟶ S` flat, if every object of the small étale
> site of `X` has an étale covering whose members factor through an étale `S`-scheme by a
> quasi-compact morphism with geometrically connected fibres, then the canonical base change map
> `f⁻¹ g_* F ⟶ h_* e⁻¹ F` is an isomorphism for every sheaf of sets `F` on the small étale site of
> `T`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_etaleLocalFactorizationCover (f : X ⟶ S) (h : Y ⟶ X)
    (e : Y ⟶ T) (g : T ⟶ S) (sq : IsPullback h e f g) [Flat f]
    (F : Sheaf (smallEtaleTopology T) (Type (max (u + 1) v)))
    (hcover : ∀ U : X.Etale,
      ∃ (ι : Type (u + 1)) (U' : ι → X.Etale) (a : ∀ i, U' i ⟶ U)
        (V : ι → S.Etale) (k : ∀ i, (U' i).left ⟶ (V i).left),
        Sieve.ofArrows U' a ∈ smallEtaleTopology X U ∧
          ∀ i, k i ≫ (V i).hom = (U' i).hom ≫ f ∧
            QuasiCompact (k i) ∧ GeometricallyConnected (k i)) :
    IsIso ((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F)
```

## Tag 0EYS, a lemma

[Tag 0EYS](https://stacks.math.columbia.edu/tag/0EYS) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_flat_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean, line 875](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean#L875). The attribute's comment: “no residual hypothesis. The source merges Tag 0EZX with Tag 0EY5, and both are supplied: the chain of identifications of the sections of `f⁻¹ g_* F` and of `h_* e⁻¹ F` over an object carrying a flat quasi-compact factorization with geometrically connected fibres is `local_baseChange_compatible`, exactly as for Tag 0EZX above, and the covering of the small étale site of `X` by objects with such a factorization is Tag 0EY5 and is `hasEnoughObjects_hasFlatConnectedFactorization`. The globalization from sections to sheaves is Tag 0H6Y.”.

> In a cartesian square of schemes whose left vertical morphism `f : X ⟶ S` is flat, locally
> of finite presentation and has geometrically reduced fibres, the canonical base change map
> `f⁻¹ g_* F ⟶ h_* e⁻¹ F` is an isomorphism for every sheaf of sets `F` on the small étale site of
> `T`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_flat_geometricallyReduced (f : X ⟶ S) (h : Y ⟶ X)
    (e : Y ⟶ T) (g : T ⟶ S) (sq : IsPullback h e f g)
    [Flat f] [LocallyOfFinitePresentation f] [GeometricallyReduced f]
    (F : Sheaf (smallEtaleTopology T) (Type (max (u + 1) v))) :
    IsIso ((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F)
```

**`Stacks.EtaleCohomology.isIso_smallEtaleBaseChangeAb_of_flat_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleBaseChangeAbOfSets.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleBaseChangeAbOfSets.lean#L303). The attribute's comment: “for abelian sheaves, at the comparison `smallEtaleBaseChangeAb` of [Stacks, Tag 0F02]; no residual hypothesis. The statement for sheaves of sets is `isIso_smallEtaleSetBaseChange_of_flat_geometricallyReduced`, and the abelian map is invertible as soon as the set-valued one is, by `isIso_smallEtaleBaseChangeAb_of_isIso_smallEtaleSetBaseChange`.”.

> **Stacks Project, Tag 0EYS, for abelian sheaves.** In a cartesian square of schemes whose
> left vertical morphism `f : X ⟶ S` is flat, locally of finite presentation and has
> geometrically reduced fibres, the base change map `f⁻¹ g_* 𝓕 ⟶ h_* e⁻¹ 𝓕` is an isomorphism for
> every abelian sheaf `𝓕` on the small étale site of `T`. The map is
> `Stacks.EtaleCohomology.smallEtaleBaseChangeAb`, the underived base change map of
> [Stacks, Tag 0F02]. It is invertible because the base change map of sheaves of sets is
> (`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_flat_geometricallyReduced`), by
> `Stacks.EtaleCohomology.isIso_smallEtaleBaseChangeAb_of_isIso_smallEtaleSetBaseChange`.

```lean
public theorem isIso_smallEtaleBaseChangeAb_of_flat_geometricallyReduced (f : X ⟶ S)
    (h : Y ⟶ X) (e : Y ⟶ T) (g : T ⟶ S) (sq : IsPullback h e f g)
    [Flat f] [LocallyOfFinitePresentation f] [GeometricallyReduced f] :
    IsIso (smallEtaleBaseChangeAb f g h e sq.w)
```

## Tag 0EZY, a lemma

[Tag 0EZY](https://stacks.math.columbia.edu/tag/0EZY) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeSepClosedField.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeSepClosedField.lean#L147). The attribute's comment: “the case of `X` of finite type over the separably closed field, stated for `X` locally of finite type. What is proved unconditionally is the covering condition of Tag 0EZX: an affine open of an étale `X`-scheme is Noetherian, hence locally connected by Tag 04MF, so the connected component of any of its points is an open quasi-compact subscheme, and over a separably closed field a connected scheme is geometrically connected by Tag 0363; flatness of `f` is automatic over a field. The source's reduction of the general case to this one -- write an affine `X` as a cofiltered limit of affine finite-type `Spec k`-schemes and use the compatibility of the base change map with such limits -- is Tag 0EZT part (1), which has no carrier in the library, so the general case is not asserted. The chain of identifications of sections on which Tag 0EZX feeds rests on Tag 0A3H read through Tag 03EF, a separate cited tag unavailable in that form, and is carried -- exactly as in Tags 0EZX, 0EYS and 0EZZ -- as the declared hypothesis `hlocal`.”.

> **Stacks Project, Tag 0EZY**, in the case of `X` locally of finite type over the separably
> closed field. Let `k` be a separably closed field and let `f : X ⟶ Spec k` be locally of finite
> type. Then in a cartesian square over `f` the canonical base change map `f⁻¹ g_* F ⟶ h_* e⁻¹ F`
> is an isomorphism for every sheaf of sets `F` on the small étale site of `T`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_isSepClosed (k : Type u) [Field k] [IsSepClosed k]
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] (h : Y ⟶ X) (e : Y ⟶ T)
    (g : T ⟶ Spec (.of k)) (sq : IsPullback h e f g)
    (F : Sheaf (smallEtaleTopology T) (Type (max (u + 1) v)))
    (hlocal : ∀ ⦃U : X.Etale⦄, HasFlatConnectedFactorization f U →
      Function.Bijective
        (((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F).hom.app (op U))) :
    IsIso ((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F)
```

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isSepClosed_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeSepClosedFieldGeneral.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeSepClosedFieldGeneral.lean#L549). The attribute's comment: “the tag's statement for an arbitrary scheme `X` over the spectrum of a separably closed field, with nothing assumed of `X` and no result of the source assumed. The assumption that `g` be quasi-compact and quasi-separated is the standing convention of Section 0EZW, stated at its start for every cartesian diagram of the section, and the source's proof passes through Tag 0EZT, which assumes it; it cannot be dropped (see this file's module docstring for a counterexample with `g` not quasi-compact). The proof is the stalkwise one of Tag 0F00 specialized to `S = Spec k`: stalks at geometric points detect isomorphisms; the stalk at `x̄` is global sections over the strict henselization `Z = Spec(O^sh_{X,x̄})`; the pasting law for the base change maps of the square of `Z ⟶ X` stacked on the given square splits the base change map of the outer rectangle into `Γ(Z, ι⁻¹ β)` followed by the base change map of the square of `Z ⟶ X` over `h`; the latter is bijective on global sections by Tag 03Q9 for sheaves of sets (`isIso_Γ_map_smallEtaleSetBaseChange_strictHenselization`, `h` being quasi-compact and quasi-separated as a base change of `g`), and the former composite is bijective by the first paragraph of Tag 0EZX (`local_baseChange_compatible`) at the final object of `Z_étale`, `Z ⟶ Spec k` being flat, quasi-compact and geometrically connected (Z is local, hence connected, and connected implies geometrically connected over a separably closed field, Tag 0363). The source's reduction to `X` affine of finite type through Tags 0EZR and 0EZT is replaced by this: its limit argument is the one inside Tag 03Q9.”.

> Let `k` be a separably closed field and consider a cartesian square of schemes
>
> ```
> X <--h-- Y
> |f       |e
> Spec k <--g-- T
> ```
>
> with `g` quasi-compact and quasi-separated. Then the canonical base change map
> `f⁻¹ g_* F ⟶ h_* e⁻¹ F` is an isomorphism for every sheaf of sets `F` on the small étale site of
> `T`. Nothing is assumed of `X`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_isSepClosed_of_quasiCompact
    (sq : IsPullback h e f g) [QuasiCompact g] [QuasiSeparated g]
    (F : Sheaf (smallEtaleTopology T) (Type (u + 1))) :
    IsIso ((smallEtaleSetBaseChange.{u, 0} e h g f sq.w.symm).app F)
```

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isSepClosed_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeSepClosedFieldUnconditional.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeSepClosedFieldUnconditional.lean#L96). The attribute's comment: “the case of `X` of finite type over the separably closed field, stated for `X` locally of finite type. What is proved unconditionally is the covering condition of Tag 0EZX: an affine open of an étale `X`-scheme is Noetherian, hence locally connected by Tag 04MF, so the connected component of any of its points is an open quasi-compact subscheme, and over a separably closed field a connected scheme is geometrically connected by Tag 0363; flatness of `f` is automatic over a field. The chain of identifications of sections on which Tag 0EZX feeds is supplied too, by `local_baseChange_compatible`, exactly as in Tags 0EZX, 0EYS and 0EZZ. What is not asserted is the source's reduction of the general case to this one, which takes two steps. Working locally on `X` to reduce to an affine `X` is Tag 0EZR clause (1), and that clause is now proved, as `isIso_smallEtaleSetsBaseChange_of_isIso_local`; but it is proved about `smallEtaleSetsBaseChange`, a second set-valued base change map built in `BaseChangeHigher/OrdinaryLocality.lean` from the composition isomorphisms of direct images, which no result identifies with the `smallEtaleSetBaseChange` of this square. The second step writes an affine `X` as a cofiltered limit of affine finite-type `Spec k`-schemes and uses the compatibility of the base change map with such limits, which is Tag 0EZT part (1); the two 0EZT carriers give the cartesian square on the limits and part (2), for abelian coefficients and the higher direct images, and part (1) -- sheaves of sets and the underived direct image, the form this map takes -- has no carrier, nor has the set-valued colimit assertion of Tag 0EYM it would be built from. The hypothesis that `f` be locally of finite type is therefore still needed, and is more than the source's statement assumes.”.

> **Stacks Project, Tag 0EZY**, in the case of `X` locally of finite type over the separably
> closed field. Let `k` be a separably closed field and let `f : X ⟶ Spec k` be locally of finite
> type. Then in a cartesian square over `f` the canonical base change map `f⁻¹ g_* F ⟶ h_* e⁻¹ F`
> is an isomorphism for every sheaf of sets `F` on the small étale site of `T`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_isSepClosed_locallyOfFiniteType (k : Type u) [Field k]
    [IsSepClosed k] (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] (h : Y ⟶ X) (e : Y ⟶ T)
    (g : T ⟶ Spec (.of k)) (sq : IsPullback h e f g)
    (F : Sheaf (smallEtaleTopology T) (Type (max (u + 1) v))) :
    IsIso ((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F)
```

## Tag 0EZZ, a lemma

[Tag 0EZZ](https://stacks.math.columbia.edu/tag/0EZZ) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isOpenMap_connectedFibreOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean, line 902](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean#L902). The attribute's comment: “no residual hypothesis. The source's proof is omitted with the hint that the hypotheses imply the covering condition of Tag 0EZX; that implication is what is proved here, and the chain of identifications of sections which Tag 0EZX then feeds on is `local_baseChange_compatible`, exactly as for Tag 0EZX above. Hypothesis (3) of the source is read as the existence of an isomorphism of the étale `X`-scheme with a finite coproduct of open subschemes of `X` over `X`; the parenthetical examples in (3) and (4), which the source derives from Tag 09Z9, are not asserted.”.

> Let `f : X ⟶ S` be flat and open, with separably closed residue fields on `S`, with every
> affine étale `X`-scheme a finite disjoint union of open subschemes of `X`, and with every
> nonempty open of a fibre of `f` connected. Then in a cartesian square over `f` the canonical base
> change map `f⁻¹ g_* F ⟶ h_* e⁻¹ F` is an isomorphism for every sheaf of sets `F` on the small
> étale site of `T`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_isOpenMap_connectedFibreOpens (f : X ⟶ S) (h : Y ⟶ X)
    (e : Y ⟶ T) (g : T ⟶ S) (sq : IsPullback h e f g) [Flat f] (hopen : IsOpenMap f)
    (hsep : ∀ s : S, IsSepClosed (S.residueField s))
    (hsplit : ∀ U : X.Etale, IsAffine U.left →
      ∃ (n : ℕ) (V : Fin n → Scheme.{u}) (j : ∀ a, V a ⟶ X)
        (_ : ∀ a, IsOpenImmersion (j a)) (i : U.left ≅ ∐ V),
        i.hom ≫ Sigma.desc j = U.hom)
    (hconn : ∀ s : S, ∀ W : (f.fiber s).Opens, W ≠ ⊥ → ConnectedSpace W.toScheme)
    (F : Sheaf (smallEtaleTopology T) (Type (max (u + 1) v))) :
    IsIso ((smallEtaleSetBaseChange.{u, v} e h g f sq.w.symm).app F)
```

## Tag 0EYR, a lemma

[Tag 0EYR](https://stacks.math.columbia.edu/tag/0EYR) in the Stacks Project.

**`Stacks.EtaleCohomology.preservesLimitsOfShape_smallEtaleInverseImage_of_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeUnconditional.lean#L107). The attribute's comment: “no residual hypothesis. Both inputs of the source's proof are supplied: the covering of the small étale site by objects with a flat quasi-compact factorization with geometrically connected fibres, which is Tag 0EY5 and is `hasEnoughObjects_hasFlatConnectedFactorization`; and the bijectivity of the canonical comparison `G(V) ⟶ (f⁻¹G)(U)` over such an object, which is Tag 0A3H in the localized form of the source's own argument and is `smallEtaleSectionsComparisonIsIso`, proved from Tag 0EZK and the small-étale instance of Tag 03EF. The globalization from sections to sheaves is Tag 0H6Y.”.

> For a morphism of schemes which is flat, locally of finite presentation and has
> geometrically reduced fibres, the inverse image functor on sheaves of sets of the small étale
> sites commutes with products.

```lean
theorem preservesLimitsOfShape_smallEtaleInverseImage_of_geometricallyReduced
    [Flat f] [LocallyOfFinitePresentation f] [GeometricallyReduced f]
    (I : Type w) :
    PreservesLimitsOfShape (Discrete I) (smallEtaleInverseImage.{u, max v w} f)
```

## Tag 0F00, a lemma

[Tag 0F00](https://stacks.math.columbia.edu/tag/0F00) in the Stacks Project.

**`Stacks.EtaleCohomology.isPullback_strictHenselizationPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationBaseChangeSections.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationBaseChangeSections.lean#L131). The attribute's comment: “the identity `Spec(O^sh_{X,x̄}) ×_X Y = Spec(O^sh_{S,f(x̄)}) ×_S T`-base-change of `Spec(O^sh_{X,x̄}) ⟶ Spec(O^sh_{S,f(x̄)})` of the source's last sentence, and nothing else. The tag's conclusion `f⁻¹ g_* F = h_* e⁻¹ F` is NOT asserted here or in `globalSectionsIso_strictHenselizationPullback` below: the source obtains it from this identification together with Tag 03PU and Tag 03Q9, and Tag 03Q9 for sheaves of sets is not available in the library (the only form of it present is restricted to a base which is already the spectrum of a strictly henselian local ring).”.

> **Stacks Project, Tag 0F00**, the base change step of its proof. In a cartesian square with
> `h : Y ⟶ X`, `e : Y ⟶ T` and `g : T ⟶ S`, the canonical morphism
> `Spec(O^sh_{X,x̄}) ×_X Y ⟶ Spec(O^sh_{S,f(x̄)}) ×_S T` is a base change of the morphism of
> strict henselizations `Spec(O^sh_{X,x̄}) ⟶ Spec(O^sh_{S,f(x̄)})`.

```lean
theorem isPullback_strictHenselizationPullbackMap (sq : IsPullback h e f g) :
    IsPullback (pullback.fst (strictHenselizationToBase B X hX x) h)
      (strictHenselizationPullbackMap B hX hS f x sq)
      (strictHenselizationSquareMap B hX hS f x)
      (pullback.fst (strictHenselizationToBase B S hS (x.map f)) g)
```

**`Stacks.EtaleCohomology.globalSectionsIso_strictHenselizationPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationBaseChangeSections.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationBaseChangeSections.lean#L162). The attribute's comment: “the application of Tag 0A3H to the morphism `Spec(O^sh_{X,x̄}) ×_X Y ⟶ Spec(O^sh_{S,f(x̄)}) ×_S T` with which the source's proof concludes, and nothing else. The tag's conclusion `f⁻¹ g_* F = h_* e⁻¹ F` is NOT asserted: the source reads the two sides of this identification as the stalks at `x̄` of `f⁻¹ g_* F` and of `h_* e⁻¹ F` by Tag 03Q9 and concludes by Tag 03PU, and Tag 03Q9 for sheaves of sets is absent from the library. Flatness of the morphism of strict henselizations, which Tag 0A3H needs and the source leaves implicit in the flatness of `f`, is the declared hypothesis `hflat`.”.

> **Stacks Project, Tag 0F00**, the application of Tag 0A3H in its proof. If the morphism of
> strict henselizations at a geometric point `x̄` of `X` is flat with geometrically connected
> fibres, then in a cartesian square the global sections of a sheaf of sets on the small étale
> site of `Spec(O^sh_{S,f(x̄)}) ×_S T` are the global sections of its inverse image on the small
> étale site of `Spec(O^sh_{X,x̄}) ×_X Y`, naturally in the sheaf.

```lean
def globalSectionsIso_strictHenselizationPullback (sq : IsPullback h e f g)
    (hflat : Flat (strictHenselizationSquareMap B hX hS f x))
    (hconn : GeometricallyConnected (strictHenselizationSquareMap B hX hS f x)) :
    Sheaf.Γ (smallEtaleTopology (strictHenselizationPullback B hS (x.map f) g))
        (Type (max (u + 1) v)) ≅
      smallEtaleInverseImage.{u, v} (strictHenselizationPullbackMap B hX hS f x sq) ⋙
        Sheaf.Γ (smallEtaleTopology (strictHenselizationPullback B hX x h))
          (Type (max (u + 1) v))
```

**`Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_geometricallyConnected_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationBaseChangeUnconditional.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationBaseChangeUnconditional.lean#L296).

> Let `f : X ⟶ S` be flat, and suppose that for every geometric
> point `x̄` of `X` the morphism `Spec(O^sh_{X,x̄}) ⟶ Spec(O^sh_{S,f(x̄)})` of strict henselizations
> has geometrically connected fibres. Then for every cartesian square
>
> ```
> Y --h--> X
> |e       |f
> v        v
> T --g--> S
> ```
>
> with `g` quasi-compact and quasi-separated, the canonical base change map
> `f⁻¹ g_* F ⟶ h_* e⁻¹ F` is an isomorphism for every sheaf of sets `F` on `T_étale`.
>
> The strict henselizations are those constructed inside a big étale site `B` containing `X` and
> `S`; the base change map is `Stacks.EtaleCohomology.smallEtaleSetBaseChange`, and the conclusion
> is that it is an isomorphism of functors, that is, at every `F`.

```lean
theorem isIso_smallEtaleSetBaseChange_of_geometricallyConnected_strictHenselization [Flat f]
    (hconn : ∀ x : GeometricPoint X,
      GeometricallyConnected (strictHenselizationSquareMap B hX hS f x))
    (sq : IsPullback h e f g) [QuasiCompact g] [QuasiSeparated g] :
    IsIso (smallEtaleSetBaseChange.{u, 0} e h g f sq.w.symm)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.87, Tag 0EZW](https://stacks.math.columbia.edu/tag/0EZW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
