---
declaration: section
origin: cited
lean: Module.finitePresentationRel_tfae, Module.FinitePresentationRel.finitePresentation, Module.FinitePresentationRel, Module.finitePresentationRel_iff_of_finite, Module.finitePresentationRel_away_of_away, finitePresentation_relative_baseChange, finitelyPresentedRelative_baseChange, Module.finitePresentationRel_comp
statement: formalized
proof: formalized
---

# 15.82 Relatively finitely presented modules

Section 15.82 of the Stacks Project, [Tag 0659](https://stacks.math.columbia.edu/tag/0659). 10 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05GY, a lemma

[Tag 05GY](https://stacks.math.columbia.edu/tag/05GY) in the Stacks Project.

**`Module.finitePresentationRel_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean#L117).

> Stacks 05GY: for an `A`-module `M` over a finite type ring map `R → A`, the three
> conditions "some presentation", "all presentations" and "all finitely presented covers" are
> equivalent.

```lean
theorem Module.finitePresentationRel_tfae [Algebra.FiniteType R A] :
    [Module.FinitePresentationRel R A M,
     Module.FinitePresentationRel.AllPresentations R A M,
     Module.FinitePresentationRel.AllFPCovers.{u} R A M].TFAE
```

**`Module.FinitePresentationRel.finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/Relative.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/Relative.lean#L129). The attribute's comment: “the final conclusion, that a module finitely presented relative to R is a finitely presented A-module”.

> A module finitely presented relative to `R` is a finitely presented `A`-module.

```lean
theorem Module.FinitePresentationRel.finitePresentation
    (h : Module.FinitePresentationRel R A M) : Module.FinitePresentation A M
```

## Tag 05GZ, a definition

[Tag 05GZ](https://stacks.math.columbia.edu/tag/05GZ) in the Stacks Project.

**`Module.FinitePresentationRel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/Relative.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/Relative.lean#L40).

> `M` is *finitely presented relative to `R`*: for some surjective `R`-algebra map
> `α : R[x_1, …, x_n] → A`, the module `M` viewed over `R[x_1, …, x_n]` via `α` is finitely
> presented.

```lean
def Module.FinitePresentationRel (R A : Type*) [CommRing R] [CommRing A] [Algebra R A]
    (M : Type*) [AddCommGroup M] [Module A M] : Prop
```

## Tag 05H0, a lemma

[Tag 05H0](https://stacks.math.columbia.edu/tag/05H0) in the Stacks Project.

**`Module.finitePresentationRel_iff_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Finite.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Finite.lean#L297).

> **Stacks Tag 05H0 (Lemma 15.82.3).** Let `R` be a ring, `φ : A → B` a finite
> map of `R`-algebras with both `R → A` and `R → B` of finite type, and `M` a
> `B`-module (hence an `A`-module via `φ`). Then `M` is finitely presented
> relative to `R` as an `A`-module iff it is finitely presented relative to `R`
> as a `B`-module.
>
> The hypothesis `[IsScalarTower R A B]` encodes that `A → B` is a map of
> `R`-algebras; `[IsScalarTower A B M]` encodes that the `A`-module structure on
> `M` is the one obtained by restriction of scalars along `φ : A → B`.

```lean
theorem Module.finitePresentationRel_iff_of_finite
    (R A B : Type*) [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra R B] [Algebra A B] [IsScalarTower R A B]
    [Algebra.FiniteType R A] [Algebra.FiniteType R B] [Module.Finite A B]
    (M : Type*) [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M] :
    Module.FinitePresentationRel R A M ↔ Module.FinitePresentationRel R B M
```

## Tag 065A, a lemma

[Tag 065A](https://stacks.math.columbia.edu/tag/065A) in the Stacks Project.

**`Module.finitePresentationRel_away_of_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Localization.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Localization.lean#L74).

> Let `A` be a finite type algebra over a localization `R_f`, and let `M` be an `A`-module
> finitely presented relative to `R_f`. For `g : A` the localized module `M_g` over `A_g` is
> finitely presented relative to `R`. The composite `R → R_f → A` is given by an `Algebra R A`
> instance together with the scalar tower `R → R_f → A`.

```lean
theorem finitePresentationRel_away_of_away {R : Type u} [CommRing R] (f : R) {A : Type v}
    [CommRing A] [Algebra (Localization.Away f) A] [Algebra R A]
    [IsScalarTower R (Localization.Away f) A]
    [Algebra.FiniteType (Localization.Away f) A] (g : A) {M : Type w} [AddCommGroup M]
    [Module A M] (hM : Module.FinitePresentationRel (Localization.Away f) A M) :
    Module.FinitePresentationRel R (Localization.Away g) (LocalizedModule.Away g M)
```

## Tag 065B, a lemma

[Tag 065B](https://stacks.math.columbia.edu/tag/065B) in the Stacks Project.

**`finitePresentation_relative_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/BaseChange.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/BaseChange.lean#L90). References: EGA IV (1.3.1); EGA IV (1.4.1), “more general”.

> Let `R → A` be a finite type ring map and `M` an `A`-module finitely presented relative
> to `R`. For any ring map `R → R'`, set
> `A' := A ⊗[R] R'` (an `R'`-algebra via the right factor and, canonically, an `A`-algebra via
> the left factor) and `M' := A' ⊗[A] M` (an `A'`-module via the left tensor factor `A'`). Then
> `R' → A'` is of finite type, and `M'` is finitely presented relative to `R'`.

```lean
theorem finitePresentation_relative_baseChange (R A R' M : Type*)
    [CommRing R] [CommRing A] [CommRing R'] [Algebra R A] [Algebra R R']
    [AddCommGroup M] [Module A M] [Algebra.FiniteType R A]
    (hM : Module.FinitePresentationRel R A M) :
    letI : Algebra R' (TensorProduct R A R') := Algebra.TensorProduct.rightAlgebra
    letI : Algebra A (TensorProduct R A R') := Algebra.TensorProduct.leftAlgebra
    Algebra.FiniteType R' (TensorProduct R A R') ∧
    Module.FinitePresentationRel R' (TensorProduct R A R')
      (TensorProduct A (TensorProduct R A R') M)
```

## Tag 0670, a lemma

[Tag 0670](https://stacks.math.columbia.edu/tag/0670) in the Stacks Project.

**`finitelyPresentedRelative_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/BaseChange.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/BaseChange.lean#L358). References: EGA IV (1.4.1), “more general”.

> Let `R → A` be a ring map, `M` an `A`-module finitely presented relative to `R`, and
> `A → A'` a ring map of finite presentation. Then the `A'`-module `A' ⊗[A] M` (here
> `TensorProduct A A' M`, with its natural `A'`-module structure) is finitely presented relative
> to `R`.
>
> The finite type hypothesis on `R → A` of the Stacks statement is not needed.

```lean
theorem finitelyPresentedRelative_baseChange
    (R A A' : Type*) [CommRing R] [CommRing A] [CommRing A']
    [Algebra R A] [Algebra A A'] [Algebra R A'] [IsScalarTower R A A']
    (M : Type*) [AddCommGroup M] [Module A M]
    (hM : Module.FinitePresentationRel R A M)
    [Algebra.FinitePresentation A A'] :
    Module.FinitePresentationRel R A' (TensorProduct A A' M)
```

## Tag 065C, a lemma

[Tag 065C](https://stacks.math.columbia.edu/tag/065C) in the Stacks Project.

**`Module.finitePresentationRel_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean#L156).

> Stacks 065C, Lemma 15.82.7. Given finite type ring maps `R → A` and `A → B` and a
> `B`-module `M`, if `M` is finitely presented relative to `A` and `A` is of finite presentation
> over `R`, then `M` is finitely presented relative to `R`.

```lean
theorem Module.finitePresentationRel_comp {R A B : Type*} [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra A B] [Algebra R B] [IsScalarTower R A B]
    [Algebra.FinitePresentation R A] {M : Type*} [AddCommGroup M] [Module B M]
    (hM : Module.FinitePresentationRel A B M) : Module.FinitePresentationRel R B M
```

## Tag 065D, a lemma

[Tag 065D](https://stacks.math.columbia.edu/tag/065D) in the Stacks Project.

**`Module.finitePresentationRel_iff_of_span_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Localization.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Localization.lean#L175).

> Relative finite presentation of a module over a finite type algebra can be checked on a
> finite family of principal opens covering the spectrum: if `f : ι → A` generates the unit ideal,
> then `M` is finitely presented relative to `R` exactly when each `M_{f i}` is finitely presented
> relative to `R` over `A_{f i}`.

```lean
theorem finitePresentationRel_iff_of_span_eq_top {R : Type u} [CommRing R] {A : Type v}
    [CommRing A] [Algebra R A] [Algebra.FiniteType R A] {M : Type w} [AddCommGroup M]
    [Module A M] {ι : Type x} [Finite ι] (f : ι → A) (hf : Ideal.span (Set.range f) = ⊤) :
    (∀ i, Module.FinitePresentationRel R (Localization.Away (f i))
      (LocalizedModule.Away (f i) M)) ↔ Module.FinitePresentationRel R A M
```

## Tag 0671, a lemma

[Tag 0671](https://stacks.math.columbia.edu/tag/0671) in the Stacks Project.

**`Module.finitePresentationRel_two_of_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean#L230). The attribute's comment: “(1)”.

> Stacks 0671, part (1). Given a short exact sequence of `A`-modules
> `0 → M' →[i] M →[p] M'' → 0` (so `i` is injective, `p` is surjective and
> `range i = ker p`), if `M'` and `M''` are finitely presented relative to `R`, then `M` is
> finitely presented relative to `R`.
>
> By Stacks 05GY, `M'` and `M''` are finitely presented over `R[x_1, …, x_n]` for *every*
> presentation `α`, so one may pick a single presentation and apply two-out-of-three over the
> polynomial ring `R[x_1, …, x_n]`.

```lean
theorem Module.finitePresentationRel_two_of_three (i : M' →ₗ[A] M) (p : M →ₗ[A] M'')
    (hi : Function.Injective i) (hp : Function.Surjective p)
    (hex : LinearMap.range i = LinearMap.ker p)
    (hM' : Module.FinitePresentationRel R A M')
    (hM'' : Module.FinitePresentationRel R A M'') :
    Module.FinitePresentationRel R A M
```

**`Module.finitePresentationRel_of_surjective_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean#L261). The attribute's comment: “(2)”.

> Stacks 0671, part (2). Given a short exact sequence of `A`-modules
> `0 → M' →[i] M →[p] M'' → 0`, if `M'` is a finite type (finitely generated) `A`-module and `M`
> is finitely presented relative to `R`, then `M''` is finitely presented relative to `R`.

```lean
theorem Module.finitePresentationRel_of_surjective_of_finite {R A : Type*} [CommRing R]
    [CommRing A] [Algebra R A] {M' M M'' : Type*} [AddCommGroup M'] [Module A M']
    [AddCommGroup M] [Module A M] [AddCommGroup M''] [Module A M'']
    (i : M' →ₗ[A] M) (p : M →ₗ[A] M'')
    (hp : Function.Surjective p)
    (hex : LinearMap.range i = LinearMap.ker p)
    (hM' : Module.Finite A M') (hM : Module.FinitePresentationRel R A M) :
    Module.FinitePresentationRel R A M''
```

## Tag 0672, a lemma

[Tag 0672](https://stacks.math.columbia.edu/tag/0672) in the Stacks Project.

**`Module.finitePresentationRel_of_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/FinitePresentationRel/Basic.lean#L305).

> Stacks 0672 (Lemma 15.82.10).
>
> Let `R → A` be a ring map (in Stacks, of finite type — the hypothesis is not needed here) and
> let `M`, `M'` be `A`-modules. If the direct sum `M × M'` is finitely presented relative to `R`,
> then both `M` and `M'` are finitely presented relative to `R`.

```lean
theorem Module.finitePresentationRel_of_prod {R A : Type*} [CommRing R] [CommRing A]
    [Algebra R A] {M M' : Type*} [AddCommGroup M] [Module A M] [AddCommGroup M'] [Module A M']
    (h : Module.FinitePresentationRel R A (M × M')) :
    Module.FinitePresentationRel R A M ∧ Module.FinitePresentationRel R A M'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.82, Tag 0659](https://stacks.math.columbia.edu/tag/0659)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
