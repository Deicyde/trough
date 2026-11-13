---
declaration: section
origin: cited
lean: Stacks.Algebraization.nonempty_preparedExtension, Stacks.Algebraization.CoherentTriple.eulerCharacteristic, Stacks.Algebraization.kernel_finiteLength, Stacks.Algebraization.cokernel_finiteLength, Stacks.Algebraization.PreparedExtension.eulerCharacteristic_eq, Stacks.Algebraization.eulerCharacteristic_add_of_shortExact, Stacks.Algebraization.CoherentTriple.eulerCharacteristic_add_of_shortExact, Stacks.Algebraization.exists_polynomial_natDegree_le_dim_supp
statement: formalized
proof: formalized
---

# 52.25 Coherent triples

Section 52.25 of the Stacks Project, [Tag 0F22](https://stacks.math.columbia.edu/tag/0F22). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F23, a lemma

[Tag 0F23](https://stacks.math.columbia.edu/tag/0F23) in the Stacks Project.

**`Stacks.Algebraization.nonempty_preparedExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTriplePreparation.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTriplePreparation.lean#L262).

> **Stacks Project, Tag 0F23.** Every coherent triple admits a prepared extension: a coherent
> module on `Spec A` on which `f` acts regularly, isomorphic to the triple's punctured-spectrum
> member over the punctured spectrum, and mapping compatibly to its closed-fibre member.
>
> The module is `𝔪ⁿ G` for a coherent extension `G ⟶ j_*F` of the punctured-spectrum member of the
> triple and a suitable power `n`; the three steps are described in the implementation notes of
> this file.

```lean
public theorem nonempty_preparedExtension (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] (f : A) (T : CoherentTriple A f) :
    Nonempty (PreparedExtension A f T)
```

## Tag 0F24, an equation

[Tag 0F24](https://stacks.math.columbia.edu/tag/0F24) in the Stacks Project.

**`Stacks.Algebraization.CoherentTriple.eulerCharacteristic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertPolynomial.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertPolynomial.lean#L92). The attribute's comment: “the Euler characteristic of the triple itself”.

> **The Euler characteristic of a coherent triple**: the length of the cokernel minus the
> length of the kernel of the closed-fibre map of a prepared extension. Prepared extensions exist
> by `Stacks.Algebraization.nonempty_preparedExtension`, and the number does not depend on the one
> chosen by `Stacks.Algebraization.PreparedExtension.eulerCharacteristic_eq`.

```lean
public noncomputable def CoherentTriple.eulerCharacteristic {A : Type u} [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] {f : A} (T : CoherentTriple A f) : ℤ
```

**`Stacks.Algebraization.kernel_finiteLength`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleLength.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleLength.lean#L490). The attribute's comment: “finite length of the kernel”.

> **The kernel of the closed-fibre map of a prepared extension has finite length over `A`.**

```lean
public theorem kernel_finiteLength
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (f : A)
    (T : CoherentTriple A f) (P : PreparedExtension A f T) :
    IsFiniteLength A (kernel P.closedFibreMap).carrier
```

**`Stacks.Algebraization.cokernel_finiteLength`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleLength.lean, line 503](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleLength.lean#L503). The attribute's comment: “finite length of the cokernel”.

> **The cokernel of the closed-fibre map of a prepared extension has finite length over
> `A`.**

```lean
public theorem cokernel_finiteLength
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (f : A)
    (T : CoherentTriple A f) (P : PreparedExtension A f T) :
    IsFiniteLength A (cokernel P.closedFibreMap).carrier
```

## Tag 0F25, a lemma

[Tag 0F25](https://stacks.math.columbia.edu/tag/0F25) in the Stacks Project.

**`Stacks.Algebraization.PreparedExtension.eulerCharacteristic_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerCharacteristic/WellDefined.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerCharacteristic/WellDefined.lean#L483).

> **Stacks Project, Tag 0F25.** The Euler characteristic of a coherent triple does not depend
> on the prepared extension used to compute it: any two prepared extensions of the same triple have
> the same Euler characteristic.

```lean
public theorem PreparedExtension.eulerCharacteristic_eq
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (f : A) (hf : f ∈ IsLocalRing.maximalIdeal A)
    (T : CoherentTriple A f) (P Q : PreparedExtension A f T) :
    P.eulerCharacteristic = Q.eulerCharacteristic
```

## Tag 0F26, a lemma

[Tag 0F26](https://stacks.math.columbia.edu/tag/0F26) in the Stacks Project.

**`Stacks.Algebraization.eulerCharacteristic_add_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerCharacteristic/Additivity.lean, line 727](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerCharacteristic/Additivity.lean#L727).

> **Stacks Project, Tag 0F26.** The Euler characteristic of a coherent triple is additive
> along a short exact sequence of coherent triples: for any prepared extensions `P`, `Q` and `N`
> of the three terms, the Euler characteristic of `Q` is the sum of those of `P` and `N`.

```lean
public theorem eulerCharacteristic_add_of_shortExact
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (f : A)
    (hf : f ∈ IsLocalRing.maximalIdeal A)
    {T S R : CoherentTriple A f} {φ : T.Hom S} {ψ : S.Hom R}
    (hT : CoherentTriple.ShortExact φ ψ)
    (P : PreparedExtension A f T) (Q : PreparedExtension A f S)
    (N : PreparedExtension A f R) :
    Q.eulerCharacteristic = P.eulerCharacteristic + N.eulerCharacteristic
```

**`Stacks.Algebraization.CoherentTriple.eulerCharacteristic_add_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertPolynomial.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertPolynomial.lean#L157). The attribute's comment: “additivity for the Euler characteristics of the triples themselves”.

> **Stacks Project, Tag 0F26 for the triples themselves.** The Euler characteristic of a
> coherent triple is additive along a short exact sequence of coherent triples.

```lean
public theorem CoherentTriple.eulerCharacteristic_add_of_shortExact {A : Type u} [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] {f : A} (hf : f ∈ IsLocalRing.maximalIdeal A)
    {T S R : CoherentTriple A f} {φ : CoherentTriple.Hom T S}
    {ψ : CoherentTriple.Hom S R} (hse : CoherentTriple.ShortExact φ ψ) :
    S.eulerCharacteristic = T.eulerCharacteristic + R.eulerCharacteristic
```

## Tag 0F27, a proposition

[Tag 0F27](https://stacks.math.columbia.edu/tag/0F27) in the Stacks Project.

**`Stacks.Algebraization.exists_polynomial_natDegree_le_dim_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertInductionStep.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertInductionStep.lean#L171).

> Let `A` be a Noetherian local ring, `f ∈ 𝔪` a nonzerodivisor, and `(L, L₀, λ)` an invertible
> coherent triple. For every coherent triple `T = (F, F₀, α)` there is a polynomial `P ∈ ℚ[t]` with
>
> `χ(T ⊗ (L, L₀, λ)^{⊗ n}) = P(n)` for every `n ∈ ℤ`,
>
> and `deg P ≤ dim(Supp F)`, the dimension being truncated at `0`.

```lean
public theorem exists_polynomial_natDegree_le_dim_supp (hf : f ∈ maximalIdeal A)
    (L : CoherentTriple A f) (hL : IsInvertibleTriple L) (T : CoherentTriple A f) :
    ∃ P : Polynomial ℚ,
      (P.natDegree : WithBot ℕ∞) ≤ max 0 (topologicalKrullDim ↥(SheafOfModules.supp T.F)) ∧
        ∀ n : ℤ, (((T.twistZ L hL n).eulerCharacteristic : ℤ) : ℚ) = P.eval (n : ℚ)
```

**`Stacks.Algebraization.exists_polynomial_natDegree_le_of_forall_sub_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertPolynomial.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleHilbertPolynomial.lean#L205). The attribute's comment: “the concluding step: polynomiality on ℤ from the first difference”.

> **A function on all of `ℤ` whose first difference is a polynomial is a polynomial.** If
> `g : ℤ → ℤ` satisfies `g (n + 1) - g n = Q(n)` at every integer `n`, with `Q` a rational
> polynomial of degree at most `d`, then `g` agrees at every integer with a rational polynomial of
> degree at most `d + 1`.
>
> This is the variant of [Stacks, Tag 00JZ] for functions defined on all integers with which the
> proof of [Stacks, Tag 0F27] concludes, and unlike `IsNumericalPolynomial` it constrains the
> function at every integer rather than only at large ones.

```lean
public theorem exists_polynomial_natDegree_le_of_forall_sub_eq {g : ℤ → ℤ} {d : ℕ}
    {Q : Polynomial ℚ} (hQ : Q.natDegree ≤ d)
    (hg : ∀ n : ℤ, (g (n + 1) : ℚ) - (g n : ℚ) = Q.eval (n : ℚ)) :
    ∃ P : Polynomial ℚ, P.natDegree ≤ d + 1 ∧ ∀ n : ℤ, (g n : ℚ) = P.eval (n : ℚ)
```

**`Stacks.Algebraization.CoherentTriple.twistPow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleTensor.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleTensor.lean#L246). The attribute's comment: “the twist of a coherent triple by the nonnegative powers of an invertible triple”.

> **The twists of a coherent triple by the nonnegative tensor powers of an invertible coherent
> triple.** The zeroth twist is the triple itself and each further one is the tensor product of the
> previous one with the invertible triple, so the `n`-th is `(F ⊗ L^\{⊗ n}, F₀ ⊗ L₀^\{⊗ n}, α ⊗ λ^\{⊗
> n})` up to the associativity of the tensor product. This is the family whose Euler
> characteristics [Stacks, Tag 0F27] asserts to be given by a polynomial.

```lean
public noncomputable def CoherentTriple.twistPow {A : Type u} [CommRing A] [IsLocalRing A]
    {f : A} (T L : CoherentTriple A f) (hL : IsInvertibleTriple L) : ℕ → CoherentTriple A f
```

**`Stacks.Algebraization.CoherentTriple.twistZ`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleTwist.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleTwist.lean#L187). The attribute's comment: “the integer twists of a coherent triple by an invertible coherent triple”.

> **The twist of a coherent triple by the `n`-th tensor power of an invertible coherent
> triple**, for `n : ℤ`. Its members are the tensor products of the members of the triple with the
> `n`-th tensor powers of the members of the invertible triple, and its identification over the
> punctured closed fibre is the tensor product of the two identifications, the second taken in its
> `n`-th tensor power.
>
> This is the family whose Euler characteristics [Stacks, Tag 0F27] asserts to be given by a
> polynomial.

```lean
public noncomputable def CoherentTriple.twistZ {A : Type u} [CommRing A] [IsLocalRing A] {f : A}
    (T L : CoherentTriple A f) (hL : IsInvertibleTriple L) (n : ℤ) : CoherentTriple A f
```

## Tag 0F28, a lemma

[Tag 0F28](https://stacks.math.columbia.edu/tag/0F28) in the Stacks Project.

**`Stacks.Algebraization.CoherentTriple.eulerCharacteristic_eq_length_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerFormula.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerFormula.lean#L168). The attribute's comment: “the Euler characteristic formula”.

> **Stacks Project, Tag 0F28.** For an invertible coherent triple over a Noetherian local ring
> of depth at least three, the Euler characteristic of the triple is the length of the cokernel of
> the canonical map on global sections.
>
> The prepared extension taken is the direct image of the triple's punctured-spectrum member; its
> closed-fibre map has a cokernel of the same length as that of the canonical map on global
> sections, and its kernel vanishes because the global sections of that direct image have depth at
> least two over `A`.

```lean
public theorem CoherentTriple.eulerCharacteristic_eq_length_cokernel (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] (f : A) (hf : f ∈ maximalIdeal A) (hreg : IsRegular f)
    (T : CoherentTriple A f)
    [AlgebraicGeometry.SheafOfModules.IsInvertible
      (Stacks.Divisors.puncturedSpectrum A).toScheme.presheaf
      (Stacks.Divisors.puncturedSpectrum A).toScheme.ringCatSheaf.2 T.F]
    [AlgebraicGeometry.SheafOfModules.IsInvertible (closedFibre A f).presheaf
      (closedFibre A f).ringCatSheaf.2 T.F₀]
    (hdepth : 3 ≤ Module.depth A (maximalIdeal A) A) :
    letI := puncturedSectionsModule A T.F
    letI := puncturedClosedFibreSectionsModule A f
      ((Scheme.Modules.pullback (puncturedClosedFibre A f).ι).obj T.F₀)
    T.eulerCharacteristic =
      ((Module.length A
        (Γ((Scheme.Modules.pullback (puncturedClosedFibre A f).ι).obj T.F₀, ⊤) ⧸
          LinearMap.range (globalSectionsMap A f T))).toNat : ℤ)
```

**`Stacks.Algebraization.CoherentTriple.eulerCharacteristic_nonneg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerFormula.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleEulerFormula.lean#L210). The attribute's comment: “nonnegativity”.

> **The Euler characteristic of an invertible coherent triple is nonnegative**, being the
> length of a cokernel.

```lean
public theorem CoherentTriple.eulerCharacteristic_nonneg (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] (f : A) (hf : f ∈ maximalIdeal A) (hreg : IsRegular f)
    (T : CoherentTriple A f)
    [AlgebraicGeometry.SheafOfModules.IsInvertible
      (Stacks.Divisors.puncturedSpectrum A).toScheme.presheaf
      (Stacks.Divisors.puncturedSpectrum A).toScheme.ringCatSheaf.2 T.F]
    [AlgebraicGeometry.SheafOfModules.IsInvertible (closedFibre A f).presheaf
      (closedFibre A f).ringCatSheaf.2 T.F₀]
    (hdepth : 3 ≤ Module.depth A (maximalIdeal A) A) :
    0 ≤ T.eulerCharacteristic
```

**`Stacks.Algebraization.globalSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleInvertible.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleInvertible.lean#L170). The attribute's comment: “the canonical map on global sections”.

> **The canonical map on global sections of a coherent triple.** It carries a section of the
> module on the punctured spectrum to its restriction to the punctured closed fibre, read through
> the triple's identification as a section of the module on the closed fibre. It is linear over
> `A`, which acts on both sides through the structure morphisms.

```lean
noncomputable def globalSectionsMap (A : Type u) [CommRing A] [IsLocalRing A] (f : A)
    (T : CoherentTriple A f) :
    letI := puncturedSectionsModule A T.F
    letI := puncturedClosedFibreSectionsModule A f
      ((Scheme.Modules.pullback (puncturedClosedFibre A f).ι).obj T.F₀)
    Γ(T.F, ⊤) →ₗ[A] Γ((Scheme.Modules.pullback (puncturedClosedFibre A f).ι).obj T.F₀, ⊤)
```

**`Stacks.Algebraization.finiteLength_cokernel_globalSectionsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleInvertible.lean, line 750](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleInvertible.lean#L750). The attribute's comment: “finite length of the cokernel”.

> **The cokernel of the canonical map on global sections has finite length.** The restriction
> map from the closed fibre to the punctured closed fibre is surjective, by Hartogs extension on
> `A / fA`, and restriction along the closed immersion is surjective on global sections, so the
> cokernel is a quotient of the cokernel of the closed-fibre map of any prepared extension of the
> triple, which has finite length.

```lean
theorem finiteLength_cokernel_globalSectionsMap (A : Type u) [CommRing A] [IsLocalRing A]
    [IsNoetherianRing A] (f : A) (hf : f ∈ maximalIdeal A) (hreg : IsRegular f)
    (T : CoherentTriple A f)
    [AlgebraicGeometry.SheafOfModules.IsInvertible (closedFibre A f).presheaf
      (closedFibre A f).ringCatSheaf.2 T.F₀]
    (hdepth : 3 ≤ Module.depth A (maximalIdeal A) A) :
    letI := puncturedSectionsModule A T.F
    letI := puncturedClosedFibreSectionsModule A f
      ((Scheme.Modules.pullback (puncturedClosedFibre A f).ι).obj T.F₀)
    IsFiniteLength A
      (Γ((Scheme.Modules.pullback (puncturedClosedFibre A f).ι).obj T.F₀, ⊤) ⧸
        LinearMap.range (globalSectionsMap A f T))
```

**`Stacks.Algebraization.CoherentTriple.eulerCharacteristic_eq_zero_iff_isTrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleTriviality.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Algebraization/CoherentTripleTriviality.lean#L316). The attribute's comment: “vanishing criterion”.

> **Stacks Project, Tag 0F28.** For an invertible coherent triple over a Noetherian local ring
> of depth at least three, the Euler characteristic of the triple vanishes exactly when the member
> on the punctured spectrum is trivial.
>
> By the Euler-characteristic formula the vanishing is the surjectivity of the canonical map on
> global sections, which for the prepared extension given by the direct image of the
> punctured-spectrum member is the surjectivity of the closed-fibre map; that map is injective by
> `Stacks.Algebraization.injective_closedFibreMap_of_pushforward`, and the two halves of the
> criterion are
> `Stacks.Algebraization.isTrivial_of_bijective_closedFibreMap` and
> `Stacks.Algebraization.isIso_closedFibreMap_of_isTrivial`.

```lean
public theorem CoherentTriple.eulerCharacteristic_eq_zero_iff_isTrivial (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] (f : A) (hf : f ∈ maximalIdeal A) (hreg : IsRegular f)
    (T : CoherentTriple A f)
    [AlgebraicGeometry.SheafOfModules.IsInvertible
      (Stacks.Divisors.puncturedSpectrum A).toScheme.presheaf
      (Stacks.Divisors.puncturedSpectrum A).toScheme.ringCatSheaf.2 T.F]
    [AlgebraicGeometry.SheafOfModules.IsInvertible (closedFibre A f).presheaf
      (closedFibre A f).ringCatSheaf.2 T.F₀]
    (hdepth : 3 ≤ Module.depth A (maximalIdeal A) A) :
    T.eulerCharacteristic = 0 ↔
      Stacks.SheafOfModules.IsTrivial (Stacks.Divisors.puncturedSpectrum A).toScheme.presheaf
        (Stacks.Divisors.puncturedSpectrum A).toScheme.ringCatSheaf.2 T.F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.25, Tag 0F22](https://stacks.math.columbia.edu/tag/0F22)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
