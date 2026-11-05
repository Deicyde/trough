---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Module.equiv_free_prod_directSum
mathlib_file: Mathlib/Algebra/Module/PID.lean
---

# Structure theorem

**Structure theorem of finitely generated modules over a PID** : A finitely generated
module over a PID is isomorphic to the product of a free module and a direct sum of some
`R ⧸ R ∙ (p i ^ e i)` where the `p i ^ e i` are prime powers.

```lean
Module.equiv_free_prod_directSum.{u, v} (R : Type u) [CommRing R] [IsPrincipalIdealRing R]
  (M : Type v) [AddCommGroup M] [_root_.Module R M] [IsDomain R] [h' : Module.Finite R M] :
  ∃ n ι x p,
    ∃ (_ : ∀ (i : ι), Irreducible (p i)),
      ∃ e, Nonempty (M ≃ₗ[R] (Fin n →₀ R) × DirectSum ι fun i => R ⧸ R ∙ p i ^ e i)
```

## Depends on

- [Finitely supported function](../../data-structures/maps/finitely-supported-function.md)
- [Irreducible element](../../general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Linear map](../fundamentals/linear-map.md)
- [Principal ideal domain](../../general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Quotient space (Fundamentals)](../fundamentals/quotient-space.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Basis](../fundamentals/basis.md)
- [Direct sum](../../../undergraduate/linear-algebra/fundamentals/direct-sum.md)
- [Isomorphism](../../general-algebra/category-theory/isomorphism.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Localization](../../general-algebra/rings/localization.md)
- [Maximal ideal](../../general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Noetherian module](../fundamentals/noetherian-module.md)
- [Noetherian ring](../../general-algebra/rings/noetherian-ring.md)
- [Polynomial in one indeterminate](../../general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Prime ideal](../../general-algebra/ideals-and-quotients/prime-ideal.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Small category](../../general-algebra/category-theory/small-category.md)
- [The category of modules over a ring](../fundamentals/the-category-of-modules-over-a-ring.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Module.equiv_free_prod_directSum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/PID.html#Module.equiv_free_prod_directSum)
- [Source of `Module.equiv_free_prod_directSum` in Mathlib/Algebra/Module/PID.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Module/PID.lean#L252)
- [Mathlib overview: Linear algebra › Finitely generated modules over a PID](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L188)
- [1000+ theorems list: Q7888360](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3953)
- [1000+ theorems project: Q7888360](https://1000-plus.github.io/all.html?length=-1#Q7888360)
- [Wikipedia: Structure theorem for finitely generated modules over a principal ideal domain](https://en.wikipedia.org/wiki/Structure_theorem_for_finitely_generated_modules_over_a_principal_ideal_domain)
- [Wikidata: Q7888360](https://www.wikidata.org/wiki/Q7888360)
