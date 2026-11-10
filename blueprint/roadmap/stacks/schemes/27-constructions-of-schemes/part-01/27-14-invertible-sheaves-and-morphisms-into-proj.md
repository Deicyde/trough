---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjChartGradedTripleTag.tag01NK, Stacks.AlgebraicGeometry.ProjInvertibleLocusEscape.not_range_subset_whereInvertible
statement: formalized
proof: formalized
---

# 27.14 Invertible sheaves and morphisms into Proj

Section 27.14 of the Stacks Project, [Tag 01NJ](https://stacks.math.columbia.edu/tag/01NJ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01NK, a lemma

[Tag 01NK](https://stacks.math.columbia.edu/tag/01NK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjChartGradedTripleTag.tag01NK`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjChartGradedTripleTag.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjChartGradedTripleTag.lean#L95). The attribute's comment: “the open U(psi), the morphism r_{L,psi} : U(psi) -> Proj A and the unital map of Z-graded algebras theta : r^*(sum_d O_X(d)) -> sum_d L^{tensor d}|_{U(psi)}; properties (1) and (2); every triple (U', r', theta') with (1) and (2) equals (U(psi), r, theta); and for d >= 1 and an open V on which psi(A_d) generates L^{tensor d}, the pair (phi, alpha) attached to the Veronese restriction of psi to V exists uniquely, r|_V = phi, and theta|_V in degree d equals alpha”.

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

**`Stacks.AlgebraicGeometry.ProjInvertibleLocusEscape.not_range_subset_whereInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ProjInvertibleLocusEscape.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ProjInvertibleLocusEscape.lean#L414).

> Let `k` be a field, let `S = k[A, B, C]` be graded by
> `deg A = 1`, `deg B = 2`, `deg C = 3` and set `X = Proj S`. Let `T = 𝐏²_k = Proj k[X₀, X₁, X₂]`
> with `𝓛 = 𝒪_T(1)`, so `𝒪_T(n) = 𝓛^{⊗ n}`, and let `ψ : S → Γ_*(T, 𝓛)` be the composite of the
> degree-preserving homomorphism `A ↦ X₀`, `B ↦ X₁²`, `C ↦ X₂³` with the canonical graded ring map
> of Tag 01MP. The image of the induced morphism `r_{𝓛, ψ} : T → X` is **not** contained in the
> invertible locus `W₁` of `𝒪_X(1)` — the largest open of `X` on which all the twists `𝒪_X(n)` are
> invertible and all their multiplication maps are isomorphisms, Tag 01MU. Indeed the point of `X`
> given by the homogeneous prime `(A, B)` is in the image, and a homogeneous element of `S` outside
> `(A, B)` has degree divisible by `3`, so no two of them have degrees differing by `1`.

```lean
public theorem not_range_subset_whereInvertible :
    ¬ Set.range (mapHom E.naturalGrading (projectiveGrading E) (coverHom E)).base ⊆
      ↑(whereInvertible E.naturalGrading 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.14, Tag 01NJ](https://stacks.math.columbia.edu/tag/01NJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
