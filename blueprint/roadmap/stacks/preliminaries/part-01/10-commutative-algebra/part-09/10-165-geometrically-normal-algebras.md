---
declaration: section
origin: cited
lean: Algebra.isNormalRing_tensorProduct_tfae, Algebra.IsGeometricallyNormal, Algebra.IsGeometricallyNormal.of_isLocalization, Algebra.IsGeometricallyNormal.of_isSeparableExtension, Algebra.IsGeometricallyNormal.isNormalRing_tensorProduct_of_isNormalRing, Algebra.isGeometricallyNormal_iff_of_isSeparable
statement: formalized
proof: formalized
---

# 10.165 Geometrically normal algebras

Section 10.165 of the Stacks Project, [Tag 037Y](https://stacks.math.columbia.edu/tag/037Y). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 037Z, a lemma

[Tag 037Z](https://stacks.math.columbia.edu/tag/037Z) in the Stacks Project.

**`Algebra.isNormalRing_tensorProduct_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyNormal/TFAE.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyNormal/TFAE.lean#L610). The attribute's comment: “The source's four conditions in its order, with a normal ring spelled by the library's `IsNormalRing` (Definition 00GV), a finitely generated field extension by `Algebra.EssFiniteType`, and the perfect closure taken abstractly, as `IsPerfectClosure`.”.

> **Stacks 037Z.** Let `k` be a field of exponential characteristic `p` and let `A` be a
> commutative `k`-algebra. The following are equivalent:
> (1) `k' ⊗[k] A` is a normal ring for every field extension `k'/k`;
> (2) `k' ⊗[k] A` is a normal ring for every finitely generated field extension `k'/k`;
> (3) `k' ⊗[k] A` is a normal ring for every finite purely inseparable extension `k'/k`;
> (4) `k^{perf} ⊗[k] A` is a normal ring, for a perfect closure `k^{perf}` of `k`.

```lean
public theorem isNormalRing_tensorProduct_tfae
    (k : Type u) [Field k] (p : ℕ) [ExpChar k p] (A : Type v) [CommRing A] [Algebra k A]
    (kperf : Type w) [Field kperf] [Algebra k kperf] [ExpChar kperf p] [PerfectRing kperf p]
    [IsPerfectClosure (algebraMap k kperf) p] :
    [∀ (k' : Type u) [Field k'] [Algebra k k'], IsNormalRing (k' ⊗[k] A),
      ∀ (k' : Type u) [Field k'] [Algebra k k'] [EssFiniteType k k'],
        IsNormalRing (k' ⊗[k] A),
      ∀ (k' : Type u) [Field k'] [Algebra k k'] [FiniteDimensional k k']
        [IsPurelyInseparable k k'], IsNormalRing (k' ⊗[k] A),
      IsNormalRing (kperf ⊗[k] A)].TFAE
```

## Tag 0380, a definition

[Tag 0380](https://stacks.math.columbia.edu/tag/0380) in the Stacks Project.

**`Algebra.IsGeometricallyNormal`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyNormal/Defs.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyNormal/Defs.lean#L111). The attribute's comment: “The first of the four equivalent conditions of Lemma 037Z, a normal ring being spelled by the library's `IsNormalRing` (Definition 00GV); the other three are criteria for it, through `Algebra.isNormalRing_tensorProduct_tfae`.”. References: EGA IV (6.7.6).

> A commutative algebra `A` over a field `k` is *geometrically normal* over `k` if the base
> change `k' ⊗[k] A` is a normal ring for every field extension `k'/k`. By Lemma 037Z it is enough
> to ask this for the finitely generated extensions, or for the finite purely inseparable ones, or
> for a single perfect closure of `k`.

```lean
public class IsGeometricallyNormal (k : Type u) (A : Type v) [Field k] [CommRing A]
    [Algebra k A] : Prop
```

## Tag 06DE, a lemma

[Tag 06DE](https://stacks.math.columbia.edu/tag/06DE) in the Stacks Project.

**`Algebra.IsGeometricallyNormal.of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyNormal/Localization.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyNormal/Localization.lean#L81). The attribute's comment: “The source's `S⁻¹A` is spelled abstractly as an `A`-algebra `A'` with `IsLocalization S A'` and `IsScalarTower k A A'`, so that the fraction field of a domain and the localizations at primes are instances of the statement rather than transports of it.”.

> A localization of a geometrically normal algebra over a field is geometrically normal: if `A`
> is geometrically normal over the field `k` and `A'` is the localization of `A` at a submonoid
> `S ⊆ A`, regarded as a `k`-algebra through `A`, then `A'` is geometrically normal over `k`.

```lean
public theorem IsGeometricallyNormal.of_isLocalization {k : Type u} {A : Type v} {A' : Type w}
    [Field k] [CommRing A] [CommRing A'] [Algebra k A] [Algebra k A'] [Algebra A A']
    [IsScalarTower k A A'] [IsGeometricallyNormal k A] (S : Submonoid A) [IsLocalization S A'] :
    IsGeometricallyNormal k A'
```

## Tag 0C30, a lemma

[Tag 0C30](https://stacks.math.columbia.edu/tag/0C30) in the Stacks Project.

**`Algebra.IsGeometricallyNormal.of_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyNormal/Separable.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyNormal/Separable.lean#L216). The attribute's comment: “Separability is the source's Definition 030O (2), `Algebra.IsSeparableExtension`, which does not require `K/k` algebraic, and not Mathlib's `Algebra.IsSeparable`; the converse implication is Proposition 0322 and is not part of this tag.”. References: EGA IV (6.7.6), “separable ⇒ geom normal”.

> A separable field extension is geometrically normal: if `K/k` is a field extension all of whose
> finitely generated subextensions are separably generated (Definition 030O (2)), then `k' ⊗[k] K` is
> a normal ring for every field extension `k'/k`.

```lean
public theorem IsGeometricallyNormal.of_isSeparableExtension {k K : Type*} [Field k] [Field K]
    [Algebra k K] [IsSeparableExtension k K] : IsGeometricallyNormal k K
```

## Tag 06DF, a lemma

[Tag 06DF](https://stacks.math.columbia.edu/tag/06DF) in the Stacks Project.

**`Algebra.IsGeometricallyNormal.isNormalRing_tensorProduct_of_isNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyNormal/TensorProduct.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyNormal/TensorProduct.lean#L468). References: EGA IV (21.14.4), “special case”.

> **Stacks 06DF.** The tensor product over a field `k` of a geometrically normal `k`-algebra and
> a normal `k`-algebra is a normal ring.

```lean
theorem Algebra.IsGeometricallyNormal.isNormalRing_tensorProduct_of_isNormalRing (k : Type u)
    (A : Type v) (B : Type w) [Field k] [CommRing A] [CommRing B] [Algebra k A] [Algebra k B]
    [Algebra.IsGeometricallyNormal k A] (hB : IsNormalRing B) : IsNormalRing (A ⊗[k] B)
```

## Tag 0C31, a lemma

[Tag 0C31](https://stacks.math.columbia.edu/tag/0C31) in the Stacks Project.

**`Algebra.isGeometricallyNormal_iff_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyNormal/Separable.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyNormal/Separable.lean#L228). The attribute's comment: “Separable algebraic is Mathlib's `Algebra.IsSeparable k k'`, which includes algebraicity; the `k`-algebra structure of `A` is the restriction of its `k'`-algebra structure.”.

> **Stacks 0C31.** For a separable algebraic field extension `k'/k`, a `k'`-algebra `A` is
> geometrically normal over `k` if and only if it is geometrically normal over `k'`. Both directions
> are tested on finite purely inseparable extensions `L` (Lemma 037Z). Over `k'`, the ring
> `L ⊗[k'] A` is a localization of `L ⊗[k] A` (Lemma 0C2X). Over `k`, the ring `k' ⊗[k] L` is a field
> and `L ⊗[k] A = (k' ⊗[k] L) ⊗[k'] A`.

```lean
public theorem isGeometricallyNormal_iff_of_isSeparable (k k' A : Type*) [Field k] [Field k']
    [CommRing A] [Algebra k k'] [Algebra k A] [Algebra k' A] [IsScalarTower k k' A]
    [Algebra.IsSeparable k k'] : IsGeometricallyNormal k A ↔ IsGeometricallyNormal k' A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.165, Tag 037Y](https://stacks.math.columbia.edu/tag/037Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
