---
declaration: section
origin: cited
lean: IsCohenMacaulayLocalRing, Module.IsMaximalCohenMacaulay.isRegular_iff_ringKrullDim_add_length_eq_ringKrullDim, Module.IsMaximalCohenMacaulay.length_eq_ringKrullDim, Module.IsMaximalCohenMacaulay.ringKrullDim_eq_height_add_ringKrullDim_quotient, Module.IsMaximalCohenMacaulay.of_isLocalization_atPrime, IsCohenMacaulayRing, Module.IsMaximalCohenMacaulay.of_isLocalization_atPrime_mvPolynomial, Module.IsMaximalCohenMacaulay.depth_lt_depth_or_isMaximalCohenMacaulay_of_exact
statement: formalized
proof: formalized
---

# 10.104 Cohen-Macaulay rings

Section 10.104 of the Stacks Project, [Tag 00N7](https://stacks.math.columbia.edu/tag/00N7). 10 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00N8, a definition

[Tag 00N8](https://stacks.math.columbia.edu/tag/00N8) in the Stacks Project.

**`IsCohenMacaulayLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Defs.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Defs.lean#L206). References: EGA 0 (16.5.13), “local ring”; EGA 0 (16.5.1); EGA IV (5.7.1); EGA IV (7.5.3).

> A Noetherian local ring `R` is called *Cohen–Macaulay* if it is
> Cohen–Macaulay as a module over itself.

```lean
def IsCohenMacaulayLocalRing (R : Type*) [CommRing R] [IsNoetherianRing R] [IsLocalRing R] :
    Prop
```

## Tag 02JN, a lemma

[Tag 02JN](https://stacks.math.columbia.edu/tag/02JN) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.isRegular_iff_ringKrullDim_add_length_eq_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/RegularSequence/DimensionCriterion.lean, line 567](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/RegularSequence/DimensionCriterion.lean#L567). The attribute's comment: “`R` Cohen–Macaulay is `Module.IsMaximalCohenMacaulay R R` (Definition 00NF at `M = R`, equal to Definition 00N8 by `Module.supportDim_self_eq_ringKrullDim`); the source's `dim(R/(x₁, …, x_i)) = dim(R) - i` is stated additively, as in `ringKrullDim_add_length_eq_ringKrullDim_of_isRegular`; the extension is an append, and the local ring structures on the quotients are existentially bound. See the module docstring.”. References: EGA 0 (16.5.6), “M = R (CM local ring)”; EGA 0 (16.5.5), “M = R; a) ⇔ b)”; EGA 0 (16.5.7), “case M = R”; EGA 0 (16.5.9), “special case”; SGA 2 III (2.6), “M = R, CM local”.

> **Regular sequences in a Cohen–Macaulay local ring are those cutting out the right
> dimension.** Let `(R, 𝔪)` be a Noetherian local Cohen–Macaulay ring and let `xs = x₁, …, x_c` be
> a list of elements of `𝔪`. Then `xs` is a regular sequence if and only if
> `dim(R/(x₁, …, x_c)) + c = dim(R)`, and in that case `xs` extends by elements of `𝔪` to a regular
> sequence of length `dim(R)` and each `R/(x₁, …, x_i)` is a Cohen–Macaulay local ring of dimension
> `dim(R) - i`. The source's subtraction is moved to the other side of the equations, Krull
> dimensions being valued in `WithBot ℕ∞`; see the module docstring.

```lean
public theorem Module.IsMaximalCohenMacaulay.isRegular_iff_ringKrullDim_add_length_eq_ringKrullDim
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hR : Module.IsMaximalCohenMacaulay R R) (xs : List R)
    (hxs : ∀ x ∈ xs, x ∈ maximalIdeal R) :
    (RingTheory.Sequence.IsRegular R xs ↔
        ringKrullDim (R ⧸ Ideal.ofList xs) + xs.length = ringKrullDim R) ∧
      (RingTheory.Sequence.IsRegular R xs →
        (∃ ys : List R, (∀ y ∈ ys, y ∈ maximalIdeal R) ∧
            RingTheory.Sequence.IsRegular R (xs ++ ys) ∧
            ((xs ++ ys).length : WithBot ℕ∞) = ringKrullDim R) ∧
        ∀ i ≤ xs.length, ∃ _ : IsLocalRing (R ⧸ Ideal.ofList (xs.take i)),
          Module.IsMaximalCohenMacaulay (R ⧸ Ideal.ofList (xs.take i))
              (R ⧸ Ideal.ofList (xs.take i)) ∧
            ringKrullDim (R ⧸ Ideal.ofList (xs.take i)) + i = ringKrullDim R)
```

## Tag 00N9, a lemma

[Tag 00N9](https://stacks.math.columbia.edu/tag/00N9) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.length_eq_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean, line 897](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean#L897). The attribute's comment: “Cohen-Macaulayness of the Noetherian local ring `R` is the predicate `Module.IsMaximalCohenMacaulay R R` (Definition 00N8, i.e. `depth_𝔪(R) = dim R`); a maximal chain of primes is a `RelSeries` for the covering relation `⋖` on `PrimeSpectrum R` whose head is minimal and whose last is maximal; the source's name `d` for `dim R` is dropped. See the module docstring.”. References: EGA IV (15.4.1), “special case”.

> **Maximal chains of primes in a Cohen–Macaulay local ring.** Let `R` be a Noetherian local
> Cohen–Macaulay ring, that is `depth_𝔪(R) = dim(R)`. Then every maximal chain of primes of `R` —
> one whose steps are covering pairs `𝔭_i ⋖ 𝔭_{i + 1}`, starting at a minimal prime and ending at
> the maximal ideal — has length `dim(R)`.

```lean
public theorem Module.IsMaximalCohenMacaulay.length_eq_ringKrullDim
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hR : Module.IsMaximalCohenMacaulay R R)
    (s : RelSeries {(p, q) : PrimeSpectrum R × PrimeSpectrum R | p ⋖ q})
    (hmin : IsMin s.head) (hmax : IsMax s.last) :
    (s.length : WithBot ℕ∞) = ringKrullDim R
