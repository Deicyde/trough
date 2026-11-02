---
declaration: definition
origin: cited
lean: FreeMagmaWithLaws
statement: formalized
---

# Free magma relative to a theory

Let $\Gamma$ be a theory with an alphabet $X$. A *free magma* with alphabet $X$ subject to the theory $\Gamma$ is a magma $M_{X,\Gamma}$ together with a function $\iota_{X,\Gamma} : X \to M_{X,\Gamma}$, with the following properties:

- **(i)** $M_{X,\Gamma}$ satisfies the theory $\Gamma$: $M_{X,\Gamma} \models \Gamma$.
- **(ii)** For any magma $M$ satisfying the theory $\Gamma$ and any function $f: X \to M$, there exists a unique magma homomorphism $\tilde{f}: M_{X,\Gamma} \to M$ such that $\tilde{f} \circ \iota_{X,\Gamma} = f$.

## Depends on

- [Models](../basic-theory-of-magmas/models-def.md)

## Lean

Formalized as [`FreeMagmaWithLaws`](https://teorth.github.io/equational_theories/docs/find/#doc/FreeMagmaWithLaws).

## Sources

- [Equational Theories blueprint: chapter/abstract_nonsense.tex, line 5](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/abstract_nonsense.tex#L5)
