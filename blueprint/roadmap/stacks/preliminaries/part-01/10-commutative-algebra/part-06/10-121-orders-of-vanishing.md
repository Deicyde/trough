---
declaration: section
origin: cited
lean: Module.length_quotient_span_mul_eq_add_and_ne_top, Submodule.IsBaseChangeLattice, Submodule.isBaseChangeLattice_iff_isLattice, Module.length_quotient_submoduleOf_eq_add, Submodule.isLattice_tfae_of_le_and_iff_of_ge_and_inf_sup, Submodule.lengthDist_eq_sub, Submodule.lengthDist_eq_sub_of_le_inf_of_sup_le, Submodule.lengthDist
statement: formalized
proof: formalized
---

# 10.121 Orders of vanishing

Section 10.121 of the Stacks Project, [Tag 02MB](https://stacks.math.columbia.edu/tag/02MB). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02MC, a lemma

[Tag 02MC](https://stacks.math.columbia.edu/tag/02MC) in the Stacks Project.

**`Module.length_quotient_span_mul_eq_add_and_ne_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L283). The attribute's comment: “Semi-locality is dropped, being used by neither assertion, and dimension `1` is weakened to dimension at most `1` (`Ring.KrullDimLE 1 R`). The additivity is the case `M = R` of `Module.length_quotSMulTop_mul`, which holds for any module and `b` acting injectively, with no hypothesis on `R`; the finiteness is Mathlib's `isFiniteLength_quotient_span_singleton` (Stacks 00PF for `M = R`).”.

> Let `R` be a Noetherian ring of Krull dimension at most one and `a`, `b ∈ R` nonzerodivisors.
> Then `length_R(R/(ab)) = length_R(R/(a)) + length_R(R/(b))`, and these three lengths are
> finite.

```lean
theorem Module.length_quotient_span_mul_eq_add_and_ne_top [IsNoetherianRing R]
    [Ring.KrullDimLE 1 R] {a b : R} (ha : a ∈ nonZeroDivisors R)
    (hb : b ∈ nonZeroDivisors R) :
    Module.length R (R ⧸ Ideal.span {a * b}) =
        Module.length R (R ⧸ Ideal.span {a}) + Module.length R (R ⧸ Ideal.span {b}) ∧
      Module.length R (R ⧸ Ideal.span {a * b}) ≠ ⊤ ∧
      Module.length R (R ⧸ Ideal.span {a}) ≠ ⊤ ∧ Module.length R (R ⧸ Ideal.span {b}) ≠ ⊤
```

## Tag 02ME, a definition

[Tag 02ME](https://stacks.math.columbia.edu/tag/02ME) in the Stacks Project.

**`Submodule.IsBaseChangeLattice`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L105). The attribute's comment: “The source's definition: `M` is a finite `R`-submodule of `V` and the canonical map `K ⊗_R M → V` is an isomorphism. `Submodule.isBaseChangeLattice_iff_isLattice` identifies it with Mathlib's `Submodule.IsLattice K M` (finite generation and `span_K M = ⊤`), and `Submodule.span_eq_top_iff_exists_basis` is the remark that the condition means `M` contains a `K`-basis of `V`; that a lattice over a discrete valuation ring is free is Mathlib's `Submodule.IsLattice.free`. The notion is stated for any ring `R` and `K`-vector space `V`, the source's standing hypotheses (`R` a Noetherian local domain of dimension one with fraction field `K`, `V` finite dimensional) restricting the context in which it is used.”.

> A *lattice* in `V` in the source's phrasing: a finite `R`-submodule `M ⊆ V` such that
> `V = K ⊗_R M`, that is, the canonical map `K ⊗_R M → V` induced by the inclusion `M ↪ V` is an
> isomorphism.

```lean
def Submodule.IsBaseChangeLattice (M : Submodule R V) : Prop
```

**`Submodule.isBaseChangeLattice_iff_isLattice`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L171). The attribute's comment: “The source's definition `Submodule.IsBaseChangeLattice` (`M` finite over `R` and `K ⊗_R M → V` an isomorphism) is equivalent to Mathlib's `Submodule.IsLattice K M` (`M` finite over `R` and `span_K M = ⊤`). Proved for any ring `R` with fraction field `K` and any `K`-vector space `V`; the source's further hypotheses (`R` Noetherian local of dimension one, `V` finite dimensional) are not needed.”.

> When `K` is the fraction field of `R`, a finite `R`-submodule `M ⊆ V` with `V = K ⊗_R M` is
> exactly a lattice in Mathlib's sense: finitely generated and spanning `V` over `K`.

```lean
theorem Submodule.isBaseChangeLattice_iff_isLattice [IsFractionRing R K] (M : Submodule R V) :
    M.IsBaseChangeLattice K ↔ Submodule.IsLattice K M
```

## Tag 02MF, a lemma

[Tag 02MF](https://stacks.math.columbia.edu/tag/02MF) in the Stacks Project.

**`Module.length_quotient_submoduleOf_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L230). The attribute's comment: “(4). Stated for arbitrary submodules `N ≤ S ≤ A` of a module over a ring, and as an identity in `ℕ∞`, so that no finiteness and none of the source's hypotheses — locality, dimension one, lattices, finite dimensionality of `V` — are needed. Parts (1)-(3) are `Submodule.isLattice_tfae_of_le_and_iff_of_ge_and_inf_sup` and part (5) is `Submodule.lengthDist_eq_sub_of_le_inf_of_sup_le`.”.

> For `N ≤ S ≤ A` submodules of `V`, `length_R(A/N) = length_R(S/N) + length_R(A/S)`, an
> identity in `ℕ∞`.

```lean
theorem Module.length_quotient_submoduleOf_eq_add {N S A : Submodule R V} (hNS : N ≤ S)
    (hSA : S ≤ A) :
    Module.length R (↥A ⧸ N.submoduleOf A) =
      Module.length R (↥S ⧸ N.submoduleOf S) + Module.length R (↥A ⧸ S.submoduleOf A)
```

**`Submodule.isLattice_tfae_of_le_and_iff_of_ge_and_inf_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L481). The attribute's comment: “Parts (1)-(3). Locality is dropped, being used by no part, and finite dimensionality of `V` follows from the existence of a lattice. Dimension one is an antecedent of parts (1) and (2), over which it is sharp — it is not weakened to `Ring.KrullDimLE 1 R`, which breaks (2) — and part (3) holds over any Noetherian domain, strengthening Mathlib's `Submodule.IsLattice.inf`. Parts (4) and (5) hold for arbitrary submodules of a module over a ring, with none of these hypotheses; part (5) needs the lattices of its statement, whose quotients have finite length by (1)-(2). They are `Module.length_quotient_submoduleOf_eq_add` and `Submodule.lengthDist_eq_sub_of_le_inf_of_sup_le`.”.

> Let `R` be a Noetherian domain with fraction field `K` and let `V` be a `K`-vector space. If
> `R` has Krull dimension `1` then: (1) for `M` a lattice and `M ≤ M'`, the conditions "`M'` is a
> lattice", "`length_R(M'/M) < ∞`" and "`M'` is finitely generated" are equivalent; (2) for `M` a
> lattice and `M' ≤ M`, `M'` is a lattice if and only if `length_R(M/M') < ∞`. Without any
> hypothesis on the dimension: (3) if `M` and `M'` are lattices then so are `M ⊓ M'` and `M ⊔ M'`.

```lean
theorem Submodule.isLattice_tfae_of_le_and_iff_of_ge_and_inf_sup {R : Type*} [CommRing R]
    [IsDomain R] [IsNoetherianRing R] {K : Type*} [Field K] [Algebra R K] [IsFractionRing R K]
    {V : Type*} [AddCommGroup V] [Module K V] [Module R V] [IsScalarTower R K V] :
    (ringKrullDim R = 1 →
      (∀ M M' : Submodule R V, Submodule.IsLattice K M → M ≤ M' →
          [Submodule.IsLattice K M', Module.length R (↥M' ⧸ M.submoduleOf M') ≠ ⊤,
            M'.FG].TFAE) ∧
      (∀ M M' : Submodule R V, Submodule.IsLattice K M → M' ≤ M →
          (Submodule.IsLattice K M' ↔ Module.length R (↥M ⧸ M'.submoduleOf M) ≠ ⊤))) ∧
    (∀ M M' : Submodule R V, Submodule.IsLattice K M → Submodule.IsLattice K M' →
        Submodule.IsLattice K (M ⊓ M') ∧ Submodule.IsLattice K (M ⊔ M'))
```

**`Submodule.lengthDist_eq_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 587](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L587). The attribute's comment: “(5), its first equality `length_R(M/M ∩ M') - length_R(M'/M ∩ M') = length_R(M/N) - length_R(M'/N)`, with `d(M, M')` the left side. The whole chain of (5), through `M + M'` and through a lattice `N' ⊇ M + M'` as well, is `Submodule.lengthDist_eq_sub_of_le_inf_of_sup_le`. Locality is dropped and dimension one is spelled as the pair `Ring.KrullDimLE 1 R` and `¬ IsField R`, which over a Noetherian domain is `ringKrullDim R = 1`.”.

> For lattices `M`, `M'` and a lattice `N` below both,
> `d(M, M') = length_R(M/N) - length_R(M'/N)`.

```lean
theorem Submodule.lengthDist_eq_sub (hR : ¬ IsField R) {M M' N : Submodule R V}
    [Submodule.IsLattice K M] [Submodule.IsLattice K M'] [Submodule.IsLattice K N] (hNM : N ≤ M)
    (hNM' : N ≤ M') :
    M.lengthDist M' = ((Module.length R (↥M ⧸ N.submoduleOf M)).toNat : ℤ)
      - ((Module.length R (↥M' ⧸ N.submoduleOf M')).toNat : ℤ)
```

**`Submodule.lengthDist_eq_sub_of_le_inf_of_sup_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 627](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L627). The attribute's comment: “(5), the whole chain of four equal expressions, the first being `d(M, M')`. Locality is dropped and dimension one is spelled as the pair `Ring.KrullDimLE 1 R` and `¬ IsField R`, which over a Noetherian domain is `ringKrullDim R = 1`; finite dimensionality of `V` follows from the existence of a lattice. Each length is truncated from `ℕ∞` by `ENat.toNat`, which is faithful here since every quotient of lattices involved has finite length by (1)-(2).”.

> Let `R` be a Noetherian domain of Krull dimension one with fraction field `K`, and let `M`,
> `M'`, `N`, `N'` be lattices in a `K`-vector space with `N ⊆ M ∩ M'` and `M + M' ⊆ N'`. Then
> `length\_R(M/M ∩ M') - length\_R(M'/M ∩ M') = length\_R(M/N) - length\_R(M'/N) =
> length\_R((M + M')/M') - length\_R((M + M')/M) = length\_R(N'/M') - length\_R(N'/M)`.

```lean
theorem Submodule.lengthDist_eq_sub_of_le_inf_of_sup_le (hR : ¬ IsField R)
    {M M' N N' : Submodule R V} [Submodule.IsLattice K M] [Submodule.IsLattice K M']
    [Submodule.IsLattice K N] [Submodule.IsLattice K N'] (hN : N ≤ M ⊓ M') (hN' : M ⊔ M' ≤ N') :
    ((Module.length R (↥M ⧸ (M ⊓ M').submoduleOf M)).toNat : ℤ)
        - ((Module.length R (↥M' ⧸ (M ⊓ M').submoduleOf M')).toNat : ℤ)
      = ((Module.length R (↥M ⧸ N.submoduleOf M)).toNat : ℤ)
        - ((Module.length R (↥M' ⧸ N.submoduleOf M')).toNat : ℤ) ∧
    ((Module.length R (↥M ⧸ N.submoduleOf M)).toNat : ℤ)
        - ((Module.length R (↥M' ⧸ N.submoduleOf M')).toNat : ℤ)
      = ((Module.length R (↥(M ⊔ M') ⧸ M'.submoduleOf (M ⊔ M'))).toNat : ℤ)
        - ((Module.length R (↥(M ⊔ M') ⧸ M.submoduleOf (M ⊔ M'))).toNat : ℤ) ∧
    ((Module.length R (↥(M ⊔ M') ⧸ M'.submoduleOf (M ⊔ M'))).toNat : ℤ)
        - ((Module.length R (↥(M ⊔ M') ⧸ M.submoduleOf (M ⊔ M'))).toNat : ℤ)
      = ((Module.length R (↥N' ⧸ M'.submoduleOf N')).toNat : ℤ)
        - ((Module.length R (↥N' ⧸ M.submoduleOf N')).toNat : ℤ)
```

## Tag 02MG, a definition

[Tag 02MG](https://stacks.math.columbia.edu/tag/02MG) in the Stacks Project.

**`Submodule.lengthDist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L538). The attribute's comment: “Stated for arbitrary submodules of a module over a ring, since the formula uses none of the source's standing hypotheses: those make the two lengths finite, and are carried by 02MF and 02MH rather than left inert here. The difference is taken after `ENat.toNat`, which is faithful on pairs of lattices by 02MF (1)-(3). See the module docstring.”.

> The distance between two submodules `M`, `M'` of a module `V` over a ring `R`: the integer
> `d(M, M') = length_R(M/(M ∩ M')) - length_R(M'/(M ∩ M'))`, with both lengths truncated from `ℕ∞`
> by `ENat.toNat`.

```lean
noncomputable def Submodule.lengthDist {R : Type*} [Ring R] {V : Type*} [AddCommGroup V]
    [Module R V] (M M' : Submodule R V) : ℤ
```

**`Submodule.lengthDist_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L546). The attribute's comment: “The remark following the definition. Stated for arbitrary submodules of a module over a ring; on a pair of lattices the length is finite by 02MF (2).”.

> For `M' ≤ M`, `d(M, M') = length_R(M/M')`.

```lean
theorem Submodule.lengthDist_of_le {M M' : Submodule R V} (h : M' ≤ M) :
    M.lengthDist M' = (Module.length R (↥M ⧸ M'.submoduleOf M)).toNat
```

## Tag 02MH, a lemma

[Tag 02MH](https://stacks.math.columbia.edu/tag/02MH) in the Stacks Project.

**`Submodule.lengthDist_antisymm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L554). The attribute's comment: “(2). Stated for arbitrary submodules of a module over a ring: with both quotients normalised by `M ⊓ M'` the identity is the antisymmetry of a difference.”.

> The distance between two submodules is antisymmetric: `d(M, M') = -d(M', M)`.

```lean
theorem Submodule.lengthDist_antisymm (M M' : Submodule R V) :
    M.lengthDist M' = - M'.lengthDist M
```

**`Submodule.lengthDist_additive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 653](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Lattice/Distance.lean#L653). The attribute's comment: “(1). Locality is dropped and dimension one is spelled as the pair `Ring.KrullDimLE 1 R` and `¬ IsField R`, which over a Noetherian domain is `ringKrullDim R = 1`; finite dimensionality of `V` follows from the existence of a lattice.”.

> For lattices `M`, `M'`, `M''` in `V`, `d(M, M'') = d(M, M') + d(M', M'')`.

```lean
theorem Submodule.lengthDist_additive (hR : ¬ IsField R) (M M' M'' : Submodule R V)
    [Submodule.IsLattice K M] [Submodule.IsLattice K M'] [Submodule.IsLattice K M''] :
    M.lengthDist M'' = M.lengthDist M' + M'.lengthDist M''
```

## Tag 02MI, a lemma

[Tag 02MI](https://stacks.math.columbia.edu/tag/02MI) in the Stacks Project.

**`Stacks.OrderOfVanishing.dist_map_eq_ord_det`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/OrderOfVanishing/Defs.lean, line 1340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/OrderOfVanishing/Defs.lean#L1340).

> **Stacks 02MI.** Let `R` be a Noetherian local domain of dimension `1` with
> fraction field `K`, let `V` be a finite dimensional `K`-vector space, and let
> `φ : V → V` be a `K`-linear isomorphism. Then for any lattice `M ⊆ V`,
> `d(M, φ(M)) = ord_R(det φ)`.

```lean
alias dist_map_eq_ord_det
```

## Tag 02MJ, a lemma

[Tag 02MJ](https://stacks.math.columbia.edu/tag/02MJ) in the Stacks Project.

**`finite_maximalSpectrum_and_ordInt_norm_eq_finsum_inertiaDeg_mul_ordInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/OrderOfVanishing/Degree.lean, line 982](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/OrderOfVanishing/Degree.lean#L982). The attribute's comment: “The first conjunct is `B` being semi-local, as `Finite (MaximalSpectrum B)`. The sum is a `finsum` over `MaximalSpectrum B`; `[κ(𝔪ᵢ) : κ(𝔪_A)]` is `Ideal.inertiaDeg 𝔪ᵢ A`, the degree of the residue field of `𝔪ᵢ` over that of `𝔪ᵢ ∩ A = 𝔪_A`; `ord` is `ordInt`. The source's `dim A = 1` is `Ring.KrullDimLE 1 A`, which also admits the field case.”.

> **The order of vanishing of a norm** (Stacks 02MJ). Let `A` be a Noetherian local domain of
> dimension one, and let `A ⊆ B` be a finite extension of domains, with fraction fields `K ⊆ L`.
> Then `B` is semi-local, with maximal ideals `𝔪₁, …, 𝔪ₙ`, and for every `y ∈ L^*` (whose norm is
> nonzero, `L/K` being finite)
>
> `ord_A(Nm_{L/K}(y)) = ∑ᵢ [κ(𝔪ᵢ) : κ(𝔪_A)] · ord_{B_{𝔪ᵢ}}(y)`.
>
> Only the source's hypotheses are assumed. Everything the right-hand side needs is constructed
> in the statement from them: `B` is Noetherian, being finite over `A`; each `B_{𝔪ᵢ}` is a
> Noetherian local domain of dimension at most one; and `B_{𝔪ᵢ}` sits inside `L` as the
> localisation of `B` at the larger submonoid `B ∖ {0}`, so that `L` is its fraction field and
> `B → B_{𝔪ᵢ} → L` is `B → L`.

```lean
theorem finite_maximalSpectrum_and_ordInt_norm_eq_finsum_inertiaDeg_mul_ordInt
    (A B : Type*) [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [IsNoetherianRing A] [IsLocalRing A] [Ring.KrullDimLE 1 A]
    [Algebra A B] [Module.Finite A B] (hAB : Function.Injective (algebraMap A B))
    (K L : Type*) [Field K] [Field L]
    [Algebra A K] [IsFractionRing A K] [Algebra B L] [IsFractionRing B L]
    [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsScalarTower A B L] :
    Finite (MaximalSpectrum B) ∧
      ∀ (y : L) (hy : y ≠ 0),
        haveI : Module.Finite K L := finiteDimensional_fractionRing_of_finite A B K L hAB
        ordInt A (Algebra.norm K y) (Algebra.norm_ne_zero_iff.mpr hy) =
          ∑ᶠ v : MaximalSpectrum B, (v.asIdeal.inertiaDeg A : ℤ) *
            letI : Algebra (Localization.AtPrime v.asIdeal) L :=
              IsLocalization.localizationAlgebraOfSubmonoidLe _ _ v.asIdeal.primeCompl
                (nonZeroDivisors B) v.asIdeal.primeCompl_le_nonZeroDivisors
            haveI : IsScalarTower B (Localization.AtPrime v.asIdeal) L :=
              IsLocalization.localization_isScalarTower_of_submonoid_le _ _
                v.asIdeal.primeCompl (nonZeroDivisors B) v.asIdeal.primeCompl_le_nonZeroDivisors
            haveI : IsFractionRing (Localization.AtPrime v.asIdeal) L :=
              IsFractionRing.isFractionRing_of_isDomain_of_isLocalization v.asIdeal.primeCompl _ _
            haveI : IsNoetherianRing B := IsNoetherianRing.of_finite A B
            haveI := Ring.krullDimLE_one_localization_atPrime_of_finite A B v.asIdeal
            ordInt (Localization.AtPrime v.asIdeal) y hy
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.121, Tag 02MB](https://stacks.math.columbia.edu/tag/02MB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
