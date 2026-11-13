---
declaration: section
origin: cited
lean: Algebra.trace', charPoly_mul_eq_minpoly_pow, norm_eq_neg_one_pow_finrank_mul_constantCoeff_minpoly_pow_finrank, trace_eq_finrank_mul_minpoly_nextCoeff, trace_restrictScalars, charpoly_restrictScalars_of_tower, charpoly_mul_of_tower, trace_trace
statement: formalized
proof: formalized
---

# 9.20 Trace and norm

Section 9.20 of the Stacks Project, [Tag 0BIE](https://stacks.math.columbia.edu/tag/0BIE). 7 tags here are carried by 12 declarations of the repository (11 in StacksCore and 1 in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BIF, a definition

[Tag 0BIF](https://stacks.math.columbia.edu/tag/0BIF) in the Stacks Project.

**`Algebra.trace'`**, a def in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/NormTrace.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/NormTrace.lean#L348). The attribute's comment: “trace”. References: EGA IV (18.2.1); SGA 1 I (4.10), “special case”; SGA 5 IIIB (5.10), “special case”.

> **Stacks 0BIF** (trace).
> The trace of an `R`-algebra `S`, defined as the linear-map trace of left multiplication
> `mul R S : S →ₗ[R] End R S`. This works for any `R`-algebra (no commutativity or finite-freeness
> assumption on `S`); it agrees with `Algebra.trace R S` whenever the latter is defined.

```lean
noncomputable def trace' (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S] : S →ₗ[R] R
```

## Tag 0BIG, a lemma

[Tag 0BIG](https://stacks.math.columbia.edu/tag/0BIG) in the Stacks Project.

**`charPoly_mul_eq_minpoly_pow`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/NormTrace.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/NormTrace.lean#L588).

> **Stacks 0BIG**.
> For a finite free extension `R ⊆ S` and `x ∈ S` such that `R[x]` is free over `R` and `S` is
> free over `R[x]`, the characteristic polynomial of `Algebra.lmul R S x` equals
> `(minpoly R x) ^ [S : R[x]]`.

```lean
theorem charPoly_mul_eq_minpoly_pow (R : Type*) {S : Type*}
    [CommRing R] [Ring S] [Algebra R S] [Free R S] [Module.Finite R S]
    (x : S) [Free R R[x]] [Free R[x] S] :
    (mul R S x).charpoly = minpoly R x ^ Module.finrank R[x] S
```

## Tag 0BIH, a lemma

[Tag 0BIH](https://stacks.math.columbia.edu/tag/0BIH) in the Stacks Project.

**`norm_eq_neg_one_pow_finrank_mul_constantCoeff_minpoly_pow_finrank`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/NormTrace.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/NormTrace.lean#L615).

> **Stacks 0BIH**.
> For a finite extension `R ⊆ S` and `x ∈ S` such that `R[x]` is free over `R` and `S` is
> free over `R[x]` (so that `S` is free over `R`), `norm R x` equals `(-1) ^ [S : R]` times the
> constant coefficient of `minpoly R x` raised to the `[S : R[x]]`-th power.

```lean
theorem norm_eq_neg_one_pow_finrank_mul_constantCoeff_minpoly_pow_finrank (R : Type*) {S : Type*}
    [CommRing R] [Ring S] [Algebra R S] [Module.Finite R S]
    (x : S) [Free R R[x]] [Free R[x] S] :
    norm R x = (-1) ^ finrank R S * (minpoly R x).constantCoeff ^ finrank R[x] S
```

Declarations registered for the tag:

- [`trace_eq_finrank_mul_minpoly_nextCoeff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=trace_eq_finrank_mul_minpoly_nextCoeff#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Trace/Basic.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Trace/Basic.lean#L10) (StacksCore).

## Tag 0BII, a lemma

[Tag 0BII](https://stacks.math.columbia.edu/tag/0BII) in the Stacks Project.

**`trace_restrictScalars`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/NormTrace.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/NormTrace.lean#L447). The attribute's comment: “trace”. References: SGA 5 IIIB (5.10.11), “special case”; SGA 5 IIIB (6.7), “special case”.

> **Stacks 0BII** (trace).
> In a tower `R ⊆ S ⊆ A` of free extensions, the `R`-trace of an `S`-linear endomorphism
> `f : A →ₗ[S] A` factors through the `S`-trace: it equals `trace' R S` applied to `f.trace S A`.
> This expresses the transitivity of trace at the level of endomorphisms. No finiteness is
> assumed: if `S` is not finite over `R` or `A` is not finite over `S`, both sides are `0`.

```lean
theorem trace_restrictScalars (R : Type*) {S A : Type*}
    [CommSemiring R] [CommSemiring S] [Semiring A]
    [Algebra R S] [Algebra S A] [Algebra R A] [IsScalarTower R S A]
    [Module.Free R S] [Module.Free S A]
    (f : A →ₗ[S] A) : (f.restrictScalars R).trace R A = trace' R S (f.trace S A)
```

**`charpoly_restrictScalars_of_tower`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/NormTrace.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/NormTrace.lean#L481). The attribute's comment: “generalization”.

> **Stacks 0BII** (generalization).
> In a tower `R ⊆ S ⊆ A` of free extensions, with `A` finite over `S` and over `R`, the
> characteristic polynomial of the `R`-linear endomorphism `f.restrictScalars R` is the polynomial
> norm of the characteristic polynomial of the `S`-linear endomorphism `f`.

```lean
theorem charpoly_restrictScalars_of_tower (R : Type*) {S A : Type*}
    [CommRing R] [CommRing S] [AddCommGroup A]
    [Algebra R S] [Module S A] [Module R A] [IsScalarTower R S A]
    [Module.Free R S] [Module.Free S A] [Module.Finite S A]
    [Module.Free R A] [Module.Finite R A]
    (f : A →ₗ[S] A) : (f.restrictScalars R).charpoly = f.charpoly.norm R S
```

## Tag 0BIJ, a lemma

[Tag 0BIJ](https://stacks.math.columbia.edu/tag/0BIJ) in the Stacks Project.

**`charpoly_mul_of_tower`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/NormTrace.lean, line 525](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/NormTrace.lean#L525). The attribute's comment: “generalization”.

> **Stacks 0BIJ** (generalization).
> Specialization of `charpoly_restrictScalars_of_tower` to left-multiplication: in a tower
> `R ⊆ S ⊆ A`, the characteristic polynomial of `mul R A x` equals the polynomial norm over `R[X]`
> of the characteristic polynomial of `mul S A x`.

```lean
theorem charpoly_mul_of_tower (R S : Type*) {A : Type*}
    [CommRing R] [CommRing S] [Ring A]
    [Algebra R S] [Algebra S A] [Algebra R A] [IsScalarTower R S A]
    [Module.Free R S] [Module.Free S A] [Module.Finite S A]
    [Module.Free R A] [Module.Finite R A]
    (x : A) : (mul R A x).charpoly = (mul S A x).charpoly.norm R S
```

**`trace_trace`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/NormTrace.lean, line 537](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/NormTrace.lean#L537). The attribute's comment: “trace”. References: SGA 4 XVII (6.3.15), “(v)”; SGA 5 IIIB (5.10.11), “special case”; SGA 5 IIIB (6.7), “special case”.

> **Stacks 0BIJ** (trace).
> Transitivity of trace in a tower of free extensions:
> `trace' R S ∘ trace' S A = trace' R A`.

```lean
theorem trace_trace (R S : Type*) {A : Type*}
    [CommSemiring R] [CommSemiring S] [Semiring A]
    [Algebra R S] [Algebra S A] [Algebra R A] [IsScalarTower R S A]
    [Module.Free R S] [Module.Free S A]
    (x : A) : trace' R S (trace' S A x) = trace' R A x
```

Declarations registered for the tag:

- [`Algebra.norm_norm`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.norm_norm#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Norm/Transitivity.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Norm/Transitivity.lean#L15) (StacksCore): “norm”.

## Tag 0BIM, a definition

[Tag 0BIM](https://stacks.math.columbia.edu/tag/0BIM) in the Stacks Project.

**`Algebra.discr'`**, a def in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Discriminant.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Discriminant.lean#L19).

> **Stacks 0BIM**.
> The discriminant of an `R`-algebra `S` as an element of `QuotSq R`: when `S` is finite free over
> `R`, return the class of `discr R b` for any chosen basis `b` (the class is independent of the
> basis); otherwise return `0`.

```lean
noncomputable def discr' (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] : QuotSq R
```

**`Algebra.mk_discr_eq_discr'`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Discriminant.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Discriminant.lean#L33).

> **Stacks 0BIM**.
> For any `R`-basis `b` of `S`, the class of the basis-discriminant `discr R b` in `QuotSq R`
> agrees with `discr' R S`, witnessing that the latter is well-defined independently of the
> chosen basis.

```lean
theorem mk_discr_eq_discr' {ι : Type*} [Fintype ι] [DecidableEq ι] (b : Basis ι R S) :
    .mk R (discr R b) = discr' R S
```

## Tag 0BIN, an exercise

[Tag 0BIN](https://stacks.math.columbia.edu/tag/0BIN) in the Stacks Project.

**`Algebra.IsQuadraticExtension.of_field_char_two`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/IsQuadraticExtension.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/IsQuadraticExtension.lean#L185). The attribute's comment: “characteristic two case”.

> **Stacks 0BIN** (characteristic two case).
> A quadratic field extension `L/K` of a field of characteristic two is either purely inseparable
> of the form `K[√a]` for a non-square `a` (with `discr' K L = 0`), or separable of the form
> `K[X]/(X^2 + X - a)` for some `a ∈ K` not of the form `x(x+1)` (with `discr' K L = 1`).

```lean
theorem of_field_char_two (K L : Type*) [Field K] [Field L] [Algebra K L]
    [CharP K 2] [IsQuadraticExtension K L] :
    (discr' K L = 0 ∧ IsPurelyInseparable K L ∧
      ∃ a : K, ¬IsSquare a ∧ Nonempty (L ≃ₐ[K] QuadraticAlgebra K a 0)) ∨
    (discr' K L = 1 ∧ Algebra.IsSeparable K L ∧
      ∃ a : K, (∀ x : K, x * (x + 1) ≠ a) ∧ Nonempty (L ≃ₐ[K] QuadraticAlgebra K a 1))
```

**`Algebra.IsQuadraticExtension.of_field_two_ne_zero`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/IsQuadraticExtension.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/IsQuadraticExtension.lean#L221). The attribute's comment: “characteristic not two case”.

> **Stacks 0BIN** (characteristic not two case).
> A quadratic field extension `L/K` over a field with `2 ≠ 0` is automatically separable,
> its discriminant class is neither `0` nor `1`, and `L` is `K`-isomorphic to `K[√a]` for some
> non-square `a ∈ K`.

```lean
theorem of_field_two_ne_zero (K L : Type*) [Field K] [Field L] [Algebra K L]
    [NeZero (2 : K)] [IsQuadraticExtension K L] :
    discr' K L ≠ 0 ∧ discr' K L ≠ 1 ∧ Algebra.IsSeparable K L ∧
      ∃ a : K, ¬IsSquare a ∧ Nonempty (L ≃ₐ[K] QuadraticAlgebra K a 0)
```

**`Algebra.IsQuadraticExtension.classification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IsQuadraticExtension.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IsQuadraticExtension.lean#L45). The attribute's comment: “complete classification: the three cases hold in every characteristic and exclude one another, case (3) with `L ≅ K[√a]` for `a` representing the discriminant”.

> **Stacks 0BIN**. Let `L/K` be an extension of fields of degree `2`. Then exactly one of the
> following happens:
> 1. the discriminant is `0`, the characteristic of `K` is `2`, and `L/K` is purely inseparable,
>    obtained by taking a square root of a non-square `a ∈ K`;
> 2. the discriminant is `1`, the characteristic of `K` is `2`, and `L/K` is separable (of the form
>    `K[X]/(X^2 + X - a)` with `a` not of the form `x(x+1)`);
> 3. the discriminant is the class of a non-square `a ∈ K`, the characteristic of `K` is not `2`,
>    and `L ≅ K[√a]` is obtained by taking a square root of the discriminant.

```lean
theorem classification (K L : Type*) [Field K] [Field L] [Algebra K L]
    [IsQuadraticExtension K L] :
    let P₁ := discr' K L = 0 ∧ ringChar K = 2 ∧ IsPurelyInseparable K L ∧
      ∃ a : K, ¬IsSquare a ∧ Nonempty (L ≃ₐ[K] QuadraticAlgebra K a 0)
    let P₂ := discr' K L = 1 ∧ ringChar K = 2 ∧ Algebra.IsSeparable K L ∧
      ∃ a : K, (∀ x : K, x * (x + 1) ≠ a) ∧ Nonempty (L ≃ₐ[K] QuadraticAlgebra K a 1)
    let P₃ := ringChar K ≠ 2 ∧ Algebra.IsSeparable K L ∧
      ∃ a : K, QuotSq.mk K a = discr' K L ∧ ¬IsSquare a ∧
        Nonempty (L ≃ₐ[K] QuadraticAlgebra K a 0)
    (P₁ ∨ P₂ ∨ P₃) ∧ ¬(P₁ ∧ P₂) ∧ ¬(P₁ ∧ P₃) ∧ ¬(P₂ ∧ P₃)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.20, Tag 0BIE](https://stacks.math.columbia.edu/tag/0BIE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
