---
declaration: section
origin: cited
lean: AlgebraicGeometry.genericallyEtale_tfae, AlgebraicGeometry.two_mul_genus_sub_two_eq_degreeOver_mul_add_of_exists_etale, AlgebraicGeometry.two_mul_genus_sub_two_eq_degreeOver_mul_add, AlgebraicGeometry.differential_uniformizer_basis, AlgebraicGeometry.two_mul_genus_sub_two_eq_degreeOver_mul_add_finsum, AlgebraicGeometry.multiplicity_kaehlerDifferent_eq_length_stalk, AlgebraicGeometry.ramificationIdx_sub_one_le_multiplicity_kaehlerDifferent, AlgebraicGeometry.multiplicity_kaehlerDifferent_eq_iff
statement: formalized
proof: formalized
---

# 53.12 Riemann-Hurwitz

Section 53.12 of the Stacks Project, [Tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C1C, a lemma

[Tag 0C1C](https://stacks.math.columbia.edu/tag/0C1C) in the Stacks Project.

**`AlgebraicGeometry.genericallyEtale_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitz.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitz.lean#L491).

> **Stacks Project, Tag 0C1C.** For a morphism `f : X ⟶ Y` of smooth curves over a field `k`
> the following are equivalent: the differential `f^*Ω_{Y/k} ⟶ Ω_{X/k}` is nonzero; the sheaf
> `Ω_{X/Y}` is supported on a proper closed subset of `X`; `f` is unramified on a nonempty open;
> `f` is étale on a nonempty open; `f` is dominant and the extension of function fields it induces
> is finite separable.

```lean
theorem genericallyEtale_tfae
    {k : Type u} [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY] [Smooth pX] [Smooth pY]
    (f : X ⟶ Y) (hf : f ≫ pY = pX) :
    List.TFAE [
      Scheme.Hom.relativeDifferentialsMap f pY pX (𝟙 (Spec (.of k)))
        (by simpa using hf) ≠ 0,
      ∃ Z : Set X, IsClosed Z ∧ Z ≠ Set.univ ∧
        SheafOfModules.supp (Scheme.Hom.relativeDifferentials f) ⊆ Z,
      ∃ U : X.Opens, Nonempty U ∧ Unramified (U.ι ≫ f),
      ∃ U : X.Opens, Nonempty U ∧ Etale (U.ι ≫ f),
      IsDominant f ∧
        (letI : Algebra (Y.residueField (f (genericPoint X)))
            (X.residueField (genericPoint X)) :=
          (f.residueFieldMap (genericPoint X)).hom.toAlgebra
         Module.Finite (Y.residueField (f (genericPoint X)))
            (X.residueField (genericPoint X)) ∧
         Algebra.IsSeparableExtension (Y.residueField (f (genericPoint X)))
            (X.residueField (genericPoint X)))]
```

## Tag 0C1D, a lemma

[Tag 0C1D](https://stacks.math.columbia.edu/tag/0C1D) in the Stacks Project.

**`AlgebraicGeometry.two_mul_genus_sub_two_eq_degreeOver_mul_add_of_exists_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DifferentialsDegreeGenus.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/DifferentialsDegreeGenus.lean#L97).

> **Stacks Project, Tag 0C1D (Riemann–Hurwitz).** Let `f : X ⟶ Y` be a morphism of smooth
> proper curves over a field `k` satisfying the equivalent conditions of Tag 0C1C (here (4): `f` is
> étale on a nonempty open), with `k = H⁰(Y, 𝒪_Y) = H⁰(X, 𝒪_X)`, and let `X`, `Y` have genus
> `g_X`, `g_Y`. Then
>
> `2g_X - 2 = (2g_Y - 2) deg(f) + deg(R)`,
>
> where `R ⊆ X` is the effective Cartier divisor cut out by the different of `f`, of degree
> `dim_k Γ(R, 𝒪_R)`, and `deg(f) = [k(X) : k(Y)]`.

```lean
theorem two_mul_genus_sub_two_eq_degreeOver_mul_add_of_exists_etale (hf : f ≫ pY = pX)
    (hgen : ∃ U : X.Opens, Nonempty U ∧ Etale (U.ι ≫ f)) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isCurve_comp k pX pY f hf
    letI : IsDominant f := isDominant_of_exists_etale_comp_ι pX pY f hf hgen
    letI : Algebra k Γ((Stacks.Discriminant.kaehlerDifferent f).subscheme, ⊤) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫
        ((Stacks.Discriminant.kaehlerDifferent f).subschemeι ≫ pX).appTop).hom.toAlgebra
    2 * (genus pX : ℤ) - 2 =
      (2 * (genus pY : ℤ) - 2) * (degreeOver f : ℤ) +
        (Module.finrank k Γ((Stacks.Discriminant.kaehlerDifferent f).subscheme, ⊤) : ℤ)
```

**`AlgebraicGeometry.two_mul_genus_sub_two_eq_degreeOver_mul_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzFormula.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzFormula.lean#L373). The attribute's comment: “the different is the Kähler different, which is the different of Tag 0BW4 by Tag 0BWG; the conditions of Tag 0C1C are stated as its condition (1)”.

> **Stacks Project, Tag 0C1D (Riemann–Hurwitz).** Let `f : X → Y` be a morphism of smooth
> proper curves over a field `k` whose differential `f^*Ω_{Y/k} → Ω_{X/k}` is nonzero (condition (1)
> of [Stacks, Tag 0C1C]), with `H⁰(X, 𝒪_X) = k = H⁰(Y, 𝒪_Y)`, and let `R ⊆ X` be the closed
> subscheme cut out by the different of `f`. Then `2g_X - 2 = (2g_Y - 2) deg(f) + deg(R)`, where
> `deg(R) = dim_k Γ(R, 𝒪_R)`.

```lean
theorem two_mul_genus_sub_two_eq_degreeOver_mul_add [IsProper pY]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ pX.appTop)]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ pY.appTop)]
    (hdf : Scheme.Hom.relativeDifferentialsMap f pY pX (𝟙 (Spec (.of k)))
      (by simpa using hf) ≠ 0) :
    letI := locallyOfFiniteType_of_isCurve_comp k pX pY f hf
    letI : IsDominant f := isDominant_of_relativeDifferentialsMap_ne_zero pX pY f hf hdf
    letI : Algebra k Γ((kaehlerDifferent f).subscheme, ⊤) :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ ((kaehlerDifferent f).subschemeι ≫ pX).appTop).hom.toAlgebra
    2 * (genus pX : ℤ) - 2 =
      (2 * (genus pY : ℤ) - 2) * (degreeOver f : ℤ) +
        Module.finrank k Γ((kaehlerDifferent f).subscheme, ⊤)
