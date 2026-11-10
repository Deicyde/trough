---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condEntropy_comp_of_injective, ProbabilityTheory.condEntropy_of_injective'
statement: formalized
proof: formalized
---

# Conditional entropy and relabeling

If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\mathbb{H}[X|Z] = \mathbb{H}[Y|Z]$.

Similarly, if $g: T \to U$ is injective, then $\mathbb{H}[X|g(Y)] = \mathbb{H}[X|Y]$.

## Depends on

- [Conditional entropy](conditional-entropy-def.md)

## Proof depends on

- [Entropy and relabeling](relabeled-entropy.md)

## Proof

For the first part, use [Conditional entropy](conditional-entropy-def.md) and then [Entropy and relabeling](relabeled-entropy.md). The second part is a direct computation.

## Lean

Formalized as [`ProbabilityTheory.condEntropy_comp_of_injective`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_comp_of_injective), [`ProbabilityTheory.condEntropy_of_injective'`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_of_injective').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 121](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L121)
