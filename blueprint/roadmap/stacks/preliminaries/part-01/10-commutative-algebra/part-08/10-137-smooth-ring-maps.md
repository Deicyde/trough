---
declaration: section
origin: cited
lean: Algebra.Smooth.localization_away, Algebra.Smooth.localization_base, Algebra.Smooth.baseChange, isLocalCompleteIntersection_of_smooth, Algebra.SubmersivePresentation, Algebra.IsStandardSmooth, Algebra.SubmersivePresentation.smooth_and_free_and_isStandardSmooth_and_isRelativeGlobalCompleteIntersection, Stacks.StandardSmooth.isStandardSmooth_SAlg
statement: formalized
proof: formalized
---

# 10.137 Smooth ring maps

Section 10.137 of the Stacks Project, [Tag 00T1](https://stacks.math.columbia.edu/tag/00T1). 18 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00T3, a lemma

[Tag 00T3](https://stacks.math.columbia.edu/tag/00T3) in the Stacks Project.

**`Algebra.Smooth.localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Localization.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Localization.lean#L141). The attribute's comment: “First assertion: any localization `S_g` is smooth over `R`. `Algebra.Smooth` is Mathlib's definition (formally smooth and of finite presentation), equivalent to 00T2 by 00TN. The localization is an abstract `IsLocalization.Away g S'`. See the module docstring.”.

> Let `R → S` be a smooth ring map and let `S'` be a localization of `S` away from an element
> `g : S`. Then `S'` is smooth over `R`.

```lean
public theorem Algebra.Smooth.localization_away {R S S' : Type*} [CommRing R] [CommRing S]
    [CommRing S'] [Algebra R S] [Algebra R S'] [Algebra S S'] [IsScalarTower R S S']
    [Algebra.Smooth R S] (g : S) [IsLocalization.Away g S'] :
    Algebra.Smooth R S'
```

**`Algebra.Smooth.localization_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Localization.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Localization.lean#L157). The attribute's comment: “Second assertion: if `f ∈ R` maps to an invertible element of `S` then `R_f → S` is smooth. Stated as the `Algebra.Smooth` analogue of `Algebra.FormallySmooth.localization_base`: the base is localized at an arbitrary submonoid `M`, and the hypothesis on `f` is the pair `[Algebra Rₘ Sₘ] [IsScalarTower R Rₘ Sₘ]`. `Algebra.Smooth` is Mathlib's definition (formally smooth and of finite presentation), equivalent to 00T2 by 00TN. See the module docstring.”.

> Let `M` be a multiplicative subset of `R` and `Rₘ` a localization of `R` at `M`. Let `Sₘ` be
> an `R`-algebra which is smooth over `R` and which is an `Rₘ`-algebra compatibly with its
> `R`-algebra structure — for `M` the powers of `f ∈ R` this last condition says that `f` maps to an
> invertible element of `Sₘ`. Then `Sₘ` is smooth over `Rₘ`.

```lean
public theorem Algebra.Smooth.localization_base {R Rₘ Sₘ : Type*} [CommRing R] [CommRing Rₘ]
    [CommRing Sₘ] [Algebra R Rₘ] [Algebra R Sₘ] [Algebra Rₘ Sₘ] [IsScalarTower R Rₘ Sₘ]
    (M : Submonoid R) [IsLocalization M Rₘ] [Algebra.Smooth R Sₘ] :
    Algebra.Smooth Rₘ Sₘ
```

## Tag 00T4, a lemma

[Tag 00T4](https://stacks.math.columbia.edu/tag/00T4) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.Smooth.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Smooth.baseChange#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Smooth/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Basic.lean#L61) (StacksFrontier): “smoothness is stable under base change”. References: EGA 0 (19.3.5), “(iii), special case”; EGA 0 (19.4.2), “Necessity, special case”; EGA 0 (19.4.6), “special case”; EGA IV (17.3.3), “(iii), special case”; EGA IV (17.7.3), “(ii)”; EGA IV (6.8.2), “special case”; EGA IV (6.8.3), “(iii), special case”; SGA 1 II (4.13), “affine ascent”; SGA 3 VIB (10.1), “smoothness, special case”; SGA 3 VIB (2.1.2), “special case”; SGA 6 VIII (1.6), “special case”; SGA 6 VIII (1.8), “affine case”; SGA 6 X (7.13.3), “special case”; SGA 1 II (1.3), “(ii), affine case”.

## Tag 00T5, a lemma

[Tag 00T5](https://stacks.math.columbia.edu/tag/00T5) in the Stacks Project.

**`isLocalCompleteIntersection_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Smooth.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Smooth.lean#L136). The attribute's comment: “The source's `smooth` (Definition 00T2) is `Algebra.Smooth`, by Proposition 00TN; its finite type hypothesis on `S` is not repeated, being `Algebra.Smooth.finitePresentation`. A local complete intersection over `k` (Definition 00S9 (2)) is `IsLocalCompleteIntersection`. See the module docstring.”.

> **A smooth algebra over a field is a local complete intersection.** Let `k` be a field and let
> `S` be a smooth `k`-algebra. Then `S` is a local complete intersection over `k`: there is a family
> of elements of `S` generating the unit ideal — equivalently, whose standard opens cover
> `Spec S` — each of whose localizations `S_g` admits a presentation `k[x₁, …, xₙ]/(f₁, …, f_c)`
> with `dim S_g = n - c`.

```lean
public theorem isLocalCompleteIntersection_of_smooth (k : Type u) [Field k] (S : Type v)
    [CommRing S] [Algebra k S] [Algebra.Smooth k S] :
    IsLocalCompleteIntersection k S
```

## Tag 00T6, a definition

[Tag 00T6](https://stacks.math.columbia.edu/tag/00T6) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.SubmersivePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.SubmersivePresentation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L246) (StacksFrontier): “standard smooth presentation (with [Finite ι])”.
- [`Algebra.IsStandardSmooth`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsStandardSmooth#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L247) (StacksFrontier): “S is standard smooth over R”.

## Tag 00T7, a lemma

[Tag 00T7](https://stacks.math.columbia.edu/tag/00T7) in the Stacks Project.

**`Algebra.SubmersivePresentation.smooth_and_free_and_isStandardSmooth_and_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/StandardSmoothProperties.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/StandardSmoothProperties.lean#L111). The attribute's comment: “The standard smooth algebra is a submersive presentation `P` (Definition 00T6 is Mathlib's `Algebra.IsStandardSmooth`). The source's `x_1, …, x_c` are the variables `P.map j` paired with the relations, so its `dx_{c+1}, …, dx_n` are the `dx_i` for `i ∉ range P.map`. `I/I²` is `P.toExtension.Cotangent`. In (6) the `R_f`-algebra structure on `S` is the one factoring `R → S`. (7) is stated for the presentation `P` itself.”.

> Let `S = R[x_1, …, x_n]/(f_1, …, f_c)` be standard smooth, via a submersive presentation `P`.
> Then (1) `R → S` is smooth; (2) `Ω_{S/R}` is free on the `dx_i` for the variables `x_i` not paired
> with a relation; (3) `I/I²` is free on the classes of the `f_j`; (4) `S_g` is standard smooth over
> `R` for every `g ∈ S`; (5) `R' ⊗_R S` is standard smooth over `R'` for every `R`-algebra `R'`; (6)
> if `f ∈ R` maps to a unit of `S`, then `S` is standard smooth over `R_f`; (7) `S` is a relative
> global complete intersection over `R`.

```lean
theorem smooth_and_free_and_isStandardSmooth_and_isRelativeGlobalCompleteIntersection :
    Algebra.Smooth R S ∧
    (∃ b : Module.Basis ((Set.range P.map)ᶜ : Set ι) S Ω[S⁄R],
      ∀ i, b i = KaehlerDifferential.D R S (P.val i)) ∧
    (∃ b : Module.Basis σ S P.toExtension.Cotangent,
      ∀ j, b j = Extension.Cotangent.mk ⟨P.relation j, P.relation_mem_ker j⟩) ∧
    (∀ g : S, IsStandardSmooth R (Localization.Away g)) ∧
    (∀ (R' : Type*) [CommRing R'] [Algebra R R'], IsStandardSmooth R' (R' ⊗[R] S)) ∧
    (∀ (f : R) (hf : IsUnit (algebraMap R S f)),
      letI := (IsLocalization.Away.lift (S := Localization.Away f) f hf).toAlgebra
      IsStandardSmooth (Localization.Away f) S) ∧
    P.toPresentation.IsRelativeGlobalCompleteIntersection
```

## Tag 00T8, an example

[Tag 00T8](https://stacks.math.columbia.edu/tag/00T8) in the Stacks Project.

**`Stacks.StandardSmooth.isStandardSmooth_SAlg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/StandardSmooth.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/StandardSmooth.lean#L409).

> **Theorem (Stacks Tag 00T8).**  With `f : Fin c → R[x_0, ..., x_{n-1}]`,
> `h = det(jacobianFirst f)`, and
> `S = R[x_0, ..., x_n] / (f_0, ..., f_{c-1}, x_n * h - 1)`, the algebra `S` is
> standard smooth over `R`.  The witnessing presentation reorders the variables so
> that the first `c + 1` variables (in the chosen order) are
> `x_0, ..., x_{c-1}, x_n`, and uses the relations `g_0, ..., g_c`.

```lean
theorem isStandardSmooth_SAlg {n c : ℕ} (hc : c ≤ n) (f : Fin c → MvPolynomial (Fin n) R) :
    IsStandardSmooth (R := R) (SAlg hc f)
```

## Tag 00T9, a lemma

[Tag 00T9](https://stacks.math.columbia.edu/tag/00T9) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.IsStandardSmooth.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.IsStandardSmooth.comp#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Smooth/Basic.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Basic.lean#L78) (StacksFrontier): “standard smoothness is stable under composition”. References: SGA 1 II (1.3), “(iii), special case”.

## Tag 00TA, a lemma

[Tag 00TA](https://stacks.math.columbia.edu/tag/00TA) in the Stacks Project.

**`Algebra.Smooth.exists_span_eq_top_isStandardSmooth_and_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Syntomic.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Syntomic.lean#L38). The attribute's comment: “The cover by standard opens `D(g)`, `g ∈ s`, is `Ideal.span s = ⊤`. Syntomic is `Algebra.Syntomic` (Definition 00SL); it is derived here directly from Lemma 00T5 on the fibres rather than through Lemmas 00T7, 00SW and 00SO.”.

> **Stacks 00TA.** Let `R → S` be a smooth ring map. There are `g ∈ S` whose standard opens
> `D(g)` cover `Spec(S)` and such that each `S_g` is standard smooth over `R`. In particular
> `R → S` is syntomic.

```lean
theorem exists_span_eq_top_isStandardSmooth_and_syntomic [Smooth R S] :
    (∃ s : Set S, Ideal.span s = ⊤ ∧ ∀ g ∈ s, IsStandardSmooth R (Localization.Away g)) ∧
      Syntomic R S
```

## Tag 00TB, a definition

[Tag 00TB](https://stacks.math.columbia.edu/tag/00TB) in the Stacks Project.

**`Algebra.SmoothAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/SmoothAt.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/SmoothAt.lean#L19). References: SGA 1 II (1.1).

> A ring map `R → S` is *smooth at a prime* `q` of `S` if there exists
> some `g ∈ S` with `g ∉ q` such that the induced map `R → S_g` is smooth.

```lean
def Algebra.SmoothAt (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    (q : Ideal S) [q.IsPrime] : Prop
```

## Tag 07BU, a lemma

[Tag 07BU](https://stacks.math.columbia.edu/tag/07BU) in the Stacks Project.

**`Algebra.isSmoothAt_tfae_h1Cotangent_and_kaehlerDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/NaiveCotangentCriterion.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/NaiveCotangentCriterion.lean#L244). The attribute's comment: “The localizations `H_1(L_{S/R})_q` and `Ω_{S/R, q}` are read on an arbitrary model `Sq` of `S_q` as `Algebra.H1Cotangent R Sq` and `Ω[Sq⁄R]`, which is Lemma 00S7 and is witnessed by the instances `Algebra.H1Cotangent.isLocalizedModule` and `KaehlerDifferential.isLocalizedModule_map`; vanishing is `Subsingleton` and `finite free` is `Module.Finite` and `Module.Free`. Item (1) is Definition 00TB verbatim, and Mathlib's `Algebra.IsSmoothAt` is added as item (5). See the module docstring.”. References: EGA 0 (22.6.4), “special case”.

> **Smoothness at a prime is the vanishing of `H_1` together with freeness of `Ω`**
> (Stacks 07BU). Let `R → S` be of finite presentation, let `q` be a prime of `S` and let `Sq` be a
> model of `S_q`. The following are equivalent: (1) `R → S` is smooth at `q`, that is `R → S_g` is
> smooth for some `g ∉ q`; (2) `H_1(L_{S/R})_q = 0` and `Ω_{S/R, q}` is a finite free
> `S_q`-module; (3) `H_1(L_{S/R})_q = 0` and `Ω_{S/R, q}` is projective; (4) `H_1(L_{S/R})_q = 0`
> and `Ω_{S/R, q}` is flat; (5) `S_q` is formally smooth over `R`.

```lean
public theorem Algebra.isSmoothAt_tfae_h1Cotangent_and_kaehlerDifferential
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S]
    (q : Ideal S) [q.IsPrime] (Sq : Type*) [CommRing Sq] [Algebra S Sq]
    [IsLocalization.AtPrime Sq q] [Algebra R Sq] [IsScalarTower R S Sq] :
    List.TFAE
      [∃ g ∉ q, Algebra.Smooth R (Localization.Away g),
       Subsingleton (Algebra.H1Cotangent R Sq) ∧
         Module.Finite Sq Ω[Sq⁄R] ∧ Module.Free Sq Ω[Sq⁄R],
       Subsingleton (Algebra.H1Cotangent R Sq) ∧ Module.Projective Sq Ω[Sq⁄R],
       Subsingleton (Algebra.H1Cotangent R Sq) ∧ Module.Flat Sq Ω[Sq⁄R],
       Algebra.IsSmoothAt R q]
```

## Tag 00TC, a lemma

[Tag 00TC](https://stacks.math.columbia.edu/tag/00TC) in the Stacks Project.

**`Algebra.smooth_iff_forall_exists_notMem_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/SmoothAt.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/SmoothAt.lean#L199). The attribute's comment: “Smoothness at a prime `q` (Definition 00TB) is spelled out as `∃ g ∉ q`, with `Localization.Away g` smooth over `R` — as in Mathlib's `Algebra.IsSmoothAt.exists_notMem_smooth` — and not as Mathlib's `Algebra.IsSmoothAt`, which is formal smoothness of `S_q` and makes the equivalence false for `S` not of finite presentation over `R` (witness: `k[x_i : i ∈ ℕ]` over `k`). Producing the finite presentation of `S` from the pointwise hypothesis is precisely the content of this lemma. Stated for algebras; `RingHom.smooth_algebraMap` gives the form for a bundled ring map. See the module docstring.”.

> **Smoothness is detected at the primes of the target.** A ring map `R → S` is smooth if and
> only if it is smooth at every prime `q` of `S`, that is, if and only if for every prime `q ⊂ S`
> there is a `g ∈ S`, `g ∉ q`, with `R → S_g` smooth (Definition 00TB).
>
> Beware that the right-hand side is the Stacks project's notion of smoothness at `q`, which is
> strictly stronger than Mathlib's `Algebra.IsSmoothAt R q = Algebra.FormallySmooth R S_q` when `S`
> is not of finite presentation over `R`; see the module docstring.

```lean
public theorem Algebra.smooth_iff_forall_exists_notMem_smooth (R : Type*) [CommRing R] (S : Type*)
    [CommRing S] [Algebra R S] :
    Algebra.Smooth R S ↔
      ∀ (q : Ideal S) [q.IsPrime], ∃ g ∉ q, Algebra.Smooth R (Localization.Away g)
```

## Tag 00TD, a lemma

[Tag 00TD](https://stacks.math.columbia.edu/tag/00TD) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.Smooth.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.Smooth.comp#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Smooth/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Basic.lean#L83) (StacksFrontier): “smoothness is stable under composition”. References: EGA IV (17.3.3), “(ii), special case”; EGA IV (6.8.3), “special case”; SGA 1 II (1.3), “(iii), special case”.

## Tag 0GIF, a lemma

[Tag 0GIF](https://stacks.math.columbia.edu/tag/0GIF) in the Stacks Project.

**`Algebra.Smooth.prod_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Pi.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Pi.lean#L256). The attribute's comment: “The product is the literal `S' × S''`, with the componentwise `Prod.algebra` structure; the abstract form (an `S` with `S ≃ₐ[R] S' × S''`) follows by transport, via `Algebra.FormallySmooth.of_equiv` and `Algebra.FinitePresentation.equiv`. The two factors are allowed to lie in different universes, so this is not an instance of Mathlib's `Algebra.FormallySmooth.pi_iff`; that lemma also settles only the formal smoothness half, the finite presentation of each factor of a finitely presented product being the content added here. See the module docstring.”.

> **A product of two algebras is smooth if and only if both factors are.** Let `R` be a ring and
> let `S = S' × S''` be a product of `R`-algebras. Then `S` is smooth over `R` if and only if both
> `S'` and `S''` are smooth over `R`.
>
> Each factor is the principal localization of `S` at one of the complementary idempotents
> `(1, 0)` and `(0, 1)`, which is why the equivalence holds; see the module docstring.

```lean
public theorem Algebra.Smooth.prod_iff (R : Type*) [CommRing R] (S' : Type*) [CommRing S']
    [Algebra R S'] (S'' : Type*) [CommRing S''] [Algebra R S''] :
    Algebra.Smooth R (S' × S'') ↔ Algebra.Smooth R S' ∧ Algebra.Smooth R S''
```

## Tag 00TE, a lemma

[Tag 00TE](https://stacks.math.columbia.edu/tag/00TE) in the Stacks Project.

**`Algebra.Presentation.isSmoothAt_iff_exists_jacobian_notMem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/JacobianCriterion.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/JacobianCriterion.lean#L386). The attribute's comment: “The subset `I ⊆ {1, …, n}` of cardinality `c` is an injection `σ ↪ ι` from the relations to the variables — that is, the extra datum of an `Algebra.PreSubmersivePresentation` — and the image of `g_I` in `S` is its `jacobian`. The hypothesis is placed on the given presentation `P`, not on the class `Algebra.IsRelativeGlobalCompleteIntersection` (00SP), since the criterion depends on `P`; it is verbatim the condition that class asserts of its chosen presentation. Index types are arbitrary finite ones rather than `Fin n`, `Fin c`, and smoothness at `q` is `Algebra.IsSmoothAt` (00TB). See the module docstring.”.

> **Jacobian criterion for smoothness at a prime.** Let `S = R[x_1, …, x_n]/(f_1, …, f_c)` be a
> presentation of `S` over `R` such that every nonempty fibre of `Spec(S) → Spec(R)` has dimension
> `n - c`, i.e. a relative global complete intersection (Definition 00SP). Then `R → S` is smooth at
> a prime `q ⊂ S` if and only if there is a subset `I ⊆ {1, …, n}` of cardinality `c` such that
> `g_I = det (∂f_j/∂x_i)_{j = 1, …, c, i ∈ I}` does not map into `q`.
>
> The subset `I` is an injection `f : σ ↪ ι` from the relations to the variables, and the image of
> `g_I` in `S` is the `Algebra.PreSubmersivePresentation.jacobian` of `P` equipped with `f`. See the
> module docstring.

```lean
public theorem Algebra.Presentation.isSmoothAt_iff_exists_jacobian_notMem {R S : Type*}
    [CommRing R] [CommRing S] [Algebra R S] {ι σ : Type*} [Finite ι] [Finite σ]
    (P : Algebra.Presentation R S ι σ)
    (hP : ∀ (p : Ideal R) [p.IsPrime], Nontrivial (p.Fiber S) →
      ringKrullDim (p.Fiber S) + Nat.card σ = Nat.card ι)
    (q : Ideal S) [q.IsPrime] :
    Algebra.IsSmoothAt R q ↔
      ∃ f : σ ↪ ι, (Algebra.PreSubmersivePresentation.mk P f f.injective).jacobian ∉ q
```

## Tag 00TF, a lemma

[Tag 00TF](https://stacks.math.columbia.edu/tag/00TF) in the Stacks Project.

**`Algebra.exists_notMem_smooth_of_isSmoothAt_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/SmoothAt.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/SmoothAt.lean#L570). The attribute's comment: “Smoothness at `q` in the conclusion is spelled out as Definition 00TB, `∃ g ∉ q` with `Localization.Away g` smooth over `R`, while smoothness of the fibre at `Q` is Mathlib's `Algebra.IsSmoothAt`; the two notions agree under hypothesis (1), so this is the weakest hypothesis with the strongest conclusion. The fibre is `Ideal.Fiber` and `Q` is pinned as the prime corresponding to `q` by `hq`, the inverse of `PrimeSpectrum.preimageEquivFiber`. Flatness of `R_p → S_q` is stated over `R`, which for the `R_p`-algebra `S_q` is the same condition (`Module.flat_iff_of_isLocalization`). This is the full generality of the tag; upstream's `Algebra.IsSmoothAt.of_formallySmooth_fiber` is the case of all three hypotheses imposed globally. See the module docstring.”. References: SGA 1 II (2.1), “(a) + (b) ⇒ smooth”; SGA 3 VIB (3.10), “special case”.

> **Flat with a smooth fibre implies smooth, at a prime.** Let `R → S` be a ring map, let `q` be
> a prime of `S` and let `Q` be the prime of the fibre `κ(p) ⊗_R S` corresponding to `q`, where `p`
> is the prime of `R` under `q`. Assume that `R → S_g` is of finite presentation for some `g ∉ q`,
> that `S_q` is flat over `R` — equivalently, that the local homomorphism `R_p → S_q` is flat — and
> that the fibre is smooth over `κ(p)` at `Q`. Then `R → S` is smooth at `q`: there is a `g ∈ S`,
> `g ∉ q`, with `R → S_g` smooth (Definition 00TB).
>
> Note that `q` lies over `p` automatically, this being part of `hq`.

```lean
public theorem Algebra.exists_notMem_smooth_of_isSmoothAt_fiber {R S : Type*} [CommRing R]
    [CommRing S] [Algebra R S] (p : Ideal R) [p.IsPrime] (Q : Ideal (p.Fiber S)) [Q.IsPrime]
    [Algebra.IsSmoothAt p.ResidueField Q] (q : Ideal S) [q.IsPrime]
    [Module.Flat R (Localization.AtPrime q)]
    (hq : Q.comap (Algebra.TensorProduct.includeRight : S →ₐ[R] p.Fiber S) = q)
    (hfp : ∃ g ∉ q, Algebra.FinitePresentation R (Localization.Away g)) :
    ∃ g ∉ q, Algebra.Smooth R (Localization.Away g)
```

## Tag 00TG, a lemma

[Tag 00TG](https://stacks.math.columbia.edu/tag/00TG) in the Stacks Project.

**`Algebra.smoothLocus_comap_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/LocusBaseChange.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/LocusBaseChange.lean#L300). The attribute's comment: “The base change is the abstract one, `Algebra.IsPushout R S R' S'`, and the two smooth loci are Mathlib's `Algebra.smoothLocus`, which for a finitely presented algebra is the source's set of primes at which the map is smooth (Definition 00TB, via Lemma 07BU). The equality is oriented as `f⁻¹(U) = V`, as in `Algebra.smoothLocus_comap_of_isLocalization`. See the module docstring.”. References: EGA IV (17.7.2), “(ii), affine case”; SGA 1 II (4.13), “affine case”.

> **The smooth locus is stable under flat base change** (Stacks 00TG). Let `R → S` be of finite
> presentation, let `R → R'` be flat and let `S'` be the base change `R' ⊗_R S`. Then the set of
> primes of `S'` at which `R' → S'` is smooth is the inverse image, under
> `f : Spec(S') → Spec(S)`, of the set of primes of `S` at which `R → S` is smooth.

```lean
public theorem Algebra.smoothLocus_comap_of_isPushout (R S R' S' : Type*) [CommRing R] [CommRing S]
    [CommRing R'] [CommRing S'] [Algebra R S] [Algebra R R'] [Algebra S S'] [Algebra R' S']
    [Algebra R S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
    [Algebra.IsPushout R S R' S'] [Algebra.FinitePresentation R S] [Module.Flat R R'] :
    PrimeSpectrum.comap (algebraMap S S') ⁻¹' Algebra.smoothLocus R S
      = Algebra.smoothLocus R' S'
```

## Tag 02UQ, a lemma

[Tag 02UQ](https://stacks.math.columbia.edu/tag/02UQ) in the Stacks Project.

**`Algebra.isSmoothAt_iff_isSmoothAt_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/LocusBaseChange.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/LocusBaseChange.lean#L461). The attribute's comment: “The source takes `K/k` a field extension; `K` is here an arbitrary commutative `k`-algebra, since only flatness of `k → K` is used and that is automatic over a field. The base change is the abstract one, `Algebra.IsPushout k S K S'`, the prime correspondence is `Ideal.LiesOver`, and smoothness at a prime is Mathlib's `Algebra.IsSmoothAt`, which for a finite type algebra over a field is the source's Definition 00TB. See the module docstring.”.

> **Smoothness at a prime is insensitive to base field extension** (Stacks 02UQ). Let `k` be a
> field, `S` a finite type `k`-algebra, `K` a `k`-algebra and `S'` the base change `K ⊗_k S`. Let
> `q'` be a prime of `S'` lying over the prime `q` of `S`. Then `S` is smooth over `k` at `q` if and
> only if `S'` is smooth over `K` at `q'`.

```lean
public theorem Algebra.isSmoothAt_iff_isSmoothAt_of_isPushout {k S K S' : Type*} [Field k]
    [CommRing S] [CommRing K] [CommRing S'] [Algebra k S] [Algebra k K] [Algebra S S']
    [Algebra K S'] [Algebra k S'] [IsScalarTower k K S'] [IsScalarTower k S S']
    [Algebra.IsPushout k S K S'] [Algebra.FiniteType k S] (q : Ideal S) (q' : Ideal S')
    [q.IsPrime] [q'.IsPrime] [q'.LiesOver q] :
    Algebra.IsSmoothAt k q ↔ Algebra.IsSmoothAt K q'
```

## Tag 04B1, a lemma

[Tag 04B1](https://stacks.math.columbia.edu/tag/04B1) in the Stacks Project.

**`Algebra.Smooth.exists_span_eq_top_isStandardSmooth_algEquiv_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/LocalStructure.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/LocalStructure.lean#L185). The attribute's comment: “The source's `R/I → S̄` is stated for an arbitrary surjection `R → R'`, which is what the proof uses (it lifts the relations along `R[x] → R'[x]`); the source's form is the case `R' = R ⧸ I`, by `Ideal.Quotient.mk_surjective`. The source's `S_i/I S_i` is the base change `R' ⊗[R] S`, identified with that quotient over `R ⧸ I` by `Algebra.TensorProduct.quotIdealMapEquivQuotTensor`. The parenthetical `(standard)` is taken as the assertion. See the module docstring.”.

> Let `R → R'` be a surjective ring map (for instance `R' = R ⧸ I`) and let `R' → S'` be
> smooth. Then there are elements `g ∈ S'` generating the unit ideal of `S'` such that each `S'_g` is
> isomorphic as an `R'`-algebra to `R' ⊗[R] S` for some standard smooth `R`-algebra `S`; that is,
> `S'` is, locally on `Spec S'`, a base change of a standard smooth `R`-algebra.

```lean
public theorem Algebra.Smooth.exists_span_eq_top_isStandardSmooth_algEquiv_tensorProduct
    (R : Type u) [CommRing R] (R' : Type v) [CommRing R'] [Algebra R R']
    (hsurj : Function.Surjective (algebraMap R R'))
    (S' : Type w) [CommRing S'] [Algebra R' S'] [Algebra.Smooth R' S'] :
    ∃ s : Set S', Ideal.span s = ⊤ ∧ ∀ g ∈ s,
      ∃ (S : Type u) (_ : CommRing S) (_ : Algebra R S) (_ : Algebra.IsStandardSmooth R S),
        Nonempty (Localization.Away g ≃ₐ[R'] R' ⊗[R] S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.137, Tag 00T1](https://stacks.math.columbia.edu/tag/00T1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
