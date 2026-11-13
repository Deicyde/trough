---
declaration: section
origin: cited
lean: MetaMathlibExt.formalAlpha, MetaMathlibExt.formalBeta, MetaMathlibExt.IsFormalSequence
statement: formalized
proof: formalized
---

# Second-order recurrences from seed triples

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/second-order-recurrences-from-seed-triples/index.html).

## Coefficient of the formal-sequence recurrence

For elements $a$, $b$, $c$ of a field $F$,
the coefficient of the formal-sequence recurrence determined by the seed triplet $(a, b, c)$ is
$\alpha = \frac{ab + bc + ca}{b^2} - 1$.

Division by zero is read as $0$, so $\alpha = -1$ when $b = 0$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL23/Kocik/kocik5.tex>, lines 482–499.

Formalized by `MetaMathlibExt.formalAlpha`, a definition declared in [MathlibExt/NumberTheory/FormalSequence.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FormalSequence.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/second-order-recurrences-from-seed-triples/index.html#formal-alpha).

## Constant term of the formal-sequence recurrence

For elements $a$, $b$, $c$ of a field
$F$, the constant term of the formal-sequence recurrence determined by the seed triplet
$(a, b, c)$ is $\beta = \frac{b^2 - ac}{b}$.

Division by zero is read as $0$, so $\beta = 0$ when $b = 0$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL23/Kocik/kocik5.tex>, lines 482–499.

Formalized by `MetaMathlibExt.formalBeta`, a definition declared in [MathlibExt/NumberTheory/FormalSequence.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FormalSequence.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/second-order-recurrences-from-seed-triples/index.html#formal-beta).

## Formal sequence from a seed triplet

Let $F$ be a field and $a, b, c \in F$. A sequence
$u : \mathbb{N} \to F$ is a formal sequence with seed triplet $(a, b, c)$ when $b \neq 0$,
$u_0 = a$, $u_1 = b$, $u_2 = c$, and for every $n \ge 0$

$$u_{n+2} = \alpha u_{n+1} - u_n + \beta,$$

where $\alpha = \frac{ab + bc + ca}{b^2} - 1$ and $\beta = \frac{b^2 - ac}{b}$ are the
coefficient and the constant term of the formal-sequence recurrence.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL23/Kocik/kocik5.tex>, lines 482–499.

Formalized by `MetaMathlibExt.IsFormalSequence`, a definition declared in [MathlibExt/NumberTheory/FormalSequence.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FormalSequence.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/second-order-recurrences-from-seed-triples/index.html#is-formal-sequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Second-order recurrences from seed triples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/second-order-recurrences-from-seed-triples/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/second-order-recurrences-from-seed-triples)
