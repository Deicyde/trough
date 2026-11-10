---
declaration: section
origin: cited
lean: Stacks.Discriminant.isInvertible_of_isGorenstein_fiber, Stacks.Discriminant.isInvertible_of_isGorenstein, Stacks.Discriminant.isGorenstein_tfae, Stacks.Discriminant.isInvertible_iff_exists_chart_dualizingModule_invertible, AlgebraicGeometry.Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber, Stacks.Discriminant.exists_affineOpens_different_isPrincipal_of_isGorenstein, Stacks.Discriminant.isLocallyPrincipal_differentIdealSheaf_of_isGorenstein, Stacks.Discriminant.different_sections_eq_noetherDifferent_of_isGorenstein
statement: formalized
proof: formalized
---

# 49.16 Quasi-finite Gorenstein morphisms

Section 49.16 of the Stacks Project, [Tag 0C14](https://stacks.math.columbia.edu/tag/0C14). 3 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C16, a lemma

[Tag 0C16](https://stacks.math.columbia.edu/tag/0C16) in the Stacks Project.

**`Stacks.Discriminant.isInvertible_of_isGorenstein_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L211). The attribute's comment: “(2) implies (3)”.

> **[Stacks, Tag 0C16], (2) implies (3).** For a quasi-finite flat morphism of Noetherian
> schemes whose fibres are Gorenstein schemes, the relative dualizing module `ω_{Y/X}` is an
> invertible `𝒪_Y`-module.
>
> Invertibility is the chartwise condition (4) of the same tag, and on a chart it is the fibrewise
> condition of [Stacks, Tag 0DWK]; the fibre ring of a chart is the ring of sections of the
> scheme-theoretic fibre over an affine open, hence Gorenstein.

```lean
theorem isInvertible_of_isGorenstein_fiber [Flat f] (ω : RelativeDualizingModuleData f)
    (hG : ∀ x : X, AlgebraicGeometry.IsGorenstein (f.fiber x)) :
    Stacks.SheafOfModules.IsInvertible Y.presheaf
      (structureSheafRing Y.toRingedSpace).property ω.sheaf
```

**`Stacks.Discriminant.isInvertible_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L230). The attribute's comment: “(1) implies (3)”.

> **[Stacks, Tag 0C16], (1) implies (3).** The relative dualizing module of a quasi-finite
> Gorenstein morphism of Noetherian schemes is an invertible `𝒪_Y`-module.
>
> Gorensteinness of the morphism is flatness together with Gorensteinness of the fibres, by
> [Stacks, Tag 0C05].

```lean
theorem isInvertible_of_isGorenstein (hF : ∀ x : X, IsLocallyNoetherian (f.fiber x))
    (hGor : Scheme.Hom.IsGorenstein f hF) (ω : RelativeDualizingModuleData f) :
    letI : Flat f := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f hF).mp hGor).1
    Stacks.SheafOfModules.IsInvertible Y.presheaf
      (structureSheafRing Y.toRingedSpace).property ω.sheaf
```

**`Stacks.Discriminant.isGorenstein_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L308).

> **[Stacks, Tag 0C16].** For a quasi-finite morphism `f : Y ⟶ X` of Noetherian schemes the
> following are equivalent:
> 1. `f` is Gorenstein;
> 2. `f` is flat and its fibres are Gorenstein;
> 3. `f` is flat and the relative dualizing module `ω_{Y/X}` of [Stacks, Tag 0BVG] is an
>    invertible `𝒪_Y`-module;
> 4. every point of `Y` has an affine open neighbourhood `V = Spec B` lying over an affine open
>    `U = Spec A` of `X` such that `A → B` is flat and `ω_{B/A}` is an invertible `B`-module.
>
> The module `ω_{Y/X}` is the canonical one, `Stacks.Discriminant.relativeDualizingModuleData f`;
> the algebraic relative dualizing module `ω_{B/A}` is computed from a finite-open factorization of
> `A → B`, and every such factorization gives an invertible module.

```lean
theorem isGorenstein_tfae :
    List.TFAE [
      Scheme.Hom.IsGorenstein f (isLocallyNoetherian_fiber_of_locallyOfFiniteType f),
      Flat f ∧ ∀ x : X, AlgebraicGeometry.IsGorenstein (f.fiber x),
      Flat f ∧ Stacks.SheafOfModules.IsInvertible Y.presheaf
        (structureSheafRing Y.toRingedSpace).property (relativeDualizingModuleData f).sheaf,
      ∀ y : Y, ∃ (U : X.affineOpens) (V : Y.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1), y ∈ V.1 ∧
        letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
        Module.Flat Γ(X, U.1) Γ(Y, V.1) ∧
          ∀ F : FiniteOpenFactorization.{u, u, u} Γ(X, U.1) Γ(Y, V.1),
            Module.Invertible Γ(Y, V.1) (dualizingModule F)]
```

**`Stacks.Discriminant.isInvertible_iff_exists_chart_dualizingModule_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/QuasiFiniteGorenstein.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/QuasiFiniteGorenstein.lean#L177). The attribute's comment: “(3) iff (4)”.

> **[Stacks, Tag 0C16], conditions (3) and (4).** For a quasi-finite morphism of locally
> Noetherian schemes with relative dualizing module `ω_{Y/X}`, the module `ω_{Y/X}` is an
> invertible `𝒪_Y`-module exactly when every point of `Y` has an affine open neighbourhood
> `V = Spec B` lying over an affine open `U = Spec A` of `X` for which the algebraic relative
> dualizing module `ω_{B/A}` is an invertible `B`-module.
>
> Both conditions of the source also ask that `f` be flat; flatness plays no role in the
> equivalence of the two readings of invertibility, so it is not assumed here.

```lean
theorem isInvertible_iff_exists_chart_dualizingModule_invertible
    (ω : RelativeDualizingModuleData f) :
    Stacks.SheafOfModules.IsInvertible Y.presheaf
        (structureSheafRing
          Y.toRingedSpace).property ω.sheaf ↔
      ∀ y : Y, ∃ (U : X.affineOpens) (V : Y.affineOpens) (hVU : V.1 ≤ f ⁻¹ᵁ U.1), y ∈ V.1 ∧
        letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
        ∀ F : FiniteOpenFactorization.{u, u, u} Γ(X, U.1) Γ(Y, V.1),
          Module.Invertible Γ(Y, V.1) (dualizingModule F)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Fibres.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/QuasiFiniteGorenstein.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/QuasiFiniteGorenstein.lean#L311) (StacksFrontier): “(1) iff (2)”.

## Tag 0C17, a remark

[Tag 0C17](https://stacks.math.columbia.edu/tag/0C17) in the Stacks Project.

**`Stacks.Discriminant.exists_affineOpens_different_isPrincipal_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L359). The attribute's comment: “(1)”.

