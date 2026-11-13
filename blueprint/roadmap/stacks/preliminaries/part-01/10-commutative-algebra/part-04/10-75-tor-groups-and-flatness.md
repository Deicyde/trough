---
declaration: section
origin: cited
lean: FreeResolution.torMap_isLift_properties, CategoryTheory.ShortComplex.ShortExact.exists_Tor'_one_composableArrows_exact_and_epi, Stacks.Tor.DoubleComplex.statement1, Stacks.Tor.DoubleComplex.statement2, tor_symm_canonically_iso, swap_eigenspace_dim, swap_not_isDiagonalizable, torSymm_zero_self_ne_one_and_ne_neg_one
statement: formalized
proof: formalized
---

# 10.75 Tor groups and flatness

Section 10.75 of the Stacks Project, [Tag 00LY](https://stacks.math.columbia.edu/tag/00LY). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00LZ, a lemma

[Tag 00LZ](https://stacks.math.columbia.edu/tag/00LZ) in the Stacks Project.

**`FreeResolution.torMap_isLift_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Finiteness.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Finiteness.lean#L476). The attribute's comment: “All three assertions: independence of the lift, the isomorphism case, and the identity case (`M₁ = M₂`, `F = G`, `φ = 𝟙`).”.

> Let `F` and `G` be free resolutions of `M₁` and `M₂`, let `φ : M₁ ⟶ M₂` and let `N` be a
> module. Then the maps `H_i(α) : H_i(F ⊗ N) ⟶ H_i(G ⊗ N)` induced by chain maps `α` lifting `φ`
> are independent of the choice of `α`; if `φ` is an isomorphism, so are all the maps `H_i(α)`;
> and if `F = G` and `φ` is the identity, all the maps `H_i(α)` are the identity.

```lean
theorem torMap_isLift_properties {M₁ M₂ : ModuleCat R} (F : FreeResolution M₁)
    (G : FreeResolution M₂) (N : ModuleCat R) (φ : M₁ ⟶ M₂) :
    (∀ (α β : F.complex ⟶ G.complex), IsLift F G φ α → IsLift F G φ β → ∀ i,
        torMap F G N α i = torMap F G N β i) ∧
      (IsIso φ → ∀ (α : F.complex ⟶ G.complex), IsLift F G φ α → ∀ i,
        IsIso (torMap F G N α i)) ∧
      (∀ (α : F.complex ⟶ F.complex), IsLift F F (𝟙 M₁) α → ∀ i, torMap F F N α i = 𝟙 _)
```

## Tag 00M0, a lemma

[Tag 00M0](https://stacks.math.columbia.edu/tag/00M0) in the Stacks Project.

**`CategoryTheory.ShortComplex.ShortExact.exists_Tor'_one_composableArrows_exact_and_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Vanishing.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Vanishing.lean#L210).

> Let `R` be a commutative ring, let `M` be an `R`-module and let
> `S : 0 → N' → N → N'' → 0` be a short exact sequence of `R`-modules. Then there is a connecting
> homomorphism `δ : Tor₁(M, N'') ⟶ M ⊗ N'` making
>
>   `Tor₁(M, N') → Tor₁(M, N) → Tor₁(M, N'') →δ M ⊗ N' → M ⊗ N → M ⊗ N''`
>
> exact, and `M ⊗ N → M ⊗ N''` is surjective. Here `Tor₁(M, -)` is `(Tor' (ModuleCat R) 1).obj M`,
> the first left derived functor of `- ⊗ N` evaluated at `M`, and the maps other than `δ` are the
> functorial ones.

```lean
public theorem exists_Tor'_one_composableArrows_exact_and_epi {R : Type u} [CommRing R]
    {S : ShortComplex (ModuleCat.{u} R)} (hS : S.ShortExact) (M : ModuleCat.{u} R) :
    (∃ δ : ((Tor' (ModuleCat.{u} R) 1).obj M).obj S.X₃ ⟶ M ⊗ S.X₁,
        (ComposableArrows.mk₅ (((Tor' (ModuleCat.{u} R) 1).obj M).map S.f)
          (((Tor' (ModuleCat.{u} R) 1).obj M).map S.g) δ (M ◁ S.f) (M ◁ S.g)).Exact) ∧
      Epi (M ◁ S.g)
```

## Tag 00M1, a lemma

[Tag 00M1](https://stacks.math.columbia.edu/tag/00M1) in the Stacks Project.

**`Stacks.Tor.DoubleComplex.statement1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean#L408). The attribute's comment: “(1)”.

> For a double complex `A` whose rows are resolutions of the horizontal cokernels and whose
> columns are resolutions of the vertical cokernels, there is an isomorphism of `R`-modules
> `H_i(R(A)_•) ≅ H_i(U(A)_•)` for every `i ≥ 0`.

```lean
theorem statement1 (A : DoubleCx R) (hrow : A.RowResolution) (hcol : A.ColResolution)
    (i : ℕ) : Nonempty (A.RHom i ≃ₗ[R] A.UHom i)
```

**`Stacks.Tor.DoubleComplex.statement2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean#L417). The attribute's comment: “(2)”.

> The isomorphisms `H_i(R(A)_•) ≅ H_i(U(A)_•)` can be chosen naturally in `A`: there is an
> assignment, to every double complex `A` satisfying the resolution hypotheses and every `i`, of an
> isomorphism `e A : H_i(R(A)_•) ≅ H_i(U(A)_•)`, such that `H_i(U(Ψ)) ∘ e A = e B ∘ H_i(R(Ψ))` for
> every morphism `Ψ : A → B` of such double complexes.

```lean
theorem statement2 :
    ∃ e : ∀ (A : DoubleCx R), A.RowResolution → A.ColResolution → ∀ i,
        (A.RHom i ≃ₗ[R] A.UHom i),
      ∀ (A B : DoubleCx R) (hrowA : A.RowResolution) (hcolA : A.ColResolution)
        (hrowB : B.RowResolution) (hcolB : B.ColResolution)
        (Ψ : DCxHom A B) (i : ℕ),
        (Ψ.UHomMap i).comp (e A hrowA hcolA i : A.RHom i →ₗ[R] A.UHom i) =
          ((e B hrowB hcolB i : B.RHom i →ₗ[R] B.UHom i)).comp (Ψ.RHomMap i)
```

## Tag 00M3, a lemma

[Tag 00M3](https://stacks.math.columbia.edu/tag/00M3) in the Stacks Project.

**`tor_symm_canonically_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Balancing/Naturality.lean, line 740](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Balancing/Naturality.lean#L740). References: EGA III (6.3.5), “(i), special case”; EGA III (6.5.5), “S = X = Y = Spec R”; EGA III (6.7.13), “special case”.

> For every `i ≥ 0` the two functors `(M, N) ↦ Tor_i^R(M, N)` and `(M, N) ↦ Tor_i^R(N, M)` are
> canonically isomorphic: there is a natural isomorphism between the bifunctor
> `Tor (ModuleCat R) i` and the swap bifunctor `(Tor (ModuleCat R) i).flip` in the functor category
> `ModuleCat R ⥤ ModuleCat R ⥤ ModuleCat R`.

```lean
theorem tor_symm_canonically_iso (i : ℕ) :
    Nonempty (Tor (ModuleCat.{u} R) i ≅ (Tor (ModuleCat.{u} R) i).flip)
```

## Tag 00M4, a remark

[Tag 00M4](https://stacks.math.columbia.edu/tag/00M4) in the Stacks Project.

**`swap_eigenspace_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean#L398). The attribute's comment: “supporting part: the eigenspace dimensions of the switch map in the example; the Tor statement is torSymm\_zero\_self\_ne\_one\_and\_ne\_neg\_one”.

> Eigenspace dimensions in characteristic `≠ 2`.
> Assume `char k ≠ 2` and `dim_k V = n`. Then the `+1`-eigenspace of the swap
> map has dimension `(n^2 + n)/2` and the `-1`-eigenspace has dimension
> `(n^2 - n)/2`.
>
> Argument: the `-1`-eigenspace has dimension `(n^2 − n)/2` by
> `swap_finrank_antisymm`. Since `E₊₁` and `E₋₁` are complementary
> (`swap_isCompl_eigenspaces`), their dimensions add to
> `finrank (V ⊗ V) = n * n = n^2` (`Submodule.finrank_add_eq_of_isCompl` and
> `Module.finrank_tensorProduct`). The remaining `+1`-dimension is then
> `n^2 − (n^2 − n)/2 = (n^2 + n)/2`, a nat-arithmetic identity (both `n^2 ± n`
> are even).
>
> This is the eigenvalue count of the example in Stacks, Remark 00M4. The remark itself, about
> the self-map of `Tor_0(V, V)` given by the symmetry of Tag 00M3, is
> `torSymm_zero_self_ne_one_and_ne_neg_one`, which identifies that self-map with `swapMap`.

```lean
theorem swap_eigenspace_dim
    (hk : (2 : k) ≠ 0) (n : ℕ) (hn : Module.finrank k V = n) :
    Module.finrank k (swapEigenspace k V (1 : k)) = (n ^ 2 + n) / 2 ∧
    Module.finrank k (swapEigenspace k V (-1 : k)) = (n ^ 2 - n) / 2
```

**`swap_not_isDiagonalizable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean#L491). The attribute's comment: “supporting part: the switch map of the example is not diagonalizable in characteristic 2; the Tor statement is torSymm\_zero\_self\_ne\_one\_and\_ne\_neg\_one”.

> Non-diagonalizability in characteristic `2`.
> Assume `char k = 2` and `dim_k V ≥ 2`. Then the swap map is not
> diagonalizable.
>
> Argument: if `σ` were diagonalizable then `⨆ λ, eigenspace λ = ⊤`. But in
> characteristic `2` every eigenspace is contained in `eigenspace 1`
> (`swap_eigenspace_le_one_char2`), so `⨆ λ, eigenspace λ ≤ eigenspace 1`, whence
> `eigenspace 1 = ⊤`, i.e. `σ x = x` for all `x`. This contradicts `swap_ne_id`,
> which produces a tensor moved by `σ`.
>
> This is the characteristic `2` sentence of the example in Stacks, Remark 00M4; the remark itself
> is `torSymm_zero_self_ne_one_and_ne_neg_one`.

```lean
theorem swap_not_isDiagonalizable
    (hk : (2 : k) = 0) (hn : 2 ≤ Module.finrank k V) :
    ¬ IsDiagonalizable (swapMap k V)
```

**`torSymm_zero_self_ne_one_and_ne_neg_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Balancing/SelfMap.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Balancing/SelfMap.lean#L114). The attribute's comment: “the degree-0 self-map of the 00M3 symmetry on Tor\_0(V, V) is the switch map, and is neither 1 nor -1 when dim V ≥ 2”.

> Stacks, Remark 00M4: for `M = N` the canonical isomorphism of Tag 00M3 gives a self-map of
> `Tor_i^R(M, M)`, and this self-map is not the identity, already for `i = 0`; changing its sign
> does not help either. Concretely, let `V` be a vector space of dimension at least `2` over a
> field `k`. Under `torZeroIso` the self-map of `Tor_0^k(V, V)` given by `torSymm` is the switch
> map `swapMap k V` of `V ⊗_k V` (whose eigenspaces have dimensions `(n² + n)/2` and `(n² − n)/2`
> in characteristic `≠ 2`, `swap_eigenspace_dim`, and which is not diagonalizable in
> characteristic `2`, `swap_not_isDiagonalizable`), and it is neither the identity nor minus the
> identity.

```lean
theorem torSymm_zero_self_ne_one_and_ne_neg_one (k : Type u) [Field k] (V : ModuleCat.{u} k)
    (hn : 2 ≤ Module.finrank k V) :
    (torZeroIso k V V).inv ≫ ((torSymm k 0).hom.app V).app V ≫ (torZeroIso k V V).hom
        = ModuleCat.ofHom (swapMap k V) ∧
      ((torSymm k 0).hom.app V).app V ≠ 𝟙 _ ∧
      ((torSymm k 0).hom.app V).app V ≠ -𝟙 _
```

## Tag 0AZ4, a lemma

[Tag 0AZ4](https://stacks.math.columbia.edu/tag/0AZ4) in the Stacks Project.

**`tor_finite_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Finiteness.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Finiteness.lean#L318). References: EGA III (6.5.13), “special case”; EGA III (6.7.9), “special case”; EGA III (7.4.7), “(i), special case”.

> Let `R` be a Noetherian ring and let `M`, `N` be finite
> `R`-modules. Then `Tor_p^R(M, N)` is a finite `R`-module for every `p`.

```lean
theorem tor_finite_of_noetherian (R : Type u) [CommRing R] [IsNoetherianRing R]
    (M N : ModuleCat.{u} R) [Module.Finite R M] [Module.Finite R N] (p : ℕ) :
    Module.Finite R (((Tor (ModuleCat.{u} R) p).obj M).obj N)
```

## Tag 00M5, a lemma

[Tag 00M5](https://stacks.math.columbia.edu/tag/00M5) in the Stacks Project.

**`Module.Flat.tfae_isZero_Tor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Flatness.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/Flatness.lean#L192). References: EGA 0 (6.1.1).

> Let `R` be a commutative ring and let `M` be an `R`-module. The following are equivalent:
> (1) `M` is flat over `R`; (2) for all `i > 0` the functor `Tor_i(M, -)` is zero; (3) the functor
> `Tor₁(M, -)` is zero; (4) `Tor₁(M, R/I) = 0` for all ideals `I ⊆ R`; (5) `Tor₁(M, R/I) = 0` for
> all finitely generated ideals `I ⊆ R`. Here `Tor_i(M, -)` is `(Tor' (ModuleCat R) i).obj M`, the
> `i`-th left derived functor of `- ⊗ N` evaluated at `M`.

```lean
public theorem tfae_isZero_Tor' {R : Type u} [CommRing R] (M : ModuleCat.{u} R) :
    List.TFAE
      [Module.Flat R M,
        ∀ i, 0 < i → IsZero ((Tor' (ModuleCat.{u} R) i).obj M),
        IsZero ((Tor' (ModuleCat.{u} R) 1).obj M),
        ∀ I : Ideal R,
          IsZero (((Tor' (ModuleCat.{u} R) 1).obj M).obj (ModuleCat.of R (R ⧸ I))),
        ∀ I : Ideal R, I.FG →
          IsZero (((Tor' (ModuleCat.{u} R) 1).obj M).obj (ModuleCat.of R (R ⧸ I)))]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.75, Tag 00LY](https://stacks.math.columbia.edu/tag/00LY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
