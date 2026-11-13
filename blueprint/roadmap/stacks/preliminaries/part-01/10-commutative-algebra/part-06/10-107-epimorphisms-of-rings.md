---
declaration: section
origin: cited
lean: CommRingCat.epi_tfae, CategoryTheory.epi_comp, epi_includeLeftRingHom_of_epi, Algebra.IsEpi.tower_top, CommRingCat.epi_ofHom_iff_forall_prime, RingHom.surjective_iff_epi_and_finite, faithfullyFlat_epimorphism_isIso, Algebra.IsEpi.surjective_algebraMap_of_field
statement: formalized
proof: formalized
---

# 10.107 Epimorphisms of rings

Section 10.107 of the Stacks Project, [Tag 04VM](https://stacks.math.columbia.edu/tag/04VM). 13 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04VN, a lemma

[Tag 04VN](https://stacks.math.columbia.edu/tag/04VN) in the Stacks Project.

**`CommRingCat.epi_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L190). The attribute's comment: “Item (1) is `CategoryTheory.Epi` in `CommRingCat`, the source's categorical notion, rather than the class `Algebra.IsEpi`, which is by definition injectivity of the multiplication map and would make item (5) restate item (1); `CommRingCat.epi_iff_epi` transfers between them. The source's `either of the ring maps` is the two items (3) and (4) below, one per map, and `is an isomorphism` is `Function.Bijective`. See the module docstring.”.

> **The tensor square detects a ring epimorphism** (Stacks 04VN). Let `R → S` be a ring map.
> The following are equivalent: (1) `R → S` is an epimorphism of commutative rings; (2) the two
> ring maps `S → S ⊗_R S`, namely `s ↦ s ⊗ 1` and `s ↦ 1 ⊗ s`, are equal; (3) `s ↦ s ⊗ 1` is an
> isomorphism; (4) `s ↦ 1 ⊗ s` is an isomorphism; (5) the multiplication map `S ⊗_R S → S` is an
> isomorphism.

```lean
theorem CommRingCat.epi_tfae {R S : Type u} [CommRing R] [CommRing S] [Algebra R S] :
    List.TFAE
      [CategoryTheory.Epi (CommRingCat.ofHom (algebraMap R S)),
       (Algebra.TensorProduct.includeLeft : S →ₐ[R] S ⊗[R] S) = Algebra.TensorProduct.includeRight,
       Function.Bijective (Algebra.TensorProduct.includeLeft : S →ₐ[R] S ⊗[R] S),
       Function.Bijective (Algebra.TensorProduct.includeRight : S →ₐ[R] S ⊗[R] S),
       Function.Bijective (Algebra.TensorProduct.lmul' (S := S) R)]
```

## Tag 04VP, a lemma

[Tag 04VP](https://stacks.math.columbia.edu/tag/04VP) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.epi_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.epi_comp#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L377) (StacksFrontier): “The case `C = CommRingCat` of the general categorical fact.”. References: SGA 3 IV (1.4).

## Tag 04VQ, a lemma

[Tag 04VQ](https://stacks.math.columbia.edu/tag/04VQ) in the Stacks Project.

**`epi_includeLeftRingHom_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L431).

> **Base change of an epimorphism is an epimorphism.** If `R → S` is an
> epimorphism in `CommRingCat` and `R → R'` is any ring map, then the canonical
> ring map `R' → R' ⊗_R S` is an epimorphism.

```lean
theorem epi_includeLeftRingHom_of_epi
    (R R' S : Type) [CommRing R] [CommRing R'] [CommRing S]
    [Algebra R R'] [Algebra R S]
    (h : Epi (CommRingCat.ofHom (algebraMap R S))) :
    Epi (CommRingCat.ofHom
      (Algebra.TensorProduct.includeLeftRingHom :
        R' →+* TensorProduct R R' S))
```

## Tag 04VR, a lemma

[Tag 04VR](https://stacks.math.columbia.edu/tag/04VR) in the Stacks Project.

**`Algebra.IsEpi.tower_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L217). The attribute's comment: “Epimorphy is Mathlib's `Algebra.IsEpi` (equivalently `CategoryTheory.Epi` in `CommRingCat`, by `CommRingCat.epi_iff_epi`), and the source's hypothesis that `A → C` is the composite `A → B → C` is `IsScalarTower A B C`. Named after its sibling `Algebra.IsIntegral.tower_top`. See the module docstring.”.

> **An epimorphism of rings stays one over a larger base** (Stacks 04VR). If `A → B → C`
> are ring maps, `A → C` being the composite, and `A → C` is an epimorphism, then `B → C` is
> an epimorphism.
>
> The proof transports the identity `1 ⊗ c = c ⊗ 1` along the base-enlargement comparison map
> `TensorProduct.mapOfCompatibleSMul B A B C C : C ⊗[A] C →ₗ[B] C ⊗[B] C`, whose
> `TensorProduct.CompatibleSMul B A C C` instance is where `IsScalarTower A B C` enters.

```lean
theorem tower_top {A B C : Type*} [CommRing A] [CommRing B] [CommRing C]
    [Algebra A B] [Algebra A C] [Algebra B C] [IsScalarTower A B C] [Algebra.IsEpi A C] :
    Algebra.IsEpi B C
```

## Tag 04VS, a lemma

[Tag 04VS](https://stacks.math.columbia.edu/tag/04VS) in the Stacks Project.

**`CommRingCat.epi_ofHom_iff_forall_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 670](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L670).

> **Stacks Tag 04VS.** Being an epimorphism is a local property of a ring
> map: a ring map `f : R →+* S` is an epimorphism of rings if and only if for
> every prime ideal `p` of `R`, the induced map `R_p →+* S_p` is an epimorphism of
> rings.

```lean
theorem CommRingCat.epi_ofHom_iff_forall_prime {R S : Type u} [CommRing R] [CommRing S]
    (f : R →+* S) :
    Epi (CommRingCat.ofHom f) ↔
      ∀ (p : Ideal R) [p.IsPrime], Epi (CommRingCat.ofHom (inducedLocalizationMap f p))
```

## Tag 04VT, a lemma

[Tag 04VT](https://stacks.math.columbia.edu/tag/04VT) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.surjective_iff_epi_and_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.surjective_iff_epi_and_finite#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L699) (StacksFrontier): “a ring map is surjective iff it is a finite epimorphism”.

## Tag 04VU, a lemma

[Tag 04VU](https://stacks.math.columbia.edu/tag/04VU) in the Stacks Project.

**`faithfullyFlat_epimorphism_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 738](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L738). References: SGA 3 VIB (12.1), “affine case”; SGA 3 XI (3.9), “Affine case”.

> If `algebraMap R S` is an epimorphism of commutative rings and `S` is faithfully flat as
> an `R`-module, then `algebraMap R S` is bijective, i.e. an isomorphism of rings.

```lean
theorem faithfullyFlat_epimorphism_isIso
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.IsEpi R S] [Module.FaithfullyFlat R S] :
    Function.Bijective (algebraMap R S)
```

## Tag 04VV, a lemma

[Tag 04VV](https://stacks.math.columbia.edu/tag/04VV) in the Stacks Project.

**`Algebra.IsEpi.surjective_algebraMap_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L233). The attribute's comment: “The source's `S = k` or `S = 0` is stated as surjectivity of `algebraMap k S`, which over a field is equivalent to it; the target need not be commutative. See the module docstring.”.

> An epimorphism of rings `k → S` out of a field `k` is surjective; equivalently, `S = k` or
> `S = 0`.
>
> Over a field the line `k · 1 ⊆ S` is split off by a linear functional `φ : S →ₗ[k] k` with
> `φ 1 = 1`; applying `φ` to the left factor of the identity `1 ⊗ s = s ⊗ 1` in `S ⊗[k] S` turns
> it into `s = algebraMap k S (φ s)`.

```lean
theorem surjective_algebraMap_of_field {k S : Type*} [Field k] [Ring S] [Algebra k S]
    [Algebra.IsEpi k S] : Function.Surjective (algebraMap k S)
```

## Tag 04VW, a lemma

[Tag 04VW](https://stacks.math.columbia.edu/tag/04VW) in the Stacks Project.

**`PrimeSpectrum.comap_injective_and_residueFieldMap_bijective_of_isEpi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Basic.lean#L353). The attribute's comment: “The equality `κ(𝔭) = κ(𝔮)` of part (2) is bijectivity of the canonical map `Ideal.ResidueField.map`; it is not surjectivity of `R_𝔭 → S_𝔮`, which is false for epimorphisms. See the module docstring.”.

> Let `R → S` be an epimorphism of rings. Then `Spec S → Spec R` is injective, and for every
> prime `𝔮 ⊆ S` lying over a prime `𝔭 ⊆ R` the canonical residue field extension
> `κ(𝔭) → κ(𝔮)` is bijective, that is, `κ(𝔭) = κ(𝔮)`.

```lean
theorem comap_injective_and_residueFieldMap_bijective_of_isEpi
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] [Algebra.IsEpi R S] :
    Function.Injective (comap (algebraMap R S)) ∧
      ∀ (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] (h : p = q.comap (algebraMap R S)),
        Function.Bijective (Ideal.ResidueField.map p q (algebraMap R S) h)
```

## Tag 04VX, a lemma

[Tag 04VX](https://stacks.math.columbia.edu/tag/04VX) in the Stacks Project.

**`TensorProduct.sum_tmul_eq_zero_iff_exists_finsupp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/SumTmulEqZero.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/SumTmulEqZero.lean#L69).

> **Vanishing of a sum of pure tensors.** Let `x : I → M` generate `M` and `y : J → N`
> generate `N`, and let `m : J →₀ M` be a finitely supported family. Then `∑_j m_j ⊗ y_j = 0` in
> `M ⊗_R N` if and only if there are scalars `a_{ij}`, only finitely many nonzero, such that
> `m_j = ∑_i a_{ij} x_i` for every `j` and `∑_j a_{ij} y_j = 0` for every `i`.
>
> The proof tensors the exact sequence `0 → K → (J →₀ R) → N → 0` given by the `y_j` with `M`,
> and writes an element of `M ⊗_R K` as `∑_i x_i ⊗ k_i` using the generators `x_i`.

```lean
theorem sum_tmul_eq_zero_iff_exists_finsupp {x : I → M}
    (hx : Submodule.span R (Set.range x) = ⊤) {y : J → N}
    (hy : Submodule.span R (Set.range y) = ⊤) (m : J →₀ M) :
    (m.sum fun j mj ↦ mj ⊗ₜ[R] y j) = 0 ↔
      ∃ a : I →₀ J →₀ R, (∀ j, m j = a.sum fun i aᵢ ↦ aᵢ j • x i) ∧
        ∀ i, ((a i).sum fun j r ↦ r • y j) = 0
```

## Tag 04VY, a lemma

[Tag 04VY](https://stacks.math.columbia.edu/tag/04VY) in the Stacks Project.

**`tmul_one_eq_one_tmul_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Cardinality.lean, line 1125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Cardinality.lean#L1125).

> For `g : S`, the identity `g ⊗ 1 = 1 ⊗ g` in `S ⊗[R] S` holds if and only if
> `g = ∑ i, ∑ j, φ (xᵢⱼ) * yᵢ * zⱼ` for some `yᵢ, zⱼ : S` and `xᵢⱼ : R` whose column sums
> `∑ i, φ (xᵢⱼ) * yᵢ` and row sums `∑ j, φ (xᵢⱼ) * zⱼ` all lie in the image of `φ`.

```lean
theorem tmul_one_eq_one_tmul_iff (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] (g : S) :
    (g ⊗ₜ[R] (1 : S) = (1 : S) ⊗ₜ[R] g) ↔
    (∃ (n : ℕ) (y z : Fin n → S) (x : Fin n → Fin n → R),
      g = ∑ i, ∑ j, (algebraMap R S (x i j)) * y i * z j ∧
      (∀ j, ∃ r : R, ∑ i, (algebraMap R S (x i j)) * y i = algebraMap R S r) ∧
      (∀ i, ∃ r : R, ∑ j, (algebraMap R S (x i j)) * z j = algebraMap R S r))
```

## Tag 04W0, a lemma

[Tag 04W0](https://stacks.math.columbia.edu/tag/04W0) in the Stacks Project.

**`epi_card_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/Cardinality.lean, line 828](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/Cardinality.lean#L828).

> If `f : R → S` is an epimorphism of commutative rings, then `|S| ≤ |R|`.

```lean
theorem epi_card_le (R S : Type u) [CommRing R] [CommRing S] (f : R →+* S)
    (hf : Epi (CommRingCat.ofHom f)) :
    Cardinal.mk S ≤ Cardinal.mk R
```

## Tag 08YS, a lemma

[Tag 08YS](https://stacks.math.columbia.edu/tag/08YS) in the Stacks Project.

**`CommRingCat.epi_tfae_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/RestrictionOfScalars.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/RestrictionOfScalars.lean#L129).

> For a homomorphism `R → S` of commutative rings, the following are equivalent:
>
> 1. `R → S` is an epimorphism of (commutative) rings;
> 2. for all `S`-modules `N₁, N₂`, every `R`-linear map is `S`-linear, i.e.
>    `Hom_S(N₁,N₂) = Hom_R(N₁,N₂)`;
> 3. the restriction-of-scalars functor `Mod_S → Mod_R` is fully faithful.

```lean
theorem epi_tfae_restrictScalars :
    [ Epi (CommRingCat.ofHom (algebraMap R S)),
      ∀ (N₁ N₂ : Type (max u v)) [AddCommGroup N₁] [AddCommGroup N₂] [Module R N₁]
        [Module R N₂] [Module S N₁] [Module S N₂] [IsScalarTower R S N₁]
        [IsScalarTower R S N₂],
        Function.Surjective (LinearMap.restrictScalars R : (N₁ →ₗ[S] N₂) → N₁ →ₗ[R] N₂),
      Nonempty (ModuleCat.restrictScalars.{max u v} (algebraMap R S)).FullyFaithful
    ].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.107, Tag 04VM](https://stacks.math.columbia.edu/tag/04VM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
