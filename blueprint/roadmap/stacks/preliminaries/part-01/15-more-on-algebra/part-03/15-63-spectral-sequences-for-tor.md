---
declaration: section
origin: cited
lean: CochainComplex.Tor.exists_spectral_sequences_tor_homology_and_terms, CochainComplex.Tor.ChangeOfRingsSpectralSequence.exists_tor_change_of_rings_spectral_sequence, RingTheory.TorBaseChange.exists_tor_base_change_spectral_sequence, CochainComplex.DerivedTensorSpectralSequence.exists_derived_tensor_spectral_sequences
statement: formalized
proof: formalized
---

# 15.63 Spectral sequences for Tor

Section 15.63 of the Stacks Project, [Tag 061Y](https://stacks.math.columbia.edu/tag/061Y). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 061Z, an example

[Tag 061Z](https://stacks.math.columbia.edu/tag/061Z) in the Stacks Project.

**`CochainComplex.Tor.exists_spectral_sequences_tor_homology_and_terms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Tor.lean, line 1258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/Tor.lean#L1258). References: EGA III (6.3.2), “Q• = module M, K bdd”; EGA III (7.6.4), “(i) spectral sequence”.

> Let `K` be a bounded-below chain complex of `R`-modules and let `M` be an `R`-module. There
> is a bounded-below free resolution `P` of `M`, and the two filtrations of `K ⊗[R] P` give
> spectral sequences abutting to its homology.
>
> The first has second page `Torⱼᴿ(Hᵢ(K), M)` and differential of bidegree `(1, -2)`. The second
> has first page `Torⱼᴿ(Kᵢ, M)`; under the displayed identifications, its first differential is
> the map on Tor induced by `Kᵢ ⟶ Kᵢ₋₁`.

```lean
public theorem exists_spectral_sequences_tor_homology_and_terms
    (R : Type u) [CommRing R]
    (K : CochainComplex (ModuleCat.{v} R) ℤ)
    (hK : ∃ a : ℤ, ∀ i : ℤ, a < i → IsZero (K.X i))
    (M : ModuleCat.{w} R) :
    let K' := ((ModuleCat.uliftFunctor.{max u w, v} R).mapHomologicalComplex
      (ComplexShape.up ℤ)).obj K
    let M' := (ModuleCat.uliftFunctor.{max u v, w} R).obj M
    ∃ (P : CochainComplex (ModuleCat.{max u v w} R) ℤ),
      ∃ (ε : P ⟶ (HomologicalComplex.single (ModuleCat.{max u v w} R)
        (ComplexShape.up ℤ) 0).obj M')
        (_ : QuasiIso ε),
      (∀ i : ℤ, Module.Free R (P.X i)) ∧
      (∀ i : ℤ, 0 < i → IsZero (P.X i)) ∧
      Nonempty (P.homology 0 ≅ M') ∧
      (∀ i : ℤ, i ≠ 0 → IsZero (P.homology i)) ∧
      ∃ (E : FirstTorSpectralSequence (ModuleCat.{max u v w} R))
        (E' : SecondTorSpectralSequence (ModuleCat.{max u v w} R))
        (_e₂ : ∀ i j : ℤ, (E.page 2).X (i, j) ≅ TorInDegree.{u, max v w} R j (K'.homology (-i)) M')
        (e₁ : ∀ i j : ℤ, (E'.page 1).X (i, j) ≅ TorInDegree.{u, max v w} R j (K'.X (-i)) M'),
        let T := HomologicalComplex.mapBifunctor K' P (moduleTensorBifunctor.{u, max v w} R)
          (ComplexShape.up ℤ)
        ∃ (F F' : HomologicalFiltration T)
          (S : TorFiltrationData E F false)
          (S' : TorFiltrationData E' F' true),
          F.step = tensorFiltrationSteps.{u, max v w} R K' P false ∧
          F'.step = tensorFiltrationSteps.{u, max v w} R K' P true ∧
          (∀ n, ∃ a b : ℤ, a ≤ b ∧ F.step a n = ⊥ ∧ F.step b n = ⊤) ∧
          (∀ n, ∃ a b : ℤ, a ≤ b ∧ F'.step a n = ⊥ ∧ F'.step b n = ⊤) ∧
          S.Converges ∧ S'.Converges ∧
          ∀ i j : ℤ,
            (e₁ i j).inv ≫ (E'.page 1).d (i, j) (i - 1, j) ≫ (e₁ (i - 1) j).hom =
              torInDegreeMap.{u, max v w} R j (K'.d (-i) (-(i - 1))) M'
```

## Tag 068F, an example

[Tag 068F](https://stacks.math.columbia.edu/tag/068F) in the Stacks Project.

**`CochainComplex.Tor.ChangeOfRingsSpectralSequence.exists_tor_change_of_rings_spectral_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/ChangeOfRingsSpectralSequence.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/ChangeOfRingsSpectralSequence.lean#L448). References: EGA III (6.9.3), “special case”; EGA III (6.9.3.2), “special case”; EGA III (6.9.3.3), “special case”; SGA 7 VIII (2.1), “special case”.

> **Stacks 068F.** Let `R → S` be a homomorphism of commutative rings, `M` an `R`-module and
> `N` an `S`-module. There is a free resolution `P^•` of `M` over `R` such that the homology of
> `P^• ⊗_R S`, with its natural `S`-module structure, computes `Tor_*^R(M, S)`, and there is a
> spectral sequence
> ```
> Tor_n^S(Tor_m^R(M, S), N) ⟹ Tor_{n+m}^R(M, N).
> ```
> The second-page identification is displayed, and the last clause records the abutment; the two
> `Nonempty` clauses before it record that the homology of the two base-changed complexes is
> `Tor_*^R(M, S)` and `Tor_*^R(M, N)` after restricting scalars along `R → S`.

```lean
public theorem exists_tor_change_of_rings_spectral_sequence
    (R S : Type u) [CommRing R] [CommRing S] (f : R →+* S)
    (M : ModuleCat.{max u v} R) (N : ModuleCat.{max u v} S) :
    ∃ (P : CochainComplex (ModuleCat.{max u v} R) ℤ),
      ∃ (ε : P ⟶ (HomologicalComplex.single (ModuleCat.{max u v} R)
        (ComplexShape.up ℤ) 0).obj M)
        (_ : QuasiIso ε),
      (∀ i : ℤ, Module.Free R (P.X i)) ∧
      (∀ i : ℤ, 0 < i → IsZero (P.X i)) ∧
      Nonempty (P.homology 0 ≅ M) ∧
      (∀ i : ℤ, i ≠ 0 → IsZero (P.homology i)) ∧
      (∀ i : ℤ, Nonempty
        ((ModuleCat.restrictScalars f).obj ((baseChangeComplex f P).homology (-i)) ≅
          TorInDegree.{u, v} R i M
            ((ModuleCat.restrictScalars f).obj (ModuleCat.of S (ULift.{v} S))))) ∧
      (∀ n : ℤ, Nonempty
        ((ModuleCat.restrictScalars f).obj
            ((baseChangeTensorComplex f P N).homology (-n)) ≅
          TorInDegree.{u, v} R n M ((ModuleCat.restrictScalars f).obj N))) ∧
      ∃ (E : FirstTorSpectralSequence (ModuleCat.{max u v} S))
        (_e₂ : ∀ i j : ℤ, (E.page 2).X (i, j) ≅
          TorInDegree.{u, v} S j ((baseChangeComplex f P).homology (-i)) N),
        HomologicalSpectralSequenceAbutsTo E
          (fun n ↦ (baseChangeTensorComplex f P N).homology (-n))
```

## Tag 0620, an example

[Tag 0620](https://stacks.math.columbia.edu/tag/0620) in the Stacks Project.

**`RingTheory.TorBaseChange.exists_tor_base_change_spectral_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/BaseChangeSpectralSequence.lean, line 714](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Tor/BaseChangeSpectralSequence.lean#L714). References: EGA III (6.9.8), “(6.9.8.1)”.

> If `A → B` and the `B`-modules `M` and `N` are flat over `A`, then for
> `B' = B ⊗[A] A'`, `M' = M ⊗[B] B'`, and `N' = N ⊗[B] B'`, there is a homological spectral sequence
> `Torᴬᵢ(Torᴮⱼ(M, N), A') ⇒ Torᴮʳᵢ₊ⱼ(M', N')`.
>
> Both sides are viewed as `A`-modules in order to state the spectral sequence in one abelian
> category.

```lean
public theorem exists_tor_base_change_spectral_sequence
    (A B A' : Type u) [CommRing A] [CommRing B] [CommRing A']
    [Algebra A B] [Algebra A A'] (M N : ModuleCat.{max u v} B)
    [Module.Flat A B]
    [Module.Flat A ((ModuleCat.restrictScalars (algebraMap A B)).obj M)]
    [Module.Flat A ((ModuleCat.restrictScalars (algebraMap A B)).obj N)] :
    ∃ (E : CochainComplex.Tor.FirstTorSpectralSequence (ModuleCat.{max u v} A))
      (_e₂ : ∀ i j : ℤ,
        (E.page 2).X (i, j) ≅
          @CochainComplex.Tor.TorInDegree.{u, v} A _ j
            (restrictScalars A B
              (@CochainComplex.Tor.TorInDegree.{u, v} B _ i M N))
            (restrictScalars A A' (@regularModule.{u, v} A' _))),
      CochainComplex.Tor.HomologicalSpectralSequenceAbutsTo E
        (fun n ↦
          (ModuleCat.restrictScalars
            (algebraMap A (BaseChangedAlgebra A B A'))).obj
            (@CochainComplex.Tor.TorInDegree.{u, v} (BaseChangedAlgebra A B A') _ n
              (@baseChange.{u, v} A B A' _ _ _ _ _ M)
              (@baseChange.{u, v} A B A' _ _ _ _ _ N)))
```

## Tag 0662, an example

[Tag 0662](https://stacks.math.columbia.edu/tag/0662) in the Stacks Project.

**`CochainComplex.DerivedTensorSpectralSequence.exists_derived_tensor_spectral_sequences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/DerivedTensor.lean, line 1317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/DerivedTensor.lean#L1317).

> **Stacks 0662.** For two bounded-above objects `K`, `L` of the derived category of a
> commutative ring `R` there are two convergent spectral sequences
> `'E_2^{p,q} = H^p(K ⊗^L H^q(L))` and `''E_2^{p,q} = H^p(H^q(K) ⊗^L L)`, both abutting to
> `H^{p+q}(K ⊗^L L)`.
>
> They are the spectral sequences of the two canonical filtrations of the total tensor complex
> `P^• ⊗ Q^•` of bounded-above complexes of projectives representing `K` and `L`; the abutment
> isomorphism is the one induced by those representatives and the canonical K-flat comparison of
> the derived tensor product, and the derived second-page isomorphisms factor through the
> filtered-complex second-page isomorphisms.

```lean
public theorem exists_derived_tensor_spectral_sequences
    (R : Type u) [CommRing R]
    (K L : DerivedCategory.Minus (ModuleCat.{u} R)) :
    ∃ (P Q : CochainComplex (ModuleCat.{u} R) ℤ) (bP bQ : ℤ),
      P.IsStrictlyLE bP ∧ (∀ i : ℤ, Projective (P.X i)) ∧
      Q.IsStrictlyLE bQ ∧ (∀ i : ℤ, Projective (Q.X i)) ∧
      ∃ (hPflat : P.KFlat) (hQflat : Q.KFlat)
        (eK : K.1 ≅ DerivedCategory.Q.obj P)
        (eL : L.1 ≅ DerivedCategory.Q.obj Q)
        (E : AssociatedFiltrationSpectralSequence ((tensorLeft P).obj Q)
            (firstDegreeFiltration P Q bP bQ))
        (E' : AssociatedFiltrationSpectralSequence ((tensorLeft P).obj Q)
            (secondDegreeFiltration P Q bP bQ))
        (firstFilteredE₂Iso : ∀ p q : ℤ,
          filteredPageObject ((tensorLeft P).obj Q) (firstDegreeFiltration P Q bP bQ)
              2 p q ≅
          ((tensorLeft P).obj ((single (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).obj
            (Q.homology q))).homology p)
        (secondFilteredE₂Iso : ∀ p q : ℤ,
          filteredPageObject ((tensorLeft P).obj Q) (secondDegreeFiltration P Q bP bQ)
              2 p q ≅
          ((tensorLeft ((single (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).obj
            (P.homology q))).obj Q).homology p)
        (firstE₂Iso : ∀ p q : ℤ, (E.spectralSequence.page 2).X (p, q) ≅
          ((tensorLeft P).obj ((single (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).obj
            (Q.homology q))).homology p)
        (secondE₂Iso : ∀ p q : ℤ, (E'.spectralSequence.page 2).X (p, q) ≅
          ((tensorLeft ((single (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).obj
            (P.homology q))).obj Q).homology p)
        (abutmentIso : ∀ n : ℤ, ((tensorLeft P).obj Q).homology n ≅
          (DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).obj
            (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj
              K.1).obj L.1))
        (firstOrdinaryToDerivedE₂Iso : ∀ p q : ℤ,
          ((tensorLeft P).obj ((single (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).obj
            (Q.homology q))).homology p ≅
          (DerivedCategory.homologyFunctor (ModuleCat.{u} R) p).obj
            (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K.1).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) q).obj L.1))))
        (secondOrdinaryToDerivedE₂Iso : ∀ p q : ℤ,
          ((tensorLeft ((single (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).obj
            (P.homology q))).obj Q).homology p ≅
          (DerivedCategory.homologyFunctor (ModuleCat.{u} R) p).obj
            (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) q).obj K.1))).obj L.1))
        (firstDerivedE₂Iso : ∀ p q : ℤ, (E.spectralSequence.page 2).X (p, q) ≅
          (DerivedCategory.homologyFunctor (ModuleCat.{u} R) p).obj
            (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj K.1).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) q).obj L.1))))
        (secondDerivedE₂Iso : ∀ p q : ℤ, (E'.spectralSequence.page 2).X (p, q) ≅
          (DerivedCategory.homologyFunctor (ModuleCat.{u} R) p).obj
            (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) q).obj K.1))).obj L.1)),
        (∀ p q : ℤ, (firstE₂Iso p q).hom =
          (E.pageIso 2 p q (by omega)).hom ≫ (firstFilteredE₂Iso p q).hom) ∧
        (∀ p q : ℤ, (secondE₂Iso p q).hom =
          (E'.pageIso 2 p q (by omega)).hom ≫ (secondFilteredE₂Iso p q).hom) ∧
        (∀ p q : ℤ, (firstDerivedE₂Iso p q).hom =
          (firstE₂Iso p q).hom ≫ (firstOrdinaryToDerivedE₂Iso p q).hom) ∧
        (∀ p q : ℤ, (secondDerivedE₂Iso p q).hom =
          (secondE₂Iso p q).hom ≫ (secondOrdinaryToDerivedE₂Iso p q).hom) ∧
        (∀ n : ℤ,
          (abutmentIso n).symm =
            (DerivedCategory.homologyFunctor (ModuleCat.{u} R) n).mapIso
              (((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor
                  R).mapIso eK).app L.1 ≪≫
                ((CochainComplex.DerivedTensor.canonicalDerivedTensorProductFunctor R).obj
                  (DerivedCategory.Q.obj P)).mapIso eL ≪≫
                (CochainComplex.DerivedTensor.canonicalDerivedTensorProduct R).comparison P Q
                  hPflat hQflat) ≪≫
              (DerivedCategory.homologyFunctorFactors (ModuleCat.{u} R) n).app
                ((tensorLeft P).obj Q))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.63, Tag 061Y](https://stacks.math.columbia.edu/tag/061Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
