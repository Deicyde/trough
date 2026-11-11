---
declaration: section
origin: cited
lean: AlgebraicGeometry.smooth_of_surjective_of_isNormal, AlgebraicGeometry.exists_chain_isInseparableDegreePrime, AlgebraicGeometry.existsUnique_iso_frobeniusTwist_of_inseparable_degree_prime, AlgebraicGeometry.existsUnique_nat_existsUnique_iso_nFoldFrobeniusTwist, AlgebraicGeometry.smooth_of_isPurelyInseparable_residueFieldMap, AlgebraicGeometry.isIso_globalSections_of_isPurelyInseparable_residueFieldMap, AlgebraicGeometry.genus_eq_of_isPurelyInseparable_residueFieldMap, Stacks.Curves.InseparableGenus.exists_charThree_notCube
statement: formalized
proof: formalized
---

# 53.13 Inseparable maps

Section 53.13 of the Stacks Project, [Tag 0CCV](https://stacks.math.columbia.edu/tag/0CCV). 10 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CCW, a lemma

[Tag 0CCW](https://stacks.math.columbia.edu/tag/0CCW) in the Stacks Project.

**`AlgebraicGeometry.smooth_of_surjective_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FlatMorphism.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/FlatMorphism.lean#L105).

> **Stacks Project, Tag 0CCW.** A normal curve over a field is smooth if it is surjectively
> dominated by a smooth curve over that field. A surjection onto a curve has nontrivial range, so
> it is flat by `AlgebraicGeometry.isFlat_of_nonconstant_of_isNormal`, and smoothness descends
> along a flat surjection.

```lean
theorem smooth_of_surjective_of_isNormal
    {k : Type u} [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY]
    (f : X ⟶ Y) (_hf : f ≫ pY = pX)
    [Surjective f] [Smooth pX] [IsNormal Y] :
    Smooth pY
```

## Tag 0CCX, a lemma

[Tag 0CCX](https://stacks.math.columbia.edu/tag/0CCX) in the Stacks Project.

**`AlgebraicGeometry.exists_chain_isInseparableDegreePrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableFactorizationChain.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableFactorizationChain.lean#L724). The attribute's comment: “the factorization into steps of degree p”.

> **Stacks Project, Tag 0CCX.** Let `k` be a field of characteristic `p`. A nonconstant
> morphism `f` of proper nonsingular curves over `k` whose extension of function fields is purely
> inseparable factors as a chain of proper nonsingular curves over `k` in which every step has
> degree `p` and induces an inseparable extension of function fields.

```lean
theorem exists_chain_isInseparableDegreePrime (p : ℕ) [Fact p.Prime] [CharP k p] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [IsProper pX] [IsProper pY]
    (hXreg : IsRegular X) (hYreg : IsRegular Y)
    (f : Over.mk pX ⟶ Over.mk pY) [IsDominant f.left]
    (hpure : letI : Algebra Y.functionField X.functionField :=
        (functionFieldMap f.left).toAlgebra
      IsPurelyInseparable Y.functionField X.functionField) :
    ∃ (n : ℕ) (Z : Fin (n + 1) → ProperNonsingularCurve k)
      (g : ∀ i : Fin n, (Z i.castSucc).obj ⟶ (Z i.succ).obj)
      (w : ∀ i : Fin (n + 1), (Z i).obj ⟶ Over.mk pY)
      (e : Over.mk pX ⟶ (Z 0).obj),
      IsIso e ∧ IsIso (w (Fin.last n)) ∧ e ≫ w 0 = f ∧
      (∀ i : Fin n, g i ≫ w i.succ = w i.castSucc) ∧
      ∀ i : Fin n, ∃ hdom : IsDominant (g i).left,
        letI : IsDominant (g i).left := hdom
        letI : Algebra (Z i.succ).obj.left.functionField
            (Z i.castSucc).obj.left.functionField := (functionFieldMap (g i).left).toAlgebra
        Module.finrank (Z i.succ).obj.left.functionField
            (Z i.castSucc).obj.left.functionField = p ∧
          ¬ Algebra.IsSeparable (Z i.succ).obj.left.functionField
            (Z i.castSucc).obj.left.functionField ∧
          (g i).left.residueDegree (genericPoint (Z i.castSucc).obj.left) = p
```

## Tag 0CCY, a lemma

[Tag 0CCY](https://stacks.math.columbia.edu/tag/0CCY) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_iso_frobeniusTwist_of_inseparable_degree_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusFactorization.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusFactorization.lean#L349).

> **Stacks Project, Tag 0CCY.** A nonconstant morphism of proper nonsingular curves over a
> field of characteristic `p`, with smooth source, whose extension of function fields is
> inseparable of degree `p`, is the relative Frobenius up to a unique isomorphism of its target
> with the Frobenius twist of its source.

```lean
theorem existsUnique_iso_frobeniusTwist_of_inseparable_degree_prime
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    {X Y : Scheme.{u}} (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [IsProper pX] [IsProper pY]
    (_hXreg : IsRegular X) (hYreg : IsRegular Y)
    [Smooth pX] (f : X ⟶ Y) (_hf : f ≫ pY = pX)
    (hnonconstant : (Set.range f).Nontrivial)
    (hdegree : f.residueDegree (genericPoint X) = p)
    (hinseparable :
      letI := (f.residueFieldMap (genericPoint X)).hom.toAlgebra
      ¬ Algebra.IsSeparable
          (Y.residueField (f (genericPoint X))) (X.residueField (genericPoint X))) :
    ∃! i : Over.mk pY ≅
        (frobeniusTwist (Spec (.of k)) p
          (Stacks.Frobenius.isInCharacteristic_of_over
            (Over.mk (𝟙 (Spec (.of k)))))).obj (Over.mk pX),
      f ≫ i.hom.left =
        (relativeFrobenius (Spec (.of k)) p
          (Stacks.Frobenius.isInCharacteristic_of_over (Over.mk (𝟙 (Spec (.of k)))))
          (Over.mk pX)).left
```

## Tag 0CCZ, a lemma

[Tag 0CCZ](https://stacks.math.columbia.edu/tag/0CCZ) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_nat_existsUnique_iso_nFoldFrobeniusTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusChainAssembly.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusChainAssembly.lean#L191). The attribute's comment: “the unique number of iterations and the unique isomorphism of the correspondingly iterated Frobenius twist of X with Y carrying the iterated relative Frobenius to f”.

> **Stacks Project, Tag 0CCZ.** Let `f : X ⟶ Y` be a nonconstant morphism of proper nonsingular
> curves over a field `k` of characteristic `p`, with `X` smooth and the induced extension of
> function fields purely inseparable. Then there is a unique number `n` of iterations and, for it, a
> unique isomorphism over `k` of the `n`-fold Frobenius twist of `X` with `Y` carrying the `n`-fold
> relative Frobenius of `X` to `f`.
>
> Both inputs of the source's proof are supplied here: the degree-`p` factorization of
> `AlgebraicGeometry.exists_chain_isInseparableDegreePrime` ([Stacks, Tag 0CCX]), converted to the
> indexing the assembly uses, and the degree of the relative Frobenius of a smooth curve,
> `AlgebraicGeometry.residueDegree_relativeFrobenius_isCurve` ([Stacks, Tag 0CCF]).

```lean
theorem existsUnique_nat_existsUnique_iso_nFoldFrobeniusTwist
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    (hS : IsInCharacteristic (Spec (.of k)) p)
    {X Y : Scheme.{u}} (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [IsProper pX] [IsProper pY] [Smooth pX]
    (hXreg : IsRegular X) (hYreg : IsRegular Y)
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (hnonconstant : (Set.range f).Nontrivial)
    (hpure : (f.residueFieldMap (genericPoint X)).hom.IsPurelyInseparable) :
    ∃! m : ℕ, ∃! e : nFoldFrobeniusTwist (Spec (.of k)) p hS m (Over.mk pX) ≅ Over.mk pY,
      nFoldRelativeFrobenius (Spec (.of k)) p hS m (Over.mk pX) ≫ e.hom = Over.homMk f hf
```

## Tag 0CD0, a lemma

[Tag 0CD0](https://stacks.math.columbia.edu/tag/0CD0) in the Stacks Project.

**`AlgebraicGeometry.smooth_of_isPurelyInseparable_residueFieldMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusGenus.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusGenus.lean#L95). The attribute's comment: “the smoothness of the target”.

> **Stacks Project, Tag 0CD0, the smoothness of the target.** Let `f : X ⟶ Y` be a nonconstant
> morphism of proper nonsingular curves over a field `k` of characteristic `p`.  If `X` is smooth
> and the extension of function fields is purely inseparable, then `Y` is smooth: by
> [Stacks, Tag 0CCZ] it is a base change of `X` along an endomorphism of the ground field, and
> smoothness is stable under base change.

```lean
theorem smooth_of_isPurelyInseparable_residueFieldMap
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    {X Y : Scheme.{u}} (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [IsProper pX] [IsProper pY] [Smooth pX]
    (hXreg : IsRegular X) (hYreg : IsRegular Y)
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (hnonconstant : (Set.range f).Nontrivial)
    (hpure : (f.residueFieldMap (genericPoint X)).hom.IsPurelyInseparable) :
    Smooth pY
```

**`AlgebraicGeometry.isIso_globalSections_of_isPurelyInseparable_residueFieldMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusGenus.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusGenus.lean#L113). The attribute's comment: “the global regular functions on the target”.

> **Stacks Project, Tag 0CD0, the global regular functions on the target.** Let `f : X ⟶ Y` be
> a nonconstant morphism of proper nonsingular curves over a field `k` of characteristic `p`.  If
> `X` is smooth, the global regular functions on `X` are the constants, and the extension of
> function fields is purely inseparable, then the global regular functions on `Y` are again the
> constants.

```lean
theorem isIso_globalSections_of_isPurelyInseparable_residueFieldMap
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    {X Y : Scheme.{u}} (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [IsProper pX] [IsProper pY] [Smooth pX]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ pX.appTop)]
    (hXreg : IsRegular X) (hYreg : IsRegular Y)
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (hnonconstant : (Set.range f).Nontrivial)
    (hpure : (f.residueFieldMap (genericPoint X)).hom.IsPurelyInseparable) :
    IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ pY.appTop)
```

**`AlgebraicGeometry.genus_eq_of_isPurelyInseparable_residueFieldMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusGenus.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableFrobeniusGenus.lean#L132). The attribute's comment: “the genus of the target”.

> **Stacks Project, Tag 0CD0, the genus of the target.** Let `f : X ⟶ Y` be a nonconstant
> morphism of proper nonsingular curves over a field `k` of characteristic `p`.  If `X` is smooth
> and the extension of function fields is purely inseparable, then `Y` has the same genus as `X`:
> it is a base change of `X` along an extension of the ground field, and the genus is invariant
> under such a base change.

```lean
theorem genus_eq_of_isPurelyInseparable_residueFieldMap
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    {X Y : Scheme.{u}} (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [IsProper pX] [IsProper pY] [Smooth pX]
    (hXreg : IsRegular X) (hYreg : IsRegular Y)
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (hnonconstant : (Set.range f).Nontrivial)
    (hpure : (f.residueFieldMap (genericPoint X)).hom.IsPurelyInseparable) :
    genus pY = genus pX
```

## Tag 0CD1, an example

[Tag 0CD1](https://stacks.math.columbia.edu/tag/0CD1) in the Stacks Project.

**`Stacks.Curves.InseparableGenus.exists_charThree_notCube`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableGenusChange.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableGenusChange.lean#L179). The attribute's comment: “the example's remark that k = 𝐅₃(a) works: a field of characteristic three with an element that is not a cube”.

> **The hypotheses of [Stacks, Tag 0CD1] are satisfiable: `𝐅₃(a)` works.** There is a field of
> characteristic three, in any universe, carrying an element which is not a cube.

```lean
theorem exists_charThree_notCube :
    ∃ (K : Type u) (_ : Field K), CharP K 3 ∧ ∃ a : K, ∀ b : K, b ^ 3 ≠ a
```

**`Stacks.Curves.InseparableGenus.planeCubicProjection_inseparable_genus_change`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableGenusChangeProperCurves.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableGenusChangeProperCurves.lean#L144).

> **[Stacks, Tag 0CD1].** Let `k` be a field of characteristic three and `a ∈ k` an element
> which is not a cube (for instance `k = 𝐅₃(a)`, `exists_charThree_notCube`). Let
> `Z = Proj (k[T₀, T₁, T₂] ⧸ (F))` be the plane cubic with homogeneous equation
> `F = T₁²T₀ - T₂³ + aT₀³`, embedded in `𝐏²_k` by `planeCubicEmbedding`, and let
> `f : Z ⟶ 𝐏¹_k` be the coordinate projection `planeCubicProjection`, which on `D₊(T₀)` sends
> `(x, y)` to `x`. Then:
>
> * `Z` is a closed subscheme of `𝐏²_k`, proper over `k`, a curve over `k`, and nonsingular;
> * `𝐏¹_k` is proper over `k`, a curve over `k`, and nonsingular;
> * `f` is a morphism over `Spec k`, it is the projection `(T₀ : T₁ : T₂) ↦ (T₀ : T₁)` in the
>   sense that `f ⁻¹ᵁ D₊(G) = Z ∩ D₊(G(T₀, T₁))` for every homogeneous `G` of positive degree, and
>   it is dominant;
> * the extension `k(Z)/k(𝐏¹_k)` of function fields induced by `f` is purely inseparable of
>   degree three;
> * the genus of `Z` is `1` and the genus of `𝐏¹_k` is `0`.
>
> So the genus is not preserved by a purely inseparable morphism of proper nonsingular curves.
> Characteristic three is `ExpChar k 3`, which for the prime `3` is the same as `CharP k 3`.

```lean
theorem planeCubicProjection_inseparable_genus_change (k : Type u) [Field k] [ExpChar k 3]
    (a : k) (ha : ∀ b : k, b ^ 3 ≠ a) :
    letI := isIntegral_planeCubicCurve k a ha
    letI := isDominant_planeCubicProjection k a
    letI : Algebra (AlgebraicGeometry.Proj
        (MvPolynomial.homogeneousSubmodule (Fin 2) k)).functionField
        (planeCubicCurve k a).functionField :=
      (dominantFunctionFieldMap (planeCubicProjection k a)).toAlgebra
    IsClosedImmersion (planeCubicEmbedding k a) ∧
      IsProper (planeCubicEmbedding k a ≫ projToSpecCoeff k 2) ∧
      IsCurve k (planeCubicEmbedding k a ≫ projToSpecCoeff k 2) ∧
      IsRegular (planeCubicCurve k a) ∧
      IsProper (projToSpecCoeff k 1) ∧
      IsCurve k (projToSpecCoeff k 1) ∧
      IsRegular (AlgebraicGeometry.Proj (MvPolynomial.homogeneousSubmodule (Fin 2) k)) ∧
      planeCubicProjection k a ≫ projToSpecCoeff k 1 =
        planeCubicEmbedding k a ≫ projToSpecCoeff k 2 ∧
      (∀ (G : MvPolynomial (Fin 2) k) (d : ℕ),
        G ∈ MvPolynomial.homogeneousSubmodule (Fin 2) k d → 0 < d →
        planeCubicProjection k a ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen
            (MvPolynomial.homogeneousSubmodule (Fin 2) k) G =
          planeCubicEmbedding k a ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen
            (MvPolynomial.homogeneousSubmodule (Fin 3) k) (coordProjHom k G)) ∧
      IsDominant (planeCubicProjection k a) ∧
      IsPurelyInseparable (AlgebraicGeometry.Proj
          (MvPolynomial.homogeneousSubmodule (Fin 2) k)).functionField
          (planeCubicCurve k a).functionField ∧
      Module.finrank (AlgebraicGeometry.Proj
          (MvPolynomial.homogeneousSubmodule (Fin 2) k)).functionField
          (planeCubicCurve k a).functionField = 3 ∧
      genus (planeCubicEmbedding k a ≫ projToSpecCoeff k 2) = 1 ∧
      genus (projToSpecCoeff k 1) = 0
```

## Tag 0CD2, a proposition

[Tag 0CD2](https://stacks.math.columbia.edu/tag/0CD2) in the Stacks Project.

**`AlgebraicGeometry.exists_nFoldRelativeFrobenius_comp_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/SeparableFrobeniusFactorization.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/SeparableFrobeniusFactorization.lean#L166).

> **Stacks Project, Tag 0CD2.** Let `k` be a field of characteristic `p > 0` and let
> `f : X ⟶ Y` be a nonconstant morphism of proper smooth curves over `k`.  Then `f` factors as
> `X ⟶ X^(p^n) ⟶ Y`, where `X^(p^n)` is the `n`-fold Frobenius twist of `X`, that is, the base
> change of `X` along the `n`-fold absolute Frobenius of `Spec k`, the first morphism is the
> `n`-fold relative Frobenius of `X`, and the second is a nonconstant morphism of proper smooth
> curves over `k` inducing a separable extension of function fields.

```lean
theorem exists_nFoldRelativeFrobenius_comp_isSeparable {k : Type u} [Field k] (p : ℕ)
    [Fact p.Prime] (hk : IsInCharacteristic (Spec (.of k)) p)
    {X Y : Scheme.{u}} (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [Smooth pX] [Smooth pY] [IsProper pX] [IsProper pY]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) (hnonconstant : (Set.range f).Nontrivial) :
    ∃ n : ℕ,
      let T := nFoldFrobeniusTwist (Spec (.of k)) p hk n (Over.mk pX)
      ∃ (g : T.left ⟶ Y) (hcurve : IsCurve k T.hom) (hdom : IsDominant g),
        letI := hcurve
        letI := hdom
        Smooth T.hom ∧ IsProper T.hom ∧ g ≫ pY = T.hom ∧
          f = (nFoldRelativeFrobenius (Spec (.of k)) p hk n (Over.mk pX)).left ≫ g ∧
          (Set.range g).Nontrivial ∧ g (genericPoint T.left) = genericPoint Y ∧
          @Algebra.IsSeparable Y.functionField T.left.functionField _ _
            (functionFieldMap g).toAlgebra
```

## Tag 0CD3, a lemma

[Tag 0CD3](https://stacks.math.columbia.edu/tag/0CD3) in the Stacks Project.

**`AlgebraicGeometry.exists_genericallyEtale_pencil_or_linearSeries_frobeniusTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/InseparableLinearSeries.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/InseparableLinearSeries.lean#L569). The attribute's comment: “both alternatives: a pencil of the same degree whose morphism to the projective line is generically etale, or a linear series of the same dimension and degree at most d / p on the Frobenius twist”.

> **Stacks Project, Tag 0CD3.** Let `k` be a field of characteristic `p > 0`, let `X` be a
> smooth proper curve over `k` and let `(ℒ, V)` be a `𝔤^r_d` on `X` with `r ≥ 1`. Then one of the
> following holds: there is a `𝔤¹_d` on `X` whose corresponding morphism `X ⟶ ℙ¹_k` of
> [Stacks, Tag 0CCP] is generically etale, or there is a `𝔤^r_{d'}` on the Frobenius twist
> `X^{(p)}` with `d' ≤ d / p`.
>
> Which alternative holds is decided by the ratios `s_j / s_0` of a basis `s_0, …, s_r` of `V`,
> read at the generic point of `X` as elements of `k(X)`: if they all lie in the compositum of `k`
> with the `p`-th powers of `k(X)` — the image of `k(X^{(p)})` — the morphism to `ℙ^r_k` factors
> through the relative Frobenius and the second alternative holds; otherwise the pencil spanned by
> `s_0` and an offending `s_j` gives the first.

```lean
theorem exists_genericallyEtale_pencil_or_linearSeries_frobeniusTwist
    (p : ℕ) [Fact p.Prime] [CharP k p] (hS : IsInCharacteristic (Spec (.of k)) p)
    {X : Scheme.{u}} (pX : X ⟶ Spec (.of k)) [IsCurve k pX] [Smooth pX] [IsProper pX]
    (hdim : topologicalKrullDim X ≤ 1) {d r : ℕ} (_hr : 1 ≤ r)
    (E : LinearSeries k pX hdim d r) :
    (∃ (E₁ : LinearSeries k pX hdim d 1) (b₁ : Module.Basis (Fin 2) k E₁.V)
        (q : X ⟶ projectiveSpaceOver 1 (Spec (.of k)))
        (_ : q ≫ (projectiveSpaceOver 1 (Spec (.of k)) ↘ Spec (.of k)) = pX)
        (α : (Scheme.Modules.pullback
            (q ≫ projectiveSpaceOver.toIntegralAtUniverse 1 (Spec (.of k)))).obj
              (twistingSheafAtUniverse.{u} 1) ⟶ E₁.L),
        (∀ i, α.app ⊤ (pullbackCoordSection.{u}
            (q ≫ projectiveSpaceOver.toIntegralAtUniverse 1 (Spec (.of k))) i) =
          seriesSections E₁ b₁ i) ∧
          ∃ U : X.Opens, Nonempty U ∧ Etale (U.ι ≫ q)) ∨
      (letI : IsCurve k ((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk pX)).hom :=
          isCurve_frobeniusTwist_curve p hS pX
       letI : IsProper ((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk pX)).hom :=
          isProper_frobeniusTwist_curve p hS pX
       ∃ d' : ℕ, p * d' ≤ d ∧ d' ≤ d / p ∧
         Nonempty (LinearSeries k ((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk pX)).hom
           (IsCurve.topologicalKrullDim_eq_one (k := k)
             (f := ((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk pX)).hom)).le d' r))
```

## Tag 0CD4, a lemma

[Tag 0CD4](https://stacks.math.columbia.edu/tag/0CD4) in the Stacks Project.

**`AlgebraicGeometry.exists_isClosed_isSeparable_finrank_residueField_le_two_mul_genus_sub_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/SeparableClosedPointGenus.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/SeparableClosedPointGenus.lean#L105).

> A smooth proper curve `X` over a field `k` with `H⁰(X, 𝒪_X) = k` and genus `g ≥ 2` has a
> closed point `x` with `κ(x)/k` finite separable of degree at most `2g - 2`.

```lean
theorem exists_isClosed_isSeparable_finrank_residueField_le_two_mul_genus_sub_two
    (hg : 2 ≤ genus f) :
    ∃ x : X, IsClosed ({x} : Set X) ∧
      (letI := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra;
      Module.Finite k (X.residueField x) ∧ Algebra.IsSeparable k (X.residueField x) ∧
        Module.finrank k (X.residueField x) ≤ 2 * genus f - 2)
```

## Tag 0C1G, a lemma

[Tag 0C1G](https://stacks.math.columbia.edu/tag/0C1G) in the Stacks Project.

**`AlgebraicGeometry.ramificationIdx_baseChange_algClosure_eq_finInsepDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/RamificationAlgebraicClosure.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Curve/RamificationAlgebraicClosure.lean#L261).

> The ramification index at a closed point of a smooth curve after extension to an algebraic
> closure is the inseparable degree of the original residue field.

```lean
public theorem ramificationIdx_baseChange_algClosure_eq_finInsepDegree
    (k K : Type u) [Field k] [Field K] [Algebra k K] [IsAlgClosure k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] [Smooth f]
    (xbar : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hxbar : IsClosed ({xbar} : Set
      (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))) :
    let p := pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    let x := p xbar
    letI : Algebra (X.presheaf.stalk x)
        ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
          Scheme.{u}).presheaf.stalk xbar) :=
      (p.stalkMap xbar).hom.toAlgebra
    letI : Algebra k (X.residueField x) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
    Stacks.DiscreteValuationRing.Ramification.ramificationIdx (X.presheaf.stalk x)
      ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
        Scheme.{u}).presheaf.stalk xbar) =
      Field.finInsepDegree k (X.residueField x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.13, Tag 0CCV](https://stacks.math.columbia.edu/tag/0CCV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
