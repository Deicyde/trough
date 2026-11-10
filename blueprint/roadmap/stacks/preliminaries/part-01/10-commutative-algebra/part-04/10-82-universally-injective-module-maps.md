---
declaration: section
origin: cited
lean: UniversallyInjective, split_universallyExact, colim_universallyExact, Function.Exact.universallyExact_tfae, Function.Exact.split_iff_forall_rTensor_injective, Module.Flat.iff_forall_rTensor_injective_of_exact, UniversallyExact.flat_of_middle_flat, universallyInjective_rTensor
statement: formalized
proof: formalized
---

# 10.82 Universally injective module maps

Section 10.82 of the Stacks Project, [Tag 058H](https://stacks.math.columbia.edu/tag/058H). 14 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 058I, a definition

[Tag 058I](https://stacks.math.columbia.edu/tag/058I) in the Stacks Project.

**`UniversallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L342). References: EGA IV (11.9.14), “special case”; EGA IV (11.9.18), “special case”; SGA 1 II (4.5).

> **Universally injective module map.**
> A homomorphism of `R`-modules `f : M →ₗ[R] N` is *universally injective* if for every
> `R`-module `Q`, the induced map `f ⊗ id_Q : M ⊗_R Q → N ⊗_R Q` (i.e. `f.rTensor Q`) is
> injective.

```lean
def UniversallyInjective {M N : Type v} [AddCommGroup M] [AddCommGroup N]
    [Module R M] [Module R N] (f : M →ₗ[R] N) : Prop
```

## Tag 058J, an example

[Tag 058J](https://stacks.math.columbia.edu/tag/058J) in the Stacks Project.

**`split_universallyExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyExact.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyExact.lean#L289). The attribute's comment: “(1)”.

> A split short exact sequence is universally exact; equivalently its first map `f₁`
> is universally injective.

```lean
theorem split_universallyExact
    {M₁ M₂ M₃ : Type v} [AddCommGroup M₁] [Module R M₁]
    [AddCommGroup M₂] [Module R M₂] [AddCommGroup M₃] [Module R M₃]
    (S : ShortExact (R := R) M₁ M₂ M₃) (hS : S.IsSplit) :
    S.UniversallyExact
```

**`colim_universallyExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyExact.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyExact.lean#L385). The attribute's comment: “(2)”.

> Filtered colimits preserve universally exact short exact sequences.

```lean
theorem colim_universallyExact
    {ι : Type v} [Preorder ι] [IsDirected ι (· ≤ ·)] [Nonempty ι] [DecidableEq ι]
    {M₁ M₂ M₃ : ι → Type v}
    [∀ i, AddCommGroup (M₁ i)] [∀ i, Module R (M₁ i)]
    [∀ i, AddCommGroup (M₂ i)] [∀ i, Module R (M₂ i)]
    [∀ i, AddCommGroup (M₃ i)] [∀ i, Module R (M₃ i)]
    (D : DirectedSES (R := R) ι M₁ M₂ M₃)
    (hD : ∀ i, (D.seq i).UniversallyExact) :
    Function.Injective D.colimF₁ ∧
      Function.Surjective D.colimF₂ ∧
      LinearMap.range D.colimF₁ = LinearMap.ker D.colimF₂ ∧
      UniversallyInjective D.colimF₁
```

## Tag 058K, a theorem

[Tag 058K](https://stacks.math.columbia.edu/tag/058K) in the Stacks Project.

**`Function.Exact.universallyExact_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniversallyExact.lean, line 1168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/UniversallyExact.lean#L1168). The attribute's comment: “Items (1)-(6), in the source's order, as a `List.TFAE`.”.

> **Stacks 058K.** Let `0 → M₁ →[f₁] M₂ →[f₂] M₃ → 0` be a short exact sequence of `R`-modules.
> The following are equivalent:
> 1. the sequence is universally exact, that is, `f₁ ⊗ id_Q` is injective for every `R`-module `Q`;
> 2. for every finitely presented `R`-module `Q` the sequence
>    `0 → M₁ ⊗ Q → M₂ ⊗ Q → M₃ ⊗ Q → 0` is exact;
> 3. whenever `x i ∈ M₁`, `y j ∈ M₂` and `a i j ∈ R` satisfy `f₁ (x i) = ∑ j, a i j • y j` for all
>    `i`, there are `z j ∈ M₁` with `x i = ∑ j, a i j • z j` for all `i`;
> 4. every commutative square `f₁ ∘ β = γ ∘ α` with `α : Rⁿ → Rᵐ`, `β : Rⁿ → M₁` and `γ : Rᵐ → M₂`
>    admits `δ : Rᵐ → M₁` with `δ ∘ α = β`;
> 5. for every finitely presented `R`-module `P` the map `Hom_R(P, M₂) → Hom_R(P, M₃)` given by
>    postcomposition with `f₂` is surjective;
> 6. the sequence is the colimit of a directed system of split exact sequences
>    `0 → M₁ → M_{2,j} → M_{3,j} → 0` with `M_{3,j}` finitely presented.

```lean
public theorem Function.Exact.universallyExact_tfae {R : Type u} [CommRing R] [Small.{v} R]
    {M₁ M₂ M₃ : Type v} [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂] [Module R M₂]
    [AddCommGroup M₃] [Module R M₃] {f₁ : M₁ →ₗ[R] M₂} {f₂ : M₂ →ₗ[R] M₃}
    (h : Function.Exact f₁ f₂) (h₁ : Function.Injective f₁) (h₂ : Function.Surjective f₂) :
    List.TFAE
      [ ∀ (Q : Type v) [AddCommGroup Q] [Module R Q], Function.Injective (f₁.rTensor Q),
        ∀ (Q : Type v) [AddCommGroup Q] [Module R Q] [Module.FinitePresentation R Q],
          Function.Injective (f₁.rTensor Q) ∧ Function.Exact (f₁.rTensor Q) (f₂.rTensor Q) ∧
            Function.Surjective (f₂.rTensor Q),
        ∀ (n m : ℕ) (x : Fin n → M₁) (y : Fin m → M₂) (a : Fin n → Fin m → R),
          (∀ i, f₁ (x i) = ∑ j, a i j • y j) → ∃ z : Fin m → M₁, ∀ i, x i = ∑ j, a i j • z j,
        ∀ (n m : ℕ) (α : (Fin n →₀ R) →ₗ[R] (Fin m →₀ R)) (β : (Fin n →₀ R) →ₗ[R] M₁)
          (γ : (Fin m →₀ R) →ₗ[R] M₂), f₁ ∘ₗ β = γ ∘ₗ α →
            ∃ δ : (Fin m →₀ R) →ₗ[R] M₁, δ ∘ₗ α = β,
        ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P],
          Function.Surjective (LinearMap.compRight (M := P) R f₂),
        ∃ (J : Type v) (_ : Preorder J) (_ : IsDirected J (· ≤ ·)) (_ : Nonempty J)
            (F : J ⥤ ShortComplex (ModuleCat.{v} R)) (c : Cocone F) (_ : IsColimit c)
            (_ : c.pt ≅ ModuleCat.shortComplexOfCompEqZero f₁ f₂ h.linearMap_comp_eq_zero),
          ∀ j, Nonempty (F.obj j).Splitting ∧ Module.FinitePresentation R (F.obj j).X₃ ∧
            IsIso ((c.ι.app j).τ₁) ]
```

## Tag 058L, a lemma

[Tag 058L](https://stacks.math.columbia.edu/tag/058L) in the Stacks Project.

**`Function.Exact.split_iff_forall_rTensor_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/UniversallyExact.lean, line 1354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/UniversallyExact.lean#L1354). The attribute's comment: “Exactness is hypothesised; splitness is the existence of a section of `f₂`.”.

> **Stacks 058L.** Let `0 → M₁ →[f₁] M₂ →[f₂] M₃ → 0` be a short exact sequence of `R`-modules
> with `M₃` of finite presentation. Then `f₂` admits an `R`-linear section — equivalently, the
> sequence is split — if and only if the sequence is universally exact, that is, if and only if
> `f₁ ⊗ id_Q : M₁ ⊗ Q → M₂ ⊗ Q` is injective for every `R`-module `Q`.

```lean
public theorem Function.Exact.split_iff_forall_rTensor_injective {R : Type u} [CommRing R]
    [Small.{v} R] {M₁ M₂ M₃ : Type v} [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂]
    [Module R M₂] [AddCommGroup M₃] [Module R M₃] [Module.FinitePresentation R M₃]
    {f₁ : M₁ →ₗ[R] M₂} {f₂ : M₂ →ₗ[R] M₃} (h : Function.Exact f₁ f₂)
    (h₁ : Function.Injective f₁) (h₂ : Function.Surjective f₂) :
    (∃ l : M₃ →ₗ[R] M₂, f₂ ∘ₗ l = LinearMap.id) ↔
      ∀ (Q : Type v) [AddCommGroup Q] [Module R Q],
        Function.Injective (f₁.rTensor Q)
```

## Tag 058M, a lemma

[Tag 058M](https://stacks.math.columbia.edu/tag/058M) in the Stacks Project.

**`Module.Flat.iff_forall_rTensor_injective_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L132). The attribute's comment: “Exactness is hypothesised; universal injectivity of `f₁` is spelled out.”.

> An `R`-module `M` is flat if and only if every short exact sequence
> `0 → M₁ →[f₁] M₂ →[f₂] M → 0` of `R`-modules is universally exact, that is, if and only if
> `f₁ ⊗ id_Q : M₁ ⊗ Q → M₂ ⊗ Q` is injective for every such sequence and every `R`-module `Q`.

```lean
public theorem Module.Flat.iff_forall_rTensor_injective_of_exact {R : Type u} [CommRing R]
    [Small.{v} R] {M : Type v} [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔
      ∀ ⦃M₁ M₂ : Type v⦄ [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂] [Module R M₂]
        (f₁ : M₁ →ₗ[R] M₂) (f₂ : M₂ →ₗ[R] M), Function.Injective f₁ →
        Function.Exact f₁ f₂ → Function.Surjective f₂ →
          ∀ (Q : Type v) [AddCommGroup Q] [Module R Q],
            Function.Injective (f₁.rTensor Q)
```

## Tag 058P, a lemma

[Tag 058P](https://stacks.math.columbia.edu/tag/058P) in the Stacks Project.

**`UniversallyExact.flat_of_middle_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyExact.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyExact.lean#L481). References: EGA 0 (6.7.4), “partial”.

> **Theorem (Stacks Tag 058P, Lemma 10.82.7).**
> Let `0 -> M_1 ->[u] M_2 ->[v] M_3 -> 0` be a universally exact sequence of `R`-modules
> with `M_2` flat. Then `M_1` is flat and `M_3` is flat.

```lean
theorem UniversallyExact.flat_of_middle_flat
    {M₁ M₂ M₃ : Type u} [AddCommGroup M₁] [AddCommGroup M₂] [AddCommGroup M₃]
    [Module R M₁] [Module R M₂] [Module R M₃]
    (u : M₁ →ₗ[R] M₂) (v : M₂ →ₗ[R] M₃)
    (hue : UniversallyExact u v) (hM₂ : Module.Flat R M₂) :
    Module.Flat R M₁ ∧ Module.Flat R M₃
```

## Tag 05CH, a lemma

[Tag 05CH](https://stacks.math.columbia.edu/tag/05CH) in the Stacks Project.

**`universallyInjective_rTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L358).

> If `u : M →ₗ[R] M'` is universally injective, then for any `R`-module `N` the induced map
> `u ⊗ id_N : M ⊗_R N → M' ⊗_R N` (i.e. `LinearMap.rTensor N u`) is again universally
> injective.

```lean
theorem universallyInjective_rTensor {R : Type} [CommRing R]
    {M : Type} [AddCommGroup M] [Module R M]
    {M' : Type} [AddCommGroup M'] [Module R M']
    (u : M →ₗ[R] M') (hu : UniversallyInjective u)
    (N : Type) [AddCommGroup N] [Module R N] :
    UniversallyInjective (LinearMap.rTensor N u)
```

## Tag 05CI, a lemma

[Tag 05CI](https://stacks.math.columbia.edu/tag/05CI) in the Stacks Project.

**`comp_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L392).

> A composition of universally injective `R`-module maps is universally injective.

```lean
theorem comp_universallyInjective {R : Type u} [CommRing R] {M N P : Type*}
    [AddCommGroup M] [AddCommGroup N] [AddCommGroup P]
    [Module R M] [Module R N] [Module R P]
    (f : M →ₗ[R] N) (g : N →ₗ[R] P)
    (hf : IsPureMono.{u, v} f) (hg : IsPureMono.{u, v} g) :
    IsPureMono.{u, v} (g ∘ₗ f)
```

## Tag 05CJ, a lemma

[Tag 05CJ](https://stacks.math.columbia.edu/tag/05CJ) in the Stacks Project.

**`Function.Injective.of_rTensor_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/InjectiveComposition.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/TensorProduct/InjectiveComposition.lean#L77). The attribute's comment: “Stated for one test module `Q`; the source's form is its closure over `Q`.”.

> Let `f : M →ₗ[R] M'` and `g : M' →ₗ[R] M''` be `R`-module maps and let `Q` be an `R`-module.
> If `(g ∘ₗ f) ⊗ id_Q` is injective, then so is `f ⊗ id_Q`. Quantifying over `Q`: if the
> composition `g ∘ₗ f` is universally injective, then `f` is universally injective.

```lean
public theorem Function.Injective.of_rTensor_comp {R : Type*} [CommSemiring R] {M M' M'' Q : Type*}
    [AddCommMonoid M] [Module R M] [AddCommMonoid M'] [Module R M'] [AddCommMonoid M'']
    [Module R M''] [AddCommMonoid Q] [Module R Q] {f : M →ₗ[R] M'} {g : M' →ₗ[R] M''}
    (h : Function.Injective ((g ∘ₗ f).rTensor Q)) : Function.Injective (f.rTensor Q)
```

## Tag 05CL, a lemma

[Tag 05CL](https://stacks.math.columbia.edu/tag/05CL) in the Stacks Project.

**`Stacks.UniversalInjectivity.LocalizationCriteria.universally_injective_check_stalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 867](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L867).

> For a ring map `R → S` and a map `f : M → M'` of `S`-modules, universal injectivity of `f` as
> a map of `R`-modules can be checked on localizations: the following are equivalent: `f` is
> universally injective over `R`; `f_q` is, for every prime `q` of `S`; `f_m` is, for every maximal
> ideal `m` of `S`; and the corresponding statements over the localizations `R_p`.

```lean
theorem universally_injective_check_stalks
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    {M : Type w} {M' : Type w'}
    [AddCommGroup M] [Module S M] [Module R M] [IsScalarTower R S M]
    [AddCommGroup M'] [Module S M'] [Module R M'] [IsScalarTower R S M']
    (f : M →ₗ[S] M') :
    [ -- (1) f is universally injective as a map of R-modules
      UniversallyInjective.{max u t} (f.restrictScalars R),
      -- (2) for every prime q of S, f_q is universally injective as a map of R-modules
      ∀ (q : Ideal S) [q.IsPrime], UniversallyInjective.{max u t} (A := R) (localizedMapR f q),
      -- (3) for every maximal m of S, f_m is universally injective as a map of R-modules
      ∀ (m : Ideal S) [m.IsMaximal], UniversallyInjective.{max u t} (A := R) (localizedMapR f m),
      -- (4) for every prime q of S, f_q is universally injective as a map of R_p-modules
      ∀ (q : Ideal S) [q.IsPrime],
        UniversallyInjective.{max u t} (A := Localization.AtPrime (q.under R)) (localizedMapRp f q),
      -- (5) for every maximal m of S, f_m is universally injective as a map of R_p-modules
      ∀ (m : Ideal S) [m.IsMaximal],
        UniversallyInjective.{max u t} (A := Localization.AtPrime (m.under R)) (localizedMapRp f m)
    ].TFAE
```

## Tag 05CM, a lemma

[Tag 05CM](https://stacks.math.columbia.edu/tag/05CM) in the Stacks Project.

**`IsLocalizedModule.rTensor_injective_of_rTensor_injective_and_iff_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Localization/UniversalInjectivity.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Localization/UniversalInjectivity.lean#L372). The attribute's comment: “Items (1) and (2) together, for one test module `Q`; the source's form is the closure over `Q`.”.

> **Stacks 05CM.** Let `A → B` be a ring map, let `S ⊆ A` and `S' ⊆ B` be multiplicative
> subsets, let `f : M → M'` be a map of `B`-modules and let `fₛ : N → N'` be its localization at
> `S'`, pinned by the square `fₛ ∘ₗ g = g' ∘ₗ f`. Let `Q` be an `A`-module with localization
> `S⁻¹Q` at `S`. Then:
>
> 1. if `f ⊗ id_Q` is injective, so is `fₛ ⊗ id_Q`, both tensor products taken over `A`;
> 2. `fₛ ⊗_A id_Q` is injective if and only if `fₛ ⊗_{S⁻¹A} id_{S⁻¹Q}` is injective.
>
> This is the source's own sentence, about one localized map. The two items are independent of each
> other and each is stated separately, over its own data alone, as
> `IsLocalizedModule.rTensor_injective_of_rTensor_injective` and
> `LinearMap.rTensor_injective_iff_extendScalarsOfIsLocalization`; those are the forms to cite.

```lean
public theorem IsLocalizedModule.rTensor_injective_of_rTensor_injective_and_iff_extendScalars
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B] (S : Submonoid A) (S' : Submonoid B)
    (Aₛ : Type*) [CommRing Aₛ] [Algebra A Aₛ] [IsLocalization S Aₛ] {M M' N N' Q Qₛ : Type*}
    [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M]
    [AddCommGroup M'] [Module A M'] [Module B M'] [IsScalarTower A B M']
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [Module Aₛ N] [IsScalarTower A Aₛ N]
    [AddCommGroup N'] [Module A N'] [Module B N'] [IsScalarTower A B N']
    [Module Aₛ N'] [IsScalarTower A Aₛ N']
    [AddCommGroup Q] [Module A Q] [AddCommGroup Qₛ] [Module A Qₛ] [Module Aₛ Qₛ]
    [IsScalarTower A Aₛ Qₛ] (g : M →ₗ[B] N) (g' : M' →ₗ[B] N') [IsLocalizedModule S' g]
    [IsLocalizedModule S' g'] (q : Q →ₗ[A] Qₛ) [IsLocalizedModule S q] (f : M →ₗ[B] M')
    (fₛ : N →ₗ[B] N') (hf : fₛ ∘ₗ g = g' ∘ₗ f) :
    (Function.Injective ((f.restrictScalars A).rTensor Q) →
        Function.Injective ((fₛ.restrictScalars A).rTensor Q)) ∧
      (Function.Injective ((fₛ.restrictScalars A).rTensor Q) ↔
        Function.Injective ((LinearMap.extendScalarsOfIsLocalization S Aₛ
          (fₛ.restrictScalars A)).rTensor Qₛ))
```

**`IsLocalizedModule.rTensor_injective_of_rTensor_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Localization/UniversalInjectivity.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Localization/UniversalInjectivity.lean#L403). The attribute's comment: “Item (1), for one test module `Q`; the source's form is the closure over `Q`.”.

> **Stacks 05CM, item (1).** Let `A → B` be a ring map, let `S' ⊆ B` be a multiplicative subset,
> let `f : M → M'` be a map of `B`-modules and let `fₛ : N → N'` be its localization at `S'`, pinned
> by the square `fₛ ∘ₗ g = g' ∘ₗ f`. Let `Q` be an `A`-module. If `f ⊗ id_Q` is injective, so is
> `fₛ ⊗ id_Q`, both tensor products taken over `A`.
>
> Quantifying over `Q`: if `f` is universally injective as a map of `A`-modules, then so is its
> localization at `S'`. Composed with
> `LinearMap.rTensor_injective_iff_extendScalarsOfIsLocalization` this gives the universal
> injectivity of the localization as a map of `S⁻¹A`-modules as well, for any `S ⊆ A` with
> `φ(S) ⊆ S'`.

```lean
public theorem IsLocalizedModule.rTensor_injective_of_rTensor_injective
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B] (S' : Submonoid B)
    {M M' N N' : Type*}
    [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M]
    [AddCommGroup M'] [Module A M'] [Module B M'] [IsScalarTower A B M']
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [AddCommGroup N'] [Module A N'] [Module B N'] [IsScalarTower A B N']
    (g : M →ₗ[B] N) (g' : M' →ₗ[B] N') [IsLocalizedModule S' g] [IsLocalizedModule S' g']
    (f : M →ₗ[B] M') (fₛ : N →ₗ[B] N') (hf : fₛ ∘ₗ g = g' ∘ₗ f) (Q : Type*) [AddCommGroup Q]
    [Module A Q] (h : Function.Injective ((f.restrictScalars A).rTensor Q)) :
    Function.Injective ((fₛ.restrictScalars A).rTensor Q)
```

**`LinearMap.rTensor_injective_iff_extendScalarsOfIsLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Localization/UniversalInjectivity.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Localization/UniversalInjectivity.lean#L428). The attribute's comment: “Item (2), for one test module `Q` and one localization `S⁻¹Q` of it; stated for an `A`-linear map between `S⁻¹A`-modules, of which the source's `B`-linear map between `(S')⁻¹B`-modules is a case.”.

> **Stacks 05CM, item (2).** Let `S ⊆ A` be a multiplicative subset, let `fₛ : N → N'` be a map
> of `A`-modules between two `S⁻¹A`-modules and let `Q` be an `A`-module with localization `S⁻¹Q` at
> `S`. Then `fₛ ⊗_A id_Q` is injective if and only if `fₛ ⊗_{S⁻¹A} id_{S⁻¹Q}` is injective.
>
> Quantifying over `Q`: for a map between `S⁻¹A`-modules — in particular between `(S')⁻¹B`-modules,
> for a multiplicative `S' ⊆ B` with `φ(S) ⊆ S'`, which is the case the source states — universal
> injectivity as a map of `A`-modules and universal injectivity as a map of `S⁻¹A`-modules are the
> same condition.

```lean
public theorem LinearMap.rTensor_injective_iff_extendScalarsOfIsLocalization
    {A : Type*} [CommRing A] (S : Submonoid A) (Aₛ : Type*) [CommRing Aₛ] [Algebra A Aₛ]
    [IsLocalization S Aₛ] {N N' Q Qₛ : Type*}
    [AddCommGroup N] [Module A N] [Module Aₛ N] [IsScalarTower A Aₛ N]
    [AddCommGroup N'] [Module A N'] [Module Aₛ N'] [IsScalarTower A Aₛ N']
    [AddCommGroup Q] [Module A Q] [AddCommGroup Qₛ] [Module A Qₛ] [Module Aₛ Qₛ]
    [IsScalarTower A Aₛ Qₛ] (q : Q →ₗ[A] Qₛ) [IsLocalizedModule S q] (fₛ : N →ₗ[A] N') :
    Function.Injective (fₛ.rTensor Q) ↔
      Function.Injective ((LinearMap.extendScalarsOfIsLocalization S Aₛ fₛ).rTensor Qₛ)
```

## Tag 0AS5, a lemma

[Tag 0AS5](https://stacks.math.columbia.edu/tag/0AS5) in the Stacks Project.

**`Module.Flat.rTensor_injective_iff_injective_mapQ_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L318). The attribute's comment: “`M/IM` is `M ⧸ I • ⊤` and the induced map is `Submodule.mapQ` along `f`; the left-hand side spells out universal injectivity, which `Mathlib` has no name for.”.

> Let `f : M →ₗ[R] M'` be a map of `R`-modules with `M'` flat. Then `f` is universally
> injective, that is `f ⊗ id_Q` is injective for every `R`-module `Q`, if and only if the induced
> map `M/IM → M'/IM'` is injective for every finitely generated ideal `I ⊆ R`.

```lean
public theorem Module.Flat.rTensor_injective_iff_injective_mapQ_smul_top {R : Type u} [CommRing R]
    [Small.{v} R] {M M' : Type v} [AddCommGroup M] [Module R M] [AddCommGroup M'] [Module R M']
    [Module.Flat R M'] (f : M →ₗ[R] M') :
    (∀ (Q : Type v) [AddCommGroup Q] [Module R Q], Function.Injective (f.rTensor Q)) ↔
      ∀ ⦃I : Ideal R⦄, I.FG →
        Function.Injective ((I • ⊤ : Submodule R M).mapQ (I • ⊤ : Submodule R M') f
          (Submodule.smul_top_le_comap_smul_top I f))
```

## Tag 0H9I, a lemma

[Tag 0H9I](https://stacks.math.columbia.edu/tag/0H9I) in the Stacks Project.

**`reflects_injections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 973](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L973). The attribute's comment: “(1)”.

> **Base change along a universally injective ring map reflects injections.**
> If `R → S` is universally injective as a map of `R`-modules and
> `f ⊗_R id_S : M ⊗[R] S → N ⊗[R] S` is injective, then `f` is injective.

```lean
theorem reflects_injections
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : UniversallyInjective (Algebra.linearMap R S))
    {M : Type u} [AddCommGroup M] [Module R M]
    {N : Type u} [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N)
    (hf : Function.Injective (LinearMap.rTensor S f)) :
    Function.Injective f
```

**`reflects_surjections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 988](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L988). The attribute's comment: “(2)”. References: EGA IV (2.2.7), “partial”; EGA IV (2.5.4.1), “more general”.

> **Base change along a universally injective ring map reflects surjections.**
> If `R → S` is universally injective as a map of `R`-modules and
> `f ⊗_R id_S : M ⊗[R] S → N ⊗[R] S` is surjective, then `f` is surjective.

```lean
theorem reflects_surjections
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : UniversallyInjective (Algebra.linearMap R S))
    {M : Type u} [AddCommGroup M] [Module R M]
    {N : Type u} [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N)
    (hf : Function.Surjective (LinearMap.rTensor S f)) :
    Function.Surjective f
```

**`reflects_isomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 1019](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L1019). The attribute's comment: “(3)”.

> **Base change along a universally injective ring map reflects isomorphisms.**
> If `R → S` is universally injective as a map of `R`-modules and
> `f ⊗_R id_S : M ⊗[R] S → N ⊗[R] S` is bijective, then `f` is bijective.

```lean
theorem reflects_isomorphisms
    {R : Type u} [CommRing R] {S : Type u} [CommRing S] [Algebra R S]
    (hRS : UniversallyInjective (Algebra.linearMap R S))
    {M : Type u} [AddCommGroup M] [Module R M]
    {N : Type u} [AddCommGroup N] [Module R N]
    (f : M →ₗ[R] N)
    (hf : Function.Bijective (LinearMap.rTensor S f)) :
    Function.Bijective f
```

## Tag 05CK, a lemma

[Tag 05CK](https://stacks.math.columbia.edu/tag/05CK) in the Stacks Project.

**`faithfullyFlat_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L485). References: EGA 0 (6.5.1), “B faithfully flat”; EGA IV (2.2.8), “affine case”; EGA 0 (6.6.1), “(a)”; SGA 3 VIB (11.14), “necessity”.

> For a faithfully flat ring map `φ : R → S`, the structure map `R → S` viewed as an
> `R`-linear map (`Algebra.linearMap R S`, where `S` is given its `R`-module structure
> via `φ`) is universally injective: for every `R`-module `Q`, the induced map
> `R ⊗_R Q → S ⊗_R Q` is injective.

```lean
theorem faithfullyFlat_universallyInjective
    {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S) (hφ : φ.FaithfullyFlat) :
    haveI := φ.toAlgebra
    UniversallyInjectivePoly (Algebra.linearMap R S)
```

**`faithfullyFlat_comap_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjective.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjective.lean#L525). The attribute's comment: “in particular”. References: EGA 0 (6.6.3), “first part, M = A”; EGA 0 (6.5.1), “B faithfully flat”; EGA 0 (22.4.8), “more general”; EGA 0 (6.5.2), “φ⁻¹(aB) = a”; EGA 0 (6.6.1), “(a) ⇒ φ⁻¹(aB) = a in (d)”; SGA 1 IV (2.6), “(i)”; SGA 3 V (9.1), “partial”.

> For a faithfully flat ring map `φ : R → S` and every ideal `I ⊆ R`, the contraction
> of the extended ideal `I S` back to `R` equals `I`, i.e. `φ⁻¹(I S) = I`.
>
> This is Mathlib's `Ideal.comap_map_eq_self_of_faithfullyFlat`, restated for a bare ring map.

```lean
theorem faithfullyFlat_comap_map_eq
    {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S) (hφ : φ.FaithfullyFlat)
    (I : Ideal R) :
    Ideal.comap φ (Ideal.map φ I) = I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.82, Tag 058H](https://stacks.math.columbia.edu/tag/058H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
