---
declaration: section
origin: cited
lean: TwoTermComplex.determinantEquivOfSurjectiveQuasiIso_apply_delta, TwoTermComplex.determinantEquiv_eq_of_homotopic_surjections, TwoTermComplex.determinantEquivOfSurjectiveQuasiIso_comp, TwoTermDeterminant.exists_determinantFunctor_natural_delta, TwoTermDeterminant.det, TwoTermDeterminant.delta, TwoTermDeterminant.det_map_delta
statement: formalized
proof: formalized
---

# 15.124 Determinants of complexes

Section 15.124 of the Stacks Project, [Tag 0FJI](https://stacks.math.columbia.edu/tag/0FJI). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FJJ, a lemma

[Tag 0FJJ](https://stacks.math.columbia.edu/tag/0FJJ) in the Stacks Project.

**`TwoTermComplex.determinantEquivOfSurjectiveQuasiIso_apply_delta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/DeterminantLine/CanonicalElement.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TwoTermComplex/DeterminantLine/CanonicalElement.lean#L143).

> **Stacks 0FJJ.** The canonical determinant equivalence associated to a
> degreewise-surjective quasi-isomorphism of two-term finite-projective complexes maps the
> canonical determinant element of the source to that of the target.

```lean
public theorem determinantEquivOfSurjectiveQuasiIso_apply_delta
    {R : Type u} [CommRing R]
    {K₁ : Type v₁} {K₀ : Type v₀} {L₁ : Type w₁} {L₀ : Type w₀}
    [AddCommGroup K₁] [Module R K₁] [Module.Finite R K₁] [Module.Projective R K₁]
    [AddCommGroup K₀] [Module R K₀] [Module.Finite R K₀] [Module.Projective R K₀]
    [AddCommGroup L₁] [Module R L₁] [Module.Finite R L₁] [Module.Projective R L₁]
    [AddCommGroup L₀] [Module R L₀] [Module.Finite R L₀] [Module.Projective R L₀]
    (K : K₁ →ₗ[R] K₀) (L : L₁ →ₗ[R] L₀) (a : TwoTermComplex.Hom K L)
    (ha : a.IsDegreewiseSurjective) (hqa : a.IsQuasiIso) (hL : TwoTermComplex.IsRankZero L) :
    letI : Module.Finite R (LinearMap.ker a.neg) :=
      TwoTermComplex.kernel_finite a.neg ha.1
    letI : Module.Projective R (LinearMap.ker a.neg) :=
      TwoTermComplex.kernel_projective a.neg ha.1
    letI : Module.Finite R (LinearMap.ker a.zero) :=
      TwoTermComplex.kernel_finite a.zero ha.2
    letI : Module.Projective R (LinearMap.ker a.zero) :=
      TwoTermComplex.kernel_projective a.zero ha.2
    let D := TwoTermComplex.determinantEquivOfSurjectiveQuasiIso K L a ha hqa
    ∃ hK : TwoTermComplex.IsRankZero K,
      D.equiv (TwoTermComplex.delta K hK) = TwoTermComplex.delta L hL
```

## Tag 0FJK, a lemma

[Tag 0FJK](https://stacks.math.columbia.edu/tag/0FJK) in the Stacks Project.

**`TwoTermComplex.determinantEquiv_eq_of_homotopic_surjections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/DeterminantLine/Homotopy.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TwoTermComplex/DeterminantLine/Homotopy.lean#L652).

> **Stacks 0FJK.** Homotopic degreewise-surjective quasi-isomorphisms between two-term
> complexes of finite projective modules induce the same canonical equivalence of determinant
> lines.

```lean
public theorem determinantEquiv_eq_of_homotopic_surjections
    {R : Type u} [CommRing R]
    {K₁ : Type v₁} {K₀ : Type v₀} {L₁ : Type w₁} {L₀ : Type w₀}
    [AddCommGroup K₁] [Module R K₁] [Module.Finite R K₁] [Module.Projective R K₁]
    [AddCommGroup K₀] [Module R K₀] [Module.Finite R K₀] [Module.Projective R K₀]
    [AddCommGroup L₁] [Module R L₁] [Module.Finite R L₁] [Module.Projective R L₁]
    [AddCommGroup L₀] [Module R L₀] [Module.Finite R L₀] [Module.Projective R L₀]
    (K : K₁ →ₗ[R] K₀) (L : L₁ →ₗ[R] L₀) (a : TwoTermComplex.Hom K L)
    (ha : a.IsDegreewiseSurjective) (hqa : a.IsQuasiIso) (h : K₀ →ₗ[R] L₁)
    (hbneg : Function.Surjective (a.neg + h.comp K))
    (hbzero : Function.Surjective (a.zero + L.comp h)) :
    let b : TwoTermComplex.Hom K L :=
      { neg := a.neg + h.comp K
        zero := a.zero + L.comp h
        comm
    := by
          ext x
          simp only [LinearMap.add_apply, LinearMap.comp_apply, map_add]
          rw [show a.zero (K x) = L (a.neg x) from LinearMap.congr_fun a.comm x] }
    b.IsQuasiIso ∧ ∀ hqb : b.IsQuasiIso,
      letI : Module.Finite R (LinearMap.ker a.neg) :=
        TwoTermComplex.kernel_finite a.neg ha.1
      letI : Module.Projective R (LinearMap.ker a.neg) :=
        TwoTermComplex.kernel_projective a.neg ha.1
      letI : Module.Finite R (LinearMap.ker a.zero) :=
        TwoTermComplex.kernel_finite a.zero ha.2
      letI : Module.Projective R (LinearMap.ker a.zero) :=
        TwoTermComplex.kernel_projective a.zero ha.2
      letI : Module.Finite R (LinearMap.ker b.neg) :=
        TwoTermComplex.kernel_finite b.neg hbneg
      letI : Module.Projective R (LinearMap.ker b.neg) :=
        TwoTermComplex.kernel_projective b.neg hbneg
      letI : Module.Finite R (LinearMap.ker b.zero) :=
        TwoTermComplex.kernel_finite b.zero hbzero
      letI : Module.Projective R (LinearMap.ker b.zero) :=
        TwoTermComplex.kernel_projective b.zero hbzero
      let Da := TwoTermComplex.determinantEquivOfSurjectiveQuasiIso K L a ha hqa
      let Db := TwoTermComplex.determinantEquivOfSurjectiveQuasiIso K L b
        ⟨hbneg, hbzero⟩ hqb
      Da.equiv = Db.equiv
```

## Tag 0FJL, a lemma

[Tag 0FJL](https://stacks.math.columbia.edu/tag/0FJL) in the Stacks Project.

**`TwoTermComplex.determinantEquivOfSurjectiveQuasiIso_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/DeterminantLine/Composition.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TwoTermComplex/DeterminantLine/Composition.lean#L253).

> **Stacks 0FJL.** The canonical determinant equivalence associated to a composite of
> degreewise-surjective quasi-isomorphisms of two-term finite-projective complexes is the
> composite of their canonical determinant equivalences.

```lean
public theorem determinantEquivOfSurjectiveQuasiIso_comp
    {R : Type u} [CommRing R]
    {K₁ : Type v₁} {K₀ : Type v₀} {L₁ : Type w₁} {L₀ : Type w₀}
    {M₁ : Type x₁} {M₀ : Type x₀}
    [AddCommGroup K₁] [Module R K₁] [Module.Finite R K₁] [Module.Projective R K₁]
    [AddCommGroup K₀] [Module R K₀] [Module.Finite R K₀] [Module.Projective R K₀]
    [AddCommGroup L₁] [Module R L₁] [Module.Finite R L₁] [Module.Projective R L₁]
    [AddCommGroup L₀] [Module R L₀] [Module.Finite R L₀] [Module.Projective R L₀]
    [AddCommGroup M₁] [Module R M₁] [Module.Finite R M₁] [Module.Projective R M₁]
    [AddCommGroup M₀] [Module R M₀] [Module.Finite R M₀] [Module.Projective R M₀]
    (K : K₁ →ₗ[R] K₀) (L : L₁ →ₗ[R] L₀) (M : M₁ →ₗ[R] M₀)
    (a : TwoTermComplex.Hom K L) (b : TwoTermComplex.Hom L M)
    (ha : a.IsDegreewiseSurjective) (hqa : a.IsQuasiIso)
    (hb : b.IsDegreewiseSurjective) (hqb : b.IsQuasiIso) :
    let c : TwoTermComplex.Hom K M :=
      { neg := b.neg.comp a.neg
        zero := b.zero.comp a.zero
        comm
    := by rw [LinearMap.comp_assoc, a.comm, ← LinearMap.comp_assoc, b.comm,
          LinearMap.comp_assoc] }
    let hc : c.IsDegreewiseSurjective :=
      ⟨hb.1.comp ha.1, hb.2.comp ha.2⟩
    ∃ hqc : c.IsQuasiIso,
      letI : Module.Finite R (LinearMap.ker a.neg) :=
        TwoTermComplex.kernel_finite a.neg ha.1
      letI : Module.Projective R (LinearMap.ker a.neg) :=
        TwoTermComplex.kernel_projective a.neg ha.1
      letI : Module.Finite R (LinearMap.ker a.zero) :=
        TwoTermComplex.kernel_finite a.zero ha.2
      letI : Module.Projective R (LinearMap.ker a.zero) :=
        TwoTermComplex.kernel_projective a.zero ha.2
      letI : Module.Finite R (LinearMap.ker b.neg) :=
        TwoTermComplex.kernel_finite b.neg hb.1
      letI : Module.Projective R (LinearMap.ker b.neg) :=
        TwoTermComplex.kernel_projective b.neg hb.1
      letI : Module.Finite R (LinearMap.ker b.zero) :=
        TwoTermComplex.kernel_finite b.zero hb.2
      letI : Module.Projective R (LinearMap.ker b.zero) :=
        TwoTermComplex.kernel_projective b.zero hb.2
      letI : Module.Finite R (LinearMap.ker c.neg) :=
        TwoTermComplex.kernel_finite c.neg hc.1
      letI : Module.Projective R (LinearMap.ker c.neg) :=
        TwoTermComplex.kernel_projective c.neg hc.1
      letI : Module.Finite R (LinearMap.ker c.zero) :=
        TwoTermComplex.kernel_finite c.zero hc.2
      letI : Module.Projective R (LinearMap.ker c.zero) :=
        TwoTermComplex.kernel_projective c.zero hc.2
      let Da := TwoTermComplex.determinantEquivOfSurjectiveQuasiIso K L a ha hqa
      let Db := TwoTermComplex.determinantEquivOfSurjectiveQuasiIso L M b hb hqb
      let Dc := TwoTermComplex.determinantEquivOfSurjectiveQuasiIso K M c hc hqc
      Da.equiv.trans Db.equiv = Dc.equiv
```

## Tag 0FJM, a lemma

[Tag 0FJM](https://stacks.math.columbia.edu/tag/0FJM) in the Stacks Project.

**`TwoTermDeterminant.exists_determinantFunctor_natural_delta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean, line 996](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean#L996).

> **Stacks 0FJM.** There is a determinant functor from perfect complexes of Tor-amplitude
> `[-1, 0]` and isomorphisms to invertible modules and isomorphisms. Its value is canonically
> identified with the determinant line of every finite-projective two-term presentation; on
> rank-zero objects the determinant of the differential defines an element natural under all
> isomorphisms.

```lean
public theorem exists_determinantFunctor_natural_delta {R : Type u} [CommRing R] :
    ∃ (det : Core (PerfectTwoTermComplex R) ⥤ Core (InvertibleModule R))
      (comparison : ∀ (K : PerfectTwoTermComplex R) (P : TwoTermPresentation K.obj),
        letI := P.finite (-1)
        letI := P.projective (-1)
        letI := P.finite 0
        letI := P.projective 0
        (det.obj ⟨K⟩).of.obj ≃ₗ[R]
          TwoTermComplex.determinantLine (P.complex.d (-1) 0).hom)
      (delta : ∀ (K : PerfectTwoTermComplex R),
        IsRankZero K.obj → (det.obj ⟨K⟩).of.obj),
      (∀ (K : PerfectTwoTermComplex R) (P : TwoTermPresentation K.obj)
          (hP : P.IsRankZero),
        letI := P.finite (-1)
        letI := P.projective (-1)
        letI := P.finite 0
        letI := P.projective 0
        (comparison K P).toLinearMap (delta K ⟨P, hP⟩) =
          TwoTermComplex.delta (P.complex.d (-1) 0).hom hP) ∧
      (∀ (K L : PerfectTwoTermComplex R) (P : TwoTermPresentation K.obj)
          (Q : TwoTermPresentation L.obj)
          (a : (⟨K⟩ : Core (PerfectTwoTermComplex R)) ⟶ ⟨L⟩)
          (f : P.complex ⟶ Q.complex)
          (_hf : P.iso.hom ≫ DerivedCategory.Q.map f ≫ Q.iso.inv = a.iso.hom.hom)
          (hs : (P.hom Q f).IsDegreewiseSurjective) (hq : (P.hom Q f).IsQuasiIso),
        letI := P.finite (-1)
        letI := P.projective (-1)
        letI := P.finite 0
        letI := P.projective 0
        letI := Q.finite (-1)
        letI := Q.projective (-1)
        letI := Q.finite 0
        letI := Q.projective 0
        let g := P.hom Q f
        letI := TwoTermComplex.kernel_finite g.neg hs.1
        letI := TwoTermComplex.kernel_projective g.neg hs.1
        letI := TwoTermComplex.kernel_finite g.zero hs.2
        letI := TwoTermComplex.kernel_projective g.zero hs.2
        ∀ x,
          (comparison L Q).toLinearMap ((det.map a).iso.hom x) =
            (TwoTermComplex.determinantEquivOfSurjectiveQuasiIso
              (P.complex.d (-1) 0).hom (Q.complex.d (-1) 0).hom g hs hq).equiv
                ((comparison K P).toLinearMap x)) ∧
      ∀ (K L : PerfectTwoTermComplex R)
        (a : (⟨K⟩ : Core (PerfectTwoTermComplex R)) ⟶ ⟨L⟩)
        (hK : IsRankZero K.obj) (hL : IsRankZero L.obj),
        (det.map a).iso.hom (delta K hK) = delta L hL
```

**`TwoTermDeterminant.det`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean, line 1102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean#L1102). The attribute's comment: “the determinant functor as a named definition, rather than as the subject of an existential quantifier”.

> **Stacks 0FJM.** The determinant functor, from perfect objects of the derived category of
> `R`-modules of Tor-amplitude in `[-1, 0]` with isomorphisms as morphisms, to invertible
> `R`-modules with isomorphisms as morphisms.

```lean
public noncomputable def det (R : Type u) [CommRing R] :
    Core (PerfectTwoTermComplex R) ⥤ Core (InvertibleModule R)
```

**`TwoTermDeterminant.delta`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean, line 1122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean#L1122). The attribute's comment: “the canonical section δ of the determinant of a rank-zero object, as a named definition”.

> **Stacks 0FJM.** The canonical element of the determinant of a perfect object of
> Tor-amplitude in `[-1, 0]` and rank zero, given by the determinant of the differential of a
> two-term presentation of it.

```lean
public noncomputable def delta {R : Type u} [CommRing R] (K : PerfectTwoTermComplex R)
    (hK : IsRankZero K.obj) : ((det R).obj ⟨K⟩).of.obj
```

**`TwoTermDeterminant.det_map_delta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean, line 1158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/TwoTermComplex/DeterminantFunctor.lean#L1158). The attribute's comment: “the compatibility det(a)(δ(L)) = δ(K) of the canonical section with isomorphisms, as a named theorem”.

> **Stacks 0FJM.** The determinant functor carries the canonical element of a rank-zero
> perfect object of Tor-amplitude in `[-1, 0]` to the canonical element of any isomorphic
> object.

```lean
public theorem det_map_delta {R : Type u} [CommRing R] {K L : PerfectTwoTermComplex R}
    (a : (⟨K⟩ : Core (PerfectTwoTermComplex R)) ⟶ ⟨L⟩)
    (hK : IsRankZero K.obj) (hL : IsRankZero L.obj) :
    ((det R).map a).iso.hom (delta K hK) = delta L hL
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.124, Tag 0FJI](https://stacks.math.columbia.edu/tag/0FJI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
