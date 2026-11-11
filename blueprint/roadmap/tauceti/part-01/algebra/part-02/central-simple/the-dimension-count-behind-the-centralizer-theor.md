---
declaration: theorem
origin: cited
lean: TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite
statement: formalized
proof: formalized
---

# The dimension count behind the centralizer theorem, asking only for what it uses

that `A`
is finite-dimensional over the field `K` and that the ring `R = B ⊗[K] Aᵐᵒᵖ` acting on `A` is
simple, which makes `A` nonzero, so that the factor of `finrank K A` cancelled at the end is
nonzero. Then

  `finrank K B * finrank K C_A(B) = finrank K A`.

Simplicity of `R` is the only algebraic hypothesis on `B` and on `A`, and there is more than one way
to supply it: `TauCeti.finrank_mul_finrank_centralizer` has it from `B` central simple and `A`
simple, while `TauCeti.finrank_mul_finrank_centralizer_of_isField` has it from `B` a subfield and
`A` central simple.

```lean
TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite.{u_1, u_2}
  {K : Type u_1} {A : Type u_2} [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A]
  (B : Subalgebra K A) [IsSimpleRing (TensorProduct K (↥B) Aᵐᵒᵖ)] :
  Module.finrank K ↥B * Module.finrank K ↥(Subalgebra.centralizer K ↑B) = Module.finrank K A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Centralizer/Basic.html#TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Centralizer/Basic.html#TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite)
- [Source of `TauCeti.finrank_mul_finrank_centralizer_of_isSimpleRing_tensorProduct_mulOpposite` in TauCeti/Algebra/CentralSimple/Centralizer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/CentralSimple/Centralizer/Basic.lean#L304)
