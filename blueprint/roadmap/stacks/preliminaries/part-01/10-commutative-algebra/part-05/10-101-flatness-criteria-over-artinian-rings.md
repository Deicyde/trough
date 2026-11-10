---
declaration: section
origin: cited
lean: Module.Flat.linearIndependent_and_span_eq_top_mkQ_comp_iff_of_isNilpotent, Module.tfae_flat_free_projective_of_isNilpotent_maximalIdeal, Stacks.FreeOfNilpotentIdeal.free_of_nilpotent_of_basis_mod_of_tor, flat_quot_idealTwo_smul_top_of_flat_quot_and_flat_baseChange, Module.Flat.of_flat_quotient_of_flat_tensorProduct_of_isNilpotent_of_injective, Module.Flat.iff_flat_quotient_and_isZero_Tor'_one, Module.Flat.of_flat_baseChange_of_injective, Module.flat_and_flat_localization_of_flat_quotient_of_isNilpotent
statement: formalized
proof: formalized
---

# 10.101 Flatness criteria over Artinian rings

Section 10.101 of the Stacks Project, [Tag 051E](https://stacks.math.columbia.edu/tag/051E). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 051F, a lemma

[Tag 051F](https://stacks.math.columbia.edu/tag/051F) in the Stacks Project.

**`Module.Flat.linearIndependent_and_span_eq_top_mkQ_comp_iff_of_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Nilpotent.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Nilpotent.lean#L282). The attribute's comment: “Stated for an arbitrary nilpotent ideal `I` of an arbitrary commutative ring, the source's local ring being the case `I = IsLocalRing.maximalIdeal R`; `M/IM` is `M ⧸ I • ⊤` over `R ⧸ I` with reduction map `Submodule.mkQ`, and `forms a basis` is `LinearIndependent … ∧ Submodule.span … = ⊤`. See the module docstring.”. References: SGA 3 VIIA (7.4.3), “special case”; SGA 3 VIII (6.2), “flat clause”.

> Let `R` be a commutative ring, let `I ⊆ R` be a nilpotent ideal and let `M` be a flat
> `R`-module. A family `x : ι → M`, indexed by an arbitrary type, is an `R`-basis of `M` if and only
> if the family of its reductions is an `R/I`-basis of `M/IM`. "Is a basis" is read as
> `LinearIndependent … ∧ Submodule.span … = ⊤`, the hypotheses of `Module.Basis.mk`.

```lean
theorem linearIndependent_and_span_eq_top_mkQ_comp_iff_of_isNilpotent {R : Type*}
    [CommRing R] {M : Type*} [AddCommGroup M] [Module R M] [Module.Flat R M] (I : Ideal R)
    (hI : IsNilpotent I) {ι : Type*} (x : ι → M) :
    (LinearIndependent (R ⧸ I) ((I • (⊤ : Submodule R M)).mkQ ∘ x) ∧
        Submodule.span (R ⧸ I) (Set.range ((I • (⊤ : Submodule R M)).mkQ ∘ x)) = ⊤) ↔
      (LinearIndependent R x ∧ Submodule.span R (Set.range x) = ⊤)
```

## Tag 051G, a lemma

[Tag 051G](https://stacks.math.columbia.edu/tag/051G) in the Stacks Project.

**`Module.tfae_flat_free_projective_of_isNilpotent_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/NilpotentIdeal.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Projective/NilpotentIdeal.lean#L386). The attribute's comment: “The equivalence is a `List.TFAE` in the source's order (flat, free, projective); nilpotence of the maximal ideal is `IsNilpotent (IsLocalRing.maximalIdeal R)`.”. References: EGA 0 (10.1.3), “case (i)”; EGA 0 (10.1.3), “case (i)”; EGA III (7.3.5), “commutative case”; EGA IV (11.3.12), “special case”; EGA IV (2.2.17), “special case”; SGA 1 IV (4.3), “(i),(ii),(iii)”; SGA 3 VIA (2.1.3), “special case”; SGA 3 VIB (6.2.2), “more general”; SGA 3 VIIA (8.4), “partial”; SGA 3 VIIB (0.2.2), “special case”; SGA 3 VIIB (0.3.7), “local Artinian rings”; SGA 3 VIIB (1.2.1), “special case”; SGA 3 VIII (6.2), “more general”.

> **Stacks 051G**: let `(R, 𝔪)` be a local ring whose maximal ideal is nilpotent — an Artinian
> local ring, for instance — and let `M` be an `R`-module. Then `M` is flat over `R` if and only if
> `M` is a free `R`-module if and only if `M` is a projective `R`-module. No finiteness hypothesis on
> `M` is needed; compare `Module.free_of_flat_of_isLocalRing`, which assumes `Module.Finite R M` over
> an arbitrary local ring, and `Module.Flat.projective_of_finitePresentation`. The proof is the
> source's: a family of elements of `M` whose reductions form a basis of `M/𝔪M` over `R/𝔪` is a basis
> of `M` over `R`, by Lemma 051F.

```lean
public theorem tfae_flat_free_projective_of_isNilpotent_maximalIdeal {R : Type*} [CommRing R]
    [IsLocalRing R] {M : Type*} [AddCommGroup M] [Module R M]
    (hR : IsNilpotent (IsLocalRing.maximalIdeal R)) :
    List.TFAE [Module.Flat R M, Module.Free R M, Module.Projective R M]
```

## Tag 051H, a lemma

[Tag 051H](https://stacks.math.columbia.edu/tag/051H) in the Stacks Project.

**`Stacks.FreeOfNilpotentIdeal.free_of_nilpotent_of_basis_mod_of_tor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Free/OfNilpotentIdeal/Freeness.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Free/OfNilpotentIdeal/Freeness.lean#L511).

> **Theorem (Stacks Project, Tag 051H; Lemma 10.101.3).**
>
> Let `R` be a ring, `I ⊆ R` an ideal, `M` an `R`-module, `A` a set, and
> `x : A → M` a family of elements of `M`. Assume:
>
> 1. `I` is nilpotent;
> 2. the family of reductions `(reduction I (x α))_{α}` forms a basis of the
>    `R/I`-module `M/IM`, witnessed by a basis `b` with `b α = reduction I (x α)`;
> 3. `Tor₁^R(R/I, M) = 0`, expressed as injectivity of the multiplication map
>    `torMul I : I ⊗_R M → M`.
>
> Then `x` is a basis of `M` as an `R`-module: it is linearly independent and
> spans `M`.

```lean
theorem free_of_nilpotent_of_basis_mod_of_tor
    {A : Type*} (x : A → M) (I : Ideal R)
    (hI : IsNilpotent I)
    (b : Module.Basis A (R ⧸ I) (M ⧸ smul (M := M) I))
    (hb : ∀ α, b α = reduction I (x α))
    (hTor : Function.Injective (torMul (M := M) I)) :
    LinearIndependent R x ∧ ⊤ ≤ Submodule.span R (Set.range x)
```

## Tag 051I, a lemma

[Tag 051I](https://stacks.math.columbia.edu/tag/051I) in the Stacks Project.

**`flat_quot_idealTwo_smul_top_of_flat_quot_and_flat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/SquareZeroCriterion.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/SquareZeroCriterion.lean#L487).

> **Stacks Tag 051I, Lemma 10.101.4.** Wires the square-zero local criterion
> (`flat_of_sq_zero_local_criterion`) to the two base-change inputs
> (`hquot_from_h1`, `htor_from_base_change`), using that the image of `I` in
> `R ⧸ I₂` is square-zero (`image_I_sq_eq_bot`).

```lean
theorem flat_quot_idealTwo_smul_top_of_flat_quot_and_flat_baseChange
    {R R' : Type*} [CommRing R] [CommRing R'] [Algebra R R']
    {M : Type*} [AddCommGroup M] [Module R M]
    (I : Ideal R)
    (h1 : Module.Flat (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M)))
    (h2 : Module.Flat R' (R' ⊗[R] M)) :
    Module.Flat (R ⧸ idealTwo I R')
      (M ⧸ (idealTwo I R') • (⊤ : Submodule R M))
```

## Tag 051J, a lemma

[Tag 051J](https://stacks.math.columbia.edu/tag/051J) in the Stacks Project.

**`Module.Flat.of_flat_quotient_of_flat_tensorProduct_of_isNilpotent_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/TorAndNilpotentDescent.lean, line 889](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/TorAndNilpotentDescent.lean#L889). The attribute's comment: “The ring map is `algebraMap R R'`; `M/IM` is `M ⧸ I • ⊤` with its canonical `R ⧸ I`-action and the base change is `R' ⊗[R] M`, acted on by `R'` through the left factor. See the module docstring.”. References: EGA IV (11.4.1), “special case”; EGA IV (11.4.9), “sufficiency (flat case)”.

> **Stacks 051J**: the local criterion for flatness along an injective ring map. Let
> `φ : R → R'` be a map of commutative rings, `I ⊆ R` a nilpotent ideal and `M` an `R`-module. If
> `φ = algebraMap R R'` is injective, `M/IM` is flat over `R ⧸ I` and the base change `R' ⊗[R] M`
> is flat over `R'`, then `M` is flat over `R`. Compare `Module.Flat.of_flat_tensorProduct`, which
> descends flatness along a faithfully flat ring map with no nilpotent ideal in sight, and
> `Module.Flat.of_flat_baseChange_of_injective` (Stacks 051L), the case where `R` is Artinian and
> `I` is its Jacobson radical, so that flatness of the reduction is automatic. The proof is the
> source's: the tower `I₁ = I`, `I_{n+1} = φ⁻¹(φ(I_n) ^ 2 R')` reaches `0` because `I` is nilpotent
> and `φ` is injective, and each step preserves flatness of the reduction by the square-zero
> criterion (Stacks 051I).

```lean
public theorem of_flat_quotient_of_flat_tensorProduct_of_isNilpotent_of_injective
    {R R' : Type*} [CommRing R] [CommRing R'] [Algebra R R']
    {M : Type*} [AddCommGroup M] [Module R M] (I : Ideal R)
    (hI : IsNilpotent I) (hφ : Function.Injective (algebraMap R R'))
    (hMI : Module.Flat (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M)))
    (hM' : Module.Flat R' (R' ⊗[R] M)) :
    Module.Flat R M
```

## Tag 051K, a lemma

[Tag 051K](https://stacks.math.columbia.edu/tag/051K) in the Stacks Project.

**`Module.Flat.iff_flat_quotient_and_isZero_Tor'_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Nilpotent.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Nilpotent.lean#L315). The attribute's comment: “The source's Artinian local `R` is weakened to `R` local with nilpotent maximal ideal, the hypothesis of 051G; `Tor_1^R(R/I, M)` is `Tor'`, which derives the first variable, as in 00MJ and 00M5. See the module docstring.”. References: EGA 0 (10.1.3), “(i): c ⇔ d, c ⇔ d”; EGA 0 (10.2.1), “a ⇒ b, a ⇔ b”; EGA IV (11.2.5), “special case”; SGA 1 IV (5.5), “(i)⇔(ii), special case”.

> The local criterion for flatness over a local ring with nilpotent maximal ideal (an Artinian
> local ring, for instance). Let `R` be such a ring, let `M` be an `R`-module and
> let `I ⊆ R` be a proper ideal. Then `M` is flat over `R` if and only if `M/IM` is flat over `R/I`
> and `Tor₁^R(R/I, M) = 0`. Here `Tor₁^R(R/I, M)` is
> `((Tor' (ModuleCat R) 1).obj (ModuleCat.of R (R ⧸ I))).obj (ModuleCat.of R M)`, the first left
> derived functor of `- ⊗ M` evaluated at `R ⧸ I`.

```lean
theorem iff_flat_quotient_and_isZero_Tor'_one {R : Type u} [CommRing R] [IsLocalRing R]
    (M : Type u) [AddCommGroup M] [Module R M] (I : Ideal R)
    (hR : IsNilpotent (IsLocalRing.maximalIdeal R)) (hI : I ≠ ⊤) :
    Module.Flat R M ↔
      Module.Flat (R ⧸ I) (M ⧸ (I • ⊤ : Submodule R M)) ∧
        IsZero (((Tor' (ModuleCat.{u} R) 1).obj (ModuleCat.of R (R ⧸ I))).obj
          (ModuleCat.of R M))
```

## Tag 051L, a lemma

[Tag 051L](https://stacks.math.columbia.edu/tag/051L) in the Stacks Project.

**`Module.Flat.of_flat_baseChange_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/BaseChange.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/BaseChange.lean#L487). The attribute's comment: “The source's `M ⊗_R S` is an arbitrary base change `f : M →ₗ[R] N` with `IsBaseChange S f`, which specialises to it by `TensorProduct.isBaseChange`; injectivity of the ring map is injectivity of `algebraMap R S`. See the module docstring.”.

> **Stacks 051L**: flatness descends along an injective ring map whose source is Artinian. Let
> `R → S` be a map of commutative rings with `R` Artinian and `algebraMap R S` injective, let `M` be
> an `R`-module and let `f : M →ₗ[R] N` exhibit `N` as the base change of `M` to `S`, for instance
> `N = S ⊗[R] M` with `f = TensorProduct.mk R S M 1`. If `N` is flat over `S`, then `M` is flat over
> `R`. Compare `Module.Flat.of_flat_tensorProduct`, where `R → S` is faithfully flat instead.

```lean
public theorem of_flat_baseChange_of_injective {R : Type*} [CommRing R] [IsArtinianRing R]
    (S : Type*) [CommRing S] [Algebra R S] {M : Type*} [AddCommGroup M] [Module R M]
    (N : Type*) [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N]
    [Module.Flat S N] {f : M →ₗ[R] N} (hf : IsBaseChange S f)
    (hRS : Function.Injective (algebraMap R S)) :
    Module.Flat R M
```

## Tag 06A5, a lemma

[Tag 06A5](https://stacks.math.columbia.edu/tag/06A5) in the Stacks Project.

**`Module.flat_and_flat_localization_of_flat_quotient_of_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FibrewiseCriterion.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FibrewiseCriterion.lean#L503). The attribute's comment: “The auxiliary ring `S'` of the source's triangle is dropped: `M` is taken to be an `S`-module over `R → S`, which is equivalent and does not mention `S'`. `IM` is written as `IS • ⊤` over `S`, and `S_q` is an abstract localization at `q`; see the module docstring.”. References: EGA IV (11.3.11), “(a) ⇒ (b), special case”; SGA 1 IV (5.9), “(ii) ⇒ (i), special case”; SGA 3 VIB (1.3.0), “special case”; SGA 3 VIB (12.7), “more general”; SGA 3 VIB (2.5), “flatness clause”.

> **Critère de platitude par fibres, nilpotent case**. Let `R → S` be a map of commutative rings,
> let `M` be an `S`-module whose `R`-module structure comes from `R → S`, and let `I ⊆ R` be a
> nilpotent ideal. If `M/IM` is flat over `S/IS` and `M` is flat over `R`, then `M` is flat over `S`,
> and `S_q` is flat over `R` for every prime `q ⊆ S` with `M ⊗_S κ(q)` nonzero.

```lean
public theorem Module.flat_and_flat_localization_of_flat_quotient_of_isNilpotent
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    {M : Type*} [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    (I : Ideal R) (hI : IsNilpotent I)
    [Module.Flat (S ⧸ I.map (algebraMap R S))
      (M ⧸ (I.map (algebraMap R S) • (⊤ : Submodule S M)))]
    [Module.Flat R M] :
    Module.Flat S M ∧
      ∀ (q : Ideal S) [q.IsPrime] (Sq : Type*) [CommRing Sq] [Algebra S Sq]
        [IsLocalization.AtPrime Sq q] [Algebra R Sq] [IsScalarTower R S Sq],
        Nontrivial (M ⊗[S] q.ResidueField) → Module.Flat R Sq
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.101, Tag 051E](https://stacks.math.columbia.edu/tag/051E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
