---
declaration: theorem
origin: cited
lean: DeGiorgi.DeGiorgi_le_eight, DeGiorgi.DeGiorgi_ge_nine, DeGiorgi.DeGiorgi_one, DeGiorgi.DeGiorgi_two, DeGiorgi.DeGiorgi_three, DeGiorgi.DeGiorgi_four, DeGiorgi.DeGiorgi_five, DeGiorgi.DeGiorgi_six, DeGiorgi.DeGiorgi_seven, DeGiorgi.DeGiorgi_eight
statement: formalized
---

# De Giorgi's conjecture

> This file states a conjecture of De Giorgi about entire solutions to $Δ u + u - u^3 = 0$.
> The conjecture is a rigidity theorem: in spatial dimension $n ≤ 8$, the level sets of bounded solutions
> which satisfy $∂₁u > 0$ everywhere are hyperplanes. It has been shown that the condition $n ≤ 8$ is sharp.
>
> The main theorems are:
> - `DeGiorgi_le_eight`: the conjecture holds in dimension $n ≤ 8$.
> - `DeGiorgi_ge_nine`: the conclusion of the conjecture does not hold if $n ≥ 9$.
>
> The cases $1 ≤ n ≤ 8$ are also listed individually to enable partial solutions.
> The cases $1 ≤ n ≤ 3$ are solved, while $4 ≤ n ≤ 8$ remains open.
>
> ## Existing results
> - The case $n = 1$ trivially holds ($u$ is injective since $∂_1 u > 0$).
> - The case $n = 2$ was proven by Ghoussoub and Gui.
> - The case $n = 3$ was proven by Ambrosio and Cabré.
> - The case $4 ≤ n ≤ 8$ was proven under an extra assumption by Savin.
> - The counterexample for $n ≥ 9$ was proven by Del Pino, Kowalczyk, and Wei.
>
> ## References
> * [Ghoussoub, Gui](https://doi.org/10.1007/s002080050196),
>   Mathematische Annalen 311 (1998) proves the conjecture for $n = 2$.
> * [Ambrosio, Cabré](https://doi.org/10.1090/S0894-0347-00-00345-3),
>   Journal of the American Mathematical Society 13 (2000) proves the conjecture for $n = 3$.
> * [Savin](https://doi.org/10.4007/annals.2009.169.41),
>   Annals of Mathematics 169 (2009) proves the case $4 ≤ n ≤ 8$ under an additional assumption.
> * [Del Pino, Kowalczyk, Wei](http://dx.doi.org/10.4007/annals.2011.174.3.3),
>   Annals of Mathematics 174 (2011) shows that the condition $n ≤ 8$ is sharp.

*Quoted from [FormalConjectures/Paper/DeGiorgi.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 10 research or textbook statements: 6 open and 4 solved.

## `DeGiorgi.DeGiorgi_le_eight`

Open: stated without proof.

> De Giorgi's conjecture holds in dimension $n ≤ 8$.

```lean
theorem DeGiorgi_le_eight (hn : n ≤ 8) : (DeGiorgi_conclusion n)
```

Category `research open`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L94).

## `DeGiorgi.DeGiorgi_ge_nine`

Solved: stated here without proof.

> In dimension $n ≥ 9$, the conclusion of De Giorgi's conjecture does not hold.

```lean
theorem DeGiorgi_ge_nine (hn : n ≥ 9) : ¬(DeGiorgi_conclusion n)
```

Category `research solved`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L101).

## `DeGiorgi.DeGiorgi_one`

Proved here.

> De Giorgi's conjecture trivially holds in dimension $n = 1$.

```lean
theorem DeGiorgi_one : (DeGiorgi_conclusion 1)
```

Category `research solved`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L108).

## `DeGiorgi.DeGiorgi_two`

Solved: stated here without proof.

> De Giorgi's conjecture holds in dimension $n = 2$.

```lean
theorem DeGiorgi_two : (DeGiorgi_conclusion 2)
```

Category `research solved`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L128).

## `DeGiorgi.DeGiorgi_three`

Solved: stated here without proof.

> De Giorgi's conjecture holds in dimension $n = 3$.

```lean
theorem DeGiorgi_three : (DeGiorgi_conclusion 3)
```

Category `research solved`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L135).

## `DeGiorgi.DeGiorgi_four`

Open: stated without proof.

> De Giorgi's conjecture holds in dimension $n = 4$.

```lean
theorem DeGiorgi_four : (DeGiorgi_conclusion 4)
```

Category `research open`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L142).

## `DeGiorgi.DeGiorgi_five`

Open: stated without proof.

> De Giorgi's conjecture holds in dimension $n = 5$.

```lean
theorem DeGiorgi_five : (DeGiorgi_conclusion 5)
```

Category `research open`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L149).

## `DeGiorgi.DeGiorgi_six`

Open: stated without proof.

> De Giorgi's conjecture holds in dimension $n = 6$.

```lean
theorem DeGiorgi_six : (DeGiorgi_conclusion 6)
```

Category `research open`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L156).

## `DeGiorgi.DeGiorgi_seven`

Open: stated without proof.

> De Giorgi's conjecture holds in dimension $n = 7$.

```lean
theorem DeGiorgi_seven : (DeGiorgi_conclusion 7)
```

Category `research open`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 163](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L163).

## `DeGiorgi.DeGiorgi_eight`

Open: stated without proof.

> De Giorgi's conjecture holds in dimension $n = 8$.

```lean
theorem DeGiorgi_eight : (DeGiorgi_conclusion 8)
```

Category `research open`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Paper/DeGiorgi.lean, line 170](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean#L170).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/DeGiorgi.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/DeGiorgi.lean)
