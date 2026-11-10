---
declaration: section
origin: cited
lean: CochainComplex.Filtered, CochainComplex.ImageSystem.filtered, CochainComplex.exists_cohomologicalSpectralSequence, CochainComplex.Filtered.exists_iso_firstPage_homology_d_eq_δ, CochainComplex.Filtered.d_gr_eq_zero_and_exists_iso_firstPage_d_eq, FilteredComplexSpectralSequence.spectralSequenceMap, CochainComplex.Filtered.inducedFilteredObject, CochainComplex.Filtered.inducedFiltration
statement: formalized
proof: formalized
---

# 12.24 Spectral sequences: filtered complexes

Section 12.24 of the Stacks Project, [Tag 012K](https://stacks.math.columbia.edu/tag/012K). 15 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 012L, a definition

[Tag 012L](https://stacks.math.columbia.edu/tag/012L) in the Stacks Project.

**`CochainComplex.Filtered`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Defs.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Defs.lean#L49). The attribute's comment: “as a complex filtered by subcomplexes, the same datum as a complex of `Fil(𝒜)`”. References: EGA 0 (11.2.2).

> A filtered complex of `C`: a cochain complex `K^•` together with a decreasing filtration
> `F^pK^•` of it by subcomplexes, i.e. a filtered object of `CochainComplex C ℤ` indexed by `ℤᵒᵖ`.

```lean
abbrev Filtered (C : Type u) [Category.{v} C] [HasZeroMorphisms C] : Type _
```

**`CochainComplex.ImageSystem.filtered`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/ImageFiltration.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/ImageFiltration.lean#L130). The attribute's comment: “a complex filtered by the images of a system of complexes mapping into it”.

> **The filtration of `X^•` by the images of a system**, as a filtered complex in the sense of
> [Stacks, Tag 012L].

```lean
public def filtered : CochainComplex.Filtered C
```

## Tag 012M, a lemma

[Tag 012M](https://stacks.math.columbia.edu/tag/012M) in the Stacks Project.

**`CochainComplex.exists_cohomologicalSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/Convergence.lean, line 775](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/Convergence.lean#L775).

> **The spectral sequence of a filtered complex.**  For a filtered complex `(K^•, F)` of an
> abelian category, with `Z_r^{p, q} = F^p K^n ⊓ (d^n)⁻¹(F^{p + r}K^{n + 1})` and
> `D_r^{p, q} = Z_{r - 1}^{p + 1, q - 1} ⊔ d^{n - 1}(Z_{r - 1}^{p - r + 1, q + r - 2})` as
> subobjects of `K^n`, the quotients `E_r^{p, q} = Z_r^{p, q} / (D_r^{p, q} ⊓ Z_r^{p, q})` are the
> pages of a cohomological spectral sequence whose differential is induced by `d`, whose zeroth
> page is `gr^p K^•`, and whose first page is therefore `H^n(gr^p K^•)`.

```lean
public theorem exists_cohomologicalSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A]
    (K : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
    (F : ∀ (_p n : ℤ), Subobject (K.X.X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hZ : ∀ r p n : ℤ, Z r p n =
      F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» (K.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1))) :
    ∃ (E : CohomologicalSpectralSequence A 0)
      (e : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
        cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)))
      (α : ∀ (p q n : ℤ), n = p + q → ((E.page 0 le_rfl).X (p, q) ≅
        ((FilteredObject.gr p).obj K).X n)),
      (∀ (r p q n : ℤ) (hr : 0 ≤ r) (hn : n = p + q),
        ∃ δ : (Z r p n : A) ⟶ (Z r (p + r) (n + 1) : A),
          δ ≫ (Z r (p + r) (n + 1)).arrow = (Z r p n).arrow ≫ K.X.d n (n + 1) ∧
          cokernel.π (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)) ≫
              (e r p q n hr hn).inv ≫ (E.page r hr).d (p, q) (p + r, q - r + 1) =
            δ ≫ cokernel.π (Subobject.ofLE _ _ (inf_le_right :
                D r (p + r) (n + 1) ⊓ Z r (p + r) (n + 1) ≤ Z r (p + r) (n + 1))) ≫
              (e r (p + r) (q - r + 1) (n + 1) hr (by omega)).inv) ∧
      (∀ (p q n : ℤ) (hn : n = p + q) (u : (Z 0 p n : A) ⟶ (K.filtration.obj (op p)).X n),
        u ≫ (K.filtration.ι.app (op p)).f n = (Z 0 p n).arrow →
        cokernel.π (Subobject.ofLE _ _ (inf_le_right : D 0 p n ⊓ Z 0 p n ≤ Z 0 p n)) ≫
            (e 0 p q n le_rfl hn).inv ≫ (α p q n hn).hom =
          u ≫ (FilteredObject.grMapπ (FilteredObject.succHom p) K).f n) ∧
      (∀ (p q n : ℤ) (hn : n = p + q),
        (E.page 0 le_rfl).d (p, q) (p, q + 1) ≫ (α p (q + 1) (n + 1) (by omega)).hom =
          (α p q n hn).hom ≫
            ((FilteredObject.gr p).obj K).d n (n + 1)) ∧
      (∀ p q n : ℤ, n = p + q → Nonempty ((E.page 1).X (p, q) ≅
        ((FilteredObject.gr p).obj K).homology n))
```

## Tag 012N, a lemma

[Tag 012N](https://stacks.math.columbia.edu/tag/012N) in the Stacks Project.

**`CochainComplex.Filtered.exists_iso_firstPage_homology_d_eq_δ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean#L750). The attribute's comment: “(1)”.

