---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_surjective_isLocallyProjective_iff_forall, AlgebraicGeometry.Space.IsLocallyProjective, AlgebraicGeometry.Space.isLocallyProjective_restrictToChartScheme_modulePullback, AlgebraicGeometry.Space.isLocallyProjective_restrictToChartScheme_modulePullback_of_isQuasicoherentOnSite
statement: formalized
proof: formalized
---

# 66.31 Locally projective modules

Section 66.31 of the Stacks Project, [Tag 060P](https://stacks.math.columbia.edu/tag/060P). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 060Q, a lemma

[Tag 060Q](https://stacks.math.columbia.edu/tag/060Q) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_surjective_isLocallyProjective_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjectiveEtaleChart.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjectiveEtaleChart.lean#L252).

> **Stacks Project, Tag 060Q.** The restriction of an `𝒪_F`-module to the Zariski site of an
> étale chart scheme is locally projective for *some* chart whose structure morphism is surjective
> on points if and only if it is locally projective for *every* étale chart.
>
> The implication from one chart to all of them is
> `AlgebraicGeometry.Space.isLocallyProjective_restrictToChartScheme_of_isSurjective`; the
> converse needs only that an algebraic space has a chart surjective on points at all, namely its
> atlas.  Quasi-coherence of `M` is the source's standing hypothesis on the module.

```lean
theorem exists_surjective_isLocallyProjective_iff_forall
    (hF : IsAlgebraicSpace B S hS F) (M : Modules.{u, u} B S hS F hF)
    (hM : M.IsQuasicoherentOnSite) :
    (∃ U : SmallEtale B S hS F, IsSurjective B S hS U.1.hom ∧
        Scheme.Modules.IsLocallyProjective (restrictToChartScheme B S hS F hF M U)) ↔
      ∀ U : SmallEtale B S hS F,
        Scheme.Modules.IsLocallyProjective (restrictToChartScheme B S hS F hF M U)
```

## Tag 060R, a definition

[Tag 060R](https://stacks.math.columbia.edu/tag/060R) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocallyProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjective.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjective.lean#L49).

> **Stacks 060R.** A quasi-coherent module on an algebraic space is locally projective if its
> restriction to every étale scheme chart is locally projective.

```lean
noncomputable abbrev IsLocallyProjective (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (F : QuasicoherentSheaves.{u, m} B S hS X hX) : Prop
```

## Tag 060S, a lemma

[Tag 060S](https://stacks.math.columbia.edu/tag/060S) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyProjective_restrictToChartScheme_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjectiveEtaleChart.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjectiveEtaleChart.lean#L278).

> **Stacks Project, Tag 060S.** The pullback of a locally projective `𝒪_Y`-module along a
> morphism `f : X ⟶ Y` of algebraic spaces is locally projective.
>
> The source's reduction: choose an étale chart `V` of `Y` surjective on points and lift it
> through `f` to an étale chart `U` of `X` surjective on points together with `ψ : U ⟶ V` making
> the square commute (Stacks 02X1).  Then `(f^*G)|_U` is the pullback of `G|_V` along `ψ`, so it
> is locally projective by Stacks 060M, and Stacks 060Q propagates that to every chart of `X`.
>
> See the implementation notes for the carried hypotheses: `hqcY` is Zariski quasi-coherence of the
> chart restrictions of `G`, `hqcX` is quasi-coherence of `f^*G` on the small étale site of `X`,
> and `hsquare` is the base-change identity `(f^*G)|_U ≅ ψ^*(G|_V)` at a commuting square of charts
> of `f`.

```lean
theorem isLocallyProjective_restrictToChartScheme_modulePullback
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (G : Modules.{u, u} B S hS Y.1 Y.2)
    (hqcY : ∀ V : SmallEtale B S hS Y.1,
      (restrictToChartScheme B S hS Y.1 Y.2 G V).IsQuasicoherent)
    (hqcX : ((modulePullback B S hS f).obj G).IsQuasicoherentOnSite)
    (hsquare : ∀ (U : SmallEtale B S hS X.1) (V : SmallEtale B S hS Y.1)
        (ψ : U.1.left ⟶ V.1.left), U.1.hom ≫ f.hom = yoneda.map ψ ≫ V.1.hom →
      (restrictToChartScheme B S hS X.1 X.2 ((modulePullback B S hS f).obj G) U ≅
        (Scheme.Modules.pullback ((BigFppfOver.toScheme B S hS).map ψ)).obj
          (restrictToChartScheme B S hS Y.1 Y.2 G V)))
    (hG : ∀ V : SmallEtale B S hS Y.1,
      Scheme.Modules.IsLocallyProjective (restrictToChartScheme B S hS Y.1 Y.2 G V))
    (U : SmallEtale B S hS X.1) :
    Scheme.Modules.IsLocallyProjective
      (restrictToChartScheme B S hS X.1 X.2 ((modulePullback B S hS f).obj G) U)
```

**`AlgebraicGeometry.Space.isLocallyProjective_restrictToChartScheme_modulePullback_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjectivePullbackSpaces.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LocallyProjectivePullbackSpaces.lean#L133).

> **Stacks Project, Tag 060S.**  The inverse image of Stacks 03LU of a quasi-coherent
> `𝒪_Y`-module whose chart restrictions are locally projective has locally projective chart
> restrictions: local projectivity of a quasi-coherent module on an algebraic space is stable
> under pullback along an arbitrary morphism of algebraic spaces.
>
> Choose an étale chart `V` of `Y` surjective on points and lift it through `f` to an étale chart
> `U₀` of `X` surjective on points with `ψ : U₀ ⟶ V` making the square commute (Stacks 02X1).
> Then `(f^*G)|_{U₀}` is the pullback of `G|_V` along `ψ`, so it is locally projective by
> Stacks 060M, and Stacks 060Q propagates that to every chart of `X`; quasi-coherence of `f^*G`,
> which the latter step needs, is Stacks 03GA.

```lean
theorem isLocallyProjective_restrictToChartScheme_modulePullback_of_isQuasicoherentOnSite
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (G : Modules.{u, u} B S hS Y.1 Y.2)
    (hG : G.IsQuasicoherentOnSite)
    (hproj : ∀ V : SmallEtale B S hS Y.1,
      Scheme.Modules.IsLocallyProjective (restrictToChartScheme B S hS Y.1 Y.2 G V))
    (U : SmallEtale B S hS X.1) :
    Scheme.Modules.IsLocallyProjective
      (restrictToChartScheme B S hS X.1 X.2 ((modulePullback B S hS f).obj G) U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.31, Tag 060P](https://stacks.math.columbia.edu/tag/060P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
