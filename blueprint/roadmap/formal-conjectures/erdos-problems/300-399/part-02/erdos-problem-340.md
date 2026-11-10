---
declaration: theorem
origin: cited
lean: Erdos340.erdos_340, Erdos340.erdos_340.variants.isTheta, Erdos340.erdos_340.variants.third, Erdos340.erdos_340.variants.sub_hasPosDensity, Erdos340.erdos_340.variants._22_mem_sub, Erdos340.erdos_340.variants._33_mem_sub, Erdos340.erdos_340.variants.cofinite_sub, Erdos340.erdos_340.variants.co_density_zero_sub
statement: formalized
---

# Erdős Problem 340

> *Reference:* [erdosproblems.com/340](https://www.erdosproblems.com/340)

*Quoted from [FormalConjectures/ErdosProblems/340.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/340](https://www.erdosproblems.com/340).

The file states 8 research or textbook statements: 6 open, 1 solved and 1 textbook result. It also has 9 test statements, counted here but not shown.

## `Erdos340.erdos_340`

Open: stated without proof.

> Let $A = \{1, 2, 4, 8, 13, 21, 31, 45, 66, 81, 97, \ldots\}$ be the greedy Sidon sequence:
> we begin with $1$ and iteratively include the next smallest integer that preserves the
> Sidon property (i.e. there are no non-trivial solutions to $a + b = c + d$). What is the
> order of growth of $A$? Is it true that $|A \cap \{1, \ldots, N\}| \gg N^{1/2 - \varepsilon}$
> for all $\varepsilon > 0$ and large $N$?

```lean
theorem erdos_340 (ε : ℝ) (hε : ε > 0) :
    (fun n : ℕ ↦ √n / n ^ ε) =O[atTop]
      fun n : ℕ ↦ ((Set.range greedySidon ∩ Set.Icc 1 n).ncard : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L80).

## `Erdos340.erdos_340.variants.isTheta`

Open: stated without proof.

> Let $A = \{1, 2, 4, 8, 13, 21, 31, 45, 66, 81, 97, \ldots\}$ be the greedy Sidon sequence:
> we begin with $1$ and iteratively include the next smallest integer that preserves the
> Sidon property (i.e. there are no non-trivial solutions to $a + b = c + d$). What is the
> order of growth of $A$? Is it true that $|A \cap \{1, \ldots, N\}| \gg N^{1/2 - \varepsilon}$
> for all $\varepsilon > 0$ and large $N$?

```lean
theorem erdos_340.variants.isTheta (ε : ℝ) (hε : ε > 0) :
    (fun n : ℕ ↦ ((Set.range greedySidon ∩ Set.Icc 1 n).ncard : ℝ)) =Θ[atTop]
      erdos_340.variants.isTheta.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L95).

## `Erdos340.erdos_340.variants.third`

Textbook result, stated without proof.

> It is trivial that this sequence grows at least like $\gg N^{1/3}$.

```lean
theorem erdos_340.variants.third (ε : ℝ) (hε : ε > 0) :
    (fun n : ℕ ↦ (n : ℝ) ^ ((1 : ℝ) / 3)) =O[atTop]
      fun n : ℕ ↦ ((Set.range greedySidon ∩ Set.Icc 1 n).ncard : ℝ)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L104).

## `Erdos340.erdos_340.variants.sub_hasPosDensity`

Open: stated without proof.

> Erdős and Graham [ErGr80] also asked about the difference set $A - A$ and whether this has
> positive density.
>
> [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
> theory. Monographies de L'Enseignement Mathematique (1980).

```lean
theorem erdos_340.variants.sub_hasPosDensity :
    Set.HasPosDensity (Set.range greedySidon - Set.range greedySidon)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L117).

## `Erdos340.erdos_340.variants._22_mem_sub`

Proved here.

> Erdős and Graham [ErGr80] also asked about the difference set $A - A$ and whether this
> contains $22$, which it does.
>
> [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
> theory. Monographies de L'Enseignement Mathematique (1980).

```lean
theorem erdos_340.variants._22_mem_sub :
    22 ∈ Set.range greedySidon - Set.range greedySidon
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L129).

## `Erdos340.erdos_340.variants._33_mem_sub`

Open: stated without proof.

> The smallest integer which is unknown to be in $A - A$ is $33$.

```lean
theorem erdos_340.variants._33_mem_sub :
    33 ∈ Set.range greedySidon - Set.range greedySidon
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L139).

## `Erdos340.erdos_340.variants.cofinite_sub`

Open: stated without proof.

> It may be true that all or almost all integers are in $A - A$.

```lean
theorem erdos_340.variants.cofinite_sub :
    ∀ᶠ n in cofinite, n ∈ Set.range greedySidon - Set.range greedySidon
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L151).

## `Erdos340.erdos_340.variants.co_density_zero_sub`

Open: stated without proof.

> It may be true that all or almost all integers are in $A - A$.

```lean
theorem erdos_340.variants.co_density_zero_sub :
    ∃ S : Set ℕ, S.HasDensity 0 ∧ ∀ n ∈ Sᶜ, n ∈ Set.range greedySidon - Set.range greedySidon
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/340.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean#L159).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/340.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/340.lean)
- [erdosproblems.com/340](https://www.erdosproblems.com/340)