> **Stacks 012N (1).** Let `E` be the spectral sequence of the filtered complex `K`, presented
> on its first page as in [Stacks, Tag 012M]: `E_1^{p, q} = Z_1^{p, q}/(D_1^{p, q} ∩ Z_1^{p, q})`,
> with `d_1` induced by `d`. Then `E_1^{p, q} = H^{p + q}(gr^pK^•)`, the class of
> `x ∈ Z_1^{p, q} ⊆ F^pK^{p + q}` going to the class of its image in `gr^pK^{p + q}`, and under
> these identifications `d_1^{p, q}` is the boundary map in cohomology of the short exact sequence
> of complexes `0 → gr^{p + 1}K^• → F^pK^•/F^{p + 2}K^• → gr^pK^• → 0`.

```lean
theorem exists_iso_firstPage_homology_d_eq_δ :
    ∃ ε : ∀ (p q n : ℤ) (_ : n = p + q),
        (E.page 1).X (p, q) ≅ ((gr p).obj K).homology n,
      (∀ (p q n : ℤ) (hn : n = p + q)
          (u : (cycles K.X K.step 1 p n : C) ⟶ (K.filtration.obj (op p)).X n)
          (_ : u ≫ (K.filtration.ι.app (op p)).f n = (cycles K.X K.step 1 p n).arrow)
          (hc : (u ≫ (grMapπ (succHom p) K).f n) ≫ ((gr p).obj K).d n (n + 1) = 0),
        cokernel.π (Subobject.ofLE _ _ (inf_le_right : boundaries K.X K.step 1 p n ⊓
            cycles K.X K.step 1 p n ≤ cycles K.X K.step 1 p n)) ≫
            (e p q n hn).inv ≫ (ε p q n hn).hom =
          ((gr p).obj K).liftCycles (u ≫ (grMapπ (succHom p) K).f n) (n + 1) (by simp) hc ≫
            ((gr p).obj K).homologyπ n) ∧
      ∀ (p q n : ℤ) (hn : n = p + q),
        (E.page 1).d (p, q) (p + 1, q) ≫ (ε (p + 1) q (n + 1) (by omega)).hom =
          (ε p q n hn).hom ≫
            (grMapCompShortComplex_shortExact (succHom (p + 1)) (succHom p) K).δ n (n + 1)
              (by simp)
```

**`CochainComplex.Filtered.d_gr_eq_zero_and_exists_iso_firstPage_d_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean, line 802](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean#L802). The attribute's comment: “(2)”.

> **Stacks 012N (2).** If `d(F^pK) ⊆ F^{p + 1}K` for all `p`, then `d` induces the zero
> differential on every `gr^pK^•`, so that `E_1^{p, q} = gr^pK^{p + q}`, the class of
> `x ∈ Z_1^{p, q} = F^pK^{p + q}` going to its image; and under these identifications `d_1^{p, q}`
> is the morphism `gr^pK^{p + q} → gr^{p + 1}K^{p + q + 1}` induced by `d`.

```lean
theorem d_gr_eq_zero_and_exists_iso_firstPage_d_eq
    (hd : ∀ p n : ℤ, (K.step (p + 1) (n + 1)).Factors ((K.step p n).arrow ≫ K.X.d n (n + 1))) :
    (∀ p i j : ℤ, ((gr p).obj K).d i j = 0) ∧
    ∃ ε : ∀ (p q n : ℤ) (_ : n = p + q), (E.page 1).X (p, q) ≅ ((gr p).obj K).X n,
      (∀ (p q n : ℤ) (hn : n = p + q)
          (u : (cycles K.X K.step 1 p n : C) ⟶ (K.filtration.obj (op p)).X n)
          (_ : u ≫ (K.filtration.ι.app (op p)).f n = (cycles K.X K.step 1 p n).arrow),
        cokernel.π (Subobject.ofLE _ _ (inf_le_right : boundaries K.X K.step 1 p n ⊓
            cycles K.X K.step 1 p n ≤ cycles K.X K.step 1 p n)) ≫
            (e p q n hn).inv ≫ (ε p q n hn).hom =
          u ≫ (grMapπ (succHom p) K).f n) ∧
      ∀ (p q n : ℤ) (hn : n = p + q), ∃ μ : ((gr p).obj K).X n ⟶ ((gr (p + 1)).obj K).X (n + 1),
        (∀ (v : (K.filtration.obj (op p)).X n ⟶ (K.filtration.obj (op (p + 1))).X (n + 1)),
          v ≫ (K.filtration.ι.app (op (p + 1))).f (n + 1) =
              (K.filtration.ι.app (op p)).f n ≫ K.X.d n (n + 1) →
            (grMapπ (succHom p) K).f n ≫ μ = v ≫ (grMapπ (succHom (p + 1)) K).f (n + 1)) ∧
        (E.page 1).d (p, q) (p + 1, q) ≫ (ε (p + 1) q (n + 1) (by omega)).hom =
          (ε p q n hn).hom ≫ μ
```

## Tag 012O, a lemma

[Tag 012O](https://stacks.math.columbia.edu/tag/012O) in the Stacks Project.

**`FilteredComplexSpectralSequence.spectralSequenceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Functoriality.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Functoriality.lean#L204). References: EGA 0 (11.2.3), “existence of E(u)”; EGA 0 (11.2.2), “functoriality”.

> A morphism `φ : K ⟶ L` of filtered complexes, i.e. carrying each `F^p K^n` into `F^p L^n`,
> induces a morphism of spectral sequences `E_r(K) ⟶ E_r(L)`: on the `r`-th pages it is the map
> `Z_r^{p,q}(K)/D_r^{p,q}(K) ⟶ Z_r^{p,q}(L)/D_r^{p,q}(L)` induced by `φ`, and these maps commute
> with the differentials `d_r` and the identifications `H(E_r) = E_{r+1}`.

```lean
noncomputable def spectralSequenceMap :
    spectralSequence K FK hantiK ⟶ spectralSequence L FL hantiL
```

## Tag 012P, a definition

