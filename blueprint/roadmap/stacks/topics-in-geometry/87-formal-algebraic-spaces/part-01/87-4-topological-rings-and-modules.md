---
declaration: section
origin: cited
lean: TopologicalModule.Nonuniform.exists_pow_X_smul_mem, TopologicalModule.Nonuniform.not_exists_forall_pow_X_smul_mem, TopologicalModule.Nonuniform.exists_isLinearTopology_not_exists_isOpen_ideal_smul_mem, TopologicalModule.continuousSMul_iff_forall_exists_smul_mem, TopologicalModule.continuousSMul_iff_forall_exists_coset_smul_coset, TopologicalRing.continuous_add_of_hasBasis_addSubgroup, TopologicalRing.exists_isOpen_ideal_map_le, TopologicalRing.closure_eq_iInter_sup_of_hasBasis
statement: formalized
proof: formalized
---

# 87.4 Topological rings and modules

Section 87.4 of the Stacks Project, [Tag 0AMQ](https://stacks.math.columbia.edu/tag/0AMQ). 12 tags here are carried by 41 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AMR, an example

[Tag 0AMR](https://stacks.math.columbia.edu/tag/0AMR) in the Stacks Project.

**`TopologicalModule.Nonuniform.exists_pow_X_smul_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/NonuniformModule.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/NonuniformModule.lean#L128). The attribute's comment: “nonuniform\_module\_example”.

> The pointwise condition of the source: for every `m` and every `x ∈ ⨁_{n ∈ ℕ} k[[t]]` there
> is a `j` with `t ^ j • x ∈ M m`. It holds because `x` has only finitely many nonzero
> coordinates.

```lean
theorem exists_pow_X_smul_mem (m : ℕ) (x : ℕ →₀ PowerSeries k) :
    ∃ j : ℕ, (X : PowerSeries k) ^ j • x ∈ coordinateSubmodule k m
```

**`TopologicalModule.Nonuniform.not_exists_forall_pow_X_smul_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/NonuniformModule.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/NonuniformModule.lean#L194). The attribute's comment: “nonuniform\_module\_example”.

> The uniform condition fails: for `m ≥ 1` there is no `j` with `t ^ j • M ⊆ M m`.

```lean
theorem not_exists_forall_pow_X_smul_mem {m : ℕ} (hm : 1 ≤ m) :
    ¬ ∃ j : ℕ, ∀ x : ℕ →₀ PowerSeries k,
      (X : PowerSeries k) ^ j • x ∈ coordinateSubmodule k m
```

**`TopologicalModule.Nonuniform.exists_isLinearTopology_not_exists_isOpen_ideal_smul_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/NonuniformModule.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/NonuniformModule.lean#L217). The attribute's comment: “nonuniform\_module\_example”.

> The source's example, as an existence statement: over `R = k[[t]]` with the `t`-adic
> topology there is a linearly topologized `R`-module `M`, with a fundamental system `N` of open
> submodules, for which no open ideal `I` of `R` satisfies `I • M ⊆ N 1`.

```lean
theorem exists_isLinearTopology_not_exists_isOpen_ideal_smul_mem :
    ∃ (τ : TopologicalSpace (ℕ →₀ PowerSeries k))
      (N : ℕ → Submodule (PowerSeries k) (ℕ →₀ PowerSeries k)),
      (@nhds _ τ 0).HasBasis (fun _ : ℕ ↦ True) (fun m ↦ (N m : Set (ℕ →₀ PowerSeries k))) ∧
      @IsTopologicalAddGroup _ τ _ ∧
      @ContinuousSMul (PowerSeries k) _ _ _ τ ∧
      @IsLinearTopology (PowerSeries k) _ _ _ _ τ ∧
      ¬ ∃ I : Ideal (PowerSeries k), IsOpen (I : Set (PowerSeries k)) ∧
          ∀ f ∈ I, ∀ x : ℕ →₀ PowerSeries k, f • x ∈ N 1
```

**`TopologicalModule.continuousSMul_iff_forall_exists_smul_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/ScalarContinuity.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/ScalarContinuity.lean#L53). The attribute's comment: “scalar\_continuity\_criterion”.

> **Tag 0AMR.** Let `I` be a fundamental system of open ideals of a topological ring `R` and
> let `N` be a fundamental system of open submodules of an `R`-module `M`. Then scalar
> multiplication `R × M → M` is continuous exactly when `I λ • x ⊆ N μ` for some `λ`, for every
> `x : M` and every `μ`.

```lean
theorem continuousSMul_iff_forall_exists_smul_mem
    (hI : (𝓝 (0 : R)).HasBasis (fun _ : ι ↦ True) fun l ↦ (I l : Set R))
    (hN : (𝓝 (0 : M)).HasBasis (fun _ : κ ↦ True) fun m ↦ (N m : Set M)) :
    ContinuousSMul R M ↔ ∀ (x : M) (μ : κ), ∃ l : ι, ∀ f ∈ I l, f • x ∈ N μ
```

**`TopologicalModule.continuousSMul_iff_forall_exists_coset_smul_coset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/ScalarContinuity.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/ScalarContinuity.lean#L85). The attribute's comment: “scalar\_continuity\_criterion”.

> **Tag 0AMR.** The displayed form of the continuity of `R × M → M`: for all `f`, `x` and `μ`
> there are `λ` and `ν` with `(f + I λ) • (x + N ν) ⊆ f • x + N μ`. The source deduces it from
> `TopologicalModule.continuousSMul_iff_forall_exists_smul_mem` using that `f • N ν + I λ • N ν ⊆
> N μ` whenever `N ν ⊆ N μ`; here `ν = μ` always works.

```lean
theorem continuousSMul_iff_forall_exists_coset_smul_coset
    (hI : (𝓝 (0 : R)).HasBasis (fun _ : ι ↦ True) fun l ↦ (I l : Set R))
    (hN : (𝓝 (0 : M)).HasBasis (fun _ : κ ↦ True) fun m ↦ (N m : Set M)) :
    ContinuousSMul R M ↔ ∀ (f : R) (x : M) (μ : κ), ∃ (l : ι) (ν : κ),
      ∀ g ∈ I l, ∀ y ∈ N ν, (f + g) • (x + y) - f • x ∈ N μ
```

**`TopologicalRing.continuous_add_of_hasBasis_addSubgroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L166). The attribute's comment: “addition\_continuous”.

> Addition is continuous when translates of additive subgroups form a neighborhood basis.

```lean
public theorem continuous_add_of_hasBasis_addSubgroup
    {M ι : Type*} [AddCommGroup M] [TopologicalSpace M]
    (Mμ : ι → AddSubgroup M)
    (hbasis : ∀ x : M, (nhds x).HasBasis (fun _ : ι => True)
      (fun μ => (fun y : M => x + y) '' (Mμ μ : Set M))) :
    Continuous (fun p : M × M => p.1 + p.2)
```

**`TopologicalRing.exists_isOpen_ideal_map_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L192). The attribute's comment: “continuous\_ring\_map\_open\_ideal”. References: EGA 0 (19.0.3), “𝔍B ⊂ 𝔎 clause”; EGA 0 (7.7.5), “existence of open J”.

> Every open ideal in the target of a continuous ring homomorphism contains the extension
> of an open ideal from the source.

```lean
public theorem exists_isOpen_ideal_map_le {R S : Type*} [CommRing R] [CommRing S]
    [TopologicalSpace R] [TopologicalSpace S] (f : R →+* S) (hf : Continuous f)
    (J : Ideal S) (hJ : IsOpen (J : Set S)) :
    ∃ I : Ideal R, IsOpen (I : Set R) ∧ Ideal.map f I ≤ J
```

## Tag 0AMS, a lemma

[Tag 0AMS](https://stacks.math.columbia.edu/tag/0AMS) in the Stacks Project.

**`TopologicalRing.closure_eq_iInter_sup_of_hasBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 562](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L562).

