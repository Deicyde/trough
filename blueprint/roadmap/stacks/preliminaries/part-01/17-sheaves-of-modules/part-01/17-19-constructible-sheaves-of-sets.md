---
declaration: section
origin: cited
lean: Stacks.Sheaves.ConstantSheafGenerators.exists_epi_from_coproduct_jExtendConst, Stacks.isFilteredColimit_of_hasCompactBasis, Stacks.exists_pullback_from_finite_sober_of_hasFiniteBasisCoequalizerPresentation, Stacks.exists_mono_to_pi_constantSheafPushforward
statement: formalized
proof: formalized
---

# 17.19 Constructible sheaves of sets

Section 17.19 of the Stacks Project, [Tag 0CAG](https://stacks.math.columbia.edu/tag/0CAG). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CAH, a lemma

[Tag 0CAH](https://stacks.math.columbia.edu/tag/0CAH) in the Stacks Project.

**`Stacks.Sheaves.ConstantSheafGenerators.exists_epi_from_coproduct_jExtendConst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/ConstantSheafGenerators.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/ConstantSheafGenerators.lean#L510).

> **Stacks 0CAH (Lemma 17.19.1).**  Let `X` be a topological space, `B` a basis for the
> topology on `X`, and `F` a sheaf of sets on `X`.  Then there is an index set `I`, a family of
> basis opens `U i ∈ B`, a family of finite sets `S i`, and a *surjection* (epimorphism in
> `Sh(X)`)
>
>   `φ : ∐_i j_{U i !}(constant sheaf S i on U i) ⟶ F`
>
> from the categorical coproduct (Def. 5) of the extensions-by-empty-set `jExtendConst X (U i) (S i)`
> of the constant sheaves `constant sheaf (S i)` on `U i`.  Here `Epi φ` expresses that `φ` is a
> surjection in the sense of Definition 6.
>
> INFORMAL PROOF (Stacks 0CAH).
> Take the index set `I = Σ x : X, F_x = {(x,s) : x ∈ X, s ∈ F_x}`, every `S i = PUnit` (a singleton,
> hence finite).  For each `i = (x,s)`, since `B` is a basis and the stalk is a colimit over open
> neighborhoods, `germ_exist_of_isBasis hB` provides a basis open `U i ∈ B` with `x ∈ U i` and a
> section `σ i ∈ F(U i)` with germ `(σ i)_x = s`.  By Sub-lemma 1 (`exists_jExtendConst_hom_germ`),
> the section `σ i` yields a morphism `ψ i : j_{U i !}underline{PUnit} ⟶ F` together with a stalk
> element `t i` of `j_{U i !}underline{PUnit}` at `x` with `stalkMap (ψ i) (t i) = s`.  Assemble the
> `ψ i` via the coproduct universal property (`Sigma.desc`) into
> `φ : ∐_i j_{U i !}underline{PUnit} ⟶ F`.
>
> For `Epi φ` we use the criterion (Def. 6): `φ` is epi iff stalkwise surjective
> (`TopCat.Sheaf.isLocallySurjective_iff_epi` ∘ `locally_surjective_iff_surjective_on_stalks`).
> Fix `x : X` and `s ∈ F_x`; let `i = ⟨x, s⟩`.  Since `Sigma.ι i ≫ φ = ψ i`
> (`Sigma.ι_desc`), applying the stalk functor and functoriality gives
> `stalkMap φ (stalkMap (Sigma.ι i) (t i)) = stalkMap (ψ i) (t i) = s`.  Hence `s` is in the image of
> `stalkMap φ`, so `φ` is surjective on every stalk, therefore `Epi`. ∎

```lean
theorem exists_epi_from_coproduct_jExtendConst
    (F : TopCat.Sheaf (Type u) X) (B : Set (Opens X)) (hB : Opens.IsBasis B) :
    ∃ (I : Type u) (U : I → Opens X) (S : I → Type u),
      (∀ i, U i ∈ B) ∧
      (∀ i, Finite (S i)) ∧
      ∃ φ : (∐ fun i => jExtendConst X (U i) (S i)) ⟶ F, Epi φ
```

## Tag 0CAI, a lemma

[Tag 0CAI](https://stacks.math.columbia.edu/tag/0CAI) in the Stacks Project.

**`Stacks.isFilteredColimit_of_hasCompactBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Spectral/CompactBasisColimit.lean, line 976](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Spectral/CompactBasisColimit.lean#L976).

> Every sheaf of sets on a space admitting a basis of quasi-compact opens is
> a filtered colimit of sheaves with finite basis coequalizer presentations.

```lean
theorem isFilteredColimit_of_hasCompactBasis (B : Set (Opens X))
    (hBasis : IsTopologicalBasis ((fun U : Opens X ↦ (U : Set X)) '' B))
    (hB : ∀ U ∈ B, IsCompact (U : Set X))
    (F : TopCat.Sheaf (Type u) (TopCat.of X)) :
    ∃ (J : Type u) (_ : SmallCategory J) (_ : IsFiltered J)
      (D : J ⥤ TopCat.Sheaf (Type u) (TopCat.of X))
      (ι : D ⟶ (Functor.const J).obj F),
      ∃ (_ : IsColimit (Cocone.mk F ι)),
        ∀ j, HasFiniteBasisCoequalizerPresentation B (D.obj j)
```

## Tag 0CAK, a lemma

[Tag 0CAK](https://stacks.math.columbia.edu/tag/0CAK) in the Stacks Project.

**`Stacks.exists_pullback_from_finite_sober_of_hasFiniteBasisCoequalizerPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Spectral/FiniteSoberPullback.lean, line 1015](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Spectral/FiniteSoberPullback.lean#L1015).

> A sheaf with a finite coequalizer presentation over the quasi-compact
> opens of a spectral space descends to a sheaf with finite stalks on a finite
> sober space.

```lean
theorem exists_pullback_from_finite_sober_of_hasFiniteBasisCoequalizerPresentation
    (F : TopCat.Sheaf (Type u) (TopCat.of X))
    (hF : HasFiniteBasisCoequalizerPresentation
      {U : Opens X | IsCompact (U : Set X)} F) :
    ∃ (Y : Type u) (_ : TopologicalSpace Y) (_ : Finite Y)
      (_ : QuasiSober Y) (_ : T0Space Y) (f : TopCat.of X ⟶ TopCat.of Y)
      (G : TopCat.Sheaf (Type u) (TopCat.of Y)),
      IsSpectralMap f ∧
        (∀ y, Finite (G.presheaf.stalk y)) ∧
        Nonempty ((TopCat.Sheaf.pullback (Type u) f).obj G ≅ F)
```

## Tag 0CAL, a lemma

[Tag 0CAL](https://stacks.math.columbia.edu/tag/0CAL) in the Stacks Project.

**`Stacks.exists_mono_to_pi_constantSheafPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Spectral/ConstructibleSheaves.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Spectral/ConstructibleSheaves.lean#L489).

> **Stacks Project, Tag 0CAL.** A constructible sheaf of sets on a spectral space — one with
> a finite presentation by finite constant sheaves extended from quasi-compact opens — is
> isomorphic to a subsheaf of a finite product of pushforwards of finite constant sheaves from
> closed constructible subspaces.

```lean
theorem exists_mono_to_pi_constantSheafPushforward [SpectralSpace X]
    (F : TopCat.Sheaf (Type u) (TopCat.of X))
    (hF : HasFiniteBasisCoequalizerPresentation
      { U : Opens X | IsCompact (U : Set X) } F) :
    ∃ (n : ℕ) (Z : Fin n → Set X),
      (∀ i, IsClosed (Z i)) ∧ (∀ i, Topology.IsConstructible (Z i)) ∧
        ∃ (S : Fin n → Type u) (_ : ∀ i, Finite (S i))
          (f : F ⟶ ∏ᶜ fun i ↦ constantSheafPushforward (Z i) (S i)), Mono f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.19, Tag 0CAG](https://stacks.math.columbia.edu/tag/0CAG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
