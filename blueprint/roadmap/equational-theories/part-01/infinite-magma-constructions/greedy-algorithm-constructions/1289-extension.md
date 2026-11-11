---
declaration: lemma
origin: cited
lean: Eq1289.Greedy.lift
statement: formalized
---

# 1289 extension

Suppose that $\diamond$ is a partial solution, and $a \diamond b$ is currently undefined. Then there exists an extension $\diamond'$ of $\diamond$ for which $a \diamond' b$ is defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $a \diamond b$ is currently undefined, introduce a new element $c$ and define $a \diamond b = c$ and $c \diamond c = c.$ If furthermore $a = (d \diamond b) \diamond b$ for some d, then also define $b \diamond c = d$ (This last step is well defined by injectivity of $R_b$).

We now check that the three axioms still hold. Law 3 is obvious, law 2 follows since $d \not = c$. For law 1, we first make the observation that $a \not = b$, for otherwise $a \diamond b$ would have been defined. This has the consequence that if $d$ exists, then $d \not = b$, for otherwise $a = (b \diamond b) \diamond b = b.$ In particular, the product $d \diamond c$ remains undefined after running the algorithm once.

We now work by cases on the values of the variables $x,y$ appearing in law 1:

- Case 1: $y=c$. In this case, for the product $x \diamond y$ to be defined, we require $x =b$ or $x = c$. In the former case either $b \diamond c$ or $(b \diamond c) \diamond c = d \diamond c$ is not defined. In the latter case, law 1 holds as $c$ is idempotent.
- Case 2: $y=b$. For $((x \diamond b) \diamond b) \diamond b$ to be defined now but not have been defined before, we require one of $x= a, (x \diamond b) = a, ((x \diamond b) \diamond b) = a.$ The first two cases are eliminated as $c \diamond b$ is not yet defined. The last case holds as then $d$ exists and equals $x$, so $b \diamond (((x \diamond b) \diamond b) \diamond b) = b \diamond (a \diamond b) = b \diamond c = x.$
- Case 3: $y \not = c, y \not = b$. We have introduced no new products with a right-hand side other than $c$ or $b$, so if $((x \diamond y) \diamond y) \diamond y$ was undefined before it remains undefined now.

## Lean

Stated as [`Eq1289.Greedy.lift`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1289.Greedy.lift); the blueprint marks no proof of it as formalized.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 437](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/infinite_magma_constructions.tex#L437)