> **Stacks Project, Tag 0AMS.** Let `M` be a linearly topologized `R`-module and let
> `L i`, `i : ι`, be a fundamental system of open submodules of `M`. The closure of a submodule
> `N ⊆ M` is the intersection of the submodules `N + L i`.

```lean
public theorem closure_eq_iInter_sup_of_hasBasis {ι : Sort*} (L : ι → Submodule R M)
    (hopen : ∀ i, IsOpen ((L i : Set M)))
    (hbasis : (𝓝 (0 : M)).HasBasis (fun _ : ι ↦ True) fun i ↦ ((L i : Set M)))
    (N : Submodule R M) :
    closure (N : Set M) = ⋂ i, ((N ⊔ L i : Submodule R M) : Set M)
```

**`TopologicalRing.topologicalClosure_eq_iInf_sup_of_hasBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L577). The attribute's comment: “the same identity read as an equality of submodules”.

> **Stacks Project, Tag 0AMS**, as an equality of submodules: the topological closure of a
> submodule `N` is the infimum of the submodules `N + L i` over a fundamental system `L i` of open
> submodules.

```lean
public theorem topologicalClosure_eq_iInf_sup_of_hasBasis [ContinuousConstSMul R M]
    {ι : Sort*} (L : ι → Submodule R M)
    (hopen : ∀ i, IsOpen ((L i : Set M)))
    (hbasis : (𝓝 (0 : M)).HasBasis (fun _ : ι ↦ True) fun i ↦ ((L i : Set M)))
    (N : Submodule R M) :
    N.topologicalClosure = ⨅ i, (N ⊔ L i : Submodule R M)
