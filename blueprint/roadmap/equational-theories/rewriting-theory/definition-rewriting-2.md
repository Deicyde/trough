---
declaration: definition
origin: cited
---

# definition-rewriting-2

We say that $R$ is *Church-Rosser* if whenever $a\leftrightarrow^* b$, there exists some $c$ such that

$$
a\rightarrow^* c\ {}^*\leftarrow b
$$

We say that $R$ is *confluent* if whenever $b_1\ {}^*\leftarrow a\rightarrow^* b_2$ there exists some $c$ such that $b_1\rightarrow^* c\ {}^*\leftarrow b_2$.

We say that $R$ is *locally confluent* if whenever $b_1\leftarrow a\rightarrow b_2$ there exists some $c$ such that $b_1\rightarrow^* c\ {}^*\leftarrow b_2$.

We say that (an arbitrary) $a$ is in *normal form* (or $a$ is a normal form) if there is no $a' \neq a$ such that $a \rightarrow a'$, and that $R$ is *weakly normalizing* if for every $a$, there is some $a'$ such that $a\rightarrow^*a'$ and $a'$ is in normal form.

We say that $R$ is *strongly normalizing* if there are no infinite rewrite sequences $a_1\rightarrow a_2\rightarrow \ldots$. In particular, a strongly normalizing $R$ is also weakly normalizing.

## Depends on

Its statement uses no other node of the blueprint.

## Sources

- [Equational Theories blueprint: chapter/rewriting.tex, line 24](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/rewriting.tex#L24)
