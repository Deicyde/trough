---
declaration: lemma
origin: cited
lean: WeakCentralGroupoid.Path.def'
statement: formalized
---

# Equivalent characterization of graph

One has $x \to y$ if and only if $x = w \diamond y$ for some $w$.

## Depends on

- [Equation 1485](../selected-laws/part-02/eq1485.md)

## Proof depends on

- [1485 equivalent to 2162](1485-dual.md)

## Proof

If $x \to y$ then $y = x \diamond z$, then writing $z = z_1 \diamond z_2$ as before we obtain

$$
x = (z_2 \diamond x) \diamond (x \diamond (z_1 \diamond z_2)) = (z_2 \diamond x) \diamond y
$$

giving the forward implication. The backwards implication follows by duality.

## Lean

Stated as [`WeakCentralGroupoid.Path.def'`](https://teorth.github.io/equational_theories/docs/find/#doc/WeakCentralGroupoid.Path.def'); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/weak_central_groupoids.tex, line 27](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/weak_central_groupoids.tex#L27)
