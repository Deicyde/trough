---
declaration: section
origin: cited
lean: Module.FiniteLength.IsAdmissibleSequence, Module.FiniteLength.AdmissibleSequence, Module.FiniteLength.DeterminantRelation, Module.FiniteLength.determinant, Module.FiniteLength.span_symbol_eq_top, Module.FiniteLength.finrank_determinant_le_one, Module.FiniteLength.exists_span_eq_top_and_span_symbol_eq_top, Module.FiniteLength.rank_determinant_le_one
statement: formalized
proof: formalized
---

# 42.68 Appendix A: Alternative approach to key lemma

Section 42.68 of the Stacks Project, [Tag 0EAZ](https://stacks.math.columbia.edu/tag/0EAZ). 39 tags here are carried by 87 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02P6, a definition

[Tag 02P6](https://stacks.math.columbia.edu/tag/02P6) in the Stacks Project.

**`Module.FiniteLength.IsAdmissibleSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean#L73). The attribute's comment: “admissible sequences”.

> **Stacks Project, Tag 02P6.** A finite sequence in a module over a local ring is
> admissible if the maximal ideal times each entry is contained in the span of the preceding
> entries.

```lean
public def IsAdmissibleSequence {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] {n : ℕ} (e : Fin n → M) : Prop
```

**`Module.FiniteLength.AdmissibleSequence`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean#L80). The attribute's comment: “symbols”.

> **Stacks Project, Tag 02P6.** The symbols used to generate the determinant: admissible
> sequences whose length is the length of the module.

```lean
public abbrev AdmissibleSequence (R : Type u) (M : Type v) [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
```

**`Module.FiniteLength.DeterminantRelation`**, an inductive in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean#L94). The attribute's comment: “admissible relations”.

> **Stacks Project, Tag 02P6.** The three families of admissible relations: a dependent
> entry gives zero, replacing an entry up to a unit and earlier entries scales by the residue
> of that unit, and two adjacent entries may be exchanged with a sign when the later entry
> satisfies the stronger admissibility condition.

```lean
public inductive DeterminantRelation {R : Type u} {M : Type v} [CommRing R]
    [IsLocalRing R] [AddCommGroup M] [Module R M] : DeterminantFree R M → Prop
```

**`Module.FiniteLength.determinant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Basic.lean#L128). The attribute's comment: “the determinant”.

> **Stacks Project, Tag 02P6.** The determinant of a finite-length module over a local
> ring, as a vector space over the residue field.

```lean
public abbrev determinant (R : Type u) (M : Type v) [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
```

## Tag 02P7, a lemma

[Tag 02P7](https://stacks.math.columbia.edu/tag/02P7) in the Stacks Project.

**`Module.FiniteLength.span_symbol_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/DimensionLeOne.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/DimensionLeOne.lean#L150). The attribute's comment: “generators”.

> **Stacks Project, Tags 02P7 and 02P9.** The symbol of every admissible sequence that
> spans a finite-length module generates its determinant over the residue field.

```lean
public theorem span_symbol_eq_top (_hM : IsFiniteLength R M)
    (e : AdmissibleSequence R M) (he : Submodule.span R (Set.range e.1) = ⊤) :
    (IsLocalRing.ResidueField R) ∙ symbol e = ⊤
```

**`Module.FiniteLength.finrank_determinant_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/DimensionLeOne.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/DimensionLeOne.lean#L160).

> **Stacks Project, Tag 02P7.** The determinant of a finite-length module over a local
> ring has dimension at most one over the residue field.

```lean
public theorem finrank_determinant_le_one
    (R : Type u) (M : Type v) [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] (hM : IsFiniteLength R M) :
    Module.finrank (IsLocalRing.ResidueField R) (determinant R M) ≤ 1
```

**`Module.FiniteLength.exists_span_eq_top_and_span_symbol_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RankLeOne.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RankLeOne.lean#L45). The attribute's comment: “generator”.

> **Stacks Project, Tag 02P7.** A finite-length module over a local ring has an
> admissible sequence that spans it, and the symbol of that sequence generates the
> determinant over the residue field.

```lean
public theorem exists_span_eq_top_and_span_symbol_eq_top
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] (hM : IsFiniteLength R M) :
    ∃ e : AdmissibleSequence R M, Submodule.span R (Set.range e.1) = ⊤ ∧
      (IsLocalRing.ResidueField R) ∙ symbol e = ⊤
```

**`Module.FiniteLength.rank_determinant_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RankLeOne.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RankLeOne.lean#L56).

> **Stacks Project, Tag 02P7.** The determinant of a finite-length module over a local
> ring has dimension at most one over the residue field.

```lean
public theorem rank_determinant_le_one
    (R : Type u) (M : Type v) [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] (hM : IsFiniteLength R M) :
    Module.rank (IsLocalRing.ResidueField R) (determinant R M) ≤ 1
```

## Tag 02P8, a lemma

[Tag 02P8](https://stacks.math.columbia.edu/tag/02P8) in the Stacks Project.

**`Module.FiniteLength.determinantExteriorPowerComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/ExteriorPower.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/ExteriorPower.lean#L254).

> For a finite-dimensional module over the residue field of a local ring, the determinant
> defined from admissible symbols is isomorphic to its top exterior power. Under this
> isomorphism a symbol is sent to the exterior product of its entries.

```lean
public noncomputable def determinantExteriorPowerComparison
    (R : Type u) (M : Type v) [CommRing R] [IsLocalRing R] [AddCommGroup M] [Module R M]
    [Module (IsLocalRing.ResidueField R) M]
    [IsScalarTower R (IsLocalRing.ResidueField R) M]
    [Module.Finite (IsLocalRing.ResidueField R) M] :
    DeterminantExteriorPowerComparison R M
```

## Tag 02P9, a lemma

[Tag 02P9](https://stacks.math.columbia.edu/tag/02P9) in the Stacks Project.

**`Module.FiniteLength.finrank_determinant_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Dimension/FinrankEqOne.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Dimension/FinrankEqOne.lean#L113). The attribute's comment: “dimension”.

> The determinant of a finite-length module over a local ring has dimension one over the
> residue field.

```lean
public theorem finrank_determinant_eq_one {R : Type u} {M : Type v} [CommRing R]
    [IsLocalRing R] [AddCommGroup M] [Module R M] (hM : IsFiniteLength R M) :
    Module.finrank (IsLocalRing.ResidueField R) (determinant R M) = 1
```

**`Module.FiniteLength.span_symbol_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/DimensionLeOne.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/DimensionLeOne.lean#L150). The attribute's comment: “generators”.

> **Stacks Project, Tags 02P7 and 02P9.** The symbol of every admissible sequence that
> spans a finite-length module generates its determinant over the residue field.

```lean
public theorem span_symbol_eq_top (_hM : IsFiniteLength R M)
    (e : AdmissibleSequence R M) (he : Submodule.span R (Set.range e.1) = ⊤) :
    (IsLocalRing.ResidueField R) ∙ symbol e = ⊤
```

## Tag 05M7, an equation

[Tag 05M7](https://stacks.math.columbia.edu/tag/05M7) in the Stacks Project.

**`Module.FiniteLength.determinantFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Functor.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Functor.lean#L472).

> **Stacks Project, Tag 05M7.** The determinant of a finite-length module over a local
> ring, together with the maps induced by module isomorphisms, is a functor to the groupoid
> of one-dimensional vector spaces over the residue field.

```lean
public noncomputable def determinantFunctor (R : Type u) [CommRing R] [IsLocalRing R] :
    DeterminantFunctor.{u, v} R
```

## Tag 02PA, a lemma

[Tag 02PA](https://stacks.math.columbia.edu/tag/02PA) in the Stacks Project.

**`Module.FiniteLength.determinantExactSequenceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/ExactSequence.lean, line 980](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/ExactSequence.lean#L980). The attribute's comment: “detexactsequencemap”.

> **Stacks Project, Tag 02PA (determinant exact-sequence map).** The canonical linear map
> from the tensor product of the determinants of the outer terms of a short exact sequence to
> the determinant of its middle term.

```lean
public noncomputable def determinantExactSequenceMap
    {R : Type u} [CommRing R] [IsLocalRing R]
    {K : Type v} {L : Type w} {M : Type x}
    [AddCommGroup K] [Module R K] [AddCommGroup L] [Module R L]
    [AddCommGroup M] [Module R M]
    (i : K →ₗ[R] L) (p : L →ₗ[R] M)
    (hi : Function.Injective i) (hp : Function.Surjective p) (hip : Function.Exact i p)
    (hK : IsFiniteLength R K) (hL : IsFiniteLength R L) (hM : IsFiniteLength R M) :
    determinant R K ⊗[IsLocalRing.ResidueField R] determinant R M →ₗ[IsLocalRing.ResidueField R]
      determinant R L
```

**`Module.FiniteLength.determinantExactSequenceMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaIsomorphism.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaIsomorphism.lean#L57). The attribute's comment: “gamma\_isomorphism”.

> **The determinant map of a short exact sequence is an isomorphism.** For a short exact
> sequence `0 → K → L → M → 0` of finite-length modules over a local ring, the determinant map
> `det(K) ⊗ det(M) → det(L)` is bijective.

```lean
public theorem determinantExactSequenceMap_bijective
    {R : Type u} [CommRing R] [IsLocalRing R]
    {K : Type v} {L : Type w} {M : Type x}
    [AddCommGroup K] [Module R K] [AddCommGroup L] [Module R L]
    [AddCommGroup M] [Module R M]
    (i : K →ₗ[R] L) (p : L →ₗ[R] M)
    (hi : Function.Injective i) (hp : Function.Surjective p) (hip : Function.Exact i p)
    (hK : IsFiniteLength R K) (hL : IsFiniteLength R L) (hM : IsFiniteLength R M) :
    Function.Bijective (determinantExactSequenceMap i p hi hp hip hK hL hM)
```

**`Module.FiniteLength.determinantExactSequenceMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaNatural.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaNatural.lean#L142). The attribute's comment: “gamma\_natural”.

> **Stacks Project, Tag 02PA (`gamma_natural`).** The determinant map of a short
> exact sequence is natural under an isomorphism of short exact sequences.

```lean
public theorem determinantExactSequenceMap_natural
    {R : Type u} [CommRing R] [IsLocalRing R]
    {K L M K' L' M' : FiniteLengthModuleIso.{u, v} R}
    (i : K.of.obj →ₗ[R] L.of.obj) (p : L.of.obj →ₗ[R] M.of.obj)
    (i' : K'.of.obj →ₗ[R] L'.of.obj) (p' : L'.of.obj →ₗ[R] M'.of.obj)
    (hi : Function.Injective i) (hp : Function.Surjective p)
    (hip : Function.Exact i p)
    (hi' : Function.Injective i') (hp' : Function.Surjective p')
    (hip' : Function.Exact i' p')
    (u : K ⟶ K') (v : L ⟶ L') (w : M ⟶ M')
    (hu : i'.comp u.iso.hom.hom.hom = v.iso.hom.hom.hom.comp i)
    (hw : p'.comp v.iso.hom.hom.hom = w.iso.hom.hom.hom.comp p) :
    (determinantExactSequenceMap i' p' hi' hp' hip'
      K'.of.property L'.of.property M'.of.property).comp
        (TensorProduct.map
          ((determinantFunctor R).mapLinearEquiv u).toLinearMap
          ((determinantFunctor R).mapLinearEquiv w).toLinearMap) =
      ((determinantFunctor R).mapLinearEquiv v).toLinearMap.comp
        (determinantExactSequenceMap i p hi hp hip
          K.of.property L.of.property M.of.property)
```

**`Module.FiniteLength.determinantExactSequenceMap_three_by_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaThreeByThree.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaThreeByThree.lean#L501). The attribute's comment: “gamma\_three\_by\_three”.

> **Stacks Project, Tag 02PA (`gamma_three_by_three`).** In a commutative
> three-by-three diagram with exact rows and columns, the two composites of determinant maps
> coincide after the middle determinant factors are interchanged with the Koszul sign.

```lean
public theorem determinantExactSequenceMap_three_by_three
    {R : Type u} [CommRing R] [IsLocalRing R]
    {A : Type vA} {B : Type vB} {C : Type vC}
    {D : Type vD} {E : Type vE} {F : Type vF}
    {G : Type vG} {H : Type vH} {I : Type vI}
    [AddCommGroup A] [Module R A] [AddCommGroup B] [Module R B]
    [AddCommGroup C] [Module R C] [AddCommGroup D] [Module R D]
    [AddCommGroup E] [Module R E] [AddCommGroup F] [Module R F]
    [AddCommGroup G] [Module R G] [AddCommGroup H] [Module R H]
    [AddCommGroup I] [Module R I]
    (iAB : A →ₗ[R] B) (pBC : B →ₗ[R] C)
    (iDE : D →ₗ[R] E) (pEF : E →ₗ[R] F)
    (iGH : G →ₗ[R] H) (pHI : H →ₗ[R] I)
    (iAD : A →ₗ[R] D) (iBE : B →ₗ[R] E) (iCF : C →ₗ[R] F)
    (pDG : D →ₗ[R] G) (pEH : E →ₗ[R] H) (pFI : F →ₗ[R] I)
    (hAB : Function.Injective iAB) (hBC : Function.Surjective pBC)
    (hexABC : Function.Exact iAB pBC)
    (hDE : Function.Injective iDE) (hEF : Function.Surjective pEF)
    (hexDEF : Function.Exact iDE pEF)
    (hGH : Function.Injective iGH) (hHI : Function.Surjective pHI)
    (hexGHI : Function.Exact iGH pHI)
    (hAD : Function.Injective iAD) (hDG : Function.Surjective pDG)
    (hexADG : Function.Exact iAD pDG)
    (hBE : Function.Injective iBE) (hEH : Function.Surjective pEH)
    (hexBEH : Function.Exact iBE pEH)
    (hCF : Function.Injective iCF) (hFI : Function.Surjective pFI)
    (hexCFI : Function.Exact iCF pFI)
    (commADEB : iDE.comp iAD = iBE.comp iAB)
    (commBEFC : pEF.comp iBE = iCF.comp pBC)
    (commDGEH : iGH.comp pDG = pEH.comp iDE)
    (commEHIF : pHI.comp pEH = pFI.comp pEF)
    (hA : IsFiniteLength R A) (hB : IsFiniteLength R B) (hC : IsFiniteLength R C)
    (hD : IsFiniteLength R D) (hE : IsFiniteLength R E) (hF : IsFiniteLength R F)
    (hG : IsFiniteLength R G) (hH : IsFiniteLength R H) (hI : IsFiniteLength R I) :
    (determinantExactSequenceMap iBE pEH hBE hEH hexBEH hB hE hH).comp
        (TensorProduct.map
          (determinantExactSequenceMap iAB pBC hAB hBC hexABC hA hB hC)
          (determinantExactSequenceMap iGH pHI hGH hHI hexGHI hG hH hI)) =
      (determinantExactSequenceMap iDE pEF hDE hEF hexDEF hD hE hF).comp
        ((TensorProduct.map
          (determinantExactSequenceMap iAD pDG hAD hDG hexADG hA hD hG)
          (determinantExactSequenceMap iCF pFI hCF hFI hexCFI hC hF hI)).comp
            (signedTensorInterchange (IsLocalRing.ResidueField R)
              (determinant R A) (determinant R C) (determinant R G) (determinant R I)
              (moduleLength R C) (moduleLength R G)))
```

**`Module.FiniteLength.determinantExactSequenceMap_comparison_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaVectorSpaces.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/GammaVectorSpaces.lean#L150). The attribute's comment: “gamma\_vector\_spaces”.

> For a short exact sequence of finite-dimensional vector spaces over the residue field of a
> local ring, under the canonical comparison of the determinant with the top exterior power, the
> determinant map sends the exterior products of two lists of vectors to the exterior product of
> the first list's image followed by arbitrary lifts of the second list.

```lean
public theorem determinantExactSequenceMap_comparison_apply
    {R : Type u} [CommRing R] [IsLocalRing R]
    {K : Type v} {L : Type w} {M : Type x}
    [AddCommGroup K] [Module R K] [Module (IsLocalRing.ResidueField R) K]
    [IsScalarTower R (IsLocalRing.ResidueField R) K]
    [AddCommGroup L] [Module R L] [Module (IsLocalRing.ResidueField R) L]
    [IsScalarTower R (IsLocalRing.ResidueField R) L]
    [AddCommGroup M] [Module R M] [Module (IsLocalRing.ResidueField R) M]
    [IsScalarTower R (IsLocalRing.ResidueField R) M]
    [Module.Finite (IsLocalRing.ResidueField R) K]
    [Module.Finite (IsLocalRing.ResidueField R) L]
    [Module.Finite (IsLocalRing.ResidueField R) M]
    (i : K →ₗ[IsLocalRing.ResidueField R] L)
    (p : L →ₗ[IsLocalRing.ResidueField R] M)
    (hi : Function.Injective i) (hp : Function.Surjective p) (hip : Function.Exact i p)
    (hK : IsFiniteLength R K) (hL : IsFiniteLength R L) (hM : IsFiniteLength R M) :
    ∃ hdim : Module.finrank (IsLocalRing.ResidueField R) L =
        Module.finrank (IsLocalRing.ResidueField R) K +
          Module.finrank (IsLocalRing.ResidueField R) M,
      ∀ (e : Fin (Module.finrank (IsLocalRing.ResidueField R) K) → K)
        (fbar : Fin (Module.finrank (IsLocalRing.ResidueField R) M) → M)
        (f : Fin (Module.finrank (IsLocalRing.ResidueField R) M) → L),
        (∀ a, p (f a) = fbar a) →
          (determinantExteriorPowerComparison R L).equiv
              (determinantExactSequenceMap (i.restrictScalars R) (p.restrictScalars R)
                hi hp hip hK hL hM
                ((determinantExteriorPowerComparison R K).equiv.symm
                    (exteriorPower.ιMulti (IsLocalRing.ResidueField R)
                      (Module.finrank (IsLocalRing.ResidueField R) K) e) ⊗ₜ
                  (determinantExteriorPowerComparison R M).equiv.symm
                    (exteriorPower.ιMulti (IsLocalRing.ResidueField R)
                      (Module.finrank (IsLocalRing.ResidueField R) M) fbar))) =
            exteriorPower.ιMulti (IsLocalRing.ResidueField R)
              (Module.finrank (IsLocalRing.ResidueField R) L)
              (fun a ↦ Fin.append (fun b ↦ i (e b)) f (Fin.cast hdim a))
```

## Tag 02PB, a lemma

[Tag 02PB](https://stacks.math.columbia.edu/tag/02PB) in the Stacks Project.

**`Module.FiniteLength.DeterminantTheory.existsUnique_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Characterization.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/Characterization.lean#L423).

> **Stacks Project, Tag 02PB.** The determinant functor of finite-length modules over a
> local ring, endowed with the maps `γ_{K → L → M}`, is characterized by its properties: every
> determinant theory, that is, every functor with maps `γ` whose restriction to modules
> annihilated by the maximal ideal is isomorphic to the usual determinant functor and which has
> properties (1), (2) and (3) of Tag 02PA, is isomorphic to the canonical one by a unique
> isomorphism compatible with all of this structure.

```lean
public theorem DeterminantTheory.existsUnique_comparison {R : Type u} [CommRing R]
    [IsLocalRing R] (D : DeterminantTheory.{u, v, w} R) :
    ∃! η : ∀ M : FiniteLengthModuleIso.{u, v} R,
      (D.toFunctor.obj M).of.obj ≃ₗ[IsLocalRing.ResidueField R]
        ((DeterminantTheory.canonical R).toFunctor.obj M).of.obj,
      D.IsComparison (DeterminantTheory.canonical R) η
```

## Tag 02PC, a lemma

[Tag 02PC](https://stacks.math.columbia.edu/tag/02PC) in the Stacks Project.

**`Module.FiniteLength.isFiniteLength_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean#L189). The attribute's comment: “finite length”.

> A module of finite length over `R` has finite length over `R₀`.

```lean
public theorem isFiniteLength_restrictScalars
    {R₀ : Type u} {R : Type v} [CommRing R₀] [IsLocalRing R₀]
    [CommRing R] [IsLocalRing R] [Algebra R₀ R]
    [IsLocalHom (algebraMap R₀ R)]
    (hκ : Function.Bijective (IsLocalRing.ResidueField.map (algebraMap R₀ R)))
    {M : Type w} [AddCommGroup M] [Module R₀ M] [Module R M]
    [IsScalarTower R₀ R M] (hM : IsFiniteLength R M) :
    IsFiniteLength R₀ M
```

**`Module.FiniteLength.moduleLength_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean#L203). The attribute's comment: “length”.

> The length is unchanged by restriction along a local homomorphism inducing an
> isomorphism of residue fields.

```lean
public theorem moduleLength_restrictScalars
    {R₀ : Type u} {R : Type v} [CommRing R₀] [IsLocalRing R₀]
    [CommRing R] [IsLocalRing R] [Algebra R₀ R]
    [IsLocalHom (algebraMap R₀ R)]
    (hκ : Function.Bijective (IsLocalRing.ResidueField.map (algebraMap R₀ R)))
    {M : Type w} [AddCommGroup M] [Module R₀ M] [Module R M]
    [IsScalarTower R₀ R M] (_hM : IsFiniteLength R M) :
    moduleLength R M = moduleLength R₀ M
```

**`Module.FiniteLength.determinantRestrictScalarsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean, line 541](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean#L541). The attribute's comment: “canonical isomorphism”.

> The canonical comparison of determinant spaces for a local ring map with unchanged
> residue field.

```lean
public noncomputable def determinantRestrictScalarsEquiv
    {R₀ : Type u} {R : Type v} [CommRing R₀] [IsLocalRing R₀]
    [CommRing R] [IsLocalRing R] [Algebra R₀ R]
    [IsLocalHom (algebraMap R₀ R)]
    (hκ : Function.Bijective (IsLocalRing.ResidueField.map (algebraMap R₀ R)))
    {M : Type w} [AddCommGroup M] [Module R₀ M] [Module R M]
    [IsScalarTower R₀ R M] (hM : IsFiniteLength R M) :
    determinant R M ≃ₛₗ[RingHomClass.toRingHom (RingEquiv.ofBijective
      (IsLocalRing.ResidueField.map (algebraMap R₀ R)) hκ).symm]
      determinant R₀ M
```

**`Module.FiniteLength.determinantRestrictScalarsEquiv_symbol`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean, line 556](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean#L556). The attribute's comment: “symbols”.

> The canonical comparison takes a determinant symbol to the symbol of the same
> sequence over the smaller local ring.

```lean
public theorem determinantRestrictScalarsEquiv_symbol
    {R₀ : Type u} {R : Type v} [CommRing R₀] [IsLocalRing R₀]
    [CommRing R] [IsLocalRing R] [Algebra R₀ R]
    [IsLocalHom (algebraMap R₀ R)]
    (hκ : Function.Bijective (IsLocalRing.ResidueField.map (algebraMap R₀ R)))
    {M : Type w} [AddCommGroup M] [Module R₀ M] [Module R M]
    [IsScalarTower R₀ R M] (hM : IsFiniteLength R M)
    (e : AdmissibleSequence R M) :
    determinantRestrictScalarsEquiv hκ hM (symbol e) =
    symbol ⟨fun i : Fin (moduleLength R₀ M) ↦
      e.1 (Fin.cast (moduleLength_restrictScalars hκ hM).symm i),
      admissibleSequence_restrictScalars hκ hM e⟩
```

**`Module.FiniteLength.determinantRestrictScalarsEquiv_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean, line 573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean#L573). The attribute's comment: “functoriality”.

> The canonical comparison commutes with symbol-preserving determinant maps induced
> by an isomorphism of modules.

```lean
public theorem determinantRestrictScalarsEquiv_natural
    {R₀ : Type u} {R : Type v} [CommRing R₀] [IsLocalRing R₀]
    [CommRing R] [IsLocalRing R] [Algebra R₀ R]
    [IsLocalHom (algebraMap R₀ R)]
    (hκ : Function.Bijective (IsLocalRing.ResidueField.map (algebraMap R₀ R)))
    {M : Type w} {N : Type x}
    [AddCommGroup M] [Module R₀ M] [Module R M] [IsScalarTower R₀ R M]
    [AddCommGroup N] [Module R₀ N] [Module R N] [IsScalarTower R₀ R N]
    (hM : IsFiniteLength R M) (hN : IsFiniteLength R N)
    (g : M ≃ₗ[R] N)
    (gR : determinant R M ≃ₗ[IsLocalRing.ResidueField R] determinant R N)
    (gR₀ : determinant R₀ M ≃ₗ[IsLocalRing.ResidueField R₀] determinant R₀ N)
    (hgR : ∀ e : AdmissibleSequence R M, ∃ e' : AdmissibleSequence R N,
      (∃ h : moduleLength R M = moduleLength R N,
        ∀ i, e'.1 (Fin.cast h i) = g (e.1 i)) ∧
      gR (symbol e) = symbol e')
    (hgR₀ : ∀ e : AdmissibleSequence R₀ M, ∃ e' : AdmissibleSequence R₀ N,
      (∃ h : moduleLength R₀ M = moduleLength R₀ N,
        ∀ i, e'.1 (Fin.cast h i) = g (e.1 i)) ∧
      gR₀ (symbol e) = symbol e')
    (z : determinant R M) :
    determinantRestrictScalarsEquiv hκ hN (gR z) =
      gR₀ (determinantRestrictScalarsEquiv hκ hM z)
```

**`Module.FiniteLength.determinantRestrictScalarsEquiv_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean, line 630](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/RestrictScalars.lean#L630). The attribute's comment: “exact sequences”.

> The determinant comparison respects the canonical determinant isomorphism of a
> short exact sequence.

```lean
public theorem determinantRestrictScalarsEquiv_exact
    {R₀ : Type u} {R : Type v} [CommRing R₀] [IsLocalRing R₀]
    [CommRing R] [IsLocalRing R] [Algebra R₀ R]
    [IsLocalHom (algebraMap R₀ R)]
    (hκ : Function.Bijective (IsLocalRing.ResidueField.map (algebraMap R₀ R)))
    {K : Type w} {L : Type x} {M : Type*}
    [AddCommGroup K] [Module R₀ K] [Module R K] [IsScalarTower R₀ R K]
    [AddCommGroup L] [Module R₀ L] [Module R L] [IsScalarTower R₀ R L]
    [AddCommGroup M] [Module R₀ M] [Module R M] [IsScalarTower R₀ R M]
    (i : K →ₗ[R] L) (p : L →ₗ[R] M)
    (hi : Function.Injective i) (hp : Function.Surjective p) (hip : Function.Exact i p)
    (hK : IsFiniteLength R K) (hL : IsFiniteLength R L) (hM : IsFiniteLength R M)
    (a : determinant R K) (b : determinant R M) :
    determinantRestrictScalarsEquiv hκ hL
        (determinantExactSequenceMap i p hi hp hip hK hL hM (a ⊗ₜ[IsLocalRing.ResidueField R] b)) =
      determinantExactSequenceMap (i.restrictScalars R₀) (p.restrictScalars R₀)
        hi hp hip (isFiniteLength_restrictScalars hκ hK)
        (isFiniteLength_restrictScalars hκ hL)
        (isFiniteLength_restrictScalars hκ hM)
        ((determinantRestrictScalarsEquiv hκ hK a) ⊗ₜ[IsLocalRing.ResidueField R₀]
          (determinantRestrictScalarsEquiv hκ hM b))
```

## Tag 02PD, a lemma

[Tag 02PD](https://stacks.math.columbia.edu/tag/02PD) in the Stacks Project.

**`Module.FiniteLength.determinantFunctor_map_unit_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/UnitScaling.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DeterminantsFiniteLength/UnitScaling.lean#L136).

> Multiplication by a unit on a finite-length module acts on its determinant
> by the corresponding power of the residue of that unit.

```lean
public theorem determinantFunctor_map_unit_smul
    {R : Type u} [CommRing R] [IsLocalRing R]
    (X : FiniteLengthModuleIso.{u, v} R) (a : Rˣ) (f : X ⟶ X)
    (hf : ∀ m : X.of.obj, f.iso.hom.hom.hom m = (a : R) • m)
    (x : determinant R X.of.obj) :
    (determinantFunctor R).mapLinearEquiv f x =
      (IsLocalRing.residue R a ^ moduleLength R X.of.obj) • x
```

## Tag 02PJ, a definition

[Tag 02PJ](https://stacks.math.columbia.edu/tag/02PJ) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Basic.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Basic.lean#L162).

> **Stacks Project, Tag 02PJ.** The determinant of an exact two-periodic complex on a
> finite-length module over a local ring.

```lean
noncomputable def periodicDeterminant
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
    (φ ψ : M →ₗ[R] M) (hφψ : Function.Exact φ ψ)
    (hψφ : Function.Exact ψ φ) (hM : IsFiniteLength R M) :
    (IsLocalRing.ResidueField R)ˣ
```

## Tag 02PK, a remark

[Tag 02PK](https://stacks.math.columbia.edu/tag/02PK) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant_symbol_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Formula.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Formula.lean#L79). The attribute's comment: “formula”.

> **Stacks Project, Tag 02PK.** For an exact two-periodic complex, the determinant symbol
> formed from an admissible sequence in the image of the first differential and lifts from the
> second image differs from the opposite symbol by the signed periodic determinant.

```lean
theorem periodicDeterminant_symbol_eq
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
    (φ ψ : M →ₗ[R] M)
    (hφψ : Function.Exact φ ψ) (hψφ : Function.Exact ψ φ)
    (hM : IsFiniteLength R M)
    (x : AdmissibleSequence R (LinearMap.range φ))
    (y : AdmissibleSequence R (LinearMap.range ψ))
    (hx : (IsLocalRing.ResidueField R) ∙ symbol x = ⊤)
    (hy : (IsLocalRing.ResidueField R) ∙ symbol y = ⊤)
    (xLift : Fin (moduleLength R (LinearMap.range φ)) → M)
    (yLift : Fin (moduleLength R (LinearMap.range ψ)) → M)
    (hxLift : ∀ i, φ (xLift i) = (x.1 i : M))
    (hyLift : ∀ j, ψ (yLift j) = (y.1 j : M)) :
    ∃ hleftLength : moduleLength R M =
        moduleLength R (LinearMap.range φ) + moduleLength R (LinearMap.range ψ),
      ∃ hrightLength : moduleLength R M =
          moduleLength R (LinearMap.range ψ) + moduleLength R (LinearMap.range φ),
        ∃ hleft : IsAdmissibleSequence (R := R)
            (fun i ↦ Fin.append (fun j ↦ (x.1 j : M)) yLift (Fin.cast hleftLength i)),
          ∃ hright : IsAdmissibleSequence (R := R)
              (fun i ↦ Fin.append (fun j ↦ (y.1 j : M)) xLift
                (Fin.cast hrightLength i)),
            symbol ⟨fun i ↦ Fin.append (fun j ↦ (x.1 j : M)) yLift
                (Fin.cast hleftLength i), hleft⟩ =
              (((-1 : IsLocalRing.ResidueField R) ^
                (moduleLength R (LinearMap.range φ) *
                  moduleLength R (LinearMap.range ψ))) *
                (periodicDeterminant φ ψ hφψ hψφ hM : IsLocalRing.ResidueField R)) •
                symbol ⟨fun i ↦ Fin.append (fun j ↦ (y.1 j : M)) xLift
                (Fin.cast hrightLength i), hright⟩
```

**`AlgebraicGeometry.eq_periodicDeterminant_of_symbol_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Formula.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Formula.lean#L185). The attribute's comment: “uniqueness”.

> **Stacks Project, Tag 02PK.** The signed comparison of symbols of generating admissible
> sequences uniquely determines the determinant of an exact two-periodic complex.

```lean
theorem eq_periodicDeterminant_of_symbol_eq
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
    (φ ψ : M →ₗ[R] M)
    (hφψ : Function.Exact φ ψ) (hψφ : Function.Exact ψ φ)
    (hM : IsFiniteLength R M)
    (x : AdmissibleSequence R (LinearMap.range φ))
    (y : AdmissibleSequence R (LinearMap.range ψ))
    (hx : (IsLocalRing.ResidueField R) ∙ symbol x = ⊤)
    (hy : (IsLocalRing.ResidueField R) ∙ symbol y = ⊤)
    (xLift : Fin (moduleLength R (LinearMap.range φ)) → M)
    (yLift : Fin (moduleLength R (LinearMap.range ψ)) → M)
    (hxLift : ∀ i, φ (xLift i) = (x.1 i : M))
    (hyLift : ∀ j, ψ (yLift j) = (y.1 j : M))
    (hleftLength : moduleLength R M =
      moduleLength R (LinearMap.range φ) + moduleLength R (LinearMap.range ψ))
    (hrightLength : moduleLength R M =
      moduleLength R (LinearMap.range ψ) + moduleLength R (LinearMap.range φ))
    (hleft : IsAdmissibleSequence (R := R)
      (fun i ↦ Fin.append (fun j ↦ (x.1 j : M)) yLift (Fin.cast hleftLength i)))
    (hright : IsAdmissibleSequence (R := R)
      (fun i ↦ Fin.append (fun j ↦ (y.1 j : M)) xLift (Fin.cast hrightLength i)))
    (d : (IsLocalRing.ResidueField R)ˣ)
    (hd : symbol ⟨fun i ↦ Fin.append (fun j ↦ (x.1 j : M)) yLift
        (Fin.cast hleftLength i), hleft⟩ =
      (((-1 : IsLocalRing.ResidueField R) ^
        (moduleLength R (LinearMap.range φ) *
          moduleLength R (LinearMap.range ψ))) *
        (d : IsLocalRing.ResidueField R)) •
        symbol ⟨fun i ↦ Fin.append (fun j ↦ (y.1 j : M)) xLift
          (Fin.cast hrightLength i), hright⟩) :
    d = periodicDeterminant φ ψ hφψ hψφ hM
```

## Tag 02PL, a lemma

[Tag 02PL](https://stacks.math.columbia.edu/tag/02PL) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant_mul_swap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Swap.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Swap.lean#L39).

> **Stacks Project, Tag 02PL.** Interchanging the two maps of an exact two-periodic complex
> inverts its periodic determinant.

```lean
theorem periodicDeterminant_mul_swap
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
    (φ ψ : M →ₗ[R] M) (hφψ : Function.Exact φ ψ)
    (hψφ : Function.Exact ψ φ) (hM : IsFiniteLength R M) :
    periodicDeterminant φ ψ hφψ hψφ hM *
        periodicDeterminant ψ φ hψφ hφψ hM = 1
```

## Tag 02PM, a lemma

[Tag 02PM](https://stacks.math.columbia.edu/tag/02PM) in the Stacks Project.

**`Module.length_eq_twice_image_length`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Length.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Length.lean#L37). The attribute's comment: “length\_eq\_twice\_image\_length”.

> **Stacks Project, Tag 02PM.** The length of an exact one-differential periodic complex is
> twice the length of the image of its differential.

```lean
lemma length_eq_twice_image_length (φ : M →ₗ[R] M) (hφ : Function.Exact φ φ) :
    Module.length R M = 2 * Module.length R (LinearMap.range φ)
```

**`AlgebraicGeometry.periodicDeterminant_self_eq_negOne_pow_range_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Sign.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Sign.lean#L64). The attribute's comment: “periodic\_determinant\_sign”.

> **Stacks Project, Tag 02PM.** The determinant of an exact one-differential periodic
> complex is the sign of the length of the image of its differential.

```lean
theorem periodicDeterminant_self_eq_negOne_pow_range_length
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
    (φ : M →ₗ[R] M) (hφ : Function.Exact φ φ) (hM : IsFiniteLength R M) :
    periodicDeterminant φ φ hφ hφ hM =
      (-1 : (IsLocalRing.ResidueField R)ˣ) ^ moduleLength R (LinearMap.range φ)
```

**`AlgebraicGeometry.periodicDeterminant_self_eq_negOne_pow_half_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Sign.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Sign.lean#L87). The attribute's comment: “periodic\_determinant\_sign”.

> **Stacks Project, Tag 02PM.** The same determinant is the sign of half the length of the
> underlying module.

```lean
theorem periodicDeterminant_self_eq_negOne_pow_half_length
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M]
    (φ : M →ₗ[R] M) (hφ : Function.Exact φ φ) (hM : IsFiniteLength R M) :
    periodicDeterminant φ φ hφ hφ hM =
      (-1 : (IsLocalRing.ResidueField R)ˣ) ^ (moduleLength R M / 2)
```

## Tag 02PN, a lemma

[Tag 02PN](https://stacks.math.columbia.edu/tag/02PN) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant_equiv_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Automorphisms.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Automorphisms.lean#L232). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 02PN, part (1).** The periodic determinant of an automorphism and
> zero is the determinant of the automorphism.

```lean
theorem periodicDeterminant_equiv_zero
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] (e : M ≃ₗ[R] M)
    (hM : IsFiniteLength R M) :
    periodicDeterminant (e : M →ₗ[R] M) 0
      (by rw [LinearMap.exact_iff]; simp [LinearMap.range_eq_top.mpr e.surjective])
      (by rw [LinearMap.exact_iff]; simp [LinearMap.ker_eq_bot.mpr e.injective])
      hM = determinantAutomorphism e hM
```

**`AlgebraicGeometry.periodicDeterminant_zero_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Automorphisms.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Automorphisms.lean#L290). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 02PN, part (2).** The periodic determinant of zero and an
> automorphism is the inverse of its determinant.

```lean
theorem periodicDeterminant_zero_equiv
    {R : Type u} {M : Type v} [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] (e : M ≃ₗ[R] M)
    (hM : IsFiniteLength R M) :
    periodicDeterminant 0 (e : M →ₗ[R] M)
      (by rw [LinearMap.exact_iff]; simp [LinearMap.ker_eq_bot.mpr e.injective])
      (by rw [LinearMap.exact_iff]; simp [LinearMap.range_eq_top.mpr e.surjective])
      hM = (determinantAutomorphism e hM)⁻¹
```

## Tag 02PO, a lemma

[Tag 02PO](https://stacks.math.columbia.edu/tag/02PO) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant_short_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/ShortExact.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/ShortExact.lean#L201).

> **Stacks Project, Tag 02PO.** The periodic determinant is multiplicative in a short exact
> sequence of exact two-periodic complexes of finite-length modules.

```lean
theorem periodicDeterminant_short_exact
    {R : Type u} [CommRing R] [IsLocalRing R]
    {M₁ : Type v₁} {M₂ : Type v₂} {M₃ : Type v₃}
    [AddCommGroup M₁] [Module R M₁]
    [AddCommGroup M₂] [Module R M₂]
    [AddCommGroup M₃] [Module R M₃]
    (φ₁ ψ₁ : M₁ →ₗ[R] M₁) (φ₂ ψ₂ : M₂ →ₗ[R] M₂)
    (φ₃ ψ₃ : M₃ →ₗ[R] M₃)
    (i : M₁ →ₗ[R] M₂) (p : M₂ →ₗ[R] M₃)
    (hi : Function.Injective i) (hp : Function.Surjective p)
    (hip : Function.Exact i p)
    (hφi : φ₂.comp i = i.comp φ₁)
    (hψi : ψ₂.comp i = i.comp ψ₁)
    (hφp : φ₃.comp p = p.comp φ₂)
    (hψp : ψ₃.comp p = p.comp ψ₂)
    (hφψ₁ : Function.Exact φ₁ ψ₁) (hψφ₁ : Function.Exact ψ₁ φ₁)
    (hφψ₂ : Function.Exact φ₂ ψ₂) (hψφ₂ : Function.Exact ψ₂ φ₂)
    (hφψ₃ : Function.Exact φ₃ ψ₃) (hψφ₃ : Function.Exact ψ₃ φ₃)
    (hM₁ : IsFiniteLength R M₁) (hM₂ : IsFiniteLength R M₂)
    (hM₃ : IsFiniteLength R M₃) :
    periodicDeterminant φ₂ ψ₂ hφψ₂ hψφ₂ hM₂ =
      periodicDeterminant φ₁ ψ₁ hφψ₁ hψφ₁ hM₁ *
        periodicDeterminant φ₃ ψ₃ hφψ₃ hψφ₃ hM₃
```

## Tag 02PP, an example

[Tag 02PP](https://stacks.math.columbia.edu/tag/02PP) in the Stacks Project.

**`DualNumber.span_symbol_dualNumberSequence_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean#L332). The attribute's comment: “dual\_generator”.

> **Stacks Project, Tag 02PP.** The symbol `[ε, 1]` of the admissible sequence `(ε, 1)` of the
> dual numbers over themselves generates their determinant over the residue field.

```lean
theorem span_symbol_dualNumberSequence_eq_top (k : Type u) [Field k] :
    (IsLocalRing.ResidueField (DualNumber k)) ∙ symbol (dualNumberSequence k) = ⊤
```

**`DualNumber.periodicGamma_unitMulT_dualRangeSequence_first`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean#L343). The attribute's comment: “dual\_gamma\_values”.

> **Stacks Project, Tag 02PP.** For the short exact sequence of the dual numbers given by the
> image of multiplication by `v ε` and multiplication by `u ε`, the determinant map sends the tensor
> of the two classes of `ε` to `u⁻¹ [ε, 1]`.

```lean
theorem periodicGamma_unitMulT_dualRangeSequence_first (k : Type u) [Field k] (u v : kˣ)
    (hvu : Function.Exact (unitMulT k v) (unitMulT k u))
    (hM : IsFiniteLength (DualNumber k) (DualNumber k)) :
    periodicGamma (unitMulT k u) (unitMulT k v) hvu hM
      (symbol (dualRangeSequence k v) ⊗ₜ[IsLocalRing.ResidueField (DualNumber k)]
        symbol (dualRangeSequence k u)) =
      algebraMap k (IsLocalRing.ResidueField (DualNumber k)) ((u⁻¹ : kˣ) : k) •
        symbol (dualNumberSequence k)
```

**`DualNumber.periodicGamma_unitMulT_dualRangeSequence_second`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean#L360). The attribute's comment: “dual\_gamma\_values”.

> **Stacks Project, Tag 02PP.** For the short exact sequence of the dual numbers given by the
> image of multiplication by `u ε` and multiplication by `v ε`, the determinant map sends the tensor
> of the two classes of `ε` to `v⁻¹ [ε, 1]`.

```lean
theorem periodicGamma_unitMulT_dualRangeSequence_second (k : Type u) [Field k] (u v : kˣ)
    (huv : Function.Exact (unitMulT k u) (unitMulT k v))
    (hM : IsFiniteLength (DualNumber k) (DualNumber k)) :
    periodicGamma (unitMulT k v) (unitMulT k u) huv hM
      (symbol (dualRangeSequence k u) ⊗ₜ[IsLocalRing.ResidueField (DualNumber k)]
        symbol (dualRangeSequence k v)) =
      algebraMap k (IsLocalRing.ResidueField (DualNumber k)) ((v⁻¹ : kˣ) : k) •
        symbol (dualNumberSequence k)
```

**`DualNumber.periodicDeterminant_unitMulT`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberDeterminant.lean#L373). The attribute's comment: “dual\_periodic\_determinant”.

> **Stacks Project, Tag 02PP.** The periodic determinant of multiplication by `u ε` and
> `v ε` on the dual numbers is `-u / v`.

```lean
theorem periodicDeterminant_unitMulT (k : Type u) [Field k] (u v : kˣ) :
    ∃ (hφψ : Function.Exact (unitMulT k u) (unitMulT k v))
      (hψφ : Function.Exact (unitMulT k v) (unitMulT k u))
      (hM : IsFiniteLength (DualNumber k) (DualNumber k)),
      periodicDeterminant (unitMulT k u) (unitMulT k v) hφψ hψφ hM =
        Units.map (algebraMap k (IsLocalRing.ResidueField (DualNumber k))) (-u / v)
```

**`DualNumber.range_unitMulT`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberIdeals.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberIdeals.lean#L52). The attribute's comment: “dual\_images\_kernels”.

> The image of multiplication by a unit multiple of `ε` is the ideal generated by `ε`.

```lean
theorem range_unitMulT (k : Type u) [Field k] (u : kˣ) :
    LinearMap.range (unitMulT k u) = Ideal.span {DualNumber.eps}
```

**`DualNumber.ker_unitMulT`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberIdeals.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/DualNumberIdeals.lean#L65). The attribute's comment: “dual\_images\_kernels”.

> The kernel of multiplication by a unit multiple of `ε` is the ideal generated by `ε`.

```lean
theorem ker_unitMulT (k : Type u) [Field k] (u : kˣ) :
    LinearMap.ker (unitMulT k u) = Ideal.span {DualNumber.eps}
```

## Tag 02PQ, an example

[Tag 02PQ](https://stacks.math.columbia.edu/tag/02PQ) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant_padicInt_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/PadicIntExample.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/PadicIntExample.lean#L274). The attribute's comment: “the determinant of the p-adic periodic complex”.

> **Stacks Project, Tag 02PQ.** Let `p` be a prime, let `a + b = l`, and let `u` and `v` be
> units of `ℤ_[p]`. Multiplication by `p ^ b * u` and by `p ^ a * v` on `ℤ_[p] / (p ^ l)` is an
> exact two-periodic complex of finite length, and its periodic determinant is
> `(-1) ^ (a * b) * u ^ a / v ^ b` in the residue field of `ℤ_[p]`.

```lean
theorem periodicDeterminant_padicInt_quotient (a b l : ℕ) (hl : a + b = l) (u v : ℤ_[p]ˣ) :
    ∃ (hφψ : Function.Exact
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ b * (u : ℤ_[p])))
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ a * (v : ℤ_[p]))))
      (hψφ : Function.Exact
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ a * (v : ℤ_[p])))
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ b * (u : ℤ_[p]))))
      (hM : IsFiniteLength ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})),
      periodicDeterminant
          (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
            ((p : ℤ_[p]) ^ b * (u : ℤ_[p])))
          (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
            ((p : ℤ_[p]) ^ a * (v : ℤ_[p]))) hφψ hψφ hM =
        (-1) ^ (a * b) *
          Units.map (IsLocalRing.residue ℤ_[p]).toMonoidHom (u ^ a / v ^ b)
```

**`AlgebraicGeometry.periodicDeterminant_padicInt_quotient_toZMod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/PadicIntExample.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/PadicIntExample.lean#L307). The attribute's comment: “the determinant mod p in order-of-vanishing form”.

> **Stacks Project, Tag 02PQ.** The same determinant read in `𝔽_p = ZMod p` and written with
> the orders of vanishing of the two differentials `α = p ^ b * u` and `β = p ^ a * v`: it is
> `(-1) ^ (ord α * ord β)` times the reduction mod `p` of the unit `α ^ (ord β) / β ^ (ord α)`,
> which is exhibited together with its defining identity in `ℚ_[p]`.

```lean
theorem periodicDeterminant_padicInt_quotient_toZMod (a b l : ℕ) (hl : a + b = l)
    (u v : ℤ_[p]ˣ) :
    ∃ (hφψ : Function.Exact
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ b * (u : ℤ_[p])))
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ a * (v : ℤ_[p]))))
      (hψφ : Function.Exact
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ a * (v : ℤ_[p])))
        (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
          ((p : ℤ_[p]) ^ b * (u : ℤ_[p]))))
      (hM : IsFiniteLength ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})) (w : ℤ_[p]ˣ),
      algebraMap ℤ_[p] ℚ_[p] (w : ℤ_[p]) =
          algebraMap ℤ_[p] ℚ_[p] ((p : ℤ_[p]) ^ b * (u : ℤ_[p])) ^
              ordInt ℤ_[p] (algebraMap ℤ_[p] ℚ_[p] ((p : ℤ_[p]) ^ a * (v : ℤ_[p])))
                (padicInt_algebraMap_pow_mul_unit_ne_zero p a v) /
            algebraMap ℤ_[p] ℚ_[p] ((p : ℤ_[p]) ^ a * (v : ℤ_[p])) ^
              ordInt ℤ_[p] (algebraMap ℤ_[p] ℚ_[p] ((p : ℤ_[p]) ^ b * (u : ℤ_[p])))
                (padicInt_algebraMap_pow_mul_unit_ne_zero p b u) ∧
        PadicInt.residueField
            ((periodicDeterminant
              (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
                ((p : ℤ_[p]) ^ b * (u : ℤ_[p])))
              (LinearMap.lsmul ℤ_[p] (ℤ_[p] ⧸ Ideal.span {(p : ℤ_[p]) ^ l})
                ((p : ℤ_[p]) ^ a * (v : ℤ_[p]))) hφψ hψφ hM :
                IsLocalRing.ResidueField ℤ_[p])) =
          (-1) ^ (ordInt ℤ_[p] (algebraMap ℤ_[p] ℚ_[p] ((p : ℤ_[p]) ^ b * (u : ℤ_[p])))
                (padicInt_algebraMap_pow_mul_unit_ne_zero p b u) *
              ordInt ℤ_[p] (algebraMap ℤ_[p] ℚ_[p] ((p : ℤ_[p]) ^ a * (v : ℤ_[p])))
                (padicInt_algebraMap_pow_mul_unit_ne_zero p a v)) *
            PadicInt.toZMod (w : ℤ_[p])
```

## Tag 02PS, an example

[Tag 02PS](https://stacks.math.columbia.edu/tag/02PS) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant_upperBlockEndomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Blocks.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Blocks.lean#L181).

> **Stacks Project, Tag 02PS.** The periodic determinant of two invertible upper-right
> blocks is the signed ratio of their ordinary matrix determinants.

```lean
theorem periodicDeterminant_upperBlockEndomorphism
    {k : Type u} [Field k] (a : ℕ)
    (U V : Matrix (Fin a) (Fin a) k) (hU : IsUnit U) (hV : IsUnit V) :
    ∃ (hUV : Function.Exact (upperBlockEndomorphism U) (upperBlockEndomorphism V))
      (hVU : Function.Exact (upperBlockEndomorphism V) (upperBlockEndomorphism U))
      (hM : IsFiniteLength k ((Fin a → k) × (Fin a → k))),
      (periodicDeterminant (upperBlockEndomorphism U) (upperBlockEndomorphism V)
        hUV hVU hM : IsLocalRing.ResidueField k) =
        (-1 : IsLocalRing.ResidueField k) ^ a *
          IsLocalRing.residue k U.det / IsLocalRing.residue k V.det
```

## Tag 02PT, an example

[Tag 02PT](https://stacks.math.columbia.edu/tag/02PT) in the Stacks Project.

**`AlgebraicGeometry.periodicDeterminant_crossPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/BlockPairExample.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/BlockPairExample.lean#L152).

> **Stacks Project, Tag 02PT.** For nonzero `u₁, u₂, v₁, v₂` in a field `k`, the two
> endomorphisms of `k^{⊕ 4}` with single nonzero matrix entries `u₁, u₂` and `v₂, v₁` form an
> exact two-periodic complex whose periodic determinant is `-u₁u₂/(v₁v₂)`.

```lean
theorem periodicDeterminant_crossPair {k : Type u} [Field k] (u₁ u₂ v₁ v₂ : kˣ) :
    ∃ (hφψ : Function.Exact (crossPairFirst (u₁ : k) u₂) (crossPairSecond (v₁ : k) v₂))
      (hψφ : Function.Exact (crossPairSecond (v₁ : k) v₂) (crossPairFirst (u₁ : k) u₂))
      (hM : IsFiniteLength k (Fin 4 → k)),
      (periodicDeterminant (crossPairFirst (u₁ : k) u₂) (crossPairSecond (v₁ : k) v₂)
        hφψ hψφ hM : IsLocalRing.ResidueField k) =
        -(IsLocalRing.residue k ((u₁ : k) * u₂) / IsLocalRing.residue k ((v₁ : k) * v₂))
```

## Tag 02PU, a lemma

[Tag 02PU](https://stacks.math.columbia.edu/tag/02PU) in the Stacks Project.

**`AlgebraicGeometry.exact_alpha_betaGamma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean#L129). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 02PU.** Exactness of `α` followed by `βγ` on the original
> module.

```lean
theorem exact_alpha_betaGamma (α β γ : M →ₗ[R] M)
    (h : ComplementaryImagesKernels α β γ) :
    Function.Exact α (β ∘ₗ γ)
```

**`AlgebraicGeometry.exact_betaGamma_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean#L137). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 02PU.** Exactness of `βγ` followed by `α` on the original
> module.

```lean
theorem exact_betaGamma_alpha (α β γ : M →ₗ[R] M)
    (h : ComplementaryImagesKernels α β γ) :
    Function.Exact (β ∘ₗ γ) α
```

**`AlgebraicGeometry.exact_alpha_beta_onGammaRange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean#L168). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 02PU.** Exactness of `α` followed by `β` on the image of `γ`.

```lean
theorem exact_alpha_beta_onGammaRange (α β γ : M →ₗ[R] M)
    (h : ComplementaryImagesKernels α β γ) :
    Function.Exact (alphaOnGammaRange α β γ h) (betaOnGammaRange α β γ h)
```

**`AlgebraicGeometry.exact_beta_alpha_onGammaRange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean#L176). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 02PU.** Exactness of `β` followed by `α` on the image of `γ`.

```lean
theorem exact_beta_alpha_onGammaRange (α β γ : M →ₗ[R] M)
    (h : ComplementaryImagesKernels α β γ) :
    Function.Exact (betaOnGammaRange α β γ h) (alphaOnGammaRange α β γ h)
```

**`AlgebraicGeometry.exact_alpha_gamma_onKerBetaQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean#L210). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 02PU.** Exactness of `α` followed by `γ` on the quotient by the
> kernel of `β`.

```lean
theorem exact_alpha_gamma_onKerBetaQuotient (α β γ : M →ₗ[R] M)
    (h : ComplementaryImagesKernels α β γ) :
    Function.Exact (alphaOnKerBetaQuotient α β γ h)
      (gammaOnKerBetaQuotient α β γ h)
```

**`AlgebraicGeometry.exact_gamma_alpha_onKerBetaQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean#L224). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 02PU.** Exactness of `γ` followed by `α` on the quotient by the
> kernel of `β`.

```lean
theorem exact_gamma_alpha_onKerBetaQuotient (α β γ : M →ₗ[R] M)
    (h : ComplementaryImagesKernels α β γ) :
    Function.Exact (gammaOnKerBetaQuotient α β γ h)
      (alphaOnKerBetaQuotient α β γ h)
```

**`AlgebraicGeometry.periodicDeterminant_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Multiplicativity.lean#L615). The attribute's comment: “part (4)”.

> **Stacks Project, Tag 02PU.** The determinant of `(M, α, βγ)` is the product of the
> determinants on the image of `γ` and the quotient by the kernel of `β`.

```lean
theorem periodicDeterminant_mul (α β γ : M →ₗ[R] M)
    (hM : IsFiniteLength R M) (h : ComplementaryImagesKernels α β γ) :
    periodicDeterminant α (β ∘ₗ γ)
        (exact_alpha_betaGamma α β γ h) (exact_betaGamma_alpha α β γ h) hM =
      periodicDeterminant (alphaOnGammaRange α β γ h)
          (betaOnGammaRange α β γ h)
          (exact_alpha_beta_onGammaRange α β γ h)
          (exact_beta_alpha_onGammaRange α β γ h)
          (hM.of_injective (LinearMap.range γ).subtype_injective) *
        periodicDeterminant (alphaOnKerBetaQuotient α β γ h)
          (gammaOnKerBetaQuotient α β γ h)
          (exact_alpha_gamma_onKerBetaQuotient α β γ h)
          (exact_gamma_alpha_onKerBetaQuotient α β γ h)
          (hM.of_surjective (Submodule.mkQ_surjective (LinearMap.ker β)))
```

## Tag 02PV, a lemma

[Tag 02PV](https://stacks.math.columbia.edu/tag/02PV) in the Stacks Project.

**`AlgebraicGeometry.connectingEquivs`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Comparison/ConnectingEquivs.lean, line 544](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Comparison/ConnectingEquivs.lean#L544). The attribute's comment: “connecting isomorphisms”.

> **Stacks Project, Tag 02PV.** The two connecting isomorphisms associated to an exact
> morphism of two-periodic complexes. The first uses `φ'` then `ψ`, and the second uses `ψ'`
> then `φ`.

```lean
noncomputable def connectingEquivs
    {R : Type u} {M : Type v} {M' : Type w}
    [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [AddCommGroup M'] [Module R M']
    (φ ψ : M →ₗ[R] M) (φ' ψ' : M' →ₗ[R] M') (α : M →ₗ[R] M')
    (hφψ : Function.Exact φ ψ) (hψφ : Function.Exact ψ φ)
    (hφ'ψ' : Function.Exact φ' ψ') (hψ'φ' : Function.Exact ψ' φ')
    (hαφ : α.comp φ = φ'.comp α) (hαψ : α.comp ψ = ψ'.comp α)
    (hKφ : LinearMap.ker α ≤ LinearMap.ker φ)
    (hKψ : LinearMap.ker α ≤ LinearMap.ker ψ)
    (hQφ : LinearMap.range φ' ≤ LinearMap.range α)
    (hQψ : LinearMap.range ψ' ≤ LinearMap.range α) :
    {e : ((M' ⧸ LinearMap.range α) ≃ₗ[R] LinearMap.ker α) ×
        ((M' ⧸ LinearMap.range α) ≃ₗ[R] LinearMap.ker α) //
      (∀ (x' : M') (y : M), α y = φ' x' →
        ((e.1 (Submodule.Quotient.mk x') : LinearMap.ker α) : M) = ψ y) ∧
      (∀ (x' : M') (y : M), α y = ψ' x' →
        ((e.2 (Submodule.Quotient.mk x') : LinearMap.ker α) : M) = φ y)}
```

**`AlgebraicGeometry.periodicDeterminant_eq_det_connecting_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Comparison/Formula.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Comparison/Formula.lean#L92). The attribute's comment: “comparison formula”.

> **Stacks Project, Tag 02PV.** The change of periodic determinant is the determinant of the
> second connecting isomorphism followed by the inverse of the first.

```lean
theorem periodicDeterminant_eq_det_connecting_mul
    {R : Type u} {M : Type v} {M' : Type w}
    [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [AddCommGroup M'] [Module R M']
    (φ ψ : M →ₗ[R] M) (φ' ψ' : M' →ₗ[R] M') (α : M →ₗ[R] M')
    (hM : IsFiniteLength R M) (hM' : IsFiniteLength R M')
    (hφψ : Function.Exact φ ψ) (hψφ : Function.Exact ψ φ)
    (hφ'ψ' : Function.Exact φ' ψ') (hψ'φ' : Function.Exact ψ' φ')
    (hαφ : α.comp φ = φ'.comp α) (hαψ : α.comp ψ = ψ'.comp α)
    (hKφ : LinearMap.ker α ≤ LinearMap.ker φ)
    (hKψ : LinearMap.ker α ≤ LinearMap.ker ψ)
    (hQφ : LinearMap.range φ' ≤ LinearMap.range α)
    (hQψ : LinearMap.range ψ' ≤ LinearMap.range α) :
    periodicDeterminant φ ψ hφψ hψφ hM =
      determinantAutomorphism
        ((connectingEquivs φ ψ φ' ψ' α hφψ hψφ hφ'ψ' hψ'φ'
          hαφ hαψ hKφ hKψ hQφ hQψ).1.2.trans
          (connectingEquivs φ ψ φ' ψ' α hφψ hψφ hφ'ψ' hψ'φ'
            hαφ hαψ hKφ hKψ hQφ hQψ).1.1.symm)
        (hM'.of_surjective (Submodule.mkQ_surjective (LinearMap.range α))) *
      periodicDeterminant φ' ψ' hφ'ψ' hψ'φ' hM'
```

**`AlgebraicGeometry.periodicDeterminant_eq_of_connecting_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Comparison/Invariance.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicComplexesDeterminants/Comparison/Invariance.lean#L66). The attribute's comment: “equal connecting isomorphisms”.

> **Stacks Project, Tag 02PV.** Equal connecting isomorphisms give equal periodic
> determinants.

```lean
theorem periodicDeterminant_eq_of_connecting_eq
    {R : Type u} {M : Type v} {M' : Type w}
    [CommRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [AddCommGroup M'] [Module R M']
    (φ ψ : M →ₗ[R] M) (φ' ψ' : M' →ₗ[R] M') (α : M →ₗ[R] M')
    (hM : IsFiniteLength R M) (hM' : IsFiniteLength R M')
    (hφψ : Function.Exact φ ψ) (hψφ : Function.Exact ψ φ)
    (hφ'ψ' : Function.Exact φ' ψ') (hψ'φ' : Function.Exact ψ' φ')
    (hαφ : α.comp φ = φ'.comp α) (hαψ : α.comp ψ = ψ'.comp α)
    (hKφ : LinearMap.ker α ≤ LinearMap.ker φ)
    (hKψ : LinearMap.ker α ≤ LinearMap.ker ψ)
    (hQφ : LinearMap.range φ' ≤ LinearMap.range α)
    (hQψ : LinearMap.range ψ' ≤ LinearMap.range α)
    (heq : (connectingEquivs φ ψ φ' ψ' α hφψ hψφ hφ'ψ' hψ'φ'
      hαφ hαψ hKφ hKψ hQφ hQψ).1.1 =
      (connectingEquivs φ ψ φ' ψ' α hφψ hψφ hφ'ψ' hψ'φ'
        hαφ hαψ hKφ hKψ hQφ hQψ).1.2) :
    periodicDeterminant φ ψ hφψ hψφ hM =
      periodicDeterminant φ' ψ' hφ'ψ' hψ'φ' hM'
```

## Tag 02PX, a lemma

[Tag 02PX](https://stacks.math.columbia.edu/tag/02PX) in the Stacks Project.

**`AlgebraicGeometry.exact_periodicQuotient_phi_psi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/PeriodicExactness.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/PeriodicExactness.lean#L88). The attribute's comment: “periodic\_exactness”.

> On the quotient by the common composite image, the map induced by `φ` is exact before
> the map induced by `ψ`.

```lean
theorem exact_periodicQuotient_phi_psi (φ ψ : M →ₗ[R] M)
    (hψ : Function.Injective ψ)
    (hcomm : LinearMap.range (φ ∘ₗ ψ) = LinearMap.range (ψ ∘ₗ φ)) :
    Function.Exact (periodicQuotientPhi φ ψ hcomm) (periodicQuotientPsi φ ψ hcomm)
```

**`AlgebraicGeometry.exact_periodicQuotient_psi_phi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/PeriodicExactness.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/PeriodicExactness.lean#L99). The attribute's comment: “periodic\_exactness”.

> On the quotient by the common composite image, the map induced by `ψ` is exact before
> the map induced by `φ`.

```lean
theorem exact_periodicQuotient_psi_phi (φ ψ : M →ₗ[R] M)
    (hφ : Function.Injective φ)
    (hcomm : LinearMap.range (φ ∘ₗ ψ) = LinearMap.range (ψ ∘ₗ φ)) :
    Function.Exact (periodicQuotientPsi φ ψ hcomm) (periodicQuotientPhi φ ψ hcomm)
```

**`Module.isFiniteLength_quotient_range_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/FiniteLength.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/FiniteLength.lean#L91). The attribute's comment: “finite\_length”.

> The quotient of a finite module of support dimension one by an injective endomorphism has
> finite length.

```lean
theorem isFiniteLength_quotient_range_of_injective
    (f : M →ₗ[A] M) (hf : Function.Injective f)
    (hdim : Module.supportDim A M = 1) :
    IsFiniteLength A (M ⧸ LinearMap.range f)
```

## Tag 02PY, a lemma

[Tag 02PY](https://stacks.math.columbia.edu/tag/02PY) in the Stacks Project.

**`AlgebraicGeometry.isFiniteLength_quotient_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean#L56). The attribute's comment: “part (1): finite length”.

> **Stacks Project, Tag 02PY.** The quotient by `abM` has finite length.

```lean
theorem isFiniteLength_quotient_mul [IsNoetherianRing A] [IsLocalRing A]
    [Module.Finite A M] (a b : A)
    (ha : IsSMulRegular M a) (hb : IsSMulRegular M b)
    (hdim : Module.supportDim A M = 1) :
    IsFiniteLength A
    (M ⧸ LinearMap.range
        ((LinearMap.lsmul A M a) ∘ₗ (LinearMap.lsmul A M b)))
```

**`AlgebraicGeometry.exact_mul_left_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean#L68). The attribute's comment: “part (1): exactness at b”.

> **Stacks Project, Tag 02PY.** Exactness at the differential induced by multiplication
> by `b`.

```lean
theorem exact_mul_left_right (a b : A)
    (hb : IsSMulRegular M b) :
    Function.Exact
      (periodicQuotientPhi
        (LinearMap.lsmul A M a) (LinearMap.lsmul A M b)
        (range_lsmul_comp_comm a b))
      (periodicQuotientPsi
        (LinearMap.lsmul A M a) (LinearMap.lsmul A M b)
        (range_lsmul_comp_comm a b))
```

**`AlgebraicGeometry.exact_mul_right_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean#L83). The attribute's comment: “part (1): exactness at a”.

> **Stacks Project, Tag 02PY.** Exactness at the differential induced by multiplication
> by `a`.

```lean
theorem exact_mul_right_left (a b : A)
    (ha : IsSMulRegular M a) :
    Function.Exact
      (periodicQuotientPsi
        (LinearMap.lsmul A M a) (LinearMap.lsmul A M b)
        (range_lsmul_comp_comm a b))
      (periodicQuotientPhi
        (LinearMap.lsmul A M a) (LinearMap.lsmul A M b)
        (range_lsmul_comp_comm a b))
```

**`AlgebraicGeometry.isFiniteLength_ring_quotient_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean#L98). The attribute's comment: “part (2): finite length”.

> **Stacks Project, Tag 02PY.** The ring quotient `A/(ab)` has finite length when `A` has
> dimension one.

```lean
theorem isFiniteLength_ring_quotient_mul
    [IsNoetherianRing A] [IsLocalRing A]
    (a b : A) (ha : IsSMulRegular A a) (hb : IsSMulRegular A b)
    (hdim : ringKrullDim A = 1) :
    IsFiniteLength A
      (A ⧸ LinearMap.range
        ((LinearMap.lsmul A A a) ∘ₗ (LinearMap.lsmul A A b)))
```

**`AlgebraicGeometry.exact_ring_mul_left_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean#L109). The attribute's comment: “part (2): exactness at b”.

> **Stacks Project, Tag 02PY.** Exactness at multiplication by `b` on `A/(ab)`.

```lean
theorem exact_ring_mul_left_right
    (a b : A) (hb : IsSMulRegular A b) :
    Function.Exact
      (periodicQuotientPhi
        (LinearMap.lsmul A A a) (LinearMap.lsmul A A b)
        (range_lsmul_comp_comm a b))
      (periodicQuotientPsi
        (LinearMap.lsmul A A a) (LinearMap.lsmul A A b)
        (range_lsmul_comp_comm a b))
```

**`AlgebraicGeometry.exact_ring_mul_right_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Exactness.lean#L122). The attribute's comment: “part (2): exactness at a”.

> **Stacks Project, Tag 02PY.** Exactness at multiplication by `a` on `A/(ab)`.

```lean
theorem exact_ring_mul_right_left
    (a b : A) (ha : IsSMulRegular A a) :
    Function.Exact
      (periodicQuotientPsi
        (LinearMap.lsmul A A a) (LinearMap.lsmul A A b)
        (range_lsmul_comp_comm a b))
      (periodicQuotientPhi
        (LinearMap.lsmul A A a) (LinearMap.lsmul A A b)
        (range_lsmul_comp_comm a b))
```

## Tag 02PZ, a definition

[Tag 02PZ](https://stacks.math.columbia.edu/tag/02PZ) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Basic.lean#L40).

> **Stacks Project, Tag 02PZ.** The symbol of a finite module of support dimension one,
> evaluated on two elements acting injectively on it.

```lean
noncomputable def moduleSymbol
    {A : Type u} {M : Type v} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] [AddCommGroup M] [Module A M] [Module.Finite A M]
    (a b : A) (ha : IsSMulRegular M a) (hb : IsSMulRegular M b)
    (hdim : Module.supportDim A M = 1) : (IsLocalRing.ResidueField A)ˣ
```

## Tag 02Q0, a lemma

[Tag 02Q0](https://stacks.math.columbia.edu/tag/02Q0) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol_mul_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Multiplicativity.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Multiplicativity.lean#L50). The attribute's comment: “multiplicativity”.

> **Stacks Project, Tag 02Q0.** The symbol is multiplicative in its second argument.

```lean
theorem moduleSymbol_mul_right
    {A : Type u} {M : Type v} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] [AddCommGroup M] [Module A M] [Module.Finite A M]
    (a b c : A) (ha : IsSMulRegular M a) (hb : IsSMulRegular M b)
    (hc : IsSMulRegular M c) (hdim : Module.supportDim A M = 1) :
    moduleSymbol a (b * c) ha (hb.mul hc) hdim =
      moduleSymbol a b ha hb hdim * moduleSymbol a c ha hc hdim
```

**`AlgebraicGeometry.moduleSymbol_mul_swap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Multiplicativity.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Multiplicativity.lean#L394). The attribute's comment: “swapped-arguments identity”.

> **Stacks Project, Tag 02Q0.** Swapping the two arguments gives inverse symbols.

```lean
theorem moduleSymbol_mul_swap
    {A : Type u} {M : Type v} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] [AddCommGroup M] [Module A M] [Module.Finite A M]
    (a b : A) (ha : IsSMulRegular M a) (hb : IsSMulRegular M b)
    (hdim : Module.supportDim A M = 1) :
    moduleSymbol a b ha hb hdim * moduleSymbol b a hb ha hdim = 1
```

## Tag 02Q1, a definition

[Tag 02Q1](https://stacks.math.columbia.edu/tag/02Q1) in the Stacks Project.

**`AlgebraicGeometry.tameSymbol`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/TameSymbol.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/TameSymbol.lean#L308).

> **Stacks Project, Tag 02Q1.** The tame symbol of a one-dimensional Noetherian local
> domain, extended to its fraction field.

```lean
noncomputable def tameSymbol {A : Type u} [CommRing A] [IsDomain A]
    [IsNoetherianRing A] [IsLocalRing A] {K : Type v} [Field K]
    [Algebra A K] [IsFractionRing A K] (hdim : ringKrullDim A = 1) :
    TameSymbol (K := K) hdim
```

## Tag 0AY9, a lemma

[Tag 0AY9](https://stacks.math.columbia.edu/tag/0AY9) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol_self_eq_negOne_pow_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Self.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Self.lean#L68).

> The symbol of a nonzerodivisor `a` with itself is `(-1) ^ length (M / aM)`.

```lean
theorem moduleSymbol_self_eq_negOne_pow_length
    {A : Type u} {M : Type v} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] [AddCommGroup M] [Module A M] [Module.Finite A M]
    (a : A) (ha : IsSMulRegular M a)
    (hdim : Module.supportDim A M = 1) :
    moduleSymbol a a ha ha hdim =
      (-1 : (IsLocalRing.ResidueField A)ˣ) ^
        moduleLength A (M ⧸ (LinearMap.lsmul A M a).range)
```

## Tag 02Q2, a lemma

[Tag 02Q2](https://stacks.math.columbia.edu/tag/02Q2) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol_unit_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Unit.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Unit.lean#L48). The attribute's comment: “module formula”.

> **Stacks Project, Tag 02Q2.** The symbol with a unit in its first argument is the
> corresponding power of its residue, with exponent the length of the quotient by the second
> argument.

```lean
theorem moduleSymbol_unit_left
    {A : Type u} {M : Type v} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] [AddCommGroup M] [Module A M] [Module.Finite A M]
    (u : Aˣ) (b : A) (hb : IsSMulRegular M b)
    (hdim : Module.supportDim A M = 1) :
    moduleSymbol (u : A) b (Units.isSMulRegular M u) hb hdim =
      IsLocalRing.residue A u ^
        moduleLength A (M ⧸ (LinearMap.lsmul A M b).range)
```

**`AlgebraicGeometry.moduleSymbol_unit_left_ring`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Unit.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Unit.lean#L110). The attribute's comment: “ring formula”.

> **Stacks Project, Tag 02Q2.** For a one-dimensional Noetherian local ring, the exponent in
> the unit-symbol formula is the order of vanishing of the second argument.

```lean
theorem moduleSymbol_unit_left_ring
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] (u : Aˣ) (b : A) (hb : IsSMulRegular A b)
    (hdim : ringKrullDim A = 1) :
    moduleSymbol (M := A) (u : A) b (Units.isSMulRegular A u) hb
      (by simpa only [Module.supportDim_self_eq_ringKrullDim] using hdim) =
      IsLocalRing.residue A u ^ (Ring.ord A b).toNat
```

## Tag 02Q3, a lemma

[Tag 02Q3](https://stacks.math.columbia.edu/tag/02Q3) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol_short_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/ShortExact.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/ShortExact.lean#L137).

> **Stacks Project, Tag 02Q3.** The symbol of the middle term of a short exact sequence is
> the product of the symbols of its outer terms.

```lean
theorem moduleSymbol_short_exact
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {M : Type v₁} {M' : Type v₂} {M'' : Type v₃}
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    [AddCommGroup M'] [Module A M'] [Module.Finite A M']
    [AddCommGroup M''] [Module A M''] [Module.Finite A M'']
    (i : M →ₗ[A] M') (p : M' →ₗ[A] M'')
    (hi : Function.Injective i) (hp : Function.Surjective p)
    (hip : Function.Exact i p)
    (a b : A)
    (haM : IsSMulRegular M a) (hbM : IsSMulRegular M b)
    (haM' : IsSMulRegular M' a) (hbM' : IsSMulRegular M' b)
    (haM'' : IsSMulRegular M'' a) (hbM'' : IsSMulRegular M'' b)
    (hdimM : Module.supportDim A M = 1)
    (hdimM' : Module.supportDim A M' = 1)
    (hdimM'' : Module.supportDim A M'' = 1) :
    moduleSymbol a b haM' hbM' hdimM' =
      moduleSymbol a b haM hbM hdimM * moduleSymbol a b haM'' hbM'' hdimM''
```

## Tag 02Q4, a lemma

[Tag 02Q4](https://stacks.math.columbia.edu/tag/02Q4) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol_eq_of_ker_coker_supportDim_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Invariance.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Invariance.lean#L478).

> **Stacks Project, Tag 02Q4.** The symbol is unchanged by a map of one-dimensional finite
> modules whose kernel and cokernel have support dimension at most zero.

```lean
theorem moduleSymbol_eq_of_ker_coker_supportDim_le_zero
    {A : Type u} {M : Type v} {M' : Type w}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    [AddCommGroup M'] [Module A M'] [Module.Finite A M']
    (α : M →ₗ[A] M') (a b : A)
    (ha : IsSMulRegular M a) (hb : IsSMulRegular M b)
    (ha' : IsSMulRegular M' a) (hb' : IsSMulRegular M' b)
    (hdim : Module.supportDim A M = 1)
    (hdim' : Module.supportDim A M' = 1)
    (hker : Module.supportDim A (LinearMap.ker α) ≤ 0)
    (hcoker : Module.supportDim A (M' ⧸ LinearMap.range α) ≤ 0) :
    moduleSymbol a b ha hb hdim = moduleSymbol a b ha' hb' hdim'
```

## Tag 02Q5, a lemma

[Tag 02Q5](https://stacks.math.columbia.edu/tag/02Q5) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol_eq_finprod_minimal_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/MinimalPrimes.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/MinimalPrimes.lean#L408).

> **Stacks Project, Tag 02Q5.** The symbol of a finite one-dimensional module is the product
> of the symbols of its minimal support quotients, weighted by localization lengths.

```lean
theorem moduleSymbol_eq_finprod_minimal_support
    {A : Type u} {M : Type v} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    (a b : A) (ha : IsSMulRegular M a) (hb : IsSMulRegular M b)
    (hdim : Module.supportDim A M = 1) :
    ∃ (haq : ∀ q : {q : PrimeSpectrum A // Minimal (· ∈ Module.support A M) q},
        IsSMulRegular (A ⧸ q.1.asIdeal) a),
    ∃ (hbq : ∀ q : {q : PrimeSpectrum A // Minimal (· ∈ Module.support A M) q},
        IsSMulRegular (A ⧸ q.1.asIdeal) b),
    ∃ (hdimq : ∀ q : {q : PrimeSpectrum A // Minimal (· ∈ Module.support A M) q},
        Module.supportDim A (A ⧸ q.1.asIdeal) = 1),
      moduleSymbol a b ha hb hdim =
        ∏ᶠ q : {q : PrimeSpectrum A // Minimal (· ∈ Module.support A M) q},
          (moduleSymbol (M := A ⧸ q.1.asIdeal) a b
            (haq q) (hbq q) (hdimq q)) ^
            (Module.length (Localization.AtPrime q.1.asIdeal)
              (LocalizedModule q.1.asIdeal.primeCompl M)).toNat
```

## Tag 02Q6, a lemma

[Tag 02Q6](https://stacks.math.columbia.edu/tag/02Q6) in the Stacks Project.

**`AlgebraicGeometry.exists_unit_algebraMap_eq_zpow_div_zpow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/DiscreteValuationRing.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/DiscreteValuationRing.lean#L242). The attribute's comment: “the power product is a unit of the valuation ring”.

> For a discrete valuation ring `A` with fraction field `K` and nonzero `x, y ∈ K`, the power
> product `x ^ (ord_A y) / y ^ (ord_A x)` is the image of a unit of `A`.

```lean
theorem exists_unit_algebraMap_eq_zpow_div_zpow
    {A : Type u} [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    {K : Type v} [Field K] [Algebra A K] [IsFractionRing A K] (x y : Kˣ) :
    ∃ w : Aˣ, algebraMap A K (w : A) =
      (x : K) ^ (ordInt A (y : K) y.ne_zero) / (y : K) ^ (ordInt A (x : K) x.ne_zero)
```

**`AlgebraicGeometry.tameSymbol_eq_negOnePow_mul_residue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/DiscreteValuationRing.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/DiscreteValuationRing.lean#L262). The attribute's comment: “the tame symbol formula”.

> For a discrete valuation ring `A` with fraction field `K` and nonzero `x, y ∈ K`, the symbol
> `d_A(x, y)` is the usual tame symbol: if `w` is a unit of `A` representing
> `x ^ (ord_A y) / y ^ (ord_A x)`, then `d_A(x, y)` is the residue of `w` times
> `(-1) ^ (ord_A x * ord_A y)`.

```lean
theorem tameSymbol_eq_negOnePow_mul_residue
    {A : Type u} [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    {K : Type v} [Field K] [Algebra A K] [IsFractionRing A K] (x y : Kˣ) (w : Aˣ)
    (hw : algebraMap A K (w : A) =
      (x : K) ^ (ordInt A (y : K) y.ne_zero) / (y : K) ^ (ordInt A (x : K) x.ne_zero)) :
    ((tameSymbol (K := K) (IsDiscreteValuationRing.ringKrullDim_eq_one A) x y :
          (IsLocalRing.ResidueField A)ˣ) : IsLocalRing.ResidueField A) =
      (((-1 : (IsLocalRing.ResidueField A)ˣ) ^
            (ordInt A (x : K) x.ne_zero * ordInt A (y : K) y.ne_zero) :
          (IsLocalRing.ResidueField A)ˣ) : IsLocalRing.ResidueField A) *
        IsLocalRing.residue A (w : A)
```

## Tag 02Q8, a lemma

[Tag 02Q8](https://stacks.math.columbia.edu/tag/02Q8) in the Stacks Project.

**`AlgebraicGeometry.moduleSymbol_steinberg_prepare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Steinberg.lean, line 983](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Steinberg.lean#L983).

> **Stacks Project, Tag 02Q8.** Let `A` be a Noetherian local ring, let `a b : A`, and let `M`
> be a finite `A`-module of support dimension one on which each of `a`, `b` and `b - a` acts
> injectively. Then
>
> `d_M(a, b - a) * d_M(b, b) = d_M(b, b - a) * d_M(a, b)`
>
> in the units of the residue field of `A`.

```lean
theorem moduleSymbol_steinberg_prepare
    {A : Type u} {M : Type v} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] [AddCommGroup M] [Module A M] [Module.Finite A M]
    (a b : A) (ha : IsSMulRegular M a) (hb : IsSMulRegular M b)
    (hba : IsSMulRegular M (b - a))
    (hdim : Module.supportDim A M = 1) :
    moduleSymbol a (b - a) ha hba hdim * moduleSymbol b b hb hb hdim =
      moduleSymbol b (b - a) hb hba hdim * moduleSymbol a b ha hb hdim
```

## Tag 02Q9, a lemma

[Tag 02Q9](https://stacks.math.columbia.edu/tag/02Q9) in the Stacks Project.

**`AlgebraicGeometry.tameSymbol_one_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/SteinbergTame.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/SteinbergTame.lean#L98). The attribute's comment: “two units of the fraction field identified by `(y : K) = 1 - (x : K)`”.

> **Stacks Project, Tag 02Q9.** Let `A` be a Noetherian local domain of dimension one with
> fraction field `K`. For `x` a unit of `K` and `y` the unit `1 - x` of `K`, the tame symbol of
> Tag 02Q1 satisfies `d_A(x, 1 - x) = 1` in the units of the residue field of `A`.
>
> Asking that both `x` and `1 - x` be units of `K` is the hypothesis `x ∉ {0, 1}` of the source.

```lean
theorem tameSymbol_one_sub {A : Type u} [CommRing A] [IsDomain A]
    [IsNoetherianRing A] [IsLocalRing A] {K : Type v} [Field K]
    [Algebra A K] [IsFractionRing A K] (hdim : ringKrullDim A = 1)
    (x y : Kˣ) (hy : (y : K) = 1 - (x : K)) :
    tameSymbol (K := K) hdim x y = 1
```

**`AlgebraicGeometry.tameSymbol_one_sub_mk0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/SteinbergTame.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/SteinbergTame.lean#L149). The attribute's comment: “an element of the fraction field other than `0` and `1`”.

> **Stacks Project, Tag 02Q9.** Let `A` be a Noetherian local domain of dimension one with
> fraction field `K`. For `x ∈ K` other than `0` and `1`, the tame symbol of Tag 02Q1 satisfies
> `d_A(x, 1 - x) = 1` in the units of the residue field of `A`.

```lean
theorem tameSymbol_one_sub_mk0 {A : Type u} [CommRing A] [IsDomain A]
    [IsNoetherianRing A] [IsLocalRing A] {K : Type v} [Field K]
    [Algebra A K] [IsFractionRing A K] (hdim : ringKrullDim A = 1)
    (x : K) (hx₀ : x ≠ 0) (hx₁ : x ≠ 1) :
    tameSymbol (K := K) hdim (Units.mk0 x hx₀)
      (Units.mk0 (1 - x) (sub_ne_zero_of_ne hx₁.symm)) = 1
```

## Tag 02QB, a lemma

[Tag 02QB](https://stacks.math.columbia.edu/tag/02QB) in the Stacks Project.

**`Module.FiniteLength.injective_iff_bijective_and_length_quotient_range_eq_order`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GoodSequenceColength.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/GoodSequenceColength.lean#L391).

> **Stacks Project, Tag 02QB.** Let `R` be a Noetherian local ring, `q` a prime with `R / q` of
> dimension one, and `φ : M → N` a map of finite modules each generated by a sequence of `l` terms
> whose successive quotients are `R / q`. Then `φ` is injective if and only if its localization at
> `q` is an isomorphism, and in this case the cokernel `N / φ(M)` has finite length equal to the
> order of the nonzero scalar `f` of the residue field at `q` with
> `[φ(x₁), …, φ(xₗ)] = f [y₁, …, yₗ]` in the determinant of the localization of `N`.

```lean
public theorem injective_iff_bijective_and_length_quotient_range_eq_order
    {R : Type u} {M : Type v} {N : Type w} [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] [AddCommGroup M] [Module R M] [Module.Finite R M]
    [AddCommGroup N] [Module R N] [Module.Finite R N]
    (q : Ideal R) [q.IsPrime] (hdim : ringKrullDim (R ⧸ q) = 1)
    (l : ℕ) (x : Fin l → M) (y : Fin l → N)
    (hx : Submodule.span R (Set.range x) = ⊤)
    (hxf : ∀ i : Fin l,
      Nonempty
        (((spanBefore (R := R) x i ⊔ R ∙ x i : Submodule R M) ⧸
            (spanBefore (R := R) x i).comap
              (spanBefore (R := R) x i ⊔ R ∙ x i : Submodule R M).subtype) ≃ₗ[R]
          R ⧸ q))
    (hy : Submodule.span R (Set.range y) = ⊤)
    (hyf : ∀ i : Fin l,
      Nonempty
        (((spanBefore (R := R) y i ⊔ R ∙ y i : Submodule R N) ⧸
            (spanBefore (R := R) y i).comap
              (spanBefore (R := R) y i ⊔ R ∙ y i : Submodule R N).subtype) ≃ₗ[R]
          R ⧸ q))
    (φ : M →ₗ[R] N) :
    letI : Ring.KrullDimLE 1 (R ⧸ q) := Ring.krullDimLE_iff.mpr hdim.le
    (Function.Injective φ ↔ Function.Bijective (LocalizedModule.map q.primeCompl φ)) ∧
      (Function.Injective φ →
        ∃ hlen : moduleLength (Localization.AtPrime q) (LocalizedModule q.primeCompl N) = l,
          ∃ hadmφ : IsAdmissibleSequence (R := Localization.AtPrime q)
              (fun i ↦ LocalizedModule.mk (φ (x (Fin.cast hlen i))) (1 : q.primeCompl)),
            ∃ hadmy : IsAdmissibleSequence (R := Localization.AtPrime q)
                (fun i ↦ LocalizedModule.mk (y (Fin.cast hlen i)) (1 : q.primeCompl)),
              ∃ f : IsLocalRing.ResidueField (Localization.AtPrime q), ∃ hf : f ≠ 0,
                symbol (⟨_, hadmφ⟩ :
                    AdmissibleSequence (Localization.AtPrime q)
                      (LocalizedModule q.primeCompl N)) =
                    f • symbol (⟨_, hadmy⟩ :
                      AdmissibleSequence (Localization.AtPrime q)
                        (LocalizedModule q.primeCompl N)) ∧
                  Module.length R (N ⧸ LinearMap.range φ) ≠ ⊤ ∧
                  ((Module.length R (N ⧸ LinearMap.range φ)).toNat : ℤ) =
                    Multiplicative.toAdd (WithZero.unzero
                      (x := Ring.ordFrac (R ⧸ q) f)
                      ((hf.isUnit.map (Ring.ordFrac (R ⧸ q))).ne_zero)))
```

## Tag 02QC, a lemma

[Tag 02QC](https://stacks.math.columbia.edu/tag/02QC) in the Stacks Project.

**`Module.FiniteLength.exists_sequence_with_successive_quotients_at_minimal_support_and_length_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LengthsDeterminants/GoodSequences.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LengthsDeterminants/GoodSequences.lean#L423). The attribute's comment: “The ring is not assumed local.”.

> **Stacks Project, Tag 02QC.** Let `M` be a finite module over a Noetherian ring `R` and
> `q` a minimal point of the support of `M`. Then there is a sequence `x₁, …, x_l` in `M` such
> that `q` is not in the support of `M / ⟨x₁, …, x_l⟩` and each successive quotient
> `⟨x₁, …, x_i⟩ / ⟨x₁, …, x_{i-1}⟩` is isomorphic to `R / q`. Moreover, every sequence with these
> two properties has `l` equal to the length of the localization `M_q` over `R_q`.

```lean
theorem exists_sequence_with_successive_quotients_at_minimal_support_and_length_eq
    {R : Type u} {M : Type v} [CommRing R] [IsNoetherianRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (q : PrimeSpectrum R) (hq : Minimal (· ∈ Module.support R M) q) :
    (∃ (l : ℕ) (x : Fin l → M),
      q ∉ Module.support R (M ⧸ Submodule.span R (Set.range x)) ∧
      ∀ i : Fin l,
        Nonempty
          (((spanBefore (R := R) x i ⊔ R ∙ x i : Submodule R M) ⧸
              (spanBefore (R := R) x i).comap
                (spanBefore (R := R) x i ⊔ R ∙ x i : Submodule R M).subtype) ≃ₗ[R]
            R ⧸ q.asIdeal)) ∧
    ∀ (l : ℕ) (x : Fin l → M),
      q ∉ Module.support R (M ⧸ Submodule.span R (Set.range x)) →
      (∀ i : Fin l,
        Nonempty
          (((spanBefore (R := R) x i ⊔ R ∙ x i : Submodule R M) ⧸
              (spanBefore (R := R) x i).comap
                (spanBefore (R := R) x i ⊔ R ∙ x i : Submodule R M).subtype) ≃ₗ[R]
            R ⧸ q.asIdeal)) →
      l = (Module.length (Localization.AtPrime q.asIdeal)
        (LocalizedModule q.asIdeal.primeCompl M)).toNat
```

## Tag 02QD, a proposition

[Tag 02QD](https://stacks.math.columbia.edu/tag/02QD) in the Stacks Project.

**`AlgebraicGeometry.neg_periodicLength_eq_finsum_ordFrac_periodicDeterminant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicLengthDeterminantFormula.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicLengthDeterminantFormula.lean#L62).

> **Stacks Project, Tag 02QD.** Let `R` be a Noetherian local ring and `(M, φ, ψ)` a
> `(2, 1)`-periodic complex with `M` finite, the cohomology of finite length and the support of `M`
> of dimension one. Then minus the multiplicity of the complex is the sum, over the minimal points
> of the support, of the orders of the periodic determinants of the localizations.

```lean
theorem neg_periodicLength_eq_finsum_ordFrac_periodicDeterminant
    {R : Type u} {M : Type v} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (φ ψ : Module.End R M) (hφψ : φ * ψ = 0) (hψφ : ψ * φ = 0)
    (hcoh : ∀ i : ZMod 2, IsFiniteLength R ((twoPeriodicComplex φ ψ hφψ hψφ).homology i))
    (hdim : Module.supportDim R M = 1) :
    ∃ hdim1 : ∀ q : {q : PrimeSpectrum R // Minimal (· ∈ Module.support R M) q},
        Ring.KrullDimLE 1 (R ⧸ q.1.asIdeal),
    ∃ hfin : ∀ q : {q : PrimeSpectrum R // Minimal (· ∈ Module.support R M) q},
        IsFiniteLength (Localization.AtPrime q.1.asIdeal)
          (LocalizedModule q.1.asIdeal.primeCompl M),
    ∃ hex₁ : ∀ q : {q : PrimeSpectrum R // Minimal (· ∈ Module.support R M) q},
        Function.Exact (LocalizedModule.map q.1.asIdeal.primeCompl φ)
          (LocalizedModule.map q.1.asIdeal.primeCompl ψ),
    ∃ hex₂ : ∀ q : {q : PrimeSpectrum R // Minimal (· ∈ Module.support R M) q},
        Function.Exact (LocalizedModule.map q.1.asIdeal.primeCompl ψ)
          (LocalizedModule.map q.1.asIdeal.primeCompl φ),
      -periodicLength (twoPeriodicComplex φ ψ hφψ hψφ) =
        ∑ᶠ q : {q : PrimeSpectrum R // Minimal (· ∈ Module.support R M) q},
          letI := hdim1 q
          Multiplicative.toAdd (WithZero.unzero
            (x := Ring.ordFrac (R ⧸ q.1.asIdeal)
              ((periodicDeterminant (LocalizedModule.map q.1.asIdeal.primeCompl φ)
                (LocalizedModule.map q.1.asIdeal.primeCompl ψ)
                (hex₁ q) (hex₂ q) (hfin q) : q.1.asIdeal.ResidueField)))
            (((periodicDeterminant (LocalizedModule.map q.1.asIdeal.primeCompl φ)
                (LocalizedModule.map q.1.asIdeal.primeCompl ψ)
                (hex₁ q) (hex₂ q) (hfin q)).isUnit.map
              (Ring.ordFrac (R ⧸ q.1.asIdeal))).ne_zero))
```

## Tag 02QE, a lemma

[Tag 02QE](https://stacks.math.columbia.edu/tag/02QE) in the Stacks Project.

**`AlgebraicGeometry.length_quotient_sub_length_ker_eq_finsum_ordOfResidueUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PeriodicLengthDeterminantFormula.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PeriodicLengthDeterminantFormula.lean#L237).

> **Stacks Project, Tag 02QE.** Let `R` be a Noetherian local ring, `M` a finite `R`-module
> whose support has dimension at most one, and `ψ : M → M` an `R`-linear map whose kernel and
> cokernel have finite length. Then the length of the cokernel minus the length of the kernel is
> the sum, over the nonclosed points `q` of the support of `M`, of the order of vanishing along
> `R ⧸ q` of the residue-field determinant of the automorphism `ψ_q` of `M_q`.

```lean
theorem length_quotient_sub_length_ker_eq_finsum_ordOfResidueUnit
    {R : Type u} {M : Type v} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M] (ψ : Module.End R M)
    (hker : IsFiniteLength R (LinearMap.ker ψ))
    (hcoker : IsFiniteLength R (M ⧸ LinearMap.range ψ))
    (hdim : Module.supportDim R M ≤ 1) :
    ∃ hdim1 : ∀ q : {q : PrimeSpectrum R //
        q ∈ Module.support R M ∧ q ≠ IsLocalRing.closedPoint R},
        Ring.KrullDimLE 1 (R ⧸ q.1.asIdeal),
    ∃ hfin : ∀ q : {q : PrimeSpectrum R //
        q ∈ Module.support R M ∧ q ≠ IsLocalRing.closedPoint R},
        IsFiniteLength (Localization.AtPrime q.1.asIdeal)
          (LocalizedModule q.1.asIdeal.primeCompl M),
    ∃ hbij : ∀ q : {q : PrimeSpectrum R //
        q ∈ Module.support R M ∧ q ≠ IsLocalRing.closedPoint R},
        Function.Bijective (LocalizedModule.map q.1.asIdeal.primeCompl ψ),
      ((Module.length R (M ⧸ LinearMap.range ψ)).toNat : ℤ) -
          ((Module.length R (LinearMap.ker ψ)).toNat : ℤ) =
        ∑ᶠ q : {q : PrimeSpectrum R //
            q ∈ Module.support R M ∧ q ≠ IsLocalRing.closedPoint R},
          @ordOfResidueUnit R _ _ q.1 q.1.isPrime (hdim1 q)
            (determinantAutomorphism
              (LinearEquiv.ofBijective
                (LocalizedModule.map q.1.asIdeal.primeCompl ψ) (hbij q)) (hfin q))
```

## Tag 02QJ, a lemma

[Tag 02QJ](https://stacks.math.columbia.edu/tag/02QJ) in the Stacks Project.

**`Stacks.Chow.finsum_fracTameSymbolOrderAt_canonical_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityCanonical.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityCanonical.lean#L123). The attribute's comment: “the second displayed form, the sum over all height-one primes”.

> **Stacks Project, Tag 02QJ: the Key Lemma for `d`.** Let `A` be a two-dimensional Noetherian
> local domain with fraction field `K` and let `f, g ∈ K^*`. Then
>
> `∑_{height(𝔮) = 1} ord_{A/𝔮}(∂_{A_𝔮}(f, g)) = 0`,
>
> the sum being over the height-one primes of `A`, with `∂_{A_𝔮}` the tame symbol of Stacks 0EAH on
> the one-dimensional Noetherian local ring `A_𝔮`
> (`Stacks.Chow.canonicalHeightOneSymbol`). Only finitely many primes contribute, by
> `Stacks.Chow.finite_fracTameSymbolOrderAt_support`, which is the first form the source gives the
> statement in.
>
> The proof is the source's:
> `Stacks.Chow.fracTameSymbolOrderAt_finsum_eq_zero_of_forall_nonZeroDivisors` expands a pair of
> fractions into four pairs of nonzerodivisors of `A`, and Stacks 0EAW
> (`Stacks.Chow.finsum_tameSymbolOrderAt_canonical_eq_zero`) kills each of the four.

```lean
theorem finsum_fracTameSymbolOrderAt_canonical_eq_zero [IsDomain A] [IsLocalRing A]
    (hdim : ringKrullDim A = 2) (f g : (FractionRing A)ˣ) :
    ∑ᶠ p : HeightOnePrime A,
      fracTameSymbolOrderAt hdim p (canonicalHeightOneSymbol p) f g = 0
```

**`Stacks.Chow.finsum_heightOneOrd_tameSymbol_totalFraction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityTotalFraction.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityTotalFraction.lean#L206). The attribute's comment: “generalization: for every two-dimensional Noetherian local ring, on the total ring of fractions”.

> **Stacks Project, Tag 0EAX: the Key Lemma, for every two-dimensional Noetherian local
> ring.** Let `A` be a two-dimensional Noetherian local ring, not necessarily a domain, with total
> ring of fractions `Q(A)`, and let `f, g ∈ Q(A)^*`. Then
>
> `∑_{height(𝔮) = 1} ord_{A/𝔮}(∂_{A_𝔮}(f, g)) = 0`,
>
> the sum being over the height-one primes of `A`, with `∂_{A_𝔮}` the tame symbol of Stacks 0EAH on
> the one-dimensional Noetherian local ring `A_𝔮`, applied to the images of `f` and `g` under
> `Stacks.Chow.heightOneFractionMap`. Only finitely many terms are nonzero, by
> `Stacks.Chow.finite_heightOneOrd_tameSymbol_totalFraction_support`.
>
> The proof is the source's: writing `f = a / b`, `g = c / d` expands the sum into four reciprocity
> sums of Stacks 0EAW, each of which vanishes.

```lean
theorem finsum_heightOneOrd_tameSymbol_totalFraction_eq_zero [IsLocalRing A]
    (hdim : ringKrullDim A = 2) (f g : (FractionRing A)ˣ) :
    ∑ᶠ p : HeightOnePrime A, heightOneOrd hdim p
      (tameSymbolOfKrullDimOne (ringKrullDim_localization_heightOnePrime p)
        (FractionRing (Localization.AtPrime p.1.asIdeal))
        (Units.map (heightOneFractionMap p).toMonoidHom f)
        (Units.map (heightOneFractionMap p).toMonoidHom g)) = 0
```

**`AlgebraicGeometry.localTameSymbol_ne_one_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Reciprocity.lean, line 534](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Reciprocity.lean#L534). The attribute's comment: “finiteness of the set of contributing primes, which makes the sum finite”.

> **Stacks Project, Tag 02QJ.** Two units of the fraction field have trivial tame symbol at
> all but finitely many height-one primes, so the reciprocity sum below is a finite sum.

```lean
theorem localTameSymbol_ne_one_finite
    {A : Type u} {K : Type v} [CommRing A] [IsDomain A] [IsNoetherianRing A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    (f g : Kˣ) :
    Set.Finite {q : {q : Ideal A // q.IsPrime ∧ q.height = 1} |
      localTameSymbol q f g ≠ 1}
```

**`AlgebraicGeometry.sum_ord_localTameSymbol_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Reciprocity.lean, line 1217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Reciprocity.lean#L1217). The attribute's comment: “the reciprocity formula, second displayed form: all height-one primes”.

> **Stacks Project, Tag 02QJ.** Let `A` be a two-dimensional Noetherian local domain
> with fraction field `K` and let `f, g` be units of `K`. The orders of vanishing of the tame
> symbols `∂_{A_𝔮}(f, g)` along `A / 𝔮`, summed over the height-one primes `𝔮` of `A`, give zero.

```lean
theorem sum_ord_localTameSymbol_eq_zero
    {A : Type u} {K : Type v} [CommRing A] [IsDomain A] [IsNoetherianRing A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [IsLocalRing A] (hdim : ringKrullDim A = 2)
    (f g : Kˣ) :
    ∃ (hquot : ∀ q : {q : Ideal A // q.IsPrime ∧ q.height = 1},
        Ring.KrullDimLE 1 (A ⧸ q.1)),
    (∑ᶠ q : {q : Ideal A // q.IsPrime ∧ q.height = 1},
        letI : q.1.IsPrime := q.2.1
        letI := hquot q
        let d := localTameSymbol q f g
        Multiplicative.toAdd (WithZero.unzero
          (x := Ring.ordFrac (A ⧸ q.1) (d : q.1.ResidueField))
          ((Units.isUnit d).map (Ring.ordFrac (A ⧸ q.1))).ne_zero)) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.68, Tag 0EAZ](https://stacks.math.columbia.edu/tag/0EAZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
