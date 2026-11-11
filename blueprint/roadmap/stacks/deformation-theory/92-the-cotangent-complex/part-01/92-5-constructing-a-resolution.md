---
declaration: section
origin: cited
lean: CommAlgCat.finiteType_succ_of_trivialKanFibration_of_isCoskeletal, CommAlgCat.exists_trivialKanFibration_from_finiteType_polynomial_simplicialAlgebra, CommAlgCat.smallResolutionLeftDerivedMooreHomologyIso, CommAlgCat.finite_homology_smallResolutionMooreComplex, CommAlgCat.finite_moduleLeftDerivedPointLowerShriek, CommAlgCat.finite_homology_cotangentComplex, CommAlgCat.IsResolution, CommAlgCat.isResolution_quasiIso_homotopyEquivalence_tfae
statement: formalized
proof: formalized
---

# 92.5 Constructing a resolution

Section 92.5 of the Stacks Project, [Tag 08PV](https://stacks.math.columbia.edu/tag/08PV). 9 tags here are carried by 38 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08PW, a lemma

[Tag 08PW](https://stacks.math.columbia.edu/tag/08PW) in the Stacks Project.

**`CommAlgCat.finiteType_succ_of_trivialKanFibration_of_isCoskeletal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/FiniteTypeCoskeletal.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/FiniteTypeCoskeletal.lean#L154).

> **Stacks 08PW**. For a finite type algebra `B` over a Noetherian ring `A`, an
> `n`-coskeletal simplicial `A`-algebra over `B` whose canonical augmentation is a trivial Kan
> fibration and whose terms through degree `n` are of finite type has a finite type term in degree
> `n + 1`.

```lean
theorem finiteType_succ_of_trivialKanFibration_of_isCoskeletal
    [IsNoetherianRing A] [Algebra.FiniteType A B]
    (P : SimplicialObject (Over (CommAlgCat.of A B))) (n : ℕ)
    (_hkan : SSet.trivialKanFibrations (underlyingAugmentation A B P))
    (hcosk : IsIso ((SimplicialObject.coskAdj n).unit.app P))
    (hfinite : ∀ k ≤ n,
      Algebra.FiniteType A (P.obj (op (SimplexCategory.mk k))).left) :
    Algebra.FiniteType A (P.obj (op (SimplexCategory.mk (n + 1)))).left
```

## Tag 08PX, a proposition

[Tag 08PX](https://stacks.math.columbia.edu/tag/08PX) in the Stacks Project.

**`CommAlgCat.exists_trivialKanFibration_from_finiteType_polynomial_simplicialAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialResolution.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialResolution.lean#L517).

> **Stacks 08PX.** A finite type algebra over a Noetherian ring has a simplicial resolution by
> polynomial algebras of finite type whose augmentation is a trivial Kan fibration on underlying
> simplicial sets.

```lean
theorem exists_trivialKanFibration_from_finiteType_polynomial_simplicialAlgebra
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [Algebra.FiniteType A B] :
    ∃ (P : SimplicialObject (CommAlgCat.{u} A))
      (ε : P ⟶ (Functor.const _).obj (CommAlgCat.of A B)),
      (∀ n : ℕ, ∃ k : ℕ,
        Nonempty ((P.obj (op ⦋n⦌) : Type u) ≃ₐ[A] MvPolynomial (Fin k) A)) ∧
      SSet.trivialKanFibrations
        (Functor.whiskerRight ε (CategoryTheory.forget (CommAlgCat.{u} A)))
```

## Tag 08PY, a lemma

[Tag 08PY](https://stacks.math.columbia.edu/tag/08PY) in the Stacks Project.

**`CommAlgCat.smallResolutionLeftDerivedMooreHomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/FiniteHomology.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/FiniteHomology.lean#L289). The attribute's comment: “the half of the statement that says which modules the conclusion is about: the cohomology of Lπ\_!(ℱ) for the point morphism of the small model of the footnote-restricted site, read degreewise at abelian coefficients, is the homology of the B-module Moore complex of ℱ(P\_•, ε). The finiteness of those modules is `CommAlgCat.finite_homology_smallResolutionMooreComplex`”.

> **`Lπ_!(ℱ) = ℱ(P_•, ε)` for a presheaf of `B`-modules, with the module structure forgotten.**
> The sections at the point of `L_nπ_!(ℱ)` are the degree `n` homology of the `B`-module Moore
> complex of `ℱ(P_•, ε)`, read as an abelian group.
>
> This is `CommAlgCat.smallResolutionLeftDerivedLowerShriekNatIso` — the conclusion of Tag 08PT at
> the small model of the restricted site — followed by the two identifications that move the
> computation from abelian groups to `B`-modules: the Moore complex of the underlying abelian
> presheaf is the image of the `B`-module Moore complex, and `forget₂` preserves homology.

```lean
def smallResolutionLeftDerivedMooreHomologyIso (n : ℕ) :
    (Stacks.ChaoticSite.pointSections.{u, u + 1, u} AddCommGrpCat.{u}).obj
        (((Stacks.ChaoticSite.abelianPointLowerShriek
              (smallBoundedPolynomialSite A B κ)).leftDerived n).obj
          (smallPolynomialModuleSheaf A B κ ℱ)) ≅
      (forget₂ (ModuleCat.{u} B) AddCommGrpCat.{u}).obj
        ((smallResolutionMooreComplex ε κ hPκ ℱ).homology n)
```

**`CommAlgCat.finite_homology_smallResolutionMooreComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/FiniteHomology.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/FiniteHomology.lean#L357). The attribute's comment: “the conclusion for a resolution satisfying the cardinality bound of the small model of the footnote-restricted site, and with the cohomology of Lπ\_! read as the homology of the B-module Moore complex of ℱ(P\_•, ε), which is what identifies it here (`CommAlgCat.smallResolutionLeftDerivedMooreHomologyIso`): the module-level Lπ\_! is absent from this library. The finiteness hypothesis is carried for the terms of the resolution, not for every object of the site”.

> **Tag 08PY for a bounded resolution.** Let `B` be Noetherian, let `ε : P_• ⟶ B` be a
> resolution of `B` over `A` whose terms are polynomial algebras on at most `κ` variables, and let
> `ℱ` be a presheaf of `B`-modules on the small model of the restricted site whose sections on the
> terms of the resolution are finite `B`-modules. Then the Moore homology of `ℱ(P_•, ε)` — which by
> `CommAlgCat.smallResolutionLeftDerivedMooreHomologyIso` is the sections at the point of
> `L_nπ_!(ℱ)` — is a finite `B`-module.

```lean
theorem finite_homology_smallResolutionMooreComplex [IsNoetherianRing (B : Type u)]
    (hfin : ∀ p : SimplexCategory,
      Module.Finite B (ℱ.obj (op ((smallResolutionCosimplicialObject ε κ hPκ).obj p))))
    (n : ℕ) : Module.Finite B ((smallResolutionMooreComplex ε κ hPκ ℱ).homology n)
```

**`CommAlgCat.finite_moduleLeftDerivedPointLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialResolutionFiniteCohomology.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialResolutionFiniteCohomology.lean#L133). The attribute's comment: “read at the small model of the footnote-restricted site, for the reason recorded for Tag 08PS in `StacksFrontier/Cotangent/ResolutionPointCriterionSmallOfModules.lean`; the cardinal bound `κ` of the footnote is a parameter, required only to be infinite so that the finite type resolution of Tag 08PX is an object of the site”.

> **Stacks 08PY.** Let `A` be a Noetherian ring, let `A → B` be a finite type ring map and let
> `π`, `B̲` be as in Tag 08PR. If `ℱ` is a `B̲`-module such that `ℱ(P, α)` is a finite `B`-module
> for every augmentation `α : P → B` whose `P` is of finite type over `A`, then every cohomology
> module of `Lπ_!(ℱ)` is a finite `B`-module.
>
> By Tag 08PX there is a resolution `ε : P_• ⟶ B` of `B` over `A` all of whose terms are
> *finite type* polynomial algebras, and by the module half of Tag 08PS the sections at the point
> of `L_nπ_!(ℱ)` are the degree `n` homology of the Moore complex of `ℱ(P_•, ε)`. Each term of that
> complex is `ℱ` evaluated at a finite type polynomial augmentation, hence a finite `B`-module, and
> `B` is Noetherian because it is of finite type over the Noetherian ring `A`; so each homology
> module is a subquotient of a finite module over a Noetherian ring.

```lean
theorem finite_moduleLeftDerivedPointLowerShriek (κ : Cardinal.{u})
    (hκ : Cardinal.aleph0.{u} ≤ κ)
    (ℱ : Sheaf (GrothendieckTopology.trivial (smallBoundedPolynomialSite A B κ))
      (ModuleCat.{u} (B : Type u)))
    (hℱ : ∀ W : smallBoundedPolynomialSite A B κ,
      Algebra.FiniteType A (smallBoundedPolynomialAlgebra A B κ W : Type u) →
        Module.Finite (B : Type u) (ℱ.obj.obj (op W)))
    (n : ℕ) :
    Module.Finite (B : Type u)
      (((modulePointLowerShriek (smallBoundedPolynomialSite A B κ)
            (B : Type u)).leftDerived n ⋙
          Stacks.ChaoticSite.pointSections.{u, u + 1, u}
            (ModuleCat.{u} (B : Type u))).obj ℱ)
```

## Tag 08PZ, a lemma

[Tag 08PZ](https://stacks.math.columbia.edu/tag/08PZ) in the Stacks Project.

**`CommAlgCat.finite_homology_cotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/FiniteHomology.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/FiniteHomology.lean#L516).

> **Tag 08PZ.** Let `A` be a Noetherian ring and let `A → B` be a finite type ring map. Then
> `H^n(L_{B/A})` is a finite `B`-module for every `n : ℤ`.
>
> In positive degrees the cotangent complex vanishes, so there is nothing to prove; the content is
> `CommAlgCat.finite_homology_cotangentComplex_of_resolution` fed with the finite type resolution
> of Tag 08PX.

```lean
theorem finite_homology_cotangentComplex (A : Type u) [CommRing A] [IsNoetherianRing A]
    (B : Type u) [CommRing B] [Algebra A B] [Algebra.FiniteType A B] (m : ℤ) :
    Module.Finite B ((cotangentComplex.{u, u} A (CommAlgCat.of A B)).homology m)
```

## Tag 08QI, a remark

[Tag 08QI](https://stacks.math.columbia.edu/tag/08QI) in the Stacks Project.

**`CommAlgCat.IsResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Resolution.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Resolution.lean#L71). The attribute's comment: “resolution”.

> **Stacks Project, Tag 08QI.**
>
> An augmentation `ε : P• ⟶ B` of a simplicial commutative `A`-algebra is a resolution of `B` over
> `A` if every `Pₙ` is a polynomial algebra over `A` and the underlying augmentation of simplicial
> sets is a trivial Kan fibration.

```lean
structure IsResolution (A : Type u) [CommRing A] (B : Type v) [CommRing B] [Algebra A B]
    (P : SimplicialObject (CommAlgCat.{v} A))
    (ε : P ⟶ (SimplicialObject.const _).obj (CommAlgCat.of A B)) : Prop
```

**`CommAlgCat.isResolution_quasiIso_homotopyEquivalence_tfae`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Resolution.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Resolution.lean#L87). The attribute's comment: “resolution\_criteria”.

> **Stacks Project, Tag 08QI.**
>
> For an augmentation `ε : P• ⟶ B` which is degreewise surjective and whose terms are polynomial
> `A`-algebras, the following are equivalent: `ε` is a resolution, the induced map of associated
> complexes is a quasi-isomorphism, and the underlying map of simplicial sets is a homotopy
> equivalence.

```lean
lemma isResolution_quasiIso_homotopyEquivalence_tfae
    (A : Type u) [CommRing A] (B : Type v) [CommRing B] [Algebra A B]
    (P : SimplicialObject (CommAlgCat.{v} A))
    (ε : P ⟶ (SimplicialObject.const _).obj (CommAlgCat.of A B))
    (hP : ∀ n : SimplexCategoryᵒᵖ, IsPolynomialAlgebra A (P.obj n))
    (hε : ∀ n : SimplexCategoryᵒᵖ, Function.Surjective (ε.app n).hom) :
    List.TFAE
      [IsResolution A B P ε,
       QuasiIso ((alternatingFaceMapComplex AddCommGrpCat.{v}).map
         (Functor.whiskerRight ε
           (forget₂ (CommAlgCat.{v} A) (AlgCat.{v} A) ⋙
            forget₂ (AlgCat.{v} A) (ModuleCat.{v} A) ⋙
            forget₂ (ModuleCat.{v} A) AddCommGrpCat.{v}))),
       SimplicialObject.homotopyEquivalences (Type v)
         (Functor.whiskerRight ε (forget (CommAlgCat.{v} A)))]
```

**`CommAlgCat.exists_isResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionCotangentAny.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ResolutionCotangentAny.lean#L85). The attribute's comment: “existence of resolutions: every A-algebra B admits a resolution, namely the standard resolution”.

> **[Stacks, Remark 08QI]: resolutions exist.** Every commutative `A`-algebra `B` admits a
> resolution over `A`: the standard resolution of `B` over `A` is one, by
> `CommAlgCat.standardResolution_isResolution`.

```lean
theorem exists_isResolution (A : Type u) [CommRing A] (B : Type (max u v)) [CommRing B]
    [Algebra A B] :
    ∃ (P : SimplicialObject (CommAlgCat.{max u v} A))
      (ε : P ⟶ (SimplicialObject.const (CommAlgCat.{max u v} A)).obj (CommAlgCat.of A B)),
      IsResolution A B P ε
```

**`CommAlgCat.cotangentComplexIsoOfResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionCotangentAny.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ResolutionCotangentAny.lean#L156). The attribute's comment: “in D(B): for an arbitrary resolution of B over A, with no bound on the number of variables, Q(L\_\{B/A}) = Q(Omega[P\_bullet/A] ⊗\_\{P\_bullet} B); the cardinal bound of the two instances of Tag 08PU this composes is supplied by the resolution itself”.

> **[Stacks, Remark 08QI]: any resolution computes the cotangent complex.** Let `ε : P_• ⟶ B` be
> a resolution of `B` over `A` — every `P_n` a polynomial algebra over `A`, `ε` a trivial Kan
> fibration of the underlying simplicial sets — with no bound on the number of variables. Then the
> cotangent complex `L_{B/A}` of [Stacks, Tag 08PN], which is built from the *standard* resolution,
> is the complex of base-changed differentials of `P_•`, as objects of `D(B)`:
>
> `Q(L_{B/A}) ≅ Q(Ω[P_•⁄A] ⊗_{P_•, ε} B)`.
>
> The proof is the source's. At the cardinal `CommAlgCat.resolutionVarCardinal`, which bounds the
> terms of `P_•` and those of the standard resolution at once, both resolutions lie on the small
> model of the footnote-restricted site, so the two instances of [Stacks, Tag 08PU] in `D(B)` —
> `CommAlgCat.standardResolutionCotangentDerivedLowerShriekIsoOfLE` and
> `CommAlgCat.smallResolutionCotangentDerivedLowerShriekIso` — identify both complexes with
> `Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)`, which mentions no resolution.

```lean
def cotangentComplexIsoOfResolution :
    DerivedCategory.Q.obj (cotangentComplex.{u, u} A B) ≅
      DerivedCategory.Q.obj (resolutionCotangentComplex.{u, u} A B P ε)
```

**`CommAlgCat.resolutionModuleLeftDerivedLowerShriekNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionCotangentAny.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ResolutionCotangentAny.lean#L182). The attribute's comment: “the cosimplicial object of a resolution and the conclusion Lpi\_!(F) = F(P\_bullet, ε) in D(B) functorially in F, for an arbitrary resolution with no bound on the number of variables, read at the small model of the footnote-restricted site for the reason recorded in `StacksFrontier/Cotangent/ResolutionPointCriterionSmall.lean`”.

> **`Lπ_!(ℱ) = ℱ(P_•, ε)` in `D(B)` for an arbitrary resolution.** Let `ε : P_• ⟶ B` be a
> resolution of `B` over `A`, with no bound on the number of variables. For every sheaf of
> `B`-modules `ℱ` on the small model of the site `C_{B/A}` restricted to polynomial algebras on at
> most `CommAlgCat.resolutionVarCardinal A B hε.isPolynomialAlgebra` variables — a bound the
> resolution supplies — the sections at the point of `L_nπ_!(ℱ)` are the degree `n` homology of the
> Moore complex of the simplicial `B`-module `ℱ(P_•, ε)`, naturally in `ℱ`.
>
> This is `CommAlgCat.smallResolutionModuleLeftDerivedLowerShriekNatIso` at that cardinal. A bound
> cannot be dispensed with altogether here, as it can in
> `CommAlgCat.cotangentComplexIsoOfResolution`: the site, and with it `π_!`, is the one restricted
> by the bound.

```lean
def resolutionModuleLeftDerivedLowerShriekNatIso (n : ℕ) :
    (modulePointLowerShriek
          (smallBoundedPolynomialSite A B (resolutionVarCardinal A B hε.isPolynomialAlgebra))
          (B : Type u)).leftDerived n ⋙
        Stacks.ChaoticSite.pointSections.{u, u + 1, u} (ModuleCat.{u} (B : Type u)) ≅
      sheafToPresheaf (GrothendieckTopology.trivial
            (smallBoundedPolynomialSite A B (resolutionVarCardinal A B hε.isPolynomialAlgebra)))
          (ModuleCat.{u} (B : Type u)) ⋙
        moduleCosimplicialMooreComplex (smallResolutionCosimplicialObject ε
            (resolutionVarCardinal A B hε.isPolynomialAlgebra)
            (isPolynomialAlgebraBelow_resolutionVarCardinal A B hε.isPolynomialAlgebra)) ⋙
          HomologicalComplex.homologyFunctor (ModuleCat.{u} (B : Type u))
            (ComplexShape.down ℕ) n
```

**`CommAlgCat.quasiIso_alternatingFaceMapComplex_map_of_isResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionIndependence.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ResolutionIndependence.lean#L199). The attribute's comment: “the remark's payoff, at the arrow level: for any two resolutions of B over A and any morphism between them, the induced map of the complexes Omega[-/A] ⊗ B is a quasi-isomorphism, so any resolution computes L\_\{B/A} and the comparison is the induced map”.

> **Remark 08QI at the arrow level.** Let `ε : P_• ⟶ B` and `ε' : P'_• ⟶ B` be resolutions of
> `B` over `A` in the sense of [Stacks, Tag 08QI]. Every morphism `ψ` of the attached simplicial
> objects of `Over B` — equivalently, every morphism `P_• ⟶ P'_•` of simplicial `A`-algebras
> compatible with the augmentations — induces a quasi-isomorphism
>
> `Ω[P_•⁄A] ⊗_{P_•} B ⟶ Ω[P'_•⁄A] ⊗_{P'_•} B`.
>
> So any resolution computes the cotangent complex, and the isomorphism is the one a morphism of
> resolutions induces; no cardinal bound appears, the terms of the two resolutions being bounded by
> a single cardinal.

```lean
theorem quasiIso_alternatingFaceMapComplex_map_of_isResolution
    (hres : IsResolution A (B : Type u) P ε) (hres' : IsResolution A (B : Type u) P' ε')
    (ψ : resolutionOver ε ⟶ resolutionOver ε') :
    QuasiIso ((alternatingFaceMapComplex (ModuleCat.{u} (B : Type u))).map
      (Functor.whiskerRight ψ (overDifferentialsFunctor (A := A) (B := B))))
```

**`CommAlgCat.resolutionCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ResolutionIndependence.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ResolutionIndependence.lean#L216). The attribute's comment: “the remark's payoff, at the object level: for any resolution of B over A the complex Omega[P\_./A] ⊗\_\{P\_.} B is L\_\{B/A} in D(B)”.

> **Remark 08QI at the object level.** The complex `Ω[P_•⁄A] ⊗_{P_•} B` of an arbitrary
> resolution of `B` over `A`, read in cohomological degrees `≤ 0`, is the cotangent complex
> `L_{B/A}` in `D(B)`. Both are identified with `Lπ_!(i^*Ω_{𝒪/A})` by [Stacks, Tag 08PU] in `D(B)`,
> read at a bound containing both the given resolution and the standard one.

```lean
def resolutionCotangentComplexIso (hres : IsResolution A (B : Type u) P ε) :
    DerivedCategory.Q.obj
        (((alternatingFaceMapComplex (ModuleCat.{u} (B : Type u))).obj
            (resolutionOver ε ⋙ overDifferentialsFunctor)).extend
          (ComplexShape.embeddingUpIntLE (0 : ℤ))) ≅
      DerivedCategory.Q.obj (cotangentComplex.{u, u} A B)
```

**`CommAlgCat.standardResolution_isResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/StandardResolutionIsResolution.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/StandardResolutionIsResolution.lean#L120). The attribute's comment: “standard\_qualifies”.

> **Stacks Project, Tag 08QI.** The standard augmented simplicial algebra of a commutative
> `A`-algebra `B` is a resolution of `B` over `A`.

```lean
public theorem standardResolution_isResolution (A : Type u) [CommRing A]
    (B : CommAlgCat.{max u v} A) :
    IsResolution A B (standardResolution A B).left (standardResolution A B).hom
```

## Tag 08QJ, a lemma

[Tag 08QJ](https://stacks.math.columbia.edu/tag/08QJ) in the Stacks Project.

**`CommAlgCat.isIso_derivedColimitTensorComparison_smallPolynomialAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteCoefficientChange.lean, line 1276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteCoefficientChange.lean#L1276). The attribute's comment: “for an `𝒪`-module in cohomological degree zero, on the small model of the site `C_{B/A}`; on a chaotic site `Li^*ℱ` and `ℱ ⊗^L_𝒪 B̲` are the same object”.

> **The change of coefficients of [Stacks, Tag 08QJ].** Let `A → B` be a ring map and let
> `𝒪`, `B̲` and `π` be as in [Stacks, Tag 08PR], read on the small model of `C_{B/A}` at the
> cardinal `CommAlgCat.standardResolutionVarCardinal A B` bounding the standard resolution. Then
> for every `𝒪`-module `ℱ`, placed in cohomological degree zero, the canonical comparison
>
> `Lπ_!(ℱ) ⟶ Lπ_!(ℱ ⊗^L_𝒪 B̲)`
>
> is an isomorphism in `D(Ab)`.
>
> The source states the right-hand side as `Lπ_!(Li^*ℱ)` for the morphism of topoi `i` attached to
> the ring map `B ⟶ B`; on a chaotic site that morphism is the identity on topoi, so `Li^*ℱ` and
> `ℱ ⊗^L_𝒪 B̲` are one and the same object of `D(Mod(B̲))` and the two readings of the statement
> coincide. The comparison itself is `Stacks.ChaoticSite.derivedColimitTensorComparison`: derived
> lower shriek applied to the unit of the derived change-of-coefficients adjunction, followed by
> the identification of `Lπ_!` on `B̲`-modules with `Lπ_!` on their underlying `𝒪`-modules, which
> is an isomorphism because restriction of scalars does not change the underlying abelian
> presheaf.
>
> Both hypotheses of [Stacks, Tag 08RX] are discharged, so nothing is assumed:
> `CommAlgCat.isPointResolution_standardResolutionSmallCosimplicialObject` is [Stacks, Tag 08PS]
> at this model, and
> `CommAlgCat.isIso_leftDerivedColimit_map_smallPolynomialAugmentationAbelian` is
> `Lπ_!(𝒪) = Lπ_!(B̲)` read degreewise. The dévissage from those two to an arbitrary `𝒪`-module
> is `Stacks.ChaoticSite.isIso_derivedColimitTensorComparison_app_single`.

```lean
public theorem isIso_derivedColimitTensorComparison_smallPolynomialAugmentation
    (F : PresheafOfModules.{u}
      (smallPolynomialStructurePresheaf A B (standardResolutionVarCardinal A B))) :
    IsIso ((Stacks.ChaoticSite.derivedColimitTensorComparison
        (smallPolynomialAugmentation A B (standardResolutionVarCardinal A B))).app
      (DerivedCategory.Q.obj
        ((HomologicalComplex.single (PresheafOfModules.{u}
          (smallPolynomialStructurePresheaf A B (standardResolutionVarCardinal A B)))
            (ComplexShape.up ℤ) 0).obj F)))
```

## Tag 08QK, a lemma

[Tag 08QK](https://stacks.math.columbia.edu/tag/08QK) in the Stacks Project.

**`CommAlgCat.polynomialSiteDerivedLowerShriekDifferentialsBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteDifferentialsBaseChangeLargeSite.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteDifferentialsBaseChangeLargeSite.lean#L316). The attribute's comment: “Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 B̲) = Lπ\_!(Ω\_\{𝒪/A}) in D(Ab), as the isomorphism induced by the base-change unit Ω\_\{𝒪/A} ⟶ Ω\_\{𝒪/A} ⊗\_𝒪 B̲, for the point morphism of the site C\_\{B/A} of Tag 08PR itself -- not of the footnote-restricted site nor of a small model of it -- with Ω\_\{𝒪/A} the sheaf of relative differentials of that site and Ω\_\{𝒪/A} ⊗\_𝒪 B̲ its base change along the augmentation 𝒪 ⟶ B̲ of Tag 08PR, under no hypothesis on A → B and no cardinal bound”.

> **`Lπ_!(Ω_{𝒪/A}) = Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)` in `D(Ab)` at the site `C_{B/A}` itself**, the last
> identification of [Stacks, Tag 08QK], as the isomorphism **induced by the base-change unit**
> `Ω_{𝒪/A} ⟶ Ω_{𝒪/A} ⊗_𝒪 B̲`.
>
> Here `Ω_{𝒪/A}` is the sheaf of relative differentials of [Stacks, Tag 08PR]'s site, read on its
> underlying abelian sheaf, `Ω_{𝒪/A} ⊗_𝒪 B̲` is its base change along the augmentation `𝒪 ⟶ B̲` of
> that tag, `π` is the point morphism of the site `C_{B/A}` -- not of a restriction of it -- and
> `Lπ_!` is the total left derived functor of the colimit over the index category, which is the
> `π_!` of [Stacks, Tag 08PF]. There is no hypothesis on `A → B` beyond its being a ring map, and no
> cardinal bound on the sets of variables.
>
> The two inputs are the criterion of [Stacks, Tag 08Q9] with no smallness hypothesis on the site,
> `Stacks.ChaoticSite.AbelianValued.isIso_totalDerivedColimit_single_map_iff_of_large`, and the
> quasi-isomorphism of Moore complexes
> `CommAlgCat.quasiIso_mooreCochain_polynomialSiteDifferentialsBaseChangeUnit`, which is the
> Δ-instance of [Stacks, Tag 08RX] rather than [Stacks, Tag 08QJ].

```lean
def polynomialSiteDerivedLowerShriekDifferentialsBaseChangeIso :
    polynomialSiteDerivedLowerShriekSingle A B
        (polynomialSiteAbelianRelativeDifferentials A B) ≅
      polynomialSiteDerivedLowerShriekSingle A B
        (polynomialSiteAbelianDifferentialsBaseChange A B)
```

**`CommAlgCat.polynomialSiteDerivedLowerShriekConstantIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean#L259). The attribute's comment: “Lπ\_!(B̲) = B in D(Ab), for the point morphism of the site C\_\{B/A} of Tag 08PR itself -- not of the footnote-restricted site nor of a small model of it -- with Lπ\_! the total left derived functor of the colimit over the index category, which is the π\_! of Tag 08PF, and with B read as the abelian group ULift.\{u+1} B exactly as the site's own ringed point CommAlgCat.polynomialRingedPoint reads it”.

> **`Lπ_!(B̲) = B` in `D(Ab)` at the site `C_{B/A}` itself**, the second identification of
> [Stacks, Tag 08QK]. Here `B̲` is the constant sheaf of rings with value `B` of
> [Stacks, Tag 08PR] read on its underlying abelian sheaf, `π` is the point morphism of the site
> `C_{B/A}` of that tag -- not of a restriction of it -- and `Lπ_!` is the total left derived
> functor of the colimit over the index category, which is the `π_!` of [Stacks, Tag 08PF].
>
> The proof is the source's: the polynomial algebra on no variables, augmented by `A → B`, is a
> terminal object of the site (`CommAlgCat.isTerminal_polynomialBaseObj`), so `π^{-1}` is the
> constant diagram and has an exact right adjoint, and [Stacks, Tag 08Q7] in the form
> `Stacks.ChaoticSite.derivedConstCompColimitIso'` gives `Lπ_! ∘ π^{-1} = id`.

```lean
def polynomialSiteDerivedLowerShriekConstantIso :
    polynomialSiteDerivedLowerShriekSingle A B (polynomialSiteAbelianConstantPresheaf A B) ≅
      polynomialSiteBaseInDerived A B
```

**`CommAlgCat.polynomialSiteDerivedLowerShriekStructureConstantIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean#L430). The attribute's comment: “Lπ\_!(𝒪) = Lπ\_!(B̲) in D(Ab), as the isomorphism induced by the augmentation 𝒪 ⟶ B̲ of Tag 08PR, for the point morphism of the site C\_\{B/A} of Tag 08PR itself -- not of the footnote-restricted site nor of a small model of it”.

> **`Lπ_!(𝒪) = Lπ_!(B̲)` in `D(Ab)` at the site `C_{B/A}` itself**, the first identification of
> [Stacks, Tag 08QK], as the isomorphism **induced by the augmentation `𝒪 ⟶ B̲`** of
> [Stacks, Tag 08PR].
>
> The two inputs are the criterion of [Stacks, Tag 08Q9] with no smallness hypothesis on the site,
> `Stacks.ChaoticSite.AbelianValued.isIso_totalDerivedColimit_single_map_iff_of_large`, and the
> quasi-isomorphism of Moore complexes
> `CommAlgCat.quasiIso_mooreCochain_polynomialSiteAbelianAugmentation`, whose own input is
> [Stacks, Tag 08QI].

```lean
def polynomialSiteDerivedLowerShriekStructureConstantIso :
    polynomialSiteDerivedLowerShriekSingle A B (polynomialSiteAbelianStructurePresheaf A B) ≅
      polynomialSiteDerivedLowerShriekSingle A B (polynomialSiteAbelianConstantPresheaf A B)
```

**`CommAlgCat.polynomialSiteDerivedLowerShriekStructureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean#L448). The attribute's comment: “Lπ\_!(𝒪) = B in D(Ab), for the point morphism of the site C\_\{B/A} of Tag 08PR itself -- not of the footnote-restricted site nor of a small model of it”.

> **`Lπ_!(𝒪) = B` in `D(Ab)` at the site `C_{B/A}` itself**, the composite of the two
> identifications `Lπ_!(𝒪) = Lπ_!(B̲)` and `Lπ_!(B̲) = B` of [Stacks, Tag 08QK].

```lean
def polynomialSiteDerivedLowerShriekStructureIso :
    polynomialSiteDerivedLowerShriekSingle A B (polynomialSiteAbelianStructurePresheaf A B) ≅
      polynomialSiteBaseInDerived A B
```

**`CommAlgCat.polynomialSiteDerivedLowerShriekCotangentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSitePointValuesLargeSite.lean#L520). The attribute's comment: “L\_\{B/A} = Lπ\_!(Ω\_\{𝒪/A} ⊗\_𝒪 B̲) in D(Ab), for the point morphism of the site C\_\{B/A} of Tag 08PR itself -- not of the footnote-restricted site nor of a small model of it: the cotangent complex of Tag 08PN, read in D(Ab) at the coefficient universe of the site, is Lπ\_! of the sheaf i^*Ω\_\{𝒪/A}”.

> **`L_{B/A} = Lπ_!(Ω_{𝒪/A} ⊗_𝒪 B̲)` in `D(Ab)` at the site `C_{B/A}` itself**, the third
> identification of [Stacks, Tag 08QK]. The left-hand side is the cotangent complex of
> [Stacks, Tag 08PN] with its `B`-module structures forgotten, read at the coefficient universe of
> the site; the right-hand side is `Lπ_!` of the abelian sheaf `i^*Ω_{𝒪/A} = Ω_{𝒪/A} ⊗_𝒪 B̲`.
>
> The two inputs are [Stacks, Tag 08PS] at `C_{B/A}` itself,
> `CommAlgCat.polynomialSiteResolutionDerivedColimitNatIso`, which computes `Lπ_!` by the extended
> Moore complex of the evaluation on the standard resolution, and
> `CommAlgCat.polynomialSiteCotangentMooreComplexIso`, which is [Stacks, Tag 08PU] identifying that
> Moore complex with the complex of `L_{B/A}`.

```lean
def polynomialSiteDerivedLowerShriekCotangentIso :
    polynomialSiteDerivedLowerShriekSingle A B (polynomialSiteAbelianCotangentPresheaf A B) ≅
      polynomialSiteCotangentInDerived A B
```

## Tag 08SA, a lemma

[Tag 08SA](https://stacks.math.columbia.edu/tag/08SA) in the Stacks Project.

**`CommAlgCat.exists_distTriang_derivedExtensionScalars_cotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/StandardResolutionOverPolynomialBase.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/StandardResolutionOverPolynomialBase.lean#L1089).

> **Stacks Project, Tag 08SA.** Let `A → B → C` be ring maps. If `B` is a polynomial algebra
> over `A`, then there is a distinguished triangle
>
> `L_{B/A} ⊗^𝐋_B C → L_{C/A} → L_{C/B} → (L_{B/A} ⊗^𝐋_B C)[1]`
>
> in `D(C)`. This is the lemma as stated.
>
> The proof is the source's. The standard resolution `P_•` of `C` over `B` is, read over `A`, also
> a resolution of `C` over `A` (`CommAlgCat.standardResolution_isResolution_restrictScalars`); the
> differentials of the tower `A → B → Pₙ` form a split short exact sequence because `Pₙ` is a
> polynomial algebra over `B`, and base changing it to `C` gives a short exact sequence of
> complexes of `C`-modules
> `Ω[B⁄A] ⊗[B] C → Ω[P_•⁄A] ⊗[P_•] C → Ω[P_•⁄B] ⊗[P_•] C`
> (`CommAlgCat.restrictedCotangentComplexShortComplex_shortExact`) whose distinguished triangle is
> the one asserted. Its last term is `L_{C/B}` by definition; its first term is `Ω[B⁄A] ⊗[B] C` in
> degree `0`, which is `L_{B/A} ⊗^𝐋_B C` by Tag 08QH and the projectivity of `Ω[B⁄A]`
> (`CommAlgCat.nonempty_derivedExtensionScalars_cotangentComplex_iso_of_isPolynomialAlgebra`); and
> its middle term is `L_{C/A}` because `P_•` and the standard resolution of `C` over `A` are two
> resolutions of `C` over `A`, so by Tag 08PU both compute derived lower shriek of `i^*Ω_{𝒪/A}` on
> the site `C_{C/A}`
> (`CommAlgCat.nonempty_q_restrictedCotangentComplex_iso_cotangentComplex`).
>
> The triangle is stated existentially, as in the source: the identifications of the first and
> middle terms are isomorphisms of objects of `D(C)`, which transport a distinguished triangle to
> one with the named objects. The three rings are taken in one universe, which is no restriction:
> three rings with maps between them always live in a common universe. The conditional form at two
> universes, with the identification of the middle term as a hypothesis, is
> `CommAlgCat.exists_distTriang_derivedExtensionScalars_of_isPolynomialAlgebra`.

```lean
public theorem exists_distTriang_derivedExtensionScalars_cotangentComplex
    (A : Type u) [CommRing A] (B : Type u) [CommRing B] [Algebra A B]
    (C : Type u) [CommRing C] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    (hB : Algebra.IsPolynomialAlgebra A B) :
    ∃ (f : (CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsGeneral
            (algebraMap B C)).functor.obj
          (DerivedCategory.Q.obj (cotangentComplexOfAlgebra.{u, u} A B)) ⟶
        DerivedCategory.Q.obj (cotangentComplexOfAlgebra.{u, u} A C))
      (g : DerivedCategory.Q.obj (cotangentComplexOfAlgebra.{u, u} A C) ⟶
        DerivedCategory.Q.obj (cotangentComplexOfAlgebra.{u, u} B C))
      (h : DerivedCategory.Q.obj (cotangentComplexOfAlgebra.{u, u} B C) ⟶
        ((CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsGeneral
            (algebraMap B C)).functor.obj
          (DerivedCategory.Q.obj (cotangentComplexOfAlgebra.{u, u} A B)))⟦(1 : ℤ)⟧),
      Pretriangulated.Triangle.mk f g h ∈
        Pretriangulated.distinguishedTriangles (C := DerivedCategory (ModuleCat.{u} C))
```

## Tag 09D4, an example

[Tag 09D4](https://stacks.math.columbia.edu/tag/09D4) in the Stacks Project.

**`Algebra.PolynomialPresentationWithKernelGenerators.Degeneracies.degeneracyZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean#L81). The attribute's comment: “degeneracies”.

> The first degeneracy fixes `uᵢ` and sends `xₜ` to `yₜ`.

```lean
noncomputable def degeneracyZero :
    DegreeOne.P1 p →ₐ[p.A] DegreeTwo.P2 p
```

**`Algebra.PolynomialPresentationWithKernelGenerators.Degeneracies.degeneracyOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean#L89). The attribute's comment: “degeneracies”.

> The second degeneracy fixes `uᵢ` and sends `xₜ` to `zₜ`.

```lean
noncomputable def degeneracyOne :
    DegreeOne.P1 p →ₐ[p.A] DegreeTwo.P2 p
```

**`Algebra.PolynomialPresentationWithKernelGenerators.Degeneracies.degeneracyZero_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean#L98). The attribute's comment: “degeneracies”.

> The first degeneracy is the unique algebra map with the displayed
> values on the old and relation variables.

```lean
theorem degeneracyZero_unique
    (f : DegreeOne.P1 p →ₐ[p.A] DegreeTwo.P2 p)
    (hu : ∀ i : p.variableIndex,
      f (MvPolynomial.X (Sum.inl i)) =
        MvPolynomial.X (DegreeTwo.DegreeTwoVariable.base i))
    (hx : ∀ t : p.relationIndex,
      f (MvPolynomial.X (Sum.inr t)) =
        MvPolynomial.X (DegreeTwo.DegreeTwoVariable.y t)) :
    f = degeneracyZero p
```

**`Algebra.PolynomialPresentationWithKernelGenerators.Degeneracies.degeneracyOne_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean#L116). The attribute's comment: “degeneracies”.

> The second degeneracy is the unique algebra map with the displayed
> values on the old and relation variables.

```lean
theorem degeneracyOne_unique
    (f : DegreeOne.P1 p →ₐ[p.A] DegreeTwo.P2 p)
    (hu : ∀ i : p.variableIndex,
      f (MvPolynomial.X (Sum.inl i)) =
        MvPolynomial.X (DegreeTwo.DegreeTwoVariable.base i))
    (hx : ∀ t : p.relationIndex,
      f (MvPolynomial.X (Sum.inr t)) =
        MvPolynomial.X (DegreeTwo.DegreeTwoVariable.z t)) :
    f = degeneracyOne p
```

**`Algebra.PolynomialPresentationWithKernelGenerators.Degeneracies.degeneracyZero_lifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean#L330). The attribute's comment: “degeneracies”.

> The displayed first degeneracy lifts the first degeneracy of the
> one-coskeleton.

```lean
theorem degeneracyZero_lifts :
    AlgCat.ofHom (degeneracyZeroLift p) ≫
        DegreeTwo.degreeTwoToCoskeleton p =
        (DegreeOne.degreeOneCoskeleton p).oneIso.inv ≫
        (DegreeOne.degreeOneCoskeleton p).simplicial.σ (0 : Fin 2)
```

**`Algebra.PolynomialPresentationWithKernelGenerators.Degeneracies.degeneracyOne_lifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean#L344). The attribute's comment: “degeneracies”.

> The displayed second degeneracy lifts the second degeneracy of the
> one-coskeleton.

```lean
theorem degeneracyOne_lifts :
    AlgCat.ofHom (degeneracyOneLift p) ≫
        DegreeTwo.degreeTwoToCoskeleton p =
      (DegreeOne.degreeOneCoskeleton p).oneIso.inv ≫
        (DegreeOne.degreeOneCoskeleton p).simplicial.σ (1 : Fin 2)
```

**`Algebra.PolynomialPresentationWithKernelGenerators.Degeneracies.explicitResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean, line 1526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/Degeneracies.lean#L1526). The attribute's comment: “degeneracies”.

> The displayed first three degrees extend to a polynomial simplicial
> resolution of `B` over `A`.

```lean
noncomputable def explicitResolution : ExplicitResolution p
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeOne.degreeOneCoskeleton`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean#L377). The attribute's comment: “degree\_one”.

> The coskeleton of the explicit one-truncated polynomial simplicial algebra.

```lean
noncomputable def degreeOneCoskeleton : DegreeOneCoskeleton p
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeOne.range_faceZero_sub_faceOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean#L563). The attribute's comment: “degree\_one”.

> Exactness at `P₀` of `P₁ → P₀ → B`.

```lean
theorem range_faceZero_sub_faceOne :
    Set.range (fun z : P1 p => faceZero p z - faceOne p z) =
      {z : p.P0 | augmentationZero p z = 0}
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeOne.facePair_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean#L606). The attribute's comment: “degree\_one”.

> Every compatible pair of degree-zero simplices lifts to degree one.

```lean
theorem facePair_surjective :
    ∀ a b : p.P0,
      augmentationZero p a = augmentationZero p b →
        ∃ z : P1 p, faceZero p z = a ∧ faceOne p z = b
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeOne.coskeleton_trivialKanFibration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean, line 700](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeOne.lean#L700). The attribute's comment: “degree\_one”.

> The augmentation of this degree-one coskeleton is a trivial Kan fibration.

```lean
theorem coskeleton_trivialKanFibration :
    SSet.trivialKanFibrations
      (Functor.whiskerRight (degreeOneCoskeleton p).augmentation
        (forget (AlgCat.{max u v w x} p.A)))
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeTwo.faces_matching`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean#L191). The attribute's comment: “degree\_two”.

> The three displayed face maps define a map to the degree-two matching object.

```lean
theorem faces_matching (q : P2 p) :
    MatchingTriple p (faceZero p q) (faceOne p q) (faceTwo p q)
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeTwo.matchingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean, line 878](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean#L878). The attribute's comment: “degree\_two”.

> The actual second degree of the one-coskeleton is canonically the algebra
> of compatible triples of degree-one elements.

```lean
noncomputable def matchingEquiv :
    ((DegreeOne.degreeOneCoskeleton p).simplicial _⦋2⦌) ≃
      {g : (DegreeOne.P1 p ×
          DegreeOne.P1 p × DegreeOne.P1 p) //
        MatchingTriple p g.1 g.2.1 g.2.2}
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeTwo.matchingEquiv_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean, line 905](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean#L905). The attribute's comment: “degree\_two”.

> The canonical matching equivalence records exactly the three actual faces
> of a degree-two simplex.

```lean
theorem matchingEquiv_faces
    (a : (DegreeOne.degreeOneCoskeleton p).simplicial _⦋2⦌) :
    (matchingEquiv p a).val =
      (coskeletonFace p 0 a, coskeletonFace p 1 a, coskeletonFace p 2 a)
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeTwo.degreeTwoToCoskeleton`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean, line 1053](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean#L1053). The attribute's comment: “degree\_two”.

> The algebra map from the displayed polynomial degree two to the actual
> degree-two object of the one-coskeleton.

```lean
noncomputable def degreeTwoToCoskeleton :
    algP2 p ⟶ (DegreeOne.degreeOneCoskeleton p).simplicial _⦋2⦌
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeTwo.matchingEquiv_degreeTwoToCoskeleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean, line 1136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean#L1136). The attribute's comment: “degree\_two”.

> Under the canonical matching equivalence, the algebra map has the three
> displayed face maps as its components.

```lean
theorem matchingEquiv_degreeTwoToCoskeleton (q : P2 p) :
    matchingEquiv p (degreeTwoToCoskeleton p (ULift.up q)) =
      ⟨(faceZero p q, faceOne p q, faceTwo p q), faces_matching p q⟩
```

**`Algebra.PolynomialPresentationWithKernelGenerators.DegreeTwo.degreeTwoToCoskeleton_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean, line 1518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/Degeneracies/DegreeTwo.lean#L1518). The attribute's comment: “degree\_two”.

> The displayed algebra map onto the actual second coskeleton degree is
> surjective.

```lean
theorem degreeTwoToCoskeleton_surjective :
    Function.Surjective (degreeTwoToCoskeleton p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.5, Tag 08PV](https://stacks.math.columbia.edu/tag/08PV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
