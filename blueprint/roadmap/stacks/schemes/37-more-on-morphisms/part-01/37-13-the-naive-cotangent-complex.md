---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.naiveCotangentComplex, Stacks.NaiveCotangentAffineQuasiIso.quasiIso_comparisonMap, AlgebraicGeometry.Scheme.isZero_homology_naiveCotangentComplex, AlgebraicGeometry.Scheme.naiveCotangentExtZeroAddEquiv, AlgebraicGeometry.Scheme.isQuasicoherent_homology_naiveCotangentComplex, AlgebraicGeometry.Scheme.naiveCotangentComplexHomologyZeroIso, Stacks.NaiveCotangentFinitePresentation.exists_affine_quasiIso_associatedDouble_naiveCotangentComplex, Stacks.Smooth.formallySmooth_iff_isZero_homology_negOne_and_isLocallyProjective_homology_zero
statement: formalized
proof: formalized
---

# 37.13 The naive cotangent complex

Section 37.13 of the Stacks Project, [Tag 0D0G](https://stacks.math.columbia.edu/tag/0D0G). 16 tags here are carried by 50 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D0H, a definition

[Tag 0D0H](https://stacks.math.columbia.edu/tag/0D0H) in the Stacks Project.

**`AlgebraicGeometry.Scheme.naiveCotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentComplex.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentComplex.lean#L70).

> **Stacks 0D0H.** The naive cotangent complex `NL_f = NL_{X/Y}` of a morphism of schemes
> `f : X ⟶ Y`: the naive cotangent complex of Stacks 08TN of the underlying morphism of ringed
> spaces of `f`, that is, `NL_{𝒪_X / f^{-1}𝒪_Y}`.

```lean
noncomputable def naiveCotangentComplex :
    CochainComplex (_root_.SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (J := Opens.grothendieckTopology X.toRingedSpace.carrier) X.toRingedSpace.sheaf)) ℤ
```

## Tag 0D0I, a lemma

[Tag 0D0I](https://stacks.math.columbia.edu/tag/0D0I) in the Stacks Project.

**`Stacks.NaiveCotangentAffineQuasiIso.quasiIso_comparisonMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentAffineQuasiIso.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentAffineQuasiIso.lean#L739). The attribute's comment: “the canonical map (NL_{A/R})~ to NL_{X/Y}|_V is an isomorphism in D(O_V)”.

> If `U` and `V` are affine, the canonical map `comparisonMap f hVU` from the sheaf associated
> to `NL_{A/R}` to the restriction of `NL_{X/Y}` to `V` is a quasi-isomorphism.

```lean
theorem quasiIso_comparisonMap (hU : IsAffineOpen U) (hV : IsAffineOpen V) :
    QuasiIso (comparisonMap f hVU)
```

## Tag 0D0J, a lemma

[Tag 0D0J](https://stacks.math.columbia.edu/tag/0D0J) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isZero_homology_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentCohomologySheaves.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentCohomologySheaves.lean#L51). The attribute's comment: “the vanishing outside degrees -1 and 0 only; quasi-coherence and H^0 = Omega are proved separately”.

> **Stacks 0D0J, vanishing clause.** The cohomology sheaves of the naive cotangent complex
> `NL_{X/Y}` of a morphism of schemes vanish outside degrees `-1` and `0`: the complex has no
> terms in those degrees, so it is exact there.

```lean
theorem isZero_homology_naiveCotangentComplex (i : ℤ) (hneg : i ≠ -1) (hzero : i ≠ 0) :
    IsZero ((naiveCotangentComplex f).homology i)
```

**`AlgebraicGeometry.Scheme.naiveCotangentExtZeroAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentExtZero.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentExtZero.lean#L237). The attribute's comment: “the Ext^0 reading of the degree-zero identification: Ext^0(NL_{X/Y}, G) = Hom(Omega_{X/Y}, G) for a morphism of schemes and an arbitrary sheaf of coefficients, the naive cotangent complex living in cohomological degrees at most zero”. References: SGA 7 VI (4.16), “identification Ext⁰(X₀”.

> **`Ext⁰_{𝒪_X}(NL_{X/Y}, 𝒢) = Hom_{𝒪_X}(Ω_{X/Y}, 𝒢)`.** The naive cotangent complex of a
> morphism of schemes lives in cohomological degrees `≤ 0`, so `Ext⁰` out of it is the group of
> homomorphisms out of its degree `0` cohomology sheaf, and that sheaf is the sheaf of relative
> differentials by [Stacks Project, Tag 0D0J].
>
> This is the `Ext⁰` term of the infinitesimal-automorphism clause of
> [Stacks Project, Tag 0DY9]: the source writes that clause's group first as
> `Ext⁰_{𝒪_X}(NL_{X/k}, 𝒪_X)` and then as `Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X)`, and this is the passage
> between the two. `f` is an arbitrary morphism of schemes and `𝒢` an arbitrary sheaf of
> `𝒪_X`-modules.

```lean
def naiveCotangentExtZeroAddEquiv {X Y : Scheme.{u}} (f : X ⟶ Y) (G : X.Modules) :
    naiveCotangentExt f G 0 ≃+ (Hom.relativeDifferentials f ⟶ G)
```

**`AlgebraicGeometry.Scheme.isQuasicoherent_homology_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentHomologyQuasicoherent.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentHomologyQuasicoherent.lean#L158). The attribute's comment: “quasi-coherence of the cohomology sheaves; not H^0 = Omega, not the vanishing”.

> **Stacks 0D0J, quasi-coherence clause.** Every cohomology sheaf of the naive cotangent
> complex `NL_{X/Y}` of a morphism of schemes is a quasi-coherent sheaf of `𝒪_X`-modules: in
> degree `-1` by the affine-local argument, in degree `0` because it is `Ω_{X/Y}`, and in every
> other degree because it is zero.

```lean
theorem isQuasicoherent_homology_naiveCotangentComplex {X Y : Scheme.{u}} (f : X ⟶ Y) (i : ℤ) :
    ((naiveCotangentComplex f).homology i).IsQuasicoherent
```

**`AlgebraicGeometry.Scheme.naiveCotangentComplexHomologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentHomologyZeroDifferentials.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentHomologyZeroDifferentials.lean#L66). The attribute's comment: “the degree-zero identification H^0 of NL with Omega; not quasi-coherence, not the vanishing in the other degrees”.

> **Stacks 0D0J, degree zero.** The degree `0` cohomology sheaf of the naive cotangent
> complex `NL_{X/Y}` of a morphism of schemes is the sheaf of relative differentials
> `Ω_{X/Y}`.

```lean
noncomputable def naiveCotangentComplexHomologyZeroIso :
    (naiveCotangentComplex f).homology 0 ≅ Hom.relativeDifferentials f
```

## Tag 0D0K, a lemma

[Tag 0D0K](https://stacks.math.columbia.edu/tag/0D0K) in the Stacks Project.

**`Stacks.NaiveCotangentFinitePresentation.exists_affine_quasiIso_associatedDouble_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentFinitePresentation.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentFinitePresentation.lean#L660). The attribute's comment: “the whole statement. `locally on X` is read as: for every point `x` of `X` there are affine opens `V ∋ x` of `X` and `U` of `Y` with `V ⊆ f^{-1}U`, and the complex of quasi-coherent `O_V`-modules is produced on that `V`. The source says `NL_{X/Y}` is quasi-isomorphic TO the two-term complex; what is produced here is a quasi-isomorphism FROM the two-term complex to `NL_{X/Y}|_V`, which is the same content, a quasi-isomorphism being invertible in `D(O_V)`. The two-term complex is `NL(P)` sheafified, for a presentation of `Gamma(X, V)` over `Gamma(Y, U)` with finitely many variables and finitely many relations, which exists because `f` is locally of finite presentation; its degree-0 term is finite free on the variables and its degree-(-1) term `I/I^2` is generated by the classes of the relations and no better, which is why the two degrees are given DIFFERENT finiteness assertions -- degree 0 `IsFinitePresentation`, degree -1 `IsFiniteType` -- exactly as the tag states. The quasi-isomorphism is the sheafification of the comparison `NL(P) -> NL_{A/R}` of [Stacks, Tag 00S1], taken in its HOMOTOPY EQUIVALENCE form so that it survives an additive functor, composed with the canonical map `(NL_{A/R})~ -> NL_{X/Y}|_V` of [Stacks, Tag 0D0I]; the target is `Scheme.naiveCotangentComplex f` ([Stacks, Tag 0D0H]) restricted along `V.iota`. The sole hypothesis is `[LocallyOfFinitePresentation f]`, which is the source's own: [Stacks, Tag 0D0K] is the lemma for a morphism locally of finite presentation. Every other input is proved: [Stacks, Tag 00S1] in `isHomotopyEquiv_nlMapCanonical`, [Stacks, Tag 0D0I] in `Stacks.NaiveCotangentAffineQuasiIso.quasiIso_comparisonMap`, and the finiteness of the two terms in `finitePresentation_cotangentSpace` and `finite_cotangent`”.

> **Stacks 0D0K.**  Let `f : X ⟶ Y` be locally of finite presentation and let `x` be a point of
> `X`.  Then there are affine opens `V ∋ x` of `X` and `U` of `Y` with `V ⊆ f^{-1}U`, a two-term
> complex `δ : M₁ ⟶ M₀` of `Γ(X, V)`-modules, and a quasi-isomorphism from the complex of sheaves
> of `𝒪_V`-modules associated to `δ` to the restriction of `NL_{X/Y}` to `V`, such that the
> degree-`0` term of that complex of sheaves is quasi-coherent of finite presentation and its
> degree-`-1` term is quasi-coherent of finite type.
>
> The two-term complex is `NL(P)` for a presentation `A = R[x_1, …, x_n]/(g_1, …, g_m)` of
> `A = Γ(X, V)` over `R = Γ(Y, U)` with finitely many variables and finitely many relations, which
> exists because `f` is locally of finite presentation.  Its degree-`0` term is finite free on the
> variables, hence finitely presented, and its degree-`-1` term `I/I²` is generated by the classes
> of the relations, hence finite — and no better, which is why the two degrees are given different
> finiteness assertions.  The quasi-isomorphism is the sheafification of the comparison
> `NL(P) ⟶ NL_{A/R}` of Stacks 00S1, which is a homotopy equivalence and therefore survives any
> additive functor, followed by the canonical map `(NL_{A/R})~ ⟶ NL_{X/Y}|_V` of Stacks 0D0I.

```lean
theorem exists_affine_quasiIso_associatedDouble_naiveCotangentComplex (f : X ⟶ Y)
    [LocallyOfFinitePresentation f] (x : X) :
    ∃ (U : Y.Opens) (V : X.Opens) (_ : IsAffineOpen U) (_ : IsAffineOpen V) (_ : x ∈ V)
      (_ : V ≤ f ⁻¹ᵁ U) (M₁ M₀ : ModuleCat.{u} Γ(X, V)) (δ : M₁ ⟶ M₀)
      (ψ : associatedDouble δ ⟶ restrictedNaiveCotangentComplex f (V := V)),
      QuasiIso ψ ∧ ((associatedDouble δ).X 0).IsFinitePresentation ∧
        ((associatedDouble δ).X (-1)).IsFiniteType ∧
        ((associatedDouble δ).X 0).IsQuasicoherent ∧
        ((associatedDouble δ).X (-1)).IsQuasicoherent
```

## Tag 0D0L, a lemma

[Tag 0D0L](https://stacks.math.columbia.edu/tag/0D0L) in the Stacks Project.

**`Stacks.Smooth.formallySmooth_iff_isZero_homology_negOne_and_isLocallyProjective_homology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentFormallySmoothConverse.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentFormallySmoothConverse.lean#L212).

> A morphism of schemes `f : X ⟶ Y` is formally smooth if and only if the degree `-1`
> cohomology sheaf of its naive cotangent complex vanishes and its degree `0` cohomology sheaf is
> locally projective.

```lean
theorem formallySmooth_iff_isZero_homology_negOne_and_isLocallyProjective_homology_zero :
    AlgebraicGeometry.FormallySmooth f ↔
      (IsZero ((Scheme.naiveCotangentComplex f).homology (-1)) ∧
        Scheme.Modules.IsLocallyProjective ((Scheme.naiveCotangentComplex f).homology 0))
```

## Tag 0D0M, a lemma

[Tag 0D0M](https://stacks.math.columbia.edu/tag/0D0M) in the Stacks Project.

**`Stacks.Smooth.formallyEtale_iff_isZero_homology_naiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentFormallyEtale.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentFormallyEtale.lean#L299).

> **[Stacks Project, Tag 0D0M].** A morphism of schemes `f : X ⟶ S` is formally étale if and
> only if both cohomology sheaves of its naive cotangent complex vanish,
> `H^{-1}(NL_{X/S}) = H^0(NL_{X/S}) = 0`.
>
> The forward implication is
> `Stacks.Smooth.isZero_homology_naiveCotangentComplex_of_formallyEtale` and the converse is
> `Stacks.Smooth.formallyEtale_of_isZero_homology_naiveCotangentComplex`.

```lean
theorem formallyEtale_iff_isZero_homology_naiveCotangentComplex :
    FormallyEtale f ↔
      IsZero ((Scheme.naiveCotangentComplex f).homology (-1)) ∧
        IsZero ((Scheme.naiveCotangentComplex f).homology 0)
```

## Tag 0D0N, a lemma

[Tag 0D0N](https://stacks.math.columbia.edu/tag/0D0N) in the Stacks Project.

**`Stacks.Smooth.smooth_iff_isZero_homology_negOne_and_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentSmoothCriterion.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentSmoothCriterion.lean#L172).

> **Smoothness read on the naive cotangent complex.** A morphism of schemes `f : X ⟶ S` is
> smooth if and only if it is locally of finite presentation, `H⁻¹(NL_{X/S}) = 0`, and
> `Ω_{X/S} = H⁰(NL_{X/S})` is finite locally free.

```lean
theorem smooth_iff_isZero_homology_negOne_and_isFiniteLocallyFree :
    AlgebraicGeometry.Smooth f ↔
      (AlgebraicGeometry.LocallyOfFinitePresentation f ∧
        IsZero ((Scheme.naiveCotangentComplex f).homology (-1)) ∧
        SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf)
          (Scheme.Hom.relativeDifferentials f))
```

**`Stacks.Smooth.smooth_iff_isZero_homology_negOne_and_isFiniteLocallyFree_homology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentSmoothCriterion.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentSmoothCriterion.lean#L193). The attribute's comment: “the third clause read on H^0(NL_{X/S}) rather than on Omega_{X/S}”.

> **Smoothness read on the naive cotangent complex, with the third clause on `H⁰(NL_{X/S})`.**
> A morphism of schemes `f : X ⟶ S` is smooth if and only if it is locally of finite presentation,
> `H⁻¹(NL_{X/S}) = 0`, and `H⁰(NL_{X/S})` is finite locally free.

```lean
theorem smooth_iff_isZero_homology_negOne_and_isFiniteLocallyFree_homology_zero :
    AlgebraicGeometry.Smooth f ↔
      (AlgebraicGeometry.LocallyOfFinitePresentation f ∧
        IsZero ((Scheme.naiveCotangentComplex f).homology (-1)) ∧
        SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf)
          ((Scheme.naiveCotangentComplex f).homology 0))
```

## Tag 0G7Z, a lemma

[Tag 0G7Z](https://stacks.math.columbia.edu/tag/0G7Z) in the Stacks Project.

**`AlgebraicGeometry.etale_iff_locallyOfFinitePresentation_and_isZero_naiveCotangentHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentEtale.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentEtale.lean#L239).

> **Étale morphisms by the naive cotangent complex.** A morphism of schemes `f : X ⟶ S` is
> étale if and only if it is locally of finite presentation and both cohomology sheaves
> `H⁻¹(NL_{X/S})` and `H⁰(NL_{X/S})` of its naive cotangent complex vanish.

```lean
theorem etale_iff_locallyOfFinitePresentation_and_isZero_naiveCotangentHomology (f : X ⟶ S) :
    Etale f ↔
      (LocallyOfFinitePresentation f ∧
        IsZero ((Scheme.naiveCotangentComplex f).homology (-1)) ∧
        IsZero ((Scheme.naiveCotangentComplex f).homology 0))
```

## Tag 0FV2, a lemma

[Tag 0FV2](https://stacks.math.columbia.edu/tag/0FV2) in the Stacks Project.

**`Stacks.Conormal.Sites.homologyNegOneIsoConormalSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalComparison/NaiveCotangentImmersionShift.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ConormalComparison/NaiveCotangentImmersionShift.lean#L153). The attribute's comment: “degree -1 clause: H^{-1}(NL_{Z/X}) is the conormal sheaf C_{Z/X}”.

> **Stacks 0FV2, degree `-1` clause.**  For an immersion of schemes `i : Z ⟶ X` the degree
> `-1` cohomology sheaf of the naive cotangent complex `NL_{Z/X}` is the conormal sheaf
> `𝒞_{Z/X}` of `Z` in `X`.
>
> Three identifications are composed.  `NL_{Z/X}` is the naive cotangent complex of the
> *canonical polynomial* presentation of `𝒪_Z` over `i^{-1}𝒪_X`, so its degree `-1` term is the
> conormal sheaf of that presentation and not of `i^{-1}𝒪_X ⟶ 𝒪_Z` itself; Stacks 08TL for the
> trivial presentation (`Stacks.SheafOfModules.quasiIso_trivialNaiveCotangentComplexComparison`)
> identifies the cohomology of the two complexes.  The complex of the trivial presentation is
> `I/I² ⟶ 0`, so its degree `-1` cohomology is `I/I²` on the nose
> (`Stacks.Conormal.Sites.trivialHomologyNegOneIso`).  Finally
> `Stacks.Conormal.Sites.sitesConormalSheafIsoConormalSheaf` identifies that sites-level `I/I²`
> with the geometric conormal sheaf `𝒞_{Z/X}`.

```lean
def homologyNegOneIsoConormalSheaf :
    (AlgebraicGeometry.Scheme.naiveCotangentComplex i).homology (-1) ≅
      (Stacks.Conormal.conormalSheaf i : Z.Modules)
```

**`Stacks.Conormal.Sites.quasiIso_conormalShiftComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalComparison/NaiveCotangentImmersionShift.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ConormalComparison/NaiveCotangentImmersionShift.lean#L243). The attribute's comment: “shift clause as a quasi-isomorphism of complexes C_{Z/X}[1] ⟶ NL_{Z/X}”.

> **Stacks 0FV2, the shift.**  For an immersion of schemes `i : Z ⟶ X` the canonical chain
> map from `𝒞_{Z/X}[1]` — the cochain complex with the conormal sheaf of `Z` in `X` in degree
> `-1` and zero in every other degree — to the naive cotangent complex `NL_{Z/X}` is a
> quasi-isomorphism.
>
> The source states the conclusion as an isomorphism `NL_{Z/X} ≅ 𝒞_{Z/X}[1]` in `D(𝒪_Z)`.  A
> quasi-isomorphism of cochain complexes of sheaves of `𝒪_Z`-modules is the scheme-level content
> of that statement: it is a map of honest complexes which the localisation functor to the derived
> category inverts.  The statement is given in that form, and the clause label says so.

```lean
theorem quasiIso_conormalShiftComparison : QuasiIso (conormalShiftComparison i)
```

**`AlgebraicGeometry.Scheme.isZero_homology_zero_naiveCotangentComplex_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentImmersionDegreeZero.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentImmersionDegreeZero.lean#L204). The attribute's comment: “degreewise form of the shift statement, degree 0 clause only: H^0(NL_{Z/X}) = 0; NOT the identification of H^{-1}(NL_{Z/X}) with the conormal sheaf”.

> **Stacks 0FV2, degree `0` clause.**  Let `i : Z ⟶ X` be an immersion of schemes.  Then the
> degree `0` cohomology sheaf of the naive cotangent complex `NL_{Z/X}` vanishes.
>
> The source states that `NL_{Z/X}` is isomorphic to `C_{Z/X}[1]` in `D(𝒪_Z)`, with `C_{Z/X}` the
> conormal sheaf of `Z` in `X`.  Since both sides are complexes concentrated in one degree, that
> assertion is the conjunction of the two degreewise statements `H⁻¹(NL_{Z/X}) ≅ C_{Z/X}` and
> `H⁰(NL_{Z/X}) = 0`.  The second is what is proved here; the first is not proved, here or
> anywhere in this library, and the attribute is scoped accordingly.

```lean
theorem isZero_homology_zero_naiveCotangentComplex_of_isImmersion {Z X : Scheme.{u}}
    (i : Z ⟶ X) [IsImmersion i] :
    Limits.IsZero ((naiveCotangentComplex i).homology 0)
```

## Tag 0E44, a lemma

[Tag 0E44](https://stacks.math.columbia.edu/tag/0E44) in the Stacks Project.

**`Stacks.NaiveCotangentSixTermSequence.pullbackToTotalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L346). The attribute's comment: “the canonical map f^*NL_{Y/Z} -> NL_{X/Z}, the chain map inducing the first and fourth arrows of the six term sequence”.

> **Stacks 0E44, the second arrow.**  The canonical map `f^*NL_{Y/Z} ⟶ NL_{X/Z}` of a pair of
> composable morphisms of schemes: the canonical map of Stacks 0E1Z of the underlying morphisms of
> ringed spaces, read on `NL_{X/Z} = NL_{f ≫ g}` through `totalCompIso`.

```lean
noncomputable def pullbackToTotalMap :
    pullbackNaiveCotangentComplex f g ⟶ Scheme.naiveCotangentComplex (f ≫ g)
```

**`Stacks.NaiveCotangentSixTermSequence.totalToRelativeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L354). The attribute's comment: “the canonical map NL_{X/Z} -> NL_{X/Y}, the chain map inducing the second and fifth arrows of the six term sequence”.

> **Stacks 0E44, the third arrow.**  The canonical map `NL_{X/Z} ⟶ NL_{X/Y}` of a pair of
> composable morphisms of schemes.

```lean
noncomputable def totalToRelativeMap :
    Scheme.naiveCotangentComplex (f ≫ g) ⟶ Scheme.naiveCotangentComplex f
```

**`Stacks.NaiveCotangentSixTermSequence.exact_sixTerm_negOne_total`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L432). The attribute's comment: “exactness of the six term sequence at its second term, H^{-1}(NL_{X/Z})”.

> **Stacks 0E44, exactness at `H^{-1}(NL_{X/Z})`.**  For morphisms of schemes `f : X ⟶ Y` and
> `g : Y ⟶ Z` the sequence
>
> `H^{-1}(f^*NL_{Y/Z}) ⟶ H^{-1}(NL_{X/Z}) ⟶ H^{-1}(NL_{X/Y})`
>
> of cohomology sheaves is exact at the middle term.  This is the corresponding assertion of
> Stacks 0E1Z for the underlying morphisms of ringed spaces.

```lean
theorem exact_sixTerm_negOne_total :
    (ShortComplex.mk (HomologicalComplex.homologyMap (pullbackToTotalMap f g) (-1))
      (HomologicalComplex.homologyMap (totalToRelativeMap f g) (-1))
      (homologyMap_pullbackToTotalMap_comp_totalToRelativeMap f g (-1))).Exact
```

**`Stacks.NaiveCotangentSixTermSequence.jacobiZariskiConnecting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L444). The attribute's comment: “the connecting map H^{-1}(NL_{X/Y}) -> H^0(f^*NL_{Y/Z}), the third arrow of the six term sequence”.

> **Stacks 0E44, the connecting map** `∂ : H^{-1}(NL_{X/Y}) ⟶ H^0(f^*NL_{Y/Z})` of the six
> term sequence, for morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ Z`: the connecting map of
> Stacks 0E1Z of the underlying morphisms of ringed spaces.

```lean
noncomputable def jacobiZariskiConnecting :
    (Scheme.naiveCotangentComplex f).homology (-1) ⟶
      (pullbackNaiveCotangentComplex f g).homology 0
```

**`Stacks.NaiveCotangentSixTermSequence.exact_sixTerm_negOne_relative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L484). The attribute's comment: “exactness of the six term sequence at its third term, H^{-1}(NL_{X/Y})”.

> **Stacks 0E44, exactness at `H^{-1}(NL_{X/Y})`.**  For morphisms of schemes `f : X ⟶ Y` and
> `g : Y ⟶ Z` the sequence
>
> `H^{-1}(NL_{X/Z}) ⟶ H^{-1}(NL_{X/Y}) --∂--> H^0(f^*NL_{Y/Z})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_sixTerm_negOne_relative :
    (ShortComplex.mk (HomologicalComplex.homologyMap (totalToRelativeMap f g) (-1))
      (jacobiZariskiConnecting f g)
      (homologyMap_totalToRelativeMap_comp_connecting f g)).Exact
```

**`Stacks.NaiveCotangentSixTermSequence.pullbackHomologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L546). The attribute's comment: “the fourth term: the identification H^0(f^*NL_{Y/Z}) = f^*Omega_{Y/Z} for the inverse-image-then-extend-scalars model of the pullback, the model the first four terms are written over”.

> **Stacks 0E44, the fourth term.**  The degree `0` cohomology sheaf of `f^*NL_{Y/Z}` is
> `f^*Ω_{Y/Z}`.
>
> The pullback is the one of Stacks 08TM and 0E1Z, the inverse image with scalars extended, which
> is the model the first four terms of the sequence are written over; `pullbackComplexIso`
> identifies it with Mathlib's `AlgebraicGeometry.Scheme.Modules.pullback`, for which the degree
> `0` identification is
> `Stacks.NaiveCotangentSixTermSequence.modulePullbackNaiveCotangentComplexHomologyZeroIso`.  It is
> this identification that makes the connecting map land in `f^*Ω_{Y/Z}`, so that the three terms
> proved here and the three degree `0` terms are one sequence.

```lean
noncomputable def pullbackHomologyZeroIso :
    (pullbackNaiveCotangentComplex f g).homology 0 ≅
      (Scheme.Modules.pullback f).obj (Scheme.Hom.relativeDifferentials g)
```

**`Stacks.NaiveCotangentSixTermSequence.connectingDifferentials`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L556). The attribute's comment: “the connecting map with its target written as f^*Omega_{Y/Z}”.

