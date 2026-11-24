---
declaration: proposition
origin: cited
lean: addIrreducible_subset_of_addSubmonoidClosure_eq_top
statement: formalized
proof: formalized
---

# Irreducible elements lie in all sets generating a salient monoid

If $M$ is a monoid with a single unit, and $S$ is a set generating $M$, then $S$ contains all irreducible elements of $M$.

## Depends on

- [Irreducible element](0-irred.md)

## Proof

Assume $p$ is an irreducible element. Since $S$ generates $M$, write

$$
p = \sum_i a_i
$$

where the $a_i$ are finitely many elements (not necessarily distinct) elements of $S$. Since $p$ is irreducible, we must have

$$
p = a_i \in S
$$

for some $i$.

## Lean

Formalized as [`addIrreducible_subset_of_addSubmonoidClosure_eq_top`](https://yaeldillies.github.io/toric/docs/find/#doc/addIrreducible_subset_of_addSubmonoidClosure_eq_top).

## Sources

- [Toric varieties blueprint: chapters/2-2-affine-monoids.tex, line 75](https://github.com/YaelDillies/toric/blob/97b1287db93f2eee84c8bb4e408058d9e721ce5b/blueprint/src/chapters/2-2-affine-monoids.tex#L75)
