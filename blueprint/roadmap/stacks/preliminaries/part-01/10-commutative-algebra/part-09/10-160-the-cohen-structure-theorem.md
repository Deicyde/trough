---
declaration: section
origin: cited
lean: IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries, IsCompleteLocalRing, quotient_isNoetherianCompleteLocalRing, finite_isProduct_isNoetherianCompleteLocalRing, complete_local_ring_noetherian, LocalSubring.IsCoefficientRing, IsCohenRing, IsCohenRing.exists_residueField_ringEquiv
statement: formalized
proof: formalized
---

# 10.160 The Cohen structure theorem

Section 10.160 of the Stacks Project, [Tag 0323](https://stacks.math.columbia.edu/tag/0323). 12 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0323, the section

[Tag 0323](https://stacks.math.columbia.edu/tag/0323) in the Stacks Project.

**`IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean#L672). The tag is given by the `attribute` command at [StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean, line 683](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean#L683). The attribute's comment: “Theorem 032A of the section, the Cohen structure theorem: a complete local ring `(R, 𝔪)` has a coefficient ring, and if `𝔪` is finitely generated then `R` is a quotient of `Λ[[x_1, …, x_n]]` with `Λ` a field or a Cohen ring. The section's opening notion, Definition 0324 of a complete local ring, is also registered under 0323, on `IsCompleteLocalRing`.”. References: EGA 0 (19.8.8), “(i)”.

> **Cohen structure theorem** (Stacks 032A). Let `(R, 𝔪)` be a complete local ring.
> 1. `R` has a coefficient ring: a local subring `Λ ⊆ R` which is complete with maximal ideal
>    `Λ ∩ 𝔪`, whose residue field maps isomorphically onto that of `R`, and with `Λ ∩ 𝔪 = pΛ` for
>    `p` the residue characteristic of `R`.
> 2. If `𝔪` is a finitely generated ideal, then `R` is isomorphic to a quotient
>    `Λ[[x_1, …, x_n]]/I` where `Λ` is either a field or a Cohen ring; equivalently, there is a
>    surjective ring homomorphism `Λ[[x_1, …, x_n]] → R`, whose kernel is `I`.

```lean
public theorem IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries
    (R : Type u) [CommRing R] [IsLocalRing R] [IsAdicComplete (maximalIdeal R) R] :
    (∃ Λ : LocalSubring R, Λ.IsCoefficientRing) ∧
      ((maximalIdeal R).FG →
        ∃ (n : ℕ) (Λ : Type u) (_ : CommRing Λ) (_ : IsDomain Λ),
          (IsField Λ ∨ IsCohenRing Λ) ∧
            ∃ f : MvPowerSeries (Fin n) Λ →+* R, Function.Surjective f)
```

**`IsCompleteLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Defs.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/Defs.lean#L56). The attribute's comment: “Definition 0324 of the section, its opening notion: a complete local ring, a local ring `(R, 𝔪)` whose canonical map `R ⟶ lim_n R / 𝔪ⁿ` is an isomorphism. The section's main theorem, the Cohen structure theorem 032A, is also registered under 0323, on `IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries`.”.

> **Complete local ring.** A local ring `(R, 𝔪)` is a *complete local ring* when the canonical
> ring map `R ⟶ lim_n R / 𝔪ⁿ` to its `𝔪`-adic completion is an isomorphism. The completion is
> Mathlib's `AdicCompletion (maximalIdeal R) R`, the inverse limit of the truncations `R / 𝔪ⁿ`, and
> a ring map is an isomorphism exactly when it is bijective (`IsCompleteLocalRing.ringEquiv`).
> Injectivity is the separatedness `⋂ₙ 𝔪ⁿ = (0)` of the source's footnote.

```lean
def IsCompleteLocalRing (R : Type u) [CommRing R] [IsLocalRing R] : Prop
```

## Tag 0324, a definition

[Tag 0324](https://stacks.math.columbia.edu/tag/0324) in the Stacks Project.

**`IsCompleteLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Defs.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/Defs.lean#L56). The attribute's comment: “The source's definition: `(R, 𝔪)` local is a complete local ring when the canonical map `R ⟶ lim_n R / 𝔪ⁿ` is an isomorphism. The limit is Mathlib's `AdicCompletion (maximalIdeal R) R` (compatible families of residues modulo `𝔪ⁿ • ⊤ = 𝔪ⁿ`), the canonical map is `algebraMap R (AdicCompletion (maximalIdeal R) R)`, and the predicate is its bijectivity, which for a ring map is being an isomorphism; `IsCompleteLocalRing.ringEquiv` is the resulting ring isomorphism. The footnote's `⋂ 𝔪ⁿ = (0)` is the injectivity half. `isCompleteLocalRing_iff_isAdicComplete` identifies the predicate with `IsAdicComplete (maximalIdeal R) R`, the spelling used by the section's later results, and `isCompleteLocalRing_iff_forall_compatible_existsUnique_mk_eq` restates it with the source's truncations `R ⧸ 𝔪ⁿ` and transition maps. The footnote's references 05JC, 05GG, 05GH are separate tags.”.

> **Complete local ring.** A local ring `(R, 𝔪)` is a *complete local ring* when the canonical
> ring map `R ⟶ lim_n R / 𝔪ⁿ` to its `𝔪`-adic completion is an isomorphism. The completion is
> Mathlib's `AdicCompletion (maximalIdeal R) R`, the inverse limit of the truncations `R / 𝔪ⁿ`, and
> a ring map is an isomorphism exactly when it is bijective (`IsCompleteLocalRing.ringEquiv`).
> Injectivity is the separatedness `⋂ₙ 𝔪ⁿ = (0)` of the source's footnote.

```lean
def IsCompleteLocalRing (R : Type u) [CommRing R] [IsLocalRing R] : Prop
```

## Tag 0325, a lemma

[Tag 0325](https://stacks.math.columbia.edu/tag/0325) in the Stacks Project.

**`quotient_isNoetherianCompleteLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean#L91). References: EGA 0 (20.7.20), “special case”; EGA IV (18.5.16), “special case”.

> If `R` is a Noetherian complete local ring and `J` is a proper ideal of `R`, then the
> quotient `R / J` is again a Noetherian complete local ring.

```lean
theorem quotient_isNoetherianCompleteLocalRing
    {R : Type*} [CommRing R] (hR : IsNoetherianCompleteLocalRing R)
    (J : Ideal R) (hJ : J ≠ ⊤) :
    IsNoetherianCompleteLocalRing (R ⧸ J)
```

**`finite_isProduct_isNoetherianCompleteLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean, line 656](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean#L656). References: EGA 0 (22.3.1), “special case”; EGA IV (18.5.9), “(ii), special case”; EGA IV (5.4.3), “special case”; SGA 1 III (1.4), “special case”; SGA 3 VIIB (0.1.1), “special case”; SGA 3 XV (1.5), “partial”; SGA 3 XV (3.9); SGA 4 VIII (4.1), “(i), special case”.

> If `R` is a Noetherian complete local ring and `R → S` is a finite ring map, then `S` is a
> finite product of Noetherian complete local rings: there exist finitely many rings
> `T 0, ..., T (m-1)`, each a Noetherian complete local ring, together with a ring isomorphism
> `S ≃+* Π i, T i`.

```lean
theorem finite_isProduct_isNoetherianCompleteLocalRing
    {R : Type u} [CommRing R] (hR : IsNoetherianCompleteLocalRing R)
    {S : Type v} [CommRing S] [Algebra R S] [Module.Finite R S] :
    ∃ (m : ℕ) (T : Fin m → Type v) (_ : ∀ i, CommRing (T i)),
      (∀ i, IsNoetherianCompleteLocalRing (T i)) ∧
      Nonempty (S ≃+* (Π i, T i))
```

## Tag 032B, a lemma

[Tag 032B](https://stacks.math.columbia.edu/tag/032B) in the Stacks Project.

**`complete_local_ring_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FGMaximalIdeal.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FGMaximalIdeal.lean#L542). References: EGA 0 (7.2.6), “special case”; EGA I (10.6.4), “special case”.

> A local ring `R` that is complete for its maximal-ideal-adic topology and whose maximal
> ideal is finitely generated is Noetherian.

```lean
theorem complete_local_ring_noetherian
    (R : Type*) [CommRing R] [IsLocalRing R]
    (hcomplete : IsAdicComplete (IsLocalRing.maximalIdeal R) R)
    (hfg : (IsLocalRing.maximalIdeal R).FG) :
    IsNoetherianRing R
```

## Tag 0326, a definition

[Tag 0326](https://stacks.math.columbia.edu/tag/0326) in the Stacks Project.

**`LocalSubring.IsCoefficientRing`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/CoefficientRing.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/CoefficientRing.lean#L100).

> A *coefficient ring* of a local ring `(R, 𝔪)` is a local subring `Λ ⊆ R` such that `Λ` is
> complete with maximal ideal `Λ ∩ 𝔪`, the residue field of `Λ` maps isomorphically onto the
> residue field of `R`, and `Λ ∩ 𝔪 = pΛ`, where `p` is the characteristic of the residue field
> of `R`.

```lean
public structure LocalSubring.IsCoefficientRing (Λ : LocalSubring R) : Prop
```

## Tag 0327, a definition

[Tag 0327](https://stacks.math.columbia.edu/tag/0327) in the Stacks Project.

**`IsCohenRing`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenRing.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenRing.lean#L47). The attribute's comment: “complete in the maximal-ideal-adic topology, uniformizer a prime number”. References: EGA 0 (19.8.4), “partial”; SGA 7 I (0.5.3).

> A *Cohen ring* is a complete discrete valuation ring whose uniformizer is
> a (rational) prime number `p`. Concretely, `R` is a domain, it is a discrete
> valuation ring, it is complete for the maximal-ideal-adic topology, and there
> is a prime number `p ∈ ℕ` such that the maximal ideal of `R` is generated by
> the image of `p` in `R`.
>
> This is a class extending `IsDiscreteValuationRing` and `IsAdicComplete` for the maximal ideal, so
> that both the valuation-theoretic and the completeness API of a Cohen ring are available to
> instance search without unfolding the definition, and only the arithmetic condition on the
> uniformizer is a field of its own.

```lean
class IsCohenRing (R : Type*) [CommRing R] [IsDomain R] : Prop extends
    IsDiscreteValuationRing R, IsAdicComplete (IsLocalRing.maximalIdeal R) R
```

## Tag 0328, a lemma

[Tag 0328](https://stacks.math.columbia.edu/tag/0328) in the Stacks Project.

**`IsCohenRing.exists_residueField_ringEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenRing.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenRing.lean#L349). The attribute's comment: “The source's `Λ/pΛ ≅ k` is the conjunction of `maximalIdeal Λ = pΛ`, pinning the uniformizer to the prime `p` that `IsCohenRing` (Stacks 0327) only asserts to exist, with a ring isomorphism `ResidueField Λ ≃+* k`, `ResidueField Λ` being `Λ ⧸ maximalIdeal Λ`. The ring `Λ` is asked for in the universe of `k`. See the module docstring.”. References: EGA 0 (19.8.6), “(ii), special case”.

> **Cohen rings exist** (Stacks 0328). Let `p` be a prime number and let `k` be a field of
> characteristic `p`. Then there is a Cohen ring `Λ` whose uniformizer is `p`, i.e. with
> `maximalIdeal Λ = pΛ`, and whose residue field `Λ/pΛ` is isomorphic to `k`.

```lean
public theorem IsCohenRing.exists_residueField_ringEquiv (p : ℕ) (hp : p.Prime) (k : Type u)
    [Field k] [CharP k p] :
    ∃ (Λ : Type u) (_ : CommRing Λ) (_ : IsDomain Λ) (_ : IsCohenRing Λ),
      maximalIdeal Λ = Ideal.span {(p : Λ)} ∧ Nonempty (ResidueField Λ ≃+* k)
```

## Tag 0329, a lemma

[Tag 0329](https://stacks.math.columbia.edu/tag/0329) in the Stacks Project.

**`IsCohenRing.existsUnique_formallySmooth_zmod_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenRing.lean, line 680](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenRing.lean#L680). The attribute's comment: “A Cohen ring determines its prime: `p` is the characteristic of the residue field, written `CharP (ResidueField Λ) p`, and this makes `p` a prime number and a uniformizer of `Λ`. The statement holds for every `n`, the case `n = 0` being the zero ring on both sides. The ring map is not supplied: the statement asserts that a ring map `ZMod (p ^ n) →+* Λ ⧸ (pⁿ)` exists, that every such map equals it, and that it is formally smooth.”.

> Let `Λ` be a Cohen ring whose residue field has characteristic `p`. For every `n` there is
> exactly one ring map `ℤ/pⁿℤ → Λ/pⁿΛ`, and it is formally smooth (Stacks 0329).

```lean
public theorem IsCohenRing.existsUnique_formallySmooth_zmod_quotient (p n : ℕ) (Λ : Type*)
    [CommRing Λ] [IsDomain Λ] [IsCohenRing Λ] [CharP (ResidueField Λ) p] :
    ∃ φ : ZMod (p ^ n) →+* Λ ⧸ Ideal.span {(p : Λ) ^ n},
      φ.FormallySmooth ∧ ∀ ψ : ZMod (p ^ n) →+* Λ ⧸ Ideal.span {(p : Λ) ^ n}, ψ = φ
```

## Tag 032A, a theorem

[Tag 032A](https://stacks.math.columbia.edu/tag/032A) in the Stacks Project.

**`IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean#L672). The attribute's comment: “Completeness of `R` is `IsAdicComplete (maximalIdeal R) R`, the source's `R ≅ lim_n R/𝔪ⁿ`. The two parts are the two conjuncts, the second guarded by its own hypothesis so that part (1) keeps the source's generality, and its `R ≅ Λ[[x_1, …, x_n]]/I` is stated as the existence of a surjection `MvPowerSeries (Fin n) Λ →+* R` with kernel `I`. See the module docstring.”. References: EGA 0 (19.8.8), “(i)”.

> **Cohen structure theorem** (Stacks 032A). Let `(R, 𝔪)` be a complete local ring.
> 1. `R` has a coefficient ring: a local subring `Λ ⊆ R` which is complete with maximal ideal
>    `Λ ∩ 𝔪`, whose residue field maps isomorphically onto that of `R`, and with `Λ ∩ 𝔪 = pΛ` for
>    `p` the residue characteristic of `R`.
> 2. If `𝔪` is a finitely generated ideal, then `R` is isomorphic to a quotient
>    `Λ[[x_1, …, x_n]]/I` where `Λ` is either a field or a Cohen ring; equivalently, there is a
>    surjective ring homomorphism `Λ[[x_1, …, x_n]] → R`, whose kernel is `I`.

```lean
public theorem IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries
    (R : Type u) [CommRing R] [IsLocalRing R] [IsAdicComplete (maximalIdeal R) R] :
    (∃ Λ : LocalSubring R, Λ.IsCoefficientRing) ∧
      ((maximalIdeal R).FG →
        ∃ (n : ℕ) (Λ : Type u) (_ : CommRing Λ) (_ : IsDomain Λ),
          (IsField Λ ∨ IsCohenRing Λ) ∧
            ∃ f : MvPowerSeries (Fin n) Λ →+* R, Function.Surjective f)
```

## Tag 032C, a remark

[Tag 032C](https://stacks.math.columbia.edu/tag/032C) in the Stacks Project.

**`cohen_structure_consequences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/QuotientOfRegular.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/QuotientOfRegular.lean#L109).

> **Stacks Project, Tag 032C.** If `k` is a field then the power series ring
> `k[[X_1, …, X_d]]` is a Noetherian complete local regular ring of dimension `d`. If `Λ` is a Cohen
> ring then `Λ[[X_1, …, X_d]]` is a complete local Noetherian regular ring of dimension `d + 1`.
> Hence any Noetherian complete local ring is a quotient of a regular local ring, and in particular
> a Noetherian complete local ring is universally catenary.
>
> The four assertions are `MvPowerSeries.isRegularLocalRing_and_ringKrullDim_of_field`,
> `MvPowerSeries.isRegularLocalRing_and_ringKrullDim_of_isCohenRing`,
> `IsLocalRing.exists_isRegularLocalRing_surjective` and
> `isUniversallyCatenary_of_isPrecomplete_maximalIdeal`. Locality of the power series rings is part
> of `IsRegularLocalRing`, and completeness of a local ring is completeness for its maximal ideal.

```lean
theorem cohen_structure_consequences :
    (∀ (k : Type u) [Field k] (d : ℕ),
      IsNoetherianRing (MvPowerSeries (Fin d) k) ∧
        IsAdicComplete (maximalIdeal (MvPowerSeries (Fin d) k)) (MvPowerSeries (Fin d) k) ∧
          IsRegularLocalRing (MvPowerSeries (Fin d) k) ∧
            ringKrullDim (MvPowerSeries (Fin d) k) = d) ∧
    (∀ (Λ : Type u) [CommRing Λ] [IsDomain Λ] [IsCohenRing Λ] (d : ℕ),
      IsNoetherianRing (MvPowerSeries (Fin d) Λ) ∧
        IsAdicComplete (maximalIdeal (MvPowerSeries (Fin d) Λ)) (MvPowerSeries (Fin d) Λ) ∧
          IsRegularLocalRing (MvPowerSeries (Fin d) Λ) ∧
            ringKrullDim (MvPowerSeries (Fin d) Λ) = (d + 1 : ℕ)) ∧
    (∀ (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
      [IsAdicComplete (maximalIdeal R) R],
      ∃ (S : Type u) (_ : CommRing S), IsRegularLocalRing S ∧
        ∃ f : S →+* R, Function.Surjective f) ∧
    (∀ (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
      [IsAdicComplete (maximalIdeal R) R], Ring.IsUniversallyCatenary R)
```

## Tag 0C0S, a lemma

[Tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S) in the Stacks Project.

**`IsRegularLocalRing.nonempty_ringEquiv_and_algEquiv_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Regular.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/Regular.lean#L362). The attribute's comment: “The source's Noetherian complete local regular ring is `IsRegularLocalRing R` with `IsAdicComplete (maximalIdeal R) R`. `R` contains `𝐅_p` or `𝐐` iff it contains a field, which is how the first part is hypothesized; the number of variables is pinned to the embedding dimension, the `d` of the source's proof. The two parts are the two conjuncts, each guarded by its own hypothesis. See the module docstring.”. References: EGA 0 (19.6.3), “a)⇒c), regular case”; EGA 0 (19.6.5), “Â ≅ K[[T\_1,...,T\_n]]”; EGA 0 (19.6.4), “special case”; EGA 0 (19.8.8), “(i), special case”.

> Let `(R, 𝔪)` be a Noetherian complete local ring which is regular, and let `d` be its
> embedding dimension `dim_{R/𝔪} 𝔪/𝔪²`, which equals `dim R`.
> 1. If `R` contains a field — equivalently `𝐅_p` or `𝐐` — then `R` is isomorphic to the power
>    series ring in `d` variables over its residue field.
> 2. If `k` is a field and `k → R` is a ring map inducing an isomorphism `k → R/𝔪`, then `R` is
>    isomorphic as a `k`-algebra to the power series ring in `d` variables over `k`.
> (Stacks 0C0S)

```lean
public theorem IsRegularLocalRing.nonempty_ringEquiv_and_algEquiv_mvPowerSeries (R : Type u)
    [CommRing R] [IsRegularLocalRing R] [IsAdicComplete (maximalIdeal R) R] (d : ℕ)
    (hd : Module.finrank (ResidueField R) (CotangentSpace R) = d) :
    (∀ (F : Type v) [Field F] [Algebra F R],
        Nonempty (R ≃+* MvPowerSeries (Fin d) (ResidueField R))) ∧
      (∀ (k : Type w) [Field k] [Algebra k R],
        Function.Bijective ((residue R).comp (algebraMap k R)) →
          Nonempty (R ≃ₐ[k] MvPowerSeries (Fin d) k))
```

## Tag 032D, a lemma

[Tag 032D](https://stacks.math.columbia.edu/tag/032D) in the Stacks Project.

**`IsLocalRing.exists_injective_finite_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/RegularSubring.lean, line 569](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/RegularSubring.lean#L569). The attribute's comment: “The subring `R₀ ⊆ R` is presented as an injective ring homomorphism `f` from the power series ring it is isomorphic to, so that items (1) and (3) are statements about `MvPowerSeries (Fin d) Λ` and item (2) is one about `f`: `f.Finite` for finiteness and `Function.Surjective ((residue R).comp f)` for the isomorphism on residue fields. See the module docstring.”. References: EGA 0 (19.8.8), “(ii)”.

> Let `(R, 𝔪)` be a Noetherian complete local domain. Then there is a subring `R₀ ⊆ R` which is
> a regular complete local ring, over which `R` is finite, which induces an isomorphism on residue
> fields, and which is a power series ring `Λ[[X_1, …, X_d]]` over a field or over a Cohen ring `Λ`.
> The subring is presented as the image of an injective ring homomorphism
> `f : Λ[[X_1, …, X_d]] → R`, finite and with `R/𝔪` generated by the image of `f`. (Stacks 032D)

```lean
public theorem IsLocalRing.exists_injective_finite_mvPowerSeries (R : Type u) [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] [IsDomain R] [IsAdicComplete (maximalIdeal R) R] :
    ∃ (d : ℕ) (Λ : Type u) (_ : CommRing Λ) (_ : IsDomain Λ),
      (IsField Λ ∨ IsCohenRing Λ) ∧
        ∃ _ : IsRegularLocalRing (MvPowerSeries (Fin d) Λ),
          IsAdicComplete (maximalIdeal (MvPowerSeries (Fin d) Λ)) (MvPowerSeries (Fin d) Λ) ∧
            ∃ f : MvPowerSeries (Fin d) Λ →+* R,
              Function.Injective f ∧ f.Finite ∧ Function.Surjective ((residue R).comp f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.160, Tag 0323](https://stacks.math.columbia.edu/tag/0323)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
