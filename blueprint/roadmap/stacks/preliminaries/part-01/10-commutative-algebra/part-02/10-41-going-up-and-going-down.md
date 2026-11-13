---
declaration: section
origin: cited
lean: RingHom.GoingUp, RingHom.GoingDown, isOpenMap_comap_satisfiesGoingDown, goingDown_iff_liftsGeneralizations, goingUp_iff_liftsSpecializations, RingHom.hasGoingDown_and_hasGoingUp_comp, goingUp_iff_isClosedMap_comap, Stacks.TensorProductSpecImage.images_eq
statement: formalized
proof: formalized
---

# 10.41 Going up and going down

Section 10.41 of the Stacks Project, [Tag 00HU](https://stacks.math.columbia.edu/tag/00HU). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00HV, a definition

[Tag 00HV](https://stacks.math.columbia.edu/tag/00HV) in the Stacks Project.

**`RingHom.GoingUp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/GoingUpGoingDown/Defs.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/GoingUpGoingDown/Defs.lean#L63). The attribute's comment: “(1)”.

> A ring map `φ : R → S` satisfies **going up** if for all primes
> `p ⊆ p'` of `R` and every prime `q` of `S` lying over `p` (that is,
> `Ideal.comap φ q = p`), there exists a prime `q'` of `S` with `q ⊆ q'`
> lying over `p'`.

```lean
def RingHom.GoingUp (φ : R →+* S) : Prop
```

**`RingHom.GoingDown`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/GoingUpGoingDown/Defs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/GoingUpGoingDown/Defs.lean#L73). The attribute's comment: “(2)”.

> A ring map `φ : R → S` satisfies **going down** if for all primes
> `p ⊆ p'` of `R` and every prime `q'` of `S` lying over `p'` (that is,
> `Ideal.comap φ q' = p'`), there exists a prime `q` of `S` with `q ⊆ q'`
> lying over `p`.

```lean
def RingHom.GoingDown (φ : R →+* S) : Prop
```

## Tag 0407, a lemma

[Tag 0407](https://stacks.math.columbia.edu/tag/0407) in the Stacks Project.

**`isOpenMap_comap_satisfiesGoingDown`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean, line 653](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean#L653).

> Stacks Tag 0407 (Lemma 10.41.2): if the induced map on prime spectra
> `φ* = PrimeSpectrum.comap φ : Spec(S) → Spec(R)` is an open map, then `φ`
> satisfies going down.

```lean
theorem isOpenMap_comap_satisfiesGoingDown
    {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    (h : IsOpenMap (comap φ)) : φ.SatisfiesGoingDown
```

## Tag 00HW, a lemma

[Tag 00HW](https://stacks.math.columbia.edu/tag/00HW) in the Stacks Project.

**`goingDown_iff_liftsGeneralizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean#L299). The attribute's comment: “(1)”.

> **Stacks 00HW (1).** A ring map `φ : R → S` satisfies going down if and only if
> generalizations lift along `Spec(S) → Spec(R)`.

```lean
theorem goingDown_iff_liftsGeneralizations (φ : R →+* S) :
    RingHom.GoingDown φ ↔
      LiftsGeneralizations (PrimeSpectrum.comap φ)
```

**`goingUp_iff_liftsSpecializations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean#L308). The attribute's comment: “(2)”.

> **Stacks 00HW (2).** A ring map `φ : R → S` satisfies going up if and only if
> specializations lift along `Spec(S) → Spec(R)`.

```lean
theorem goingUp_iff_liftsSpecializations (φ : R →+* S) :
    RingHom.GoingUp φ ↔
      LiftsSpecializations (PrimeSpectrum.comap φ)
```

## Tag 00HX, a lemma

[Tag 00HX](https://stacks.math.columbia.edu/tag/00HX) in the Stacks Project.

**`RingHom.hasGoingDown_and_hasGoingUp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean#L128). The attribute's comment: “Both assertions, for a composite of ring maps. For a tower of algebras they are `Algebra.HasGoingDown.trans` and `Algebra.HasGoingUp.trans`, which carry this tag as well.”.

> **Stacks 00HX.** If the ring maps `f : R →+* S` and `g : S →+* T` satisfy going down, then so
> does `g ∘ f`; likewise for going up.

```lean
public theorem hasGoingDown_and_hasGoingUp_comp {R S T : Type*} [CommRing R] [CommRing S]
    [CommRing T] (f : R →+* S) (g : S →+* T) :
    (letI := f.toAlgebra; letI := g.toAlgebra; letI := (g.comp f).toAlgebra;
      Algebra.HasGoingDown R S → Algebra.HasGoingDown S T → Algebra.HasGoingDown R T) ∧
    (letI := f.toAlgebra; letI := g.toAlgebra; letI := (g.comp f).toAlgebra;
      Algebra.HasGoingUp R S → Algebra.HasGoingUp S T → Algebra.HasGoingUp R T)
```

## Tag 00HZ, a lemma

[Tag 00HZ](https://stacks.math.columbia.edu/tag/00HZ) in the Stacks Project.

**`goingUp_iff_isClosedMap_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Specialization.lean#L358).

> **Stacks 00HZ.** For a ring map `φ : R → S`, going up holds if and only if the
> induced map `Spec(S) → Spec(R)` is closed.

```lean
theorem goingUp_iff_isClosedMap_comap (φ : R →+* S) :
    RingHom.GoingUp φ ↔ IsClosedMap (PrimeSpectrum.comap φ)
```

## Tag 037F, a lemma

[Tag 037F](https://stacks.math.columbia.edu/tag/037F) in the Stacks Project.

**`Stacks.TensorProductSpecImage.images_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorProduct/SpecImage.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/TensorProduct/SpecImage.lean#L257).

> The images in `Spec(R)` of the two diagonal maps coincide:
> `im(Spec(α)) = im(Spec(α'))`.

```lean
theorem images_eq (hι : Function.Injective ι) :
    Set.range (PrimeSpectrum.comap (R := R)
        (S := Localization.Away (baseChangeIncl k R S S' ι f)) (alphaMap k R S S' ι f)) =
      Set.range (PrimeSpectrum.comap (R := R) (S := Localization.Away f) (alphaPrime k R S'
          f))
```

## Tag 00EA, a lemma

[Tag 00EA](https://stacks.math.columbia.edu/tag/00EA) in the Stacks Project.

**`localization_eq_of_unique_prime_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/UniquePrimeOver.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/UniquePrimeOver.lean#L67).

> If `p` is a prime of `R` with a unique prime `q` of `S` lying over it, and `R → S`
> satisfies going up (or going down together with injectivity of contraction on primes),
> then the localization of `S` at the image of `R ∖ p` is also a localization of `S` at
> the complement of `q`; that is, `S_p = S_q`.

```lean
theorem localization_eq_of_unique_prime_over
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p]
    (huniq : ∀ q' : Ideal S, q'.IsPrime → q'.LiesOver p → q' = q)
    (h2 :
      (∀ (p₁ p₂ : Ideal R) (q₁ : Ideal S), p₁.IsPrime → p₂.IsPrime → q₁.IsPrime →
          p₁ ≤ p₂ → q₁.under R = p₁ →
            ∃ q₂ : Ideal S, q₂.IsPrime ∧ q₁ ≤ q₂ ∧ q₂.under R = p₂) ∨
      (Algebra.HasGoingDown R S ∧
        ∀ (q₁ q₂ : Ideal S), q₁.IsPrime → q₂.IsPrime →
          q₁.under R = q₂.under R → q₁ = q₂)) :
    IsLocalization q.primeCompl
      (Localization (Algebra.algebraMapSubmonoid S p.primeCompl))
```

## Tag 080T, a lemma

[Tag 080T](https://stacks.math.columbia.edu/tag/080T) in the Stacks Project.

**`generalizingMap_suppMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Support/GoingDown.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Support/GoingDown.lean#L377). References: SGA 1 IV (2.4), “more general”.

> **Stacks Tag 080T (topological formulation).** If `N` is a finite `S`-module that is
> flat over `R`, then generalizations lift along `π : Supp(N) → Spec(R)`.

```lean
theorem generalizingMap_suppMap [Module.Finite S N] [Module.Flat R N] :
    GeneralizingMap (suppMap (R := R) (S := S) (N := N))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.41, Tag 00HU](https://stacks.math.columbia.edu/tag/00HU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
