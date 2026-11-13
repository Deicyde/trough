---
declaration: section
origin: cited
lean: Stacks.ClosedSubschemeProjQuotient.projQuotientIso, Stacks.ClosedSubschemeProjQuotient.projQuotientIso_hom_comp_ambientHom, Stacks.AlgebraicGeometry.RelativeProjGradedIdeal.exists_iso_projQuotient_twistKer, AlgebraicGeometry.ProjectiveSpectrum.Proj.mem_idealOfClosedSubscheme_iff, AlgebraicGeometry.ProjectiveSpectrum.Proj.idealOfClosedSubscheme, AlgebraicGeometry.ProjectiveSpectrum.Proj.idealOfClosedSubscheme_isHomogeneous, Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.idealOfClosedSubscheme, Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.mem_idealOfClosedSubscheme_iff
statement: formalized
proof: formalized
---

# 31.32 Closed subschemes of relative proj

Section 31.32 of the Stacks Project, [Tag 084M](https://stacks.math.columbia.edu/tag/084M). 6 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0801, a lemma

[Tag 0801](https://stacks.math.columbia.edu/tag/0801) in the Stacks Project.

**`Stacks.ClosedSubschemeProjQuotient.projQuotientIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean#L243). The attribute's comment: “the absolute case, over an affine base”. References: EGA II (2.9.2), “more general”.

> **The isomorphism `Z ≅ Proj (𝒮 / I(Z))`.** It is the lift of `i` through the closed immersion
> `Stacks.ClosedSubschemeProjQuotient.ambientHom`, which is invertible because the two closed
> subschemes have the same ideal sheaf.

```lean
def projQuotientIso [CompactSpace (AlgebraicGeometry.Proj 𝒮)]
    {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮) [IsClosedImmersion i] :
    Z ≅ projQuotient 𝒮 i
```

**`Stacks.ClosedSubschemeProjQuotient.projQuotientIso_hom_comp_ambientHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean#L257). The attribute's comment: “the identification is over the ambient Proj; the absolute case, over an affine base”.

> **The isomorphism is canonical**: it is compatible with the two morphisms to `Proj 𝒮`, so it
> is an equality of closed subschemes of `Proj 𝒮` and not merely an abstract isomorphism.

```lean
theorem projQuotientIso_hom_comp_ambientHom [CompactSpace (AlgebraicGeometry.Proj 𝒮)]
    {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮) [IsClosedImmersion i] :
    (projQuotientIso 𝒮 i).hom ≫ ambientHom 𝒮 i = i
```

**`Stacks.AlgebraicGeometry.RelativeProjGradedIdeal.exists_iso_projQuotient_twistKer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/Identification.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/Identification.lean#L317). References: EGA II (2.9.2), “more general”; EGA II (3.6.2), “more general”.

> **Stacks Tag 0801.** Let `S` be a scheme, `𝒜` a quasi-coherent graded `𝒪_S`-algebra,
> `p : X = Proj_S(𝒜) ⟶ S` the relative homogeneous spectrum and `i : Z ⟶ X` a closed subscheme.
> Let `ℐ ⊆ 𝒜` be the kernel of the canonical map `𝒜 ⟶ ⨁_{d ≥ 0} p_*((i_*𝒪_Z)(d))`. If `p` is
> quasi-compact then `Z = Proj_S(𝒜/ℐ)`.
>
> The ideal is `Stacks.AlgebraicGeometry.RelativeProjGradedIdeal.twistKerGradedIdeal`, the
> degreewise kernel of the homogeneous-section map of Tag 01NR followed by the unit of the
> pullback–pushforward adjunction at `i`; the quotient is
> `Stacks.AlgebraicGeometry.RelativeProjGradedIdeal.quotAlgebra` and the closed immersion
> `Proj_S(𝒜/ℐ) ⟶ Proj_S(𝒜)` is `projQuotientHom`. The equality `Z = Proj_S(𝒜/ℐ)` of the source is
> read, as everywhere in this repository, as an isomorphism over the ambient relative Proj.
>
> The proof is `ker_eq_ker_projQuotientHom_twistKer` fed to `exists_iso_projQuotient_of_ker_eq`,
> which produces the isomorphism from the equality of ideal sheaves by
> `AlgebraicGeometry.IsClosedImmersion.lift` and `isIso_lift`.

```lean
theorem exists_iso_projQuotient_twistKer [IsClosedImmersion i]
    [QuasiCompact (relativeProj 𝒜).toBase] :
    ∃ e : Z ≅ (relativeProj (quotAlgebra 𝒜 (twistKerGradedIdeal 𝒜 D i))).scheme,
      e.hom ≫ projQuotientHom 𝒜 (twistKerGradedIdeal 𝒜 D i) = i
```

## Tag 0BXK, an example

[Tag 0BXK](https://stacks.math.columbia.edu/tag/0BXK) in the Stacks Project.

**`Stacks.ClosedSubschemeProjQuotient.projQuotientIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean#L243). The attribute's comment: “the first assertion: for `X = Proj 𝒮` quasi-compact, every closed subscheme `Z ⊆ X` has the form `V₊(I(Z))`”. References: EGA II (2.9.2), “more general”.

> **The isomorphism `Z ≅ Proj (𝒮 / I(Z))`.** It is the lift of `i` through the closed immersion
> `Stacks.ClosedSubschemeProjQuotient.ambientHom`, which is invertible because the two closed
> subschemes have the same ideal sheaf.

```lean
def projQuotientIso [CompactSpace (AlgebraicGeometry.Proj 𝒮)]
    {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮) [IsClosedImmersion i] :
    Z ≅ projQuotient 𝒮 i
```

**`Stacks.ClosedSubschemeProjQuotient.projQuotientIso_hom_comp_ambientHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedSubschemeProjQuotient/Saturation.lean#L257). The attribute's comment: “the first assertion: the identification `Z = V₊(I(Z))` is one of closed subschemes of `X = Proj 𝒮`, not merely an abstract isomorphism”.

> **The isomorphism is canonical**: it is compatible with the two morphisms to `Proj 𝒮`, so it
> is an equality of closed subschemes of `Proj 𝒮` and not merely an abstract isomorphism.

```lean
theorem projQuotientIso_hom_comp_ambientHom [CompactSpace (AlgebraicGeometry.Proj 𝒮)]
    {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮) [IsClosedImmersion i] :
    (projQuotientIso 𝒮 i).hom ≫ ambientHom 𝒮 i = i
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.mem_idealOfClosedSubscheme_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ProjClosedSubschemeKernel.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ProjClosedSubschemeKernel.lean#L240). The attribute's comment: “ideal\_of\_a\_closed\_subscheme”.

> An element of `S` lies in the ideal of a closed subscheme `Z ⊆ Proj 𝒮` exactly when, for
> every `n`, the section of `𝒪(n)` attached to its degree-`n` homogeneous component pulls back to
> zero on `Z`.

```lean
theorem mem_idealOfClosedSubscheme_iff {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮)
    [IsClosedImmersion i] (a : S) :
    a ∈ idealOfClosedSubscheme 𝒮 i ↔
      ∀ n : ℕ, pullbackGlobalSections i (twistingSheaf 𝒮 (n : ℤ))
        (degreeSection 𝒮 n (DirectSum.decompose 𝒮 a n)) = 0
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.idealOfClosedSubscheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ProjIdealOfClosedSubscheme.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ProjIdealOfClosedSubscheme.lean#L57). The attribute's comment: “ideal\_of\_a\_closed\_subscheme”.

> The ideal of a closed subscheme of `Proj 𝒮`, generated by the homogeneous elements whose
> canonical twisted sections vanish after pullback to the subscheme.

```lean
noncomputable def idealOfClosedSubscheme {Z : Scheme.{u}}
    (i : Z ⟶ Proj 𝒮) [IsClosedImmersion i] : Ideal S
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.idealOfClosedSubscheme_isHomogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/ProjIdealOfClosedSubscheme.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/ProjIdealOfClosedSubscheme.lean#L72). The attribute's comment: “ideal\_of\_a\_closed\_subscheme”.

> The ideal of a closed subscheme is homogeneous: it is generated by homogeneous elements.

```lean
theorem idealOfClosedSubscheme_isHomogeneous {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮)
    [IsClosedImmersion i] :
    (idealOfClosedSubscheme 𝒮 i).IsHomogeneous 𝒮
```

**`Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.idealOfClosedSubscheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean#L267). The attribute's comment: “ideal\_of\_a\_closed\_subscheme”.

> **Stacks 0BXK.** The homogeneous ideal of a closed subscheme of `Proj 𝒮`, generated by the
> homogeneous elements whose canonical twisted global section pulls back to zero on the
> subscheme.

```lean
public def idealOfClosedSubscheme {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮) [IsClosedImmersion i] :
    Ideal S
```

**`Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.mem_idealOfClosedSubscheme_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean#L278). The attribute's comment: “ideal\_of\_a\_closed\_subscheme”.

> **Stacks 0BXK.** An element lies in the ideal of `Z` exactly when the section attached to
> each of its homogeneous components pulls back to zero on `Z`.
>
> In particular the span of the homogeneous equations is the kernel of the canonical graded map
> to the twisted global sections, in every degree and also on inhomogeneous elements.

```lean
public theorem mem_idealOfClosedSubscheme_iff {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮)
    [IsClosedImmersion i] (a : S) :
    a ∈ idealOfClosedSubscheme 𝒮 i ↔
      ∀ n : ℕ, pullbackGlobalSections i (twistingSheaf 𝒮 (n : ℤ))
        (degreeSection 𝒮 n ((DirectSum.decompose 𝒮 a) n)) = 0
```

**`Stacks.AlgebraicGeometry.IdealOfClosedSubscheme.idealOfClosedSubscheme_isHomogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/IdealOfClosedSubscheme/Basic.lean#L306). The attribute's comment: “ideal\_of\_a\_closed\_subscheme”.

> **Stacks 0BXK.** The ideal of a closed subscheme is homogeneous.

```lean
public theorem idealOfClosedSubscheme_isHomogeneous {Z : Scheme.{u}} (i : Z ⟶ Proj 𝒮)
    [IsClosedImmersion i] : (idealOfClosedSubscheme 𝒮 i).IsHomogeneous 𝒮
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.forall_degreeSection_quotientGradingMk_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/GeneralDegree.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/GeneralDegree.lean#L275). The attribute's comment: “for `d` the lcm of the degrees of generators of `A` over `A_0`, `I(V_+(I)) = {x ∈ A | A_{nd} x ⊂ I for all n ≫ 0}`; `𝒪_{V_+(I)}(n)` is the twisting sheaf of `V_+(I) = Proj(A/I)`, the reading in which the source derives this from Cohomology of Schemes tag 0BXF applied to `A/I`”.

> **Stacks 0BXK for a graded ring that is not generated in degree one: the ideal of equations of
> `V₊(I)` is the set of elements that `𝒮 (n · d)` carries into `I` for every `n ≫ 0`**, where `d` is
> the least common multiple of the degrees of a finite family of homogeneous generators of `S` over
> `𝒮 0`:
>
> `I(V₊(I)) = {x ∈ A | A_{nd} x ⊆ I for all n ≫ 0}`.
>
> An element lies in `I(V₊(I)) = Ker(A ⟶ ⨁_{n ≥ 0} Γ(V₊(I), 𝒪_{V₊(I)}(n)))` exactly when the
> twisted section attached to the class of each of its homogeneous components vanishes on
> `V₊(I) = Proj (𝒮 ⧸ I)`; both sides of the formula are degreewise conditions, and the finitely
> many components are matched by taking the largest of their exponents.

```lean
theorem forall_degreeSection_quotientGradingMk_eq_zero_iff [IsNoetherianRing S] {ι : Type*}
    [Fintype ι] (g : ι → S) (e : ι → ℕ) (he : ∀ j, 0 < e j) (hg : ∀ j, g j ∈ 𝒮 (e j))
    (hgen : Algebra.adjoin (𝒮 0) (Set.range g) = ⊤) (x : S) :
    (∀ n : ℕ, degreeSection (quotientGrading I) n
        (quotientGradingMk I n (decompose 𝒮 x n)) = 0) ↔
      ∃ N : ℕ, ∀ m : ℕ, N ≤ m →
        ∀ y : S, y ∈ 𝒮 (m * Finset.univ.lcm e) → y * x ∈ I.toIdeal
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.setOf_forall_degreeSection_quotientGradingMk_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/GeneralDegree.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/GeneralDegree.lean#L312). The attribute's comment: “for `d` the lcm of the degrees of generators of `A` over `A_0`, `I(V_+(I)) = {x ∈ A | A_{nd} x ⊂ I for all n ≫ 0}`; `𝒪_{V_+(I)}(n)` is the twisting sheaf of `V_+(I) = Proj(A/I)`, the reading in which the source derives this from Cohomology of Schemes tag 0BXF applied to `A/I`”.

> **The same, as the equality of sets the source displays:**
>
> `I(V₊(I)) = {x ∈ A | A_{nd} x ⊂ I for all n ≫ 0}`.

```lean
theorem setOf_forall_degreeSection_quotientGradingMk_eq_zero [IsNoetherianRing S] {ι : Type*}
    [Fintype ι] (g : ι → S) (e : ι → ℕ) (he : ∀ j, 0 < e j) (hg : ∀ j, g j ∈ 𝒮 (e j))
    (hgen : Algebra.adjoin (𝒮 0) (Set.range g) = ⊤) :
    {x : S | ∀ n : ℕ, degreeSection (quotientGrading I) n
        (quotientGradingMk I n (decompose 𝒮 x n)) = 0} =
      {x : S | ∃ N : ℕ, ∀ m : ℕ, N ≤ m →
        ∀ y : S, y ∈ 𝒮 (m * Finset.univ.lcm e) → y * x ∈ I.toIdeal}
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.mem_idealOfClosedSubscheme_projMap_quotientMk_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/VPlus.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/VPlus.lean#L208). The attribute's comment: “standard\_saturation”.

> **The saturation formula for the ideal of equations of `V₊(I)`.** Over a Noetherian graded
> ring generated by `𝒮 1` over `𝒮 0`, an element of `S` is an equation for the closed subscheme
> `V₊(I) = Proj (𝒮 ⧸ I)` exactly when one whole homogeneous component `𝒮 N` multiplies it into
> `I`:
>
> `I(V₊(I)) = {x ∈ S | 𝒮 N · x ⊆ I for some N}`.

```lean
theorem mem_idealOfClosedSubscheme_projMap_quotientMk_iff [IsNoetherianRing S]
    (hgen : Algebra.adjoin (𝒮 0) ((𝒮 1 : Set S)) = ⊤) (x : S) :
    x ∈ idealOfClosedSubscheme 𝒮 (Proj.map (quotientMk I) hq) ↔
      ∃ N : ℕ, ∀ y : S, y ∈ 𝒮 N → y * x ∈ I.toIdeal
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.coe_idealOfClosedSubscheme_projMap_quotientMk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/VPlus.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/VPlus.lean#L244). The attribute's comment: “standard\_saturation”.

> **The saturation formula as an equality of sets**, the shape in which the source displays it:
>
> `I(V₊(I)) = {x ∈ S | 𝒮 N · x ⊆ I for some N ≥ 0}`.

```lean
theorem coe_idealOfClosedSubscheme_projMap_quotientMk [IsNoetherianRing S]
    (hgen : Algebra.adjoin (𝒮 0) ((𝒮 1 : Set S)) = ⊤) :
    ((idealOfClosedSubscheme 𝒮 (Proj.map (quotientMk I) hq) : Ideal S) : Set S) =
      {x : S | ∃ N : ℕ, ∀ y : S, y ∈ 𝒮 N → y * x ∈ I.toIdeal}
```

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.exists_closedImmersion_idealOfClosedSubscheme_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/VPlus.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/VPlus.lean#L269). The attribute's comment: “saturated\_ideals”.

> **A homogeneous ideal is the ideal of equations of a closed subscheme of `Proj 𝒮` exactly
> when it is saturated.** One direction is
> `AlgebraicGeometry.ProjectiveSpectrum.Proj.saturated_idealOfClosedSubscheme`, that an ideal of
> equations is saturated; the other takes `Z = V₊(I)` and reads off the saturation formula.
>
> "Saturated" is spelled as the source does, as the equality of `I` with its own saturation.

```lean
theorem exists_closedImmersion_idealOfClosedSubscheme_eq_iff [IsNoetherianRing S]
    (hgen : Algebra.adjoin (𝒮 0) ((𝒮 1 : Set S)) = ⊤) :
    (∃ (Z : Scheme.{u}) (i : Z ⟶ Proj 𝒮) (_ : IsClosedImmersion i),
        idealOfClosedSubscheme 𝒮 i = I.toIdeal) ↔
      (I.toIdeal : Set S) = {x : S | ∃ N : ℕ, ∀ y : S, y ∈ 𝒮 N → y * x ∈ I.toIdeal}
```

**`Stacks.WeightedProjSaturation.X_one_dvd_of_mem_grading`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean#L141). The attribute's comment: “the counterexample of the last paragraph, `A = ℚ[x, y]` with `deg x = 2` and `deg y = 3`: for homogeneous `f` with `6 ∣ deg (f y)` one has `y ∣ f`”.

> **Stacks 0BXK, in the counterexample of its last paragraph: a homogeneous `f` with
> `6 ∣ deg(f · y)` is divisible by `y`.** Every monomial `x^a y^b` of `f` has `2a + 3b = n` with
> `n + 3` divisible by `6`, so `n` is odd, so `b` is odd and in particular nonzero.

```lean
theorem X_one_dvd_of_mem_grading (n : ℕ) (f : MvPolynomial (Fin 2) ℚ) (hf : f ∈ grading n)
    (h6 : 6 ∣ n + 3) : (MvPolynomial.X 1 : MvPolynomial (Fin 2) ℚ) ∣ f
```

**`Stacks.WeightedProjSaturation.mul_X_one_mem_squareIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean#L151). The attribute's comment: “the counterexample of the last paragraph: for homogeneous `f` with `6 ∣ deg (f y)` one has `f y ∈ I = (y²)`”.

> **Stacks 0BXK, in the counterexample of its last paragraph: hence `f · y ∈ I = (y²)`.**

```lean
theorem mul_X_one_mem_squareIdeal (n : ℕ) (f : MvPolynomial (Fin 2) ℚ) (hf : f ∈ grading n)
    (h6 : 6 ∣ n + 3) :
    f * (MvPolynomial.X 1 : MvPolynomial (Fin 2) ℚ) ∈ squareIdeal
```

**`Stacks.WeightedProjSaturation.mem_squareIdeal_of_mem_span_X_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean#L164). The attribute's comment: “the counterexample of the last paragraph: `(A y)_{6n} ⊆ I` for `I = (y²)`, the degreewise test `y` passes”.

> **The degreewise test of Stacks 0BXK's general formula, for `y` in this ring:
> `(A · y)_{6n} ⊆ I` for every `n`.** An element of the ideal `(y)` that is homogeneous of a degree
> divisible by `6` already lies in `(y²)`: divisibility by `y` makes the exponent `b` of `y` in
> every monomial positive, and `2a + 3b = 6n` makes it even, so it is at least `2`.

```lean
theorem mem_squareIdeal_of_mem_span_X_one (n : ℕ) (z : MvPolynomial (Fin 2) ℚ)
    (hz : z ∈ Ideal.span {(MvPolynomial.X 1 : MvPolynomial (Fin 2) ℚ)})
    (hdeg : z ∈ grading (6 * n)) : z ∈ squareIdeal
```

**`Stacks.WeightedProjSaturation.X_zero_pow_mul_X_one_notMem_squareIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjSaturation/WeightedExample.lean#L189). The attribute's comment: “the counterexample of the last paragraph: `xⁿ y ∉ I` for every `n`, with `I = (y²)`”.

> **Stacks 0BXK, in the counterexample of its last paragraph: `xⁿ · y ∉ I` for every `n`.** The
> only monomial of `xⁿ y` carries the exponent `1` at `y`, which is less than `2`.

```lean
theorem X_zero_pow_mul_X_one_notMem_squareIdeal (n : ℕ) :
    (MvPolynomial.X 0 : MvPolynomial (Fin 2) ℚ) ^ n * MvPolynomial.X 1 ∉ squareIdeal
```

## Tag 0BXL, a lemma

[Tag 0BXL](https://stacks.math.columbia.edu/tag/0BXL) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.projectiveSpace_idealOfClosedSubscheme_isPrincipal_of_codimension_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CodimOneSubscheme/ProjHeightOne.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CodimOneSubscheme/ProjHeightOne.lean#L294).

> **Stacks Project, Tag 0BXL.** Let `R` be a Noetherian unique factorization domain and let `Z`
> be a closed subscheme of `P^n_R = Proj R[T₀, …, Tₙ]` which has no embedded points and every
> irreducible component of which has codimension one in `P^n_R`. Then the homogeneous ideal
> `I(Z) ⊆ R[T₀, …, Tₙ]` corresponding to `Z` is principal.
>
> A polynomial ring over a Noetherian UFD is a Noetherian UFD and is generated in degree one, so
> this is the general `Proj` statement
> `idealOfClosedSubscheme_isPrincipal_of_codimension_one`. For the conclusion in the form of a
> single homogeneous equation see
> `projectiveSpace_exists_homogeneous_eq_idealOfClosedSubscheme`.

```lean
theorem projectiveSpace_idealOfClosedSubscheme_isPrincipal_of_codimension_one (R : Type u)
    [CommRing R] [IsDomain R] [IsNoetherianRing R] [UniqueFactorizationMonoid R] (n : ℕ)
    {Z : Scheme.{u}} (i : Z ⟶ Proj (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) R))
    [IsClosedImmersion i] (hno : HasNoEmbeddedPoints Z)
    (hcodim : ∀ W ∈ irreducibleComponents Z, ∀ x : Z,
      IsGenericPoint x W → codimension (IrreducibleCloseds.closureSingleton (i.base x)) = 1) :
    (idealOfClosedSubscheme
      (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) R) i).IsPrincipal
```

## Tag 0802, a lemma

[Tag 0802](https://stacks.math.columbia.edu/tag/0802) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjTwists.exists_finiteType_degreeQuotientPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/FiniteTypeDegreeQuotientPresentation.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/FiniteTypeDegreeQuotientPresentation.lean#L68).

> **Stacks Project, Tag 0802.** A closed subscheme of finite presentation of a quasi-compact
> relative `Proj` over a quasi-compact quasi-separated base is the relative `Proj` of the quotient
> of `𝒜` by the graded ideal generated by a quasi-coherent finite type submodule `ℱ` of a single
> homogeneous piece `𝒜_d` with `d > 0`.
>
> The relative case of Tag 0801 — the graded-quotient presentation that
> `…RelativeProjGradedIdeal.exists_finiteType_degreeQuotientPresentation` consumes — is
> `…RelativeProjTwists.gradedQuotientPresentation`, so the statement carries no hypothesis beyond
> the tag's own.

```lean
public theorem exists_finiteType_degreeQuotientPresentation (A : SheafGradedAlgebra S)
    {Z : Scheme.{u}} (i : Z ⟶ (relativeProj A).scheme)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsClosedImmersion i]
    [QuasiCompact (relativeProj A).toBase]
    (hi : AlgebraicGeometry.FinitePresentation i) :
    ∃ d : ℕ, 0 < d ∧ ∃ ℱ : (A.piece (d : ℤ)).Submodule,
      ℱ.toSheafOfModules.IsQuasicoherent ∧
        SheafOfModules.IsFiniteType.{u, u, u} ℱ.toSheafOfModules ∧
          Nonempty (DegreeQuotientPresentation A i ℱ)
```

## Tag 0803, a lemma

[Tag 0803](https://stacks.math.columbia.edu/tag/0803) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjGradedIdeal.exists_finiteType_presentation_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/DegreePresenter.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/DegreePresenter.lean#L137).

> Let `S` be a quasi-compact and quasi-separated scheme, `𝒜` a
> quasi-coherent graded `𝒪_S`-algebra, `p : X = Proj_S(𝒜) ⟶ S` the relative homogeneous spectrum,
> `i : Z ⟶ X` a closed subscheme and `U ⊆ S` an open of the base. Assume
>
> 1. `p` is quasi-compact,
> 2. `i` is of finite presentation,
> 3. `U ∩ p(i(Z)) = ∅`,
> 4. `U` is quasi-compact, and
> 5. every graded piece `𝒜_n` is a finite type `𝒪_S`-module.
>
> Then there are `d > 0` and a quasi-coherent finite type `𝒪_S`-submodule `ℱ ⊆ 𝒜_d` such that
>
> (a) `Z = Proj_S(𝒜/ℱ𝒜)`, read as a `DegreeQuotientPresentation` — an identification of `Z` with
> the relative Proj of the quotient of `𝒜` by the graded ideal generated by `ℱ`, over `Proj_S(𝒜)`;
> and
>
> (b) the support of `𝒜_d/ℱ` does not meet `U`.

```lean
theorem exists_finiteType_presentation_supp (U : S.Opens)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsClosedImmersion i]
    [QuasiCompact (relativeProj A).toBase]
    (hi : AlgebraicGeometry.FinitePresentation i)
    (hU : (U : Set S) ∩ Set.range (i ≫ (relativeProj A).toBase).base = ∅)
    (hUc : IsCompact (U : Set S))
    (hA : ∀ n : ℕ, SheafOfModules.IsFiniteType.{u, u, u} (A.piece (n : ℤ))) :
    ∃ d : ℕ, 0 < d ∧ ∃ ℱ : (A.piece (d : ℤ)).Submodule,
      ℱ.toSheafOfModules.IsQuasicoherent ∧
        SheafOfModules.IsFiniteType.{u, u, u} ℱ.toSheafOfModules ∧
          (U : Set S) ∩ (⟨(cokernel ℱ.ι).val, (cokernel ℱ.ι).isSheaf⟩ :
              RingedSpace.ModuleSheaf.{u} S.toRingedSpace).supp = ∅ ∧
            Nonempty (DegreeQuotientPresentation A i ℱ)
```

**`Stacks.AlgebraicGeometry.RelativeProjTwists.exists_finiteType_presentation_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/FiniteTypePresentationOffSupport.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/RelativeProjGradedIdeal/FiniteTypePresentationOffSupport.lean#L81).

> **Stacks Project, Tag 0803.** Let `i : Z ⟶ Proj_S(𝒜)` be a closed subscheme of finite
> presentation of a quasi-compact relative `Proj` over a quasi-compact quasi-separated base, let
> `U` be a quasi-compact open of the base missing the image of `Z`, and let every `𝒜_n` be of
> finite type. Then `Z` is the relative `Proj` of the quotient of `𝒜` by the graded ideal generated
> by a quasi-coherent finite type submodule `ℱ` of a single homogeneous piece `𝒜_d` with `d > 0`,
> and `ℱ` may be chosen so that the support of `𝒜_d/ℱ` is disjoint from `U`.
>
> The relative case of Tag 0801 — the vanishing-ideal presentation that
> `…RelativeProjGradedIdeal.exists_finiteType_presentation_supp_of_vanishingIdeal` consumes — is
> `…RelativeProjTwists.vanishingIdealPresentation`, so the statement carries no hypothesis beyond
> the tag's own.

```lean
public theorem exists_finiteType_presentation_supp (A : SheafGradedAlgebra S) {Z : Scheme.{u}}
    (i : Z ⟶ (relativeProj A).scheme) (U : S.Opens)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsClosedImmersion i]
    [QuasiCompact (relativeProj A).toBase]
    (hi : AlgebraicGeometry.FinitePresentation i)
    (hU : (U : Set S) ∩ Set.range (i ≫ (relativeProj A).toBase).base = ∅)
    (hUc : IsCompact (U : Set S))
    (hA : ∀ n : ℕ, SheafOfModules.IsFiniteType.{u, u, u} (A.piece (n : ℤ))) :
    ∃ d : ℕ, 0 < d ∧ ∃ ℱ : (A.piece (d : ℤ)).Submodule,
      ℱ.toSheafOfModules.IsQuasicoherent ∧
        SheafOfModules.IsFiniteType.{u, u, u} ℱ.toSheafOfModules ∧
          (U : Set S) ∩ (⟨(cokernel ℱ.ι).val, (cokernel ℱ.ι).isSheaf⟩ :
              RingedSpace.ModuleSheaf.{u} S.toRingedSpace).supp = ∅ ∧
            Nonempty (DegreeQuotientPresentation A i ℱ)
```

## Tag 0B3V, a lemma

[Tag 0B3V](https://stacks.math.columbia.edu/tag/0B3V) in the Stacks Project.

**`Stacks.RelativeProj.isClosedImmersion_of_section_projectiveBundleToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Section.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/Section.lean#L61). The attribute's comment: “closed immersion”.

> **A section of the projection of a projective bundle is a closed immersion.** Since
> `π : 𝐏(F) ⟶ X` is separated (Tag 01O2) and `σ ≫ π = 𝟙 X` is an isomorphism, `σ` is a closed
> immersion.

```lean
theorem isClosedImmersion_of_section_projectiveBundleToBase (X : Scheme.{u}) (F : X.Modules)
    [F.IsQuasicoherent] (σ : X ⟶ projectiveBundle X F)
    (hσ : σ ≫ projectiveBundleToBase X F = 𝟙 X) : IsClosedImmersion σ
```

**`Stacks.RelativeProj.sectionOfInvertibleQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionOfQuotient.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionOfQuotient.lean#L339). The attribute's comment: “from an invertible quotient to a section: the construction”.

> **A surjection `q : E ⟶ ℒ` onto an invertible `𝒪_X`-module determines a section of
> `π : 𝐏(E) ⟶ X`.** This is the direction of Tag 0B3V's bijection that produces a section: `q`
> determines a unital homomorphism `(𝟙_X)^*Sym(E) ⟶ ⨁_n ℒ^{⊗ n}` of sheaves of graded algebras
> whose degree-one component is surjective — a quadruple of Section 01NS of degree one over
> `𝟙_X` — and the representability of the functor of quadruples classifies that quadruple by a
> morphism `X ⟶ 𝐏(E)` over `X`.

```lean
def sectionOfInvertibleQuotient [Epi q] : X ⟶ projectiveBundle X E
```

**`Stacks.RelativeProj.sectionOfInvertibleQuotient_comp_projectiveBundleToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionOfQuotient.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionOfQuotient.lean#L345). The attribute's comment: “from an invertible quotient to a section: it is a section of the projection”.

> **The morphism of `sectionOfInvertibleQuotient` is a section of `π : 𝐏(E) ⟶ X`.**

```lean
theorem sectionOfInvertibleQuotient_comp_projectiveBundleToBase [Epi q] :
    sectionOfInvertibleQuotient X E L q ≫ projectiveBundleToBase X E = 𝟙 X
```

**`Stacks.RelativeProj.exists_iso_of_sectionOfInvertibleQuotient_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionOfQuotient.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveBundle/SectionOfQuotient.lean#L412). The attribute's comment: “from an invertible quotient to a section: the map is injective, i.e. a section determines the invertible quotient it comes from up to isomorphism of the quotient module”.

> **Two surjections onto invertible modules determining the same section of `π` differ by an
> isomorphism of their targets.** This is the injectivity of Tag 0B3V's map from invertible
> quotients to sections: the two quadruples are strictly equivalent, which gives an isomorphism
> `β : ℒ ≅ ℒ'` carrying one twisting to the other, and in degree one that equation — precomposed
> with the pullback of the degree-one generator of `Sym(E)` and postcomposed with the
> identification `(ℒ')^{⊗ 1} ≅ ℒ'` — is `q ≫ β = q'`.

```lean
theorem exists_iso_of_sectionOfInvertibleQuotient_eq [Epi q]
    (L' : SheafOfModules.{u} (structureRingSheaf X.toRingedSpace))
    [Stacks.SheafOfModules.IsInvertible X.toRingedSpace.presheaf (isSheafStruct X) L']
    (q' : E ⟶ L') [Epi q']
    (h : sectionOfInvertibleQuotient X E L q = sectionOfInvertibleQuotient X E L' q') :
    ∃ α : L ≅ L', q ≫ α.hom = q'
```

**`Stacks.RelativeProj.projectiveBundle_sections_classification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleConormal/SectionsClause.lean, line 656](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveBundleConormal/SectionsClause.lean#L656). References: EGA II (4.2.10), “special case”; EGA II (4.2.3), “Case Y = X”; SGA 4 XVIII (1.3.3), “partial”.

> **[Stacks, Tag 0B3V].** Let `X` be a scheme, `ℰ` a quasi-coherent `𝒪_X`-module and
> `π : 𝐏(ℰ) ⟶ X` its projective bundle (`projectiveBundle`, `projectiveBundleToBase`), with
> tautological quotient `π^*ℰ ⟶ 𝒪(1)` (`tautologicalDatum ℰ`). Then:
>
> 1. **the bijection**: `projectiveBundleSectionsEquiv` is a bijection from the sections `σ` of `π`
>    onto the invertible quotients `q : ℰ → 𝓛` up to isomorphism, sending `σ` to the class of
>    `σ^*` of the tautological quotient — `σ` goes to the class of `q` exactly when there is
>    `e : σ^*𝒪(1) ≅ 𝓛` carrying `σ^*` of the tautological quotient to `q`;
> 2. every section `σ` is a closed immersion;
> 3. **the canonical isomorphism** `projectiveBundleConormalIso : Ker(q) ⊗ 𝓛^{⊗ -1} ≅ 𝒞_{σ(X)/𝐏(ℰ)}`
>    for `σ` matched with `q` through `e`, whose underlying map is the canonical map
>    `Stacks.ProjectiveBundleConormal.conormalCanonicalMap` (locally `k ⊗ s^{-1} ↦ k/s`) read
>    through the base-change map of conormal sheaves along the presentation comparison
>    `bundlePresentationIso` of `𝐏(ℰ)`;
> 4. **compatibility with base change** along any morphism `g : X' ⟶ X`, for sections lying over
>    each other along `projectiveBundleBaseChange`: the bijection sends `σ'` to the base change
>    `Stacks.ProjectiveBundleQuotients.baseChangeClass` of the class of `σ`; and the square formed
>    by `g^*` of the canonical isomorphism at `σ`, the canonical isomorphism at `σ'`, the base
>    change `Stacks.Divisors.conormalSourceBaseChange` of the source and the base-change map
>    `Stacks.Conormal.conormalBaseChangeMap` of conormal sheaves commutes.
>
> No hypothesis is placed on `X`, `X'`, `g`, or on `ℰ` beyond quasi-coherence.

```lean
theorem projectiveBundle_sections_classification :
    (∀ (σ : X ⟶ projectiveBundle X E) (hσ : σ ≫ projectiveBundleToBase X E = 𝟙 X)
        (Q : Stacks.Divisors.InvertibleQuotient X E),
      projectiveBundleSectionsEquiv ⟨σ, hσ⟩ =
          Quotient.mk (Stacks.Divisors.invertibleQuotientSetoid X E) Q ↔
        ∃ e : (Scheme.Modules.pullback σ).obj (tautologicalDatum E).twist ≅ Q.L,
          (tautologicalDatum E).pullbackQuotientMap σ hσ ≫ e.hom = Q.q) ∧
    (∀ (σ : X ⟶ projectiveBundle X E), σ ≫ projectiveBundleToBase X E = 𝟙 X →
      IsClosedImmersion σ) ∧
    (∀ (Q : Stacks.Divisors.InvertibleQuotient X E) (σ : X ⟶ projectiveBundle X E)
        (hσ : σ ≫ projectiveBundleToBase X E = 𝟙 X)
        (e : (Scheme.Modules.pullback σ).obj (tautologicalDatum E).twist ≅ Q.L)
        (hqe : (tautologicalDatum E).pullbackQuotientMap σ hσ ≫ e.hom = Q.q),
      haveI := isClosedImmersion_of_section_projectiveBundleToBase X E σ hσ
      (projectiveBundleConormalIso E Q hσ e hqe).hom =
        conormalCanonicalMap E Q (presentationSection_comp_toBase E σ hσ)
            (presentationClassifyingIso E Q e)
            (sectionQuotientMap_comp_presentationClassifyingIso E Q hσ e hqe) ≫
          (Scheme.Modules.pullbackId X).inv.app _ ≫
            Stacks.Conormal.conormalBaseChangeMap (presentationSection_square E σ)) ∧
    (∀ (X' : Scheme.{u}) (g : X' ⟶ X) (σ : X ⟶ projectiveBundle X E)
        (hσ : σ ≫ projectiveBundleToBase X E = 𝟙 X)
        (σ' : X' ⟶ projectiveBundle X' ((Scheme.Modules.pullback g).obj E))
        (hσ' : σ' ≫ projectiveBundleToBase X' ((Scheme.Modules.pullback g).obj E) = 𝟙 X'),
        σ' ≫ projectiveBundleBaseChange g E _ (Iso.refl _) = g ≫ σ →
      projectiveBundleSectionsEquiv ⟨σ', hσ'⟩ =
        Stacks.ProjectiveBundleQuotients.baseChangeClass g (Iso.refl _)
          (projectiveBundleSectionsEquiv ⟨σ, hσ⟩)) ∧
    (∀ (X' : Scheme.{u}) (g : X' ⟶ X) (E' : X'.Modules) [E'.IsQuasicoherent]
        (hE : E' ≅ (Scheme.Modules.pullback g).obj E)
        (Q : Stacks.Divisors.InvertibleQuotient X E)
        (Q' : Stacks.Divisors.InvertibleQuotient X' E')
        (hL : Q'.L ≅ (Scheme.Modules.pullback g).obj Q.L)
        (hq : Q'.q ≫ hL.hom = hE.hom ≫ (Scheme.Modules.pullback g).map Q.q)
        (σ : X ⟶ projectiveBundle X E) (hσ : σ ≫ projectiveBundleToBase X E = 𝟙 X)
        (e : (Scheme.Modules.pullback σ).obj (tautologicalDatum E).twist ≅ Q.L)
        (hqe : (tautologicalDatum E).pullbackQuotientMap σ hσ ≫ e.hom = Q.q)
        (σ' : X' ⟶ projectiveBundle X' E') (hσ' : σ' ≫ projectiveBundleToBase X' E' = 𝟙 X')
        (e' : (Scheme.Modules.pullback σ').obj (tautologicalDatum E').twist ≅ Q'.L)
        (hqe' : (tautologicalDatum E').pullbackQuotientMap σ' hσ' ≫ e'.hom = Q'.q)
        (comm : σ' ≫ projectiveBundleBaseChange g E E' hE = g ≫ σ),
      haveI := isClosedImmersion_of_section_projectiveBundleToBase X E σ hσ
      haveI := isClosedImmersion_of_section_projectiveBundleToBase X' E' σ' hσ'
      (Stacks.Divisors.conormalSourceBaseChange g E E' hE Q Q' hL hq).hom ≫
          (projectiveBundleConormalIso E' Q' hσ' e' hqe').hom =
        (Scheme.Modules.pullback g).map (projectiveBundleConormalIso E Q hσ e hqe).hom ≫
          Stacks.Conormal.conormalBaseChangeMap comm)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.32, Tag 084M](https://stacks.math.columbia.edu/tag/084M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
