---
declaration: section
origin: cited
lean: exists_henselization, flat_henselization_and_bijective_quotientMap, isHenselization_of_henselizationPair, henselization_isNoetherian_and_completion_equiv, henselization_preserves_filtered_colimits, henselizations_equiv_of_zeroLocus_eq, henselization_tensorProduct_bijective_of_isIntegral, henselization_iInf_equiv_pi
statement: formalized
proof: formalized
---

# 15.12 Henselization of pairs

Section 15.12 of the Stacks Project, [Tag 0EM7](https://stacks.math.columbia.edu/tag/0EM7). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A02, a lemma

[Tag 0A02](https://stacks.math.columbia.edu/tag/0A02) in the Stacks Project.

**`exists_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/UniversalProperty.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/UniversalProperty.lean#L427).

> Every pair `(A, I)` has a henselization: there is a henselian pair `(Aʰ, IAʰ)` under `(A, I)`
> which is initial among henselian pairs under `(A, I)`. Equivalently, the inclusion of henselian
> pairs into pairs has a left adjoint.

```lean
theorem exists_henselization (A : Type u) [CommRing A] (I : Ideal A) :
    ∃ (Ah : Type u) (_ : CommRing Ah) (ι : A →+* Ah),
      HenselianPair Ah (I.map ι) ∧
        ∀ (B : Type v) (_ : CommRing B) (J : Ideal B),
          HenselianPair B J →
            ∀ f : A →+* B, I ≤ J.comap f →
              ∃! g : Ah →+* B, g.comp ι = f ∧ I.map ι ≤ J.comap g
```

## Tag 0AGU, a lemma

[Tag 0AGU](https://stacks.math.columbia.edu/tag/0AGU) in the Stacks Project.

**`flat_henselization_and_bijective_quotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/FlatLocalNoetherian.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/FlatLocalNoetherian.lean#L53).

> The structural map to the henselization of a pair is flat, and it induces an isomorphism modulo
> every power of the distinguished ideal.

```lean
public theorem flat_henselization_and_bijective_quotientMap
    (A : Type u) [CommRing A] (I : Ideal A)
    (Ah : Type v) [CommRing Ah] [Algebra A Ah]
    (hh : HenselianPair Ah (I.map (algebraMap A Ah)))
    (hι : ∀ (B : Type (max u v)) (_ : CommRing B) (J : Ideal B),
      HenselianPair B J →
        ∀ f : A →+* B, I ≤ J.comap f →
          ∃! g : Ah →+* B,
            g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g) :
    Module.Flat A Ah ∧
      ∀ n : ℕ,
        Function.Bijective
          (Ideal.quotientMap (Ideal.map (algebraMap A Ah) (I ^ n))
            (algebraMap A Ah) Ideal.le_comap_map)
```

## Tag 0A03, a lemma

[Tag 0A03](https://stacks.math.columbia.edu/tag/0A03) in the Stacks Project.

**`isHenselization_of_henselizationPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/FlatLocalNoetherian.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/FlatLocalNoetherian.lean#L140).

> A henselization of the pair consisting of a local ring and its maximal ideal is a henselization
> of the local ring. In particular, the target is local and the structural map is a local ring
> homomorphism.

```lean
public theorem isHenselization_of_henselizationPair
    (A : Type u) [CommRing A] [IsLocalRing A]
    (Ah : Type u) [CommRing Ah] [Algebra A Ah]
    (hh : HenselianPair Ah
      ((maximalIdeal A).map (algebraMap A Ah)))
    (hι : ∀ (B : Type u) (_ : CommRing B) (J : Ideal B),
      HenselianPair B J →
        ∀ f : A →+* B, maximalIdeal A ≤ J.comap f →
          ∃! g : Ah →+* B,
            g.comp (algebraMap A Ah) = f ∧
              (maximalIdeal A).map (algebraMap A Ah) ≤ J.comap g) :
    ∃ (_ : IsLocalRing Ah) (_ : IsLocalHom (algebraMap A Ah)),
      IsHenselization A (ResidueField A) Ah
```

## Tag 0AGV, a lemma

[Tag 0AGV](https://stacks.math.columbia.edu/tag/0AGV) in the Stacks Project.

**`henselization_isNoetherian_and_completion_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/FlatLocalNoetherian.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/FlatLocalNoetherian.lean#L249).

> The henselization of a Noetherian pair is Noetherian and has the same adic completion. The
> structural map to the henselization is flat, and the canonical map from the henselization to the
> original completion is faithfully flat (and hence, in particular, flat).

```lean
public theorem henselization_isNoetherian_and_completion_equiv
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (Ah : Type v) [CommRing Ah] [Algebra A Ah]
    (hh : HenselianPair Ah (I.map (algebraMap A Ah)))
    (hι : ∀ (B : Type (max u v)) (_ : CommRing B) (J : Ideal B),
      HenselianPair B J →
        ∀ f : A →+* B, I ≤ J.comap f →
          ∃! g : Ah →+* B,
            g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g) :
    Function.Bijective
        (adicCompletionMap (algebraMap A Ah) I
          (I.map (algebraMap A Ah)) le_rfl) ∧
      IsNoetherianRing Ah ∧
        (algebraMap A Ah).Flat ∧
        ∃ g : Ah →ₐ[A] AdicCompletion I A,
          g.toRingHom.Flat ∧
            g.toRingHom.FaithfullyFlat
```

## Tag 0A04, a lemma

[Tag 0A04](https://stacks.math.columbia.edu/tag/0A04) in the Stacks Project.

**`henselization_preserves_filtered_colimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean#L144).

> Henselization of pairs commutes with filtered colimits. More precisely, for a filtered diagram
> of pairs and its naturally induced diagram of henselizations, any colimit of the latter is a
> henselization of the colimit of the former. Its extended ideal is the supremum of the images of the
> extended ideals at the stages.

```lean
theorem henselization_preserves_filtered_colimits
    {K : Type v} [SmallCategory K] [IsFiltered K]
    (F Fh : Functor K CommRingCat.{max u v})
    (I : ∀ k, Ideal (F.obj k))
    (hI : ∀ ⦃j k⦄ (f : j ⟶ k), Ideal.map (F.map f).hom (I j) ≤ I k)
    (η : F ⟶ Fh)
    (hFh : ∀ k, HenselianPair (Fh.obj k) (Ideal.map (η.app k).hom (I k)))
    (hη : ∀ k (B : Type w) (_ : CommRing B) (J : Ideal B),
      HenselianPair B J →
        ∀ f : F.obj k →+* B, I k ≤ J.comap f →
          ∃! g : Fh.obj k →+* B,
            g.comp (η.app k).hom = f ∧ Ideal.map (η.app k).hom (I k) ≤ J.comap g)
    (c : Cocone F) (hc : IsColimit c)
    (ch : Cocone Fh) (hch : IsColimit ch) :
    let ηc : c.pt →+* ch.pt := (hc.desc (Cocone.mk ch.pt (η ≫ ch.ι))).hom
    let Ic : Ideal c.pt := ⨆ k, Ideal.map (c.ι.app k).hom (I k)
    Ideal.map ηc Ic =
        (⨆ k, (Ideal.map ((ch.ι.app k).hom.comp (η.app k).hom) (I k) : Ideal ch.pt)) ∧
      HenselianPair ch.pt (Ideal.map ηc Ic) ∧
      ∀ (B : Type w) (_ : CommRing B) (J : Ideal B),
        HenselianPair B J →
          ∀ f : c.pt →+* B, Ic ≤ J.comap f →
            ∃! g : ch.pt →+* B,
              g.comp ηc = f ∧ Ideal.map ηc Ic ≤ J.comap g
```

## Tag 0F0L, a lemma

[Tag 0F0L](https://stacks.math.columbia.edu/tag/0F0L) in the Stacks Project.

**`henselizations_equiv_of_zeroLocus_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean#L280).

> Henselization of a pair depends only on the radical of its ideal: two ideals with the same
> vanishing locus give canonically isomorphic henselizations over the base ring.

```lean
theorem henselizations_equiv_of_zeroLocus_eq
    (A : Type u) [CommRing A] (I J : Ideal A)
    (AI AJ : Type u) [CommRing AI] [CommRing AJ] [Algebra A AI] [Algebra A AJ]
    (hAI : HenselianPair AI (I.map (algebraMap A AI)))
    (hAJ : HenselianPair AJ (J.map (algebraMap A AJ)))
    (hI : ∀ (B : Type u) (_ : CommRing B) (K : Ideal B),
      HenselianPair B K →
        ∀ f : A →+* B, I ≤ K.comap f →
          ∃! g : AI →+* B,
            g.comp (algebraMap A AI) = f ∧ I.map (algebraMap A AI) ≤ K.comap g)
    (hJ : ∀ (B : Type u) (_ : CommRing B) (K : Ideal B),
      HenselianPair B K →
        ∀ f : A →+* B, J ≤ K.comap f →
          ∃! g : AJ →+* B,
            g.comp (algebraMap A AJ) = f ∧ J.map (algebraMap A AJ) ≤ K.comap g)
    (hIJ : PrimeSpectrum.zeroLocus (I : Set A) = PrimeSpectrum.zeroLocus (J : Set A)) :
    ∃! e : AI ≃+* AJ,
      e.toRingHom.comp (algebraMap A AI) = algebraMap A AJ
```

## Tag 0DYE, a lemma

[Tag 0DYE](https://stacks.math.columbia.edu/tag/0DYE) in the Stacks Project.

**`henselization_tensorProduct_bijective_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean#L326).

> Henselization commutes with integral base change. For an integral map of pairs
> `(A, I) → (B, J)` for which `J` and `IB` have the same vanishing locus, the canonical map
> `Aʰ ⊗[A] B → Bʰ` induced by the map of henselizations is an isomorphism.

```lean
theorem henselization_tensorProduct_bijective_of_isIntegral
    (A Ah : Type u) (B Bh : Type v) [CommRing A] [CommRing B] [CommRing Ah] [CommRing Bh]
    [Algebra A B] [Algebra A Ah] [Algebra B Bh] [Algebra A Bh] [IsScalarTower A B Bh]
    [Algebra.IsIntegral A B] (I : Ideal A) (J : Ideal B)
    (hmap : I ≤ J.comap (algebraMap A B))
    (hzero : PrimeSpectrum.zeroLocus (J : Set B) =
      PrimeSpectrum.zeroLocus (I.map (algebraMap A B) : Set B))
    (hAh : HenselianPair Ah (I.map (algebraMap A Ah)))
    (hBh : HenselianPair Bh (J.map (algebraMap B Bh)))
    (hAh_univ : ∀ (C : Type (max u v)) (_ : CommRing C) (K : Ideal C),
      HenselianPair C K →
        ∀ f : A →+* C, I ≤ K.comap f →
          ∃! g : Ah →+* C,
            g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ K.comap g)
    (hBh_univ : ∀ (C : Type (max u v)) (_ : CommRing C) (K : Ideal C),
      HenselianPair C K →
        ∀ f : B →+* C, J ≤ K.comap f →
          ∃! g : Bh →+* C,
            g.comp (algebraMap B Bh) = f ∧ J.map (algebraMap B Bh) ≤ K.comap g)
    (g : Ah →ₐ[A] Bh)
    (hg : I.map (algebraMap A Ah) ≤ (J.map (algebraMap B Bh)).comap g) :
    Function.Bijective
      (Algebra.TensorProduct.lift g (IsScalarTower.toAlgHom A B Bh)
        (fun _ _ ↦ Commute.all _ _))
```

## Tag 0H7Q, a lemma

[Tag 0H7Q](https://stacks.math.columbia.edu/tag/0H7Q) in the Stacks Project.

**`henselization_iInf_equiv_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean, line 539](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Pair/Henselization/Compatibilities.lean#L539).

> Let `(I i)` be a finite nonempty family of pairwise comaximal ideals of a commutative ring `A`.
> For arbitrary choices of a henselization `Aʰ` of `A` along `⨅ i, I i` and henselizations `Aʰᵢ`
> along each `I i`, the natural map from `Aʰ` to the product of the `Aʰᵢ` is an isomorphism. The
> displayed compatibility with the structure maps identifies this isomorphism canonically.

```lean
theorem henselization_iInf_equiv_pi {ι : Type} [Finite ι] [Nonempty ι]
    (A : Type u) [CommRing A] (I : ι → Ideal A)
    (hI : ∀ i j, i ≠ j → I i ⊔ I j = ⊤)
    (Ah : Type u) [CommRing Ah] (algebraMap_h : A →+* Ah)
    (hAh : HenselianPair Ah ((⨅ i, I i).map algebraMap_h) ∧
      ∀ (B : Type u) (_ : CommRing B) (J : Ideal B),
        HenselianPair B J →
          ∀ f : A →+* B, (⨅ i, I i) ≤ J.comap f →
            ∃! g : Ah →+* B,
              g.comp algebraMap_h = f ∧ (⨅ i, I i).map algebraMap_h ≤ J.comap g)
    (Ahi : ι → Type u) [∀ i, CommRing (Ahi i)] (algebraMap_i : ∀ i, A →+* Ahi i)
    (hAhi : ∀ i, HenselianPair (Ahi i) ((I i).map (algebraMap_i i)) ∧
      ∀ (B : Type u) (_ : CommRing B) (J : Ideal B),
        HenselianPair B J →
          ∀ f : A →+* B, I i ≤ J.comap f →
            ∃! g : Ahi i →+* B,
              g.comp (algebraMap_i i) = f ∧ (I i).map (algebraMap_i i) ≤ J.comap g) :
    ∃! e : Ah ≃+* (∀ i, Ahi i),
      ∀ (a : A) (i : ι), e (algebraMap_h a) i = algebraMap_i i a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.12, Tag 0EM7](https://stacks.math.columbia.edu/tag/0EM7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
