---
declaration: lemma
origin: cited
lean: KummerCriterion.p_mul_bernoulli_mem_padicInt_vonStaudt
statement: formalized
proof: formalized
---

# vonstaudt-p-integral

Let $p$ be a prime and $n$ an even index. Then $pB_n \in \mathbb{Z}_p$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By von Staudt–Clausen, $B_n$ differs from an integer by the correction sum $\sum_{(q-1)\mid n} 1/q$. Each summand has prime denominator, so multiplying by $p$ clears the single possible factor of $p$ in the denominator and leaves a $p$-adic integer.

## Lean

Formalized as [`KummerCriterion.p_mul_bernoulli_mem_padicInt_vonStaudt`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.p_mul_bernoulli_mem_padicInt_vonStaudt).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 104](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L104)
