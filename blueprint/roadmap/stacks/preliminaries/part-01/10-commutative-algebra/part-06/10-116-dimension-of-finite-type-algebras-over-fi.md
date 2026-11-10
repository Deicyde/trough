---
declaration: section
origin: cited
lean: ringKrullDim_eq_trdeg_and_ringKrullDim_localization_eq_trdeg, Ideal.trdeg_residueField_lt_trdeg_residueField_of_lt, PrimeSpectrum.localKrullDim_eq_height_add_trdeg_residueField, PrimeSpectrum.localKrullDim_comap_add_height_eq_localKrullDim_add_height_comap, Algebra.IsPushout.ringKrullDim_eq, Algebra.IsPushout.localKrullDim_comap_eq, Algebra.IsPushout.height_fiber_add_height_eq_and_add_trdeg_eq
statement: formalized
proof: formalized
---

# 10.116 Dimension of finite type algebras over fields, reprise

Section 10.116 of the Stacks Project, [Tag 07NB](https://stacks.math.columbia.edu/tag/07NB). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00P0, a lemma

[Tag 00P0](https://stacks.math.columbia.edu/tag/00P0) in the Stacks Project.

**`ringKrullDim_eq_trdeg_and_ringKrullDim_localization_eq_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/FiniteTypeOverField.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/FiniteTypeOverField.lean#L255). The attribute's comment: “The transcendence degree is compared through `Cardinal.toENat`, the field of fractions is an abstract `IsFractionRing` and the local ring an abstract `IsLocalization.AtPrime`. See the module docstring.”. References: EGA IV (5.5.8), “special case”.

> **Stacks 00P0.** Let `k` be a field, let `S` be a finite type `k`-algebra which is a domain,
> and let `K` be its field of fractions. Then the Krull dimension of `S` is the transcendence
> degree of `K` over `k`, and the local ring of `S` at every maximal ideal has that same
> dimension.

```lean
public theorem ringKrullDim_eq_trdeg_and_ringKrullDim_localization_eq_trdeg
    (k : Type u) [Field k] (S : Type v) [CommRing S] [IsDomain S] [Algebra k S]
    [Algebra.FiniteType k S] (K : Type w) [Field K] [Algebra S K] [IsFractionRing S K]
    [Algebra k K] [IsScalarTower k S K] :
    ringKrullDim S = (Cardinal.toENat (Algebra.trdeg k K) : WithBot ℕ∞) ∧
      ∀ (𝔪 : Ideal S) [𝔪.IsMaximal] (A : Type x) [CommRing A] [Algebra S A]
          [IsLocalization.AtPrime A 𝔪],
        ringKrullDim A = (Cardinal.toENat (Algebra.trdeg k K) : WithBot ℕ∞)
```

## Tag 06RP, a lemma

[Tag 06RP](https://stacks.math.columbia.edu/tag/06RP) in the Stacks Project.

**`Ideal.trdeg_residueField_lt_trdeg_residueField_of_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TranscendenceDegree/ResidueField.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TranscendenceDegree/ResidueField.lean#L193). The attribute's comment: “The residue field `κ(𝔮)` is Mathlib's `Ideal.ResidueField`, the fraction field of `S ⧸ 𝔮`, and the comparison is a strict inequality of `Cardinal`, both degrees being finite. See the module docstring.”.

> **Stacks 06RP.** Let `k` be a field, let `S` be a finite type `k`-algebra, and let
> `𝔮 ⊊ 𝔮'` be prime ideals of `S`. Then the transcendence degree over `k` of the residue field
> `κ(𝔮')` is strictly smaller than that of `κ(𝔮)`.

```lean
public theorem Ideal.trdeg_residueField_lt_trdeg_residueField_of_lt
    (k : Type u) [Field k] {S : Type v} [CommRing S] [Algebra k S] [Algebra.FiniteType k S]
    {q q' : Ideal S} [q.IsPrime] [q'.IsPrime] (h : q < q') :
    Algebra.trdeg k q'.ResidueField < Algebra.trdeg k q.ResidueField
```

## Tag 00P1, a lemma

[Tag 00P1](https://stacks.math.columbia.edu/tag/00P1) in the Stacks Project.

**`PrimeSpectrum.localKrullDim_eq_height_add_trdeg_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/LocalDimension.lean, line 783](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/LocalDimension.lean#L783). The attribute's comment: “`dim_x X` is `TopologicalSpace.localKrullDim`, Definition 0055 (4); `dim(S_𝔭)` is `𝔭.height`, `κ(𝔭)` is `Ideal.ResidueField`, and the transcendence degree is compared through `Cardinal.toENat`. See the module docstring.”. References: EGA IV (17.15.8), “special case”.

> **Stacks 00P1.** Let `k` be a field, let `S` be a finite type `k`-algebra, let `X = Spec S`,
> and let `x ∈ X` be a point, with prime ideal `𝔭 = x.asIdeal`. Then the dimension of `X` at `x` —
> the least dimension of an open neighbourhood of `x` — is the height of `𝔭` plus the transcendence
> degree over `k` of the residue field `κ(𝔭)`.

```lean
public theorem localKrullDim_eq_height_add_trdeg_residueField
    (k : Type u) [Field k] {S : Type v} [CommRing S] [Algebra k S] [Algebra.FiniteType k S]
    (x : PrimeSpectrum S) :
    TopologicalSpace.localKrullDim (PrimeSpectrum S) x =
      ((x.asIdeal.height + Cardinal.toENat (Algebra.trdeg k x.asIdeal.ResidueField) : ℕ∞) :
        WithBot ℕ∞)
```

## Tag 00P2, a lemma

[Tag 00P2](https://stacks.math.columbia.edu/tag/00P2) in the Stacks Project.

**`PrimeSpectrum.localKrullDim_comap_add_height_eq_localKrullDim_add_height_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Codimension.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Codimension.lean#L164). The attribute's comment: “`dim_x X` is `TopologicalSpace.localKrullDim`, Definition 0055 (4), and `height 𝔭` is `Ideal.height`, as in the sibling 00P1; the source's difference of differences is stated as the equivalent equality of sums, subtraction in `WithBot ℕ∞` being truncated. See the module docstring.”.

> **Stacks 00P2.** Let `k` be a field, let `f : S' → S` be a surjection of finite type
> `k`-algebras, let `x ∈ Spec S` be a point and let `x' = comap f x` be the corresponding point of
> `Spec S'`. Then the dimension of `Spec S'` at `x'` exceeds the dimension of `Spec S` at `x` by
> exactly the amount by which the height of `x'` exceeds the height of `x`.

```lean
public theorem localKrullDim_comap_add_height_eq_localKrullDim_add_height_comap
    (k : Type u) [Field k] {S' : Type v} {S : Type w} [CommRing S'] [CommRing S]
    [Algebra k S'] [Algebra k S] [Algebra.FiniteType k S'] (f : S' →ₐ[k] S)
    (hf : Function.Surjective f) (x : PrimeSpectrum S) :
    TopologicalSpace.localKrullDim (PrimeSpectrum S') (comap f.toRingHom x) +
        (x.asIdeal.height : WithBot ℕ∞) =
      TopologicalSpace.localKrullDim (PrimeSpectrum S) x +
        ((comap f.toRingHom x).asIdeal.height : WithBot ℕ∞)
```

## Tag 00P3, a lemma

[Tag 00P3](https://stacks.math.columbia.edu/tag/00P3) in the Stacks Project.

**`Algebra.IsPushout.ringKrullDim_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/BaseChange.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/BaseChange.lean#L246). The attribute's comment: “The base change `K ⊗_k S` is an arbitrary pushout square of `k`-algebras `Algebra.IsPushout k K S T`; the source's literal form is `inferInstance` once `Algebra.TensorProduct.rightAlgebra` is a local instance. See the module docstring.”.

> **Stacks 00P3.** Let `k` be a field, let `S` be a `k`-algebra of finite type and let `K/k` be a
> field extension. Then `S` and its base change `T = K ⊗_k S` have the same Krull dimension.

```lean
public theorem Algebra.IsPushout.ringKrullDim_eq (k K S T : Type*) [Field k] [Field K]
    [CommRing S] [CommRing T] [Algebra k K] [Algebra k S] [Algebra k T] [Algebra K T]
    [Algebra S T] [IsScalarTower k K T] [IsScalarTower k S T] [Algebra.IsPushout k K S T]
    [Algebra.FiniteType k S] :
    ringKrullDim S = ringKrullDim T
```

## Tag 00P4, a lemma

[Tag 00P4](https://stacks.math.columbia.edu/tag/00P4) in the Stacks Project.

**`Algebra.IsPushout.localKrullDim_comap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/BaseChange.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/BaseChange.lean#L570). The attribute's comment: “`dim_x X` is `TopologicalSpace.localKrullDim`, Definition 0055 (4), as in the siblings 00P1 and 00P2; the base change `K ⊗_k S` is an arbitrary pushout square of `k`-algebras `Algebra.IsPushout k K S T`, as in the sibling 00P3; and `q_K` lying over `q` is expressed by taking `x = PrimeSpectrum.comap (algebraMap S T) xK`. See the module docstring.”.

> **Stacks 00P4.** Let `k` be a field, let `S` be a finite type `k`-algebra, let `K/k` be a
> field extension and let `T = K ⊗_k S` be the base change, presented as a pushout square. Let
> `xK ∈ Spec T` be a point, with prime `q_K`, and let `x = comap (algebraMap S T) xK ∈ Spec S` be
> the point of the prime `q = q_K ∩ S` that it lies over. Then `Spec S` has the same dimension at
> `x` as `Spec T` has at `xK`.

```lean
public theorem localKrullDim_comap_eq (k K S T : Type*) [Field k] [Field K]
    [CommRing S] [CommRing T] [Algebra k K] [Algebra k S] [Algebra k T] [Algebra K T]
    [Algebra S T] [IsScalarTower k K T] [IsScalarTower k S T] [Algebra.IsPushout k K S T]
    [Algebra.FiniteType k S] (xK : PrimeSpectrum T) :
    TopologicalSpace.localKrullDim (PrimeSpectrum S)
        (PrimeSpectrum.comap (algebraMap S T) xK) =
      TopologicalSpace.localKrullDim (PrimeSpectrum T) xK
```

## Tag 0CWE, a lemma

[Tag 0CWE](https://stacks.math.columbia.edu/tag/0CWE) in the Stacks Project.

**`Algebra.IsPushout.height_fiber_add_height_eq_and_add_trdeg_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/BaseChange.lean, line 873](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/BaseChange.lean#L873). The attribute's comment: “The dimension of the fibre `(S_K ⊗_S κ(𝔮))_{𝔮_K}` is the height of the image of `𝔮_K` in `S_K ⧸ 𝔮 S_K`, Mathlib's spelling in the going-down height formula (Lemma 00ON); the two equalities are stated additively rather than with a truncated subtraction in `ℕ∞`; the base change `K ⊗_k S` is an arbitrary pushout square of `k`-algebras, as in the siblings 00P3 and 00P4; and transcendence degrees are compared through `Cardinal.toENat`, as in 00P1. See the module docstring.”.

> **Stacks 0CWE.** Let `k` be a field, let `S` be a finite type `k`-algebra, let `K/k` be a
> field extension and let `T = K ⊗_k S` be the base change, presented as a pushout square. Then for
> every prime `q` of `S` and every prime `Q` of `T` lying over `q`, the dimension of the fibre ring
> `(T ⊗_S κ(q))_Q` — the height of the image of `Q` in `T ⧸ q T` — added to `dim S_q` gives
> `dim T_Q`, and added to `trdeg_K κ(Q)` gives `trdeg_k κ(q)`. Moreover, given `q` there is a prime
> `Q` over `q` for which this dimension is zero.

```lean
public theorem height_fiber_add_height_eq_and_add_trdeg_eq (k K S T : Type*) [Field k] [Field K]
    [CommRing S] [CommRing T] [Algebra k K] [Algebra k S] [Algebra k T] [Algebra K T]
    [Algebra S T] [IsScalarTower k K T] [IsScalarTower k S T] [Algebra.IsPushout k K S T]
    [Algebra.FiniteType k S] :
    (∀ (q : Ideal S) [q.IsPrime] (Q : Ideal T) [Q.IsPrime] [Q.LiesOver q],
        (Q.map (Ideal.Quotient.mk (q.map (algebraMap S T)))).height + q.height = Q.height ∧
        (Q.map (Ideal.Quotient.mk (q.map (algebraMap S T)))).height
            + Cardinal.toENat (Algebra.trdeg K Q.ResidueField)
          = Cardinal.toENat (Algebra.trdeg k q.ResidueField)) ∧
      ∀ (q : Ideal S) [q.IsPrime], ∃ (Q : Ideal T) (_ : Q.IsPrime) (_ : Q.LiesOver q),
        (Q.map (Ideal.Quotient.mk (q.map (algebraMap S T)))).height = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.116, Tag 07NB](https://stacks.math.columbia.edu/tag/07NB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
