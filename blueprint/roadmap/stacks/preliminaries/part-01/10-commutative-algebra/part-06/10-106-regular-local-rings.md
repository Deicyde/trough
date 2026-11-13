---
declaration: section
origin: cited
lean: IsRegularLocalRing.gradedRing_maximalIdeal_isPolynomialAlgebra, IsRegularLocalRing.isQuasiRegular, IsRegularLocalRing.isDomain, Stacks.Blowup.isWeaklyRegular_of_span_range_eq_maximalIdeal, IsRegularLocalRing.isRegular_and_isRegularLocalRing_quotient_and_isMaximalCohenMacaulay, IsRegularLocalRing.exists_ofList_eq_maximalIdeal_length_eq_spanFinrank_and_ofList_take_eq, free_mod_x, regular_mcm_free
statement: formalized
proof: formalized
---

# 10.106 Regular local rings

Section 10.106 of the Stacks Project, [Tag 00NN](https://stacks.math.columbia.edu/tag/00NN). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00NO, a lemma

[Tag 00NO](https://stacks.math.columbia.edu/tag/00NO) in the Stacks Project.

**`IsRegularLocalRing.gradedRing_maximalIdeal_isPolynomialAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/AssociatedGradedPolynomial.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/AssociatedGradedPolynomial.lean#L432). The attribute's comment: “The graded-RING form: the canonical ring map `κ[X_1, …, X_d] → ⨁_{n ≥ 0} 𝔪^n/𝔪^(n+1)`, `X_i ↦ x_i mod 𝔪^2`, of a minimal generating sequence of the maximal ideal is bijective, and carries the degree-`n` homogeneous polynomials exactly onto `𝔪^n/𝔪^(n+1)`; that is the source's isomorphism of the graded ring with the graded polynomial algebra, with the isomorphism pinned to the source's own map rather than merely asserted. See also `IsRegularLocalRing.isQuasiRegular` for the graded-module form (Tag 061N/061P).”.

> **Stacks 00NO, in the form of a graded-ring isomorphism.** Let `(R, 𝔪, κ)` be a regular local
> ring of dimension `d` and let `xs = x_1, …, x_d` be a minimal set of generators of `𝔪`, that is, a
> list generating `𝔪` whose length is the minimal number of generators of `𝔪` (which equals `dim R`).
> Then the canonical map of graded rings
> `κ[X_1, …, X_d] → ⨁_{n ≥ 0} 𝔪^n/𝔪^(n+1)`, `X_i ↦ x_i mod 𝔪^2`,
> is bijective (first clause) and carries the homogeneous polynomials of degree `n` onto the
> degree-`n` part `𝔪^n/𝔪^(n+1)` (second clause). Together: the graded ring
> `⨁_{n ≥ 0} 𝔪^n/𝔪^(n+1)` is the graded polynomial algebra `κ[X_1, …, X_d]` over the residue
> field, as graded rings.

```lean
public theorem gradedRing_maximalIdeal_isPolynomialAlgebra
    (hxs : Ideal.ofList xs = maximalIdeal R)
    (hmin : xs.length = (maximalIdeal R).spanFinrank)
    (hx : ∀ i : Fin xs.length, xs[i] ∈ maximalIdeal R) :
    Function.Bijective
        (AssociatedGraded.polyGradedHom (maximalIdeal R) (fun i : Fin xs.length => xs[i]) hx) ∧
      ∀ (n : ℕ) (y : AssociatedGraded.gradedRing (maximalIdeal R)),
        y ∈ AssociatedGraded.grading (maximalIdeal R) n ↔
          ∃ p : MvPolynomial (Fin xs.length) (R ⧸ maximalIdeal R), p.IsHomogeneous n ∧
            AssociatedGraded.polyGradedHom (maximalIdeal R)
              (fun i : Fin xs.length => xs[i]) hx p = y
```

**`IsRegularLocalRing.isQuasiRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Basic.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/Basic.lean#L478). The attribute's comment: “Stated as quasi-regularity (Tag 061P) of a minimal generating sequence of the maximal ideal, which is exactly the assertion that the source's graded surjection `κ[X_1, …, X_d] → ⨁ m^n/m^(n+1)`, `X_i ↦ x_i mod m^2`, is an isomorphism. See the module docstring.”.

> **Stacks 00NO.** Let `(R, m, κ)` be a regular local ring of dimension `d` and let
> `xs = x_1, …, x_d` be a minimal set of generators of `m`, that is, a list generating `m` whose
> length is the minimal number of generators of `m` (which equals `dim R`). Then `xs` is a
> quasi-regular sequence: the canonical map of graded `κ[X_1, …, X_d]`-modules
> `κ[X_1, …, X_d] ⊗_κ (R/m) → ⨁_{n ≥ 0} m^n/m^(n + 1)`, `X^e ⊗ 1 ↦ x^e mod m^(|e| + 1)`, is
> bijective. Equivalently, the graded ring `⨁_{n ≥ 0} m^n/m^(n + 1)` is the graded polynomial
> algebra `κ[X_1, …, X_d]` over the residue field.

```lean
public theorem IsRegularLocalRing.isQuasiRegular {R : Type*} [CommRing R] [IsRegularLocalRing R]
    (xs : List R) (hxs : Ideal.ofList xs = maximalIdeal R)
    (hmin : xs.length = (maximalIdeal R).spanFinrank) :
    RingTheory.Sequence.IsQuasiRegular R xs
```

## Tag 00NP, a lemma

[Tag 00NP](https://stacks.math.columbia.edu/tag/00NP) in the Stacks Project.

**`IsRegularLocalRing.isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Basic.lean, line 779](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/Basic.lean#L779).

> **A regular local ring is a domain.** If the maximal ideal of a Noetherian local ring `R` can
> be generated by `dim R` elements, then `R` has no zero divisors.

```lean
public theorem IsRegularLocalRing.isDomain (R : Type*) [CommRing R] [IsRegularLocalRing R] :
    IsDomain R
```

## Tag 00NQ, a lemma

[Tag 00NQ](https://stacks.math.columbia.edu/tag/00NQ) in the Stacks Project.

**`Stacks.Blowup.isWeaklyRegular_of_span_range_eq_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ProjectiveLineExceptional.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/ProjectiveLineExceptional.lean#L307). The attribute's comment: “for a two-dimensional regular local ring and a two-element generating family of the maximal ideal”.

> **Two generators of the maximal ideal of a regular local ring of dimension two form a regular
> sequence.** A family of two elements spanning `𝔪` has the minimal length
> `(𝔪).spanFinrank = dim A = 2`, so Tag 00NQ applies to it.

```lean
theorem isWeaklyRegular_of_span_range_eq_maximalIdeal (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) (x : Fin 2 → A)
    (hspan : IsLocalRing.maximalIdeal A = Ideal.span (Set.range x)) :
    RingTheory.Sequence.IsWeaklyRegular A [x 0, x 1]
```

**`IsRegularLocalRing.isRegular_and_isRegularLocalRing_quotient_and_isMaximalCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Basic.lean, line 1038](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/Basic.lean#L1038). The attribute's comment: “Cohen-Macaulayness is the named predicate `Module.IsMaximalCohenMacaulay R R` (Definition 00NF), the equality `depth_𝔪(R) = dim R`; the minimal generating sequence is bound inside the clause that uses it, so the `in particular` is a statement about `R` alone. See the module docstring.”. References: EGA 0 (17.1.3), “CM clause”; SGA 4½ Cycle (2.2.1), “special case”.

> **A minimal set of generators of the maximal ideal of a regular local ring is a regular
> sequence.** Let `(R, 𝔪)` be a regular local ring. Then every list `xs = x₁, …, x_d` generating
> `𝔪` of the minimal length `d = (𝔪).spanFinrank` is a regular sequence on `R`, and each initial
> quotient `R/(x₁, …, x_c)` is a regular local ring of dimension `d - c`; in particular `R` is
> Cohen-Macaulay, that is, maximal Cohen-Macaulay over itself.

```lean
public theorem isRegular_and_isRegularLocalRing_quotient_and_isMaximalCohenMacaulay
    (R : Type*) [CommRing R] [IsRegularLocalRing R] :
    (∀ xs : List R, Ideal.ofList xs = maximalIdeal R →
        xs.length = (maximalIdeal R).spanFinrank →
        RingTheory.Sequence.IsRegular R xs ∧
          ∀ c ≤ xs.length, IsRegularLocalRing (R ⧸ Ideal.ofList (xs.take c)) ∧
            ringKrullDim (R ⧸ Ideal.ofList (xs.take c)) + c = ringKrullDim R) ∧
      Module.IsMaximalCohenMacaulay R R
```

## Tag 00NR, a lemma

[Tag 00NR](https://stacks.math.columbia.edu/tag/00NR) in the Stacks Project.

**`IsRegularLocalRing.exists_ofList_eq_maximalIdeal_length_eq_spanFinrank_and_ofList_take_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Basic.lean, line 1403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/Basic.lean#L1403). The attribute's comment: “A minimal set of generators of `𝔪` is a list generating it whose length is `(𝔪).spanFinrank`, and `(x₁, …, x_c)` is the ideal generated by the length-`c` prefix of that list, as in Tag 00NQ. The source's existentially bound `c` is pinned by the dimension equation `dim (R ⧸ I) + c = dim R` proved along with it. See the module docstring.”.

> **An ideal of a regular local ring with regular quotient is generated by part of a minimal
> set of generators of the maximal ideal.** Let `(R, 𝔪)` be a regular local ring and let `I` be an
> ideal of `R` such that `R ⧸ I` is a regular local ring as well. Then there is a list
> `xs = x₁, …, x_d` generating `𝔪` of the minimal length `d = (𝔪).spanFinrank` and a `c ≤ d` with
> `I = (x₁, …, x_c)`; moreover `dim (R ⧸ I) + c = dim R`, i.e. `c = dim R - dim (R ⧸ I)`.

```lean
public theorem exists_ofList_eq_maximalIdeal_length_eq_spanFinrank_and_ofList_take_eq
    {R : Type*} [CommRing R] [IsRegularLocalRing R] (I : Ideal R)
    (hI : IsRegularLocalRing (R ⧸ I)) :
    ∃ xs : List R, Ideal.ofList xs = maximalIdeal R ∧
      xs.length = (maximalIdeal R).spanFinrank ∧
      ∃ c ≤ xs.length, Ideal.ofList (xs.take c) = I ∧
        ringKrullDim (R ⧸ I) + c = ringKrullDim R
```

## Tag 00NS, a lemma

[Tag 00NS](https://stacks.math.columbia.edu/tag/00NS) in the Stacks Project.

**`free_mod_x`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/MaximalCohenMacaulay.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/MaximalCohenMacaulay.lean#L67). References: EGA 0 (10.1.2), “special case”; EGA 0 (10.2.2), “(x), special case”; SGA 1 IV (4.1), “(b), special case”.

> **Stacks Tag 00NS.** Let `R` be a Noetherian local ring with maximal ideal
> `m`, and let `x ∈ m`. Let `M` be a finite `R`-module on which `x` is a
> nonzerodivisor and such that `M / xM` is free over `R / xR`. Then `M` is free
> over `R`.

```lean
theorem free_mod_x
    (R : Type*) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (x : R) (hx : x ∈ maximalIdeal R)
    (hnzd : IsSMulRegular M x)
    (hfree : Module.Free (R ⧸ Ideal.span {x})
      (M ⧸ (Ideal.span {x} • (⊤ : Submodule R M)))) :
    Module.Free R M
```

## Tag 00NT, a lemma

[Tag 00NT](https://stacks.math.columbia.edu/tag/00NT) in the Stacks Project.

**`regular_mcm_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/MaximalCohenMacaulay.lean, line 2010](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/MaximalCohenMacaulay.lean#L2010). References: EGA 0 (17.3.5), “(i), sufficiency”; EGA IV (6.1.5), “special case”.

> Stacks Tag 00NT (Lemma 10.106.6): over a regular local ring, any nonzero
> finitely generated maximal Cohen-Macaulay module is free.

```lean
theorem regular_mcm_free
    (R : Type*) [CommRing R] [IsRegularLocalRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] [Nontrivial M]
    (hM : IsMaxCM R M) : Module.Free R M
```

## Tag 00NU, a lemma

[Tag 00NU](https://stacks.math.columbia.edu/tag/00NU) in the Stacks Project.

**`isRegularLocalRing_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Criteria.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/Criteria.lean#L145). The attribute's comment: “regular sequence”. References: EGA IV (19.1.2), “sufficiency direction”; EGA 0 (17.1.1), “more general”; EGA 0 (17.1.7), “b⇒regularity of A”; EGA IV (16.9.12), “sufficiency”; EGA IV (7.9.7), “partial”; SGA 6 X (7.7), “special case”.

> **Stacks 00NU**, regular sequence case. Let `R` be a Noetherian local ring, and
> `rs` a regular sequence such that `R / (rs)` is a regular local ring. Then `R` is a
> regular local ring.

```lean
theorem isRegularLocalRing_of_isRegular (R : Type*) [CommRing R] [IsLocalRing R] [IsNoetherian R R]
    (rs : List R) (hrs : RingTheory.Sequence.IsRegular R rs)
    (hreg : IsRegularLocalRing (R ⧸ Ideal.ofList rs)) :
    IsRegularLocalRing R
```

**`isRegularLocalRing_of_nonZeroDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Criteria.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/Criteria.lean#L199). The attribute's comment: “single element”. References: EGA IV (19.1.2), “principal J, sufficiency”; EGA 0 (17.1.1), “(d) ⇒ (c)”; EGA 0 (17.1.7), “r=1: b⇒regularity of A”; EGA 0 (17.1.8), “a ⇒ b”; EGA IV (16.9.12), “special case”; EGA IV (7.9.7), “partial”; SGA 6 X (7.7), “special case”.

> **Stacks 00NU**, single nonzerodivisor case. Let `R` be a Noetherian local ring,
> and `x` a nonzerodivisor such that `R / xR` is a regular local ring. Then `R` is a
> regular local ring.
>
> This is the special case `rs = [x]` of `isRegularLocalRing_of_isRegular`.

```lean
theorem isRegularLocalRing_of_nonZeroDivisor (R : Type*) [CommRing R] [IsLocalRing R]
    [IsNoetherian R R]
    (x : R) (hx : x ∈ nonZeroDivisors R)
    (hreg : IsRegularLocalRing (R ⧸ Ideal.span {x})) :
    IsRegularLocalRing R
```

## Tag 07DX, a lemma

[Tag 07DX](https://stacks.math.columbia.edu/tag/07DX) in the Stacks Project.

**`CommRingCat.isRegularLocalRing_pt_of_forall_isRegularLocalRing_of_forall_isLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/Colimit.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/Colimit.lean#L439). The attribute's comment: “The directed system is a functor on a nonempty `u`-small directed preorder together with an arbitrary colimit cocone, as in 0AS7; locality of a transition map is `IsLocalHom` of the underlying ring homomorphism; `IsRegularLocalRing` of the colimit includes the assertion that it is local. See the module docstring.”.

> Let `F : J ⥤ CommRingCat` be a directed system `(R i, φ i i')` of commutative rings over a
> nonempty, `u`-small directed preorder `J`, and let `c` be a colimit cocone on `F`, so that `c.pt`
> is `colim_i R i`. If every `R i` is a regular local ring, every transition map is a local ring map,
> and the colimit is Noetherian, then the colimit is a regular local ring — in particular it is
> local, its maximal ideal being the colimit of the maximal ideals of the `R i`.

```lean
public theorem isRegularLocalRing_pt_of_forall_isRegularLocalRing_of_forall_isLocalHom
    {J : Type w} [Preorder J] [IsDirectedOrder J] [Nonempty J] [Small.{u} J]
    {F : J ⥤ CommRingCat.{u}}
    (hreg : ∀ j : J, IsRegularLocalRing (F.obj j))
    (hloc : ∀ ⦃i j : J⦄ (u : i ⟶ j), IsLocalHom (F.map u).hom)
    {c : Cocone F} (hc : IsColimit c) [IsNoetherianRing c.pt] :
    IsRegularLocalRing c.pt
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.106, Tag 00NN](https://stacks.math.columbia.edu/tag/00NN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
