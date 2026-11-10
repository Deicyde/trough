---
declaration: section
origin: cited
lean: Module.Flat.of_isMaximalCohenMacaulay_of_ringKrullDim_eq_add, Module.Flat.of_ofList_eq_maximalIdeal_of_isWeaklyRegular_map, Module.Flat.exists_ge_flat_of_isColimit, Module.Flat.injective_and_flat_quotient_range_of_injective_mapQ_maximalIdeal, Module.Flat.isSMulRegular_and_flat_quotient_span_of_isSMulRegular_quotient, Module.Flat.isSMulRegular_and_flat_quotient_smul_of_isSMulRegular_maximalIdeal, Module.Flat.isRegular_and_flat_quotient_ofList_smul_of_isRegular_maximalIdeal, Module.Flat.of_rTensor_subtype_injective_of_flat_quotient_of_essentiallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 10.128 More flatness criteria

Section 10.128 of the Stacks Project, [Tag 00R3](https://stacks.math.columbia.edu/tag/00R3). 10 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00R4, a lemma

[Tag 00R4](https://stacks.math.columbia.edu/tag/00R4) in the Stacks Project.

**`Module.Flat.of_isMaximalCohenMacaulay_of_ringKrullDim_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/MiracleFlatness.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/MiracleFlatness.lean#L292). The attribute's comment: “Regularity of the Noetherian local ring `R` is `IsRegularLocalRing R`; Cohen-Macaulayness of `S` (Definition 00N8) is `Module.IsMaximalCohenMacaulay S S`, i.e. `depth_{𝔪_S}(S) = dim S`; and `dim(S/𝔪_R S)` is the Krull dimension of the quotient of `S` by the image ideal of the maximal ideal of `R`. See the module docstring.”. References: EGA IV (6.1.5), “case M = B”; EGA IV (15.4.2), “e′)⇒b), partial”.

> **Miracle flatness, Stacks 00R4.** Let `R → S` be a local homomorphism of Noetherian local
> rings with `R` regular and `S` Cohen–Macaulay, i.e. `depth_{𝔪_S}(S) = dim(S)`. If
> `dim(S) = dim(R) + dim(S/𝔪_R S)`, then `S` is flat over `R`.

```lean
public theorem Module.Flat.of_isMaximalCohenMacaulay_of_ringKrullDim_eq_add
    {R S : Type*} [CommRing R] [IsRegularLocalRing R] [CommRing S] [IsLocalRing S]
    [IsNoetherianRing S] [Algebra R S] [IsLocalHom (algebraMap R S)]
    (hS : Module.IsMaximalCohenMacaulay S S)
    (hdim : ringKrullDim S =
      ringKrullDim R + ringKrullDim (S ⧸ (maximalIdeal R).map (algebraMap R S))) :
    Module.Flat R S
```

## Tag 07DY, a lemma

[Tag 07DY](https://stacks.math.columbia.edu/tag/07DY) in the Stacks Project.

**`Module.Flat.of_ofList_eq_maximalIdeal_of_isWeaklyRegular_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/RegularSequence.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/RegularSequence.lean#L214). The attribute's comment: “Stated for a finite `S`-module `M` in place of `S` itself, the source's statement being the case `M = S`; a regular system of parameters is a list generating the maximal ideal whose length is its minimal number of generators; and the source's regular sequence is weakened to `RingTheory.Sequence.IsWeaklyRegular`, its nonvanishing clause being replaced by `IsLocalHom`. See the module docstring.”.

> Let `R` be a regular local ring, let `xs = x₁, …, x_d` be a regular system of parameters of
> `R`, that is, a list generating `𝔪_R` whose length is the minimal number of generators of `𝔪_R`,
> let `S` be a Noetherian local ring receiving a local homomorphism from `R` and let `M` be a
> finite `S`-module. If the images of `x₁, …, x_d` in `S` form a weakly `M`-regular sequence, then
> `M` is flat over `R`. Taking `M = S` shows that `R → S` is flat.

```lean
public theorem Module.Flat.of_ofList_eq_maximalIdeal_of_isWeaklyRegular_map
    {R : Type*} (S : Type*) (M : Type*) [CommRing R] [IsRegularLocalRing R] [CommRing S]
    [IsLocalRing S] [IsNoetherianRing S] [Algebra R S] [IsLocalHom (algebraMap R S)]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M] [Module.Finite S M]
    (xs : List R) (hxs : Ideal.ofList xs = maximalIdeal R)
    (hmin : xs.length = (maximalIdeal R).spanFinrank)
    (hreg : IsWeaklyRegular M (xs.map (algebraMap R S))) :
    Module.Flat R M
```

## Tag 00R6, a lemma

[Tag 00R6](https://stacks.math.columbia.edu/tag/00R6) in the Stacks Project.

**`Module.Flat.exists_ge_flat_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/Flat.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/SpreadingOut/Flat.lean#L101). The attribute's comment: “The system "as in Lemma 00QX" is spelled out as the data and the six conditions concluded by `RingHom.EssentiallyOfFinitePresentation.exists_isColimit_essFiniteType_module`, together with locality of the transition maps `A i → A j`, which is the source's "system of local homomorphisms of local rings" read as a system in the category of local rings and is what 00MO needs to know `(𝔪 i) A j` is proper. The hypotheses of 00QX are not assumed, being either unused or consequences of the system. The conclusion is the cofinal form (`∀ i, ∃ j ≥ i`), which is what the source's proof produces and what the dependents use. See the module docstring.”.

> Let `(A i → B i, N i)` be a directed system as in 00QX, with colimits `R → S` and `M`: each
> `A i` is essentially of finite type over `ℤ`, each `A i → B i` is a local homomorphism of local
> rings essentially of finite type, each transition map `A i → A j` is local, each `N i` is a finite
> `B i`-module, each `B j` is a localization of `B i ⊗_{A i} A j` at a prime ideal, and each `N j` is
> the base change of `N i` along `B i → B j`. If `M` is flat over `R`, then for every index `i` there
> is `j ≥ i` such that `N j` is flat over `A j`.

```lean
public theorem exists_ge_flat_of_isColimit
    {R S M : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M] [Module.Flat R M]
    {Λ : Type u} [Preorder Λ] [Nonempty Λ] [IsDirected Λ (· ≤ ·)]
    {A B : Λ ⥤ CommRingCat.{u}} {φ : A ⟶ B} {N : Λ ⥤ AddCommGrpCat.{u}}
    (mod : ∀ i, Module (B.obj i) (N.obj i))
    (hsmul : ∀ ⦃i j : Λ⦄ (h : i ⟶ j) (b : B.obj i) (m : N.obj i),
      N.map h (b • m) = B.map h b • N.map h m)
    {ρ : A ⟶ (Functor.const Λ).obj (CommRingCat.of R)}
    {σ : B ⟶ (Functor.const Λ).obj (CommRingCat.of S)}
    {ν : N ⟶ (Functor.const Λ).obj (AddCommGrpCat.of M)}
    (hR : IsColimit (Cocone.mk (CommRingCat.of R) ρ))
    (_hS : IsColimit (Cocone.mk (CommRingCat.of S) σ))
    (hM : IsColimit (Cocone.mk (AddCommGrpCat.of M) ν))
    (hφ : ∀ i, φ.app i ≫ σ.app i = ρ.app i ≫ CommRingCat.ofHom (algebraMap R S))
    (hν : ∀ (i : Λ) (b : B.obj i) (m : N.obj i),
      (ν.app i (b • m) : M) = HSMul.hSMul (α := S) (β := M) (σ.app i b) (ν.app i m))
    (hAlocal : ∀ i, IsLocalRing (A.obj i)) (hBlocal : ∀ i, IsLocalRing (B.obj i))
    (hφlocal : ∀ i, IsLocalHom (φ.app i).hom)
    (hAmaplocal : ∀ ⦃i j : Λ⦄ (h : i ⟶ j), IsLocalHom (A.map h).hom)
    (hAft : ∀ i, Algebra.EssFiniteType ℤ (A.obj i))
    (hφft : ∀ i, (φ.app i).hom.EssFiniteType)
    (hNfin : ∀ i, Module.Finite (B.obj i) (N.obj i))
    (hBloc : ∀ ⦃i j : Λ⦄ (h : i ⟶ j),
      letI := (pushout.desc (B.map h) (φ.app j) (φ.naturality h).symm).hom.toAlgebra
      ∃ (q : Ideal ↑(pushout (φ.app i) (A.map h))) (_ : q.IsPrime),
        IsLocalization q.primeCompl ↑(B.obj j))
    (hNbc : ∀ ⦃i j : Λ⦄ (h : i ⟶ j),
      letI : Algebra ↑(B.obj i) ↑(B.obj j) := (B.map h).hom.toAlgebra
      letI : Module ↑(B.obj i) ↑(N.obj j) := Module.compHom _ (B.map h).hom
      letI : IsScalarTower ↑(B.obj i) ↑(B.obj j) ↑(N.obj j) :=
        .of_algebraMap_smul fun _ _ => rfl
      IsBaseChange ↑(B.obj j)
        (⟨(N.map h).hom.toAddHom, hsmul h⟩ : ↑(N.obj i) →ₗ[↑(B.obj i)] ↑(N.obj j)))
    (i : Λ) :
    ∃ j, i ≤ j ∧
      (letI : Module ↑(A.obj j) ↑(N.obj j) := Module.compHom _ (φ.app j).hom
       Module.Flat ↑(A.obj j) ↑(N.obj j))
```

## Tag 046Y, a lemma

[Tag 046Y](https://stacks.math.columbia.edu/tag/046Y) in the Stacks Project.

**`Module.Flat.injective_and_flat_quotient_range_of_injective_mapQ_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriterionNonNoetherian.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriterionNonNoetherian.lean#L279). The attribute's comment: “`M/𝔪M` is `M ⧸ 𝔪 • (⊤ : Submodule R M)` and `ū` the canonical `Submodule.mapQ` of `u`. Hypothesis (1) is `RingHom.EssentiallyOfFinitePresentation` (Definition 00QM (2)), Mathlib having no such predicate. The cokernel `N/u(M)` is `N ⧸ LinearMap.range u`, and the two conclusions are conjoined; see the module docstring.”. References: SGA 1 IV (5.7), “(ii) ⟹ (i)”.

> Let `R → S` be a local homomorphism of local rings with `S` essentially of finite presentation
> over `R`, let `𝔪` be the maximal ideal of `R`, and let `u : M → N` be a map of `S`-modules with
> `M`, `N` of finite presentation over `S` and `N` flat over `R`. If the induced map
> `ū : M/𝔪M → N/𝔪N` is injective, then `u` is injective and `N/u(M)` is flat over `R`.
>
> Here `M/𝔪M` is `M ⧸ 𝔪 • ⊤` and `ū` is the canonical `Submodule.mapQ`, which sends the class of `x`
> to the class of `u x`.

```lean
public theorem Module.Flat.injective_and_flat_quotient_range_of_injective_mapQ_maximalIdeal
    {R S M N : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N]
    [Module.FinitePresentation S M] [Module.FinitePresentation S N] [Module.Flat R N]
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation) (u : M →ₗ[S] N)
    (hu :
      Function.Injective
        (Submodule.mapQ (maximalIdeal R • (⊤ : Submodule R M))
          (maximalIdeal R • (⊤ : Submodule R N)) (u.restrictScalars R)
          (Submodule.smul_top_le_comap_smul_top (maximalIdeal R) (u.restrictScalars R)))) :
    Function.Injective u ∧ Module.Flat R (N ⧸ LinearMap.range u)
```

## Tag 046Z, a lemma

[Tag 046Z](https://stacks.math.columbia.edu/tag/046Z) in the Stacks Project.

**`Module.Flat.isSMulRegular_and_flat_quotient_span_of_isSMulRegular_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceRegularParameter.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceRegularParameter.lean#L238). The attribute's comment: “the case M := S, spelled with ring quotients by ideals”. References: EGA IV (11.3.8), “(c) ⇒ (a), special case”.

> **Stacks 046Z with both quotients taken by ideals.** Let `R → S` be a local homomorphism of
> local rings which is essentially of finite presentation and makes `S` flat over `R`. If `a ∈ S`
> is a nonzerodivisor on the fibre `S ⧸ 𝔪S`, then `a` is a nonzerodivisor on `S` and `S ⧸ (a)` is
> again flat over `R`.
>
> This is the `M = S` case of
> `Module.Flat.isSMulRegular_and_flat_quotient_smul_of_isSMulRegular_maximalIdeal`, restated with
> the fibre and the quotient written as quotients of the ring by ideals rather than as quotients of
> the module `S` by `I • ⊤`. The two agree because extending an ideal to the top submodule of the
> ring returns the ideal, and that identification is an equality of submodules, so the hypothesis
> and the conclusion are transported along `Submodule.quotEquivOfEq` rather than compared as
> types.

```lean
public theorem Module.Flat.isSMulRegular_and_flat_quotient_span_of_isSMulRegular_quotient
    {R S : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [Module.Flat R S]
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation) {a : S}
    (ha : IsSMulRegular (S ⧸ Ideal.map (algebraMap R S) (maximalIdeal R)) a) :
    IsSMulRegular S a ∧ Module.Flat R (S ⧸ Ideal.span {a})
```

**`Module.Flat.isSMulRegular_and_flat_quotient_smul_of_isSMulRegular_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/RegularSequenceOverBase.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/RegularSequenceOverBase.lean#L70). The attribute's comment: “Stated in module form (the source's case is `M := S`), with `𝔪M` spelled `Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S M)` and `fM` spelled `Ideal.span {f} • ⊤`, and "nonzerodivisor" spelled `IsSMulRegular`. Hypothesis (1) is `RingHom.EssentiallyOfFinitePresentation` (Definition 00QM (2)), Mathlib having no such predicate. The two conclusions are conjoined; see the module docstring.”. References: EGA IV (11.3.8), “(c) ⇒ (a), special case”.

> **Stacks 046Z.** Let `R → S` be a local homomorphism of local rings with `S` essentially of
> finite presentation over `R`, let `𝔪` be the maximal ideal of `R`, and let `M` be an `S`-module of
> finite presentation which is flat over `R`. If `f ∈ S` is a nonzerodivisor on the fibre `M/𝔪M`,
> then `f` is a nonzerodivisor on `M` and `M/fM` is flat over `R`.
>
> The source is the case `M = S`: `f` is a nonzerodivisor in `S` and `S/fS` is flat over `R`. Here
> `𝔪M` is `𝔪S • ⊤` and `fM` is `Ideal.span {f} • ⊤`; see the module docstring.

```lean
public theorem Module.Flat.isSMulRegular_and_flat_quotient_smul_of_isSMulRegular_maximalIdeal
    {R S M : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.FinitePresentation S M] [Module.Flat R M]
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation) {f : S}
    (hf :
      IsSMulRegular (M ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S M))) f) :
    IsSMulRegular M f ∧ Module.Flat R (M ⧸ (Ideal.span {f} • (⊤ : Submodule S M)))
```

## Tag 0470, a lemma

[Tag 0470](https://stacks.math.columbia.edu/tag/0470) in the Stacks Project.

**`Module.Flat.isRegular_and_flat_quotient_ofList_smul_of_isRegular_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/RegularSequenceOverBase.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/RegularSequenceOverBase.lean#L172). The attribute's comment: “Stated in module form (the source's case is `M := S`), with the sequence a `List S`, `𝔪M` spelled `Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S M)` and the partial quotients spelled `M ⧸ Ideal.ofList (fs.take i) • ⊤`. "Regular sequence" is Mathlib's `RingTheory.Sequence.IsRegular`, which is Definition 00LF verbatim (nonvanishing clause included). Hypothesis (1) is `RingHom.EssentiallyOfFinitePresentation` (Definition 00QM (2)), Mathlib having no such predicate. The two conclusions are conjoined; see the module docstring.”. References: EGA 0 (15.1.16), “c)=>a), ess fin pres”; EGA 0 (15.1.17), “(f_i) is M-regular”; EGA IV (11.3.8), “c) ⇒ a)”.

> **Stacks 0470.** Let `R → S` be a local homomorphism of local rings with `S` essentially of
> finite presentation over `R`, let `𝔪` be the maximal ideal of `R`, and let `M` be an `S`-module of
> finite presentation which is flat over `R`. If a sequence `f₁, …, f_c` of elements of `S` is
> regular on the fibre `M/𝔪M`, then it is regular on `M` and every partial quotient
> `M/(f₁, …, f_i)M` is flat over `R`.
>
> The source is the case `M = S`: `f₁, …, f_c` is a regular sequence in `S` and each `S/(f₁, …, f_i)`
> is flat over `R`. Here `𝔪M` is `𝔪S • ⊤` and `M/(f₁, …, f_i)M` is
> `M ⧸ Ideal.ofList (fs.take i) • ⊤`; see the module docstring.

```lean
public theorem Module.Flat.isRegular_and_flat_quotient_ofList_smul_of_isRegular_maximalIdeal
    {R S M : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.FinitePresentation S M] [Module.Flat R M]
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation) (fs : List S)
    (hfs :
      RingTheory.Sequence.IsRegular
        (M ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S M))) fs) :
    RingTheory.Sequence.IsRegular M fs ∧
      ∀ i, Module.Flat R (M ⧸ (Ideal.ofList (fs.take i) • (⊤ : Submodule S M)))
```

## Tag 0471, a lemma

[Tag 0471](https://stacks.math.columbia.edu/tag/0471) in the Stacks Project.

**`Module.Flat.of_rTensor_subtype_injective_of_flat_quotient_of_essentiallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriterionEssFP.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriterionEssFP.lean#L351). The attribute's comment: “The hypothesis `Tor_1^R(M, R/I) = 0` is stated in the form Remark 00M6 identifies it with, the injectivity of `I ⊗_R M → R ⊗_R M`, as in the Noetherian sibling 00ML; this is the form the source's proof produces and the form 00ML consumes, and unlike `Tor_1` it puts `R` and `M` in no common universe. Hypothesis (1) is `RingHom.EssentiallyOfFinitePresentation` (Definition 00QM (2)), Mathlib having no such predicate. See the module docstring.”. References: EGA IV (11.3.12), “b⇒a, b⇒a for arbitrary A”; SGA 1 IV (5.6), “(ii)⇒(i), special case”.

> The local criterion for flatness for local maps essentially of finite presentation.
> Let `R → S` be a local homomorphism of local rings with `S` essentially of finite presentation over
> `R`, let `I ≠ R` be an ideal of `R` and let `M` be an `S`-module of finite presentation. If
> `Tor₁^R(R/I, M) = 0` and `M/IM` is flat over `R/I`, then `M` is flat over `R`.
>
> Here the Tor hypothesis appears in the form of Remark 00M6, as the injectivity of
> `I ⊗_R M → R ⊗_R M`, and `M/IM` is `M ⧸ I • ⊤` with its canonical `R ⧸ I`-module structure. No ring
> is assumed Noetherian; the Noetherian variant is 00ML.

```lean
public theorem of_rTensor_subtype_injective_of_flat_quotient_of_essentiallyOfFinitePresentation
    {R : Type u} (S : Type v) (M : Type w) [CommRing R] [CommRing S] [IsLocalRing R]
    [IsLocalRing S] [Algebra R S] [IsLocalHom (algebraMap R S)] [AddCommGroup M] [Module R M]
    [Module S M] [IsScalarTower R S M] [Module.FinitePresentation S M]
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation) (I : Ideal R) (hI : I ≠ ⊤)
    (hTor : Function.Injective (I.subtype.rTensor M))
    (hflat : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M)))) :
    Module.Flat R M
```

## Tag 00R7, a lemma

[Tag 00R7](https://stacks.math.columbia.edu/tag/00R7) in the Stacks Project.

**`Module.flat_algebra_and_flat_of_flat_quotient_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FibrewiseCriterionEssFP.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FibrewiseCriterionEssFP.lean#L351). The attribute's comment: “Hypothesis (1) is `RingHom.EssentiallyOfFinitePresentation` (Definition 00QM (2)) applied to `algebraMap R S` and `algebraMap R S'`, Mathlib having no such predicate. The fibre is `M ⧸ (𝔪S) • (⊤ : Submodule S M)` over the ring `S ⧸ 𝔪S`, as in 06A5, and the two conclusions are conjoined; see the module docstring.”. References: EGA IV (11.3.10), “special case”; SGA 1 I (5.9), “partial”; SGA 1 IV (5.9), “(ii) ⇒ (i)”; SGA 3 VIB (1.3.0), “special case”; SGA 3 VIB (12.7), “special case”; SGA 3 VIB (2.5), “flatness clause”; SGA 3 X (3.5), “Flat case”.

> **Critère de platitude par fibres.** Let `R → S → S'` be local homomorphisms of
> local rings with `R → S` and `R → S'` essentially of finite presentation, let `𝔪` be the maximal
> ideal of `R`, and let `M` be a nonzero `S'`-module of finite presentation over `S'`. If the fibre
> `M/𝔪M` is flat over `S/𝔪S` and `M` is flat over `R`, then `S` is flat over `R` and `M` is flat
> over `S`.
>
> Here `𝔪S` is `Ideal.map (algebraMap R S) (maximalIdeal R)` and `M/𝔪M` is `M ⧸ 𝔪S • ⊤` taken over
> `S`, so that it is a module over `S/𝔪S`.

```lean
public theorem Module.flat_algebra_and_flat_of_flat_quotient_maximalIdeal
    {R S S' M : Type*} [CommRing R] [CommRing S] [CommRing S']
    [IsLocalRing R] [IsLocalRing S] [IsLocalRing S']
    [Algebra R S] [Algebra S S'] [Algebra R S'] [IsScalarTower R S S']
    [IsLocalHom (algebraMap R S)] [IsLocalHom (algebraMap S S')]
    [AddCommGroup M] [Module R M] [Module S M] [Module S' M]
    [IsScalarTower R S M] [IsScalarTower S S' M]
    [Module.FinitePresentation S' M] [Nontrivial M]
    [Module.Flat (S ⧸ (maximalIdeal R).map (algebraMap R S))
      (M ⧸ ((maximalIdeal R).map (algebraMap R S) • (⊤ : Submodule S M)))]
    [Module.Flat R M]
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation)
    (hS' : (algebraMap R S').EssentiallyOfFinitePresentation) :
    Module.Flat R S ∧ Module.Flat S M
```

## Tag 05UV, a lemma

[Tag 05UV](https://stacks.math.columbia.edu/tag/05UV) in the Stacks Project.

**`Module.essentiallyOfFinitePresentation_and_flat_and_flat_of_flat_quotient_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FibrewiseCriterionEssFPBase.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FibrewiseCriterionEssFPBase.lean#L463). The attribute's comment: “"Essentially of finite type" is Mathlib's `Algebra.EssFiniteType` (Definition 00QM (1)); "essentially of finite presentation" is `RingHom.EssentiallyOfFinitePresentation` (Definition 00QM (2)), Mathlib having no such predicate. The chain `R → S → S'` is `IsScalarTower R S S'`, `𝔪S` is `(maximalIdeal R).map (algebraMap R S)` and `𝔪M` is `𝔪S • ⊤` over `S`, so that the fibre `M/𝔪M` is a module over the ring `S/𝔪S`. "`M` is not zero" is `Nontrivial M`. The three conclusions are conjoined; see the module docstring.”. References: EGA IV (11.3.10), “special case”; SGA 1 I (5.9), “partial”; SGA 1 IV (5.9), “(ii) ⇒ (i)”; SGA 3 VIB (1.3.0), “special case”; SGA 3 VIB (12.7), “special case”; SGA 3 VIB (2.5), “flatness clause”; SGA 3 X (3.5), “Flat case”.

> Let `R → S → S'` be local homomorphisms of local rings, let `𝔪` be the maximal
> ideal of `R`, and let `M` be a nonzero `S'`-module of finite presentation. Assume `R → S'` is
> essentially of finite presentation, `R → S` is essentially of finite type, `M` is flat over `R`,
> and the fibre `M/𝔪M` is flat over `S/𝔪S`. Then `R → S` is essentially of finite presentation, `S`
> is flat over `R`, and `M` is flat over `S`.
>
> Here `𝔪S` is `(maximalIdeal R).map (algebraMap R S)` and `𝔪M` is `𝔪S • ⊤`, so that `M/𝔪M` is a
> module over the fibre ring `S/𝔪S`.

```lean
public theorem
    Module.essentiallyOfFinitePresentation_and_flat_and_flat_of_flat_quotient_maximalIdeal
    {R S S' M : Type*} [CommRing R] [CommRing S] [CommRing S']
    [IsLocalRing R] [IsLocalRing S] [IsLocalRing S']
    [Algebra R S] [Algebra S S'] [Algebra R S'] [IsScalarTower R S S']
    [IsLocalHom (algebraMap R S)] [IsLocalHom (algebraMap S S')]
    [AddCommGroup M] [Module R M] [Module S M] [Module S' M]
    [IsScalarTower R S M] [IsScalarTower S S' M]
    [Algebra.EssFiniteType R S] [Module.FinitePresentation S' M] [Nontrivial M] [Module.Flat R M]
    [Module.Flat (S ⧸ (maximalIdeal R).map (algebraMap R S))
      (M ⧸ ((maximalIdeal R).map (algebraMap R S) • (⊤ : Submodule S M)))]
    (hS' : (algebraMap R S').EssentiallyOfFinitePresentation) :
    (algebraMap R S).EssentiallyOfFinitePresentation ∧ Module.Flat R S ∧ Module.Flat S M
```

## Tag 0CEL, a lemma

[Tag 0CEL](https://stacks.math.columbia.edu/tag/0CEL) in the Stacks Project.

**`Module.flat_and_flat_localization_of_flat_quotient_of_locallyNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FibreCriterionNilpotent.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FibreCriterionNilpotent.lean#L373). The attribute's comment: “"Locally nilpotent" is `∀ x ∈ I, IsNilpotent x`. `IM` is written as `IS • ⊤` over `S`, `S_q` is an abstract localization of `S` at `q`, and "essentially of finite presentation" is `RingHom.EssentiallyOfFinitePresentation`; see the module docstring.”. References: EGA IV (11.3.11), “(a) ⇒ (b), special case”; SGA 1 IV (5.9), “(ii) ⇒ (i), special case”; SGA 3 VIB (1.3.0), “special case”; SGA 3 VIB (2.5), “flatness clause”.

> Let `R → S → S'` be ring maps with `R → S` of finite type and `R → S'` of finite
> presentation, let `I ⊆ R` be an ideal all of whose elements are nilpotent, and let `M` be a
> finitely presented `S'`-module. If `M/IM` is flat over `S/IS` and `M` is flat over `R`, then `M` is
> flat over `S`, and `S_q` is flat and essentially of finite presentation over `R` for every prime
> `q ⊆ S` with `M ⊗_S κ(q)` nonzero.

```lean
theorem Module.flat_and_flat_localization_of_flat_quotient_of_locallyNilpotent
    {R S S' : Type*} [CommRing R] [CommRing S] [CommRing S'] [Algebra R S] [Algebra S S']
    [Algebra R S'] [IsScalarTower R S S']
    {M : Type*} [AddCommGroup M] [Module R M] [Module S M] [Module S' M]
    [IsScalarTower R S M] [IsScalarTower S S' M]
    (I : Ideal R) (hI : ∀ x ∈ I, IsNilpotent x)
    [Algebra.FiniteType R S] [Algebra.FinitePresentation R S'] [Module.FinitePresentation S' M]
    [Module.Flat (S ⧸ I.map (algebraMap R S))
      (M ⧸ (I.map (algebraMap R S) • (⊤ : Submodule S M)))]
    [Module.Flat R M] :
    Module.Flat S M ∧
      ∀ (q : Ideal S) [q.IsPrime] (Sq : Type*) [CommRing Sq] [Algebra S Sq]
        [IsLocalization.AtPrime Sq q] [Algebra R Sq] [IsScalarTower R S Sq],
        Nontrivial (M ⊗[S] q.ResidueField) →
          Module.Flat R Sq ∧ (algebraMap R Sq).EssentiallyOfFinitePresentation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.128, Tag 00R3](https://stacks.math.columbia.edu/tag/00R3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
