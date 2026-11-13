---
declaration: section
origin: cited
lean: CommAlgCat.quasiIso_midCotangentComplexMap, CommAlgCat.isIso_Q_map_midCotangentComplexMap, CommAlgCat.midCotangentComplexDerivedIso, CommAlgCat.midBaseChangeOverDifferentialsIso, CommAlgCat.midCotangentComplexHomologyIso, CommAlgCat.isZero_cotangentComplex_of_derivedTensor_self, CommAlgCat.isZero_cotangentComplexDerived_of_torIndependent_unconditional, CommAlgCat.isZero_cotangentComplexDerived_of_flat_of_bijective
statement: formalized
proof: formalized
---

# 92.8 Localization and étale ring maps

Section 92.8 of the Stacks Project, [Tag 08QY](https://stacks.math.columbia.edu/tag/08QY). 7 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08QZ, a lemma

[Tag 08QZ](https://stacks.math.columbia.edu/tag/08QZ) in the Stacks Project.

**`CommAlgCat.quasiIso_midCotangentComplexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDerived.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDerived.lean#L221). The attribute's comment: “on the cotangent complexes: under the tag's own hypothesis B = B ⊗\_A^𝐋 A' -- Tor independence of A' and B over A, and bijectivity of A' ⊗\_A B → B -- the canonical map L\_\{B/A} ⟶ L\_\{B/A'} of Tag 08PN is a quasi-isomorphism”.

> **Stacks 08QZ.** Let `A → A' → B` be ring maps such that `B = B ⊗_A^𝐋 A'`, which is to say
> that `Tor_i^A(A', B)` vanishes for `i > 0` and the canonical map `A' ⊗_A B → B`,
> `a' ⊗ x ↦ a' · x`, is bijective. Then the canonical map `L_{B/A} ⟶ L_{B/A'}` of Tag 08PN,
> `CommAlgCat.midCotangentComplexMap`, is a quasi-isomorphism.
>
> This is the special case `B' = B` of Stacks 08QQ,
> `CommAlgCat.quasiIso_cotangentExtendScalarsMooreMap`: the square of the tower has the identity of
> `B` for its vertical map, so `B ⊗_A^𝐋 A' = B'` is the hypothesis of the tag, and the base-change
> map `L_{B/A} ⊗_B B' ⟶ L_{B'/A'}` of 08QQ is, under
> `CommAlgCat.midCotangentMooreMap_eq`, the functoriality map `L_{B/A} ⟶ L_{B/A'}`. Remark 08QI,
> which 08QQ carried as a hypothesis, is `CommAlgCat.cotangentComputedByEveryResolution`, so
> nothing beyond the tag's own hypothesis is assumed.

```lean
theorem quasiIso_midCotangentComplexMap
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hφ : Function.Bijective
      (baseChangeUnit (B' := midAlgebra A' B) (AlgHom.id A (B : Type u)))) :
    QuasiIso (midCotangentComplexMap A' B)
```

**`CommAlgCat.isIso_Q_map_midCotangentComplexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDerived.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDerived.lean#L241). The attribute's comment: “the lemma as the invertibility in D(B) of the canonical map of Tag 08PN: under the tag's own hypothesis B = B ⊗\_A^𝐋 A', the image of L\_\{B/A} ⟶ L\_\{B/A'} under the localization D(B) is invertible”.

> **Stacks 08QZ in the derived category.** Under the tag's hypothesis `B = B ⊗_A^𝐋 A'` the
> canonical map `L_{B/A} ⟶ L_{B/A'}` of Tag 08PN becomes an isomorphism in `D(B)`.

```lean
theorem isIso_Q_map_midCotangentComplexMap
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hφ : Function.Bijective
      (baseChangeUnit (B' := midAlgebra A' B) (AlgHom.id A (B : Type u)))) :
    IsIso (DerivedCategory.Q.map (midCotangentComplexMap A' B))
```

**`CommAlgCat.midCotangentComplexDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDerived.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDerived.lean#L262).

> **Stacks 08QZ: `L_{B/A} = L_{B/A'}` in `D(B)`.** Let `A → A' → B` be ring maps such that
> `B = B ⊗_A^𝐋 A'` — that is, `Tor_i^A(A', B) = 0` for `i > 0` and `A' ⊗_A B → B` is bijective.
> Then the cotangent complexes of `B` over `A` and over `A'` are isomorphic in `D(B)`, by the
> canonical map `CommAlgCat.midCotangentComplexMap` of Tag 08PN.
>
> This is the conclusion the source states. The degreewise form,
> `CommAlgCat.midCotangentComplexHomologyIso`, is a separate statement proved directly from the two
> resolutions; an isomorphism of cohomology in each degree does not by itself produce an
> isomorphism in `D(B)`, and the comparison here is the canonical one.
>
> This is the whole of the tag: the hypothesis is the source's, written out, and the conclusion is
> the source's, an isomorphism in `D(B)` along the canonical map.

```lean
def midCotangentComplexDerivedIso
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hφ : Function.Bijective
      (baseChangeUnit (B' := midAlgebra A' B) (AlgHom.id A (B : Type u)))) :
    DerivedCategory.Q.obj (cotangentComplex.{u, u} A B) ≅
      DerivedCategory.Q.obj (cotangentComplex.{u, u} A' (midAlgebra A' B))
```

**`CommAlgCat.midBaseChangeOverDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDifferentials.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDifferentials.lean#L309). The attribute's comment: “the step the proof turns on: the sheaf (P → B) ↦ Ω\_\{P/A} ⊗\_P B on C\_\{B/A} is the pullback along u : (P → B) ↦ (A' ⊗\_A P → B) of the sheaf (Q → B) ↦ Ω\_\{Q/A'} ⊗\_Q B on C\_\{B/A'}, stated on all augmented algebras rather than only the polynomial ones. The passage from here to L\_\{B/A} = L\_\{B/A'} is `CommAlgCat.midCotangentComplexHomologyIso`”.

> **`i^*Ω_{𝒪/A} = u^{-1}(i^*Ω_{𝒪/A'})`, the step of Stacks 08QZ that the proof turns on.**
> For a tower of ring maps `A → A' → B`, the functor sending an `A`-algebra `P` augmented to `B` to
> `Ω_{P/A} ⊗_P B` is the composite of the base-change functor `(P → B) ↦ (A' ⊗_A P → B)` of
> Stacks 08QN with the functor sending an `A'`-algebra `Q` augmented to `B` to `Ω_{Q/A'} ⊗_Q B`:
> ```
> Ω_{P/A} ⊗_P B = Ω_{(A' ⊗_A P)/A'} ⊗_{A' ⊗_A P} B ,
> ```
> naturally in `(P → B)`. Each component is Stacks 00RV base changed along the augmentation,
> `Stacks.KaehlerDifferential.augmentationBaseChangeEquiv`, and naturality holds because both
> composites send the pure differential `1 ⊗ d p` to `1 ⊗ d(1 ⊗ p)` — the pure differentials
> generate, by `CommAlgCat.overDifferentials_hom_ext`.
>
> The source's `C_{B/A}` is the full subcategory of the polynomial algebras, so the comparison of
> abelian sheaves it asks for is the restriction of this isomorphism along that inclusion; nothing
> below uses that `P` is a polynomial algebra.

```lean
def midBaseChangeOverDifferentialsIso :
    overDifferentialsFunctor (B := B) ≅
      midBaseChangeOver A' B ⋙ overDifferentialsFunctor (A := A') (B := midAlgebra A' B)
```

**`CommAlgCat.midCotangentComplexHomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDifferentials.lean, line 534](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDifferentials.lean#L534). The attribute's comment: “the cohomology of L\_\{B/A} and of L\_\{B/A'} agrees in every degree, as B-modules, under the tag's own hypothesis B = B ⊗\_A^𝐋 A' — Tor independence of A' and B over A, and bijectivity of A' ⊗\_A B → B. Degreewise rather than in D(B), because the module half of Tag 08PS, which is what compares the two resolutions of B over A', is itself a statement about (Lπ\_!)\_n and H\_n. The tag's own conclusion, an isomorphism in D(B) along the canonical map of Tag 08PN, is `CommAlgCat.midCotangentComplexDerivedIso`”.

> **Stacks 08QZ: `L_{B/A} = L_{B/A'}`.** Let `A → A' → B` be ring maps such that
> `B = B ⊗_A^𝐋 A'`, which is to say that `Tor_i^A(A', B)` vanishes for `i > 0` and the canonical
> map `A' ⊗_A B → B`, `a' ⊗ x ↦ a' · x`, is bijective. Then the cotangent complexes of `B` over
> `A` and of `B` over `A'` have the same cohomology in every degree, as `B`-modules.
>
> The proof is the source's. The cohomology of `L_{B/A}` in degree `-n` is the degree `n` homology
> of the complex of `Ω_{P_•/A} ⊗_{P_•} B` for the standard resolution `P_•` of `B` over `A`
> (Tag 08PN, `CommAlgCat.cotangentComplexHomologyMooreIso`); that simplicial module is
> `Ω_{(A' ⊗_A P_•)/A'} ⊗_{A' ⊗_A P_•} B` by the comparison of
> `CommAlgCat.midBaseChangeOverDifferentialsIso`, which is the step of Stacks 08QZ that the
> source's proof turns on; and `A' ⊗_A P_•` and the standard resolution of `B` over `A'` are two
> resolutions of `B` over `A'`, so Tag 08PT computes the same `L_nπ_!(Ω_{𝒪/A'} ⊗_𝒪 B̲)` from both
> (`CommAlgCat.resolutionModuleLeftDerivedCotangentHomologyIso`).
>
> The hypothesis enters exactly once, and only through the first half of the proof of Stacks 08QP:
> `CommAlgCat.isResolution_augmentationBaseChange` turns it into the statement that
> `A' ⊗_A P_• ⟶ B` is a resolution of `B` over `A'`, which is what Tag 08PT needs of the
> base-changed resolution. Both halves are used there: Tor independence makes
> `s(P_•) ⊗_A A'` compute `B ⊗_A^𝐋 A'`, and bijectivity of `A' ⊗_A B → B` identifies its
> degree-zero homology with `B`.
>
> The conclusion here is degreewise, not an isomorphism in `D(B)`: the module half of Tag 08PS,
> `CommAlgCat.smallResolutionModuleLeftDerivedLowerShriekNatIso`, identifies the degree `n`
> functor `(Lπ_!)_n` with the degree `n` homology of the Moore complex, so the two resolutions of
> `B` over `A'` are compared one degree at a time. The source's isomorphism in `D(B)` is
> `CommAlgCat.midCotangentComplexDerivedIso` of
> `StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChangeDerived.lean`, which carries the same
> hypotheses and is not deduced from this statement — degreewise isomorphisms do not give one in
> `D(B)`.

```lean
def midCotangentComplexHomologyIso
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hφ : Function.Bijective
      (baseChangeUnit (B' := midAlgebra A' B) (AlgHom.id A (B : Type u))))
    (n : ℕ) :
    (cotangentComplex.{u, u} A B).homology (-(n : ℤ)) ≅
      (cotangentComplex.{u, u} A' (midAlgebra A' B)).homology (-(n : ℤ))
```

## Tag 08R0, a lemma

[Tag 08R0](https://stacks.math.columbia.edu/tag/08R0) in the Stacks Project.

**`CommAlgCat.isZero_cotangentComplex_of_derivedTensor_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SelfDerivedTensorVanishing.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SelfDerivedTensorVanishing.lean#L87).

> **Stacks Project, Tag 08R0.** Let `A → B` be a ring map such that `B = B ⊗_A^𝐋 B`, that is,
> `Tor_i^A(B, B) = 0` for `i > 0` and the multiplication map `B ⊗_A B → B` is bijective. Then
> `L_{B/A} = 0` in `D(B)`.
>
> By [Stacks, Tag 08QZ] for the tower `A → B → B` (`CommAlgCat.midCotangentComplexHomologyIso`),
> the cohomology of `L_{B/A}` in each degree `≤ 0` is that of `L_{B/B}`, which vanishes
> (`CommAlgCat.isZero_cotangentComplex_self`); in positive degrees `L_{B/A}` is itself zero.

```lean
theorem isZero_cotangentComplex_of_derivedTensor_self (A : Type u) [CommRing A]
    (B : CommAlgCat.{u} A)
    (hTor : RingTheory.TorIndependence.TorIndependent A B B)
    (hmul : Function.Bijective
      (Algebra.TensorProduct.lmul' (S := (B : Type u)) A)) :
    Limits.IsZero (DerivedCategory.Q.obj (cotangentComplex.{u, u} A B))
```

## Tag 08R1, a lemma

[Tag 08R1](https://stacks.math.columbia.edu/tag/08R1) in the Stacks Project.

**`CommAlgCat.isZero_cotangentComplexDerived_of_torIndependent_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/EtaleVanishingUnconditional.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/EtaleVanishingUnconditional.lean#L74). The attribute's comment: “the lemma in full: `Tor^A_i(B, B) = 0` for `i > 0` (`hTor`) and `L_{B/(B ⊗_A B)} = 0` (`hCot`) give `L_{B/A} = 0` in `D(B)`. The distinguished triangle of the tower `B → B ⊗_A B → B` is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`, which holds for arbitrary ring maps and so covers the surjective multiplication `B ⊗_A B → B`. `hTor` is consumed by Stacks 08QQ (`CommAlgCat.derivedCotangentComplexBaseChangeIso`) in identifying the first vertex of the triangle with `L_{B/A}`, and `hCot` is the vanishing of its third vertex. The `B ⊗_A B`-algebra structure on `B` is the multiplication map, `CommAlgCat.diagonalAlgebra`”.

> **[Stacks, Tag 08R1].** Let `A → B` be a ring map such that `Tor^A_i(B, B) = 0` for `i > 0`
> and such that `L_{B/(B ⊗_A B)} = 0`. Then `L_{B/A} = 0` in `D(B)`.
>
> This is `CommAlgCat.isZero_cotangentComplexDerived_of_torIndependent` at the distinguished
> triangle of the tower `B → B ⊗_A B → B` that Proposition 08QX,
> `CommAlgCat.productFundamentalTriangle_distinguished`, provides.

```lean
theorem isZero_cotangentComplexDerived_of_torIndependent_unconditional
    (hTor : RingTheory.TorIndependence.TorIndependent A B (B : Type u))
    (hCot : IsZero (fundamentalVertex₃.{u, u} (B ⊗[A] B) B)) :
    IsZero (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B))
```

## Tag 08R2, a lemma

[Tag 08R2](https://stacks.math.columbia.edu/tag/08R2) in the Stacks Project.

**`CommAlgCat.isZero_cotangentComplexDerived_of_flat_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/EtaleVanishing.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/EtaleVanishing.lean#L169). The attribute's comment: “item (2) of the lemma, a flat epimorphism of rings: `Module.Flat A B` together with bijectivity of `b ↦ b ⊗ 1 : B → B ⊗_A B`, which is item (3) of `CommRingCat.epi_tfae` (Stacks 04VN, proved in this library) and is therefore exactly the source's epimorphism condition. NOTHING is carried: no instance of Proposition 08QX is assumed. Both hypotheses are load-bearing — flatness gives the Tor independence that `CommAlgCat.cotangentComplexDerived_iso_fundamentalVertex₁_diagonal` consumes, and the epimorphism condition is what makes `L_{(B ⊗_A B)/B}` vanish”.

> **[Stacks, Tag 08R2] item (2).** Let `A → B` be a flat epimorphism of rings. Then
> `L_{B/A} = 0` in `D(B)`.
>
> The epimorphism condition is bijectivity of `b ↦ b ⊗ 1 : B → B ⊗_A B`, which is item (3) of
> `CommRingCat.epi_tfae`; see the module docstring. Flatness gives `Tor^A_i(B, B) = 0` for `i > 0`,
> so `CommAlgCat.cotangentComplexDerived_iso_fundamentalVertex₁_diagonal` identifies `L_{B/A}` with
> `L_{(B ⊗_A B)/B} ⊗^𝐋_{(B ⊗_A B)} B`; and `L_{(B ⊗_A B)/B}` vanishes because the structure map
> `B → B ⊗_A B` is an isomorphism. No cotangent triangle is used.

```lean
theorem isZero_cotangentComplexDerived_of_flat_of_bijective [Module.Flat A B]
    (h : Function.Bijective (algebraMap B (B ⊗[A] B))) :
    IsZero (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B))
```

**`CommAlgCat.isZero_cotangentComplexDerived_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/EtaleVanishingFurtherCases.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/EtaleVanishingFurtherCases.lean#L99). The attribute's comment: “item (3) of the lemma, `B = S⁻¹A` for a multiplicative subset `S ⊂ A`, read as `IsLocalization S B`. NOTHING is carried: the source derives it from item (2), and so does this proof, through `CommAlgCat.isZero_cotangentComplexDerived_localization`, a localization being flat and an epimorphism. The localization hypothesis is load-bearing, being the only source of both”.

> **[Stacks, Tag 08R2] item (3).** Let `S ⊂ A` be a multiplicative subset and let
> `B = S⁻¹A`. Then `L_{B/A} = 0` in `D(B)`.
>
> A localization is flat and an epimorphism, so this is item (2),
> `CommAlgCat.isZero_cotangentComplexDerived_of_flat_of_bijective`, through
> `CommAlgCat.isZero_cotangentComplexDerived_localization`.

```lean
theorem isZero_cotangentComplexDerived_of_isLocalization (S : Submonoid A) [IsLocalization S B] :
    IsZero (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B))
```

**`CommAlgCat.isZero_cotangentComplexDerived_of_unramified_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/EtaleVanishingFurtherCases.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/EtaleVanishingFurtherCases.lean#L116). The attribute's comment: “item (4) of the lemma, `A → B` unramified and flat: `Algebra.Unramified A B` (formally unramified and of finite type, which is Stacks 00UT by Stacks 00UU) together with `Module.Flat A B`. NOTHING is carried: the source derives it from item (1), and so does this proof — flatness and unramifiedness make the multiplication `B ⊗_A B → B` a localization at an idempotent, hence flat (`Algebra.WeaklyEtale.of_formallyUnramified_of_flat`), and item (1) is `CommAlgCat.isZero_cotangentComplexDerived_of_weaklyEtale_unconditional`, whose triangle is Proposition 08QX. Both hypotheses are load-bearing”.

> **[Stacks, Tag 08R2] item (4).** Let `A → B` be unramified and flat. Then `L_{B/A} = 0` in
> `D(B)`.
>
> Unramified is Mathlib's `Algebra.Unramified`, formally unramified and of finite type, which is
> the source's definition (Stacks 00UT, through 00UU). A flat unramified algebra is weakly étale,
> `Algebra.WeaklyEtale.of_formallyUnramified_of_flat`, so this is item (1).

```lean
theorem isZero_cotangentComplexDerived_of_unramified_of_flat [Algebra.Unramified A B]
    [Module.Flat A B] :
    IsZero (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B))
```

**`CommAlgCat.isZero_cotangentComplexDerived_of_isHenselization_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/EtaleVanishingFurtherCases.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/EtaleVanishingFurtherCases.lean#L140). The attribute's comment: “items (7) and (8) of the lemma, at once, for an ARBITRARY ring `A`: `B` a henselization (`L = κ(𝔭)`, item (7)) or a strict henselization (`L = κ(𝔭)^sep`, item (8)) of the local ring `A_𝔭 = Localization.AtPrime 𝔭` of `A`, read as `IsLocalRing.IsHenselization` (Stacks 04GQ) with the `A`-algebra structure on `B` the composite `A → A_𝔭 → B`. NOTHING is carried: the triangle of `A → A_𝔭 → B` is Proposition 08QX, `CommAlgCat.exists_distTriang_fundamentalVertex`; its first vertex vanishes by item (3) and its third by `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived_unconditional`, which is the source's route through items (5) and (6) over the local ring”.

> **[Stacks, Tag 08R2] items (7) and (8).** Let `A` be a ring, `𝔭 ⊂ A` a prime, and let
> `A_𝔭 → B` be a henselization of the local ring `A_𝔭` of `A` with residue field a prescribed
> extension `κ(𝔭) ⊆ L`. Then `L_{B/A} = 0` in `D(B)`.
>
> At `L = κ(𝔭)` this is item (7), a henselization of a local ring of `A`, and at `L = κ(𝔭)^sep`
> it is item (8), a strict henselization. The fundamental triangle of `A → A_𝔭 → B`
> (Proposition 08QX) has first vertex `L_{A_𝔭/A} ⊗^𝐋 B = 0` by item (3) and third vertex
> `L_{B/A_𝔭} = 0` by the local case
> `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived_unconditional`, so its middle vertex
> `L_{B/A}` vanishes.

```lean
theorem isZero_cotangentComplexDerived_of_isHenselization_atPrime (p : Ideal A) [p.IsPrime]
    (L : Type v) [Field L] [Algebra (IsLocalRing.ResidueField (Localization.AtPrime p)) L]
    [IsLocalRing B] [Algebra (Localization.AtPrime p) B]
    [IsScalarTower A (Localization.AtPrime p) B]
    [IsLocalRing.IsHenselization (Localization.AtPrime p) L B] :
    IsZero (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B))
```

**`CommAlgCat.isZero_cotangentComplexDerived_of_weaklyEtale_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/EtaleVanishingUnconditional.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/EtaleVanishingUnconditional.lean#L93). The attribute's comment: “item (1) of the lemma, `A → B` weakly étale — `Module.Flat A B` together with flatness of the multiplication map `B ⊗_A B → B`, which is Mathlib's `Algebra.WeaklyEtale`. NOTHING is carried: the distinguished triangle of the tower `B → B ⊗_A B → B` is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. Weak étaleness is NOT dead: `Module.Flat A B` supplies the Tor-independence hypothesis of Stacks 08R1, and flatness of the multiplication map supplies the vanishing of `L_{B/(B ⊗_A B)}` through item (2)”.

> **[Stacks, Tag 08R2] item (1).** Let `A → B` be weakly étale: `A → B` flat and the
> multiplication map `B ⊗_A B → B` flat. Then `L_{B/A} = 0` in `D(B)`.
>
> This is `CommAlgCat.isZero_cotangentComplexDerived_of_weaklyEtale` at the distinguished triangle
> of the tower `B → B ⊗_A B → B` that Proposition 08QX provides.

```lean
theorem isZero_cotangentComplexDerived_of_weaklyEtale_unconditional [Algebra.WeaklyEtale A B] :
    IsZero (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B))
```

**`CommAlgCat.isZero_cotangentComplexDerived_of_etale_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/EtaleVanishingUnconditional.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/EtaleVanishingUnconditional.lean#L105). The attribute's comment: “item (5) of the lemma, `A → B` étale, obtained as the instance of item (1) along Mathlib's instance `Algebra.Etale → Algebra.WeaklyEtale`. NOTHING is carried, as in item (1). Étaleness is load-bearing, being the only source of the two flatness facts item (1) consumes”.

> **[Stacks, Tag 08R2] item (5).** If `A → B` is étale then `L_{B/A} = 0` in `D(B)`.
>
> An étale algebra is weakly étale, so this is the instance of item (1).

```lean
theorem isZero_cotangentComplexDerived_of_etale_unconditional [Algebra.Etale A B] :
    IsZero (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B))
```

**`CommAlgCat.cotangentComplex_isZero_of_filtered_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/FilteredColimitVanishing.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/FilteredColimitVanishing.lean#L185). The attribute's comment: “item (6) of the lemma, `A → B` a filtered colimit of ring maps for which the cotangent complex vanishes: a filtered system `f : A ⟶ B` of ring maps in `CommRingCat` with `L_{B_i/A_i} = 0` at every stage gives `L_{colim B/colim A} = 0`. NOTHING is carried; the source's route through Stacks 08S9 is followed (the cotangent complexes form a colimit cocone, `CommAlgCat.isColimit_cotangentComplexAbCocone`), after replacing the filtered index category by a cofinal directed order”.

> **Stacks Project, Tag 08R2, filtered colimits.** If every map of a filtered system of ring
> maps has vanishing relative cotangent complex, so has the map induced on the colimits.

```lean
theorem cotangentComplex_isZero_of_filtered_colimit
    {J : Type u} [SmallCategory J] [IsFiltered J]
    (A B : J ⥤ CommRingCat.{u}) (f : A ⟶ B)
    (h : ∀ i : J,
      letI : Algebra (A.obj i) (B.obj i) := (f.app i).hom.toAlgebra
      IsZero (DerivedCategory.Q.obj
        (cotangentComplex (A.obj i) (CommAlgCat.of (A.obj i) (B.obj i))))) :
    letI : Algebra (colimit A : CommRingCat.{u}) (colimit B : CommRingCat.{u}) :=
      (colim.map f).hom.toAlgebra
    IsZero (DerivedCategory.Q.obj
      (cotangentComplex (colimit A : CommRingCat.{u})
        (CommAlgCat.of (colimit A : CommRingCat.{u})
          (colimit B : CommRingCat.{u}))))
```

**`IsLocalRing.IsHenselization.isZero_cotangentComplexDerived_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/HenselizationUnconditional.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/HenselizationUnconditional.lean#L84). The attribute's comment: “items (7) and (8) of the lemma, at once: `L_{R^h/R} = 0` and `L_{R^{sh}/R} = 0` for `R → Rh` a henselization of the local ring `R` with residue field the prescribed extension `κ ⊆ L` (`IsLocalRing.IsHenselization`, Stacks 04GQ), item (7) being the case `L = κ` and item (8) the case `L = κ^sep`. NOTHING is carried: item (5) needs the distinguished triangle of the diagonal tower `P → P ⊗_R P → P` of every étale stage, and that is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`, through `CommAlgCat.hasEtaleDiagonalTriangle`, so it applies at every étale stage of the colimit presentation even though the index category is produced inside the proof. The source's own route is followed: items (5) and (6), the latter being `CommAlgCat.cotangentComplex_isZero_of_filtered_colimit`. The henselization hypothesis is load-bearing through `IsLocalRing.IsHenselization.ind_etale`, which supplies the presentation of `Rh` as a filtered colimit of étale `R`-algebras”.

> **[Stacks, Tag 08R2] items (7) and (8).** Let `(R, 𝔪, κ)` be a local ring and let `R → Rh` be
> a henselization of `R` with residue field a prescribed extension `κ ⊆ L` of its residue field.
> Then `L_{Rh/R} = 0` in `D(Rh)`.
>
> At `L = κ` this is item (7), the henselization `R → R^h`, and at `L = κ^sep` a separable
> algebraic closure it is item (8), a strict henselization `R → R^{sh}`. This is
> `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived` with its family of diagonal
> triangles supplied by `CommAlgCat.hasEtaleDiagonalTriangle`.

```lean
theorem isZero_cotangentComplexDerived_unconditional {R : Type u} [CommRing R] [IsLocalRing R]
    (L : Type v) [Field L] [Algebra (ResidueField R) L] {Rh : Type u} [CommRing Rh]
    [IsLocalRing Rh] [Algebra R Rh] [IsHenselization R L Rh] :
    IsZero (cotangentComplexDerived.{u, u} R (CommAlgCat.of R Rh))
```

## Tag 08R3, a lemma

[Tag 08R3](https://stacks.math.columbia.edu/tag/08R3) in the Stacks Project.

**`CommAlgCat.isIso_fundamentalMor₁_of_isZero_fundamentalVertex₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/ProductDescent.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Triangle/ProductDescent.lean#L393). The attribute's comment: “the lemma for arbitrary ring maps `A → B → C` with `A`, `B`, `C` in one universe: if `L_{C/B} = 0` in `D(C)` (`IsZero (CommAlgCat.fundamentalVertex₃ B C)`, the cotangent complex of `B → C`), then the first morphism `CommAlgCat.fundamentalMor₁ : L_{B/A} ⊗^𝐋_B C ⟶ L_{C/A}` of the fundamental triangle is an isomorphism, i.e. `L_{C/A} = L_{B/A} ⊗^𝐋_B C`. Proved from the distinguished triangle of Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`”.

> **Stacks Project, Tag 08R3.** Let `A → B → C` be ring maps such that `L_{C/B} = 0`. Then
> `L_{C/A} = L_{B/A} ⊗^𝐋_B C`: precisely, the first morphism `CommAlgCat.fundamentalMor₁` of the
> fundamental triangle, `L_{B/A} ⊗^𝐋_B C ⟶ L_{C/A}` in `D(C)`, is an isomorphism.
>
> Here `L_{C/B} = 0` is `IsZero (CommAlgCat.fundamentalVertex₃ B C)`, the vanishing in `D(C)` of the
> cotangent complex of `B → C`. The three rings `A`, `B`, `C` are taken in one universe `Type u`,
> as for the triangle of [Stacks, Tag 08QX].
>
> The proof is the source's: the fundamental triangle
> `CommAlgCat.productFundamentalTriangle_distinguished` (Proposition 08QX) is distinguished, and a
> distinguished triangle with vanishing third vertex has invertible first morphism
> (`CommAlgCat.isIso_of_isZero_fundamentalVertex₃`).

```lean
theorem isIso_fundamentalMor₁_of_isZero_fundamentalVertex₃
    (h : IsZero (fundamentalVertex₃.{u, u, u + 1} B C)) :
    IsIso (fundamentalMor₁.{u} A B C)
```

**`CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_of_isZero_fundamentalVertex₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Triangle/ProductDescent.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Triangle/ProductDescent.lean#L411). The attribute's comment: “the lemma for arbitrary ring maps `A → B → C` with `A`, `B`, `C` in one universe: if `L_{C/B} = 0` in `D(C)`, then `L_{C/A} = L_{B/A} ⊗^𝐋_B C`, read as an isomorphism `CommAlgCat.fundamentalVertex₁ A B C ≅ CommAlgCat.fundamentalVertex₂ A C` in `D(C)`. Proved from the distinguished triangle of Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`”.

> **Stacks Project, Tag 08R3**, as an isomorphism. Let `A → B → C` be ring maps such that
> `L_{C/B} = 0`. Then `L_{C/A} = L_{B/A} ⊗^𝐋_B C`, read as an isomorphism
> `L_{B/A} ⊗^𝐋_B C ≅ L_{C/A}` in `D(C)` between the first and second vertices of the fundamental
> triangle. The rings `A`, `B`, `C` are taken in one universe `Type u`. The isomorphism is the first
> morphism of the distinguished triangle of [Stacks, Tag 08QX],
> `CommAlgCat.productFundamentalTriangle_distinguished`; see
> `CommAlgCat.isIso_fundamentalMor₁_of_isZero_fundamentalVertex₃`.

```lean
theorem nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_of_isZero_fundamentalVertex₃
    (h : IsZero (fundamentalVertex₃.{u, u, u + 1} B C)) :
    Nonempty (fundamentalVertex₁.{u, u, u + 1, u + 1} A B C ≅
      fundamentalVertex₂.{u, u, u + 1} A C)
```

## Tag 08SF, a lemma

[Tag 08SF](https://stacks.math.columbia.edu/tag/08SF) in the Stacks Project.

**`CommAlgCat.nonempty_cotangentComplexDerivedBaseChange_iso_localization_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LocalizationUnconditional.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/LocalizationUnconditional.lean#L94). The attribute's comment: “the lemma in full, with NOTHING carried. The distinguished fundamental triangle of the tower `A → B → T⁻¹B` is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. Everything else is proved outright too: `L_{T⁻¹B/B} = 0` is `isZero_cotangentComplexDerived_localization` from Tag 08R2 item (2), and `L_{T⁻¹B/A} ≅ L_{T⁻¹B/S⁻¹A}` is `nonempty_cotangentComplexDerived_iso_localizationBase` from Tag 08QQ at the identity base change, at the localization square. The source's equality is read as an isomorphism in D(T⁻¹B) without naming the arrow, as Tag 08R3 and Tag 08QQ do, no canonical arrow being available to pin. All four rings are in a single universe, which is the generality of Tag 08QQ”.

> **[Stacks, Tag 08SF].** Let `A → B` be a ring map and let `S ⊆ A` and `T ⊆ B` be
> multiplicative subsets such that `S` maps into `T`. Then
>
> `L_{T⁻¹B/S⁻¹A} = L_{B/A} ⊗^𝐋_B T⁻¹B`
>
> in `D(T⁻¹B)`.
>
> This is `CommAlgCat.nonempty_cotangentComplexDerivedBaseChange_iso_localization` applied to the
> distinguished triangle of the tower `A → B → T⁻¹B` from Proposition 08QX,
> `CommAlgCat.exists_distTriang_fundamentalVertex`. Every other input is proved as well:
> `L_{T⁻¹B/B} = 0` is `CommAlgCat.isZero_cotangentComplexDerived_localization`, and
> `L_{T⁻¹B/A} ≅ L_{T⁻¹B/S⁻¹A}` is
> `CommAlgCat.nonempty_cotangentComplexDerived_iso_localizationBase`.

```lean
theorem nonempty_cotangentComplexDerivedBaseChange_iso_localization_unconditional
    (hST : ∀ s ∈ S, algebraMap A B s ∈ T) :
    Nonempty (cotangentComplexDerivedBaseChange.{u, u} A (CommAlgCat.of A B) B' ≅
      cotangentComplexDerived.{u, u} A' (CommAlgCat.of A' B'))
```

**`CommAlgCat.nonempty_extendScalars_cotangentComplex_iso_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LocalizationUnconditional.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/LocalizationUnconditional.lean#L124). The attribute's comment: “the lemma in full, with NOTHING carried, reading the source's `⊗_B T⁻¹B` as the DEGREEWISE extension of scalars along `B → T⁻¹B` — which is the tensor product the source writes, the derived reading being `nonempty_cotangentComplexDerivedBaseChange_iso_localization_unconditional`. The two differ only by `nonempty_derivedExtensionScalars_cotangentComplex_iso`, which identifies the derived base change of `L_{B/A}` with the degreewise one and assumes nothing of `B → T⁻¹B`, `L_{B/A}` being a complex of free `B`-modules vanishing in positive degrees. The source's equality is read as an isomorphism in D(T⁻¹B) without naming the arrow, as Tag 08R3 and Tag 08QQ do, no canonical arrow being available to pin. All four rings are in a single universe, which is the generality of Tag 08QQ”.

> **[Stacks, Tag 08SF], with the base change read degreewise.** Let `A → B` be a ring map and
> let `S ⊆ A` and `T ⊆ B` be multiplicative subsets such that `S` maps into `T`. Then
>
> `L_{T⁻¹B/S⁻¹A} = L_{B/A} ⊗_B T⁻¹B`
>
> in `D(T⁻¹B)`, where the right-hand side is the *degreewise* extension of scalars along
> `B → T⁻¹B` — which is the tensor product the source writes.
>
> This is `CommAlgCat.nonempty_cotangentComplexDerivedBaseChange_iso_localization_unconditional`
> composed with the identification of the derived base change of `L_{B/A}` with the degreewise
> one, `CommAlgCat.nonempty_derivedExtensionScalars_cotangentComplex_iso`. That identification
> needs no hypothesis on `B → T⁻¹B`: `L_{B/A}` is a complex of free `B`-modules vanishing in
> positive degrees, so it already computes its own derived base change.

```lean
theorem nonempty_extendScalars_cotangentComplex_iso_localization
    (hST : ∀ s ∈ S, algebraMap A B s ∈ T) :
    Nonempty (DerivedCategory.Q.obj (cotangentComplex A' (CommAlgCat.of A' B')) ≅
      DerivedCategory.Q.obj ((CochainComplex.extendScalarsLarge.{0, u, u}
        (algebraMap B B')).obj (cotangentComplex A (CommAlgCat.of A B))))
```

## Tag 08UN, a lemma

[Tag 08UN](https://stacks.math.columbia.edu/tag/08UN) in the Stacks Project.

**`CommAlgCat.nonempty_fundamentalVertex₂_iso_fundamentalVertex₃_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Henselization.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Henselization.lean#L319). The attribute's comment: “the FIRST of the lemma's two equalities, `L_{B^h/A^h} = L_{B^h/A}`, and its `resp.` strict variant `L_{B^{sh}/A^{sh}} = L_{B^{sh}/A}` — one statement for both, because the henselization and a strict henselization are the two instances `L = κ` and `L = κ^sep` of `IsLocalRing.IsHenselization` (Stacks 04GQ). It is proved for an ARBITRARY `A^h`-algebra `C` in place of `B^h`, which is a generalization of the lemma and not a weakening of it. TWO carried hypotheses: `hT`, the distinguished triangle of Proposition 08QX for the tower `A → A^h → C`, which is not formalized in this library (see the `No @[stacks 08QX]` section of `StacksFrontier.Cotangent.Triangle.Distinguished`), and `hQX`, the family of instances of Proposition 08QX that items (7) and (8) of Stacks 08R2 consume. The source's input `L_{A^h/A} = 0` is NOT carried: it is proved here, as `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived`, which is what makes the henselization hypothesis on `A^h` load-bearing. The lemma's SECOND equality, `L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h`, is `CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_henselization`”.

> **[Stacks, Tag 08UN], the identification over the henselized source.** Let `A → A^h` be a
> henselization of the local ring `A` and let `C` be an `A^h`-algebra. Then
> `L_{C/A} = L_{C/A^h}` in `D(C)`.
>
> This is the first equality of the lemma, at `C = B^h`: the fundamental triangle of the tower
> `A → A^h → C` has first vertex `L_{A^h/A} ⊗^𝐋_{A^h} C`, which vanishes because `L_{A^h/A} = 0`,
> so its second arrow `L_{C/A} ⟶ L_{C/A^h}` is an isomorphism. Both the henselization `A^h` and a
> strict henselization `A^{sh}` are instances of `IsLocalRing.IsHenselization`, so the statement
> covers the lemma's `resp.` variant as well.

```lean
theorem nonempty_fundamentalVertex₂_iso_fundamentalVertex₃_henselization [IsLocalRing A]
    (L : Type v) [Field L] [Algebra (ResidueField A) L]
    (Ah : Type u) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah] [IsHenselization A L Ah]
    (C : Type u) [CommRing C] [Algebra A C] [Algebra Ah C] [IsScalarTower A Ah C]
    (hQX : HasEtaleDiagonalTriangle.{u} A)
    {α : fundamentalVertex₁.{u, u} A Ah C ⟶ fundamentalVertex₂.{u, u} A C}
    {β : fundamentalVertex₂.{u, u} A C ⟶ fundamentalVertex₃.{u, u} Ah C}
    {γ : fundamentalVertex₃.{u, u} Ah C ⟶ (fundamentalVertex₁.{u, u} A Ah C)⟦(1 : ℤ)⟧}
    (hT : Triangle.mk α β γ ∈ distTriang (DerivedCategory (ModuleCat.{u} C))) :
    Nonempty (fundamentalVertex₂.{u, u} A C ≅ fundamentalVertex₃.{u, u} Ah C)
```

**`CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Henselization.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Henselization.lean#L353). The attribute's comment: “the SECOND of the lemma's two equalities, `L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h`, and its `resp.` strict variant `L_{B^{sh}/A} = L_{B/A} ⊗^𝐋_B B^{sh}` — one statement for both, the henselization and a strict henselization being the two instances `L = κ` and `L = κ^sep` of `IsLocalRing.IsHenselization` (Stacks 04GQ). TWO carried hypotheses: `hT`, the distinguished triangle of Proposition 08QX for the tower `A → B → B^h`, not formalized in this library, and `hQX`, the family of instances of Proposition 08QX that items (7) and (8) of Stacks 08R2 consume. The source's input `L_{B^h/B} = 0` is NOT carried: it is proved here, as `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived`, so the henselization hypothesis on `B^h` is load-bearing. The lemma's FIRST equality, `L_{B^h/A^h} = L_{B^h/A}`, is `CommAlgCat.nonempty_fundamentalVertex₂_iso_fundamentalVertex₃_henselization`. NOTE that the local ring homomorphism `A → B` of the source is not assumed: the conclusion holds for any ring map `A → B` whose target is local, which is a generalization”.

> **[Stacks, Tag 08UN], the derived scalar-extension identification.** Let `A → B` be a ring
> map, let `B → B^h` be a henselization of the local ring `B`, and let `A → B → B^h` be a tower.
> Then `L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h` in `D(B^h)`.
>
> This is the second equality of the lemma: the fundamental triangle of the tower `A → B → B^h`
> has third vertex `L_{B^h/B}`, which vanishes because `B → B^h` is a henselization, so its first
> arrow is an isomorphism. As above, one statement covers the lemma's `resp.` variant.

```lean
theorem nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_henselization
    (B : Type u) [CommRing B] [IsLocalRing B] [Algebra A B] (L : Type v) [Field L]
    [Algebra (ResidueField B) L]
    (Bh : Type u) [CommRing Bh] [IsLocalRing Bh] [Algebra B Bh] [IsHenselization B L Bh]
    [Algebra A Bh] [IsScalarTower A B Bh] (hQX : HasEtaleDiagonalTriangle.{u} B)
    {α : fundamentalVertex₁.{u, u} A B Bh ⟶ fundamentalVertex₂.{u, u} A Bh}
    {β : fundamentalVertex₂.{u, u} A Bh ⟶ fundamentalVertex₃.{u, u} B Bh}
    {γ : fundamentalVertex₃.{u, u} B Bh ⟶ (fundamentalVertex₁.{u, u} A B Bh)⟦(1 : ℤ)⟧}
    (hT : Triangle.mk α β γ ∈ distTriang (DerivedCategory (ModuleCat.{u} Bh))) :
    Nonempty (fundamentalVertex₁.{u, u} A B Bh ≅ fundamentalVertex₂.{u, u} A Bh)
```

**`CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₃_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Henselization.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/Henselization.lean#L386). The attribute's comment: “the lemma's full chain `L_{B^h/A^h} = L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h`, read as the isomorphism `L_{B/A} ⊗^𝐋_B B^h ≅ L_{B^h/A^h}` in `D(B^h)` obtained by composing the two equalities, together with its `resp.` strict variant — one statement for both, the henselization and a strict henselization being the instances `L = κ` and `L = κ^sep` of `IsLocalRing.IsHenselization` (Stacks 04GQ). The induced map `A^h → B^h` is taken as given data (an `A^h`-algebra structure on `B^h` with `IsScalarTower A A^h B^h`) rather than constructed. FOUR carried hypotheses: the two distinguished triangles `hT₁` and `hT₂` of Proposition 08QX, for the towers `A → B → B^h` and `A → A^h → B^h`, Proposition 08QX not being formalized in this library; and `hQXA`, `hQXB`, the families of instances of Proposition 08QX that items (7) and (8) of Stacks 08R2 consume over `A` and over `B`. The source's inputs `L_{A^h/A} = 0` and `L_{B^h/B} = 0` are NOT carried: both are proved, by `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived`, so both henselization hypotheses are load-bearing”.

> **[Stacks, Tag 08UN], the full chain.** Let `A → B` be a ring map of local rings, let
> `A → A^h` and `B → B^h` be henselizations, and let `A^h → B^h` be compatible with them. Then
> `L_{B^h/A^h} = L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h` in `D(B^h)`, read as an isomorphism
> `L_{B/A} ⊗^𝐋_B B^h ≅ L_{B^h/A^h}`.
>
> This composes the two identifications above. The `resp.` strict variant is the same statement
> at `L_A = κ_A^sep` and `L_B = κ_B^sep`.

```lean
theorem nonempty_fundamentalVertex₁_iso_fundamentalVertex₃_henselization [IsLocalRing A]
    (B : Type u) [CommRing B] [IsLocalRing B] [Algebra A B]
    (LA : Type v) [Field LA] [Algebra (ResidueField A) LA]
    (LB : Type w) [Field LB] [Algebra (ResidueField B) LB]
    (Ah : Type u) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah] [IsHenselization A LA Ah]
    (Bh : Type u) [CommRing Bh] [IsLocalRing Bh] [Algebra B Bh] [IsHenselization B LB Bh]
    [Algebra A Bh] [IsScalarTower A B Bh] [Algebra Ah Bh] [IsScalarTower A Ah Bh]
    (hQXA : HasEtaleDiagonalTriangle.{u} A) (hQXB : HasEtaleDiagonalTriangle.{u} B)
    {α₁ : fundamentalVertex₁.{u, u} A B Bh ⟶ fundamentalVertex₂.{u, u} A Bh}
    {β₁ : fundamentalVertex₂.{u, u} A Bh ⟶ fundamentalVertex₃.{u, u} B Bh}
    {γ₁ : fundamentalVertex₃.{u, u} B Bh ⟶ (fundamentalVertex₁.{u, u} A B Bh)⟦(1 : ℤ)⟧}
    (hT₁ : Triangle.mk α₁ β₁ γ₁ ∈ distTriang (DerivedCategory (ModuleCat.{u} Bh)))
    {α₂ : fundamentalVertex₁.{u, u} A Ah Bh ⟶ fundamentalVertex₂.{u, u} A Bh}
    {β₂ : fundamentalVertex₂.{u, u} A Bh ⟶ fundamentalVertex₃.{u, u} Ah Bh}
    {γ₂ : fundamentalVertex₃.{u, u} Ah Bh ⟶ (fundamentalVertex₁.{u, u} A Ah Bh)⟦(1 : ℤ)⟧}
    (hT₂ : Triangle.mk α₂ β₂ γ₂ ∈ distTriang (DerivedCategory (ModuleCat.{u} Bh))) :
    Nonempty (fundamentalVertex₁.{u, u} A B Bh ≅ fundamentalVertex₃.{u, u} Ah Bh)
```

**`CommAlgCat.nonempty_fundamentalVertex₂_iso_fundamentalVertex₃_henselization_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/HenselizationUnconditional.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/HenselizationUnconditional.lean#L118). The attribute's comment: “the FIRST of the lemma's two equalities, `L_{B^h/A^h} = L_{B^h/A}`, and its `resp.` strict variant `L_{B^{sh}/A^{sh}} = L_{B^{sh}/A}` — one statement for both, because the henselization and a strict henselization are the two instances `L = κ` and `L = κ^sep` of `IsLocalRing.IsHenselization` (Stacks 04GQ). It is proved for an ARBITRARY `A^h`-algebra `C` in place of `B^h`, which is a generalization of the lemma and not a weakening of it. NOTHING is carried: the distinguished triangle of the tower `A → A^h → C` is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. The source's input `L_{A^h/A} = 0` is not carried either: it is proved, as `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived_unconditional`, which is what makes the henselization hypothesis on `A^h` load-bearing. The lemma's SECOND equality, `L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h`, is `CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_henselization_unconditional`”.

> **[Stacks, Tag 08UN], the identification over the henselized source.** Let `A → A^h` be a
> henselization of the local ring `A` and let `C` be an `A^h`-algebra. Then
> `L_{C/A} = L_{C/A^h}` in `D(C)`.
>
> This is `CommAlgCat.nonempty_fundamentalVertex₂_iso_fundamentalVertex₃_henselization` at the
> triangle of the tower `A → A^h → C` that Proposition 08QX provides.

```lean
theorem nonempty_fundamentalVertex₂_iso_fundamentalVertex₃_henselization_unconditional
    [IsLocalRing A] (L : Type v) [Field L] [Algebra (ResidueField A) L]
    (Ah : Type u) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah] [IsHenselization A L Ah]
    (C : Type u) [CommRing C] [Algebra A C] [Algebra Ah C] [IsScalarTower A Ah C] :
    Nonempty (fundamentalVertex₂.{u, u} A C ≅ fundamentalVertex₃.{u, u} Ah C)
```

**`CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_henselization_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/HenselizationUnconditional.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/HenselizationUnconditional.lean#L146). The attribute's comment: “the SECOND of the lemma's two equalities, `L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h`, and its `resp.` strict variant `L_{B^{sh}/A} = L_{B/A} ⊗^𝐋_B B^{sh}` — one statement for both, the henselization and a strict henselization being the two instances `L = κ` and `L = κ^sep` of `IsLocalRing.IsHenselization` (Stacks 04GQ). NOTHING is carried: the distinguished triangle of the tower `A → B → B^h` is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. The source's input `L_{B^h/B} = 0` is not carried either: it is proved, as `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived_unconditional`, so the henselization hypothesis on `B^h` is load-bearing. The lemma's FIRST equality, `L_{B^h/A^h} = L_{B^h/A}`, is `CommAlgCat.nonempty_fundamentalVertex₂_iso_fundamentalVertex₃_henselization_unconditional`. NOTE that the local ring homomorphism `A → B` of the source is not assumed: the conclusion holds for any ring map `A → B` whose target is local, which is a generalization”.

> **[Stacks, Tag 08UN], the derived scalar-extension identification.** Let `A → B` be a ring
> map, let `B → B^h` be a henselization of the local ring `B`, and let `A → B → B^h` be a tower.
> Then `L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h` in `D(B^h)`.
>
> This is `CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_henselization` at the
> triangle of the tower `A → B → B^h` that Proposition 08QX provides.

```lean
theorem nonempty_fundamentalVertex₁_iso_fundamentalVertex₂_henselization_unconditional
    (B : Type u) [CommRing B] [IsLocalRing B] [Algebra A B] (L : Type v) [Field L]
    [Algebra (ResidueField B) L]
    (Bh : Type u) [CommRing Bh] [IsLocalRing Bh] [Algebra B Bh] [IsHenselization B L Bh]
    [Algebra A Bh] [IsScalarTower A B Bh] :
    Nonempty (fundamentalVertex₁.{u, u} A B Bh ≅ fundamentalVertex₂.{u, u} A Bh)
```

**`CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₃_henselization_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/HenselizationUnconditional.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/HenselizationUnconditional.lean#L175). The attribute's comment: “the lemma's full chain `L_{B^h/A^h} = L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h`, read as the isomorphism `L_{B/A} ⊗^𝐋_B B^h ≅ L_{B^h/A^h}` in `D(B^h)` obtained by composing the two equalities, together with its `resp.` strict variant — one statement for both, the henselization and a strict henselization being the instances `L = κ` and `L = κ^sep` of `IsLocalRing.IsHenselization` (Stacks 04GQ). The induced map `A^h → B^h` is taken as given data (an `A^h`-algebra structure on `B^h` with `IsScalarTower A A^h B^h`) rather than constructed. NOTHING is carried: the distinguished triangles of the towers `A → B → B^h` and `A → A^h → B^h` are both Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. The source's inputs `L_{A^h/A} = 0` and `L_{B^h/B} = 0` are not carried either: both are proved, by `IsLocalRing.IsHenselization.isZero_cotangentComplexDerived_unconditional`, so both henselization hypotheses are load-bearing”.

> **[Stacks, Tag 08UN], the full chain.** Let `A → B` be a ring map of local rings, let
> `A → A^h` and `B → B^h` be henselizations, and let `A^h → B^h` be compatible with them. Then
> `L_{B^h/A^h} = L_{B^h/A} = L_{B/A} ⊗^𝐋_B B^h` in `D(B^h)`, read as an isomorphism
> `L_{B/A} ⊗^𝐋_B B^h ≅ L_{B^h/A^h}`.
>
> This is `CommAlgCat.nonempty_fundamentalVertex₁_iso_fundamentalVertex₃_henselization` at the
> triangles of the towers `A → B → B^h` and `A → A^h → B^h` that Proposition 08QX provides.

```lean
theorem nonempty_fundamentalVertex₁_iso_fundamentalVertex₃_henselization_unconditional
    [IsLocalRing A] (B : Type u) [CommRing B] [IsLocalRing B] [Algebra A B]
    (LA : Type v) [Field LA] [Algebra (ResidueField A) LA]
    (LB : Type w) [Field LB] [Algebra (ResidueField B) LB]
    (Ah : Type u) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah] [IsHenselization A LA Ah]
    (Bh : Type u) [CommRing Bh] [IsLocalRing Bh] [Algebra B Bh] [IsHenselization B LB Bh]
    [Algebra A Bh] [IsScalarTower A B Bh] [Algebra Ah Bh] [IsScalarTower A Ah Bh] :
    Nonempty (fundamentalVertex₁.{u, u} A B Bh ≅ fundamentalVertex₃.{u, u} Ah Bh)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.8, Tag 08QY](https://stacks.math.columbia.edu/tag/08QY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