> **[Stacks, Tag 0C17 (1)].** The different of a quasi-finite Gorenstein morphism of Noetherian
> schemes is a locally principal ideal: every point of `Y` has an affine open neighbourhood
> `V = Spec B` on which the ideal of sections of `𝔇_f` is generated by a single element of `B`.

```lean
theorem exists_affineOpens_different_isPrincipal_of_isGorenstein
    (ω : RelativeDualizingModuleData f) :
    letI : Flat f := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f _).mp hGor).1
    ∀ (τ : RelativeTraceSection ω) (y : Y),
      ∃ V : Y.affineOpens, y ∈ (V : Set Y) ∧
        (show Ideal Γ(Y, V.1) from (different ω τ).toSubmodule.obj (op V.1)).IsPrincipal
```

**`Stacks.Discriminant.isLocallyPrincipal_differentIdealSheaf_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L372). The attribute's comment: “(2)”.

> **[Stacks, Tag 0C17 (2)].** The closed subscheme `R ⊆ Y` cut out by the different of a
> quasi-finite Gorenstein morphism of Noetherian schemes is a locally principal closed
> subscheme.

```lean
theorem isLocallyPrincipal_differentIdealSheaf_of_isGorenstein
    (ω : RelativeDualizingModuleData f) :
    letI : Flat f := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f _).mp hGor).1
    ∀ τ : RelativeTraceSection ω,
      Stacks.Divisors.IsLocallyPrincipal (differentIdealSheaf ω τ)
```

**`Stacks.Discriminant.different_sections_eq_noetherDifferent_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L384). The attribute's comment: “(3)”.

