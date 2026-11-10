---
declaration: section
origin: cited
lean: Algebra.FiniteType.iff_finiteType_tensorProduct, Algebra.FinitePresentation.baseChange, Algebra.FinitePresentation.of_finitePresentation_tensorProduct_of_faithfullyFlat, Module.exists_finite_isBaseChange_of_surjective_algebraMap, Module.exists_finite_isLocalizedModule_comp, Module.exists_finite_isLocalizedModule_comp_atPrime, exists_away_prod_of_localRingHom_bijective, Algebra.FinitePresentation.exists_algEquiv_localizationAway_of_algEquiv_atPrime
statement: formalized
proof: formalized
---

# 10.126 Algebras and modules of finite presentation

Section 10.126 of the Stacks Project, [Tag 05N4](https://stacks.math.columbia.edu/tag/05N4). 11 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00QP, a lemma

[Tag 00QP](https://stacks.math.columbia.edu/tag/00QP) in the Stacks Project.

**`Algebra.FiniteType.iff_finiteType_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L317). References: SGA 1 VIII (3.4); SGA 1 VIII (3.3), “finite type, affine”.

> **Stacks 00QP**. Being of finite type descends along a faithfully flat base change:
> for a faithfully flat `R`-algebra `R'`, an `R`-algebra `S` is of finite type if and only
> if `R' ⊗[R] S` is of finite type over `R'`.

```lean
theorem Algebra.FiniteType.iff_finiteType_tensorProduct
    (R S R' : Type*) [CommRing R] [CommRing S] [CommRing R']
    [Algebra R S] [Algebra R R'] [Module.FaithfullyFlat R R'] :
    Algebra.FiniteType R S ↔ Algebra.FiniteType R' (R' ⊗[R] S)
```

## Tag 00QQ, a lemma

[Tag 00QQ](https://stacks.math.columbia.edu/tag/00QQ) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FinitePresentation.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FinitePresentation.baseChange#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L331) (StacksFrontier): “a base change of an algebra of finite presentation is of finite presentation”. References: EGA IV (8.6.2), “special case”; EGA IV (1.4.1); EGA IV (1.4.3), “(iii), special case”; EGA IV (1.6.2), “(iii), special case”; SGA 1 VIII (3.6), “partial”; SGA 3 XIX (2.1), “special case”.
- [`Algebra.FinitePresentation.of_finitePresentation_tensorProduct_of_faithfullyFlat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FinitePresentation.of_finitePresentation_tensorProduct_of_faithfullyFlat#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L333) (StacksFrontier): “finite presentation descends along a faithfully flat base change”. References: EGA IV (2.7.1), “special case”; EGA IV (2.7.1.1), “partial”; SGA 1 VIII (3.6), “affine case”; SGA 3 VIB (10.8), “special case”; SGA 3 XIX (2.1), “special case”; SGA 6 VIII (1.6), “special case”.

## Tag 05N5, a lemma

[Tag 05N5](https://stacks.math.columbia.edu/tag/05N5) in the Stacks Project.

**`Module.exists_finite_isBaseChange_of_surjective_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 667](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L667). The attribute's comment: “Stated for an arbitrary surjection `Rₛ → R'` from a localization `Rₛ = S⁻¹R` in place of `R' = S⁻¹(R/I)`, of which it is the case `R' = Rₛ ⧸ I·Rₛ`; `S⁻¹(M/IM)` is the base change `R' ⊗_R M`, pinned by `IsBaseChange R' g` for the source's map `g : M → M'`. Items (1) and (2) are the two conjuncts.”.

> **Stacks 05N5.** Let `R` be a ring, `S ⊆ R` a multiplicative subset, `Rₛ = S⁻¹R` and let
> `R'` be a quotient of `Rₛ` (for instance `R' = S⁻¹(R/I) = Rₛ/I·Rₛ` for an ideal `I ⊆ R`). For
> every finite `R'`-module `M'` there is a finite `R`-module `M` and an `R`-linear map
> `g : M → M'` exhibiting `M'` as the base change `R' ⊗_R M`, i.e. as `S⁻¹(M/IM)`; and if `M'` is
> finitely presented over `R'`, then `M` may be taken finitely presented over `R`.

```lean
theorem exists_finite_isBaseChange_of_surjective_algebraMap {R : Type u} [CommRing R]
    (S : Submonoid R) (Rₛ : Type v) [CommRing Rₛ] [Algebra R Rₛ] [IsLocalization S Rₛ]
    {R' : Type w} [CommRing R'] [Algebra R R'] [Algebra Rₛ R'] [IsScalarTower R Rₛ R']
    (M' : Type t) [AddCommGroup M'] [Module R M'] [Module R' M'] [IsScalarTower R R' M']
    [Module.Finite R' M'] (hsurj : Function.Surjective (algebraMap Rₛ R')) :
    ∃ (M : Type u) (_ : AddCommGroup M) (_ : Module R M) (g : M →ₗ[R] M'),
      Module.Finite R M ∧ IsBaseChange R' g ∧
        (Module.FinitePresentation R' M' → Module.FinitePresentation R M)
```

## Tag 05N6, a lemma

[Tag 05N6](https://stacks.math.columbia.edu/tag/05N6) in the Stacks Project.

**`Module.exists_finite_isLocalizedModule_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L478). The attribute's comment: “Localizations are abstract (`IsLocalization S Rₛ`, `IsLocalizedModule S f`); the induced isomorphism `S⁻¹M' → S⁻¹M` is pinned as `IsLocalizedModule S (f ∘ₗ φ)`; `M'` is produced in the universe of `R`. Items (1) and (2) are the two conjuncts, (2) as an implication about the same `M'`.”.

> **Stacks 05N6.** Let `R` be a ring, `S ⊆ R` a multiplicative subset, `M` an `R`-module and
> `f : M → Mₛ` a localization of `M` at `S`, over a localization `Rₛ` of `R` at `S`.
>
> 1. If `Mₛ = S⁻¹M` is a finite `Rₛ`-module, then there is a finite `R`-module `M'` and an
>    `R`-linear map `φ : M' → M` inducing an isomorphism `S⁻¹M' ≅ S⁻¹M`, spelled
>    `IsLocalizedModule S (f ∘ₗ φ)`.
> 2. If `Mₛ` is moreover a finitely presented `Rₛ`-module, then `M'` is of finite presentation
>    over `R`.

```lean
theorem exists_finite_isLocalizedModule_comp {R : Type u} [CommRing R] (S : Submonoid R)
    (Rₛ : Type v) [CommRing Rₛ] [Algebra R Rₛ] [IsLocalization S Rₛ]
    {M : Type w} [AddCommGroup M] [Module R M]
    {Mₛ : Type t} [AddCommGroup Mₛ] [Module R Mₛ] [Module Rₛ Mₛ] [IsScalarTower R Rₛ Mₛ]
    (f : M →ₗ[R] Mₛ) [IsLocalizedModule S f] [Module.Finite Rₛ Mₛ] :
    ∃ (M' : Type u) (_ : AddCommGroup M') (_ : Module R M') (φ : M' →ₗ[R] M),
      Module.Finite R M' ∧ IsLocalizedModule S (f ∘ₗ φ) ∧
        (Module.FinitePresentation Rₛ Mₛ → Module.FinitePresentation R M')
```

## Tag 05GJ, a lemma

[Tag 05GJ](https://stacks.math.columbia.edu/tag/05GJ) in the Stacks Project.

**`Module.exists_finite_isLocalizedModule_comp_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L527). The attribute's comment: “The case `S = p.primeCompl` of 05N6 (`Module.exists_finite_isLocalizedModule_comp`), stated in the same shape: localizations are abstract, the induced isomorphism `M'ₚ → Mₚ` is pinned as `IsLocalizedModule p.primeCompl (f ∘ₗ φ)`, `M'` is produced in the universe of `R`, and items (1) and (2) are the two conjuncts, (2) as an implication about the same `M'`.”.

> **Stacks 05GJ.** Let `R` be a ring, `p ⊆ R` a prime ideal, `M` an `R`-module and
> `f : M → Mₚ` a localization of `M` at `p.primeCompl`, over a localization `Rₚ` of `R` at `p`.
>
> 1. If `Mₚ` is a finite `Rₚ`-module, then there is a finite `R`-module `M'` and an `R`-linear map
>    `φ : M' → M` inducing an isomorphism `M'ₚ ≅ Mₚ`, spelled
>    `IsLocalizedModule p.primeCompl (f ∘ₗ φ)`.
> 2. If `Mₚ` is moreover a finitely presented `Rₚ`-module, then `M'` is of finite presentation
>    over `R`.

```lean
theorem exists_finite_isLocalizedModule_comp_atPrime {R : Type u} [CommRing R]
    (p : Ideal R) [p.IsPrime]
    (Rₚ : Type v) [CommRing Rₚ] [Algebra R Rₚ] [IsLocalization.AtPrime Rₚ p]
    {M : Type w} [AddCommGroup M] [Module R M]
    {Mₚ : Type t} [AddCommGroup Mₚ] [Module R Mₚ] [Module Rₚ Mₚ] [IsScalarTower R Rₚ Mₚ]
    (f : M →ₗ[R] Mₚ) [IsLocalizedModule p.primeCompl f] [Module.Finite Rₚ Mₚ] :
    ∃ (M' : Type u) (_ : AddCommGroup M') (_ : Module R M') (φ : M' →ₗ[R] M),
      Module.Finite R M' ∧ IsLocalizedModule p.primeCompl (f ∘ₗ φ) ∧
        (Module.FinitePresentation Rₚ Mₚ → Module.FinitePresentation R M')
```

## Tag 00QR, a lemma

[Tag 00QR](https://stacks.math.columbia.edu/tag/00QR) in the Stacks Project.

**`exists_away_prod_of_localRingHom_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/LocalIsomorphism/ProductSplitting.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/SpreadingOut/LocalIsomorphism/ProductSplitting.lean#L429).

> Let `φ : R → S` be a ring map of commutative rings, and let `q ⊆ S` be a prime ideal lying over
> the prime `p ⊆ R` (i.e. `p = q.comap φ`). Assume `S` is of finite presentation over `R`, and that
> the induced map on localizations `φ_p : R_p → S_q` (`Localization.localRingHom`) is bijective.
> Then there exist `f : R` with `f ∉ p` and an `R_f`-algebra `C` such that `S_f ≅ R_f × C` as
> `R_f`-algebras, where `S_f := Localization.Away (φ f)` is given the `R_f`-algebra structure
> induced by `Localization.awayMap φ f`.

```lean
theorem exists_away_prod_of_localRingHom_bijective (R S : Type) [CommRing R] [CommRing S] [Algebra R
  S] (p : Ideal R) [p.IsPrime]
    (q : Ideal S) [q.IsPrime] (hpq : p = q.comap (algebraMap R S)) [Algebra.FinitePresentation R S]
    (hiso : Function.Bijective (Localization.localRingHom p q (algebraMap R S) hpq)) :
    ∃ f : R,
      f ∉ p ∧
        ∃ (C : Type) (_ : CommRing C) (_ : Algebra (Localization.Away f) C),
          letI : Algebra (Localization.Away f) (Localization.Away (algebraMap R S f)) :=
            (Localization.awayMap (algebraMap R S) f).toAlgebra
          Nonempty
            (Localization.Away (algebraMap R S f) ≃ₐ[Localization.Away f]
              (Localization.Away f × C))
```

## Tag 00QS, a lemma

[Tag 00QS](https://stacks.math.columbia.edu/tag/00QS) in the Stacks Project.

**`Algebra.FinitePresentation.exists_algEquiv_localizationAway_of_algEquiv_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/LocalIsomorphism/AwayIsomorphism.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/SpreadingOut/LocalIsomorphism/AwayIsomorphism.lean#L484). The attribute's comment: “The local rings `S_q`, `S'_{q'}` are abstract (`IsLocalization.AtPrime Sq q` with `IsScalarTower R S Sq`, so that the `R`-algebra structure is the composite `R → S → Sq`), which makes the hypothesis available for any model; the localizations `S_g`, `S'_{g'}` of the conclusion are the models `Localization.Away g`, `Localization.Away g'`, a choice that costs no strength by uniqueness of localizations. As in the source only the existence of an `R`-algebra isomorphism is claimed, not the compatibility with the given isomorphism of local rings that the proof also produces. See the module docstring.”.

> Let `R` be a ring, let `S` and `S'` be `R`-algebras of finite presentation,
> and let `q ⊆ S`, `q' ⊆ S'` be primes. If the local rings `S_q` and `S'_{q'}` are isomorphic as
> `R`-algebras, then there are `g ∈ S`, `g ∉ q` and `g' ∈ S'`, `g' ∉ q'` such that `S_g` and
> `S'_{g'}` are isomorphic as `R`-algebras.

```lean
public theorem exists_algEquiv_localizationAway_of_algEquiv_atPrime {R : Type u} [CommRing R]
    {S : Type v} [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S] {S' : Type v'}
    [CommRing S'] [Algebra R S'] [Algebra.FinitePresentation R S'] (q : Ideal S) [q.IsPrime]
    (q' : Ideal S') [q'.IsPrime] (Sq : Type w) [CommRing Sq] [Algebra S Sq]
    [IsLocalization.AtPrime Sq q] [Algebra R Sq] [IsScalarTower R S Sq] (Sq' : Type w')
    [CommRing Sq'] [Algebra S' Sq'] [IsLocalization.AtPrime Sq' q'] [Algebra R Sq']
    [IsScalarTower R S' Sq'] (e : Sq ≃ₐ[R] Sq') :
    ∃ g ∉ q, ∃ g' ∉ q', Nonempty (Localization.Away g ≃ₐ[R] Localization.Away g')
```

## Tag 0G8U, a lemma

[Tag 0G8U](https://stacks.math.columbia.edu/tag/0G8U) in the Stacks Project.

**`finiteType_of_isNilpotent_quotient_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Descent.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Descent.lean#L437). References: SGA 3 VIB (1.3.0), “(i)”.

> **Stacks Tag 0G8U (Lemma 10.126.8).** Let `R` be a ring, let `I` be a nilpotent ideal
> of `R`, and let `S` be an `R`-algebra such that the induced ring map `R ⧸ I → S ⧸ IS` is
> of finite type. Then the structure map `R → S` is of finite type.

```lean
theorem finiteType_of_isNilpotent_quotient_finiteType
    (R : Type*) [CommRing R] (I : Ideal R)
    (S : Type*) [CommRing S] [Algebra R S]
    (hI : IsNilpotent I)
    (hft : Algebra.FiniteType (R ⧸ I) (S ⧸ I.map (algebraMap R S))) :
    Algebra.FiniteType R S
```

## Tag 07RD, a lemma

[Tag 07RD](https://stacks.math.columbia.edu/tag/07RD) in the Stacks Project.

**`surjective_of_surjective_mod_locallyNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nilpotent/Descent.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nilpotent/Descent.lean#L260).

> **Stacks Tag 07RD.** Let `R` be a commutative ring, `I ⊆ R` a locally
> nilpotent ideal, and `f : S →ₐ[R] S'` an `R`-algebra map such that the induced
> map `S → S'/IS'` is surjective and `S'` is of finite type over `R`. Then `f`
> is surjective.
>
> The proof is the Stacks 07RD argument, reorganized to avoid
> the `R₀` reduction by observing that the finitely many nilpotent coefficients
> generate a nilpotent ideal directly via Tag 00IM with `J = ⊥`.
>
> Let `P := MvPolynomial ι R` for a `Fintype ι`. Since `S'` is finite type over
> `R`, choose a *surjective* `R`-algebra hom `φ : P →ₐ[R] S'` (generators
> `xⱼ := φ (X j)`).
>
> `hsurj` says `π ∘ f` is surjective, where `π = Ideal.Quotient.mk (IS')`. Hence
> for each `j` there is `sⱼ ∈ S` with `π (xⱼ) = π (f sⱼ)`, i.e.
> `xⱼ - f sⱼ ∈ IS' = Ideal.map (algebraMap R S') I`.
>
> An element of `IS'` is a finite sum `Σ_k (algebraMap aₖ)·bₖ` with `aₖ ∈ I`,
> `bₖ ∈ S'`. Lift each `bₖ` through `φ` to `βₖ ∈ P`, and set
> `h j := Σ_k (C aₖ) · βₖ ∈ P`, so that `φ (h j) = xⱼ - f sⱼ`. Define
> `g j := X j - h j`, whence `φ (g j) = xⱼ - (xⱼ - f sⱼ) = f sⱼ ∈ range f`.
>
> Let `𝔫 ⊆ R` be the ideal generated by the finite set `{aₖ}` of coefficients
> used above. Each `aₖ ∈ I` is nilpotent (`hI`), so `𝔫 ≤ (⊥ : Ideal R).radical`
> (the nilradical); and `𝔫` is finitely generated. By Tag 00IM
> (`Ideal.exists_pow_le_of_le_radical_of_fg`) there is `N` with `𝔫 ^ N ≤ ⊥`, i.e.
> `𝔫 ^ N = ⊥`: `𝔫` is nilpotent. Put `𝔐 := Ideal.map C 𝔫 ⊆ P`; then
> `𝔐 ^ N ≤ Ideal.map C (𝔫 ^ N) = ⊥`, so `𝔐` is nilpotent, and each `h j ∈ 𝔐`
> (it is a combination of `C aₖ` with `aₖ ∈ 𝔫`).
>
> By `aeval_sub_nilpotent_surjective`, `σ := aeval g : P →ₐ[R] P` is surjective.
> Therefore the `R`-subalgebra of `P` generated by `{g j}` is `⊤` (it contains
> `σ.range = ⊤`, and `Algebra.adjoin R {g j} = σ.range`). Applying `φ`:
> `S' = φ '' P = φ '' (adjoin R {g j}) = Algebra.adjoin R {φ (g j)}
>      = Algebra.adjoin R {f sⱼ} ≤ (f.range : Subalgebra R S')`,
> since each `f sⱼ ∈ f.range` and `f.range` is an `R`-subalgebra. Hence
> `f.range = ⊤`, i.e. `f` is surjective. ∎

```lean
theorem surjective_of_surjective_mod_locallyNilpotent
    (I : Ideal R) (hI : I.IsLocallyNilpotent)
    (f : S →ₐ[R] S')
    (hsurj : Function.Surjective
      ((Ideal.Quotient.mk (extendedIdeal I S')).comp f.toRingHom))
    (hft : Algebra.FiniteType R S') :
    Function.Surjective f
```

## Tag 087P, a lemma

[Tag 087P](https://stacks.math.columbia.edu/tag/087P) in the Stacks Project.

**`isomorphism_of_flat_surjective_087P`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/Away.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/SpreadingOut/Away.lean#L334).

> **Stacks Tag 087P (Lemma 10.126.10).**
> Under the stated hypotheses there is `g ∈ S`, `g ∉ q`, with `φ_g : S_g → S'_g` an
> isomorphism (i.e. bijective).

```lean
theorem isomorphism_of_flat_surjective_087P
    (hIq : I.map (algebraMap R S) ≤ q)
    (hsurj : Function.Surjective (φ : S → S'))
    (hiso : Function.Bijective (phiqBar I φ q Sq S'q))
    (hft : (algebraMap R S).FiniteType)
    (hfp : (algebraMap R S').FinitePresentation)
    (hflat : Module.Flat R S'q) :
    ∃ g : S, g ∉ q ∧ Function.Bijective (phig φ g)
```

## Tag 07RE, a lemma

[Tag 07RE](https://stacks.math.columbia.edu/tag/07RE) in the Stacks Project.

**`AlgHom.bijective_of_bijective_quotientMapₐ_of_le_nilradical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 743](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L743). The attribute's comment: “That `I` consists of nilpotents is spelled `I ≤ nilradical R`, the source's `S/IS → S'/IS'` is `Ideal.quotientMapₐ` applied to `f`, and finite type, finite presentation and flatness are instance arguments.”. References: SGA 1 III (4.2), “affine case + finiteness”.

> **Stacks 07RE**. Let `I ⊆ R` be an ideal all of whose elements are nilpotent, let `S` be of
> finite type over `R` and let `S'` be of finite presentation and flat over `R`. If an `R`-algebra
> map `f : S →ₐ[R] S'` induces a bijection `S/IS → S'/IS'`, then `f` is bijective.

```lean
theorem AlgHom.bijective_of_bijective_quotientMapₐ_of_le_nilradical
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] {S' : Type w} [CommRing S']
    [Algebra R S] [Algebra R S'] [Algebra.FiniteType R S] [Algebra.FinitePresentation R S']
    [Module.Flat R S'] (I : Ideal R) (hI : I ≤ nilradical R) (f : S →ₐ[R] S')
    (hf : Function.Bijective
      (Ideal.quotientMapₐ (I.map (algebraMap R S')) f
          (Ideal.map_le_iff_le_comap.mpr fun x hx ↦
            show f (algebraMap R S x) ∈ I.map (algebraMap R S') from
              f.commutes x ▸ Ideal.mem_map_of_mem _ hx) :
        S ⧸ I.map (algebraMap R S) →ₐ[R] S' ⧸ I.map (algebraMap R S'))) :
    Function.Bijective f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.126, Tag 05N4](https://stacks.math.columbia.edu/tag/05N4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
