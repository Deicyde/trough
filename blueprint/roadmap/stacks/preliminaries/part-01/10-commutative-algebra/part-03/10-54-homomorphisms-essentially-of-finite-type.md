---
declaration: section
origin: cited
lean: IsEssentiallyOfFiniteType, IsEssentiallyOfFinitePresentation, essFiniteType_comp, essFinitePresentation_comp, RingHom.EssentiallyOfFinitePresentation.baseChange, RingHom.EssFiniteType.isStableUnderBaseChange, finite_iff_residue_finite, finiteType_iff_residue_finiteType
statement: formalized
proof: formalized
---

# 10.54 Homomorphisms essentially of finite type

Section 10.54 of the Stacks Project, [Tag 07DR](https://stacks.math.columbia.edu/tag/07DR). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00QM, a definition

[Tag 00QM](https://stacks.math.columbia.edu/tag/00QM) in the Stacks Project.

**`IsEssentiallyOfFiniteType`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/Defs.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/Defs.lean#L55). The attribute's comment: “(1)”. References: EGA IV (1.3.8).

> A ring map `f : R →+* S` is *essentially of finite type* if `S` is, as an
> `R`-algebra (via `f`), the localization at some submonoid of an `R`-algebra `T`
> of finite type.

```lean
def IsEssentiallyOfFiniteType.{u} (R S : Type u) [CommRing R] [CommRing S]
    (f : R →+* S) : Prop
```

**`IsEssentiallyOfFinitePresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/Defs.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/Defs.lean#L65). The attribute's comment: “(2)”.

> A ring map `f : R →+* S` is *essentially of finite presentation* if `S` is,
> as an `R`-algebra (via `f`), the localization at some submonoid of an
> `R`-algebra `T` of finite presentation.

```lean
def IsEssentiallyOfFinitePresentation.{u} (R S : Type u) [CommRing R] [CommRing S]
    (f : R →+* S) : Prop
```

## Tag 07DS, a lemma

[Tag 07DS](https://stacks.math.columbia.edu/tag/07DS) in the Stacks Project.

**`essFiniteType_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/Composition.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/Composition.lean#L256). The attribute's comment: “(1)”. References: EGA IV (1.3.9).

> **Statement 1.** The class of ring maps essentially of finite type is
> preserved under composition (Stacks Tag 07DS, first assertion).

```lean
theorem essFiniteType_comp {R : Type u} {S : Type v} {T : Type w}
    [CommRing R] [CommRing S] [CommRing T] {f : R →+* S} {g : S →+* T}
    (hf : f.EssFiniteType) (hg : g.EssFiniteType) : (g.comp f).EssFiniteType
```

**`essFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/Composition.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/Composition.lean#L282). The attribute's comment: “(2)”.

> **Statement 2.** The class of ring maps essentially of finite presentation
> is preserved under composition (Stacks Tag 07DS, second assertion).
>
> The proof combines Stacks tag 053N, transitivity of finite presentation,
> localization-of-localization, and a universe re-presentation:
>
> 1. Unpack `hf`: f.p. `R`-algebra `A`, with `S = M⁻¹A` (`IsLocalization M S`).
>    Unpack `hg`: f.p. `S`-algebra `B`, with `T = N₂⁻¹B` (`IsLocalization N₂ T`).
> 2. `A` acts on `B` through `S` (`IsScalarTower A S B`).
> 3. `essFP_descent M B`: descend `B` to a f.p. `A`-algebra `B₀` with
>    `B = N⁻¹B₀` (`IsLocalization N B`).
> 4. `Algebra.FinitePresentation.trans R A B₀`: since `A` is f.p./R and `B₀` is
>    f.p./A, `B₀` is f.p./R.
> 5. localization-of-localization: `B = N⁻¹B₀` and `T = N₂⁻¹B`, so
>    `T = U⁻¹B₀` for `U := localizationLocalizationSubmodule N N₂`
>    (`IsLocalization.localization_localization_isLocalization`).
> 6. `essFP_reuniverse`: re-present the f.p. `R`-algebra `B₀ : Type (max u v w)`
>    (with its localization `IsLocalization U T`) by a f.p. `R`-algebra
>    `A' : Type (max u w)` carrying `IsLocalization U' T`, matching the universe
>    demanded by `RingHom.EssentiallyOfFinitePresentation` for `g.comp f : R →+* T`.

```lean
theorem essFinitePresentation_comp {R : Type u} {S : Type v} {T : Type w}
    [CommRing R] [CommRing S] [CommRing T] {f : R →+* S} {g : S →+* T}
    (hf : f.EssentiallyOfFinitePresentation) (hg : g.EssentiallyOfFinitePresentation) :
    (g.comp f).EssentiallyOfFinitePresentation
```

## Tag 0AUF, a lemma

[Tag 0AUF](https://stacks.math.columbia.edu/tag/0AUF) in the Stacks Project.

**`RingHom.EssentiallyOfFinitePresentation.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/BaseChange.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/BaseChange.lean#L84). The attribute's comment: “(2)”.

> **Essential finite presentation is preserved by base change.**  The target is written in the
> canonical tensor-product model of the pushout; invariance under isomorphism identifies this with
> any other model of the base change.

```lean
theorem baseChange {R : Type u} {S : Type v} {T : Type w}
    [CommRing R] [CommRing S] [CommRing T] [Algebra R S]
    (f : R →+* T) (h : f.EssentiallyOfFinitePresentation) :
    letI := f.toAlgebra
    ((Algebra.TensorProduct.includeLeft (R := R) (S := S) (A := S) (B := T)).toRingHom)
      |>.EssentiallyOfFinitePresentation
```

Declarations registered for the tag:

- [`RingHom.EssFiniteType.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.EssFiniteType.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/EssentialFiniteness/BaseChange.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/BaseChange.lean#L30) (StacksFrontier): “(1)”. References: EGA IV (1.3.9).

## Tag 07DT, a lemma

[Tag 07DT](https://stacks.math.columbia.edu/tag/07DT) in the Stacks Project.

**`finite_iff_residue_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/ArtinianTarget.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/ArtinianTarget.lean#L296). The attribute's comment: “(1)”.

> `f : R → S` is finite if and only if the composite `π ∘ f : R → S/m` is finite.

```lean
theorem finite_iff_residue_finite (f : R →+* S) :
    f.Finite ↔ ((IsLocalRing.residue S).comp f).Finite
```

**`finiteType_iff_residue_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/ArtinianTarget.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/ArtinianTarget.lean#L306). The attribute's comment: “(2)”. References: EGA I (6.4.11), “special case”.

> `f : R → S` is of finite type if and only if the composite `π ∘ f : R → S/m`
> is of finite type.

```lean
theorem finiteType_iff_residue_finiteType (f : R →+* S) :
    f.FiniteType ↔ ((IsLocalRing.residue S).comp f).FiniteType
```

**`essFiniteType_iff_residue_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/EssentialFiniteness/ArtinianTarget.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/EssentialFiniteness/ArtinianTarget.lean#L316). The attribute's comment: “(3)”. References: EGA I (6.4.11), “special case”.

> `f : R → S` is essentially of finite type if and only if the composite
> `π ∘ f : R → S/m` is essentially of finite type.

```lean
theorem essFiniteType_iff_residue_essFiniteType (f : R →+* S) :
    f.EssFiniteType ↔ ((IsLocalRing.residue S).comp f).EssFiniteType
```

## Tag 0AUG, a lemma

[Tag 0AUG](https://stacks.math.columbia.edu/tag/0AUG) in the Stacks Project.

**`exists_isLocalizationOfQuotientMap_mvPolynomial_atMaximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/ClosedPointOfSpecialFibre.lean, line 827](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/ClosedPointOfSpecialFibre.lean#L827).

> Let `R → S` be a ring map of local rings, not necessarily local, that is essentially of finite
> type. Then there are `n : ℕ` and a maximal ideal `𝔪 ⊆ R[x_1, …, x_n]` lying over the maximal ideal
> of `R` such that `S` is a localization of a quotient of the local ring `R[x_1, …, x_n]_𝔪`,
> compatibly with the `R`-algebra structures.

```lean
theorem exists_isLocalizationOfQuotientMap_mvPolynomial_atMaximal
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S]
    [Algebra R S] [Algebra.EssFiniteType R S] :
    ∃ (n : ℕ) (𝔪 : Ideal (MvPolynomial (Fin n) R)) (_ : 𝔪.IsMaximal),
      haveI : 𝔪.IsPrime := (‹𝔪.IsMaximal›).isPrime
      𝔪.comap (algebraMap R (MvPolynomial (Fin n) R)) = IsLocalRing.maximalIdeal R ∧
      ∃ (g : Localization.AtPrime 𝔪 →+* S),
        g.comp (algebraMap R (Localization.AtPrime 𝔪)) = algebraMap R S ∧
        IsLocalizationOfQuotientMap g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.54, Tag 07DR](https://stacks.math.columbia.edu/tag/07DR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
