---
declaration: theorem
origin: cited
lean: Ideal.absNorm_lt_absNorm_of_lt, Ideal.eq_of_le_of_absNorm_eq, FractionalIdeal.absNorm_eq_finprod_count, FractionalIdeal.exists_mem_count_spanSingleton_eq, Ideal.exists_principal_prime_over_of_norm_natAbs_eq
statement: formalized
proof: formalized
---

# Ideal norms, factorization and principal primes

In an infinite commutative Dedekind domain with finite quotients, a nonzero smaller ideal has strictly larger absolute norm, and nested ideals of equal absolute norm coincide. Over a Dedekind domain finite free over the integers, each nonzero fractional-ideal norm is the finite-support product of height-one prime norms raised to signed integer exponents; the fraction field needs no number-field structure. In an infinite Dedekind domain finite free over the integers, a supplied element with prime absolute algebraic norm yields a principal prime above that rational prime. Over any Dedekind domain and fraction field, a nonzero fractional ideal contains a nonzero element whose principal ideal attains the same signed exponent at a fixed height-one prime; the ideal need not be principal.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml) of [FormalFrontier/dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.absNorm_lt_absNorm_of_lt` (theorem), declared in [DedekindIdealArithmetic/Ideal/AbsNorm.lean, line 29](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/AbsNorm.lean#L29).
- `Ideal.eq_of_le_of_absNorm_eq` (theorem), declared in [DedekindIdealArithmetic/Ideal/AbsNorm.lean, line 42](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/AbsNorm.lean#L42).
- `FractionalIdeal.absNorm_eq_finprod_count` (theorem), declared in [DedekindIdealArithmetic/Ideal/FractionalNorm.lean, line 53](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/FractionalNorm.lean#L53).
- `FractionalIdeal.exists_mem_count_spanSingleton_eq` (theorem), declared in [DedekindIdealArithmetic/Ideal/CountAttainment.lean, line 84](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/CountAttainment.lean#L84).
- `Ideal.exists_principal_prime_over_of_norm_natAbs_eq` (theorem), declared in [DedekindIdealArithmetic/Ideal/PrincipalPrime.lean, line 27](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/PrincipalPrime.lean#L27).

Read from the source at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), without running Lean.

## Sources

- [dedekind-ideal-arithmetic at c7630759: formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml)
- [Source of `Ideal.absNorm_lt_absNorm_of_lt` in DedekindIdealArithmetic/Ideal/AbsNorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/AbsNorm.lean#L29)
- [Source of `Ideal.eq_of_le_of_absNorm_eq` in DedekindIdealArithmetic/Ideal/AbsNorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/AbsNorm.lean#L42)
- [Source of `FractionalIdeal.absNorm_eq_finprod_count` in DedekindIdealArithmetic/Ideal/FractionalNorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/FractionalNorm.lean#L53)
- [Source of `FractionalIdeal.exists_mem_count_spanSingleton_eq` in DedekindIdealArithmetic/Ideal/CountAttainment.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/CountAttainment.lean#L84)
- [Source of `Ideal.exists_principal_prime_over_of_norm_natAbs_eq` in DedekindIdealArithmetic/Ideal/PrincipalPrime.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Ideal/PrincipalPrime.lean#L27)
