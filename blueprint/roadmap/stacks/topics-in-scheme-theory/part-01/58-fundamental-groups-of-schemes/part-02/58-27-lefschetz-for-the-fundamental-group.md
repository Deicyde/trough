---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_depthAddDim, Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_isProper, Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_neighborhood_of_isProper, Stacks.FundamentalGroup.finiteEtaleColimitEquivalence_zeroScheme_of_depth, Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_zeroScheme_of_hasPurity_of_depth, Stacks.FundamentalGroup.connectedSpace_zeroScheme_iff_of_hasPurity_of_depth, Stacks.FundamentalGroup.fundamentalGroupEquiv_zeroScheme_of_hasPurity_of_depth
statement: formalized
proof: formalized
---

# 58.27 Lefschetz for the fundamental group

Section 58.27 of the Stacks Project, [Tag 0ELB](https://stacks.math.columbia.edu/tag/0ELB). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ELC, a proposition

[Tag 0ELC](https://stacks.math.columbia.edu/tag/0ELC) in the Stacks Project.

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_depthAddDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean#L253). The attribute's comment: “first statement: restriction FÉt_X → FÉt_Y to the zero scheme of a section of an ample invertible module is fully faithful. Nothing is carried: Stacks 0EL1 is isIso_zeroSchemeComparison_of_isProper, and the passage from it to full faithfulness is the formalized Stacks 0EKP chain followed by Stacks 0EL8”. References: SGA 1 X (2.13), “partial”.

> **[Stacks, Tag 0ELC], first statement.** Let `k` be a field, `X` a proper scheme over `k`,
> `L` an ample invertible `𝒪_X`-module, `s ∈ Γ(X, L)` and `Y = Z(s)` the zero scheme of `s`. If
> `depth(𝒪_{X, x}) + dim({x}‾) > 1` at every point `x` of `X` outside `Y`, then the restriction
> functor `FÉt_X ⟶ FÉt_Y` is fully faithful.
>
> The statement is that of
> `Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_isProper`, and
> **nothing is carried here**: the source's appeal to
> Algebraic and Formal Geometry, Proposition [Stacks, Tag 0EL1] is
> `Stacks.Algebraization.isIso_zeroSchemeComparison_of_isProper`, and the route from there to full
> faithfulness runs through conditions (2) and (4) of [Stacks, Tag 0EKP] rather than through
> [Stacks, Tag 0EJZ]; see the module documentation for the chain. This is the full faithfulness that
> the source uses in [Stacks, Tag 0ELE].
>
> `CategoryTheory.Functor.FullyFaithful` carries the inverse map on hom sets as data, so full
> faithfulness is recorded as `Nonempty _.FullyFaithful`. `X` is
> Noetherian by `Stacks.FundamentalGroup.isNoetherian_of_isProper_of_isAmple`.

```lean
public theorem fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_depthAddDim
    (hdepth : DepthAddDimGtOneOutsideSupport X (zeroScheme X L s)) :
    Nonempty (finiteEtaleBaseChange (zeroScheme X L s).subschemeι).FullyFaithful
```

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemeRestrictionFromDepth.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemeRestrictionFromDepth.lean#L78). The attribute's comment: “first statement: restriction FÉt_X → FÉt_Y to the zero scheme of a section of an ample invertible module on a proper scheme over a field is fully faithful when depth + dim > 1 off the zero scheme”. References: SGA 1 X (2.13), “partial”.

> **[Stacks, Tag 0ELC], first statement.** Let `k` be a field, `X` a proper scheme over `k`,
> `L` an ample invertible `𝒪_X`-module, `s ∈ Γ(X, L)` and `Y = Z(s)` the zero scheme of `s`. If
> `depth(𝒪_{X, x}) + dim({x}‾) > 1` at every point `x` of `X ∖ Y`, then the restriction functor
> `FÉt_X ⟶ FÉt_Y` is fully faithful.
>
> `CategoryTheory.Functor.FullyFaithful` carries the inverse map on hom sets as data, so full
> faithfulness is stated as `Nonempty _.FullyFaithful`.

```lean
public theorem fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_isProper
    (k : Type u) [Field k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L]
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple X L) (s : Γ(L, ⊤))
    (hdepth : DepthAddDimGtOneOutsideSupport X (zeroScheme X L s)) :
    Nonempty (finiteEtaleBaseChange (zeroScheme X L s).subschemeι).FullyFaithful
```

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_neighborhood_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemeRestrictionFromDepth.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemeRestrictionFromDepth.lean#L99). The attribute's comment: “second statement: restriction FÉt_V → FÉt_Y is fully faithful for every open V of X containing the zero scheme”. References: SGA 1 X (2.13), “partial”; SGA 2 XII (3.5), “more general”.

> **[Stacks, Tag 0ELC], second statement.** In the situation of
> `Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_isProper`, the
> restriction functor `FÉt_V ⟶ FÉt_Y` is fully faithful for every open subscheme `V ⊆ X`
> containing `Y`.
>
> The open subschemes containing `Y` are `Stacks.FundamentalGroup.Neighborhood X Y`, and the
> closed immersion `Y ⟶ V` is `Stacks.FundamentalGroup.Neighborhood.toSchemeHom`.

```lean
public theorem fullyFaithful_finiteEtaleBaseChange_neighborhood_of_isProper
    (k : Type u) [Field k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L]
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple X L) (s : Γ(L, ⊤))
    (hdepth : DepthAddDimGtOneOutsideSupport X (zeroScheme X L s))
    (W : Neighborhood X (zeroScheme X L s)) :
    Nonempty (finiteEtaleBaseChange
      (Neighborhood.toSchemeHom X (zeroScheme X L s) W)).FullyFaithful
```

## Tag 0ELD, a proposition

[Tag 0ELD](https://stacks.math.columbia.edu/tag/0ELD) in the Stacks Project.

**`Stacks.FundamentalGroup.finiteEtaleColimitEquivalence_zeroScheme_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemeFiniteEtaleEquivalence.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemeFiniteEtaleEquivalence.lean#L100). The attribute's comment: “the restriction functor colim_V FÉt_V → FÉt_Y is an equivalence, stated as its fully faithful half and its essentially surjective half, at exactly the source's hypotheses”.

> **Stacks Project, Tag 0ELD.** Let `k` be a field, `X` a proper scheme over `k`, `L` an ample
> invertible `𝒪_X`-module, `s ∈ Γ(X, L)`, `Y = Z(s)` the zero scheme of `s`, and `𝒱` the open
> subschemes of `X` containing `Y`, ordered by reverse inclusion. If
> `depth(𝒪_{X, x}) + dim({x}‾) > 2` for every `x ∈ X ∖ Y`, then the restriction functor
> `colim_𝒱 FÉt_V ⟶ FÉt_Y` is an equivalence.
>
> The equivalence `colim_𝒱 FÉt_V ≃ FÉt_Y` is stated as its two halves: the restriction functor is
> fully faithful (`FiniteEtaleColimitFullyFaithful X Y`: morphisms of restrictions to `Y` come from
> morphisms over a smaller neighbourhood, and morphisms with equal restrictions to `Y` agree over a
> smaller neighbourhood), and essentially surjective (every finite étale cover of `Y` is the
> restriction of a finite étale cover of some open neighbourhood of `Y`).

```lean
public theorem finiteEtaleColimitEquivalence_zeroScheme_of_depth
    (k : Type u) [Field k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsProper g]
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L]
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple X L) (s : Γ(L, ⊤))
    (hdepth : DepthAddDimGtTwoOutsideSupport X (zeroScheme X L s)) :
    FiniteEtaleColimitFullyFaithful X (zeroScheme X L s) ∧
      ∀ A : FiniteEtaleOver (zeroScheme X L s).subscheme,
        ∃ (W : Neighborhood X (zeroScheme X L s))
          (U : FiniteEtaleOver (Neighborhood.open X (zeroScheme X L s) W).toScheme),
          Nonempty ((finiteEtaleBaseChange
            (Neighborhood.toSchemeHom X (zeroScheme X L s) W)).obj U ≅ A)
```

## Tag 0ELE, a proposition

[Tag 0ELE](https://stacks.math.columbia.edu/tag/0ELE) in the Stacks Project.

**`Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_zeroScheme_of_hasPurity_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean#L452). The attribute's comment: “first conclusion: restriction FÉt_X → FÉt_Y to the zero scheme of a section of an ample invertible module is an equivalence”. References: SGA 1 X (2.13), “more general”; SGA 2 XII (3.5), “special case”.

> **[Stacks, Tag 0ELE], the first conclusion.** Let `k` be a field, `X` a proper scheme over
> `k`, `L` an ample invertible `𝒪_X`-module, `s ∈ Γ(X, L)` and `Y = Z(s)` the zero scheme of `s`.
> Assume that `depth(𝒪_{X, x}) + dim({x}‾) > 2` for every `x ∈ X ∖ Y`, and that purity holds for
> `𝒪_{X, x}` at every closed `x ∈ X ∖ Y`. Then the restriction functor `FÉt_X ⟶ FÉt_Y` is an
> equivalence.
>
> The proof is the source's. Full faithfulness is
> `Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_zeroScheme_of_depthAddDim`
> ([Stacks, Tag 0ELC]), whose bound `> 1` follows from the bound `> 2` assumed here. For essential
> surjectivity, [Stacks, Tag 0ELD] writes a given finite étale cover of `Y` as the restriction of a
> finite étale cover of an open neighbourhood `V` of `Y`; every point of `X ∖ V` is a closed point
> off `Y`, because its closure misses `Y` and so lies in the affine open where `s` does not vanish,
> and purity therefore holds there, so [Stacks, Tag 0EY7] extends the cover from `V` to all of `X`.
>
> The depth hypothesis is `Stacks.FundamentalGroup.DepthAddDimGtTwoOutsideSupport`, which unfolds
> to the displayed inequality in the extended integers.

```lean
public theorem isEquivalence_finiteEtaleBaseChange_zeroScheme_of_hasPurity_of_depth
    (hdepth : DepthAddDimGtTwoOutsideSupport X (zeroScheme X L s))
    (hpurity : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) → IsClosed ({x} : Set X) →
      AlgebraicGeometry.HasPurity (X.presheaf.stalk x)) :
    (finiteEtaleBaseChange (zeroScheme X L s).subschemeι).IsEquivalence
```

**`Stacks.FundamentalGroup.connectedSpace_zeroScheme_iff_of_hasPurity_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean#L467). The attribute's comment: “the "or equivalently": X is connected if and only if its zero scheme Y = Z(s) is”.

> **[Stacks, Tag 0ELE], the "or equivalently".** In the situation of
> `Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_zeroScheme_of_hasPurity_of_depth` the
> zero scheme `Y = Z(s)` is connected exactly when `X` is. This is [Stacks, Tag 0BQA] part (2)
> applied to the equivalence `FÉt_X ⟶ FÉt_Y`.

```lean
public theorem connectedSpace_zeroScheme_iff_of_hasPurity_of_depth
    (hdepth : DepthAddDimGtTwoOutsideSupport X (zeroScheme X L s))
    (hpurity : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) → IsClosed ({x} : Set X) →
      AlgebraicGeometry.HasPurity (X.presheaf.stalk x)) :
    ConnectedSpace (zeroScheme X L s).subscheme ↔ ConnectedSpace X