> **[Stacks, Tag 0C17 (3)].** On affine opens `V = Spec B ⊆ Y` and `U = Spec A ⊆ X` with
> `f(V) ⊆ U`, the different of a quasi-finite Gorenstein morphism of Noetherian schemes is the
> Noether different of `B` over `A`.

```lean
theorem different_sections_eq_noetherDifferent_of_isGorenstein
    (ω : RelativeDualizingModuleData f) (U : X.affineOpens) (V : Y.affineOpens)
    (hVU : V.1 ≤ f ⁻¹ᵁ U.1) :
    letI : Flat f := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f _).mp hGor).1
    letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U V hVU).hom.toAlgebra
    letI : IsNoetherianRing Γ(X, U.1) := IsLocallyNoetherian.component_noetherian U
    letI : IsNoetherianRing Γ(Y, V.1) := IsLocallyNoetherian.component_noetherian V
    letI : Module.Flat Γ(X, U.1) Γ(Y, V.1) :=
      RingHom.flat_algebraMap_iff.mp (f.flat_appLE U.2 V.2 hVU)
    letI : Algebra.QuasiFinite Γ(X, U.1) Γ(Y, V.1) :=
      RingHom.quasiFinite_algebraMap.mp (LocallyQuasiFinite.quasiFinite_appLE U.2 V.2 hVU)
    ∀ τ : RelativeTraceSection ω,
      (show Ideal Γ(Y, V.1) from (different ω τ).toSubmodule.obj (op V.1)) =
        noetherDifferent Γ(X, U.1) Γ(Y, V.1)
```

