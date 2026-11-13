---
declaration: section
origin: cited
lean: Stacks.Algebraization.isConnected_zeroLocus_diff_and_isConnected_puncturedSpectrum_quotient, Stacks.Algebraization.eq_empty_or_isConnected_zeroLocus_sdiff, Stacks.Algebraization.eq_empty_or_isConnected_zeroLocus_sdiff_of_isDualizingComplex, Stacks.Algebraization.isConnected_zeroLocus_singleton_sdiff_of_isDomain
statement: formalized
proof: formalized
---

# 52.14 Application to connectedness

Section 52.14 of the Stacks Project, [Tag 0ECQ](https://stacks.math.columbia.edu/tag/0ECQ). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ECR, a lemma

[Tag 0ECR](https://stacks.math.columbia.edu/tag/0ECR) in the Stacks Project.

**`Stacks.Algebraization.isConnected_zeroLocus_diff_and_isConnected_puncturedSpectrum_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/VarbaroConnectedness.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/VarbaroConnectedness.lean#L615). The attribute's comment: “both assertions: the connectedness of Y ∖ Z for closed Z ⊆ Y with dim(Z) < min(c, d - 1) - cd(A, I), and of the punctured spectrum of A/I when cd(A, I) < min(c, d - 1)”. References: SGA 2 XIII (2.1), “more general”.

> **Stacks Project, Tag 0ECR** (Varbaro, Theorem 1.6). Let `(A, 𝔪)` be a Noetherian complete
> local ring and `I` a proper ideal of `A`. Set `X = Spec(A)` and `Y = V(I)`, and denote by
>
> 1. `d` the minimal dimension of an irreducible component of `X`
>    (`minDimIrreducibleComponent`), and
> 2. `c` the minimal dimension of a closed subset `Z ⊆ X` such that `X ∖ Z` is disconnected
>    (`minDimDisconnectingClosed`).
>
> Then for `Z ⊆ Y` closed, `Y ∖ Z` is connected if `dim(Z) < min(c, d - 1) - cd(A, I)`. In
> particular, the punctured spectrum of `A/I` is connected if `cd(A, I) < min(c, d - 1)`.
>
> Both minima are attained (`exists_irreducibleComponent_topologicalKrullDim_eq_minDim`,
> `exists_isClosed_not_isConnected_compl_topologicalKrullDim_eq_minDim`). The dimension of `Z` is
> its Krull dimension, `⊥` for `Z = ∅`, compared with the integer `min(c, d - 1) - cd(A, I)` in the
> extended integers. The punctured spectrum of `A/I` is the set of its non-maximal primes.

```lean
theorem isConnected_zeroLocus_diff_and_isConnected_puncturedSpectrum_quotient
    [IsAdicComplete (maximalIdeal A) A] (I : Ideal A) (hI : I ≠ ⊤) :
    (∀ Z : Set (PrimeSpectrum A), IsClosed Z → Z ⊆ zeroLocus (I : Set A) →
      krullDimToEInt (topologicalKrullDim Z) <
        ((min (minDimDisconnectingClosed (PrimeSpectrum A) : ℤ)
            ((minDimIrreducibleComponent (PrimeSpectrum A) : ℤ) - 1) -
          cohomologicalDimension A I I.fg_of_isNoetherianRing : ℤ) : EInt) →
      IsConnected (zeroLocus (I : Set A) \ Z)) ∧
    (cohomologicalDimension A I I.fg_of_isNoetherianRing <
        min (minDimDisconnectingClosed (PrimeSpectrum A) : ℤ)
          ((minDimIrreducibleComponent (PrimeSpectrum A) : ℤ) - 1) →
      IsConnected {p : PrimeSpectrum (A ⧸ I) | ¬ p.asIdeal.IsMaximal})
```

## Tag 0EG5, a lemma

[Tag 0EG5](https://stacks.math.columbia.edu/tag/0EG5) in the Stacks Project.

**`Stacks.Algebraization.eq_empty_or_isConnected_zeroLocus_sdiff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/ConnectednessApplication.lean, line 702](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/ConnectednessApplication.lean#L702). The attribute's comment: “V(I) minus V(a) is empty or connected; hcmp carries 0EIF, the one hypothesis 0EG2 still has”.

> **Stacks Project, Tag 0EG5.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex `K`,
> 2. if `𝔭` is a minimal prime of `A` not contained in `V(I)` and `𝔮 ∈ V(𝔭) ∩ V(𝔞)`, then
>    `dim((A/𝔭)_𝔮) > cd(A, I) + 1`, and
> 3. every nonempty open `V ⊆ Spec(A)` containing `V(I) ∖ V(𝔞)` is connected.
>
> Then `V(I) ∖ V(𝔞)` is either empty or connected.
>
> The proof replaces `A` by its reduction, where the inequality in (2) holds at every associated
> point of the structure sheaf of `U = Spec(A) ∖ V(𝔞)`, and applies Stacks 0EG2 to that structure
> sheaf. A disconnection of `V(I) ∖ V(𝔞)` is turned into a compatible family of sections of
> `𝒪_U / Iⁿ 𝒪_U` which is `1` on one piece and `0` on the other — the nontrivial idempotent of the
> source — and Stacks 0EG2 realizes it as a function on a single open neighbourhood `V` of
> `V(I) ∖ V(𝔞)`, whose germs along that locus take the two values `1` and `0`; the two opens where
> they are attained disconnect a neighbourhood of `V(I) ∖ V(𝔞)`, contradicting (3).
>
> The hypothesis `hcmp` carries the one input Stacks 0EG2 still needs, quantified over every
> Noetherian ring and every pair of ideals, because the reduction step applies Stacks 0EG2 to the
> reduction of `A` rather than to `A`. Its only field is Stacks 0EIF (`serreOneAlternative`),
> which is neither this conclusion nor the conclusion of Stacks 0EG2. The middle clause of Stacks
> 0H48, which Stacks 0EG2 also consumes, is supplied by
> `Stacks.Algebraization.middleComparisonOfShortExact`, and the short exact sequence by
> `Stacks.Algebraization.associatedPointSplitting`.
> Everything this adds over Stacks 0EG2 is proved here: the reduction to the reduced
> case, that minimal primes give condition (2) of Stacks 0EG2, the construction of the
> idempotent, and the passage from a realized idempotent to a disconnection of a neighbourhood.

```lean
public theorem eq_empty_or_isConnected_zeroLocus_sdiff (A : Type u) [CommRing A]
    [IsNoetherianRing A] (I a : Ideal A) (hIa : I ≤ a) [IsAdicComplete I A]
    (K : DerivedCategory (ModuleCat.{u} A)) (hK : Dualizing.IsDualizingComplex K)
    (hdim : ∀ p q : PrimeSpectrum A, p.asIdeal ∈ minimalPrimes A → ¬ I ≤ p.asIdeal →
      p.asIdeal ≤ q.asIdeal → a ≤ q.asIdeal →
      ((cohomologicalDimension A I I.fg_of_isNoetherianRing + 1 : ℤ) : EInt) <
        krullDimToEInt (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
          p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))))
    (hconn : ∀ V : Set (PrimeSpectrum A), IsOpen V → V.Nonempty →
      PrimeSpectrum.zeroLocus (I : Set A) \ PrimeSpectrum.zeroLocus (a : Set A) ⊆ V →
      _root_.IsConnected V)
    (hcmp : ConnectednessComparisonInput.{u}) :
    PrimeSpectrum.zeroLocus (I : Set A) \ PrimeSpectrum.zeroLocus (a : Set A) = ∅ ∨
      _root_.IsConnected
        (PrimeSpectrum.zeroLocus (I : Set A) \ PrimeSpectrum.zeroLocus (a : Set A))
```

**`Stacks.Algebraization.eq_empty_or_isConnected_zeroLocus_sdiff_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalLocusConnected.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalLocusConnected.lean#L89).

> **Stacks Project, Tag 0EG5.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A`. Assume
>
> 1. `A` is `I`-adically complete and has a dualizing complex,
> 2. if `𝔭` is a minimal prime of `A` not contained in `V(I)` and `𝔮 ∈ V(𝔭) ∩ V(𝔞)`, then
>    `dim((A/𝔭)_𝔮) > cd(A, I) + 1`, and
> 3. every nonempty open `V ⊆ Spec(A)` containing `V(I) ∖ V(𝔞)` is connected.
>
> Then `V(I) ∖ V(𝔞)` is either empty or connected.
>
> The proof replaces `A` by its reduction, where the inequality in (2) holds at every associated
> point of the structure sheaf of `U = Spec(A) ∖ V(𝔞)`, and applies Stacks 0EG2 to that structure
> sheaf. A disconnection of `V(I) ∖ V(𝔞)` is turned into a compatible family of sections of
> `𝒪_U / Iⁿ 𝒪_U` which is `1` on one piece and `0` on the other, the nontrivial idempotent of the
> source; Stacks 0EG2 realizes it as a function on an open neighbourhood `V` of `V(I) ∖ V(𝔞)`
> whose germs along that locus take the two values `1` and `0`, and the two opens where they are
> attained disconnect a neighbourhood of `V(I) ∖ V(𝔞)`, contradicting (3).

```lean
public theorem eq_empty_or_isConnected_zeroLocus_sdiff_of_isDualizingComplex (A : Type u)
    [CommRing A] [IsNoetherianRing A] (I a : Ideal A) (hIa : I ≤ a) [IsAdicComplete I A]
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hdim : ∀ p q : PrimeSpectrum A, p.asIdeal ∈ minimalPrimes A → ¬ I ≤ p.asIdeal →
      p.asIdeal ≤ q.asIdeal → a ≤ q.asIdeal →
      ((cohomologicalDimension A I I.fg_of_isNoetherianRing + 1 : ℤ) : EInt) <
        krullDimToEInt (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
          p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))))
    (hconn : ∀ V : Set (PrimeSpectrum A), IsOpen V → V.Nonempty →
      PrimeSpectrum.zeroLocus (I : Set A) \ PrimeSpectrum.zeroLocus (a : Set A) ⊆ V →
      _root_.IsConnected V) :
    PrimeSpectrum.zeroLocus (I : Set A) \ PrimeSpectrum.zeroLocus (a : Set A) = ∅ ∨
      _root_.IsConnected
        (PrimeSpectrum.zeroLocus (I : Set A) \ PrimeSpectrum.zeroLocus (a : Set A))
```

## Tag 0EG3, a lemma

[Tag 0EG3](https://stacks.math.columbia.edu/tag/0EG3) in the Stacks Project.

**`Stacks.Algebraization.isConnected_zeroLocus_singleton_sdiff_of_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusConnected.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalLocusConnected.lean#L81). The attribute's comment: “the whole statement: Y minus Z is connected, at the source's hypotheses”.

> **Stacks Project, Tag 0EG3.** Let `A` be a Noetherian domain which has a dualizing complex
> and which is complete with respect to a nonzero `f ∈ A`. Let `f ∈ 𝔞 ⊆ A` be an ideal. Assume
> every irreducible component of `Z = V(𝔞)` has codimension `> 2` in `X = Spec(A)`, that is,
> `2 < ht(𝔮)` for every minimal prime `𝔮` of `𝔞`. Then `Y ∖ Z` is connected, where `Y = V(f)`.
>
> The dualizing complex may be taken in any model of `D(A)`. The hypothesis `f ≠ 0` is the
> source's; the argument does not use it.

```lean
public theorem isConnected_zeroLocus_singleton_sdiff_of_isDomain (A : Type u) [CommRing A]
    [IsDomain A] [IsNoetherianRing A] [HasDerivedCategory.{w} (ModuleCat.{u} A)]
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (f : A) (_hf : f ≠ 0) [IsAdicComplete (Ideal.span {f}) A] (a : Ideal A) (hfa : f ∈ a)
    (hcodim : ∀ q ∈ a.minimalPrimes, 2 < q.height) :
    _root_.IsConnected
      (PrimeSpectrum.zeroLocus ({f} : Set A) \ PrimeSpectrum.zeroLocus (a : Set A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.14, Tag 0ECQ](https://stacks.math.columbia.edu/tag/0ECQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