```

**`Stacks.FundamentalGroup.fundamentalGroupEquiv_zeroScheme_of_hasPurity_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LefschetzZeroSchemePurity.lean#L488). The attribute's comment: “second conclusion: for X, equivalently Y, connected, the induced map π₁(Y, y‾) → π₁(X, y‾) is an isomorphism of topological groups at every geometric point of Y”. References: SGA 1 X (2.13), “more general”; SGA 2 X (3.10), “special case”; SGA 2 XII (4.9), “4.9 a), special case”.

> **[Stacks, Tag 0ELE], the second conclusion.** In the situation of
> `Stacks.FundamentalGroup.isEquivalence_finiteEtaleBaseChange_zeroScheme_of_hasPurity_of_depth`,
> with `X` and `Y = Z(s)` connected, the map `π₁(Y, y‾) ⟶ π₁(X, y‾)` induced by the closed immersion
> is an isomorphism of topological groups for every geometric point `y‾` of `Y`. The isomorphism
> produced is the canonical induced map `AlgebraicGeometry.etaleFundamentalGroupMap`. This is
> [Stacks, Tag 0BQA] part (2), the lemma the source's proof quotes for the `π₁` statement.

```lean
public theorem fundamentalGroupEquiv_zeroScheme_of_hasPurity_of_depth
    (hdepth : DepthAddDimGtTwoOutsideSupport X (zeroScheme X L s))
    (hpurity : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) → IsClosed ({x} : Set X) →
      AlgebraicGeometry.HasPurity (X.presheaf.stalk x))
    [ConnectedSpace (zeroScheme X L s).subscheme] [ConnectedSpace X]
    (y : AlgebraicGeometry.GeometricPoint (zeroScheme X L s).subscheme) :
    ∃ e : AlgebraicGeometry.EtaleFundamentalGroup (zeroScheme X L s).subscheme y ≃ₜ*
        AlgebraicGeometry.EtaleFundamentalGroup X (y.map (zeroScheme X L s).subschemeι),
      ∀ σ : AlgebraicGeometry.EtaleFundamentalGroup (zeroScheme X L s).subscheme y,
        e σ = AlgebraicGeometry.etaleFundamentalGroupMap
          (zeroScheme X L s).subschemeι y σ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.27, Tag 0ELB](https://stacks.math.columbia.edu/tag/0ELB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