**`Stacks.Discriminant.isEffectiveCartierDivisor_and_invertibleSheafIso_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L409). The attribute's comment: “(6)”.

> **[Stacks, Tag 0C17 (6)].** If a quasi-finite Gorenstein morphism of Noetherian schemes is
> étale at the associated points of `Y`, then the closed subscheme `R ⊆ Y` cut out by the different
> is an effective Cartier divisor, and there is exactly one isomorphism `𝒪_Y(R) ≅ ω_{Y/X}` carrying
> the canonical section `1_R` to the trace element `τ_{Y/X}`.
>
> Gorensteinness makes `f` flat and `ω_{Y/X}` invertible, which is the situation of
> [Stacks, Tag 0BWA (3)].

```lean
theorem isEffectiveCartierDivisor_and_invertibleSheafIso_of_isGorenstein
    (ω : RelativeDualizingModuleData f)
    (hét : ∀ y ∈ Stacks.Divisors.schemeAssociatedPoints Y, EtaleAt f y) :
    letI : Flat f := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f _).mp hGor).1
    ∀ τ : RelativeTraceSection ω,
      Stacks.Divisors.IsEffectiveCartierDivisor (differentIdealSheaf ω τ) ∧
        ∃! e : Stacks.Divisors.invertibleSheaf' (differentIdealSheaf ω τ) ≅ ω.sheaf,
          Scheme.Modules.Hom.app e.hom ⊤
            ((Stacks.Divisors.canonicalSection' (differentIdealSheaf ω τ)).eval (op ⊤)) =
              τ.sect
```

**`Stacks.Discriminant.discriminantIdeal_eq_normIdealSheaf_differentIdealSheaf_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L440). The attribute's comment: “(5)”.

> **[Stacks, Tag 0C17 (5)].** If a finite Gorenstein morphism of Noetherian schemes has
> relative dualizing module `ω_{Y/X}` and trace element `τ_{Y/X}`, then the norm of the closed
> subscheme `R ⊆ Y` cut out by the different is the discriminant `D_f`: as ideal sheaves on `X`,
> `Norm_f(𝔇_f)` is the discriminant ideal sheaf.
>
> Gorensteinness makes `f` flat and `ω_{Y/X}` invertible, which is the situation of
> [Stacks, Tag 0BWA (2)].

```lean
theorem discriminantIdeal_eq_normIdealSheaf_differentIdealSheaf_of_isGorenstein
    (ω : RelativeDualizingModuleData f) :
    letI : Flat f := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f _).mp hGor).1
    letI : Stacks.Morphisms.IsFiniteLocallyFree f :=
      (Stacks.Morphisms.isFiniteLocallyFree_iff_isFinite_flat_of_isLocallyNoetherian f).mpr
        ⟨inferInstance, inferInstance⟩
    ∀ τ : RelativeTraceSection ω,
      discriminantIdeal f = Stacks.Norm.normIdealSheaf f (differentIdealSheaf ω τ)
```

**`Stacks.Discriminant.isIso_different_baseChange_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Different/TheDifferent/GorensteinInvertible.lean#L471). The attribute's comment: “(4)”.

> **[Stacks, Tag 0C17 (4)].** Formation of the closed subscheme `R ⊆ Y` cut out by the
> different of a quasi-finite Gorenstein morphism of Noetherian schemes commutes with base change
> along an arbitrary morphism `g : X' ⟶ X`: the closed immersion `R' ⟶ R ×_Y Y'` induced by
> `Y' ⟶ Y` is an isomorphism.
>
> Gorensteinness makes `ω_{Y/X}` invertible, which is the case of [Stacks, Tag 0BW7] in which the
> inverse image of the different is the different of the base change with no flatness hypothesis
> on `g`.

```lean
theorem isIso_different_baseChange_of_isGorenstein {R R' : Scheme.{u}}
    (ω : RelativeDualizingModuleData f) (i : R ⟶ Y) [IsClosedImmersion i] :
    letI : Flat f := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f _).mp hGor).1
    ∀ (τ : RelativeTraceSection ω) (ω' : RelativeDualizingModuleData (pullback.snd f g))
      (τ' : RelativeTraceSection ω') (i' : R' ⟶ pullback f g) [IsClosedImmersion i'],
      i.ker = differentIdealSheaf ω τ → i'.ker = differentIdealSheaf ω' τ' →
      ∀ (k : R' ⟶ R) (hk : k ≫ i = i' ≫ pullback.fst f g), IsIso (pullback.lift k i' hk)
```

## Tag 0C18, a remark

[Tag 0C18](https://stacks.math.columbia.edu/tag/0C18) in the Stacks Project.

**`Stacks.Duality.existsUnique_invertibleSheafIso_upperShriekDualSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFiniteGorenstein.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFiniteGorenstein.lean#L88). The attribute's comment: “if f is finite: O\_X(R) = omega\_\{X/Y} comes from tau\_\{X/Y}, dual to Trace\_f”.

> **Stacks Project, Tag 0C18, the finite case.** Let `f : X ⟶ Y` be a finite Gorenstein
> morphism of schemes separated and of finite type over a Noetherian base, with `X` Cohen–Macaulay
> and `f` étale at the generic points of `X`, and let `R ⊆ X` be cut out by the different of the
> relative dualizing module `ω_{X/Y} = H⁰(f^!𝒪_Y)` of Tag 0BUL. Then the isomorphism
> `𝒪_X(R) ≅ ω_{X/Y}` of Tag 0C17 is the unique one sending the canonical section `1_R` to the
> section `τ_{X/Y}` of `H⁰(f^!𝒪_Y)` corresponding under duality to `Trace_f : f_*𝒪_X ⟶ 𝒪_Y`
> (Tag 0BVI).

```lean
theorem existsUnique_invertibleSheafIso_upperShriekDualSection [IsFinite f.left]
    (hGor : f.left.IsGorenstein (isLocallyNoetherian_fiber_left f))
    (hX : IsCohenMacaulay X.left) (hét : ∀ x ∈ genericPoints X.left, EtaleAt f.left x)
    (j : CompactificationOf (Over.mk f.left)) :
    letI : Flat f.left := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f.left
      (isLocallyNoetherian_fiber_left f)).mp hGor).1
    ∃! e : Stacks.Divisors.invertibleSheaf' (differentIdealSheaf
        (upperShriekRelativeDualizingModuleData f j)
        (relativeTraceSectionData (upperShriekRelativeDualizingModuleData f j))) ≅
        (upperShriekRelativeDualizingModuleData f j).sheaf,
      Scheme.Modules.Hom.app e.hom ⊤
          ((Stacks.Divisors.canonicalSection' (differentIdealSheaf
            (upperShriekRelativeDualizingModuleData f j)
            (relativeTraceSectionData (upperShriekRelativeDualizingModuleData f j)))).eval
              (op ⊤)) =
        upperShriekDualSection f (pushforwardTrace f.left) j
