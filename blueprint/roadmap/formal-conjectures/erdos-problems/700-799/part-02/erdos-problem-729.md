---
declaration: theorem
origin: cited
lean: Erdos729.erdos_729
statement: formalized
---

# Erdős Problem 729

> *References:*
> - [erdosproblems.com/729](https://www.erdosproblems.com/729)
> - [EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., *On the prime factors of $\binom{2n}{n}$*. Math. Comp. (1975), 83-92.
> - [Er68c] Erdős, P., *Aufgabe 557*. Elemente Math. (1968), 111-113.

*Quoted from [FormalConjectures/ErdosProblems/729.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/729.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/729](https://www.erdosproblems.com/729).

The file states 1 research or textbook statement: 1 solved.

## `Erdos729.erdos_729`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos729.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos729.lean).

> Let $C>0$ be a constant. Are there infinitely many integers $a,b,n$ with $a+b> n+C\log n$ such
> that the denominator of
>
> $$\frac{n!}{a!b!}$$
>
> contains only primes $\ll_C 1$?
>
> Erdős [Er68c] proved that if $a!b!\mid n!$ then $a+b\leq n+O(\log n)$. This has been proved in the affirmative by Barreto and Leeham, using ChatGPT and Aristotle, with a modification of the argument used for [728].

```lean
theorem erdos_729 :
    ∀ (C : ℝ) (hC : C > 0),
      ∃ K ≥ 3, Set.Infinite { T : ℕ × ℕ × ℕ |
        let (a, b, n) := T
        a > 0 ∧ b > 0 ∧ n > 0 ∧
        (a : ℝ) + b > n + C * Real.log n ∧
        ∀ p, p.Prime → p > K →
          padicValNat p ((n.factorial / (a.factorial * b.factorial) : ℚ).den) = 0 }
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/729.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/729.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/729.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/729.lean)
- [erdosproblems.com/729](https://www.erdosproblems.com/729)
