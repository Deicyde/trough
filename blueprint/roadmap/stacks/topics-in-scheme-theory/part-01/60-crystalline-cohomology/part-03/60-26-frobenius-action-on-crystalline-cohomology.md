---
declaration: section
origin: cited
lean: Crystalline.FCrystalSituation, Crystalline.SmallFCrystal, Crystalline.SmallFCrystal.Nondegenerate, Matrix.det_mul_det_and_two_sided_of_mul_eq_pow_smul_one, Crystalline.FCrystal.nsmul_two_sided_of_rankLE, Crystalline.FCrystal.nondegenerate_conditions_of_rankLE, Crystalline.FCrystal.exists_isFiniteLocallyFreeOfRankLE_of_compactSpace, Crystalline.GlobalCrystallineSituation.SmallSite.statement07N5
statement: formalized
proof: formalized
---

# 60.26 Frobenius action on crystalline cohomology

Section 60.26 of the Stacks Project, [Tag 07N0](https://stacks.math.columbia.edu/tag/07N0). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07N2, a situation

[Tag 07N2](https://stacks.math.columbia.edu/tag/07N2) in the Stacks Project.

**`Crystalline.FCrystalSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusCrystalSituation.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusCrystalSituation.lean#L44).

> A global crystalline situation over an affine divided power base, with the distinguished
> prime in its divided power ideal and a divided power endomorphism of the base ring lifting the
> absolute Frobenius modulo that prime.
>
> See [Stacks Project, Tag 07N2](https://stacks.math.columbia.edu/tag/07N2).

```lean
public structure FCrystalSituation
```

## Tag 07N3, a definition

[Tag 07N3](https://stacks.math.columbia.edu/tag/07N3) in the Stacks Project.

**`Crystalline.SmallFCrystal`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/FCrystal.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/FCrystal.lean#L116). The attribute's comment: “F-crystal”.

> **Stacks Project, Tag 07N3.**  An *F-crystal on `X/S` relative to `σ`*: a crystal `E` in
> finite locally free `𝒪_{X/S}`-modules on the small crystalline site `Cris(X/S)` together with a map
> `F_E : (F_X)_cris^* E ⟶ E`.
>
> The crystal in finite locally free modules is the notion of [Stacks, Tag 07IU] on `Cris(X/S)`,
> `...SmallSite.ModuleSheaf.IsFiniteLocallyFreeQuasicoherentCrystal`:
> quasi-coherence, condition (1) of [Stacks, Tag 07IT], together with finite local freeness.  The
> pullback `(F_X)_cris^*` is `Crystalline.FCrystalSituation.smallFrobeniusModulePullback`, the
> pullback of modules along `(F_X)_cris = π_X ∘ (F_X)_CRIS ∘ i_X` of [Stacks, Tag 07IK].

```lean
structure SmallFCrystal (T : FCrystalSituation.{u})
```

**`Crystalline.SmallFCrystal.Nondegenerate`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/FCrystal.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/FCrystal.lean#L130). The attribute's comment: “nondegenerate”.

> **Stacks Project, Tag 07N3.**  An F-crystal is *nondegenerate* when there are an integer
> `i ≥ 0` and a map `V : E ⟶ (F_X)_cris^* E` with `V ∘ F_E = p ^ i`, the composite being taken
> diagrammatically as `F_E ≫ V`, an endomorphism of `(F_X)_cris^* E`, and the scalar `p ^ i` acting
> through the `ℕ`-action on morphisms.

```lean
def SmallFCrystal.Nondegenerate {T : FCrystalSituation.{u}} (E : SmallFCrystal T) : Prop
```

## Tag 07N4, a remark

[Tag 07N4](https://stacks.math.columbia.edu/tag/07N4) in the Stacks Project.

**`Matrix.det_mul_det_and_two_sided_of_mul_eq_pow_smul_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracy.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracy.lean#L202). The attribute's comment: “the matrix computation: for r × r matrices K, L over a ring R with K L = p ^ i 1, det(K) det(L) = p ^ (r i), the adjugate L' of L satisfies L' L = L L' = det(L) 1, and K' = p ^ (r i) K satisfies K' L = p ^ j 1 and L K' = p ^ j 1 for j = r i + i”.

> **The matrix computation of [Stacks, Tag 07N4].**  Let `R` be a commutative ring, `r` an
> integer and `K, L` two `r × r` matrices over `R` with `K L = pⁱ 1`.  Then:
>
> * `det(K) det(L) = p ^ (r i)`;
> * the adjugate `L'` of `L` satisfies `L' L = L L' = det(L) 1`;
> * `K' = p ^ (r i) K` satisfies `K' L = p ^ j 1` and `L K' = p ^ j 1`, where `j = r i + i`.
>
> The second-sided identity `L K' = p ^ j 1` is the content: it is obtained, as in the source, from
> the adjugate and the determinant identity.  The element `p` is arbitrary, and `r ≥ 1` is not
> needed.

```lean
theorem det_mul_det_and_two_sided_of_mul_eq_pow_smul_one {r : ℕ}
    {K L : Matrix (Fin r) (Fin r) R} {p : R} {i : ℕ}
    (h : K * L = p ^ i • (1 : Matrix (Fin r) (Fin r) R)) :
    K.det * L.det = p ^ (r * i) ∧
      (L.adjugate * L = L.det • (1 : Matrix (Fin r) (Fin r) R) ∧
        L * L.adjugate = L.det • (1 : Matrix (Fin r) (Fin r) R)) ∧
      (p ^ (r * i) • K) * L = p ^ (r * i + i) • (1 : Matrix (Fin r) (Fin r) R) ∧
      L * (p ^ (r * i) • K) = p ^ (r * i + i) • (1 : Matrix (Fin r) (Fin r) R)
```

**`Crystalline.FCrystal.nsmul_two_sided_of_rankLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracyBoundedRank.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracyBoundedRank.lean#L97). The attribute's comment: “for an F-crystal (E, F) whose rank is bounded by rmax and V as in Definition 07N3 with V ∘ F = p ^ i id, the map V' = p ^ N V with N ≥ rmax * i satisfies V' ∘ F = p ^ (N + i) id and F ∘ V' = p ^ (N + i) id”.

> **The last sentence of [Stacks, Tag 07N4].**  Let `(E, F_E)` be an `F`-crystal whose rank is
> bounded by `rmax`, and let `V` be as in [Stacks, Tag 07N3], `F_E ≫ V = p ^ i • 𝟙`, that is
> `V ∘ F_E = p ^ i • id`.  Setting `V' = p ^ N • V` with `N ≥ rmax * i` gives both
> `V' ∘ F_E = p ^ (N + i) • id` and `F_E ∘ V' = p ^ (N + i) • id`; in diagrammatic order these are
> `F_E ≫ V' = p ^ (N + i) • 𝟙` and `V' ≫ F_E = p ^ (N + i) • 𝟙`.

```lean
theorem FCrystal.nsmul_two_sided_of_rankLE
    (hE : AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRankLE
      (crystallineRingedSite T.global) E.crystal rmax)
    {V : E.crystal ⟶ T.frobeniusModulePullback.obj E.crystal}
    (hV : E.frobenius ≫ V = (T.global.p ^ i) • 𝟙 (T.frobeniusModulePullback.obj E.crystal))
    (hN : rmax * i ≤ N) :
    E.frobenius ≫ ((T.global.p ^ N) • V) =
        (T.global.p ^ (N + i)) • 𝟙 (T.frobeniusModulePullback.obj E.crystal) ∧
      ((T.global.p ^ N) • V) ≫ E.frobenius = (T.global.p ^ (N + i)) • 𝟙 E.crystal
```

**`Crystalline.FCrystal.nondegenerate_conditions_of_rankLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracyBoundedRank.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracyBoundedRank.lean#L170). The attribute's comment: “if the rank of E is bounded, both conditions follow from the nondegeneracy condition of Definition 07N3: there is V' with V' ∘ F = p ^ n id and F ∘ V' = p ^ n id, and there is j ≥ 0 such that Ker(F) and Coker(F) are killed by p ^ j”.

> **[Stacks, Tag 07N4]: for an `F`-crystal of bounded rank, both conditions follow from
> nondegeneracy.**  Let `(E, F)` be an `F`-crystal as in [Stacks, Tag 07N3] whose rank is bounded
> by `rmax`.  If `E` is nondegenerate, that is `V ∘ F = p ^ i • id` for some `i ≥ 0` and some
> `V : E ⟶ (F_X)_cris^* E`, then
>
> * there are `n` and `V'` with `V' ∘ F = p ^ n • id` and `F ∘ V' = p ^ n • id`, the condition
>   often assumed in the literature, and
> * there is an integer `j ≥ 0` such that `Ker(F)` and `Coker(F)` are killed by `p ^ j`, the
>   condition needed for [Stacks, Tag 07N5].
>
> The kernel and the cokernel are described by their universal properties: every map into
> `(F_X)_cris^* E` which `F` sends to zero, and every map out of `E` which kills the image of `F`,
> is killed by `p ^ j`.

```lean
theorem FCrystal.nondegenerate_conditions_of_rankLE
    (hE : AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRankLE
      (crystallineRingedSite T.global) E.crystal rmax) (hnd : E.Nondegenerate) :
    (∃ (n : ℕ) (V' : E.crystal ⟶ T.frobeniusModulePullback.obj E.crystal),
        E.frobenius ≫ V' = (T.global.p ^ n) • 𝟙 (T.frobeniusModulePullback.obj E.crystal) ∧
          V' ≫ E.frobenius = (T.global.p ^ n) • 𝟙 E.crystal) ∧
      ∃ j : ℕ,
        (∀ (Q : SheafOfModules.{u} (crystallineStructureSheaf T.global))
          (q : Q ⟶ T.frobeniusModulePullback.obj E.crystal),
          q ≫ E.frobenius = 0 → (T.global.p ^ j) • q = 0) ∧
        (∀ (Q : SheafOfModules.{u} (crystallineStructureSheaf T.global))
          (q : E.crystal ⟶ Q), E.frobenius ≫ q = 0 → (T.global.p ^ j) • q = 0)
```

**`Crystalline.FCrystal.exists_isFiniteLocallyFreeOfRankLE_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracyBoundedRank.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FrobeniusNondegeneracyBoundedRank.lean#L314). The attribute's comment: “the rank of E is bounded if X is quasi-compact”.

> If `X` is quasi-compact, there is an integer `rmax` such that every object of `CRIS(X/S)` has a
> covering on each member of which `E` is a direct sum of at most `rmax` copies of `𝒪_{X/S}`.

```lean
theorem FCrystal.exists_isFiniteLocallyFreeOfRankLE_of_compactSpace [CompactSpace T.global.X] :
    ∃ rmax : ℕ, AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRankLE
      (crystallineRingedSite T.global) E.crystal rmax
```

## Tag 07N5, a theorem

[Tag 07N5](https://stacks.math.columbia.edu/tag/07N5) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.statement07N5`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Frobenius07N5Theorem.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Frobenius07N5Theorem.lean#L271). The attribute's comment: “the theorem: for a nondegenerate F-crystal over a p-adically complete Noetherian A with X -> S\_0 proper smooth, the canonical map F\_E o (F\_X)\_cris^* on RGamma(Cris(X/S), E) becomes an isomorphism after inverting p”.

> **[Stacks, Tag 07N5].**  In Situation [Stacks, Tag 07N2] let `(E, F_E)` be a nondegenerate
> `F`-crystal.  Assume `A` is a `p`-adically complete Noetherian ring and that `X → S₀` is proper
> smooth.  Then the canonical map
>
> `F_E ∘ (F_X)^*_cris : RΓ(Cris(X/S), E) ⊗^L_{A, σ} A ⟶ RΓ(Cris(X/S), E)`
>
> becomes an isomorphism after inverting `p`.
>
> The conclusion is `...SmallSite.Statement07N5` at `...SmallSite.frobeniusMap07N5Canonical`, the
> canonical `F_E ∘ (F_X)^*_cris`, and its standing hypotheses — `A` Noetherian, `A` `p`-adically
> complete, `X ⟶ S₀` proper, `X ⟶ S₀` smooth, `E` an `F`-crystal, `E` nondegenerate — are the
> tag's own.
>
> The proof is the source's.  The map of the theorem is the composite of the three arrows
> (`frobeniusMap07N5Canonical_eq_comp`).  Arrow 1 is an isomorphism
> (`...SmallSite.isIso_baseChangeArrow07QC`, from [Stacks, Tag 07MU] and [Stacks, Tag 07MY]);
> arrow 2 is an isogeny (`becomesIsoAfterInvertingPrime_relativeFrobeniusArrow07N6`, from
> [Stacks, Tag 07QB]), so arrows 1 and 2 together are an isogeny
> (`becomesIsoAfterInvertingPrime_baseChangeArrow07QC_comp`); arrow 3 is an isogeny by
> nondegeneracy (`...SmallSite.becomesIsoAfterInvertingPrime_frobeniusCohomologyMap`,
> [Stacks, Tag 07N4], with the rank bound `exists_hasBoundedCommonLocalRank_of_isProper`); and the
> three combine by `...SmallSite.becomesIsoAfterInvertingPrime_iff_of_factors`.

```lean
theorem statement07N5 : Statement07N5 T (frobeniusMap07N5Canonical T)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.26, Tag 07N0](https://stacks.math.columbia.edu/tag/07N0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
