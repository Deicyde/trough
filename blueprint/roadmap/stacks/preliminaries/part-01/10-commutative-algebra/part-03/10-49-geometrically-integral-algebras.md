---
declaration: section
origin: cited
lean: Algebra.IsGeometricallyIntegral, geometricallyIntegral_iff_irreducible_and_reduced, Algebra.isGeometricallyIntegral_tfae, Algebra.IsGeometricallyIntegral.isDomain_tensorProduct
statement: formalized
proof: formalized
---

# 10.49 Geometrically integral algebras

Section 10.49 of the Stacks Project, [Tag 05DW](https://stacks.math.columbia.edu/tag/05DW). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05DX, a definition

[Tag 05DX](https://stacks.math.columbia.edu/tag/05DX) in the Stacks Project.

**`Algebra.IsGeometricallyIntegral`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/Defs.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/Defs.lean#L120). References: EGA IV (4.6.2), “affine, special case”; SGA 6 XII (1.2), “special case”.

> A `k`-algebra `S` is **geometrically integral over `k`** if every base change of
> `Spec S ⟶ Spec k` along a field-valued point of `Spec k` is an integral scheme, equivalently
> if for every field extension `k'/k` the ring `S ⊗[k] k'` is a domain
> (`Algebra.isGeometricallyIntegral_iff_isDomain_tensorProduct`).

```lean
public abbrev Algebra.IsGeometricallyIntegral (k S : Type u) [Field k] [CommRing S]
    [Algebra k S] : Prop
```

## Tag 05DY, a lemma

[Tag 05DY](https://stacks.math.columbia.edu/tag/05DY) in the Stacks Project.

**`geometricallyIntegral_iff_irreducible_and_reduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/Defs.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/Defs.lean#L238). References: EGA IV (4.6.14), “special case”; EGA IV (4.6.2), “affine, special case”; SGA 3 XIX (2.1), “partial”.

> A `k`-algebra `S` is geometrically integral over `k` if and only if it is both
> geometrically irreducible and geometrically reduced over `k`. This is Stacks tag 05DY.
>
> `GeometricallyReduced` uses the convention `IsReduced (k' ⊗[k] S)` (extension on the
> left). The local statements about `S ⊗[k] k'` (algebra on the left) are interchanged with
> these via the canonical ring isomorphism `Algebra.TensorProduct.comm`.

```lean
theorem geometricallyIntegral_iff_irreducible_and_reduced
    (k : Type u) [Field k] (S : Type v) [CommRing S] [Algebra k S] :
    GeometricallyIntegral.{u, v, w} k S ↔
      GeometricallyIrreducible.{u, v, w} k S ∧ GeometricallyReduced.{u, v, w} k S
```

## Tag 0FWF, a lemma

[Tag 0FWF](https://stacks.math.columbia.edu/tag/0FWF) in the Stacks Project.

**`Algebra.isGeometricallyIntegral_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/TFAE.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/TFAE.lean#L124).

> **Stacks 0FWF.** Let `k` be a field and let `S` be a `k`-algebra. The following are
> equivalent: (1) `S` is geometrically integral over `k`; (2) `S ⊗[k] k'` is a domain for every
> field extension `k'/k`; (3) `S ⊗[k] k'` is a domain for every finite extension `k'/k`;
> (4) `S ⊗[k] AlgebraicClosure k` is a domain.

```lean
public theorem Algebra.isGeometricallyIntegral_tfae (k S : Type u) [Field k] [CommRing S]
    [Algebra k S] :
    List.TFAE
      [ Algebra.IsGeometricallyIntegral k S,
        ∀ (k' : Type u) [Field k'] [Algebra k k'], IsDomain (S ⊗[k] k'),
        ∀ (k' : Type u) [Field k'] [Algebra k k'] [Module.Finite k k'], IsDomain (S ⊗[k] k'),
        IsDomain (S ⊗[k] AlgebraicClosure k) ]
```

## Tag 09P9, a lemma

[Tag 09P9](https://stacks.math.columbia.edu/tag/09P9) in the Stacks Project.

**`Algebra.IsGeometricallyIntegral.isDomain_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/TensorProduct.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/TensorProduct.lean#L100).

> Let `k` be a field, let `S` be a geometrically integral `k`-algebra and let `R` be a
> `k`-algebra which is an integral domain. Then `R ⊗[k] S` is an integral domain.

```lean
public theorem Algebra.IsGeometricallyIntegral.isDomain_tensorProduct (k R S : Type u) [Field k]
    [CommRing R] [IsDomain R] [Algebra k R] [CommRing S] [Algebra k S]
    [Algebra.IsGeometricallyIntegral k S] : IsDomain (R ⊗[k] S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.49, Tag 05DW](https://stacks.math.columbia.edu/tag/05DW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
