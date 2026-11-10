---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isClosedImmersion_adicFibre_iso, AlgebraicGeometry.Space.exists_isFinite_adicFibre_iso_of_tower, AlgebraicGeometry.Space.existsUnique_adicFibreMap_eq, AlgebraicGeometry.Space.existsUnique_adicFibreMap_eq_of_isLocallyOfFiniteType, AlgebraicGeometry.Space.exists_isProjective_algebraization_of_dimension_le_one, AlgebraicGeometry.Space.C1605.exists_iso_isProjective_of_isProper_of_dimension_adicFibre_le_one
statement: formalized
proof: formalized
---

# 76.43 Grothendieck's algebraization theorem

Section 76.43 of the Stacks Project, [Tag 0A00](https://stacks.math.columbia.edu/tag/0A00). 6 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08BG, a lemma

[Tag 08BG](https://stacks.math.columbia.edu/tag/08BG) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isClosedImmersion_adicFibre_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedSubspaceTowerAlgebraization.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedSubspaceTowerAlgebraization.lean#L56).

> **Stacks 08BG.** Let `A` be a Noetherian ring complete with respect to an ideal `I`, write
> `S = Spec A` and `S_n = Spec(A / I^{n+1})`, and let `X ⟶ S` be a separated morphism of finite
> type of algebraic spaces, with adic fibres `X_n = X ×_S S_n`.  Let `Z_n` be algebraic spaces with
> morphisms `j_n : Z_n ⟶ X_n` and `t_n : Z_n ⟶ Z_{n+1}` making every square
> `Z_n ⟶ Z_{n+1}` over `X_n ⟶ X_{n+1}` cartesian.  If `Z_0 ⟶ X_0` is a closed immersion and
> `Z_0 ⟶ S_0` is proper, then there is a closed immersion `i : Z ⟶ X` of algebraic spaces with
> `Z ⟶ S` proper and isomorphisms `Z_n ≅ Z ×_S S_n` over `X_n`, compatible with the transition
> maps.
>
> The index `n` stands for the source's `n + 1`: `Z 0 = Z_1`, `X 0 = X_1`, `S 0 = S_1`.

```lean
theorem exists_isClosedImmersion_adicFibre_iso [IsNoetherianRing A] [IsAdicComplete I A]
    {X : (BigFppfOver B (Spec (.of A)) hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hS X)
    (fX : X ⟶ yoneda.obj (baseObject A B hS)) (hft : IsFiniteType B (Spec (.of A)) hS fX)
    (hsep : IsSeparated B (Spec (.of A)) hS fX)
    (Z : ℕ → (BigFppfOver B (Spec (.of A)) hS)ᵒᵖ ⥤ Type u)
    (hZ : ∀ n, IsAlgebraicSpace B (Spec (.of A)) hS (Z n))
    (j : ∀ n, Z n ⟶ adicFibre A I B hS hSn fX n) (t : ∀ n, Z n ⟶ Z (n + 1))
    (hcart : ∀ n, IsPullback (t n) (j n) (j (n + 1)) (adicFibreSucc A I B hS hSn fX n))
    (hj : IsClosedImmersion B (Spec (.of A)) hS (j 0))
    (hprop : IsProper B (Spec (.of A)) hS
      (j 0 ≫ pullback.snd fX (yoneda.map (adicThickeningMap A I B hS hSn 0)))) :
    ∃ (W : (BigFppfOver B (Spec (.of A)) hS)ᵒᵖ ⥤ Type u)
      (_ : IsAlgebraicSpace B (Spec (.of A)) hS W) (i : W ⟶ X),
      IsClosedImmersion B (Spec (.of A)) hS i ∧ IsProper B (Spec (.of A)) hS (i ≫ fX) ∧
      ∃ e : ∀ n, Z n ≅ adicFibre A I B hS hSn (i ≫ fX) n,
        (∀ n, (e n).hom ≫ adicFibreMap A I B hS hSn i rfl n = j n) ∧
        (∀ n, t n ≫ (e (n + 1)).hom = (e n).hom ≫ adicFibreSucc A I B hS hSn (i ≫ fX) n)
```

## Tag 0A01, a lemma

[Tag 0A01](https://stacks.math.columbia.edu/tag/0A01) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFinite_adicFibre_iso_of_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AdicFiniteAlgebraization/FiniteAlgebraization.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AdicFiniteAlgebraization/FiniteAlgebraization.lean#L62).

> **Algebraization of a finite tower over the adic fibres.**  Let `A` be a Noetherian ring
> complete along `I`, `S = Spec A`, and `f : X ⟶ S` a separated morphism of finite type of algebraic
> spaces with adic fibres `X_n = X ×_S S_n`.  Let `y_n : Y_n ⟶ X_n` be algebraic spaces over the
> adic fibres with transitions `t_n : Y_n ⟶ Y_{n + 1}` making cartesian squares over the transitions
> `X_n ⟶ X_{n + 1}`, with `Y_0 ⟶ X_0` finite and `Y_0 ⟶ S_0` proper.  Then there is a finite
> `π : Y ⟶ X` with `Y` proper over `S`, and isomorphisms `Y_n ≅ Y ×_S S_n` lying over `X_n`,
> compatible with the transitions, and exhibiting `Y_n` as `Y ×_X X_n`.
>
> The tower is indexed from `0`: `S_n` is `Spec (A / I ^ (n + 1))`, so the `n`-th term here is the
> `(n + 1)`-st term `Y_{n + 1}` of Stacks, and `Y_0 ⟶ X_0`, `Y_0 ⟶ S_0` are Stacks' `Y_1 ⟶ X_1`,
> `Y_1 ⟶ S_1`.

```lean
theorem exists_isFinite_adicFibre_iso_of_tower [IsAdicComplete I A]
    (hsep : IsSeparated B (Spec (.of A)) hA f) (hft : IsFiniteType B (Spec (.of A)) hA f)
    (Y : ℕ → AlgebraicSpaces B (Spec (.of A)) hA) (y : ∀ n, Y n ⟶ adicFibreSpace A I B hA hX f n)
    (tY : ∀ n, Y n ⟶ Y (n + 1))
    (hcart : ∀ n, IsPullback (tY n) (y n) (y (n + 1)) (adicFibreSuccHom A I B hA hX f n))
    (hfin0 : IsFinite B (Spec (.of A)) hA (y 0).hom)
    (hprop : IsProper B (Spec (.of A)) hA ((y 0).hom ≫ adicFibreSnd A I B hA f 0)) :
    ∃ (Z : AlgebraicSpaces B (Spec (.of A)) hA) (π : Z ⟶ ⟨X, hX⟩),
      IsFinite B (Spec (.of A)) hA π.hom ∧ IsProper B (Spec (.of A)) hA (π.hom ≫ f) ∧
      ∃ e : ∀ n, Y n ≅ adicFibreSpace A I B hA Z.2 (π.hom ≫ f) n,
        (∀ n, (e n).hom.hom ≫
          adicFibreMap A I B hA (contains_adicThickening A I B hA) π.hom rfl n = (y n).hom) ∧
        (∀ n, tY n ≫ (e (n + 1)).hom =
          (e n).hom ≫ adicFibreSuccHom A I B hA Z.2 (π.hom ≫ f) n) ∧
        (∀ n, IsPullback ((e n).hom ≫ adicFibreFst A I B hA Z.2 (π.hom ≫ f) n) (y n) π
          (adicFibreFstHom A I B hA hX f n))
```

## Tag 0A4Z, a lemma

[Tag 0A4Z](https://stacks.math.columbia.edu/tag/0A4Z) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.existsUnique_adicFibreMap_eq`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MorphismAlgebraization.lean#L443), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/MorphismAlgebraizationTag.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MorphismAlgebraizationTag.lean#L23) (StacksFrontier).

## Tag 0GHK, a remark

[Tag 0GHK](https://stacks.math.columbia.edu/tag/0GHK) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_adicFibreMap_eq_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MorphismAlgebraizationLocallyFiniteType.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MorphismAlgebraizationLocallyFiniteType.lean#L248). The attribute's comment: “the separated case: `Y ⟶ S` separated and locally of finite type; the quasi-separated case rests on Bhatt and Hall–Rydh, outside the Stacks project, and the open general question is not a statement”.

> **Stacks 0GHK, the separated case.** Let `A` be a Noetherian ring complete with respect to
> an ideal `I`, `S = Spec A`, `S_n = Spec (A / I^{n+1})`, and let `X`, `Y` be algebraic spaces over
> `S` with `X ⟶ S` proper and `Y ⟶ S` separated and locally of finite type. A compatible system
> of morphisms `g_n : X_n ⟶ Y_n` over the `S_n` between the adic fibres is the system of adic
> fibres of exactly one morphism `g : X ⟶ Y` over `S`.
>
> Remark 0GHK asks whether Stacks 0A4Z survives with `Y ⟶ S` only locally of finite type. This
> declaration formalizes the remark's assertion that the answer is yes when `Y ⟶ S` is separated,
> by the remark's reduction to a quasi-compact open of `Y` containing the image of `g_1` (here
> `g 0`); uniqueness is included, as in Stacks 0A4Z. The remark's statement "we don't know the
> answer in general" is an open question, not a mathematical assertion, and is not formalized.
> The remark's further assertion for `Y ⟶ S` only quasi-separated is not formalized: the remark
> gives no proof inside the Stacks project, deferring to Bhatt's algebraization theorem for
> `D_perf` and to Hall–Rydh's coherent Tannaka duality, papers outside the project.

```lean
theorem existsUnique_adicFibreMap_eq_of_isLocallyOfFiniteType [IsNoetherianRing A]
    [IsAdicComplete I A] (hX : IsAlgebraicSpace B _ hS X) (hY : IsAlgebraicSpace B _ hS Y)
    (fX : X ⟶ yoneda.obj (baseObject A B hS)) (fY : Y ⟶ yoneda.obj (baseObject A B hS))
    (hpX : IsProper B _ hS fX) (hsY : IsSeparated B _ hS fY)
    (hlY : IsLocallyOfFiniteType B _ hS fY)
    (g : ∀ n, adicFibre A I B hS hSn fX n ⟶ adicFibre A I B hS hSn fY n)
    (hg : ∀ n, g n ≫ pullback.snd fY (yoneda.map (adicThickeningMap A I B hS hSn n)) =
      pullback.snd fX (yoneda.map (adicThickeningMap A I B hS hSn n)))
    (hgc : ∀ n, adicFibreSucc A I B hS hSn fX n ≫ g (n + 1) =
      g n ≫ adicFibreSucc A I B hS hSn fY n) :
    ∃! φ : X ⟶ Y, ∃ hφ : φ ≫ fY = fX, ∀ n, adicFibreMap A I B hS hSn φ hφ n = g n
```

## Tag 0E7R, a lemma

[Tag 0E7R](https://stacks.math.columbia.edu/tag/0E7R) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isProjective_algebraization_of_dimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalCurve/SpaceAlgebraization.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/FormalCurve/SpaceAlgebraization.lean#L72).

> **[Stacks, Tag 0E7R], algebraization of formal curves.** Let `A` be a complete local
> Noetherian ring, `S = Spec A`, `Sₙ = Spec (A / 𝔪 ^ (n + 1))`, and let `Xₙ ⟶ Sₙ` be algebraic spaces
> with transition maps `iₙ : Xₙ ⟶ Xₙ₊₁` making every square over `Sₙ ⟶ Sₙ₊₁` cartesian. If
> `X₀ ⟶ S₀` is proper and `dim X₀ ≤ 1`, there are a projective morphism of schemes `fY : Y ⟶ S`
> and morphisms `kₙ : Xₙ ⟶ Y`, compatible with the `iₙ`, identifying each `Xₙ` with `Y ×_S Sₙ`.

```lean
theorem exists_isProjective_algebraization_of_dimension_le_one
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [IsAdicComplete (maximalIdeal A) A]
    (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of A)))
    (X : ℕ → (BigFppfOver B (Spec (.of A)) hS)ᵒᵖ ⥤ Type u)
    (hX : ∀ n, IsAlgebraicSpace B (Spec (.of A)) hS (X n))
    (p : ∀ n, X n ⟶ yoneda.obj (adicThickeningObject A (maximalIdeal A) B hS
      (contains_adicThickening A (maximalIdeal A) B hS) n))
    (i : ∀ n, X n ⟶ X (n + 1))
    (hcart : ∀ n, IsPullback (i n) (p n) (p (n + 1))
      (yoneda.map (adicThickeningSuccMap A (maximalIdeal A) B hS
        (contains_adicThickening A (maximalIdeal A) B hS) n)))
    (hproper : IsProper B (Spec (.of A)) hS (p 0))
    (hdim : dimension B (Spec (.of A)) hS (X 0) (hX 0) ≤ 1) :
    ∃ (Y : Scheme.{u}) (hY : B.Contains Y) (fY : Y ⟶ Spec (.of A)),
      IsProjective fY ∧ IsProjectiveMorphism fY ∧
      ∃ k : ∀ n, X n ⟶ yoneda.obj (siteObject B (Spec (.of A)) hS hY fY),
        (∀ n, i n ≫ k (n + 1) = k n) ∧
        ∀ n, IsPullback (k n) (p n) (yoneda.map (siteObjectToBase A B hS hY fY))
          (yoneda.map (adicThickeningMap A (maximalIdeal A) B hS
            (contains_adicThickening A (maximalIdeal A) B hS) n))
```

## Tag 0AE7, a lemma

[Tag 0AE7](https://stacks.math.columbia.edu/tag/0AE7) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.C1605.exists_iso_isProjective_of_isProper_of_dimension_adicFibre_le_one`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationCompleteLocalProjective.lean#L87), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ProperCurveOverCompleteLocalScheme.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperCurveOverCompleteLocalScheme.lean#L25) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.43, Tag 0A00](https://stacks.math.columbia.edu/tag/0A00)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