> **Stacks 0E44, the third arrow with its target written as `f^*Ω_{Y/Z}`.**  The connecting
> map of the six term sequence, read through the identification of its target `H^0(f^*NL_{Y/Z})`
> with `f^*Ω_{Y/Z}`.

```lean
noncomputable def connectingDifferentials :
    (Scheme.naiveCotangentComplex f).homology (-1) ⟶
      (Scheme.Modules.pullback f).obj (Scheme.Hom.relativeDifferentials g)
```

**`Stacks.NaiveCotangentSixTermSequence.exact_sixTerm_zero_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L569). The attribute's comment: “exactness of the six term sequence at its fourth term, H^0(f^*NL_{Y/Z}) = f^*Omega_{Y/Z}”.

> **Stacks 0E44, exactness at `H^0(f^*NL_{Y/Z})`.**  For morphisms of schemes `f : X ⟶ Y` and
> `g : Y ⟶ Z` the sequence
>
> `H^{-1}(NL_{X/Y}) --∂--> H^0(f^*NL_{Y/Z}) ⟶ H^0(NL_{X/Z})`
>
> of cohomology sheaves is exact at the middle term.

```lean
theorem exact_sixTerm_zero_pullback :
    (ShortComplex.mk (jacobiZariskiConnecting f g)
      (HomologicalComplex.homologyMap (pullbackToTotalMap f g) 0)
      (connecting_comp_homologyMap_pullbackToTotalMap f g)).Exact
