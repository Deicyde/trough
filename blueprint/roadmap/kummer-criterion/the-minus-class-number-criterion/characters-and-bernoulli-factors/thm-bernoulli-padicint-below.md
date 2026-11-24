---
declaration: theorem
origin: cited
lean: KummerCriterion.bernoulli_mem_padicInt_of_lt_sub_one
statement: formalized
proof: formalized
---

# bernoulli-padicInt-below

For $0\lt n\lt p-1$, the classical Bernoulli number $B_n$ is $p$-adically integral: $B_n \in \mathbb{Z}_p$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the von Staudt–Clausen theorem, the denominator of $B_n$ (for $n$ even, the only nontrivial case) is the product of the primes $q$ with $(q-1)\mid n$. If $p$ occurred, then $p - 1 \le n$, contradicting $n < p-1$. Hence the denominator is prime to $p$ and $B_n \in \mathbb{Z}_p$.

## Lean

Formalized as [`KummerCriterion.bernoulli_mem_padicInt_of_lt_sub_one`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.bernoulli_mem_padicInt_of_lt_sub_one).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 61](https://github.com/riccardobrasca/KummerCriterion/blob/d6f2d56131fb9a992bcfc97e46aa1dec7d8c7018/blueprint/src/subsections/hminus-formula.tex#L61)
