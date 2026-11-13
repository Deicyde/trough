---
declaration: section
origin: cited
lean: Stacks.Cohomology.FlatBaseChange.baseChangeMap, Stacks.Cohomology.FlatBaseChange.baseChangeMap_fac
statement: formalized
proof: formalized
---

# 20.17 The base change map

Section 20.17 of the Stacks Project, [Tag 02N6](https://stacks.math.columbia.edu/tag/02N6). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02N7, a lemma

[Tag 02N7](https://stacks.math.columbia.edu/tag/02N7) in the Stacks Project.

**`Stacks.Cohomology.FlatBaseChange.baseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/FlatBaseChange.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/FlatBaseChange.lean#L209). The attribute's comment: “base-change morphism”.

> **Stacks 02N7, the base change map.** For a commutative diagram of ringed spaces whose
> horizontal morphisms `g` and `g'` are flat, the canonical map
>
> `g^* Rf_* ⟶ R(f')_* (g')^*`
>
> of functors on bounded below derived categories of sheaves of modules, so in particular
> `g^* Rf_* ℱ^• ⟶ R(f')_* (g')^* ℱ^•` in `D⁺(S')` for every bounded below complex `ℱ^•` of
> `𝒪_X`-modules. It is the descent of the underived base change map along the derived-functor unit
> of `Rf_*`, and `baseChangeMap_fac` says that this determines it.

```lean
def baseChangeMap :
    (modulePushforward f).rightDerivedFunctorPlus ⋙ flatPullback g hg ⟶
      flatPullback g' hg' ⋙ (modulePushforward f').rightDerivedFunctorPlus
```

**`Stacks.Cohomology.FlatBaseChange.baseChangeMap_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/FlatBaseChange.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/FlatBaseChange.lean#L222). The attribute's comment: “canonical characterization”.

> **Stacks 02N7, canonicity of the base change map.** Composed with the derived-functor unit
> of `Rf_*`, the base change map is the comparison `baseChangeOnHomotopyCategory` on the bounded
> below homotopy category. Since `Rf_* ⋙ g^*` is a right derived functor of `f_* ⋙ g^*` with that
> unit, this equation determines the base change map; it is the sense in which the map of the
> source is canonical rather than merely existing.

```lean
theorem baseChangeMap_fac :
    Functor.whiskerRight (modulePushforward f).rightDerivedFunctorPlusUnith
        (flatPullback g hg) ≫
      (Functor.associator _ _ _).hom ≫
      Functor.whiskerLeft DerivedCategory.Plus.Qh (baseChangeMap f f' g g' comm hg hg') =
        baseChangeOnHomotopyCategory f f' g g' comm hg hg'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.17, Tag 02N6](https://stacks.math.columbia.edu/tag/02N6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