```

## Tag 0C1E, a lemma

[Tag 0C1E](https://stacks.math.columbia.edu/tag/0C1E) in the Stacks Project.

**`AlgebraicGeometry.differential_uniformizer_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/UniformizerDifferential.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/UniformizerDifferential.lean#L206).

> **Stacks Project, Tag 0C1E.** At a closed point of a scheme over a field, smooth there of
> relative dimension one and with separable residue field, the differential of any uniformizer
> freely generates the stalk of relative differentials.

```lean
theorem differential_uniformizer_basis
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    (x : X) (hx : IsClosed ({x} : Set X))
    (hsm : InfinitesimalLifting.SmoothAt f x)
    (hdim : topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = 1)
    (hsep :
      letI : Algebra k (X.residueField x) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫ X.Γevaluation x).hom.toAlgebra
      Algebra.IsSeparable k (X.residueField x))
    (s : X.presheaf.stalk x)
    (hs : maximalIdeal (X.presheaf.stalk x) = Ideal.span {s})
    (U : X.Opens) (hxU : x ∈ U) (a : X.presheaf.obj (op U))
    (hsa : ((X.presheaf.germ U x hxU).hom a) = s) :
    letI := relativeDifferentialStalkModule f x
    ∃ e : X.presheaf.stalk x ≃ₗ[X.presheaf.stalk x] relativeDifferentialStalk f x,
      e 1 =
        (TopCat.Presheaf.germ (C := AddCommGrpCat.{u})
            (Scheme.Hom.relativeDifferentials f).val.presheaf U x hxU)
          ((Scheme.Hom.universalRelativeDerivation f).d a)
```

## Tag 0C1F, a lemma

