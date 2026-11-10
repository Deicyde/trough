---
declaration: section
origin: cited
lean: KaehlerDifferential.pthRootDifferentialTrace_eq_comp_map, KaehlerDifferential.higherTrace, KaehlerDifferential.higherTrace_apply_of_le, KaehlerDifferential.higherTrace_apply_top, KaehlerDifferential.higherTrace_smul_baseForm, KaehlerDifferential.higherTrace_eq_of_presentations, KaehlerDifferential.relativeTraceComplex_trace_eq_higherTraceComplexMap, AlgebraicGeometry.existsUnique_higherTraceExtension_relativeDifferentials
statement: formalized
proof: formalized
---

# 54.2 A trace map in positive characteristic

Section 54.2 of the Stacks Project, [Tag 0ADY](https://stacks.math.columbia.edu/tag/0ADY). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ADZ, a lemma

[Tag 0ADZ](https://stacks.math.columbia.edu/tag/0ADZ) in the Stacks Project.

**`KaehlerDifferential.pthRootDifferentialTrace_eq_comp_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/TraceMapPositive/Basic.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/TraceMapPositive/Basic.lean#L655).

> Differential traces for two presentations of a degree-`p` purely inseparable algebra
> are intertwined by every `R`-algebra homomorphism between the presentations.

```lean
theorem pthRootDifferentialTrace_eq_comp_map (p : ℕ) [Fact p.Prime]
    {R : Type u} [CommRing R] [CharP R p] (a b : R)
    (φ : AdjoinRoot (X ^ p - C a) →ₐ[R] AdjoinRoot (X ^ p - C b))
    (trX : Ω[AdjoinRoot (X ^ p - C a)⁄R] →ₗ[R] Ω[R⁄ℤ])
    (trY : Ω[AdjoinRoot (X ^ p - C b)⁄R] →ₗ[R] Ω[R⁄ℤ])
    (hX : IsPthRootDifferentialTrace p a trX)
    (hY : IsPthRootDifferentialTrace p b trY) :
    letI : Algebra (AdjoinRoot (X ^ p - C a)) (AdjoinRoot (X ^ p - C b)) :=
      φ.toRingHom.toAlgebra
    trX = trY.comp ((KaehlerDifferential.map R R
      (AdjoinRoot (X ^ p - C a)) (AdjoinRoot (X ^ p - C b))).restrictScalars R)
```

## Tag 0AX5, a lemma

[Tag 0AX5](https://stacks.math.columbia.edu/tag/0AX5) in the Stacks Project.

**`KaehlerDifferential.higherTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean#L686). The attribute's comment: “the trace map”.

> The higher trace on differential forms for a presentation
> `S ≅ R[X]/(X ^ p - a)`.

```lean
public noncomputable def higherTrace (hp : p.Prime) [CharP Λ p] (a : R)
    (e : AdjoinRoot (Polynomial.X ^ p - Polynomial.C a) ≃ₐ[R] S) :
    (⋀[S]^(t + 1) (Ω[S⁄Λ])) →ₗ[R] (⋀[R]^(t + 1) (Ω[R⁄Λ]))
```

**`KaehlerDifferential.higherTrace_apply_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean#L707). The attribute's comment: “values below the top power”.

> The higher trace of `η₁ ∧ ⋯ ∧ ηₜ ∧ xⁱ dx` vanishes for `i ≤ p - 2`.

```lean
public theorem higherTrace_apply_of_le (hp : p.Prime) [CharP Λ p] (a : R)
    (e : AdjoinRoot (Polynomial.X ^ p - Polynomial.C a) ≃ₐ[R] S) (i : ℕ)
    (hi : i ≤ p - 2) (η : Fin t → Ω[R⁄Λ]) :
    higherTrace (t := t) hp a e
      (exteriorPower.ιMulti S (t + 1)
        (Fin.snoc (fun j => KaehlerDifferential.map Λ Λ R S (η j))
          ((e (AdjoinRoot.root (Polynomial.X ^ p - Polynomial.C a))) ^ i •
            KaehlerDifferential.D Λ S
              (e (AdjoinRoot.root (Polynomial.X ^ p - Polynomial.C a)))))) = 0
```

**`KaehlerDifferential.higherTrace_apply_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean, line 726](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean#L726). The attribute's comment: “value at the top power”.

> The higher trace of `η₁ ∧ ⋯ ∧ ηₜ ∧ x^(p-1) dx` is
> `η₁ ∧ ⋯ ∧ ηₜ ∧ da`.

```lean
public theorem higherTrace_apply_top (hp : p.Prime) [CharP Λ p] (a : R)
    (e : AdjoinRoot (Polynomial.X ^ p - Polynomial.C a) ≃ₐ[R] S)
    (η : Fin t → Ω[R⁄Λ]) :
    higherTrace (t := t) hp a e
      (exteriorPower.ιMulti S (t + 1)
        (Fin.snoc (fun j => KaehlerDifferential.map Λ Λ R S (η j))
          ((e (AdjoinRoot.root (Polynomial.X ^ p - Polynomial.C a))) ^ (p - 1) •
            KaehlerDifferential.D Λ S
              (e (AdjoinRoot.root (Polynomial.X ^ p - Polynomial.C a)))))) =
      exteriorPower.ιMulti R (t + 1)
        (Fin.snoc η (KaehlerDifferential.D Λ R a))
```

**`KaehlerDifferential.higherTrace_smul_baseForm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean, line 747](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean#L747). The attribute's comment: “vanishing on forms from the base”.

> The higher trace annihilates the image of
> `S ⊗[R] Ω^{t+1}_{R/Λ} → Ω^{t+1}_{S/Λ}`.  The displayed elements are a generating family for
> that image.

```lean
public theorem higherTrace_smul_baseForm (hp : p.Prime) [CharP Λ p] (a : R)
    (e : AdjoinRoot (Polynomial.X ^ p - Polynomial.C a) ≃ₐ[R] S) (s : S)
    (η : Fin (t + 1) → Ω[R⁄Λ]) :
    higherTrace (t := t) hp a e
      (s • exteriorPower.ιMulti S (t + 1)
        (fun j => KaehlerDifferential.map Λ Λ R S (η j))) = 0
```

**`KaehlerDifferential.higherTrace_eq_of_presentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean, line 762](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/Basic/TraceMap.lean#L762). The attribute's comment: “independence of presentation”.

> The higher trace is independent of the presentation of `S` as an algebra obtained by
> adjoining a `p`-th root. In particular, changing the chosen generator does not change the
> canonical trace on higher relative differential forms.

```lean
public theorem higherTrace_eq_of_presentations (hp : p.Prime) [CharP Λ p]
    (a b : R)
    (e : AdjoinRoot (Polynomial.X ^ p - Polynomial.C a) ≃ₐ[R] S)
    (f : AdjoinRoot (Polynomial.X ^ p - Polynomial.C b) ≃ₐ[R] S) :
    higherTrace (t := t) (Λ := Λ) hp a e =
      higherTrace (t := t) (Λ := Λ) hp b f
```

## Tag 0FLF, a remark

[Tag 0FLF](https://stacks.math.columbia.edu/tag/0FLF) in the Stacks Project.

**`KaehlerDifferential.relativeTraceComplex_trace_eq_higherTraceComplexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/TraceMapPositive/TraceIdentification.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/TraceMapPositive/TraceIdentification.lean#L99). The attribute's comment: “Tr = Θ_{S/R}, for Θ_{S/R} the map of relative de Rham complexes induced (0FLC (3)) by the trace maps on absolute forms of the framed algebra S/R”.

> **Tr = Θ_{S/R}.**  Let `𝐅_p ⊂ Λ ⊂ R ⊂ S` with `S ≅ R[x]/(x ^ p - a)`, and let `f` be any
> frame of `S/R` (for instance the monogenic one, `KaehlerDifferential.rootExtFrame`; the trace maps
> do not depend on it).  The map of relative de Rham complexes `Θ_{S/R} : Ω^•_{S/Λ} ⟶ Ω^•_{R/Λ}`
> induced by the trace maps on absolute forms of Proposition 0FLC is the map built from the trace
> `Tr` of Lemma 0AX5.

```lean
theorem relativeTraceComplex_trace_eq_higherTraceComplexMap (hp : p.Prime) [CharP Λ p] (a : R)
    (e : AdjoinRoot (Polynomial.X ^ p - Polynomial.C a) ≃ₐ[R] S) {d : ℕ} [NeZero d]
    (f : ChartFrame d R S) :
    relativeTraceComplex Λ f.trace f.isWedgeLinear_trace f.commutesWithD_trace =
      higherTraceComplexMap hp a e
```

## Tag 0AX6, a lemma

[Tag 0AX6](https://stacks.math.columbia.edu/tag/0AX6) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_higherTraceExtension_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/ReflexiveHullExtensionSupplement.lean, line 947](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/HigherTrace/ReflexiveHullExtensionSupplement.lean#L947). The attribute's comment: “the existence and uniqueness of the canonical trace map `f_*Ω^i_{Y/S} ⟶ (Ω^i_{X/S})^∨∨` whose stalk at the generic point is the trace map of [Stacks, Tag 0AX5], through the constructed identifications of both generic stalks”.

> Let `f : Y ⟶ X` be a finite dominant morphism of integral
> schemes over `S` with `X` normal and locally Noetherian, let the extension of function fields
> `L/K` that `f` induces be presented as `L ≅ K[x]/(xᵖ - a)`, and let `i = t + 1 ≥ 1`.  Then there
> is a unique map of `𝒪_X`-modules
>
> `Tr : f_*Ω^i_{Y/S} ⟶ (Ω^i_{X/S})^∨∨`
>
> whose stalk at the generic point of `X` is the trace map of [Stacks, Tag 0AX5] on
> `⋀ⁱ Ω_{L/Λ} ⟶ ⋀ⁱ Ω_{K/Λ}`, where `Λ` is the local ring of `S` below the generic point, the
> left-hand side is the generic stalk of `f_*Ω^i_{Y/S}` by
> `AlgebraicGeometry.genericPushforwardFormsEquiv` and the right-hand side is the generic stalk of
> `Ω^i_{X/S}` by `AlgebraicGeometry.genericFormsStalkEquiv`.  The trace does not depend on the
> presentation (`KaehlerDifferential.higherTrace_eq_of_presentations`), so quantifying over `a` and
> `e` rather than fixing them is what makes `Tr` canonical.

```lean
theorem existsUnique_higherTraceExtension_relativeDifferentials {S X Y : Scheme.{u}} (q : X ⟶ S)
    (f : Y ⟶ X)
    {p t : ℕ} (hp : p.Prime)
    [IsIntegral X] [IsIntegral Y] [IsLocallyNoetherian X]
    [IsNormal X] [IsFinite f] [IsDominant f]
    [(Scheme.Hom.relativeDifferentials q).IsCoherent]
    [CharP (ToType (S.presheaf.stalk (q.base (genericPoint X)))) p] :
    letI : Algebra (ToType (S.presheaf.stalk (q.base (genericPoint X)))) ↑X.functionField :=
      algebraStalkMap q (genericPoint X)
    letI : Algebra ↑X.functionField ↑Y.functionField := (functionFieldMap f).toAlgebra
    letI := genericBaseFunctionFieldAlgebra q f
    haveI := isScalarTower_genericBaseFunctionField q f
    ∀ (a : ↑X.functionField)
      (e : AdjoinRoot (Polynomial.X ^ p - Polynomial.C a) ≃ₐ[↑X.functionField]
        ↑Y.functionField),
      ∃! Tr : (Scheme.Modules.pushforward f).obj
            (Scheme.Hom.relativeDifferentialForms (f ≫ q) ((t + 1 : ℕ) : ℤ)) ⟶
          reflexiveHull (Scheme.Hom.relativeDifferentialForms q ((t + 1 : ℕ) : ℤ)),
        ∀ ω, ((TopCat.Presheaf.stalkFunctor Ab (genericPoint X)).map
              (Scheme.Modules.Hom.mapPresheaf (X := X) Tr))
                (genericPushforwardFormsEquiv q f (t + 1) ω) =
            ((TopCat.Presheaf.stalkFunctor Ab (genericPoint X)).map
              (Scheme.Modules.Hom.mapPresheaf (X := X)
                (toReflexiveHull (Scheme.Hom.relativeDifferentialForms q
                  ((t + 1 : ℕ) : ℤ))).1))
              (genericFormsStalkEquiv q (t + 1)
                (KaehlerDifferential.higherTrace hp a e ω))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.2, Tag 0ADY](https://stacks.math.columbia.edu/tag/0ADY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
