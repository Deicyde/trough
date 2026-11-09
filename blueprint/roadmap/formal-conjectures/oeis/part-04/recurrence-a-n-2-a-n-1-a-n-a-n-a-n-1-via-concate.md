---
declaration: theorem
origin: cited
lean: OeisA70823.conjecture
statement: formalized
---

# Recurrence $a(n+2) = |a(n+1)a(n) - a(n)a(n+1)|$ via concatenation

> The sequence starts with $a(1) = 0, a(2) = 1$. For $n \ge 1$,
>
> $$a(n+2) = |\text{concat}(a(n+1), a(n)) - \text{concat}(a(n), a(n+1))|$$
>
> where concatenation is in decimal representation.
>
> *References:*
> - [A070823](https://oeis.org/A070823)

*Quoted from [FormalConjectures/OEIS/70823.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/70823.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA70823.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a070823-counterexample/blob/51399770e734616c6463be034e41f7469991d752/lean/OeisA70823CounterexampleFC.lean#L72-L81](https://github.com/KitaKen1/oeis-a070823-counterexample/blob/51399770e734616c6463be034e41f7469991d752/lean/OeisA70823CounterexampleFC.lean#L72-L81).

> $a(n) \equiv 0 \pmod 3$ if $n > 2$. Is $a(n)$ always of the form $2^j \cdot 3^k \cdot s$
> where $s$ is a squarefree number?
>
> Answer: False, $a(20)$ is divisible by $13^2$ but not by $13^3$.

```lean
theorem conjecture :
    ¬ ∀ n : ℕ, 2 < n →
      a n ≡ 0 [MOD 3] ∧
        ∃ j k s : ℕ, a n = 2 ^ j * 3 ^ k * s ∧ Squarefree s
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/70823.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/70823.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/70823.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/70823.lean)
- [A070823](https://oeis.org/A070823)
