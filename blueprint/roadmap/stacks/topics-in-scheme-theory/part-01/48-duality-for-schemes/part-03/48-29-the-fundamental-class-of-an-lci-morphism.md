---
declaration: section
origin: cited
lean: Stacks.Duality.isIso_stalkMap_locallyRingedSpaceDeterminantMap_iff, Stacks.Duality.ClosedOpenProperFactorization.exists_fundamentalClass_of_isLocalCompleteIntersection, Stacks.Duality.SmoothLocus.exists_map_exteriorPower_isIso_of_smoothAt
statement: formalized
proof: formalized
---

# 48.29 The fundamental class of an lci morphism

Section 48.29 of the Stacks Project, [Tag 0E9X](https://stacks.math.columbia.edu/tag/0E9X). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E9Y, a lemma

[Tag 0E9Y](https://stacks.math.columbia.edu/tag/0E9Y) in the Stacks Project.

**`Stacks.Duality.isIso_stalkMap_locallyRingedSpaceDeterminantMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/FundamentalClassDeterminantSource.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/FundamentalClassDeterminantSource.lean#L617).

> **[Stacks, Tag 0E9Y].** Let `X` be a locally ringed space and `E₁ --α--> E₀ --π--> F ⟶ 0` an
> exact sequence of `O_X`-modules with `E₁` and `E₀` finite locally free of ranks `r₁` and `r₀`.
> The canonical map `⋀^{r₀ - r₁} F ⟶ ⋀^{r₁}(E₁^∨) ⊗ ⋀^{r₀} E₀` is an isomorphism on the stalk at
> `x` if and only if `F` is locally free of rank `r₀ - r₁` on an open neighbourhood of `x`: that
> is, `r₀ - r₁` is a natural number and `F` is free of that rank on some open `U ∋ x`.

```lean
theorem isIso_stalkMap_locallyRingedSpaceDeterminantMap_iff [Epi π]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E₁ r₁]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E₀ r₀]
    (x : ↥Y.toRingedSpace.carrier) :
    IsIso (AlgebraicGeometry.SheafOfModules.stalkMap
        (toRingCat (Opens.grothendieckTopology ↥Y.toRingedSpace.carrier) Y.toRingedSpace.sheaf) x
        (locallyRingedSpaceDeterminantMap Y α π hαπ hS r₁ r₀)) ↔
      r₁ ≤ r₀ ∧ ∃ U : Opens ↥Y.toRingedSpace.carrier, x ∈ U ∧
        ∃ t : LocallyFreeRank.Trivialization Y.toRingedSpace.carrier
          (LocallyFreeRank.toRingSheaf Y.toRingedSpace.carrier Y.toRingedSpace.sheaf) F U,
          Nonempty (t.ι ≃ Fin (r₀ - r₁))
```

## Tag 0E9Z, a lemma

[Tag 0E9Z](https://stacks.math.columbia.edu/tag/0E9Z) in the Stacks Project.

**`Stacks.Duality.ClosedOpenProperFactorization.exists_fundamentalClass_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekLocalCompleteIntersection/Decomposition.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekLocalCompleteIntersection/Decomposition.lean#L258).

> Let `S` be Noetherian and `f : X ⟶ Y` a local complete intersection morphism of `FTS S`
> which factors as an immersion `ι : X ⟶ P` followed by a proper smooth morphism `g : P ⟶ Y`; let
> `f^!` be computed at any compactification `j` of `f`. Then there is a locally constant function
> `r` on `X` such that `ω_{X/Y} = H^{-r}(f^!𝒪_Y)` is the only nonzero cohomology sheaf of `f^!𝒪_Y`
> (the stalk of `H^k(f^!𝒪_Y)` at `x` is nonzero exactly for `k = -r(x)`), and a map
> `∧^r Ω_{X/Y} ⟶ ω_{X/Y}` whose stalk at `x` is an isomorphism exactly when `f` is smooth at `x`.
>
> As `r` is only locally constant, the map is given on each piece of a decomposition of `X` into
> pairwise disjoint open and closed subschemes covering `X` on which `r` is constant.

