---
declaration: theorem
origin: cited
lean: Erdos848.erdos_848, Erdos848.erdos_848.variants.asymptotic
statement: formalized
---

# Erdős Problem 848

> Is the maximum size of a set $A \subseteq \{1, \dots, N\}$ such that $ab + 1$ is never
> squarefree (for all $a, b \in A$) achieved by taking those $n \equiv 7 \pmod{25}$?
>
> *References:*
>  - [erdosproblems.com/848](https://www.erdosproblems.com/848)
>  - [Er92b] Erdős, P. "Some of my favourite problems in number theory, combinatorics,
>    and geometry." Resenhas do Instituto de Matemático e Estatística da Universidade
>    de São Paulo 2.2 (1995): 165-186.
>  - [Sa25] Sawhney, M. "Problem 848." (2025)
>    https://www.math.columbia.edu/~msawhney/Problem_848.pdf
>  - Full formal proof of asymptotic result: https://github.com/The-Obstacle-Is-The-Way/erdos-banger

*Quoted from [FormalConjectures/ErdosProblems/848.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/848.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/848](https://www.erdosproblems.com/848).

The file states 2 research or textbook statements: 2 solved.

## `Erdos848.erdos_848`

Solved: stated here without proof.

> Is the maximum size of a set $A ⊆ \{1, \dots, N\}$ such that $ab + 1$ is never squarefree
> (for all $a, b ∈ A$) achieved by taking those $n ≡ 7 \pmod{25}$?
>
> This asks whether `Erdos848 N` holds for all $N$ (formulated using `A ⊆ Finset.range N`).
>
> This was solved for all sufficiently large $N$ by Sawhney in this note. In fact, Sawhney proves
> something slightly stronger, that there exists some constant $c>0$ such that if
> $\lvert A\rvert \geq (\frac{1}{25}-c)N$ and $N$ is large then $A$ is contained in either
> $\{ n\equiv 7\pmod{25}\}$ or $\{n\equiv 18\pmod{25}\}$.

```lean
theorem erdos_848 : ∀ N, Erdos848For N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/848.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/848.lean#L66).

## `Erdos848.erdos_848.variants.asymptotic`

Solved: stated here; a Lean proof is at [https://github.com/The-Obstacle-Is-The-Way/erdos-banger/blob/1cc2ac8e9d70516e979733c6ea5c4d2eb652d1f5/formal/lean/Erdos/848.lean](https://github.com/The-Obstacle-Is-The-Way/erdos-banger/blob/1cc2ac8e9d70516e979733c6ea5c4d2eb652d1f5/formal/lean/Erdos/848.lean).

> There exists $N₀$ such that for all $N ≥ N₀$, if $A ⊆ \{1, \dots, N\}$ satisfies that $ab + 1$
> is never squarefree for all $a, b ∈ A$, then $|A| ≤ |\{n ≤ N : n ≡ 7 \pmod{25}\}|$.
>
> More precisely, Sawhney proves: there exist absolute constants $η > 0$ and $N₀$
> such that for all $N ≥ N₀$, if $|A| ≥ (1/25 - η)N$ then $A ⊆ \{n : n ≡ 7 \pmod{25}\}$ or
> $A ⊆ \{n : n ≡ 18 \pmod{25}\}$.
>
> A complete formal Lean 4 proof is available at:
> https://github.com/The-Obstacle-Is-The-Way/erdos-banger

```lean
theorem erdos_848.variants.asymptotic : ∀ᶠ N in Filter.atTop, Erdos848For N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/848.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/848.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/848.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/848.lean)
- [erdosproblems.com/848](https://www.erdosproblems.com/848)
