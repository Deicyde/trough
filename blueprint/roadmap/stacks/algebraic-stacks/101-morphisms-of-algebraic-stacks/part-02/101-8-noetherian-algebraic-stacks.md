---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsNoetherianStack, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyNoetherian_of_isImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.hasRelativeProperty_quasiCompact_of_isImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.isNoetherianStack_of_isImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyNoetherianSpace_points_of_isLocallyNoetherian, AlgebraicGeometry.Stack.AlgebraicStacks.noetherianSpace_points_of_isQuasiCompactStack, AlgebraicGeometry.Stack.AlgebraicStacks.quasiSober_points_of_isLocallyNoetherian
statement: formalized
proof: formalized
---

# 101.8 Noetherian algebraic stacks

Section 101.8 of the Stacks Project, [Tag 050Z](https://stacks.math.columbia.edu/tag/050Z). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0510, a definition

[Tag 0510](https://stacks.math.columbia.edu/tag/0510) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsNoetherianStack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianStack.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianStack.lean#L72).

> **Stacks 0510**, verbatim: *"Let `𝒳` be an algebraic stack. We say `𝒳` is Noetherian if `𝒳`
> is quasi-compact, quasi-separated and locally Noetherian."*
>
> Quasi-compactness is `AlgebraicGeometry.Stack.IsQuasiCompactStack` (**Stacks 04YB**),
> quasi-separatedness is the absolute axiom `AlgebraicGeometry.Stack.IsQuasiSeparatedAbs`
> (**Stacks 050D**, part (8)) and local Noetherianity is the smooth-scheme-atlas criterion
> `AlgebraicGeometry.Stack.HasPropertyOnSomeSchemeAtlas` of **Stacks 04YG** at
> `AlgebraicGeometry.IsLocallyNoetherian`.

```lean
noncomputable abbrev IsNoetherianStack (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

## Tag 0CPM, a lemma

[Tag 0CPM](https://stacks.math.columbia.edu/tag/0CPM) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyNoetherian_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianAlgebraicStack.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianAlgebraicStack.lean#L228). The attribute's comment: “part (1): the source is locally Noetherian”.

> **Stacks 0CPM, part (1), first half**, verbatim: *"Let `j : 𝒳 → 𝒴` be an immersion of
> algebraic stacks. If `𝒴` is locally Noetherian, then `𝒳` is locally Noetherian [and `j` is
> quasi-compact]."* Local Noetherianity of an algebraic stack over `S` is the smooth-scheme-atlas
> criterion of **Stacks 04YG** at `AlgebraicGeometry.IsLocallyNoetherian`.
>
> The 2-fibre product `𝒫 = V ×_𝒴 𝒳` of a locally Noetherian smooth surjective scheme chart
> `g : V ⟶ 𝒴` with `j` has first projection a base change of `j`, so `𝒫` is representable by an
> algebraic space `F` and the induced morphism `F ⟶ V` is locally of finite type; `F` is then
> locally Noetherian by Stacks 04ZK, and an étale scheme chart of `F` composed with the second
> projection — a base change of `g`, hence smooth and surjective — is a locally Noetherian scheme
> atlas of `𝒳`.
>
> Quasi-compactness of `j`, the other half of part (1), and part (2) are in
> `StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactImmersion.lean`, which consumes this
> statement.

```lean
theorem isLocallyNoetherian_of_isImmersion
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (j : 𝒳 ⟶ 𝒴) (hj : IsImmersion B S hS j)
    (hY : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴) :
    HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.hasRelativeProperty_quasiCompact_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactImmersion.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactImmersion.lean#L97). The attribute's comment: “part (1): the 1-morphism is quasi-compact, in the sense of Stacks 03YK”.

> Let `j : 𝒳 ⟶ 𝒴` be an immersion of algebraic stacks, where `𝒴` has a smooth surjective
> scheme atlas with locally Noetherian source. Then `j` is quasi-compact: it has the relative
> property of Stacks 03YK at quasi-compactness of morphisms of algebraic spaces.

```lean
theorem hasRelativeProperty_quasiCompact_of_isImmersion
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (j : 𝒳 ⟶ 𝒴) (hj : IsImmersion B S hS j)
    (hY : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴) :
    HasRelativeProperty.{u, u, u + 1, u} B S hS
      (Space.quasiCompactProperty B S hS) j.hom hj.1
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isNoetherianStack_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactImmersion.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactImmersion.lean#L164). The attribute's comment: “part (2): the source is Noetherian”.

> Let `j : 𝒳 ⟶ 𝒴` be an immersion of algebraic stacks. If `𝒴` is Noetherian, then `𝒳` is
> Noetherian.

```lean
theorem isNoetherianStack_of_isImmersion
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (j : 𝒳 ⟶ 𝒴) (hj : IsImmersion B S hS j)
    (hY : IsNoetherianStack.{u, w, w'} B S hS 𝒴) :
    IsNoetherianStack.{u, w, w'} B S hS 𝒳
```

## Tag 0DQI, a lemma

[Tag 0DQI](https://stacks.math.columbia.edu/tag/0DQI) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyNoetherianSpace_points_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianPointsAlgebraicStack.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianPointsAlgebraicStack.lean#L150). The attribute's comment: “part (1)”.

> **Stacks 0DQI, part (1).** The space of points of Stacks 04XL of a locally Noetherian
> algebraic stack over `S` is a locally Noetherian topological space.
>
> Local Noetherianity of the stack is read as the existential atlas condition of Stacks 04YF: a
> smooth surjective 1-morphism from the algebraic stack of a locally Noetherian scheme `U` of the
> site. The point space of that algebraic stack is the topological space of `U`, which is locally
> Noetherian by Stacks 01OZ, and the chart is open on points by Stacks 06R7 and surjective on points
> by the definition of Stacks 04ZS, so Stacks 04Z8 part (2) carries local Noetherianity across.

```lean
theorem isLocallyNoetherianSpace_points_of_isLocallyNoetherian
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hN : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳) :
    letI := Stack.pointTopology B S hS 𝒳.val
    IsLocallyNoetherianSpace (Stack.points B S hS 𝒳.val.val 𝒳.val.property)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.noetherianSpace_points_of_isQuasiCompactStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianPointsAlgebraicStack.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianPointsAlgebraicStack.lean#L170). The attribute's comment: “part (2)”.

> **Stacks 0DQI, part (2).** The space of points of Stacks 04XL of a quasi-compact locally
> Noetherian algebraic stack over `S` is a Noetherian topological space.
>
> Quasi-compactness of Stacks 04YB is compactness of the point space, so this is Stacks 04ZB applied
> to part (1). The name records only the quasi-compactness hypothesis; the local-Noetherianity
> hypothesis is the same atlas condition part (1) carries.

```lean
theorem noetherianSpace_points_of_isQuasiCompactStack
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hqc : Stack.IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (hN : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳) :
    letI := Stack.pointTopology B S hS 𝒳.val
    NoetherianSpace (Stack.points B S hS 𝒳.val.val 𝒳.val.property)
```

## Tag 0GVX, a lemma

[Tag 0GVX](https://stacks.math.columbia.edu/tag/0GVX) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasiSober_points_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianPointsAlgebraicStack.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianPointsAlgebraicStack.lean#L192).

> **Stacks 0GVX.** The space of points of Stacks 04XL of a locally Noetherian algebraic stack
> over `S` is quasi-sober in the sense of Stacks 004X: every irreducible closed subset of it has a
> generic point.
>
> Local Noetherianity is read as the atlas condition of Stacks 04YF, which supplies a smooth
> surjective 1-morphism from the algebraic stack of a locally Noetherian scheme `U` of the site.
> The point space of that algebraic stack is the topological space of `U`, hence is quasi-sober and
> locally Noetherian, and the chart is continuous, open and surjective on points, so quasi-sobriety
> passes to `|𝒳|`.

```lean
theorem quasiSober_points_of_isLocallyNoetherian
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hN : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳) :
    letI := Stack.pointTopology B S hS 𝒳.val
    QuasiSober (Stack.points B S hS 𝒳.val.val 𝒳.val.property)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.8, Tag 050Z](https://stacks.math.columbia.edu/tag/050Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
