---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsVariety, AlgebraicGeometry.gaussianRationals_isVariety, AlgebraicGeometry.gaussianRationals_product_reducible, AlgebraicGeometry.gaussianRationals_product_not_isVariety, AlgebraicGeometry.gaussianRationals_product_iso_coprod, AlgebraicGeometry.isVariety_pullback
statement: formalized
proof: formalized
---

# 33.3 Varieties

Section 33.3 of the Stacks Project, [Tag 020C](https://stacks.math.columbia.edu/tag/020C). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 020D, a definition

[Tag 020D](https://stacks.math.columbia.edu/tag/020D) in the Stacks Project.

**`AlgebraicGeometry.IsVariety`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Basic.lean#L50).

> A scheme over a field is a variety when it is integral and its structure morphism is
> separated and of finite type.

```lean
class IsVariety (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) : Prop
    extends IsIntegral X, IsSeparated f, LocallyOfFiniteType f, QuasiCompact f
```

## Tag 020G, an example

[Tag 020G](https://stacks.math.columbia.edu/tag/020G) in the Stacks Project.

**`AlgebraicGeometry.gaussianRationals_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean#L296). The attribute's comment: “each factor is a variety”.

> `Spec ℚ(i)` is a variety over `ℚ`.

```lean
public theorem gaussianRationals_isVariety :
    IsVariety ℚ gaussianRationalsToRat
```

**`AlgebraicGeometry.gaussianRationals_product_reducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean#L308). The attribute's comment: “the product is reducible”.

> The product `Spec ℚ(i) ×_{Spec ℚ} Spec ℚ(i)` is reducible.

```lean
public theorem gaussianRationals_product_reducible :
    ¬ IrreducibleSpace
      (pullback gaussianRationalsToRat gaussianRationalsToRat : Scheme)
```

**`AlgebraicGeometry.gaussianRationals_product_not_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean#L341). The attribute's comment: “the product is not a variety”.

> The product of these two varieties is not a variety.

```lean
public theorem gaussianRationals_product_not_isVariety :
    ¬ IsVariety ℚ
      (pullback.fst gaussianRationalsToRat gaussianRationalsToRat ≫
        gaussianRationalsToRat)
```

**`AlgebraicGeometry.gaussianRationals_product_iso_coprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean#L349). The attribute's comment: “the product is two copies of the factor”.

> The product is isomorphic to two disjoint copies of `Spec ℚ(i)`.

```lean
public theorem gaussianRationals_product_iso_coprod :
    Nonempty ((pullback gaussianRationalsToRat gaussianRationalsToRat) ≅
      (Spec (.of GaussianRationals) ⨿ Spec (.of GaussianRationals)))
```

## Tag 05P3, a lemma

[Tag 05P3](https://stacks.math.columbia.edu/tag/05P3) in the Stacks Project.

**`AlgebraicGeometry.isVariety_pullback`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Product.lean#L82).

> **Stacks Project, Tag 05P3.** The fibre product of two varieties over an
> algebraically closed field is a variety.

```lean
public instance isVariety_pullback (k : Type u) [Field k] [IsAlgClosed k]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [IsVariety k f] [IsVariety k g] :
    IsVariety k (pullback.fst f g ≫ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.3, Tag 020C](https://stacks.math.columbia.edu/tag/020C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
