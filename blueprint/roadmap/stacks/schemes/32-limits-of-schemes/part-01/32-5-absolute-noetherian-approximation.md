---
declaration: section
origin: cited
lean: Stacks.FiniteTypeOpenModel.exists_openModel, Stacks.FiniteTypeOpenModel.openModel_directed, Stacks.FiniteTypeOpenModel.openModelCocone_isColimit, AlgebraicGeometry.isOpenImmersion_iSup_basicOpen_comp_SpecMap_of_isPullback, AlgebraicGeometry.finiteTypeApproximationOfIsLimit, AlgebraicGeometry.Scheme.exists_isLimit_affine_locallyOfFiniteType, AlgebraicGeometry.exists_isLimit_finiteType, AlgebraicGeometry.LimitFPObjectDescent.finiteTypeSchemeApproximation
statement: formalized
proof: formalized
---

# 32.5 Absolute Noetherian Approximation

Section 32.5 of the Stacks Project, [Tag 01Z1](https://stacks.math.columbia.edu/tag/01Z1). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01Z7, a lemma

[Tag 01Z7](https://stacks.math.columbia.edu/tag/01Z7) in the Stacks Project.

**`Stacks.FiniteTypeOpenModel.exists_openModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeOpenModel.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeOpenModel.lean#L521). The attribute's comment: “existence of a finite-type open model”. References: EGA II (5.1.9), “base Spec ℤ, affine”.

> An open immersion of a finite-type scheme into an affine scheme
> descends to a finite-type subalgebra.

```lean
public theorem exists_openModel {R : Type u} [CommRing R] {W : Scheme.{u}}
    (f : W ⟶ Spec (.of R))
    [LocallyOfFiniteType (terminal.from W)]
    [QuasiCompact (terminal.from W)] [IsOpenImmersion f] :
    ∃ A : Subalgebra ℤ R, IsOpenModel f A
```

**`Stacks.FiniteTypeOpenModel.openModel_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeOpenModel.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeOpenModel.lean#L530). The attribute's comment: “directedness of the finite-type open models”.

> Finite-type subalgebras admitting the open model are directed by inclusion.

```lean
public theorem openModel_directed {R : Type u} [CommRing R] {W : Scheme.{u}}
    (f : W ⟶ Spec (.of R))
    [LocallyOfFiniteType (terminal.from W)]
    [QuasiCompact (terminal.from W)] [IsOpenImmersion f] :
    ∀ A B : Subalgebra ℤ R, IsOpenModel f A → IsOpenModel f B →
      ∃ C : Subalgebra ℤ R, IsOpenModel f C ∧ A ≤ C ∧ B ≤ C
```

**`Stacks.FiniteTypeOpenModel.openModelCocone_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeOpenModel.lean, line 548](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeOpenModel.lean#L548). The attribute's comment: “colimit of the finite-type open models”.

> The canonical cocone of finite-type open models is a colimit cocone.

```lean
public theorem openModelCocone_isColimit {R : Type u} [CommRing R] {W : Scheme.{u}}
    (f : W ⟶ Spec (.of R))
    [LocallyOfFiniteType (terminal.from W)]
    [QuasiCompact (terminal.from W)] [IsOpenImmersion f] :
    Nonempty (IsColimit (openModelCocone f))
```

## Tag 01Z9, a lemma

[Tag 01Z9](https://stacks.math.columbia.edu/tag/01Z9) in the Stacks Project.

**`AlgebraicGeometry.isOpenImmersion_iSup_basicOpen_comp_SpecMap_of_isPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NoetherianApproximation/FibreProductOpenImmersion.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/NoetherianApproximation/FibreProductOpenImmersion.lean#L104).

> In a cartesian square of rings, a finite union of standard opens which descend from the
> other side of the square and on which that side becomes an isomorphism maps by an open
> immersion to the spectrum of the remaining corner.

```lean
lemma isOpenImmersion_iSup_basicOpen_comp_SpecMap_of_isPullback
    {B R B' R' : Type u} [CommRing B] [CommRing R] [CommRing B'] [CommRing R']
    (s : B →+* R) (p : B' →+* B) (r : B' →+* R') (t : R' →+* R)
    (hcart : IsPullback (CommRingCat.ofHom p) (CommRingCat.ofHom r)
      (CommRingCat.ofHom s) (CommRingCat.ofHom t))
    {n : ℕ} (f : Fin n → R') (g : Fin n → B)
    (hfg : ∀ i, t (f i) = s (g i))
    (hloc : ∀ i, Function.Bijective (Localization.awayMap s (g i))) :
    IsOpenImmersion
      ((⨆ i, PrimeSpectrum.basicOpen (f i) : (Spec (.of R')).Opens).ι ≫
        Spec.map (CommRingCat.ofHom r))
```

## Tag 07RN, a lemma

[Tag 07RN](https://stacks.math.columbia.edu/tag/07RN) in the Stacks Project.

**`AlgebraicGeometry.finiteTypeApproximationOfIsLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitApproxClose/Induction.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitApproxClose/Induction.lean#L64).

> **Stacks Project, Tag 07RN**, as data: the extended system itself.
> It is `AlgebraicGeometry.exists_finiteTypeApproximation` together with the choice of a witness,
> so it is noncomputable; the construction is propositional throughout, every stage of it being
> chosen from an existential statement.

```lean
noncomputable def finiteTypeApproximationOfIsLimit {I : Type u} [Preorder I] [Nonempty I]
    [IsDirected I (· ≤ ·)] (D : Iᵒᵈ ⥤ Scheme.{u})
    [∀ {i j : Iᵒᵈ} (v : i ⟶ j), IsAffineHom (D.map v)]
    [∀ i, LocallyOfFiniteType (terminal.from (D.obj i))]
    [∀ i, QuasiCompact (terminal.from (D.obj i))]
    (S : Scheme.{u}) [CompactSpace S] [QuasiSeparatedSpace S] (U : S.Opens)
    [CompactSpace (U : Scheme.{u})]
    (p : (Functor.const Iᵒᵈ).obj (U : Scheme.{u}) ⟶ D)
    (hp : IsLimit (Cone.mk (U : Scheme.{u}) p)) :
    Scheme.FiniteTypeApproximation D S U p
```

## Tag 01ZA, a proposition

[Tag 01ZA](https://stacks.math.columbia.edu/tag/01ZA) in the Stacks Project.

**`AlgebraicGeometry.Scheme.exists_isLimit_affine_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeApproximation/Absolute.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/FiniteTypeApproximation/Absolute.lean#L62).

> **Absolute Noetherian approximation.**  A quasi-compact and quasi-separated scheme `S` is
> the inverse limit of an inverse system of schemes over a directed set whose transition
> morphisms are affine and whose every stage is of finite type over the integers.

```lean
theorem exists_isLimit_affine_locallyOfFiniteType (S : Scheme.{u}) [CompactSpace S]
    [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (F : Iᵒᵈ ⥤ Scheme.{u}) (c : (Functor.const Iᵒᵈ).obj S ⟶ F),
      (∀ {i j : Iᵒᵈ} (f : i ⟶ j), IsAffineHom (F.map f)) ∧
      (∀ i, LocallyOfFiniteType (terminal.from (F.obj i))) ∧
      (∀ i, QuasiCompact (terminal.from (F.obj i))) ∧
      Nonempty (IsLimit (Cone.mk S c))
```

**`AlgebraicGeometry.exists_isLimit_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/NoetherianApproximation/Absolute.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/NoetherianApproximation/Absolute.lean#L79).

> **Stacks Project, Tag 01ZA.** A quasi-compact and quasi-separated scheme is the inverse
> limit of a directed system of schemes of finite type over the integers with affine transition
> morphisms.

```lean
public theorem exists_isLimit_finiteType (S : Scheme.{u}) [CompactSpace S]
    [QuasiSeparatedSpace S] :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
      (D : Iᵒᵖ ⥤ Scheme.{u}) (c : Cone D),
      (∀ {i j : Iᵒᵖ} (v : i ⟶ j), IsAffineHom (D.map v)) ∧
      (∀ i, LocallyOfFiniteType (terminal.from (D.obj i))) ∧
      (∀ i, QuasiCompact (terminal.from (D.obj i))) ∧
      Nonempty (IsLimit c) ∧ c.pt = S
```

Declarations registered for the tag:

- [`AlgebraicGeometry.LimitFPObjectDescent.finiteTypeSchemeApproximation`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/LimitFPObjectDescent/Approximation.lean#L197), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Approximation/Basic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Approximation/Basic.lean#L43) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.5, Tag 01Z1](https://stacks.math.columbia.edu/tag/01Z1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
