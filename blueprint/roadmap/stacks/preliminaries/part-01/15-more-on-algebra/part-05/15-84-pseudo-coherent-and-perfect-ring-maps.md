---
declaration: section
origin: cited
lean: Algebra.PseudoCoherent, Algebra.Perfect, Algebra.perfect_iff_pseudoCoherent_and_exists_flat_roof, Algebra.PseudoCoherent.of_finiteType, Algebra.Perfect.of_flat_of_finitePresentation, Algebra.Perfect.of_finiteType_of_isRegularRing, RingHom.IsLocalCompleteIntersection.perfect, PseudoCoherence.relativelyPseudoCoherent_iff_pseudoCoherent
statement: formalized
proof: formalized
---

# 15.84 Pseudo-coherent and perfect ring maps

Section 15.84 of the Stacks Project, [Tag 067G](https://stacks.math.columbia.edu/tag/067G). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 067H, a definition

[Tag 067H](https://stacks.math.columbia.edu/tag/067H) in the Stacks Project.

**`Algebra.PseudoCoherent`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean#L88). The attribute's comment: “(1)”.

> An `A`-algebra `B` is *pseudo-coherent* if `B` is a quotient `A[x₁, …, xₙ] ⧸ I` of a
> polynomial algebra such that the `A[x₁, …, xₙ]`-module `A[x₁, …, xₙ] ⧸ I` has a resolution by
> finite free modules.
>
> This is Stacks 067H (1) in the form of the remark that follows it, with `B` replaced by the
> isomorphic `A[x₁, …, xₙ]`-module `A[x₁, …, xₙ] ⧸ I`, which lives in the universe of `A`. By
> Stacks 0675 it says that `A → B` is of finite type and that `B`, as a module over itself, is
> pseudo-coherent relative to `A` (for `A` and `B` in one universe,
> `Algebra.pseudoCoherent_iff_exists_isModuleRelativelyPseudoCoherent`). The resolution then exists
> over every finite polynomial presentation
> (`Algebra.PseudoCoherent.nonempty_finiteFreeModuleResolution`). When `A` and `B` live in one
> universe, the condition is the same for `B` itself, made an `A[x₁, …, xₙ]`-module through the
> presentation (`Algebra.PseudoCoherent.nonempty_finiteFreeModuleResolution_quotient_iff_compHom`).

```lean
public class Algebra.PseudoCoherent (A : Type u) (B : Type v) [CommRing A] [CommRing B]
    [Algebra A B] : Prop
```

**`Algebra.Perfect`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean#L159). The attribute's comment: “(2)”. References: SGA 6 III (4.1), “affine case”.

> An `A`-algebra `B` is *perfect* if `B` is a quotient `A[x₁, …, xₙ] ⧸ I` of a polynomial
> algebra such that the `A[x₁, …, xₙ]`-module `A[x₁, …, xₙ] ⧸ I` has a resolution by finite free
> modules and finite projective dimension.
>
> This is Stacks 067H (2) in the form of Stacks 068Y, with `B` replaced by the isomorphic
> `A[x₁, …, xₙ]`-module `A[x₁, …, xₙ] ⧸ I`, which lives in the universe of `A`, as for
> `Algebra.PseudoCoherent`. The resolution by finite free modules is the field of
> `Algebra.PseudoCoherent`, and finite projective dimension is Mathlib's `HasProjectiveDimensionLE`.
> Stacks 067H (2) asks for `A → B` to be pseudo-coherent with `B` of finite Tor dimension as an
> `A`-module. Stacks 068Y is the comparison
> (`Algebra.perfect_iff_pseudoCoherent_and_exists_flat_roof`, where finite Tor dimension is a bounded
> complex of flat `A`-modules joined to `B[0]` by a roof of quasi-isomorphisms, Stacks 0654), and
> `Algebra.perfect_iff_pseudoCoherent_and_moduleHasFiniteTorDimension` reads it in any model of
> `D(A)`. When `A` and `B` live in one universe, `B` is perfect exactly when, for some presentation,
> `B` itself, made an `A[x₁, …, xₙ]`-module through it, has a finite resolution by finite projective
> modules, as Stacks 068Y words it (`Algebra.perfect_iff_exists_finite_projective_resolution`; with
> pseudo-coherence on the right-hand side,
> `Algebra.perfect_iff_pseudoCoherent_and_exists_finite_projective_resolution`).
>
> The terminology is that of Stacks and of SGA 6 (*morphisme parfait*); it is unrelated to perfect
> rings in the sense of `PerfectRing` (Frobenius).

```lean
public class Algebra.Perfect (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B] :
    Prop
```

## Tag 068Y, a lemma

[Tag 068Y](https://stacks.math.columbia.edu/tag/068Y) in the Stacks Project.

**`Algebra.perfect_iff_pseudoCoherent_and_exists_flat_roof`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/PerfectPresentation.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/PerfectPresentation.lean#L279).

> **Stacks 068Y.** An `A`-algebra `B` is perfect in the sense of `Algebra.Perfect` (a resolution
> by finite free modules and finite projective dimension over a polynomial presentation) exactly when
> it is perfect in the sense of Stacks 067H (2) as worded: pseudo-coherent, with `B` of finite Tor
> dimension as an `A`-module, read off a bounded complex of flat `A`-modules joined to `B[0]` by a
> roof of quasi-isomorphisms (Stacks 0654). The statement mentions no derived category. The forward
> direction restricts a finite resolution by finite projective modules over a polynomial algebra to
> `A`, reading no model; the reverse direction is Stacks 068X at a presentation, which reads
> Stacks 066Q and 065H in the standard model.

```lean
public theorem _root_.Algebra.perfect_iff_pseudoCoherent_and_exists_flat_roof {A B : Type u}
    [CommRing A] [CommRing B] [Algebra A B] :
    Algebra.Perfect A B ↔
      Algebra.PseudoCoherent A B ∧
        ∃ (a b : ℤ) (E : CochainComplex (ModuleCat.{u} A) ℤ), (∀ i, Module.Flat A (E.X i)) ∧
          E.IsStrictlyGE a ∧ E.IsStrictlyLE b ∧
            CochainComplex.QuasiIsoRoof E
              ((CochainComplex.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A B))
```

## Tag 067I, a lemma

[Tag 067I](https://stacks.math.columbia.edu/tag/067I) in the Stacks Project.

**`Algebra.PseudoCoherent.of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Noetherian.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/Noetherian.lean#L38). References: SGA 6 III (1.3), “third example, affine”.

> **Stacks 067I.** A finite-type ring map whose source is Noetherian is pseudo-coherent.

```lean
public theorem of_finiteType
    (A : Type u) (B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [Algebra.FiniteType A B] :
    Algebra.PseudoCoherent A B
```

## Tag 067J, a lemma

[Tag 067J](https://stacks.math.columbia.edu/tag/067J) in the Stacks Project.

**`Algebra.Perfect.of_flat_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/PerfectPresentation.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/PerfectPresentation.lean#L401).

> **Stacks 067J.** A flat algebra of finite presentation is perfect.
>
> `B` is isomorphic to the quotient of a polynomial algebra over `A` by the kernel of a presentation,
> which lives in the universe of `A`. That quotient is pseudo-coherent
> (`Algebra.PseudoCoherent.of_flat_of_finitePresentation`) and, being flat, is its own bounded flat
> roof, so it is perfect by Stacks 068Y; `Algebra.Perfect.equiv` carries this back to `B`.

```lean
public theorem _root_.Algebra.Perfect.of_flat_of_finitePresentation (A : Type u) (B : Type v)
    [CommRing A] [CommRing B] [Algebra A B] [Module.Flat A B] [Algebra.FinitePresentation A B] :
    Algebra.Perfect A B
```

## Tag 067K, a lemma

[Tag 067K](https://stacks.math.columbia.edu/tag/067K) in the Stacks Project.

**`Algebra.Perfect.of_finiteType_of_isRegularRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Regular.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/Regular.lean#L75).

> **Stacks 067K.** A finite-type algebra over a regular ring is perfect. It is a theorem and not
> an instance: with Stacks 0682 (a perfect algebra is of finite presentation) it would close an
> instance cycle.
>
> The source assumes in addition that the regular ring has finite Krull dimension; that hypothesis
> is not needed, because the bound on the length of the resolution is produced from
> quasi-compactness of the prime spectrum of the polynomial ring rather than from a bound on its
> global dimension.

```lean
public theorem of_finiteType_of_isRegularRing (A : Type u) (B : Type v) [CommRing A]
    [CommRing B] [Algebra A B] [IsRegularRing A] [Algebra.FiniteType A B] :
    Algebra.Perfect A B
```

## Tag 07EN, a lemma

[Tag 07EN](https://stacks.math.columbia.edu/tag/07EN) in the Stacks Project.

**`RingHom.IsLocalCompleteIntersection.perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/CompleteIntersection.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/CompleteIntersection.lean#L272). References: SGA 6 III (4.1.1), “second part, affine”; SGA 6 VIII (1.7), “affine case”.

> **Stacks 07EN.** A local complete intersection homomorphism is perfect.

```lean
public theorem IsLocalCompleteIntersection.perfect {A : Type u} {B : Type v} [CommRing A]
    [CommRing B] {f : A →+* B} (h : IsLocalCompleteIntersection f) : f.Perfect
```

## Tag 0DHQ, a lemma

[Tag 0DHQ](https://stacks.math.columbia.edu/tag/0DHQ) in the Stacks Project.

**`PseudoCoherence.relativelyPseudoCoherent_iff_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Absolute.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/Absolute.lean#L132).

> **Stacks 0DHQ.** Let `R → A` be a pseudo-coherent ring map. An object of `D(A)` is
> `m`-pseudo-coherent relative to `R` exactly when it is `m`-pseudo-coherent, and it is
> pseudo-coherent relative to `R` exactly when it is pseudo-coherent.

```lean
public theorem relativelyPseudoCoherent_iff_pseudoCoherent
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    (hRA : Algebra.PseudoCoherent R A)
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) :
    (IsRelativelyPseudoCoherentFrom (R := R) K m ↔ IsPseudoCoherentFrom K m) ∧
    (IsRelativelyPseudoCoherent (R := R) K ↔ IsPseudoCoherent K)
```

## Tag 0E1T, a lemma

[Tag 0E1T](https://stacks.math.columbia.edu/tag/0E1T) in the Stacks Project.

**`PseudoCoherence.pseudoCoherent_tfae_of_surjective_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Surjection.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/PseudoCoherentMap/Surjection.lean#L110). The attribute's comment: “item (3) relative to `B`; printed `A`, a typo, see errata.md”.

> **Stacks 0E1T.** Let `R → B → A` be ring maps with `B → A` surjective and `B`, `A` flat and of
> finite presentation over `R`, and let `K ∈ D(A)` with restriction `Kₑ ∈ D(B)`. Then `K` is
> pseudo-coherent, `K` is pseudo-coherent relative to `R`, `K` is pseudo-coherent relative to `B`,
> `Kₑ` is pseudo-coherent, and `Kₑ` is pseudo-coherent relative to `R` are equivalent; the same
> holds for `m`-pseudo-coherence. Item (3) is printed "relative to `A`" in the source, a typo for
> "relative to `B`" (the proof derives (3) ⇔ (4) from the definition using that `B → A` is
> surjective); see `errata.md`.

```lean
public theorem pseudoCoherent_tfae_of_surjective_base
    {R : Type u} {B : Type u} {A : Type u}
    [CommRing R] [CommRing B] [CommRing A]
    [Algebra R B] [Algebra B A] [Algebra R A] [IsScalarTower R B A]
    [Module.Flat R B] [Algebra.FinitePresentation R B]
    [Module.Flat R A] [Algebra.FinitePresentation R A]
    (hsurj : Function.Surjective (algebraMap B A))
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) :
    letI : Module.Finite B A := Module.Finite.of_surjective (Algebra.linearMap B A) hsurj
    let Kₑ := (ModuleCat.restrictScalars.{u} (algebraMap B A)).mapDerivedCategory.obj K
    List.TFAE [
      IsPseudoCoherent K,
      IsRelativelyPseudoCoherent (R := R) K,
      IsRelativelyPseudoCoherent (R := B) K,
      IsPseudoCoherent Kₑ,
      IsRelativelyPseudoCoherent (R := R) Kₑ] ∧
    List.TFAE [
      IsPseudoCoherentFrom K m,
      IsRelativelyPseudoCoherentFrom (R := R) K m,
      IsRelativelyPseudoCoherentFrom (R := B) K m,
      IsPseudoCoherentFrom Kₑ m,
      IsRelativelyPseudoCoherentFrom (R := R) Kₑ m]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.84, Tag 067G](https://stacks.math.columbia.edu/tag/067G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