```lean
theorem exists_fundamentalClass_of_isLocalCompleteIntersection
    (hlci : IsLocalCompleteIntersectionMorphism f.left) (j : CompactificationOf (Over.mk f.left)) :
    ∃ r : X.left → ℤ, IsLocallyConstant r ∧
      (∀ (x : X.left) (k : ℤ),
        Nontrivial ↑((upperShriekHomology f j k).presheaf.stalk x) ↔ k = -r x) ∧
      ∃ (A : Type) (V : A → X.left.Opens) (n : A → ℤ),
        (∀ a, IsClosed (V a : Set X.left)) ∧ Pairwise (Function.onFun Disjoint V) ∧ (⨆ a, V a) = ⊤ ∧
        (∀ a, ∀ x ∈ V a, r x = n a) ∧
        ∀ a, ∃ φ : (Scheme.Modules.restrictFunctor (V a).ι).obj
            (Scheme.Modules.exteriorPower (Scheme.Hom.relativeDifferentials f.left) (n a)) ⟶
          (Scheme.Modules.restrictFunctor (V a).ι).obj (upperShriekHomology f j (-n a)),
          ∀ x : (V a).toScheme, IsIso (AlgebraicGeometry.SheafOfModules.stalkMap
              (CategoryTheory.Sheaf.toRingCat (Opens.grothendieckTopology
                ↥(V a).toScheme.toLocallyRingedSpace.toRingedSpace.carrier)
                (V a).toScheme.toLocallyRingedSpace.toRingedSpace.sheaf) x φ) ↔
            InfinitesimalLifting.SmoothAt f.left ((V a).ι x)
```

## Tag 0EA0, a lemma

[Tag 0EA0](https://stacks.math.columbia.edu/tag/0EA0) in the Stacks Project.

**`Stacks.Duality.SmoothLocus.exists_map_exteriorPower_isIso_of_smoothAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekLocalCompleteIntersection/SmoothLocus.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekLocalCompleteIntersection/SmoothLocus.lean#L409).

> **Stacks Project, Tag 0EA0.** Let `S` be Noetherian, `f : X ⟶ Y` a morphism of `FTS S` and
> `r ≥ 0`. Assume
> 1. `Y` is Cohen–Macaulay,
> 2. `f` factors as an immersion `ι : X ⟶ P` followed by a smooth proper `g : P ⟶ Y`,
> 3. `f` is Koszul at every `x ∈ X` with `dim 𝒪_{X,x} ≤ 1`, and
> 4. `trdeg_{κ(f(ξ))} κ(ξ) = r` at every generic point `ξ` of an irreducible component of `X`.
>
> Then, with `ω_{X/Y} = H^{-r}(f^!𝒪_Y)` (`f^!` at any compactification `j`), there is a map
> `∧^r Ω_{X/Y} ⟶ ω_{X/Y}` which is an isomorphism at every point where `f` is smooth.
>
> Two steps of the source's proof are corrected. The locally constant function of
> [Stacks, Tag 0E9Z] on the local complete intersection locus `U` is `r` only on the pieces where it
> equals `r` (in general it is `r - dim 𝒪_{Y,f(ξ)}` at generic points `ξ`); every smooth point lies
> on such a piece, and on the others `ω_{X/Y}` vanishes and the map is taken to be zero. The
> extension across `X ∖ U` by [Stacks, Tag 0E9I] needs `depth(ω_{X/Y,x}) ≥ 2` there; the `(S₂)`
> property of [Stacks, Tag 0E9V] does not give this alone, and it is proved as
> `min(2, dim 𝒪_{X,x}) ≤ depth(ω_{X/Y,x})`
> (`Stacks.Duality.min_two_ringKrullDim_le_moduleDepth_modulesStalk_homology_upperShriek`).

```lean
theorem exists_map_exteriorPower_isIso_of_smoothAt {S : Scheme.{u}} [IsNoetherian S]
    {X Y : FTS S} (f : X ⟶ Y) (r : ℕ) (hY : AlgebraicGeometry.IsCohenMacaulay Y.left)
    {P : Scheme.{u}} (ι : X.left ⟶ P) [IsImmersion ι] (g : P ⟶ Y.left) [Smooth g] [IsProper g]
    (hfac : ι ≫ g = f.left)
    (hK : ∀ x : X.left, ringKrullDim (X.left.presheaf.stalk x) ≤ 1 → KoszulAt f.left x)
    (htr : ∀ ξ : X.left, closure {ξ} ∈ irreducibleComponents X.left →
      Stacks.Chow.residueTrdeg f.left ξ = (r : Cardinal))
    (j : CompactificationOf (Over.mk f.left)) :
    ∃ φ : Scheme.Modules.exteriorPower (Scheme.Hom.relativeDifferentials f.left) (r : ℤ) ⟶
        upperShriekHomology f j (-(r : ℤ)),
      ∀ x : X.left, InfinitesimalLifting.SmoothAt f.left x →
        IsIso (AlgebraicGeometry.SheafOfModules.stalkMap
          (Sheaf.toRingCat (Opens.grothendieckTopology
            ↥X.left.toLocallyRingedSpace.toRingedSpace.carrier)
            X.left.toLocallyRingedSpace.toRingedSpace.sheaf) x φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.29, Tag 0E9X](https://stacks.math.columbia.edu/tag/0E9X)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