```

## Tag 00NA, a lemma

[Tag 00NA](https://stacks.math.columbia.edu/tag/00NA) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.ringKrullDim_eq_height_add_ringKrullDim_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean, line 1321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean#L1321). The attribute's comment: “Cohen-Macaulayness of `R` is the hypothesis `Module.IsMaximalCohenMacaulay R R`, i.e. `depth_𝔪(R) = dim R` (Definition 00N8); `dim(R_𝔭)` is written `𝔭.height`; the source's name `d` for `dim R` is dropped.”. References: EGA 0 (16.5.11), “case M = R”; EGA 0 (16.5.10), “(ii) for M = A”; EGA IV (15.4.1), “special case”.

> **The dimension formula in a Cohen–Macaulay local ring.** If `R` is a Noetherian local
> Cohen–Macaulay ring, that is `depth_𝔪(R) = dim R`, then every prime `𝔭` of `R` satisfies
> `dim R = dim R_𝔭 + dim R/𝔭`, the dimension of the localisation `R_𝔭` being written as the
> height of `𝔭`.

```lean
public theorem Module.IsMaximalCohenMacaulay.ringKrullDim_eq_height_add_ringKrullDim_quotient
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hR : Module.IsMaximalCohenMacaulay R R) (p : Ideal R) [p.IsPrime] :
    ringKrullDim R = p.height + ringKrullDim (R ⧸ p)
```

## Tag 00NB, a lemma

[Tag 00NB](https://stacks.math.columbia.edu/tag/00NB) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.of_isLocalization_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Localization.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Localization.lean#L439). The attribute's comment: “Cohen-Macaulayness of a Noetherian local ring is the predicate `Module.IsMaximalCohenMacaulay S S`, i.e. `depth_{𝔪_S}(S) = dim S` (Definition 00N8); the localization is an abstract `IsLocalization.AtPrime`. See the module docstring.”. References: EGA 0 (16.5.10), “(i) for M = A”; EGA 0 (16.5.13), “partial”; EGA IV (6.11.5), “special case”.

> **Cohen–Macaulayness localizes at a prime.** If `R` is a Noetherian local Cohen–Macaulay
> ring, that is `depth_𝔪(R) = dim R`, then for every prime `𝔭` of `R` the local ring `R_𝔭` is
> Cohen–Macaulay: `depth_{𝔭R_𝔭}(R_𝔭) = dim R_𝔭`. The localization is any `R`-algebra `Rₚ` with
> `IsLocalization.AtPrime Rₚ p`.

```lean
public theorem Module.IsMaximalCohenMacaulay.of_isLocalization_atPrime {R : Type*} [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] (hR : Module.IsMaximalCohenMacaulay R R) (p : Ideal R)
    [p.IsPrime] (Rₚ : Type*) [CommRing Rₚ] [Algebra R Rₚ] [IsLocalization.AtPrime Rₚ p]
    [IsLocalRing Rₚ] : Module.IsMaximalCohenMacaulay Rₚ Rₚ
