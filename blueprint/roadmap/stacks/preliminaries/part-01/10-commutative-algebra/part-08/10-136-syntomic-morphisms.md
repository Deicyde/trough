---
declaration: section
origin: cited
lean: Algebra.Syntomic, Algebra.IsPushout.syntomic_iff, Algebra.IsPushout.syntomic, isSyntomic_of_isSyntomic_localization_away, Algebra.Presentation.IsRelativeGlobalCompleteIntersection, Algebra.IsRelativeGlobalCompleteIntersection, Algebra.exists_presentation_basis_cotangent_of_free_cotangent, MvPolynomial.universalFactorizationMapBaseChangeAlgHomEquiv
statement: formalized
proof: formalized
---

# 10.136 Syntomic morphisms

Section 10.136 of the Stacks Project, [Tag 00SK](https://stacks.math.columbia.edu/tag/00SK). 17 tags here are carried by 32 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00SL, a definition

[Tag 00SL](https://stacks.math.columbia.edu/tag/00SL) in the Stacks Project.

**`Algebra.Syntomic`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/Defs.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/Defs.lean#L70). The attribute's comment: “Stated for an `R`-algebra `S`, as Mathlib states `Algebra.Smooth`; for a ring map `f : R →+* S` it is `Algebra.Syntomic R S` at `f.toAlgebra`. The fibre ring is Mathlib's `Ideal.Fiber p S = κ(p) ⊗[R] S`, the source's `S ⊗_R κ(p)` with the factors exchanged so that the `κ(p)`-algebra structure is the one Mathlib puts on a tensor product. See the module docstring.”. References: EGA IV (19.3.6), “affine case”.

> A ring map `R → S` is **syntomic**, and `S` is a **flat local complete intersection over
> `R`**, if it is flat, of finite presentation, and if all of its fibre rings `S ⊗_R κ(p)` are
> local complete intersections over `κ(p)` (`IsLocalCompleteIntersection`).

```lean
public class Algebra.Syntomic (R : Type*) [CommRing R] (S : Type*) [CommRing S] [Algebra R S] :
    Prop
```

## Tag 00SM, a lemma

[Tag 00SM](https://stacks.math.columbia.edu/tag/00SM) in the Stacks Project.

**`Algebra.IsPushout.syntomic_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/BaseChange.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/BaseChange.lean#L227). The attribute's comment: “The base change `S' = R' ⊗_R S` is an arbitrary pushout square `Algebra.IsPushout R R' S S'`; the source's literal form is `inferInstance` once `Algebra.TensorProduct.rightAlgebra` is a local instance. Faithful flatness is `Module.FaithfullyFlat R R'`, the module-level form Mathlib's descent lemmas use. See the module docstring.”.

> Let `R → S` be a ring map, let `R → R'` be faithfully flat and let `S'` be the base change of
> `S` along `R → R'`, so `S' = R' ⊗_R S`. Then `R' → S'` is syntomic if and only if `R → S` is
> syntomic.

```lean
public theorem Algebra.IsPushout.syntomic_iff (R R' S S' : Type*) [CommRing R] [CommRing R']
    [CommRing S] [CommRing S'] [Algebra R R'] [Algebra R S] [Algebra R S'] [Algebra R' S']
    [Algebra S S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
    [Algebra.IsPushout R R' S S'] [Module.FaithfullyFlat R R'] :
    Algebra.Syntomic R' S' ↔ Algebra.Syntomic R S
```

## Tag 00SN, a lemma

[Tag 00SN](https://stacks.math.columbia.edu/tag/00SN) in the Stacks Project.

**`Algebra.IsPushout.syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/BaseChange.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/BaseChange.lean#L211). The attribute's comment: “The base change is an arbitrary pushout square `Algebra.IsPushout R S R' S'`, the square `RingHom.IsStableUnderBaseChange` quantifies over and the orientation of Mathlib's `Algebra.IsPushout.isIntegral`; the source's literal `S' = S ⊗_R R'` is `TensorProduct.isPushout`. Nothing is assumed about `R → R'`. See the module docstring.”.

> Any base change of a syntomic ring map is syntomic: if `R → S` is syntomic and `S'` is the base
> change of `S` along an arbitrary ring map `R → R'`, so `S' = S ⊗_R R'`, then `R' → S'` is
> syntomic.

```lean
public theorem Algebra.IsPushout.syntomic (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    (R' S' : Type*) [CommRing R'] [CommRing S'] [Algebra R R'] [Algebra R S'] [Algebra S S']
    [Algebra R' S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
    [Algebra.IsPushout R S R' S'] [Algebra.Syntomic R S] :
    Algebra.Syntomic R' S'
```

## Tag 00SO, a lemma

[Tag 00SO](https://stacks.math.columbia.edu/tag/00SO) in the Stacks Project.

**`isSyntomic_of_isSyntomic_localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RingHom/FinitePresentation.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RingHom/FinitePresentation.lean#L378).

> Syntomic is local on the source: let `R → S` be a ring map and suppose there are
> elements `g_1, …, g_m ∈ S` generating the unit ideal of `S` such that for each `i` the
> composite `R → S_{g_i}` is syntomic. Then `R → S` is syntomic.

```lean
theorem isSyntomic_of_isSyntomic_localization_away
    (R : Type*) [CommRing R] (S : Type*) [CommRing S] [Algebra R S]
    (m : ℕ) (g : Fin m → S) (hg : Ideal.span (Set.range g) = ⊤)
    (h : ∀ i, IsSyntomic R (Localization.Away (g i))) :
    IsSyntomic R S
```

## Tag 00SP, a definition

[Tag 00SP](https://stacks.math.columbia.edu/tag/00SP) in the Stacks Project.

**`Algebra.Presentation.IsRelativeGlobalCompleteIntersection`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Defs.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Defs.lean#L245). The attribute's comment: “The source's displayed `S = R[x_1, …, x_n]/(f_1, …, f_c)`, a presentation together with the dimension property of its fibres; `Algebra.IsRelativeGlobalCompleteIntersection` is the property of the ring map, defined through this one. Stated for arbitrary finite index types, with `n = Nat.card ι` and `c = Nat.card σ`. The fibre ring is `Ideal.Fiber p S = κ(p) ⊗[R] S`, and `dim = n - c` is written additively as `ringKrullDim (p.Fiber S) + Nat.card σ = Nat.card ι` in `WithBot ℕ∞` rather than with the truncated subtraction `Algebra.Presentation.dimension`. See the module docstring.”.

> A presentation `S = R[x_1, …, x_n]/(f_1, …, f_c)` of `S` over `R` **is a relative global
> complete intersection** if every nonempty fibre of `Spec(S) → Spec(R)` has dimension `n - c`.
>
> The number of variables is `n = Nat.card ι` and the number of relations is `c = Nat.card σ`, the
> fibre over a prime `p` of `R` is the spectrum of `p.Fiber S = κ(p) ⊗_R S`, it is nonempty exactly
> when that ring is nonzero, and `dim = n - c` is written as the equation
> `ringKrullDim (p.Fiber S) + c = n` in `WithBot ℕ∞`.

```lean
public class Algebra.Presentation.IsRelativeGlobalCompleteIntersection {R S : Type*} [CommRing R]
    [CommRing S] [Algebra R S] {ι σ : Type*} [Finite ι] [Finite σ]
    (P : Algebra.Presentation R S ι σ) : Prop
```

**`Algebra.IsRelativeGlobalCompleteIntersection`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Defs.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Defs.lean#L264). The attribute's comment: “Stated for an `R`-algebra `S`, as Mathlib states `Algebra.Smooth` and as the sibling `Algebra.Syntomic` (00SL) is stated; for a ring map `f : R →+* S` it is `Algebra.IsRelativeGlobalCompleteIntersection R S` at `f.toAlgebra`. The presentation `S = R[x_1, …, x_n]/(f_1, …, f_c)` is `Algebra.Presentation R S (Fin n) (Fin c)` and the dimension condition on it is `Algebra.Presentation.IsRelativeGlobalCompleteIntersection`, through which this one is defined, as Mathlib defines `Algebra.IsStandardSmoothOfRelativeDimension` through `Algebra.SubmersivePresentation`. See the module docstring.”.

> A ring map `R → S` is a **relative global complete intersection** if there is a presentation
> `S = R[x_1, …, x_n]/(f_1, …, f_c)` such that every nonempty fibre of `Spec(S) → Spec(R)` has
> dimension `n - c`, that is, a presentation satisfying
> `Algebra.Presentation.IsRelativeGlobalCompleteIntersection`.

```lean
public class Algebra.IsRelativeGlobalCompleteIntersection (R : Type*) [CommRing R] (S : Type*)
    [CommRing S] [Algebra R S] : Prop
```

## Tag 07CF, a lemma

[Tag 07CF](https://stacks.math.columbia.edu/tag/07CF) in the Stacks Project.

**`Algebra.exists_presentation_basis_cotangent_of_free_cotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cotangent/FreeConormalPresentation.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Cotangent/FreeConormalPresentation.lean#L42).

> A finitely presented `R`-algebra `S` admitting a presentation `S = R[x₁, …, xₙ]/I` with
> `I/I²` free over `S` admits a presentation `S = R[y₁, …, y_m]/(f₁, …, f_c)` whose conormal
> module is free with basis the classes of `f₁, …, f_c`.

```lean
theorem exists_presentation_basis_cotangent_of_free_cotangent [FinitePresentation R S]
    (h : ∃ (ι : Type) (_ : Finite ι) (P : Generators R S ι),
      Module.Free S P.toExtension.Cotangent) :
    ∃ (ι σ : Type) (_ : Finite ι) (_ : Finite σ) (P : Presentation R S ι σ)
      (b : Module.Basis σ S P.toExtension.Cotangent),
      ∀ r, b r = Extension.Cotangent.mk ⟨P.relation r, P.relation_mem_ker r⟩
```

## Tag 00SQ, an example

[Tag 00SQ](https://stacks.math.columbia.edu/tag/00SQ) in the Stacks Project.

**`MvPolynomial.universalFactorizationMapBaseChangeAlgHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L79). The attribute's comment: “the source's `k`-algebra maps `S_k → K` are tuples `β, γ` with `x^{n+m} + α_1 x^{n+m-1} + … = (x^n + β_1 x^{n-1} + …)(x^m + γ_1 x^{m-1} + …)` in `K`; here for any `K`-algebra `L` over any base ring, the tuples being the monic factors of degrees `m` and `k`, the total degree being `n = m + k`”.

> `K`-algebra maps from the fibre ring `K ⊗_{R[a]} S` of the universal factorization map
> `φ : R[a] → S` to a `K`-algebra `L` correspond to factorizations over `L` of the image
> `x^n + α_{n-1} x^{n-1} + ⋯ + α_0` of the free monic polynomial into monic polynomials of degrees
> `m` and `k`. The factorization attached to `f` consists of the images under `f` of the two factors
> of the free monic polynomial over `S`.

```lean
noncomputable def universalFactorizationMapBaseChangeAlgHomEquiv (K L : Type*) [CommRing K]
    [CommRing L] [Algebra (MvPolynomial (Fin n) R) K] [Algebra K L]
    [Algebra (MvPolynomial (Fin n) R) L] [IsScalarTower (MvPolynomial (Fin n) R) K L] :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    (K ⊗[MvPolynomial (Fin n) R] (MvPolynomial (Fin m) R ⊗[R] MvPolynomial (Fin k) R) →ₐ[K] L) ≃
      {q : MonicDegreeEq L m × MonicDegreeEq L k //
        q.1.1 * q.2.1 = (freeMonic R n).map (algebraMap (MvPolynomial (Fin n) R) L)}
```

**`Polynomial.finite_monicDegreeEq_mul_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L137). The attribute's comment: “the source's finiteness of the set of tuples `β, γ` in a field `K` with `x^{n+m} + α_1 x^{n+m-1} + … = (x^n + β_1 x^{n-1} + …)(x^m + γ_1 x^{m-1} + …)`; here for any polynomial over any field, with factor degrees `m` and `k`”.

> Over a field `L`, a polynomial has only finitely many factorizations into monic polynomials of
> given degrees `m` and `k`.

```lean
theorem finite_monicDegreeEq_mul_eq (L : Type*) [Field L] (m k : ℕ) (p : L[X]) :
    Finite {q : MonicDegreeEq L m × MonicDegreeEq L k // q.1.1 * q.2.1 = p}
```

**`MvPolynomial.isIntegral_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L166). The attribute's comment: “the source's last paragraph: each of `b_i, c_j` is integral over `R`; here every element of `S`, over any base ring, the total degree being `n = m + k`”.

> Every element of `S` is integral over `R[a]` under the universal factorization map.

```lean
theorem isIntegral_universalFactorizationMap :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Algebra.IsIntegral (MvPolynomial (Fin n) R)
      (MvPolynomial (Fin m) R ⊗[R] MvPolynomial (Fin k) R)
```

**`MvPolynomial.finite_primeSpectrum_tensorProduct_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L192). The attribute's comment: “the source's statement that all fibres have finitely many closed points; here all points, over any base ring, the total degree being `n = m + k`”.

> Every fibre `K ⊗_{R[a]} S` of the universal factorization map `R[a] → S` over a field `K` has
> finitely many points.

```lean
theorem finite_primeSpectrum_tensorProduct_universalFactorizationMap (K : Type*) [Field K]
    [Algebra (MvPolynomial (Fin n) R) K] :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Finite (PrimeSpectrum
      (K ⊗[MvPolynomial (Fin n) R] (MvPolynomial (Fin m) R ⊗[R] MvPolynomial (Fin k) R)))
```

**`MvPolynomial.ringKrullDim_tensorProduct_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L205). The attribute's comment: “the source's statement that all fibres have dimension `0`, over any base ring, the total degree being `n = m + k`; the fibre over a prime `p` is the case `K = κ(p)`”.

> Every nonempty fibre `K ⊗_{R[a]} S` of the universal factorization map `R[a] → S` over a field
> `K` has dimension `0`.

```lean
theorem ringKrullDim_tensorProduct_universalFactorizationMap (K : Type*) [Field K]
    [Algebra (MvPolynomial (Fin n) R) K] :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Nontrivial
        (K ⊗[MvPolynomial (Fin n) R] (MvPolynomial (Fin m) R ⊗[R] MvPolynomial (Fin k) R)) →
      ringKrullDim
        (K ⊗[MvPolynomial (Fin n) R] (MvPolynomial (Fin m) R ⊗[R] MvPolynomial (Fin k) R)) = 0
```

**`MvPolynomial.universalFactorizationMapPresentation_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L223). The attribute's comment: “the source's `S` is a relative global complete intersection over `R`, for the presentation by the `b_i, c_j` and the equations `a_k = a_k(b_i, c_j)`, over any base ring, the total degree being `n = m + k`”.

> The canonical presentation `S = R[a][b, c]/(a_l - a_l(b, c))` of the universal factorization
> map, with `m + k` variables and `n = m + k` relations, is a relative global complete
> intersection.

```lean
theorem universalFactorizationMapPresentation_isRelativeGlobalCompleteIntersection :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Algebra.Presentation.IsRelativeGlobalCompleteIntersection
      (universalFactorizationMapPresentation R n m k hn).toPresentation
```

**`MvPolynomial.isRelativeGlobalCompleteIntersection_universalFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L236). The attribute's comment: “the source's `R → S` is a relative global complete intersection, as a property of the ring map, over any base ring, the total degree being `n = m + k`”.

> The universal factorization map `R[a_0, …, a_{n-1}] → R[b] ⊗_R R[c]` is a relative global
> complete intersection.

```lean
theorem isRelativeGlobalCompleteIntersection_universalFactorizationMap :
    letI := (universalFactorizationMap R n m k hn).toAlgebra
    Algebra.IsRelativeGlobalCompleteIntersection (MvPolynomial (Fin n) R)
      (MvPolynomial (Fin m) R ⊗[R] MvPolynomial (Fin k) R)
```

Declarations registered for the tag:

- [`MvPolynomial.universalFactorizationMapPresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MvPolynomial.universalFactorizationMapPresentation#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L61) (StacksFrontier): “the source's `S` generated over `R` by the `n + m` elements `b_i, c_j`, with the `n + m` equations `a_k = a_k(b_i, c_j)`: a presentation with variables `Fin m ⊕ Fin k` and relations `Fin n`, over any base ring, the total degree being `n = m + k`”.
- [`MvPolynomial.finite_universalFactorizationMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MvPolynomial.finite_universalFactorizationMap#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/UniversalFactorization.lean#L66) (StacksFrontier): “the source's last paragraph: `R → S` is a finite ring map, over any base ring, the total degree being `n = m + k`”.

## Tag 00SS, a lemma

[Tag 00SS](https://stacks.math.columbia.edu/tag/00SS) in the Stacks Project.

**`Algebra.IsRelativeGlobalCompleteIntersection.baseChange_and_localization_away_and_localization_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Relative.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Relative.lean#L314). The attribute's comment: “The three parts are the three conjuncts, with the auxiliary rings quantified inside the statement so that each carries only its own data, and each part is available separately as `baseChange`, `of_isLocalizationAway` and `localization_base`. Part (1) is over an arbitrary pushout square `Algebra.IsPushout R S R' S'`, the orientation of the sibling 00SN, with nothing assumed about `R → R'`; part (2) over an arbitrary `IsLocalization.Away g S'`, the source's `h` restricting nothing since `R[x_1, …, x_n] → S` is surjective; part (3) over a localization at an arbitrary submonoid `M ⊆ R` rather than only at the powers of one `f ∈ R`, the factorization `R → Rₘ → S` being `[Algebra Rₘ S]` with `[IsScalarTower R Rₘ S]`. See the module docstring.”.

> Let `S = R[x_1, …, x_n]/(f_1, …, f_c)` be a relative global complete intersection over `R`.
> Then
>
> 1. for any ring map `R → R'` the base change `S' = R' ⊗_R S` is a relative global complete
>    intersection over `R'`, presented as `R'[x_1, …, x_n]/(f_1, …, f_c)`;
> 2. for any `g ∈ S`, the image of some `h ∈ R[x_1, …, x_n]`, the localization `S_g` is a relative
>    global complete intersection over `R`, presented as
>    `R[x_1, …, x_n, x_{n+1}]/(f_1, …, f_c, hx_{n+1} - 1)`;
> 3. if `R → S` factors through a localization `R_M` of `R`, then `S` is a relative global complete
>    intersection over `R_M`, presented as `R_M[x_1, …, x_n]/(f_1, …, f_c)`.

```lean
public theorem baseChange_and_localization_away_and_localization_base (R : Type u) (S : Type v)
    [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.IsRelativeGlobalCompleteIntersection R S] :
    (∀ (R' : Type u') (S' : Type v') [CommRing R'] [CommRing S'] [Algebra R R'] [Algebra R S']
        [Algebra S S'] [Algebra R' S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
        [Algebra.IsPushout R S R' S'], Algebra.IsRelativeGlobalCompleteIntersection R' S') ∧
      (∀ (g : S) (S' : Type w) [CommRing S'] [Algebra S S'] [Algebra R S'] [IsScalarTower R S S']
        [IsLocalization.Away g S'], Algebra.IsRelativeGlobalCompleteIntersection R S') ∧
      (∀ (M : Submonoid R) (Rₘ : Type t) [CommRing Rₘ] [Algebra R Rₘ] [IsLocalization M Rₘ]
        [Algebra Rₘ S] [IsScalarTower R Rₘ S],
          Algebra.IsRelativeGlobalCompleteIntersection Rₘ S)
```

**`Algebra.IsRelativeGlobalCompleteIntersection.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Relative.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Relative.lean#L333). The attribute's comment: “Part (1), over an arbitrary pushout square `Algebra.IsPushout R S R' S'` — the orientation and binders of the sibling 00SN, `Algebra.IsPushout.syntomic`.”.

> The base change of a relative global complete intersection is a relative global complete
> intersection: if `S = R[x_1, …, x_n]/(f_1, …, f_c)` is one over `R` and
> `Algebra.IsPushout R S R' S'`, so that `S' = R' ⊗_R S = R'[x_1, …, x_n]/(f_1, …, f_c)`, then `S'`
> is a relative global complete intersection over `R'`. Nothing is assumed about `R → R'`.

```lean
public theorem baseChange (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    (R' : Type u') (S' : Type v') [CommRing R'] [CommRing S'] [Algebra R R'] [Algebra R S']
    [Algebra S S'] [Algebra R' S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
    [Algebra.IsPushout R S R' S'] [Algebra.IsRelativeGlobalCompleteIntersection R S] :
    Algebra.IsRelativeGlobalCompleteIntersection R' S'
```

**`Algebra.IsRelativeGlobalCompleteIntersection.of_isLocalizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Relative.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Relative.lean#L348). The attribute's comment: “Part (2), for an arbitrary localization away from `g`; the source's `h` restricts nothing, since `R[x_1, …, x_n] → S` is surjective. Binders as in `Algebra.FinitePresentation.of_isLocalizationAway`, the same statement for finite presentation.”.

> A localization of a relative global complete intersection away from an element is a relative
> global complete intersection: if `S = R[x_1, …, x_n]/(f_1, …, f_c)` is one over `R`, `g ∈ S` is the
> image of `h ∈ R[x_1, …, x_n]`, and `S'` is the localization `S_g`, then
> `S' = R[x_1, …, x_n, x_{n+1}]/(f_1, …, f_c, hx_{n+1} - 1)` is a relative global complete
> intersection over `R`.

```lean
public theorem of_isLocalizationAway {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.IsRelativeGlobalCompleteIntersection R S] (g : S) {S' : Type w}
    [CommRing S'] [Algebra S S'] [Algebra R S'] [IsScalarTower R S S'] [IsLocalization.Away g S'] :
    Algebra.IsRelativeGlobalCompleteIntersection R S'
```

**`Algebra.IsRelativeGlobalCompleteIntersection.localization_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Relative.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Relative.lean#L361). The attribute's comment: “Part (3), for a localization at an arbitrary submonoid `M ⊆ R` rather than only at the powers of one `f ∈ R`; the factorization `R → Rₘ → S` is `[Algebra Rₘ S]` with `[IsScalarTower R Rₘ S]`. Binders as in `Algebra.FormallySmooth.localization_base`.”.

> A relative global complete intersection over `R` whose structure map factors through a
> localization `Rₘ` of `R` is a relative global complete intersection over `Rₘ`: if
> `S = R[x_1, …, x_n]/(f_1, …, f_c)` is one over `R` and `R → S` factors as `R → Rₘ → S`, then
> `S = Rₘ[x_1, …, x_n]/(f_1, …, f_c)` is a relative global complete intersection over `Rₘ`.

```lean
public theorem localization_base {R : Type u} [CommRing R] (M : Submonoid R) {S : Type v}
    [CommRing S] [Algebra R S] [Algebra.IsRelativeGlobalCompleteIntersection R S] {Rₘ : Type t}
    [CommRing Rₘ] [Algebra R Rₘ] [IsLocalization M Rₘ] [Algebra Rₘ S] [IsScalarTower R Rₘ S] :
    Algebra.IsRelativeGlobalCompleteIntersection Rₘ S
```

## Tag 00ST, a lemma

[Tag 00ST](https://stacks.math.columbia.edu/tag/00ST) in the Stacks Project.

**`Algebra.Presentation.exists_sub_one_mem_map_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Relative.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Relative.lean#L538). The attribute's comment: “(1): the fibre of `Spec(S/IS) → Spec(R/I)` over `𝔭/I` is the fibre `κ(𝔭) ⊗_R S = 𝔭.Fiber S` of `Spec(S) → Spec(R)` over `𝔭 ⊇ I`, and only nonempty fibres are constrained, as in Definition 00SP; `g ↦ 1 ∈ S/IS` is `g - 1 ∈ IS`. The presentation of `S_g` is `Algebra.Presentation.localizationAwayComp`.”.

> Let `S = R[x_1, …, x_n]/(f_1, …, f_c)`, presented by `P`, and let `I ⊆ R`
> be an ideal such that the fibres of `Spec(S/IS) → Spec(R/I)` have dimension `n - c`, that is, every
> nonempty fibre of `Spec(S) → Spec(R)` over a prime `𝔭 ⊇ I` has dimension `n - c`. Then there is an
> `h ∈ R[x_1, …, x_n]` whose image `g ∈ S` maps to `1 ∈ S/IS`, such that
> `S_g = R[x_1, …, x_n, x_{n+1}]/(f_1, …, f_c, h x_{n+1} - 1)` is a relative global complete
> intersection with this presentation.

```lean
theorem Algebra.Presentation.exists_sub_one_mem_map_isRelativeGlobalCompleteIntersection
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] {ι σ : Type*} [Finite ι] [Finite σ]
    (P : Algebra.Presentation R S ι σ) (I : Ideal R)
    (hI : ∀ (p : Ideal R) [p.IsPrime], I ≤ p → Nontrivial (p.Fiber S) →
      ringKrullDim (p.Fiber S) + ((Nat.card σ : ℕ) : WithBot ℕ∞) =
        ((Nat.card ι : ℕ) : WithBot ℕ∞)) :
    ∃ h : P.Ring, algebraMap P.Ring S h - 1 ∈ I.map (algebraMap R S) ∧
      (P.localizationAwayComp h
        (Localization.Away (algebraMap P.Ring S h))).IsRelativeGlobalCompleteIntersection
```

**`Algebra.Presentation.exists_isUnit_fiber_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Relative.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Relative.lean#L595). The attribute's comment: “(2): the fibre `S ⊗_R κ(𝔭)` is `𝔭.Fiber S = κ(𝔭) ⊗_R S`, in which `g` is `1 ⊗ g`, and `dim = n - c` is written additively as in Definition 00SP. The presentation of `S_g` is `Algebra.Presentation.localizationAwayComp`.”.

> Let `S = R[x_1, …, x_n]/(f_1, …, f_c)`, presented by `P`, and let `𝔭` be a
> prime of `R` with `dim(S ⊗_R κ(𝔭)) = n - c`. Then there is an `h ∈ R[x_1, …, x_n]` whose image
> `g ∈ S` maps to a unit of `S ⊗_R κ(𝔭)`, such that
> `S_g = R[x_1, …, x_n, x_{n+1}]/(f_1, …, f_c, h x_{n+1} - 1)` is a relative global complete
> intersection with this presentation.

```lean
theorem Algebra.Presentation.exists_isUnit_fiber_isRelativeGlobalCompleteIntersection
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] {ι σ : Type*} [Finite ι] [Finite σ]
    (P : Algebra.Presentation R S ι σ) (p : Ideal R) [p.IsPrime]
    (hp : ringKrullDim (p.Fiber S) + ((Nat.card σ : ℕ) : WithBot ℕ∞) =
      ((Nat.card ι : ℕ) : WithBot ℕ∞)) :
    ∃ h : P.Ring, IsUnit (Algebra.TensorProduct.includeRight (R := R) (A := p.ResidueField)
        (algebraMap P.Ring S h)) ∧
      (P.localizationAwayComp h
        (Localization.Away (algebraMap P.Ring S h))).IsRelativeGlobalCompleteIntersection
```

**`Algebra.Presentation.exists_notMem_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/Relative.lean, line 641](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/Relative.lean#L641). The attribute's comment: “(3): the presentation of `S_g` is `Algebra.Presentation.localizationAwayComp`, the source's `R[x_1, …, x_n, x_{n+1}]/(f_1, …, f_c, h x_{n+1} - 1)`, and `dim_𝔮(S/R) = n - c` is `Algebra.relativeDimensionAt R 𝔮 + c = n` (tag 00QD), written additively as in Definition 00SP. The numbers of variables and relations are `Nat.card ι` and `Nat.card σ`.”.

> Let `S = R[x_1, …, x_n]/(f_1, …, f_c)`, presented by `P`, and let `𝔮` be a
> prime of `S` with `dim_𝔮(S/R) = n - c`. Then there is an `h ∈ R[x_1, …, x_n]` whose image `g ∈ S`
> is not in `𝔮`, such that
> `S_g = R[x_1, …, x_n, x_{n+1}]/(f_1, …, f_c, h x_{n+1} - 1)` is a relative global complete
> intersection with this presentation.

```lean
theorem Algebra.Presentation.exists_notMem_isRelativeGlobalCompleteIntersection
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] {ι σ : Type*} [Finite ι] [Finite σ]
    (P : Algebra.Presentation R S ι σ) (q : Ideal S) [q.IsPrime]
    (hq : Algebra.relativeDimensionAt R q + ((Nat.card σ : ℕ) : WithBot ℕ∞) =
      ((Nat.card ι : ℕ) : WithBot ℕ∞)) :
    ∃ h : P.Ring, algebraMap P.Ring S h ∉ q ∧
      (P.localizationAwayComp h
        (Localization.Away (algebraMap P.Ring S h))).IsRelativeGlobalCompleteIntersection
```

## Tag 00SU, a lemma

[Tag 00SU](https://stacks.math.columbia.edu/tag/00SU) in the Stacks Project.

**`Algebra.Presentation.exists_fg_isRelativeGlobalCompleteIntersection_naive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/Morphisms.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/Morphisms.lean#L698). The attribute's comment: “The subalgebra is a finitely generated `Subalgebra ℤ R`, the relations over it are `f₀` with `MvPolynomial.map (algebraMap R₀ R) (f₀ k) = f_k`, and `S₀` is presented by `Algebra.Presentation.naive`. Stated for arbitrary finite index types.”.

> **Stacks 00SU.** Let `S = R[x_1, …, x_n]/(f_1, …, f_c)` be a relative global complete
> intersection. There is a finite type `ℤ`-subalgebra `R₀ ⊆ R` with `f_k ∈ R₀[x_1, …, x_n]` such
> that `S₀ = R₀[x_1, …, x_n]/(f_1, …, f_c)` is a relative global complete intersection.

```lean
theorem Algebra.Presentation.exists_fg_isRelativeGlobalCompleteIntersection_naive
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] {ι σ : Type*} [Finite ι] [Finite σ]
    (P : Algebra.Presentation R S ι σ) [P.IsRelativeGlobalCompleteIntersection] :
    ∃ (R₀ : Subalgebra ℤ R) (_ : R₀.FG) (f₀ : σ → MvPolynomial ι R₀),
      (∀ j, MvPolynomial.map (algebraMap R₀ R) (f₀ j) = P.relation j) ∧
        (Algebra.Presentation.naive (v := f₀)).IsRelativeGlobalCompleteIntersection
```

## Tag 00SV, a lemma

[Tag 00SV](https://stacks.math.columbia.edu/tag/00SV) in the Stacks Project.

**`Algebra.Presentation.isRegular_localization_relation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean, line 947](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean#L947). The attribute's comment: “(1): `RingTheory.Sequence.IsRegular` is Definition 00LF verbatim, nonvanishing clause included, for the list of images of `f_1, …, f_c` in `Localization.AtPrime 𝔮'`, `𝔮' = 𝔮 ∩ R[x_1, …, x_n]`.”.

> **Stacks 00SV (1).** Let `S = R[x_1, …, x_n]/(f_1, …, f_c)`, presented by `P`, be a relative
> global complete intersection (Definition 00SP). For every prime `𝔮` of `S`, with corresponding
> prime `𝔮'` of `R[x_1, …, x_n]`, the relations `f_1, …, f_c` form a regular sequence in the local
> ring `R[x_1, …, x_n]_{𝔮'}`.

```lean
theorem Algebra.Presentation.isRegular_localization_relation {R : Type*} [CommRing R] {S : Type*}
    [CommRing S] [Algebra R S] {ι : Type*} [Finite ι] {c : ℕ}
    (P : Algebra.Presentation R S ι (Fin c)) [P.IsRelativeGlobalCompleteIntersection]
    (q : Ideal S) [q.IsPrime] :
    RingTheory.Sequence.IsRegular (Localization.AtPrime (q.comap (algebraMap P.Ring S)))
      ((List.ofFn P.relation).map
        (algebraMap P.Ring (Localization.AtPrime (q.comap (algebraMap P.Ring S)))))
```

**`Algebra.Presentation.flat_localization_quotient_relation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean, line 964](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean#L964). The attribute's comment: “(2): `R[x_1, …, x_n]_{𝔮'}/(f_1, …, f_i)` is the quotient of `Localization.AtPrime 𝔮'` by the ideal generated by the first `i` images of the relations, for every `i : ℕ` (`List.take` saturates at `c`).”.

> **Stacks 00SV (2).** Let `S = R[x_1, …, x_n]/(f_1, …, f_c)`, presented by `P`, be a relative
> global complete intersection (Definition 00SP). For every prime `𝔮` of `S`, with corresponding
> prime `𝔮'` of `R[x_1, …, x_n]`, each of the rings `R[x_1, …, x_n]_{𝔮'}/(f_1, …, f_i)` is flat
> over `R`.

```lean
theorem Algebra.Presentation.flat_localization_quotient_relation {R : Type*} [CommRing R]
    {S : Type*} [CommRing S] [Algebra R S] {ι : Type*} [Finite ι] {c : ℕ}
    (P : Algebra.Presentation R S ι (Fin c)) [P.IsRelativeGlobalCompleteIntersection]
    (q : Ideal S) [q.IsPrime] (i : ℕ) :
    Module.Flat R (Localization.AtPrime (q.comap (algebraMap P.Ring S)) ⧸
      Ideal.ofList (((List.ofFn P.relation).map
        (algebraMap P.Ring (Localization.AtPrime (q.comap (algebraMap P.Ring S))))).take i))
```

**`Algebra.Presentation.exists_basis_cotangent_relation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean, line 981](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean#L981). The attribute's comment: “(3): the conormal module `I/I²` is `P.toExtension.Cotangent`, and the basis is pinned: its `i`-th vector is the class of the relation `f_i`.”.

> **Stacks 00SV (3).** Let `S = R[x_1, …, x_n]/(f_1, …, f_c)`, presented by `P`, be a relative
> global complete intersection (Definition 00SP). Then the conormal module `I/I²` of
> `I = (f_1, …, f_c)` is free over `S` on the classes of `f_1, …, f_c`.

```lean
theorem Algebra.Presentation.exists_basis_cotangent_relation {R : Type*} [CommRing R] {S : Type*}
    [CommRing S] [Algebra R S] {ι : Type*} [Finite ι] {c : ℕ}
    (P : Algebra.Presentation R S ι (Fin c)) [P.IsRelativeGlobalCompleteIntersection] :
    ∃ b : Module.Basis (Fin c) S P.toExtension.Cotangent,
      ∀ i, b i = Algebra.Extension.Cotangent.mk ⟨P.relation i, P.relation_mem_ker i⟩
```

## Tag 00SW, a lemma

[Tag 00SW](https://stacks.math.columbia.edu/tag/00SW) in the Stacks Project.

**`Algebra.Syntomic.of_isRelativeGlobalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/RelativeGlobalCompleteIntersection.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/RelativeGlobalCompleteIntersection.lean#L138). The attribute's comment: “Stated for the class `Algebra.IsRelativeGlobalCompleteIntersection R S` and concluding `Algebra.Syntomic R S`, the whole of Definition 00SL, not only the flatness that the source's "i.e., flat" singles out.”.

> A relative global complete intersection is syntomic: if `S = R[x_1, …, x_n]/(f_1, …, f_c)`
> is a relative global complete intersection over `R`, then `R → S` is flat, of finite
> presentation, and its fibres are local complete intersections over the residue fields.

```lean
theorem Algebra.Syntomic.of_isRelativeGlobalCompleteIntersection (R S : Type*) [CommRing R]
    [CommRing S] [Algebra R S] [Algebra.IsRelativeGlobalCompleteIntersection R S] :
    Algebra.Syntomic R S
```

## Tag 03HS, a lemma

[Tag 03HS](https://stacks.math.columbia.edu/tag/03HS) in the Stacks Project.

**`Polynomial.Monic.exists_finite_free_faithfullyFlat_syntomic_map_eq_prod_X_sub_C`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/SplittingExtension.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/SplittingExtension.lean#L287). The attribute's comment: “The source's finite free faithfully flat *extension* `A ⊂ A'`: the injectivity of `algebraMap A A'` is not a conjunct, being `FaithfulSMul.algebraMap_injective` applied to `Module.FaithfullyFlat A A'`. The splitting is the explicit product over `Fin P.natDegree`, which names the roots the consumers use and is stronger than `Polynomial.Splits`. Unlike the Mathlib sibling `Polynomial.Monic.exists_splits_map`, no `Nontrivial A` is assumed and the extension is also faithfully flat and syntomic (Definition 00SL). See the module docstring.”.

> **Stacks 03HS.** Let `A` be a ring and let `P ∈ A[x]` be monic. There is a finite free,
> faithfully flat, syntomic extension `A ⊂ A'` and elements `β_1, …, β_n ∈ A'`, `n = deg P`, with
> `P = ∏ (x - β_i)` in `A'[x]`. The inclusion `A ⊂ A'` is the faithful flatness: it gives
> `FaithfulSMul A A'`, hence `algebraMap A A'` injective.

```lean
public theorem Polynomial.Monic.exists_finite_free_faithfullyFlat_syntomic_map_eq_prod_X_sub_C
    {A : Type u} [CommRing A] {P : A[X]} (hP : P.Monic) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra A A') (_ : Module.Finite A A')
      (_ : Module.Free A A') (_ : Module.FaithfullyFlat A A') (_ : Algebra.Syntomic A A')
      (β : Fin P.natDegree → A'), P.map (algebraMap A A') = ∏ i, (X - C (β i))
```

## Tag 00SY, a lemma

[Tag 00SY](https://stacks.math.columbia.edu/tag/00SY) in the Stacks Project.

**`Algebra.exists_notMem_syntomic_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/SyntomicAt.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/SyntomicAt.lean#L561). The attribute's comment: “The principal localization `S_g` is `Localization.Away g`, the local ring map `R_𝔭 → S_𝔮` is `Localization.localRingHom` for the lying-over relation, and `S_𝔮/𝔭S_𝔮` is the fibre `𝔭.Fiber S_𝔮 = κ(𝔭) ⊗_R S_𝔮`, canonically a `κ(𝔭)`-algebra, which is `S_𝔮/𝔭S_𝔮` because `S_𝔮` is an `R_𝔭`-algebra.”.

> Let `R → S` be a ring map and let `𝔮` be a prime of `S` lying over the prime `𝔭` of `R`. The
> following are equivalent:
>
> 1. there is a `g ∈ S`, `g ∉ 𝔮`, such that `R → S_g` is syntomic;
> 2. there is a `g ∈ S`, `g ∉ 𝔮`, such that `S_g` is a relative global complete intersection over
>    `R`;
> 3. there is a `g ∈ S`, `g ∉ 𝔮`, such that `R → S_g` is of finite presentation, the local ring map
>    `R_𝔭 → S_𝔮` is flat, and `S_𝔮/𝔭S_𝔮` is a complete intersection over `κ(𝔭)`.

```lean
theorem Algebra.exists_notMem_syntomic_tfae {R S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p] :
    List.TFAE
      [∃ g ∉ q, Algebra.Syntomic R (Localization.Away g),
        ∃ g ∉ q, Algebra.IsRelativeGlobalCompleteIntersection R (Localization.Away g),
        ∃ g ∉ q,
          Algebra.FinitePresentation R (Localization.Away g) ∧
            (letI : Algebra (Localization.AtPrime p) (Localization.AtPrime q) :=
              (Localization.localRingHom p q (algebraMap R S) (q.over_def p)).toAlgebra
             Module.Flat (Localization.AtPrime p) (Localization.AtPrime q)) ∧
              IsCompleteIntersection p.ResidueField (p.Fiber (Localization.AtPrime q))]
```

## Tag 07BT, a lemma

[Tag 07BT](https://stacks.math.columbia.edu/tag/07BT) in the Stacks Project.

**`Algebra.Generators.finite_and_projective_tensor_cotangent_of_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/Morphisms.lean, line 918](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/Morphisms.lean#L918). The attribute's comment: “The presentation `R[x_1, …, x_n] → S` is `Algebra.Generators R S (Fin n)`, `I/I²` is its cotangent module `P.toExtension.Cotangent`, and `(I/I²)_g` is the base change `T ⊗_S I/I²` to a localization `T` of `S` away from `g`. The source's hypothesis that `I` is finitely generated is not needed.”.

> **Stacks 07BT.** Let `S = R[x_1, …, x_n]/I` and let `g ∈ S` be such that `S_g` is syntomic
> over `R`. Then `(I/I²)_g` is a finite projective `S_g`-module.

```lean
theorem Algebra.Generators.finite_and_projective_tensor_cotangent_of_syntomic {R S T : Type*}
    [CommRing R] [CommRing S] [CommRing T] [Algebra R S] [Algebra R T] [Algebra S T]
    [IsScalarTower R S T] (g : S) [IsLocalization.Away g T] [Algebra.Syntomic R T] {n : ℕ}
    (P : Algebra.Generators R S (Fin n)) :
    Module.Finite T (T ⊗[S] P.toExtension.Cotangent) ∧
      Module.Projective T (T ⊗[S] P.toExtension.Cotangent)
```

## Tag 00SZ, a lemma

[Tag 00SZ](https://stacks.math.columbia.edu/tag/00SZ) in the Stacks Project.

**`Algebra.IsRelativeGlobalCompleteIntersection.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/Morphisms.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/Morphisms.lean#L477). The attribute's comment: “(2). Stated for the class `Algebra.IsRelativeGlobalCompleteIntersection` along a scalar tower `R → S → S'`; the composite presentation is `Algebra.Presentation.isRelativeGlobalCompleteIntersection_comp`.”.

> **Stacks 00SZ (2).** If `R → S` and `S → S'` are relative global complete intersections,
> then so is `R → S'`.

```lean
theorem Algebra.IsRelativeGlobalCompleteIntersection.comp (R S S' : Type*) [CommRing R]
    [CommRing S] [CommRing S'] [Algebra R S] [Algebra S S'] [Algebra R S'] [IsScalarTower R S S']
    [Algebra.IsRelativeGlobalCompleteIntersection R S]
    [Algebra.IsRelativeGlobalCompleteIntersection S S'] :
    Algebra.IsRelativeGlobalCompleteIntersection R S'
```

**`Algebra.Syntomic.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/Morphisms.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/Morphisms.lean#L490). The attribute's comment: “(1). Stated for the class `Algebra.Syntomic` along a scalar tower `R → S → S'`.”.

> **Stacks 00SZ (1).** If `R → S` and `S → S'` are syntomic, then so is `R → S'`.

```lean
theorem Algebra.Syntomic.comp (R S S' : Type*) [CommRing R] [CommRing S] [CommRing S']
    [Algebra R S] [Algebra S S'] [Algebra R S'] [IsScalarTower R S S'] [Algebra.Syntomic R S]
    [Algebra.Syntomic S S'] : Algebra.Syntomic R S'
```

## Tag 00T0, a lemma

[Tag 00T0](https://stacks.math.columbia.edu/tag/00T0) in the Stacks Project.

**`Algebra.Syntomic.exists_span_eq_top_algEquiv_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Syntomic/Morphisms.lean, line 852](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Syntomic/Morphisms.lean#L852). The attribute's comment: “The syntomic `R/I`-algebra `S̄` is an `R`-algebra through `R → R/I`, the elements `ḡ_i` are a set `s` with `Ideal.span s = ⊤`, and `S̄_{ḡ_i} ≅ S_i/IS_i` is an isomorphism of `R`-algebras.”.

> **Stacks 00T0.** Let `I ⊆ R` be an ideal and let `R/I → S̄` be syntomic. There are
> elements `ḡ_i ∈ S̄` generating the unit ideal such that every `S̄_{ḡ_i}` is isomorphic to
> `S_i/IS_i` for a relative global complete intersection `S_i` over `R`.

```lean
theorem Algebra.Syntomic.exists_span_eq_top_algEquiv_quotient {R : Type u} [CommRing R]
    (I : Ideal R) {S : Type v} [CommRing S] [Algebra R S] [Algebra (R ⧸ I) S]
    [IsScalarTower R (R ⧸ I) S] [Algebra.Syntomic (R ⧸ I) S] :
    ∃ s : Set S, Ideal.span s = ⊤ ∧ ∀ g ∈ s, ∃ (T : Type u) (_ : CommRing T) (_ : Algebra R T),
      Algebra.IsRelativeGlobalCompleteIntersection R T ∧
        Nonempty ((T ⧸ I.map (algebraMap R T)) ≃ₐ[R] Localization.Away g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.136, Tag 00SK](https://stacks.math.columbia.edu/tag/00SK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
