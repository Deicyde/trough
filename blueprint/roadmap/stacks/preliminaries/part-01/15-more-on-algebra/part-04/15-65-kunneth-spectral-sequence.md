---
declaration: section
origin: cited
lean: CochainComplex.Kunneth.exists_kunneth_convolution_spectral_sequence, CochainComplex.KFlat.exists_free_kFlat_filtered_resolution, CochainComplex.Kunneth.exists_kunneth_filtered_complex, CochainComplex.Kunneth.exists_kunneth_spectral_sequence, CochainComplex.Kunneth.tor_isZero_and_exists_kunneth_shortExact
statement: formalized
proof: formalized
---

# 15.65 Künneth spectral sequence

Section 15.65 of the Stacks Project, [Tag 0H7V](https://stacks.math.columbia.edu/tag/0H7V). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H7W, a lemma

[Tag 0H7W](https://stacks.math.columbia.edu/tag/0H7W) in the Stacks Project.

**`CochainComplex.Kunneth.exists_kunneth_convolution_spectral_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Kunneth.lean, line 2171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/Kunneth.lean#L2171).

> For decreasingly filtered complexes `K` and `L` satisfying the flatness and K-flatness
> assumptions of the Künneth construction, there is a convolution-filtered tensor product `T` and an
> associated spectral sequence with the expected first page. If both filtrations are finite, or their
> steps are eventually acyclic and eventually quasi-isomorphic to the underlying complexes, then the
> first page has finite support in each total degree, the induced filtration on cohomology is finite,
> and the sequence converges with the canonical stable-page comparison.

```lean
public theorem exists_kunneth_convolution_spectral_sequence
    (R : Type u) [CommRing R]
    (K L : FilteredObject (CochainComplex (ModuleCat.{u} R) ℤ) ℤᵒᵖ)
    (hflatK :
      (∀ n : ℤ, Module.Flat R (K.X.X n)) ∧
      (∀ i n : ℤ, Module.Flat R ((K.filtration.obj (op i)).X n)) ∧
      (∀ i n : ℤ, Module.Flat R (((FilteredObject.gr i).obj K).X n)))
    (hflatL :
      (∀ n : ℤ, Module.Flat R (L.X.X n)) ∧
      (∀ i n : ℤ, Module.Flat R ((L.filtration.obj (op i)).X n)) ∧
      (∀ i n : ℤ, Module.Flat R (((FilteredObject.gr i).obj L).X n)))
    (hkflatK : K.X.KFlat ∧ (∀ i : ℤ, (K.filtration.obj (op i)).KFlat) ∧
      (∀ i : ℤ, ((FilteredObject.gr i).obj K).KFlat))
    (hkflatL : L.X.KFlat ∧ (∀ i : ℤ, (L.filtration.obj (op i)).KFlat) ∧
      (∀ i : ℤ, ((FilteredObject.gr i).obj L).KFlat)) :
    ∃ (T : FilteredObject (CochainComplex (ModuleCat.{u} R) ℤ) ℤᵒᵖ)
      (eT : K.X ⊗ L.X ≅ T.X),
      (∀ p n : ℤ, ∀ Q : Subobject (T.X.X n),
        Subobject.mk ((T.filtration.ι.app (op p)).f n) ≤ Q ↔
          ∀ ij : {ij : ℤ × ℤ // ij.1 + ij.2 = p},
            imageSubobject ((((K.filtration.ι.app (op ij.1.1)) ⊗ₘ
              (L.filtration.ι.app (op ij.1.2))) ≫ eT.hom).f n) ≤ Q) ∧
      ∃ (F : ∀ (_p n : ℤ), Subobject (T.X.X n))
        (Z : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
        (D : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
        (FH : ∀ (n _p : ℤ), Subobject (T.X.homology n))
        (E : CohomologicalSpectralSequence (ModuleCat.{u} R) 0)
        (hE : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))),
      (∀ p n : ℤ, F p n = Subobject.mk ((T.filtration.ι.app (op p)).f n)) ∧
      (∀ r p n : ℤ, Z r p n =
        F p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj (F (p + r) (n + 1))) ∧
      (∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
        (Subobject.«exists» (T.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1))) ∧
      (∀ n p : ℤ, FH n p =
        imageSubobject (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n)) ∧
      (∀ p q : ℤ, Nonempty ((E.page 1 (by omega)).X (p, q) ≅
        ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = p} ↦
          (((FilteredObject.gr ij.1.1).obj K) ⊗
            ((FilteredObject.gr ij.1.2).obj L)).homology (p + q))) ∧
      (((K.filtration.IsFinite ∧ L.filtration.IsFinite) ∨
          ∃ a b : ℤ, a < b ∧
            (∀ i : ℤ, b < i → (K.filtration.obj (op i)).Acyclic) ∧
            (∀ i : ℤ, i < a → QuasiIso (K.filtration.ι.app (op i))) ∧
            (∀ j : ℤ, b < j → (L.filtration.obj (op j)).Acyclic) ∧
            (∀ j : ℤ, j < a → QuasiIso (L.filtration.ι.app (op j)))) →
      (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 1 (by omega)).X (p, n - p))}.Finite) ∧
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
      (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
      (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
    (∀ p n : ℤ,
      IsGLB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj (F (p + r) (n + 1)) ⊔ F (p + 1) n)
        (kernelSubobject (T.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n) ∧
      IsLUB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.«exists» (T.X.d (n - 1) n)).obj (F (p - r) (n - 1)) ⊔
            F (p + 1) n)
        (imageSubobject (T.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n)) ∧
    (∀ p n : ℤ,
      let A := (Subobject.pullback (T.X.iCycles n)).obj (F p n)
      let N := kernelSubobject (T.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n
      let B := imageSubobject (T.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n
      ∃ (a : (A : ModuleCat.{u} R) ⟶ (N : ModuleCat.{u} R))
        (b : (A : ModuleCat.{u} R) ⟶
          image (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))
        (e : cokernel (Subobject.ofLE (B ⊓ N) N inf_le_right) ≅
          cokernel (image.preComp
            (HomologicalComplex.homologyMap (T.filtration.diagram.map
              (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
            (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))),
        A.arrow ≫ T.X.iCycles n = a ≫ N.arrow ∧
        A.arrow ≫ T.X.homologyπ n =
          b ≫ image.ι (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n) ∧
        a ≫ cokernel.π (Subobject.ofLE (B ⊓ N) N inf_le_right) ≫ e.hom =
          b ≫ cokernel.π (image.preComp
            (HomologicalComplex.homologyMap (T.filtration.diagram.map
              (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
            (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))))
```

## Tag 0H7X, a lemma

[Tag 0H7X](https://stacks.math.columbia.edu/tag/0H7X) in the Stacks Project.

**`CochainComplex.KFlat.exists_free_kFlat_filtered_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/FilteredResolution.lean, line 1383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/KFlat/FilteredResolution.lean#L1383).

> A filtered complex of modules admits a filtered morphism from a complex whose underlying
> terms, filtration steps, and associated graded pieces are free and K-flat, and this morphism is
> a quasi-isomorphism on the underlying complex, on every filtration step, and on every associated
> graded piece.

```lean
public theorem exists_free_kFlat_filtered_resolution
    (R : Type u) [CommRing R]
    (K : FilteredObject (CochainComplex (ModuleCat.{u} R) ℤ) ℤᵒᵖ) :
    ∃ (P : FilteredObject (CochainComplex (ModuleCat.{u} R) ℤ) ℤᵒᵖ) (f : P ⟶ K),
      (∀ n : ℤ, Module.Free R (P.X.X n)) ∧
      (∀ i n : ℤ, Module.Free R ((P.filtration.obj (op i)).X n)) ∧
      (∀ i n : ℤ,
        Module.Free R (((FilteredObject.gr i).obj P).X n)) ∧
      P.X.KFlat ∧
      (∀ i : ℤ, (P.filtration.obj (op i)).KFlat) ∧
      (∀ i : ℤ, ((FilteredObject.gr i).obj P).KFlat) ∧
      QuasiIso f.hom ∧
      (∀ i : ℤ, QuasiIso (f.natTrans.app (op i))) ∧
      (∀ i : ℤ, QuasiIso ((FilteredObject.gr i).map f))
```

## Tag 0H7Y, a proposition

[Tag 0H7Y](https://stacks.math.columbia.edu/tag/0H7Y) in the Stacks Project.

**`CochainComplex.Kunneth.exists_kunneth_filtered_complex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Kunneth.lean, line 2318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/Kunneth.lean#L2318).

> Two filtered complexes of modules have a filtered K-flat tensor representative whose
> associated spectral sequence has the expected Künneth first page. If the filtration steps of both
> complexes are eventually acyclic and eventually quasi-isomorphic to the underlying complexes,
> then the first page is bounded in every total degree, the induced filtration on cohomology is
> finite, and the spectral sequence converges canonically to the cohomology of the derived tensor
> product.

```lean
public theorem exists_kunneth_filtered_complex
    (R : Type u) [CommRing R]
    (K L : FilteredObject (CochainComplex (ModuleCat.{u} R) ℤ) ℤᵒᵖ) :
    ∃ (P Q : FilteredObject (CochainComplex (ModuleCat.{u} R) ℤ) ℤᵒᵖ)
      (f : P ⟶ K) (g : Q ⟶ L)
      (T : FilteredObject (CochainComplex (ModuleCat.{u} R) ℤ) ℤᵒᵖ)
      (eT : P.X ⊗ Q.X ≅ T.X),
      ((∀ n : ℤ, Module.Flat R (P.X.X n)) ∧
        (∀ i n : ℤ, Module.Flat R ((P.filtration.obj (op i)).X n)) ∧
        (∀ i n : ℤ, Module.Flat R (((FilteredObject.gr i).obj P).X n)) ∧
        P.X.KFlat ∧
        (∀ i : ℤ, (P.filtration.obj (op i)).KFlat) ∧
        (∀ i : ℤ, ((FilteredObject.gr i).obj P).KFlat) ∧
        QuasiIso f.hom ∧
        (∀ i : ℤ, QuasiIso (f.natTrans.app (op i))) ∧
        (∀ i : ℤ, QuasiIso ((FilteredObject.gr i).map f))) ∧
      ((∀ n : ℤ, Module.Flat R (Q.X.X n)) ∧
        (∀ i n : ℤ, Module.Flat R ((Q.filtration.obj (op i)).X n)) ∧
        (∀ i n : ℤ, Module.Flat R (((FilteredObject.gr i).obj Q).X n)) ∧
        Q.X.KFlat ∧
        (∀ i : ℤ, (Q.filtration.obj (op i)).KFlat) ∧
        (∀ i : ℤ, ((FilteredObject.gr i).obj Q).KFlat) ∧
        QuasiIso g.hom ∧
        (∀ i : ℤ, QuasiIso (g.natTrans.app (op i))) ∧
        (∀ i : ℤ, QuasiIso ((FilteredObject.gr i).map g))) ∧
      (∀ p n : ℤ, ∀ U : Subobject (T.X.X n),
        Subobject.mk ((T.filtration.ι.app (op p)).f n) ≤ U ↔
          ∀ ij : {ij : ℤ × ℤ // ij.1 + ij.2 = p},
            imageSubobject ((((P.filtration.ι.app (op ij.1.1)) ⊗ₘ
              (Q.filtration.ι.app (op ij.1.2))) ≫ eT.hom).f n) ≤ U) ∧
      ∃ (F : ∀ (_p n : ℤ), Subobject (T.X.X n))
        (Z : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
        (D : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
        (FH : ∀ (n _p : ℤ), Subobject (T.X.homology n))
        (E : CohomologicalSpectralSequence (ModuleCat.{u} R) 0)
        (hE : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _
            (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))),
        (∀ p n : ℤ, F p n = Subobject.mk ((T.filtration.ι.app (op p)).f n)) ∧
        (∀ r p n : ℤ, Z r p n =
          F p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj (F (p + r) (n + 1))) ∧
        (∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
          (Subobject.«exists» (T.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1))) ∧
        (∀ n p : ℤ, FH n p =
          imageSubobject (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n)) ∧
        (∀ p q : ℤ, Nonempty ((E.page 1 (by omega)).X (p, q) ≅
          ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = p} ↦
            (((FilteredObject.gr ij.1.1).obj P) ⊗
              ((FilteredObject.gr ij.1.2).obj Q)).homology (p + q))) ∧
        (((∃ b : ℤ, ∀ i : ℤ, b < i → (K.filtration.obj (op i)).Acyclic) ∧
          (∃ a : ℤ, ∀ i : ℤ, i < a → QuasiIso (K.filtration.ι.app (op i))) ∧
          (∃ b : ℤ, ∀ j : ℤ, b < j → (L.filtration.obj (op j)).Acyclic) ∧
          (∃ a : ℤ, ∀ j : ℤ, j < a → QuasiIso (L.filtration.ι.app (op j)))) →
          (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 1 (by omega)).X (p, n - p))}.Finite) ∧
          (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
          (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
            (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
          (∀ p n : ℤ,
            IsGLB (Set.range fun r : ℕ ↦
                F p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj
                  (F (p + r) (n + 1)) ⊔ F (p + 1) n)
              (kernelSubobject (T.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n) ∧
            IsLUB (Set.range fun r : ℕ ↦
                F p n ⊓ (Subobject.«exists» (T.X.d (n - 1) n)).obj
                  (F (p - r) (n - 1)) ⊔ F (p + 1) n)
              (imageSubobject (T.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n)) ∧
          (∀ p n : ℤ,
            let A := (Subobject.pullback (T.X.iCycles n)).obj (F p n)
            let N := kernelSubobject (T.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n
            let B := imageSubobject (T.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n
            ∃ (a : (A : ModuleCat.{u} R) ⟶ (N : ModuleCat.{u} R))
              (b : (A : ModuleCat.{u} R) ⟶
                image (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))
              (e : cokernel (Subobject.ofLE (B ⊓ N) N inf_le_right) ≅
                cokernel (image.preComp
                  (HomologicalComplex.homologyMap (T.filtration.diagram.map
                    (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
                  (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))),
              A.arrow ≫ T.X.iCycles n = a ≫ N.arrow ∧
              A.arrow ≫ T.X.homologyπ n =
                b ≫ image.ι (HomologicalComplex.homologyMap
                  (T.filtration.ι.app (op p)) n) ∧
              a ≫ cokernel.π (Subobject.ofLE (B ⊓ N) N inf_le_right) ≫ e.hom =
                b ≫ cokernel.π (image.preComp
                  (HomologicalComplex.homologyMap (T.filtration.diagram.map
                    (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
                  (HomologicalComplex.homologyMap
                    (T.filtration.ι.app (op p)) n))))
```

## Tag 0H7Z, a lemma

[Tag 0H7Z](https://stacks.math.columbia.edu/tag/0H7Z) in the Stacks Project.

**`CochainComplex.Kunneth.exists_kunneth_spectral_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/KunnethTor.lean, line 989](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/KunnethTor.lean#L989). References: EGA III (6.3.2), “(6.3.2.2)”; EGA III (6.5.4), “(6.5.4.2)”; EGA III (6.8.2), “m=2, modules over a ring”.

> **Künneth spectral sequence.** For bounded complexes `K` and `L` of modules over a
> commutative ring, there is a bounded cohomological spectral sequence with
> `E₂^(p,q) = ⊕_(i+j=q) Tor_(-p)(H^i(K), H^j(L))`, converging to the cohomology in degree
> `p + q` of the derived tensor product. The derived tensor product is represented here by the
> tensor product of K-flat replacements of `K` and `L`.

```lean
public theorem exists_kunneth_spectral_sequence
    (R : Type u) [CommRing R]
    (K : CochainComplex (ModuleCat.{v} R) ℤ)
    (L : CochainComplex (ModuleCat.{w} R) ℤ)
    (aK bK aL bL : ℤ) [K.IsGE aK] [K.IsLE bK] [L.IsGE aL] [L.IsLE bL] :
    let S := ULift.{max v w} R
    let U : ModuleCat.{v} R ⥤ ModuleCat.{max u v w} S :=
      ModuleCat.uliftFunctor.{max u w} R ⋙ ModuleCat.restrictScalars ULift.ringEquiv.toRingHom
    let V : ModuleCat.{w} R ⥤ ModuleCat.{max u v w} S :=
      ModuleCat.uliftFunctor.{max u v} R ⋙ ModuleCat.restrictScalars ULift.ringEquiv.toRingHom
    let K' := (U.mapHomologicalComplex (ComplexShape.up ℤ)).obj K
    let L' := (V.mapHomologicalComplex (ComplexShape.up ℤ)).obj L
    ∃ (P Q : CochainComplex (ModuleCat S) ℤ) (f : P ⟶ K') (g : Q ⟶ L')
      (_ : QuasiIso f) (_ : QuasiIso g) (_ : P.KFlat) (_ : Q.KFlat)
      (T : FilteredObject (CochainComplex (ModuleCat S) ℤ) ℤᵒᵖ)
      (eT : P ⊗ Q ≅ T.X)
      (E : E₂CohomologicalSpectralSequence (ModuleCat S))
      (F : ∀ (_p n : ℤ), Subobject (T.X.X n))
      (Z : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
      (D : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
      (FH : ∀ (_n _p : ℤ), Subobject (T.X.homology _n))
      (hE : ∀ (r p q : ℤ) (hr : 2 ≤ r), (E.page r hr).X (p, q) ≅
        cokernel (Subobject.ofLE _ _
          (inf_le_right : D (r - 1) (-q) (p + q) ⊓ Z (r - 1) (-q) (p + q) ≤
            Z (r - 1) (-q) (p + q)))),
      (∀ p n : ℤ, F p n = Subobject.mk ((T.filtration.ι.app (op p)).f n)) ∧
      (∀ r p n : ℤ, Z r p n =
        F p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj (F (p + r) (n + 1))) ∧
      (∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
        (Subobject.«exists» (T.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1))) ∧
      (∀ n p : ℤ, FH n p =
        imageSubobject (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n)) ∧
      (∀ p q : ℤ, p ≤ 0 →
        Nonempty ((E.page 2).X (p, q) ≅
          ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = q} ↦
            ((Tor' (ModuleCat S) (-p).toNat).obj (K'.homology ij.1.1)).obj
              (L'.homology ij.1.2))) ∧
      (∀ p q : ℤ, 0 < p → IsZero ((E.page 2).X (p, q))) ∧
      (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 2).X (p, n - p))}.Finite) ∧
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
      (∀ p q : ℤ, ∃ (r₀ : ℤ) (hr₀ : 2 ≤ r₀), ∀ (r : ℤ) (hr : r₀ ≤ r),
        let n := p + q
        let i := -q
        let N := kernelSubobject (T.X.d n (n + 1)) ⊓ F i n ⊔ F (i + 1) n
        let B := imageSubobject (T.X.d (n - 1) n) ⊓ F i n ⊔ F (i + 1) n
        (E.page r (by omega)).d (p, q) (p + r, q - r + 1) = 0 ∧
          Z (r - 1) i n ⊔ F (i + 1) n = N ∧
          (D (r - 1) i n ⊓ Z (r - 1) i n) ⊔ F (i + 1) n = B ⊓ N) ∧
      (∀ p n : ℤ,
        let A := (Subobject.pullback (T.X.iCycles n)).obj (F p n)
        let N := kernelSubobject (T.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n
        let B := imageSubobject (T.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n
        ∃ (a : (A : ModuleCat S) ⟶ (N : ModuleCat S))
          (b : (A : ModuleCat S) ⟶
            image (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))
          (e : cokernel (Subobject.ofLE (B ⊓ N) N inf_le_right) ≅
            cokernel (image.preComp
              (HomologicalComplex.homologyMap (T.filtration.diagram.map
                (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
              (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))),
          A.arrow ≫ T.X.iCycles n = a ≫ N.arrow ∧
          A.arrow ≫ T.X.homologyπ n =
            b ≫ image.ι (HomologicalComplex.homologyMap
              (T.filtration.ι.app (op p)) n) ∧
          a ≫ cokernel.π (Subobject.ofLE (B ⊓ N) N inf_le_right) ≫ e.hom =
            b ≫ cokernel.π (image.preComp
              (HomologicalComplex.homologyMap (T.filtration.diagram.map
                (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
              (HomologicalComplex.homologyMap
                (T.filtration.ι.app (op p)) n)))
```

## Tag 0H80, an example

[Tag 0H80](https://stacks.math.columbia.edu/tag/0H80) in the Stacks Project.

**`CochainComplex.Kunneth.tor_isZero_and_exists_kunneth_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/KunnethTor.lean, line 1327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/SpectralSequence/KunnethTor.lean#L1327). References: EGA III (7.6.4), “(i) short exact sequence”.

> **Künneth short exact sequence over a Dedekind domain.** Higher Tor modules vanish over a
> Dedekind domain. Thus the bounded Künneth spectral sequence degenerates at `E₂`, and its edge
> maps exhibit the cohomology of a derived tensor product as an extension of the direct sum of
> tensor products in total degree `n` by the direct sum of first Tor modules in total degree
> `n + 1`.

```lean
public theorem tor_isZero_and_exists_kunneth_shortExact
    (R : Type u) [CommRing R] [IsDedekindDomain R] :
    let S := ULift.{max v w} R
    let U : ModuleCat.{v} R ⥤ ModuleCat.{max u v w} S :=
      ModuleCat.uliftFunctor.{max u w} R ⋙ ModuleCat.restrictScalars ULift.ringEquiv.toRingHom
    let V : ModuleCat.{w} R ⥤ ModuleCat.{max u v w} S :=
      ModuleCat.uliftFunctor.{max u v} R ⋙ ModuleCat.restrictScalars ULift.ringEquiv.toRingHom
    (∀ (M : ModuleCat.{v} R) (N : ModuleCat.{w} R) (i : ℕ), i ≠ 0 → i ≠ 1 →
      IsZero (((Tor' (ModuleCat S) i).obj (U.obj M)).obj (V.obj N))) ∧
    ∀ (K : CochainComplex (ModuleCat.{v} R) ℤ) (L : CochainComplex (ModuleCat.{w} R) ℤ)
      (aK bK aL bL : ℤ) [K.IsGE aK] [K.IsLE bK] [L.IsGE aL] [L.IsLE bL],
      let K' := (U.mapHomologicalComplex (ComplexShape.up ℤ)).obj K
      let L' := (V.mapHomologicalComplex (ComplexShape.up ℤ)).obj L
      ∃ (P Q : CochainComplex (ModuleCat S) ℤ) (f : P ⟶ K') (g : Q ⟶ L')
        (_ : QuasiIso f) (_ : QuasiIso g) (_ : P.KFlat) (_ : Q.KFlat)
        (T : FilteredObject (CochainComplex (ModuleCat S) ℤ) ℤᵒᵖ)
        (eT : P ⊗ Q ≅ T.X)
        (E : E₂CohomologicalSpectralSequence (ModuleCat S))
        (F : ∀ (_p n : ℤ), Subobject (T.X.X n))
        (Z : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
        (D : ∀ (_r _p n : ℤ), Subobject (T.X.X n))
        (FH : ∀ (_n _p : ℤ), Subobject (T.X.homology _n))
        (_hE : ∀ (r p q : ℤ) (hr : 2 ≤ r), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _
            (inf_le_right : D (r - 1) (-q) (p + q) ⊓ Z (r - 1) (-q) (p + q) ≤
              Z (r - 1) (-q) (p + q))))
        (e₂ : ∀ (p q : ℤ) (_hp : p ≤ 0), (E.page 2).X (p, q) ≅
          ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = q} ↦
            ((Tor' (ModuleCat S) (-p).toNat).obj (K'.homology ij.1.1)).obj
              (L'.homology ij.1.2)),
        (∀ p n : ℤ, F p n = Subobject.mk ((T.filtration.ι.app (op p)).f n)) ∧
        (∀ r p n : ℤ, Z r p n =
          F p n ⊓ (Subobject.pullback (T.X.d n (n + 1))).obj (F (p + r) (n + 1))) ∧
        (∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
          (Subobject.«exists» (T.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1))) ∧
        (∀ n p : ℤ, FH n p =
          imageSubobject (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n)) ∧
        (∀ p q : ℤ, 0 < p → IsZero ((E.page 2).X (p, q))) ∧
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 2).X (p, n - p))}.Finite) ∧
        (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
        (∀ p q : ℤ, ∃ (r₀ : ℤ) (hr₀ : 2 ≤ r₀), ∀ (r : ℤ) (hr : r₀ ≤ r),
          let n := p + q
          let i := -q
          let N := kernelSubobject (T.X.d n (n + 1)) ⊓ F i n ⊔ F (i + 1) n
          let B := imageSubobject (T.X.d (n - 1) n) ⊓ F i n ⊔ F (i + 1) n
          (E.page r (by omega)).d (p, q) (p + r, q - r + 1) = 0 ∧
            Z (r - 1) i n ⊔ F (i + 1) n = N ∧
            (D (r - 1) i n ⊓ Z (r - 1) i n) ⊔ F (i + 1) n = B ⊓ N) ∧
        (∀ p n : ℤ,
          let A := (Subobject.pullback (T.X.iCycles n)).obj (F p n)
          let N := kernelSubobject (T.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n
          let B := imageSubobject (T.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n
          ∃ (a : (A : ModuleCat S) ⟶ (N : ModuleCat S))
            (b : (A : ModuleCat S) ⟶
              image (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))
            (e : cokernel (Subobject.ofLE (B ⊓ N) N inf_le_right) ≅
              cokernel (image.preComp
                (HomologicalComplex.homologyMap (T.filtration.diagram.map
                  (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
                (HomologicalComplex.homologyMap (T.filtration.ι.app (op p)) n))),
            (A.arrow ≫ T.X.iCycles n = a ≫ N.arrow ∧
            A.arrow ≫ T.X.homologyπ n =
              b ≫ image.ι (HomologicalComplex.homologyMap
                (T.filtration.ι.app (op p)) n) ∧
            a ≫ cokernel.π (Subobject.ofLE (B ⊓ N) N inf_le_right) ≫ e.hom =
              b ≫ cokernel.π (image.preComp
                (HomologicalComplex.homologyMap (T.filtration.diagram.map
                  (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
                (HomologicalComplex.homologyMap
                  (T.filtration.ι.app (op p)) n)))) ∧
        (∀ (r p q : ℤ) (hr : 2 ≤ r),
          (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
        ∀ n : ℤ,
          FH n (-n - 1) = ⊤ ∧ FH n (-n + 1) = ⊥ ∧
          ∃ (torZeroTensor :
              (∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n} ↦
                ((Tor' (ModuleCat S) (-0 : ℤ).toNat).obj
                  (K'.homology ij.1.1)).obj (L'.homology ij.1.2)) ≅
              ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n} ↦
                K'.homology ij.1.1 ⊗ L'.homology ij.1.2)
            (torOne :
              (∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n + 1} ↦
                ((Tor' (ModuleCat S) (-(-1 : ℤ)).toNat).obj
                  (K'.homology ij.1.1)).obj (L'.homology ij.1.2)) ≅
              ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n + 1} ↦
                ((Tor' (ModuleCat S) 1).obj (K'.homology ij.1.1)).obj
                  (L'.homology ij.1.2))
            (eTensor : (E.page 2).X (0, n) ≅
              ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n} ↦
                K'.homology ij.1.1 ⊗ L'.homology ij.1.2)
            (eTor : (E.page 2).X (-1, n + 1) ≅
              ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n + 1} ↦
                ((Tor' (ModuleCat S) 1).obj (K'.homology ij.1.1)).obj
                  (L'.homology ij.1.2))
            (e₀ : (E.page 2).X (0, n) ≅ (FH n (-n) : ModuleCat S))
            (e₁ : (E.page 2).X (-1, n + 1) ≅ cokernel (FH n (-n)).arrow)
            (ι : (∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n} ↦
                K'.homology ij.1.1 ⊗ L'.homology ij.1.2) ⟶ (P ⊗ Q).homology n)
            (π : (P ⊗ Q).homology n ⟶
              ∐ fun ij : {ij : ℤ × ℤ // ij.1 + ij.2 = n + 1} ↦
                ((Tor' (ModuleCat S) 1).obj (K'.homology ij.1.1)).obj
                  (L'.homology ij.1.2))
            (h : ι ≫ π = 0),
            eTensor = (e₂ 0 n (by omega)).trans torZeroTensor ∧
            eTor = (e₂ (-1) (n + 1) (by omega)).trans torOne ∧
            ι = eTensor.inv ≫ e₀.hom ≫ (FH n (-n)).arrow ≫
                HomologicalComplex.homologyMap eT.inv n ∧
            π = HomologicalComplex.homologyMap eT.hom n ≫
                cokernel.π (FH n (-n)).arrow ≫ e₁.inv ≫ eTor.hom ∧
            (ShortComplex.mk ι π h).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.65, Tag 0H7V](https://stacks.math.columbia.edu/tag/0H7V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
