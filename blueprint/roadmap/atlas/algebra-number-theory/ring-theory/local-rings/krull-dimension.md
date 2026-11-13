---
declaration: section
origin: cited
lean: ringKrullDim_le_of_integral, exists_ltSeries_of_integral_of_injective, ringKrullDim_ge_of_integral_of_injective, ringKrullDim_eq_of_integral_of_injective, IsLocalRing.eq_bot_of_lt_of_ne_maximalIdeal_of_ringKrullDim_le_two
statement: formalized
proof: formalized
---

# Krull dimension

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/krull-dimension/index.html).

## Krull dimension does not increase along integral algebras

Let $A$ and $B$ be commutative
rings and let $B$ be an $A$-algebra that is integral over $A$. Then the Krull dimension of $B$ is
at most the Krull dimension of $A$.

The structure map $A \to B$ need not be injective. The inequality comes from incomparability:
contracting prime ideals of $B$ to $A$ is strictly monotone, so it gives a strictly monotone map
from the prime spectrum of $B$ to the prime spectrum of $A$.

Formalized by `ringKrullDim_le_of_integral`, a theorem declared in [MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/krull-dimension/index.html#ring-krull-dim-le-of-integral).

## Prime chains lift along injective integral maps

Every finite chain of prime ideals lifts along an injective integral algebra map.

Formalized by `exists_ltSeries_of_integral_of_injective`, a theorem declared in [MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/krull-dimension/index.html#exists-lt-series-of-integral-of-injectiv).

## Krull dimension does not decrease along injective integral maps

Krull dimension cannot decrease along an injective integral algebra map.

Formalized by `ringKrullDim_ge_of_integral_of_injective`, a theorem declared in [MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/krull-dimension/index.html#ring-krull-dim-ge-of-integral-of-injecti).

## Injective integral maps preserve Krull dimension

An injective integral algebra map preserves Krull dimension.

Formalized by `ringKrullDim_eq_of_integral_of_injective`, a theorem declared in [MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/IntegralKrullDim.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/krull-dimension/index.html#ring-krull-dim-eq-of-integral-of-injecti).

## Short prime chains when the completion has dimension at most two

In a Noetherian local domain whose adic completion has Krull dimension
at most `2`, any prime strictly below a non-maximal prime is `⊥`.

Formalized by `IsLocalRing.eq_bot_of_lt_of_ne_maximalIdeal_of_ringKrullDim_le_two`, a theorem declared in [MathlibExt/RingTheory/LocalRing/KrullDimLeTwo.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/KrullDimLeTwo.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/krull-dimension/index.html#eq-bot-of-lt-of-ne-maximal-ideal-of-ring).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Krull dimension](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/krull-dimension/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/local-rings/krull-dimension)