```

**`Stacks.Duality.nonempty_homology_upperShriek_iso_pullback_tensor_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFiniteGorenstein.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFiniteGorenstein.lean#L212). The attribute's comment: “omega\_X = f^* omega\_Y (x) omega\_\{X/Y} = f^* omega\_Y (x) O\_X(R)”.

> **Stacks Project, Tag 0C18.** Let `S` be Noetherian, `f : X ⟶ Y` a quasi-finite Gorenstein
> morphism of `FTS S` étale at the generic points of `X`, with `X` Cohen–Macaulay, and let
> `ω_Y^• = π_Y^!ω_T`, `ω_X^• = π_X^!ω_T` for `π_X = f ≫ π_Y` and `ω_T` bounded below (for instance
> a dualizing complex on the base). Let `ω_{X/Y}` be any relative dualizing module (Tag 0BVG; by
> Tag 0BUL it is `H⁰(f^!𝒪_Y)`), `τ` its trace element and `R` the closed subscheme cut out by the
> different. Then in every degree `i`
> `Hⁱ(ω_X^•) ≅ f^*Hⁱ(ω_Y^•) ⊗ ω_{X/Y} ≅ f^*Hⁱ(ω_Y^•) ⊗ 𝒪_X(R)`.
> When `X` and `Y` are Cohen–Macaulay and `ω_T` is dualizing, `ω_X^•` and `ω_Y^•` have a single
> nonzero cohomology sheaf on each connected component, in the same degree; `ω_X` and `ω_Y` are
> these sheaves, and the displayed isomorphisms are `ω_X = f^*ω_Y ⊗ ω_{X/Y} = f^*ω_Y ⊗ 𝒪_X(R)`.

```lean
theorem nonempty_homology_upperShriek_iso_pullback_tensor_of_isGorenstein
    (hGor : f.left.IsGorenstein (isLocallyNoetherian_fiber_left f))
    (hX : IsCohenMacaulay X.left) (hét : ∀ x ∈ genericPoints X.left, EtaleAt f.left x)
    {T : FTS S} (πY : Y ⟶ T) (πX : X ⟶ T) (hπ : f ≫ πY = πX)
    (jY : CompactificationOf (Over.mk πY.left)) (jX : CompactificationOf (Over.mk πX.left))
    (ωT : quasiCoherentDerivedCategory T.left) (hωT : DerivedCategoryB.IsBoundedBelow ωT.obj)
    (i : ℤ) :
    letI : Flat f.left := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f.left
      (isLocallyNoetherian_fiber_left f)).mp hGor).1
    ∀ (ω : RelativeDualizingModuleData f.left) (τ : RelativeTraceSection ω),
      Nonempty ((DerivedCategory.homologyFunctor X.left.Modules i).obj
          ((upperShriek πX jX).obj ωT).obj ≅
        ((Stacks.SheafOfModules.Tensor.sheafTensor X.left.sheaf).obj
          ((Scheme.Modules.pullback f.left).obj
            ((DerivedCategory.homologyFunctor Y.left.Modules i).obj
              ((upperShriek πY jY).obj ωT).obj))).obj ω.sheaf) ∧
      Nonempty ((DerivedCategory.homologyFunctor X.left.Modules i).obj
          ((upperShriek πX jX).obj ωT).obj ≅
        ((Stacks.SheafOfModules.Tensor.sheafTensor X.left.sheaf).obj
          ((Scheme.Modules.pullback f.left).obj
            ((DerivedCategory.homologyFunctor Y.left.Modules i).obj
              ((upperShriek πY jY).obj ωT).obj))).obj
          (Stacks.Divisors.invertibleSheaf' (differentIdealSheaf ω τ)))
```

