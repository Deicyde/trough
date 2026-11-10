---
declaration: section
origin: cited
lean: Stacks.Cohomology.ToposBaseChange.baseChangeMap, Stacks.Cohomology.ToposBaseChange.baseChangeMap_fac
statement: formalized
proof: formalized
---

# 21.15 The base change map

Section 21.15 of the Stacks Project, [Tag 0735](https://stacks.math.columbia.edu/tag/0735). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0736, a lemma

[Tag 0736](https://stacks.math.columbia.edu/tag/0736) in the Stacks Project.

**`Stacks.Cohomology.ToposBaseChange.baseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/FlatBaseChange.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/FlatBaseChange.lean#L179). The attribute's comment: “base-change morphism”.

> **The base change map** `g^* Rf_* ⟶ R(f')_* (g')^*` of a commutative square of ringed topoi
> whose horizontal morphisms `g` and `g'` are flat, on bounded below derived categories of sheaves
> of modules: the descent of the underived base change map `moduleBaseChange` to bounded below
> derived categories.

```lean
def baseChangeMap :
    (pushforwardModules f.toRingedToposModulesHom).rightDerivedFunctorPlus ⋙
        flatPullback g hg ⟶
      flatPullback g' hg' ⋙
        (pushforwardModules f'.toRingedToposModulesHom).rightDerivedFunctorPlus
```

**`Stacks.Cohomology.ToposBaseChange.baseChangeMap_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/FlatBaseChange.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/FlatBaseChange.lean#L194). The attribute's comment: “canonical characterization”.

> Composed with the derived-functor unit of `Rf_*`, the base change map `baseChangeMap` is the
> comparison `baseChangeOnHomotopyCategory` on the bounded below homotopy category.

```lean
theorem baseChangeMap_fac :
    Functor.whiskerRight
        (pushforwardModules f.toRingedToposModulesHom).rightDerivedFunctorPlusUnith
        (flatPullback g hg) ≫
      (Functor.associator _ _ _).hom ≫
      Functor.whiskerLeft DerivedCategory.Plus.Qh (baseChangeMap f f' g g' comm hg hg') =
        baseChangeOnHomotopyCategory f f' g g' comm hg hg'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.15, Tag 0735](https://stacks.math.columbia.edu/tag/0735)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
