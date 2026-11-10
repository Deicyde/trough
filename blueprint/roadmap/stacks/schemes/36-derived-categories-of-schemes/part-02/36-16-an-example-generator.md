---
declaration: section
origin: cited
lean: Stacks.AmpleNonvanishing.exists_nonzero_hypercohomology_tensorPower, Stacks.AmpleNonvanishingChart.exists_twistedSection_restrict_eq_tensorSection, Stacks.AlgebraicGeometry.ProjKoszulComplex.acyclic_koszulComplex_and_locallyFree_koszulTerm, Stacks.AlgebraicGeometry.ExampleGenerator.twist_mem_gen_of_le, Stacks.AlgebraicGeometry.ExampleGenerator.twist_neg_mem_gen, Stacks.AlgebraicGeometry.ExampleGenerator.isWeakTriangulatedGenerator_twistSumDerivedQCoh, Stacks.AlgebraicGeometry.ExampleGenerator.isWeakTriangulatedGenerator_twistSumQCoh, Stacks.Duality.DerivedPushforward.conditions_of_multiplicativeClosure
statement: formalized
proof: formalized
---

# 36.16 An example generator

Section 36.16 of the Stacks Project, [Tag 0BQQ](https://stacks.math.columbia.edu/tag/0BQQ). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BQR, a lemma

[Tag 0BQR](https://stacks.math.columbia.edu/tag/0BQR) in the Stacks Project.

**`Stacks.AmpleNonvanishing.exists_nonzero_hypercohomology_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/Derived.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/Derived.lean#L223). The attribute's comment: “the general derived statement: K is an arbitrary nonzero object of D\_QCoh(O\_X), the tensor product is the derived one of Tag 06YH with a tensor power of L in degree zero, and the cohomology is the derived hypercohomology of Tag 08JA in degree p. The hypothesis is stated at the locally small model of D(O\_X), the only model Tag 08DB is available at, and the conclusion at the standard model, the only model Tag 08JA is available at; the object in the conclusion is K itself, Stacks.Injectives.grothendieckModelEquiv being the identity on objects. The degree-zero module case, which this does not subsume because it carries an explicit witness, is the separate carrier Stacks.AmpleNonvanishingChart.exists\_twistedSection\_restrict\_eq\_tensorSection”.

> **[Stacks, Tag 0BQR].** Let `X` be a scheme, `L` an ample invertible `𝒪_X`-module and `K` a
> **nonzero** object of `D_QCoh(𝒪_X)`. Then there are an exponent `n` and a degree `p` with
>
> `H^p(X, K ⊗^𝐋_{𝒪_X} L^{⊗ n}[0]) ≠ 0`.
>
> The tensor product is the derived tensor product of [Stacks, Tag 06YH] with the `n`-th tensor
> power of `L` placed in degree zero, and the cohomology is the derived hypercohomology, the
> degree-`p` homology of unbounded derived global sections. The object the conclusion is about is
> `K` itself, read in the standard model of the derived category; see the implementation notes on
> the two models.

```lean
theorem exists_nonzero_hypercohomology_tensorPower (X : Scheme.{u}) (L : X.Modules)
    [IsInvertibleModule X L] (hL : IsAmple X L)
    (K : (@DerivedCategoryB.derivedCategoryB X.Modules _ _
      (AlgebraicGeometry.Scheme.Modules.hasDerivedCategory X)
      (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory)
    (hK : ¬ IsZero K) :
    ∃ (n : ℕ) (p : ℤ),
      ¬ IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} p).obj
        ((derivedModuleGlobalSections
            (Stacks.SheafOfModules.ringedSite X.toRingedSpace.sheaf)).obj
          (((Stacks.Cohomology.TorAmplitude.derTensor X.toRingedSpace).tensor.obj
              ((Stacks.Injectives.grothendieckModelEquiv X.Modules).inverse.obj K.1)).obj
            (DerivedCategory.Q.obj
              ((HomologicalComplex.single (Stacks.DerivedTensor.RingedSite.Modules X.sheaf)
                (ComplexShape.up ℤ) 0).obj (tensorPowModule X L (n : ℤ)))))))
```

**`Stacks.AmpleNonvanishingChart.exists_twistedSection_restrict_eq_tensorSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/TwistedSectionChart.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/TwistedSectionChart.lean#L141). The attribute's comment: “run at a quasi-coherent module rather than at an object of D\_QCoh(O\_X) in a degree: Gamma(X, F tensor L^p) is nonzero, witnessed by an explicit tau. The derived-category form is a separate assertion; see the module docstring”.

> **[Stacks, Tag 0BQR] for a quasi-coherent module.** For `L` an ample invertible `𝒪_X`-module
> and `F` a nonzero quasi-coherent `𝒪_X`-module there are an exponent `p`, a global section `σ` of
> `L ^⊗ p` with affine nonvanishing open `U = X_σ`, a **nonzero** section `t` of `F` over `U`, and a
> **nonzero** global section `τ` of `F ⊗ L ^⊗ p` with `τ|_U = t ⊗ σ|_U`.
>
> These are the five steps of the source argument run on a module instead of on a complex: the
> point with nonzero stalk, the affine chart of ampleness, the nonzero section on it, the
> surjectivity half of [Stacks, Tag 01PW], and — for `τ ≠ 0` — the whiskered clause 2 of
> [Stacks, Tag 01CY] in the form
> `Stacks.SectionProduct.eq_zero_of_tensorSection_eq_zero`: over an open inside `X_σ` the product
> with `σ` kills no section of `F`, so `τ|_U = t ⊗ σ|_U` with `t ≠ 0` forces `τ ≠ 0`.

```lean
theorem exists_twistedSection_restrict_eq_tensorSection {X : Scheme.{u}} (L : X.Modules)
    [IsInvertibleModule X L] (hL : IsAmple X L) (F : X.Modules) [F.IsQuasicoherent]
    (hF : ¬ IsZero F) :
    ∃ (p : ℕ) (σ : Γ(tensorPowModule X L (p : ℤ), ⊤)) (U : X.Opens)
      (τ : Γ(F ⊗ tensorPowModule X L (p : ℤ), ⊤)) (t : Γ(F, U)),
      U = Stacks.AmpleTheory.powNonvanishingOpen X L p σ ∧ IsAffineOpen U ∧ t ≠ 0 ∧ τ ≠ 0 ∧
        resTop U τ = tensorSection F (tensorPowModule X L (p : ℤ)) t (resTop U σ)
```

## Tag 0BQS, a lemma

[Tag 0BQS](https://stacks.math.columbia.edu/tag/0BQS) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjKoszulComplex.acyclic_koszulComplex_and_locallyFree_koszulTerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjKoszulComplex/LocallyFree.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjKoszulComplex/LocallyFree.lean#L152).

> **Stacks 0BQS.** Let `A` be a ring and `X = P^n_A = Proj A[X₀, …, Xₙ]`. For every integer `a`
> there is an exact complex of vector bundles
>
> `0 ⟶ 𝒪_X(a) ⟶ … ⟶ 𝒪_X(a+j)^{⊕ binom(n+1, j)} ⟶ … ⟶ 𝒪_X(a+n+1) ⟶ 0`
>
> on `X`, namely the Koszul complex `Stacks.AlgebraicGeometry.ProjKoszulComplex.koszulComplex` of
> the coordinates `X₀, …, Xₙ`, graded so that the generators of the `j`-th exterior power sit in
> degree `j` and twisted by `a`. Its `j`-th term is the direct sum of copies of `𝒪_X(a+j)` indexed
> by the `j`-element subsets of the coordinates, of which there are `binom(n+1, j)`, and each term
> is free on that index set over every standard open of a degree-one element, those opens covering
> `X`; the complex is acyclic, so it is exact in every degree, and it is concentrated in degrees
> `0, …, n+1` because outside that range the index set is empty.

```lean
theorem acyclic_koszulComplex_and_locallyFree_koszulTerm (j : ℕ) :
    (koszulComplex A n a).Acyclic ∧
      (koszulComplex A n a).X (j : ℤ) =
        (⨁ fun _ : koszulIndex (n + 1) (j : ℤ) =>
          twistingSheaf (polyGrading A n) (a + (j : ℤ))) ∧
      Fintype.card (koszulIndex (n + 1) (j : ℤ)) = (n + 1).choose j ∧
      ∃ (I : Type u) (U : I → Opens (ProjectiveSpectrum.top (polyGrading A n))),
        (Opens.grothendieckTopology (ProjectiveSpectrum.top (polyGrading A n))).CoversTop U ∧
          ∀ f : I, Nonempty (SheafOfModules.free.{u} (ULift.{u} (koszulIndex (n + 1) (j : ℤ))) ≅
            (koszulTerm A n a (j : ℤ)).over (U f))
```

## Tag 0A9V, a lemma

[Tag 0A9V](https://stacks.math.columbia.edu/tag/0A9V) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ExampleGenerator.twist_mem_gen_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/Koszul.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/Koszul.lean#L116). The attribute's comment: “each of the twists O, O(-1), …, O(-n) lies in the subcategory generated by E”.

> Each of the `n + 1` displayed twists is a direct summand of `E`, hence lies in `⟨E⟩`.

```lean
theorem twist_mem_gen_of_le (i : Fin (n + 1)) :
    twist A n (-(i : ℤ)) ∈ gen (twistSum A n)
```

**`Stacks.AlgebraicGeometry.ExampleGenerator.twist_neg_mem_gen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/Koszul.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/Koszul.lean#L227). The attribute's comment: “the subcategory generated by E contains every twist O(-m), m ≥ 0”.

> **Every twist `𝒪_X(-m)`, `m ≥ 0`, lies in `⟨E⟩`.** For `X = P^n_A` and
> `E = 𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)`, every twist `𝒪_X(-m)` with `m ≥ 0` lies in the subcategory
> `⟨E⟩` of [Stacks, Tag 09SI] generated by `E`.
>
> Strong induction on `m`. For `m ≤ n` the twist is a direct summand of `E`. For `m ≥ n + 1` the
> one-step descent `twist_mem_gen_of_shift_mem_gen` at `a = -m` reduces the claim to the twists
> `𝒪_X(-m+p)` for `1 ≤ p ≤ n + 1`, and `-m + p = -(m - p)` with `m - p < m`.

```lean
theorem twist_neg_mem_gen (m : ℕ) : twist A n (-(m : ℤ)) ∈ gen (twistSum A n)
```

**`Stacks.AlgebraicGeometry.ExampleGenerator.isWeakTriangulatedGenerator_twistSumDerivedQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/KoszulQuasiCoherent.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/KoszulQuasiCoherent.lean#L151).

> Let `A` be a ring and `X = P^n_A`. Then `E = 𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)` is a generator
> of `D_QCoh(𝒪_X)` in the sense of [Stacks, Tag 09SJ]: every object of `D_QCoh(𝒪_X)` receiving
> only zero maps from the shifts of `E` is zero.

```lean
theorem isWeakTriangulatedGenerator_twistSumDerivedQCoh :
    (ObjectProperty.singleton (twistSumDerivedQCoh A n)).IsWeakTriangulatedGenerator
```

**`Stacks.AlgebraicGeometry.ExampleGenerator.isWeakTriangulatedGenerator_twistSumQCoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/QuasiCoherentGenerator.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/QuasiCoherentGenerator.lean#L278). The attribute's comment: “the generator conclusion of Definition 09SJ(3) for D\_QCoh(O\_X), with no hypothesis beyond the tag's. The generation step on the whole of D(O\_X) is Stacks.AlgebraicGeometry.ExampleGenerator.twist\_neg\_mem\_gen”.

> **[Stacks, Tag 0A9V] on `D_QCoh(𝒪_X)`.** For `X = P^n_A` the object
> `E = 𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)` in degree zero is a weak generator of `D_QCoh(𝒪_X)`.
>
> An object `K` of `D_QCoh(𝒪_X)` receiving only zero morphisms from the shifts of `E` receives
> only zero morphisms from every object of `⟨E⟩` ([Stacks, Tag 09SK]), hence from every
> `𝒪_X(-m)[-p]` with `m ≥ 0` — that is the generation step
> `Stacks.AlgebraicGeometry.ExampleGenerator.twist_neg_mem_gen`. Those twists are enough to force
> `K = 0` by `Stacks.AmpleNonvanishing.isZero_of_hom_single_eq_zero`, whose presentation
> hypothesis is `exists_epi_coproduct_twist_nonpos`.

```lean
theorem isWeakTriangulatedGenerator_twistSumQCoh :
    (ObjectProperty.singleton (twistSumQCoh A n)).IsWeakTriangulatedGenerator
```

## Tag 0BQT, a remark

[Tag 0BQT](https://stacks.math.columbia.edu/tag/0BQT) in the Stacks Project.

**`Stacks.Duality.DerivedPushforward.conditions_of_multiplicativeClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/GeneratorClauses.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/GeneratorClauses.lean#L365). The attribute's comment: “the clause that the three conditions hold when f is affine, when f is an open immersion, and when f is a composition of such”.

> **[Stacks, Tag 0BQT]: the three conditions hold when `f` is affine, when `f` is an open
> immersion, and when `f` is a composition of such.** Let `f : X ⟶ Y` be a finite composite of
> affine morphisms and open immersions between quasi-compact and quasi-separated schemes, and let
> `E` be a weak generator of `D_QCoh(𝒪_Y)`. Then
>
> 1. every object `K` of `D_QCoh(𝒪_X)` with `Rf_*K` zero is itself zero;
> 2. `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` reflects isomorphisms;
> 3. `Lf^*E` is a weak generator of `D_QCoh(𝒪_X)`.
>
> Condition (3) is
> `isWeakTriangulatedGenerator_quasiCoherentDerivedPullback_of_openFactorization`, applied to the
> trivial factorization `f = f ≫ 𝟙 Y`; (1) and (2) follow from it by
> `tfae_isZero_quasiCoherentDerivedPushforward`, the equivalence of the three conditions.

```lean
theorem conditions_of_multiplicativeClosure {X Y : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y] {f : X ⟶ Y}
    (hf : ((@IsAffineHom) ⊔ (@IsOpenImmersion) :
      MorphismProperty (Scheme.{u})).multiplicativeClosure f)
    (E : Stacks.Duality.quasiCoherentDerivedCategory Y)
    (hE : (ObjectProperty.singleton E).IsWeakTriangulatedGenerator) :
    (∀ K : Stacks.Duality.quasiCoherentDerivedCategory X,
        IsZero ((qcqsRestrictedDerivedPushforward f).obj K) → IsZero K) ∧
      (qcqsRestrictedDerivedPushforward f).ReflectsIsomorphisms ∧
      (ObjectProperty.singleton
        ((Stacks.Duality.quasiCoherentDerivedPullback' f).obj E)
        ).IsWeakTriangulatedGenerator
```

**`Stacks.Duality.DerivedPushforward.isWeakTriangulatedGenerator_restrictedTwistSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/ProjectiveImmersionGenerator.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/ProjectiveImmersionGenerator.lean#L167). The attribute's comment: “the second consequence drawn from the remark: for X a quasi-compact locally closed subscheme of P^n\_A, the object O\_X ⊕ O\_X(-1) ⊕ … ⊕ O\_X(-n) is a generator for D\_QCoh(O\_X)”.

> For `i : W ⟶ P^n_A` an immersion with `W` quasi-compact, the object
> `𝒪_W ⊕ 𝒪_W(-1) ⊕ ⋯ ⊕ 𝒪_W(-n)`, placed in degree zero, generates `D_QCoh(𝒪_W)`.

```lean
theorem isWeakTriangulatedGenerator_restrictedTwistSum [IsImmersion i] [CompactSpace W] :
    (ObjectProperty.singleton (restrictedTwistSum i)).IsWeakTriangulatedGenerator
```

**`Stacks.Duality.DerivedPushforward.tfae_isZero_quasiCoherentDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/PullbackGenerator.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/PullbackGenerator.lean#L197).

> **[Stacks, Tag 0BQT].** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> schemes with `Y` quasi-compact, and let `E` be a weak generator of `D_QCoh(𝒪_Y)` — the object
> [Stacks, Tag 09IS] provides, and the one hypothesis the source's remark carries. Then the
> following are equivalent:
>
> 1. every object `K` of `D_QCoh(𝒪_X)` with `Rf_*K` zero is itself zero;
> 2. `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` reflects isomorphisms;
> 3. `Lf^*E` is a weak generator of `D_QCoh(𝒪_X)`.
>
> (1) ⇒ (2): complete a morphism `α` whose image is invertible to a distinguished triangle; `Rf_*`
> is exact, so it carries that triangle to a distinguished triangle whose first morphism is
> `Rf_*α`, whence its third vertex `Rf_*(cone α)` is zero, whence `cone α` is zero by (1), whence
> `α` is invertible. (2) ⇒ (1): if `Rf_*K` is zero then the zero endomorphism of `Rf_*K` is its
> identity, so the zero endomorphism of `K` is invertible by (2) and `𝟙 K = 0`.
>
> (1) ⇔ (3): `K` is right orthogonal to the shifts of `Lf^*E` exactly when `Rf_*K` is right
> orthogonal to the shifts of `E`, by
> `rightOrthogonal_shiftClosure_singleton_quasiCoherentDerivedPullback_iff`, and the latter says
> exactly that `Rf_*K` is zero because `E` generates.

```lean
theorem tfae_isZero_quasiCoherentDerivedPushforward
    (E : Stacks.Duality.quasiCoherentDerivedCategory Y)
    (hE : (ObjectProperty.singleton E).IsWeakTriangulatedGenerator) :
    [∀ K : Stacks.Duality.quasiCoherentDerivedCategory X,
        IsZero ((qcqsRestrictedDerivedPushforward f).obj K) → IsZero K,
      (qcqsRestrictedDerivedPushforward f).ReflectsIsomorphisms,
      (ObjectProperty.singleton
        ((Stacks.Duality.quasiCoherentDerivedPullback' f).obj E)
        ).IsWeakTriangulatedGenerator].TFAE
```

**`Stacks.Duality.DerivedPushforward.isWeakTriangulatedGenerator_quasiCoherentDerivedPullback_specMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/PullbackGenerator.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/PullbackGenerator.lean#L257). The attribute's comment: “the conditions hold for an affine morphism: the case of a morphism Spec φ of affine schemes, where Lf^* carries a generator to a generator”.

> **[Stacks, Tag 0BQT] for a morphism of affine schemes: `L(Spec φ)^*` carries a generator to a
> generator.** Let `φ : R ⟶ S` be a map of commutative rings and let `E` be a weak generator of
> `D_QCoh(𝒪_{Spec R})`. Then `L(Spec φ)^*E` is a weak generator of `D_QCoh(𝒪_{Spec S})`.
>
> This is the implication (2) ⇒ (3) of `tfae_isZero_quasiCoherentDerivedPushforward`, whose
> condition (2) holds for `Spec φ` by [Stacks, Tag 08I8]; it is the source's clause that the three
> conditions of the remark hold when `f` is affine, in the case of a morphism of affine
> schemes.

```lean
theorem isWeakTriangulatedGenerator_quasiCoherentDerivedPullback_specMap
    (E : Stacks.Duality.quasiCoherentDerivedCategory (Spec R))
    (hE : (ObjectProperty.singleton E).IsWeakTriangulatedGenerator) :
    (ObjectProperty.singleton
        ((Stacks.Duality.quasiCoherentDerivedPullback' (Spec.map φ)).obj E)
      ).IsWeakTriangulatedGenerator
```

**`Stacks.Duality.DerivedPushforward.isWeakTriangulatedGenerator_derivedStructureSheaf_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QuasiAffineGenerator.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QuasiAffineGenerator.lean#L165). The attribute's comment: “the first consequence drawn from the remark: if X is a quasi-affine scheme then the structure sheaf O\_X is a generator for D\_QCoh(O\_X)”.

> **[Stacks, Tag 0BQT]: if `X` is a quasi-affine scheme then `𝒪_X` generates
> `D_QCoh(𝒪_X)`.** This is the first consequence the source draws from its remark.
>
> A quasi-affine scheme is quasi-compact, quasi-separated, and its canonical morphism
> `j : X ⟶ Spec Γ(X, 𝒪_X)` is an open immersion; the target is affine, hence quasi-compact and
> quasi-separated. The remark's clause for an open immersion therefore applies to `j`, and `𝒪` is
> a generator on the affine target by
> `isWeakTriangulatedGenerator_derivedStructureSheaf_spec`, so `Lj^*𝒪` is a generator — and
> `Lj^*𝒪` is `𝒪_X`.

```lean
theorem isWeakTriangulatedGenerator_derivedStructureSheaf_of_isQuasiAffine (X : Scheme.{u})
    [X.IsQuasiAffine] :
    (ObjectProperty.singleton (derivedStructureSheaf X)).IsWeakTriangulatedGenerator
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.16, Tag 0BQQ](https://stacks.math.columbia.edu/tag/0BQQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
