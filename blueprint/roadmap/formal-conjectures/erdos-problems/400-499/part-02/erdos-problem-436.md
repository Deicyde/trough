---
declaration: theorem
origin: cited
lean: Erdos436.erdos_436.parts.i, Erdos436.erdos_436.parts.ii, Erdos436.erdos_436.variants.two_two, Erdos436.erdos_436.variants.three_two, Erdos436.erdos_436.variants.four_two, Erdos436.erdos_436.variants.five_two, Erdos436.erdos_436.variants.six_two, Erdos436.erdos_436.variants.seven_two, Erdos436.erdos_436.variants.three_three, Erdos436.erdos_436.variants.even_three, Erdos436.erdos_436.variants.ge_four
statement: formalized
---

# Erdős Problem 436

> *References:*
> - [erdosproblems.com/436](https://www.erdosproblems.com/436)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [LeLe62] Lehmer, D. H. and Lehmer, Emma, *On runs of residues*. Proc. Amer. Math. Soc. (1962),
>   102-106.
> - [LLMS62] Lehmer, D. H. and Lehmer, E. and Mills, W. H. and Selfridge, J. L., *Machine proof of a
>   theorem on cubic residues*. Math. Comp. (1962), 407-415.
> - [BiMi63] Bierstedt, R. G. and Mills, W. H., *On the bound for a pair of consecutive quartic
>   residues of a prime*. Proc. Amer. Math. Soc. (1963), 628-632.
> - [LLM63] Lehmer, D. H. and Lehmer, Emma and Mills, W. H., *Pairs of consecutive power residues*.
>   Canadian J. Math. (1963), 172-177.
> - [BLL64] Brillhart, John and Lehmer, D. H. and Lehmer, Emma, *Bounds for pairs of consecutive
>   seventh and higher power residues*. Math. Comp. (1964), 397-407.
> - [Gr64g] Graham, R. L., *On quadruples of consecutive $k$th power residues*. Proc. Amer. Math.
>   Soc. (1964), 196-197.
> - [Du65] Dunton, M., *Bounds for pairs of cubic residues*. Proc. Amer. Math. Soc. (1965),
>   330-332.
> - [Hi91] Hildebrand, Adolf, *On consecutive $k$th power residues. II*. Michigan Math. J. (1991),
>   241-253.

*Quoted from [FormalConjectures/ErdosProblems/436.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/436](https://www.erdosproblems.com/436).

The file states 11 research or textbook statements: 1 open and 10 solved. It also has 1 test statement, counted here but not shown.

## `Erdos436.erdos_436.parts.i`

Solved: stated here without proof.

> If $p$ is a prime and $k, m \geq 2$, let $r(k, m, p)$ be the minimal $r$ such that
> $r, r + 1, \ldots, r + m - 1$ are all $k$th power residues modulo $p$, and let
> $\Lambda(k, m) = \limsup_{p \to \infty} r(k, m, p)$. Is $\Lambda(k, 2)$ finite for all $k$?
>
> A question of Lehmer and Lehmer [LeLe62]. Hildebrand [Hi91] proved that $\Lambda(k, 2)$ is finite
> for all $k \geq 2$.

```lean
theorem erdos_436.parts.i : ∀ k ≥ 2, Λ k 2 < ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L77).

## `Erdos436.erdos_436.parts.ii`

Open: stated without proof.

> Is $\Lambda(k, 3)$ finite for all odd $k$?
>
> Lehmer, Lehmer, Mills and Selfridge [LLMS62] proved $\Lambda(3, 3) = 23532$. The question is open
> for odd $k \geq 5$.

```lean
theorem erdos_436.parts.ii : ∀ k ≥ 3, Odd k → Λ k 3 < ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L87).

## `Erdos436.erdos_436.variants.two_two`

Solved: stated here without proof.

> Lehmer and Lehmer [LeLe62] proved $\Lambda(2, 2) = 9$.

```lean
theorem erdos_436.variants.two_two : Λ 2 2 = 9
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L92).

## `Erdos436.erdos_436.variants.three_two`

Solved: stated here without proof.

> Dunton [Du65] proved $\Lambda(3, 2) = 77$.

```lean
theorem erdos_436.variants.three_two : Λ 3 2 = 77
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L97).

## `Erdos436.erdos_436.variants.four_two`

Solved: stated here without proof.

> Bierstedt and Mills [BiMi63] proved $\Lambda(4, 2) = 1224$.

```lean
theorem erdos_436.variants.four_two : Λ 4 2 = 1224
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L102).

## `Erdos436.erdos_436.variants.five_two`

Solved: stated here without proof.

> Lehmer, Lehmer and Mills [LLM63] proved $\Lambda(5, 2) = 7888$.

```lean
theorem erdos_436.variants.five_two : Λ 5 2 = 7888
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L107).

## `Erdos436.erdos_436.variants.six_two`

Solved: stated here without proof.

> Lehmer, Lehmer and Mills [LLM63] proved $\Lambda(6, 2) = 202124$.

```lean
theorem erdos_436.variants.six_two : Λ 6 2 = 202124
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L112).

## `Erdos436.erdos_436.variants.seven_two`

Solved: stated here without proof.

> Brillhart, Lehmer and Lehmer [BLL64] proved $\Lambda(7, 2) = 1649375$.

```lean
theorem erdos_436.variants.seven_two : Λ 7 2 = 1649375
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L117).

## `Erdos436.erdos_436.variants.three_three`

Solved: stated here without proof.

> Lehmer, Lehmer, Mills and Selfridge [LLMS62] proved $\Lambda(3, 3) = 23532$.

```lean
theorem erdos_436.variants.three_three : Λ 3 3 = 23532
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L122).

## `Erdos436.erdos_436.variants.even_three`

Solved: stated here without proof.

> Lehmer and Lehmer [LeLe62] proved $\Lambda(k, 3) = \infty$ for all even $k$.

```lean
theorem erdos_436.variants.even_three : ∀ k ≥ 2, Even k → Λ k 3 = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L127).

## `Erdos436.erdos_436.variants.ge_four`

Solved: stated here without proof.

> Graham [Gr64g] proved $\Lambda(k, l) = \infty$ for all $k \geq 2$ and $l \geq 4$.

```lean
theorem erdos_436.variants.ge_four : ∀ k ≥ 2, ∀ l ≥ 4, Λ k l = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/436.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean#L132).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/436.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/436.lean)
- [erdosproblems.com/436](https://www.erdosproblems.com/436)
