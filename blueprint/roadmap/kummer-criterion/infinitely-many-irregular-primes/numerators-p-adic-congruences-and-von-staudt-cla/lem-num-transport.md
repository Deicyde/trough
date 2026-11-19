---
declaration: lemma
origin: cited
lean: KummerCriterion.prime_dvd_num_of_padic_sub_eq_p_mul
statement: formalized
proof: formalized
---

# num-transport

Let $q, r$ be rationals with $q \equiv r \pmod{p}$. If $p\mid\operatorname{num}(q)$, then $p\mid\operatorname{num}(r)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Divisibility of the numerator by $p$ is equivalent to $q \in p\mathbb{Z}_p$, which is invariant under perturbation by elements of $p\mathbb{Z}_p$.

## Lean

Formalized as [`KummerCriterion.prime_dvd_num_of_padic_sub_eq_p_mul`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.prime_dvd_num_of_padic_sub_eq_p_mul).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 67](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L67)
