---
declaration: section
origin: cited
lean: PseudoCoherence.derivedTensorPolynomialEvalZeroIso, PseudoCoherence.isPseudoCoherentFrom_iff_restrictScalars_polynomial_evalZero, PseudoCoherence.isPseudoCoherentFrom_polynomialPresentation_independent, PseudoCoherence.IsRelativelyPseudoCoherentFrom, PseudoCoherence.IsRelativelyPseudoCoherent, PseudoCoherence.IsModuleRelativelyPseudoCoherentFrom, PseudoCoherence.IsModuleRelativelyPseudoCoherent, PseudoCoherence.isRelativelyPseudoCoherentFrom_and_isRelativelyPseudoCoherent_iff_restrictScalars
statement: formalized
proof: formalized
---

# 15.83 Relatively pseudo-coherent modules

Section 15.83 of the Stacks Project, [Tag 065E](https://stacks.math.columbia.edu/tag/065E). 17 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 065F, a lemma

[Tag 065F](https://stacks.math.columbia.edu/tag/065F) in the Stacks Project.

**`PseudoCoherence.derivedTensorPolynomialEvalZeroIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/PolynomialRetract.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/PolynomialRetract.lean#L330).

> **Stacks 065F.** If `R[X] → R` evaluates `X` at zero, then for every `K ∈ D(R)`,
> the derived tensor product of `K`, regarded as an `R[X]`-complex, with `R` is isomorphic in
> `D(R)` to `K ⊞ K[1]`.

```lean
public theorem derivedTensorPolynomialEvalZeroIso
    {R : Type u} [CommRing R]
    (D : KFlatDerivedTensoringDatum (Polynomial R))
    (K : DerivedCategory (ModuleCat.{u} R)) :
    let ev : Polynomial R →+* R := Polynomial.eval₂RingHom (RingHom.id R) 0
    letI : Module (Polynomial R) R := ev.toAlgebra.toModule
    Nonempty
      ((ModuleCat.restrictScalars
          (Polynomial.C : R →+* Polynomial R)).mapDerivedCategory.obj
            ((D.tensor.obj ((ModuleCat.restrictScalars ev).mapDerivedCategory.obj K)).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} (Polynomial R)) 0).obj
                (ModuleCat.of (Polynomial R) R))) ≅
        Limits.biprod K
          ((shiftFunctor (DerivedCategory (ModuleCat.{u} R)) (1 : ℤ)).obj K))
```

## Tag 065G, a lemma

[Tag 065G](https://stacks.math.columbia.edu/tag/065G) in the Stacks Project.

**`PseudoCoherence.isPseudoCoherentFrom_iff_restrictScalars_polynomial_evalZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Polynomial.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Polynomial.lean#L208).

> **Stacks 065G.** An object of `D(R)` is `m`-pseudo-coherent over `R` if and only if,
> after letting `X` act by zero, it is `m`-pseudo-coherent over `R[X]`.
>
> For an object represented by a complex, `Functor.mapDerivedCategoryFactors` identifies the
> right-hand object with the localization of that complex after restriction of scalars.

```lean
public theorem isPseudoCoherentFrom_iff_restrictScalars_polynomial_evalZero
    {R : Type u} [CommRing R]
    (K : DerivedCategory (ModuleCat.{max u v} R)) (m : ℤ) :
    let ev : Polynomial R →+* R := Polynomial.eval₂RingHom (RingHom.id R) (0 : R)
    IsPseudoCoherentFrom K m ↔
      IsPseudoCoherentFrom
        ((ModuleCat.restrictScalars.{max u v} ev).mapDerivedCategory.obj K) m
```

## Tag 065H, a lemma

