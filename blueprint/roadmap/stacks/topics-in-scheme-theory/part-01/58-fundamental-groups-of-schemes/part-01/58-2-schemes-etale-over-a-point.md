---
declaration: section
origin: cited
lean: AlgebraicGeometry.ContinuousGSet.ofMulAction, AlgebraicGeometry.ContinuousGSet.homEquiv, AlgebraicGeometry.ContinuousGSet, AlgebraicGeometry.etaleEquivalenceContinuousGSet
statement: formalized
proof: formalized
---

# 58.2 Schemes étale over a point

Section 58.2 of the Stacks Project, [Tag 04JI](https://stacks.math.columbia.edu/tag/04JI). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04JJ, a definition

[Tag 04JJ](https://stacks.math.columbia.edu/tag/04JJ) in the Stacks Project.

**`AlgebraicGeometry.ContinuousGSet.ofMulAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean, line 1414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean#L1414). The attribute's comment: “G-sets”.

> A `G`-set, or discrete `G`-set: a set with a left action of `G` which is continuous when the
> set is given the discrete topology and `G × X` the product topology.

```lean
public def ofMulAction (X : Type v) [MulAction G X]
    (h : (Action.ofMulAction G X).IsContinuous) : ContinuousGSet.{u, v} G
```

**`AlgebraicGeometry.ContinuousGSet.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean, line 1423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean#L1423). The attribute's comment: “morphisms of G-sets”.

> A morphism of `G`-sets is precisely a `G`-equivariant map of the underlying sets: no
> continuity condition is imposed on it.

```lean
public def homEquiv (X Y : ContinuousGSet.{u, v} G) :
    (X ⟶ Y) ≃ {f : X.obj.obj.V → Y.obj.obj.V // ∀ (g : G) (x : X.obj.obj.V),
      f (ConcreteCategory.hom (X.obj.obj.ρ g).asHom x) =
        ConcreteCategory.hom (Y.obj.obj.ρ g).asHom (f x)}
```

Declarations registered for the tag:

- [`AlgebraicGeometry.ContinuousGSet`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean#L424), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean, line 1442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean#L1442) (StacksFrontier): “the category G-Sets”.

## Tag 03QR, a lemma

[Tag 03QR](https://stacks.math.columbia.edu/tag/03QR) in the Stacks Project.

**`AlgebraicGeometry.etaleEquivalenceContinuousGSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean, line 1378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SchemesEtalePoint/Basic.lean#L1378). References: SGA 3 VIIB (2.5), “k a field”; SGA 4 VIII (2.1), “X_ét ≌ B_π”.

> If `L` is a separable closure of `K`, schemes étale over `K` are
> equivalent to discrete continuous `Gal(L/K)`-sets. The underlying set of the
> image of `X` is naturally the set of morphisms `Spec L ⟶ X` over `Spec K`,
> and the action of `σ` is precomposition by `Spec.map σ`.

```lean
public theorem etaleEquivalenceContinuousGSet
    (K L : Type u) [Field K] [Field L] [Algebra K L] [IsSepClosure K L] :
    ∃ E : (Spec (.of K)).Etale ≌ ContinuousGSet.{u, u} Gal(L/K),
      ∃ e : ∀ X,
        (E.functor.obj X).obj.obj.V ≃
          (separableClosureGeometricPoint K L ⟶
            (Scheme.Etale.forget (Spec (.of K))).obj X),
        (∀ {X Y} (f : X ⟶ Y) (x),
          e Y ((E.functor.map f).hom x) =
            e X x ≫ (Scheme.Etale.forget (Spec (.of K))).map f) ∧
        (∀ X (σ : Gal(L/K)) (x),
          (e X (ConcreteCategory.hom ((E.functor.obj X).obj.obj.ρ σ).asHom x)).left =
            Spec.map (CommRingCat.ofHom σ.toAlgHom.toRingHom) ≫ (e X x).left)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.2, Tag 04JI](https://stacks.math.columbia.edu/tag/04JI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