```

**`Stacks.NaiveCotangentSixTermSequence.exact_sixTerm_zero_total`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 588](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L588). The attribute's comment: “exactness of the six term sequence at its fifth term, H^0(NL_{X/Z}) = Omega_{X/Z}”.

> **Stacks 0E44, exactness at `H^0(NL_{X/Z})`.**  For morphisms of schemes `f : X ⟶ Y` and
> `g : Y ⟶ Z` the sequence
>
> `H^0(f^*NL_{Y/Z}) ⟶ H^0(NL_{X/Z}) ⟶ H^0(NL_{X/Y})`
>
> of cohomology sheaves is exact at the middle term.  With the degree `0` identifications of
> Stacks 0D0J and `pullbackHomologyZeroIso` this is exactness at `Ω_{X/Z}`; it is stated on the
> cohomology sheaves so that it is the same sequence as the three nodes above.

```lean
theorem exact_sixTerm_zero_total :
    (ShortComplex.mk (HomologicalComplex.homologyMap (pullbackToTotalMap f g) 0)
      (HomologicalComplex.homologyMap (totalToRelativeMap f g) 0)
      (homologyMap_pullbackToTotalMap_comp_totalToRelativeMap f g 0)).Exact
```

**`Stacks.NaiveCotangentSixTermSequence.epi_homologyMap_totalToRelativeMap_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermFirstTerms.lean#L600). The attribute's comment: “the final `-> 0` of the six term sequence, its exactness at H^0(NL_{X/Y}) = Omega_{X/Y}”.

> **Stacks 0E44, the final `⟶ 0`.**  The canonical map `NL_{X/Z} ⟶ NL_{X/Y}` is surjective on
> degree `0` cohomology sheaves, that is, the six term sequence is exact at `H^0(NL_{X/Y})`.  With
> the degree `0` identification of Stacks 0D0J this is exactness at `Ω_{X/Y}`.

```lean
theorem epi_homologyMap_totalToRelativeMap_zero :
    Epi (HomologicalComplex.homologyMap (totalToRelativeMap f g) 0)
```

**`Stacks.NaiveCotangentSixTermSequence.isZero_homology_modulePullbackNaiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermSequence.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermSequence.lean#L166). The attribute's comment: “the vanishing of H^i(f^*NL_{Y/Z}) outside degrees -1 and 0 only”.

> **Stacks 0E44, the extent of the sequence.** The cohomology sheaves of `f^*NL_{Y/Z}` vanish
> outside degrees `-1` and `0`.  Together with the same statement for `NL_{X/Z}` and `NL_{X/Y}`
> (`AlgebraicGeometry.Scheme.isZero_homology_naiveCotangentComplex`) this is why the sequence of
> Stacks 0E44 has six terms, starting at `H^{-1}(f^*NL_{Y/Z})` and ending at `0` after the degree
> `0` cohomology sheaf of `NL_{X/Y}`.

```lean
theorem isZero_homology_modulePullbackNaiveCotangentComplex (i : ℤ) (hneg : i ≠ -1)
    (hzero : i ≠ 0) :
    IsZero ((modulePullbackNaiveCotangentComplex f g).homology i)
```

**`Stacks.NaiveCotangentSixTermSequence.modulePullbackNaiveCotangentComplexHomologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermSequence.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermSequence.lean#L180). The attribute's comment: “the fourth term for Mathlib's model of the pullback: the identification H^0(f^*NL_{Y/Z}) = f^*Omega_{Y/Z}, which Stacks.NaiveCotangentSixTermSequence.pullbackHomologyZeroIso carries to the model the sequence itself is written over”.

> **Stacks 0E44, the fourth term.** The degree `0` cohomology sheaf of `f^*NL_{Y/Z}` is
> `f^*Ω_{Y/Z}`.  The pullback of sheaves of modules along `f` is a left adjoint, hence preserves
> the cokernel that computes the degree `0` cohomology sheaf of a complex with nothing above
> degree `0`, and `H^0(NL_{Y/Z})` is `Ω_{Y/Z}` by Stacks 0D0J.

```lean
noncomputable def modulePullbackNaiveCotangentComplexHomologyZeroIso :
    (modulePullbackNaiveCotangentComplex f g).homology 0 ≅
      (Scheme.Modules.pullback f).obj (Scheme.Hom.relativeDifferentials g)
```

**`Stacks.NaiveCotangentSixTermSequence.differentialsSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermSequence.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentSixTermSequence.lean#L202). The attribute's comment: “the last three terms and their exactness, for the canonical maps of relative differentials of 01UX; the six term sequence itself, with the arrows induced by the canonical maps of naive cotangent complexes throughout, is in StacksFrontier.AlgebraicGeometry.MoreMorphisms.NaiveCotangentSixTermFirstTerms”.

> **Stacks 0E44, the last three terms.** For morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ Z`
> the last three terms of the six term sequence of cohomology sheaves,
>
> `f^*Ω_{Y/Z} ⟶ Ω_{X/Z} ⟶ Ω_{X/Y} ⟶ 0`,
>
> form an exact sequence: the composite of the two canonical maps of relative differentials is
> zero, the resulting short complex is exact at `Ω_{X/Z}`, and the second map is an epimorphism.
> The three terms are the degree `0` cohomology sheaves of `f^*NL_{Y/Z}`, of `NL_{X/Z}` and of
> `NL_{X/Y}`, by `modulePullbackNaiveCotangentComplexHomologyZeroIso` and by Stacks 0D0J.

