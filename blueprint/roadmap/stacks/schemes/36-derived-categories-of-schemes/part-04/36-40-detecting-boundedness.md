---
declaration: section
origin: cited
lean: Stacks.Koszul.Truncation.truncGE_restriction_of_hom_koszul_eq_zero, Stacks.Koszul.Truncation.hom_koszul_eq_zero_of_truncGE_restriction, Stacks.Koszul.Truncation.truncLE_restriction_koszul_criterion, Stacks.DerivedQCoh.eventually_subsingleton_hom_iff_truncGE_of_isPerfect, Stacks.Perfect.eventually_subsingleton_hom_iff_truncLE_of_isLE, Stacks.SheafOfModules.tfae_minus_of_isPerfect_generator, Stacks.Cohomology.ExtensionByZeroClosedSupport.isPerfect_jShriek_of_closedSupport_and_restrict, Stacks.SheafOfModules.eventually_subsingleton_shiftedHom_iff_ext
statement: formalized
proof: formalized
---

# 36.40 Detecting Boundedness

Section 36.40 of the Stacks Project, [Tag 0GEI](https://stacks.math.columbia.edu/tag/0GEI). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GEJ, a lemma

[Tag 0GEJ](https://stacks.math.columbia.edu/tag/0GEJ) in the Stacks Project.

**`Stacks.Koszul.Truncation.truncGE_restriction_of_hom_koszul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/KoszulHighDegreeOrthogonality.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/KoszulHighDegreeOrthogonality.lean#L462). The attribute's comment: “(2) implies (1)”.

> **[Stacks, Tag 0GEJ], the implication "Koszul orthogonality implies truncated
> restriction".** Let `f₁, …, f_r ∈ A`, let `U = ⋃ᵢ D(f_i) ⊆ Spec A`, let `j : U ⟶ Spec A` be the
> inclusion and let `K` be the sheafified Koszul complex of the sequence. Let `E` be an object of
> `D_QCoh(𝒪_{Spec A})`. If every morphism `K⟦-n⟧ ⟶ E` vanishes for `n ≥ a`, then the canonical map
> `E ⟶ Rj_*(E|_U)` becomes invertible after truncation in degrees `≥ a`.
>
> This is condition (2) of the source implying condition (1), at the source's own index: the
> premise is at `a` and the conclusion at `a`.
>
> The cone `N` of the unit restricts to zero on `U`, receives no morphism from `K⟦-n⟧` for
> `n ≥ a - 1`, and has quasi-coherent cohomology sheaves — the last because `E` does and `Rj_*`
> preserves quasi-coherent cohomology along a quasi-compact open immersion ([Stacks, Tag 08D5]).
> The graded detection statement
> `Stacks.Koszul.Truncation.isZero_homology_of_forall_hom_koszulObject_eq_zero` then kills the
> homology of `N` in degrees `≥ a - 1`, which is what makes the truncated map invertible. That is
> where the commutative algebra of the source sits: the Koszul power triangles of
> [Stacks, Tag 062C], the lifting lemma of [Stacks, Tag 08E3] and the affine comparison
> `D(A) ≌ D_QCoh(𝒪_{Spec A})` of [Stacks, Tag 06Z0]. The two other inputs of the source are
> proved too: the Koszul object restricts to zero on `U` by
> `Stacks.Koszul.OpenComplement.isZero_derivedRestrict_koszulObject`, and `Rj_*` is fully faithful
> by the instance
> `Stacks.Duality.OpenImmersion.isIso_derivedRestrictPushforwardAdjunction_counit_app`.

```lean
theorem truncGE_restriction_of_hom_koszul_eq_zero
    (E : DerivedCategory (Spec (CommRingCat.of A)).Modules) (hE : qcohSpec A E) (a : ℤ)
    (h : ∀ n : ℤ, a ≤ n → Subsingleton ((koszulObject f)⟦-n⟧ ⟶ E)) :
    IsIso ((DerivedCategory.TStructure.t.truncGE a).map
      ((derivedRestrictPushforwardAdjunction (openComplement f).ι).unit.app E))
```

**`Stacks.Koszul.Truncation.hom_koszul_eq_zero_of_truncGE_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/KoszulHighDegreeOrthogonality.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/KoszulHighDegreeOrthogonality.lean#L495). The attribute's comment: “(1) implies (2) with a replaced by a + r, not the published a + 1, which is false for r ≥ 2 — see the module docstring for the counterexample over k[x,y]”.

> **[Stacks, Tag 0GEJ], the implication "truncated restriction implies Koszul orthogonality
> `r` degrees up".** In the situation above, if the canonical map `E ⟶ Rj_*(E|_U)` is invertible
> after truncation in degrees `≥ a`, then every morphism `K⟦-n⟧ ⟶ E` vanishes for `n ≥ a + r`.
>
> The argument spends the window
> `Stacks.Koszul.Truncation.subsingleton_hom_koszulObject_shift_of_isLE`, which is the perfectness
> of `K`: `K` is a bounded complex of finite free modules in degrees `-r, …, 0`, so `Hom(K⟦-m⟧, M)`
> sees only the homology of `M` in the `r + 1` degrees `m - r, …, m`. It is applied to
> `τ_{≤a-1}E` and to `τ_{≤a-1}(Rj_*(E|_U))`, both of which have quasi-coherent cohomology
> sheaves — and quasi-coherence is not a convenience here, the window being false without it.
>
> **The index is `a + r`, and the `a + 1` of the published statement of the tag is false for
> `r ≥ 2`.** This is an approved erratum of the Stacks Project, recorded against the tag; the
> Stacks source text is left as published. The module documentation gives the counterexample
> over `k[x, y]`, where `a + r` is sharp.

```lean
theorem hom_koszul_eq_zero_of_truncGE_restriction
    (E : DerivedCategory (Spec (CommRingCat.of A)).Modules) (hE : qcohSpec A E) (a : ℤ)
    (h : IsIso ((DerivedCategory.TStructure.t.truncGE a).map
      ((derivedRestrictPushforwardAdjunction (openComplement f).ι).unit.app E))) :
    ∀ n : ℤ, a + (r : ℤ) ≤ n → Subsingleton ((koszulObject f)⟦-n⟧ ⟶ E)
```

## Tag 0GEK, a lemma

[Tag 0GEK](https://stacks.math.columbia.edu/tag/0GEK) in the Stacks Project.

**`Stacks.Koszul.Truncation.truncLE_restriction_koszul_criterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/KoszulTruncatedOrthogonality.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/KoszulTruncatedOrthogonality.lean#L335). The attribute's comment: “Corrected per errata.md (0GEK, wrong index): for E in D\_QCoh, (1) at a implies (2) at a, and (2) at a+1 implies (1) at a. The printed '(2) implies (1)' at the same a is false (Stacks.Koszul.Errata.erratum\_0GEK: A = k[x], f = (x), E = 𝒪\_X, a = 0); the printed '(1) implies (2) with a replaced by a-1' follows from the first conjunct”.

> Let `f₁, …, f_r ∈ A`, let `U = ⋃ᵢ D(f_i) ⊆ X = Spec A`, let `j : U ⟶ X` be the inclusion, let
> `K` be the sheafified Koszul complex of the sequence, let `E` be an object of `D_QCoh(𝒪_X)` and let
> `a ∈ ℤ`. Write (1) at `a` for "the canonical map `τ_{≤a}E ⟶ τ_{≤a}Rj_*(E|_U)` is an isomorphism"
> and (2) at `a` for "every morphism `K⟦-n⟧ ⟶ E` with `n ≤ a` vanishes". Then (1) at `a` implies
> (2) at `a`, and (2) at `a + 1` implies (1) at `a`.
>
> This is [Stacks, Tag 0GEK] corrected per `errata.md` (entry 0GEK, false statement, wrong index):
> the printed "(2) implies (1)" at the same `a` is false (`Stacks.Koszul.Errata.erratum_0GEK`, with
> `A = k[x]`, `f = (x)`, `E = 𝒪_X`, `a = 0`, proved on the affine side `D(A) ≌ D_QCoh(𝒪_X)`),
> and the printed "(1) implies (2) with `a` replaced by `a - 1`" is contained in the first
> conjunct.

```lean
theorem truncLE_restriction_koszul_criterion
    (E : DerivedCategory (Spec (CommRingCat.of A)).Modules)
    (hE : DerivedCategoryB.derivedCategoryB (A := (Spec (CommRingCat.of A)).Modules)
      (SheafOfModules.isQuasicoherent (Spec (CommRingCat.of A)).ringCatSheaf) E)
    (a : ℤ) :
    (IsIso ((DerivedCategory.TStructure.t.truncLE a).map
        ((derivedRestrictPushforwardAdjunction (openComplement f).ι).unit.app E)) →
      ∀ n : ℤ, n ≤ a → Subsingleton ((koszulObject f)⟦-n⟧ ⟶ E)) ∧
    ((∀ n : ℤ, n ≤ a + 1 → Subsingleton ((koszulObject f)⟦-n⟧ ⟶ E)) →
      IsIso ((DerivedCategory.TStructure.t.truncLE a).map
        ((derivedRestrictPushforwardAdjunction (openComplement f).ι).unit.app E)))
```

## Tag 0GEL, a lemma

[Tag 0GEL](https://stacks.math.columbia.edu/tag/0GEL) in the Stacks Project.

**`Stacks.DerivedQCoh.eventually_subsingleton_hom_iff_truncGE_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundednessOfAPerfectComplex.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundednessOfAPerfectComplex.lean#L222).

> **[Stacks, Tag 0GEL].** Let `X` be a quasi-compact and quasi-separated scheme, let `P` be a
> perfect object of `D(𝒪_X)`, let `E` be an object of `D_QCoh(𝒪_X)` and let `a` be an integer. Then
>
> 1. `Hom_{D(𝒪_X)}(P⟦-i⟧, E) = 0` for `i ≫ 0`
>
> if and only if
>
> 2. `Hom_{D(𝒪_X)}(P⟦-i⟧, τ_{≥a}E) = 0` for `i ≫ 0`,
>
> where `τ_{≥a}` is the canonical truncation of `D(𝒪_X)` and vanishing of a Hom-group is
> subsingletonness of the morphism type, the derived category being additive.
>
> Both implications are the truncation triangle
> `τ_{≤a-1}E ⟶ E ⟶ τ_{≥a}E ⟶ (τ_{≤a-1}E)⟦1⟧`: a morphism `P⟦-i⟧ ⟶ E` which dies in `τ_{≥a}E`
> factors through `τ_{≤a-1}E`, and a morphism `P⟦-i⟧ ⟶ τ_{≥a}E` which dies in `(τ_{≤a-1}E)⟦1⟧`
> factors through `E`. So each direction needs only that `τ_{≤a-1}E` and `(τ_{≤a-1}E)⟦1⟧` receive
> no nonzero morphism from `P⟦-i⟧` for `i` large; both of them lie in `D_QCoh(𝒪_X)` and are bounded
> above, by `a - 1` and `a - 2`, and
> `Stacks.DerivedQCoh.exists_threshold_subsingleton_hom_negShift_of_isPerfect` kills both from
> `i ≥ a - 1 + c` on, with `c` the threshold that perfectness of `P` supplies through
> [Stacks, Tag 09M4].

```lean
theorem eventually_subsingleton_hom_iff_truncGE_of_isPerfect
    (P E : DerivedCategory X.Modules)
    (hP : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) P)
    (hE : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (a : ℤ) :
    (∃ N : ℤ, ∀ i : ℤ, N ≤ i → Subsingleton (P⟦-i⟧ ⟶ E)) ↔
      ∃ N : ℤ, ∀ i : ℤ, N ≤ i →
        Subsingleton (P⟦-i⟧ ⟶ (DerivedCategory.TStructure.t.truncGE a).obj E)
```

## Tag 0GEM, a lemma

[Tag 0GEM](https://stacks.math.columbia.edu/tag/0GEM) in the Stacks Project.

**`Stacks.Perfect.eventually_subsingleton_hom_iff_truncLE_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundedness.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DetectingBoundedness.lean#L258).

> **[Stacks, Tag 0GEM].** Let `X` be a scheme, let `P` and `E` be objects of `D(𝒪_X)` with `P`
> bounded above by `nP`, and let `a` be an integer. Then `Hom(P⟦-i⟧, E) = 0` for `i ≪ 0` if and only
> if `Hom(P⟦-i⟧, τ_{≤a}E) = 0` for `i ≪ 0`.
>
> The source states this for `P` perfect on a quasi-compact quasi-separated scheme and `E` in
> `D_QCoh(𝒪_X)`; the argument consumes only boundedness above of `P`, which those hypotheses imply,
> so the statement here is strictly more general and a consumer holding the source's hypotheses may
> restrict. The vanishing that makes the truncation triangle harmless is pure t-structure
> orthogonality: `P⟦-i⟧` is `≤ nP + i`, while `τ_{>a}E` is `≥ a + 1`, and `nP + i < a + 1` for
> `i ≪ 0`.

```lean
theorem eventually_subsingleton_hom_iff_truncLE_of_isLE
    (P E : DerivedCategory X.Modules) (nP : ℤ) (hP : P.IsLE nP) (a : ℤ) :
    (∃ N : ℤ, ∀ i : ℤ, i ≤ N → Subsingleton (P⟦-i⟧ ⟶ E)) ↔
      ∃ N : ℤ, ∀ i : ℤ, i ≤ N →
        Subsingleton (P⟦-i⟧ ⟶ (DerivedCategory.TStructure.t.truncLE a).obj E)
```

## Tag 0GEN, a proposition

[Tag 0GEN](https://stacks.math.columbia.edu/tag/0GEN) in the Stacks Project.

**`Stacks.SheafOfModules.tfae_minus_of_isPerfect_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundednessGenerator.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundednessGenerator.lean#L331).

> Let `X` be a quasi-compact and quasi-separated scheme, let `G` be a perfect
> object of `D(𝒪_X)` which generates `D_QCoh(𝒪_X)`, and let `E ∈ D_QCoh(𝒪_X)`. The following are
> equivalent:
>
> 1. `E ∈ D^-_QCoh(𝒪_X)`;
> 2. `Hom_{D(𝒪_X)}(G[-i], E) = 0` for `i ≫ 0`;
> 3. `Ext^i_X(G, E) = 0` for `i ≫ 0`;
> 4. `RHom_X(G, E)` is in `D^-(ℤ)`;
> 5. `H^i(X, G^∨ ⊗^L E) = 0` for `i ≫ 0`;
> 6. `RΓ(X, G^∨ ⊗^L E)` is in `D^-(ℤ)`;
> 7. for every perfect object `P` of `D(𝒪_X)`: (a) the assertions (2), (3), (4) hold with `G`
>    replaced by `P`, (b) `H^i(X, P ⊗^L E) = 0` for `i ≫ 0`, and (c) `RΓ(X, P ⊗^L E)` is in
>    `D^-(ℤ)`.
>
> Generation of `D_QCoh(𝒪_X)` by `G` is the hypothesis that an object of `D(𝒪_X)` with
> quasi-coherent cohomology receiving only zero morphisms from the shifts of `G` is zero, and
> `E ∈ D_QCoh(𝒪_X)` is quasi-coherence of the cohomology sheaves of `E`. `RHom_X(G, E)` is the
> global derived hom, read in `D(ℤ)`; `D^-(ℤ)` is the property `minus` of the canonical
> t-structure on `D(AddCommGrpCat)`.

```lean
theorem tfae_minus_of_isPerfect_generator
    (hqc : CompactSpace X) (hqs : QuasiSeparatedSpace X)
    (G E : DerivedCategory (StructureSheafModules X.sheaf))
    (hG : (ringedSite X.sheaf).IsPerfect G)
    (hgen : ∀ K : DerivedCategory (StructureSheafModules X.sheaf),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor
          (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent) →
        (∀ (n : ℤ) (f : G⟦n⟧ ⟶ K), f = 0) → IsZero K)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj E).IsQuasicoherent) :
    List.TFAE
      [(DerivedCategory.TStructure.t (C := StructureSheafModules X.sheaf)).minus E,
        ∃ N : ℤ, ∀ i, N ≤ i → Subsingleton (G⟦-i⟧ ⟶ E),
        ∃ N : ℤ, ∀ i, N ≤ i → Subsingleton (DerivedCategory.Ext G E i),
        (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).minus
          ((RingedSite.underlyingDerivedGroup (ringedSite X.sheaf)).obj
            (((globalDerivedHom X.sheaf).obj (op G)).obj E)),
        ∃ N : ℤ, ∀ i, N ≤ i → IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
          ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
            (((derivedTensor X.sheaf).obj (derivedDual X.sheaf G)).obj E))),
        (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).minus
          ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
            (((derivedTensor X.sheaf).obj (derivedDual X.sheaf G)).obj E)),
        ∀ P : DerivedCategory (StructureSheafModules X.sheaf), (ringedSite X.sheaf).IsPerfect P →
          ((∃ N : ℤ, ∀ i, N ≤ i → Subsingleton (P⟦-i⟧ ⟶ E)) ∧
            (∃ N : ℤ, ∀ i, N ≤ i → Subsingleton (DerivedCategory.Ext P E i)) ∧
            (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).minus
              ((RingedSite.underlyingDerivedGroup (ringedSite X.sheaf)).obj
                (((globalDerivedHom X.sheaf).obj (op P)).obj E))) ∧
          (∃ N : ℤ, ∀ i, N ≤ i → IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
            ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
              (((derivedTensor X.sheaf).obj P).obj E)))) ∧
          (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).minus
            ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
              (((derivedTensor X.sheaf).obj P).obj E))]
```

## Tag 0GEP, an equation

[Tag 0GEP](https://stacks.math.columbia.edu/tag/0GEP) in the Stacks Project.

**`Stacks.Cohomology.ExtensionByZeroClosedSupport.isPerfect_jShriek_of_closedSupport_and_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/ExtensionByZeroClosedSupport.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/PerfectComplexes/ExtensionByZeroClosedSupport.lean#L121).

> **Stacks 0GEP.** Let `j : U → X` be an open subspace of a ringed space and let `T ⊆ U` be
> closed in `X`. For a perfect object `E` of the derived category of `𝒪_U`-modules whose cohomology
> sheaves are supported on `T`, the object `K' = j_! E` satisfies
>
> * `j_! E = Rj_* E`: the canonical map `j_! E ⟶ Rj_* E` is an isomorphism ([Stacks, Tag 08DF]);
> * `K'` is a perfect object of `D(𝒪_X)` ([Stacks, Tag 08DP]);
> * `K'` is supported on the closed set `T`;
> * `K'` restricts to `E` on `U`.
>
> These are the assertions made of the complex `K' = R(V → X)_* K = R(V → X)_! K` in the proof of
> [Stacks, Tag 0GEN], where `K` is the Koszul complex on functions cutting out `T = X \ U'`
> inside the affine open `V`.

```lean
theorem isPerfect_jShriek_of_closedSupport_and_restrict
    (X : RingedSpace.{u, u}) (U : Opens X) (T : Set X) (hT : IsClosed T) (hTU : T ⊆ (U : Set X))
    (Rj : DerivedCategory (SheafOfModules.{u} (resRing U (structureSheafRing X))) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (αj : (jPush U (structureSheafRing X)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rj)
    (hRj : Rj.IsRightDerivedFunctor αj
      (HomotopyCategory.quasiIso (SheafOfModules.{u} (resRing U (structureSheafRing X)))
        (ComplexShape.up ℤ)))
    (E : DerivedCategory (SheafOfModules.{u} (resRing U (structureSheafRing X))))
    (hE : RingedSpace.IsPerfect (X := X.restrict U.isOpenEmbedding) E)
    (hET : AlgebraicGeometry.CohomologySupportedOn (resRing U (structureSheafRing X))
      ((fun x : Usp U ↦ x.1) ⁻¹' T) E) :
    IsIso ((extensionByZeroToDerivedPushforward (structureSheafRing X) U Rj αj).app E) ∧
      RingedSpace.IsPerfect (X := X)
        ((jShriek U (structureSheafRing X)).mapDerivedCategory.obj E) ∧
      AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X) T
        ((jShriek U (structureSheafRing X)).mapDerivedCategory.obj E) ∧
      Nonempty ((jStar U (structureSheafRing X)).mapDerivedCategory.obj
        ((jShriek U (structureSheafRing X)).mapDerivedCategory.obj E) ≅ E)
```

## Tag 0GEQ, a proposition

[Tag 0GEQ](https://stacks.math.columbia.edu/tag/0GEQ) in the Stacks Project.

**`Stacks.SheafOfModules.eventually_subsingleton_shiftedHom_iff_ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundedBelowGenerator.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundedBelowGenerator.lean#L94). The attribute's comment: “conditions (2) and (3): eventual vanishing of Hom(G[-i], E) and of Ext^i(G, E)”.

> **Stacks 0GEQ, conditions (2) and (3).** For a perfect generator `G` of `D_QCoh(𝒪_X)` on a
> quasi-compact, quasi-separated scheme and an object `E` of `D_QCoh(𝒪_X)`, the groups
> `Hom_{D(𝒪_X)}(G⟦-i⟧, E)` vanish for `i ≪ 0` exactly when the groups `Ext^i_X(G, E)` do.
>
> The two conditions hold of the same `i`, because `⟦-i⟧` is left adjoint to `⟦i⟧`.

```lean
theorem eventually_subsingleton_shiftedHom_iff_ext
    (_hqc : CompactSpace X) (_hqs : QuasiSeparatedSpace X)
    (G E : DerivedCategory (StructureSheafModules X.sheaf))
    (_hG : (ringedSite X.sheaf).IsPerfect G)
    (_hgen : ∀ K : DerivedCategory (StructureSheafModules X.sheaf),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor
          (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent) →
        (∀ (n : ℤ) (f : G⟦n⟧ ⟶ K), f = 0) → IsZero K)
    (_hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj E).IsQuasicoherent) :
    (∃ N : ℤ, ∀ i ≤ N, Subsingleton (G⟦-i⟧ ⟶ E)) ↔
      ∃ N : ℤ, ∀ i ≤ N, Subsingleton (DerivedCategory.Ext G E i)
```

**`Stacks.SheafOfModules.plus_derivedGlobalSections_derivedTensor_derivedDual_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundedBelowGenerator.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundedBelowGenerator.lean#L127). The attribute's comment: “conditions (5) and (6): eventual vanishing of H^i(X, G^vee ⊗ E) and membership of RGamma(X, G^vee ⊗ E) in D^+(Z)”.

> **Stacks 0GEQ, conditions (5) and (6).** For a perfect generator `G` of `D_QCoh(𝒪_X)` on a
> quasi-compact, quasi-separated scheme and an object `E` of `D_QCoh(𝒪_X)`, the cohomology groups
> `H^i(X, G^∨ ⊗^L_{𝒪_X} E)` vanish for `i ≪ 0` exactly when `RΓ(X, G^∨ ⊗^L_{𝒪_X} E)` lies in
> `D⁺(ℤ)`.
>
> This is the description of the bounded-below derived category by its cohomology, applied to the
> single object `RΓ(X, G^∨ ⊗^L_{𝒪_X} E)` of `D(AddCommGrpCat)`.

```lean
theorem plus_derivedGlobalSections_derivedTensor_derivedDual_iff
    (_hqc : CompactSpace X) (_hqs : QuasiSeparatedSpace X)
    (G E : DerivedCategory (StructureSheafModules X.sheaf))
    (_hG : (ringedSite X.sheaf).IsPerfect G)
    (_hgen : ∀ K : DerivedCategory (StructureSheafModules X.sheaf),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor
          (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent) →
        (∀ (n : ℤ) (f : G⟦n⟧ ⟶ K), f = 0) → IsZero K)
    (_hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj E).IsQuasicoherent) :
    (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).plus
        ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
          (((derivedTensor X.sheaf).obj E).obj (derivedDual X.sheaf G))) ↔
      ∃ N : ℤ, ∀ n ≤ N, IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} n).obj
        ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
          (((derivedTensor X.sheaf).obj E).obj (derivedDual X.sheaf G))))
```

**`Stacks.SheafOfModules.tfae_plus_of_isPerfect_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundednessGenerator.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/DetectingBoundednessGenerator.lean#L409). The attribute's comment: “the full statement: the equivalence of conditions (1) to (7), with (7) split into (a), (b) and (c), for every perfect P”.

> Let `X` be a quasi-compact and quasi-separated scheme, let `G` be a perfect
> object of `D(𝒪_X)` which generates `D_QCoh(𝒪_X)`, and let `E ∈ D_QCoh(𝒪_X)`. The following are
> equivalent:
>
> 1. `E ∈ D^+_QCoh(𝒪_X)`;
> 2. `Hom_{D(𝒪_X)}(G[-i], E) = 0` for `i ≪ 0`;
> 3. `Ext^i_X(G, E) = 0` for `i ≪ 0`;
> 4. `RHom_X(G, E)` is in `D^+(ℤ)`;
> 5. `H^i(X, G^∨ ⊗^L E) = 0` for `i ≪ 0`;
> 6. `RΓ(X, G^∨ ⊗^L E)` is in `D^+(ℤ)`;
> 7. for every perfect object `P` of `D(𝒪_X)`: (a) the assertions (2), (3), (4) hold with `G`
>    replaced by `P`, (b) `H^i(X, P ⊗^L E) = 0` for `i ≪ 0`, and (c) `RΓ(X, P ⊗^L E)` is in
>    `D^+(ℤ)`.
>
> Generation of `D_QCoh(𝒪_X)` by `G` is the hypothesis that an object of `D(𝒪_X)` with
> quasi-coherent cohomology receiving only zero morphisms from the shifts of `G` is zero, and
> `E ∈ D_QCoh(𝒪_X)` is quasi-coherence of the cohomology sheaves of `E`. `RHom_X(G, E)` is the
> global derived hom, read in `D(ℤ)`; `D^+(ℤ)` is the property `plus` of the canonical
> t-structure on `D(AddCommGrpCat)`.
>
> This is the full statement of Stacks 0GEQ: all seven of its conditions, under exactly its
> hypotheses.

```lean
theorem tfae_plus_of_isPerfect_generator
    (hqc : CompactSpace X) (hqs : QuasiSeparatedSpace X)
    (G E : DerivedCategory (StructureSheafModules X.sheaf))
    (hG : (ringedSite X.sheaf).IsPerfect G)
    (hgen : ∀ K : DerivedCategory (StructureSheafModules X.sheaf),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor
          (StructureSheafModules X.sheaf) i).obj K).IsQuasicoherent) →
        (∀ (n : ℤ) (f : G⟦n⟧ ⟶ K), f = 0) → IsZero K)
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (StructureSheafModules X.sheaf) i).obj E).IsQuasicoherent) :
    List.TFAE
      [(DerivedCategory.TStructure.t (C := StructureSheafModules X.sheaf)).plus E,
        ∃ N : ℤ, ∀ i ≤ N, Subsingleton (G⟦-i⟧ ⟶ E),
        ∃ N : ℤ, ∀ i ≤ N, Subsingleton (DerivedCategory.Ext G E i),
        (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).plus
          ((RingedSite.underlyingDerivedGroup (ringedSite X.sheaf)).obj
            (((globalDerivedHom X.sheaf).obj (op G)).obj E)),
        ∃ N : ℤ, ∀ i ≤ N, IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
          ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
            (((derivedTensor X.sheaf).obj (derivedDual X.sheaf G)).obj E))),
        (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).plus
          ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
            (((derivedTensor X.sheaf).obj (derivedDual X.sheaf G)).obj E)),
        ∀ P : DerivedCategory (StructureSheafModules X.sheaf), (ringedSite X.sheaf).IsPerfect P →
          ((∃ N : ℤ, ∀ i ≤ N, Subsingleton (P⟦-i⟧ ⟶ E)) ∧
            (∃ N : ℤ, ∀ i ≤ N, Subsingleton (DerivedCategory.Ext P E i)) ∧
            (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).plus
              ((RingedSite.underlyingDerivedGroup (ringedSite X.sheaf)).obj
                (((globalDerivedHom X.sheaf).obj (op P)).obj E))) ∧
          (∃ N : ℤ, ∀ i ≤ N, IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
            ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
              (((derivedTensor X.sheaf).obj P).obj E)))) ∧
          (DerivedCategory.TStructure.t (C := AddCommGrpCat.{u})).plus
            ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
              (((derivedTensor X.sheaf).obj P).obj E))]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.40, Tag 0GEI](https://stacks.math.columbia.edu/tag/0GEI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
