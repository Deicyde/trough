---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: LinearIndependent.tmul_of_isDomain
---

# The tensor product of linearly independent families

Let $R$ be a domain and $M, N$ two $R$-semimodules. If $f$ and $g$ are linearly independent families of points in $M$ and $N$, then $(i, j) \mapsto f i \otimes g j$ is a linearly independent family of points in $M \otimes N$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We will prove the equivalent statement:

Let $P, Q$ be two free $R$ modules, $f : P \to M$ and $g : Q \to N$ be two $R$-linear injective maps. Then $f \otimes g : P \otimes_R Q \to M \otimes_R N$ is injective.

Let $K$ be the field of fractions of $R$.

The map

$$
P \otimes_R Q \to (K \otimes_R P) \otimes_R (K \otimes_R Q) = (K \otimes_R P) \otimes_K (K \otimes_R Q)
$$

is injective because $R \to K$ is injective and all the modules involved are flat. The map

$$
(K \otimes_R P) \otimes_K (K \otimes_R Q) \to (K \otimes_R M) \otimes_K (K \otimes_R N)
$$

is injective because all the modules involved are $K$-flat (as $K$ is a field).

$P \otimes_R Q \to M \otimes_R N$ is now a factor of the composition of the two injections above, and is thus is injective.

## Lean

Formalized as [`LinearIndependent.tmul_of_isDomain`](https://yaeldillies.github.io/toric/docs/find/#doc/LinearIndependent.tmul_of_isDomain).

## Sources

- [Toric varieties blueprint: chapters/2-1-tensor-product.tex, line 4](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-1-tensor-product.tex#L4)
