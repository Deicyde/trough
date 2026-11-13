---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_assoc, AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_comm
statement: formalized
proof: formalized
---

# 50.5 Hodge cohomology

Section 50.5 of the Stacks Project, [Tag 0FM4](https://stacks.math.columbia.edu/tag/0FM4). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FM5, a lemma

[Tag 0FM5](https://stacks.math.columbia.edu/tag/0FM5) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean#L321). The attribute's comment: “the cup product on H^*\_Hodge(X/S) = ⨁\_\{p+q=n} H^q(X, Ω^p) is associative; the cup product is constructed (hodgeCohomologyCupProduct: the 0FKU pairing of the ringed space (X, A) along the wedge product), nothing assumed”.

> The cup product on `H^*_{Hodge}(X/S)` is associative: `(x ∪ y) ∪ z = x ∪ (y ∪ z)` for `x`,
> `y`, `z` of total degrees `n`, `m`, `l`, the two sides read in the same group
> `H^{n + m + l}_{Hodge}(X/S)`.

```lean
theorem hodgeTotalCupProduct_assoc (n m l : ℕ) (x : hodgeCohomology B n)
    (y : hodgeCohomology B m) (z : hodgeCohomology B l) :
    reindexHodgeTotal B (add_assoc n m l)
        (hodgeTotalCupProduct B (n + m) l (hodgeTotalCupProduct B n m x y) z) =
      hodgeTotalCupProduct B n (m + l) x (hodgeTotalCupProduct B m l y z)
```

**`AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean#L354). The attribute's comment: “the cup product on H^*\_Hodge(X/S) is graded commutative, x ∪ y = (-1)^(nm) y ∪ x for x, y of total degrees n, m; the cup product is constructed (hodgeCohomologyCupProduct), nothing assumed”.

> The cup product on `H^*_{Hodge}(X/S)` is graded commutative: `x ∪ y = (-1)^{nm} y ∪ x` for
> `x` of degree `n` and `y` of degree `m`.

```lean
theorem hodgeTotalCupProduct_comm (n m : ℕ) (x : hodgeCohomology B n)
    (y : hodgeCohomology B m) :
    hodgeTotalCupProduct B n m x y =
      ((((n : ℤ) * m).negOnePow : ℤ)) •
        reindexHodgeTotal B (add_comm m n) (hodgeTotalCupProduct B m n y x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.5, Tag 0FM4](https://stacks.math.columbia.edu/tag/0FM4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