[Tag 012P](https://stacks.math.columbia.edu/tag/012P) in the Stacks Project.

**`CochainComplex.Filtered.inducedFilteredObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Convergence.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Convergence.lean#L271). The attribute's comment: “the induced filtration of `H^n(K^•)`, bundled as an object of `Fil(𝒜)`”. References: EGA 0 (11.2.2).

> **The cohomology of a filtered complex, filtered.** `H^n(K^•)` together with the filtration
> `F^pH^n(K^•) = Im(H^n(F^pK^•) ⟶ H^n(K^•))` induced on it by `(K^•, F)` ([Stacks, Tag 012P]), as
> an object of `Fil(C) = CategoryTheory.FilteredObject C ℤᵒᵖ`.  Packaging the induced filtration
> this way is what lets `CategoryTheory.FilteredObject.gr p` be applied to it, so that the graded
> pieces `gr^pH^n(K^•)` are the values of a functor.

```lean
noncomputable def inducedFilteredObject (K : Filtered C) (n : ℤ) : FilteredObject C ℤᵒᵖ
```

**`CochainComplex.Filtered.inducedFiltration`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Defs.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Defs.lean#L72).

> The filtration of `H^n(K^•)` induced by a filtered complex `K^•`, with steps
> `F^pH^n(K^•) = Im(H^n(F^pK^•) ⟶ H^n(K^•))`.

```lean
noncomputable def inducedFiltration : Filtration (K.X.homology n) ℤᵒᵖ
```

**`CochainComplex.Filtered.inducedFilteredObjectFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Leray/FunctorialFilteredAbutment.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Leray/FunctorialFilteredAbutment.lean#L118). The attribute's comment: “the induced filtration of `H^n`, functorially in the filtered complex”.

> The cohomology `H^n` of a functorial filtered complex, with its induced filtration, as a
> functor to `Fil(𝒜)`.

```lean
def inducedFilteredObjectFunctor (G : D ⥤ Filtered C) (n : ℤ) : D ⥤ FilteredObject C ℤᵒᵖ
```

## Tag 012R, an equation

[Tag 012R](https://stacks.math.columbia.edu/tag/012R) in the Stacks Project.

**`sub_image_homologyMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/InducedFiltration.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/InducedFiltration.lean#L601).

> **Stacks 012R.** The step `F^{p'}H^n(K^•)` of the induced filtration on cohomology, read as a
> subobject of `K^n`, is `Ker(d^n) ∩ F^{p'}K^n + Im(d^{n-1})`.

```lean
lemma sub_image_homologyMap (F : ℤ → ∀ m : ℤ, Subobject (K.X.X m))
    (hF : ∀ p' m : ℤ, F p' m = Subobject.mk ((K.filtration.ι.app (op p')).f m)) (p' : ℤ) :
    (Subobject.exists (K.X.iCycles n)).obj ((Subobject.pullback (K.X.homologyπ n)).obj
        (Subobject.mk (image.ι (HomologicalComplex.homologyMap
          (K.filtration.ι.app (op p')) n))))
      = kernelSubobject (K.X.d n (n + 1)) ⊓ F p' n ⊔ imageSubobject (K.X.d (n - 1) n)
```

## Tag 0BDT, an equation

[Tag 0BDT](https://stacks.math.columbia.edu/tag/0BDT) in the Stacks Project.

**`CochainComplex.Filtered.exists_iso_gradedHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean#L419).

> **Stacks 0BDT.** The graded piece `gr^pH^n(K^•) = F^pH^n(K^•)/F^{p + 1}H^n(K^•)` of the
> filtration induced on cohomology is
> `(Ker(d) ∩ F^pK^n)/(Ker(d) ∩ F^{p + 1}K^n + Im(d) ∩ F^pK^n)`: there is an isomorphism between the
> two compatible with the canonical maps to both from the cycles of `K^•` lying in `F^pK^n`.

```lean
theorem exists_iso_gradedHomology (p n : ℤ) :
    ∃ (a : (K.cyclesInStep p n : C) ⟶
        (kernelSubobject (K.X.d n (n + 1)) ⊓ K.step p n : Subobject (K.X.X n)))
      (b : (K.cyclesInStep p n : C) ⟶
        image (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))
      (e : cokernel (Subobject.ofLE _ _ (K.kernel_inf_step_succ_sup_image_inf_step_le p n)) ≅
        K.gradedHomology p n),
      a ≫ (kernelSubobject (K.X.d n (n + 1)) ⊓ K.step p n).arrow =
        (K.cyclesInStep p n).arrow ≫ K.X.iCycles n ∧
      b ≫ image.ι (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n) =
        (K.cyclesInStep p n).arrow ≫ K.X.homologyπ n ∧
      a ≫ cokernel.π (Subobject.ofLE _ _ (K.kernel_inf_step_succ_sup_image_inf_step_le p n)) ≫
          e.hom =
        b ≫ cokernel.π (image.preComp
          (HomologicalComplex.homologyMap (K.filtration.diagram.map
            (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
          (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))
```

## Tag 012Q, a lemma

[Tag 012Q](https://stacks.math.columbia.edu/tag/012Q) in the Stacks Project.

**`CochainComplex.exists_epi_gradedPiece_homology_of_isGLB_isLUB`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/StablePage.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/StablePage.lean#L569).

> **Stacks 012Q.** Let `𝒜` be an abelian category and let `(K^•, F)` be a filtered complex of
> `𝒜`, with degreewise filtration subobjects `F^p K^n`. Fix `p, n : ℤ` and write `q = n - p`.
> Assume the stable cycles `Z_∞^{p, q}` and the stable boundaries `B_∞^{p, q}` exist, i.e. that
> `Z` is the greatest lower bound of the subobjects `F^p K^n ∩ (d^n)⁻¹(F^\{p + r}K^\{n + 1})
> + F^\{p + 1}K^n` and `B` the least upper bound of the subobjects
> `F^p K^n ∩ d^{n - 1}(F^{p - r}K^{n - 1}) + F^{p + 1}K^n` of `K^n`. Then
> `B_∞^{p, q} ≤ Z_∞^{p, q}`, so the limit `E_∞^{p, q} = Z_∞^{p, q}/B_∞^{p, q}` exists, and the
> graded piece `gr^p H^n(K^•)` of the induced filtration on cohomology is a subquotient of it: the
> object `A = Ker(d^n) ∩ F^p K^n` maps to `Z_∞^{p, q}` and to `F^p H^n(K^•)`, its image `S` in
> `E_∞^{p, q}` is a subobject of `E_∞^{p, q}`, and the induced map `S ⟶ gr^p H^n(K^•)` is an
> epimorphism.

```lean
public theorem exists_epi_gradedPiece_homology_of_isGLB_isLUB
    {C : Type u} [Category.{v} C] [Abelian C]
    (K : FilteredObject (CochainComplex C ℤ) ℤᵒᵖ) (p n : ℤ)
    (F : ℤ → ∀ m : ℤ, Subobject (K.X.X m))
    (hF : ∀ p' m : ℤ, F p' m = Subobject.mk ((K.filtration.ι.app (op p')).f m))
    (A : Subobject (K.X.cycles n)) (hA : A = (Subobject.pullback (K.X.iCycles n)).obj (F p n))
    (Z B : Subobject (K.X.X n))
    (hZ : IsGLB (Set.range fun r : ℕ =>
      F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)) ⊔ F (p + 1) n) Z)
    (hB : IsLUB (Set.range fun r : ℕ =>
      F p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (F (p - r) (n - 1)) ⊔ F (p + 1) n) B) :
    B ≤ Z ∧
    ∃ (a : (A : C) ⟶ (Z : C))
      (b : (A : C) ⟶ image (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))
      (S : Subobject (cokernel (Subobject.ofLE (B ⊓ Z) Z inf_le_right)))
      (g : (A : C) ⟶ (S : C))
      (e : (S : C) ⟶ cokernel (image.preComp
        (HomologicalComplex.homologyMap (K.filtration.diagram.map
          (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
        (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))),
      A.arrow ≫ K.X.iCycles n = a ≫ Z.arrow ∧
      A.arrow ≫ K.X.homologyπ n =
        b ≫ image.ι (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n) ∧
      Epi g ∧ Epi e ∧
      g ≫ S.arrow = a ≫ cokernel.π (Subobject.ofLE (B ⊓ Z) Z inf_le_right) ∧
      g ≫ e = b ≫ cokernel.π (image.preComp
        (HomologicalComplex.homologyMap (K.filtration.diagram.map
          (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
        (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))
```

## Tag 0BDU, a definition

[Tag 0BDU](https://stacks.math.columbia.edu/tag/0BDU) in the Stacks Project.

**`IsRegularChainComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L45). The attribute's comment: “regular”.

> A cohomological spectral sequence `E` (with `d_r` of bidegree `(r, 1 - r)`) is
> *regular* if for every `(p, q) : ℤ × ℤ` there exists `b : ℤ` such that the
> differential `d_r^{p,q} : E_r^{p,q} → E_r^{p + r, q - r + 1}` is zero for all
> `r ≥ b` (with `r₀ ≤ r`).

```lean
def IsRegularChainComplex (E : CohomologicalSpectralSequence C r₀) : Prop
```

**`IsCoregular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L54). The attribute's comment: “coregular”.

> A cohomological spectral sequence `E` (with `d_r` of bidegree `(r, 1 - r)`)
> is *coregular* if for every `(p, q) : ℤ × ℤ` there exists `b : ℤ` such that the
> differential `d_r^{p - r, q + r - 1} : E_r^{p-r, q+r-1} → E_r^{p, q}` is zero for
> all `r ≥ b` (with `r₀ ≤ r`).

```lean
def IsCoregular (E : CohomologicalSpectralSequence C r₀) : Prop
```

**`IsBounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L62). The attribute's comment: “bounded”. References: EGA 0 (11.1.1), “partial”.

> A cohomological spectral sequence `E` is *bounded* if for every total degree
> `n : ℤ` there are only finitely many pairs `p : ℤ` such that
> `E_{r₀}^{p, n - p}` is nonzero.

```lean
def IsBounded (E : CohomologicalSpectralSequence C r₀) : Prop
```

**`IsBoundedBelow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L69). The attribute's comment: “bounded below”.

> A cohomological spectral sequence `E` is *bounded below* if for every total
> degree `n : ℤ` there exists `b : ℤ` such that `E_{r₀}^{p, n - p} = 0` for all
> `p ≥ b`.

```lean
def IsBoundedBelow (E : CohomologicalSpectralSequence C r₀) : Prop
```

**`IsBoundedAbove`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L76). The attribute's comment: “bounded above”.

> A cohomological spectral sequence `E` is *bounded above* if for every total
> degree `n : ℤ` there exists `b : ℤ` such that `E_{r₀}^{p, n - p} = 0` for all
> `p ≤ b`.

```lean
def IsBoundedAbove (E : CohomologicalSpectralSequence C r₀) : Prop
```

## Tag 0BDV, a lemma

[Tag 0BDV](https://stacks.math.columbia.edu/tag/0BDV) in the Stacks Project.

**`CohomologicalSpectralSequence.isRegularChainComplex_iff_Z_eventually_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L175). The attribute's comment: “(1)”.

> Part (1): the spectral sequence is regular iff for all `p, q` the cycles `Z_r^{p,q}` are
> eventually constant.

```lean
theorem isRegularChainComplex_iff_Z_eventually_constant :
    IsRegularChainComplex E ↔ ∀ p q : ℤ, ∃ b : ℤ, ∀ r, b ≤ r → E.Z (p, q) r = E.Z (p, q) b
```

**`CohomologicalSpectralSequence.isCoregular_iff_B_eventually_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L192). The attribute's comment: “(2)”.

> Part (2): the spectral sequence is coregular iff for all `p, q` the boundaries `B_r^{p,q}`
> are eventually constant.

```lean
theorem isCoregular_iff_B_eventually_constant :
    IsCoregular E ↔ ∀ p q : ℤ, ∃ b : ℤ, ∀ r, b ≤ r → E.B (p, q) r = E.B (p, q) b
```

**`CohomologicalSpectralSequence.isBounded_iff_isBoundedBelow_and_isBoundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L206). The attribute's comment: “(3)”.

> Part (3): the spectral sequence is bounded iff it is both bounded below and bounded
> above.

```lean
theorem isBounded_iff_isBoundedBelow_and_isBoundedAbove :
    IsBounded E ↔ IsBoundedBelow E ∧ IsBoundedAbove E
```

**`CohomologicalSpectralSequence.isRegularChainComplex_of_isBoundedBelow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L224). The attribute's comment: “(4)”.

> Part (4): if the spectral sequence is bounded below, then it is regular.

```lean
theorem isRegularChainComplex_of_isBoundedBelow (h : IsBoundedBelow E) :
    IsRegularChainComplex E
```

**`CohomologicalSpectralSequence.isCoregular_of_isBoundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Boundedness.lean#L234). The attribute's comment: “(5)”.

> Part (5): if the spectral sequence is bounded above, then it is coregular.

```lean
theorem isCoregular_of_isBoundedAbove (h : IsBoundedAbove E) : IsCoregular E
```

## Tag 012U, a definition

[Tag 012U](https://stacks.math.columbia.edu/tag/012U) in the Stacks Project.

**`CochainComplex.Filtered.WeaklyConverges`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L211). The attribute's comment: “(1)”. References: EGA 0 (11.1.3), “special case”.

> **Stacks 012U (1).** The spectral sequence of a filtered complex `K` *weakly converges* to
> `H^*(K^•)` if for all `p, n` the stable cycles `Z_∞^{p, n - p}` and boundaries
> `B_∞^{p, n - p}` exist and `gr^p H^n(K^•) = E_∞^{p, n - p}` via [Stacks, Tag 012Q]: there is an
> isomorphism `E_∞^{p, n - p} = Z_∞^{p, n - p}/B_∞^{p, n - p} ≅ gr^p H^n(K^•)` compatible with the
> canonical maps to both from `Ker(d^n) ∩ F^p K^n`.

```lean
def WeaklyConverges : Prop
```

**`CochainComplex.Filtered.Abuts`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L231). The attribute's comment: “(2)”.

> **Stacks 012U (2).** The spectral sequence of a filtered complex `K` *abuts* to `H^*(K^•)` if
> it weakly converges to `H^*(K^•)` and for all `n` the induced filtration on `H^n(K^•)` is
> separated, `⋂_p F^p H^n(K^•) = 0`, and exhaustive, `⋃_p F^p H^n(K^•) = H^n(K^•)`.

```lean
def Abuts : Prop
```

**`CochainComplex.Filtered.Converges`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Defs/FilteredComplex.lean#L239). The attribute's comment: “(3)”.

> **Stacks 012U (3).** The spectral sequence of a filtered complex `K` *converges* to
> `H^*(K^•)` if it is regular, abuts to `H^*(K^•)`, and
> `H^n(K^•) = lim_p H^n(K^•)/F^p H^n(K^•)` for all `n`.

```lean
def Converges : Prop
```

## Tag 012V, a lemma

[Tag 012V](https://stacks.math.columbia.edu/tag/012V) in the Stacks Project.

**`CochainComplex.exists_iso_stablePage_iff_and_isGLB_isLUB_inducedFiltration_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/StablePage.lean, line 648](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/StablePage.lean#L648).

> **Stacks 012V.** Let `𝒜` be an abelian category, let `(K^•, F)` be a filtered complex of `𝒜`
> with degreewise filtration subobjects `F p n = F^p K^n`, and fix `p n : ℤ`; write `q = n - p`,
> `A = Ker(d^n) ∩ F^p K^n`, `N = Ker(d^n) ∩ F^p K^n + F^{p + 1}K^n` (the left-hand side of the
> inclusion (012S)), `D = Im(d^{n - 1}) ∩ F^p K^n + F^{p + 1}K^n` (the right-hand side of the
> inclusion (012T)), and `FH p' = F^{p'} H^n(K^•)` for the induced filtration on cohomology. Then:
>
> 1. whenever `Z = Z_∞^{p, q}` and `B = B_∞^{p, q}` exist, the graded piece `gr^p H^n(K^•)` is the
>    whole of the limit `E_∞^{p, q} = Z/B` — that is, there is an isomorphism between them
>    compatible with the two canonical maps out of `A` — if and only if `Z = N` and `B = D`, i.e.
>    if and only if (012S) and (012T) are equalities;
> 2. the induced filtration on `H^n(K^•)` is separated, `⋂_{p'} F^{p'} H^n(K^•) = 0`, if and only if
>    `⋂_{p'} (Ker(d^n) ∩ F^{p'}K^n + Im(d^{n - 1})) = Im(d^{n - 1})`, and it is exhaustive,
>    `⋃_{p'} F^{p'}H^n(K^•) = H^n(K^•)`, if and only if
>    `⋃_{p'} (Ker(d^n) ∩ F^{p'}K^n + Im(d^{n - 1})) = Ker(d^n)`.
>
> Weak convergence to `H^*(K^•)` is (1) for all `p, n`, and abutment is weak convergence together
> with (2) for all `n`.

```lean
public theorem exists_iso_stablePage_iff_and_isGLB_isLUB_inducedFiltration_iff
    {C : Type u} [Category.{v} C] [Abelian C]
    (K : FilteredObject (CochainComplex C ℤ) ℤᵒᵖ) (p n : ℤ)
    (F : ℤ → ∀ m : ℤ, Subobject (K.X.X m))
    (hF : ∀ p' m : ℤ, F p' m = Subobject.mk ((K.filtration.ι.app (op p')).f m))
    (A : Subobject (K.X.cycles n))
    (hA : A = (Subobject.pullback (K.X.iCycles n)).obj (F p n))
    (N D : Subobject (K.X.X n))
    (hN : N = kernelSubobject (K.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n)
    (hD : D = imageSubobject (K.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n)
    (FH : ℤ → Subobject (K.X.homology n))
    (hFH : ∀ p' : ℤ, FH p' =
      Subobject.mk (image.ι (HomologicalComplex.homologyMap (K.filtration.ι.app (op p')) n))) :
    (∀ Z B : Subobject (K.X.X n),
        IsGLB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)) ⊔ F (p + 1) n) Z →
        IsLUB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (F (p - r) (n - 1)) ⊔
            F (p + 1) n) B →
        ∀ a : (A : C) ⟶ (Z : C), a ≫ Z.arrow = A.arrow ≫ K.X.iCycles n →
        ∀ b : (A : C) ⟶ image (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n),
          b ≫ image.ι (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n) =
            A.arrow ≫ K.X.homologyπ n →
        ((∃ e : cokernel (Subobject.ofLE (B ⊓ Z) Z inf_le_right) ≅
              cokernel (image.preComp
                (HomologicalComplex.homologyMap (K.filtration.diagram.map
                  (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
                (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n)),
            a ≫ cokernel.π (Subobject.ofLE (B ⊓ Z) Z inf_le_right) ≫ e.hom =
              b ≫ cokernel.π (image.preComp
                (HomologicalComplex.homologyMap (K.filtration.diagram.map
                  (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
                (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))) ↔
          Z = N ∧ B = D)) ∧
      (IsGLB (Set.range FH) ⊥ ↔
        IsGLB (Set.range fun p' : ℤ => kernelSubobject (K.X.d n (n + 1)) ⊓ F p' n ⊔
          imageSubobject (K.X.d (n - 1) n)) (imageSubobject (K.X.d (n - 1) n))) ∧
      (IsLUB (Set.range FH) ⊤ ↔
        IsLUB (Set.range fun p' : ℤ => kernelSubobject (K.X.d n (n + 1)) ⊓ F p' n ⊔
          imageSubobject (K.X.d (n - 1) n)) (kernelSubobject (K.X.d n (n + 1))))
```

## Tag 012W, a lemma

[Tag 012W](https://stacks.math.columbia.edu/tag/012W) in the Stacks Project.

**`CochainComplex.Filtered.abutsTo_of_isDegreewiseFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/AbutsTo.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/AbutsTo.lean#L132). The attribute's comment: “(2) and (3) together, in the form `E` abuts to `H^*(K^•)`”.

> **The spectral sequence of a degreewise finite filtered complex abuts to its cohomology.**
>
> The spectral sequence is presented as in [Stacks, Tag 012W]: by an isomorphism `hE` of each page
> with the subquotient `Z_r^{p,q}/(D_r^{p,q} ⊓ Z_r^{p,q})` of `K^n`.  This is the presentation in
> which [Stacks, Tag 012M], [Stacks, Tag 012W], [Stacks, Tag 0132] and [Stacks, Tag 015N] all state
> their conclusions, so a consumer which has invoked one of those already has the data to hand.
>
> The filtration witnessing the abutment is the one [Stacks, Tag 012P] induces on `H^n(K^•)`, and
> degreewise finiteness of the filtration of `K^•` is the only hypothesis.

```lean
theorem abutsTo_of_isDegreewiseFinite (K : Filtered C) (F : ∀ (_p n : ℤ), Subobject (K.X.X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hZ : ∀ r p n : ℤ, Z r p n =
      F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» (K.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
    (E : CohomologicalSpectralSequence C 0)
    (hE : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)))
    (hK : K.filtration.IsDegreewiseFinite) :
    SpectralSequence.AbutsTo E (fun n => K.X.homology n)
```

**`CochainComplex.Filtered.abutsTo_of_isDegreewiseFinite'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/AbutsTo.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/AbutsTo.lean#L161). The attribute's comment: “(2) and (3), for the canonical spectral sequence of a filtered complex”. References: SGA 4 Vbis (2.5.2), “partial”.

> **The canonical spectral sequence of a degreewise finite filtered complex abuts to its
> cohomology.**  `abutsTo_of_isDegreewiseFinite` for
> `CochainComplex.Filtered.spectralSequenceFunctor`, whose pages are the subquotients
> `Z_r^{p,q}/(D_r^{p,q} ⊓ Z_r^{p,q})` on the nose, so that the presentation hypotheses are
> discharged and degreewise finiteness is the only one left.

```lean
theorem abutsTo_of_isDegreewiseFinite' (K : Filtered C)
    (hK : K.filtration.IsDegreewiseFinite) :
    SpectralSequence.AbutsTo (spectralSequenceFunctor.obj K) (fun n => K.X.homology n)
```

**`CochainComplex.Filtered.nonempty_pageInfinityIso_gr'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Convergence.lean, line 801](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Convergence.lean#L801). The attribute's comment: “(3), the comparison `E_∞^{p,q} ≅ gr^pH^n(K^•)` of (012V) is an isomorphism”.

> **`E_∞^{p,q} ≅ gr^p H^{p+q}(K^•)`.**  For a filtered complex `(K^•, F)` of an abelian
> category whose filtration is finite in each degree, the infinity page of its spectral sequence at
> the bidegree `(p, q)` is the `p`-th graded piece of the filtration induced on `H^{p+q}(K^•)`.
>
> This is the convergence datum of [Stacks, Tag 012W\](3): the spectral sequence converges to
> `H^*(K^•)`.  Degreewise finiteness of the filtration is the only hypothesis; the boundedness, the
> finiteness of the induced filtration, the regularity and the two equalities (012S), (012T) that
> the statement of 012W lists separately are all consequences of it, and are discharged here.
>
> The isomorphism is `pageInfinityIsoGrAt` at a stable page chosen by `exists_isStableFrom`; only
> its existence is asserted, because a page chosen here is not a page chosen anywhere else.

```lean
theorem nonempty_pageInfinityIso_gr' (hK : K.filtration.IsDegreewiseFinite) (p q : ℤ) :
    Nonempty (E.pageInfinity (p, q) ≅
      (FilteredObject.gr p).obj (K.inducedFilteredObject (p + q)))
```

**`CochainComplex.Filtered.nonempty_pageInfinityIso_gr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Convergence.lean, line 832](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Convergence.lean#L832). The attribute's comment: “(3), for the canonical spectral sequence of a filtered complex”. References: SGA 4 Vbis (2.5.2), “partial”.

> **`E_∞^{p,q} ≅ gr^p H^{p+q}(K^•)` for the canonical spectral sequence of a filtered
> complex.**  `nonempty_pageInfinityIso_gr'` for
> `CochainComplex.Filtered.spectralSequenceFunctor`, whose pages are the subquotients
> `Z_r^{p,q}/(D_r^{p,q} ⊓ Z_r^{p,q})` on the nose.

```lean
theorem nonempty_pageInfinityIso_gr (K : Filtered C)
    (hK : K.filtration.IsDegreewiseFinite) (p q : ℤ) :
    Nonempty ((spectralSequenceFunctor.obj K).pageInfinity (p, q) ≅
      (FilteredObject.gr p).obj (K.inducedFilteredObject (p + q)))
```

**`CochainComplex.isBounded_and_converges_of_isDegreewiseFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/Convergence.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/Convergence.lean#L378). References: EGA 0 (11.2.4), “special case”.

> **Stacks 012W.** Let `𝒜` be an abelian category and let `(K^•, F)` be a filtered complex of
> `𝒜` whose filtration is finite in each degree. Let `E` be the spectral sequence of `(K^•, F)`,
> so that its page at `(r, p, q)` is `Z_r^{p,q}/D_r^{p,q}` for `n = p + q`, where
> `Z_r^{p,q} = F^p K^n ⊓ (d^n)⁻¹(F^{p+r}K^{n+1})` and
> `D_r^{p,q} = Z_{r-1}^{p+1,q-1} ⊔ d^{n-1}(Z_{r-1}^{p-r+1,q+r-2})`, and let
> `F^p H^n(K^•) = Im(H^n(F^pK^•) ⟶ H^n(K^•))` be the induced filtration on cohomology. Then:
>
> 1. `E` is bounded: for every `n` only finitely many `E_0^{p, n-p}` are nonzero;
> 2. the induced filtration on each `H^n(K^•)` is finite;
> 3. `E` converges to `H^*(K^•)`: it is regular, `d_r^{p,q} = 0` for `r ≫ 0`, and it converges
>    weakly, the stable cycles and boundaries `Z_∞^{p,q}` and `B_∞^{p,q}` existing and being equal
>    to `Ker(d^n) ⊓ F^p K^n ⊔ F^{p+1}K^n` and `Im(d^{n-1}) ⊓ F^p K^n ⊔ F^{p+1}K^n`, i.e. equality
>    holding in (012S) and (012T);
> 4. if `𝒞 ⊆ 𝒜` is a weak Serre subcategory with `E_r^{p,q}` in `𝒞` for all `p, q` and some
>    `r ≥ 0`, then every `H^n(K^•)` is in `𝒞`.

```lean
public theorem isBounded_and_converges_of_isDegreewiseFinite
    {A : Type u} [Category.{v} A] [Abelian A]
    (K : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
    (hK : K.filtration.IsDegreewiseFinite)
    (F : ∀ (_p n : ℤ), Subobject (K.X.X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hZ : ∀ r p n : ℤ, Z r p n =
      F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» (K.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
    (FH : ∀ (n _p : ℤ), Subobject (K.X.homology n))
    (hFH : ∀ n p : ℤ, FH n p =
      imageSubobject (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))
    (E : CohomologicalSpectralSequence A 0)
    (hE : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))) :
    (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0).X (p, n - p))}.Finite) ∧
    (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
    (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
      (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
    (∀ p n : ℤ,
      IsGLB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)) ⊔ F (p + 1) n)
        (kernelSubobject (K.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n) ∧
      IsLUB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (F (p - r) (n - 1)) ⊔ F (p + 1) n)
        (imageSubobject (K.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n)) ∧
    (∀ (P : ObjectProperty A) [P.IsWeakSerreClass] (r : ℤ) (hr : 0 ≤ r),
      (∀ p q : ℤ, P ((E.page r hr).X (p, q))) → ∀ n : ℤ, P (K.X.homology n))
```

## Tag 0BDW, a lemma

[Tag 0BDW](https://stacks.math.columbia.edu/tag/0BDW) in the Stacks Project.

**`CochainComplex.Filtered.finite_homology_and_sum_negOnePow_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean, line 1212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex.lean#L1212).

> **Stacks 0BDW.** Let `(K^•, F)` be a filtered complex of `C` whose filtration is finite in
> each degree, and let `E` be its spectral sequence, presented by the identification of its pages
> with `Z_s^{p, q}/(D_s^{p, q} ∩ Z_s^{p, q})` of [Stacks, Tag 012M]. If some page `E_r` has only
> finitely many nonzero terms, then only finitely many `H^n(K^•)` are nonzero, and for every weak
> Serre subcategory `P` of `C` containing the terms of `E_r` (for instance the smallest one) the
> `H^n(K^•)` lie in `P` and `∑ (-1)^n [H^n(K^•)] = ∑ (-1)^{p + q} [E_r^{p, q}]` in `K₀(P)`.

```lean
theorem finite_homology_and_sum_negOnePow_eq (hK : K.filtration.IsDegreewiseFinite)
    (E : CohomologicalSpectralSequence C 0)
    (e : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : boundaries K.X K.step r p n ⊓
        cycles K.X K.step r p n ≤ cycles K.X K.step r p n)))
    (r : ℤ) (hr : 0 ≤ r) (hfin : {pq : ℤ × ℤ | ¬ IsZero ((E.page r hr).X pq)}.Finite)
    (P : ObjectProperty C) [P.IsWeakSerreClass] (hP : ∀ pq : ℤ × ℤ, P ((E.page r hr).X pq)) :
    {n : ℤ | ¬ IsZero (K.X.homology n)}.Finite ∧
    ∃ hH : ∀ n : ℤ, P (K.X.homology n),
      ∑ᶠ n : ℤ, (n.negOnePow : ℤ) • KZero.mk P.FullSubcategory ⟨K.X.homology n, hH n⟩ =
        ∑ᶠ pq : ℤ × ℤ, ((pq.1 + pq.2).negOnePow : ℤ) •
          KZero.mk P.FullSubcategory ⟨(E.page r hr).X pq, hP pq⟩
```

## Tag 0BK5, a lemma

[Tag 0BK5](https://stacks.math.columbia.edu/tag/0BK5) in the Stacks Project.

**`CochainComplex.isBounded_and_converges_of_eventually_isZero_of_eventually_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/Convergence.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/FilteredComplex/Basic/Convergence.lean#L677). References: EGA 0 (13.6.4), “partial”.

> **Stacks 0BK5.** Let `𝒜` be an abelian category and let `(K^•, F)` be a filtered complex of
> `𝒜` such that, for every `n`, `H^n(F^pK^•) = 0` for `p ≫ 0` and `H^n(F^pK^•) ⟶ H^n(K^•)` is an
> isomorphism for `p ≪ 0`. Let `E` be the spectral sequence of `(K^•, F)`, presented as in
> `isBounded_and_converges_of_isDegreewiseFinite` by its pages `Z_r^{p,q}/D_r^{p,q}`, and let
> `F^p H^n(K^•) = Im(H^n(F^pK^•) ⟶ H^n(K^•))`. Then:
>
> 1. `E` is bounded: for every `n` only finitely many `E_1^{p, n-p}` are nonzero;
> 2. the induced filtration on each `H^n(K^•)` is finite;
> 3. `E` converges to `H^*(K^•)`: it is regular, the stable cycles and boundaries exist and equality
>    holds in (012S) and (012T), and the resulting canonical comparison
>    `E_∞^{p, n-p} ≅ gr^p H^n(K^•)` of [Stacks, Tag 012V] is an isomorphism.
>
> Boundedness is stated on the first page, where the source's proof establishes it: under these
> hypotheses `E_0^{p, q} = gr^p K^{p+q}` need not vanish for `|p| ≫ 0` (take any acyclic complex
> with a nowhere-stationary filtration by acyclic subcomplexes), so the source's spectral sequence
> is bounded as a spectral sequence starting at `r = 1`.

```lean
public theorem isBounded_and_converges_of_eventually_isZero_of_eventually_isIso
    {A : Type u} [Category.{v} A] [Abelian A]
    (K : FilteredObject (CochainComplex A ℤ) ℤᵒᵖ)
    (F : ∀ (_p n : ℤ), Subobject (K.X.X n))
    (hF : ∀ p n : ℤ, F p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
    (Z : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hZ : ∀ r p n : ℤ, Z r p n =
      F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)))
    (D : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
    (hD : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
      (Subobject.«exists» (K.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
    (FH : ∀ (n _p : ℤ), Subobject (K.X.homology n))
    (hFH : ∀ n p : ℤ, FH n p =
      imageSubobject (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))
    (E : CohomologicalSpectralSequence A 0)
    (hE : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
      cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)))
    (hzero : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
      IsZero ((K.filtration.obj (op p)).homology n))
    (hiso : ∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
      IsIso (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n)) :
    (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 1 (by omega)).X (p, n - p))}.Finite) ∧
    (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
    (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
      (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
    (∀ p n : ℤ,
      IsGLB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (F (p + r) (n + 1)) ⊔
            F (p + 1) n)
        (kernelSubobject (K.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n) ∧
      IsLUB (Set.range fun r : ℕ =>
          F p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (F (p - r) (n - 1)) ⊔
            F (p + 1) n)
        (imageSubobject (K.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n)) ∧
    (∀ p n : ℤ,
      let C := (Subobject.pullback (K.X.iCycles n)).obj (F p n)
      let N := kernelSubobject (K.X.d n (n + 1)) ⊓ F p n ⊔ F (p + 1) n
      let B := imageSubobject (K.X.d (n - 1) n) ⊓ F p n ⊔ F (p + 1) n
      ∃ (a : (C : A) ⟶ (N : A))
        (b : (C : A) ⟶ image (HomologicalComplex.homologyMap
          (K.filtration.ι.app (op p)) n))
        (e : cokernel (Subobject.ofLE (B ⊓ N) N inf_le_right) ≅
          cokernel (image.preComp
            (HomologicalComplex.homologyMap (K.filtration.diagram.map
              (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
            (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n))),
        C.arrow ≫ K.X.iCycles n = a ≫ N.arrow ∧
        C.arrow ≫ K.X.homologyπ n =
          b ≫ image.ι (HomologicalComplex.homologyMap
            (K.filtration.ι.app (op p)) n) ∧
        a ≫ cokernel.π (Subobject.ofLE (B ⊓ N) N inf_le_right) ≫ e.hom =
          b ≫ cokernel.π (image.preComp
            (HomologicalComplex.homologyMap (K.filtration.diagram.map
              (homOfLE (Int.le_add_one le_rfl) : (p : ℤ) ⟶ p + 1).op) n)
            (HomologicalComplex.homologyMap
              (K.filtration.ι.app (op p)) n)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.24, Tag 012K](https://stacks.math.columbia.edu/tag/012K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
