---
declaration: section
origin: cited
lean: CochainComplex.KFlat, CochainComplex.KFlat.kFlat_tright_preserves_quasiIso, CochainComplex.KFlat.ScalarBaseChange.kFlat_extendScalars, CochainComplex.KFlat.tensor, CochainComplex.KFlat.kFlat_two_out_of_three_of_distTriang, KFlatTwoOutOfThree.kFlat_two_out_of_three, CochainComplex.KFlat.kFlat_of_flat, CochainComplex.KFlat.kFlat_colimit
statement: formalized
proof: formalized
---

# 15.60 Derived tensor product

Section 15.60 of the Stacks Project, [Tag 06XY](https://stacks.math.columbia.edu/tag/06XY). 16 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06XZ, a definition

[Tag 06XZ](https://stacks.math.columbia.edu/tag/06XZ) in the Stacks Project.

**`CochainComplex.KFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/KFlat.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/KFlat.lean#L49).

> A cochain complex `K` of `R`-modules is *K-flat* if the total complex `Tot(M ⊗_R K)` is
> acyclic for every acyclic cochain complex `M` of `R`-modules. Here `⊗` is the monoidal product of
> cochain complexes, i.e. the total complex of the tensor product double complex with the Koszul
> sign convention.

```lean
def CochainComplex.KFlat (K : CochainComplex (ModuleCat.{max u v} R) ℤ) : Prop
```

## Tag 06Y0, a lemma

[Tag 06Y0](https://stacks.math.columbia.edu/tag/06Y0) in the Stacks Project.

**`CochainComplex.KFlat.kFlat_tright_preserves_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/QuasiIso.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/QuasiIso.lean#L60).

> Tensoring with a K-flat complex and taking the total complex preserves
> quasi-isomorphisms in the homotopy category.

```lean
public theorem kFlat_tright_preserves_quasiIso {R : Type u} [CommRing R]
    (K : CochainComplex (ModuleCat.{max u v} R) ℤ) (hK : K.KFlat) :
    HomotopyCategory.quasiIso (ModuleCat.{max u v} R) (ComplexShape.up ℤ) ≤
      (HomotopyCategory.quasiIso (ModuleCat.{max u v} R) (ComplexShape.up ℤ)).inverseImage
        (Tright K)
```

## Tag 06Y1, a lemma

[Tag 06Y1](https://stacks.math.columbia.edu/tag/06Y1) in the Stacks Project.

**`CochainComplex.KFlat.ScalarBaseChange.kFlat_extendScalars`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/ScalarBaseChange.lean, line 693](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/ScalarBaseChange.lean#L693).

> **Stacks 06Y1.** Extension of scalars along `φ : R →+* R'` carries a K-flat complex of
> `R`-modules to a K-flat complex of `R'`-modules: tensoring over `R'` with the base change is,
> after restriction of scalars, tensoring over `R`, and restriction of scalars reflects
> acyclicity.
>
> The two rings inhabit independent universes `uR` and `uA`, as they do in the source, where they
> are related only by a ring map; the module universe `max v uR uA` is independent of both and
> large enough to hold the modules of either ring. `CochainComplex.kFlat_baseChange` in
> `StacksFrontier.Homology.KFlat.BaseChange` is the specialization of this statement to a single
> common universe.

```lean
public lemma kFlat_extendScalars (φ : R →+* R')
    (K : CochainComplex (ModuleCat.{max v uR uA} R) ℤ)
    (hK : CochainComplex.KFlat.{uR, max v uA} K) :
    CochainComplex.KFlat.{uA, max v uR} ((extendScalarsLarge.{v, uR, uA} φ).obj K)
```

## Tag 0795, a lemma

[Tag 0795](https://stacks.math.columbia.edu/tag/0795) in the Stacks Project.

**`CochainComplex.KFlat.tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/Basic.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/Basic.lean#L629).

> (Stacks tag 0795, Lemma 15.60.4) If `K` and `L` are K-flat complexes of
> `R`-modules, then `Tot(K ⊗_R L)` (i.e. the monoidal tensor product `K ⊗ L`) is
> K-flat.
>
> For acyclic `M`, K-flatness of `K` makes `M ⊗ K` acyclic, then K-flatness of `L`
> makes `(M ⊗ K) ⊗ L` acyclic, and acyclicity transfers to `M ⊗ (K ⊗ L)` across the
> associator.

```lean
theorem CochainComplex.KFlat.tensor (K L : CochainComplex (ModuleCat R) ℤ)
    (hK : K.KFlat) (hL : L.KFlat) : (K ⊗ L).KFlat
```

## Tag 06Y2, a lemma

[Tag 06Y2](https://stacks.math.columbia.edu/tag/06Y2) in the Stacks Project.

**`CochainComplex.KFlat.kFlat_two_out_of_three_of_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/Triangle.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/Triangle.lean#L52).

> K-flatness is a two-out-of-three property in a distinguished triangle of the homotopy
> category.

```lean
theorem kFlat_two_out_of_three_of_distTriang
    {R : Type u} [CommRing R] {K₁ K₂ K₃ : CochainComplex (ModuleCat.{u} R) ℤ}
    (f : (HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)).obj K₁ ⟶
      (HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)).obj K₂)
    (g : (HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)).obj K₂ ⟶
      (HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)).obj K₃)
    (h : (HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)).obj K₃ ⟶
      ((HomotopyCategory.quotient (ModuleCat.{u} R) (ComplexShape.up ℤ)).obj K₁)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk f g h ∈
      distTriang (HomotopyCategory (ModuleCat.{u} R) (ComplexShape.up ℤ))) :
    (K₂.KFlat → K₃.KFlat → K₁.KFlat) ∧
      (K₁.KFlat → K₃.KFlat → K₂.KFlat) ∧
      (K₁.KFlat → K₂.KFlat → K₃.KFlat)
```

## Tag 0BYH, a lemma

[Tag 0BYH](https://stacks.math.columbia.edu/tag/0BYH) in the Stacks Project.

**`KFlatTwoOutOfThree.kFlat_two_out_of_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/Basic.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/Basic.lean#L544).

> Two-out-of-three for K-flatness (Stacks Tag 0BYH, Lemma 15.60.6).
> Given a short exact sequence of complexes `0 → K₁ → K₂ → K₃ → 0` with every
> `K₃^n` flat, if at least two of `K₁, K₂, K₃` are K-flat, then all three are.
>
> Case analysis on the disjunction `h`, completing the missing third K-flatness via
> the corresponding directional lemma.

```lean
theorem kFlat_two_out_of_three {R : Type u} [CommRing R] (S : ShortComplex (Cx R))
    (hse : S.ShortExact) (hflat : ∀ n : ℤ, Module.Flat R (S.X₃.X n))
    (h : (CochainComplex.KFlat S.X₁ ∧ CochainComplex.KFlat S.X₂) ∨
          (CochainComplex.KFlat S.X₁ ∧ CochainComplex.KFlat S.X₃) ∨
          (CochainComplex.KFlat S.X₂ ∧ CochainComplex.KFlat S.X₃)) :
    CochainComplex.KFlat S.X₁ ∧ CochainComplex.KFlat S.X₂ ∧ CochainComplex.KFlat S.X₃
```

## Tag 064K, a lemma

[Tag 064K](https://stacks.math.columbia.edu/tag/064K) in the Stacks Project.

**`CochainComplex.KFlat.kFlat_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/Flat.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/Flat.lean#L510). References: SGA 4 XVII (4.1.7), “(ii), modules over ring”.

> **Stacks 064K.** A bounded above cochain complex of flat modules is K-flat.

```lean
public theorem kFlat_of_flat {R : Type u} [CommRing R]
    (P : CochainComplex (ModuleCat.{max u v} R) ℤ) (d : ℤ) [P.IsStrictlyLE d]
    [∀ n : ℤ, Module.Flat R (P.X n)] :
    P.KFlat
```

## Tag 06Y3, a lemma

[Tag 06Y3](https://stacks.math.columbia.edu/tag/06Y3) in the Stacks Project.

**`CochainComplex.KFlat.kFlat_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/Flat.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/Flat.lean#L543).

> A filtered colimit of K-flat complexes of modules is K-flat.

```lean
public theorem kFlat_colimit {R : Type u} [CommRing R]
    {J : Type v} [Category.{w} J] [Small.{max u x} J] [LocallySmall.{max u x} J] [IsFiltered J]
    (K : J ⥤ CochainComplex (ModuleCat.{max u x} R) ℤ)
    (hK : ∀ j, (K.obj j).KFlat) : (colimit K).KFlat
```

## Tag 0E8F, a lemma

[Tag 0E8F](https://stacks.math.columbia.edu/tag/0E8F) in the Stacks Project.

**`CochainComplex.KFlat.kFlat_of_tensor_finitelyPresented_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/FinitelyPresented.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/FinitelyPresented.lean#L534).

> **Stacks 0E8F.** A cochain complex whose tensor product with every finitely presented module
> is acyclic is K-flat.

```lean
public theorem kFlat_of_tensor_finitelyPresented_acyclic {R : Type u} [CommRing R]
    (K : CochainComplex (ModuleCat.{u} R) ℤ)
    (hK : ∀ M : ModuleCat.{u} R, Module.FinitePresentation R M →
      (K ⊗ (HomologicalComplex.single (ModuleCat.{u} R) (ComplexShape.up ℤ) 0).obj M).Acyclic) :
    K.KFlat
```

## Tag 06Y4, a lemma

[Tag 06Y4](https://stacks.math.columbia.edu/tag/06Y4) in the Stacks Project.

**`CochainComplex.KFlat.exists_kFlat_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/Resolution.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/Resolution.lean#L126).

> **Stacks 06Y4.** Every cochain complex of modules admits a termwise-surjective
> quasi-isomorphism from a K-flat complex with flat terms.

```lean
theorem exists_kFlat_resolution {R : Type u} [CommRing R]
    (M : CochainComplex (ModuleCat.{max u v} R) ℤ) :
    ∃ (K : CochainComplex (ModuleCat.{max u v} R) ℤ) (f : K ⟶ M),
      K.KFlat ∧
        (∀ n : ℤ, Module.Flat R (K.X n)) ∧
        QuasiIso f ∧
        ∀ n : ℤ, Function.Surjective (f.f n).hom
```

## Tag 09PB, a remark

[Tag 09PB](https://stacks.math.columbia.edu/tag/09PB) in the Stacks Project.

**`CochainComplex.KFlat.property_of_coproducts_of_two_out_of_three_of_shifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/FilteredColimitShifts.lean, line 1375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/FilteredColimitShifts.lean#L1375).

> Every complex has a split filtered resolution whose graded pieces are
> coproducts of shifts of the ring and whose filtration yields the canonical telescope triangle.
> Moreover, a property of objects of `D(R)` that is preserved by coproducts, satisfies
> two-out-of-three for distinguished triangles, and holds for every shift of `R`, holds for every
> object of `D(R)`.

```lean
theorem property_of_coproducts_of_two_out_of_three_of_shifts {R : Type u} [Ring R]
    [Small.{v} R] :
    (∀ M : CochainComplex (ModuleCat.{v} R) ℤ, Nonempty (SplitFilteredFreeResolution M)) ∧
      ∀ (T : DerivedCategory (ModuleCat.{v} R) → Prop),
        (∀ {I : Type v} (K : I → DerivedCategory (ModuleCat.{v} R)) [HasCoproduct K],
          (∀ i, T (K i)) → T (∐ K)) →
        (∀ (Δ : Triangle (DerivedCategory (ModuleCat.{v} R))),
          Δ ∈ distinguishedTriangles →
            (T Δ.obj₁ → T Δ.obj₂ → T Δ.obj₃) ∧
            (T Δ.obj₁ → T Δ.obj₃ → T Δ.obj₂) ∧
            (T Δ.obj₂ → T Δ.obj₃ → T Δ.obj₁)) →
        (∀ k : ℤ, T (((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj
          (ModuleCat.of R (Shrink.{v} R)))⟦k⟧)) →
        ∀ K, T K
```

## Tag 064L, a lemma

[Tag 064L](https://stacks.math.columbia.edu/tag/064L) in the Stacks Project.

**`CochainComplex.DerivedTensor.quasiIso_trightCochain_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensorKFlatResolution.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensorKFlatResolution.lean#L124).

> A quasi-isomorphism between K-flat complexes remains a quasi-isomorphism after tensoring on
> the right with any complex. This is the companion of `quasiIso_tleftCochain_map` (Stacks 064L),
> whose fixed factor is the left one.

```lean
theorem quasiIso_trightCochain_map
    {P Q : CochainComplex (ModuleCat.{max u v} R) ℤ} (α : P ⟶ Q) [QuasiIso α]
    (hP : P.KFlat) (hQ : Q.KFlat) (L : CochainComplex (ModuleCat.{max u v} R) ℤ) :
    QuasiIso ((TrightCochain L).map α)
```

**`CochainComplex.DerivedTensor.quasiIso_tleftCochain_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensorLargeUniverse.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensorLargeUniverse.lean#L200).

> A quasi-isomorphism between K-flat complexes remains a quasi-isomorphism after tensoring on
> the left with any complex and taking the total complex.

```lean
public theorem quasiIso_tleftCochain_map {R : Type u} [CommRing R]
    {P Q : CochainComplex (ModuleCat.{max u v} R) ℤ} (α : P ⟶ Q) [QuasiIso α]
    (hP : P.KFlat) (hQ : Q.KFlat) (L : CochainComplex (ModuleCat.{max u v} R) ℤ) :
    QuasiIso ((TleftCochain L).map α)
```

## Tag 064M, a definition

[Tag 064M](https://stacks.math.columbia.edu/tag/064M) in the Stacks Project.

**`CochainComplex.DerivedTensor.derivedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean#L63). References: SGA 4 XVII (4.1.7), “(i), modules over ring”.

> The derived tensor product with `M`, computed by a K-flat resolution of a representative of
> `M`.

```lean
public noncomputable def derivedTensorProduct
    (M : DerivedCategory (ModuleCat.{max u v} R)) :
    DerivedCategory (ModuleCat.{max u v} R) ⥤ DerivedCategory (ModuleCat.{max u v} R)
```

**`CochainComplex.DerivedTensor.derivedTensorProduct_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean#L79).

> The derived tensor product commutes with the shift functors.

```lean
public noncomputable instance derivedTensorProduct_commShift
    (M : DerivedCategory (ModuleCat.{max u v} R)) :
    (derivedTensorProduct M).CommShift ℤ
```

**`CochainComplex.DerivedTensor.derivedTensorProduct_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean#L100).

> The derived tensor product is an exact functor of triangulated categories.

```lean
public noncomputable instance derivedTensorProduct_isTriangulated
    (M : DerivedCategory (ModuleCat.{max u v} R)) :
    (derivedTensorProduct M).IsTriangulated
```

**`CochainComplex.DerivedTensor.derivedTensorProduct_iso_lift_of_kFlat_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensorFunctorLargeUniverse.lean#L207).

> A K-flat resolution of any representative of `M` computes the derived tensor product.
> The comparison is a natural isomorphism, uniquely determined by its pullback to the homotopy
> category.

```lean
public theorem derivedTensorProduct_iso_lift_of_kFlat_resolution
    (M : DerivedCategory (ModuleCat.{max u v} R))
    (P K : CochainComplex (ModuleCat.{max u v} R) ℤ) (f : K ⟶ P) [QuasiIso f]
    (hK : K.KFlat)
    (_eP : (DerivedCategory.Qh (C := ModuleCat.{max u v} R)).obj
      ((HomotopyCategory.quotient (ModuleCat.{max u v} R) (ComplexShape.up ℤ)).obj P) ≅ M) :
    let W := HomotopyCategory.quasiIso (ModuleCat.{max u v} R) (ComplexShape.up ℤ)
    let F := Tright K ⋙ DerivedCategory.Qh
    let hF : W.IsInvertedBy F := fun _ _ g hg ↦
      Localization.inverts DerivedCategory.Qh W _
        (CochainComplex.KFlat.kFlat_tright_preserves_quasiIso K hK g hg)
    let F' := Localization.lift F hF DerivedCategory.Qh
    Nonempty (DerivedCategory.Qh ⋙ derivedTensorProduct M ≅ F) ∧
      ∀ α : DerivedCategory.Qh ⋙ derivedTensorProduct M ≅ F,
        ∃! e : derivedTensorProduct M ≅ F',
          Functor.isoWhiskerLeft DerivedCategory.Qh e =
            α ≪≫ (Localization.fac F hF DerivedCategory.Qh).symm
```

## Tag 0BYI, a lemma

[Tag 0BYI](https://stacks.math.columbia.edu/tag/0BYI) in the Stacks Project.

**`CochainComplex.DerivedTensor.canonicalSymmetricDerivedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensor.lean, line 754](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensor.lean#L754).

> **Stacks 0BYI.** The canonical derived tensor product, equipped with its symmetry functorial
> in both complexes and represented on K-flat complexes in degrees `p` and `q` by the ordinary
> tensor braiding with the sign `(-1) ^ (p * q)`.

```lean
public noncomputable def canonicalSymmetricDerivedTensorProduct
    (R : Type u) [CommRing R]
    [HasDerivedCategory (ModuleCat.{u} R)] : SymmetricDerivedTensorProduct R
```

## Tag 0BYJ, a lemma

[Tag 0BYJ](https://stacks.math.columbia.edu/tag/0BYJ) in the Stacks Project.

**`CochainComplex.DerivedTensor.derivedTensorProduct_associator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensor.lean, line 1066](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensor.lean#L1066).

> **Stacks 0BYJ.** The derived tensor product is associative up to a canonical isomorphism,
> functorial in all three complexes. On K-flat representatives this is the standard associator
> of tensor products of complexes.

```lean
public theorem derivedTensorProduct_associator
    (R : Type u) [CommRing R] [HasDerivedCategory (ModuleCat.{u} R)] :
    let D := DerivedCategory (ModuleCat.{u} R)
    let C := CochainComplex (ModuleCat.{u} R) ℤ
    let Q := DerivedCategory.Q (C := ModuleCat.{u} R)
    let T := canonicalDerivedTensorProduct R
    ∃ associator : ∀ K L M : D,
          (T.tensor.obj ((T.tensor.obj K).obj L)).obj M ≅
            (T.tensor.obj K).obj ((T.tensor.obj L).obj M),
        (∀ {K K' L L' M M' : D} (f : K ⟶ K') (g : L ⟶ L') (h : M ⟶ M'),
          (T.tensor.map ((T.tensor.map f).app L ≫ (T.tensor.obj K').map g)).app M ≫
                (T.tensor.obj ((T.tensor.obj K').obj L')).map h ≫
                (associator K' L' M').hom =
            (associator K L M).hom ≫
              (T.tensor.map f).app ((T.tensor.obj L).obj M) ≫
              (T.tensor.obj K').map
                ((T.tensor.map g).app M ≫ (T.tensor.obj L').map h)) ∧
        ∀ (K L M : C) (hK : K.KFlat) (hL : L.KFlat) (hM : M.KFlat),
          let hKL := CochainComplex.KFlat.tensor R K L hK hL
          let hLM := CochainComplex.KFlat.tensor R L M hL hM
          (associator (Q.obj K) (Q.obj L) (Q.obj M)).hom ≫
                (T.tensor.obj (Q.obj K)).map (T.comparison L M hL hM).hom ≫
                (T.comparison K (L ⊗ M) hK hLM).hom =
            (T.tensor.map (T.comparison K L hK hL).hom).app (Q.obj M) ≫
              (T.comparison (K ⊗ L) M hKL hM).hom ≫
              Q.map (HomologicalComplex.associator K L M).hom
```

## Tag 0G6M, a lemma

[Tag 0G6M](https://stacks.math.columbia.edu/tag/0G6M) in the Stacks Project.

**`CochainComplex.KFlat.exists_kFlat_factorization_up_to_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/KFlat/Resolution.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/KFlat/Resolution.lean#L310).

> A morphism from a K-flat complex factors up to homotopy through another K-flat complex
> which maps to the target by a quasi-isomorphism. When the source has flat terms, the intermediate
> complex can be chosen with flat terms.

```lean
theorem exists_kFlat_factorization_up_to_homotopy
    {R : Type u} [CommRing R] {K L : CochainComplex (ModuleCat.{u} R) ℤ} (a : K ⟶ L)
    (hK : K.KFlat) :
    ∃ (N : CochainComplex (ModuleCat.{u} R) ℤ) (b : K ⟶ N) (c : N ⟶ L),
      N.KFlat ∧
        QuasiIso c ∧
        Nonempty (Homotopy a (b ≫ c)) ∧
        ((∀ n : ℤ, Module.Flat R (K.X n)) → ∀ n : ℤ, Module.Flat R (N.X n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.60, Tag 06XY](https://stacks.math.columbia.edu/tag/06XY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
