---
declaration: section
origin: cited
lean: torMap_independent_of_lift, CategoryTheory.ShortComplex.ShortExact.exists_Tor'_one_composableArrows_exact_and_epi, Stacks.Tor.DoubleComplex.statement1, Stacks.Tor.DoubleComplex.statement2, tor_symm_canonically_iso, swap_eigenspace_dim, swap_not_isDiagonalizable, tor_finite_of_noetherian
statement: formalized
proof: formalized
---

# 10.75 Tor groups and flatness

Section 10.75 of the Stacks Project, [Tag 00LY](https://stacks.math.columbia.edu/tag/00LY). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00LZ, a lemma

[Tag 00LZ](https://stacks.math.columbia.edu/tag/00LZ) in the Stacks Project.

**`torMap_independent_of_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Finiteness.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/Finiteness.lean#L442).

> The induced map on homology is independent of the choice of the lift: two chain maps
> `α, β : F.complex ⟶ G.complex` both lifting `φ : M₁ ⟶ M₂` induce equal maps
> `H_i(F ⊗ N) ⟶ H_i(G ⊗ N)`.

```lean
theorem torMap_independent_of_lift {R : Type} [CommRing R] {M₁ M₂ : ModuleCat R}
    (F : FreeResolution M₁) (G : FreeResolution M₂) (N : ModuleCat R) {φ : M₁ ⟶ M₂}
    (α β : F.complex ⟶ G.complex) (hα : IsLift F G φ α) (hβ : IsLift F G φ β) (i : ℕ) :
    torMap F G N α i = torMap F G N β i
```

## Tag 00M0, a lemma

[Tag 00M0](https://stacks.math.columbia.edu/tag/00M0) in the Stacks Project.

**`CategoryTheory.ShortComplex.ShortExact.exists_Tor'_one_composableArrows_exact_and_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Vanishing.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/Vanishing.lean#L210).

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

**`Stacks.Tor.DoubleComplex.statement1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean#L408). The attribute's comment: “(1)”.

> For a double complex `A` whose rows are resolutions of the horizontal cokernels and whose
> columns are resolutions of the vertical cokernels, there is an isomorphism of `R`-modules
> `H_i(R(A)_•) ≅ H_i(U(A)_•)` for every `i ≥ 0`.

```lean
theorem statement1 (A : DoubleCx R) (hrow : A.RowResolution) (hcol : A.ColResolution)
    (i : ℕ) : Nonempty (A.RHom i ≃ₗ[R] A.UHom i)
```

**`Stacks.Tor.DoubleComplex.statement2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/Balancing/CanonicalIso.lean#L417). The attribute's comment: “(2)”.

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

**`tor_symm_canonically_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Balancing/Naturality.lean, line 740](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/Balancing/Naturality.lean#L740). References: EGA III (6.3.5), “(i), special case”; EGA III (6.5.5), “S = X = Y = Spec R”; EGA III (6.7.13), “special case”.

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

**`swap_eigenspace_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean#L394).

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

```lean
theorem swap_eigenspace_dim
    (hk : (2 : k) ≠ 0) (n : ℕ) (hn : Module.finrank k V = n) :
    Module.finrank k (swapEigenspace k V (1 : k)) = (n ^ 2 + n) / 2 ∧
    Module.finrank k (swapEigenspace k V (-1 : k)) = (n ^ 2 - n) / 2
```

**`swap_not_isDiagonalizable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/TensorProduct/Swap.lean#L483).

> Non-diagonalizability in characteristic `2`.
> Assume `char k = 2` and `dim_k V ≥ 2`. Then the swap map is not
> diagonalizable.
>
> Argument: if `σ` were diagonalizable then `⨆ λ, eigenspace λ = ⊤`. But in
> characteristic `2` every eigenspace is contained in `eigenspace 1`
> (`swap_eigenspace_le_one_char2`), so `⨆ λ, eigenspace λ ≤ eigenspace 1`, whence
> `eigenspace 1 = ⊤`, i.e. `σ x = x` for all `x`. This contradicts `swap_ne_id`,
> which produces a tensor moved by `σ`.

```lean
theorem swap_not_isDiagonalizable
    (hk : (2 : k) = 0) (hn : 2 ≤ Module.finrank k V) :
    ¬ IsDiagonalizable (swapMap k V)
```

## Tag 0AZ4, a lemma

[Tag 0AZ4](https://stacks.math.columbia.edu/tag/0AZ4) in the Stacks Project.

**`tor_finite_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Finiteness.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/Finiteness.lean#L317). References: EGA III (6.5.13), “special case”; EGA III (6.7.9), “special case”; EGA III (7.4.7), “(i), special case”.

> Let `R` be a Noetherian ring and let `M`, `N` be finite
> `R`-modules. Then `Tor_p^R(M, N)` is a finite `R`-module for every `p`.

```lean
theorem tor_finite_of_noetherian (R : Type u) [CommRing R] [IsNoetherianRing R]
    (M N : ModuleCat.{u} R) [Module.Finite R M] [Module.Finite R N] (p : ℕ) :
    Module.Finite R (((Tor (ModuleCat.{u} R) p).obj M).obj N)
```

## Tag 00M5, a lemma

[Tag 00M5](https://stacks.math.columbia.edu/tag/00M5) in the Stacks Project.

**`Module.Flat.tfae_isZero_Tor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/Flatness.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/Flatness.lean#L192). References: EGA 0 (6.1.1).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