[Tag 0C1F](https://stacks.math.columbia.edu/tag/0C1F) in the Stacks Project.

**`AlgebraicGeometry.two_mul_genus_sub_two_eq_degreeOver_mul_add_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzFormula.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzFormula.lean#L401). The attribute's comment: “the formula 2g_X - 2 = (2g_Y - 2) deg(f) + Σ d_x [κ(x) : k] over the closed points x; the different is the Kähler different, which is the different of Tag 0BW4 by Tag 0BWG”.

> **Stacks Project, Tag 0C1F, the formula.** Under the assumptions of [Stacks, Tag 0C1D],
> `2g_X - 2 = (2g_Y - 2) deg(f) + ∑_x d_x [κ(x) : k]`, the sum over the closed points `x` of `X`,
> where `d_x = length_{𝒪_{X,x}}(𝒪_{X,x} / 𝓘_{R,x})` is the multiplicity of `x` in the closed
> subscheme `R` cut out by the different of `f`.

```lean
theorem two_mul_genus_sub_two_eq_degreeOver_mul_add_finsum [IsProper pY]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ pX.appTop)]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ pY.appTop)]
    (hdf : Scheme.Hom.relativeDifferentialsMap f pY pX (𝟙 (Spec (.of k)))
      (by simpa using hf) ≠ 0) :
    letI := locallyOfFiniteType_of_isCurve_comp k pX pY f hf
    letI : IsDominant f := isDominant_of_relativeDifferentialsMap_ne_zero pX pY f hf hdf
    2 * (genus pX : ℤ) - 2 =
      (2 * (genus pY : ℤ) - 2) * (degreeOver f : ℤ) +
        ((∑ᶠ x : {x : X // IsClosed ({x} : Set X)},
          letI : Algebra k (X.presheaf.stalk x.1) :=
            ((Scheme.ΓSpecIso (.of k)).inv ≫ pX.appTop ≫
              X.presheaf.germ ⊤ x.1 (by simp)).hom.toAlgebra
          (Module.length (X.presheaf.stalk x.1)
              (X.presheaf.stalk x.1 ⧸ IdealSheafData.stalk (kaehlerDifferent f) x.1)).toNat *
            Module.finrank k (IsLocalRing.ResidueField (X.presheaf.stalk x.1)) : ℕ) : ℤ)
```

**`AlgebraicGeometry.multiplicity_kaehlerDifferent_eq_length_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzLocal.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzLocal.lean#L302). The attribute's comment: “(1): `d_x = length_{𝒪_{X,x}}(Ω_{X/Y,x})`, for a dominant morphism of smooth curves; the different is the Kähler different, which is the different of Tag 0BW4 by Tag 0BWG”.

> **Stacks Project, Tag 0C1F, part (1).** Let `f : X → Y` be a dominant morphism of smooth
> curves over a field and `x ∈ X` a closed point. The multiplicity `d_x = length_{𝒪_{X,x}} 𝒪_{R,x}`
> of `x` in the closed subscheme `R` cut out by the different of `f` is the length of the stalk
> `Ω_{X/Y,x}` of the sheaf of relative differentials.

```lean
theorem multiplicity_kaehlerDifferent_eq_length_stalk (hx : IsClosed ({x} : Set X)) :
    letI := locallyOfFiniteType_of_isCurve_comp k pX pY f hf
    letI : DecidableEq (OrderDual (TopologicalSpace.OpenNhds x)) := Classical.decEq _
    Module.length (X.presheaf.stalk x)
        (X.presheaf.stalk x ⧸ IdealSheafData.stalk (kaehlerDifferent f) x) =
      Module.length (ToType (X.sheaf.presheaf.stalk x))
        (ToType (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u})
          (Scheme.Hom.relativeDifferentials f).val.presheaf x))
```

**`AlgebraicGeometry.ramificationIdx_sub_one_le_multiplicity_kaehlerDifferent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzLocal.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzLocal.lean#L325). The attribute's comment: “(2): `d_x ≥ e_x - 1`, for a dominant morphism of smooth curves; the different is the Kähler different, which is the different of Tag 0BW4 by Tag 0BWG”.

> **Stacks Project, Tag 0C1F, part (2).** Let `f : X → Y` be a dominant morphism of smooth
> curves over a field and `x ∈ X` a closed point with image `y`. The multiplicity `d_x` of `x` in
> the closed subscheme cut out by the different of `f` is at least `e_x - 1`, where `e_x` is the
> ramification index of `𝒪_{X,x}` over `𝒪_{Y,y}`.

```lean
theorem ramificationIdx_sub_one_le_multiplicity_kaehlerDifferent (hx : IsClosed ({x} : Set X)) :
    letI := locallyOfFiniteType_of_isCurve_comp k pX pY f hf
    letI := (f.stalkMap x).hom.toAlgebra
    ((ramificationIdx (Y.presheaf.stalk (f x)) (X.presheaf.stalk x) - 1 : ℕ) : ℕ∞) ≤
      Module.length (X.presheaf.stalk x)
        (X.presheaf.stalk x ⧸ IdealSheafData.stalk (kaehlerDifferent f) x)
```

**`AlgebraicGeometry.multiplicity_kaehlerDifferent_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzLocal.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/RiemannHurwitzLocal.lean#L347). The attribute's comment: “(3): `d_x = e_x - 1` if and only if `𝒪_{X,x}` is tamely ramified over `𝒪_{Y,y}`, for a dominant morphism of smooth curves; the different is the Kähler different, which is the different of Tag 0BW4 by Tag 0BWG”.

> **Stacks Project, Tag 0C1F, part (3).** Let `f : X → Y` be a dominant morphism of smooth
> curves over a field and `x ∈ X` a closed point with image `y`. The multiplicity `d_x` of `x` in
> the closed subscheme cut out by the different of `f` equals `e_x - 1` if and only if `𝒪_{X,x}` is
> tamely ramified over `𝒪_{Y,y}`: the residue field extension `κ(x) / κ(y)` is separable and the
> characteristic of `κ(y)` does not divide `e_x`.

```lean
theorem multiplicity_kaehlerDifferent_eq_iff (hx : IsClosed ({x} : Set X)) :
    letI := locallyOfFiniteType_of_isCurve_comp k pX pY f hf
    letI := (f.stalkMap x).hom.toAlgebra
    Module.length (X.presheaf.stalk x)
        (X.presheaf.stalk x ⧸ IdealSheafData.stalk (kaehlerDifferent f) x) =
        ((ramificationIdx (Y.presheaf.stalk (f x)) (X.presheaf.stalk x) - 1 : ℕ) : ℕ∞) ↔
      (letI := (f.residueFieldMap x).hom.toAlgebra;
        Algebra.IsSeparable (Y.residueField (f x)) (X.residueField x)) ∧
        ¬ ringChar (Y.residueField (f x)) ∣
          ramificationIdx (Y.presheaf.stalk (f x)) (X.presheaf.stalk x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.12, Tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
