---
declaration: section
origin: cited
lean: MetaMathlibExt.condorcet_jury_theorem, MetaMathlibExt.condorcet_jury_theorem_of_iIndepFun
statement: formalized
proof: formalized
---

# Condorcet's jury theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/condorcet-s-jury-theorem/index.html).

## Condorcet's jury theorem

Let $\mu$ be a probability measure on a measurable space
$\Omega$, let $X_0, X_1, \dots$ be measurable maps from $\Omega$ to $\{\text{true}, \text{false}\}$
(the votes, true meaning a correct vote), and let $p$ be a number with $1/2 < p < 1$. Suppose that
each vote is correct with probability $p$, that is $\mu(X_i = \text{true}) = p$ for every $i$, and
that the events $\{X_i = \text{true}\}$ are independent: for every nonempty finite set $s$ of
indices, $\mu\bigl(\bigcap_{i \in s} \{X_i = \text{true}\}\bigr) = \prod_{i \in s}
\mu(X_i = \text{true})$. For $n \in \mathbb{N}$ let $M_n$ be the event that more than
$\lfloor n/2 \rfloor$ of the first $n$ votes $X_0, \dots, X_{n-1}$ are correct. Then
$\mu(M_n) \to 1$ as $n \to \infty$, and $\mu(M_n) > p$ for every odd $n > 1$.

## Sources

- https://en.wikipedia.org/wiki/Condorcet%27s_jury_theorem.

Formalized by `MetaMathlibExt.condorcet_jury_theorem`, a theorem declared in [MathlibExt/Probability/Condorcet.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Condorcet.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/condorcet-s-jury-theorem/index.html#condorcet-jury-theorem).

## Condorcet's jury theorem for mutually independent votes

Let $\mu$ be a probability measure
on a measurable space $\Omega$, let $X_0, X_1, \dots$ be measurable maps from $\Omega$ to
$\{\text{true}, \text{false}\}$ (the votes, true meaning a correct vote) that are mutually
independent random variables under $\mu$, and let $p$ be a number with $1/2 < p < 1$. Suppose that
each vote is correct with probability $p$, that is $\mu(X_i = \text{true}) = p$ for every $i$. For
$n \in \mathbb{N}$ let $M_n$ be the event that more than $\lfloor n/2 \rfloor$ of the first $n$
votes $X_0, \dots, X_{n-1}$ are correct. Then $\mu(M_n) \to 1$ as $n \to \infty$, and
$\mu(M_n) > p$ for every odd $n > 1$.

Formalized by `MetaMathlibExt.condorcet_jury_theorem_of_iIndepFun`, a theorem declared in [MathlibExt/Probability/Condorcet.lean, line 1018](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Condorcet.lean#L1018). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/condorcet-s-jury-theorem/index.html#condorcet-jury-theorem-of-i-indep-fun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Condorcet's jury theorem](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/social-choice/condorcet-s-jury-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/social-choice/condorcet-s-jury-theorem)
