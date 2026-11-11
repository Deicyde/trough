---
declaration: section
origin: cited
lean: LinearMap.IsDifferentialOperatorOfOrderLE, isDiffOpOfOrder_comp, LinearMap.exists_universal_isDifferentialOperatorOfOrderLE, LinearMap.IsUniversalDifferentialOperatorOfOrderLE, diff1EquivDerProd, LinearMap.IsDifferentialOperatorOfOrderLE.exists_shortExact_principalParts, LinearMap.IsUniversalDifferentialOperatorOfOrderLE.isBaseChange, LinearMap.isUniversalDifferentialOperatorOfOrderLE_mkQ_comp_mk_one
statement: formalized
proof: formalized
---

# 10.133 Finite order differential operators

Section 10.133 of the Stacks Project, [Tag 09CH](https://stacks.math.columbia.edu/tag/09CH). 12 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09CI, a definition

[Tag 09CI](https://stacks.math.columbia.edu/tag/09CI) in the Stacks Project.

**`LinearMap.IsDifferentialOperatorOfOrderLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/Defs.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/Defs.lean#L110). The attribute's comment: “The source's `k` bounds the order: `Diff⁰ ⊆ Diff¹ ⊆ …`, whence `LE` in the name. The commutator `m ↦ D (g • m) - g • D m` is the difference of the two composites of `D` with `Algebra.lsmul R R _ g`, multiplication by `g`. The `S`-module `Diffᵏ_{S/R}(M, N)` of the paragraph following the definition is a separate statement. See the module docstring.”. References: EGA IV (16.8.1), “affine (module) case”; SGA 3 VIIA (1.4), “affine case”; SGA 6 II (AppII.1.2.2), “Diff^n, affine case”; SGA 3 VIIA (1.1.1), “partial”.

> Let `R → S` be a ring map, let `M` and `N` be `S`-modules, and let `k : ℕ`.
> `D.IsDifferentialOperatorOfOrderLE S k` says that the `R`-linear map `D : M → N` is a
> *differential operator of order at most `k`* relative to `R → S`. By induction on `k`: order at
> most `0` means `S`-linear, and order at most `k + 1` means that for every `g : S` the commutator
> `m ↦ D (g • m) - g • D m` is a differential operator of order at most `k`.

```lean
public def IsDifferentialOperatorOfOrderLE (S : Type*) [Semiring S] [Algebra R S] [Module S M]
    [IsScalarTower R S M] [Module S N] [IsScalarTower R S N] : ℕ → (M →ₗ[R] N) → Prop
```

## Tag 09CJ, a lemma

[Tag 09CJ](https://stacks.math.columbia.edu/tag/09CJ) in the Stacks Project.

**`isDiffOpOfOrder_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/Defs.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/Defs.lean#L458). References: EGA IV (16.8.9), “affine case”; SGA 3 VIIA (1.2), “affine, deviations of id”; SGA 3 VIIA (1.4), “partial”.

> The composition of a differential operator of order `k` with one of order `k'` is a
> differential operator of order `k + k'`.

```lean
theorem isDiffOpOfOrder_comp
    {L : Type*} [AddCommGroup L] [Module S L] [Module R L] [IsScalarTower R S L]
    (k k' : ℕ) (D : L →ₗ[R] M) (D' : M →ₗ[R] N)
    (hD : IsDiffOpOfOrder S k D) (hD' : IsDiffOpOfOrder S k' D') :
    IsDiffOpOfOrder S (k + k') (D'.comp D)
```

## Tag 09CK, a lemma

[Tag 09CK](https://stacks.math.columbia.edu/tag/09CK) in the Stacks Project.

**`LinearMap.exists_universal_isDifferentialOperatorOfOrderLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/PrincipalParts.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/PrincipalParts.lean#L335). The attribute's comment: “Stated in the universal-object form of the paragraph following the lemma: the isomorphism `Diffᵏ_{S/R}(M, N) = Hom_S(Pᵏ_{S/R}(M), N)` is the map `α ↦ α ∘ D_univ`, so the universal operator is pinned and functoriality in `N` is automatic. See the module docstring.”. References: EGA IV (16.8.3), “affine case”; SGA 6 II (AppII.1.2.3), “affine (module) case”; SGA 6 II (AppII.1.2.2), “affine case”.

> **Stacks 09CK.** Let `R → S` be a ring map, let `M` be an `S`-module and let `k : ℕ`. There
> exist an `S`-module `P` and a differential operator `D_univ : M → P` of order at most `k`
> relative to `R → S` such that, for every `S`-module `N`, precomposition with `D_univ` is a
> bijection from the `S`-linear maps `P → N` onto the differential operators `M → N` of order at
> most `k`. Thus `P = Pᵏ_{S/R}(M)` represents `Diffᵏ_{S/R}(M, -)`, functorially in `N`.

```lean
public theorem exists_universal_isDifferentialOperatorOfOrderLE (k : ℕ) :
    ∃ (P : Type (max v w)) (_ : AddCommGroup P) (_ : Module R P) (_ : Module S P)
      (_ : IsScalarTower R S P) (Duniv : M →ₗ[R] P),
      Duniv.IsDifferentialOperatorOfOrderLE S k ∧
        ∀ (N : Type x) [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N],
          Function.Injective (fun α : P →ₗ[S] N => α.restrictScalars R ∘ₗ Duniv) ∧
            Set.range (fun α : P →ₗ[S] N => α.restrictScalars R ∘ₗ Duniv) =
              {D : M →ₗ[R] N | D.IsDifferentialOperatorOfOrderLE S k}
```

## Tag 09CL, a definition

[Tag 09CL](https://stacks.math.columbia.edu/tag/09CL) in the Stacks Project.

**`LinearMap.IsUniversalDifferentialOperatorOfOrderLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/Defs.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/Defs.lean#L387). The attribute's comment: “The source names the module `Pᵏ_{S/R}(M)` it has just constructed; defined here is the property of a pair `(P, D)` of being one, which determines it up to unique isomorphism and so applies to every construction. Existence of such a pair is Lemma 09CK. See the module docstring.”. References: SGA 6 II (AppII.1.2.2), “affine case”.

> Let `R → S` be a ring map, let `M` be an `S`-module and let `k : ℕ`. For an
> `R`-linear map `D : M → P` into an `S`-module `P`, the property
> `D.IsUniversalDifferentialOperatorOfOrderLE S k` says that `D` is a differential operator of order
> at most `k` relative to `R → S` and that every differential operator `E : M → N` of order at most
> `k` into an `S`-module factors as `E = α ∘ D` for a unique `S`-linear map `α : P → N`. Equivalently
> `α ↦ α ∘ D` is the canonical isomorphism `Hom_S(P, N) = Diffᵏ_{S/R}(M, N)` of Lemma 09CK: that is,
> `P` is a *module of principal parts of order `k`* of `M`, written `Pᵏ_{S/R}(M)`, and `D` is its
> universal differential operator. Such a pair is unique up to unique isomorphism.

```lean
public def IsUniversalDifferentialOperatorOfOrderLE (S : Type v) [Semiring S] [Algebra R S]
    [Module S M] [IsScalarTower R S M] [Module S P] [IsScalarTower R S P] (k : ℕ)
    (D : M →ₗ[R] P) : Prop
```

## Tag 09CM, an example

[Tag 09CM](https://stacks.math.columbia.edu/tag/09CM) in the Stacks Project.

**`diff1EquivDerProd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/OrderOne.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/OrderOne.lean#L177). References: SGA 3 VIIA (1.3.1), “Dev≤1 ≃ O\_S ⊕ Der\_S”.

> The `S`-module isomorphism `Diff¹(S, N) ≃ₗ[S] Der_R(S, N) × N` given by `D ↦ (σ_D, D 1)`, where
> `σ_D g = D g - g · D 1`, with inverse `(σ, x) ↦ σ + λ_x`.

```lean
def diff1EquivDerProd : Diff1 R S N ≃ₗ[S] (Derivation R S N × N)
```

## Tag 09CN, a lemma

[Tag 09CN](https://stacks.math.columbia.edu/tag/09CN) in the Stacks Project.

**`LinearMap.IsDifferentialOperatorOfOrderLE.exists_shortExact_principalParts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/PrincipalParts.lean, line 897](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/PrincipalParts.lean#L897). The attribute's comment: “Stated for an arbitrary universal order-≤ 1 differential operator `D : M → P` rather than for a chosen construction of `P¹_{S/R}(M)`, whose existence is Lemma 09CK; both maps of the sequence are pinned by equations, from which functoriality in `M` is formal. See the module docstring.”. References: SGA 6 II (AppII.1.2.4), “n = 1, ring setting”.

> **Stacks 09CN.** Let `R → S` be a ring map and let `M` be an `S`-module. Let `D : M → P` be a
> universal differential operator of order at most `1` on `M`, i.e. `D` has order at most `1` and
> every order-`≤ 1` operator out of `M` factors uniquely through `D` by an `S`-linear map, so that
> `P` is a module of principal parts `P¹_{S/R}(M)`. Then there is a short exact sequence
> `0 → Ω[S⁄R] ⊗[S] M → P → M → 0`, the *sequence of principal parts*, whose first map sends
> `d b ⊗ₜ m` to `D (b • m) - b • D m` and whose second map is the retraction of `D`.

```lean
public theorem exists_shortExact_principalParts {R : Type*} {S : Type u} {M : Type v} {P : Type w}
    [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [AddCommGroup P] [Module R P] [Module S P] [IsScalarTower R S P]
    (D : M →ₗ[R] P) (hD : D.IsDifferentialOperatorOfOrderLE S 1)
    (huniv : ∀ (N : Type (max u v w)) [AddCommGroup N] [Module R N] [Module S N]
      [IsScalarTower R S N] (E : M →ₗ[R] N), E.IsDifferentialOperatorOfOrderLE S 1 →
      ∃! α : P →ₗ[S] N, ∀ m : M, α (D m) = E m) :
    ∃ (ι : Ω[S⁄R] ⊗[S] M →ₗ[S] P) (π : P →ₗ[S] M),
      (∀ (b : S) (m : M), ι (KaehlerDifferential.D R S b ⊗ₜ[S] m) = D (b • m) - b • D m) ∧
      (∀ m : M, π (D m) = m) ∧
      Function.Injective ι ∧ Function.Exact ι π ∧ Function.Surjective π
```

## Tag 0H8Z, a lemma

[Tag 0H8Z](https://stacks.math.columbia.edu/tag/0H8Z) in the Stacks Project.

**`LinearMap.IsUniversalDifferentialOperatorOfOrderLE.isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean, line 880](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean#L880). The attribute's comment: “Modules of principal parts appear through the universal property of Definition 09CL rather than as chosen constructions, and both base changes in Mathlib's `IsBaseChange` form. The map of Remark 09CP is the hypothesis `hψ`, which pins it since a universal `D` generates `P` over `B`. See the module docstring.”.

> **Stacks 0H8Z.** Let `A → A'` and `A → B` be ring maps, let `B' = B ⊗_A A'`, let `M` be a
> `B`-module and let `M' = M ⊗_A A'`, a `B'`-module, with `φ : M → M'` the canonical map. Let
> `D : M → P` be a universal differential operator of order at most `k` relative to `A → B` and let
> `D' : M' → P'` be one relative to `A' → B'`, so that `P = Pᵏ_{B/A}(M)` and `P' = Pᵏ_{B'/A'}(M')`
> are modules of principal parts. Then the map `ψ : P → P'` of Remark 09CP, i.e. the unique
> `B`-linear map with `ψ ∘ D = D' ∘ φ`, exhibits `P'` as the base change of `P` along `A → A'`:
> `Pᵏ_{B/A}(M) ⊗_A A' = Pᵏ_{B'/A'}(M')`.

```lean
public theorem isBaseChange
    [CommRing A] [CommRing A'] [CommRing B] [CommRing B']
    [Algebra A A'] [Algebra A B] [Algebra A B'] [Algebra A' B'] [Algebra B B']
    [IsScalarTower A A' B'] [IsScalarTower A B B'] [Algebra.IsPushout A A' B B']
    [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M]
    [AddCommGroup M'] [Module A M'] [Module A' M'] [Module B M'] [Module B' M']
    [IsScalarTower A A' M'] [IsScalarTower A B M'] [IsScalarTower A' B' M']
    [IsScalarTower B B' M']
    [AddCommGroup P] [Module A P] [Module B P] [IsScalarTower A B P]
    [AddCommGroup P'] [Module A P'] [Module A' P'] [Module B P'] [Module B' P']
    [IsScalarTower A A' P'] [IsScalarTower A B P'] [IsScalarTower A' B' P']
    [IsScalarTower B B' P']
    {k : ℕ} {D : M →ₗ[A] P} {D' : M' →ₗ[A'] P'}
    (hD : D.IsUniversalDifferentialOperatorOfOrderLE B k)
    (φ : M →ₗ[B] M') (hφ : IsBaseChange A' (φ.restrictScalars A))
    (hD' : D'.IsUniversalDifferentialOperatorOfOrderLE B' k)
    (ψ : P →ₗ[B] P') (hψ : ∀ m : M, ψ (D m) = D' (φ m)) :
    IsBaseChange A' (ψ.restrictScalars A)
```

## Tag 0H90, a lemma

[Tag 0H90](https://stacks.math.columbia.edu/tag/0H90) in the Stacks Project.

**`LinearMap.isUniversalDifferentialOperatorOfOrderLE_mkQ_comp_mk_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/PrincipalParts.lean, line 1357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/PrincipalParts.lean#L1357). The attribute's comment: “Stated as: the quotient, with the map `m ↦ class of 1 ⊗ₜ m`, is a module of principal parts of order `k` (Definition 09CL), which supplies the source's canonical isomorphism by uniqueness of a representing pair and pins the map. The `S ⊗[R] S`-action on `S ⊗[R] M` is the hypothesis `hsmul`, which determines it; it cannot be an instance, as it restricts to two different `Module S (S ⊗[R] M)` structures. See the module docstring.”. References: EGA IV (16.8.2), “factorization of D”; EGA IV (16.8.1), “special case”; SGA 3 VIIA (1.4.1), “affine case”.

> **Stacks 0H90.** Let `R → S` be a ring map, let `M` be an `S`-module, let `k : ℕ` and let
> `J = Ker(S ⊗[R] S → S)` be the kernel of the multiplication map. Then the `S`-module
> `(S ⊗[R] M)/J^{k + 1}(S ⊗[R] M)`, with `s` acting as multiplication by `s ⊗ₜ 1`, together with
> the `R`-linear map `m ↦ class of 1 ⊗ₜ m`, is a module of principal parts of order `k` of `M`:
> that map is a differential operator of order at most `k` relative to `R → S` and every such
> operator out of `M` factors uniquely `S`-linearly through it. Equivalently, there is a canonical
> isomorphism `Pᵏ_{S/R}(M) → (S ⊗[R] M)/J^{k + 1}(S ⊗[R] M)` carrying the universal differential
> operator of order `k` to `m ↦ class of 1 ⊗ₜ m`.

```lean
public theorem isUniversalDifferentialOperatorOfOrderLE_mkQ_comp_mk_one
    [Module (S ⊗[R] S) (S ⊗[R] M)] [IsScalarTower S (S ⊗[R] S) (S ⊗[R] M)]
    (hsmul : ∀ (a b t : S) (m : M), (a ⊗ₜ[R] b) • (t ⊗ₜ[R] m) = (a * t) ⊗ₜ[R] (b • m)) (k : ℕ) :
    (((KaehlerDifferential.ideal R S ^ (k + 1) •
          (⊤ : Submodule (S ⊗[R] S) (S ⊗[R] M))).restrictScalars S).mkQ.restrictScalars R ∘ₗ
        TensorProduct.mk R S M 1).IsUniversalDifferentialOperatorOfOrderLE S k
```

## Tag 0G34, a lemma

[Tag 0G34](https://stacks.math.columbia.edu/tag/0G34) in the Stacks Project.

**`deRham_isDiffOpOfOrder_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/OrderOne.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/OrderOne.lean#L310).

> Let `A → B` be a ring map and `i ≥ 0`. The de Rham differential `d : Ωⁱ_{B/A} → Ωⁱ⁺¹_{B/A}`,
> an additive map that is `A`-linear (`hAlin`) and satisfies
> `d (b₀ · db₁ ∧ ⋯ ∧ dbᵢ) = db₀ ∧ db₁ ∧ ⋯ ∧ dbᵢ` (`hChar`), is a differential operator of order `1`
> relative to `A → B`: for every `b ∈ B` the map `ω ↦ d (b · ω) - b · d ω` is `B`-linear.

```lean
theorem deRham_isDiffOpOfOrder_one (i : ℕ)
    (d : (⋀[B]^i (Ω[B⁄A])) →+ (⋀[B]^(i + 1) (Ω[B⁄A])))
    (hAlin : IsALinear A B d)
    (hChar : ∀ b : Fin (i+1) → B, d (deRhamGen i b) = deRhamTop i b) :
    IsDiffOpLE A B 1 d
```

## Tag 0G35, a lemma

[Tag 0G35](https://stacks.math.columbia.edu/tag/0G35) in the Stacks Project.

**`isDiffOpLE_succ_of_comm_isDiffOpLE_on_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/Defs.lean, line 763](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/Defs.lean#L763).

> Let `A → B` be a ring map, let `(g i)`
> generate `B` as an `A`-algebra, let `M, N` be `B`-modules and `D : M →+ N` an
> `A`-linear map. Fix `k ≥ 1` (written `k + 1` here). If for every `i` the commutator
> `diffOpComm (g i) D` is a differential operator of order `≤ k`, then `D` is a
> differential operator of order `≤ k + 1`.

```lean
theorem isDiffOpLE_succ_of_comm_isDiffOpLE_on_generators
    {ι : Type*} (g : ι → B)
    (hgen : Algebra.adjoin A (Set.range g) = ⊤)
    {M N : Type*} [AddCommGroup M] [AddCommGroup N] [Module B M] [Module B N]
    (D : M →+ N) (hD : IsALinear A B D) (k : ℕ)
    (hcomm : ∀ i : ι, IsDiffOpLE A B k (diffOpComm (g i) D)) :
    IsDiffOpLE A B (k + 1) D
```

## Tag 0G36, a lemma

[Tag 0G36](https://stacks.math.columbia.edu/tag/0G36) in the Stacks Project.

**`LinearMap.IsDifferentialOperatorOfOrderLE.existsUnique_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/Localization.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/Localization.lean#L632). The attribute's comment: “Stated for abstract localizations `IsLocalization T S'`, `IsLocalizedModule T f`, `IsLocalizedModule T g` rather than for `Localization T` and `LocalizedModule T`. The order of the extension is relative to `R → S'`, as in the source's proof. `extends` is spelled as the equation `E ∘ₗ f.restrictScalars R = g.restrictScalars R ∘ₗ D`, so the source's canonical maps are pinned; the case `k = 0` is `IsLocalizedModule.lift`. See the module docstring.”.

> **Stacks 0G36.** Let `R → S` be a ring map, let `M` and `N` be `S`-modules and let `T ⊆ S` be
> a multiplicative subset. A differential operator `D : M → N` of order at most `k` relative to
> `R → S` extends uniquely to a differential operator of order at most `k` relative to
> `R → T⁻¹S` on the localizations: there is a unique `R`-linear map `E : T⁻¹M → T⁻¹N` which is a
> differential operator of order at most `k` and satisfies `E ∘ f = g ∘ D` for the localization
> maps `f : M → T⁻¹M` and `g : N → T⁻¹N`.

```lean
public theorem existsUnique_extension {k : ℕ} {D : M →ₗ[R] N}
    (hD : D.IsDifferentialOperatorOfOrderLE S k) (T : Submonoid S) [IsLocalization T S']
    (f : M →ₗ[S] M') (g : N →ₗ[S] N') [IsLocalizedModule T f] [IsLocalizedModule T g] :
    ∃! E : M' →ₗ[R] N', E.IsDifferentialOperatorOfOrderLE S' k ∧
      E ∘ₗ f.restrictScalars R = g.restrictScalars R ∘ₗ D
```

## Tag 0G37, a lemma

[Tag 0G37](https://stacks.math.columbia.edu/tag/0G37) in the Stacks Project.

**`LinearMap.IsDifferentialOperatorOfOrderLE.rTensorB`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean#L363). The attribute's comment: “the operator `D ⊗ id_N` itself; `rTensorB_tmul` is its values on pure tensors, `order_rTensorB` the order bound and `eq_rTensorB` its uniqueness. The `B`-algebra structure on `A ⊗[R] B` and the actions on `M ⊗[R] N`, `M' ⊗[R] N` are hypotheses because Mathlib has no such instances; `halg`, `hsmul` and `hsmul'` pin them to the canonical ones. See the module docstring.”.

> **The operator `D ⊗ id_N`.** The tensor product of an `R`-linear map `D : M →ₗ[R] M'` with the
> identity of a `B`-module `N`, as a `B`-linear map `M ⊗[R] N → M' ⊗[R] N`. Its underlying `R`-linear
> map is `LinearMap.rTensor N D`; the content of the definition is the `B`-linearity, `B` acting
> through `algebraMap B (A ⊗[R] B) b = 1 ⊗ₜ b` on the factor `N` that `D ⊗ id_N` leaves alone. Here
> `hsmul` and `hsmul'` say that `A ⊗[R] B` acts on the tensor products by
> `(a ⊗ b) • (m ⊗ n) = (a • m) ⊗ (b • n)`, and `halg` that `B → A ⊗[R] B` is `b ↦ 1 ⊗ b`.

```lean
public def rTensorB
    (halg : ∀ b : B, algebraMap B (A ⊗[R] B) b = 1 ⊗ₜ[R] b)
    (hsmul : ∀ (a : A) (b : B) (m : M) (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n))
    (hsmul' : ∀ (a : A) (b : B) (m : M') (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n))
    (D : M →ₗ[R] M') : M ⊗[R] N →ₗ[B] M' ⊗[R] N
```

**`LinearMap.IsDifferentialOperatorOfOrderLE.rTensorB_tmul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean#L375). The attribute's comment: “the values of `rTensorB` on pure tensors”.

> `D ⊗ id_N` sends `m ⊗ n` to `D m ⊗ n`.

```lean
public lemma rTensorB_tmul
    (halg : ∀ b : B, algebraMap B (A ⊗[R] B) b = 1 ⊗ₜ[R] b)
    (hsmul : ∀ (a : A) (b : B) (m : M) (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n))
    (hsmul' : ∀ (a : A) (b : B) (m : M') (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n))
    (D : M →ₗ[R] M') (m : M) (n : N) :
    rTensorB halg hsmul hsmul' D (m ⊗ₜ[R] n) = D m ⊗ₜ[R] n
```

**`LinearMap.IsDifferentialOperatorOfOrderLE.order_rTensorB`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean#L389). The attribute's comment: “the order bound on `rTensorB`”.

> If `D` is a differential operator of order at most `k` relative to `R → A`, then `D ⊗ id_N` is
> one of order at most `k` relative to `B → A ⊗[R] B`.

```lean
public lemma order_rTensorB {k : ℕ} {D : M →ₗ[R] M'}
    (hD : D.IsDifferentialOperatorOfOrderLE A k)
    (halg : ∀ b : B, algebraMap B (A ⊗[R] B) b = 1 ⊗ₜ[R] b)
    (hsmul : ∀ (a : A) (b : B) (m : M) (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n))
    (hsmul' : ∀ (a : A) (b : B) (m : M') (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n)) :
    (rTensorB halg hsmul hsmul' D).IsDifferentialOperatorOfOrderLE (A ⊗[R] B) k
```

**`LinearMap.IsDifferentialOperatorOfOrderLE.eq_rTensorB`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DifferentialOperator/BaseChange.lean#L402). The attribute's comment: “uniqueness of `rTensorB`”.

> `D ⊗ id_N` is the only `B`-linear map `M ⊗[R] N → M' ⊗[R] N` carrying `m ⊗ n` to `D m ⊗ n`.

```lean
public lemma eq_rTensorB {D : M →ₗ[R] M'}
    (halg : ∀ b : B, algebraMap B (A ⊗[R] B) b = 1 ⊗ₜ[R] b)
    (hsmul : ∀ (a : A) (b : B) (m : M) (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n))
    (hsmul' : ∀ (a : A) (b : B) (m : M') (n : N),
      (a ⊗ₜ[R] b) • (m ⊗ₜ[R] n) = (a • m) ⊗ₜ[R] (b • n))
    (D' : M ⊗[R] N →ₗ[B] M' ⊗[R] N)
    (hD' : ∀ (m : M) (n : N), D' (m ⊗ₜ[R] n) = D m ⊗ₜ[R] n) :
    D' = rTensorB halg hsmul hsmul' D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.133, Tag 09CH](https://stacks.math.columbia.edu/tag/09CH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