```lean
theorem differentialsSequence_exact :
    ∃ h : Scheme.Hom.relativeDifferentialsMap f g (f ≫ g) (𝟙 Z)
        (Category.comp_id (f ≫ g)).symm ≫ f.toRelativeDifferentials g = 0,
      (ShortComplex.mk _ _ h).Exact ∧ Epi (f.toRelativeDifferentials g)
```

## Tag 0FV3, a lemma

[Tag 0FV3](https://stacks.math.columbia.edu/tag/0FV3) in the Stacks Project.

**`Stacks.NaiveCotangentCompositionTriangle.coneMap_comp_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangle.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangle.lean#L150). The attribute's comment: “the canonical map f^*NL_{Y/Z} -> C(NL_{X/Z} -> NL_{X/Y})[-1] of 0E1Z and its compatibility, up to the sign of the cocone projection, with the canonical map f^*NL_{Y/Z} -> NL_{X/Z}; NOT its invertibility, which is where the complete intersection hypothesis enters and which is isIso_Q_map_coneMap_of_lci”.

> **Stacks 0FV3**, the comparison.  The canonical map
> `f^*NL_{Y/Z} ⟶ C(NL_{X/Z} ⟶ NL_{X/Y})[-1]` of Stacks 0E1Z, composed with the projection of the
> mapping cocone onto `NL_{X/Z}`, is the negative of the canonical map `f^*NL_{Y/Z} ⟶ NL_{X/Z}`.
> This is what makes the comparison a lift of that canonical map; the sign is the one between the
> projection out of the mapping cocone and the projection of Stacks 0E1Z.

```lean
theorem coneMap_comp_fst :
    ringedSpaceNaiveCotangentConeMap f g ≫ mappingCocone.fst (relativeNaiveCotangentMap f g) =
      -pulledNaiveCotangentMap f g
```

**`Stacks.NaiveCotangentCompositionTriangle.triangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangle.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangle.lean#L182). The attribute's comment: “the distinguished triangle C(NL_{X/Z} -> NL_{X/Y})[-1] -> NL_{X/Z} -> NL_{X/Y} -> C(NL_{X/Z} -> NL_{X/Y})[-1][1] of D(O_X), whose second morphism is the canonical map, together with the canonical map of 0E1Z into its first vertex (coneMap_comp_fst); NOT the invertibility of that comparison, which is where the complete intersection hypothesis enters, and NOT the recovery of the six-term exact sequence of 0E44 -- those two are isIso_Q_map_coneMap_of_lci and lciTriangle_recovers_sixTerm, and the triangle with f^*NL_{Y/Z} as its first vertex is lciTriangle_distinguished”.

> **Stacks 0FV3**, the triangle.  The triangle on the canonical map `NL_{X/Z} ⟶ NL_{X/Y}`,
> with the shift by `-1` of its cone as first vertex, is a distinguished triangle of `D(𝒪_X)`.

```lean
theorem triangle_distinguished : triangle f g ∈ distTriang _
```

**`Stacks.NaiveCotangentCompositionTriangle.isIso_Q_map_coneMap_of_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangleLci.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangleLci.lean#L126). The attribute's comment: “the canonical map f^*NL_{Y/Z} -> C(NL_{X/Z} -> NL_{X/Y})[-1] of 0E1Z is an ISOMORPHISM in D(O_X) when X -> Y is a complete intersection morphism, which is the reduction the source's proof makes”.

> **Stacks 0FV3, the isomorphism.**  For morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ Z` with
> `f` a local complete intersection morphism, the canonical map
>
> `f^*NL_{Y/Z} ⟶ C(NL_{X/Z} ⟶ NL_{X/Y})[-1]`
>
> of Stacks 0E1Z is an isomorphism in `D(𝒪_X)`.
>
> This is the reduction the source makes: the triangle of Stacks 0FV3 is the triangle of the
> mapping cocone of `NL_{X/Z} ⟶ NL_{X/Y}` with its first vertex replaced by `f^*NL_{Y/Z}` along
> this isomorphism.  The map is surjective on `H^{-1}` and an isomorphism on `H⁰` for an arbitrary
> pair of composable morphisms of ringed spaces; injectivity on `H^{-1}` is what the complete
> intersection hypothesis supplies, through Stacks 07D4 at the stalks.

```lean
theorem isIso_Q_map_coneMap_of_lci (hf : IsLocalCompleteIntersectionMorphism f) :
    IsIso (DerivedCategory.Q.map
      (ringedSpaceNaiveCotangentConeMap f.toLRSHom.toShHom g.toLRSHom.toShHom))
```

**`Stacks.NaiveCotangentCompositionTriangle.lciTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangleLci.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangleLci.lean#L170). The attribute's comment: “the canonical distinguished triangle f^*NL_{Y/Z} -> NL_{X/Z} -> NL_{X/Y} -> f^*NL_{Y/Z}[1] of D(O_X) for a complete intersection morphism X -> Y, with its first two morphisms the canonical maps (lciTriangle_mor₁, lciTriangle_mor₂)”. References: SGA 6 VIII (2.6), “more general”.

> **Stacks 0FV3.**  For morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ Z` with `f` a local
> complete intersection morphism, the canonical triangle
>
> `f^*NL_{Y/Z} ⟶ NL_{X/Z} ⟶ NL_{X/Y} ⟶ f^*NL_{Y/Z}[1]`
>
> is a distinguished triangle of `D(𝒪_X)`: it is the triangle of the mapping cocone of the
> canonical map `NL_{X/Z} ⟶ NL_{X/Y}`, which is distinguished, with its first vertex replaced along
> the comparison of Stacks 0E1Z, an isomorphism by `isIso_Q_map_coneMap_of_lci`.  Its first two
> morphisms are the canonical maps, by `lciTriangle_mor₁` and `lciTriangle_mor₂`.

```lean
theorem lciTriangle_distinguished (hf : IsLocalCompleteIntersectionMorphism f) :
    lciTriangle f g hf ∈ distTriang _
```

**`Stacks.NaiveCotangentCompositionTriangle.lciTriangle_recovers_sixTerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangleLci.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentCompositionTriangleLci.lean#L197). The attribute's comment: “the recovery of the six-term exact sequence of 0E44 from lciTriangle: its first two morphisms are the images under Q of the canonical chain maps f^*NL_{Y/Z} -> NL_{X/Z} and NL_{X/Z} -> NL_{X/Y}, and the six-term sequence of the maps those induce on cohomology sheaves, with the connecting morphism of the long exact sequence of the cone, is exact at its four interior terms and ends in `-> 0`”.

> **Stacks 0FV3: the triangle recovers the six-term exact sequence of Stacks 0E44.**  The long
> exact sequence of cohomology sheaves of the triangle
>
> `f^*NL_{Y/Z} ⟶ NL_{X/Z} ⟶ NL_{X/Y} ⟶ f^*NL_{Y/Z}[1]`
>
> is the six-term exact sequence
>
> `H^{-1}(f^*NL_{Y/Z}) ⟶ H^{-1}(NL_{X/Z}) ⟶ H^{-1}(NL_{X/Y}) --∂--> H⁰(f^*NL_{Y/Z}) ⟶`
> `H⁰(NL_{X/Z}) ⟶ H⁰(NL_{X/Y}) ⟶ 0`:
>
> its five assertions are exactness at the four interior terms and the final `⟶ 0`.  The two arrows
> are the maps induced by the canonical chain maps, whose images under `DerivedCategory.Q` are the
> first two morphisms of the triangle by `lciTriangle_mor₁` and `lciTriangle_mor₂`, and the
> connecting morphism is `Stacks.SheafOfModules.ringedSpaceJacobiZariskiConnecting`, the connecting
> morphism of the long exact sequence of the cone read through the comparison of Stacks 0E1Z.  The
> sequence has six terms and no more because all three vertices have vanishing cohomology outside
> degrees `-1` and `0`.

```lean
theorem lciTriangle_recovers_sixTerm (hf : IsLocalCompleteIntersectionMorphism f) :
    (lciTriangle f g hf).mor₁ =
        DerivedCategory.Q.map
          (pulledNaiveCotangentMap f.toLRSHom.toShHom g.toLRSHom.toShHom) ∧
      (lciTriangle f g hf).mor₂ =
        DerivedCategory.Q.map
          (relativeNaiveCotangentMap f.toLRSHom.toShHom g.toLRSHom.toShHom) ∧
      (ringedSpaceJacobiZariskiHomologySequence f.toLRSHom.toShHom
        g.toLRSHom.toShHom (-1)).Exact ∧
      (ShortComplex.mk
        (HomologicalComplex.homologyMap
          (relativeNaiveCotangentMap f.toLRSHom.toShHom g.toLRSHom.toShHom) (-1))
        (ringedSpaceJacobiZariskiConnecting f.toLRSHom.toShHom g.toLRSHom.toShHom)
        (homologyMap_comp_ringedSpaceJacobiZariskiConnecting
          f.toLRSHom.toShHom g.toLRSHom.toShHom)).Exact ∧
      (ShortComplex.mk
        (ringedSpaceJacobiZariskiConnecting f.toLRSHom.toShHom g.toLRSHom.toShHom)
        (HomologicalComplex.homologyMap
          (pulledNaiveCotangentMap f.toLRSHom.toShHom g.toLRSHom.toShHom) 0)
        (ringedSpaceJacobiZariskiConnecting_comp_homologyMap
          f.toLRSHom.toShHom g.toLRSHom.toShHom)).Exact ∧
      (ringedSpaceJacobiZariskiHomologySequence f.toLRSHom.toShHom
        g.toLRSHom.toShHom 0).Exact ∧
      Epi (HomologicalComplex.homologyMap
        (relativeNaiveCotangentMap f.toLRSHom.toShHom g.toLRSHom.toShHom) 0)
```

**`Stacks.NaiveCotangentCompositionTriangle.connecting_comp_homologyMap_eq_homologyδOfTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean#L142). The attribute's comment: “the connecting map of the six-term sequence of 0E44, read along H^0 of the canonical map of 0E1Z, is the connecting morphism of the long exact sequence of the triangle of the mapping cocone of NL_{X/Z} -> NL_{X/Y}”.

> **The connecting map of Stacks 0E44 is a triangle connecting morphism.**  Composed with the
> map induced on `H⁰` by the canonical map of Stacks 0E1Z it is the connecting morphism of the long
> exact sequence of the triangle
>
> `C(NL_{X/Z} ⟶ NL_{X/Y})[-1] ⟶ NL_{X/Z} ⟶ NL_{X/Y} ⟶ C(NL_{X/Z} ⟶ NL_{X/Y})[-1][1]`
>
> of the mapping cocone, whose image in `D(𝒪_X)` is the triangle of Stacks 0FV3 before its first
> vertex is replaced by `f^*NL_{Y/Z}` along that same map.

```lean
theorem connecting_comp_homologyMap_eq_homologyδOfTriangle :
    jacobiZariskiConnecting f g ≫ HomologicalComplex.homologyMap
        (ringedSpaceNaiveCotangentConeMap (ringedSpaceHom f) (ringedSpaceHom g)) 0 =
      CochainComplex.homologyδOfTriangle
        (CochainComplex.mappingCocone.triangle (iteratedRelativeMap f g)) (-1) 0 (by omega)
```

**`Stacks.NaiveCotangentCompositionTriangle.lciSchemeTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean#L226). The attribute's comment: “the canonical distinguished triangle f^*NL_{Y/Z} -> NL_{X/Z} -> NL_{X/Y} -> f^*NL_{Y/Z}[1] of D(O_X) for a complete intersection morphism X -> Y, written over the complexes and the two canonical chain maps of the six-term sequence of 0E44 (lciSchemeTriangle_mor₁, lciSchemeTriangle_mor₂)”. References: SGA 6 VIII (2.6), “more general”.

> **Stacks 0FV3.**  For morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ Z` with `f` a local
> complete intersection morphism, the canonical triangle
>
> `f^*NL_{Y/Z} ⟶ NL_{X/Z} ⟶ NL_{X/Y} ⟶ f^*NL_{Y/Z}[1]`
>
> is a distinguished triangle of `D(𝒪_X)`, with `NL_{X/Z}` the naive cotangent complex of `f ≫ g`
> and its first two morphisms the two canonical chain maps of the six-term exact sequence of
> Stacks 0E44.
>
> It is the triangle of `Stacks.NaiveCotangentCompositionTriangle.lciTriangle` with its second
> vertex transported along the identification of `NL_{f ≫ g}` with its iterated spelling.

```lean
theorem lciSchemeTriangle_distinguished (hf : IsLocalCompleteIntersectionMorphism f) :
    lciSchemeTriangle f g hf ∈ distTriang _
```

**`Stacks.NaiveCotangentCompositionTriangle.δ_lciSchemeTriangle_comp_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean#L262). The attribute's comment: “the connecting morphism of the triangle, read along H^0 of the canonical map of 0E1Z, is the negative of the connecting morphism of the long exact sequence of the triangle of the mapping cocone of NL_{X/Z} -> NL_{X/Y}”.

> **The connecting morphism of the triangle of Stacks 0FV3.**  Composed with the map induced on
> `H⁰` by the canonical map of Stacks 0E1Z it is the negative of the connecting morphism of the
> triangle of the mapping cocone of `NL_{X/Z} ⟶ NL_{X/Y}`.  The sign is the one between the
> projection out of the mapping cocone and the projection through which Stacks 0E1Z characterises
> its canonical map; it is the price of the triangle's first morphism being the canonical map
> `f^*NL_{Y/Z} ⟶ NL_{X/Z}` with no sign.

```lean
theorem δ_lciSchemeTriangle_comp_map (hf : IsLocalCompleteIntersectionMorphism f) :
    DerivedCategory.HomologySequence.δ (lciSchemeTriangle f g hf) (-1) 0 (by omega) ≫
        (DerivedCategory.homologyFunctor (_root_.SheafOfModules.{u}
            (Stacks.SheafOfModules.Tensor.ringSheaf
              (J := Opens.grothendieckTopology (X.toRingedSpace : TopCat))
              X.toRingedSpace.sheaf)) (0 : ℤ)).map (DerivedCategory.Q.map
          (ringedSpaceNaiveCotangentConeMap (ringedSpaceHom f) (ringedSpaceHom g))) =
      -(DerivedCategory.HomologySequence.δ
        (triangle (ringedSpaceHom f) (ringedSpaceHom g)) (-1) 0 (by omega))
```

**`Stacks.NaiveCotangentCompositionTriangle.lciSchemeTriangle_recovers_sixTerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentLciTriangleSixTerm.lean#L307). The attribute's comment: “the recovery of the six-term exact sequence of 0E44 from lciSchemeTriangle: its first two morphisms are the images under Q of the two canonical chain maps of 0E44, its connecting morphism and the connecting map of 0E44 are both the connecting morphism of the long exact sequence of the triangle of the mapping cocone read along H^0 of the canonical map of 0E1Z, and the six-term sequence of those arrows is exact at its four interior terms and ends in `-> 0`”.

> **Stacks 0FV3: the triangle recovers the six-term exact sequence of Stacks 0E44.**  For
> morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ Z` with `f` a local complete intersection
> morphism, the long exact sequence of cohomology sheaves of the distinguished triangle
>
> `f^*NL_{Y/Z} ⟶ NL_{X/Z} ⟶ NL_{X/Y} ⟶ f^*NL_{Y/Z}[1]`
>
> is the six-term exact sequence
>
> `H^{-1}(f^*NL_{Y/Z}) ⟶ H^{-1}(NL_{X/Z}) ⟶ H^{-1}(NL_{X/Y}) --∂--> f^*Ω_{Y/Z} ⟶ Ω_{X/Z} ⟶`
> `Ω_{X/Y} ⟶ 0`
>
> of Stacks 0E44.  The nine assertions below are: its first two morphisms are the images under
> `DerivedCategory.Q` of the two canonical chain maps `pullbackToTotalMap` and
> `totalToRelativeMap` of Stacks 0E44, which induce four of the five arrows; its connecting
> morphism and the connecting map `jacobiZariskiConnecting` of Stacks 0E44 both become, along the
> map induced on `H⁰` by the canonical map of Stacks 0E1Z, the connecting morphism of the long
> exact sequence of the triangle of the mapping cocone — up to the sign of the cocone projection;
> and the sequence of those arrows is exact at its four interior terms and ends in `⟶ 0`.  The
> last three terms are `f^*Ω_{Y/Z}`, `Ω_{X/Z}` and `Ω_{X/Y}` by
> `Stacks.NaiveCotangentSixTermSequence.pullbackHomologyZeroIso` and Stacks 0D0J.

```lean
theorem lciSchemeTriangle_recovers_sixTerm (hf : IsLocalCompleteIntersectionMorphism f) :
    (lciSchemeTriangle f g hf).mor₁ = DerivedCategory.Q.map (pullbackToTotalMap f g) ∧
      (lciSchemeTriangle f g hf).mor₂ = DerivedCategory.Q.map (totalToRelativeMap f g) ∧
      DerivedCategory.HomologySequence.δ (lciSchemeTriangle f g hf) (-1) 0 (by omega) ≫
          (DerivedCategory.homologyFunctor (_root_.SheafOfModules.{u}
            (Stacks.SheafOfModules.Tensor.ringSheaf
              (J := Opens.grothendieckTopology (X.toRingedSpace : TopCat))
              X.toRingedSpace.sheaf)) (0 : ℤ)).map (DerivedCategory.Q.map
            (ringedSpaceNaiveCotangentConeMap (ringedSpaceHom f) (ringedSpaceHom g))) =
        -(DerivedCategory.HomologySequence.δ
          (triangle (ringedSpaceHom f) (ringedSpaceHom g)) (-1) 0 (by omega)) ∧
      jacobiZariskiConnecting f g ≫ HomologicalComplex.homologyMap
          (ringedSpaceNaiveCotangentConeMap (ringedSpaceHom f) (ringedSpaceHom g)) 0 =
        CochainComplex.homologyδOfTriangle
          (CochainComplex.mappingCocone.triangle (iteratedRelativeMap f g)) (-1) 0 (by omega) ∧
      (ShortComplex.mk (HomologicalComplex.homologyMap (pullbackToTotalMap f g) (-1))
        (HomologicalComplex.homologyMap (totalToRelativeMap f g) (-1))
        (homologyMap_pullbackToTotalMap_comp_totalToRelativeMap f g (-1))).Exact ∧
      (ShortComplex.mk (HomologicalComplex.homologyMap (totalToRelativeMap f g) (-1))
        (jacobiZariskiConnecting f g)
        (homologyMap_totalToRelativeMap_comp_connecting f g)).Exact ∧
      (ShortComplex.mk (jacobiZariskiConnecting f g)
        (HomologicalComplex.homologyMap (pullbackToTotalMap f g) 0)
        (connecting_comp_homologyMap_pullbackToTotalMap f g)).Exact ∧
      (ShortComplex.mk (HomologicalComplex.homologyMap (pullbackToTotalMap f g) 0)
        (HomologicalComplex.homologyMap (totalToRelativeMap f g) 0)
        (homologyMap_pullbackToTotalMap_comp_totalToRelativeMap f g 0)).Exact ∧
      Epi (HomologicalComplex.homologyMap (totalToRelativeMap f g) 0)
```

## Tag 0G80, a lemma

[Tag 0G80](https://stacks.math.columbia.edu/tag/0G80) in the Stacks Project.

**`AlgebraicGeometry.Smooth.of_comp_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/CancelEtale.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/CancelEtale.lean#L51).

> Let `X → Y → Z` be morphisms of schemes. If `X → Z` is smooth and `Y → Z` is étale, then
> `X → Y` is smooth.

```lean
public theorem Smooth.of_comp_of_etale {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    [Smooth (f ≫ g)] [Etale g] : Smooth f
```

## Tag 0FV4, a lemma

[Tag 0FV4](https://stacks.math.columbia.edu/tag/0FV4) in the Stacks Project.

**`Stacks.NaiveCotangentFormallySmoothComparison.quasiIso_naiveCotangentToDifferentialsSingle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFormallySmoothComparison.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFormallySmoothComparison.lean#L260). The attribute's comment: “the 0D0L input NL_{P/Y} = Omega_{P/Y} as a quasi-isomorphism of complexes”.

> **The 0D0L input of [Stacks Project, Tag 0FV4].**  For a formally smooth morphism of schemes
> `g : P ⟶ Y` the canonical chain map `NL_{P/Y} ⟶ Ω_{P/Y}[0]` is a quasi-isomorphism: the naive
> cotangent complex of `g` is identified with its sheaf of relative differentials placed in degree
> `0`.
>
> This is the step the proof of 0FV4 records as `NL_{P/Y} = Ω_{P/Y}`.  Its two ingredients are the
> clauses of [Stacks Project, Tag 0D0L] proved for a formally smooth morphism, namely the vanishing
> of the cohomology sheaves outside degree `0`
> (`Stacks.Smooth.isZero_homology_naiveCotangentComplex_of_formallySmooth`, which rests on
> `Stacks.Smooth.isZero_homology_negOne_naiveCotangentComplex_of_formallySmooth`), together with
> the degree-zero identification `H⁰(NL_{P/Y}) = Ω_{P/Y}` of [Stacks Project, Tag 0D0J].  Those are
> statements about cohomology sheaves; what is added here is the chain map itself, which is what
> 0FV4 uses.
>
> As in `Stacks.Conormal.Sites.quasiIso_conormalShiftComparison` — the corresponding step of 0FV4
> coming from [Stacks Project, Tag 0FV2] — the conclusion is given as a quasi-isomorphism of
> complexes of sheaves of `𝒪_P`-modules, which is the chain-level content of the source's
> identification in `D(𝒪_P)`: a map of honest complexes that the localisation functor to the
> derived category inverts.
>
> The other three steps of 0FV4's proof are not covered; see the `Scope` section of this file.

```lean
theorem quasiIso_naiveCotangentToDifferentialsSingle
    (hg : Stacks.Smooth.FormallySmoothScheme g) :
    QuasiIso (naiveCotangentToDifferentialsSingle g)
```

**`Stacks.NaiveCotangentFormallySmoothComparison.isIso_Q_map_naiveCotangentToDifferentialsSingle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFormallySmoothComparison.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFormallySmoothComparison.lean#L285). The attribute's comment: “the 0D0L input: NL_{P/Y} -> Omega_{P/Y}[0] is invertible in D(O_P)”.

> **The 0D0L input of [Stacks Project, Tag 0FV4], read in `D(𝒪_P)`.**  For a formally smooth
> morphism of schemes `g : P ⟶ Y` the canonical chain map `NL_{P/Y} ⟶ Ω_{P/Y}[0]` becomes an
> isomorphism in the derived category of sheaves of `𝒪_P`-modules; that is, `NL_{P/Y}` and
> `Ω_{P/Y}[0]` are canonically isomorphic objects of `D(𝒪_P)`.
>
> This is the form `NL_{P/Y} = Ω_{P/Y}` in which the proof of 0FV4 uses the step.  Its content is
> that of `quasiIso_naiveCotangentToDifferentialsSingle`, the localisation functor to the derived
> category inverting exactly the quasi-isomorphisms; what is added is that the two complexes are
> compared as objects of `D(𝒪_P)` rather than by their cohomology sheaves.  The derived category is
> the one of `HasDerivedCategory.standard`, taken as a local instance.
>
> Only this one step of 0FV4 is covered; see the `Scope` section of this file.

```lean
theorem isIso_Q_map_naiveCotangentToDifferentialsSingle
    (hg : Stacks.Smooth.FormallySmoothScheme g) :
    IsIso (DerivedCategory.Q.map (naiveCotangentToDifferentialsSingle g))
```

**`Stacks.NaiveCotangentImmersionFormallySmooth.naiveCotangentIsoConormalDifferentialComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentImmersionFormallySmooth.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentImmersionFormallySmooth.lean#L129). The attribute's comment: “the canonical isomorphism NL_{X/Y} = (C_{X/P} -> i^*Omega_{P/Y}) in D(O_X), with C_{X/P} in degree -1, for f = g . i with i an immersion and g formally smooth”. References: SGA 6 VIII (2.2), “more general”.

> **[Stacks Project, Tag 0FV4].**  Let `f : X ⟶ Y` be a morphism of schemes which factors as
> `f = g ∘ i` with `i : X ⟶ P` an immersion and `g : P ⟶ Y` formally smooth (for example smooth,
> by [Stacks Project, Tag 02H6]).  Then there is a canonical isomorphism
>
> `NL_{X/Y} ≅ (𝒞_{X/P} ⟶ i^*Ω_{P/Y})`
>
> in `D(𝒪_X)`, where the conormal sheaf `𝒞_{X/P}` is placed in degree `-1`.
>
> The right-hand side is `Stacks.ConormalSequenceRight.conormalDifferentialComplex i g`: the
> two-term complex whose degree `-1` term is the conormal sheaf of [Stacks Project, Tag 01R2],
> whose degree `0` term is `i^*Ω_{P/Y}`, and whose only differential is the first arrow of the
> conormal sequence of [Stacks Project, Tag 01UZ].
>
> See the `Route` section of this file; the proof does not go through the distinguished triangle of
> [Stacks Project, Tag 0FV3] and so has no sign to track.

```lean
def naiveCotangentIsoConormalDifferentialComplex (f : X ⟶ Y) (hf : f = i ≫ g)
    (hg : Stacks.Smooth.FormallySmoothScheme g) :
    DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f : CochainComplex X.Modules ℤ) ≅
      DerivedCategory.Q.obj (Stacks.ConormalSequenceRight.conormalDifferentialComplex i g)
```

**`Stacks.NaiveCotangentPullbackFormallySmooth.isZero_homology_negOne_modulePullbackNaiveCotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentPullbackFormallySmooth.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentPullbackFormallySmooth.lean#L339). The attribute's comment: “the pullback step: H^{-1}(i^*NL_{P/Y}) = 0, the detail the source omits”.

> **The pullback step of [Stacks Project, Tag 0FV4]: the vanishing `H^{-1}(i^*NL_{P/Y}) = 0`.**
> For a formally smooth morphism of schemes `g : P ⟶ Y` and an arbitrary morphism `i : X ⟶ P` the
> degree `-1` cohomology sheaf of the termwise pullback along `i` of `NL_{P/Y}` vanishes.
>
> This is the step the source records as a small detail omitted, and obtains from local projectivity
> of `Ω_{P/Y}` — the locally projective clause of [Stacks Project, Tag 0D0L] — through
> [Stacks Project, Tag 0FUY].  The pullback of sheaves of modules is only right exact, so this does
> not follow from the vanishing `H^{-1}(NL_{P/Y}) = 0` before pullback; what makes it true is that
> local projectivity splits the one differential of `NL_{P/Y}` at every stalk, and a split
> monomorphism stays one under any functor.  See the `Route` section of this file.
>
> Only this step of 0FV4 is covered; see the `Scope` section of this file.

```lean
theorem isZero_homology_negOne_modulePullbackNaiveCotangentComplex
    (hg : Stacks.Smooth.FormallySmoothScheme g) :
    IsZero ((modulePullbackNaiveCotangentComplex i g).homology (-1))
```

**`Stacks.NaiveCotangentPullbackFormallySmooth.quasiIso_pullbackNaiveCotangentToDifferentialsSingle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentPullbackFormallySmooth.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentPullbackFormallySmooth.lean#L385). The attribute's comment: “the pullback step: i^*NL_{P/Y} -> i^*Omega_{P/Y}[0] is a quasi-isomorphism”.

> **The pullback step of [Stacks Project, Tag 0FV4].** For a formally smooth morphism of schemes
> `g : P ⟶ Y` and an arbitrary morphism `i : X ⟶ P` the canonical chain map
> `i^*NL_{P/Y} ⟶ i^*Ω_{P/Y}[0]` is a quasi-isomorphism: the pullback along `i` of the naive cotangent
> complex of `g` is identified with the pullback of its sheaf of relative differentials, placed in
> degree `0`.
>
> This is the form `NL_{P/Y} = Ω_{P/Y}` in which the proof of 0FV4 uses the tag *after* pulling back
> along `i`, and it is the step that does not follow from
> `Stacks.NaiveCotangentFormallySmoothComparison.quasiIso_naiveCotangentToDifferentialsSingle`, the
> same statement before pullback, the pullback of sheaves of modules not being exact.  Its three
> ingredients are the vanishing
> `isZero_homology_negOne_modulePullbackNaiveCotangentComplex` proved above, and the two clauses
> of [Stacks Project, Tag 0E44] available in
> `StacksFrontier.AlgebraicGeometry.MoreMorphisms.NaiveCotangentSixTermSequence`: the identification
> `H^0(i^*NL_{P/Y}) = i^*Ω_{P/Y}` and the vanishing of the cohomology sheaves outside degrees `-1`
> and `0`.
>
> Only this step of 0FV4 is covered; see the `Scope` section of this file.

```lean
theorem quasiIso_pullbackNaiveCotangentToDifferentialsSingle
    (hg : Stacks.Smooth.FormallySmoothScheme g) :
    QuasiIso (pullbackNaiveCotangentToDifferentialsSingle i g)
```

**`Stacks.NaiveCotangentPullbackFormallySmooth.isIso_Q_map_pullbackNaiveCotangentToDifferentialsSingle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentPullbackFormallySmooth.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentPullbackFormallySmooth.lean#L415). The attribute's comment: “the pullback step in D(O_X): i^*NL_{P/Y} = i^*Omega_{P/Y}[0]”.

> **The pullback step of [Stacks Project, Tag 0FV4], read in `D(𝒪_X)`.** For a formally smooth
> morphism of schemes `g : P ⟶ Y` and an arbitrary morphism `i : X ⟶ P` the canonical chain map
> `i^*NL_{P/Y} ⟶ i^*Ω_{P/Y}[0]` becomes an isomorphism in the derived category of sheaves of
> `𝒪_X`-modules; that is, `i^*NL_{P/Y}` and `i^*Ω_{P/Y}[0]` are canonically isomorphic objects of
> `D(𝒪_X)`.
>
> This is the form in which the proof of 0FV4 uses the step: the first vertex of its distinguished
> triangle is `i^*NL_{P/Y}`, and what the proof needs of it is that it is `i^*Ω_{P/Y}` in degree `0`.
> Its content is that of
> `quasiIso_pullbackNaiveCotangentToDifferentialsSingle`, the localisation functor to the derived
> category inverting exactly the quasi-isomorphisms.  The
> derived category is the one of `HasDerivedCategory.standard`, taken as a local instance.
>
> Only this step of 0FV4 is covered; see the `Scope` section of this file.

```lean
theorem isIso_Q_map_pullbackNaiveCotangentToDifferentialsSingle
    (hg : Stacks.Smooth.FormallySmoothScheme g) :
    IsIso (DerivedCategory.Q.map (pullbackNaiveCotangentToDifferentialsSingle i g))
```

## Tag 0FV5, a lemma

[Tag 0FV5](https://stacks.math.columbia.edu/tag/0FV5) in the Stacks Project.

**`Stacks.NaiveCotangentBaseChange.isIso_homologyMap_zero_baseChangeMapOfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentBaseChangeHomologyCartesian.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentBaseChangeHomologyCartesian.lean#L476). The attribute's comment: “the degree-zero ISOMORPHISM, for a CARTESIAN square (`hsq : IsPullback g' f' f g`) and NO other hypothesis -- in particular no flatness. The canonical map is CONSTRUCTED, not assumed: `Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison` is the source's own composite of the [Stacks, Tag 08TM] identification of `(g')^*NL_{X/Y}` with a base change (`Stacks.SheafOfModules.pulledNaiveCotangentComparison`), the base-change map `NL_{B/A} (x)_B C -> NL_{C/A}` of [Stacks, Tag 0E1Y] (`Stacks.SheafOfModules.spaceBaseChangeNaiveCotangentMap`) for the tower `(g')^-1 f^-1 O_Y -> (g')^-1 O_X -> O_{X'}`, and the relative map `NL_{C/A} -> NL_{C/B}` (`Stacks.SheafOfModules.spaceRelativeNaiveCotangentComplexMap`) for the tower through `(f')^-1 O_{Y'}`. The base-ring comparison it is taken against is the CANONICAL one of the square, `AlgebraicGeometry.BaseChangeStalk.baseRingComparison`, with its compatibility `AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp`; it is built from the square and is not a `Classical.choose` of a non-unique existence statement. It is the same map the flat statements [Stacks, Tag 0FJZ] and [Stacks, Tag 0FK0] are about. PROVED: the reduction to the stalks ([Stacks, Tag 08TL], through `AlgebraicGeometry.SheafOfModules.isIso_homologyMap_iff_forall_stalk`); the degreewise vanishing outside degrees -1 and 0; and the stalkwise statement `isBijectiveOnCokernel_stalkFunctor_map_baseChangeMapOfComparison`, which is `Stacks.NaiveCotangentTowerStalk.isBijectiveOnCokernel_stalkFunctor_map_towerComposite` read through the stalk identification of the naive cotangent complex ([Stacks, Tag 0D09], the stalk-level form of [Stacks, Tag 0D0I]) and fed with the ring-level ARBITRARY base change [Stacks, Tag 0FUZ] `NaiveCotangent.naiveCotangentComplex_baseChange_homology`, composed with localization of the target [Stacks, Tag 00S7] in `NaiveCotangent.isH₀IsoH₁Surj_nlExtensionBaseChangeMap_of_isLocalization_tensor`. The one geometric input is the identification of `O_{X',x'}` as a localization of `O_{Y',f'(x')} (x)_{O_{Y,y}} O_{X,g'(x')}`, `AlgebraicGeometry.BaseChangeStalk.stalk_isLocalization_of_isPullback_inverseImage_comm` ([Stacks, Tag 01JR]), and that is the one place cartesianness is used. The companion clause, the `H^{-1}` surjection, is `Stacks.NaiveCotangentBaseChange.epi_homologyMap_negOne_baseChangeMapOfComparison`”.

> **Stacks 0FV5, the degree-zero isomorphism.**  For a cartesian square of schemes the
> canonical map `(g')^*NL_{X/Y} ⟶ NL_{X'/Y'}` induces an isomorphism on degree-zero cohomology.
>
> No flatness is assumed anywhere, and the canonical map is constructed and not assumed: it is
> `Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison` taken against the canonical
> base-ring comparison `AlgebraicGeometry.BaseChangeStalk.baseRingComparison` of the square.

```lean
theorem isIso_homologyMap_zero_baseChangeMapOfComparison (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y')
    (g' : X' ⟶ X) (hsq : IsPullback g' f' f g) :
    IsIso (HomologicalComplex.homologyMap
      (baseChangeMapOfComparison f f' g' (baseRingComparison f f' g' g hsq.w)
        (baseRingComparison_comp f f' g' g hsq.w)) 0)
```

**`Stacks.NaiveCotangentBaseChange.epi_homologyMap_negOne_baseChangeMapOfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentBaseChangeHomologyCartesian.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentBaseChangeHomologyCartesian.lean#L514). The attribute's comment: “the degree-minus-one SURJECTION, for a CARTESIAN square (`hsq : IsPullback g' f' f g`) and NO other hypothesis -- in particular no flatness. The canonical map is the one described on `Stacks.NaiveCotangentBaseChange.isIso_homologyMap_zero_baseChangeMapOfComparison`, the same constructed map `Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison` taken against the canonical base-ring comparison of the square. PROVED: the reduction of EPIMORPHY to the stalks (`AlgebraicGeometry.SheafOfModules.epi_homologyMap_iff_forall_stalk`, the epimorphy counterpart of [Stacks, Tag 08TL]); the degreewise vanishing outside degrees -1 and 0; and the stalkwise statement `isSurjectiveOnKernel_stalkFunctor_map_baseChangeMapOfComparison`, which is `Stacks.NaiveCotangentTowerStalk.isSurjectiveOnKernel_stalkFunctor_map_towerComposite` fed with the ring-level ARBITRARY base change [Stacks, Tag 0FUZ]. Only SURJECTIVITY on the degree -1 cycles is assumed and only a surjection is concluded, which is what the source asserts and all that [Stacks, Tag 0FUZ] supplies: injectivity there is the half flatness would buy, and is the content of the stronger [Stacks, Tag 0FJZ] / [Stacks, Tag 0FK0]. The companion clause, the `H^0` isomorphism, is `Stacks.NaiveCotangentBaseChange.isIso_homologyMap_zero_baseChangeMapOfComparison`”.

> **Stacks 0FV5, the degree-minus-one surjection.**  For a cartesian square of schemes the
> canonical map `(g')^*NL_{X/Y} ⟶ NL_{X'/Y'}` induces a surjection on degree-minus-one
> cohomology.
>
> No flatness is assumed anywhere, and nothing is claimed about injectivity in degree `-1`: the
> source's `H^{-1}` assertion is a surjection and not an isomorphism, and that is exactly what the
> ring-level statement provides.

```lean
theorem epi_homologyMap_negOne_baseChangeMapOfComparison (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y')
    (g' : X' ⟶ X) (hsq : IsPullback g' f' f g) :
    Epi (HomologicalComplex.homologyMap
      (baseChangeMapOfComparison f f' g' (baseRingComparison f f' g' g hsq.w)
        (baseRingComparison_comp f f' g' g hsq.w)) (-1))
```

**`AlgebraicGeometry.Scheme.isIso_baseChangeNaiveCotangentHomologyZeroMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentBaseChangeHomology.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentBaseChangeHomology.lean#L677). The attribute's comment: “the degree-zero ISOMORPHISM, for a CARTESIAN square, with no hypothesis beyond the cartesianness the source itself assumes. The map is `AlgebraicGeometry.Scheme.baseChangeNaiveCotangentHomologyZeroMap`, the canonical map `(g')^*Omega_{X/Y} -> Omega_{X'/Y'}` of [Stacks, Tag 01UV] (`AlgebraicGeometry.Scheme.Hom.relativeDifferentialsMap`, characterized there by compatibility with the universal derivations) read through the degree-zero identification `H^0(NL) = Omega` of [Stacks, Tag 0D0J] (`AlgebraicGeometry.Scheme.naiveCotangentComplexHomologyZeroIso`) at both ends. Like the source's own map it is defined from COMMUTATIVITY alone, and cartesianness is used only for invertibility, through [Stacks, Tag 01V0] (`AlgebraicGeometry.Scheme.Hom.isIso_relativeDifferentialsMap_of_isPullback`, which is itself proved outright from the cartesian-stalk localization and `KaehlerDifferential.tensorKaehlerEquivOfFormallyEtalePushout`). This is a SECOND, independent route to the tag's `H^0` clause, through the sheaf of relative differentials. The tag's two clauses for the canonical map of COMPLEXES are proved outright at `Stacks.NaiveCotangentBaseChange.isIso_homologyMap_zero_baseChangeMapOfComparison` and `Stacks.NaiveCotangentBaseChange.epi_homologyMap_negOne_baseChangeMapOfComparison`, which take the same canonical base-ring comparison of the square that [Stacks, Tag 0FJZ] does. NOT covered here: that the map of this statement is the one induced on `H^0` by that map of complexes. Comparing the two needs the identification of Mathlib's `AlgebraicGeometry.Scheme.Modules.pullback` -- the functor `Omega` and its canonical maps are stated over -- with the inverse-image-then-extend-scalars model that map of complexes is stated over, which is the open input recorded at `StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/StructureSheaf.lean`”.

> **Stacks Project, Tag 0FV5, the degree-zero isomorphism.**  For a cartesian square of
> schemes the canonical map `(g')^*H^0(NL_{X/Y}) ⟶ H^0(NL_{X'/Y'})` is an isomorphism.
>
> The map is `AlgebraicGeometry.Scheme.baseChangeNaiveCotangentHomologyZeroMap`, defined for every
> commutative square; cartesianness is used only here, through Stacks 01V0.  See the tag clause
> for what this statement does and does not cover.

```lean
theorem isIso_baseChangeNaiveCotangentHomologyZeroMap (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y')
    (g' : X' ⟶ X) (hcart : IsPullback g' f' f g) :
    IsIso (baseChangeNaiveCotangentHomologyZeroMap f g f' g' hcart.w)
```

## Tag 0FJZ, a lemma

[Tag 0FJZ](https://stacks.math.columbia.edu/tag/0FJZ) in the Stacks Project.

**`Stacks.NaiveCotangentFlatBaseChange.quasiIso_baseChangeMapOfComparison_of_flat_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFlatBaseChange.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFlatBaseChange.lean#L239). The attribute's comment: “the flat-base-change quasi-isomorphism, with no hypotheses beyond a CARTESIAN square (`hsq : IsPullback g' f' f g`) and `[Flat g]`. The canonical map is CONSTRUCTED, not assumed: `Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison` is the source's own composite of the [Stacks, Tag 08TM] identification of `(g')^*NL_{X/Y}` with a base change (`Stacks.SheafOfModules.pulledNaiveCotangentComparison`), the base-change map `NL_{B/A} (x)_B C -> NL_{C/A}` of [Stacks, Tag 0E1Y] (`Stacks.SheafOfModules.spaceBaseChangeNaiveCotangentMap`) for the tower `(g')^-1 f^-1 O_Y -> (g')^-1 O_X -> O_{X'}`, and the relative map `NL_{C/A} -> NL_{C/B}` (`Stacks.SheafOfModules.spaceRelativeNaiveCotangentComplexMap`) for the tower through `(f')^-1 O_{Y'}`. The base-ring comparison it is taken against is the CANONICAL one of the square, `AlgebraicGeometry.BaseChangeStalk.baseRingComparison`, together with its compatibility `AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp`; it is built from the square and is not a `Classical.choose` of a non-unique existence statement. PROVED: the construction of the map; the degreewise vanishing outside degrees -1 and 0 (`isZero_pulledComplex_X`); the reduction of quasi-isomorphy to the stalks (`quasiIso_baseChangeMapOfComparison_of_forall_stalk`, resting on [Stacks, Tag 08TL] `AlgebraicGeometry.SheafOfModules.quasiIso_of_forall_stalk_quasiIso`); and the stalkwise statement itself, `Stacks.NaiveCotangentFlatBaseChangeStalk.quasiIso_stalkFunctor_map_baseChangeMapOfComparison`. That stalkwise statement is `Stacks.NaiveCotangentTowerStalk.quasiIso_stalkFunctor_map_towerComposite` fed with the ring-level flat base change `NaiveCotangent.isQuasiIso_nlExtensionBaseChangeMap_of_flat_base` ([Stacks, Tag 00S4]), read through the stalk identification of the naive cotangent complex ([Stacks, Tag 0D09], `Stacks.SheafOfModules.stalkLegNegOne` / `stalkLegZero` / `stalkLeg_d`). Its two ring-level inputs are both discharged here: the flatness of the stalk of the canonical base-ring comparison, which `AlgebraicGeometry.BaseChangeStalk.stalkFunctor_map_baseRingComparison` identifies with the stalk map of `g` conjugated by three isomorphisms and which Mathlib's `AlgebraicGeometry.Flat.stalkMap` then makes flat, so `[Flat g]` does work here and is not decorative; and the identification of `O_{X',x'}` as a localization of `O_{Y',y'} (x)_{O_{Y,y}} O_{X,x}`, which is `AlgebraicGeometry.BaseChangeStalk.stalk_isLocalization_of_isPullback_inverseImage_comm` ([Stacks, Tag 01JR]) and is the one place cartesianness of the square is used. SCOPE: the statement is about the undecorated comparison `(g')^*NL_{X/Y} -> NL_{X'/Y'}`; nothing is claimed here about the derived pullback `L(g')^*NL_{X/Y}`”.

> **Flat base change.**  For a cartesian square of schemes whose lower horizontal morphism
> `g : Y' ⟶ Y` is flat, the canonical comparison `(g')^*NL_{X/Y} ⟶ NL_{X'/Y'}`, taken against the
> canonical base-ring comparison `AlgebraicGeometry.BaseChangeStalk.baseRingComparison` of the
> square, is a quasi-isomorphism.

```lean
theorem quasiIso_baseChangeMapOfComparison_of_flat_base (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y')
    (g' : X' ⟶ X) (hsq : IsPullback g' f' f g) [AlgebraicGeometry.Flat g] :
    QuasiIso (baseChangeMapOfComparison f f' g'
      (AlgebraicGeometry.BaseChangeStalk.baseRingComparison f f' g' g hsq.w)
      (AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp f f' g' g hsq.w))
```

## Tag 0FK0, a lemma

[Tag 0FK0](https://stacks.math.columbia.edu/tag/0FK0) in the Stacks Project.

**`Stacks.NaiveCotangentDerivedFlatBaseChange.isIso_derivedBaseChangeMapOfComparison_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentDerivedFlatBaseChange.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentDerivedFlatBaseChange.lean#L206). The attribute's comment: “the SECOND clause -- the DERIVED comparison `L(g')^* NL_{X/Y} -> NL_{X'/Y'}` is a quasi-isomorphism when `NL_{X/Y}` has tor-amplitude in [-1,0] -- with no hypotheses beyond a CARTESIAN square (`hsq : IsPullback g' f' f g`), `[Flat f]` and that tor-amplitude. The first clause is `Stacks.NaiveCotangentFlatBaseChange.quasiIso_baseChangeMapOfComparison_of_flat_algebra`. The DERIVED PULLBACK is not assumed: it is `Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback`, the total left derived functor of termwise pullback of [Stacks, Tag 06YJ], which exists for every morphism of ringed spaces, and the comparison `L(g')^* K -> (g')^* K` at a complex is `Stacks.DerivedPullback.Composition.derivedPullbackComparisonOnComplex`. TOR AMPLITUDE is the ringed-space notion of [Stacks, Tag 08CG], `Stacks.Cohomology.TorAmplitude.HasTorAmplitude`, tested against EVERY `O_X`-module. The map is CONSTRUCTED, not assumed: `derivedBaseChangeMapOfComparison` is the Tag 06YJ comparison, then the identification `pulledComplexIso` of Mathlib's termwise pullback with the inverse-image-then-extend-scalars model, then the first clause's map of complexes `Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison`, taken against the CANONICAL base-ring comparison `AlgebraicGeometry.BaseChangeStalk.baseRingComparison` of the square. PROVED HERE: that `NL_{X/Y}` is K-flat under the tor-amplitude hypothesis (`kFlat_naiveCotangentComplex_of_hasTorAmplitude`), which is the whole content of the clause beyond the first -- its degree 0 term is flat because each stalk is the free cotangent space of the canonical presentation of the stalk map (`Stacks.SheafOfModules.isFlat_naiveCotangentComplex_X_zero`, [Stacks, Tag 05NE] plus `Algebra.Generators.cotangentSpaceBasis`), so its degree -1 term is flat by the ringed-space form of [Stacks, Tag 0653] (`Stacks.Cohomology.TorAmplitude.DoubleFlat.isFlat_X_negOne_of_hasTorAmplitude`, the stupid filtration of a two-term complex fed to [Stacks, Tag 08CJ] (1)), and a bounded-above complex of flat modules is K-flat by [Stacks, Tag 06YQ]; and that a K-flat complex inverts the Tag 06YJ comparison (`isIso_derivedPullbackComparisonOnComplex_of_kFlat`). The two models of `(g')^*` are identified by `RingedSpaceModuleAdjunction.modulePullbackIsoTwoStep`, proved here from uniqueness of left adjoints, which closes the input that `StacksFrontier/AlgebraicGeometry/EtaleAlgebra/FlatBaseChange/StructureSheaf.lean` had recorded as open. SCOPE: the undecorated first clause is on `Stacks.NaiveCotangentFlatBaseChange.quasiIso_baseChangeMapOfComparison_of_flat_algebra`; the two declarations together are the whole tag”.

> **Stacks 0FK0, the derived clause.**  For a cartesian square of schemes whose right vertical
> morphism `f : X ⟶ Y` is flat and whose naive cotangent complex `NL_{X/Y}` has Tor amplitude in
> `[-1, 0]`, the canonical derived comparison `L(g')^*NL_{X/Y} ⟶ NL_{X'/Y'}` is an isomorphism in
> `D(𝒪_{X'})`.
>
> The Tor amplitude makes `NL_{X/Y}` K-flat, so the comparison `L(g')^*NL_{X/Y} ⟶ (g')^*NL_{X/Y}`
> is invertible by Stacks 06YJ; the remaining factor is the base change map of complexes, which is
> a quasi-isomorphism by the first clause.

```lean
theorem isIso_derivedBaseChangeMapOfComparison_of_flat (f : X ⟶ Y) (g : Y' ⟶ Y) (f' : X' ⟶ Y')
    (g' : X' ⟶ X) (hsq : IsPullback g' f' f g) [AlgebraicGeometry.Flat f]
    (htor : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      (DerivedCategory.Q.obj (Scheme.naiveCotangentComplex f)) (-1) 0) :
    IsIso (derivedBaseChangeMapOfComparison f f' g'
      (AlgebraicGeometry.BaseChangeStalk.baseRingComparison f f' g' g hsq.w)
      (AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp f f' g' g hsq.w))
```

**`Stacks.NaiveCotangentFlatBaseChange.quasiIso_baseChangeMapOfComparison_of_flat_algebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFlatBaseChange.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NaiveCotangentFlatBaseChange.lean#L296). The attribute's comment: “the FIRST clause -- the quasi-isomorphism when `X -> Y` is flat -- with no hypotheses beyond a CARTESIAN square (`hsq : IsPullback g' f' f g`) and `[Flat f]`. The canonical map is CONSTRUCTED, not assumed, exactly as on `Stacks.NaiveCotangentFlatBaseChange.quasiIso_baseChangeMapOfComparison_of_flat_base`: `Stacks.NaiveCotangentFlatBaseChange.baseChangeMapOfComparison` is the source's own composite of the [Stacks, Tag 08TM] identification of `(g')^*NL_{X/Y}` with a base change (`Stacks.SheafOfModules.pulledNaiveCotangentComparison`), the base-change map `NL_{B/A} (x)_B C -> NL_{C/A}` of [Stacks, Tag 0E1Y] (`Stacks.SheafOfModules.spaceBaseChangeNaiveCotangentMap`) for the tower `(g')^-1 f^-1 O_Y -> (g')^-1 O_X -> O_{X'}`, and the relative map `NL_{C/A} -> NL_{C/B}` (`Stacks.SheafOfModules.spaceRelativeNaiveCotangentComplexMap`) for the tower through `(f')^-1 O_{Y'}`. The base-ring comparison it is taken against is the CANONICAL one of the square, `AlgebraicGeometry.BaseChangeStalk.baseRingComparison`, together with its compatibility `AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp`; it is built from the square and is not a `Classical.choose` of a non-unique existence statement. PROVED: the construction of the map; the degreewise vanishing outside degrees -1 and 0 (`isZero_pulledComplex_X`); the reduction of quasi-isomorphy to the stalks (`quasiIso_baseChangeMapOfComparison_of_forall_stalk`, resting on [Stacks, Tag 08TL] `AlgebraicGeometry.SheafOfModules.quasiIso_of_forall_stalk_quasiIso`); and the stalkwise statement itself, `Stacks.NaiveCotangentFlatAlgebraBaseChangeStalk` `.quasiIso_stalkFunctor_map_baseChangeMapOfComparison`. That stalkwise statement is `Stacks.NaiveCotangentTowerStalk.quasiIso_stalkFunctor_map_towerComposite` fed with the ring-level base change for a flat algebra `NaiveCotangent.isQuasiIso_nlExtensionBaseChangeMap_of_flat_algebra`, read through the stalk identification of the naive cotangent complex ([Stacks, Tag 0D09] / [Stacks, Tag 0098]). That ring-level statement is proved here from the two elementwise inputs of [Stacks, Tag 0FJU]: surjectivity on the degree -1 cycles and bijectivity on the cokernels, which hold for an arbitrary base change by [Stacks, Tag 0FUZ] (`NaiveCotangent.naiveCotangentComplex_baseChange_homology`), and injectivity on those cycles, which is what flatness of the algebra buys (`NaiveCotangent.cotangent_intrinsic_baseChange_cycle_injective_of_flat`); then flat base change to the pushout is composed with localization of the target over a fixed base ([Stacks, Tag 00S7]). Its two geometric inputs are both discharged here: the flatness of the stalk of the first map of the tower, which `AlgebraicGeometry.BaseChangeStalk.stalkInverseImageBaseRingIso_hom_comp_stalkMap` identifies with the stalk map of `f` conjugated by two isomorphisms and which Mathlib's `AlgebraicGeometry.Flat.stalkMap` then makes flat, so `[Flat f]` does work here and is not decorative; and the identification of `O_{X',x'}` as a localization of `O_{Y',y'} (x)_{O_{Y,y}} O_{X,x}`, which is `AlgebraicGeometry.BaseChangeStalk.stalk_isLocalization_of_isPullback_inverseImage_comm` ([Stacks, Tag 01JR]) and is the one place cartesianness of the square is used. SCOPE: the statement is about the undecorated comparison `(g')^*NL_{X/Y} -> NL_{X'/Y'}`, which is the tag's first clause; nothing is claimed here about the tag's second clause, the DERIVED comparison `L(g')^*NL_{X/Y} -> NL_{X'/Y'}` under Tor amplitude in [-1,0]”.

> **Base change along a flat morphism.**  For a cartesian square of schemes whose right
> vertical morphism `f : X ⟶ Y` is flat, the canonical comparison `(g')^*NL_{X/Y} ⟶ NL_{X'/Y'}`,
> taken against the canonical base-ring comparison
> `AlgebraicGeometry.BaseChangeStalk.baseRingComparison` of the square, is a quasi-isomorphism.

```lean
theorem quasiIso_baseChangeMapOfComparison_of_flat_algebra (f : X ⟶ Y) (g : Y' ⟶ Y)
    (f' : X' ⟶ Y') (g' : X' ⟶ X) (hsq : IsPullback g' f' f g) [AlgebraicGeometry.Flat f] :
    QuasiIso (baseChangeMapOfComparison f f' g'
      (AlgebraicGeometry.BaseChangeStalk.baseRingComparison f f' g' g hsq.w)
      (AlgebraicGeometry.BaseChangeStalk.baseRingComparison_comp f f' g' g hsq.w))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.13, Tag 0D0G](https://stacks.math.columbia.edu/tag/0D0G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
