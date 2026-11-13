---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjChartGradedTripleTag.tag01NK, Stacks.AlgebraicGeometry.ProjInvertibleLocusEscape.mapHom_coverHom_surjective_and_not_range_subset_twistInvertibleLocus
statement: formalized
proof: formalized
---

# 27.14 Invertible sheaves and morphisms into Proj

Section 27.14 of the Stacks Project, [Tag 01NJ](https://stacks.math.columbia.edu/tag/01NJ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01NK, a lemma

[Tag 01NK](https://stacks.math.columbia.edu/tag/01NK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjChartGradedTripleTag.tag01NK`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjChartGradedTripleTag.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjChartGradedTripleTag.lean#L95). The attribute's comment: “the open U(psi), the morphism r\_\{L,psi} : U(psi) -> Proj A and the unital map of Z-graded algebras theta : r^*(sum\_d O\_X(d)) -> sum\_d L^\{tensor d}|\_\{U(psi)}; properties (1) and (2); every triple (U', r', theta') with (1) and (2) equals (U(psi), r, theta); and for d >= 1 and an open V on which psi(A\_d) generates L^\{tensor d}, the pair (phi, alpha) attached to the Veronese restriction of psi to V exists uniquely, r|\_V = phi, and theta|\_V in degree d equals alpha”.

> Let `A` be a graded ring, `X = Proj A`, `T` a scheme, `L` an invertible `𝒪_T`-module and
> `ψ : A → Γ_*(T, L)` a homomorphism of graded rings. Put
> `U(ψ) = ⋃_{f ∈ A_+ homogeneous} T_{ψ(f)}`. Then `ψ` induces the canonical morphism
> `r_{L, ψ} = ψ.glued : U(ψ) ⟶ X` and the map of `ℤ`-graded algebras
> `θ = theta 𝒜 ψ : r_{L, ψ}^*(⨁_{d ∈ ℤ} 𝒪_X(d)) ⟶ ⨁_{d ∈ ℤ} L^{⊗ d}|_{U(ψ)}`, and:
>
> 1. `U(ψ)` is the union of the `T_{ψ(f)}` (by definition);
> 2. `θ` preserves the unit;
> 3. **property (1)**: `r_{L, ψ}^{-1}(D₊(f)) = T_{ψ(f)}` for `f ∈ A_+` homogeneous;
> 4. **property (2)**: for every `d ≥ 0` and `a ∈ A_d`, `θ` carries the pullback of the global
>    section of `𝒪_X(d)` attached to `a` (the map of [Stacks, Tag 01MP]) to `ψ(a)|_{U(ψ)}` — the
>    commutativity of the square of the tag;
> 5. **the characterization**: every triple `(U', r', θ')` — an open of `T`, a morphism
>    `U' ⟶ X` and a map of graded algebras `r'^*(⨁ 𝒪_X(d)) ⟶ ⨁ L^{⊗ d}|_{U'}` — with properties
>    (1) and (2) is `(U(ψ), r_{L, ψ}, θ)`;
> 6. **the final assertion**: for `d ≥ 1` and an open `V ⊆ T` on which the sections `ψ(A_d)`
>    generate `L^{⊗ d}|_V`, the pair `(φ, α)` of [Stacks, Tag 01N8] for
>    `ψ|_{A^{(d)}} : A^{(d)} → Γ_*(V, L^{⊗ d})` exists and is unique, and for it
>    `r_{L, ψ}|_V = φ` and the restriction of the degree-`d` part of `θ` to `V`, read through the
>    canonical identifications `(r_{L, ψ}|_V)^*𝒪_X(d) = φ^*𝒪_X(d)` and
>    `L^{⊗ d}|_{U(ψ)}|_V = L|_V^{⊗ d}`, is `α`.
>
> The value `ψ(a)` is read in the tensor powers of [Stacks, Tag 01CU] that the Laurent algebra is
> made of, through the canonical comparison
> `Stacks.AlgebraicGeometry.ProjChartGradedDivision.intValue`.
> The sections `ψ(A_d)` generate `L^{⊗ d}|_V` exactly when their nonvanishing opens cover `V`.

```lean
theorem tag01NK :
    ψ.coveringOpen
        = ⨆ p : (e : ℕ) × 𝒜 (e + 1),
            nonvanishingOpen T (natTensorPow L (p.1 + 1)) (ψ.toFun (p.1 + 1) p.2)
      ∧ SheafOfModules.sectionsMap ((theta 𝒜 ψ).app 0)
          (Stacks.Conormal.gradedPullback ψ.glued
            (Stacks.AlgebraicGeometry.ProjConeTwist.integerTwistAlgebra 𝒜)).one
        = (laurentRestrict 𝒜 ψ).one
      ∧ (∀ {e : ℕ} {f : A} (hf : f ∈ 𝒜 e), 0 < e →
          ψ.coveringOpen.ι ''ᵁ (ψ.glued ⁻¹ᵁ AlgebraicGeometry.Proj.basicOpen 𝒜 f)
            = nonvanishingOpen T (natTensorPow L e) (ψ.toFun e ⟨f, hf⟩))
      ∧ (∀ (d : ℕ) {a : A} (ha : a ∈ 𝒜 d),
          ((theta 𝒜 ψ).app (d : ℤ)).val.app (op ⊤)
              (Scheme.Modules.pullbackSection ψ.glued (twistM 𝒜 (d : ℤ)) ⊤ ⊤
                (fun _ _ => trivial) (degreeSection 𝒜 d ⟨a, ha⟩))
            = resTop (tensorPowerModule T L (d : ℤ)) (intValue ψ d ⟨a, ha⟩)
                (ψ.coveringOpen.ι ''ᵁ ⊤))
      ∧ (∀ t : Triple 𝒜 L, IsTriple ψ t → t = canonicalTriple ψ)
      ∧ (∀ {d : ℕ} (hd : 0 < d) {V : T.Opens}
          (hVgen : V ≤ ⨆ g : 𝒜 d, nonvanishingOpen T (natTensorPow L d) (ψ.toFun d g)),
          (∃! p : Pair 𝒜 (natTensorPow ((Scheme.Modules.pullback V.ι).obj L) d) d,
              IsCompatible 𝒜 (veroneseAt 𝒜 (GradedSections.pullback V.ι ψ) d) p) ∧
          ∀ p : Pair 𝒜 (natTensorPow ((Scheme.Modules.pullback V.ι).obj L) d) d,
            IsCompatible 𝒜 (veroneseAt 𝒜 (GradedSections.pullback V.ι ψ) d) p →
            ∃ h : T.homOfLE (hVgen.trans (iSup_nonvanishingOpen_le_coveringOpen 𝒜 ψ hd))
                ≫ ψ.glued = toProj 𝒜 p.1,
              (Scheme.Modules.pullbackCongr h.symm).hom.app (twistM 𝒜 (d : ℤ))
                ≫ (Scheme.Modules.pullbackComp
                    (T.homOfLE (hVgen.trans (iSup_nonvanishingOpen_le_coveringOpen 𝒜 ψ hd)))
                    ψ.glued).inv.app (twistM 𝒜 (d : ℤ))
                ≫ (Scheme.Modules.pullback
                    (T.homOfLE (hVgen.trans (iSup_nonvanishingOpen_le_coveringOpen 𝒜 ψ hd)))).map
                    ((theta 𝒜 ψ).app (d : ℤ))
                ≫ (Scheme.Modules.pullback
                    (T.homOfLE (hVgen.trans (iSup_nonvanishingOpen_le_coveringOpen 𝒜 ψ hd)))).map
                    ((Scheme.Modules.restrictFunctorIsoPullback ψ.coveringOpen.ι).hom.app
                      (tensorPowerModule T L (d : ℤ)))
                ≫ (Scheme.Modules.pullbackComp
                    (T.homOfLE (hVgen.trans (iSup_nonvanishingOpen_le_coveringOpen 𝒜 ψ hd)))
                    ψ.coveringOpen.ι).hom.app (tensorPowerModule T L (d : ℤ))
                ≫ (Scheme.Modules.pullbackCongr (T.homOfLE_ι _)).hom.app
                    (tensorPowerModule T L (d : ℤ))
                ≫ (Scheme.Modules.pullback V.ι).map (powCompare L d).inv
                ≫ (pullbackNatTensorPowIso V.ι L d).inv
                = p.2.hom)
```

## Tag 01NL, a remark

[Tag 01NL](https://stacks.math.columbia.edu/tag/01NL) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjInvertibleLocusEscape.mapHom_coverHom_surjective_and_not_range_subset_twistInvertibleLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjInvertibleLocusEscapeSurjective.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjInvertibleLocusEscapeSurjective.lean#L350). The attribute's comment: “the remark as one theorem: for S = k[A, B, C] with weights 1, 2, 3 and ψ : S → Γ\_*(P²\_k, O(1)) given by A ↦ X₀, B ↦ X₁², C ↦ X₂³, the morphism r\_\{L,ψ} : P²\_k → Proj S is defined everywhere, satisfies property (1) of Tag 01NK, is surjective, O\_X(1) is not invertible everywhere on X = Proj S, and the image of r\_\{L,ψ} is not contained in the locus where the single sheaf O\_X(1) is invertible”.

> **Stacks Tag 01NL.** Let `k` be a field, `S = k[A, B, C]` graded by `deg A = 1`,
> `deg B = 2`, `deg C = 3`, and `X = Proj S`; let `T = 𝐏²_k` with `𝓛 = 𝒪_T(1)`, and let
> `ψ : S → Γ_*(T, 𝓛)` be `A ↦ X₀`, `B ↦ X₁²`, `C ↦ X₂³` followed by the canonical map of Tag 01MP.
> Then:
>
> 1. the morphism `r_{𝓛, ψ}` induced by `φ` is defined on all of `T`, so it is a morphism `T → X`;
> 2. it satisfies property (1) of Tag 01NK, `r^{-1}(D₊(f)) = T_{ψ(f)}` for `f` homogeneous of
>    positive degree, which characterizes `r_{𝓛, ψ}` (the section appearing is the degree-`deg f`
>    component of `ψ(f)`, by `psi_apply_homogeneous`);
> 3. it is surjective;
> 4. `𝒪_X(1)` is not invertible at every point of `X`; and
> 5. the image of `r_{𝓛, ψ}` is not contained in the locus where `𝒪_X(1)` is invertible.
>
> The locus in (4) and (5) is `twistInvertibleLocus E.naturalGrading 1`, the union of the opens on
> which the restriction of `𝒪_X(1)` is an invertible module; it contains Tag 01MU's `W₁`, so (5)
> is stronger than `not_range_subset_whereInvertible`.

```lean
public theorem mapHom_coverHom_surjective_and_not_range_subset_twistInvertibleLocus :
    mapDomain E.naturalGrading (projectiveGrading E) (coverHom E) = ⊤ ∧
      (∀ {d : ℕ}, 0 < d → ∀ {f : E.S} (hf : f ∈ E.naturalGrading d)
        (y : (mapDomain E.naturalGrading (projectiveGrading E) (coverHom E)).toScheme),
        (mapHom E.naturalGrading (projectiveGrading E) (coverHom E)).base y ∈
            AlgebraicGeometry.Proj.basicOpen E.naturalGrading f ↔
          (y.1 : ProjectiveSpectrum (projectiveGrading E)) ∈
            Stacks.Ample.nonvanishingLocus (X := AlgebraicGeometry.Proj (projectiveGrading E))
              (twistingSheaf (projectiveGrading E) (d : ℤ))
              (degreeSection (projectiveGrading E) d
                ⟨coverHom E f, coverAlgHom_mem_projectiveGrading E hf⟩)) ∧
      Function.Surjective (mapHom E.naturalGrading (projectiveGrading E) (coverHom E)).base ∧
      twistInvertibleLocus E.naturalGrading 1 ≠ ⊤ ∧
      ¬ Set.range (mapHom E.naturalGrading (projectiveGrading E) (coverHom E)).base ⊆
        ↑(twistInvertibleLocus E.naturalGrading 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.14, Tag 01NJ](https://stacks.math.columbia.edu/tag/01NJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
