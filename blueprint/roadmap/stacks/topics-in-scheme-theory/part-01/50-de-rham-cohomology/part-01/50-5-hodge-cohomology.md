---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.hodgeCupProduct_assoc, AlgebraicGeometry.SheafOfModules.hodgeCupProduct_comm, AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_assoc, AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_comm
statement: formalized
proof: formalized
---

# 50.5 Hodge cohomology

Section 50.5 of the Stacks Project, [Tag 0FM4](https://stacks.math.columbia.edu/tag/0FM4). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FM5, a lemma

[Tag 0FM5](https://stacks.math.columbia.edu/tag/0FM5) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.hodgeCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProduct.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProduct.lean#L358). The attribute's comment: “the cup product on Hodge cohomology is associative, on classes of pure bidegree; the 0FKU pairing with its 0FP4 law is the carried parameter HodgeCohomologyCupProduct”.

> **Stacks Project, Tag 0FM5.** The cup product on `H^*_{Hodge}(X/S)` is **associative**. This
> is Cohomology, Lemma 0FP4 together with the associativity of the wedge product.

```lean
theorem hodgeCupProduct_assoc (p p' p'' : ℕ) (q q' q'' : ℤ)
    (ξ : hodgeCohomologyComponent B p q) (ζ : hodgeCohomologyComponent B p' q')
    (θ : hodgeCohomologyComponent B p'' q'') :
    reindexHodge B (Nat.add_assoc p p' p'') (add_assoc q q' q'')
        (hodgeCupProduct B c (p + p') p'' (q + q') q''
          (hodgeCupProduct B c p p' q q' ξ ζ) θ) =
      hodgeCupProduct B c p (p' + p'') q (q' + q'')
        ξ (hodgeCupProduct B c p' p'' q' q'' ζ θ)
```

**`AlgebraicGeometry.SheafOfModules.hodgeCupProduct_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProduct.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProduct.lean#L386). The attribute's comment: “the cup product on Hodge cohomology is graded commutative for the total degree p + q, sign (-1)^((p+q)(p'+q')), on classes of pure bidegree; the 0FKU pairing with its 0FP5 law is the carried parameter HodgeCohomologyCupProduct”.

> **Stacks Project, Tag 0FM5.** The cup product on `H^*_{Hodge}(X/S)` is **graded
> commutative**: `ξ ∪ ζ = (-1)^{(p + q)(p' + q')} ζ ∪ ξ` for `ξ` in `H^q(X, Ω^p)` and `ζ` in
> `H^{q'}(X, Ω^{p'})`, the sign of the total degrees. This is Cohomology, Lemma 0FP5 together with
> the graded commutativity of the wedge product.

```lean
theorem hodgeCupProduct_comm (p p' : ℕ) (q q' : ℤ)
    (ξ : hodgeCohomologyComponent B p q) (ζ : hodgeCohomologyComponent B p' q') :
    hodgeCupProduct B c p p' q q' ξ ζ =
      (((((p : ℤ) + q) * ((p' : ℤ) + q')).negOnePow : ℤ)) •
        reindexHodge B (Nat.add_comm p' p) (add_comm q' q)
          (hodgeCupProduct B c p' p q' q ζ ξ)
```

**`AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean#L321). The attribute's comment: “the cup product on H^*\_Hodge(X/S) = ⨁\_\{p+q=n} H^q(X, Ω^p) is associative; the cup product is constructed (hodgeCohomologyCupProduct: the 0FKU pairing of the ringed space (X, A) along the wedge product), nothing assumed”.

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

**`AlgebraicGeometry.SheafOfModules.hodgeTotalCupProduct_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeCohomology/CupProductLaws.lean#L354). The attribute's comment: “the cup product on H^*\_Hodge(X/S) is graded commutative, x ∪ y = (-1)^(nm) y ∪ x for x, y of total degrees n, m; the cup product is constructed (hodgeCohomologyCupProduct), nothing assumed”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
