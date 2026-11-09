---
declaration: theorem
origin: cited
lean: RamseyNumbers.ramsey_number_five_five, RamseyNumbers.ramsey_number_five_five_lower_bound, RamseyNumbers.ramsey_number_five_five_upper_bound, RamseyNumbers.ramsey_number_three_three, RamseyNumbers.ramsey_number_three_four, RamseyNumbers.ramsey_number_three_five, RamseyNumbers.ramsey_number_three_six, RamseyNumbers.ramsey_number_three_seven, RamseyNumbers.ramsey_number_three_eight, RamseyNumbers.ramsey_number_three_nine, RamseyNumbers.ramsey_number_four_four, RamseyNumbers.ramsey_number_four_five, RamseyNumbers.ramsey_number_six_six, RamseyNumbers.ramsey_number_six_six_lower_bound, RamseyNumbers.ramsey_number_six_six_upper_bound
statement: formalized
---

# Ramsey numbers

> The (graph) Ramsey number $R(k,\ell)$ is the least natural number $n$ such that every simple graph
> on $n$ vertices contains either a clique of size $k$ or an independent set of size $\ell$
> (equivalently, the complement graph contains a clique of size $\ell$).
>
> We formalize the classical open problem of determining $R(5,5)$, together with the currently best
> known bounds $43 \le R(5,5) \le 46$.
>
> Note: the diagonal Ramsey number $R(n,n)$ can also be formulated in terms of 2-colorings of
> $2$-subsets, as `Combinatorics.hypergraphRamsey 2 n` (see `FormalConjecturesForMathlib/Combinatorics/Ramsey.lean`).
>
> *References:*
> - [Wikipedia: Ramsey number](https://en.wikipedia.org/wiki/Ramsey_number)
> - [Rad] S. P. Radziszowski, *Small Ramsey Numbers*, Electronic Journal of Combinatorics, Dynamic
>   Survey DS1. (Updated periodically.) https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1
> - [Exoo89] G. Exoo, *A lower bound for* $R(5,5)$, Journal of Graph Theory 13 (1989), 97–98.
>   DOI: 10.1002/jgt.3190130113
> - [AM24] V. Angeltveit and B. McKay, *$R(5,5) \le 46$*, arXiv:2409.15709 (2024).
> - [OEIS A212954](https://oeis.org/A212954)
> - [MathWorld: Ramsey Number](https://mathworld.wolfram.com/RamseyNumber.html)

*Quoted from [FormalConjectures/Wikipedia/RamseyNumbers.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 15 research or textbook statements: 2 open and 13 solved. It also has 3 API statements, counted here but not shown.

## `RamseyNumbers.ramsey_number_five_five`

Open: stated without proof.

> The open problem: determine the Ramsey number $R(5,5)$.
>
> It is known that $43 \le R(5,5) \le 46$.

```lean
theorem ramsey_number_five_five :
    R(5, 5) = ramsey_number_five_five.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L98).

## `RamseyNumbers.ramsey_number_five_five_lower_bound`

Solved: stated here without proof.

> Lower bound $43 \le R(5,5)$, equivalently: there exists a graph on $42$ vertices with no
> $5$-clique and no independent set of size $5$.

```lean
theorem ramsey_number_five_five_lower_bound :
    ∃ G : SimpleGraph (Fin 42), G.CliqueFree 5 ∧ (Gᶜ).CliqueFree 5
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L107).

## `RamseyNumbers.ramsey_number_five_five_upper_bound`

Solved: stated here without proof.

> Upper bound $R(5,5) \le 46$, i.e. every graph on $46$ vertices contains a $5$-clique or an
> independent set of size $5$.

```lean
theorem ramsey_number_five_five_upper_bound :
    IsGraphRamsey 46 5 5
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L116).

## `RamseyNumbers.ramsey_number_three_three`

Solved: stated here without proof.

> $R(3,3) = 6$.

```lean
theorem ramsey_number_three_three : R(3, 3) = 6
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L129).

## `RamseyNumbers.ramsey_number_three_four`

Solved: stated here without proof.

> $R(3,4) = 9$.

```lean
theorem ramsey_number_three_four : R(3, 4) = 9
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L134).

## `RamseyNumbers.ramsey_number_three_five`

Solved: stated here without proof.

> $R(3,5) = 14$.

```lean
theorem ramsey_number_three_five : R(3, 5) = 14
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L139).

## `RamseyNumbers.ramsey_number_three_six`

Solved: stated here without proof.

> $R(3,6) = 18$.

```lean
theorem ramsey_number_three_six : R(3, 6) = 18
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L144).

## `RamseyNumbers.ramsey_number_three_seven`

Solved: stated here without proof.

> $R(3,7) = 23$.

```lean
theorem ramsey_number_three_seven : R(3, 7) = 23
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L149).

## `RamseyNumbers.ramsey_number_three_eight`

Solved: stated here without proof.

> $R(3,8) = 28$.

```lean
theorem ramsey_number_three_eight : R(3, 8) = 28
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 154](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L154).

## `RamseyNumbers.ramsey_number_three_nine`

Solved: stated here without proof.

> $R(3,9) = 36$ (Grinstead–Roberts).

```lean
theorem ramsey_number_three_nine : R(3, 9) = 36
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L159).

## `RamseyNumbers.ramsey_number_four_four`

Solved: stated here without proof.

> The diagonal Ramsey number $R(4,4) = 18$.

```lean
theorem ramsey_number_four_four : R(4, 4) = 18
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L164).

## `RamseyNumbers.ramsey_number_four_five`

Solved: stated here without proof.

> $R(4,5) = 25$ (McKay–Radziszowski).

```lean
theorem ramsey_number_four_five : R(4, 5) = 25
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 169](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L169).

## `RamseyNumbers.ramsey_number_six_six`

Open: stated without proof.

> The diagonal Ramsey number $R(6,6)$ is unknown. The best known bounds recorded in [Rad] are
> $102 \le R(6,6) \le 165$.

```lean
theorem ramsey_number_six_six : R(6, 6) = ramsey_number_six_six.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 179](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L179).

## `RamseyNumbers.ramsey_number_six_six_lower_bound`

Solved: stated here without proof.

> Lower bound $102 \le R(6,6)$, equivalently: there exists a graph on $101$ vertices with no
> $6$-clique and no independent set of size $6$.

```lean
theorem ramsey_number_six_six_lower_bound :
    ∃ G : SimpleGraph (Fin 101), G.CliqueFree 6 ∧ (Gᶜ).CliqueFree 6
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 187](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L187).

## `RamseyNumbers.ramsey_number_six_six_upper_bound`

Solved: stated here without proof.

> Upper bound $R(6,6) \le 165$, i.e. every graph on $165$ vertices contains a $6$-clique or an
> independent set of size $6$.

```lean
theorem ramsey_number_six_six_upper_bound :
    IsGraphRamsey 165 6 6
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/RamseyNumbers.lean, line 196](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean#L196).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RamseyNumbers.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RamseyNumbers.lean)
- [Wikipedia: Ramsey number](https://en.wikipedia.org/wiki/Ramsey_number)
