---
declaration: section
origin: cited
lean: Algebra.FormallyUnramified.tfae_isSeparable_unramified_etale, KaehlerDifferential.D_eq_zero_iff_exists_pow_eq, IntermediateField.finrank_adjoin_eq_pow_of_linearIndependent_D, Algebra.isSeparableExtension_iff_injective_mapBaseChange, Algebra.FormallySmooth.isSeparableExtension, Algebra.formallySmooth_iff_subsingleton_h1Cotangent, Algebra.FormallySmooth.of_algebraicIndependent_and_of_isSeparable_and_of_isSeparableExtension, Algebra.FormallySmooth.iff_isSeparableExtension
statement: formalized
proof: formalized
---

# 10.158 Formal smoothness of fields

Section 10.158 of the Stacks Project, [Tag 031U](https://stacks.math.columbia.edu/tag/031U). 11 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 090W, a lemma

[Tag 090W](https://stacks.math.columbia.edu/tag/090W) in the Stacks Project.

**`Algebra.FormallyUnramified.tfae_isSeparable_unramified_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Unramified/Field.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Unramified/Field.lean#L244). The attribute's comment: “The six items are the entries, in the source's order, of one `List.TFAE`. A finitely generated field extension is `Algebra.EssFiniteType`, `Ω[K⁄k] = 0` is `Subsingleton Ω[K⁄k]`, and étale is Mathlib's formally étale plus finite presentation, which is the source's Definition 00U1 by its Lemma 00UR. See the module docstring.”. References: EGA 0 (21.7.4), “more general”; EGA 0 (19.10.3), “(iii)”; EGA IV (17.4.2), “field extension K/k”; EGA IV (17.4.1), “field extension case”; EGA IV (17.15.11), “X = Spec of a field”; EGA 0 (21.7.4), “more general”; SGA 1 I (3.1), “(i)<=>(ii), field ext”; SGA 3 XI (1.3), “field extension case”.

> **Stacks 090W.** Let `K/k` be a finitely generated field extension. The following are
> equivalent:
>
> 1. `K` is a finite separable field extension of `k`;
> 2. `Ω[K⁄k] = 0`;
> 3. `K` is formally unramified over `k`;
> 4. `K` is unramified over `k`;
> 5. `K` is formally étale over `k`;
> 6. `K` is étale over `k`.

```lean
public theorem Algebra.FormallyUnramified.tfae_isSeparable_unramified_etale
    (k K : Type*) [Field k] [Field K] [Algebra k K] [Algebra.EssFiniteType k K] :
    List.TFAE
      [Module.Finite k K ∧ Algebra.IsSeparable k K,
       Subsingleton Ω[K⁄k],
       Algebra.FormallyUnramified k K,
       Algebra.Unramified k K,
       Algebra.FormallyEtale k K,
       Algebra.Etale k K]
```

## Tag 031W, a lemma

[Tag 031W](https://stacks.math.columbia.edu/tag/031W) in the Stacks Project.

**`KaehlerDifferential.D_eq_zero_iff_exists_pow_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Kaehler/PerfectField.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Kaehler/PerfectField.lean#L237). The attribute's comment: “The source's `d a = 0 in Ω_{K/k}` is `KaehlerDifferential.D k K a = 0` and `a` is a `p`-th power is `∃ b, b ^ p = a`; characteristic `p > 0` is `[Fact p.Prime] [CharP k p]` on the base. See the module docstring.”. References: EGA 0 (21.4.4), “more general”; EGA 0 (21.4.6), “(a) ⇔ (b), special case”.

> **Vanishing differentials over a perfect field are `p`-th powers.** Let `k` be a perfect
> field of characteristic `p > 0`, let `K/k` be a field extension and let `a : K`. Then `d a = 0` in
> `Ω[K⁄k]` if and only if `a` is a `p`-th power in `K`. Equivalently, the kernel of the universal
> `k`-derivation `d : K → Ω[K⁄k]` is the subfield of `p`-th powers of `K`.

```lean
public theorem KaehlerDifferential.D_eq_zero_iff_exists_pow_eq {k K : Type*} [Field k] [Field K]
    [Algebra k K] [PerfectField k] (p : ℕ) [Fact p.Prime] [CharP k p] (a : K) :
    KaehlerDifferential.D k K a = 0 ↔ ∃ b : K, b ^ p = a
```

## Tag 07DZ, a lemma

[Tag 07DZ](https://stacks.math.columbia.edu/tag/07DZ) in the Stacks Project.

**`IntermediateField.finrank_adjoin_eq_pow_of_linearIndependent_D`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PthRoots.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/PthRoots.lean#L196). The attribute's comment: “The source's `Ω_{k/𝔽_p}` is `Ω[k⁄ZMod p]`, characteristic `p > 0` is `[Fact p.Prime] [Algebra (ZMod p) k]`, and `k(a_1^{1/p}, …, a_n^{1/p})` is `IntermediateField.adjoin k (Set.range b)` for a family `b` of `p`-th roots in an ambient extension `K/k`, which is unique since Frobenius is injective. See the module docstring.”.

> **Adjoining `p`-th roots of elements with independent differentials.** Let `k` be a field of
> characteristic `p > 0` and let `a : ι → k` be a finite family such that the differentials `d aᵢ`
> are linearly independent in `Ω[k⁄𝔽_p]`. If `b : ι → K` is a family of `p`-th roots of the `aᵢ` in
> an extension field `K/k`, then the field extension `k(a_1^{1/p}, …, a_n^{1/p}) = k(bᵢ : i)` has
> degree `p ^ #ι` over `k`.

```lean
public theorem IntermediateField.finrank_adjoin_eq_pow_of_linearIndependent_D {k K : Type*}
    [Field k] [Field K] (p : ℕ) [Fact p.Prime] [Algebra (ZMod p) k] [Algebra k K] {ι : Type*}
    [Fintype ι] (a : ι → k) (b : ι → K) (hb : ∀ i, b i ^ p = algebraMap k K (a i))
    (h : LinearIndependent k fun i ↦ KaehlerDifferential.D (ZMod p) k (a i)) :
    Module.finrank k (IntermediateField.adjoin k (Set.range b)) = p ^ Fintype.card ι
```

## Tag 031X, a lemma

[Tag 031X](https://stacks.math.columbia.edu/tag/031X) in the Stacks Project.

**`Algebra.isSeparableExtension_iff_injective_mapBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/KaehlerDifferential/Separable.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/FieldTheory/KaehlerDifferential/Separable.lean#L411). The attribute's comment: “Differentials are taken over `𝐙`, which for a field of characteristic `p` is the source's `𝐅_p`, and the characteristic hypothesis is dropped: both conditions hold outright in characteristic zero, and the consumers (Lemmas 031Y, 0321 and Proposition 0322) are stated for all characteristics. See the module docstring.”. References: EGA 0 (20.6.3).

> A field extension `K/k` is separable in the sense of `Algebra.IsSeparableExtension` if and only
> if the canonical map `K ⊗_k Ω_{k/𝐙} → Ω_{K/𝐙}` is injective.

```lean
public theorem Algebra.isSeparableExtension_iff_injective_mapBaseChange (k K : Type*) [Field k]
    [Field K] [Algebra k K] :
    Algebra.IsSeparableExtension k K ↔
      Function.Injective (KaehlerDifferential.mapBaseChange ℤ k K)
```

## Tag 031Y, a lemma

[Tag 031Y](https://stacks.math.columbia.edu/tag/031Y) in the Stacks Project.

**`Algebra.FormallySmooth.isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Field.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/Field.lean#L261). The attribute's comment: “Separability is `Algebra.IsSeparableExtension` (Definition 030O(2)), not Mathlib's `Algebra.IsSeparable`, which asks the extension to be algebraic and would make the statement false for purely transcendental extensions. See the module docstring.”. References: EGA 0 (19.6.1), “necessity”; EGA 0 (19.0.2), “necessity”.

> Let `K/k` be an extension of fields. If `K` is formally smooth over `k`, then `K` is a
> separable extension of `k`: every subextension of `K/k` finitely generated over `k` has a
> separating transcendence basis.

```lean
public theorem Algebra.FormallySmooth.isSeparableExtension (k K : Type*) [Field k] [Field K]
    [Algebra k K] [Algebra.FormallySmooth k K] : Algebra.IsSeparableExtension k K
```

## Tag 031Z, a lemma

[Tag 031Z](https://stacks.math.columbia.edu/tag/031Z) in the Stacks Project.

**`Algebra.formallySmooth_iff_subsingleton_h1Cotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/FieldCotangent.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/FieldCotangent.lean#L56). The attribute's comment: “Stated for a field `K` over an arbitrary commutative base ring `R`; the source's base field `k` is the case `R := k`, and no hypothesis on the base is used. `H_1(L_{K/k}) = 0` is `Subsingleton (Algebra.H1Cotangent R K)`. See the module docstring.”.

> A field `K` which is an algebra over a commutative ring `R` is formally smooth over `R` if and
> only if `H¹(L_{K/R}) = 0`.

```lean
public theorem Algebra.formallySmooth_iff_subsingleton_h1Cotangent
    (R K : Type*) [CommRing R] [Field K] [Algebra R K] :
    Algebra.FormallySmooth R K ↔ Subsingleton (Algebra.H1Cotangent R K)
```

## Tag 0320, a lemma

[Tag 0320](https://stacks.math.columbia.edu/tag/0320) in the Stacks Project.

**`Algebra.FormallySmooth.of_algebraicIndependent_and_of_isSeparable_and_of_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Field.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/Field.lean#L223). The attribute's comment: “The source's parts (1), (2), (3) are the conjuncts `.1`, `.2.1`, `.2.2`. Purely transcendental is `AlgebraicIndependent` together with `IntermediateField.adjoin k s = ⊤`, as in the Mathlib sibling `Algebra.FormallySmooth.of_algebraicIndependent`; separable algebraic is `Algebra.IsSeparable`; separable is `Algebra.IsSeparableExtension`, Definition 030O(2), which does not presuppose algebraicity. See the module docstring.”. References: EGA 0 (19.6.1), “sufficiency”; EGA 0 (21.5.1), “more general”; EGA 0 (21.5.1), “more general”; EGA 0 (19.0.2), “sufficiency”; EGA 0 (22.2.1), “special case”.

> Let `K/k` be an extension of fields. Then `K` is formally smooth over `k` in each of the
> following three cases: (1) `K` is purely transcendental over `k`, that is, `K` is generated as an
> intermediate field by an algebraically independent set; (2) `K` is separable algebraic over `k`;
> (3) `K` is separable over `k` in the sense of `Algebra.IsSeparableExtension`.

```lean
public theorem
    Algebra.FormallySmooth.of_algebraicIndependent_and_of_isSeparable_and_of_isSeparableExtension
    (k K : Type*) [Field k] [Field K] [Algebra k K] :
    (∀ s : Set K, AlgebraicIndependent k ((↑) : s → K) → IntermediateField.adjoin k s = ⊤ →
        Algebra.FormallySmooth k K) ∧
      (Algebra.IsSeparable k K → Algebra.FormallySmooth k K) ∧
      (Algebra.IsSeparableExtension k K → Algebra.FormallySmooth k K)
```

## Tag 0321, a lemma

[Tag 0321](https://stacks.math.columbia.edu/tag/0321) in the Stacks Project.

**`Algebra.FormallySmooth.iff_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Field.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/Field.lean#L294). The attribute's comment: “Separability is `Algebra.IsSeparableExtension`, Definition 030O (2), which does not presuppose algebraicity and so is not `Algebra.IsSeparable`; formal smoothness is `Algebra.FormallySmooth`, Definition 00TI. The characteristic split is dropped: both implications hold in every characteristic (the source's proof is `combine Lemmas 031Y and 0320`, neither of which mentions the characteristic), so part (2) is this equivalence and part (1) is it together with the characteristic-zero case of Lemma 030Z. See the module docstring.”. References: EGA 0 (19.6.1); EGA 0 (21.5.1), “more general”; EGA 0 (21.5.1), “more general”; EGA 0 (19.0.2).

> A field extension `K/k` is formally smooth over `k` if and only if it is separable over `k` in
> the sense of `Algebra.IsSeparableExtension`.

```lean
public theorem Algebra.FormallySmooth.iff_isSeparableExtension (k K : Type*) [Field k] [Field K]
    [Algebra k K] : Algebra.FormallySmooth k K ↔ Algebra.IsSeparableExtension k K
```

## Tag 0322, a proposition

[Tag 0322](https://stacks.math.columbia.edu/tag/0322) in the Stacks Project.

**`Algebra.isSeparableExtension_of_charZero_and_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Field.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormallySmooth/Field.lean#L509). The attribute's comment: “The equivalences are stated uniformly in the characteristic: `k^{1/p}` is `AdjoinPthRoots k` for the exponential characteristic, which in characteristic zero makes the second condition, hence all of them, automatic, and the source's characteristic-zero list is recovered. Differentials are taken over `𝐙` in both characteristics. See the module docstring.”. References: EGA 0 (20.6.3).

> Let `K/k` be a field extension. If the characteristic of `k` is zero then `K` is separable over
> `k`; and, in any characteristic, the following are equivalent: `K` is separable over `k`, the ring
> `K ⊗_k k^{1/p}` is reduced for the exponential characteristic `p` of `k`, `K` is geometrically
> reduced over `k`, the map `K ⊗_k Ω_{k/𝐙} → Ω_{K/𝐙}` is injective, `H_1(L_{K/k}) = 0`, and `K` is
> formally smooth over `k`.

```lean
public theorem Algebra.isSeparableExtension_of_charZero_and_tfae (k K : Type*) [Field k] [Field K]
    [Algebra k K] :
    (CharZero k → Algebra.IsSeparableExtension k K) ∧
      List.TFAE
        [Algebra.IsSeparableExtension k K,
          IsReduced (K ⊗[k] AdjoinPthRoots k),
          Algebra.IsGeometricallyReduced k K,
          Function.Injective (KaehlerDifferential.mapBaseChange ℤ k K),
          Subsingleton (Algebra.H1Cotangent k K),
          Algebra.FormallySmooth k K]
```

## Tag 037X, a lemma

[Tag 037X](https://stacks.math.columbia.edu/tag/037X) in the Stacks Project.

**`Algebra.IsSeparableExtension.tfae_exists_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Field.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/Field.lean#L318). References: SGA 1 II (5.7), “partial”.

> **A finitely generated field extension is separable if and only if it is the localization of a
> smooth algebra.** For a finitely generated field extension `K/k` the following are equivalent:
> `K/k` is separable; some smooth `k`-subalgebra of `K` has `K` as its fraction field; some smooth
> `k`-algebra has `K` as a localization.

```lean
public theorem Algebra.IsSeparableExtension.tfae_exists_smooth
    (k : Type*) (K : Type v) [Field k] [Field K] [Algebra k K] [Algebra.EssFiniteType k K] :
    List.TFAE
      [Algebra.IsSeparableExtension k K,
        ∃ R : Subalgebra k K, Algebra.Smooth k R ∧ IsFractionRing R K,
        ∃ (R : Type v) (_ : CommRing R) (_ : Algebra k R) (_ : Algebra R K)
          (_ : IsScalarTower k R K) (S : Submonoid R),
          Algebra.Smooth k R ∧ IsLocalization S K]
```

## Tag 07BV, a lemma

[Tag 07BV](https://stacks.math.columbia.edu/tag/07BV) in the Stacks Project.

**`Subalgebra.directedOn_isGlobalCompleteIntersectionOver_and_exists_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/FieldExtensionCompleteIntersectionColimit.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/FieldExtensionCompleteIntersectionColimit.lean#L472). The attribute's comment: “First part. The filtered colimit is the directed union of the global complete intersection `k`-subalgebras of `K`; see the module docstring.”.

> **Stacks 07BV, first part.** Every field extension `K/k` is a filtered colimit of global
> complete intersection algebras over `k`: the `k`-subalgebras of `K` that are global complete
> intersections over `k` form a directed family whose union is `K`.

```lean
theorem Subalgebra.directedOn_isGlobalCompleteIntersectionOver_and_exists_mem
    (k K : Type*) [Field k] [Field K] [Algebra k K] :
    DirectedOn (· ≤ ·) {A : Subalgebra k K | IsGlobalCompleteIntersectionOver k A} ∧
      ∀ x : K, ∃ A ∈ {A : Subalgebra k K | IsGlobalCompleteIntersectionOver k A}, x ∈ A
```

**`Subalgebra.directedOn_smooth_and_exists_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/FieldExtensionCompleteIntersectionColimit.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smooth/FieldExtensionCompleteIntersectionColimit.lean#L484). The attribute's comment: “Second part. The filtered colimit is the directed union of the smooth `k`-subalgebras of `K`; see the module docstring.”.

> **Stacks 07BV, second part.** A separable field extension `K/k` is a filtered colimit of
> smooth `k`-algebras: the smooth `k`-subalgebras of `K` form a directed family whose union
> is `K`.

```lean
theorem Subalgebra.directedOn_smooth_and_exists_mem
    (k K : Type*) [Field k] [Field K] [Algebra k K] [Algebra.IsSeparableExtension k K] :
    DirectedOn (· ≤ ·) {A : Subalgebra k K | Algebra.Smooth k A} ∧
      ∀ x : K, ∃ A ∈ {A : Subalgebra k K | Algebra.Smooth k A}, x ∈ A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.158, Tag 031U](https://stacks.math.columbia.edu/tag/031U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
