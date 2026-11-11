---
declaration: section
origin: cited
lean: IsLocalRing.isAdicComplete_maximalIdeal_iff_forall_compatible_existsUnique_mk_eq, quotient_isNoetherianCompleteLocalRing, finite_isProduct_isNoetherianCompleteLocalRing, complete_local_ring_noetherian, LocalSubring.IsCoefficientRing, IsCohenRing, IsCohenRing.exists_residueField_ringEquiv, IsCohenRing.formallySmooth_quotient_span_pow
statement: formalized
proof: formalized
---

# 10.160 The Cohen structure theorem

Section 10.160 of the Stacks Project, [Tag 0323](https://stacks.math.columbia.edu/tag/0323). 12 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0323, the section

[Tag 0323](https://stacks.math.columbia.edu/tag/0323) in the Stacks Project.

**`IsLocalRing.isAdicComplete_maximalIdeal_iff_forall_compatible_existsUnique_mk_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/InverseLimitCharacterization.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/InverseLimitCharacterization.lean#L122). The attribute's comment: “0323 is the label of the heading `\section{The Cohen structure theorem}`, not of a mathematical statement: it has no hypotheses and no conclusion, so NO single theorem can be a faithful formalization of it, and this attribute is placed under the project's rule that a tag which is not a statement as written is carried in corrected form with the correction recorded. The correction: 0323 is carried here, on the section's OPENING NOTION — the section begins `Here is a fundamental notion in commutative algebra` and then states Definition 0324, the definition of a complete local ring, which is what this declaration characterizes — and the section's remaining eleven labelled items are carried at their own tags elsewhere in this library, not here. Namely: 032A, the Cohen structure theorem itself, on `IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries` in `StacksFrontier.RingTheory.CompleteLocalRing.CohenStructureTheorem`; 032D on `IsLocalRing.exists_injective_finite_mvPowerSeries` in the same module; 0C0S, the power series description of a regular complete local ring, on `IsRegularLocalRing.nonempty_ringEquiv_and_algEquiv_mvPowerSeries` in `StacksFrontier.RingTheory.CompleteLocalRing.Regular`; 0325 on `quotient_isNoetherianCompleteLocalRing` and `finite_isProduct_isNoetherianCompleteLocalRing`, and 032B on `complete_local_ring_noetherian`, all in `StacksFrontier.RingTheory.CompleteLocalRing.Noetherian`; 0326 on `LocalSubring.IsCoefficientRing` in `StacksFrontier.RingTheory.CompleteLocalRing.CoefficientRing`; 0327 on the class `IsCohenRing`, 0328 on `IsCohenRing.exists_residueField_ringEquiv` and 0329 on `IsCohenRing.formallySmooth_quotient_span_pow`, all in `StacksFrontier.RingTheory.CohenRing`; and 032C on `isUniversallyCatenary_of_isPrecomplete_maximalIdeal` in `StacksFrontier.RingTheory.Catenary.Formal`. With 0324 carried here, every labelled item of the section now has a carrier and only the heading itself had none.”.

> **A local ring is complete exactly when it is the inverse limit of its adic truncations.**
>
> Let `(R, 𝔪)` be a local ring. Then `R` is `𝔪`-adically complete if and only if for every
> family `f` of residues `f n : R ⧸ 𝔪ⁿ` that is compatible with the truncation maps
> `R ⧸ 𝔪ⁿ → R ⧸ 𝔪ᵏ` for `k ≤ n`, there is a *unique* `r : R` whose residue modulo `𝔪ⁿ` is
> `f n` for every `n`.
>
> This is the Stacks project's definition of a complete local ring: a compatible family is an
> element of `lim_n R / 𝔪ⁿ`, existence of `r` says the canonical map `R → lim_n R / 𝔪ⁿ` is
> surjective, and uniqueness says it is injective, so the two together say that this ring map is
> an isomorphism. Uniqueness for the zero family is the separatedness `⋂ₙ 𝔪ⁿ = (0)` that the
> source's footnote insists on; it corresponds to the `IsHausdorff` half of `IsAdicComplete`,
> while existence corresponds to the `IsPrecomplete` half.

```lean
theorem IsLocalRing.isAdicComplete_maximalIdeal_iff_forall_compatible_existsUnique_mk_eq
    (R : Type u) [CommRing R] [IsLocalRing R] :
    IsAdicComplete (maximalIdeal R) R ↔
      ∀ f : (n : ℕ) → R ⧸ maximalIdeal R ^ n,
        (∀ (k n : ℕ) (h : k ≤ n),
            Ideal.Quotient.factor (Ideal.pow_le_pow_right h) (f n) = f k) →
          ∃! r : R, ∀ n : ℕ, Ideal.Quotient.mk (maximalIdeal R ^ n) r = f n
```

## Tag 0324, a definition

[Tag 0324](https://stacks.math.columbia.edu/tag/0324) in the Stacks Project.

**`IsLocalRing.isAdicComplete_maximalIdeal_iff_forall_compatible_existsUnique_mk_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/InverseLimitCharacterization.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/InverseLimitCharacterization.lean#L122). The attribute's comment: “The source defines `(R, 𝔪)` to be a *complete local ring* when the canonical map `R ⟶ lim_n R / 𝔪ⁿ` is an isomorphism. This library has no definition of its own for that: completeness of a local ring is spelled `IsAdicComplete (IsLocalRing.maximalIdeal R) R` everywhere downstream (for instance in 032A, 032D and 0C0S), and introducing a second name for it would shadow canonical Mathlib API. So the definition is carried as the CHARACTERIZATION theorem that identifies the library's spelling with the source's: `IsAdicComplete` holds iff every compatible family of residues modulo `𝔪ⁿ` comes from a unique element of `R`, i.e. iff the canonical ring map into the inverse limit is bijective, hence an isomorphism. `lim_n R/𝔪ⁿ` is not named as an object; it is spelled by its universal property, with the source's own truncations `Ideal.Quotient.mk (𝔪ⁿ)` and transition maps `Ideal.Quotient.factor`, so the statement does not depend on a model of the limit. The source's footnote — that this includes `⋂ 𝔪ⁿ = (0)`, `R` complete AND separated — is the uniqueness half of the `∃!`, applied to the zero family; it matches the `IsHausdorff` component of `IsAdicComplete`, existence matching `IsPrecomplete`. The footnote's three cross-references (05JC, 05GG, 05GH) are remarks on when the completion is itself complete and Noetherian; they are separate tags and are not claimed here.”.

> **A local ring is complete exactly when it is the inverse limit of its adic truncations.**
>
> Let `(R, 𝔪)` be a local ring. Then `R` is `𝔪`-adically complete if and only if for every
> family `f` of residues `f n : R ⧸ 𝔪ⁿ` that is compatible with the truncation maps
> `R ⧸ 𝔪ⁿ → R ⧸ 𝔪ᵏ` for `k ≤ n`, there is a *unique* `r : R` whose residue modulo `𝔪ⁿ` is
> `f n` for every `n`.
>
> This is the Stacks project's definition of a complete local ring: a compatible family is an
> element of `lim_n R / 𝔪ⁿ`, existence of `r` says the canonical map `R → lim_n R / 𝔪ⁿ` is
> surjective, and uniqueness says it is injective, so the two together say that this ring map is
> an isomorphism. Uniqueness for the zero family is the separatedness `⋂ₙ 𝔪ⁿ = (0)` that the
> source's footnote insists on; it corresponds to the `IsHausdorff` half of `IsAdicComplete`,
> while existence corresponds to the `IsPrecomplete` half.

```lean
theorem IsLocalRing.isAdicComplete_maximalIdeal_iff_forall_compatible_existsUnique_mk_eq
    (R : Type u) [CommRing R] [IsLocalRing R] :
    IsAdicComplete (maximalIdeal R) R ↔
      ∀ f : (n : ℕ) → R ⧸ maximalIdeal R ^ n,
        (∀ (k n : ℕ) (h : k ≤ n),
            Ideal.Quotient.factor (Ideal.pow_le_pow_right h) (f n) = f k) →
          ∃! r : R, ∀ n : ℕ, Ideal.Quotient.mk (maximalIdeal R ^ n) r = f n
```

## Tag 0325, a lemma

[Tag 0325](https://stacks.math.columbia.edu/tag/0325) in the Stacks Project.

**`quotient_isNoetherianCompleteLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean#L91). References: EGA 0 (20.7.20), “special case”; EGA IV (18.5.16), “special case”.

> If `R` is a Noetherian complete local ring and `J` is a proper ideal of `R`, then the
> quotient `R / J` is again a Noetherian complete local ring.

```lean
theorem quotient_isNoetherianCompleteLocalRing
    {R : Type*} [CommRing R] (hR : IsNoetherianCompleteLocalRing R)
    (J : Ideal R) (hJ : J ≠ ⊤) :
    IsNoetherianCompleteLocalRing (R ⧸ J)
```

**`finite_isProduct_isNoetherianCompleteLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean, line 657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FiniteProduct.lean#L657). References: EGA 0 (22.3.1), “special case”; EGA IV (18.5.9), “(ii), special case”; EGA IV (5.4.3), “special case”; SGA 1 III (1.4), “special case”; SGA 3 VIIB (0.1.1), “special case”; SGA 3 XV (1.5), “partial”; SGA 3 XV (3.9); SGA 4 VIII (4.1), “(i), special case”.

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

**`complete_local_ring_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FGMaximalIdeal.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/Noetherian/FGMaximalIdeal.lean#L541). References: EGA 0 (7.2.6), “special case”; EGA I (10.6.4), “special case”.

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

**`LocalSubring.IsCoefficientRing`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/CoefficientRing.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/CoefficientRing.lean#L100).

> A *coefficient ring* of a local ring `(R, 𝔪)` is a local subring `Λ ⊆ R` such that `Λ` is
> complete with maximal ideal `Λ ∩ 𝔪`, the residue field of `Λ` maps isomorphically onto the
> residue field of `R`, and `Λ ∩ 𝔪 = pΛ`, where `p` is the characteristic of the residue field
> of `R`.

```lean
public structure LocalSubring.IsCoefficientRing (Λ : LocalSubring R) : Prop
```

## Tag 0327, a definition

[Tag 0327](https://stacks.math.columbia.edu/tag/0327) in the Stacks Project.

**`IsCohenRing`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenRing.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenRing.lean#L46). References: EGA 0 (19.8.4), “partial”; SGA 7 I (0.5.3).

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

**`IsCohenRing.exists_residueField_ringEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenRing.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenRing.lean#L348). The attribute's comment: “The source's `Λ/pΛ ≅ k` is the conjunction of `maximalIdeal Λ = pΛ`, pinning the uniformizer to the prime `p` that `IsCohenRing` (Stacks 0327) only asserts to exist, with a ring isomorphism `ResidueField Λ ≃+* k`, `ResidueField Λ` being `Λ ⧸ maximalIdeal Λ`. The ring `Λ` is asked for in the universe of `k`. See the module docstring.”. References: EGA 0 (19.8.6), “(ii), special case”.

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

**`IsCohenRing.formallySmooth_quotient_span_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenRing.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenRing.lean#L666). The attribute's comment: “The source's `p > 0` prime and `p` a uniformizer are consequences of `CharP (ResidueField Λ) p` for a Cohen ring, so only the latter is assumed, and `n ≥ 1` is dropped because `n = 0` gives the zero ring on both sides. The `ZMod (p ^ n)`-algebra structure is assumed rather than synthesized; it is unique where it exists, so this pins the source's map `ℤ/pⁿℤ → Λ/pⁿΛ`. See the module docstring.”.

> Let `Λ` be a Cohen ring whose residue field has characteristic `p`, so that `p` is a
> uniformizer of `Λ`. For every `n` the ring map `ℤ/pⁿℤ → Λ/pⁿΛ` is formally smooth
> (Stacks 0329).

```lean
public theorem IsCohenRing.formallySmooth_quotient_span_pow (p n : ℕ) (Λ : Type*) [CommRing Λ]
    [IsDomain Λ] [IsCohenRing Λ] [CharP (ResidueField Λ) p]
    [Algebra (ZMod (p ^ n)) (Λ ⧸ Ideal.span {(p : Λ) ^ n})] :
    Algebra.FormallySmooth (ZMod (p ^ n)) (Λ ⧸ Ideal.span {(p : Λ) ^ n})
```

## Tag 032A, a theorem

[Tag 032A](https://stacks.math.columbia.edu/tag/032A) in the Stacks Project.

**`IsLocalRing.exists_isCoefficientRing_and_exists_surjective_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/CoefficientRing.lean#L672). The attribute's comment: “Completeness of `R` is `IsAdicComplete (maximalIdeal R) R`, the source's `R ≅ lim_n R/𝔪ⁿ`. The two parts are the two conjuncts, the second guarded by its own hypothesis so that part (1) keeps the source's generality, and its `R ≅ Λ[[x_1, …, x_n]]/I` is stated as the existence of a surjection `MvPowerSeries (Fin n) Λ →+* R` with kernel `I`. See the module docstring.”. References: EGA 0 (19.8.8), “(i)”.

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

**`isUniversallyCatenary_of_isPrecomplete_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Formal.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Formal.lean#L293). The attribute's comment: “universally catenary”. References: EGA IV (5.2.5), “special case”; EGA IV (5.6.4), “special case”; EGA IV (7.1.11), “clause (i), special case”; EGA IV (7.5.3), “more general”.

> **Stacks Project, Tag 032C.** A Noetherian complete local ring is universally catenary.
>
> By the Cohen structure theorem it is a quotient of a power series ring over a field or over a
> Cohen ring, hence of a regular local ring; a regular local ring is Cohen-Macaulay with full
> support, so [Stacks, Tag 00NM] applies, and universal catenarity passes to quotients.
>
> Completeness is asked for as precompleteness for the maximal ideal, as in [Stacks, Tag 07PJ]; the
> Hausdorff half is automatic for a Noetherian local ring, so a ring carrying
> `IsAdicComplete (IsLocalRing.maximalIdeal R) R` satisfies the hypothesis by inference.

```lean
theorem isUniversallyCatenary_of_isPrecomplete_maximalIdeal
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsPrecomplete (IsLocalRing.maximalIdeal R) R] : Ring.IsUniversallyCatenary R
```

## Tag 0C0S, a lemma

[Tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S) in the Stacks Project.

**`IsRegularLocalRing.nonempty_ringEquiv_and_algEquiv_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/Regular.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/Regular.lean#L362). The attribute's comment: “The source's Noetherian complete local regular ring is `IsRegularLocalRing R` with `IsAdicComplete (maximalIdeal R) R`. `R` contains `𝐅_p` or `𝐐` iff it contains a field, which is how the first part is hypothesized; the number of variables is pinned to the embedding dimension, the `d` of the source's proof. The two parts are the two conjuncts, each guarded by its own hypothesis. See the module docstring.”. References: EGA 0 (19.6.3), “a)⇒c), regular case”; EGA 0 (19.6.5), “Â ≅ K[[T\_1,...,T\_n]]”; EGA 0 (19.6.4), “special case”; EGA 0 (19.8.8), “(i), special case”.

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

**`IsLocalRing.exists_injective_finite_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/RegularSubring.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/CohenStructureTheorem/RegularSubring.lean#L569). The attribute's comment: “The subring `R₀ ⊆ R` is presented as an injective ring homomorphism `f` from the power series ring it is isomorphic to, so that items (1) and (3) are statements about `MvPowerSeries (Fin d) Λ` and item (2) is one about `f`: `f.Finite` for finiteness and `Function.Surjective ((residue R).comp f)` for the isomorphism on residue fields. See the module docstring.”. References: EGA 0 (19.8.8), “(ii)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