```

## Tag 0ARZ, a lemma

[Tag 0ARZ](https://stacks.math.columbia.edu/tag/0ARZ) in the Stacks Project.

**`TopologicalRing.completionSubtype_injective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L143). The attribute's comment: “part (1), injectivity”.

> **Stacks Project, Tag 0ARZ, part (1).** The map from the completion of a
> submodule to the completion of the ambient linearly topologized module is
> injective.

```lean
public lemma completionSubtype_injective (N : Submodule R M) :
    Function.Injective (completionSubtype N)
```

**`TopologicalRing.exact_completionSubtype_completionQuotient`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L247). The attribute's comment: “part (1), exactness”.

> **Stacks Project, Tag 0ARZ, part (1).** The image of the completed
> submodule is the kernel of the map from the completed module to the completion
> of its quotient.

```lean
public lemma exact_completionSubtype_completionQuotient (N : Submodule R M) :
    range (completionSubtype N) =
      {x | completionQuotient N x = (0 : M ⧸ N)}
```

**`TopologicalRing.range_completionSubtype_eq_closure`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L275). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0ARZ, part (2).** In the completion of a linearly
> topologized module, the image of the completion of a submodule is precisely the
> closure of the image of that submodule.

```lean
public lemma range_completionSubtype_eq_closure (N : Submodule R M) :
    range (completionSubtype N) =
      closure (range fun x : N ↦ (x.1 : TopologicalCompletion M))
```

## Tag 0AMT, a lemma

[Tag 0AMT](https://stacks.math.columbia.edu/tag/0AMT) in the Stacks Project.

**`TopologicalRing.t2Space_quotient_of_isClosed`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 596](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L596). The attribute's comment: “the quotient is separated”.

> **Stacks Project, Tag 0AMT.** The quotient of a linearly topologized module by a closed
> submodule is separated; this is the Hausdorff half of the completeness of `M ⧸ N`.

```lean
public lemma t2Space_quotient_of_isClosed {R : Type u} {M : Type v}
    [CommRing R] [TopologicalSpace R] [IsTopologicalRing R]
    [AddCommGroup M] [Module R M] [TopologicalSpace M] [IsTopologicalAddGroup M]
    [IsLinearTopology R M] (N : Submodule R M) (hN : IsClosed (N : Set M)) :
    T2Space (M ⧸ N)
```

**`TopologicalRing.completeSpace_quotient_of_isCountablyGenerated`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 608](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L608). The attribute's comment: “the quotient is complete”.

> **Stacks Project, Tag 0AMT.** The quotient of a complete, linearly topologized module with a
> countable fundamental system of neighbourhoods of zero by a submodule is itself complete for the
> canonical uniformity of a topological additive group.

```lean
public lemma completeSpace_quotient_of_isCountablyGenerated {R : Type u} {M : Type v}
    [CommRing R] [TopologicalSpace R] [IsTopologicalRing R]
    [AddCommGroup M] [Module R M] [TopologicalSpace M] [IsTopologicalAddGroup M]
    [IsLinearTopology R M] (N : Submodule R M)
    (hM : @CompleteSpace M (IsTopologicalAddGroup.rightUniformSpace M))
    (hcount : (nhds (0 : M)).IsCountablyGenerated) :
    @CompleteSpace (M ⧸ N) (IsTopologicalAddGroup.rightUniformSpace (M ⧸ N))
```

Declarations registered for the tag:

- [`Submodule.isOpenMap_mkQ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.isOpenMap_mkQ#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L625) (StacksFrontier): “the map to the quotient is open”.

## Tag 0AS0, a lemma

[Tag 0AS0](https://stacks.math.columbia.edu/tag/0AS0) in the Stacks Project.

**`TopologicalRing.completionQuotient_surjective_of_isCountablyGenerated`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L425). The attribute's comment: “part (1), surjectivity”.

> **Stacks Project, Tag 0AS0, part (1).** For a linearly topologized module
> with a countable fundamental system of neighborhoods of zero, the canonical
> map from its completion to the completion of a quotient is surjective.

```lean
public lemma completionQuotient_surjective_of_isCountablyGenerated
    (N : Submodule R M) (hM : (nhds (0 : M)).IsCountablyGenerated) :
    Function.Surjective (TopologicalRing.completionQuotient N)
```

**`TopologicalRing.completionQuotient_isOpenMap_of_isCountablyGenerated`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L435). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 0AS0, part (3).** For a linearly topologized module
> with a countable fundamental system of neighborhoods of zero, the canonical
> map from its completion to the completion of a quotient is open.

```lean
public lemma completionQuotient_isOpenMap_of_isCountablyGenerated
    (N : Submodule R M) (hM : (nhds (0 : M)).IsCountablyGenerated) :
    IsOpenMap (TopologicalRing.completionQuotient N)
```

Declarations registered for the tag:

- [`TopologicalRing.completionSubtype_injective`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L143), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L411) (StacksFrontier): “part (1), injectivity”.
- [`TopologicalRing.exact_completionSubtype_completionQuotient`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L247), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L414) (StacksFrontier): “part (1), exactness at the middle term”.
- [`TopologicalRing.range_completionSubtype_eq_closure`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L275), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L417) (StacksFrontier): “part (2)”.

## Tag 0F1S, a lemma

[Tag 0F1S](https://stacks.math.columbia.edu/tag/0F1S) in the Stacks Project.

**`TopologicalRing.exists_isOpen_adic_submodule_completionAlong`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean#L439). The attribute's comment: “open\_adic\_completion”.

> The completion of a module containing an open `I`-adic submodule again contains an open
> submodule with the `I`-adic topology.

```lean
public lemma exists_isOpen_adic_submodule_completionAlong
    {R : Type*} [CommRing R] [TopologicalSpace R] [IsTopologicalRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [TopologicalSpace M]
    [IsTopologicalAddGroup M] [ContinuousSMul R M]
    (I : Ideal R) (hI : I.FG) (N : Submodule R M) (_hN : IsOpen (N : Set M))
    (_hAdic : (𝓝 (0 : N)).HasBasis (fun _ : ℕ ↦ True)
      (fun n ↦ ((I ^ n • ⊤ : Submodule R N) : Set N))) :
    ∃ P : Submodule R (TopologicalRing.CompletionAlong I N),
      @IsOpen (TopologicalRing.CompletionAlong I N)
          (TopologicalRing.CompletionAlong.limitTopology I N) (P : Set _) ∧
        TopologicalSpace.induced
          (fun p : P => (p : TopologicalRing.CompletionAlong I N))
          (TopologicalRing.CompletionAlong.limitTopology I N) = I.adicModuleTopology P
```

**`TopologicalRing.CompletionAlong.quotPowEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean, line 674](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean#L674). The attribute's comment: “completion\_mod\_ideal\_power”.

> The second conclusion of Tag 0F1S at the level of the filtration `I ^ n N`:
> `M^ / I ^ n M^ = M / I ^ n M`.

```lean
public noncomputable def quotPowEquiv (I : Ideal R) (hI : I.FG) (N : Submodule R M) (n : ℕ) :
    ((CompletionAlong I N) ⧸ (I ^ n • ⊤ : Submodule R (CompletionAlong I N))) ≃ₗ[R]
      (M ⧸ (I ^ n • ⊤ : Submodule R M))
```

**`TopologicalRing.exists_isOpen_adic_submodule_completionOverOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean, line 874](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean#L874). The attribute's comment: “open\_adic\_completion”.

> Tag 0F1S, first conclusion, over the completion of `M` taken over all of its open
> submodules: `M^` has an open submodule whose topology is `I`-adic.

```lean
public lemma exists_isOpen_adic_submodule_completionOverOpen (I : Ideal R) (hI : I.FG)
    (N : Submodule R M) (hN : IsOpen (N : Set M))
    (hAdic : (𝓝 (0 : N)).HasBasis (fun _ : ℕ ↦ True)
      (fun n ↦ ((I ^ n • ⊤ : Submodule R N) : Set N))) :
    ∃ P : Submodule R (CompletionOverOpen R M),
      @IsOpen (CompletionOverOpen R M) (CompletionOverOpen.limitTopology R M) (P : Set _) ∧
        TopologicalSpace.induced (fun p : P ↦ (p : CompletionOverOpen R M))
          (CompletionOverOpen.limitTopology R M) = I.adicModuleTopology P
```

**`TopologicalRing.completionOverOpenQuotPowEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean, line 914](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionAlong.lean#L914). The attribute's comment: “completion\_mod\_ideal\_power”.

> Tag 0F1S, second conclusion, over the completion of `M` taken over all of its open
> submodules: `M^ / I ^ n M^ = M / I ^ n M` for every `n`, in particular for every `n ≥ 1`.

```lean
public noncomputable def completionOverOpenQuotPowEquiv (I : Ideal R) (hI : I.FG)
    (N : Submodule R M) (hN : IsOpen (N : Set M))
    (hAdic : (𝓝 (0 : N)).HasBasis (fun _ : ℕ ↦ True)
      (fun n ↦ ((I ^ n • ⊤ : Submodule R N) : Set N))) (n : ℕ) :
    ((CompletionOverOpen R M) ⧸ (I ^ n • ⊤ : Submodule R (CompletionOverOpen R M))) ≃ₗ[R]
      (M ⧸ (I ^ n • ⊤ : Submodule R M))
```

## Tag 0AMU, a definition

[Tag 0AMU](https://stacks.math.columbia.edu/tag/0AMU) in the Stacks Project.

**`TopologicalRing.tensorProductTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean#L210). The attribute's comment: “tensor product”. References: EGA 0 (20.4.1).

> The topology on the usual tensor product whose fundamental open
> submodules are the images of `P ⊗[R] N + M ⊗[R] Q` for open `P` and `Q`.

```lean
def tensorProductTopology : TopologicalSpace (M ⊗[R] N)
```

**`TopologicalRing.CompletedTensorProduct`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean#L300). The attribute's comment: “completed tensor product”. References: EGA 0 (7.7.2), “completed tensor product”; EGA 0 (7.7.1); EGA 0 (7.7.5), “completed tensor product”; SGA 3 VIIB (0.3), “def of L⊗̂M”; SGA 3 VIIB (0.5.A), “def of M⊗̂\_k N”.

> The completed tensor product of two topologized modules: the uniform
> completion of their tensor product with its tensor product topology.

```lean
abbrev CompletedTensorProduct
```

**`TopologicalRing.quotientTensorProductLimitIdentification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean, line 576](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean#L576). The attribute's comment: “second inverse-limit identification”. References: EGA 0 (7.7.2), “(M/V)⊗(N/W) identif.”; EGA 0 (7.7.1), “lim M/V ⊗ N/W”; EGA 0 (7.7.5), “lim M/Mμ ⊗ N/Nν”; SGA 3 VIIB (0.3), “lim (L/L')⊗(M/M')”.

> The componentwise quotient-tensor-quotient equivalences identify the two
> inverse limits in Tag 0AMU.  The specification records that the map is exactly
> `TensorProduct.quotientTensorQuotientEquiv` in every component.

```lean
noncomputable def quotientTensorProductLimitIdentification :
    { e : QuotientTensorProductLimit (R := R) (M := M) (N := N) ≃L[R]
        TensorProductQuotientLimit (R := R) (M := M) (N := N) //
      ∀ x : QuotientTensorProductLimit (R := R) (M := M) (N := N),
        ∀ i : TensorProductSubmoduleIndex (R := R) (M := M) (N := N),
          ((e x : TensorProductQuotientLimit (R := R) (M := M) (N := N)) :
              ∀ j : TensorProductSubmoduleIndex (R := R) (M := M) (N := N),
                TensorProductQuotient j) i =
            TensorProduct.quotientTensorQuotientEquiv i.1.1 i.2.1
              (((x : QuotientTensorProductLimit (R := R) (M := M) (N := N)) :
                  ∀ j : TensorProductSubmoduleIndex (R := R) (M := M) (N := N),
                    QuotientTensorProduct j) i) }
```

**`TopologicalRing.exists_completedTensorProductEquivQuotientLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean, line 843](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean#L843). The attribute's comment: “first inverse-limit identification”. References: EGA 0 (7.7.2), “lim (M⊗N)/(...) identif.”; EGA 0 (7.7.1), “limit identification”; EGA 0 (7.7.5), “lim (M⊗N)/(Mμ⊗N+M⊗Nν)”; SGA 3 VIIB (0.3), “P = lim quotients”.

> The completion is canonically topologically linearly isomorphic to the
> inverse limit of its discrete quotients. Every component of the identification
> extends the usual quotient map.

```lean
theorem exists_completedTensorProductEquivQuotientLimit :
    ∃ e : CompletedTensorProduct (R := R) (M := M) (N := N) ≃L[R]
        TensorProductQuotientLimit (R := R) (M := M) (N := N),
      ∀ z : M ⊗[R] N,
        ∀ i : TensorProductSubmoduleIndex (R := R) (M := M) (N := N),
          ((e (↑z : CompletedTensorProduct (R := R) (M := M) (N := N)) :
              TensorProductQuotientLimit (R := R) (M := M) (N := N)) :
              ∀ j : TensorProductSubmoduleIndex (R := R) (M := M) (N := N),
                TensorProductQuotient j) i = Submodule.Quotient.mk z
```

## Tag 0AMV, a definition

[Tag 0AMV](https://stacks.math.columbia.edu/tag/0AMV) in the Stacks Project.

**`TopologicalRing.IsWeakIdealOfDefinition`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L72). The attribute's comment: “part (2)”.

> A weak ideal of definition is an open ideal consisting entirely of
> topologically nilpotent elements.

```lean
abbrev IsWeakIdealOfDefinition {R : Type*} [CommRing R] [TopologicalSpace R]
    (I : Ideal R) : Prop
```

**`TopologicalRing.IsWeaklyPreAdmissible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L79). The attribute's comment: “part (3)”.

> A topological ring is weakly pre-admissible if it has a weak ideal of
> definition.

```lean
abbrev IsWeaklyPreAdmissible (R : Type*) [CommRing R] [TopologicalSpace R] : Prop
```

**`TopologicalRing.IsWeaklyAdmissible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L86). The attribute's comment: “part (4)”.

> A linearly topologized ring is weakly admissible if it is weakly
> pre-admissible, complete, and separated. Completeness uses the canonical
> uniformity of its additive topological group.

```lean
abbrev IsWeaklyAdmissible (R : Type*) [CommRing R] [TopologicalSpace R]
    [IsTopologicalRing R] [IsLinearTopology R R] : Prop
```

Declarations registered for the tag:

- [`IsTopologicallyNilpotent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsTopologicallyNilpotent#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L65) (StacksFrontier): “part (1)”. References: EGA 0 (7.1.1); SGA 3 VIIB (0.1.2).

## Tag 0DCZ, a lemma

[Tag 0DCZ](https://stacks.math.columbia.edu/tag/0DCZ) in the Stacks Project.

**`TopologicalRing.henselianPair_of_isWeaklyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/Completion.lean#L502). References: EGA 0 (7.1.10).

> **Stacks Project, Tag 0DCZ.** A weak ideal of definition in a weakly
> admissible topological ring forms a henselian pair with the ring.

```lean
theorem henselianPair_of_isWeaklyAdmissible
    (A : Type*) [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] (hA : TopologicalRing.IsWeaklyAdmissible A)
    (I : Ideal A) (hI : TopologicalRing.IsWeakIdealOfDefinition I) :
    HenselianPair A I
```

## Tag 0AMW, a lemma

[Tag 0AMW](https://stacks.math.columbia.edu/tag/0AMW) in the Stacks Project.

**`TopologicalRing.isClosed_topologicalNilradical`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L112). The attribute's comment: “closedness”.

> In a linearly topologized commutative ring, the ideal of topologically nilpotent
> elements is closed.

```lean
public lemma isClosed_topologicalNilradical {B : Type*} [CommRing B] [TopologicalSpace B]
    [IsTopologicalRing B] [IsLinearTopology B B] :
    IsClosed (topologicalNilradical B : Set B)
```

**`TopologicalRing.topologicalNilradical_isRadical`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L130). The attribute's comment: “radicality”.

> In a linearly topologized commutative ring, the ideal of topologically nilpotent
> elements is radical.

```lean
public lemma topologicalNilradical_isRadical {B : Type*} [CommRing B] [TopologicalSpace B]
    [IsLinearTopology B B] :
    (topologicalNilradical B).IsRadical
```

**`TopologicalRing.closure_map_le_topologicalNilradical`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L150). The attribute's comment: “part (2)”. References: SGA 3 VIIB (0.1.3), “r(A) ↦ r(B)”.

> Extending an ideal consisting of topologically nilpotent elements along a continuous
> ring homomorphism and taking its closure still gives an ideal consisting of topologically
> nilpotent elements.

```lean
public lemma closure_map_le_topologicalNilradical
    {A B : Type*} [CommRing A] [TopologicalSpace A] [CommRing B] [TopologicalSpace B]
    [IsLinearTopology A A] [IsTopologicalRing B] [IsLinearTopology B B]
    (φ : A →+* B) (hφ : Continuous φ)
    (I : Ideal A) (hI : I ≤ topologicalNilradical A) :
    Ideal.closure (I.map φ) ≤ topologicalNilradical B
```

Declarations registered for the tag:

- [`topologicalNilradical`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=topologicalNilradical#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L97) (StacksFrontier): “the ideal”. References: EGA 0 (7.1.3); EGA 0 (7.1.6).
- [`IsTopologicallyNilpotent.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsTopologicallyNilpotent.map#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L143) (StacksFrontier): “part (1)”. References: SGA 3 VIIB (0.1.3), “more general”.

## Tag 0AMZ, a lemma

[Tag 0AMZ](https://stacks.math.columbia.edu/tag/0AMZ) in the Stacks Project.

**`TopologicalRing.closure_map_eq_ker_completedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean, line 1149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct.lean#L1149).

> The closure of the extension of `I` to `B` is the kernel of the canonical map
> `B → B ⊗̂[A] (A ⧸ I)`.

```lean
public theorem closure_map_eq_ker_completedTensorProduct
    {A B : Type*} [CommRing A] [CommRing B] [Algebra A B]
    [TopologicalSpace A] [TopologicalSpace B]
    [IsTopologicalRing A] [IsTopologicalRing B]
    [IsLinearTopology A A] [IsLinearTopology B B]
    (h : Continuous (algebraMap A B)) (I : Ideal A) :
    (Ideal.closure (I.map (algebraMap A B)) : Set B) =
      {b : B | (↑(b ⊗ₜ[A] (1 : A ⧸ I)) :
        TopologicalRing.CompletedTensorProduct (R := A) (M := B) (N := A ⧸ I)) = 0}
```

## Tag 0GB4, a lemma

[Tag 0GB4](https://stacks.math.columbia.edu/tag/0GB4) in the Stacks Project.

**`TopologicalRing.isAdicStar_completedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarBaseChange.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AdicStarBaseChange.lean#L84). The attribute's comment: “the adic\_finite clauses, assembled as membership in WAdm^\{adic*}”.

> The completed tensor product of two objects of `WAdm^{adic*}` over a third is again an
> object of `WAdm^{adic*}`: it is adic and it has a finitely generated ideal of definition.

```lean
theorem isAdicStar_completedTensorProduct {A₀ A₁ A : Type u}
    [CommRing A₀] [TopologicalSpace A₀] [IsTopologicalRing A₀] [IsLinearTopology A₀ A₀]
    [CommRing A₁] [TopologicalSpace A₁] [IsTopologicalRing A₁] [IsLinearTopology A₁ A₁]
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [Algebra A₀ A₁] [Algebra A₀ A]
    (h₁ : IsAdicStar A₁) (hA : IsAdicStar A)
    (hc₁ : Continuous (algebraMap A₀ A₁)) (hcA : Continuous (algebraMap A₀ A)) :
    IsAdicStar (CompletedTensorProduct (R := A₀) (M := A₁) (N := A))
```

**`TopologicalRing.isCountablyWeaklyAdmissible_completedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedBaseChange.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedBaseChange.lean#L73). The attribute's comment: “the weakly\_admissible and countable\_basis clauses, assembled as membership in WAdm^count”.

> **Lemma 87.4.12 (Stacks 0GB4) on the class `WAdm^count`.** The completed tensor product of
> two countably indexed weakly admissible topological rings over a third is again one: it is
> weakly admissible and its fundamental system of neighbourhoods of zero is countable.
>
> This is the well definedness that the notion of stability under base change of Stacks 0GBC
> needs, and it is what the chart argument of Stacks 0GBD needs of the class beyond the
> stability clause itself, in order to transport `P` along the isomorphism identifying the chart
> ring of a fibre product of charts with the completed tensor product.

```lean
public theorem isCountablyWeaklyAdmissible_completedTensorProduct {A₀ A₁ A : Type u}
    [CommRing A₀] [TopologicalSpace A₀] [IsTopologicalRing A₀] [IsLinearTopology A₀ A₀]
    [CommRing A₁] [TopologicalSpace A₁] [IsTopologicalRing A₁] [IsLinearTopology A₁ A₁]
    [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [Algebra A₀ A₁] [Algebra A₀ A]
    (h₁ : IsCountablyWeaklyAdmissible A₁) (hA : IsCountablyWeaklyAdmissible A) :
    IsCountablyWeaklyAdmissible
      (CompletedTensorProduct (R := A₀) (M := A₁) (N := A))
```

**`TopologicalRing.completedTensorProduct_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L366). The attribute's comment: “adic\_finite”.

> The completed tensor product of two pre-adic, linearly topologized algebras with finitely
> generated ideals of definition is adic.

```lean
public theorem completedTensorProduct_isAdic
    {B A C : Type*} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C] [Algebra B A] [Algebra B C]
    (_hBA : Continuous (algebraMap B A)) (_hBC : Continuous (algebraMap B C))
    (_hA : TopologicalRing.IsPreAdic A)
    (_hAfg : ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧ I.FG)
    (_hC : TopologicalRing.IsPreAdic C)
    (_hCfg : ∃ J : Ideal C, TopologicalRing.IsIdealOfDefinition J ∧ J.FG) :
    TopologicalRing.IsAdic (CompletedTensorProduct (R := B) (M := A) (N := C))
```

**`TopologicalRing.exists_fg_ideal_of_definition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L385). The attribute's comment: “adic\_finite”.

> The completed tensor product has a finitely generated ideal of definition.

```lean
public theorem exists_fg_ideal_of_definition
    {B A C : Type*} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
    [IsLinearTopology B B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
    [IsLinearTopology C C] [Algebra B A] [Algebra B C]
    (_hBA : Continuous (algebraMap B A)) (_hBC : Continuous (algebraMap B C))
    (_hA : TopologicalRing.IsPreAdic A)
    (_hAfg : ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧ I.FG)
    (_hC : TopologicalRing.IsPreAdic C)
    (_hCfg : ∃ J : Ideal C, TopologicalRing.IsIdealOfDefinition J ∧ J.FG) :
    ∃ K : Ideal (CompletedTensorProduct (R := B) (M := A) (N := C)),
      K.FG ∧ TopologicalRing.IsIdealOfDefinition K
```

**`TopologicalRing.completedTensorProduct_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean, line 657](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L657). The attribute's comment: “adic\_noetherian”.

> If the induced quotient map is of finite type, the completed tensor product
> of pre-adic Noetherian algebras is Noetherian.

```lean
public theorem completedTensorProduct_isNoetherianRing
    {B A C : Type*} [CommRing B] [CommRing A] [CommRing C]
    [Algebra B A] [Algebra B C]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    [IsNoetherianRing A] [IsNoetherianRing C]
    (hA : TopologicalRing.IsPreAdic A) (hC : TopologicalRing.IsPreAdic C)
    (hFinite : ∃ h : topologicalNilradical B ≤
        (topologicalNilradical A).comap (algebraMap B A),
      (Ideal.quotientMap (topologicalNilradical A) (algebraMap B A) h).FiniteType) :
    IsNoetherianRing (CompletedTensorProduct (R := B) (M := A) (N := C))
```

**`TopologicalRing.completedTensorProduct_isAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean, line 815](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L815). The attribute's comment: “admissible”. References: EGA 0 (7.7.7), “admissibility”.

> The completed tensor product of pre-admissible linearly topologized
> algebras is admissible.

```lean
public theorem completedTensorProduct_isAdmissible
    {B A C : Type*} [CommRing B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing C] [TopologicalSpace C]
    [IsTopologicalRing C] [IsLinearTopology C C]
    [Algebra B A] [Algebra B C]
    (hA : TopologicalRing.IsPreAdmissible A)
    (hC : TopologicalRing.IsPreAdmissible C) :
    TopologicalRing.IsAdmissible
      (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C))
```

**`TopologicalRing.isCountablyGenerated_nhds_zero_completedTensorProduct`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean, line 922](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L922). The attribute's comment: “countable\_basis”.

> The completed tensor product of two linearly topologized rings with
> countable fundamental systems of open ideals has a countable fundamental
> system of open ideals.

```lean
public lemma isCountablyGenerated_nhds_zero_completedTensorProduct
    {B A C : Type*} [CommRing B] [CommRing A] [CommRing C]
    [Algebra B A] [Algebra B C]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    (hA : (nhds (0 : A)).IsCountablyGenerated)
    (hC : (nhds (0 : C)).IsCountablyGenerated) :
    (nhds
      (0 : TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C))).IsCountablyGenerated
```

**`TopologicalRing.completedTensorProduct_isWeaklyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean, line 952](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/Adic.lean#L952). The attribute's comment: “weakly\_admissible”.

> The completed tensor product of two weakly pre-admissible linearly
> topologized rings is weakly admissible.

```lean
public theorem completedTensorProduct_isWeaklyAdmissible
    {B A C : Type*} [CommRing B] [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] [CommRing C] [TopologicalSpace C]
    [IsTopologicalRing C] [IsLinearTopology C C]
    [Algebra B A] [Algebra B C]
    (hA : TopologicalRing.IsWeaklyPreAdmissible A)
    (hC : TopologicalRing.IsWeaklyPreAdmissible C) :
    TopologicalRing.IsWeaklyAdmissible
      (TopologicalRing.CompletedTensorProduct (R := B) (M := A) (N := C))
```

**`TopologicalRing.projectionKernel_isWeakIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/WeakIdeal.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletedTensorProduct/WeakIdeal.lean#L157). The attribute's comment: “the projection kernels as weak ideals of definition”.

> **The projection kernel cut out by two weak ideals of definition is a weak ideal of
> definition of the completed tensor product.** It is open by
> `TopologicalRing.isOpen_projectionKernel`, and it consists of topologically nilpotent elements
> because it is the closure of the sum of the two extended ideals.

```lean
public theorem projectionKernel_isWeakIdealOfDefinition (i : ι) (j : κ)
    (hI : TopologicalRing.IsWeakIdealOfDefinition (I i))
    (hJ : TopologicalRing.IsWeakIdealOfDefinition (J j)) :
    TopologicalRing.IsWeakIdealOfDefinition
      (projectionKernel (B := B) I J bI bJ i j)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.4, Tag 0AMQ](https://stacks.math.columbia.edu/tag/0AMQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
