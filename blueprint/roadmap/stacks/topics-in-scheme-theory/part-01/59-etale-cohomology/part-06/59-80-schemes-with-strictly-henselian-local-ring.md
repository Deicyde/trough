---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleZariskiSheafHAddEquiv, Stacks.EtaleCohomology.StrictlyHenselian.subsingleton_H_of_degreeOne_kernel_eq_zero, AlgebraicGeometry.subsingleton_etaleCohomology_of_closed_points, AlgebraicGeometry.subsingleton_etaleCohomology_of_closed_points', AlgebraicGeometry.exists_coproduct_open_immersions, AlgebraicGeometry.stalk_strictlyHenselian, Stacks.EtaleCohomology.isZero_rightDerived_smallEtalePushforward_constantSheaf, AlgebraicGeometry.exists_finite_coproduct_open_immersions
statement: formalized
proof: formalized
---

# 59.80 Schemes with strictly henselian local rings

Section 59.80 of the Stacks Project, [Tag 0EZN](https://stacks.math.columbia.edu/tag/0EZN). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09AX, a lemma

[Tag 09AX](https://stacks.math.columbia.edu/tag/09AX) in the Stacks Project.

**`AlgebraicGeometry.etaleZariskiSheafHAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/EtaleZariskiCohomology.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/EtaleZariskiCohomology.lean#L194).

> Let `S` be a scheme all of whose local rings are strictly henselian. Then
> for every abelian sheaf `F` on the small étale site of `S` and every degree `p`, étale cohomology
> `H^p(S_étale, F)` agrees with Zariski cohomology `H^p(S_Zariski, ε_* F)` of its restriction to
> the open subschemes of `S`.

```lean
public def etaleZariskiSheafHAddEquiv
    (hlocal : ∀ x : S, StrictlyHenselianLocalRing ↥(S.presheaf.stalk x))
    (F : Sheaf (Scheme.smallEtaleTopology S) AddCommGrpCat.{u + 1}) (p : ℕ) :
    Sheaf.H.{w, u + 1} F p ≃+ Sheaf.H.{w, u + 1} ((zariskiPushforward S).obj F) p
```

## Tag 0GY0, a lemma

[Tag 0GY0](https://stacks.math.columbia.edu/tag/0GY0) in the Stacks Project.

**`Stacks.EtaleCohomology.StrictlyHenselian.subsingleton_H_of_degreeOne_kernel_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianSpectrumVanishing.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianSpectrumVanishing.lean#L419).

> Let `R` be a ring all of whose local rings are strictly henselian and let `F` be an abelian
> sheaf on the small étale site of `Spec R`. If for all `f, g ∈ R` the kernel of
>
> `H¹(D(f + g), F) ⟶ H¹(D(f(f + g)), F) ⊕ H¹(D(g(f + g)), F)`
>
> is zero, then `H^q(Spec R, F) = 0` for every `q > 0`.

```lean
public theorem subsingleton_H_of_degreeOne_kernel_eq_zero
    (hlocal : ∀ x : Spec (CommRingCat.of R), StrictlyHenselianLocalRing
      ↥((Spec (CommRingCat.of R)).presheaf.stalk x))
    (F : Sheaf (MayerVietoris.topology (Spec (CommRingCat.of R))) AddCommGrpCat.{u + 1})
    (h₁ : ∀ f g : R, ∀ y : (opensCohomology F 1).obj (op (PrimeSpectrum.basicOpen (f + g))),
      (opensCohomology F 1).map
          (homOfLE (PrimeSpectrum.basicOpen_mul_le_right f (f + g))).op y = 0 →
      (opensCohomology F 1).map
          (homOfLE (PrimeSpectrum.basicOpen_mul_le_right g (f + g))).op y = 0 → y = 0)
    (q : ℕ) (hq : 0 < q) :
    Subsingleton (Sheaf.H.{u + 1} F q)
```

## Tag 09AY, a lemma

[Tag 09AY](https://stacks.math.columbia.edu/tag/09AY) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_etaleCohomology_of_closed_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointsVanishing.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointsVanishing.lean#L200).

> **Positive-degree étale cohomology vanishes on an affine scheme all of whose points are
> closed and all of whose residue fields are separably closed.**

```lean
public theorem subsingleton_etaleCohomology_of_closed_points
    (hclosed : ∀ x : S, IsClosed ({x} : Set S))
    (hsep : ∀ x : S, IsSepClosed ↥(S.residueField x))
    [HasSheafify (Scheme.smallEtaleTopology S) AddCommGrpCat.{max u v}]
    [(Scheme.smallEtaleTopology S).WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    [HasExt.{w} (Sheaf (Scheme.smallEtaleTopology S) AddCommGrpCat.{max u v})]
    (F : Sheaf (Scheme.smallEtaleTopology S) AddCommGrpCat.{max u v}) (q : ℕ) (hq : 0 < q) :
    Subsingleton (Sheaf.H.{w, max u v} F q)
```

**`AlgebraicGeometry.subsingleton_etaleCohomology_of_closed_points'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointsVanishing.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointsVanishing.lean#L216). The attribute's comment: “at the coefficient universe of the small étale site”.

> **Positive-degree étale cohomology vanishes on an affine scheme all of whose points are
> closed and all of whose residue fields are separably closed**, for abelian sheaves at the
> coefficient universe `u + 1` of the small étale site itself.

```lean
public theorem subsingleton_etaleCohomology_of_closed_points'
    (hclosed : ∀ x : S, IsClosed ({x} : Set S))
    (hsep : ∀ x : S, IsSepClosed ↥(S.residueField x))
    [HasExt.{w} (Sheaf (Scheme.smallEtaleTopology S) AddCommGrpCat.{u + 1})]
    (F : Sheaf (Scheme.smallEtaleTopology S) AddCommGrpCat.{u + 1}) (q : ℕ) (hq : 0 < q) :
    Subsingleton (Sheaf.H.{w, u + 1} F q)
```

## Tag 09Z9, a lemma

[Tag 09Z9](https://stacks.math.columbia.edu/tag/09Z9) in the Stacks Project.

**`AlgebraicGeometry.exists_coproduct_open_immersions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/NormalSepClosedFunctionField.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/NormalSepClosedFunctionField.lean#L216). The attribute's comment: “part (1)”.

> A separated étale morphism to an integral normal scheme with separably closed function field
> is a disjoint union of open immersions.

```lean
theorem exists_coproduct_open_immersions
    (X : Scheme.{u}) [IsIntegral X] [IsNormal X]
    [IsSepClosed X.functionField]
    (U : Scheme.{u}) (f : U ⟶ X) [Etale f] [IsSeparated f] :
    ∃ (I : Type u) (V : I → Scheme.{u}) (j : ∀ i, V i ⟶ X)
      (_ : ∀ i, IsOpenImmersion (j i)) (e : U ≅ ∐ V),
      e.hom ≫ Sigma.desc j = f
```

**`AlgebraicGeometry.stalk_strictlyHenselian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/NormalSepClosedFunctionField.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/NormalSepClosedFunctionField.lean#L260). The attribute's comment: “part (2)”.

> Every local ring of an integral normal scheme with separably closed function field is
> strictly henselian.

```lean
instance stalk_strictlyHenselian
    (X : Scheme.{u}) [IsIntegral X] [IsNormal X]
    [IsSepClosed X.functionField] (x : X) :
    _root_.StrictlyHenselianLocalRing (X.presheaf.stalk x)
```

## Tag 0EZP, a lemma

[Tag 0EZP](https://stacks.math.columbia.edu/tag/0EZP) in the Stacks Project.

**`Stacks.EtaleCohomology.isZero_rightDerived_smallEtalePushforward_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NormalSepClosedConstantDirectImage.lean, line 804](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NormalSepClosedConstantDirectImage.lean#L804).

> **Stacks Project, Tag 0EZP.** Higher direct images of a constant abelian
> étale sheaf vanish when the source is integral, normal, and has separably
> closed function field.

```lean
public theorem isZero_rightDerived_smallEtalePushforward_constantSheaf
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsIntegral X] [IsNormal X] [IsSepClosed X.functionField]
    [HasSheafify X.smallEtaleTopology AddCommGrpCat.{w}]
    [HasSheafify Y.smallEtaleTopology AddCommGrpCat.{w}]
    [HasInjectiveResolutions (Sheaf X.smallEtaleTopology AddCommGrpCat.{w})]
    (M : AddCommGrpCat.{w}) (q : ℕ) (hq : 0 < q) :
    IsZero ((((smallEtaleBaseChange f).sheafPushforwardContinuous
      AddCommGrpCat.{w} Y.smallEtaleTopology X.smallEtaleTopology).rightDerived q).obj
        ((constantSheaf X.smallEtaleTopology AddCommGrpCat.{w}).obj M))
```

## Tag 09ZA, a lemma

[Tag 09ZA](https://stacks.math.columbia.edu/tag/09ZA) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_coproduct_open_immersions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean#L284). The attribute's comment: “finite disjoint union”.

> **Stacks Project, Tag 09ZA, first assertion.** An affine etale scheme over a closed
> subscheme of an integral normal affine scheme with separably closed function field is a finite
> disjoint union of open subschemes of the closed subscheme.

```lean
theorem exists_finite_coproduct_open_immersions
    (X : Scheme.{u}) [IsAffine X] [IsIntegral X] [IsNormal X]
    [IsSepClosed X.functionField]
    (Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i]
    (V : Scheme.{u}) [IsAffine V] (f : V ⟶ Z) [Etale f] :
    ∃ (n : ℕ) (U : Fin n → Scheme.{u}) (j : ∀ a, U a ⟶ Z)
      (_ : ∀ a, IsOpenImmersion (j a)) (e : V ≅ ∐ U),
      e.hom ≫ Sigma.desc j = f
```

**`AlgebraicGeometry.exists_section_of_surjective_finite_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean#L457). The attribute's comment: “section”.

> **Stacks Project, Tag 09ZA, final assertion.** A surjective finite etale morphism over a
> closed subscheme of an integral normal affine scheme with separably closed function field has a
> section.

```lean
theorem exists_section_of_surjective_finite_etale
    (X : Scheme.{u}) [IsAffine X] [IsIntegral X] [IsNormal X]
    [IsSepClosed X.functionField]
    (Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i]
    (V : Scheme.{u}) [IsAffine V] (f : V ⟶ Z)
    [Surjective f] [IsFinite f] [Etale f] :
    ∃ s : Z ⟶ V, s ≫ f = 𝟙 Z
```

## Tag 09ZB, a lemma

[Tag 09ZB](https://stacks.math.columbia.edu/tag/09ZB) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_smallEtaleH1_constantSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean#L899).

> **Stacks Project, Tag 09ZB.** The first cohomology of the small étale site of a closed
> subscheme of an integral normal affine scheme with separably closed function field, with
> coefficients in a finite constant abelian group, vanishes.
>
> This is `AlgebraicGeometry.subsingleton_smallEtaleH1_constantSheaf` with its descent hypothesis
> discharged: a torsor under the constant sheaf is finite locally constant, hence representable by
> a scheme finite étale over `Z` by the unconditional
> `Stacks.EtaleCohomology.isFiniteLocallyConstant_iff_finiteEtaleRepresentable`, and that scheme
> has a section because `Z` is a closed subscheme of a normal integral affine scheme with
> separably closed function field.

```lean
theorem subsingleton_smallEtaleH1_constantSheaf'
    (B : BigEtaleSite.{u})
    (X : Scheme.{u}) [IsAffine X] [IsIntegral X] [IsNormal X]
    [IsSepClosed X.functionField]
    (Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i] (hZ : B.Contains Z)
    (M : AddCommGrpCat.{u + 1}) [Finite M]
    [HasSheafify (SmallEtale.topology B Z hZ) AddCommGrpCat.{u + 1}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B Z hZ) AddCommGrpCat.{u + 1})] :
    Subsingleton (Sheaf.H ((constantSheaf (SmallEtale.topology B Z hZ)
      AddCommGrpCat.{u + 1}).obj M) 1)
```

## Tag 09ZC, a lemma

[Tag 09ZC](https://stacks.math.columbia.edu/tag/09ZC) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_smallEtaleH_constantSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean, line 1086](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ClosedSubschemeOfNormal.lean#L1086).

> **Stacks Project, Tag 09ZC.** The étale cohomology of a closed subscheme of a normal
> integral affine scheme with separably closed function field, with coefficients in a finite
> constant abelian group, vanishes in every positive degree.
>
> This is `AlgebraicGeometry.subsingleton_smallEtaleH_constantSheaf` with its descent hypothesis
> discharged: the degree-one input is the unconditional
> `AlgebraicGeometry.subsingleton_smallEtaleH1_constantSheaf'` on the basic opens of `Z`, and the
> passage to all positive degrees is the vanishing criterion of Stacks 0GY0.

```lean
theorem subsingleton_smallEtaleH_constantSheaf'
    (B : BigEtaleSite.{u})
    (X : Scheme.{u}) [IsAffine X] [IsIntegral X] [IsNormal X]
    [IsSepClosed X.functionField]
    (Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i] (hZ : B.Contains Z)
    (M : AddCommGrpCat.{u + 1}) [Finite M]
    [HasSheafify (SmallEtale.topology B Z hZ) AddCommGrpCat.{u + 1}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B Z hZ) AddCommGrpCat.{u + 1})]
    (q : ℕ) (hq : 0 < q) :
    Subsingleton (Sheaf.H ((constantSheaf (SmallEtale.topology B Z hZ)
      AddCommGrpCat.{u + 1}).obj M) q)
```

## Tag 09ZD, a lemma

[Tag 09ZD](https://stacks.math.columbia.edu/tag/09ZD) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.exists_isIntegralHom_surjective_forall_subsingleton_H`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/IntegralCoverVanishing.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/AffineAnalogRegistration.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/AffineAnalogRegistration.lean#L30) (StacksFrontier): “part (1): an affine scheme has an integral surjective cover X' → X such that every closed subscheme Z' of X' has H^q\_ét(Z', M) = 0 for every finite abelian group M and every q ≥ 1”.
- [`Stacks.EtaleCohomology.exists_isFinite_surjective_restriction_constantSheaf_eq_zero`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/FiniteCoverKilling.lean#L182), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/AffineAnalogRegistration.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/AffineAnalogProper/AffineAnalogRegistration.lean#L34) (StacksFrontier): “part (2): for a closed subscheme Z of an affine X, a finite abelian group M, q ≥ 1 and ξ ∈ H^q\_ét(Z, M), some finite surjective X' → X of finite presentation makes ξ pull back to zero in H^q\_ét(X' ×\_X Z, M)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.80, Tag 0EZN](https://stacks.math.columbia.edu/tag/0EZN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
