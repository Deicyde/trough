---
declaration: section
origin: cited
lean: Crystalline.DividedPowerStructure, Crystalline.DividedPowerScheme, Crystalline.DividedPowerScheme.Hom, Crystalline.SchemeThickening, Crystalline.DividedPowerScheme.instHasPullbacksDividedPowerScheme, Crystalline.DividedPowerScheme.underlyingPullbackComparison_isClosedImmersion, Crystalline.DividedPowerScheme.closedFiberPullbackComparison_fst, Crystalline.DividedPowerScheme.closedFiberPullbackComparison_snd
statement: formalized
proof: formalized
---

# 60.7 Divided power schemes

Section 60.7 of the Stacks Project, [Tag 07I1](https://stacks.math.columbia.edu/tag/07I1). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07I2, a definition

[Tag 07I2](https://stacks.math.columbia.edu/tag/07I2) in the Stacks Project.

**`Crystalline.DividedPowerStructure`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Scheme.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Scheme.lean#L99).

> A divided power structure on a sheaf of ideals: every ideal of sections has divided powers,
> and every restriction map is compatible with them.

```lean
public structure DividedPowerStructure (O : Sheaf J CommRingCat.{w})
    (I : (SheafOfModules.unit (ringSheaf O)).Submodule)
```

## Tag 07I3, a definition

[Tag 07I3](https://stacks.math.columbia.edu/tag/07I3) in the Stacks Project.

**`Crystalline.DividedPowerScheme`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Scheme.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Scheme.lean#L234). The attribute's comment: “divided power schemes”.

> A scheme equipped with a quasi-coherent sheaf of ideals and a divided power structure on
> that ideal.

```lean
public structure DividedPowerScheme
```

**`Crystalline.DividedPowerScheme.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Scheme.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/Scheme.lean#L254). The attribute's comment: “morphisms of divided power schemes”.

> A morphism of divided power schemes. On each open subset of the target, the induced map on
> sections is a homomorphism of divided power rings. In particular, it maps the target ideal into
> the source ideal.

```lean
public structure Hom (X Y : DividedPowerScheme.{u})
```

## Tag 07I4, a definition

[Tag 07I4](https://stacks.math.columbia.edu/tag/07I4) in the Stacks Project.

**`Crystalline.SchemeThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/Basic.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/Basic.lean#L76).

> **A divided power thickening of schemes.**  A thickening `immersion : source ⟶ target.scheme`
> whose defining ideal is, on every affine open, the divided power ideal of `target`.

```lean
structure SchemeThickening
```

## Tag 07ME, a lemma

[Tag 07ME](https://stacks.math.columbia.edu/tag/07ME) in the Stacks Project.

**`Crystalline.DividedPowerScheme.instHasPullbacksDividedPowerScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean#L123). The attribute's comment: “existence of fibre products”.

> Divided power schemes admit fibre products.

```lean
public instance instHasPullbacksDividedPowerScheme :
    HasPullbacks (DividedPowerScheme.{u})
```

**`Crystalline.DividedPowerScheme.underlyingPullbackComparison_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean#L159). The attribute's comment: “closed immersion into the ordinary fibre product”.

> The underlying scheme of the divided power fibre product is a closed subscheme
> of the ordinary scheme-theoretic fibre product.

```lean
public theorem underlyingPullbackComparison_isClosedImmersion :
    IsClosedImmersion (underlyingPullbackComparison f f')
```

**`Crystalline.DividedPowerScheme.closedFiberPullbackComparison_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean#L205). The attribute's comment: “closed-fibre comparison commutes with first projection”.

> The closed-fibre comparison followed by the first projection is the closed fibre of the
> first projection.

```lean
public theorem closedFiberPullbackComparison_fst :
    closedFiberPullbackComparison f f' ≫
      pullback.fst (closedFiberMap f) (closedFiberMap f') =
        closedFiberMap (pullback.fst f f')
```

**`Crystalline.DividedPowerScheme.closedFiberPullbackComparison_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean#L214). The attribute's comment: “closed-fibre comparison commutes with second projection”.

> The closed-fibre comparison followed by the second projection is the closed fibre of the
> second projection.

```lean
public theorem closedFiberPullbackComparison_snd :
    closedFiberPullbackComparison f f' ≫
      pullback.snd (closedFiberMap f) (closedFiberMap f') =
        closedFiberMap (pullback.snd f f')
```

**`Crystalline.DividedPowerScheme.closedFiberPullbackComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FibreProduct/Existence.lean#L222). The attribute's comment: “fibre product of closed fibres”.

> The canonical comparison of closed fibres is an isomorphism.

```lean
public theorem closedFiberPullbackComparison_isIso :
    IsIso (closedFiberPullbackComparison f f')
```

## Tag 07MF, a situation

[Tag 07MF](https://stacks.math.columbia.edu/tag/07MF) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/Basic.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/Basic.lean#L107).

> The standing global crystalline situation: a prime `p`, a divided power scheme `(S, I, γ)`
> over `ℤ_(p)`, and a scheme `X` over the closed fibre `S₀ = V(I)` on which `p` is locally
> nilpotent.

```lean
structure GlobalCrystallineSituation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.7, Tag 07I1](https://stacks.math.columbia.edu/tag/07I1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
