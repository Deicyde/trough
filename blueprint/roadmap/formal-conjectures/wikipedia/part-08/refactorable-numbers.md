---
declaration: theorem
origin: cited
lean: RefactorableNumber.refactorable_hasDensity_zero, RefactorableNumber.no_three_consecutive_refactorable, RefactorableNumber.infinitely_many_consecutive_refactorable_pairs, RefactorableNumber.zelinsky_refactorable_progression_conjecture
statement: formalized
---

# Refactorable Numbers

> An integer $n \ge 1$ is called *refactorable* (or a *$\tau$-number*, OEIS A033950) when its divisor
> count $d(n) = |\operatorname{divisors}(n)|$ divides $n$. Kennedy and Cooper (1990) introduced
> $\tau$-numbers and proved their natural density vanishes; Simon Colton (1999) independently studied
> them as refactorable numbers (see `FormalConjectures.OEIS.«111291»` for Colton's counting bound).
> Joshua Zelinsky (2002) proved that three consecutive integers cannot all be refactorable. Both
> Colton's conjecture on infinitely many refactorable pairs $(n, n + 1)$ and Zelinsky's conjecture on
> refactorable integers in arithmetic progressions remain open.
>
> *References:*
> - [Wikipedia: Refactorable number](https://en.wikipedia.org/wiki/Refactorable_number)
> - [OEIS A033950](https://oeis.org/A033950)
> - R. E. Kennedy and C. N. Cooper (1990), *Int. J. Math. Math. Sci.* **13**(2), 383–386.
> - S. Colton (1999), *J. Integer Seq.* **2**, Art. 99.1.2.
> - J. Zelinsky (2002), *J. Integer Seq.* **5**, Art. 02.2.8.

*Quoted from [FormalConjectures/Wikipedia/RefactorableNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RefactorableNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 2 test statements, counted here but not shown.

## `RefactorableNumber.refactorable_hasDensity_zero`

Solved: stated here without proof.

> **Kennedy–Cooper Theorem (1990):** Refactorable integers have natural density $0$.

```lean
theorem refactorable_hasDensity_zero :
    {n : ℕ | n.IsRefactorable}.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RefactorableNumber.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RefactorableNumber.lean#L55).

## `RefactorableNumber.no_three_consecutive_refactorable`

Solved: stated here without proof.

> **Zelinsky's Theorem (2002):** Three consecutive integers cannot all be refactorable.

```lean
theorem no_three_consecutive_refactorable (n : ℕ) :
    ¬ (n.IsRefactorable ∧ (n + 1).IsRefactorable ∧ (n + 2).IsRefactorable)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RefactorableNumber.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RefactorableNumber.lean#L61).

## `RefactorableNumber.infinitely_many_consecutive_refactorable_pairs`

Open: stated without proof.

> **Colton's Conjecture (1999, Conjecture 2):** Infinitely many positive integers $n$ satisfy
> both $n$ and $n + 1$ refactorable.

```lean
theorem infinitely_many_consecutive_refactorable_pairs :
    {n : ℕ | n.IsRefactorable ∧ (n + 1).IsRefactorable}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RefactorableNumber.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RefactorableNumber.lean#L68).

## `RefactorableNumber.zelinsky_refactorable_progression_conjecture`

Open: stated without proof.

> **Zelinsky's Conjecture (2002, Conjecture 32):** Every arithmetic progression of positive
> integers containing a refactorable number contains infinitely many; equivalently, for every modulus
> $m \ge 1$ and refactorable $n_0$, some refactorable $n > n_0$ satisfies $n \equiv n_0 \pmod m$.

```lean
theorem zelinsky_refactorable_progression_conjecture :
    ∀ m n₀ : ℕ, 1 ≤ m → n₀.IsRefactorable →
      ∃ n : ℕ, n₀ < n ∧ n.IsRefactorable ∧ n ≡ n₀ [MOD m]
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RefactorableNumber.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RefactorableNumber.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RefactorableNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RefactorableNumber.lean)
- [Wikipedia: Refactorable number](https://en.wikipedia.org/wiki/Refactorable_number)
