---
declaration: section
origin: cited
lean: AlgebraicGeometry.LocalLefschetzSituation.hasPurity_quotientRing_of_dualizing, AlgebraicGeometry.LocalLefschetzSituation.hasPurity_quotientRing_of_isAdicComplete, AlgebraicGeometry.hasPurity_of_isCompleteIntersectionRing
statement: formalized
proof: formalized
---

# 58.25 Purity in local case, II

Section 58.25 of the Stacks Project, [Tag 0BPB](https://stacks.math.columbia.edu/tag/0BPB). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DXZ, a lemma

[Tag 0DXZ](https://stacks.math.columbia.edu/tag/0DXZ) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.hasPurity_quotientRing_of_dualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NeighbourhoodVocabularyDualizing.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NeighbourhoodVocabularyDualizing.lean#L175). The attribute's comment: “purity for A/fA under the tag's four hypotheses; nothing beyond them is assumed”.

> **Stacks Project, Tag 0DXZ.**  Let `(A, 𝔪)` be a Noetherian local ring and let `f ∈ 𝔪`.
> Write `X = Spec A`.  Assume
>
> 1. `A` has a dualizing complex and is `f`-adically complete,
> 2. one of
>    * (a) `A_f` satisfies Serre's condition `(S₂)` and every irreducible component of `X` not
>      contained in `V(f)` has dimension at least `4`, or
>    * (b) `depth(A_𝔭) + dim(A/𝔭) > 3` whenever `𝔭 ∉ V(f)` and `V(𝔭) ∩ V(f) ≠ {𝔪}`,
> 3. purity holds for `(A_f)_𝔭` for every maximal ideal `𝔭 ⊂ A_f`, and
> 4. purity holds for `A`.
>
> Then purity holds for `A / fA`.
>
> The source's argument is followed.  A finite étale cover of the punctured spectrum `U₀` of
> `A / fA` is, by the essential surjectivity of `FÉt_U ⥤ FÉt_{U₀}` under (1)–(3), the restriction
> of a finite étale cover of the punctured spectrum `U` of `A`; hypothesis (4) extends the latter
> over `X`; and the restriction of that extension to `Spec (A / fA)` is the desired extension of
> the original cover.

```lean
theorem hasPurity_quotientRing_of_dualizing [HasDerivedCategory.{w} (ModuleCat.{u} S.A)]
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hcomplete : IsAdicComplete (Ideal.span {S.f}) S.A)
    (hcond :
      (PropertySkRing (Localization.Away S.f) 2 ∧
          ∀ p : PrimeSpectrum S.A, IsMinimalPrime p.asIdeal → S.f ∉ p.asIdeal →
            (4 : WithBot ℕ∞) ≤ ringKrullDim (S.A ⧸ p.asIdeal)) ∨
        (∀ p : PrimeSpectrum S.A, S.f ∉ p.asIdeal →
          ({q : PrimeSpectrum S.A | p.asIdeal ≤ q.asIdeal} ∩
            {q : PrimeSpectrum S.A | S.f ∈ q.asIdeal}) ≠
            {⟨maximalIdeal S.A, (maximalIdeal.isMaximal S.A).isPrime⟩} →
          (3 : WithBot ℕ∞) <
            (Module.depth (Localization.AtPrime p.asIdeal)
              (maximalIdeal (Localization.AtPrime p.asIdeal))
              (Localization.AtPrime p.asIdeal) : WithBot ℕ∞) +
              ringKrullDim (S.A ⧸ p.asIdeal)))
    (haway : ∀ (p : Ideal (Localization.Away S.f)) [p.IsMaximal],
      HasPurity (Localization.AtPrime p))
    (hpurity : HasPurity S.A) :
    HasPurity S.quotientRing
```

## Tag 0BPC, a lemma

[Tag 0BPC](https://stacks.math.columbia.edu/tag/0BPC) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.hasPurity_quotientRing_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/HypersurfaceExtension.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/HypersurfaceExtension.lean#L275). The attribute's comment: “purity for A/fA under the tag's five hypotheses; nothing beyond them is assumed”.

> **Stacks Project, Tag 0BPC.**  Let `(A, 𝔪)` be a Noetherian local ring and let `f ∈ 𝔪`.
> Assume
>
> 1. `A` is `f`-adically complete,
> 2. `f` is a nonzerodivisor,
> 3. `H¹_𝔪(A/fA)` and `H²_𝔪(A/fA)` are finite `A`-modules,
> 4. purity holds for `(A_f)_𝔭` for every maximal ideal `𝔭 ⊂ A_f`, and
> 5. purity holds for `A`.
>
> Then purity holds for `A / fA`.
>
> The source proves this by the proof of Stacks 0DXZ with Stacks 0EKA in place of Stacks 0EK9, and
> that is what happens here.  A finite étale cover of `U₀` is, by Stacks 0EKA, the restriction of a
> finite étale cover of `U`; hypothesis (5) extends the latter over `X`; and the restriction of that
> extension to `X₀ = Spec (A / fA)` is the extension of the original cover.

```lean
theorem hasPurity_quotientRing_of_isAdicComplete
    (hcomplete : IsAdicComplete S.principalIdeal S.A) (hnzd : S.f ∈ nonZeroDivisors S.A)
    (hH1 : Module.Finite S.A (localCohomologyModule S.A (maximalIdeal S.A)
      (maximalIdeal S.A).fg_of_isNoetherianRing (ModuleCat.of S.A S.quotientRing) 1))
    (hH2 : Module.Finite S.A (localCohomologyModule S.A (maximalIdeal S.A)
      (maximalIdeal S.A).fg_of_isNoetherianRing (ModuleCat.of S.A S.quotientRing) 2))
    (haway : ∀ (p : Ideal (Localization.Away S.f)) [p.IsMaximal],
      HasPurity (Localization.AtPrime p))
    (hpurity : HasPurity S.A) :
    HasPurity S.quotientRing
```

## Tag 0BPD, a proposition

[Tag 0BPD](https://stacks.math.columbia.edu/tag/0BPD) in the Stacks Project.

**`AlgebraicGeometry.hasPurity_of_isCompleteIntersectionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompleteIntersectionPurity.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompleteIntersectionPurity.lean#L512). The attribute's comment: “purity for a complete intersection local ring of dimension at least three; the complete intersection hypothesis is `LocalCompleteIntersection.IsCompleteIntersectionRing` (Tag 09Q3 (1)) and purity is `AlgebraicGeometry.HasPurity`”. References: SGA 2 X (3.4), “3.4(ii)”; SGA 2 XII (3.5), “partial”; SGA 2 XII (4.9), “Clause a)”.

> **Purity for a complete intersection of dimension at least three, [Stacks, Tag 0BPD].** Let
> `(A, 𝔪)` be a Noetherian local ring which is a complete intersection of dimension at least
> three. Then purity holds for `A`: every finite étale cover of the punctured spectrum of `A` is,
> up to isomorphism, the restriction of a finite étale cover of `Spec A`.
>
> Purity descends from the completion of `A`, which by hypothesis is the quotient of a regular
> local ring by an ideal generated by a regular sequence.

```lean
theorem hasPurity_of_isCompleteIntersectionRing
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : LocalCompleteIntersection.IsCompleteIntersectionRing A)
    (hdim : 3 ≤ ringKrullDim A) :
    HasPurity A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.25, Tag 0BPB](https://stacks.math.columbia.edu/tag/0BPB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
