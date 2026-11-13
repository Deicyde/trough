---
declaration: section
origin: cited
lean: PrimeSpectrum.primeSpectrumProdHomeo, PrimeSpectrum.sigmaToPiHomeo, PrimeSpectrum.preconnectedSpace_iff_mul_eq_zero_add_eq_one, PrimeSpectrum.preconnectedSpace_iff_isIdempotentElem, PrimeSpectrum.connectedSpace_iff_isIdempotentElem, IsLocalization.Away.quotient_span_singleton_of_isIdempotentElem, IsLocalization.Away.quotientAlgEquiv, PrimeSpectrum.isClopen_zeroLocus_of_isIdempotentElem_of_fg
statement: formalized
proof: formalized
---

# 10.21 Open and closed subsets of spectra

Section 10.21 of the Stacks Project, [Tag 04PN](https://stacks.math.columbia.edu/tag/04PN). 3 tags here are carried by 6 declarations of the repository (all in StacksCore) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00ED, a lemma

[Tag 00ED](https://stacks.math.columbia.edu/tag/00ED) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.primeSpectrumProdHomeo`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.primeSpectrumProdHomeo#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L20) (StacksCore).
- [`PrimeSpectrum.sigmaToPiHomeo`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.sigmaToPiHomeo#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L21) (StacksCore): “for an arbitrary finite product”.

## Tag 00EF, a lemma

[Tag 00EF](https://stacks.math.columbia.edu/tag/00EF) in the Stacks Project.

**`PrimeSpectrum.preconnectedSpace_iff_mul_eq_zero_add_eq_one`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L72). The attribute's comment: “for a semiring, phrased with complementary pairs”.

> **Stacks 00EF**, in its most general form. Over a semiring the statement must be phrased with
> *complementary pairs* rather than idempotents: an idempotent need not have a complement, so
> "every idempotent is `0` or `1`" is strictly stronger than preconnectedness there. Mathlib's own
> example, on `PrimeSpectrum.mulZeroAddOneEquivClopens`, is the semiring `{0, 0.5, 1}` with `⊔ = +`
> and `⊓ = *`, in which `0.5` is idempotent and uncomplemented.
>
> Pairs `e * f = 0`, `e + f = 1` are exactly what index the clopens of `Spec R`, which is why this
> is the level at which the equivalence is true.

```lean
theorem preconnectedSpace_iff_mul_eq_zero_add_eq_one :
    PreconnectedSpace (PrimeSpectrum R) ↔
      ∀ e f : R, e * f = 0 → e + f = 1 → e = 0 ∨ f = 0
```

**`PrimeSpectrum.preconnectedSpace_iff_isIdempotentElem`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L96). The attribute's comment: “without the nonzero hypothesis, for `PreconnectedSpace`”. References: EGA III (7.8.6.1), “affine case Z = Spec R”.

> **Stacks 00EF** without the nonzero hypothesis. Over a ring every idempotent `e` has the
> complement `1 - e`, so the pair formulation collapses to the familiar one.
>
> This form needs no `Nontrivial R`: for the zero ring `Spec R` is empty, hence preconnected, and
> the right-hand side holds vacuously. It is `ConnectedSpace` — which bundles nonemptiness — that
> forces the hypothesis, see `connectedSpace_iff_isIdempotentElem`.

```lean
theorem preconnectedSpace_iff_isIdempotentElem :
    PreconnectedSpace (PrimeSpectrum R) ↔ ∀ e : R, IsIdempotentElem e → e = 0 ∨ e = 1
```

**`PrimeSpectrum.connectedSpace_iff_isIdempotentElem`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L110). References: EGA III (7.8.6.1), “special case”.

> **Stacks 00EF**: for a nonzero ring, `Spec R` is connected if and only if `R` has no
> nontrivial idempotents.
>
> The `Nontrivial R` hypothesis is load-bearing and not merely inherited from the tag's wording:
> for the zero ring the right-hand side holds vacuously while `Spec R` is empty, so `ConnectedSpace`
> fails. Dropping it would make the statement false, not weaker.

```lean
theorem connectedSpace_iff_isIdempotentElem [Nontrivial R] :
    ConnectedSpace (PrimeSpectrum R) ↔ ∀ e : R, IsIdempotentElem e → e = 0 ∨ e = 1
```

## Tag 00EH, a lemma

[Tag 00EH](https://stacks.math.columbia.edu/tag/00EH) in the Stacks Project.

**`IsLocalization.Away.quotient_span_singleton_of_isIdempotentElem`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Localization/Away/Lemmas.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Away/Lemmas.lean#L30). The attribute's comment: “(2)”. References: SGA 3 VIIB (0.1.1), “partial”.

> **Stacks 00EH**, clause (2), in the tag's orientation: for an idempotent `e`, the quotient
> `R ⧸ (e)` is the localization of `R` away from `1 - e`.
>
> This is `IsLocalization.Away.quotient_of_isIdempotentElem` with `e` replaced by `1 - e`, but that
> substitution cannot be performed by rewriting: the offending `1 - (1 - e)` occurs as a *type index*
> of the quotient, so `simp` and `▸` both fail on the motive. Going through
> `IsLocalization.away_of_isIdempotentElem` instead puts the kernel equation in hypothesis position,
> where `simp` reaches it.

```lean
theorem IsLocalization.Away.quotient_span_singleton_of_isIdempotentElem {e : R}
    (he : IsIdempotentElem e) : IsLocalization.Away (1 - e) (R ⧸ Ideal.span {e})
```

**`IsLocalization.Away.quotientAlgEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Localization/Away/Lemmas.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Away/Lemmas.lean#L37). The attribute's comment: “(2)”.

> **Stacks 00EH**, clause (2), as the isomorphism the tag states. Mathlib carries only the
> `IsLocalization.Away` predicate, never a bundled map, so this records `R ⧸ (e) ≅ R_{1 - e}`.

```lean
noncomputable def IsLocalization.Away.quotientAlgEquiv {e : R} (he : IsIdempotentElem e) :
    (R ⧸ Ideal.span {e}) ≃ₐ[R] Localization.Away (1 - e)
```

**`PrimeSpectrum.isClopen_zeroLocus_of_isIdempotentElem_of_fg`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L123). The attribute's comment: “(3)”.

> **Stacks 00EH**, clause (3): the vanishing locus of a finitely generated idempotent ideal is
> open as well as closed.
>
> Only one implication holds. `I.FG` cannot be dropped — in a rank-one non-discrete valuation ring
> the maximal ideal satisfies `m * m = m` without being finitely generated, and `V(m)` is closed but
> not open — and there is no converse: for `I = (x)` in `k[x]/(x²)` the set `V(I)` is all of
> `Spec R`, hence clopen, while `I * I = 0 ≠ I`.

```lean
theorem isClopen_zeroLocus_of_isIdempotentElem_of_fg {I : Ideal R} (hfg : I.FG)
    (h : IsIdempotentElem I) : IsClopen (zeroLocus (I : Set R))
```

Declarations registered for the tag:

- [`Ideal.isIdempotentElem_iff_of_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.isIdempotentElem_iff_of_fg#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/IdempotentFG.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/IdempotentFG.lean#L12) (StacksCore): “(1)”.
- [`IsLocalization.Away.quotient_of_isIdempotentElem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.Away.quotient_of_isIdempotentElem#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Away/Lemmas.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Away/Lemmas.lean#L15) (StacksCore): “(2)”. References: SGA 3 VIIB (0.1.1), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.21, Tag 04PN](https://stacks.math.columbia.edu/tag/04PN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
