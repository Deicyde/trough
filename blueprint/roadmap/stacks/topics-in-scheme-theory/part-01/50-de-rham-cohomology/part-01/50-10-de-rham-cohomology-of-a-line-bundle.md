---
declaration: section
origin: cited
lean: KaehlerDifferential.deRhamDifferential_maps_gradedDifferentialFormComponent, KaehlerDifferential.isInternal_gradedDifferentialComponent, KaehlerDifferential.isInternal_gradedDifferentialFormComponent, KaehlerDifferential.gradedDifferentialFormComponent_wedgeMul_mem, KaehlerDifferential.gradedDifferentialFormComponent, KaehlerDifferential.gradedDifferentialComponent, Stacks.LineBundle.Situation.gradedLaurentForms, Stacks.LineBundle.Situation.residueShortComplex_shortExact
statement: formalized
proof: formalized
---

# 50.10 de Rham cohomology of a line bundle

Section 50.10 of the Stacks Project, [Tag 0FU8](https://stacks.math.columbia.edu/tag/0FU8). 6 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FU9, a remark

[Tag 0FU9](https://stacks.math.columbia.edu/tag/0FU9) in the Stacks Project.

**`KaehlerDifferential.deRhamDifferential_maps_gradedDifferentialFormComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/DifferentialDegree.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/DifferentialDegree.lean#L44). The attribute's comment: “differential_preserves_degree”.

> The de Rham differential preserves the total degree of homogeneous
> differential forms.

```lean
theorem deRhamDifferential_maps_gradedDifferentialFormComponent
    {G : Type u} {R : Type v} {A : Type w}
    [AddCommMonoid G] [CommRing R] [CommRing A] [Algebra R A]
    (gr : G → Submodule R A) (hunit : (1 : A) ∈ gr 0) (p : ℕ) (g : G)
    (d : (⋀[A]^p (KaehlerDifferential R A)) →ₗ[R]
      (⋀[A]^(p + 1) (KaehlerDifferential R A)))
    (hd : ∀ a : Fin (p + 1) → A,
      d (a 0 • exteriorPower.ιMulti A p (fun i ↦
        KaehlerDifferential.D R A (a i.succ))) =
        exteriorPower.ιMulti A (p + 1) (fun i ↦
          KaehlerDifferential.D R A (a i))) :
    Submodule.map d (gradedDifferentialFormComponent gr p g) ≤
      gradedDifferentialFormComponent gr (p + 1) g
```

**`KaehlerDifferential.isInternal_gradedDifferentialComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/DifferentialsDirectSum.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/DifferentialsDirectSum.lean#L42). The attribute's comment: “differentials_direct_sum”.

> **Stacks Project, Tag 0FU9.** The Kähler differentials of a graded
> commutative algebra are the internal direct sum of their homogeneous
> components.

```lean
theorem isInternal_gradedDifferentialComponent
    {G : Type u} {R : Type v} {A : Type w}
    [AddCommMonoid G] [DecidableEq G]
    [CommRing R] [CommRing A] [Algebra R A]
    (gr : G → Submodule R A) [GradedAlgebra gr] :
    DirectSum.IsInternal (gradedDifferentialComponent gr)
```

**`KaehlerDifferential.isInternal_gradedDifferentialFormComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/FormsDirectSum/Decomposition.lean, line 642](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/FormsDirectSum/Decomposition.lean#L642). The attribute's comment: “forms_direct_sum”.

> Differential forms decompose as the internal direct sum of their
> homogeneous total-degree components.

```lean
theorem isInternal_gradedDifferentialFormComponent
    {G : Type u} {R : Type v} {A : Type w}
    [AddCommMonoid G] [DecidableEq G]
    [CommRing R] [CommRing A] [Algebra R A]
    (gr : G → Submodule R A) [SetLike.GradedMonoid gr]
    (hgr : DirectSum.IsInternal gr) (p : ℕ) :
    DirectSum.IsInternal
      (gradedDifferentialFormComponent gr p)
```

**`KaehlerDifferential.gradedDifferentialFormComponent_wedgeMul_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/FormsDirectSum/GradedExteriorAlgebra.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/FormsDirectSum/GradedExteriorAlgebra.lean#L253). The attribute's comment: “wedge_compatible_with_gradings”.

> **Stacks Project, Tag 0FU9.** The wedge product is compatible with the gradings: the wedge
> of a form of exterior degree `p` and total degree `g` with a form of exterior degree `q` and
> total degree `h` has exterior degree `p + q` and total degree `g + h`.

```lean
theorem gradedDifferentialFormComponent_wedgeMul_mem
    {G : Type u} {R : Type v} {A : Type w}
    [AddCommMonoid G] [CommRing R] [CommRing A] [Algebra R A]
    (gr : G → Submodule R A) [SetLike.GradedMonoid gr]
    (p q : ℕ) {g h : G}
    {x : ⋀[A]^p (KaehlerDifferential R A)}
    (hx : x ∈ gradedDifferentialFormComponent gr p g)
    {y : ⋀[A]^q (KaehlerDifferential R A)}
    (hy : y ∈ gradedDifferentialFormComponent gr q h) :
    exteriorPower.wedgeMul p q x y ∈
      gradedDifferentialFormComponent gr (p + q) (g + h)
```

**`KaehlerDifferential.gradedDifferentialFormComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/GradedComponents.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/GradedComponents.lean#L58). The attribute's comment: “graded_differential_form_components”.

> The degree-`g` component of the `p`-forms of `A` over `R`, generated over
> `R` by `a₀ ⋅ da₁ ∧ ⋯ ∧ daₚ` for homogeneous elements whose degrees sum
> to `g`.

```lean
noncomputable def gradedDifferentialFormComponent
    {G : Type u} {R : Type v} {A : Type w}
    [AddCommMonoid G] [CommRing R] [CommRing A] [Algebra R A]
    (gr : G → Submodule R A) (p : ℕ) (g : G) :
    Submodule R (⋀[A]^p (KaehlerDifferential R A))
```

**`KaehlerDifferential.gradedDifferentialComponent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/GradedComponents.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/DeRhamCohomology/GradedComponents.lean#L75). The attribute's comment: “graded_differential_form_components”.

> The degree-`g` component of the Kähler differentials of `A` over `R`.
>
> This is the degree-one differential-form component, viewed in
> `KaehlerDifferential R A` through the canonical degree-one exterior-power
> equivalence.

```lean
noncomputable def gradedDifferentialComponent
    {G : Type u} {R : Type v} {A : Type w}
    [AddCommMonoid G] [CommRing R] [CommRing A] [Algebra R A]
    (gr : G → Submodule R A) (g : G) :
    Submodule R (KaehlerDifferential R A)
```

**`Stacks.LineBundle.Situation.gradedLaurentForms`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/GradedForms.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/GradedForms.lean#L301). The attribute's comment: “the sheaf-level graded components of the pushed-forward de Rham forms of L-star”.

> **The degree-`n` part `Ω^p_{L^⋆/S, n}` of the pushed-forward relative differential forms of
> the complement of the zero section of a line bundle**: the smallest sub-`𝒪_X`-module sheaf of
> `(L^⋆ → X)_* Ω^p_{L^⋆/S}` containing, over every affine open of `X`, the homogeneous forms of
> degree `n`. This is the sheaf-level counterpart of the graded components of Tag 0FU9.

```lean
def Situation.gradedLaurentForms (p : ℕ) (n : ℤ) :
    (D.laurentFormsPushforward (p : ℤ)).Submodule
```

## Tag 0FUF, a lemma

[Tag 0FUF](https://stacks.math.columbia.edu/tag/0FUF) in the Stacks Project.

**`Stacks.LineBundle.Situation.residueShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ResidueSequence.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ResidueSequence.lean#L586).

> Let `f : X ⟶ S` be a morphism of schemes, `L` an invertible
> `𝒪_X`-module and `π : L^⋆ ⟶ X` the complement of the zero section of the line bundle of `L`, with
> `Ω^•_{L^⋆/S,0}` the weight-zero part of `π_*Ω^•_{L^⋆/S}` for the grading by the action of `𝔾_m`
> (`Stacks.LineBundle.Situation.weightZeroComplex`, Tag 0FU9). Then the sequence of complexes of
> sheaves of abelian groups on `X`
>
> `0 → Ω^•_{X/S} → Ω^•_{L^⋆/S,0} → Ω^•_{X/S}[-1] → 0`
>
> is short exact. The first map is the pullback of forms along `π`
> (`Stacks.LineBundle.Situation.pullbackHom`); the second is the residue
> (`Stacks.LineBundle.Situation.residueHom`), which over an open where `L` is trivialized by a
> generator `s`, so that `s` is a unit of degree one on `L^⋆`, sends `π^*α + d log s ∧ π^*β` to `β`
> (`Stacks.LineBundle.Situation.residueHom_decomposition`) independently of the trivialization.

```lean
theorem Situation.residueShortComplex_shortExact : D.residueShortComplex.ShortExact
```

**`LaurentDeRham.weightComponent_eq_weightForms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LaurentResidue.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LaurentResidue.lean#L506). The attribute's comment: “the local computation: 1 and dlog T generate the weight-zero forms”.

> **The weight components of the de Rham complex of `A[T;T⁻¹]`, explicitly**: a relative form of
> weight `g` is uniquely `Tᵍ ω' + Tᵍ dlog T ∧ ω` with `ω'` and `ω` pulled back from `A`.

```lean
theorem weightComponent_eq_weightForms (g : ℤ) (p : ℕ) :
    weightComponent R A g p = weightForms R A g p
```

**`LaurentDeRham.residue_mapExteriorPower_add_wedgeLeft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LaurentResidue.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LaurentResidue.lean#L635). The attribute's comment: “the local computation: the defining formula for the residue”.

> **The defining formula of the residue**: `Res (ω' + dlog T ∧ ω) = ω`.

```lean
theorem residue_mapExteriorPower_add_wedgeLeft (p : ℕ) (ω' : ↥(⋀[A]^(p + 1) (Ω[A⁄R])))
    (ω : ↥(⋀[A]^p (Ω[A⁄R]))) :
    residue R A p (mapExteriorPower R A A[T;T⁻¹] (p + 1) ω' +
        exteriorPower.wedgeLeft (dlogT R A) p (mapExteriorPower R A A[T;T⁻¹] p ω)) = ω
```

**`LaurentDeRham.shortExact_residueShortComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LaurentResidue.lean, line 921](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LaurentResidue.lean#L921). The attribute's comment: “the affine local case: the residue short exact sequence for A[T;T⁻¹] over R”.

> **The residue short exact sequence of complexes** of Stacks 0FUF, in its affine form:
> `0 → Ω^•_{A/R} → Ω^•_{A[T;T⁻¹]/R,0} → Ω^•_{A/R}[-1] → 0`.  The first map is the pullback of forms
> along `A → A[T;T⁻¹]`, the second is the residue `ω' + dlog T ∧ ω ↦ ω`, and the shift carries the
> differential `−d`.

```lean
theorem shortExact_residueShortComplex : (residueShortComplex R A).ShortExact
```

**`LaurentDeRham.residue_mapExteriorPower_add_wedgeLeft_dlogUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LaurentResidueTrivialization.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LaurentResidueTrivialization.lean#L186). The attribute's comment: “the local computation: the residue formula holds for every trivialization, not only for the coordinate T”.

> **The defining formula of the residue holds in every coordinate**:
> `Res (ω' + dlog u ∧ ω) = ω` for every unit `u` of `A[T;T⁻¹]` homogeneous of weight one.

```lean
theorem residue_mapExteriorPower_add_wedgeLeft_dlogUnit {v : A[T;T⁻¹]ˣ}
    (hv : (v : A[T;T⁻¹]) ∈ weightGrading R A 1) (p : ℕ)
    (ω' : ↥(⋀[A]^(p + 1) (Ω[A⁄R]))) (ω : ↥(⋀[A]^p (Ω[A⁄R]))) :
    residue R A p (mapExteriorPower R A A[T;T⁻¹] (p + 1) ω' +
        exteriorPower.wedgeLeft (Stacks.LogPoles.dlogUnit R v) p
          (mapExteriorPower R A A[T;T⁻¹] p ω)) = ω
```

**`LaurentDeRham.exists_of_mem_weightComponent_succ_dlogUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LaurentResidueTrivialization.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LaurentResidueTrivialization.lean#L200). The attribute's comment: “the local computation: 1 and dlog u generate the weight-zero forms for every trivialization, not only for the coordinate T”.

> **`1` and `dlog u` generate the weight-zero forms** for every coordinate `u`: a weight-zero
> form of positive degree is `ω' + dlog u ∧ ω` with `ω'` and `ω` pulled back from `A`.

```lean
theorem exists_of_mem_weightComponent_succ_dlogUnit {v : A[T;T⁻¹]ˣ}
    (hv : (v : A[T;T⁻¹]) ∈ weightGrading R A 1) {p : ℕ}
    {x : ↥(⋀[A[T;T⁻¹]]^(p + 1) (Ω[A[T;T⁻¹]⁄R]))} (hx : x ∈ weightComponent R A 0 (p + 1)) :
    ∃ (ω' : ↥(⋀[A]^(p + 1) (Ω[A⁄R]))) (ω : ↥(⋀[A]^p (Ω[A⁄R]))),
      x = mapExteriorPower R A A[T;T⁻¹] (p + 1) ω' +
        exteriorPower.wedgeLeft (Stacks.LogPoles.dlogUnit R v) p
          (mapExteriorPower R A A[T;T⁻¹] p ω)
```

**`LaurentDeRham.eq_of_mapExteriorPower_add_wedgeLeft_dlogUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/LaurentResidueTrivialization.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/LaurentResidueTrivialization.lean#L217). The attribute's comment: “the local computation: the residue is independent of the trivialization”.

> **The residue does not depend on the coordinate.**  If a weight-zero form is written
> `ω₁' + dlog u ∧ ω₁` in one coordinate and `ω₂' + dlog v ∧ ω₂` in another, then `ω₁ = ω₂`: both
> are its residue.

```lean
theorem eq_of_mapExteriorPower_add_wedgeLeft_dlogUnit {v w : A[T;T⁻¹]ˣ}
    (hv : (v : A[T;T⁻¹]) ∈ weightGrading R A 1)
    (hw : (w : A[T;T⁻¹]) ∈ weightGrading R A 1) {p : ℕ}
    {ω₁' ω₂' : ↥(⋀[A]^(p + 1) (Ω[A⁄R]))} {ω₁ ω₂ : ↥(⋀[A]^p (Ω[A⁄R]))}
    (h : mapExteriorPower R A A[T;T⁻¹] (p + 1) ω₁' +
          exteriorPower.wedgeLeft (Stacks.LogPoles.dlogUnit R v) p
            (mapExteriorPower R A A[T;T⁻¹] p ω₁) =
        mapExteriorPower R A A[T;T⁻¹] (p + 1) ω₂' +
          exteriorPower.wedgeLeft (Stacks.LogPoles.dlogUnit R w) p
            (mapExteriorPower R A A[T;T⁻¹] p ω₂)) :
    ω₁ = ω₂
```

## Tag 0FUG, a lemma

[Tag 0FUG](https://stacks.math.columbia.edu/tag/0FUG) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.DeRhamResidueSequence.boundary_eq_deRhamClassDerivedMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/ResidueBoundary.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/ResidueBoundary.lean#L217). The attribute's comment: “the boundary map of the residue sequence of 0FUF is the map of 0FU7 for the de Rham first Chern class; the global form of 0FUF, the lift of the boundary map to right differential graded modules, its value at the unit, and the comparison of the two realizations of de Rham cohomology are carried as the explicit named hypotheses S, hlift, hev and realizationComparison”.

> **Stacks Project, Tag 0FUG.** **The boundary map
>
> `δ : Ω^•_{X/S} ⟶ Ω^•_{X/S}[2]`
>
> of the residue sequence of Tag 0FUF is the morphism of Tag 0FU7 attached to the de Rham first
> Chern class `c₁^{dR}(ℒ)`**, that is, cup product by `c₁^{dR}(ℒ)`.
>
> Four inputs of the Stacks proof are hypotheses, because the library does not have them; see the
> implementation notes of this file.
>
> * `S`, the residue sequence of Tag 0FUF in its global form: only its affine local computation
>   `LaurentDeRham.shortExact_residueShortComplex` is in the library.
> * `hlift`, that `δ` lifts to the derived category of right differential graded
>   `Ω^•_{X/S}`-modules. In Stacks this comes from the residue sequence being one of right
>   differential graded modules together with the descent of Differential Graded Sheaves, Section
>   24.32, the same input that
>   `AlgebraicGeometry.SheafOfModules.DeRhamDerivedModuleCorrespondence` carries for Tag 0FU7.
> * `hev`, that `δ(1) = c₁^{dR}(ℒ)`, which Stacks proves by mapping the short exact sequence of
>   abelian sheaves `0 → 𝒪_X^* → E → ℤ → 0` into the translated residue sequence.
> * `realizationComparison`, which transports the de Rham first Chern class of Tag 0FLE,
>   `AlgebraicGeometry.SheafOfModules.deRhamFirstChernClassAbelianOf`, from the abelian-sheaf
>   realization of de Rham cohomology, in which it is constructed because `d log` is not
>   `𝒪_X`-linear, to the sheaf-of-`A`-modules realization, in which the classes of Tag 0FU7 live.
>
> What is proved is the last step of the Stacks proof: by the uniqueness in Tag 0FU7,
> `AlgebraicGeometry.SheafOfModules.eq_deRhamClassDerivedMorphism`, a morphism with those two
> properties is the morphism attached to `c₁^{dR}(ℒ)`.

```lean
theorem boundary_eq_deRhamClassDerivedMorphism (c : DeRhamDerivedModuleCorrespondence B D)
    (realizationComparison : deRhamCohomologyAbelian B D 2 →+ deRhamCohomology B D 2)
    (L : _root_.SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L)
    (hlift : ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D 2,
      c.forget 2 g = S.boundary)
    (hev : c.evalOne 2 S.boundary =
      realizationComparison (deRhamFirstChernClassAbelianOf B D L hL)) :
    S.boundary = deRhamClassDerivedMorphism B D c 2
      (realizationComparison (deRhamFirstChernClassAbelianOf B D L hL))
```

**`AlgebraicGeometry.SheafOfModules.DeRhamResidueSequence.boundary_eq_boundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/ResidueBoundary.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/FirstChernClass/ResidueBoundary.lean#L234). The attribute's comment: “the boundary map is independent of the chosen residue sequence”.

> **Stacks Project, Tag 0FUG.** The boundary map of the residue sequence does not depend on the
> choice of the residue sequence: two residue sequences whose boundary maps both lift to the derived
> category of right differential graded `Ω^•_{X/S}`-modules and both take the value `c₁^{dR}(ℒ)` at
> the unit have the same boundary map, both being cup product by `c₁^{dR}(ℒ)`.

```lean
theorem boundary_eq_boundary (S' : DeRhamResidueSequence B D)
    (c : DeRhamDerivedModuleCorrespondence B D)
    (realizationComparison : deRhamCohomologyAbelian B D 2 →+ deRhamCohomology B D 2)
    (L : _root_.SheafOfModules.{u} (structureSheaf X.sheaf))
    (hL : Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L)
    (hlift : ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D 2,
      c.forget 2 g = S.boundary)
    (hev : c.evalOne 2 S.boundary =
      realizationComparison (deRhamFirstChernClassAbelianOf B D L hL))
    (hlift' : ∃ g : deRhamDerivedRegular B D ⟶ deRhamDerivedRegularShift B D 2,
      c.forget 2 g = S'.boundary)
    (hev' : c.evalOne 2 S'.boundary =
      realizationComparison (deRhamFirstChernClassAbelianOf B D L hL)) :
    S.boundary = S'.boundary
```

**`Stacks.LineBundle.Situation.residueShiftedSequence_boundary_eq_deRhamClassMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ResidueBoundaryChernClass.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/ResidueBoundaryChernClass.lean#L47).

> **Stacks Project, Tag 0FUG.** For a line bundle `ℒ` on `X` over `S`, the boundary map
> `δ : Ω^•_{X/S} ⟶ Ω^•_{X/S}[2]` in `D(f^{-1}𝒪_S)` of the shifted residue sequence of Tag 0FUF is the
> morphism `ξ'` of Tag 0FU7 attached to the de Rham first Chern class `ξ = c₁^{dR}(ℒ)`.

```lean
theorem Situation.residueShiftedSequence_boundary_eq_deRhamClassMorphism (D : Situation.{u}) :
    D.residueShiftedSequence.boundary =
      AlgebraicGeometry.SheafOfModules.deRhamClassMorphism (Scheme.Hom.deRhamAlgebras D.f)
        (AlgebraicGeometry.SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras D.f)) 2
        (AlgebraicGeometry.SheafOfModules.deRhamCohomologyFirstChernClass (X := D.X.toRingedSpace)
          (Scheme.Hom.deRhamAlgebras D.f)
          (AlgebraicGeometry.SheafOfModules.deRhamDifferential (Scheme.Hom.deRhamAlgebras D.f)) D.L
          (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ D.L D.invertible))
```

## Tag 0FUH, a lemma

[Tag 0FUH](https://stacks.math.columbia.edu/tag/0FUH) in the Stacks Project.

**`Stacks.LineBundle.Situation.gradedTwistIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/HomogeneousTwistComparison.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/HomogeneousTwistComparison.lean#L372). The attribute's comment: “clause (1): the degree-n part is identified with the twisted degree-zero part”.

> **Clause (1) of Tag 0FUH**: the degree-`n` part of the pushed-forward relative differential
> forms of the complement of the zero section is the degree-zero part twisted by `L^{⊗ n}`,
> `Ω^p_{L^⋆/S, n} = Ω^p_{L^⋆/S, 0} ⊗_{𝒪_X} L^{⊗ n}`. The isomorphism is multiplication of a form by
> the homogeneous function of a local section of `L^{⊗ n}`, so it is the canonical map and not a
> choice. That the two sides are *quasi-coherent* `𝒪_X`-modules, which is the rest of what the
> printed clause asserts, is `Stacks.LineBundle.Situation.isQuasicoherent_gradedAt` and
> `Situation.isQuasicoherent_gradedTwistSource` of
> `StacksFrontier.AlgebraicGeometry.DeRham.LineBundle.HomogeneousTwistCompatible`.

```lean
def Situation.gradedTwistIso (p : ℕ) (n : ℤ) :
    ((sheafTensor D.X.sheaf).obj (D.gradedAt p 0)).obj (D.tensorPowerAt n) ≅
      D.gradedAt p n
```

**`Stacks.LineBundle.Situation.isQuasicoherent_gradedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/HomogeneousTwistCompatible.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/HomogeneousTwistCompatible.lean#L655). The attribute's comment: “clause (1): the degree-n part is a quasi-coherent O_X-module”.

> **The degree-`n` part `Ω^p_{L^⋆/S, n}` is quasi-coherent**, read at the indexing the tensor
> product of Tag 05NA and the comparison map of clause (1) are defined over. This is
> `Situation.isQuasicoherent_gradedLaurentForms` at the `Situation.gradedAt` spelling, which is the
> same object by definition.

```lean
theorem Situation.isQuasicoherent_gradedAt (p : ℕ) (n : ℤ) :
    (D.gradedAt p n).IsQuasicoherent
```

**`Stacks.LineBundle.Situation.isQuasicoherent_gradedTwistSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/HomogeneousTwistCompatible.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/HomogeneousTwistCompatible.lean#L664). The attribute's comment: “clause (1): the twisted degree-zero part is a quasi-coherent O_X-module”.

> **The source `Ω^p_{L^⋆/S, 0} ⊗_{𝒪_X} L^{⊗ n}` of the comparison map of clause (1) is
> quasi-coherent**: both factors are, the degree-zero part by
> `Situation.isQuasicoherent_gradedAt` and the tensor power by
> `Situation.isQuasicoherent_tensorPower`, so Tag 0GQM applies.

```lean
theorem Situation.isQuasicoherent_gradedTwistSource (p : ℕ) (n : ℤ) :
    (((Stacks.SheafOfModules.Tensor.sheafTensor D.X.sheaf).obj (D.gradedAt p 0)).obj
      (D.tensorPowerAt n)).IsQuasicoherent
```

**`Stacks.LineBundle.Situation.gradedFormsIsoLaurent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpaceLaurentComparison.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpaceLaurentComparison.lean#L660). The attribute's comment: “clause (3): for `n > 0`, `Ω^p_{L/S, n} = Ω^p_{L^⋆/S, n}` (printed `L/X`, a misprint for `L/S`)”.

> For `n > 0` and `p ≥ 0`, the weight-`n` part of the pushed-forward relative `p`-forms of the
> total space `𝕃` of `L` over `S` is the weight-`n` part of the pushed-forward relative `p`-forms of
> `L^⋆` over `S`: `Ω^p_{𝕃/S, n} ≅ Ω^p_{L^⋆/S, n}`, through the restriction of forms along `L^⋆ ⊆ 𝕃`.
>
> The printed statement reads `Ω^p_{L/X, n}`, a misprint for `Ω^p_{L/S, n}`: the forms relative to
> `X` satisfy `Ω^p_{L/X, n} = 0` for `p ≥ 2` while `Ω^p_{L^⋆/S, n}` is in general nonzero, and the
> use of this lemma in the proof of Tag 0FUK concerns the forms relative to `S`.

```lean
def Situation.gradedFormsIsoLaurent (p : ℕ) {n : ℕ} (hn : 0 < n) :
    (D.gradedTotalForms p n).toSheafOfModules ≅
      (D.gradedLaurentForms p (n : ℤ)).toSheafOfModules
```

**`Stacks.LineBundle.Situation.deRhamComplexIsoTotalWeightZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpaceWeightZero.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpaceWeightZero.lean#L529). The attribute's comment: “clause (2): `Ω^•_{X/S} = Ω^•_{L/S, 0}` as complexes (printed `L/X`, a misprint for `L/S`)”.

> Let `f : X ⟶ S` be a morphism of schemes, `L` an invertible `𝒪_X`-module and `π : 𝕃 ⟶ X`
> its total space. Then `Ω^•_{X/S} = Ω^•_{𝕃/S, 0}` as complexes: the de Rham complex of `X` over
> `S` is isomorphic to the weight-zero subcomplex of `π_* Ω^•_{𝕃/S}`, through the canonical map
> `Stacks.LineBundle.Situation.deRhamPushforward` (see
> `Stacks.LineBundle.Situation.deRhamComplexIsoTotalWeightZero_hom_ι`).
>
> The printed statement writes `Ω^•_{L/X, 0}`; the subscript `L/X` is a misprint for `L/S`: the
> relative forms of `L` over `X` vanish in degree one in weight zero, and the paragraph before the
> lemma as well as its use in the proof of Tag 0FUK (`π_*Ω^a_{L/S} = Ω^a_{P/S} ⊕ ⋯`) concern
> `L/S`.

```lean
def Situation.deRhamComplexIsoTotalWeightZero : D.baseDeRhamComplex ≅ D.totalWeightZeroComplex
```

**`LaurentDeRham.weightComponentSmulEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/WeightComparison.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/WeightComparison.lean#L172). The attribute's comment: “clause (1), affine local case: Tⁿ • carries weight zero onto weight n”.

> **Clause (1) of Stacks 0FUH, affine locally**: multiplication by `Tⁿ` is an isomorphism from
> the weight-zero part of `Ω^p_{A[T;T⁻¹]/R}` onto its weight-`n` part, for every integer `n`.  It
> is the local form of `Ω^p_{L^⋆/S, n} = Ω^p_{L^⋆/S, 0} ⊗ L^{⊗n}`, the trivialization of `L^{⊗n}`
> over the affine being `Tⁿ`.

```lean
def weightComponentSmulEquiv (n : ℤ) (p : ℕ) :
    ↥(weightComponent R A 0 p) ≃ₗ[R] ↥(weightComponent R A n p)
```

**`PolynomialDeRham.deRhamComplexWeightZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/WeightComparison.lean, line 771](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/WeightComparison.lean#L771). The attribute's comment: “clause (2), affine local case; the printed subscript L/X is a typo for L/S”.

> **Clause (2) of Stacks 0FUH, affine locally**: the de Rham complex of `A` over `R` is the
> weight-zero part of the de Rham complex of `A[X]` over `R`, through the pullback of forms.  It is
> the local form of `Ω^•_{X/S} = Ω^•_{L/S, 0}`.

```lean
def deRhamComplexWeightZeroIso : deRhamComplex R A ≅ deRhamComplexWeightZero R A
```

**`PolynomialDeRham.laurentWeightEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/WeightComparison.lean, line 912](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/WeightComparison.lean#L912). The attribute's comment: “clause (3), affine local case; the printed subscript L/X is a typo for L/S”.

> **Clause (3) of Stacks 0FUH, affine locally**: for `n > 0` the restriction of forms along
> `A[X] → A[T;T⁻¹]` is an isomorphism from the weight-`n` part of `Ω^p_{A[X]/R}` onto the weight-`n`
> part of `Ω^p_{A[T;T⁻¹]/R}`.  It is the local form of `Ω^p_{L/S, n} = Ω^p_{L^⋆/S, n}`; positivity
> of `n` is needed, since in weight `n ≤ 0` the form `Tⁿ dlog T` is not the restriction of a form on
> the total space.

```lean
def laurentWeightEquiv (n : ℕ) (hn : 0 < n) (p : ℕ) :
    ↥(weightComponent R A n p) ≃ₗ[R] ↥(LaurentDeRham.weightComponent R A (n : ℤ) p)
```

## Tag 0FUI, a lemma

[Tag 0FUI](https://stacks.math.columbia.edu/tag/0FUI) in the Stacks Project.

**`Stacks.LineBundle.Situation.quasiIso_deRhamPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpacePoincareLemma.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpacePoincareLemma.lean#L225). The attribute's comment: “first assertion: `Ω^•_{X/S} ⟶ π_*Ω^•_{L/S}` is a quasi-isomorphism when `S` lies over `Spec ℚ` (here over `Spec R` for any `ℚ`-algebra `R`)”.

> **Stacks Project, Tag 0FUI, first assertion.** Let `f : X ⟶ S` be a morphism of schemes with
> `S` lying over `Spec R` for a `ℚ`-algebra `R` — for instance `R = ℚ` — let `L` be an invertible
> `𝒪_X`-module and let `π : 𝕃 ⟶ X` be its total space. Then the canonical map
> `Ω^•_{X/S} ⟶ π_*Ω^•_{𝕃/S}` is a quasi-isomorphism.

```lean
theorem Situation.quasiIso_deRhamPushforward : QuasiIso D.deRhamPushforward
```

**`Stacks.LineBundle.Situation.isIso_deRhamCohomologyPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpacePoincareLemma.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/LineBundle/TotalSpacePoincareLemma.lean#L271). The attribute's comment: “second assertion: `H^*_dR(X/S) = H^*_dR(L/S)`, the pullback along `π` being an isomorphism in every degree, when `S` lies over `Spec ℚ` (here over `Spec R` for any `ℚ`-algebra `R`)”.

> **Stacks Project, Tag 0FUI, second assertion.** In the situation of
> `Stacks.LineBundle.Situation.quasiIso_deRhamPushforward`, pullback along the projection
> `π : 𝕃 ⟶ X` of the total space of the line bundle is an isomorphism
> `H^i_{dR}(X/S) ≅ H^i_{dR}(𝕃/S)` in every degree `i`.

```lean
theorem Situation.isIso_deRhamCohomologyPullback (i : ℤ) :
    IsIso (Scheme.Hom.deRhamCohomologyPullback D.totalSpaceToBase D.f
      (D.totalSpaceToBase ≫ D.f) (𝟙 D.S) D.totalSpaceToBase_comp i)
```

**`PolynomialDeRham.inclHomotopyEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/PolynomialQuasiIso.lean, line 913](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/PolynomialQuasiIso.lean#L913). The attribute's comment: “the affine case: the de Rham complex is unchanged by adjoining a variable”.

> **The Poincaré lemma for a polynomial algebra**: over a `ℚ`-algebra the inclusion
> `Ω^•_{A/R} → Ω^•_{A[X]/R}` is a homotopy equivalence, with homotopy inverse the map induced by
> evaluation at `0`.

```lean
def inclHomotopyEquiv : HomotopyEquiv (deRhamComplex R A) (deRhamComplex R A[X])
```

**`PolynomialDeRham.quasiIso_incl`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/PolynomialQuasiIso.lean, line 921](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/PolynomialQuasiIso.lean#L921). The attribute's comment: “the affine case, as a quasi-isomorphism”.

> The inclusion `Ω^•_{A/R} → Ω^•_{A[X]/R}` is a quasi-isomorphism.

```lean
instance quasiIso_incl : QuasiIso (incl R A)
```

## Tag 0FUJ, an example

[Tag 0FUJ](https://stacks.math.columbia.edu/tag/0FUJ) in the Stacks Project.

**`PolynomialDeRham.polynomialEquiv_oneEquiv_deRhamDifferential_zero_X_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean#L102). The attribute's comment: “the displayed decomposition of the de Rham complex of the affine line: d Xⁿ = n X^{n-1} dX”.

> **The decomposition of the de Rham complex of the affine line**: on the monomial basis the only
> differential of `Ω^•_{A[X]/A}` sends `Xⁿ` to `n X^{n-1} dX`.  Together with
> `PolynomialDeRham.subsingleton_exteriorPower_polynomial`, which says the complex stops after degree
> one, this is the direct sum `A ⊕ ⨁_{n ≥ 1} (A · Xⁿ --n--> A · X^{n-1} dX)`.

```lean
theorem polynomialEquiv_oneEquiv_deRhamDifferential_zero_X_pow (n : ℕ) :
    polynomialEquiv A (exteriorPower.oneEquiv A[X] (Ω[A[X]⁄A]) (deRhamDifferential (A := A) 0
        ((exteriorPower.zeroEquiv A[X] (Ω[A[X]⁄A])).symm ((X : A[X]) ^ n)))) =
      (n : A[X]) * (X : A[X]) ^ (n - 1)
```

**`PolynomialDeRham.not_quasiIso_incl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean#L193). The attribute's comment: “the counterexample: in characteristic p > 0 the Poincaré lemma 0FUI fails for the affine line over a field, so its ℚ-algebra hypothesis is necessary”.

> **The Poincaré lemma fails in positive characteristic.**  For a field `k` of characteristic
> `p > 0` the inclusion of de Rham complexes `Ω^•_{k/k} → Ω^•_{k[X]/k}` is not a quasi-isomorphism:
> the source vanishes in degree one, while the target has `X^{p-1} dX` as a non-exact closed form.
> So the hypothesis `ℚ ⊆ A` of `PolynomialDeRham.quasiIso_incl` cannot be dropped.
>
> This is the affine content of Stacks 0FUJ: taking `X = S = Spec(k)` and `L = 𝐀^1_k` in Stacks
> 0FUI, the map `Ω^•_{X/S} → π_*Ω^•_{L/S}` on global sections is exactly `incl k k`.

```lean
theorem not_quasiIso_incl (hp : p ≠ 0) : ¬ QuasiIso (incl k k)
```

**`PolynomialDeRham.not_finiteDimensional_ker_deRhamDifferential_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean#L210). The attribute's comment: “H⁰ of the de Rham complex of the affine line is infinite dimensional in characteristic p > 0”.

> In characteristic `p > 0` the closed degree-zero forms on `𝐀^1_k` are infinite dimensional:
> `H^0_{dR}(𝐀^1_k/k)` contains every `p`-th power substitution `expand k p f`, because
> `d/dX (expand k p f) = expand k p (df/dX) · p X^{p-1} = 0`.

```lean
theorem not_finiteDimensional_ker_deRhamDifferential_zero (hp : p ≠ 0) :
    ¬ FiniteDimensional k (LinearMap.ker (deRhamDifferential (A := k) (B := k[X]) 0))
```

**`PolynomialDeRham.not_finiteDimensional_deRhamCohomology_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DeRham/PolynomialCharP.lean#L242). The attribute's comment: “H¹ of the de Rham complex of the affine line is infinite dimensional in characteristic p > 0”.

> In characteristic `p > 0` the degree-one de Rham cohomology of `𝐀^1_k` is infinite dimensional:
> `f ↦ [expand k p f · X^{p-1} dX]` is an injective `k`-linear map out of `k[X]`, because the
> coefficient of a derivative in every degree `≡ -1 mod p` vanishes.

```lean
theorem not_finiteDimensional_deRhamCohomology_one (hp : p ≠ 0) :
    ¬ FiniteDimensional k (↥(⋀[k[X]]^1 (Ω[k[X]⁄k])) ⧸
      LinearMap.range (deRhamDifferential (A := k) (B := k[X]) 0))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.10, Tag 0FU8](https://stacks.math.columbia.edu/tag/0FU8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
