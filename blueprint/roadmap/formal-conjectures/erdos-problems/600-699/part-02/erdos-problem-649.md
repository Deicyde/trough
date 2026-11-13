---
declaration: theorem
origin: cited
lean: Erdos649.erdos_649, Erdos649.erdos_649.variants.finite, Erdos649.erdos_649.variants.no_solution_two_seven, Erdos649.erdos_649.variants.tong, Erdos649.erdos_649.variants.tong_question, Erdos649.erdos_649.variants.sampaio, Erdos649.erdos_649.variants.rmm_2020
statement: formalized
---

# Erdős Problem 649

> *References:*
> - [erdosproblems.com/649](https://www.erdosproblems.com/649)
> - [Ma35] Mahler, Kurt, *Über den grössten Primteiler spezieller Polynome zweiten Grades*. Archiv
>   für math. og naturvid (1935).
> - [Ro64b] Rotkiewicz, André, *Sur les nombres naturels $n$ et $k$ tels que les nombres $n$ et $nk$
>   sont à la fois pseudopremiers*. Atti Accad. Naz. Lincei Rend. Cl. Sci. Fis. Mat. Nat. (8)
>   (1964), 816-818.

*Quoted from [FormalConjectures/ErdosProblems/649.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/649](https://www.erdosproblems.com/649).

The file states 7 research or textbook statements: 1 open, 3 solved and 3 textbook results.

## `Erdos649.erdos_649`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L488](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L488).

> Let $P(m)$ denote the greatest prime factor of $m$. Is it true that, for any two primes $p,q$,
> there exists some integer $n$ such that $P(n)=p$ and $P(n+1)=q$?
>
> In fact, the answer to this question as written is easily seen to be no, since there are no
> solutions to $2^k\equiv -1\pmod{7}$, and hence this fails with $p=2$ and $q=7$. It is possible
> that Erdős meant to exclude such obstructions, by amending this to 'odd primes' or 'all
> sufficiently large primes' or such.
>
> The statement below assumes $p \neq q$: for $p = q$ no such $n$ exists, because $p$ would divide
> both $n$ and $n+1$.

```lean
theorem erdos_649 :
    ¬ ∀ p q : ℕ, p.Prime → q.Prime → p ≠ q →
      ∃ n : ℕ, n.maxPrimeFac = p ∧ (n + 1).maxPrimeFac = q
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/649.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean#L50).

## `Erdos649.erdos_649.variants.finite`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L97](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L97).

> The number of solutions is finite for any fixed $p,q$ since the largest prime factor of $n(n+1)$
> tends to $\infty$ (Mahler [Ma35] showed that this is $\gg \log\log n$, see
> [368](https://www.erdosproblems.com/368)).

```lean
theorem erdos_649.variants.finite (p q : ℕ) :
    {n : ℕ | n.maxPrimeFac = p ∧ (n + 1).maxPrimeFac = q}.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/649.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean#L62).

## `Erdos649.erdos_649.variants.no_solution_two_seven`

Textbook result, proved here.

> In fact, the answer to this question as written is easily seen to be no, since there are no
> solutions to $2^k\equiv -1\pmod{7}$, and hence this fails with $p=2$ and $q=7$.

```lean
theorem erdos_649.variants.no_solution_two_seven :
    ¬ ∃ n : ℕ, n.maxPrimeFac = 2 ∧ (n + 1).maxPrimeFac = 7
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/649.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean#L71).

## `Erdos649.erdos_649.variants.tong`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L374](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L374).

> Even with such amendments, this problem is false in a strong sense: Alan Tong has provided the
> following elegant elementary proof that, for any given prime $p$, there are infinitely many
> primes $q$ such that this statement is false: let $m$ be the product of all primes $\leq p$, and
> choose a prime $q$ congruent to $-1$ modulo $4m$. If $p$ is the greatest prime divisor of $n$
> then, using quadratic reciprocity, every prime divisor of $n$ is a quadratic residue modulo $q$,
> and hence $n$ is a quadratic residue modulo $q$. On the other hand, since $q\equiv 3\pmod{4}$ we
> know that $-1$ is not a quadratic residue modulo $q$, and hence $n\not\equiv -1\pmod{q}$, so it
> is impossible for $q\mid n+1$.

```lean
theorem erdos_649.variants.tong (p : ℕ) (hp : p.Prime) :
    {q : ℕ |
      q.Prime ∧ ¬ ∃ n : ℕ, n.maxPrimeFac = p ∧ (n + 1).maxPrimeFac = q}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/649.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean#L104).

## `Erdos649.erdos_649.variants.tong_question`

Open: stated without proof.

> Tong asks whether, for any given odd prime $q$, there are infinitely many primes $p$ such that
> there is no integer $n$ with $P(n)=p$ and $P(n+1)=q$.

```lean
theorem erdos_649.variants.tong_question :
    ∀ q : ℕ, q.Prime → Odd q →
      {p : ℕ |
        p.Prime ∧ ¬ ∃ n : ℕ, n.maxPrimeFac = p ∧ (n + 1).maxPrimeFac = q}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/649.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean#L114).

## `Erdos649.erdos_649.variants.sampaio`

Textbook result, proved here.

> Sampaio independently observed that the answer to Erdős' original problem is no if one of the
> primes can be $2$ - for example this is false with $p=19$ and $q=2$, since if $n+1=2^k$ and
> $19\mid n$ then (since $2$ is a primitive root modulo $19$) we must have $18\mid k$, and hence
> $73\mid 2^{18}-1\mid n$.

```lean
theorem erdos_649.variants.sampaio :
    ¬ ∃ n : ℕ, n.maxPrimeFac = 19 ∧ (n + 1).maxPrimeFac = 2
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/649.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean#L127).

## `Erdos649.erdos_649.variants.rmm_2020`

Textbook result, stated without proof. A Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L1090](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos649.lean#L1090).

> Problem 6 in the 12th Romanian Master of Mathematics Competitions in 2020 was to prove that there
> exist infinitely many odd primes $p$ such that, for every $n$, $P(n)P(n+1)\neq 2p$.

```lean
theorem erdos_649.variants.rmm_2020 :
    {p : ℕ | p.Prime ∧ Odd p ∧
      ∀ n : ℕ, n.maxPrimeFac * (n + 1).maxPrimeFac ≠ 2 * p}.Infinite
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/649.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean#L159).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/649.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/649.lean)
- [erdosproblems.com/649](https://www.erdosproblems.com/649)
