---
declaration: theorem
origin: cited
lean: TauCeti.finrank_mul_finrank_centralizer
statement: formalized
proof: formalized
---

# The centralizer theorem

For a central simple `K`-subalgebra `B` of a finite-dimensional
simple `K`-algebra `A`, the dimensions of `B` and of its centralizer are complementary:

  `finrank K B * finrank K C_A(B) = finrank K A`.

This is the dimension count of
`TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite`, whose one
algebraic hypothesis — simplicity of `B ⊗[K] Aᵐᵒᵖ` — `IsSimpleRing.tensorProduct` supplies
from `B` central simple and `Aᵐᵒᵖ` simple.

```lean
TauCeti.finrank_mul_finrank_centralizer.{u_1, u_2} {K : Type u_1} {A : Type u_2} [Field K] [Ring A]
  [Algebra K A] [IsSimpleRing A] [FiniteDimensional K A] (B : Subalgebra K A)
  [Algebra.IsCentral K ↥B] [IsSimpleRing ↥B] :
  Module.finrank K ↥B * Module.finrank K ↥(Subalgebra.centralizer K ↑B) = Module.finrank K A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dimension count behind the centralizer theorem, asking only for what it uses](the-dimension-count-behind-the-centralizer-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_mul_finrank_centralizer`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Centralizer/Basic.html#TauCeti.finrank_mul_finrank_centralizer).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_mul_finrank_centralizer`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Centralizer/Basic.html#TauCeti.finrank_mul_finrank_centralizer)
- [Source of `TauCeti.finrank_mul_finrank_centralizer` in TauCeti/Algebra/CentralSimple/Centralizer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CentralSimple/Centralizer/Basic.lean#L413)