**`Stacks.Duality.upperShriek_quasiFinite_isGorenstein_dualizing_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFiniteGorenstein.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekQuasiFiniteGorenstein.lean#L276). The attribute's comment: “the whole remark: omega\_X = f^* omega\_Y (x) omega\_\{X/Y} = f^* omega\_Y (x) O\_X(R), and for f finite O\_X(R) = omega\_\{X/Y} comes from tau\_\{X/Y}, dual to Trace\_f”.

> **Stacks Project, Tag 0C18**, the whole remark. Let `S` be Noetherian and `f : X ⟶ Y` a
> quasi-finite Gorenstein morphism of schemes separated and of finite type over `S`, with `X`
> Cohen–Macaulay and `f` étale at the generic points of `X`. Let `ω_Y^• = π_Y^!ω_T` and
> `ω_X^• = π_X^!ω_T` for `π_X = f ≫ π_Y` and a bounded below `ω_T` (for instance `T = S` with its
> dualizing complex `ω_S^•`, which gives the normalized dualizing complexes). Then:
>
> 1. for every relative dualizing module `ω_{X/Y}` (Tag 0BVG; by Tag 0BUL it is `H⁰(f^!𝒪_Y)`),
>    with trace element `τ` and `R` the closed subscheme cut out by the different, in every degree
>    `i` one has `Hⁱ(ω_X^•) ≅ f^*Hⁱ(ω_Y^•) ⊗ ω_{X/Y} ≅ f^*Hⁱ(ω_Y^•) ⊗ 𝒪_X(R)`; in the degree of the
>    dualizing modules this is `ω_X = f^*ω_Y ⊗ ω_{X/Y} = f^*ω_Y ⊗ 𝒪_X(R)`;
> 2. if moreover `f` is finite, the isomorphism `𝒪_X(R) ≅ ω_{X/Y} = H⁰(f^!𝒪_Y)` is the unique one
>    sending the canonical section `1_R` to the section `τ_{X/Y}` which corresponds under duality to
>    `Trace_f : f_*𝒪_X ⟶ 𝒪_Y` (Tag 0BVI).

```lean
theorem upperShriek_quasiFinite_isGorenstein_dualizing_iso
    (hGor : f.left.IsGorenstein (isLocallyNoetherian_fiber_left f))
    (hX : IsCohenMacaulay X.left) (hét : ∀ x ∈ genericPoints X.left, EtaleAt f.left x)
    {T : FTS S} (πY : Y ⟶ T) (πX : X ⟶ T) (hπ : f ≫ πY = πX)
    (jY : CompactificationOf (Over.mk πY.left)) (jX : CompactificationOf (Over.mk πX.left))
    (ωT : quasiCoherentDerivedCategory T.left) (hωT : DerivedCategoryB.IsBoundedBelow ωT.obj) :
    letI : Flat f.left := ((Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber f.left
      (isLocallyNoetherian_fiber_left f)).mp hGor).1
    (∀ (i : ℤ) (ω : RelativeDualizingModuleData f.left) (τ : RelativeTraceSection ω),
      Nonempty ((DerivedCategory.homologyFunctor X.left.Modules i).obj
          ((upperShriek πX jX).obj ωT).obj ≅
        ((Stacks.SheafOfModules.Tensor.sheafTensor X.left.sheaf).obj
          ((Scheme.Modules.pullback f.left).obj
            ((DerivedCategory.homologyFunctor Y.left.Modules i).obj
              ((upperShriek πY jY).obj ωT).obj))).obj ω.sheaf) ∧
      Nonempty ((DerivedCategory.homologyFunctor X.left.Modules i).obj
          ((upperShriek πX jX).obj ωT).obj ≅
        ((Stacks.SheafOfModules.Tensor.sheafTensor X.left.sheaf).obj
          ((Scheme.Modules.pullback f.left).obj
            ((DerivedCategory.homologyFunctor Y.left.Modules i).obj
              ((upperShriek πY jY).obj ωT).obj))).obj
          (Stacks.Divisors.invertibleSheaf' (differentIdealSheaf ω τ)))) ∧
    ∀ [IsFinite f.left] (j : CompactificationOf (Over.mk f.left)),
      ∃! e : Stacks.Divisors.invertibleSheaf' (differentIdealSheaf
          (upperShriekRelativeDualizingModuleData f j)
          (relativeTraceSectionData (upperShriekRelativeDualizingModuleData f j))) ≅
          (upperShriekRelativeDualizingModuleData f j).sheaf,
        Scheme.Modules.Hom.app e.hom ⊤
            ((Stacks.Divisors.canonicalSection' (differentIdealSheaf
              (upperShriekRelativeDualizingModuleData f j)
              (relativeTraceSectionData (upperShriekRelativeDualizingModuleData f j)))).eval
                (op ⊤)) =
          upperShriekDualSection f (pushforwardTrace f.left) j
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.16, Tag 0C14](https://stacks.math.columbia.edu/tag/0C14)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
