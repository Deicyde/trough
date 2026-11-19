---
declaration: lemma
origin: cited
lean: KummerCriterion.infinite_of_forall_finite_set_not_cover
statement: formalized
proof: formalized
---

# infinite-of-escape

Let $P$ be a predicate on the natural numbers. If no finite set contains every $n$ with $P(n)$, then $\{n \mid P(n)\}$ is infinite.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If the set were finite, it would itself be a finite covering set.

## Lean

Formalized as [`KummerCriterion.infinite_of_forall_finite_set_not_cover`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.infinite_of_forall_finite_set_not_cover).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 42](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L42)
