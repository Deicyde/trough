---
declaration: section
origin: cited
lean: DifferentialGradedModule.PropertyPFiltration, Stacks.DifferentialGraded.DGModule.PropertyPFiltration, Stacks.DifferentialGraded.DGModule.admissible_ses_of_propertyP, DifferentialGradedModule.leftOrthogonal_acyclic_of_propertyP, DifferentialGraded.LeftModule.exists_cover, DifferentialGradedModule.exists_cover, DifferentialGraded.NativeCover.exists_dgModule_surjective_cover, DifferentialGradedModule.exists_propertyP_resolution
statement: formalized
proof: formalized
---

# 22.20 P-resolutions

Section 22.20 of the Stacks Project, [Tag 09KK](https://stacks.math.columbia.edu/tag/09KK). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09KK, the section

[Tag 09KK](https://stacks.math.columbia.edu/tag/09KK) in the Stacks Project.

**`DifferentialGradedModule.PropertyPFiltration`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/PropertyP.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/PropertyP.lean#L315). The attribute's comment: “a filtration as in property (P): exhaustive, admissible inclusions, graded pieces direct sums of shifts A[k]; bundled encoding”.

> A *property-(P) filtration* of a differential graded `A`-module `P` (Tag 09KK): an
> exhaustive increasing filtration `0 = F_{-1} ⊆ F_0 ⊆ F_1 ⊆ ⋯ ⊆ P` by differential graded
> submodules whose inclusions are admissible monomorphisms and whose successive quotients are
> direct sums of shifts of `A`.
>
> The stages are presented by injective homomorphisms `ι i : F i ⟶ P` rather than as submodules,
> and the graded pieces by surjective homomorphisms onto direct sums of shifts with the prescribed
> kernel; the implicit stage `F_{-1} = 0` is encoded by the requirement that `F 0` itself be
> isomorphic to a direct sum of shifts.

```lean
structure PropertyPFiltration (P : DifferentialGradedModule.{u, u, u} A)
```

Declarations registered for the tag:

- [`Stacks.DifferentialGraded.DGModule.PropertyPFiltration`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Basic.lean#L375), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/PropertyP.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/PropertyP.lean#L354) (StacksFrontier): “a filtration as in property (P); unbundled encoding”.

## Tag 09KL, a lemma

[Tag 09KL](https://stacks.math.columbia.edu/tag/09KL) in the Stacks Project.

**`Stacks.DifferentialGraded.DGModule.admissible_ses_of_propertyP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Telescope.lean, line 908](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Telescope.lean#L908).

> **Stacks Tag 09KL (Lemma 22.20.1).**
> Let `(A, d)` be a *lawful* differential graded algebra, `P` a lawful differential graded
> `A`-module, and `F_*` a filtration as in property (P) (Definition 3, with all its
> gradedness/lawfulness/quotient conditions bundled into `PropertyPFiltration`).  Then the
> telescope object `⨁_{i ≥ 0} F_i P` is itself a lawful differential graded `A`-module, and
> there exist DG homomorphisms `α` and `β` whose underlying linear maps are the explicit
> telescoping maps `telescopeAlphaFun F` and `telescopeBetaFun F`, fitting into an admissible
> short exact sequence of differential graded `A`-modules
> `0 → ⨁_{i ≥ 0} F_i P →[α] ⨁_{i ≥ 0} F_i P →[β] P → 0`.
>
> In particular this asserts items (1)–(5) of the Main Statement: the source/target object
> lives in the category `Mod_(A,d)` (it is lawful), `α, β` are DG homomorphisms with the
> prescribed underlying maps, `α` is injective, `β` is surjective, `range α = ker β`, and the
> sequence is admissible.
>
> Proof: assemble the eight sub-lemmas above.  Lawfulness is `telescopeObj_isLawful`; obtain
> `α, β` from `exists_telescopeAlpha`/`exists_telescopeBeta` with `α.toFun = telescopeAlphaFun F`
> and `β.toFun = telescopeBetaFun F`; the `AdmissibleSES` fields are then
> `telescopeAlphaFun_injective`,
> `telescopeBetaFun_surjective`, `telescope_exact`, `telescopeAlpha_admissibleMono`, and
> `telescopeBeta_admissibleEpi`, with the underlying-map equalities `hα`, `hβ` used to rewrite
> `α.toFun`/`β.toFun` to the explicit telescope maps.

```lean
theorem admissible_ses_of_propertyP
    {P : DGModule A} (hP : P.IsLawful)
    (F : PropertyPFiltration P) :
    (telescopeObj F).IsLawful ∧
    ∃ (α : Hom (telescopeObj F) (telescopeObj F)) (β : Hom (telescopeObj F) P),
      α.toFun = telescopeAlphaFun F ∧
      β.toFun = telescopeBetaFun F ∧
      AdmissibleSES α β
```

## Tag 09KM, a lemma

[Tag 09KM](https://stacks.math.columbia.edu/tag/09KM) in the Stacks Project.

**`DifferentialGradedModule.leftOrthogonal_acyclic_of_propertyP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/LeftOrthogonalAcyclic.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/LeftOrthogonalAcyclic.lean#L126).

> **Stacks Tag 09KM.** *"Let `(A, d)` be a differential graded algebra. Let `P` be a
> differential graded `A`-module with property (P). Then `Hom_{K(Mod_(A,d))}(P, N) = 0` for all
> acyclic differential graded `A`-modules `N`."*
>
> Here the vanishing of all those hom-sets is phrased as membership of `P` in the left orthogonal
> of the acyclic objects of the homotopy category, which says that every morphism out of `P` into
> an object satisfying `acyclic'` is zero; since every object of `HomotopyCategory A` is the image
> of a differential graded module, the two readings agree.

```lean
theorem leftOrthogonal_acyclic_of_propertyP {P : DifferentialGradedModule A}
    (F : PropertyPFiltration P) :
    (acyclic' A).leftOrthogonal ((toHomotopyCategory A).obj P)
```

## Tag 09KN, a lemma

[Tag 09KN](https://stacks.math.columbia.edu/tag/09KN) in the Stacks Project.

**`DifferentialGraded.LeftModule.exists_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean, line 913](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/LeftNativeCover.lean#L913).

> **Stacks 09KN for left differential graded modules.** Let `(A, d)` be a differential graded
> algebra over a commutative ring `R` and let `N` be a *left* differential graded `A`-module. Then
> there are a family of degrees `k : ι → ℤ`, a family of cell kinds `b : ι → Bool` and a
> homomorphism `f : ⨁ᵢ Q_{kᵢ} ⟶ N` such that
>
> 1. `f` is surjective;
> 2. a homogeneous cocycle of `N` of degree `m` is the image of a cocycle of degree `m`, and
>    consequently `Ker(d) → Ker(d_N)` is surjective — part (2) of the source lemma; and
> 3. `⨁ᵢ Q_{kᵢ}` sits in an admissible short exact sequence
>    `0 → ⨁ᵢ A[-kᵢ-1] → ⨁ᵢ Q_{kᵢ} → ⨁ᵢ A[-kᵢ] → 0`
>
> whose two ends are direct sums of shifts of `A`.
>
> The cover is indexed by the homogeneous elements of `N`, which give two-cells and supply (1),
> together with the homogeneous *cocycles* of `N`, which give bare cells and supply (2): the
> generator `xᵢ` of a bare cell is itself a cocycle, homogeneous of degree `kᵢ`, and it maps to
> the cocycle it indexes. A general cocycle of `N` is the finite sum of its homogeneous
> components, which are cocycles by `induction_cocycle`.
>
> The degreewise form of (2) is recorded as well as the plain one because that is what the proof
> of Stacks 09KT needs: the differential of a graded dual is precomposition with the *signed*
> differential, and the sign is only known on a homogeneous element.

```lean
theorem exists_cover (A : DifferentialGradedAlgebra R) (N : LeftModule A) :
    ∃ (ι : Type u) (_ : DecidableEq ι) (k : ι → ℤ) (b : ι → Bool)
      (f : twoCellSum A k b ⟶ N),
      Function.Surjective f.toFun ∧
      (∀ (m : ℤ) (z : N.M), z ∈ N.grading m → N.d z = 0 →
        ∃ q : (twoCellSum A k b).M, q ∈ (twoCellSum A k b).grading m ∧
          (twoCellSum A k b).d q = 0 ∧ f.toFun q = z) ∧
      (∀ z : N.M, N.d z = 0 →
        ∃ q : (twoCellSum A k b).M, (twoCellSum A k b).d q = 0 ∧ f.toFun q = z) ∧
      ∃ (i : directSumShifts A (fun c => -k c - 1) ⟶ twoCellSum A k b)
        (p : twoCellSum A k b ⟶ directSumShifts A (fun c => -k c)),
        IsAdmissibleShortExact i p
```

**`DifferentialGradedModule.exists_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/NativeCoverBundled.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/NativeCoverBundled.lean#L77).

> **Stacks 09KN** in the bundled encoding. Let `(A, d)` be a differential graded algebra over
> a commutative ring `R` and let `M` be a right differential graded `A`-module. Then there is a
> right differential graded `A`-module `P` and a homomorphism `f : P ⟶ M` such that
>
> 1. `f` is surjective;
> 2. `f` is surjective on cocycles in every degree: every degree-`n` cocycle of `M` is the image
>    of a degree-`n` cocycle of `P`; and
> 3. `P` is an extension of a direct sum of shifts of `A` by a direct sum of shifts of `A`, by an
>    admissible short exact sequence `P' ⟶ P ⟶ P''` whose two ends `P'` and `P''` admit bijective
>    homomorphisms onto `directSumShifts A k'` and `directSumShifts A k''` respectively.
>
> This is `DifferentialGraded.NativeCover.exists_native_cover` transported to the bundled
> encoding.

```lean
theorem exists_cover (A : DifferentialGradedAlgebra R) (M : DifferentialGradedModule A) :
    ∃ (P : DifferentialGradedModule A) (f : P ⟶ M),
      Function.Surjective f.toFun ∧
      (∀ (n : ℤ) (y : M.M), y ∈ M.grading n → M.d y = 0 →
        ∃ x : P.M, x ∈ P.grading n ∧ P.d x = 0 ∧ f.toFun x = y) ∧
      ∃ (P' P'' : DifferentialGradedModule A) (i : P' ⟶ P) (p : P ⟶ P'')
        (ι' ι'' : Type u) (dec' : DecidableEq ι') (dec'' : DecidableEq ι'')
        (k' : ι' → ℤ) (k'' : ι'' → ℤ)
        (e' : P' ⟶ @directSumShifts _ _ A ι' dec' k')
        (e'' : P'' ⟶ @directSumShifts _ _ A ι'' dec'' k''),
        Function.Bijective e'.toFun ∧ Function.Bijective e''.toFun ∧
        IsAdmissibleShortExact i p
```

**`DifferentialGraded.NativeCover.exists_dgModule_surjective_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/NativeCover/Assembly.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/NativeCover/Assembly.lean#L639).

> **Theorem (Stacks Project, Tag 09KN, Lemma 22.20.3).**
>
> Let `(A, d)` be a differential graded algebra over `R` and `M` a differential
> graded `A`-module.  Then there exists a differential graded `A`-module `P` and a
> homomorphism `φ : P → M` of differential graded `A`-modules such that:
> 1. `φ` is surjective;
> 2. the induced map on cocycles `Ker(d_P) → Ker(d_M)` is graded surjective, i.e.
>    every degree-`n` cocycle of `M` is the image of a degree-`n` cocycle of `P`;
>    and
> 3. `P` sits in an admissible short exact sequence `0 → P' → P → P'' → 0` of
>    differential graded `A`-modules where both `P'` and `P''` are isomorphic to
>    direct sums of shifts of `A`.
>
> All objects live in a common universe `Type u`.

```lean
theorem exists_dgModule_surjective_cover
    {R : Type u} {A : Type u} [CommRing R] [Ring A] [Algebra R A]
    {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] (dA : DGAlgebra R A 𝒜)
    {M : Type u} [AddCommGroup M] [Module R M] (PM : DGModule R A 𝒜 dA M) :
    ∃ (P : Type u) (_ : AddCommGroup P) (_ : Module R P)
      (PP : DGModule R A 𝒜 dA P) (φ : DGModule.Hom PP PM),
      -- (1) φ is surjective
      φ.Surjective ∧
      -- (2) the induced map on cocycles is graded surjective
      φ.GradedSurjectiveOnCocycles ∧
      -- (3) P sits in an admissible SES with both ends direct sums of shifts of A
      (∃ (P' : Type u) (_ : AddCommGroup P') (_ : Module R P')
        (PP' : DGModule R A 𝒜 dA P')
        (P'' : Type u) (_ : AddCommGroup P'') (_ : Module R P'')
        (PP'' : DGModule R A 𝒜 dA P''),
        -- the shift index types live in `Type u` as well, which is what the
        -- single-universe reading of Tag 09KN asserts
        IsDirectSumOfShifts.{u, u, u, u} PP' ∧ IsDirectSumOfShifts.{u, u, u, u} PP'' ∧
        Nonempty (AdmissibleSES PP' PP PP''))
```

## Tag 09KP, a lemma

[Tag 09KP](https://stacks.math.columbia.edu/tag/09KP) in the Stacks Project.

**`DifferentialGradedModule.exists_propertyP_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/PropertyP.lean, line 635](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/PropertyP.lean#L635).

> **Property-(P) resolutions exist** (Tag 09KP). Every right differential graded module `M`
> over a differential graded algebra `(A, d)` receives a quasi-isomorphism from a differential
> graded `A`-module `P` carrying a property-(P) filtration: an exhaustive increasing filtration by
> differential graded submodules with admissible inclusions whose successive quotients are direct
> sums of shifts of `A`.

```lean
theorem exists_propertyP_resolution (A : DifferentialGradedAlgebra.{u, u} R)
    (M : DifferentialGradedModule.{u, u, u} A) :
    ∃ (P : DifferentialGradedModule.{u, u, u} A) (f : P ⟶ M),
      QuasiIso ((forgetToCochainComplex A).map f) ∧ Nonempty (PropertyPFiltration P)
```

**`Stacks.DifferentialGraded.DGModule.exists_propertyP_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/PropertyPResolution.lean, line 1297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/PropertyPResolution.lean#L1297).

> **Property-(P) resolutions exist.** Every lawful differential graded module `M` over a lawful
> differential graded algebra `A` receives a quasi-isomorphism from a lawful differential graded
> `A`-module `P` carrying a property-(P) filtration: an exhaustive increasing filtration by
> differential graded submodules with admissible inclusions whose graded pieces are direct sums of
> shifts of `A`.

```lean
public theorem exists_propertyP_resolution (A : DGAlgebra.{u, v} R) (hA : A.IsLawful)
    (M : DGModule.{u, w, v} A) (hM : M.IsLawful) :
    ∃ (P : DGModule.{u, max v w, v} A) (_hP : P.IsLawful) (f : DGModule.Hom P M),
      IsQuasiIsomorphism f ∧
        Nonempty (DGModule.PropertyPFiltration.{u, v, max v w, max v w, max v w, max v w} P)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.20, Tag 09KK](https://stacks.math.columbia.edu/tag/09KK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