```

## Tag 00NC, a definition

[Tag 00NC](https://stacks.math.columbia.edu/tag/00NC) in the Stacks Project.

**`IsCohenMacaulayRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Defs.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Defs.lean#L248). References: EGA 0 (16.5.13); EGA IV (7.5.3).

> A Noetherian ring `R` is *Cohen–Macaulay* if every localisation `R_𝔭` at a
> prime ideal `𝔭` is a Cohen–Macaulay local ring.

```lean
def IsCohenMacaulayRing (R : Type*) [CommRing R] [IsNoetherianRing R] : Prop
```

## Tag 00ND, a lemma

[Tag 00ND](https://stacks.math.columbia.edu/tag/00ND) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.of_isLocalization_atPrime_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/MvPolynomial.lean, line 1575](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/MvPolynomial.lean#L1575). The attribute's comment: “Cohen-Macaulayness of a Noetherian local ring is `Module.IsMaximalCohenMacaulay S S` (Definition 00N8); that of a Noetherian ring (Definition 00NC) is spelled out as a condition on its localizations at primes, the hypothesis at the concrete `Localization.AtPrime` and the conclusion at an abstract `IsLocalization.AtPrime`; `R[x_1, …, x_n]` is `MvPolynomial σ R` for finite `σ`. See the module docstring.”. References: EGA IV (6.3.6); EGA IV (6.11.9).

> **A polynomial algebra over a Noetherian Cohen–Macaulay ring is Cohen–Macaulay.** Let `R` be
> a Noetherian ring all of whose local rings `R_𝔭` are Cohen–Macaulay, and let `σ` be finite. Then
> for every prime `𝔮` of `R[x_i : i ∈ σ]`, every localization `S` of `R[x_i : i ∈ σ]` at `𝔮` is a
> Cohen–Macaulay local ring.

```lean
public theorem Module.IsMaximalCohenMacaulay.of_isLocalization_atPrime_mvPolynomial {R : Type*}
    [CommRing R] [IsNoetherianRing R]
    (hR :
      ∀ (p : Ideal R) [p.IsPrime],
        Module.IsMaximalCohenMacaulay (Localization.AtPrime p) (Localization.AtPrime p))
    {σ : Type*} [Finite σ] (q : Ideal (MvPolynomial σ R)) [q.IsPrime] (S : Type*) [CommRing S]
    [Algebra (MvPolynomial σ R) S] [IsLocalization.AtPrime S q] [IsLocalRing S] :
    Module.IsMaximalCohenMacaulay S S
```

## Tag 00NE, a lemma

[Tag 00NE](https://stacks.math.columbia.edu/tag/00NE) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.depth_lt_depth_or_isMaximalCohenMacaulay_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Syzygy.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Syzygy.lean#L338). The attribute's comment: “Cohen-Macaulayness of the Noetherian local ring `R` is `Module.IsMaximalCohenMacaulay R R`, i.e. `depth_𝔪(R) = dim R` (Definition 00N8); `R^{⊕n}` is an arbitrary finite free module `F`; the alternative `M = 0` is the hypothesis `[Nontrivial M]`; and `depth(K) = depth(M) = d` is maximal Cohen-Macaulayness of `K` and of `M`. See the module docstring.”.

> **Depth of a syzygy module over a Cohen–Macaulay local ring.** Let `(R, 𝔪)` be a Noetherian
> local Cohen–Macaulay ring, that is `depth_𝔪(R) = dim R`, let `F` be a finite free `R`-module and
> let `0 → K → F → M → 0` be a short exact sequence of `R`-modules, given by `f : K →ₗ[R] F`
> injective, `g : F →ₗ[R] M` surjective and `Function.Exact f g`, with `M` nonzero. Then either
> `depth_𝔪(M) < depth_𝔪(K)`, or `depth_𝔪(K) = depth_𝔪(M) = dim R`, i.e. both `K` and `M` are
> maximal Cohen–Macaulay.
>
> The source states the third alternative as `depth(K) = depth(M) = d` and the middle term as
> `R^{⊕n}`, and lists `M = 0` as a first alternative in place of the hypothesis
> `[Nontrivial M]`.

```lean
public theorem IsMaximalCohenMacaulay.depth_lt_depth_or_isMaximalCohenMacaulay_of_exact
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hR : IsMaximalCohenMacaulay R R) {K F M : Type*} [AddCommGroup K] [Module R K]
    [AddCommGroup F] [Module R F] [Module.Free R F] [Module.Finite R F] [AddCommGroup M]
    [Module R M] [Nontrivial M] {f : K →ₗ[R] F} {g : F →ₗ[R] M} (h : Function.Exact f g)
    (hf : Function.Injective f) (hg : Function.Surjective g) :
    depth R (maximalIdeal R) M < depth R (maximalIdeal R) K ∨
      (IsMaximalCohenMacaulay R K ∧ IsMaximalCohenMacaulay R M)
```

## Tag 00NG, a lemma

[Tag 00NG](https://stacks.math.columbia.edu/tag/00NG) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.exists_composableArrows_exact_free_and_isMaximalCohenMacaulay_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/FreeComplex.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/FreeComplex.lean#L479). The attribute's comment: “Cohen-Macaulayness of the Noetherian local ring `R` is `Module.IsMaximalCohenMacaulay R R`, i.e. `depth_𝔪(R) = dim R` (Definition 00N8); the complex is a `ComposableArrows (ModuleCat R) (d - e + 1)` whose rightmost object is `M`, its interior exactness being `Exact` and the outer two conditions `Mono` and `Epi` as in `ShortComplex.ShortExact`. See the module docstring.”.

> **Finite free complexes with a maximal Cohen–Macaulay kernel.** Let `(R, 𝔪)` be a Noetherian
> local Cohen–Macaulay ring, that is `depth_𝔪(R) = dim R`, of dimension `d`, and let `M` be a
> finite `R`-module of depth `e`. Then there is an exact complex
>
>   `0 → K → F_{d-e-1} → ⋯ → F₀ → M → 0`
>
> of `R`-modules with the `d - e` modules `Fᵢ` finite free and `K` maximal Cohen–Macaulay. The
> complex is a `ComposableArrows (ModuleCat R) (d - e + 1)` with rightmost object `M`, whose
> exactness at the interior objects `Fᵢ` is `S.Exact` and whose outer two exactness conditions are
> `Mono (S.map' 0 1)` and `Epi (S.map' (d - e) (d - e + 1))`; the module `K` is its leftmost
> object `S.left`.

```lean
public theorem exists_composableArrows_exact_free_and_isMaximalCohenMacaulay_left {R : Type u}
    [CommRing R] [IsNoetherianRing R] [IsLocalRing R] (hR : Module.IsMaximalCohenMacaulay R R)
    (M : ModuleCat.{u} R) [Module.Finite R M] {d e : ℕ} (hd : ringKrullDim R = d)
    (he : Module.depth R (maximalIdeal R) M = e) :
    ∃ S : ComposableArrows (ModuleCat.{u} R) (d - e + 1),
      S.right = M ∧ S.Exact ∧ Mono (S.map' 0 1) ∧ Epi (S.map' (d - e) (d - e + 1)) ∧
        (∀ i, Module.Finite R (S.obj i)) ∧
        (∀ (i : ℕ) (hi : i < d - e), Module.Free R (S.obj' (i + 1))) ∧
        Module.IsMaximalCohenMacaulay R S.left
```

## Tag 06LC, a lemma

[Tag 06LC](https://stacks.math.columbia.edu/tag/06LC) in the Stacks Project.

**`exists_isRegular_map_length_eq_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/RegularSequence/LocalRingMap.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/RegularSequence/LocalRingMap.lean#L639).

> The main theorem (Stacks Tag 06LC).  Reduce to the engine lemma at `d` the finite value
> of `ringKrullDim B`.

```lean
theorem exists_isRegular_map_length_eq_ringKrullDim {A B : Type*} [CommRing A] [CommRing B]
  [IsLocalRing A] [IsLocalRing B]
    [IsNoetherianRing B] (hCM : IsCohenMacaulayLocalRing B) (φ : A →+* B)
    (h : IsLocalRing.maximalIdeal B = (Ideal.map φ (IsLocalRing.maximalIdeal A)).radical) :
    ∃ f : List A,
      (f.length : WithBot ℕ∞) = ringKrullDim B ∧ RingTheory.Sequence.IsRegular B (f.map φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.104, Tag 00N7](https://stacks.math.columbia.edu/tag/00N7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
