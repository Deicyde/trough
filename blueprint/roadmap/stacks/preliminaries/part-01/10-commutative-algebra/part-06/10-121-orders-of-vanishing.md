---
declaration: section
origin: cited
lean: Module.length_quotSMulTop_mul, span_eq_top_of_isBaseChange, Module.length_quotient_submoduleOf_eq_add, Submodule.isLattice_tfae_of_le_and_iff_of_ge_and_inf_sup, Submodule.lengthDist_eq_sub, Submodule.lengthDist, Submodule.lengthDist_of_le, Submodule.lengthDist_antisymm
statement: formalized
proof: formalized
---

# 10.121 Orders of vanishing

Section 10.121 of the Stacks Project, [Tag 02MB](https://stacks.math.columbia.edu/tag/02MB). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02MC, a lemma

[Tag 02MC](https://stacks.math.columbia.edu/tag/02MC) in the Stacks Project.

**`Module.length_quotSMulTop_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L146). The attribute's comment: “Stated for an arbitrary module `M` in place of `R`, of which the source's identity `length_R(R ⧸ (ab)) = length_R(R ⧸ (a)) + length_R(R ⧸ (b))` is the case `M = R`, and with `b` a nonzerodivisor weakened to `b` acting injectively on `M`. The equation uses no hypothesis on `R`; the source's finiteness assertion is `isFiniteLength_quotient_span_singleton`. See the module docstring.”.

> Let `R` be a commutative ring, `M` an `R`-module and `a`, `b ∈ R` with `b` acting injectively
> on `M`. Then `length_R(M ⧸ abM) = length_R(M ⧸ aM) + length_R(M ⧸ bM)`, an identity in `ℕ∞`.

```lean
theorem Module.length_quotSMulTop_mul {R M : Type*} [CommRing R] [AddCommGroup M]
    [Module R M] {a b : R} (hb : IsSMulRegular M b) :
    Module.length R (QuotSMulTop (a * b) M) =
      Module.length R (QuotSMulTop a M) + Module.length R (QuotSMulTop b M)
```

## Tag 02ME, a definition

[Tag 02ME](https://stacks.math.columbia.edu/tag/02ME) in the Stacks Project.

**`span_eq_top_of_isBaseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L71). The attribute's comment: “The definition itself is Mathlib's `Submodule.IsLattice K M`, finite generation over `R` together with `span_K M = ⊤`; this is the implication from the source's phrasing `V = K ⊗_R M`, the remark following the definition. Locality of `R`, dimension one and finite dimensionality of `V` are used by neither.”.

> If the canonical base-change map `K ⊗[R] M → V` induced by the inclusion `M ↪ V` is an
> isomorphism, then the `K`-span of `M` inside `V` is all of `V`.

```lean
lemma span_eq_top_of_isBaseChange (R : Type*) [CommRing R] (K : Type*) [CommRing K] [Algebra R K]
    (V : Type*) [AddCommGroup V] [Module K V] [Module R V] [IsScalarTower R K V]
    (M : Submodule R V) (h : IsBaseChange K M.subtype) :
    Submodule.span K (M : Set V) = ⊤
```

## Tag 02MF, a lemma

[Tag 02MF](https://stacks.math.columbia.edu/tag/02MF) in the Stacks Project.

**`Module.length_quotient_submoduleOf_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L115). The attribute's comment: “(4). Stated for arbitrary submodules `N ≤ S ≤ A` of a module over a ring, and as an identity in `ℕ∞`, so that no finiteness and none of the source's hypotheses — locality, dimension one, lattices, finite dimensionality of `V` — are needed. Parts (1)-(3) are `Submodule.isLattice_tfae_of_le_and_iff_of_ge_and_inf_sup` and part (5) is `Submodule.lengthDist_eq_sub`.”.

> For `N ≤ S ≤ A` submodules of `V`, `length_R(A/N) = length_R(S/N) + length_R(A/S)`, an
> identity in `ℕ∞`.

```lean
theorem Module.length_quotient_submoduleOf_eq_add {N S A : Submodule R V} (hNS : N ≤ S)
    (hSA : S ≤ A) :
    Module.length R (↥A ⧸ N.submoduleOf A) =
      Module.length R (↥S ⧸ N.submoduleOf S) + Module.length R (↥A ⧸ S.submoduleOf A)
```

**`Submodule.isLattice_tfae_of_le_and_iff_of_ge_and_inf_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L337). The attribute's comment: “Parts (1)-(3). Locality is dropped, being used by no part, and finite dimensionality of `V` follows from the existence of a lattice. Dimension one is an antecedent of parts (1) and (2), over which it is sharp — it is not weakened to `Ring.KrullDimLE 1 R`, which breaks (2) — and part (3) holds over any Noetherian domain, strengthening Mathlib's `Submodule.IsLattice.inf`. Parts (4) and (5) hold for arbitrary submodules of a module over a ring, with none of these hypotheses; they are `Module.length_quotient_submoduleOf_eq_add` and `Submodule.lengthDist_eq_sub`.”.

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

**`Submodule.lengthDist_eq_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L442). The attribute's comment: “(5), in the form `length_R(M/M ∩ M') - length_R(M'/M ∩ M') = length_R(M/N) - length_R(M'/N)`; of the source's three expressions for `d(M, M')` this is the one formalised, the two through `M + M'` and through a lattice `N' ⊇ M + M'` being open. Locality is dropped and dimension one is spelled as the pair `Ring.KrullDimLE 1 R` and `¬ IsField R`, which over a Noetherian domain is `ringKrullDim R = 1`.”.

> For lattices `M`, `M'` and a lattice `N` below both,
> `d(M, M') = length_R(M/N) - length_R(M'/N)`.

```lean
theorem Submodule.lengthDist_eq_sub (hR : ¬ IsField R) {M M' N : Submodule R V}
    [Submodule.IsLattice K M] [Submodule.IsLattice K M'] [Submodule.IsLattice K N] (hNM : N ≤ M)
    (hNM' : N ≤ M') :
    M.lengthDist M' = ((Module.length R (↥M ⧸ N.submoduleOf M)).toNat : ℤ)
      - ((Module.length R (↥M' ⧸ N.submoduleOf M')).toNat : ℤ)
```

## Tag 02MG, a definition

[Tag 02MG](https://stacks.math.columbia.edu/tag/02MG) in the Stacks Project.

**`Submodule.lengthDist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L394). The attribute's comment: “Stated for arbitrary submodules of a module over a ring, since the formula uses none of the source's standing hypotheses: those make the two lengths finite, and are carried by 02MF and 02MH rather than left inert here. The difference is taken after `ENat.toNat`, which is faithful on pairs of lattices by 02MF (1)-(3). See the module docstring.”.

> The distance between two submodules `M`, `M'` of a module `V` over a ring `R`: the integer
> `d(M, M') = length_R(M/(M ∩ M')) - length_R(M'/(M ∩ M'))`, with both lengths truncated from `ℕ∞`
> by `ENat.toNat`.

```lean
noncomputable def Submodule.lengthDist {R : Type*} [Ring R] {V : Type*} [AddCommGroup V]
    [Module R V] (M M' : Submodule R V) : ℤ
```

**`Submodule.lengthDist_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L402). The attribute's comment: “The remark following the definition. Stated for arbitrary submodules of a module over a ring; on a pair of lattices the length is finite by 02MF (2).”.

> For `M' ≤ M`, `d(M, M') = length_R(M/M')`.

```lean
theorem Submodule.lengthDist_of_le {M M' : Submodule R V} (h : M' ≤ M) :
    M.lengthDist M' = (Module.length R (↥M ⧸ M'.submoduleOf M)).toNat
```

## Tag 02MH, a lemma

[Tag 02MH](https://stacks.math.columbia.edu/tag/02MH) in the Stacks Project.

**`Submodule.lengthDist_antisymm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L410). The attribute's comment: “(2). Stated for arbitrary submodules of a module over a ring: with both quotients normalised by `M ⊓ M'` the identity is the antisymmetry of a difference.”.

> The distance between two submodules is antisymmetric: `d(M, M') = -d(M', M)`.

```lean
theorem Submodule.lengthDist_antisymm (M M' : Submodule R V) :
    M.lengthDist M' = - M'.lengthDist M
```

**`Submodule.lengthDist_additive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Lattice/Distance.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Lattice/Distance.lean#L457). The attribute's comment: “(1). Locality is dropped and dimension one is spelled as the pair `Ring.KrullDimLE 1 R` and `¬ IsField R`, which over a Noetherian domain is `ringKrullDim R = 1`; finite dimensionality of `V` follows from the existence of a lattice.”.

> For lattices `M`, `M'`, `M''` in `V`, `d(M, M'') = d(M, M') + d(M', M'')`.

```lean
theorem Submodule.lengthDist_additive (hR : ¬ IsField R) (M M' M'' : Submodule R V)
    [Submodule.IsLattice K M] [Submodule.IsLattice K M'] [Submodule.IsLattice K M''] :
    M.lengthDist M'' = M.lengthDist M' + M'.lengthDist M''
```

## Tag 02MI, a lemma

[Tag 02MI](https://stacks.math.columbia.edu/tag/02MI) in the Stacks Project.

**`Stacks.OrderOfVanishing.dist_map_eq_ord_det`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/OrderOfVanishing/Defs.lean, line 1338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/OrderOfVanishing/Defs.lean#L1338).

> **Stacks 02MI.** Let `R` be a Noetherian local domain of dimension `1` with
> fraction field `K`, let `V` be a finite dimensional `K`-vector space, and let
> `φ : V → V` be a `K`-linear isomorphism. Then for any lattice `M ⊆ V`,
> `d(M, φ(M)) = ord_R(det φ)`.

```lean
alias dist_map_eq_ord_det
```

## Tag 02MJ, a lemma

[Tag 02MJ](https://stacks.math.columbia.edu/tag/02MJ) in the Stacks Project.

**`ord_norm_eq_sum_inertiaDeg_mul_ord`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/OrderOfVanishing/Norm.lean, line 2765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/OrderOfVanishing/Norm.lean#L2765).

> **Stacks 02MJ.** The order of vanishing of the norm of `b` is the sum, over the maximal
> ideals `v` of `B`, of the inertia degree of `v` times the order of vanishing of `b` in `B_v`.
>
> The localization data for each maximal ideal of `B` is supplied as instance hypotheses: for
> each `v : MaximalSpectrum B` the localization `Localization.AtPrime v.asIdeal` is a Noetherian
> ring of Krull dimension at most `1`, carries an algebra structure to `L` compatible with
> `B → L`, the `IsScalarTower` hypothesis pinning it down as the canonical localization map, and
> is a fraction ring of `L`. These say exactly that each `B_{mᵢ}` is a one-dimensional Noetherian
> local domain with fraction field `L`.

```lean
theorem ord_norm_eq_sum_inertiaDeg_mul_ord
    (A B : Type*) [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [Algebra A B] [Module.Finite A B]
    [IsNoetherianRing A] [IsLocalRing A] [Ring.KrullDimLE 1 A]
    (K L : Type*) [Field K] [Field L]
    [Algebra A K] [IsFractionRing A K] [Algebra B L] [IsFractionRing B L]
    [Algebra K L] [Algebra A L] [IsScalarTower A K L] [IsScalarTower A B L]
    [Fintype (MaximalSpectrum B)]
    [∀ v : MaximalSpectrum B, IsNoetherianRing (Localization.AtPrime v.asIdeal)]
    [∀ v : MaximalSpectrum B, Ring.KrullDimLE 1 (Localization.AtPrime v.asIdeal)]
    [∀ v : MaximalSpectrum B, Algebra (Localization.AtPrime v.asIdeal) L]
    [∀ v : MaximalSpectrum B, IsScalarTower B (Localization.AtPrime v.asIdeal) L]
    [∀ v : MaximalSpectrum B, IsFractionRing (Localization.AtPrime v.asIdeal) L]
    (hAB : Function.Injective (algebraMap A B))
    (y : L) (hy : y ≠ 0)
    (x : K) (hx : x = Algebra.norm K y)
    (hx0 : x ≠ 0) :
    ordInt A x hx0 =
      ∑ v : MaximalSpectrum B,
        (Ideal.inertiaDeg' (IsLocalRing.maximalIdeal A) v.asIdeal : ℤ) *
          ordInt (Localization.AtPrime v.asIdeal) y hy
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.121, Tag 02MB](https://stacks.math.columbia.edu/tag/02MB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
