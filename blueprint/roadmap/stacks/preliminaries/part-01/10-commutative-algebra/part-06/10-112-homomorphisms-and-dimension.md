---
declaration: section
origin: cited
lean: ringKrullDim_le_of_goingUp, ringKrullDim_le_of_goingDown, comap_isMaximal_of_goingUp, integral_dim_up, Algebra.IsIntegral.ringKrullDim_eq, Ideal.Fiber, PrimeSpectrum.primesOverOrderIsoFiber, Ideal.Fiber.localizationAlgEquivQuotient
statement: formalized
proof: formalized
---

# 10.112 Homomorphisms and dimension

Section 10.112 of the Stacks Project, [Tag 00OG](https://stacks.math.columbia.edu/tag/00OG). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00OH, a lemma

[Tag 00OH](https://stacks.math.columbia.edu/tag/00OH) in the Stacks Project.

**`ringKrullDim_le_of_goingUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean#L158). References: EGA IV (5.4.1), “(ii), special case”.

> **Going-up version.**
> If `φ : R → S` satisfies going up and the induced map `Spec(S) → Spec(R)` is
> surjective, then `dim(R) ≤ dim(S)`.
>
> This follows from `chain_lift_goingUp` through `krullDim_le_of_chain_lift`, since
> `ringKrullDim R` is `krullDim (PrimeSpectrum R)` by definition.

```lean
theorem ringKrullDim_le_of_goingUp (φ : R →+* S) (hup : GoingUp_00oh φ)
    (hsurj : Function.Surjective (PrimeSpectrum.comap φ)) :
    ringKrullDim R ≤ ringKrullDim S
```

**`ringKrullDim_le_of_goingDown`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean#L169). References: EGA IV (5.4.1), “(ii), special case”.

> **Going-down version.**
> If `φ : R → S` satisfies going down and the induced map `Spec(S) → Spec(R)` is
> surjective, then `dim(R) ≤ dim(S)`.
>
> This follows from `chain_lift_goingDown` through `krullDim_le_of_chain_lift`.

```lean
theorem ringKrullDim_le_of_goingDown (φ : R →+* S) (hdown : GoingDown_00oh φ)
    (hsurj : Function.Surjective (PrimeSpectrum.comap φ)) :
    ringKrullDim R ≤ ringKrullDim S
```

## Tag 00OI, a lemma

[Tag 00OI](https://stacks.math.columbia.edu/tag/00OI) in the Stacks Project.

**`comap_isMaximal_of_goingUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean#L208).

> **Stacks Tag 00OI.** If `φ : R → S` satisfies going up and `q ⊆ S` is a maximal
> ideal, then its contraction `φ⁻¹(q)` is a maximal ideal of `R`.

```lean
theorem comap_isMaximal_of_goingUp (φ : R →+* S) (hφ : GoingUp φ)
    (q : Ideal S) (hq : q.IsMaximal) :
    (Ideal.comap φ q).IsMaximal
```

## Tag 00OJ, a lemma

[Tag 00OJ](https://stacks.math.columbia.edu/tag/00OJ) in the Stacks Project.

**`integral_dim_up`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/GoingUpGoingDown.lean#L259). References: EGA 0 (16.1.5), “dim(B) ≤ dim(A)”; EGA IV (4.1.2), “(ii), special case”; EGA IV (5.4.2), “Affine case”; EGA IV (5.4.3), “dim(B) ≤ dim(A)”; EGA IV (5.5.1), “special case”; EGA IV (5.5.2), “special case”; EGA IV (5.6.6), “special case”.

> **Stacks Tag 00OJ.** If `f : R → S` is a ring map making `S` integral over `R`,
> then `ringKrullDim S ≤ ringKrullDim R` and every closed point of `Spec(S)` contracts
> to a closed point of `Spec(R)`.

```lean
theorem integral_dim_up
    {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    (hf : f.IsIntegral) :
    ringKrullDim S ≤ ringKrullDim R ∧
    ∀ q : PrimeSpectrum S, IsClosed ({q} : Set (PrimeSpectrum S)) →
      IsClosed ({PrimeSpectrum.comap f q} : Set (PrimeSpectrum R))
```

## Tag 00OK, a lemma

[Tag 00OK](https://stacks.math.columbia.edu/tag/00OK) in the Stacks Project.

**`Algebra.IsIntegral.ringKrullDim_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/IntegralExtension.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/IntegralExtension.lean#L215). The attribute's comment: “The source's ring inclusion `R ⊆ S` is stated as an `R`-algebra `S` with `algebraMap R S` injective, spelled `FaithfulSMul R S`; see the module docstring.”. References: EGA 0 (16.1.5), “ρ injective case”; EGA IV (5.4.3), “more general”.

> **Stacks 00OK.** If `S` is an integral `R`-algebra whose structure map `R → S` is injective
> (for instance an integral ring extension `R ⊆ S`), then `R` and `S` have the same Krull
> dimension.

```lean
public theorem Algebra.IsIntegral.ringKrullDim_eq (R S : Type*) [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.IsIntegral R S] [FaithfulSMul R S] :
    ringKrullDim R = ringKrullDim S
```

## Tag 00OL, a definition

[Tag 00OL](https://stacks.math.columbia.edu/tag/00OL) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.Fiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Fiber#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L238) (StacksFrontier): “the fibre ring S ⊗\_R κ(p) (written κ(p) ⊗\_R S)”. References: EGA III (4.6.2), “special case”; EGA IV (7.3.13), “more general”; EGA IV (12.1.1.4), “special case”; EGA IV (15.1.1), “affine, special case”; EGA IV (15.4.1), “special case”; EGA IV (1.8.6), “affine case”; EGA IV (2.2.1), “special case”; EGA IV (2.5.5), “affine fiber module”; EGA IV (3.3.1), “special case”; SGA 1 II (4.8), “more general”; SGA 1 III (1.7); SGA 7 VI (5.1).
- [`PrimeSpectrum.primesOverOrderIsoFiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.primesOverOrderIsoFiber#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L239) (StacksFrontier): “primes q of S lying over p = primes of the fibre ring (inverse: comap along S -> κ(p) ⊗\_R S)”.
- [`Ideal.Fiber.localizationAlgEquivQuotient`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.Fiber.localizationAlgEquivQuotient#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L241) (StacksFrontier): “(S ⊗\_R κ(p))\_q = S\_q / p S\_q, with q the prime of S under the fibre prime”.
- [`Localization.AtPrime.isLocalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Localization.AtPrime.isLocalRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L243) (StacksFrontier): “the localization at a prime is a local ring”. References: EGA 0 (10.3.1.1), “B is a local ring”; EGA 0 (1.2.3), “A\_p is a local ring”; EGA 0 (1.2.7), “A\_p is local”; EGA 0 (7.6.17), “special case”; EGA I (1.1.1), “A\_x is a local ring”; SGA 3 VIIB (0.1.1), “partial”.

## Tag 031E, a lemma

[Tag 031E](https://stacks.math.columbia.edu/tag/031E) in the Stacks Project.

**`isRegularLocalRing_of_flat_of_closedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RegularLocalRing/FlatLocalHom.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RegularLocalRing/FlatLocalHom.lean#L268). References: EGA IV (6.5.2), “(ii), local case”; EGA IV (7.5.1.1), “special case”; SGA 1 I (9.1), “A regular ⇒ B regular”.

> Let `φ : R → S` be a local homomorphism of local
> Noetherian rings such that:
> 1. `R` is regular,
> 2. the closed fibre `S / m_R S` is regular, and
> 3. `φ : R → S` is flat.
> Then `S` is regular.

```lean
theorem isRegularLocalRing_of_flat_of_closedFibre (R S : Type*) [CommRing R] [CommRing S]
    [IsLocalRing R] [IsNoetherianRing R] [IsLocalRing S] [IsNoetherianRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)]
    (hR : IsRegularLocalRing R)
    (hfibre : IsRegularLocalRing (ClosedFibre R S))
    (hflat : Module.Flat R S) :
    IsRegularLocalRing S
```

## Tag 00R5, a lemma

[Tag 00R5](https://stacks.math.columbia.edu/tag/00R5) in the Stacks Project.

**`Module.isMaximalCohenMacaulay_self_and_ringKrullDim_eq_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/FlatLocalHom.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/FlatLocalHom.lean#L206). The attribute's comment: “Cohen-Macaulayness of a Noetherian local ring `A` (Definition 00N8) is `Module.IsMaximalCohenMacaulay A A`, i.e. `depth_{𝔪_A}(A) = dim A`; the source's two alternatives are the disjunctive hypothesis `h` over the flatness common to both. See the module docstring.”. References: EGA 0 (17.3.5), “(ii) necessity”.

> **Stacks 00R5.** Let `R → S` be a local homomorphism of Noetherian local rings with `R`
> Cohen–Macaulay, i.e. `depth_{𝔪_R}(R) = dim(R)`. If `S` is flat over `R` and is either finite over
> `R` or of dimension at most `dim(R)`, then `S` is Cohen–Macaulay and `dim(R) = dim(S)`.

```lean
public theorem Module.isMaximalCohenMacaulay_self_and_ringKrullDim_eq_of_flat
    {R S : Type*} [CommRing R] [CommRing S] [IsNoetherianRing R] [IsNoetherianRing S]
    [IsLocalRing R] [IsLocalRing S] [Algebra R S] [IsLocalHom (algebraMap R S)]
    [Module.Flat R S] (hR : Module.IsMaximalCohenMacaulay R R)
    (h : Module.Finite R S ∨ ringKrullDim S ≤ ringKrullDim R) :
    Module.IsMaximalCohenMacaulay S S ∧ ringKrullDim R = ringKrullDim S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.112, Tag 00OG](https://stacks.math.columbia.edu/tag/00OG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