[Tag 065H](https://stacks.math.columbia.edu/tag/065H) in the Stacks Project.

**`PseudoCoherence.isPseudoCoherentFrom_polynomialPresentation_independent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Presentation.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Presentation.lean#L224).

> **Stacks 065H.** For a finite-type `R`-algebra `A`, `m`-pseudo-coherence of an object of
> `D(A)` after restriction to a finite polynomial presentation is independent of the presentation.
> The same is true of pseudo-coherence. For an object represented by a complex,
> `Functor.mapDerivedCategoryFactors` identifies each restricted object below with the localization
> of the representing complex after degreewise restriction of scalars.

```lean
public theorem isPseudoCoherentFrom_polynomialPresentation_independent
    {R : Type u} {A : Type w} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (K : DerivedCategory (ModuleCat.{max u v} A)) (m : ℤ) :
    ((∃ (n : ℕ) (α : MvPolynomial (Fin n) R →ₐ[R] A), Function.Surjective α ∧
        IsPseudoCoherentFrom
          ((ModuleCat.restrictScalars.{max u v} α.toRingHom).mapDerivedCategory.obj K) m) ↔
      ∀ (n : ℕ) (α : MvPolynomial (Fin n) R →ₐ[R] A), Function.Surjective α →
        IsPseudoCoherentFrom
          ((ModuleCat.restrictScalars.{max u v} α.toRingHom).mapDerivedCategory.obj K) m) ∧
    ((∃ (n : ℕ) (α : MvPolynomial (Fin n) R →ₐ[R] A), Function.Surjective α ∧
        IsPseudoCoherent
          ((ModuleCat.restrictScalars.{max u v} α.toRingHom).mapDerivedCategory.obj K)) ↔
      ∀ (n : ℕ) (α : MvPolynomial (Fin n) R →ₐ[R] A), Function.Surjective α →
        IsPseudoCoherent
          ((ModuleCat.restrictScalars.{max u v} α.toRingHom).mapDerivedCategory.obj K))
```

## Tag 065I, a definition

[Tag 065I](https://stacks.math.columbia.edu/tag/065I) in the Stacks Project.

**`PseudoCoherence.IsRelativelyPseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean#L84). The attribute's comment: “(1)”.

> **Stacks 065I (1).** An object of `D(A)` is `m`-pseudo-coherent relative to `R` if its
> restriction of scalars along every finite polynomial presentation of `A` over `R` is
> `m`-pseudo-coherent. By Stacks 065H it is equivalent to require this of one presentation.

```lean
public def IsRelativelyPseudoCoherentFrom
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) : Prop
```

**`PseudoCoherence.IsRelativelyPseudoCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean#L94). The attribute's comment: “(2)”.

> **Stacks 065I (2).** An object of `D(A)` is pseudo-coherent relative to `R` if it is
> `m`-pseudo-coherent relative to `R` for every integer `m`.

```lean
public def IsRelativelyPseudoCoherent
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (K : DerivedCategory (ModuleCat.{u} A)) : Prop
```

**`PseudoCoherence.IsModuleRelativelyPseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean#L102). The attribute's comment: “(3)”.

> **Stacks 065I (3).** An `A`-module is `m`-pseudo-coherent relative to `R` if the object
> concentrated in degree zero that it determines has that property.

```lean
public def IsModuleRelativelyPseudoCoherentFrom
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (M : Type u) [AddCommGroup M] [Module A M] (m : ℤ) : Prop
```

**`PseudoCoherence.IsModuleRelativelyPseudoCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Defs.lean#L111). The attribute's comment: “(4)”.

> **Stacks 065I (4).** An `A`-module is pseudo-coherent relative to `R` if the object
> concentrated in degree zero that it determines has that property.

```lean
public def IsModuleRelativelyPseudoCoherent
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (M : Type u) [AddCommGroup M] [Module A M] : Prop
```

## Tag 0673, a lemma

[Tag 0673](https://stacks.math.columbia.edu/tag/0673) in the Stacks Project.

**`PseudoCoherence.isRelativelyPseudoCoherentFrom_and_isRelativelyPseudoCoherent_iff_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Finite.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Finite.lean#L237).

> **Stacks 0673.** Restriction of scalars along a finite map of finite-type `R`-algebras
> preserves and reflects relative `m`-pseudo-coherence and relative pseudo-coherence.

```lean
public theorem isRelativelyPseudoCoherentFrom_and_isRelativelyPseudoCoherent_iff_restrictScalars
    {R : Type u} {A : Type u} {B : Type u} [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra R B] [Algebra A B] [IsScalarTower R A B]
    [Algebra.FiniteType R A] [Module.Finite A B]
    (K : DerivedCategory (ModuleCat.{u} B)) (m : ℤ) :
    letI : Algebra.FiniteType R B :=
      Algebra.FiniteType.trans (inferInstance : Algebra.FiniteType R A)
        (Module.Finite.finiteType B)
    let Kₐ := (ModuleCat.restrictScalars.{u} (algebraMap A B)).mapDerivedCategory.obj K
    (IsRelativelyPseudoCoherentFrom (R := R) K m ↔
      IsRelativelyPseudoCoherentFrom (R := R) Kₐ m) ∧
    (IsRelativelyPseudoCoherent (R := R) K ↔
      IsRelativelyPseudoCoherent (R := R) Kₐ)
```

## Tag 0674, a lemma

[Tag 0674](https://stacks.math.columbia.edu/tag/0674) in the Stacks Project.

**`PseudoCoherence.isRelativelyPseudoCoherent_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Triangle.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Triangle.lean#L47).

> **Stacks 0674.** Relative pseudo-coherence is preserved around a distinguished triangle,
> with the indicated shift in the degree bound. Without a degree bound it is a two-out-of-three
> property.

```lean
public theorem isRelativelyPseudoCoherent_of_distinguished
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (m : ℤ)
    (T : Triangle (DerivedCategory (ModuleCat.{u} A)))
    (hT : T ∈ distinguishedTriangles) :
    ((IsRelativelyPseudoCoherentFrom (R := R) T.obj₁ (m + 1) →
        IsRelativelyPseudoCoherentFrom (R := R) T.obj₂ m →
        IsRelativelyPseudoCoherentFrom (R := R) T.obj₃ m) ∧
      (IsRelativelyPseudoCoherentFrom (R := R) T.obj₁ m →
        IsRelativelyPseudoCoherentFrom (R := R) T.obj₃ m →
        IsRelativelyPseudoCoherentFrom (R := R) T.obj₂ m) ∧
      (IsRelativelyPseudoCoherentFrom (R := R) T.obj₂ (m + 1) →
        IsRelativelyPseudoCoherentFrom (R := R) T.obj₃ m →
        IsRelativelyPseudoCoherentFrom (R := R) T.obj₁ (m + 1))) ∧
    ((IsRelativelyPseudoCoherent (R := R) T.obj₁ →
        IsRelativelyPseudoCoherent (R := R) T.obj₂ →
        IsRelativelyPseudoCoherent (R := R) T.obj₃) ∧
      (IsRelativelyPseudoCoherent (R := R) T.obj₁ →
        IsRelativelyPseudoCoherent (R := R) T.obj₃ →
        IsRelativelyPseudoCoherent (R := R) T.obj₂) ∧
      (IsRelativelyPseudoCoherent (R := R) T.obj₂ →
        IsRelativelyPseudoCoherent (R := R) T.obj₃ →
        IsRelativelyPseudoCoherent (R := R) T.obj₁))
```

## Tag 0675, a lemma

[Tag 0675](https://stacks.math.columbia.edu/tag/0675) in the Stacks Project.

**`PseudoCoherence.moduleRelativelyPseudoCoherent_iff_finiteness_and_resolutions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Module.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Module.lean#L197).

> **Stacks 0675.** For a module over a finite-type `R`-algebra, relative
> pseudo-coherence in degrees `0`, `-1`, and `-d` is equivalent respectively to finite
> generation, relative finite presentation, and the existence over every polynomial presentation
> of a finite free resolution through degree `d`. Relative pseudo-coherence is equivalent to the
> existence over every polynomial presentation of an infinite finite free resolution.

```lean
public theorem moduleRelativelyPseudoCoherent_iff_finiteness_and_resolutions
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (M : Type u) [AddCommGroup M] [Module A M] :
    (IsModuleRelativelyPseudoCoherentFrom (R := R) (A := A) M 0 ↔
      Module.Finite A M) ∧
    (IsModuleRelativelyPseudoCoherentFrom (R := R) (A := A) M (-1) ↔
      Module.FinitePresentationRel R A M) ∧
    (∀ d : ℕ, IsModuleRelativelyPseudoCoherentFrom (R := R) (A := A)
      M (-(d : ℤ)) ↔
      ∀ (n : ℕ) (α : MvPolynomial (Fin n) R →ₐ[R] A), Function.Surjective α →
        @HasFiniteFreeResolutionOfLength _ _ M _
          (Module.compHom M α.toRingHom) d) ∧
    (IsModuleRelativelyPseudoCoherent (R := R) (A := A) M ↔
      ∀ (n : ℕ) (α : MvPolynomial (Fin n) R →ₐ[R] A), Function.Surjective α →
        Nonempty (@FiniteFreeModuleResolution _ _ M _
          (Module.compHom M α.toRingHom)))
```

## Tag 0676, a lemma

[Tag 0676](https://stacks.math.columbia.edu/tag/0676) in the Stacks Project.

**`PseudoCoherence.isRelativelyPseudoCoherentFrom_and_isRelativelyPseudoCoherent_of_biproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Summand.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Summand.lean#L42).

> Each summand of a relatively `m`-pseudo-coherent binary biproduct is
> relatively `m`-pseudo-coherent, and each summand of a relatively pseudo-coherent binary
> biproduct is relatively pseudo-coherent.

```lean
public theorem isRelativelyPseudoCoherentFrom_and_isRelativelyPseudoCoherent_of_biproduct
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (K L : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) :
    (IsRelativelyPseudoCoherentFrom (R := R) (K ⊞ L) m →
      IsRelativelyPseudoCoherentFrom (R := R) K m ∧
        IsRelativelyPseudoCoherentFrom (R := R) L m) ∧
    (IsRelativelyPseudoCoherent (R := R) (K ⊞ L) →
      IsRelativelyPseudoCoherent (R := R) K ∧
        IsRelativelyPseudoCoherent (R := R) L)
```

## Tag 0677, a lemma

[Tag 0677](https://stacks.math.columbia.edu/tag/0677) in the Stacks Project.

**`PseudoCoherence.relativelyPseudoCoherentFrom_and_relativelyPseudoCoherent_of_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/BoundedAbove.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/BoundedAbove.lean#L49).

> **Stacks 0677.** A bounded-above complex with suitably relatively pseudo-coherent terms is
> relatively pseudo-coherent in the corresponding degrees. In particular, relative
> pseudo-coherence of every term implies relative pseudo-coherence of the complex.

```lean
public theorem relativelyPseudoCoherentFrom_and_relativelyPseudoCoherent_of_boundedAbove
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (K : CochainComplex (ModuleCat.{u} A) ℤ)
    (hK : ∃ b : ℤ, K.IsStrictlyLE b) :
    (∀ m : ℤ,
      (∀ i : ℤ, IsModuleRelativelyPseudoCoherentFrom (R := R) (A := A) (K.X i) (m - i)) →
        IsRelativelyPseudoCoherentFrom (R := R) (DerivedCategory.Q.obj K) m) ∧
    ((∀ i : ℤ, IsModuleRelativelyPseudoCoherent (R := R) (A := A) (K.X i)) →
      IsRelativelyPseudoCoherent (R := R) (DerivedCategory.Q.obj K))
```

## Tag 0678, a lemma

[Tag 0678](https://stacks.math.columbia.edu/tag/0678) in the Stacks Project.

**`PseudoCoherence.relativelyPseudoCoherent_of_boundedAbove_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/BoundedAboveCohomology.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/BoundedAboveCohomology.lean#L91).

> **Stacks 0678.** A cohomologically bounded-above derived object whose cohomology modules
> are relatively pseudo-coherent in the corresponding degrees is relatively pseudo-coherent.

```lean
public theorem relativelyPseudoCoherent_of_boundedAbove_cohomology
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [Algebra.FiniteType R A] (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ)
    (hK : ∃ b : ℤ, ∀ i : ℤ, b < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj K)) :
    ((∀ i : ℤ, IsModuleRelativelyPseudoCoherentFrom (R := R) (A := A)
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj K) (m - i)) →
      IsRelativelyPseudoCoherentFrom (R := R) K m) ∧
    ((∀ i : ℤ, IsModuleRelativelyPseudoCoherent (R := R) (A := A)
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj K)) →
      IsRelativelyPseudoCoherent (R := R) K)
```

## Tag 0679, a lemma

[Tag 0679](https://stacks.math.columbia.edu/tag/0679) in the Stacks Project.

**`PseudoCoherence.localization_preserves_relativePseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Localization.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Localization.lean#L510).

> **Stacks 0679.** Localizing a complex that is relatively `m`-pseudo-coherent, respectively
> pseudo-coherent, over `R_f` produces a complex with the corresponding property relative to
> `R`.

```lean
public theorem localization_preserves_relativePseudoCoherent
    {R : Type u} {Rf : Type u} {A : Type u} {Ag : Type u}
    [CommRing R] [CommRing Rf] [CommRing A] [CommRing Ag]
    [Algebra R Rf] (f : R) [IsLocalization.Away f Rf]
    [Algebra Rf A] [Algebra.FiniteType Rf A]
    [Algebra R A] [IsScalarTower R Rf A]
    (g : A) [Algebra A Ag] [IsLocalization.Away g Ag]
    [Algebra R Ag] [IsScalarTower R A Ag]
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) :
    letI : Algebra.FiniteType R Rf :=
      IsLocalization.finiteType_of_monoid_fg (Submonoid.powers f) Rf
    letI : Algebra.FiniteType R A := Algebra.FiniteType.trans
      (inferInstance : Algebra.FiniteType R Rf) (inferInstance : Algebra.FiniteType Rf A)
    letI : Algebra.FiniteType A Ag :=
      IsLocalization.finiteType_of_monoid_fg (Submonoid.powers g) Ag
    letI : Algebra.FiniteType R Ag := Algebra.FiniteType.trans
      (inferInstance : Algebra.FiniteType R A) (inferInstance : Algebra.FiniteType A Ag)
    (IsRelativelyPseudoCoherentFrom (R := Rf) K m →
      IsRelativelyPseudoCoherentFrom (R := R)
        ((derivedExtensionScalarsGeneral.{u, u, u} (algebraMap A Ag)).functor.obj K) m) ∧
    (IsRelativelyPseudoCoherent (R := Rf) K →
      IsRelativelyPseudoCoherent (R := R)
        ((derivedExtensionScalarsGeneral.{u, u, u} (algebraMap A Ag)).functor.obj
          K))
```

## Tag 067A, a lemma

[Tag 067A](https://stacks.math.columbia.edu/tag/067A) in the Stacks Project.

**`PseudoCoherence.derivedExtensionScalars_preserves_relativelyPseudoCoherent_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/TorIndependentBaseChange.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/TorIndependentBaseChange.lean#L271). References: SGA 6 III (1.10), “a), affine case”; SGA 6 III (1.8), “affine, E₂ = O”; SGA 6 III (4.7), “(a), special case”.

> A Tor-independent base change preserves relative `m`-pseudo-coherence for every integer `m`,
> as well as relative pseudo-coherence.
>
> The chosen `R'`-algebra `R' ⊗[R] A` is identified with the source's `A ⊗[R] R'` by
> `Algebra.TensorProduct.commRight R R' A`.

```lean
public theorem derivedExtensionScalars_preserves_relativelyPseudoCoherent_of_torIndependent
    {R : Type u} {A : Type u} {R' : Type u}
    [CommRing R] [CommRing A] [CommRing R']
    [Algebra R A] [Algebra R R'] [Algebra.FiniteType R A]
    (K : DerivedCategory (ModuleCat.{u} A))
    (hTor : TorIndependent R A R') :
    let A' := R' ⊗[R] A
    letI : Algebra R' A' := Algebra.TensorProduct.leftAlgebra
    let f : A →+* A' := Algebra.TensorProduct.includeRight.toRingHom
    (∀ m : ℤ, IsRelativelyPseudoCoherentFrom (R := R) K m →
      IsRelativelyPseudoCoherentFrom (R := R')
        ((derivedExtensionScalarsGeneral.{u, u, u} f).functor.obj K)
          m) ∧
      (IsRelativelyPseudoCoherent (R := R) K →
        IsRelativelyPseudoCoherent (R := R')
          ((derivedExtensionScalarsGeneral.{u, u, u} f).functor.obj
            K))
```

## Tag 067B, a lemma

[Tag 067B](https://stacks.math.columbia.edu/tag/067B) in the Stacks Project.

**`PseudoCoherence.derivedExtensionScalars_preserves_relativelyPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Tower.lean, line 944](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Tower.lean#L944).

> If `B` is pseudo-coherent relative to `A`, derived extension of scalars from `A` to `B`
> preserves relative `m`-pseudo-coherence and relative pseudo-coherence over the base ring `R`.

```lean
public theorem derivedExtensionScalars_preserves_relativelyPseudoCoherent
    {R : Type u} {A : Type u} {B : Type u}
    [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra A B] [Algebra R B] [IsScalarTower R A B]
    [Algebra.FiniteType R A] [Algebra.FiniteType A B]
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ)
    (hB : IsModuleRelativelyPseudoCoherent.{u}
      (R := A) (A := B) B) :
    letI : Algebra.FiniteType R B :=
      Algebra.FiniteType.trans (R := R) (S := A) (A := B) inferInstance inferInstance
    (IsRelativelyPseudoCoherentFrom (R := R) K m →
      IsRelativelyPseudoCoherentFrom (R := R)
        ((derivedExtensionScalars hB).obj K) m) ∧
    (IsRelativelyPseudoCoherent (R := R) K →
      IsRelativelyPseudoCoherent (R := R)
        ((derivedExtensionScalars hB).obj K))
```

## Tag 067C, a lemma

[Tag 067C](https://stacks.math.columbia.edu/tag/067C) in the Stacks Project.

**`PseudoCoherence.tensorProduct_preserves_relativelyPseudoCoherent_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/TowerModule.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/TowerModule.lean#L128).

> Flat extension of scalars preserves relative `m`-pseudo-coherence and relative
> pseudo-coherence for modules.

```lean
public theorem tensorProduct_preserves_relativelyPseudoCoherent_of_flat
    {R : Type u} {A : Type u} {B : Type u}
    [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra A B] [Algebra R B] [IsScalarTower R A B]
    [Algebra.FiniteType R A] [Algebra.FiniteType A B]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Flat A B] (m : ℤ)
    (hB : IsModuleRelativelyPseudoCoherent (R := A) (A := B) B) :
    letI : Algebra.FiniteType R B :=
      Algebra.FiniteType.trans (R := R) (S := A) (A := B) inferInstance inferInstance
    (IsModuleRelativelyPseudoCoherentFrom (R := R) (A := A) M m →
      IsModuleRelativelyPseudoCoherentFrom (R := R) (A := B)
        (TensorProduct A B M) m) ∧
    (IsModuleRelativelyPseudoCoherent (R := R) (A := A) M →
      IsModuleRelativelyPseudoCoherent (R := R) (A := B)
        (TensorProduct A B M))
```

## Tag 067D, a lemma

[Tag 067D](https://stacks.math.columbia.edu/tag/067D) in the Stacks Project.

**`PseudoCoherence.relativelyPseudoCoherent_iff_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Composition.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Composition.lean#L258). References: SGA 6 I (2.14), “(ii), affine case”.

> **Stacks 067D.** Relative pseudo-coherence is invariant under composition with a relatively
> pseudo-coherent finite-type algebra, for every object of the derived category.

```lean
public theorem relativelyPseudoCoherent_iff_of_comp
    {R : Type u} {A : Type u} {B : Type u}
    [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra A B] [Algebra R B] [IsScalarTower R A B]
    [Algebra.FiniteType R A] [Algebra.FiniteType A B]
    (hA : IsModuleRelativelyPseudoCoherent (R := R) (A := A) A)
    (K : DerivedCategory (ModuleCat.{u} B)) (m : ℤ) :
    letI : Algebra.FiniteType R B :=
      Algebra.FiniteType.trans (R := R) (S := A) (A := B) inferInstance inferInstance
    (IsRelativelyPseudoCoherentFrom (R := A) K m ↔
      IsRelativelyPseudoCoherentFrom (R := R) K m) ∧
    (IsRelativelyPseudoCoherent (R := A) K ↔
      IsRelativelyPseudoCoherent (R := R) K)
```

## Tag 067E, a lemma

[Tag 067E](https://stacks.math.columbia.edu/tag/067E) in the Stacks Project.

**`PseudoCoherence.relativelyPseudoCoherent_iff_localizationAway_of_span_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Locality.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Locality.lean#L563).

> **Stacks 067E.** Relative `m`-pseudo-coherence and relative pseudo-coherence are local on
> a finite principal cover of a finite-type algebra.

```lean
public theorem relativelyPseudoCoherent_iff_localizationAway_of_span_eq_top
    {R : Type u} {A : Type u} [CommRing R] [CommRing A]
    [Algebra R A] [Algebra.FiniteType R A]
    {ι : Type*} [Finite ι] (f : ι → A) (hf : Ideal.span (Set.range f) = ⊤)
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) :
    ((∀ i,
      letI : Algebra.FiniteType A (Localization.Away (f i)) :=
        IsLocalization.finiteType_of_monoid_fg (Submonoid.powers (f i)) _
      letI : Algebra.FiniteType R (Localization.Away (f i)) :=
        Algebra.FiniteType.trans (R := R) (S := A)
          (A := Localization.Away (f i)) inferInstance inferInstance
      IsRelativelyPseudoCoherentFrom (R := R)
        ((localizationAwayFunctorAux.{u, u} (f i)).obj K) m) ↔
      IsRelativelyPseudoCoherentFrom (R := R) K m) ∧
    ((∀ i,
      letI : Algebra.FiniteType A (Localization.Away (f i)) :=
        IsLocalization.finiteType_of_monoid_fg (Submonoid.powers (f i)) _
      letI : Algebra.FiniteType R (Localization.Away (f i)) :=
        Algebra.FiniteType.trans (R := R) (S := A)
          (A := Localization.Away (f i)) inferInstance inferInstance
      IsRelativelyPseudoCoherent (R := R)
        ((localizationAwayFunctorAux.{u, u} (f i)).obj K)) ↔
      IsRelativelyPseudoCoherent (R := R) K)
```

## Tag 067F, a lemma

[Tag 067F](https://stacks.math.columbia.edu/tag/067F) in the Stacks Project.

**`PseudoCoherence.relativePseudoCoherent_iff_boundedAbove_finite_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/Relative/Noetherian.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/PseudoCoherent/Relative/Noetherian.lean#L147).

> **Stacks 067F.** For a finite-type algebra over a Noetherian ring, relative
> pseudo-coherence from degree `m` means bounded-above finite homology in degrees at least `m`;
> relative pseudo-coherence means bounded-above finite homology in every degree; and relative
> pseudo-coherence of a module is equivalent to its finiteness.

```lean
public theorem relativePseudoCoherent_iff_boundedAbove_finite_homology
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    [IsNoetherianRing R] [Algebra.FiniteType R A]
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ)
    (M : Type u) [AddCommGroup M] [Module A M] :
    (IsRelativelyPseudoCoherentFrom (R := R) K m ↔
      (∃ b : ℤ, ∀ i : ℤ, b < i →
        IsZero ((DerivedCategory.homologyFunctor
          (ModuleCat.{u} A) i).obj K)) ∧
      ∀ i : ℤ, m ≤ i →
        Module.Finite A ((DerivedCategory.homologyFunctor
          (ModuleCat.{u} A) i).obj K)) ∧
    (IsRelativelyPseudoCoherent (R := R) K ↔
      (∃ b : ℤ, ∀ i : ℤ, b < i →
        IsZero ((DerivedCategory.homologyFunctor
          (ModuleCat.{u} A) i).obj K)) ∧
      ∀ i : ℤ,
        Module.Finite A ((DerivedCategory.homologyFunctor
          (ModuleCat.{u} A) i).obj K)) ∧
    (IsModuleRelativelyPseudoCoherent (R := R) (A := A) M ↔
      Module.Finite A M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.83, Tag 065E](https://stacks.math.columbia.edu/tag/065E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
