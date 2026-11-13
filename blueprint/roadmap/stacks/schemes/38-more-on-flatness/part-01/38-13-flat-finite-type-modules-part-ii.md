---
declaration: section
origin: cited
lean: Stacks.PureModules.exists_not_mem_and_mem_associatedPrimes_not_le_fiberIdeal, Stacks.WeaklyAssociatedPrimes.isWeaklyAssociatedPrime_and_isAssociatedPrimeStacks_fibre_of_tensorProduct, Stacks.WeaklyAssociatedPrimes.tensorFibreFormula05IG, Stacks.PureModules.comap_associatedPrime_le_fiberIdeal_of_isUnit, Stacks.Divisors.isWeaklyAssociatedPoint_tensorPullback_iff_of_finiteType, Stacks.WeaklyAssociatedPrimes.weaklyAssociatedPrimes_tensorProduct_eq_fibrewise_assStacks_of_small, Stacks.WeaklyAssociatedPrimes.weaklyAssociatedPrimes_tensorProduct_eq_fibrewise_assStacks_of_small', Stacks.Divisors.weaklyAssociatedPoints_tensorPullback_eq
statement: formalized
proof: formalized
---

# 38.13 Flat finite type modules, Part II

Section 38.13 of the Stacks Project, [Tag 05IF](https://stacks.math.columbia.edu/tag/05IF). 13 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CU6, a lemma

[Tag 0CU6](https://stacks.math.columbia.edu/tag/0CU6) in the Stacks Project.

**`Stacks.PureModules.exists_not_mem_and_mem_associatedPrimes_not_le_fiberIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/FibreAssociatedPrimes.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/FibreAssociatedPrimes.lean#L64).

> **Stacks Project, Tag 0CU6.** An element can be chosen outside `q` whose image in the
> fibre lies in every associated prime of the fibre module that is not contained in the
> extension of `q`.

```lean
theorem exists_not_mem_and_mem_associatedPrimes_not_le_fiberIdeal
    {R S N : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S] [AddCommGroup N] [Module S N]
    [Module.FinitePresentation S N]
    (p : Ideal R) (q : Ideal S) [p.IsPrime] [q.IsPrime] [q.LiesOver p] :
    letI : Algebra S (p.Fiber S) := Algebra.TensorProduct.rightAlgebra
    ∃ g : S, g ∉ q ∧
      ∀ r ∈ associatedPrimes (p.Fiber S) (TensorProduct S (p.Fiber S) N),
        ¬ r ≤ Ideal.map
          (Algebra.TensorProduct.includeRight : S →ₐ[R] p.Fiber S).toRingHom q →
        (Algebra.TensorProduct.includeRight : S →ₐ[R] p.Fiber S) g ∈ r
```

## Tag 05IG, a lemma

[Tag 05IG](https://stacks.math.columbia.edu/tag/05IG) in the Stacks Project.

**`Stacks.WeaklyAssociatedPrimes.isWeaklyAssociatedPrime_and_isAssociatedPrimeStacks_fibre_of_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/FlatFibreAtPrime.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/FlatFibreAtPrime.lean#L498). The attribute's comment: “RESTRICTED: the implication ⟹ only, and its base clause carries the extra hypothesis that 𝔭 is finitely generated, which the tag does not have. That hypothesis stands in for the étale-local structure theorem 05ID, proved only scheme-side here”.

> **[Stacks, Tag 05IG], the implication `⟹`.**  Let `R → S` be a ring map of finite
> presentation, let `N` be an `S`-module of finite presentation which is flat as an `R`-module, let
> `M` be an `R`-module, and let `𝔮` be a prime of `S` lying over a prime `𝔭` of `R` which is
> finitely generated.  If `𝔮` is *weakly* associated to `N ⊗_R M` over `S`, then `𝔭` is *weakly*
> associated to `M` over `R` and `𝔮-bar` is an *associated* prime, in the strict sense of
> [Stacks, Tag 00LA], of `N-bar` over the fibre ring `S-bar`.
>
> Finite generation of `𝔭` enters the base clause only.  It stands in for the étale-local
> structure theorem [Stacks, Tag 05ID], which the source uses to make `N` projective over the base
> and which this library has only in scheme-theoretic form;  see the module documentation for what
> the ring-theoretic form would need.  With `N` projective over a local base the witness lands in a
> finite free summand and no prime avoidance is needed, whereas the finiteness-free content
> available here (`exists_smul_pow_eq_zero_localizedModule_of_tensorProduct`) only covers `𝔭 R_𝔭`
> by the primes weakly associated to `M_𝔭`, and finitely many generators of `𝔭` are what turn
> that covering into a single witness.  The variant
> `..._of_tensorProduct_of_finite` trades it for finiteness of `WeakAss_R(M)`, and the fibre clause
> `isAssociatedPrimeStacks_fibre_of_isWeaklyAssociatedPrime_tensorProduct` is free of both.
>
> The converse implication of the tag is not proved here;  see the module documentation.

```lean
theorem isWeaklyAssociatedPrime_and_isAssociatedPrimeStacks_fibre_of_tensorProduct
    [Algebra.FinitePresentation R S] [Module.FinitePresentation S N] [Module.Flat R N]
    (q : Ideal S) [q.IsPrime] [q.LiesOver p] (hfg : p.FG)
    (hq : IsWeaklyAssociatedPrime S (N ⊗[R] M) q) :
    IsWeaklyAssociatedPrime R M p ∧
      IsAssociatedPrimeStacks (Localization (primeComplImage S p) ⧸ fibreIdeal S p)
        ((Localization (primeComplImage S p) ⧸ fibreIdeal S p) ⊗[S] N)
        (Ideal.map (algebraMap S (Localization (primeComplImage S p) ⧸ fibreIdeal S p)) q)
```

**`Stacks.WeaklyAssociatedPrimes.tensorFibreFormula05IG`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/TensorFibreFormula.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/TensorFibreFormula.lean#L60).

> **[Stacks, Tag 05IG].**  Let `R → S` be a ring map of finite presentation, let `N` be a
> finitely presented `S`-module which is flat as an `R`-module, let `M` be an `R`-module and let `𝔮`
> be a prime of `S` lying over a prime `𝔭` of `R`.  Then `𝔮` is weakly associated to `N ⊗_R M` if and
> only if `𝔭` is weakly associated to `M` and some prime of the fibre ring `S ⊗_R κ(𝔭)` associated —
> in the strict sense of [Stacks, Tag 00LA] — to the fibre module contracts to `𝔮`.
>
> Both directions are proved, and no hypothesis beyond the tag's own is used.

```lean
theorem tensorFibreFormula05IG : TensorFibreFormula05IG.{u}
```

## Tag 0CU7, an equation

[Tag 0CU7](https://stacks.math.columbia.edu/tag/0CU7) in the Stacks Project.

**`Stacks.PureModules.comap_associatedPrime_le_fiberIdeal_of_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/FibreAssociatedPrimesAway.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/FibreAssociatedPrimesAway.lean#L73).

> **Stacks Project, Tag 0CU7.** With `g ∈ S` chosen as in Tag 0CU6, let `B` be an étale algebra
> over the fibre ring `p.Fiber S` in which the image of `g` is a unit. Then every prime of `B`
> associated to the base change of the fibre module contracts to a prime of `p.Fiber S` contained
> in the extension of `q`.
>
> Indeed, such a contraction is associated to the fibre module itself, because `B` is flat over the
> fibre ring and the fibre ring is Noetherian; were it not contained in the extension of `q`, the
> choice of `g` would put the image of `g` inside it, contradicting the fact that the image of `g`
> in `B` is a unit.

```lean
theorem comap_associatedPrime_le_fiberIdeal_of_isUnit
    {R S N B : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S] [AddCommGroup N] [Module S N]
    [Module.FinitePresentation S N]
    (p : Ideal R) (q : Ideal S) [p.IsPrime] [q.IsPrime] [q.LiesOver p]
    [CommRing B] [Algebra (p.Fiber S) B] [Algebra.Etale (p.Fiber S) B]
    (g : S)
    (hg : letI : Algebra S (p.Fiber S) := Algebra.TensorProduct.rightAlgebra
      g ∉ q ∧
        (∀ r ∈ associatedPrimes (p.Fiber S)
          (TensorProduct S (p.Fiber S) N),
          (¬ r ≤ Ideal.map
            (Algebra.TensorProduct.includeRight : S →ₐ[R] p.Fiber S).toRingHom q →
            (Algebra.TensorProduct.includeRight : S →ₐ[R] p.Fiber S) g ∈ r)))
    (hunit : IsUnit ((algebraMap (p.Fiber S) B)
      ((Algebra.TensorProduct.includeRight : S →ₐ[R] p.Fiber S) g))) :
    letI : Algebra S (p.Fiber S) := Algebra.TensorProduct.rightAlgebra
    ∀ r' ∈ associatedPrimes B
      (TensorProduct (p.Fiber S) B (TensorProduct S (p.Fiber S) N)),
      Ideal.comap (algebraMap (p.Fiber S) B) r' ≤
        Ideal.map
          (Algebra.TensorProduct.includeRight : S →ₐ[R] p.Fiber S).toRingHom q
```

## Tag 05IH, a lemma

[Tag 05IH](https://stacks.math.columbia.edu/tag/05IH) in the Stacks Project.

**`Stacks.Divisors.isWeaklyAssociatedPoint_tensorPullback_iff_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociatedTensorPullbackIff.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociatedTensorPullbackIff.lean#L118).

> Let `S` be a scheme, let `f : X ⟶ S` be locally of finite type, let `x ∈ X`, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type and let `G` be a quasi-coherent `𝒪_S`-module. If `F` is
> flat at `x` over `S`, then `x` is weakly associated to `F ⊗_{𝒪_X} f^*G` if and only if `f x` is
> weakly associated to `G` and `x` is an associated point of the restriction of `F` to the fibre
> `X_{f x}`, that is, `x` lies in the relative assassin `Ass_{X/S}(F)`.

```lean
theorem isWeaklyAssociatedPoint_tensorPullback_iff_of_finiteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) (G : S.Modules) [F.IsQuasicoherent] [F.IsFiniteType] [G.IsQuasicoherent]
    (x : X) (hF : IsFlatOverAt f.toLRSHom.toShHom F x) :
    IsWeaklyAssociatedPoint
        ((((Stacks.SheafOfModules.Tensor.sheafTensor
                  ⟨((X.toLocallyRingedSpace.toRingedSpace)).presheaf,
                    ((X.toLocallyRingedSpace.toRingedSpace)).IsSheaf⟩).obj (F)).obj
              (((Scheme.Modules.pullback f).obj G)))) x ↔
      (IsWeaklyAssociatedPoint G (f x) ∧ x ∈ relativeAssassin f F)
```

## Tag 05II, a lemma

[Tag 05II](https://stacks.math.columbia.edu/tag/05II) in the Stacks Project.

**`Stacks.WeaklyAssociatedPrimes.weaklyAssociatedPrimes_tensorProduct_eq_fibrewise_assStacks_of_small`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/TensorFibreEssentiallyFiniteType.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/TensorFibreEssentiallyFiniteType.lean#L449). The attribute's comment: “the full set equality; the two rings lie in one universe, as `IsEssentiallyOfFiniteType` requires, and the modules are in arbitrary universes”.

> **[Stacks, Tag 05II].** For `R → S` essentially of finite type, `N` a localization of a
> finite `S`-module flat over `R` and `M` any `R`-module, the weakly associated primes of
> `N ⊗[R] M` are the contractions of the primes of the fibre rings `S ⊗[R] κ(p)` associated to the
> fibre modules, over the weakly associated primes `p` of `M`.

```lean
theorem weaklyAssociatedPrimes_tensorProduct_eq_fibrewise_assStacks_of_small
    (R S : Type u) (M : Type v) (N₀ : Type w) (N : Type x)
    [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module R M]
    [AddCommGroup N₀] [Module S N₀] [Module.Finite S N₀]
    [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Flat R N]
    (hfinite : IsEssentiallyOfFiniteType R S (algebraMap R S))
    (T : Submonoid S) (f : N₀ →ₗ[S] N) [IsLocalizedModule T f] :
    weaklyAssociatedPrimes S (N ⊗[R] M) =
      {q : Ideal S | ∃ p ∈ weaklyAssociatedPrimes R M, ∃ hp : p.IsPrime,
        letI : p.IsPrime := hp
        ∃ q' ∈ assStacks (S ⊗[R] p.ResidueField)
          ((S ⊗[R] p.ResidueField) ⊗[S] N),
          q = Ideal.comap (Algebra.TensorProduct.includeLeft (R := R)
            (S := S) (A := S) (B := p.ResidueField)).toRingHom q'}
```

**`Stacks.WeaklyAssociatedPrimes.weaklyAssociatedPrimes_tensorProduct_eq_fibrewise_assStacks_of_small'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/TensorFibreFormulaEssentiallyFiniteType.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/WeaklyAssociatedPrime/TensorFibreFormulaEssentiallyFiniteType.lean#L143). The attribute's comment: “the full set equality, for a module in the universe of the two rings”.

> For `M` in the universe of the two rings, the weakly associated primes of `N ⊗[R] M` are the
> contractions of the primes of the fibre rings associated to the fibre modules, over the weakly
> associated primes of `M`.

```lean
theorem weaklyAssociatedPrimes_tensorProduct_eq_fibrewise_assStacks_of_small'
    (R S : Type u) (M : Type u) (N₀ : Type w) (N : Type x)
    [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module R M]
    [AddCommGroup N₀] [Module S N₀] [Module.Finite S N₀]
    [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Flat R N]
    (hfinite : IsEssentiallyOfFiniteType R S (algebraMap R S))
    (T : Submonoid S) (f : N₀ →ₗ[S] N) [IsLocalizedModule T f] :
    weaklyAssociatedPrimes S (N ⊗[R] M) =
      {q : Ideal S | ∃ p ∈ weaklyAssociatedPrimes R M, ∃ hp : p.IsPrime,
        letI : p.IsPrime := hp
        ∃ q' ∈ assStacks (S ⊗[R] p.ResidueField)
          ((S ⊗[R] p.ResidueField) ⊗[S] N),
          q = Ideal.comap (Algebra.TensorProduct.includeLeft (R := R)
            (S := S) (A := S) (B := p.ResidueField)).toRingHom q'}
```

## Tag 05IJ, a lemma

[Tag 05IJ](https://stacks.math.columbia.edu/tag/05IJ) in the Stacks Project.

**`Stacks.Divisors.weaklyAssociatedPoints_tensorPullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociatedTensorPullbackFormula.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/WeaklyAssociatedTensorPullbackFormula.lean#L89). The attribute's comment: “the set equality for f locally of finite type, F quasi-coherent of finite type and flat over S, G quasi-coherent; unconditional”.

> **[Stacks, Tag 05IJ].** Let `f : X ⟶ S` be locally of finite type, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type which is flat over `S`, and let `G` be a
> quasi-coherent `𝒪_S`-module. Then the weakly associated points of `F ⊗_{𝒪_X} f^*G` are exactly
> the points of the fibres `X_s`, over the weakly associated points `s` of `G`, that are
> associated to the restriction of `F` to `X_s`.
>
> This is the global form of Tag 05IH, and the source's proof of it is the pointwise statement
> plus the passage to sets. Both are already in
> `StacksFrontier.AlgebraicGeometry.Flatness.WeaklyAssociatedTensorPullbackGlobal`, up to the same
> algebraic input that Tag 05IH needed; supplying it here removes the hypothesis.

```lean
theorem weaklyAssociatedPoints_tensorPullback_eq
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) (G : S.Modules)
    [F.IsQuasicoherent] [F.IsFiniteType] [G.IsQuasicoherent]
    (hF : IsFlatOver f.toLRSHom.toShHom F) :
    weaklyAssociatedPoints
        (((Stacks.SheafOfModules.Tensor.sheafTensor
              ⟨(X.toLocallyRingedSpace.toRingedSpace).presheaf,
                (X.toLocallyRingedSpace.toRingedSpace).IsSheaf⟩).obj F).obj
          ((Scheme.Modules.pullback f).obj G)) =
      ⋃ s ∈ weaklyAssociatedPoints G,
        f.fiberι s '' associatedPoints ((Scheme.Modules.pullback (f.fiberι s)).obj F)
```

## Tag 05IK, a theorem

[Tag 05IK](https://stacks.math.columbia.edu/tag/05IK) in the Stacks Project.

**`AlgebraicGeometry.isOpen_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocus.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocus.lean#L231). The attribute's comment: “openness of the relative flat locus”. References: EGA IV (11.1.6), “case C = B”; EGA IV (11.3.3), “wk assoc pts loc finite”; SGA 3 VIB (13.1), “(i) U open”.

> **Stacks Project, Tag 05IK (openness).** The locus where a quasi-coherent module of finite
> type is flat over the target of a morphism locally of finite presentation is open, provided the
> weakly associated points of the target are locally finite.

```lean
theorem isOpen_flatLocus
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hS : ∀ s : S, ∃ W : S.Opens, s ∈ W ∧
      (schemeWeaklyAssociatedPoints S ∩ (W : Set S)).Finite) :
    IsOpen (flatLocus f F)
```

**`AlgebraicGeometry.isFinitePresentation_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocus.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocus.lean#L352). The attribute's comment: “finite presentation on the flat locus”.

> **Stacks Project, Tag 05IK (finite presentation on the flat locus).** For a morphism locally
> of finite presentation whose target has locally finite weakly associated points, a quasi-coherent
> module of finite type restricts to a module of finite presentation on the open subscheme that is
> its relative flat locus.

```lean
theorem isFinitePresentation_flatLocus
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hS : ∀ s : S, ∃ W : S.Opens, s ∈ W ∧
      (schemeWeaklyAssociatedPoints S ∩ (W : Set S)).Finite) :
    letI U : X.Opens := ⟨flatLocus f F, isOpen_flatLocus f F hS⟩
    (F.restrict U.ι).IsFinitePresentation
```

**`AlgebraicGeometry.isFlatOver_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocus.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocus.lean#L366). The attribute's comment: “flatness over the base on the flat locus”.

> **Stacks Project, Tag 05IK (flatness on the flat locus).** For a morphism locally of finite
> presentation whose target has locally finite weakly associated points, a quasi-coherent module of
> finite type restricts to a module flat over the base on the open subscheme that is its relative
> flat locus.

```lean
theorem isFlatOver_flatLocus
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hS : ∀ s : S, ∃ W : S.Opens, s ∈ W ∧
      (schemeWeaklyAssociatedPoints S ∩ (W : Set S)).Finite) :
    letI U : X.Opens := ⟨flatLocus f F, isOpen_flatLocus f F hS⟩
    IsFlatOver (U.ι ≫ f).toLRSHom.toShHom (F.restrict U.ι)
```

## Tag 05IL, a lemma

[Tag 05IL](https://stacks.math.columbia.edu/tag/05IL) in the Stacks Project.

**`Stacks.Flatness.isOpen_setOf_flat_localizedModule_atPrime_of_finite_weaklyAssociatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatLocusFiniteModuleOpenness.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FlatLocusFiniteModuleOpenness.lean#L74). The attribute's comment: “openness of the relative flat locus”. References: EGA IV (11.1.6), “case C = B”; EGA IV (11.3.3), “WeakAss finite”.

> **Stacks Project, Tag 05IL (openness).** For a ring map `R → S` of finite presentation and a
> finite `S`-module `M`, the locus of primes `q` of `S` at which `M_q` is flat over `R` is open in
> `Spec S`, provided `R` has only finitely many weakly associated primes.

```lean
theorem isOpen_setOf_flat_localizedModule_atPrime_of_finite_weaklyAssociatedPrimes
    (hR : (weaklyAssociatedPrimes R R).Finite) :
    IsOpen {q : PrimeSpectrum S | Module.Flat R (LocalizedModule.AtPrime q.asIdeal M)}
```

**`Stacks.Flatness.finitePresentation_localizedModule_away_of_basicOpen_subset_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatLocusFiniteModuleOpenness.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FlatLocusFiniteModuleOpenness.lean#L111). The attribute's comment: “finite presentation on a basic open inside the flat locus”.

> **Stacks Project, Tag 05IL (finite presentation on a basic open).** For a ring map `R → S` of
> finite presentation and a finite `S`-module `M`, if the basic open `D(g)` is contained in the
> locus where `M` is flat over `R`, then `M_g` is a finitely presented `S_g`-module, provided `R`
> has only finitely many weakly associated primes.

```lean
theorem finitePresentation_localizedModule_away_of_basicOpen_subset_flatLocus
    (hR : (weaklyAssociatedPrimes R R).Finite) (g : S)
    (hg : (↑(PrimeSpectrum.basicOpen g) : Set (PrimeSpectrum S)) ⊆
      {q : PrimeSpectrum S | Module.Flat R (LocalizedModule.AtPrime q.asIdeal M)}) :
    Module.FinitePresentation (Localization.Away g) (LocalizedModule.Away g M)
```

**`Stacks.Flatness.OpenFlatLocus.flat_localizedModule_away_of_forall_flat_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/OpenFlatLocusNoetherian.lean, line 877](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/OpenFlatLocusNoetherian.lean#L877). The attribute's comment: “flatness over the base”.

> **Flatness over the base spreads from the points of a basic open to the basic open itself.** If
> `M_{𝔮}` is flat over `R` for every prime `𝔮` of `S` with `g ∉ 𝔮`, then `M_g` is flat over `R`.
>
> Flatness over `R` is local on `Spec (S_g)` (`Module.flat_of_isLocalized_maximal`), and the local
> ring of `M_g` at a prime `P` of `S_g` is the localization of `M` at the prime `P ∩ S` of `S`:
> `(S_g)_P` is the localization of `S` at `P ∩ S`
> (`IsLocalization.isLocalization_atPrime_localization_atPrime`), and a composite of two base changes
> is a base change (`IsBaseChange.comp`).

```lean
theorem flat_localizedModule_away_of_forall_flat_atPrime {R S M : Type*} [CommRing R]
    [CommRing S]
    [Algebra R S] [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M] (g : S)
    (H : ∀ q : PrimeSpectrum S, q ∈ PrimeSpectrum.basicOpen g →
      Module.Flat R (LocalizedModule.AtPrime q.asIdeal M)) :
    Module.Flat R (LocalizedModule.Away g M)
```

## Tag 05IM, a lemma

[Tag 05IM](https://stacks.math.columbia.edu/tag/05IM) in the Stacks Project.

**`AlgebraicGeometry.isOpen_setOf_isFlatAt_of_locallyOfFiniteType_of_locally_finite_weakAss`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/FlatLocus.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/FlatLocus.lean#L44). The attribute's comment: “openness of the locus of flatness”.

> **Openness of the flat locus.** For a morphism `f : X ⟶ S` locally of finite type whose base
> has locally finite weakly associated points, the set of points at which `f` is flat is open.

```lean
theorem isOpen_setOf_isFlatAt_of_locallyOfFiniteType_of_locally_finite_weakAss
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (hS : ∀ s : S, ∃ V : S.Opens, s ∈ V ∧
      (schemeWeaklyAssociatedPoints S ∩ (V : Set S)).Finite) :
    IsOpen {x : X | IsFlatAt f.toLRSHom.toShHom x}
```

**`AlgebraicGeometry.locallyOfFinitePresentation_restrict_of_subset_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/FlatLocus.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/FlatLocus.lean#L106). The attribute's comment: “the flat locus is locally of finite presentation over the base”.

> **Finite presentation on the flat locus.** For a morphism `f : X ⟶ S` locally of finite type
> whose base has locally finite weakly associated points, the restriction of `f` to an open
> subscheme contained in the locus of points of flatness is locally of finite presentation.

```lean
theorem locallyOfFinitePresentation_restrict_of_subset_flatLocus
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (hS : ∀ s : S, ∃ V : S.Opens, s ∈ V ∧
      (schemeWeaklyAssociatedPoints S ∩ (V : Set S)).Finite)
    (U : X.Opens) (hU : (U : Set X) ⊆ {x : X | IsFlatAt f.toLRSHom.toShHom x}) :
    LocallyOfFinitePresentation (U.ι ≫ f)
```

**`AlgebraicGeometry.flat_of_subset_setOf_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/PointwiseOpenLocus.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/PointwiseOpenLocus.lean#L88). The attribute's comment: “the flat locus is flat over the base”.

> A morphism which is flat at every point of an open subscheme of its source is flat after
> restriction to that open subscheme.

```lean
theorem flat_of_subset_setOf_isFlatAt {X S : Scheme.{u}} (f : X ⟶ S) (V : X.Opens)
    (hV : (V : Set X) ⊆ {x : X | IsFlatAt f.toLRSHom.toShHom x}) :
    Flat (V.ι ≫ f)
```

## Tag 05IN, a lemma

[Tag 05IN](https://stacks.math.columbia.edu/tag/05IN) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_flat_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/FlatLocus.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/FlatLocus.lean#L55).

> A morphism locally of finite type and flat over an integral base is locally of finite
> presentation.

```lean
theorem locallyOfFinitePresentation_of_flat_of_isIntegral
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [Flat f] [IsIntegral S] :
    LocallyOfFinitePresentation f
```

## Tag 053G, a proposition

[Tag 053G](https://stacks.math.columbia.edu/tag/053G) in the Stacks Project.

**`Stacks.Flatness.finitePresentation_of_flat_of_finiteType_of_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean#L149). The attribute's comment: “(1): a flat algebra of finite type over a domain is of finite presentation”.

> **Stacks Project, Tag 053G, part (1).** A flat algebra of finite type over a domain is of
> finite presentation.

```lean
theorem finitePresentation_of_flat_of_finiteType_of_isDomain
    {R : Type u} [CommRing R] [IsDomain R] {S : Type v} [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] [Module.Flat R S] :
    Algebra.FinitePresentation R S
```

**`Stacks.Flatness.finitePresentation_of_finite_of_flat_of_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean#L158). The attribute's comment: “(2): a finite module flat over a domain is finitely presented”.

> **Stacks Project, Tag 053G, part (2).** A finite module over an algebra of finite type over a
> domain is finitely presented as soon as it is flat over the domain.

```lean
theorem finitePresentation_of_finite_of_flat_of_isDomain
    {R : Type u} [CommRing R] [IsDomain R] {S : Type v} [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] {M : Type w} [AddCommGroup M] [Module S M] [Module R M]
    [IsScalarTower R S M] [Module.Finite S M] [Module.Flat R M] :
    Module.FinitePresentation S M
```

## Tag 05IQ, a lemma

[Tag 05IQ](https://stacks.math.columbia.edu/tag/05IQ) in the Stacks Project.

**`AlgebraicGeometry.isOpen_flatLocus_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocusFiniteType.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocusFiniteType.lean#L169). The attribute's comment: “openness of the relative flat locus”. References: SGA 3 VIB (13.1), “(i) U open”.

> **Stacks Project, Tag 05IQ (openness).** The locus where a quasi-coherent module of finite
> type is flat over the target of a morphism locally of finite type is open, provided the weakly
> associated points of the target are locally finite.

```lean
theorem isOpen_flatLocus_of_locallyOfFiniteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hS : ∀ s : S, ∃ W : S.Opens, s ∈ W ∧
      (schemeWeaklyAssociatedPoints S ∩ (W : Set S)).Finite) :
    IsOpen (flatLocus f F)
```

**`AlgebraicGeometry.isFlatOver_flatLocus_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocusFiniteType.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocusFiniteType.lean#L293). The attribute's comment: “flatness over the base on the flat locus”.

> **Stacks Project, Tag 05IQ (flatness on the flat locus).** The restriction of the module to
> its relative flat locus is flat over the base.

```lean
theorem isFlatOver_flatLocus_of_locallyOfFiniteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hS : ∀ s : S, ∃ W : S.Opens, s ∈ W ∧
      (schemeWeaklyAssociatedPoints S ∩ (W : Set S)).Finite) :
    letI U : X.Opens := ⟨flatLocus f F, isOpen_flatLocus_of_locallyOfFiniteType f F hS⟩
    IsFlatOver (U.ι ≫ f).toLRSHom.toShHom (F.restrict U.ι)
```

**`AlgebraicGeometry.isFinitelyPresentedRelative_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocusFiniteType.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteTypeII/ModuleFlatLocusFiniteType.lean#L306). The attribute's comment: “relative finite presentation on the flat locus”.

> **Stacks Project, Tag 05IQ (relative finite presentation on the flat locus).** The
> restriction of the module to its relative flat locus is finitely presented relative to the
> base.

```lean
theorem isFinitelyPresentedRelative_flatLocus
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hS : ∀ s : S, ∃ W : S.Opens, s ∈ W ∧
      (schemeWeaklyAssociatedPoints S ∩ (W : Set S)).Finite) :
    letI U : X.Opens := ⟨flatLocus f F, isOpen_flatLocus_of_locallyOfFiniteType f F hS⟩
    IsFinitelyPresentedRelative (U.ι ≫ f) (F.restrict U.ι)
```

## Tag 05IR, a lemma

[Tag 05IR](https://stacks.math.columbia.edu/tag/05IR) in the Stacks Project.

**`Stacks.Flatness.isOpen_setOf_flat_localizedModule_atPrime_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean#L92). The attribute's comment: “openness of the relative flat locus”. References: EGA IV (11.1.6), “case C = B”; EGA IV (11.3.3), “WeakAss finite”.

> **Stacks Project, Tag 05IR (openness).** For a ring map `R → S` of finite type and a finite
> `S`-module `M`, the locus of primes `q` of `S` at which `M_q` is flat over `R` is open in
> `Spec S`, provided `R` has only finitely many weakly associated primes.

```lean
theorem isOpen_setOf_flat_localizedModule_atPrime_of_finiteType
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    {M : Type w} [AddCommGroup M] [Module S M] [Module R M] [IsScalarTower R S M]
    [Module.Finite S M] (hR : (weaklyAssociatedPrimes R R).Finite) :
    IsOpen {q : PrimeSpectrum S | Module.Flat R (LocalizedModule.AtPrime q.asIdeal M)}
```

**`Stacks.Flatness.finitePresentationRel_localizedModule_away_of_basicOpen_subset_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FlatLocusFiniteTypeAlgebra.lean#L171). The attribute's comment: “relative finite presentation on a basic open inside the flat locus”.

> **Stacks Project, Tag 05IR (relative finite presentation on a basic open).** For a ring map
> `R → S` of finite type and a finite `S`-module `M`, if the basic open `D(g)` is contained in the
> locus where `M` is flat over `R`, then `M_g` is an `S_g`-module finitely presented relative to
> `R`, provided `R` has only finitely many weakly associated primes.

```lean
theorem finitePresentationRel_localizedModule_away_of_basicOpen_subset_flatLocus
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    {M : Type w} [AddCommGroup M] [Module S M] [Module R M] [IsScalarTower R S M]
    [Module.Finite S M] (hR : (weaklyAssociatedPrimes R R).Finite) (g : S)
    (hg : (↑(PrimeSpectrum.basicOpen g) : Set (PrimeSpectrum S)) ⊆
      {q : PrimeSpectrum S | Module.Flat R (LocalizedModule.AtPrime q.asIdeal M)}) :
    Module.FinitePresentationRel R (Localization.Away g) (LocalizedModule.Away g M)
```

**`Stacks.Flatness.OpenFlatLocus.flat_localizedModule_away_of_forall_flat_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/OpenFlatLocusNoetherian.lean, line 877](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/OpenFlatLocusNoetherian.lean#L877). The attribute's comment: “flatness over the base”.

> **Flatness over the base spreads from the points of a basic open to the basic open itself.** If
> `M_{𝔮}` is flat over `R` for every prime `𝔮` of `S` with `g ∉ 𝔮`, then `M_g` is flat over `R`.
>
> Flatness over `R` is local on `Spec (S_g)` (`Module.flat_of_isLocalized_maximal`), and the local
> ring of `M_g` at a prime `P` of `S_g` is the localization of `M` at the prime `P ∩ S` of `S`:
> `(S_g)_P` is the localization of `S` at `P ∩ S`
> (`IsLocalization.isLocalization_atPrime_localization_atPrime`), and a composite of two base changes
> is a base change (`IsBaseChange.comp`).

```lean
theorem flat_localizedModule_away_of_forall_flat_atPrime {R S M : Type*} [CommRing R]
    [CommRing S]
    [Algebra R S] [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M] (g : S)
    (H : ∀ q : PrimeSpectrum S, q ∈ PrimeSpectrum.basicOpen g →
      Module.Flat R (LocalizedModule.AtPrime q.asIdeal M)) :
    Module.Flat R (LocalizedModule.Away g M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.13, Tag 05IF](https://stacks.math.columbia.edu/tag/05IF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
