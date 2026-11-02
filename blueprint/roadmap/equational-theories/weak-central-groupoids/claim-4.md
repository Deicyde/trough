---
declaration: lemma
origin: cited
lean: WeakCentralGroupoid.isGood_five
statement: formalized
---

# Claim 4

If $a \to b \to c \to d \to e \to a$ is a 5-cycle in the directed graph, and $a \to b \to c$ and $c \to d \to e$ are good paths, then $b \to c \to d$ is also good.

## Depends on

- [Equation 1485](../selected-laws/part-02/eq1485.md)

## Proof depends on

- [Equivalent characterization of graph](graph-dual.md)

## Proof

If $a \to b \to c$ is good then $b = a \diamond c$; if $c \to d \to e$ is good then $d = c \diamond e$; and if $e \to a$ then $a = e \diamond z$ for some $z$ by definition. By (2162) we then have

$$
c = ((e \diamond z) \diamond c) \diamond (c \diamond e) = b \diamond d
$$

so $b \to c \to d$ is good.

## Lean

Formalized as [`WeakCentralGroupoid.isGood_five`](https://teorth.github.io/equational_theories/docs/find/#doc/WeakCentralGroupoid.isGood_five).

## Sources

- [Equational Theories blueprint: chapter/weak_central_groupoids.tex, line 45](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/weak_central_groupoids.tex#L45)
