---
declaration: lemma
origin: cited
lean: KummerCriterion.positiveResidue_properties
statement: formalized
proof: formalized
---

# positive-residue

Let $p$ be an odd prime and $m$ an even index with $(p-1)\nmid m$. Then $m' := m \bmod (p-1)$ satisfies $0 < m' < p-1$, $m'$ is even, and $m \equiv m' \pmod{p-1}$. In particular $2 \le m' \le p-3$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The residue is nonzero precisely because $(p-1)\nmid m$, and it inherits parity from $m$ since $p-1$ is even.

## Lean

Formalized as [`KummerCriterion.positiveResidue_properties`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.positiveResidue_properties).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 254](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L254)
