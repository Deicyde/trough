---
declaration: section
origin: cited
lean: finrank_kaehler_baseChange_eq_finrank_cotangent, Algebra.isSmoothAt_tfae_of_isAlgClosed, Algebra.isSmoothAt_tfae_localKrullDim_and_isRegularLocalRing, KaehlerDifferential.kerCotangentToTensor_injective_of_isSeparableExtension, Algebra.isSmoothAt_iff_isRegularLocalRing, not_isNilpotent_of_hasFreeSummandDifferential, nonzerodivisor_of_hasFreeSummandDifferential, Algebra.isSmoothAt_tfae_free_kaehlerDifferential_isRegularLocalRing
statement: formalized
proof: formalized
---

# 10.140 Smooth algebras over fields

Section 10.140 of the Stacks Project, [Tag 00TQ](https://stacks.math.columbia.edu/tag/00TQ). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00TR, a lemma

[Tag 00TR](https://stacks.math.columbia.edu/tag/00TR) in the Stacks Project.

**`finrank_kaehler_baseChange_eq_finrank_cotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/CotangentAtMaximalIdeal.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/CotangentAtMaximalIdeal.lean#L199).

> For an algebraically closed field $k$, a finite type $k$-algebra $S$, and a maximal ideal
> $\mathfrak{m} \subset S$, the dimension over the residue field
> $\kappa(\mathfrak{m}) = S/\mathfrak{m}$ of the cotangent space
> $\Omega_{S/k} \otimes_S \kappa(\mathfrak{m})$ equals the dimension of
> $\mathfrak{m}/\mathfrak{m}^2$.

```lean
theorem finrank_kaehler_baseChange_eq_finrank_cotangent
    (k S : Type*) [Field k] [IsAlgClosed k] [CommRing S] [Algebra k S]
    [Algebra.FiniteType k S] (𝔪 : Ideal S) [𝔪.IsMaximal] :
    Module.finrank (S ⧸ 𝔪) ((S ⧸ 𝔪) ⊗[S] KaehlerDifferential k S) =
      Module.finrank (S ⧸ 𝔪) 𝔪.Cotangent
```

## Tag 00TS, a lemma

[Tag 00TS](https://stacks.math.columbia.edu/tag/00TS) in the Stacks Project.

**`Algebra.isSmoothAt_tfae_of_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/RegularLocalRing/ClosedPointRegularity.lean, line 719](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/RegularLocalRing/ClosedPointRegularity.lean#L719). The attribute's comment: “The residue field `κ(𝔪)` is `S ⧸ 𝔪`, and the fibre `Ω_{S/k} ⊗_S κ(𝔪)` is the base change `(S ⧸ 𝔪) ⊗[S] Ω[S⁄k]`, whose factors are transposed so that the left one carries the scalar action making it a `κ(𝔪)`-vector space. `dim S_𝔪` is `ringKrullDim Sₘ` for an arbitrary model `Sₘ` of the localization, matching Mathlib's `IsRegularLocalRing`. The source's item (4) is stated twice, as the existential and as Mathlib's `Algebra.IsSmoothAt`; those are items 4 and 5. See the module docstring.”. References: EGA 0 (22.6.7), “alg. closed k, max ideal”; EGA IV (17.15.5), “affine, k alg closed”; EGA IV (17.15.9), “k alg closed, closed pt”; SGA 1 II (5.3), “alg. closed k, max ideal”; SGA 1 II (5.5), “alg closed k, closed pt”; SGA 1 II (5.9), “k alg closed, closed pt”.

> **Regularity at a closed point equals smoothness, over an algebraically closed field**
> (Stacks 00TS). For an algebraically closed field `k`, a finite type `k`-algebra `S`, a maximal
> ideal `𝔪 ⊆ S` and a model `Sₘ` of `S_𝔪`, the following are equivalent: (1) `S_𝔪` is a regular
> local ring; (2) `dim_{κ(𝔪)} Ω_{S/k} ⊗_S κ(𝔪) ≤ dim S_𝔪`; (3) the same with equality;
> (4) there is a `g ∈ S`, `g ∉ 𝔪`, with `S_g` smooth over `k`; (5) in other words, `S/k` is smooth
> at `𝔪`.

```lean
public theorem Algebra.isSmoothAt_tfae_of_isAlgClosed {k S : Type*} [Field k] [IsAlgClosed k]
    [CommRing S] [Algebra k S] [Algebra.FiniteType k S] (𝔪 : Ideal S) [𝔪.IsMaximal]
    (Sₘ : Type*) [CommRing Sₘ] [Algebra S Sₘ] [IsLocalization.AtPrime Sₘ 𝔪] :
    List.TFAE
      [IsRegularLocalRing Sₘ,
       (Module.finrank (S ⧸ 𝔪) ((S ⧸ 𝔪) ⊗[S] Ω[S⁄k]) : WithBot ℕ∞) ≤ ringKrullDim Sₘ,
       (Module.finrank (S ⧸ 𝔪) ((S ⧸ 𝔪) ⊗[S] Ω[S⁄k]) : WithBot ℕ∞) = ringKrullDim Sₘ,
       ∃ g ∉ 𝔪, Algebra.Smooth k (Localization.Away g),
       Algebra.IsSmoothAt k 𝔪]
```

## Tag 00TT, a lemma

[Tag 00TT](https://stacks.math.columbia.edu/tag/00TT) in the Stacks Project.

**`Algebra.isSmoothAt_tfae_localKrullDim_and_isRegularLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/RegularLocalRing/LocalDimensionCriterion.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/RegularLocalRing/LocalDimensionCriterion.lean#L379). The attribute's comment: “`𝔮` and `x` are one datum `x : PrimeSpectrum S` with `𝔮 = x.asIdeal`; `dim_x X` is `TopologicalSpace.localKrullDim`, Topology Definition 0055 (4); `κ(𝔮)` is `Ideal.ResidueField x.asIdeal` and the fibre `Ω_{S/k} ⊗_S κ(𝔮)` is the base change `κ(𝔮) ⊗[S] Ω[S⁄k]`, whose factors are transposed so that the left one carries the scalar action making it a `κ(𝔮)`-vector space; `S_𝔮` is an arbitrary model `Sq`. The source's `moreover` is the final conjunct and not a fourth equivalent item, regularity being strictly weaker than smoothness over a nonperfect field. See the module docstring.”. References: EGA IV (17.15.5), “affine case”; SGA 1 II (5.3), “first assertion”; SGA 1 II (5.5), “affine (i)<=>(ii bis)”.

> **Smoothness at a point is the differential fibre having the local dimension**
> (Stacks 00TT). Let `k` be a field, let `S` be a finite type `k`-algebra, let `X = Spec S`, let
> `x ∈ X` be a point with prime ideal `𝔮 = x.asIdeal`, and let `Sq` be a model of `S_𝔮`. The
> following are equivalent: (1) `S` is smooth at `𝔮` over `k`; (2)
> `dim_{κ(𝔮)} Ω_{S/k} ⊗_S κ(𝔮) ≤ dim_x X`; (3) the same with equality. Moreover, in this case the
> local ring `S_𝔮` is regular.

```lean
public theorem Algebra.isSmoothAt_tfae_localKrullDim_and_isRegularLocalRing
    {k S : Type*} [Field k] [CommRing S] [Algebra k S] [Algebra.FiniteType k S]
    (x : PrimeSpectrum S) (Sq : Type*) [CommRing Sq] [Algebra S Sq]
    [IsLocalization.AtPrime Sq x.asIdeal] :
    List.TFAE
      [Algebra.IsSmoothAt k x.asIdeal,
       (Module.finrank x.asIdeal.ResidueField (x.asIdeal.ResidueField ⊗[S] Ω[S⁄k]) : WithBot ℕ∞) ≤
         localKrullDim (PrimeSpectrum S) x,
       (Module.finrank x.asIdeal.ResidueField (x.asIdeal.ResidueField ⊗[S] Ω[S⁄k]) : WithBot ℕ∞) =
         localKrullDim (PrimeSpectrum S) x] ∧
      (Algebra.IsSmoothAt k x.asIdeal → IsRegularLocalRing Sq)
```

## Tag 00TU, a lemma

[Tag 00TU](https://stacks.math.columbia.edu/tag/00TU) in the Stacks Project.

**`KaehlerDifferential.kerCotangentToTensor_injective_of_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Kaehler/Separable.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Kaehler/Separable.lean#L199). The attribute's comment: “`d` is `KaehlerDifferential.kerCotangentToTensor k R B`, whose domain `(RingHom.ker (algebraMap R B)).Cotangent` is `I/I²` and whose codomain `B ⊗[R] Ω[R⁄k]` has the factors of the source's `Ω_{R/k} ⊗_R κ` transposed, so that the left one carries the `B`-vector space structure. Finitely generated separable is `Algebra.EssFiniteType` together with the notion of Stacks 030O (2). Generalized: the quotient is an arbitrary surjection onto a field rather than the residue field of a local ring, and `R` is not assumed Noetherian; the source's statement is the case `B := IsLocalRing.ResidueField R`. See the module docstring.”.

> **The differential is injective on `I/I²` for a separable field quotient** (Stacks 00TU).
> Let `k` be a field, let `R` be a `k`-algebra and let `R → B` be a surjection onto a field `B`
> which is a finitely generated separable extension of `k`. Then `d : I/I² → Ω_{R/k} ⊗_R B`,
> `x ↦ 1 ⊗ dx`, is injective, where `I = ker(R → B)`. For `R` local and `B = R/𝔪` this is
> injectivity of `d` on `𝔪/𝔪²`.

```lean
public theorem KaehlerDifferential.kerCotangentToTensor_injective_of_isSeparableExtension
    (k R B : Type*) [Field k] [CommRing R] [Field B] [Algebra k R] [Algebra R B] [Algebra k B]
    [IsScalarTower k R B] [Algebra.EssFiniteType k B] [Algebra.IsSeparableExtension k B]
    (h : Function.Surjective (algebraMap R B)) :
    Function.Injective (kerCotangentToTensor k R B)
```

## Tag 00TV, a lemma

[Tag 00TV](https://stacks.math.columbia.edu/tag/00TV) in the Stacks Project.

**`Algebra.isSmoothAt_iff_isRegularLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/RegularLocalRing/SeparableResidueRegular.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/RegularLocalRing/SeparableResidueRegular.lean#L409). The attribute's comment: “`κ(𝔮)` is `Ideal.ResidueField q`, and its separability over `k` is `Algebra.IsSeparableExtension`, Definition 030O (2); that does not presuppose algebraicity, so it is not `Algebra.IsSeparable`. `S_𝔮` is an arbitrary model `Sq`, pinned by `IsLocalization.AtPrime Sq q`; regularity is `IsRegularLocalRing` (Definition 00KU) and smoothness at `𝔮` is `Algebra.IsSmoothAt`. The two-item enumeration is an `Iff`. Finite generation of `κ(𝔮)/k` is not assumed, being a consequence of `Algebra.FiniteType k S`. See the module docstring.”. References: EGA IV (17.15.1), “last assertion”; EGA 0 (22.6.7), “separable residue field”; EGA IV (17.15.9), “a)”; SGA 1 II (5.4), “affine local, κ(q)/k sep”; SGA 1 II (5.10), “affine case”; SGA 1 II (5.3), “regular ⇒ smooth”; SGA 1 II (5.9), “(i) <=> smooth in (ii)”.

> **Smoothness at a prime with separable residue field is regularity** (Stacks 00TV). Let `k` be
> a field, let `S` be a finite type `k`-algebra, let `𝔮 ⊆ S` be a prime whose residue field `κ(𝔮)`
> is separable over `k`, and let `Sq` be a model of `S_𝔮`. Then `S` is smooth at `𝔮` over `k` if and
> only if `S_𝔮` is a regular local ring.

```lean
public theorem Algebra.isSmoothAt_iff_isRegularLocalRing
    {k S : Type*} [Field k] [CommRing S] [Algebra k S] [Algebra.FiniteType k S]
    (q : Ideal S) [q.IsPrime] [Algebra.IsSeparableExtension k q.ResidueField]
    (Sq : Type*) [CommRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq q] :
    Algebra.IsSmoothAt k q ↔ IsRegularLocalRing Sq
```

## Tag 00TW, a lemma

[Tag 00TW](https://stacks.math.columbia.edu/tag/00TW) in the Stacks Project.

**`not_isNilpotent_of_hasFreeSummandDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/CotangentAtMaximalIdeal.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/CotangentAtMaximalIdeal.lean#L257). The attribute's comment: “(1)”.

> Let `R → S` be a map of `ℚ`-algebras with `S` nonzero, and let `f ∈ S` be such that
> `Ω[S⁄R] = S·df ⊕ C` with `df` a free generator of `S·df`. Then `f` is not nilpotent.

```lean
theorem not_isNilpotent_of_hasFreeSummandDifferential
    (R S : Type*) [CommRing R] [CommRing S]
    [Algebra ℚ R] [Algebra ℚ S] [Algebra R S] [IsScalarTower ℚ R S] [Nontrivial S]
    (f : S) (hf : HasFreeSummandDifferential R S f) :
    ¬ IsNilpotent f
```

**`nonzerodivisor_of_hasFreeSummandDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/CotangentAtMaximalIdeal.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/CotangentAtMaximalIdeal.lean#L286). The attribute's comment: “(2)”.

> Let `R → S` be a map of `ℚ`-algebras with `S` a Noetherian local ring, and let `f ∈ S` be such
> that `Ω[S⁄R] = S·df ⊕ C` with `df` a free generator of `S·df`. Then `f` is a nonzerodivisor:
> `f * a = 0 → a = 0`.

```lean
theorem nonzerodivisor_of_hasFreeSummandDifferential
    (R S : Type*) [CommRing R] [CommRing S]
    [Algebra ℚ R] [Algebra ℚ S] [Algebra R S] [IsScalarTower ℚ R S]
    [IsNoetherianRing S] [IsLocalRing S]
    (f : S) (hf : HasFreeSummandDifferential R S f) :
    ∀ a : S, f * a = 0 → a = 0
```

## Tag 00TX, a lemma

[Tag 00TX](https://stacks.math.columbia.edu/tag/00TX) in the Stacks Project.

**`Algebra.isSmoothAt_tfae_free_kaehlerDifferential_isRegularLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/RegularLocalRing/CharZeroRegularity.lean, line 607](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/RegularLocalRing/CharZeroRegularity.lean#L607). The attribute's comment: “The localized module `Ω_{S/k, 𝔮}` is `Ω[Sq⁄k]`, which by `KaehlerDifferential.isLocalizedModule_map` is the localization of `Ω[S⁄k]` at `q.primeCompl`, the identification the source's own proof uses. The source's parenthetical `(finite)` is not a conjunct: `Module.Finite Sq Ω[Sq⁄k]` holds unconditionally here. `S_𝔮` is an arbitrary model `Sq`, pinned by `IsLocalization.AtPrime Sq q` and `IsScalarTower k S Sq`, as in the siblings 00TT and 00TV; regularity is `IsRegularLocalRing` (Definition 00KU (2)) and smoothness at `𝔮` is `Algebra.IsSmoothAt`. The three-item enumeration is a `List.TFAE`. See the module docstring.”. References: EGA IV (17.15.7), “affine case”; EGA IV (17.15.5), “affine, char 0”; SGA 1 II (5.7), “char 0, local at prime”; SGA 1 II (5.4), “char 0, affine local”; SGA 1 II (5.5), “char 0, affine, k'=k”; SGA 1 II (5.9), “characteristic zero”; SGA 1 III (5.2), “special case”.

> **Smoothness, free differentials and regularity agree in characteristic zero**
> (Stacks 00TX). Let `k` be a field of characteristic `0`, let `S` be a finite type `k`-algebra, let
> `𝔮 ⊆ S` be a prime and let `Sq` be a model of `S_𝔮`. The following are equivalent: (1) `S` is
> smooth at `𝔮` over `k`; (2) the `S_𝔮`-module `Ω_{S/k, 𝔮}` is free; (3) the local ring `S_𝔮` is
> regular.

```lean
public theorem Algebra.isSmoothAt_tfae_free_kaehlerDifferential_isRegularLocalRing
    {k S : Type*} [Field k] [CharZero k] [CommRing S] [Algebra k S] [Algebra.FiniteType k S]
    (q : Ideal S) [q.IsPrime] (Sq : Type*) [CommRing Sq] [Algebra k Sq] [Algebra S Sq]
    [IsScalarTower k S Sq] [IsLocalization.AtPrime Sq q] :
    List.TFAE
      [Algebra.IsSmoothAt k q,
       Module.Free Sq Ω[Sq⁄k],
       IsRegularLocalRing Sq]
```

## Tag 07ND, a lemma

[Tag 07ND](https://stacks.math.columbia.edu/tag/07ND) in the Stacks Project.

**`Algebra.smoothAt_bot_iff_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/GenericPoint.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/GenericPoint.lean#L112). The attribute's comment: “Smoothness at `(0)` is Definition 00TB, `Algebra.SmoothAt R S (⊥ : Ideal S)`: some `g ∉ (0)` with `Localization.Away g` smooth (so of finite presentation) over `R`, not Mathlib's `Algebra.IsSmoothAt`, which is only formal smoothness of `S_{(0)}`; the formal-smoothness form is `Algebra.isSmoothAt_bot_iff_isSeparableExtension`, and the passage to 00TB uses generic finite presentation (00FG). Separability of the possibly transcendental extension `L/K` is `Algebra.IsSeparableExtension`, Definition 030O (2), not `Algebra.IsSeparable`. The fraction fields are abstract, pinned by `IsFractionRing`, and the source's injectivity of `R → S` is implied by the compatible `K`-algebra structure on `L` rather than assumed. See the module docstring.”.

> **Smoothness at the generic point is separability of the fraction field extension**
> (Stacks 07ND). Let `R → S` be a finite type map of domains, let `K` and `L` be the fraction fields
> of `R` and `S`, and let `L` be a `K`-algebra compatibly with both towers — which forces `R → S` to
> be injective. Then `R → S` is smooth at `𝔮 = (0)` in the sense of Definition 00TB — some nonzero
> `g ∈ S` has `S_g` smooth over `R` — if and only if `L/K` is separable.

```lean
public theorem Algebra.smoothAt_bot_iff_isSeparableExtension (R S K L : Type*)
    [CommRing R] [CommRing S] [Field K] [Field L] [IsDomain R] [IsDomain S]
    [Algebra R S] [Algebra.FiniteType R S] [Algebra R K] [IsFractionRing R K]
    [Algebra S L] [IsFractionRing S L] [Algebra R L] [Algebra K L]
    [IsScalarTower R S L] [IsScalarTower R K L] :
    Algebra.SmoothAt R S (⊥ : Ideal S) ↔ Algebra.IsSeparableExtension K L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.140, Tag 00TQ](https://stacks.math.columbia.edu/tag/00TQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
