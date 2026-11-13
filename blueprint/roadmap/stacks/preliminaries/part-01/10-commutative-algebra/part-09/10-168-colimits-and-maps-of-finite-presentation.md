---
declaration: section
origin: cited
lean: Module.Flat.eventually_flat_of_directed, Module.Flat.exists_finiteType_model, Module.Flat.exists_finitePresentation_model_of_directed, Module.Flat.exists_flat_models_and_eventually_flat, Algebra.exists_faithfullyFlat_finitePresentation_model, Stacks.DirectLimit.FiniteDescent.finite_baseChange_of_colimit_finite, surjective_baseChange_of_colimit, Stacks.DirectLimit.UnramifiedDescent.colimit_unramified
statement: formalized
proof: formalized
---

# 10.168 Colimits and maps of finite presentation, II

Section 10.168 of the Stacks Project, [Tag 07RF](https://stacks.math.columbia.edu/tag/07RF). 10 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02JO, a lemma

[Tag 02JO](https://stacks.math.columbia.edu/tag/02JO) in the Stacks Project.

**`Module.Flat.eventually_flat_of_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/FlatModel/DirectedModel.lean, line 779](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SpreadingOut/FlatModel/DirectedModel.lean#L779). The attribute's comment: “(3)”. References: EGA IV (11.2.6), “affine case, (ii)”; EGA IV (11.2.6.1), “(ii) necessity”.

> **Stacks 02JO (3).** Let `R → S` be of finite presentation and let `M` be a finitely
> presented `S`-module which is flat over `R`. Let `(R → S, M) = colim_λ (R_λ → S_λ, M_λ)` be a
> directed colimit such that `R_μ ⊗_{R_λ} S_λ → S_μ` and `S_μ ⊗_{S_λ} M_λ → M_μ` are isomorphisms
> for `μ ≥ λ`, each `R_λ → S_λ` is of finite presentation and each `M_λ` is a finitely presented
> `S_λ`-module. Then `M_λ` is flat over `R_λ` for all sufficiently large `λ`.

```lean
theorem Module.Flat.eventually_flat_of_directed {R S : Type u} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FinitePresentation R S] (M : Type w) [AddCommGroup M] [Module R M]
    [Module S M] [IsScalarTower R S M] [Module.FinitePresentation S M] [Module.Flat R M]
    {ι : Type*} [Preorder ι] [Nonempty ι] [IsDirected ι (· ≤ ·)]
    {A B : ι → Type v} [∀ i, CommRing (A i)] [∀ i, CommRing (B i)] [∀ i, Algebra (A i) (B i)]
    {N : ι → Type*} [∀ i, AddCommGroup (N i)] [∀ i, Module (B i) (N i)]
    (a : ∀ i j, i ≤ j → A i →+* A j) (b : ∀ i j, i ≤ j → B i →+* B j)
    (n : ∀ i j (h : i ≤ j), N i →ₛₗ[b i j h] N j)
    [DirectedSystem A fun i j h => a i j h] [DirectedSystem B fun i j h => b i j h]
    [DirectedSystem N fun i j h => n i j h]
    (hab : ∀ i j (h : i ≤ j),
      (b i j h).comp (algebraMap (A i) (B i)) = (algebraMap (A j) (B j)).comp (a i j h))
    (ρ : ∀ i, A i →+* R) (σ : ∀ i, B i →+* S) (ν : ∀ i, N i →ₛₗ[σ i] M)
    (hρ : ∀ i j (h : i ≤ j) x, ρ j (a i j h x) = ρ i x)
    (hσ : ∀ i j (h : i ≤ j) x, σ j (b i j h x) = σ i x)
    (hν : ∀ i j (h : i ≤ j) x, ν j (n i j h x) = ν i x)
    (hρσ : ∀ i, (σ i).comp (algebraMap (A i) (B i)) = (algebraMap R S).comp (ρ i))
    (hρs : ∀ r, ∃ i x, ρ i x = r) (hρz : ∀ i x, ρ i x = 0 → ∃ j, ∃ h : i ≤ j, a i j h x = 0)
    (hσs : ∀ s, ∃ i x, σ i x = s) (hσz : ∀ i x, σ i x = 0 → ∃ j, ∃ h : i ≤ j, b i j h x = 0)
    (hνs : ∀ m, ∃ i x, ν i x = m) (hνz : ∀ i x, ν i x = 0 → ∃ j, ∃ h : i ≤ j, n i j h x = 0)
    (hpush : ∀ i j (h : i ≤ j), CategoryTheory.IsPushout (CommRingCat.ofHom (a i j h))
      (CommRingCat.ofHom (algebraMap (A i) (B i))) (CommRingCat.ofHom (algebraMap (A j) (B j)))
      (CommRingCat.ofHom (b i j h)))
    (hbc : ∀ i j (h : i ≤ j), letI := algebraB b h
      letI := Module.compHom (N j) (b i j h)
      haveI : IsScalarTower (B i) (B j) (N j) := .of_algebraMap_smul fun _ _ => rfl
      IsBaseChange (B j) (transLinear b n h))
    (hfp : ∀ i, Algebra.FinitePresentation (A i) (B i))
    (hfpN : ∀ i, Module.FinitePresentation (B i) (N i)) :
    ∃ i, ∀ j, i ≤ j →
      letI := Module.compHom (N j) (algebraMap (A j) (B j)); Module.Flat (A j) (N j)
```

**`Module.Flat.exists_finiteType_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/FlatModel/FiniteTypeModel.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SpreadingOut/FlatModel/FiniteTypeModel.lean#L254). The attribute's comment: “(1)”.

> **Stacks 02JO (1).** Let `R → S` be of finite presentation and let `M` be a finitely
> presented `S`-module which is flat over `R`. Then there are a ring `R₀` of finite type over `ℤ`,
> an `R₀`-algebra `S₀` of finite type and a finite `S₀`-module `M₀` flat over `R₀`, together with
> ring maps `R₀ → R`, `S₀ → S` and an `S₀`-linear map `M₀ → M`, such that `S = R ⊗_{R₀} S₀` and
> `M = S ⊗_{S₀} M₀`.

```lean
theorem Module.Flat.exists_finiteType_model {R S : Type u} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FinitePresentation R S] (M : Type w) [AddCommGroup M] [Module R M]
    [Module S M] [IsScalarTower R S M] [Module.FinitePresentation S M] [Module.Flat R M] :
    ∃ (R₀ S₀ M₀ : Type u) (_ : CommRing R₀) (_ : CommRing S₀) (_ : Algebra R₀ S₀)
      (_ : Algebra R₀ R) (_ : Algebra S₀ S) (_ : Algebra R₀ S) (_ : IsScalarTower R₀ R S)
      (_ : IsScalarTower R₀ S₀ S) (_ : AddCommGroup M₀) (_ : Module S₀ M₀) (_ : Module R₀ M₀)
      (_ : IsScalarTower R₀ S₀ M₀) (_ : Module S₀ M) (_ : IsScalarTower S₀ S M)
      (f : M₀ →ₗ[S₀] M),
      Algebra.FiniteType ℤ R₀ ∧ Algebra.FiniteType R₀ S₀ ∧ Module.Finite S₀ M₀ ∧
        Module.Flat R₀ M₀ ∧ Algebra.IsPushout R₀ R S₀ S ∧ IsBaseChange S f
```

**`Module.Flat.exists_finitePresentation_model_of_directed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/FlatModel/FiniteTypeModel.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SpreadingOut/FlatModel/FiniteTypeModel.lean#L288). The attribute's comment: “(2)”. References: EGA IV (1.8.4.2).

> **Stacks 02JO (2).** Let `R → S` be of finite presentation and let `M` be a finitely
> presented `S`-module which is flat over `R`. If `R = colim_λ R_λ` is a directed colimit, then
> there are `λ`, an `R_λ`-algebra `S_λ` of finite presentation and a finitely presented
> `S_λ`-module `M_λ` which is flat over `R_λ`, with an algebra map `S_λ → S` and an `S_λ`-linear
> map `M_λ → M` exhibiting `S = R ⊗_{R_λ} S_λ` and `M = S ⊗_{S_λ} M_λ`.

```lean
theorem Module.Flat.exists_finitePresentation_model_of_directed {R S : Type u} [CommRing R]
    [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S] (M : Type w) [AddCommGroup M]
    [Module R M] [Module S M] [IsScalarTower R S M] [Module.FinitePresentation S M]
    [Module.Flat R M] {ι : Type*} [Preorder ι] [Nonempty ι] [IsDirected ι (· ≤ ·)]
    {A : ι → Type v} [∀ i, CommRing (A i)] (a : ∀ i j, i ≤ j → A i →+* A j)
    [DirectedSystem A fun i j h => a i j h] (ρ : ∀ i, A i →+* R)
    (hρ : ∀ i j (h : i ≤ j) x, ρ j (a i j h x) = ρ i x) (hs : ∀ r, ∃ i x, ρ i x = r)
    (hz : ∀ i x, ρ i x = 0 → ∃ j, ∃ h : i ≤ j, a i j h x = 0) :
    ∃ i, letI := (ρ i).toAlgebra
      ∃ (T P : Type (max u v)) (_ : CommRing T) (_ : Algebra (A i) T) (_ : Algebra T S)
        (_ : Algebra (A i) S) (_ : IsScalarTower (A i) R S) (_ : IsScalarTower (A i) T S)
        (_ : AddCommGroup P) (_ : Module T P) (_ : Module (A i) P) (_ : IsScalarTower (A i) T P)
        (_ : Module T M) (_ : IsScalarTower T S M) (f : P →ₗ[T] M),
        Algebra.FinitePresentation (A i) T ∧ Module.FinitePresentation T P ∧
          Module.Flat (A i) P ∧ Algebra.IsPushout (A i) R T S ∧ IsBaseChange S f
```

**`Module.Flat.exists_flat_models_and_eventually_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/FlatModel/Packaged.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SpreadingOut/FlatModel/Packaged.lean#L47).

> **Stacks 02JO.** Let `R → S` be of finite presentation and let `M` be a finitely presented
> `S`-module which is flat over `R`. Then:
>
> 1. there are a ring `R₀` of finite type over `ℤ`, an `R₀`-algebra `S₀` of finite type and a finite
>    `S₀`-module `M₀` flat over `R₀`, with maps to `R`, `S` and `M` exhibiting `S = R ⊗_{R₀} S₀` and
>    `M = S ⊗_{S₀} M₀`;
> 2. if `R = colim_λ R_λ` is a directed colimit, such a model already exists over some `R_λ`, with
>    `R_λ → S_λ` of finite presentation and `M_λ` a finitely presented `S_λ`-module;
> 3. if `(R → S, M) = colim_λ (R_λ → S_λ, M_λ)` is a directed colimit of finitely presented pairs
>    with cartesian transition squares, then `M_λ` is flat over `R_λ` for all large `λ`.
>
> This is the packaged three-part form of the tag, stated at the universe generality the source
> asserts: the index `I`, the three colimits `R`, `S`, `M`, the stage families `A`, `B`, `N` and the
> model `R₀`, `S₀`, `M₀` of part (1) all live in independent universes. The three parts are also
> available separately as `Module.Flat.exists_finiteType_model`,
> `Module.Flat.exists_finitePresentation_model_of_directed` and
> `Module.Flat.eventually_flat_of_directed`, which are proved with `R` and `S` in one universe (and,
> in part (1), with the model in that universe); this statement is deduced from them by the universe
> transport of the previous section, with no repetition of the spreading-out argument.

```lean
theorem Module.Flat.exists_flat_models_and_eventually_flat
    {R : Type uR} {S : Type uS} {M : Type uM}
    [CommRing R] [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.FinitePresentation S M] [Module.Flat R M] :
    (∃ (R₀ : Type uR₀) (S₀ : Type uS₀) (M₀ : Type uM₀)
        (_ : CommRing R₀) (_ : CommRing S₀) (_ : Algebra R₀ S₀)
        (_ : Algebra R₀ R) (_ : Algebra S₀ S) (_ : Algebra R₀ S)
        (_ : IsScalarTower R₀ R S) (_ : IsScalarTower R₀ S₀ S)
        (_ : AddCommGroup M₀) (_ : Module S₀ M₀) (_ : Module R₀ M₀)
        (_ : IsScalarTower R₀ S₀ M₀) (_ : Module S₀ M) (_ : IsScalarTower S₀ S M)
        (f : M₀ →ₗ[S₀] M),
      Algebra.FiniteType ℤ R₀ ∧ Algebra.FiniteType R₀ S₀ ∧ Module.Finite S₀ M₀ ∧
        Module.Flat R₀ M₀ ∧ Algebra.IsPushout R₀ R S₀ S ∧ IsBaseChange S f) ∧
    (∀ (I : Type uI) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
        (A : I → Type uA) (_ : ∀ i, CommRing (A i))
        (a : ∀ i j, i ≤ j → A i →+* A j)
        (_ : DirectedSystem A (fun i j h ↦ a i j h))
        (ρ : ∀ i, A i →+* R),
      (∀ i j (h : i ≤ j), ρ j ∘ a i j h = ρ i) →
      (∀ x : R, ∃ i y, ρ i y = x) →
      (∀ i y, ρ i y = 0 → ∃ (j : I) (h : i ≤ j), a i j h y = 0) →
      ∃ i : I,
        letI : Algebra (A i) R := (ρ i).toAlgebra
        ∃ (T : Type (max uA uS)) (P : Type (max (max uA uS) uM))
            (_ : CommRing T) (_ : Algebra (A i) T)
            (_ : Algebra T S) (_ : Algebra (A i) S)
            (_ : IsScalarTower (A i) R S) (_ : IsScalarTower (A i) T S)
            (_ : AddCommGroup P) (_ : Module T P) (_ : Module (A i) P)
            (_ : IsScalarTower (A i) T P) (_ : Module T M) (_ : IsScalarTower T S M)
            (f : P →ₗ[T] M),
          algebraMap (A i) R = ρ i ∧
            Algebra.FinitePresentation (A i) T ∧ Module.FinitePresentation T P ∧
            Module.Flat (A i) P ∧ Algebra.IsPushout (A i) R T S ∧ IsBaseChange S f) ∧
    (∀ (I : Type uI) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
        (A : I → Type uA) (B : I → Type uB) (N : I → Type uN)
        (_ : ∀ i, CommRing (A i)) (_ : ∀ i, CommRing (B i))
        (_ : ∀ i, AddCommGroup (N i)) (_ : ∀ i, Module (B i) (N i))
        (a : ∀ i j, i ≤ j → A i →+* A j)
        (b : ∀ i j, i ≤ j → B i →+* B j)
        (_ : DirectedSystem A (fun i j h ↦ a i j h))
        (_ : DirectedSystem B (fun i j h ↦ b i j h))
        (g : ∀ i, A i →+* B i)
        (n : ∀ i j, (h : i ≤ j) → N i →ₛₗ[b i j h] N j)
        (ρ : ∀ i, A i →+* R) (σ : ∀ i, B i →+* S)
        (ν : ∀ i, N i →+ M)
        (hg : ∀ i j (h : i ≤ j), (g j).comp (a i j h) = (b i j h).comp (g i)),
      (∀ i x, n i i le_rfl x = x) →
      (∀ i j k (hij : i ≤ j) (hjk : j ≤ k) x,
        n j k hjk (n i j hij x) = n i k (hij.trans hjk) x) →
      (∀ i j (h : i ≤ j), ρ j ∘ a i j h = ρ i) →
      (∀ i j (h : i ≤ j), σ j ∘ b i j h = σ i) →
      (∀ i j (h : i ≤ j) x, ν j (n i j h x) = ν i x) →
      (∀ i, (algebraMap R S).comp (ρ i) = (σ i).comp (g i)) →
      (∀ i x m, ν i (g i x • m) = ρ i x • ν i m) →
      (∀ i y m, ν i (y • m) = σ i y • ν i m) →
      (∀ x : R, ∃ i y, ρ i y = x) →
      (∀ i y, ρ i y = 0 → ∃ (j : I) (h : i ≤ j), a i j h y = 0) →
      (∀ x : S, ∃ i y, σ i y = x) →
      (∀ i y, σ i y = 0 → ∃ (j : I) (h : i ≤ j), b i j h y = 0) →
      (∀ x : M, ∃ i y, ν i y = x) →
      (∀ i y, ν i y = 0 → ∃ (j : I) (h : i ≤ j), n i j h y = 0) →
      (∀ i,
        letI : Algebra (A i) (B i) := (g i).toAlgebra
        Algebra.FinitePresentation (A i) (B i)) →
      (∀ i, Module.FinitePresentation (B i) (N i)) →
      (∀ i j (h : i ≤ j),
        letI : Algebra (A i) (B i) := (g i).toAlgebra
        letI : Algebra (A i) (A j) := (a i j h).toAlgebra
        letI : Algebra (B i) (B j) := (b i j h).toAlgebra
        letI : Algebra (A j) (B j) := (g j).toAlgebra
        letI : Algebra (A i) (B j) := ((g j).comp (a i j h)).toAlgebra
        letI : IsScalarTower (A i) (A j) (B j) :=
          IsScalarTower.of_algebraMap_smul fun _ _ ↦ rfl
        letI : IsScalarTower (A i) (B i) (B j) :=
          IsScalarTower.of_algebraMap_smul fun x y ↦ by
            change b i j h (g i x) * y = g j (a i j h x) * y
            exact congrArg (fun z : B j ↦ z * y)
              (by simpa using (RingHom.congr_fun (hg i j h) x).symm)
        Algebra.IsPushout (A i) (A j) (B i) (B j)) →
      (∀ i j (h : i ≤ j),
        letI : Algebra (B i) (B j) := (b i j h).toAlgebra
        letI : Module (B i) (N j) := Module.compHom (N j) (b i j h)
        letI : IsScalarTower (B i) (B j) (N j) :=
          IsScalarTower.of_algebraMap_smul fun _ _ ↦ rfl
        IsBaseChange (B j)
          (⟨(n i j h).toAddHom, fun x y ↦ (n i j h).map_smul' x y⟩ :
            N i →ₗ[B i] N j)) →
      ∃ i, ∀ j, i ≤ j →
        letI : Module (A j) (N j) := Module.compHom (N j) (g j)
        Module.Flat (A j) (N j))
```

## Tag 034Y, a lemma

[Tag 034Y](https://stacks.math.columbia.edu/tag/034Y) in the Stacks Project.

**`Algebra.exists_faithfullyFlat_finitePresentation_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ColimitsII/FaithfullyFlatModel.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ColimitsII/FaithfullyFlatModel.lean#L216). The attribute's comment: “The diagram is the data `R → A₀ → A` with `IsScalarTower R A₀ A` (the left square) and `A₀ → B₀ → B`, `A₀ → A → B` through a common `A₀ → B` (the right square); `B = A ⊗_{A₀} B₀` is `Algebra.IsPushout A₀ A B₀ B`. The rings `A₀`, `B₀` live in the universe of `R`, `A` and `B`.”.

> **Stacks 034Y.** Let `R → A → B` be ring maps with `A → B` faithfully flat of finite
> presentation. Then there are an `R`-algebra `A₀` of finite presentation and a faithfully flat
> `A₀`-algebra `B₀` of finite presentation, with maps `A₀ → A` of `R`-algebras and `B₀ → B`
> compatible with `A₀ → B₀` and `A → B`, such that `B = A ⊗_{A₀} B₀`.

```lean
theorem Algebra.exists_faithfullyFlat_finitePresentation_model {R : Type v} {A B : Type u}
    [CommRing R] [CommRing A] [CommRing B] [Algebra R A] [Algebra A B] [Module.FaithfullyFlat A B]
    [Algebra.FinitePresentation A B] :
    ∃ (A₀ B₀ : Type (max u v)) (_ : CommRing A₀) (_ : CommRing B₀) (_ : Algebra R A₀)
      (_ : Algebra A₀ B₀) (_ : Algebra A₀ A) (_ : IsScalarTower R A₀ A) (_ : Algebra B₀ B)
      (_ : Algebra A₀ B) (_ : IsScalarTower A₀ A B) (_ : IsScalarTower A₀ B₀ B),
      Algebra.FinitePresentation R A₀ ∧ Module.FaithfullyFlat A₀ B₀ ∧
        Algebra.FinitePresentation A₀ B₀ ∧ Algebra.IsPushout A₀ A B₀ B
```

## Tag 07RG, a lemma

[Tag 07RG](https://stacks.math.columbia.edu/tag/07RG) in the Stacks Project.

**`Stacks.DirectLimit.FiniteDescent.finite_baseChange_of_colimit_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Finite.lean, line 525](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Finite.lean#L525).

> Let `L` be the directed colimit of a directed system of `R`-algebras `(A i)`, and let
> `φ : B →ₐ[R] C` be a map of `R`-algebras of finite type. If the base change
> `id_L ⊗ φ : L ⊗_R B → L ⊗_R C` is a finite ring map, then there is an index `i` such that the
> base change `id_{A i} ⊗ φ : A i ⊗_R B → A i ⊗_R C` is a finite ring map.

```lean
theorem finite_baseChange_of_colimit_finite
    {A : ι → Type*} [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)]
    {f : ∀ ⦃i j⦄, i ≤ j → A i →ₐ[R] A j}
    {L : Type*} [CommRing L] [Algebra R L]
    {g : ∀ i, A i →ₐ[R] L}
    (φ : B →ₐ[R] C)
    (hcolim : IsDirectedColimit A f L g)
    (hfin_type : φ.FiniteType)
    (hfin : (baseChange L φ).toRingHom.Finite) :
    ∃ i : ι, (baseChange (A i) φ).toRingHom.Finite
```

## Tag 07RH, a lemma

[Tag 07RH](https://stacks.math.columbia.edu/tag/07RH) in the Stacks Project.

**`surjective_baseChange_of_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Surjective.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Surjective.lean#L276). References: SGA 3 VIB (10.1), “special case”.

> Let `A = colim_i Aᵢ` be a directed colimit of `A₀`-algebras, and let `C₀` be an
> `A₀`-algebra that is of finite type over the `A₀`-algebra `B₀` (via the structure map
> `φ₀ : B₀ → C₀`). If the base change `id_A ⊗ φ₀ : A ⊗_{A₀} B₀ → A ⊗_{A₀} C₀` is
> surjective, then there is some index `i` for which the base change
> `id_{Aᵢ} ⊗ φ₀ : Aᵢ ⊗_{A₀} B₀ → Aᵢ ⊗_{A₀} C₀` is already surjective.

```lean
theorem surjective_baseChange_of_colimit
    (hcolim : IsRingColimit A₀ Aᵢ f A g)
    (hsurj : Function.Surjective (baseChangeColim A₀ A B₀ C₀))
    (hft : Algebra.FiniteType B₀ C₀) :
    ∃ i : I, Function.Surjective (baseChange A₀ Aᵢ B₀ C₀ i)
```

## Tag 0C4F, a lemma

[Tag 0C4F](https://stacks.math.columbia.edu/tag/0C4F) in the Stacks Project.

**`Stacks.DirectLimit.UnramifiedDescent.colimit_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Unramified.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Unramified.lean#L530).

> If the base change `Φ = id_A ⊗ φ₀` of `φ₀` to the directed colimit `A = colim_i Aᵢ` is
> unramified and `C₀` is of finite type over `B₀` via `φ₀`, then the base change
> `Φᵢ = id_{Aᵢ} ⊗ φ₀` is unramified at some finite stage `i ≥ O`, where `G i` is an
> `A₀`-algebra via `f O i h`.

```lean
theorem colimit_unramified
    (hΦ :
      letI : Algebra ((A G f) ⊗[G O] B₀) ((A G f) ⊗[G O] C₀) :=
        (phiColim G f O B₀ C₀ φ₀).toRingHom.toAlgebra
      Algebra.Unramified ((A G f) ⊗[G O] B₀) ((A G f) ⊗[G O] C₀))
    (hFT :
      letI : Algebra B₀ C₀ := φ₀.toRingHom.toAlgebra
      Algebra.FiniteType B₀ C₀) :
    ∃ i, ∃ (h : O ≤ i),
      letI : Algebra (G O) (G i) := (f O i h).toAlgebra
      letI φᵢ : (G i) ⊗[G O] B₀ →ₐ[G i] (G i) ⊗[G O] C₀ :=
        Algebra.TensorProduct.map (AlgHom.id (G i) (G i)) φ₀
      letI : Algebra ((G i) ⊗[G O] B₀) ((G i) ⊗[G O] C₀) := φᵢ.toRingHom.toAlgebra
      Algebra.Unramified ((G i) ⊗[G O] B₀) ((G i) ⊗[G O] C₀)
```

## Tag 0C32, a lemma

[Tag 0C32](https://stacks.math.columbia.edu/tag/0C32) in the Stacks Project.

**`Stacks.DirectLimit.FinitePresentationDescent.isIso_of_finitePresentation_colim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Bijective.lean, line 836](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Algebra/DirectLimit/Descent/Bijective.lean#L836).

> Let `A = colim_{i ∈ I} A_i` be a directed colimit of commutative rings, fix an index
> `i₀ ∈ I`, and let `φ₀ : B₀ → C₀` be a map of `A i₀`-algebras. If the base-changed map
> `φ : A ⊗_{A i₀} B₀ → A ⊗_{A i₀} C₀` is bijective and `φ₀` is of finite presentation, then there
> exists an index `i ≥ i₀` such that the base-changed map
> `φ_i : A_i ⊗_{A i₀} B₀ → A_i ⊗_{A i₀} C₀` is bijective.

```lean
theorem isIso_of_finitePresentation_colim
    (hfp : (φ₀ : B₀ →+* C₀).FinitePresentation)
    (hφ : Function.Bijective (phiColim A f i₀ B₀ C₀ φ₀)) :
    ∃ i : ι, ∃ h : i₀ ≤ i, Function.Bijective (phiAt A f i₀ B₀ C₀ φ₀ i h)
```

## Tag 07RI, a lemma

[Tag 07RI](https://stacks.math.columbia.edu/tag/07RI) in the Stacks Project.

**`RingHom.Etale.exists_baseChange_etale_of_colimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/ColimitBaseChange.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/ColimitBaseChange.lean#L378). The attribute's comment: “The source's `A_0` is the base ring `R` and its index set restricted to `i ≥ 0`, which is cofinal, is the diagram; `A = colim A_i` is `Limits.ColimitPresentation J A` in `CommAlgCat R` over an arbitrary filtered `J`, together with the `PreservesColimit` instance saying the colimit is computed on underlying sets, and the base change of `φ` is Mathlib's `Algebra.TensorProduct.map (AlgHom.id R _) φ`. See the module docstring.”.

> **Étale spreads out in a filtered colimit of base rings.** Let `A` be the colimit of a
> filtered diagram of `R`-algebras `Aᵢ`, computed on underlying sets, and let `φ : B →ₐ[R] C` be of
> finite presentation. If the base change `1 ⊗ φ : A ⊗[R] B → A ⊗[R] C` is étale, then
> `1 ⊗ φ : Aᵢ ⊗[R] B → Aᵢ ⊗[R] C` is étale for some `i`.

```lean
public theorem exists_baseChange_etale_of_colimitPresentation
    {R : Type u} [CommRing R] {J : Type w} [Category.{t} J] [IsFiltered J]
    {A : CommAlgCat.{v} R} (pres : ColimitPresentation J A)
    [PreservesColimit (pres.diag ⋙ forget₂ (CommAlgCat R) CommRingCat) (forget CommRingCat)]
    {B C : Type*} [CommRing B] [CommRing C] [Algebra R B] [Algebra R C] (φ : B →ₐ[R] C)
    (hφ : φ.toRingHom.FinitePresentation)
    (hA : (Algebra.TensorProduct.map (AlgHom.id R ↥A) φ).toRingHom.Etale) :
    ∃ i : J, (Algebra.TensorProduct.map (AlgHom.id R ↥(pres.diag.obj i)) φ).toRingHom.Etale
```

## Tag 0C0B, a lemma

[Tag 0C0B](https://stacks.math.columbia.edu/tag/0C0B) in the Stacks Project.

**`RingHom.Smooth.exists_baseChange_smooth_of_colimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/Smooth.lean, line 1125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SpreadingOut/Smooth.lean#L1125). The attribute's comment: “The source's `A_0` is the base ring `R` and its index set restricted to `i ≥ 0`, which is cofinal, is the diagram; `A = colim A_i` is `Limits.ColimitPresentation J A` in `CommAlgCat R` over a filtered `J` whose colimit is computed on underlying sets, and the base change of `φ` is Mathlib's `Algebra.TensorProduct.map (AlgHom.id R _) φ`. Smooth is `RingHom.Smooth`, the source's Definition 00T2. See the module docstring.”.

> **Smoothness spreads out in a filtered colimit of base rings.** Let `A` be the colimit of a
> filtered diagram of `R`-algebras `Aᵢ`, computed on underlying sets, and let `φ : B →ₐ[R] C` be of
> finite presentation. If the base change `1 ⊗ φ : A ⊗[R] B → A ⊗[R] C` is smooth, then
> `1 ⊗ φ : Aᵢ ⊗[R] B → Aᵢ ⊗[R] C` is smooth for some `i`.

```lean
public theorem exists_baseChange_smooth_of_colimitPresentation
    {R : Type u} [CommRing R] {J : Type w} [Category.{t} J] [IsFiltered J]
    {A : CommAlgCat.{v} R} (pres : ColimitPresentation J A)
    [PreservesColimit (pres.diag ⋙ forget₂ (CommAlgCat.{v} R) CommRingCat.{v})
      (forget CommRingCat)]
    {B C : Type*} [CommRing B] [CommRing C] [Algebra R B] [Algebra R C] (φ : B →ₐ[R] C)
    (hφ : φ.toRingHom.FinitePresentation)
    (hA : (Algebra.TensorProduct.map (AlgHom.id R ↥A) φ).toRingHom.Smooth) :
    ∃ i : J, (Algebra.TensorProduct.map (AlgHom.id R ↥(pres.diag.obj i)) φ).toRingHom.Smooth
```

## Tag 0C33, a lemma

[Tag 0C33](https://stacks.math.columbia.edu/tag/0C33) in the Stacks Project.

**`Algebra.IsRelativeGlobalCompleteIntersection.exists_stage_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ColimitsII/TensorProductStage.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ColimitsII/TensorProductStage.lean#L259). The attribute's comment: “The relative global complete intersection case. The colimit `A` is the ring `R` with the cocone `ρ`, given elementwise: every element of `R` comes from a stage, and an element of a stage dying in `R` dies at a later stage. The maps `A_i ⊗ B₀ → A_i ⊗ C₀` are `Algebra.TensorProduct.map id φ₀`.”.

> **Stacks 0C33, relative global complete intersections.** Let `A = colim_i A_i` be a directed
> colimit of rings, let `0 ≤ i` be an index and `φ₀ : B₀ → C₀` a map of `A₀`-algebras with `C₀` of
> finite presentation over `B₀`. If `A ⊗_{A₀} B₀ → A ⊗_{A₀} C₀` is a relative global complete
> intersection, then so is `A_i ⊗_{A₀} B₀ → A_i ⊗_{A₀} C₀` for some `i ≥ 0`.

```lean
theorem Algebra.IsRelativeGlobalCompleteIntersection.exists_stage_tensorProduct
    {ι : Type*} [Preorder ι] [IsDirected ι (· ≤ ·)]
    {A : ι → Type u} [∀ i, CommRing (A i)] (a : ∀ i j, i ≤ j → A i →+* A j)
    [DirectedSystem A fun i j h => a i j h] {R : Type*} [CommRing R] (ρ : ∀ i, A i →+* R)
    (hρ : ∀ i j (h : i ≤ j) x, ρ j (a i j h x) = ρ i x) (hρs : ∀ r, ∃ i x, ρ i x = r)
    (hρz : ∀ i x, ρ i x = 0 → ∃ j, ∃ h : i ≤ j, a i j h x = 0)
    {i₀ : ι} {B₀ C₀ : Type v} [CommRing B₀] [CommRing C₀] [Algebra (A i₀) B₀] [Algebra (A i₀) C₀]
    (φ₀ : B₀ →ₐ[A i₀] C₀) (hfp : φ₀.FinitePresentation)
    (h : letI := (ρ i₀).toAlgebra
      letI := (Algebra.TensorProduct.map (AlgHom.id (A i₀) R) φ₀).toRingHom.toAlgebra
      Algebra.IsRelativeGlobalCompleteIntersection (R ⊗[A i₀] B₀) (R ⊗[A i₀] C₀)) :
    ∃ i, ∃ h : i₀ ≤ i, letI := (a i₀ i h).toAlgebra
      letI := (Algebra.TensorProduct.map (AlgHom.id (A i₀) (A i)) φ₀).toRingHom.toAlgebra
      Algebra.IsRelativeGlobalCompleteIntersection (A i ⊗[A i₀] B₀) (A i ⊗[A i₀] C₀)
```

**`Algebra.Syntomic.exists_stage_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ColimitsII/TensorProductStage.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ColimitsII/TensorProductStage.lean#L281). The attribute's comment: “The syntomic case, with the conventions of the relative global complete intersection case.”.

> **Stacks 0C33, syntomic ring maps.** Let `A = colim_i A_i` be a directed colimit of rings,
> let `0 ≤ i` be an index and `φ₀ : B₀ → C₀` a map of `A₀`-algebras with `C₀` of finite
> presentation over `B₀`. If `A ⊗_{A₀} B₀ → A ⊗_{A₀} C₀` is syntomic, then so is
> `A_i ⊗_{A₀} B₀ → A_i ⊗_{A₀} C₀` for some `i ≥ 0`.

```lean
theorem Algebra.Syntomic.exists_stage_tensorProduct
    {ι : Type*} [Preorder ι] [IsDirected ι (· ≤ ·)]
    {A : ι → Type u} [∀ i, CommRing (A i)] (a : ∀ i j, i ≤ j → A i →+* A j)
    [DirectedSystem A fun i j h => a i j h] {R : Type*} [CommRing R] (ρ : ∀ i, A i →+* R)
    (hρ : ∀ i j (h : i ≤ j) x, ρ j (a i j h x) = ρ i x) (hρs : ∀ r, ∃ i x, ρ i x = r)
    (hρz : ∀ i x, ρ i x = 0 → ∃ j, ∃ h : i ≤ j, a i j h x = 0)
    {i₀ : ι} {B₀ C₀ : Type v} [CommRing B₀] [CommRing C₀] [Algebra (A i₀) B₀] [Algebra (A i₀) C₀]
    (φ₀ : B₀ →ₐ[A i₀] C₀) (hfp : φ₀.FinitePresentation)
    (h : letI := (ρ i₀).toAlgebra
      letI := (Algebra.TensorProduct.map (AlgHom.id (A i₀) R) φ₀).toRingHom.toAlgebra
      Algebra.Syntomic (R ⊗[A i₀] B₀) (R ⊗[A i₀] C₀)) :
    ∃ i, ∃ h : i₀ ≤ i, letI := (a i₀ i h).toAlgebra
      letI := (Algebra.TensorProduct.map (AlgHom.id (A i₀) (A i)) φ₀).toRingHom.toAlgebra
      Algebra.Syntomic (A i ⊗[A i₀] B₀) (A i ⊗[A i₀] C₀)
```

## Tag 034Z, a lemma

[Tag 034Z](https://stacks.math.columbia.edu/tag/034Z) in the Stacks Project.

**`Algebra.exists_quasiFinite_faithfullyFlat_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FinitePresentation/ColimitsII/QuasiFiniteFactorization.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FinitePresentation/ColimitsII/QuasiFiniteFactorization.lean#L535). The attribute's comment: “The commutative triangle is the data `R → S → S'` with `IsScalarTower R S S'`; quasi-finiteness (Definition 00PL) is `Algebra.QuasiFinite`, which omits the finite type clause of the source's definition, supplied here by `Algebra.FinitePresentation`. `S'` lives in the universe of `R` and `S`.”. References: EGA IV (17.16.2), “affine case”.

> **Stacks 034Z.** Let `R → S` be a faithfully flat ring map of finite presentation. Then there
> is an `S`-algebra `S'` such that `R → S'` is quasi-finite, faithfully flat and of finite
> presentation.

```lean
theorem Algebra.exists_quasiFinite_faithfullyFlat_finitePresentation
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [Module.FaithfullyFlat R S] [Algebra.FinitePresentation R S] :
    ∃ (S' : Type u) (_ : CommRing S') (_ : Algebra R S') (_ : Algebra S S')
      (_ : IsScalarTower R S S'), Algebra.QuasiFinite R S' ∧ Module.FaithfullyFlat R S' ∧
        Algebra.FinitePresentation R S'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.168, Tag 07RF](https://stacks.math.columbia.edu/tag/07RF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
